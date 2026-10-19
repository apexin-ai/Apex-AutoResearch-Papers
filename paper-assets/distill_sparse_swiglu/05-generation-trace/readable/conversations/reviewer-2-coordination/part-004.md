# Reviewer 2 coordination — Part 4 of 5

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 5 →](part-005.md) · [Structured JSON](../../../sessions/96/96af94fcc323c852e454.json)

## Round 40

### Tool call

_source line 1634 · 2026-05-22T23:45:22.733747+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告（新颖性与完整性）\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 实验设计扎实、分析有洞见的实证研究，但核心贡献（KL 训练 sparsity masks）相对于 MaskLLM 的新颖性增量有限，\"dominant design dimension\" 的 claim 仅基于两种信号类型的对比，overclaim 风险较高。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论整体合理，实验设计规范（C1 ablation、per-layer decomposition 等设计精巧），但核心 claim \"output-distribution alignment is the dominant design dimension\" 仅基于 BCE vs KL 二元对比，未测试其他分布级别损失函数（reverse KL、JSD、logit MSE），支撑不足以称\"dominant\" |\n| Excitement | 2.5 / 5 | §3.6 梯度分析（BCE per-neuron independent vs KL coupled through output distribution）是有价值的分析性洞见；但整体方法是将已有技术（KL distillation + Gumbel relaxation）应用到新场景（contextual activation sparsity），incremental flavor 较重；无 wall-clock speedup 削弱实际影响力 |\n| Reproducibility | 4.0 / 5 | 超参数、训练细节、predictor 架构均有详细描述；Appendix A-B 提供了完整的 inference efficiency 和 bottleneck sensitivity 分析；代码未公开但描述足够复现 |\n| Overall Assessment | 3.0 / 5 | Findings 水平——实证工作扎实，但新颖性不足以达到主会议 bar |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分\n- 具体位置：Section 2 (Related Work, paragraph \"Weight Pruning, Distillation, and Routing\") 及 Section 3.4\n- 问题：MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM (\"MaskLLM shares the recipe-level principle of frozen weights + learnable masks + KL training\")，未深入分析为何在 contextual activation sparsity setting 下这一 recipe 会产生质性不同的 behavior。\n- 为什么影响接收：如果 reviewer/AC 认为这是 MaskLLM 在不同 sparsity setting 的直接应用，整篇论文的贡献定位会受到根本性质疑。\n- 建议修改方向：(1) 专门设立 paragraph 深入对比 MaskLLM——不仅说\"区别在哪\"，更要说\"为什么这些区别导致了不同的技术挑战和 findings\"（如 MaskLLM 的 Gumbel-Softmax 在有限候选集上采样 vs. 本文 Gumbel-Sigmoid 在连续空间上的 per-neuron relaxation；MaskLLM 无 cross-layer coupling 因为 N:M masks 是 layer-local 的）；(2) §3.6 梯度分析是本文的独特贡献，应更突出其与 MaskLLM 的区别——MaskLLM 未分析 gradient coupling。\n\n**N2** [critical] \"Dominant design dimension\" claim overclaimed\n- 具体位置：Abstract (\"output-distribution alignment is the critical design dimension for learned sparsity\"), Section 5 Conclusion (\"Output-distribution alignment is the dominant design dimension for PPL\")\n- 问题：该 claim 仅基于两种 signal type 的对比：BCE（per-neuron classification）vs. forward KL（output distribution）。论文未测试：\n  - **Reverse KL**（仅在 Section 3.5 提及\"forward rather than reverse KL\" 并引用一个 validation choice，但未提供 reverse KL 实验结果）\n  - **JSD**（Jensen-Shannon divergence，knowledge distillation 领域常用）\n  - **MSE on logits/hidden states**（intermediate distillation，不同于 per-neuron BCE 也不同于 output KL）\n  - **Cosine similarity on output distributions**\n  在仅比较两种方法的情况下声称\"dominant\"，逻辑上不成立。此外，Table 3 中 BCE+Gumbel (32.22) vs KL (28.13) 的差距虽然显著，但 BCE+Gumbel 仍然远优于 BCE-only，说明 Gumbel relaxation 本身也是重要因素，不能简单归功于 KL vs BCE。\n- 为什么影响接收：Overclaim 是 ARR reviewer 的核心 red flag。如果 claim 被降级为 \"KL outperforms BCE for contextual sparsity prediction\"，论文的 framing 需要全面调整。\n- 建议修改方向：(1) 补充至少一种其他分布级别损失（reverse KL 或 JSD）的实验；(2) 将 claim 软化为 \"output-distribution alignment substantially outperforms per-neuron classification\"，而非 \"dominant design dimension\"。\n\n**N3** [critical] 实验规模单一，削弱 generalizability claim\n- 具体位置：Section 4 全部主实验（Table 2-4, Figure 2）均基于 LLaMA-3.1-8B；跨架构实验（Mistral-7B, Qwen-2.5-14B）仅在 Appendix N-O\n- 问题：论文声称发现了 learned sparsity 的通用设计原则（\"the dominant design dimension\"），但核心实验（Table 2-4, §4.3-4.5）全部基于单一模型（LLaMA-3.1-8B）。跨架构验证（Appendix N: Mistral-7B 仅 Table 16 一个表；Appendix O: Qwen-2.5-14B 仅 Table 13-14）过于简略。特别是：\n  - Qwen-2.5-14B 的 Table 13 仅展示 30% sparsity 下的 PPL 和 downstream accuracy，无 C1 ablation 或 gradient SNR 分析\n  - 无任何 70B+ 模型的实验，而 sparsity 在大模型上的实际价值更高\n  - 无非 LLaMA-family 架构的深入分析（如 Falcon、Gemma 等）\n- 为什么影响接收：从单一 8B 模型推广到 \"the dominant design dimension for learned sparsity\" 的 generalization gap 过大。\n- 建议修改方向：(1) 将至少一个跨架构实验（含 C1 ablation）提升到主文；(2) 在 Limitations 中明确承认实验规模的局限性。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无 wall-clock speedup 结果\n- 具体位置：Abstract (\"wall-clock speedup without sparse kernel support is not addressed here\"), Appendix A\n- 问题：作为一篇 activation sparsity 论文，完全不报告实际推理加速效果是一个明显缺失。Appendix A 仅展示 predictor overhead (6.4%) 和 dense inference 对比下的 latency，但未展示 sparse execution 的实际加速。论文承认 \"unstructured element-wise masks... do not translate to wall-clock speedup without sparse kernel support\"——这实质上承认了方法当前没有实际加速价值。\n- 建议：(1) 至少展示使用已有 sparse kernel (如 Triton block-sparse) 的 wall-clock 对比；或 (2) 在 Limitations 中更显著地讨论此限制而非仅一句话带过。\n\n**W2** [warning] 训练数据过于有限\n- 具体位置：Section 4.1 (\"trained for 1000 steps on WikiText-103\")\n- 问题：Predictor 仅在 WikiText-103 上训练 1000 步（约 200M tokens）。Appendix D (Out-of-Distribution Evaluation) 在 C4 上测试了 OOD 泛化，结果 \"comparable\" 但仅在 PPL 和 3 个下游任务上验证。未测试：\n  - 代码生成任务（HumanEval/MBPP）\n  - 多语言文本\n  - 长文档理解\n  训练数据的 domain 和 volume 对 predictor 泛化能力的影响未充分讨论。\n\n**W3** [warning] 2D Taxonomy 贡献度有限\n- 具体位置：Section 3.7, Table 1\n- 问题：Signal type × coupling scope 的 2D 分类（Table 1）作为组织框架有用，但新颖洞见有限——它本质上是对已有方法的 post-hoc 归类。Table 1 标注 \"Empty cells represent unexplored combinations; their relative merit is an open question\"，但论文未尝试填充这些空白（如 coupled BCE+MSE 或 per-token BCE），也未讨论为什么某些组合不可行或不有趣。如果 taxonomy 是贡献之一，需要更深入的分析。\n\n**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆\n- 具体位置：Section 3.3, Table 3\n- 问题：Table 3 的 C1 ablation 中，BCE achieves PPL 11.79 vs KL 11.79 (几乎相同)，但 BCE+Gumbel = 32.22 vs standard BCE = 需要从正文对比。关键问题是：论文将 KL 的优势归因于\"output-distribution alignment\"，但 KL 方法同时使用了 Gumbel-Sigmoid relaxation（§3.3），而 BCE baseline 使用 hard threshold。这引入了混淆变量——KL 的优势可能部分来自 Gumbel relaxation 本身（连续梯度流）而非 KL vs BCE 的信号差异。Table 4 的 \"Relaxation, Divergence, and SPON\" 行显示 Gumbel-Sigmoid 对 STE 有 PPL 15.77 → 11.79 的巨大改进，说明 relaxation method 本身是关键因素。论文应更清晰地 disentangle 这两个因素。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.5 公式 (7)：geometric penalty schedule 的 deadzone ε = 0.02 未充分 justify 为什么选择这个值\n- Figure 2 右图：y 轴 \"WikiText-2 PPL↓\" 与左图 \"Achieved Model-Level Sparsity (%)\" 的对比信息密度可以提高——建议加入 Pareto frontier 标注\n- Section 4.2 脚注 2：\"TEAL is deterministic; single-run evaluation suffices\" ——但 KL predictor 使用了 Gumbel noise，single-run evaluation 是否足够？论文提到 3-seed evaluation（Table 2 报告 mean±std），但应在正文而非脚注中明确\n- Appendix 编号从 A 到 U（21 个 appendix sections），信息量虽大但部分内容可精简（如 Appendix P \"SPON Orthogonality\" 仅 4 行）\n- 部分符号不一致：正文用 $m_\\ell$ 但部分地方用 $m^{(\\ell)}$\n\n---\n\n## 遗漏的相关工作\n\n**应引用但未引用：**\n1. **SparseInfer** (Li et al., 2024, arXiv:2411.12692): Training-free prediction of activation sparsity for fast LLM inference。直接相关——另一种 training-free 的 sparsity predictor 方法，应在 Related Work 讨论作为对比。\n2. **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025): Group-based sparsity prediction method，在 prediction accuracy 上有创新。\n3. **TurboSparse** (Song et al., 2024, arXiv:2406.05955): dReLU activation for SwiGLU models achieving ~90% sparsity。虽然是 activation engineering 而非 prediction，但与论文 \"Activation Function Engineering\" 小节（Section 2, p.3）直接相关，且同样关注 SwiGLU 模型的 sparsity。需确认是否已引用（从 PDF 难以完全确认 references 列表）。\n\n**建议检查：**\n4. Universal Properties of Activation Sparsity (2025, arXiv:2509.00454): 研究 activation sparsity 的跨模型通用属性，与本文 §4.4 mask pattern analysis 相关。\n\n---\n\n## 主要优势\n\n1. **§3.6 梯度分析是真正的分析性贡献**：清晰展示 BCE gradient $\\partial \\mathcal{L}_{BCE}/\\partial o_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian $\\partial \\mathcal{L}_{KL}/\\partial o_j$ 耦合所有 neuron——这解释了为什么 KL 能发现 composition-aware mask patterns。这是本文最有价值的洞见。\n\n2. **C1 target-swap ablation 设计精巧（§4.3, Table 3）**：用 KL-derived masks 训练 BCE predictor（C1），证明 mask pattern 质量本身可迁移（PPL within 0.79pp of KL），有力支撑了\"KL 的优势在于 pattern discovery 而非仅 loss function\"的论点。\n\n3. **实验覆盖面宽（虽深度不足）**：主文和 Appendix 共覆盖了 allocation analysis（§4.5）、per-layer retention（Appendix E）、training stability（Appendix F）、mask pattern visualization（Appendix M）、cross-architecture（Appendix N-O）等多个维度，信息密度高。\n\n4. **定位诚实**：论文自称 \"primarily an empirical study\"（Section 2, p.2）且始终保持这一定位，未虚增方法论贡献。Limitations 章节（虽简短）覆盖了三个核心局限。\n\n5. **Predictor 设计高效**：75.9M 参数（< 1% base model），2.37M per layer，训练 1000 步（~45 min on single GPU）——实际部署门槛低。\n\n---\n\n## 总结判断\n\n本文是一篇执行良好的实证研究，§3.6 梯度分析和 C1 ablation 是有价值的贡献。但三个核心问题阻碍了主会议接收：(1) 与 MaskLLM 的新颖性区分不充分——核心 recipe 相同，区别主要在 sparsity setting；(2) \"dominant design dimension\" claim 仅基于 BCE vs KL 二元对比，overclaimed；(3) 实验几乎完全依赖 LLaMA-3.1-8B，generalizability 证据不足。建议降级为 \"KL outperforms BCE for contextual sparsity prediction in SwiGLU models\"，补充 reverse KL/JSD 实验，并在主文中加入跨架构 C1 ablation。以当前形式适合 Findings 而非主会议。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告（新颖性与完整性）\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 实验设计扎实、分析有洞见的实证研究，但核心贡献（KL 训练 sparsity masks）相对于 MaskLLM 的新颖性增量有限，\"dominant design dimension\" 的 claim 仅基于两种信号类型的对比，overclaim 风险较高。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5 / 5 | 方法论整体合理，实验设计规范（C1 ablation、per-layer decomposition 等设计精巧），但核心 claim \"output-distribution alignment is the dominant design dimension\" 仅基于 BCE vs KL 二元对比，未测试其他分布级别损失函数（reverse KL、JSD、logit MSE），支撑不足以称\"dominant\" |\n| Excitement | 2.5 / 5 | §3.6 梯度分析（BCE per-neuron independent vs KL coupled through output distribution）是有价值的分析性洞见；但整体方法是将已有技术（KL distillation + Gumbel relaxation）应用到新场景（contextual activation sparsity），incremental flavor 较重；无 wall-clock speedup 削弱实际影响力 |\n| Reproducibility | 4.0 / 5 | 超参数、训练细节、predictor 架构均有详细描述；Appendix A-B 提供了完整的 inference efficiency 和 bottleneck sensitivity 分析；代码未公开但描述足够复现 |\n| Overall Assessment | 3.0 / 5 | Findings 水平——实证工作扎实，但新颖性不足以达到主会议 bar |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心贡献与 MaskLLM 的新颖性区分不充分\n- 具体位置：Section 2 (Related Work, paragraph \"Weight Pruning, Distillation, and Routing\") 及 Section 3.4\n- 问题：MaskLLM (Fang et al., 2024, NeurIPS 2024 Spotlight) 已提出 KL divergence + Gumbel relaxation 训练可学习 sparsity masks 的范式。本文声称的区别是：(a) contextual vs. static masks, (b) activation sparsity vs. N:M weight sparsity, (c) cross-layer coupling analysis。但 (a) 和 (b) 属于 sparsity setting 的差异而非训练方法论的创新——核心 recipe（KL on output distributions + differentiable mask sampling）完全一致。论文 Section 2 仅用一句话提到 MaskLLM (\"MaskLLM shares the recipe-level principle of frozen weights + learnable masks + KL training\")，未深入分析为何在 contextual activation sparsity setting 下这一 recipe 会产生质性不同的 behavior。\n- 为什么影响接收：如果 reviewer/AC 认为这是 MaskLLM 在不同 sparsity setting 的直接应用，整篇论文的贡献定位会受到根本性质疑。\n- 建议修改方向：(1) 专门设立 paragraph 深入对比 MaskLLM——不仅说\"区别在哪\"，更要说\"为什么这些区别导致了不同的技术挑战和 findings\"（如 MaskLLM 的 Gumbel-Softmax 在有限候选集上采样 vs. 本文 Gumbel-Sigmoid 在连续空间上的 per-neuron relaxation；MaskLLM 无 cross-layer coupling 因为 N:M masks 是 layer-local 的）；(2) §3.6 梯度分析是本文的独特贡献，应更突出其与 MaskLLM 的区别——MaskLLM 未分析 gradient coupling。\n\n**N2** [critical] \"Dominant design dimension\" claim overclaimed\n- 具体位置：Abstract (\"output-distribution alignment is the critical design dimension for learned sparsity\"), Section 5 Conclusion (\"Output-distribution alignment is the dominant design dimension for PPL\")\n- 问题：该 claim 仅基于两种 signal type 的对比：BCE（per-neuron classification）vs. forward KL（output distribution）。论文未测试：\n  - **Reverse KL**（仅在 Section 3.5 提及\"forward rather than reverse KL\" 并引用一个 validation choice，但未提供 reverse KL 实验结果）\n  - **JSD**（Jensen-Shannon divergence，knowledge distillation 领域常用）\n  - **MSE on logits/hidden states**（intermediate distillation，不同于 per-neuron BCE 也不同于 output KL）\n  - **Cosine similarity on output distributions**\n  在仅比较两种方法的情况下声称\"dominant\"，逻辑上不成立。此外，Table 3 中 BCE+Gumbel (32.22) vs KL (28.13) 的差距虽然显著，但 BCE+Gumbel 仍然远优于 BCE-only，说明 Gumbel relaxation 本身也是重要因素，不能简单归功于 KL vs BCE。\n- 为什么影响接收：Overclaim 是 ARR reviewer 的核心 red flag。如果 claim 被降级为 \"KL outperforms BCE for contextual sparsity prediction\"，论文的 framing 需要全面调整。\n- 建议修改方向：(1) 补充至少一种其他分布级别损失（reverse KL 或 JSD）的实验；(2) 将 claim 软化为 \"output-distribution alignment substantially outperforms per-neuron classification\"，而非 \"dominant design dimension\"。\n\n**N3** [critical] 实验规模单一，削弱 generalizability claim\n- 具体位置：Section 4 全部主实验（Table 2-4, Figure 2）均基于 LLaMA-3.1-8B；跨架构实验（Mistral-7B, Qwen-2.5-14B）仅在 Appendix N-O\n- 问题：论文声称发现了 learned sparsity 的通用设计原则（\"the dominant design dimension\"），但核心实验（Table 2-4, §4.3-4.5）全部基于单一模型（LLaMA-3.1-8B）。跨架构验证（Appendix N: Mistral-7B 仅 Table 16 一个表；Appendix O: Qwen-2.5-14B 仅 Table 13-14）过于简略。特别是：\n  - Qwen-2.5-14B 的 Table 13 仅展示 30% sparsity 下的 PPL 和 downstream accuracy，无 C1 ablation 或 gradient SNR 分析\n  - 无任何 70B+ 模型的实验，而 sparsity 在大模型上的实际价值更高\n  - 无非 LLaMA-family 架构的深入分析（如 Falcon、Gemma 等）\n- 为什么影响接收：从单一 8B 模型推广到 \"the dominant design dimension for learned sparsity\" 的 generalization gap 过大。\n- 建议修改方向：(1) 将至少一个跨架构实验（含 C1 ablation）提升到主文；(2) 在 Limitations 中明确承认实验规模的局限性。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 无 wall-clock speedup 结果\n- 具体位置：Abstract (\"wall-clock speedup without sparse kernel support is not addressed here\"), Appendix A\n- 问题：作为一篇 activation sparsity 论文，完全不报告实际推理加速效果是一个明显缺失。Appendix A 仅展示 predictor overhead (6.4%) 和 dense inference 对比下的 latency，但未展示 sparse execution 的实际加速。论文承认 \"unstructured element-wise masks... do not translate to wall-clock speedup without sparse kernel support\"——这实质上承认了方法当前没有实际加速价值。\n- 建议：(1) 至少展示使用已有 sparse kernel (如 Triton block-sparse) 的 wall-clock 对比；或 (2) 在 Limitations 中更显著地讨论此限制而非仅一句话带过。\n\n**W2** [warning] 训练数据过于有限\n- 具体位置：Section 4.1 (\"trained for 1000 steps on WikiText-103\")\n- 问题：Predictor 仅在 WikiText-103 上训练 1000 步（约 200M tokens）。Appendix D (Out-of-Distribution Evaluation) 在 C4 上测试了 OOD 泛化，结果 \"comparable\" 但仅在 PPL 和 3 个下游任务上验证。未测试：\n  - 代码生成任务（HumanEval/MBPP）\n  - 多语言文本\n  - 长文档理解\n  训练数据的 domain 和 volume 对 predictor 泛化能力的影响未充分讨论。\n\n**W3** [warning] 2D Taxonomy 贡献度有限\n- 具体位置：Section 3.7, Table 1\n- 问题：Signal type × coupling scope 的 2D 分类（Table 1）作为组织框架有用，但新颖洞见有限——它本质上是对已有方法的 post-hoc 归类。Table 1 标注 \"Empty cells represent unexplored combinations; their relative merit is an open question\"，但论文未尝试填充这些空白（如 coupled BCE+MSE 或 per-token BCE），也未讨论为什么某些组合不可行或不有趣。如果 taxonomy 是贡献之一，需要更深入的分析。\n\n**W4** [warning] Gumbel-Sigmoid relaxation 的贡献被低估/混淆\n- 具体位置：Section 3.3, Table 3\n- 问题：Table 3 的 C1 ablation 中，BCE achieves PPL 11.79 vs KL 11.79 (几乎相同)，但 BCE+Gumbel = 32.22 vs standard BCE = 需要从正文对比。关键问题是：论文将 KL 的优势归因于\"output-distribution alignment\"，但 KL 方法同时使用了 Gumbel-Sigmoid relaxation（§3.3），而 BCE baseline 使用 hard threshold。这引入了混淆变量——KL 的优势可能部分来自 Gumbel relaxation 本身（连续梯度流）而非 KL vs BCE 的信号差异。Table 4 的 \"Relaxation, Divergence, and SPON\" 行显示 Gumbel-Sigmoid 对 STE 有 PPL 15.77 → 11.79 的巨大改进，说明 relaxation method 本身是关键因素。论文应更清晰地 disentangle 这两个因素。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.5 公式 (7)：geometric penalty schedule 的 deadzone ε = 0.02 未充分 justify 为什么选择这个值\n- Figure 2 右图：y 轴 \"WikiText-2 PPL↓\" 与左图 \"Achieved Model-Level Sparsity (%)\" 的对比信息密度可以提高——建议加入 Pareto frontier 标注\n- Section 4.2 脚注 2：\"TEAL is deterministic; single-run evaluation suffices\" ——但 KL predictor 使用了 Gumbel noise，single-run evaluation 是否足够？论文提到 3-seed evaluation（Table 2 报告 mean±std），但应在正文而非脚注中明确\n- Appendix 编号从 A 到 U（21 个 appendix sections），信息量虽大但部分内容可精简（如 Appendix P \"SPON Orthogonality\" 仅 4 行）\n- 部分符号不一致：正文用 $m_\\ell$ 但部分地方用 $m^{(\\ell)}$\n\n---\n\n## 遗漏的相关工作\n\n**应引用但未引用：**\n1. **SparseInfer** (Li et al., 2024, arXiv:2411.12692): Training-free prediction of activation sparsity for fast LLM inference。直接相关——另一种 training-free 的 sparsity predictor 方法，应在 Related Work 讨论作为对比。\n2. **GRASP** (Group-Based Prediction of Activation Sparsity, DAC 2025): Group-based sparsity prediction method，在 prediction accuracy 上有创新。\n3. **TurboSparse** (Song et al., 2024, arXiv:2406.05955): dReLU activation for SwiGLU models achieving ~90% sparsity。虽然是 activation engineering 而非 prediction，但与论文 \"Activation Function Engineering\" 小节（Section 2, p.3）直接相关，且同样关注 SwiGLU 模型的 sparsity。需确认是否已引用（从 PDF 难以完全确认 references 列表）。\n\n**建议检查：**\n4. Universal Properties of Activation Sparsity (2025, arXiv:2509.00454): 研究 activation sparsity 的跨模型通用属性，与本文 §4.4 mask pattern analysis 相关。\n\n---\n\n## 主要优势\n\n1. **§3.6 梯度分析是真正的分析性贡献**：清晰展示 BCE gradient $\\partial \\mathcal{L}_{BCE}/\\partial o_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian $\\partial \\mathcal{L}_{KL}/\\partial o_j$ 耦合所有 neuron——这解释了为什么 KL 能发现 composition-aware mask patterns。这是本文最有价值的洞见。\n\n2. **C1 target-swap ablation 设计精巧（§4.3, Table 3）**：用 KL-derived masks 训练 BCE predictor（C1），证明 mask pattern 质量本身可迁移（PPL within 0.79pp of KL），有力支撑了\"KL 的优势在于 pattern discovery 而非仅 loss function\"的论点。\n\n3. **实验覆盖面宽（虽深度不足）**：主文和 Appendix 共覆盖了 allocation analysis（§4.5）、per-layer retention（Appendix E）、training stability（Appendix F）、mask pattern visualization（Appendix M）、cross-architecture（Appendix N-O）等多个维度，信息密度高。\n\n4. **定位诚实**：论文自称 \"primarily an empirical study\"（Section 2, p.2）且始终保持这一定位，未虚增方法论贡献。Limitations 章节（虽简短）覆盖了三个核心局限。\n\n5. **Predictor 设计高效**：75.9M 参数（< 1% base model），2.37M per layer，训练 1000 步（~45 min on single GPU）——实际部署门槛低。\n\n---\n\n## 总结判断\n\n本文是一篇执行良好的实证研究，§3.6 梯度分析和 C1 ablation 是有价值的贡献。但三个核心问题阻碍了主会议接收：(1) 与 MaskLLM 的新颖性区分不充分——核心 recipe 相同，区别主要在 sparsity setting；(2) \"dominant design dimension\" claim 仅基于 BCE vs KL 二元对比，overclaimed；(3) 实验几乎完全依赖 LLaMA-3.1-8B，generalizability 证据不足。建议降级为 \"KL outperforms BCE for contextual sparsity prediction in SwiGLU models\"，补充 reverse KL/JSD 实验，并在主文中加入跨架构 C1 ablation。以当前形式适合 Findings 而非主会议。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-22T23:45:26.396929+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3663
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-22T23:45:31.024385+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1637 · 2026-05-22T23:45:31.075014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-22T23:45:34.587797+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-22T23:45:34.638488+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1640 · 2026-05-22T23:45:42.307154+00:00_

审稿完成。核心结论：

- **Overall: 3.0/5 (Findings)**
- 3 个 Critical 问题：(1) 与 MaskLLM 的新颖性区分不充分（核心 KL+Gumbel recipe 相同）；(2) "dominant design dimension" claim overclaimed（仅 BCE vs KL 二元对比，未测试 reverse KL/JSD 等）；(3) 实验几乎全依赖 LLaMA-3.1-8B，generalizability 证据不足
- 主要优势：§3.6 梯度分析是真正的分析性贡献，C1 target-swap ablation 设计精巧，定位诚实
- 4 个 Should-Fix：无 wall-clock speedup、训练数据有限、2D taxonomy 贡献度有限、Gumbel relaxation 与 KL 的贡献未充分 disentangle

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 41

## Round 41

14 recorded events


### User

_source line 1641 · 2026-05-22T23:48:00.501848+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿报告（方法严谨性与实验设计）

**Overall**: 3.0 / 5 — Findings

### Must-Fix 问题

**N1 [Critical] Per-layer KL 分解存在根本性 confound，定量结论不可靠**
- K=1 训练时仅 mask 1/32 层，推理时 mask 全部 32 层，32× train-inference mismatch。Abstract/Conclusion 仍将 "signal type accounts for the majority of the PPL gap" 作为核心贡献呈现，未充分传达 upper bound 资格限定。
- K=4 在 50% 下比 K=1 差（44.23 vs 34.85），与 "K 越大越接近 E2E" 的直觉矛盾，论文未提供机制解释。
- K=4 在 30% MMLU 超过 E2E（42.7 vs 40.7），混入 allocation 效应。
- 仅两个数据点（K=1, K=4）无法支撑 "29-97% on downstream tasks" 的精确分解。

**N2 [Critical] 知识密集型任务系统性退步缺乏机制分析**
- KL 在所有测试规模和架构上均系统性地低于 TEAL 的 MMLU/GSM8K：8B -5.2pp MMLU, 14B -20pp GSM8K。
- 论文推测 "distribution-matching objectives systematically sacrifice reasoning-critical pathways" 仅是事后叙事，无实验支撑。
- §4.4 Remove valley (MMLU +3.4pp) 是一个数据点但未回答根本问题：为什么 KL 会学到牺牲知识路径的 allocation pattern？

### Should-Fix 问题

**W1 [Warning] C1 ablation 残余 confound 未完全控制**
- C1 同时改变训练目标和 mask 表示（soft → hard）。BCE+Gumbel (32.22) vs standard BCE (27.97) 使用 magnitude-based targets，不能直接推广到 KL-derived targets。Oracle mask 提取（logits > 0 二值化）可能丢失排序信息。

**W2 [Warning] 无 wall-clock 加速**
- Predictor 增加 6.4% 推理延迟，无稀疏内核支持。

**W3 [Warning] 评估覆盖度存在关键空白**
- 无生成任务评估（MT-Bench, AlpacaEval）；序列长度固定 2048；batched inference 未评估。

**W4 [Warning] 高方差指标的统计可靠性不足**
- ARC-c σ=3.6pp 在 3 seed 下 95% CI 约 ±8.9pp；BoolQ σ=11.5pp；Table 4 多行仅 s42 单 seed。

**W5 [Warning] Geometric penalty schedule 在 30% 目标下偏差较大**
- ε=0.02 deadzone 导致 30% 目标永远无法精确达到（28.5% actual）；main text Table 2 标注 "30%" 可能误导。

### Questions
Q1. K=4 50% 为何比 K=1 差？是否有 gradient interference 解释？
Q2. 知识退步是否与 WikiText-103 训练数据有关？
Q3. C1 oracle 提取二值化是否尝试过保留连续分数？
Q4. STE 在 30% 仅 20.8% sparsity，是否调整过 lr/gradient scaling？
Q5. MSE 30% 3-seed mean 是否包含所有 3 个 seed？

### Missing References
- Meng et al., 2022 "Locating and Editing Factual Associations in GPT"
- Li et al., 2023 "Inference with Reference"
- MaskLLM 无实验对比

---

请对上述每个 N1-N2、W1-W5 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-22T23:48:36.271189+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "5,7,8",
  "dpi": "165"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "5,7,8",
    "dpi": "165"
  }
}
```

</details>

---


### Tool result

_source line 1643 · 2026-05-22T23:48:36.824233+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 512.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 557.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 552.9}], \"total_pages\": 19, \"rendered_pages\": 3, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-22T23:48:40.236718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-22T23:48:41.040291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-22T23:48:41.090961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1647 · 2026-05-22T23:48:41.447186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1648 · 2026-05-22T23:48:42.101413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-22T23:48:42.453562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-22T23:50:57.732986+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Per-layer KL 分解的 confound 问题**\n\nR1 的核心批评成立。具体同意以下几点：\n\n1. **32× train-inference mismatch 是真实 confound**：K=1 训练时仅 mask 1/32 层，模型几乎在 dense 状态下运行，optimizer 面对的 loss landscape 远比 E2E（32 层全 mask）平滑。K=1 的好表现可能反映的是\"训练容易\"而非\"signal type 本身足够\"——论文未控制这一混淆变量。\n\n2. **K=4 在 50% 下比 K=1 差（PPL 44.23 vs 34.85）确实缺乏机制解释**：论文 §4.5 (p.8) 仅说 \"coupling scope dominates at high sparsity, reversing the 30% pattern\"，但未解释为什么增加 coupling（K=4）反而恶化。一个合理假设是 4 层同时 masking 在 50% sparsity 下引入过大扰动导致 gradient interference，但这需要实验验证（如 gradient norm/SNR 随 K 的变化曲线）。\n\n3. **\"29-97% on downstream tasks\" 的精确分解仅基于两个数据点（K=1, K=4）**：要声称精确的百分比分解，至少需要 K=2, 4, 8, 16 等更多数据点以观察趋势。\n\n**但补充一点**：R1 的批评主要针对 per-layer KL decomposition 实验（§4.5），而论文对 signal type 重要性的论证并非仅依赖此实验。§3.6 的梯度分析（BCE gradient $\\partial \\mathcal{L}/\\partial o_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron）提供了与实验独立的理论论证。Table 3 的 C1 ablation 也从另一角度支撑了 signal type 的重要性。所以 N1 削弱的是 \"quantitative decomposition\" 的精度，但不完全否定 \"signal type matters\" 的定性结论。\n\n建议作者：(1) 删除或大幅软化 \"29-97%\" 的精确分解 claim；(2) 补充更多 K 值的实验或移除 decomposition framing，改为定性讨论；(3) 明确承认 K=1 的 near-dense training confound。\n\n---\n\n**[AGREE] R1-N2: 知识密集型任务退步缺乏机制分析**\n\n完全同意。这也与我 Review 中的 W1 (wall-clock) 关切呼应——如果方法在 MMLU/GSM8K 上系统性退步，其实际部署场景会进一步受限。\n\n具体补充：\n\n1. **退步的一致性和幅度令人担忧**：从论文数据看，KL predictor 在 30% sparsity 下 MMLU 40.7±1.3（Table 2）vs TEAL baseline 应该更高；在 Qwen-2.5-14B 上 GSM8K 退步更严重（Table 13, Appendix O）。这不是个别 seed 的噪声，而是跨架构的系统性 pattern。\n\n2. **§4.4 的 \"Remove valley\" 实验（Table 4: MMLU +3.4pp）方向正确但不够**：它证明了 allocation pattern 影响 MMLU，但未回答核心问题——为什么 KL 的 output-distribution objective 会系统性地学到一个牺牲知识路径的 allocation？是因为 WikiText-103 训练分布中知识密集型 context 不足？还是 KL 本身的 mode-covering 特性导致它对高 entropy 层（恰好是知识存储层）施加更强的 sparsity 压力？论文应至少提出并讨论这些假设。\n\n3. **R1 建议的 Meng et al. (2022) \"Locating and Editing Factual Associations\" 参考是合理的**：理解哪些层/neuron 存储 factual knowledge 可以帮助解释为什么 KL 的 allocation 会伤害 MMLU。但我认为这更适合作为 future work 方向而非 must-fix——要求作者做完整的 knowledge attribution analysis 超出了 revision 的合理范围。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: C1 ablation 残余 confound**\n\n同意 soft→hard mask representation 变化引入了额外混淆变量。具体而言：\n\n1. KL 训练使用 Gumbel-Sigmoid 连续 soft masks（§3.3），C1 ablation 用 $\\mathbb{1}(s_j \\geq 0)$ 二值化提取 oracle masks。这一过程丢弃了 neuron importance 的 **排序信息**——两个 $s_j = 0.01$ 和 $s_j = 5.0$ 的 neuron 被等同对待。如 R1 所问（Q3），保留连续分数可能改善 C1 结果。\n\n2. 但 C1 的核心结论（KL-derived patterns transfer quality advantage to simpler training, PPL within 0.79pp）在方向上仍然成立——即使存在 confound，0.79pp 的差距说明 mask pattern 质量是主要贡献因素。confound 的存在使精确量化不可靠，但定性结论稳健。\n\n---\n\n**[AGREE] R1-W2: 无 wall-clock 加速**\n\n完全同意，我在自己的审稿中也将此列为 W1。Appendix A 显示 predictor 增加 6.4% overhead，且 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"（Abstract）。对于一篇 sparsity 论文，这是显著缺失。\n\n---\n\n**[AGREE] R1-W3: 评估覆盖度空白**\n\n同意所有三点：\n\n1. **无生成任务（MT-Bench, AlpacaEval）**：sparsity 对 autoregressive generation quality 的影响可能与 perplexity 和 MC-style downstream tasks 不同——generation 中误差可能累积，而 PPL 只衡量 next-token prediction。这与 N2 (knowledge-intensive degradation) 结合尤为重要：如果 MMLU 已经退步，generation quality 退步可能更严重。\n\n2. **序列长度固定 2048**：论文未讨论长序列下 activation pattern 是否变化。contextual sparsity 的核心假设是 mask depends on input——如果 input 长度从 2048 增到 8192 或 32K，pattern 可能发生质性变化。\n\n3. **Batched inference 未评估**：实际部署中 batch size > 1 是常态，但 predictor 的 overhead 和 sparsity pattern 的 batch consistency 均未测试。\n\n---\n\n**[AGREE] R1-W4: 高方差指标的统计可靠性**\n\n同意，但补充 nuance：\n\n1. **PPL（论文的 primary metric）方差很低**：Table 2 报告 11.84±0.15（3-seed），置信区间窄，结论可靠。\n\n2. **但 downstream tasks 方差确实过大**：ARC-c σ=3.6pp 在 3 seed 下 95% CI ≈ ±8.9pp，这意味着 KL vs TEAL 的差异（如 Table 2 中 ARC-c 的绝对值）可能在统计上不显著。BoolQ σ=11.5pp 更是使得该指标的任何结论都不可靠。论文应至少做 paired permutation test 或报告 effect size。\n\n3. **Table 4 多行单 seed（s42）确实削弱可信度**：特别是 ablation study（Table 4）的 \"Relaxation, Divergence, and SPON\" 部分，这些是论文的核心 design choice 验证，理应 multi-seed。\n\n---\n\n**[REBUT] R1-W5: Geometric penalty 在 30% 目标下偏差**\n\n部分不同意。\n\n1. R1 说 \"30% 目标永远无法精确达到（28.5% actual）\"——但论文 Appendix C (Table 9, p.13) 明确报告了 actual sparsity 随 target 的收敛曲线，且指出 \"the controller reliably drives actual sparsity to within ±2% of the target across all tested regimes\"。28.5% vs 30% 是 1.5pp 偏差，在 sparsity 研究中属于正常范围。\n\n2. **但 labeling 的 concern 有道理**：主文 Table 2 表头标注 \"uniforms at 30%\" 而非 \"uniforms at ~28.5% actual\"，这可能误导读者做精确的跨方法对比（如与 TEAL exactly 30% 对比）。建议在 Table 2 脚注标注 actual sparsity range。\n\n3. ε=0.02 deadzone 的工程合理性在 Appendix C 有解释（\"suppresses oscillation near the target\"），这不是任意选择。但 R1 的 concern 是 deadzone 导致 systematic undershoot，这确实需要在正文中 acknowledge。\n\n总结：偏差本身不严重（1.5pp），但 labeling 应更精确。这是 minor 而非 warning 级别问题。\n\n---\n\n### 对 R1 Questions 的补充看法\n\n**Q1 (K=4 50% 为何比 K=1 差)**：R1 的问题切中要害。我推测是因为 50% sparsity 下同时 mask 4 层（K=4 = 4/32 = 12.5% 层被 mask）引入的前向扰动远大于 K=1，导致 gradient signal 质量下降。但这需要实验验证（如比较 K=1/2/4/8 的 training loss curve 和 gradient SNR）。\n\n**Q2 (知识退步是否与 WikiText-103 有关)**：合理假设。WikiText-103 是百科风格但主要是英文维基，可能缺少数学推理和多步逻辑链的训练信号。如果在 code+math 混合数据上训练 predictor，MMLU/GSM8K 表现可能改善。但这也是推测，需要实验。\n\n**Q3 (C1 保留连续分数)**：好问题。当前 $\\mathbb{1}(s_j \\geq 0)$ 二值化确实丢弃了 ranking 信息。一个改进方案是用 KL-derived soft scores 作为 BCE target 的 soft label（而非 hard 0/1），这可能更干净地隔离 pattern quality 的贡献。\n\n**Q4 (STE 30% 仅 20.8% sparsity)**：Table 4 显示 STE 在 30% 下 PPL 15.77，且实际 sparsity 仅 20.8%。这说明 STE 的 gradient 通路问题不仅影响 quality 还影响 sparsity control——进一步支持 Gumbel-Sigmoid 作为 relaxation method 的重要性。但 R1 问是否调过 lr/gradient scaling——论文确实应回答这一问题，否则 STE 可能是 undertrained 而非方法本身不行。\n\n**Q5 (MSE 30% 3-seed)**：合理的数据完整性问题，应在 camera-ready 中明确。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Per-layer KL 分解的 confound 问题**\n\nR1 的核心批评成立。具体同意以下几点：\n\n1. **32× train-inference mismatch 是真实 confound**：K=1 训练时仅 mask 1/32 层，模型几乎在 dense 状态下运行，optimizer 面对的 loss landscape 远比 E2E（32 层全 mask）平滑。K=1 的好表现可能反映的是\"训练容易\"而非\"signal type 本身足够\"——论文未控制这一混淆变量。\n\n2. **K=4 在 50% 下比 K=1 差（PPL 44.23 vs 34.85）确实缺乏机制解释**：论文 §4.5 (p.8) 仅说 \"coupling scope dominates at high sparsity, reversing the 30% pattern\"，但未解释为什么增加 coupling（K=4）反而恶化。一个合理假设是 4 层同时 masking 在 50% sparsity 下引入过大扰动导致 gradient interference，但这需要实验验证（如 gradient norm/SNR 随 K 的变化曲线）。\n\n3. **\"29-97% on downstream tasks\" 的精确分解仅基于两个数据点（K=1, K=4）**：要声称精确的百分比分解，至少需要 K=2, 4, 8, 16 等更多数据点以观察趋势。\n\n**但补充一点**：R1 的批评主要针对 per-layer KL decomposition 实验（§4.5），而论文对 signal type 重要性的论证并非仅依赖此实验。§3.6 的梯度分析（BCE gradient $\\partial \\mathcal{L}/\\partial o_j = \\sigma(s_j) - m_j^*$ 仅依赖 neuron $j$，而 KL gradient 通过 downstream Jacobian 耦合所有 neuron）提供了与实验独立的理论论证。Table 3 的 C1 ablation 也从另一角度支撑了 signal type 的重要性。所以 N1 削弱的是 \"quantitative decomposition\" 的精度，但不完全否定 \"signal type matters\" 的定性结论。\n\n建议作者：(1) 删除或大幅软化 \"29-97%\" 的精确分解 claim；(2) 补充更多 K 值的实验或移除 decomposition framing，改为定性讨论；(3) 明确承认 K=1 的 near-dense training confound。\n\n---\n\n**[AGREE] R1-N2: 知识密集型任务退步缺乏机制分析**\n\n完全同意。这也与我 Review 中的 W1 (wall-clock) 关切呼应——如果方法在 MMLU/GSM8K 上系统性退步，其实际部署场景会进一步受限。\n\n具体补充：\n\n1. **退步的一致性和幅度令人担忧**：从论文数据看，KL predictor 在 30% sparsity 下 MMLU 40.7±1.3（Table 2）vs TEAL baseline 应该更高；在 Qwen-2.5-14B 上 GSM8K 退步更严重（Table 13, Appendix O）。这不是个别 seed 的噪声，而是跨架构的系统性 pattern。\n\n2. **§4.4 的 \"Remove valley\" 实验（Table 4: MMLU +3.4pp）方向正确但不够**：它证明了 allocation pattern 影响 MMLU，但未回答核心问题——为什么 KL 的 output-distribution objective 会系统性地学到一个牺牲知识路径的 allocation？是因为 WikiText-103 训练分布中知识密集型 context 不足？还是 KL 本身的 mode-covering 特性导致它对高 entropy 层（恰好是知识存储层）施加更强的 sparsity 压力？论文应至少提出并讨论这些假设。\n\n3. **R1 建议的 Meng et al. (2022) \"Locating and Editing Factual Associations\" 参考是合理的**：理解哪些层/neuron 存储 factual knowledge 可以帮助解释为什么 KL 的 allocation 会伤害 MMLU。但我认为这更适合作为 future work 方向而非 must-fix——要求作者做完整的 knowledge attribution analysis 超出了 revision 的合理范围。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: C1 ablation 残余 confound**\n\n同意 soft→hard mask representation 变化引入了额外混淆变量。具体而言：\n\n1. KL 训练使用 Gumbel-Sigmoid 连续 soft masks（§3.3），C1 ablation 用 $\\mathbb{1}(s_j \\geq 0)$ 二值化提取 oracle masks。这一过程丢弃了 neuron importance 的 **排序信息**——两个 $s_j = 0.01$ 和 $s_j = 5.0$ 的 neuron 被等同对待。如 R1 所问（Q3），保留连续分数可能改善 C1 结果。\n\n2. 但 C1 的核心结论（KL-derived patterns transfer quality advantage to simpler training, PPL within 0.79pp）在方向上仍然成立——即使存在 confound，0.79pp 的差距说明 mask pattern 质量是主要贡献因素。confound 的存在使精确量化不可靠，但定性结论稳健。\n\n---\n\n**[AGREE] R1-W2: 无 wall-clock 加速**\n\n完全同意，我在自己的审稿中也将此列为 W1。Appendix A 显示 predictor 增加 6.4% overhead，且 \"unstructured element-wise masks do not translate to wall-clock speedup without sparse kernel support\"（Abstract）。对于一篇 sparsity 论文，这是显著缺失。\n\n---\n\n**[AGREE] R1-W3: 评估覆盖度空白**\n\n同意所有三点：\n\n1. **无生成任务（MT-Bench, AlpacaEval）**：sparsity 对 autoregressive generation quality 的影响可能与 perplexity 和 MC-style downstream tasks 不同——generation 中误差可能累积，而 PPL 只衡量 next-token prediction。这与 N2 (knowledge-intensive degradation) 结合尤为重要：如果 MMLU 已经退步，generation quality 退步可能更严重。\n\n2. **序列长度固定 2048**：论文未讨论长序列下 activation pattern 是否变化。contextual sparsity 的核心假设是 mask depends on input——如果 input 长度从 2048 增到 8192 或 32K，pattern 可能发生质性变化。\n\n3. **Batched inference 未评估**：实际部署中 batch size > 1 是常态，但 predictor 的 overhead 和 sparsity pattern 的 batch consistency 均未测试。\n\n---\n\n**[AGREE] R1-W4: 高方差指标的统计可靠性**\n\n同意，但补充 nuance：\n\n1. **PPL（论文的 primary metric）方差很低**：Table 2 报告 11.84±0.15（3-seed），置信区间窄，结论可靠。\n\n2. **但 downstream tasks 方差确实过大**：ARC-c σ=3.6pp 在 3 seed 下 95% CI ≈ ±8.9pp，这意味着 KL vs TEAL 的差异（如 Table 2 中 ARC-c 的绝对值）可能在统计上不显著。BoolQ σ=11.5pp 更是使得该指标的任何结论都不可靠。论文应至少做 paired permutation test 或报告 effect size。\n\n3. **Table 4 多行单 seed（s42）确实削弱可信度**：特别是 ablation study（Table 4）的 \"Relaxation, Divergence, and SPON\" 部分，这些是论文的核心 design choice 验证，理应 multi-seed。\n\n---\n\n**[REBUT] R1-W5: Geometric penalty 在 30% 目标下偏差**\n\n部分不同意。\n\n1. R1 说 \"30% 目标永远无法精确达到（28.5% actual）\"——但论文 Appendix C (Table 9, p.13) 明确报告了 actual sparsity 随 target 的收敛曲线，且指出 \"the controller reliably drives actual sparsity to within ±2% of the target across all tested regimes\"。28.5% vs 30% 是 1.5pp 偏差，在 sparsity 研究中属于正常范围。\n\n2. **但 labeling 的 concern 有道理**：主文 Table 2 表头标注 \"uniforms at 30%\" 而非 \"uniforms at ~28.5% actual\"，这可能误导读者做精确的跨方法对比（如与 TEAL exactly 30% 对比）。建议在 Table 2 脚注标注 actual sparsity range。\n\n3. ε=0.02 deadzone 的工程合理性在 Appendix C 有解释（\"suppresses oscillation near the target\"），这不是任意选择。但 R1 的 concern 是 deadzone 导致 systematic undershoot，这确实需要在正文中 acknowledge。\n\n总结：偏差本身不严重（1.5pp），但 labeling 应更精确。这是 minor 而非 warning 级别问题。\n\n---\n\n### 对 R1 Questions 的补充看法\n\n**Q1 (K=4 50% 为何比 K=1 差)**：R1 的问题切中要害。我推测是因为 50% sparsity 下同时 mask 4 层（K=4 = 4/32 = 12.5% 层被 mask）引入的前向扰动远大于 K=1，导致 gradient signal 质量下降。但这需要实验验证（如比较 K=1/2/4/8 的 training loss curve 和 gradient SNR）。\n\n**Q2 (知识退步是否与 WikiText-103 有关)**：合理假设。WikiText-103 是百科风格但主要是英文维基，可能缺少数学推理和多步逻辑链的训练信号。如果在 code+math 混合数据上训练 predictor，MMLU/GSM8K 表现可能改善。但这也是推测，需要实验。\n\n**Q3 (C1 保留连续分数)**：好问题。当前 $\\mathbb{1}(s_j \\geq 0)$ 二值化确实丢弃了 ranking 信息。一个改进方案是用 KL-derived soft scores 作为 BCE target 的 soft label（而非 hard 0/1），这可能更干净地隔离 pattern quality 的贡献。\n\n**Q4 (STE 30% 仅 20.8% sparsity)**：Table 4 显示 STE 在 30% 下 PPL 15.77，且实际 sparsity 仅 20.8%。这说明 STE 的 gradient 通路问题不仅影响 quality 还影响 sparsity control——进一步支持 Gumbel-Sigmoid 作为 relaxation method 的重要性。但 R1 问是否调过 lr/gradient scaling——论文确实应回答这一问题，否则 STE 可能是 undertrained 而非方法本身不行。\n\n**Q5 (MSE 30% 3-seed)**：合理的数据完整性问题，应在 camera-ready 中明确。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-22T23:51:01.195766+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3462
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-22T23:51:06.425681+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-22T23:51:06.477214+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_21/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 1654 · 2026-05-22T23:51:21.815355+00:00_

交叉回应已提交。总结：

- **R1-N1 (per-layer KL decomposition confound)**: [AGREE] — 32× train-inference mismatch 是真实 confound，K=4 anomaly 未解释，"29-97%" 精确分解证据不足。但补充指出 §3.6 梯度分析和 C1 ablation 提供了独立于该 decomposition 的 signal type 重要性证据。
- **R1-N2 (知识密集型退步)**: [AGREE] — 跨架构系统性退步缺乏机制解释，"sacrifice reasoning-critical pathways" 是事后叙事。
- **R1-W1 (C1 confound)**: [AGREE] — soft→hard 变化引入混淆，但定性结论（0.79pp gap）仍稳健。
- **R1-W2 (无 wall-clock)**: [AGREE]
- **R1-W3 (评估空白)**: [AGREE] — 无生成任务、固定序列长度、无 batched inference 均为真实缺失。
- **R1-W4 (高方差)**: [AGREE] — PPL 可靠但 downstream tasks（ARC-c, BoolQ）方差过大。
- **R1-W5 (geometric penalty 偏差)**: [REBUT] — 1.5pp 偏差属正常范围且 Appendix C 有详细报告，但同意 Table 2 labeling 应更精确。建议降级为 minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 42

## Round 42

88 recorded events


### User

_source line 1655 · 2026-05-23T00:34:26.541287+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式**: Long paper，8 页正文限制（不含 references/limitations/ethics），ACL 模板 (acl.sty)
- **匿名规则**: Double-blind
- **评分标准**: ARR Overall Assessment 1-5 分（4=Conference，3.5=Borderline Conference，3=Findings）

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- 各章节: 同目录下 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex

## 你的审查侧重

### 1. 新颖性评估
- 核心贡献是什么？是将 KL distillation 应用到 activation sparsity prediction——这与 MaskLLM（KL + static N:M weight masks）有多大区别？
- MaskLLM 三点区分（§2 Related Work）是否有说服力：(a) contextual vs static, (b) cross-layer allocation, (c) distribution shift robustness
- "2D taxonomy"（Table 2）是否真的组织了 prior work，还是为了制造 novelty？
- Target-swap ablation（C1）和 per-layer KL decomposition 作为分析贡献是否足够新颖？
- 与 DejaVu、FastForward、ShadowLLM、D2DMoE 的 positioning 是否准确

### 2. 完整性
- 评估覆盖度：PPL + 6 个下游任务够吗？是否缺少生成任务（MT-Bench, AlpacaEval）？
- Seq length 固定 2048——是否覆盖了实际场景？
- Batched inference 未评估——这对实际部署意味着什么？
- 仅 7-14B 规模——是否足以支撑 general claims？
- 训练数据仅 WikiText-103——OOD 泛化是否被充分验证（C4 evaluation 在 Appendix D）？

### 3. 写作质量
- Abstract 信息密度是否合理？8 句 abstract 是否 too dense？
- Introduction 逻辑流是否清晰：problem → gap → approach → results → contributions
- Claims 与 evidence 的匹配：特别注意 "signal type accounts for the majority of the PPL gap" 这个 claim 是否被 upper bound caveat 充分修饰
- "dominant design dimension" / "primary design dimension" 等措辞是否过强
- Conclusion 是否准确反映了论文发现（包括 limitations）
- 术语一致性：检查全文术语使用是否统一
- 数字引用准确性：正文中引用的数字是否与表格一致

### 4. 格式合规
- 页数检查：正文是否在 8 页内？
- 匿名性：是否有 de-anonymizing 信息（代码链接、GPU 型号泄露身份、致谢等）
- 参考文献格式：natbib, ACL .bst
- Figure/Table 质量：字号是否可读（≥8pt），caption 是否 self-contained
- Limitations 章节覆盖度

### 5. Missing References
- 检查是否遗漏了 2024-2026 年的重要相关工作
- 特别注意：contextual sparsity prediction、KL distillation for pruning、SwiGLU sparsity 方向的新工作

请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues → Missing References → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-23T00:34:34.182208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-23T00:34:34.182828+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-23T00:34:36.291343+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-23T00:34:36.342039+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-23T00:34:38.750872+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-23T00:34:38.851681+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/skills/projects/distill_sparse_swiglu/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/skills/projects/distill_sparse_swiglu/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-23T00:34:44.423042+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1663 · 2026-05-23T00:34:45.979104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-23T00:34:50.249717+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1665 · 2026-05-23T00:34:52.513522+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-23T00:34:57.603773+00:00_

Web search results for query: "ACL Rolling Review ARR reviewer guidelines review form criteria 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL Rolling Review (ARR) reviewer guidelines and criteria for 2025-2026:

## Review Form Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Reviewer Guidelines and Requirements

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Important Policies for 2025-2026

**Review Quality Standards:** The program chairs and ARR EiCs will consider egregious cases reported by chairs, including extremely terse reviews, unprofessional tone, and LLM-generated reviews.

**Consequences for Irresponsible Reviewing:** 'Highly irresponsible' reviewers or chairs may have thei
…[truncated 868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7354
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-23T00:34:58.960502+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6446
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-23T00:35:06.692191+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment), their scales, and what each score level means. Also extract any guidelines about what makes a good review, what reviewers should evaluate, and the review form structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions (soundness, excitement, overall assessment), their scales, and what each score level means. Also extract any guidelines about what makes a good review, what reviewers should evaluate, and the review form structure."
  }
}
```

</details>

---


### Tool call

_source line 1669 · 2026-05-23T00:35:07.394784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-23T00:35:08.102452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1671 · 2026-05-23T00:35:08.960984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-23T00:35:09.415536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1673 · 2026-05-23T00:35:09.617011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2222
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-23T00:35:09.617480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1675 · 2026-05-23T00:35:10.775671+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2673
}
```

</details>

---


### Tool result

_source line 1676 · 2026-05-23T00:35:12.333454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3372
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-23T00:35:12.788011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3372
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-23T00:35:12.839388+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3221
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-23T00:35:14.604140+00:00_

# ARR Review Form Criteria and Guidelines

## Scoring Dimensions

The document specifies **three required scores** for reviewers (as of February 2025):

1. **Soundness** - Technical validity and methodology assessment
2. **Excitement** - Personal interest and subjective appeal
3. **Overall Assessment** - Explicit recommendation for acceptance/rejection

The guidelines note that "soundness scores must be justified by the text of the review." Low soundness ratings require explicit justification; otherwise, reviews lack "faithful explanation of your recommendation."

## Key Evaluation Standards

**Soundness encompasses:**
- Technical correctness and validity
- Appropriate methodology choices
- Reproducibility and sufficient implementation details
- Sound argumentation and evidence

**Excitement reflects:**
- Reviewer's personal interest (orthogonal to soundness)
- Subjective preference rather than objective quality
- Recognition that sound work may not personally excite all reviewers

**Overall Assessment combines:**
- Soundness evaluation
- Excitement considerations
- Novelty and potential impact factors
- All papers meeting conference standards must demonstrate sufficient soundness and reproducibility

## What Makes a Strong Review

The document emphasizes reviewers should:

- "Be specific" with concrete examples rather than vague criticisms
- Provide "sufficient evidence for the claim that the authors are making" without demanding excessive additional experiments
- Maintain "professional and neutral" tone, avoiding sarcasm or dismissiveness
- Read papers twice: first for expectations adjustment, then in-depth

The guidelines warn against common problematic review patterns (H1-H17) including dismissing surprising results, demanding unnecessary comparisons, or conflating limitations with fundamental weaknesses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7911
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-23T00:35:22.484230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1681 · 2026-05-23T00:35:22.937194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1682 · 2026-05-23T00:35:23.340645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1683 · 2026-05-23T00:35:23.341082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1684 · 2026-05-23T00:35:24.249847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1312
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-23T00:35:24.251013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-23T00:35:24.251487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1687 · 2026-05-23T00:35:24.452513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1688 · 2026-05-23T00:35:25.156077+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-23T00:35:25.408054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-23T00:35:32.985750+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-23T00:35:34.548227+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 329.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1562
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-23T00:35:37.107568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1693 · 2026-05-23T00:35:37.411424+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1694 · 2026-05-23T00:35:38.369257+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-23T00:35:38.369994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-23T00:35:38.520891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1697 · 2026-05-23T00:35:38.872751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1698 · 2026-05-23T00:35:39.325627+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1699 · 2026-05-23T00:35:39.326061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1700 · 2026-05-23T00:35:39.879992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-23T00:35:40.133586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-23T00:35:44.803163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-23T00:35:45.610571+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-23T00:35:45.611037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-23T00:35:46.065219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-23T00:35:46.065684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-23T00:35:46.567507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-23T00:35:48.075983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2010
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-23T00:35:48.077923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-23T00:35:54.551903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-23T00:35:54.803150+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (max $\Delta$$\leq$0.79pp, 3-seed).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at 30\% (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1712 · 2026-05-23T00:35:54.853759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-23T00:35:54.904560+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation suggests that KL-discovered mask targets carry most of the quality information at inference: BCE trained on KL-derived targets reproduces KL quality (max $\Delta$$\leq$0.79pp at 50\%, s42), while magnitude-trained BCE achieves 28.13$\pm$0.20. Cross-
…[truncated 2908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-23T00:35:59.420887+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-23T00:35:59.521885+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importan
…[truncated 9554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-23T00:35:59.572589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1717 · 2026-05-23T00:35:59.874416+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-23T00:36:05.662180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-23T00:36:06.013823+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse} address dynamic sparsity--quantization interaction; AWQ~\cite{lin2024awq} applies activation-aware weight quantization for on-device deployment; Outlier Suppression+~\cite{wei2023outlier} mitigates outlier-induced quantization errors via shifting and scaling.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines non-uniform per-layer sparsity ratios based on activation outlier distribution for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a
…[truncated 5177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-23T00:36:06.014235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-23T00:36:06.465991+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL (signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-23T00:36:06.466359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-23T00:36:06.817688+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. Evaluation is limited to 7--14B; scaling to 70B+ and wall-clock speedup via sparse kernels remain future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-23T00:36:06.818045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1725 · 2026-05-23T00:36:06.918662+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-23T00:36:12.137209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-23T00:36:12.389237+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 36747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-23T00:36:18.412899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-23T00:36:18.413747+00:00_

1	% =============================================================================
2	% Additional references (R20 review response)
3	% =============================================================================
4	
5	@article{huang2025larosa,
6	  title={La{R}o{SA}: Accelerating Large Language Model Inference with Layerwise Rotated Sparse Activation},
7	  author={Huang, Fangcheng and others},
8	  journal={arXiv preprint arXiv:2507.01299},
9	  year={2025}
10	}
11	
12	@inproceedings{geva2023dissecting,
13	  title = {Dissecting Recall of Factual Associations in Auto-Regressive Language Models},
14	  author = {Geva, Mor and Bastings, Jasmijn and Filippova, Katja and Globerson, Amir},
15	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
16	  pages = {12216--12235},
17	  year = {2023},
18	}
19	
20	@article{fu2024lazyllm,
21	  title = {{LazyLLM}: Dynamic Token Pruning for Efficient Long Context {LLM} Inference},
22	  author = {Qichen Fu and Minsik Cho and Thomas Merth and Sachin Mehta and Mohammad Rastegari and Mahyar Najibi},
23	  year = {2024},
24	  journal = {arXiv preprint arXiv:2407.14057},
25	}
26	
27	@article{zhang2025cots,
28	  title = {{COTS}: Connected Sparse Activation for Efficient {LLM} Inference},
29	  author = {Yilong Zhang and Junyuan Shang and Huanqi Cao and Shiyao Li and Shuguang Jiang and Lingxiao Ma and Shun Zheng and Cheng Li and Jiang Bian},
30	  year = {2025},
31	  journal = {arXiv preprint arXiv:2502.14475},
32	}
33	
34	@inproceedings{alizadeh2024llmflash,
35	  title = {{LLM} in a Flash: Efficient Large Language Model Inference with Limited Memory},
36	  author = {Keivan Alizadeh and Iman Mirzadeh and Dmitry Belenko and Karen Khatamifard and Minsik Cho and Carlo C Del Mundo and Mohammad Rastegari and Mehrdad Farajtabar},
37	  year = {2024},
38	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
39	}
40	
41	@article{wei2023outlier,
4
…[truncated 24334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-23T00:36:26.819706+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "contextual sparsity prediction LLM activation sparsity 2025 2026 new methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "contextual sparsity prediction LLM activation sparsity 2025 2026 new methods"
  }
}
```

</details>

---


### Tool call

_source line 1731 · 2026-05-23T00:36:27.371901+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement overall assessment score scale 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement overall assessment score scale 2025"
  }
}
```

</details>

---


### Tool result

_source line 1732 · 2026-05-23T00:36:35.167550+00:00_

Web search results for query: "ACL ARR review form soundness excitement overall assessment score scale 2025"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Responsiveness of the Various Short-Form Versions of the Knee Injury and Osteoarthritis Outcome Score Between 2 and 5 Years After Anterior Cruciate Ligament Reconstruction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10960337/"}]

Based on the search results, here's what I found about the ACL ARR (ACL Rolling Review) review form scoring system for 2025:

## Three Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

The soundness scale includes levels such as: 5 = Excellent, 4 = Strong, and 3 = Acceptable.

## Excitement Sco
…[truncated 654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7795
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-23T00:36:35.971150+00:00_

Web search results for query: "contextual sparsity prediction LLM activation sparsity 2025 2026 new methods"

Links: [{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"}]

Based on the search results, here are the latest developments in contextual sparsity prediction and LLM activation sparsity for 2025-2026:

## Recent Methods (2025-2026)

**SVD Contextual Sparsity Predictors** (March 2026)
A recent framework accelerates inference of ReGLU-based feed-forward networks using a training-free method for building sparse pattern predictors through truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with threshold calibration and inference executors. This approach achieves up to 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on complex math and code generation tasks.

**Activation Pattern Clustering** (April 2026)
A sparsity predicting approach for large language models via activation pattern clustering has been developed, with results showing up to 79.34% clustering precision while maintaining minimal degradation in 
…[truncated 840 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9151
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-23T00:36:40.236123+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 definitions), all fields reviewers must fill, and any specific guidelines about what each score means. I need the exact wording for soundness scale, excitement scale, and overall assessment scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their exact scales (1-5 definitions), all fields reviewers must fill, and any specific guidelines about what each score means. I need the exact wording for soundness scale, excitement scale, and overall assessment scale."
  }
}
```

</details>

---


### Tool result

_source line 1735 · 2026-05-23T00:36:46.407519+00:00_

# ACL Rolling Review Form - Complete Structure

## Required Fields

Reviewers must complete:
1. Paper Summary
2. Summary of Strengths
3. Summary of Weaknesses
4. Comments/Suggestions/Typos
5. Five numerical scoring dimensions
6. Limitations and Societal Impact assessment
7. Ethical Concerns review
8. Reproducibility evaluation
9. Author identity disclosure

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale):
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with minor risk of missing details
- 3: "Pretty sure" but may have missed specifics
- 2: "Willing to defend" but likely gaps exist
- 1: "Not my area" or very unclear paper

**Soundness** (1-5 with half-point increments):
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: Some main claims insufficiently supported"
- 1: "Major Issues: not sufficiently thorough for publication"

**Excitement** (1-5 with half-point increments):
- 5: "Highly Exciting: would recommend to others"
- 4: "Exciting: would mention to others"
- 3: "Interesting: might mention to others"
- 2: "Potentially Interesting: doesn't resonate personally"
- 1: "Not Exciting: no broader community appeal"

**Overall Assessment** (1-5 with half-point increments):
- 5: "Consider for Award" (top 2.5%)
- 4: "Conference: could be accepted"
- 3: "Findings: acceptable for findings track"
- 2: "Resubmit next cycle"
- 1: "Do not resubmit"

## Additional Scales

**Reproducibility** (1-5): ranges from "could easily reproduce" to "could not reproduce"

**Datasets & Software** (1-5): rates from "Enabling" to "No usable [resources] submitted"

**Author Identity** (1-5): disclosure of potential double-blind violations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6171
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-23T00:42:18.599773+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## Paper Summary\n\n本文提出用前向 KL 散度（output-distribution distillation）替代 BCE 来训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，而 BCE 独立处理每个神经元。在 LLaMA-3.1-8B 上 30% sparsity 下，KL predictor 将 PPL 相对 TEAL 降低 14.5%（matched sparsity），在 Mistral-7B 和 Qwen-2.5-14B 上 PPL 优势泛化。论文通过 C1 target-swap ablation 和 per-layer KL 分解，将 KL 的优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope（cross-layer vs per-layer），发现 signal type 主导 PPL 差距（upper bound），coupling scope 对下游 commonsense 任务有实质贡献但对 reasoning 贡献有限。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、分析框架有巧思的实证论文，但方法本身新颖性有限（将已有技术 KL+Gumbel 应用于稀疏预测器训练），且知识密集型任务的系统性退化和缺乏实际 wall-clock 加速削弱了实用价值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论扎实（multi-seed、cross-architecture、controlled ablation），但 K=1 per-layer 控制有 train-inference mismatch confound，MSE baseline 在 50% 仅 1/3 seed 成功 |\n| Excitement | 3/5 | C1 ablation 和 signal type/coupling scope 分解是有信息量的分析贡献，但核心方法（KL+Gumbel→sparsity predictor）是已有技术的直接应用 |\n| Overall Assessment | 3.5/5 | Borderline Conference：分析贡献扎实但技术新颖性受限，知识任务退化和无 speedup 限制实用性 |\n| Confidence | 4/5 | 对 LLM 稀疏性和知识蒸馏方向较为熟悉 |\n| Reproducibility | 4/5 | 超参数、架构细节充分，承诺开源 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查\n\n- 具体位置：§4.1 (Knowledge-Task Regression: Hypothesis)、§4.6 (Cross-Architecture and Scale)、Limitations\n- 问题：KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设（WikiText-103 训练数据偏差、forward KL mode-covering 稀释稀有激活），但 **没有做任何控制实验来验证这些假设**。例如：(a) 在更多样化的训练数据上训练 predictor 能否缓解？(b) 调整 temperature 或使用 reverse KL 是否能保护 reasoning pathways？这些都是可行的消融实验但未执行。\n- 为什么影响接收：一个声称优于 TEAL 的方法如果在知识任务上系统退化，其实用价值大打折扣。读者需要知道这是方法固有的限制还是可以通过简单改进缓解的。仅提出假设而不验证，使核心发现的实用意义存疑。\n- 建议修改方向：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，测试知识任务是否改善。或者测试 task-specific allocation（论文自己在 Appendix T 的 constraint analysis 中展示了 remove-valley 能提升 MMLU +3.4pp 和 GSM8K +1.6pp，这一发现应在正文中更突出）。\n\n**N2** [critical] 方法新颖性的边界需要更清晰地论证\n\n- 具体位置：§1 Introduction、§3 Method、§2 Related Work\n- 问题：核心技术贡献——KL 散度 + Gumbel-Sigmoid 松弛训练 sparsity predictor——每个组件都是成熟技术：KL distillation (Hinton 2015)、Gumbel-Sigmoid (Maddison 2017, Louizos 2018)、sparsity predictor 架构 (DejaVu 2023)。MaskLLM (Fang et al., 2024) 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask 训练。论文在 §2 提出的三点区分（contextual vs static, cross-layer allocation, distribution shift robustness）是合理的，但这些区别更多来自 **应用场景的不同**（activation sparsity vs weight sparsity），而非方法论的创新。\n- 为什么影响接收：ACL 审稿需要评估 contribution 的 significance。若核心方法仅是将已有技术组合应用到新场景，则论文需要在分析贡献上具有更强的 novelty 来弥补。C1 ablation 和 per-layer decomposition 是有价值的分析贡献，但它们作为主要 contribution 是否足够需要 reviewer 判断。\n- 建议修改方向：论文可以更明确地将自己定位为 **分析驱动的实证贡献**（the paper already does this somewhat with \"primarily an empirical study\"），并加强 C1 ablation 和 signal type/coupling scope 分解的 framing，将其作为主要贡献而非辅助发现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Per-layer KL 分解在 50% sparsity 下失效\n\n- 具体位置：§4.5 (Per-Layer KL)，Table 4\n- 问题：在 50% sparsity 下，K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，而 E2E KL 为 11.84。论文假设这是 partial coupling 下的 gradient interference，但未提供证据。这意味着论文的核心分析框架（signal type vs coupling scope decomposition）在高稀疏度下不适用，但 abstract 和 conclusion 仍使用来自 30% 实验的分解结果做出 general claims。\n- 建议：在 abstract/conclusion 中明确限定 decomposition 结论的适用范围（\"at moderate sparsity\"），或提供 50% 下的替代分析。\n\n**W2** [warning] 无 wall-clock 加速，6.4% latency overhead\n\n- 具体位置：Appendix A、§1 Introduction (sentence 8)\n- 问题：论文诚实地披露了这一点（appreciated），但这意味着目前的方法在实际部署中不仅没有加速，反而增加了 6.4% 延迟。Without sparse kernel support, the predictor is purely an analytical tool, not a practical system contribution. 这对一篇投稿到 NLP 会议（而非系统会议）的论文是可以接受的，但对实用影响的声明需要相应弱化。\n- 建议：这已在论文中处理得相当好。可在 Conclusion 中更明确地说明 \"实际加速取决于未来稀疏核的支持\" 而非仅在 appendix 中提及。\n\n**W3** [warning] 缺少生成质量评估\n\n- 具体位置：Limitations (acknowledged)\n- 问题：评估仅涵盖 PPL 和 multiple-choice benchmarks。Open-ended generation (MT-Bench, AlpacaEval) 在 sparsity 下的表现可能与 PPL/选择题结果不一致。特别是论文发现 KL 的 mode-covering 特性在 commonsense 上优势但知识任务退化——这对生成质量可能有不同的影响模式。\n- 建议：这已在 Limitations 中提及。若能增加 MT-Bench 或 AlpacaEval 的结果将显著增强论文的完整性。\n\n**W4** [warning] Introduction 中 \"19%\" PPL 减少数字有误\n\n- 具体位置：§4.1, Introduction ¶13\n- 问题：Introduction 声称 \"reducing TEAL's perplexity by 19% (10.82 → 8.81)\"。实际计算：(10.82 - 8.81) / 10.82 = 18.58%，约 18.6%，而非 19%。Abstract 正确使用了 matched-sparsity 的 14.5%。这种不精确虽小，但在审稿人 verify 数字时会引发信任问题。\n- 建议：修正为 18.6% 或 ~19%，并注明此为 nominal sparsity 下的比较（actual sparsity 分别为 28.5% vs 29.3%）。\n\n**W5** [warning] MSE baseline 在 50% sparsity 下的可靠性\n\n- 具体位置：Appendix G (MSE Baseline Configuration)、Table 4\n- 问题：MSE baseline 在 50% sparsity 下，seed 123 catastrophic failure (PPL=15,789, 仅 5.1% 实际稀疏度)。因此 Table 4 中 MSE 50% 的 229.26 实际仅来自 seed 42（标注 §），而非 3-seed 平均。这使得 MSE 在高稀疏度下的比较不可靠，但论文在 §3.7 中仍使用 MSE 50% 结果（\"1.7×/9.6× worse PPL\"）来论证 taxonomy 的预测力。\n- 建议：正文中使用 MSE 50% 结果时应明确注明 single-seed caveat，并讨论这种 instability 是否反映了 MSE loss 本身的问题还是实现细节。\n\n**W6** [warning] C1 ablation 中 seed 42 oracle provenance 问题\n\n- 具体位置：Table 3 footnote、Appendix P\n- 问题：C1 ablation 的 s42 oracle 来自 \"earlier training run\"，而 s123/s456 使用 matched retrained oracles。s42 的 PPL gap (0.65pp at 30%) 显著大于 s123/s456 (≤0.03pp)。虽然论文在 footnote 中披露了这一点，但 s42 是唯一有 50% 数据的 seed，使得 50% 的 C1 结论基于可能有 confound 的单 seed。\n- 建议：提供 s123 或 s456 在 50% sparsity 下的 C1 结果以增强稳健性，或明确说明 50% 的 C1 结论仅基于 s42。\n\n---\n\n## 小问题（不影响接收）\n\n- **Table 2 比较不对齐**：BCE 30% 使用 TEAL global 分配（标注 †），而 KL 30% 使用 uniform 分配，使直接比较不公平。建议在同一 allocation 下展示 BCE 结果，或在 caption 中更醒目地标注。\n- **Abstract 信息密度偏高**：9 句 abstract 涵盖了 problem、method、主结果、C1 ablation、signal type claim、coupling scope claim、cross-arch、disclaimer——信息量极大，但对首次阅读的读者来说可能太密集。考虑将 abstract 压缩至 6-7 句，将 C1 和 decomposition 细节移至正文。\n- **Conclusion 过于简洁**：仅 4 句话，缺少对 future work 方向的讨论（如 task-aware allocation, diverse training data, sparse kernel integration）。\n- **术语一致性**：\"output-distribution alignment\"、\"output-distribution distillation\"、\"output-distribution objective\" 在全文中交替使用，建议统一。\n- **Figure 2 caption 的 14.5%**：此处使用 matched-sparsity 的 14.5%，而 §4.1 正文使用 nominal 的 \"19%\"（实为 18.6%），两处使用不同基准但未解释，可能造成困惑。\n- **GPU 型号**：\"NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96GB)\" 是非常具体的新硬件（2025 年发布），虽然不直接暴露身份，但在 double-blind 审稿中需注意——拥有该 GPU 的实验室相对较少。\n\n---\n\n## Missing References\n\n本文的 related work 覆盖面相当完善（50+ 引用），涵盖了 training-free、predictor-based、activation function engineering、weight pruning、KL distillation、MoE routing 等主要方向。以下为可能的补充：\n\n- **TurboSparse-Mistral**（Song et al., 2025）：虽已引用 TurboSparse，但该系列后续工作包括特定模型适配，可能值得更新引用。\n- 论文未引用 **Mixtral-of-Experts** 相关的稀疏激活工作，虽然 MoE 与 activation sparsity 有本质区别，但部分读者可能期望看到更明确的区分说明。\n- 建议补充检索 2026 年 1-5 月是否有新的 **KL distillation for activation sparsity** 的工作（如 SVD-CSP 已引用，但该方向可能有更多新进展）。\n\n总体上，missing references 不构成重大问题。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：3-seed 评估、cross-architecture 验证（3 个模型）、matched-sparsity 比较、多达 18 个 appendix sections 的补充实验。这在同类工作中是高标准。\n2. **C1 target-swap ablation 设计巧妙**：通过将 KL 发现的 mask 模式转移给 BCE 训练，干净地分离了 \"mask pattern quality\" 和 \"gradient coupling mechanism\" 的贡献。这是一个有 insight 的实验设计。\n3. **诚实的 limitations 披露**：论文自始至终坦诚地报告了知识任务退化、无 wall-clock 加速、评估限制等。这增强了结果的可信度。\n4. **Per-layer KL decomposition**：K=1 和 K=4 控制实验合理地（虽然不完美地）分解了 signal type 和 coupling scope 的贡献，并发现了有趣的 task-dependent dissociation。\n5. **写作质量**：Claims 有适当的 hedging（\"upper bound\"、\"suggests\"、\"primarily empirical\"），数字引用有 exp_id 追踪。\n6. **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化了推理管线。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 |\n| Excitement | 3 |\n| Overall Assessment | 3.5 |\n| Reviewer Confidence | 4 |\n| Reproducibility | 4 |",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## Paper Summary\n\n本文提出用前向 KL 散度（output-distribution distillation）替代 BCE 来训练 SwiGLU LLM 的轻量级稀疏性预测器（<1% base 参数）。核心 insight 是 KL 将所有 mask 决策通过输出分布耦合，而 BCE 独立处理每个神经元。在 LLaMA-3.1-8B 上 30% sparsity 下，KL predictor 将 PPL 相对 TEAL 降低 14.5%（matched sparsity），在 Mistral-7B 和 Qwen-2.5-14B 上 PPL 优势泛化。论文通过 C1 target-swap ablation 和 per-layer KL 分解，将 KL 的优势解耦为 signal type（output-distribution vs intermediate loss）和 coupling scope（cross-layer vs per-layer），发现 signal type 主导 PPL 差距（upper bound），coupling scope 对下游 commonsense 任务有实质贡献但对 reasoning 贡献有限。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 实验设计严谨、分析框架有巧思的实证论文，但方法本身新颖性有限（将已有技术 KL+Gumbel 应用于稀疏预测器训练），且知识密集型任务的系统性退化和缺乏实际 wall-clock 加速削弱了实用价值。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验方法论扎实（multi-seed、cross-architecture、controlled ablation），但 K=1 per-layer 控制有 train-inference mismatch confound，MSE baseline 在 50% 仅 1/3 seed 成功 |\n| Excitement | 3/5 | C1 ablation 和 signal type/coupling scope 分解是有信息量的分析贡献，但核心方法（KL+Gumbel→sparsity predictor）是已有技术的直接应用 |\n| Overall Assessment | 3.5/5 | Borderline Conference：分析贡献扎实但技术新颖性受限，知识任务退化和无 speedup 限制实用性 |\n| Confidence | 4/5 | 对 LLM 稀疏性和知识蒸馏方向较为熟悉 |\n| Reproducibility | 4/5 | 超参数、架构细节充分，承诺开源 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识密集型任务的系统性退化缺乏充分调查\n\n- 具体位置：§4.1 (Knowledge-Task Regression: Hypothesis)、§4.6 (Cross-Architecture and Scale)、Limitations\n- 问题：KL predictor 在所有测试规模上系统性地在 MMLU/GSM8K 上退化（8B: MMLU -5.2pp; Mistral: GSM8K 15.9→8.6; Qwen-14B: GSM8K -20pp, MMLU -8.1pp）。论文仅提出两个假设（WikiText-103 训练数据偏差、forward KL mode-covering 稀释稀有激活），但 **没有做任何控制实验来验证这些假设**。例如：(a) 在更多样化的训练数据上训练 predictor 能否缓解？(b) 调整 temperature 或使用 reverse KL 是否能保护 reasoning pathways？这些都是可行的消融实验但未执行。\n- 为什么影响接收：一个声称优于 TEAL 的方法如果在知识任务上系统退化，其实用价值大打折扣。读者需要知道这是方法固有的限制还是可以通过简单改进缓解的。仅提出假设而不验证，使核心发现的实用意义存疑。\n- 建议修改方向：至少执行一个控制实验——例如在 C4 或 RedPajama 子集上训练 predictor，测试知识任务是否改善。或者测试 task-specific allocation（论文自己在 Appendix T 的 constraint analysis 中展示了 remove-valley 能提升 MMLU +3.4pp 和 GSM8K +1.6pp，这一发现应在正文中更突出）。\n\n**N2** [critical] 方法新颖性的边界需要更清晰地论证\n\n- 具体位置：§1 Introduction、§3 Method、§2 Related Work\n- 问题：核心技术贡献——KL 散度 + Gumbel-Sigmoid 松弛训练 sparsity predictor——每个组件都是成熟技术：KL distillation (Hinton 2015)、Gumbel-Sigmoid (Maddison 2017, Louizos 2018)、sparsity predictor 架构 (DejaVu 2023)。MaskLLM (Fang et al., 2024) 已将 KL + Gumbel-Softmax 用于可学习稀疏 mask 训练。论文在 §2 提出的三点区分（contextual vs static, cross-layer allocation, distribution shift robustness）是合理的，但这些区别更多来自 **应用场景的不同**（activation sparsity vs weight sparsity），而非方法论的创新。\n- 为什么影响接收：ACL 审稿需要评估 contribution 的 significance。若核心方法仅是将已有技术组合应用到新场景，则论文需要在分析贡献上具有更强的 novelty 来弥补。C1 ablation 和 per-layer decomposition 是有价值的分析贡献，但它们作为主要 contribution 是否足够需要 reviewer 判断。\n- 建议修改方向：论文可以更明确地将自己定位为 **分析驱动的实证贡献**（the paper already does this somewhat with \"primarily an empirical study\"），并加强 C1 ablation 和 signal type/coupling scope 分解的 framing，将其作为主要贡献而非辅助发现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Per-layer KL 分解在 50% sparsity 下失效\n\n- 具体位置：§4.5 (Per-Layer KL)，Table 4\n- 问题：在 50% sparsity 下，K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，而 E2E KL 为 11.84。论文假设这是 partial coupling 下的 gradient interference，但未提供证据。这意味着论文的核心分析框架（signal type vs coupling scope decomposition）在高稀疏度下不适用，但 abstract 和 conclusion 仍使用来自 30% 实验的分解结果做出 general claims。\n- 建议：在 abstract/conclusion 中明确限定 decomposition 结论的适用范围（\"at moderate sparsity\"），或提供 50% 下的替代分析。\n\n**W2** [warning] 无 wall-clock 加速，6.4% latency overhead\n\n- 具体位置：Appendix A、§1 Introduction (sentence 8)\n- 问题：论文诚实地披露了这一点（appreciated），但这意味着目前的方法在实际部署中不仅没有加速，反而增加了 6.4% 延迟。Without sparse kernel support, the predictor is purely an analytical tool, not a practical system contribution. 这对一篇投稿到 NLP 会议（而非系统会议）的论文是可以接受的，但对实用影响的声明需要相应弱化。\n- 建议：这已在论文中处理得相当好。可在 Conclusion 中更明确地说明 \"实际加速取决于未来稀疏核的支持\" 而非仅在 appendix 中提及。\n\n**W3** [warning] 缺少生成质量评估\n\n- 具体位置：Limitations (acknowledged)\n- 问题：评估仅涵盖 PPL 和 multiple-choice benchmarks。Open-ended generation (MT-Bench, AlpacaEval) 在 sparsity 下的表现可能与 PPL/选择题结果不一致。特别是论文发现 KL 的 mode-covering 特性在 commonsense 上优势但知识任务退化——这对生成质量可能有不同的影响模式。\n- 建议：这已在 Limitations 中提及。若能增加 MT-Bench 或 AlpacaEval 的结果将显著增强论文的完整性。\n\n**W4** [warning] Introduction 中 \"19%\" PPL 减少数字有误\n\n- 具体位置：§4.1, Introduction ¶13\n- 问题：Introduction 声称 \"reducing TEAL's perplexity by 19% (10.82 → 8.81)\"。实际计算：(10.82 - 8.81) / 10.82 = 18.58%，约 18.6%，而非 19%。Abstract 正确使用了 matched-sparsity 的 14.5%。这种不精确虽小，但在审稿人 verify 数字时会引发信任问题。\n- 建议：修正为 18.6% 或 ~19%，并注明此为 nominal sparsity 下的比较（actual sparsity 分别为 28.5% vs 29.3%）。\n\n**W5** [warning] MSE baseline 在 50% sparsity 下的可靠性\n\n- 具体位置：Appendix G (MSE Baseline Configuration)、Table 4\n- 问题：MSE baseline 在 50% sparsity 下，seed 123 catastrophic failure (PPL=15,789, 仅 5.1% 实际稀疏度)。因此 Table 4 中 MSE 50% 的 229.26 实际仅来自 seed 42（标注 §），而非 3-seed 平均。这使得 MSE 在高稀疏度下的比较不可靠，但论文在 §3.7 中仍使用 MSE 50% 结果（\"1.7×/9.6× worse PPL\"）来论证 taxonomy 的预测力。\n- 建议：正文中使用 MSE 50% 结果时应明确注明 single-seed caveat，并讨论这种 instability 是否反映了 MSE loss 本身的问题还是实现细节。\n\n**W6** [warning] C1 ablation 中 seed 42 oracle provenance 问题\n\n- 具体位置：Table 3 footnote、Appendix P\n- 问题：C1 ablation 的 s42 oracle 来自 \"earlier training run\"，而 s123/s456 使用 matched retrained oracles。s42 的 PPL gap (0.65pp at 30%) 显著大于 s123/s456 (≤0.03pp)。虽然论文在 footnote 中披露了这一点，但 s42 是唯一有 50% 数据的 seed，使得 50% 的 C1 结论基于可能有 confound 的单 seed。\n- 建议：提供 s123 或 s456 在 50% sparsity 下的 C1 结果以增强稳健性，或明确说明 50% 的 C1 结论仅基于 s42。\n\n---\n\n## 小问题（不影响接收）\n\n- **Table 2 比较不对齐**：BCE 30% 使用 TEAL global 分配（标注 †），而 KL 30% 使用 uniform 分配，使直接比较不公平。建议在同一 allocation 下展示 BCE 结果，或在 caption 中更醒目地标注。\n- **Abstract 信息密度偏高**：9 句 abstract 涵盖了 problem、method、主结果、C1 ablation、signal type claim、coupling scope claim、cross-arch、disclaimer——信息量极大，但对首次阅读的读者来说可能太密集。考虑将 abstract 压缩至 6-7 句，将 C1 和 decomposition 细节移至正文。\n- **Conclusion 过于简洁**：仅 4 句话，缺少对 future work 方向的讨论（如 task-aware allocation, diverse training data, sparse kernel integration）。\n- **术语一致性**：\"output-distribution alignment\"、\"output-distribution distillation\"、\"output-distribution objective\" 在全文中交替使用，建议统一。\n- **Figure 2 caption 的 14.5%**：此处使用 matched-sparsity 的 14.5%，而 §4.1 正文使用 nominal 的 \"19%\"（实为 18.6%），两处使用不同基准但未解释，可能造成困惑。\n- **GPU 型号**：\"NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96GB)\" 是非常具体的新硬件（2025 年发布），虽然不直接暴露身份，但在 double-blind 审稿中需注意——拥有该 GPU 的实验室相对较少。\n\n---\n\n## Missing References\n\n本文的 related work 覆盖面相当完善（50+ 引用），涵盖了 training-free、predictor-based、activation function engineering、weight pruning、KL distillation、MoE routing 等主要方向。以下为可能的补充：\n\n- **TurboSparse-Mistral**（Song et al., 2025）：虽已引用 TurboSparse，但该系列后续工作包括特定模型适配，可能值得更新引用。\n- 论文未引用 **Mixtral-of-Experts** 相关的稀疏激活工作，虽然 MoE 与 activation sparsity 有本质区别，但部分读者可能期望看到更明确的区分说明。\n- 建议补充检索 2026 年 1-5 月是否有新的 **KL distillation for activation sparsity** 的工作（如 SVD-CSP 已引用，但该方向可能有更多新进展）。\n\n总体上，missing references 不构成重大问题。\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：3-seed 评估、cross-architecture 验证（3 个模型）、matched-sparsity 比较、多达 18 个 appendix sections 的补充实验。这在同类工作中是高标准。\n2. **C1 target-swap ablation 设计巧妙**：通过将 KL 发现的 mask 模式转移给 BCE 训练，干净地分离了 \"mask pattern quality\" 和 \"gradient coupling mechanism\" 的贡献。这是一个有 insight 的实验设计。\n3. **诚实的 limitations 披露**：论文自始至终坦诚地报告了知识任务退化、无 wall-clock 加速、评估限制等。这增强了结果的可信度。\n4. **Per-layer KL decomposition**：K=1 和 K=4 控制实验合理地（虽然不完美地）分解了 signal type 和 coupling scope 的贡献，并发现了有趣的 task-dependent dissociation。\n5. **写作质量**：Claims 有适当的 hedging（\"upper bound\"、\"suggests\"、\"primarily empirical\"），数字引用有 exp_id 追踪。\n6. **Compensation redundancy finding**：发现 KL predictor 使得额外的 67.2M 参数补偿网络冗余，简化了推理管线。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5 |\n| Excitement | 3 |\n| Overall Assessment | 3.5 |\n| Reviewer Confidence | 4 |\n| Reproducibility | 4 |",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-23T00:42:22.365317+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Tool call

_source line 1738 · 2026-05-23T00:42:28.048095+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1739 · 2026-05-23T00:42:28.098713+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-23T00:42:31.711609+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_22/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-23T00:42:31.762263+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1742 · 2026-05-23T00:42:42.518603+00:00_

审稿意见已提交给 Review Director。

总结：Overall 3.5（Borderline Conference）。两个 Must-Fix：(1) 知识任务系统性退化仅有假设无控制实验验证；(2) 方法新颖性边界需更清晰论证（KL+Gumbel 均为成熟技术，核心是应用到新场景）。六个 Should-Fix 包括 per-layer decomposition 在 50% 下失效、无 wall-clock 加速、缺少生成评估、Introduction "19%" 数字不准确、MSE baseline 50% 仅单 seed、C1 ablation 的 s42 oracle provenance 问题。主要优势是实验设计严谨（3-seed, 3 architectures, 18 appendix sections）、C1 target-swap ablation 设计巧妙、limitations 披露诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 43

## Round 43

4 recorded events


### User

_source line 1743 · 2026-05-23T00:43:10.436637+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.5 (Borderline Conference), Soundness 3.5, Excitement 3, Confidence 4

### Must-Fix 问题

**N1** [critical] Per-layer KL K=4 在 50% sparsity 的反常行为削弱 coupling decomposition 的可信度
- K=4 per-layer KL 在 50% sparsity 的 PPL 为 44.23，劣于 K=1 的 34.85，而 E2E KL 为 11.84。如果 coupling 是有益的，增加 masked layers 数量（K=1→K=4）应缩小与 E2E 的差距，但实际上差距扩大了。论文给出的解释是 "gradient interference"，但纯粹是 speculation。
- 建议：(1) 增加 K=2, K=8, K=16 实验；(2) 或限制 decomposition 分析仅在 30% 下声称有效；(3) 分析 K=4 at 50% 的 per-layer sparsity 分布。

**N2** [critical] MMLU K=4 超过 E2E 的 anomaly 暴露 decomposition confound
- K=4 在 MMLU 上系统性超过 E2E（所有 3 个 seed），论文解释为 K=4 的 near-uniform per-layer sparsity（std=0.003）匹配了 uniform inference protocol。但这说明 K=4 control 无法独立地隔离 coupling 效应——它同时改变了 allocation pattern。
- 建议：(1) 在 main text 中明确讨论 allocation confound；(2) 考虑在 K=4 实验中强制使用与 E2E 相同的 per-layer allocation pattern。

**N3** [critical] Qwen-2.5-14B 的 GSM8K -20pp regression 仅有单 seed 支撑
- GSM8K 从 52.1pp（TEAL）下降到 32.0pp（KL），降幅达 20pp，且标准差为 5.2pp。Global allocation 行仅有 seed 42。
- 建议：补充 Qwen-14B 至少 3-seed 评估，或弱化跨规模趋势的措辞。

### Should-Fix 问题

**W1** 系统性 knowledge-task regression 缺乏机制分析（仅假设无验证）
**W2** C1 ablation s42 oracle 来自不同 checkpoint（s42 gap 0.65pp vs s123/s456 ≤0.03pp）
**W3** BCE 30% 仅报告 global allocation，缺少 uniform 对比
**W4** Sparsity controller 在 30% target 饱和（λ=5000 cap, actual 28.5%）
**W5** 无 wall-clock speedup 限制实际影响

### 小问题
- §4.2 "19%" 实际为 18.6%
- Eq. 3 s_j 缺少层标 ℓ
- §3.4 T 和 τ 可能让读者困惑
- Table 4 STE 30% 在不同 actual sparsity 下对比
- Limitations 未提及 14B regression 加剧对 70B+ 前景的影响

### 主要优势
1. C1 target-swap ablation 设计巧妙
2. 实验控制严格（KL/BCE/MSE 同架构同数据同 optimizer）
3. 诚实的 limitations
4. 丰富的 appendix
5. 2D taxonomy 有用
6. 3-seed 评估 PPL σ=0.02

### Questions
Q1: K=4 at 50% 为什么比 K=1 差？有 K=2, K=8 数据吗？
Q2: K=4 中强制使用 E2E 的 per-layer allocation，MMLU anomaly 是否消失？
Q3: 是否尝试过在 GSM8K/math 数据上训练 predictor？
Q4: BCE 30% 为什么缺少 uniform allocation 数据？
Q5: remove-valley 中，是否存在同时改善 MMLU 和 ARC-c 的 allocation？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-23T00:44:58.194810+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: K=4 在 50% sparsity 的反常行为削弱 decomposition 可信度**\n\n同意这是一个实质性问题。我在自己的 W1 中也指出了这一点。论文的 \"gradient interference\" 解释确实是 speculation（§4.5: \"We hypothesize that partial coupling (K=4 of 32 layers) under tight capacity amplifies gradient interference\"），没有任何实验证据支撑。\n\n补充观察：这个反常不仅影响可信度，还从根本上限制了 decomposition 框架的 generality——论文的分析核心贡献之一（signal type vs coupling scope decomposition）在高稀疏度下不可用。论文 abstract 和 conclusion 中的 general claims（\"signal type accounts for the majority of the PPL gap\"）实际上只在 30% sparsity 下有证据支持。\n\nR1 建议的 K=2, K=8, K=16 梯度实验很好，能帮助区分 \"K 增加后性能单调改善\"（支持 coupling 有益）vs \"存在最优 K\"（支持 gradient interference）。\n\n**[AGREE] R1-N2: MMLU K=4 anomaly 暴露 allocation confound**\n\n同意。K=4 训练产生 near-uniform per-layer sparsity (std=0.003)，而 E2E KL 产生非均匀分配（L14-L18 valley, L22-L28 aggressive pruning，见 Appendix U Table 21）。因此 K=4 vs E2E 的差异同时反映了 coupling scope 和 allocation pattern 两个变量的变化，无法独立归因。\n\n论文在 Appendix T footnote 和 Appendix S 的 constraint analysis 中已隐式承认了这一点——remove-valley 条件下 MMLU=44.0%，与 K=4 的 42.7% 接近——但这一 confound 仅在 appendix 中讨论，在正文 §4.5 的 decomposition 叙事中未充分体现。\n\nR1 建议的 \"强制 K=4 使用 E2E 的 per-layer allocation\" 在技术上是可行的（推理时 override per-layer budget），这将是一个更干净的控制实验。\n\n**[PARTIALLY REBUT] R1-N3: Qwen-14B GSM8K -20pp 仅单 seed 支撑**\n\n部分反驳。R1 声称 \"-20pp regression 仅有单 seed 支撑\"，但根据 Appendix K Table 14，uniform allocation 行的 KL 结果标注为 32.0±5.2，表明这是 3-seed 结果（尽管高方差 std=5.2pp）。TEAL 是 deterministic 无需多 seed。因此 -20pp 的 gap（52.1 vs 32.0）是 3-seed KL 与 deterministic TEAL 的比较，并非单 seed。\n\n不过，R1 的担忧仍有部分道理：\n1. Global allocation 行确实仅为 seed 42（KL 48.82 vs TEAL 49.51，几乎无差异）\n2. Uniform allocation 的 std=5.2pp 极高（CV=16.3%），95% CI 约为 ±10pp\n3. 3 个 seed 的统计力较弱\n\n因此，虽然 -20pp 非单 seed，但其可靠性确实受限于高方差和少量 seed。建议论文在引用此数字时使用完整的 \"32.0±5.2 vs 52.1\" 而非仅 \"-20pp\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Knowledge-task regression 缺乏机制分析**\n\n完全同意，我将此列为自己的 N1（Must-Fix）。这是两位 reviewer 共同指出的问题，权重应加大。论文在 Appendix S 中已有 remove-valley constraint analysis 证明 allocation redistribution 能恢复 MMLU +3.4pp / GSM8K +1.6pp，这一发现应在正文中更突出地呈现，并启发进一步的控制实验（如在 math-heavy 数据上训练 predictor）。\n\n**[AGREE] R1-W2: C1 s42 oracle provenance 问题**\n\n同意。我在 W6 中也指出了这一点。s42 的 0.65pp gap 与 s123/s456 的 ≤0.03pp gap 差异显著。50% sparsity 的 C1 结论仅基于 s42，增加了 confound 风险。\n\n**[AGREE] R1-W3: BCE 30% 缺少 uniform allocation 对比**\n\n同意。Table 2 中 BCE 30% 使用 TEAL global（标注 †），而 KL 30% 使用 uniform，使读者难以直接比较。我在自己的 minor issues 中也提到了这一点。\n\n**[PARTIALLY REBUT] R1-W4: Sparsity controller 在 30% 饱和**\n\n部分反驳。论文在 Appendix C 已充分 address 了这一问题：\n\n1. 实际稀疏度 28.5%（偏差 5%），但论文提供了 matched-sparsity 比较——KL at 28.5% vs TEAL at 28.5% (PPL 10.30)，gap 为 14.5%（§4.1 和 Figure 2 caption）\n2. Appendix C 明确指出 \"This does not affect conclusions: TEAL at 28.5% actual sparsity yields PPL 10.30 (vs. 10.97 at exact 30%), a 0.67 PPL difference negligible relative to the KL vs. TEAL gap\"\n3. 对于方法论而言，Lagrangian 控制器的饱和是一个工程问题（可通过调高 λ_max 或使用更激进的 schedule 来解决），不影响核心发现\n\n不过 R1 的 concern 有一定道理：如果 KL predictor 在 30% target 下只能达到 28.5%，这意味着方法在精确稀疏度控制上有局限性。建议论文在正文（而非仅 appendix）中讨论这一 deviation。\n\n**[AGREE] R1-W5: 无 wall-clock speedup**\n\n同意。我在 W2 中也指出了这一点。论文的诚实披露值得肯定，但这确实限制了实用影响。\n\n---\n\n### 小问题\n\n**[AGREE] 19% → 18.6%**：我也在 W4 中指出了这一数值不精确。(10.82-8.81)/10.82 = 18.58%，四舍五入到 19% 偏激进。\n\n**[AGREE] Eq. 4 s_j 缺少层标 ℓ**：确认 §3.3 Eq. 4 中 s_j 和 m̃_j 均缺少 ℓ 上标，而 §3.1 中 s^(ℓ) 有层标。应保持一致。\n\n**[AGREE] T 和 τ 可能混淆**：§3.4 最后一句 \"No temperature scaling (T=1) is applied (Hinton, 2015)\" 中的 T 指 distillation temperature，与 Gumbel-Sigmoid 的 τ 不同。建议明确区分或使用不同符号。\n\n**[AGREE] Table 4 STE 30% 比较不公平**：STE 在 30% target 下仅达到 20.8% actual sparsity（标注 ‡），与其他方法在不同实际稀疏度下比较，应标注更醒目或提供 matched-sparsity 结果。\n\n**[AGREE] Limitations 未提 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K: -1.3pp at 8B → -20pp at 14B），但 Limitations 未讨论这对 70B+ 的前景意味着什么。这是一个合理的补充建议。\n\n---\n\n### Questions 回应\n\n**Q1 (K=2, K=8 data)**：同意这些实验有价值。若 K 与 PPL 的关系呈 U 形（K=1 best among per-layer, K=4 worse, E2E best），支持 gradient interference 假设；若单调改善，支持 coupling 有益。\n\n**Q2 (K=4 forced allocation)**：好的实验建议。在推理时用 E2E KL 的 per-layer budget 覆盖 K=4 predictor 的 near-uniform pattern，可隔离 allocation confound vs coupling 效应。\n\n**Q3 (Math training data)**：与我的 N1 一致。在 GSM8K 或数学文本上训练 predictor 是测试知识退化是否源于训练数据偏差的直接方法。\n\n**Q4 (BCE 30% uniform)**：合理的问题。缺少 BCE 30% uniform 使 Table 2 的比较不对称。可能是 BCE 在 uniform allocation 下表现更差，作者选择了 BCE 最优的配置（global），但这应该被解释。\n\n**Q5 (Remove-valley compromise)**：好问题。Appendix S 的 remove-valley 提升了 MMLU +3.4pp 和 GSM8K +1.6pp 但 ARC-c -1.5pp。是否存在 Pareto-optimal 的中间方案（如部分缩窄 valley 而非完全移除）值得探索，但可能超出本文范围。\n\n---\n\n### 总结\n\n我与 R1 在核心评估上高度一致：论文实验设计严谨，C1 ablation 和 decomposition 分析有价值，但 (1) 技术新颖性有限，(2) decomposition 框架在 50% 下失效且有 allocation confound，(3) 知识任务退化缺乏机制调查。\n\n两位 reviewer 共同认可的优势：实验控制质量、诚实的 limitations、C1 ablation 设计。\n两位 reviewer 共同的 concerns：decomposition 的可信度（K=4 anomaly）、knowledge regression（unverified hypotheses）、无 speedup。\n\n我维持 **Overall 3.5 (Borderline Conference)** 评分。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: K=4 在 50% sparsity 的反常行为削弱 decomposition 可信度**\n\n同意这是一个实质性问题。我在自己的 W1 中也指出了这一点。论文的 \"gradient interference\" 解释确实是 speculation（§4.5: \"We hypothesize that partial coupling (K=4 of 32 layers) under tight capacity amplifies gradient interference\"），没有任何实验证据支撑。\n\n补充观察：这个反常不仅影响可信度，还从根本上限制了 decomposition 框架的 generality——论文的分析核心贡献之一（signal type vs coupling scope decomposition）在高稀疏度下不可用。论文 abstract 和 conclusion 中的 general claims（\"signal type accounts for the majority of the PPL gap\"）实际上只在 30% sparsity 下有证据支持。\n\nR1 建议的 K=2, K=8, K=16 梯度实验很好，能帮助区分 \"K 增加后性能单调改善\"（支持 coupling 有益）vs \"存在最优 K\"（支持 gradient interference）。\n\n**[AGREE] R1-N2: MMLU K=4 anomaly 暴露 allocation confound**\n\n同意。K=4 训练产生 near-uniform per-layer sparsity (std=0.003)，而 E2E KL 产生非均匀分配（L14-L18 valley, L22-L28 aggressive pruning，见 Appendix U Table 21）。因此 K=4 vs E2E 的差异同时反映了 coupling scope 和 allocation pattern 两个变量的变化，无法独立归因。\n\n论文在 Appendix T footnote 和 Appendix S 的 constraint analysis 中已隐式承认了这一点——remove-valley 条件下 MMLU=44.0%，与 K=4 的 42.7% 接近——但这一 confound 仅在 appendix 中讨论，在正文 §4.5 的 decomposition 叙事中未充分体现。\n\nR1 建议的 \"强制 K=4 使用 E2E 的 per-layer allocation\" 在技术上是可行的（推理时 override per-layer budget），这将是一个更干净的控制实验。\n\n**[PARTIALLY REBUT] R1-N3: Qwen-14B GSM8K -20pp 仅单 seed 支撑**\n\n部分反驳。R1 声称 \"-20pp regression 仅有单 seed 支撑\"，但根据 Appendix K Table 14，uniform allocation 行的 KL 结果标注为 32.0±5.2，表明这是 3-seed 结果（尽管高方差 std=5.2pp）。TEAL 是 deterministic 无需多 seed。因此 -20pp 的 gap（52.1 vs 32.0）是 3-seed KL 与 deterministic TEAL 的比较，并非单 seed。\n\n不过，R1 的担忧仍有部分道理：\n1. Global allocation 行确实仅为 seed 42（KL 48.82 vs TEAL 49.51，几乎无差异）\n2. Uniform allocation 的 std=5.2pp 极高（CV=16.3%），95% CI 约为 ±10pp\n3. 3 个 seed 的统计力较弱\n\n因此，虽然 -20pp 非单 seed，但其可靠性确实受限于高方差和少量 seed。建议论文在引用此数字时使用完整的 \"32.0±5.2 vs 52.1\" 而非仅 \"-20pp\"。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Knowledge-task regression 缺乏机制分析**\n\n完全同意，我将此列为自己的 N1（Must-Fix）。这是两位 reviewer 共同指出的问题，权重应加大。论文在 Appendix S 中已有 remove-valley constraint analysis 证明 allocation redistribution 能恢复 MMLU +3.4pp / GSM8K +1.6pp，这一发现应在正文中更突出地呈现，并启发进一步的控制实验（如在 math-heavy 数据上训练 predictor）。\n\n**[AGREE] R1-W2: C1 s42 oracle provenance 问题**\n\n同意。我在 W6 中也指出了这一点。s42 的 0.65pp gap 与 s123/s456 的 ≤0.03pp gap 差异显著。50% sparsity 的 C1 结论仅基于 s42，增加了 confound 风险。\n\n**[AGREE] R1-W3: BCE 30% 缺少 uniform allocation 对比**\n\n同意。Table 2 中 BCE 30% 使用 TEAL global（标注 †），而 KL 30% 使用 uniform，使读者难以直接比较。我在自己的 minor issues 中也提到了这一点。\n\n**[PARTIALLY REBUT] R1-W4: Sparsity controller 在 30% 饱和**\n\n部分反驳。论文在 Appendix C 已充分 address 了这一问题：\n\n1. 实际稀疏度 28.5%（偏差 5%），但论文提供了 matched-sparsity 比较——KL at 28.5% vs TEAL at 28.5% (PPL 10.30)，gap 为 14.5%（§4.1 和 Figure 2 caption）\n2. Appendix C 明确指出 \"This does not affect conclusions: TEAL at 28.5% actual sparsity yields PPL 10.30 (vs. 10.97 at exact 30%), a 0.67 PPL difference negligible relative to the KL vs. TEAL gap\"\n3. 对于方法论而言，Lagrangian 控制器的饱和是一个工程问题（可通过调高 λ_max 或使用更激进的 schedule 来解决），不影响核心发现\n\n不过 R1 的 concern 有一定道理：如果 KL predictor 在 30% target 下只能达到 28.5%，这意味着方法在精确稀疏度控制上有局限性。建议论文在正文（而非仅 appendix）中讨论这一 deviation。\n\n**[AGREE] R1-W5: 无 wall-clock speedup**\n\n同意。我在 W2 中也指出了这一点。论文的诚实披露值得肯定，但这确实限制了实用影响。\n\n---\n\n### 小问题\n\n**[AGREE] 19% → 18.6%**：我也在 W4 中指出了这一数值不精确。(10.82-8.81)/10.82 = 18.58%，四舍五入到 19% 偏激进。\n\n**[AGREE] Eq. 4 s_j 缺少层标 ℓ**：确认 §3.3 Eq. 4 中 s_j 和 m̃_j 均缺少 ℓ 上标，而 §3.1 中 s^(ℓ) 有层标。应保持一致。\n\n**[AGREE] T 和 τ 可能混淆**：§3.4 最后一句 \"No temperature scaling (T=1) is applied (Hinton, 2015)\" 中的 T 指 distillation temperature，与 Gumbel-Sigmoid 的 τ 不同。建议明确区分或使用不同符号。\n\n**[AGREE] Table 4 STE 30% 比较不公平**：STE 在 30% target 下仅达到 20.8% actual sparsity（标注 ‡），与其他方法在不同实际稀疏度下比较，应标注更醒目或提供 matched-sparsity 结果。\n\n**[AGREE] Limitations 未提 14B regression 对更大规模的影响**：8B→14B regression 加剧（GSM8K: -1.3pp at 8B → -20pp at 14B），但 Limitations 未讨论这对 70B+ 的前景意味着什么。这是一个合理的补充建议。\n\n---\n\n### Questions 回应\n\n**Q1 (K=2, K=8 data)**：同意这些实验有价值。若 K 与 PPL 的关系呈 U 形（K=1 best among per-layer, K=4 worse, E2E best），支持 gradient interference 假设；若单调改善，支持 coupling 有益。\n\n**Q2 (K=4 forced allocation)**：好的实验建议。在推理时用 E2E KL 的 per-layer budget 覆盖 K=4 predictor 的 near-uniform pattern，可隔离 allocation confound vs coupling 效应。\n\n**Q3 (Math training data)**：与我的 N1 一致。在 GSM8K 或数学文本上训练 predictor 是测试知识退化是否源于训练数据偏差的直接方法。\n\n**Q4 (BCE 30% uniform)**：合理的问题。缺少 BCE 30% uniform 使 Table 2 的比较不对称。可能是 BCE 在 uniform allocation 下表现更差，作者选择了 BCE 最优的配置（global），但这应该被解释。\n\n**Q5 (Remove-valley compromise)**：好问题。Appendix S 的 remove-valley 提升了 MMLU +3.4pp 和 GSM8K +1.6pp 但 ARC-c -1.5pp。是否存在 Pareto-optimal 的中间方案（如部分缩窄 valley 而非完全移除）值得探索，但可能超出本文范围。\n\n---\n\n### 总结\n\n我与 R1 在核心评估上高度一致：论文实验设计严谨，C1 ablation 和 decomposition 分析有价值，但 (1) 技术新颖性有限，(2) decomposition 框架在 50% 下失效且有 allocation confound，(3) 知识任务退化缺乏机制调查。\n\n两位 reviewer 共同认可的优势：实验控制质量、诚实的 limitations、C1 ablation 设计。\n两位 reviewer 共同的 concerns：decomposition 的可信度（K=4 anomaly）、knowledge regression（unverified hypotheses）、无 speedup。\n\n我维持 **Overall 3.5 (Borderline Conference)** 评分。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1745 · 2026-05-23T00:45:01.756831+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---


### Assistant

_source line 1746 · 2026-05-23T00:45:08.966498+00:00_

交叉回应已提交给 Review Director。

总结：与 R1 在大部分核心评估上一致。对 R1-N3（Qwen-14B GSM8K 单 seed）做了 partial rebut——该数据实为 3-seed 但高方差。对 R1-W4（sparsity controller 饱和）做了 partial rebut——论文已在 Appendix C 提供了 matched-sparsity 对比。其余 Must-Fix 和 Should-Fix 均同意。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 44

## Round 44

86 recorded events


### User

_source line 1747 · 2026-05-23T01:28:39.633257+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性**的审查。

## Venue 信息
- **目标会议**：EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
- **截止日期**：2026-05-25
- **正文页数限制**：8 页（ACL 模板）
- **匿名规则**：Double-blind
- **附录**：允许，审稿人可选择性参考

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf`

## 审查侧重

请重点审查以下方面，对每个方面给出具体发现：

### 1. 新颖性与贡献边界
- 核心组件（KL divergence + Gumbel-Sigmoid + predictor MLP）均为成熟技术——论文是否充分承认了这一点？
- 与 MaskLLM（同样使用 KL + Gumbel + frozen weights + learnable masks）的区分是否有说服力？
- 论文自定位为 "empirical study"——其 empirical 贡献（C1 ablation, signal-type/coupling decomposition）的新颖性是否足以达到 EMNLP 录取标准？
- Contribution list 的排序和措辞是否准确反映实际贡献？

### 2. 叙事框架与声明范围
- Abstract/Introduction/Conclusion 中的核心声明是否有充分实验支撑？特别是关于 "primary design dimension" 的声明
- signal type vs coupling scope 的分解声明是否限定在了适用范围内（30% moderate sparsity）？
- MMLU/GSM8K 退步在正文中的讨论是否到位？是否被轻描淡写？
- 论文的 framing 是否会给读者造成误导性印象（如暗示方法可用于实际加速）？

### 3. Related Work 覆盖与定位
- 是否遗漏了 2025-2026 年的重要相关工作？
- Taxonomy（Table 1）的分类框架是否合理？是否有应纳入但缺失的方法？
- 与 DejaVu, FastForward, ShadowLLM, D2D-MoE 的比较讨论是否公平？
- 引用格式和完整性

### 4. 写作质量与术语一致性
- 术语使用是否一致（output-distribution alignment / KL distillation / output-distribution objective）？
- 数值准确性（如 Introduction 中的百分比是否与实验数据一致）
- 表格标注是否清晰（Table 2 的 †, ‡, * 等）
- 论文整体可读性和叙事流畅度

### 5. 格式与合规性
- 8 页限制是否满足？
- 匿名性是否完整（无自引泄露）？
- Limitations 和 Ethics 章节是否符合 EMNLP 2026 要求？
- 参考文献格式是否一致（ACL natbib）？

请给出结构化审稿意见：Strengths（逐条）、Weaknesses（逐条，标注 Must-Fix / Should-Fix / Minor）、Questions、Missing References。最后给出 Overall Assessment 评分（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）和置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1748 · 2026-05-23T01:28:49.347071+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1749 · 2026-05-23T01:28:49.347412+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-23T01:28:51.841856+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1751 · 2026-05-23T01:28:53.797738+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1752 · 2026-05-23T01:28:58.583349+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form criteria, and related information:

## Reviewer Guidelines

Reviewers should follow a workflow of reading the paper, getting a first impression, and searching for related work. If reviewers feel qualified to review only some aspects of the paper, they should state in the review if they did not check major parts, such as proofs.

Reviewers should check for academic conflicts of interest and recuse themselves if the s
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6741
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-23T01:29:01.383395+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.4}], \"total_pages\": 19, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7585
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-23T01:29:07.310248+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions (e.g. soundness, excitement, overall assessment), their scales, and descriptions. List every field a reviewer must fill in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions (e.g. soundness, excitement, overall assessment), their scales, and descriptions. List every field a reviewer must fill in."
  }
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-23T01:29:07.712238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1756 · 2026-05-23T01:29:08.669974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1757 · 2026-05-23T01:29:08.871193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1758 · 2026-05-23T01:29:09.223112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-23T01:29:09.627866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-23T01:29:09.628328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-23T01:29:10.434268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1211
}
```

</details>

---


### Tool result

_source line 1762 · 2026-05-23T01:29:10.635856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-23T01:29:14.953118+00:00_

# ACL Rolling Review Form - Complete Criteria and Fields

## Required Text Fields

1. **Paper Summary** - Describe the paper's topic and content
2. **Summary of Strengths** - Major reasons for publication at selective *ACL venues
3. **Summary of Weaknesses** - Concerns prioritizing other papers; numbered format encouraged
4. **Comments/Suggestions/Typos** - Additional improvement suggestions

## Scoring Dimensions

### Reviewer Confidence (1-5 scale)
- 5: Positive evaluation; carefully read with familiar background
- 4: Quite sure; important points checked
- 3: Pretty sure; general area knowledge but incomplete detail checking
- 2: Willing to defend but details possibly missed
- 1: Outside expertise area or incomprehensible paper

### Soundness (1-5 scale with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong support; minor experiments optional
- 3: Acceptable; main claims supported
- 2: Poor; insufficient support for major claims
- 1: "Major Issues: This study is not yet sufficiently thorough"

### Excitement (1-5 scale with .5 increments)
- 5: Highly Exciting; would recommend to others
- 4: Exciting; would mention to others
- 3: Interesting; might mention selectively
- 2: Potentially Interesting; limited resonance
- 1: Not Exciting; no broader community appeal

### Overall Assessment (1-5 scale with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Additional Fields

5. **Best Paper Justification** - Required if scoring 5 or 4.5 on Overall Assessment
6. **Limitations and Societal Impact** - Evaluation of author discussion on limitations and impacts
7. **Ethical Concerns** - Assessment against ACL code of ethics
8. **Needs Ethics Review** - Determination if specialized ethics committee review needed
9. **Repr
…[truncated 354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7642
}
```

</details>

---


### Tool call

_source line 1764 · 2026-05-23T01:29:21.184823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1765 · 2026-05-23T01:29:21.838238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1766 · 2026-05-23T01:29:22.190893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-23T01:29:22.293254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-23T01:29:23.599449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1761
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-23T01:29:23.600188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-23T01:29:23.652202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-23T01:29:24.610839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-23T01:29:24.611308+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "9-19"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "9-19"
  }
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-23T01:29:26.070261+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.0}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 589.9}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png\", \"wid
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-23T01:29:29.994249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1775 · 2026-05-23T01:29:30.948935+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1776 · 2026-05-23T01:29:31.400355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 1777 · 2026-05-23T01:29:31.603326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-23T01:29:31.855563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-23T01:29:32.561911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool call

_source line 1780 · 2026-05-23T01:29:32.562324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-23T01:29:33.319649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1716
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-23T01:29:33.675201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-23T01:29:33.726584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1871
}
```

</details>

---


### Tool result

_source line 1784 · 2026-05-23T01:29:34.534333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1972
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-23T01:29:35.240117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1564
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-23T01:29:39.713546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1787 · 2026-05-23T01:29:40.215490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1788 · 2026-05-23T01:29:41.170635+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-23T01:29:41.171345+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-23T01:29:41.322027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1791 · 2026-05-23T01:29:41.674185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1792 · 2026-05-23T01:29:41.830154+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 508
}
```

</details>

---


### Tool call

_source line 1793 · 2026-05-23T01:29:42.031206+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_23/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-23T01:29:42.536324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-23T01:29:42.893241+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-23T01:29:49.323452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-23T01:29:49.374174+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-23T01:29:52.192743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-23T01:29:52.193135+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive decline; post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; not fully orthogonal with coupling scope).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-23T01:29:52.343832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-23T01:29:52.344495+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 3030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-23T01:29:57.695177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-23T01:29:57.695734+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-23T01:29:57.746210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-23T01:29:57.847294+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuro
…[truncated 9747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-23T01:30:01.778727+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-23T01:30:02.030179+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-23T01:30:05.541938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1809 · 2026-05-23T01:30:06.395182+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension for PPL at moderate sparsity (30\%; signal type accounts for the majority of the gap; upper bound); cross-layer coupling contributes task-dependently---substantially for commonsense, marginally for reasoning (3-seed $K{=}4$-corrected; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A predictor ($<$1\% of base) reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude, with commonsense gains but knowledge-task regression across scales.
6	Limitations: MMLU/GSM8K decline, no wall-clock speedup, evaluation bounded at 7--14B.
7	Code and trained predictors will be released upon acceptance.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-23T01:30:06.395639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1811 · 2026-05-23T01:30:06.546520+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. The aggravation from 8B to 14B (GSM8K regression deepening from $-$1.3pp to $-$20.1pp) raises concern about scaling to 70B+; wall-clock speedup via sparse kernels also remains future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-23T01:30:06.546972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-23T01:30:06.598209+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-23T01:30:11.366213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1815 · 2026-05-23T01:30:11.417073+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 3263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-23T01:30:19.428566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-23T01:30:19.429281+00:00_

100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Geometric Penalty Schedule Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the geometric penalty schedule across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Geometric penalty schedule convergence across sparsity targets (margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable wi
…[truncated 12697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-23T01:30:23.562165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "299",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-23T01:30:23.612892+00:00_

299	\label{app:comp_convergence}
300	
301	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
302	
303	
304	\section{Qwen-2.5-14B Detailed Results}
305	\label{app:14b}
306	
307	\begin{table}[h]
308	\centering
309	\caption{Qwen-2.5-14B at 30\% nominal sparsity. Actual sparsity differs: KL 29.6\% (3-seed), TEAL 29.3\% (target 30\%). \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
310	\label{tab:14b}
311	\small
312	\resizebox{\columnwidth}{!}{
313	\begin{tabular}{lcccccccc}
314	\toprule
315	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
316	\midrule
317	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\
318	\midrule
319	\multicolumn{8}{l}{\emph{Global top-$k$ allocation}} \\
320	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \textbf{75.01} & \textbf{77.37} \\ % exp_id: qwen14b_kl30_s42
321	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 & 70.51 & 74.70 \\ % exp_id: qwen14b_teal30_eval
322	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} & 53.43 & 68.28 \\ % exp_id: qwen14b_bce30_s42_eval
323	\midrule
324	\multicolumn{8}{l}{\emph{Uniform allocation}} \\
325	KL (Ours) & \textbf{7.90} & 53.50 & \textbf{72.82} & 63.55 & 32.0$\pm$5.2 & \textbf{72.68$\pm$0.2} & \textbf{76.01$\pm$1.1} \\ % exp_id: qwen14b_kl30_uniform (v3/v5 3-seed, HS/PIQA updated from v3
…[truncated 10811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-23T01:30:28.079364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "498",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-23T01:30:28.080009+00:00_

498	\section{Per-Layer KL Downstream Decomposition}
499	\label{app:perlayer_downstream}
500	
501	Table~\ref{tab:perlayer_downstream} reports raw downstream numbers for the signal type vs.\ coupling scope decomposition at 30\% sparsity (\S\ref{sec:perlayer}). BoolQ's $\approx$100\% coupling is an upper bound confounded by high cross-seed variance ($\pm$11.5pp for per-layer KL); the $K{=}4$ pilot (Table~\ref{tab:k4_downstream}) suggests much of this gap is train--inference mismatch.
502	
503	\begin{table}[h]
504	\centering
505	\caption{2D decomposition at 30\% sparsity (LLaMA-3.1-8B, uniform allocation). All rows are 3-seed mean$\pm$std. Signal type = per-layer KL $-$ MSE; coupling = E2E KL $-$ per-layer KL. Percentages are upper bounds (dimensions not fully orthogonal; see \S\ref{sec:perlayer}).}
506	\label{tab:perlayer_downstream}
507	\resizebox{\columnwidth}{!}{
508	\begin{tabular}{lcccccc}
509	\toprule
510	& PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & BoolQ \\
511	\midrule
512	E2E KL & 8.81$\pm$0.02 & 43.7 & 68.9 & 40.7 & 7.5 & 73.7 \\
513	Per-layer KL & 9.05$\pm$0.02 & 39.9 & 65.9 & 38.6 & 5.8 & 64.5 \\
514	MSE & 18.52$\pm$1.68 & 35.8$\pm$4.1 & 59.8$\pm$2.6 & 30.7$\pm$2.6 & 2.3$\pm$0.7 & 64.5$\pm$5.3 \\
515	\midrule
516	Total gap & 9.71 & 7.9 & 9.1 & 10.0 & 5.2 & 9.2 \\
517	Signal type (\%) & 97.5 & 51.9 & 67.0 & 79.0 & 67.3 & $\approx$0 \\
518	Coupling (\%) & 2.5 & 48.1 & 33.0 & 21.0 & 32.7 & $\approx$100 \\
519	\bottomrule
520	\end{tabular}}
521	\end{table}
522	
523	\section{$K{=}4$ Mismatch Control}
524	\label{app:k4_downstream}
525	
526	Table~\ref{tab:k4_downstream} reports 3-seed $K{=}4$ per-layer KL results at 30\% sparsity.
527	Training with $K{=}4$ random layers per step reduces the train--inference mismatch (4/32 vs.\ 1/32 layers masked during training, while inference applies all 32).
528	The gap closure column reports the fraction of the $K{=}1 \to$ E2E KL gap closed by $K{=}4$.
529	
530	\begin{table}[h]
531	\centering
532	\caption{3-seed $K{=}4$ mis
…[truncated 4109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1822 · 2026-05-23T01:30:35.004553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity prediction LLM SwiGLU 2025 2026 contextual sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity prediction LLM SwiGLU 2025 2026 contextual sparsity"
  }
}
```

</details>

---


### Tool call

_source line 1823 · 2026-05-23T01:30:35.205651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "knowledge distillation sparsity predictor large language model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "knowledge distillation sparsity predictor large language model 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 1824 · 2026-05-23T01:30:42.189173+00:00_

Web search results for query: "knowledge distillation sparsity predictor large language model 2025 2026"

Links: [{"title":"[2603.13765] Knowledge Distillation for Large Language Models","url":"https://arxiv.org/abs/2603.13765"},{"title":"Knowledge distillation and dataset distillation of large language models: emerging trends, challenges, and future directions - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12634706/"},{"title":"Preprint. A Survey of On-Policy Distillation for Large Language Models","url":"https://arxiv.org/pdf/2604.00626"},{"title":"Sparse Logit Sampling: Accelerating Knowledge Distillation in LLMs","url":"https://arxiv.org/pdf/2503.16870"},{"title":"Knowledge distillation and dataset distillation of large language models: emerging trends, challenges, and future directions - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/41278248/"},{"title":"[2504.14772] Knowledge Distillation and Dataset Distillation of Large Language Models: Emerging Trends, Challenges, and Future Directions","url":"https://arxiv.org/abs/2504.14772"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"Knowledge Distillation for Large Language Models","url":"https://arxiv.org/html/2603.13765v1"}]

Based on the search results, here are the relevant findings on knowledge distillation, sparsity predictors, and large language models from 2025-2026:

## Knowledge Distillation for LLMs

A resource-efficient framework for compressing large language models through knowledge distillation combined with guided chain-of-thought reinforcement learning has been proposed, demonstrating recent advances in this area. As of early 2026, self-distillation constitutes the largest and fastest-growing category in knowledge distillation research. Full-vocabulary logit distillation yields more stable gradients and more faithful knowledge transfer, with industrial implementations making this feasible even for very 
…[truncated 756 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6983
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-23T01:30:42.892993+00:00_

Web search results for query: "activation sparsity prediction LLM SwiGLU 2025 2026 contextual sparsity"

Links: [{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2603.12272"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"}]

I've successfully performed the web search on activation sparsity prediction for LLMs with SwiGLU and contextual sparsity. Here are the key findings from the search results:

## Key Recent Work (2025-2026)

Recent research on contextual sparsity predictors for LLM inference demonstrates up to a 1.8x reduction in end-to-end decoding time with an average activation sparsity level of 90% in FFNs while maintaining less than 1% degradation in benchmark scores.

## Contextual Sparsity Overview

A key characteristic of ReGLU-based LLMs is dynamic (or contextual) sparsity – the phenomenon where only a small subset of neurons within FFN blocks are activated for any given input. A prevalent approach for leveraging contextual sparsity involves employing lightweight, learnable sparsity predictors that generate input-specific sparse activation patterns prior to FFN forward passes.

## SwiGLU-Based Approaches

Recent work proposes CATS, achieving training-free activation sparsity on SwiGLU based LLMs by applying magnitude pruning on the output of Wgate, achieving up to 50% sparsity in Wup and Wdown for Mist
…[truncated 379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7888
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-23T01:30:45.905666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ActTail global activation sparsity LLM 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ActTail global activation sparsity LLM 2025 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 1827 · 2026-05-23T01:30:46.759004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MaskLLM learnable pruning mask LLM semi-structured sparsity Gumbel 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MaskLLM learnable pruning mask LLM semi-structured sparsity Gumbel 2024"
  }
}
```

</details>

---


### Tool result

_source line 1828 · 2026-05-23T01:30:52.061332+00:00_

Web search results for query: "MaskLLM learnable pruning mask LLM semi-structured sparsity Gumbel 2024"

Links: [{"title":"Paper page - MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://huggingface.co/papers/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Llu9nJal7b"},{"title":"MaskLLM","url":"https://vainf.github.io/maskllm-project-page/"},{"title":"[Quick Review] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://liner.com/review/maskllm-learnable-semistructured-sparsity-for-large-language-models"},{"title":"[2409.17481] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/abs/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2409.17481"},{"title":"NeurIPS Poster MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://neurips.cc/virtual/2024/poster/95573"},{"title":"MaskLLM: A Learnable AI Method that Facilitates End-to End Training of LLM Sparsity on Large-Scale Datasets - MarkTechPost","url":"https://www.marktechpost.com/2024/10/02/maskllm-a-learnable-ai-method-that-facilitates-end-to-end-training-of-llm-sparsity-on-large-scale-datasets/"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397199936_MaskLLM_Learnable_Semi-Structured_Sparsity_for_Large_Language_Models"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/html/2409.17481v1"}]

Based on the search results, here's what I found about MaskLLM:

## Overview

MaskLLM is a learnable pruning method that establishes semi-structured (N:M) sparsity in LLMs, aimed at reducing computational overhead during inference.

## Key Technical Approach

MaskLLM uses 
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5302
}
```

</details>

---


### Tool result

_source line 1829 · 2026-05-23T01:30:52.567000+00:00_

Web search results for query: "ActTail global activation sparsity LLM 2025 arxiv"

Links: [{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2603.12272"},{"title":"[2603.12272] ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2603.12272"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2603.12272"},{"title":"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity","url":"https://arxiv.org/html/2411.02335v2"},{"title":"[2412.12178] Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/abs/2412.12178"}]

I found the paper! Here's what the search results show about ActTail:

## Overview

Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement. 

## ActTail Method

ActTail is a TopK magnitude-based activation sparsity method with global activation sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. It captures heterogeneity via the heavy-tail exponent computed from each projection's empirical spectral density (ESD), which is used as a quantitative indicator to assign projection-specific sparsity budgets.

## Key Contribution

The main innovation addresses a limitation of existing methods: existing activation sparsity methods typically apply uniform sparsity across projections, ignoring the heterogeneous statistical properties of Transformer weights and thereby amplifying the performance degradation.

## Results

Experiments on LLaMA and Mistral models show that the method improves both perplexity and downstream task performance at high sparsity compared to uniform allocation. At 80% sparsity, perplexity is reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, and 9.4% on Mistral-7B.

The paper was published on arXiv (ID: 2603.12272) with a p
…[truncated 134 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6661
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-23T01:34:39.948168+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4 (Quite sure; important points checked, familiar with activation sparsity and KL distillation literature)\n**一句话总结**: 扎实的实证研究，将 KL distillation 首次系统应用于 contextual activation sparsity prediction，实验覆盖面广且诚实，但核心贡献（signal type vs coupling scope 分解）存在不可忽视的方法论混淆，加上缺乏实际加速和知识任务系统退步，限制了影响力。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主体实验设计合理，多 seed 评估值得肯定；但 signal type vs coupling scope 分解的 K=1 control 存在 train-inference mismatch 混淆，K=4 在 50% 失效；C1 ablation 有 soft-vs-hard confound |\n| Excitement | 2.5/5 | 将成熟组件（KL、Gumbel-Sigmoid、MLP predictor）应用于新场景，empirical findings 有参考价值但缺乏方法论创新或实际效率提升 |\n| Reproducibility | 4/5 | 训练细节充分（超参、硬件、seed），exp_id 标注便于追溯，承诺 release code/predictors；唯一不足是 oracle mask 提取的 trajectory 依赖性 |\n| Overall Assessment | 3.5/5 | Borderline Conference——实验深度足够 Findings，但核心分解 claim 的方法论问题和有限新颖性使 Conference 门槛有风险 |\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 系统且诚实的实证框架。** 论文从五种 loss 函数的对比出发，覆盖三种架构（LLaMA-3.1-8B、Mistral-7B-v0.3、Qwen-2.5-14B）、多个 sparsity 级别（25%–70%）和两种 allocation 策略。全程 3-seed 评估（PPL σ=0.02）、OOD 测试（C4）、cross-seed mask 一致性分析，实验可信度高。对 wall-clock speedup 缺失、MMLU/GSM8K 退步等 limitation 的主动披露体现了学术诚信（Abstract line 8, Limitations section）。\n\n**S2. C1 Target-Swap Ablation 设计巧妙。** 将 KL 发现的 mask pattern 提取后用标准 BCE 重新训练（Table 3），在 30% (≤1.70pp) 和 50% (≤0.79pp) 均接近 KL 性能，有力地证明了 mask target quality 而非 gradient coupling 是推理时质量的主要驱动力。这是一个有意义的实验设计。\n\n**S3. PPL 改进显著且跨架构一致。** KL predictor 在 30% sparsity 下 PPL 降低 14.5%（matched actual sparsity），50% 降低约 50%。该优势在 Mistral-7B 上一致复现（−17.3%, 3-seed, Table 16），PPL 层面的改进令人信服。\n\n**S4. Compensation 冗余性发现实用。** 证明 FastForward 风格的 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），可省去推理开销和额外参数，对实际部署有价值。\n\n**S5. 写作质量整体较高。** 叙事从问题定义到方法到实验的逻辑链清晰，Section 3.6 的 gradient analysis 提供了直觉，Related Work 的二维 taxonomy（Table 1）提供了有用的文献整理框架。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量\n\n- 具体位置：Section 4.4 (¶Per-Layer KL), Table 4, Abstract, Conclusion\n- 问题：分解的核心 claim 是\"signal type accounts for the majority of the PPL gap\"（Abstract line 5, Conclusion line 1）。但 K=1 per-layer KL 的 control 设计同时改变了两个变量：(1) 移除 cross-layer gradient coupling, (2) 引入严重的 train-inference mismatch（训练时仅 mask 1/32 layers，推理时 mask 全部 32 layers）。论文承认这是\"upper bound\"（Section 4.4 footnote 5），但仍然在 Abstract 和 Conclusion 中将其作为核心结论陈述。K=4 control 仅部分缓解：在 50% sparsity 下 K=4 (44.23) 反而比 K=1 (34.85) 差，论文自身也承认该分解\"unreliable under the current design\"（Section 4.4 最后一段）。一个在 50% 失效的分解不应在 Abstract 中以不加限定的方式呈现。\n- 为什么影响接收：这是论文的第一条 contribution（Section 1, bullet 1）。如果分解本身不可靠，该 contribution 的价值大幅缩水。\n- 建议修改方向：(1) 在 Abstract 和 Conclusion 中明确限定为\"at 30% moderate sparsity, subject to train-inference mismatch confound\"；(2) 考虑设计更干净的 deconfounding 实验，例如训练时 mask 全部 32 layers 但每 layer 独立优化（不传播 cross-layer gradient），或使用 stop-gradient 阻断 cross-layer 梯度流。\n\n**N2** [critical] 知识任务系统性退步的讨论深度不够，与\"primary design dimension\"的强 claim 矛盾\n\n- 具体位置：Section 4.2 (¶Knowledge-Task Regression), Table 2, Section 5, Abstract\n- 问题：KL predictor 在所有测试规模上知识密集型任务系统退步——8B MMLU −5.2pp, 14B GSM8K −20.1pp (σ=5.2pp), Mistral GSM8K −7.3pp (8.6 vs 15.9)。Abstract 仅说\"commonsense gains but knowledge-intensive decline\"，没有量化 decline 幅度。Conclusion 将其归入一句\"Limitations\"。但 Section 4.2 的 hypothesis（训练数据偏倚 + forward KL mode-covering 稀释 rare activations）仅是推测，没有实验验证。Constraint experiment（Appendix T）只部分验证了 allocation 因素（MMLU +3.4pp），loss-level contribution\"awaits knowledge-neuron probing\"。\n- 为什么影响接收：如果方法在知识/推理任务上系统性变差，称 output-distribution alignment 为\"primary design dimension\"就有误导性——它只是 PPL 和 commonsense 的 primary dimension，对 knowledge-intensive 任务则是 inferior。\n- 建议修改方向：(1) Abstract 应量化 MMLU/GSM8K 退步幅度；(2) 将\"primary design dimension\"限定为\"for perplexity and commonsense tasks at moderate sparsity\"；(3) 在 main text 中更深入讨论知识退步的原因（而非只在 hypothesis 段推测）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 MaskLLM 的区分需要加强，Taxonomy Table 1 中遗漏 MaskLLM\n\n- 具体位置：Section 2 (¶Predictor-Based Contextual Sparsity), Table 1\n- 问题：MaskLLM（NeurIPS 2024）与本文共享核心 recipe：frozen weights + learnable masks + KL divergence training + Gumbel sampling。论文列出三点区分（contextual vs static masks, cross-layer allocation, distribution shift robustness），这些区分是合理的，但论文没有做任何实验来验证这些区分的影响（例如，在 activation sparsity 场景下直接对比 MaskLLM 的 static mask 方案）。更值得注意的是，Table 1 的 taxonomy 中 Static × Coupled 仅列了 SPON，而 MaskLLM 也属于此格（static per-weight masks + KL coupled training），应被纳入。\n- 建议：(1) 在 Table 1 的 Static × Coupled 格中加入 MaskLLM；(2) 增加一段讨论明确说明为什么 contextual adaptation 是 activation sparsity 场景中关键的额外需求。\n\n**W2** [warning] 14.5% PPL improvement 的引用基准在 Abstract/Introduction 与 Main Table 不一致，可能误导读者\n\n- 具体位置：Abstract line 3, Introduction ¶14, Table 2\n- 问题：Abstract 和 Introduction 声称\"reduces perplexity by 14.5% over TEAL at matched sparsity (8.81 vs. 10.30, both at 28.5%)\"。但 10.30 这个数字来自 Appendix D（matched actual sparsity comparison），不在 main text 的 Table 2 中。Table 2 中 TEAL uniform 30% 的 PPL 是 10.82。按 Table 2 的对比，KL 的改进是 (10.82−8.81)/10.82 = 18.6%，而非 14.5%。论文选择更保守的 14.5% 是可以理解的，但一级读者会去 Table 2 验证，发现数字对不上。\n- 建议：在 Abstract 中用 Table 2 的数字（或同时报告两个基准），或在 Table 2 中增加 matched actual sparsity 的对比行。\n\n**W3** [warning] 缺少重要近期相关工作：ActTail (March 2026)\n\n- 具体位置：Section 2\n- 问题：ActTail (arXiv:2603.12272, March 2026) 提出基于 Heavy-Tailed Self-Regularization 理论的全局 activation sparsity allocation 方法，直接针对\"uniform sparsity across projections ignores heterogeneous statistical properties\"的问题。该工作与本文的 global top-k allocation 和 per-layer sparsity distribution 分析（Section 4.6, Appendix E）高度相关，应当讨论。\n- 建议：在 Related Work 的 Training-Free Activation Sparsity 段中加入 ActTail 的讨论。\n\n**W4** [warning] 论文实际未展示任何推理加速，但 title 和 framing 可能产生效率方面的误导\n\n- 具体位置：Title, Section 1, Appendix A\n- 问题：标题\"Output-Distribution Distillation for Contextual Sparsity Prediction\"暗示了对推理效率的贡献。但实际上方法增加 6.4% latency overhead（Appendix A, Table 5），且明确表示\"wall-clock speedup requires sparse kernel support not addressed here\"（Abstract, Section 1）。虽然论文诚实地披露了这一点，但 framing 仍可能给匆忙的读者留下效率改进的印象。\n- 建议：在 Abstract 和 Introduction 更早的位置明确声明\"this work focuses on prediction quality, not inference speedup\"，或在 Limitations 中更突出这一点。\n\n**W5** [warning] C1 Ablation 的 Soft-vs-Hard Confound 未完全解决\n\n- 具体位置：Section 4.3 (¶Soft-vs-Hard Confound)\n- 问题：C1 ablation 在提取 oracle masks 时将 KL predictor 的连续 logits 二值化（logits > 0），因此 C1 同时改变了 target source 和 mask representation。论文注意到了这一点并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比，但这个对比本身不足以排除 confound——因为 BCE+Gumbel 使用的是 magnitude-based targets 而非 KL-derived targets。完全的 deconfounding 需要将 KL 的连续 soft scores（而非二值化版本）传递给 BCE predictor 作为 regression targets。\n- 建议：在讨论中明确承认这一 confound 无法完全排除，或增加一个使用 soft regression targets 的实验。\n\n---\n\n## 小问题（不影响接收）\n\n**M1.** Introduction ¶14 中\"forward KL outperforms reverse KL by 8.6% and JSD by 6.4%\"（Section 1）未标注 sparsity level。这些数字来自 50% (Table 4)，在 30% 时差距小得多（KL 8.81 vs JSD 8.90 vs RevKL 9.26）。应明确标注。\n\n**M2.** 术语在全文中不完全一致：\"output-distribution alignment\"（Method/Conclusion）、\"output-distribution objective\"（Introduction）、\"output-distribution-coupled objective\"（Related Work）、\"KL distillation\"（多处）指代同一概念。建议在首次出现时定义统一术语并一致使用。\n\n**M3.** Table 2 的注脚标记较密集（†, ‡, *, ±），读者需要反复参照 caption 才能理解每行的确切设置。特别是 BCE 30% 的 † 标注说\"TEAL global\"但 main text 并未在显著位置解释为什么 BCE 用 global 而 KL 的主要报告用 uniform。建议简化或在正文中简述。\n\n**M4.** Section 4.2 中 \"MMLU 40.7±1.3%\" 在正文和 Table 2 中一致，但 Introduction ¶14 表述为\"stable downstream (MMLU 40.7±1.3%, 3-seed)\"——相对于 dense 65.27% 而言，MMLU 降低了 24.5pp，称之为\"stable\"是否准确？这里指的是跨 seed 的稳定性，而非绝对性能的稳定性，应当澄清措辞。\n\n**M5.** 页数合规性：Conclusion（Section 5）文本似乎延伸至第 9 页开头（约 1-2 行溢出）。EMNLP 2026 的 8 页正文限制是硬约束。建议检查 LaTeX 编译结果，确保 Section 5 完全在第 8 页内结束。如果确实溢出，需要压缩正文。\n\n**M6.** Introduction 中\"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"——68% divergence 和 32% Jaccard 是同一个度量的两种表述（Jaccard distance = 1 − IoU），但同一句中同时给出两个数字容易混淆。\n\n**M7.** Qwen-2.5-14B 的 GSM8K 退步从 8B 的 −1.3pp 剧增至 14B 的 −20.1pp，但论文未深入分析原因。Limitations 仅提及\"aggravation from 8B to 14B\"。如果方法在 scale up 时退步加剧，这对 scalability claim 是重大挑战。\n\n---\n\n## 缺失引用（Missing References）\n\n1. **ActTail** (arXiv:2603.12272, March 2026)——基于 HT-SR 理论的全局 activation sparsity allocation，与本文的 per-layer allocation 分析直接相关。\n2. 论文已引用的 MaskLLM 讨论充分，但应在 Table 1 taxonomy 中体现其位置。\n\n---\n\n## Questions to Authors\n\n1. 对于 N1：是否有可能设计一个 stop-gradient 实验，在保持 output-distribution KL loss 的同时阻断 cross-layer gradient propagation？这将比 per-layer KL 更干净地隔离 coupling scope。\n\n2. 对于 N2：在 14B scale 上 GSM8K 退步 −20.1pp（σ=5.2pp），你们是否验证过这不是由于 Qwen-2.5-14B 的 SwiGLU 架构差异（d_ff = 18944 vs LLaMA 的 14336）导致的 predictor 架构不匹配？\n\n3. 关于 W2：为什么选择在 Abstract 中报告 Appendix 的 matched-sparsity 数字（10.30）而非 main table 的 nominal-sparsity 数字（10.82）？如果 actual sparsity 不同，比较 PPL 的意义何在——是否应该先解决 sparsity controller 的精度问题？\n\n4. Table 4 中 Per-layer KL K=4 在 50% 时 PPL=44.23，比 K=1 的 34.85 差很多。你们的 hypothesis（partial coupling 在 tight capacity 下 amplifies gradient interference）有没有进一步的实验支持？\n\n---\n\n## 总结\n\n本文提出将 output-distribution KL distillation 应用于 SwiGLU LLM 的 contextual activation sparsity prediction，是该方向上首个系统性实证研究。PPL 层面的改进显著且跨架构一致，C1 target-swap ablation 设计有新意，compensation 冗余性发现有实用价值。\n\n主要顾虑集中在两点：(1) signal type vs coupling scope 分解——论文的核心 empirical contribution——的方法论可靠性不足，confound 在 50% 下完全无法消除；(2) 知识密集型任务的系统性退步与\"primary design dimension\"的强 claim 之间存在张力。此外，方法目前未展示实际推理加速，新颖性主要来自成熟组件在新场景的应用。\n\n这些问题不影响论文在 Findings 的合理性（solid empirical work），但要达到 Conference 门槛，核心 claim 的精确性和分解实验的严谨性需要提升。\n\n**推荐**：3.5 (Borderline Conference)——如果作者能在 rebuttal 中 (1) 限定分解 claim 的适用范围并提供更干净的 deconfounding 证据，(2) 在 Abstract/Conclusion 中平衡 PPL 优势与知识任务退步的叙述，有机会升至 Conference。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**Confidence**: 4 (Quite sure; important points checked, familiar with activation sparsity and KL distillation literature)\n**一句话总结**: 扎实的实证研究，将 KL distillation 首次系统应用于 contextual activation sparsity prediction，实验覆盖面广且诚实，但核心贡献（signal type vs coupling scope 分解）存在不可忽视的方法论混淆，加上缺乏实际加速和知识任务系统退步，限制了影响力。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主体实验设计合理，多 seed 评估值得肯定；但 signal type vs coupling scope 分解的 K=1 control 存在 train-inference mismatch 混淆，K=4 在 50% 失效；C1 ablation 有 soft-vs-hard confound |\n| Excitement | 2.5/5 | 将成熟组件（KL、Gumbel-Sigmoid、MLP predictor）应用于新场景，empirical findings 有参考价值但缺乏方法论创新或实际效率提升 |\n| Reproducibility | 4/5 | 训练细节充分（超参、硬件、seed），exp_id 标注便于追溯，承诺 release code/predictors；唯一不足是 oracle mask 提取的 trajectory 依赖性 |\n| Overall Assessment | 3.5/5 | Borderline Conference——实验深度足够 Findings，但核心分解 claim 的方法论问题和有限新颖性使 Conference 门槛有风险 |\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 系统且诚实的实证框架。** 论文从五种 loss 函数的对比出发，覆盖三种架构（LLaMA-3.1-8B、Mistral-7B-v0.3、Qwen-2.5-14B）、多个 sparsity 级别（25%–70%）和两种 allocation 策略。全程 3-seed 评估（PPL σ=0.02）、OOD 测试（C4）、cross-seed mask 一致性分析，实验可信度高。对 wall-clock speedup 缺失、MMLU/GSM8K 退步等 limitation 的主动披露体现了学术诚信（Abstract line 8, Limitations section）。\n\n**S2. C1 Target-Swap Ablation 设计巧妙。** 将 KL 发现的 mask pattern 提取后用标准 BCE 重新训练（Table 3），在 30% (≤1.70pp) 和 50% (≤0.79pp) 均接近 KL 性能，有力地证明了 mask target quality 而非 gradient coupling 是推理时质量的主要驱动力。这是一个有意义的实验设计。\n\n**S3. PPL 改进显著且跨架构一致。** KL predictor 在 30% sparsity 下 PPL 降低 14.5%（matched actual sparsity），50% 降低约 50%。该优势在 Mistral-7B 上一致复现（−17.3%, 3-seed, Table 16），PPL 层面的改进令人信服。\n\n**S4. Compensation 冗余性发现实用。** 证明 FastForward 风格的 67.2M 补偿网络在 KL predictor 下完全冗余（Appendix J），可省去推理开销和额外参数，对实际部署有价值。\n\n**S5. 写作质量整体较高。** 叙事从问题定义到方法到实验的逻辑链清晰，Section 3.6 的 gradient analysis 提供了直觉，Related Work 的二维 taxonomy（Table 1）提供了有用的文献整理框架。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Signal type vs coupling scope 分解存在不可消除的混淆变量\n\n- 具体位置：Section 4.4 (¶Per-Layer KL), Table 4, Abstract, Conclusion\n- 问题：分解的核心 claim 是\"signal type accounts for the majority of the PPL gap\"（Abstract line 5, Conclusion line 1）。但 K=1 per-layer KL 的 control 设计同时改变了两个变量：(1) 移除 cross-layer gradient coupling, (2) 引入严重的 train-inference mismatch（训练时仅 mask 1/32 layers，推理时 mask 全部 32 layers）。论文承认这是\"upper bound\"（Section 4.4 footnote 5），但仍然在 Abstract 和 Conclusion 中将其作为核心结论陈述。K=4 control 仅部分缓解：在 50% sparsity 下 K=4 (44.23) 反而比 K=1 (34.85) 差，论文自身也承认该分解\"unreliable under the current design\"（Section 4.4 最后一段）。一个在 50% 失效的分解不应在 Abstract 中以不加限定的方式呈现。\n- 为什么影响接收：这是论文的第一条 contribution（Section 1, bullet 1）。如果分解本身不可靠，该 contribution 的价值大幅缩水。\n- 建议修改方向：(1) 在 Abstract 和 Conclusion 中明确限定为\"at 30% moderate sparsity, subject to train-inference mismatch confound\"；(2) 考虑设计更干净的 deconfounding 实验，例如训练时 mask 全部 32 layers 但每 layer 独立优化（不传播 cross-layer gradient），或使用 stop-gradient 阻断 cross-layer 梯度流。\n\n**N2** [critical] 知识任务系统性退步的讨论深度不够，与\"primary design dimension\"的强 claim 矛盾\n\n- 具体位置：Section 4.2 (¶Knowledge-Task Regression), Table 2, Section 5, Abstract\n- 问题：KL predictor 在所有测试规模上知识密集型任务系统退步——8B MMLU −5.2pp, 14B GSM8K −20.1pp (σ=5.2pp), Mistral GSM8K −7.3pp (8.6 vs 15.9)。Abstract 仅说\"commonsense gains but knowledge-intensive decline\"，没有量化 decline 幅度。Conclusion 将其归入一句\"Limitations\"。但 Section 4.2 的 hypothesis（训练数据偏倚 + forward KL mode-covering 稀释 rare activations）仅是推测，没有实验验证。Constraint experiment（Appendix T）只部分验证了 allocation 因素（MMLU +3.4pp），loss-level contribution\"awaits knowledge-neuron probing\"。\n- 为什么影响接收：如果方法在知识/推理任务上系统性变差，称 output-distribution alignment 为\"primary design dimension\"就有误导性——它只是 PPL 和 commonsense 的 primary dimension，对 knowledge-intensive 任务则是 inferior。\n- 建议修改方向：(1) Abstract 应量化 MMLU/GSM8K 退步幅度；(2) 将\"primary design dimension\"限定为\"for perplexity and commonsense tasks at moderate sparsity\"；(3) 在 main text 中更深入讨论知识退步的原因（而非只在 hypothesis 段推测）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 MaskLLM 的区分需要加强，Taxonomy Table 1 中遗漏 MaskLLM\n\n- 具体位置：Section 2 (¶Predictor-Based Contextual Sparsity), Table 1\n- 问题：MaskLLM（NeurIPS 2024）与本文共享核心 recipe：frozen weights + learnable masks + KL divergence training + Gumbel sampling。论文列出三点区分（contextual vs static masks, cross-layer allocation, distribution shift robustness），这些区分是合理的，但论文没有做任何实验来验证这些区分的影响（例如，在 activation sparsity 场景下直接对比 MaskLLM 的 static mask 方案）。更值得注意的是，Table 1 的 taxonomy 中 Static × Coupled 仅列了 SPON，而 MaskLLM 也属于此格（static per-weight masks + KL coupled training），应被纳入。\n- 建议：(1) 在 Table 1 的 Static × Coupled 格中加入 MaskLLM；(2) 增加一段讨论明确说明为什么 contextual adaptation 是 activation sparsity 场景中关键的额外需求。\n\n**W2** [warning] 14.5% PPL improvement 的引用基准在 Abstract/Introduction 与 Main Table 不一致，可能误导读者\n\n- 具体位置：Abstract line 3, Introduction ¶14, Table 2\n- 问题：Abstract 和 Introduction 声称\"reduces perplexity by 14.5% over TEAL at matched sparsity (8.81 vs. 10.30, both at 28.5%)\"。但 10.30 这个数字来自 Appendix D（matched actual sparsity comparison），不在 main text 的 Table 2 中。Table 2 中 TEAL uniform 30% 的 PPL 是 10.82。按 Table 2 的对比，KL 的改进是 (10.82−8.81)/10.82 = 18.6%，而非 14.5%。论文选择更保守的 14.5% 是可以理解的，但一级读者会去 Table 2 验证，发现数字对不上。\n- 建议：在 Abstract 中用 Table 2 的数字（或同时报告两个基准），或在 Table 2 中增加 matched actual sparsity 的对比行。\n\n**W3** [warning] 缺少重要近期相关工作：ActTail (March 2026)\n\n- 具体位置：Section 2\n- 问题：ActTail (arXiv:2603.12272, March 2026) 提出基于 Heavy-Tailed Self-Regularization 理论的全局 activation sparsity allocation 方法，直接针对\"uniform sparsity across projections ignores heterogeneous statistical properties\"的问题。该工作与本文的 global top-k allocation 和 per-layer sparsity distribution 分析（Section 4.6, Appendix E）高度相关，应当讨论。\n- 建议：在 Related Work 的 Training-Free Activation Sparsity 段中加入 ActTail 的讨论。\n\n**W4** [warning] 论文实际未展示任何推理加速，但 title 和 framing 可能产生效率方面的误导\n\n- 具体位置：Title, Section 1, Appendix A\n- 问题：标题\"Output-Distribution Distillation for Contextual Sparsity Prediction\"暗示了对推理效率的贡献。但实际上方法增加 6.4% latency overhead（Appendix A, Table 5），且明确表示\"wall-clock speedup requires sparse kernel support not addressed here\"（Abstract, Section 1）。虽然论文诚实地披露了这一点，但 framing 仍可能给匆忙的读者留下效率改进的印象。\n- 建议：在 Abstract 和 Introduction 更早的位置明确声明\"this work focuses on prediction quality, not inference speedup\"，或在 Limitations 中更突出这一点。\n\n**W5** [warning] C1 Ablation 的 Soft-vs-Hard Confound 未完全解决\n\n- 具体位置：Section 4.3 (¶Soft-vs-Hard Confound)\n- 问题：C1 ablation 在提取 oracle masks 时将 KL predictor 的连续 logits 二值化（logits > 0），因此 C1 同时改变了 target source 和 mask representation。论文注意到了这一点并报告了 BCE+Gumbel (32.22) vs standard BCE (27.97) 的对比，但这个对比本身不足以排除 confound——因为 BCE+Gumbel 使用的是 magnitude-based targets 而非 KL-derived targets。完全的 deconfounding 需要将 KL 的连续 soft scores（而非二值化版本）传递给 BCE predictor 作为 regression targets。\n- 建议：在讨论中明确承认这一 confound 无法完全排除，或增加一个使用 soft regression targets 的实验。\n\n---\n\n## 小问题（不影响接收）\n\n**M1.** Introduction ¶14 中\"forward KL outperforms reverse KL by 8.6% and JSD by 6.4%\"（Section 1）未标注 sparsity level。这些数字来自 50% (Table 4)，在 30% 时差距小得多（KL 8.81 vs JSD 8.90 vs RevKL 9.26）。应明确标注。\n\n**M2.** 术语在全文中不完全一致：\"output-distribution alignment\"（Method/Conclusion）、\"output-distribution objective\"（Introduction）、\"output-distribution-coupled objective\"（Related Work）、\"KL distillation\"（多处）指代同一概念。建议在首次出现时定义统一术语并一致使用。\n\n**M3.** Table 2 的注脚标记较密集（†, ‡, *, ±），读者需要反复参照 caption 才能理解每行的确切设置。特别是 BCE 30% 的 † 标注说\"TEAL global\"但 main text 并未在显著位置解释为什么 BCE 用 global 而 KL 的主要报告用 uniform。建议简化或在正文中简述。\n\n**M4.** Section 4.2 中 \"MMLU 40.7±1.3%\" 在正文和 Table 2 中一致，但 Introduction ¶14 表述为\"stable downstream (MMLU 40.7±1.3%, 3-seed)\"——相对于 dense 65.27% 而言，MMLU 降低了 24.5pp，称之为\"stable\"是否准确？这里指的是跨 seed 的稳定性，而非绝对性能的稳定性，应当澄清措辞。\n\n**M5.** 页数合规性：Conclusion（Section 5）文本似乎延伸至第 9 页开头（约 1-2 行溢出）。EMNLP 2026 的 8 页正文限制是硬约束。建议检查 LaTeX 编译结果，确保 Section 5 完全在第 8 页内结束。如果确实溢出，需要压缩正文。\n\n**M6.** Introduction 中\"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"——68% divergence 和 32% Jaccard 是同一个度量的两种表述（Jaccard distance = 1 − IoU），但同一句中同时给出两个数字容易混淆。\n\n**M7.** Qwen-2.5-14B 的 GSM8K 退步从 8B 的 −1.3pp 剧增至 14B 的 −20.1pp，但论文未深入分析原因。Limitations 仅提及\"aggravation from 8B to 14B\"。如果方法在 scale up 时退步加剧，这对 scalability claim 是重大挑战。\n\n---\n\n## 缺失引用（Missing References）\n\n1. **ActTail** (arXiv:2603.12272, March 2026)——基于 HT-SR 理论的全局 activation sparsity allocation，与本文的 per-layer allocation 分析直接相关。\n2. 论文已引用的 MaskLLM 讨论充分，但应在 Table 1 taxonomy 中体现其位置。\n\n---\n\n## Questions to Authors\n\n1. 对于 N1：是否有可能设计一个 stop-gradient 实验，在保持 output-distribution KL loss 的同时阻断 cross-layer gradient propagation？这将比 per-layer KL 更干净地隔离 coupling scope。\n\n2. 对于 N2：在 14B scale 上 GSM8K 退步 −20.1pp（σ=5.2pp），你们是否验证过这不是由于 Qwen-2.5-14B 的 SwiGLU 架构差异（d_ff = 18944 vs LLaMA 的 14336）导致的 predictor 架构不匹配？\n\n3. 关于 W2：为什么选择在 Abstract 中报告 Appendix 的 matched-sparsity 数字（10.30）而非 main table 的 nominal-sparsity 数字（10.82）？如果 actual sparsity 不同，比较 PPL 的意义何在——是否应该先解决 sparsity controller 的精度问题？\n\n4. Table 4 中 Per-layer KL K=4 在 50% 时 PPL=44.23，比 K=1 的 34.85 差很多。你们的 hypothesis（partial coupling 在 tight capacity 下 amplifies gradient interference）有没有进一步的实验支持？\n\n---\n\n## 总结\n\n本文提出将 output-distribution KL distillation 应用于 SwiGLU LLM 的 contextual activation sparsity prediction，是该方向上首个系统性实证研究。PPL 层面的改进显著且跨架构一致，C1 target-swap ablation 设计有新意，compensation 冗余性发现有实用价值。\n\n主要顾虑集中在两点：(1) signal type vs coupling scope 分解——论文的核心 empirical contribution——的方法论可靠性不足，confound 在 50% 下完全无法消除；(2) 知识密集型任务的系统性退步与\"primary design dimension\"的强 claim 之间存在张力。此外，方法目前未展示实际推理加速，新颖性主要来自成熟组件在新场景的应用。\n\n这些问题不影响论文在 Findings 的合理性（solid empirical work），但要达到 Conference 门槛，核心 claim 的精确性和分解实验的严谨性需要提升。\n\n**推荐**：3.5 (Borderline Conference)——如果作者能在 rebuttal 中 (1) 限定分解 claim 的适用范围并提供更干净的 deconfounding 证据，(2) 在 Abstract/Conclusion 中平衡 PPL 优势与知识任务退步的叙述，有机会升至 Conference。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1831 · 2026-05-23T01:34:43.941558+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3993
}
```

</details>

---


### Assistant

_source line 1832 · 2026-05-23T01:34:53.733955+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall: 3.5 (Borderline Conference)**，Confidence 4/5
- **2 个 Must-Fix**：(1) signal type vs coupling scope 分解的 train-inference mismatch confound 在 50% 完全失效，但 Abstract/Conclusion 以不加限定的方式陈述；(2) 知识任务系统退步与"primary design dimension"强 claim 矛盾，Abstract 未量化 decline
- **5 个 Should-Fix**：MaskLLM 在 taxonomy 中缺位、14.5% 基准数字在 Abstract 与 Table 2 不一致、缺少 ActTail 引用、无实际加速但 framing 可能误导、C1 soft-vs-hard confound 未解决
- **7 个 Minor**：术语一致性、页数可能溢出、MMLU"stable"措辞、Qwen-14B GSM8K 退步缺乏分析等

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 45

## Round 45

4 recorded events


### User

_source line 1833 · 2026-05-23T01:35:39.270800+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（引用论文中的 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

### Overall: 3.5 / 5 — Borderline Conference, Confidence 4/5

### Must-Fix 问题

**N1** [critical] 知识类任务系统性退化随 scale 恶化，机制分析不充分
- KL 在所有测试规模上 MMLU/GSM8K 低于 TEAL——8B: MMLU -5.2pp, GSM8K -1.3pp (30%)；14B: GSM8K -20.1pp (σ=5.2)。退化从 8B 到 14B 恶化。论文提出两个假设（训练数据同质性、forward KL mode-covering），仅用 constraint experiment（remove valley, MMLU +3.4pp）部分验证第一个因素，第二个因素无实验支撑。建议至少做 mixed domain 训练或 knowledge neuron probe。

**N2** [critical] Per-layer KL 分解在 50% 稀疏度下失效
- K=4 per-layer KL (PPL 44.23) 比 K=1 (34.85) 更差，E2E KL 为 11.84。50% 下分解完全失效。K=4 MMLU 异常（42.7±1.4 > E2E 40.7±1.3）暴露 allocation confound：K=4 产生 near-uniform allocation (std=0.003)，signal type 和 coupling scope 并非正交。建议增加更多 K 值或强制 K=4 使用 E2E allocation pattern。

**N3** [critical] 缺乏实际推理加速，实用贡献为零
- 6.4% latency overhead，unstructured masks 无 sparse kernel 加速。方法比 dense inference 更慢。建议至少做 proof-of-concept sparse kernel 加速，或与 LaRoSA 等已有加速方法在 mask quality 层面对比。

### Should-Fix 问题

**W1** [warning] 3 seeds 下游统计力不足（MMLU 30% global σ=9.5，95% CI 约 ±23.5pp）
**W2** [warning] Table 2 baseline 比较条件不统一（BCE 30% 用 global，KL 用 uniform+global；BCE 50% 用 2700 steps）
**W3** [warning] C1 ablation soft-vs-hard confound（二值化丢失 ranking 信息）
**W4** [warning] Qwen-14B 仅 30% sparsity，无 50% 结果，评估不完整
**W5** [warning] Forward KL vs Reverse KL 在 30% 处差距微小（8.81 vs 9.26）

### 小问题
- Eq. 5 求和方式正文未明确（附录才说明 average over positions）
- Table 2 脚注 ‡ matched sparsity 对比应更显著
- Figure 1 过于简略
- SPON 讨论在 §2 和 §4.5 重复
- C1 s42 oracle provenance 应在 Table 3 caption 更显著标注

### 主要优势
1. C1 target-swap ablation 设计精巧
2. 对局限性的诚实披露极罕见
3. PPL 改善显著且一致（14.5%/50%/82%）
4. 实验覆盖面广（5 种 loss、3 架构、6 sparsity levels）
5. 2D taxonomy 有用
6. 训练成本极低（单 GPU ~45 min）

### Questions
Q1: 多样化数据训练是否能修复知识任务退化？
Q2: K=4 强制使用 E2E allocation 时 MMLU 异常是否消失？
Q3: BCE+Gumbel+Penalty (38.02) 为何比无 penalty (32.22) 更差？
Q4: L14-L18 protection valley 在 Mistral/Qwen 上是否也出现？
Q5: KL teacher + BCE student 两阶段训练是否可行？

### Missing References
- CATS 应作为 baseline 对比或解释排除原因
- MaskLLM 应有 PPL 层面数字对比
- Mixture-of-Depths 与 per-token mask prediction 的对偶关系

---

请逐条回应以上所有 Must-Fix、Should-Fix 和主要 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-23T01:37:49.702359+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 的逐条交叉回应\n\n## Must-Fix\n\n**[AGREE] R1-N1: 知识类任务系统性退化随 scale 恶化，机制分析不充分**\n\n同意。与我的 N2 完全一致。补充证据：Mistral-7B GSM8K 也出现反转（KL 8.6±2.2 vs TEAL 15.9, Table 16），退化跨架构一致。Constraint experiment（Appendix T）最多解释约 65% 的 MMLU 退步（+3.4pp / −5.2pp），剩余归因于 loss function 本身的 mode-covering 特性（Section 4.2 最后一句），无实验支撑。Mixed-domain training 是 rebuttal 中最直接的验证手段。\n\n**[AGREE] R1-N2: Per-layer KL 分解在 50% 下失效**\n\n同意，与我的 N1 高度重叠。额外补充：K=4 MMLU 异常（42.7 > E2E 40.7, Appendix S）不仅是 allocation confound，更暴露 signal type 与 coupling scope 维度的非正交性——K=4 的 near-uniform allocation (std=0.003) 等价于移除 valley pattern（Appendix T: remove-valley → MMLU=44.0）。论文在 Section 4.4 最后一段承认 50% 下分解\"unreliable\"，但 Abstract 和 Conclusion 中的 claim 无此限定。\n\n**[REBUT] R1-N3: 缺乏实际推理加速，实用贡献为零**\n\n部分反驳。\"实用贡献为零\"过于绝对。(1) 论文明确自定位为 empirical study（Abstract line 8），贡献在于理解训练目标对 mask quality 的影响；(2) Compensation 冗余性发现（Section 4.4, Appendix J, Table 5）实际减少推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数；(3) C1 ablation 证明 KL-derived targets 可迁移到更简单的 BCE predictor（Table 3），这对实际部署有工程价值。但同意应增加与 LaRoSA 等已有加速方法的 mask quality 对比。建议将 N3 从 critical 降级为 warning。\n\n## Should-Fix\n\n**[AGREE] R1-W1**: 3 seeds 统计力不足，MMLU 30% global σ=9.5 使结论可信度极低。论文的处理（PPL 为 primary metric，下游仅作 directional evidence，Section 4.2）是诚实的，但 key comparisons 应增加 seeds。\n\n**[AGREE] R1-W2**: Table 2 条件不统一。BCE 30% 用 global（脚注 †），KL 主报告用 uniform；BCE 50% 用 2700 steps。建议 Table 2 增加条件标注列，或将 BCE 30% uniform (PPL 15.71, Table 4) 纳入正表。\n\n**[AGREE] R1-W3**: C1 soft-vs-hard confound 与我的 W5 一致。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（两者均用 magnitude targets）。需 soft KL-derived targets → regression 的实验。\n\n**[AGREE] R1-W4**: Qwen-14B 缺 50% 结果，scaling 分析不完整。论文声称 cross-scale evidence 为 contribution（Section 1 bullet 2），但 14B 仅覆盖单一 sparsity level。\n\n**[REBUT] R1-W5**: Forward KL vs RevKL 30% 差距小（0.45pp）恰恰支持论文结论——三种 output-distribution losses（KL/RevKL/JSD）之间差距远小于它们与 BCE (15.71) / MSE (18.52) 的差距（Table 4），说明 output-distribution alignment 是 primary factor。50% 处差距扩大至 +8.6% 符合理论预期（Section 3.4, false negatives cascade under global allocation）。但同意 Introduction 中\"8.6%/6.4%\"应标注 sparsity level。\n\n## Questions\n\n**Q1**: 合理，论文仅测试推理时 domain shift（Appendix D），未测试训练数据多样性影响。应在 rebuttal 提供。\n\n**Q2**: 极好的实验建议。强制 K=4 使用 E2E 的 non-uniform allocation 可直接验证 allocation vs coupling 的因果关系。论文有 constraint framework（Appendix T）可支持。\n\n**Q3**: 论文未解释。推测：BCE 无 cross-neuron coupling，penalty 强制 sparsity 但 BCE 的 loss 无法指导 global context 下的 neuron 选择，导致 penalty-driven masks 更差。与论文核心论点一致但应明确讨论。\n\n**Q4**: 论文仅报告 LLaMA 的 per-layer distribution（Appendix U）。如果 valley pattern 非通用，cross-architecture claim 需限定。\n\n**Q5**: 本质即 C1 ablation。Table 3 已证明可行（gap ≤1.70pp at 30%）。用 soft regression targets 替代二值化可进一步改进。\n\n## 两位 Reviewer 的共识总结\n\nR1 和 R2 在以下 critical issues 上完全一致：\n1. **Signal type/coupling 分解的方法论可靠性**（R1-N2 ≈ R2-N1）：50% 下失效，Abstract/Conclusion 的 claim 需限定\n2. **知识任务系统性退步**（R1-N1 ≈ R2-N2）：机制分析不足，\"primary design dimension\" claim 有误导性\n3. **C1 soft-vs-hard confound**（R1-W3 ≈ R2-W5）：未完全解决\n\n唯一分歧在 R1-N3（实际加速缺失）：R1 定性为 critical，R2 认为应降级为 warning——论文的自定位和 compensation 冗余性发现提供了一定实用价值。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 的逐条交叉回应\n\n## Must-Fix\n\n**[AGREE] R1-N1: 知识类任务系统性退化随 scale 恶化，机制分析不充分**\n\n同意。与我的 N2 完全一致。补充证据：Mistral-7B GSM8K 也出现反转（KL 8.6±2.2 vs TEAL 15.9, Table 16），退化跨架构一致。Constraint experiment（Appendix T）最多解释约 65% 的 MMLU 退步（+3.4pp / −5.2pp），剩余归因于 loss function 本身的 mode-covering 特性（Section 4.2 最后一句），无实验支撑。Mixed-domain training 是 rebuttal 中最直接的验证手段。\n\n**[AGREE] R1-N2: Per-layer KL 分解在 50% 下失效**\n\n同意，与我的 N1 高度重叠。额外补充：K=4 MMLU 异常（42.7 > E2E 40.7, Appendix S）不仅是 allocation confound，更暴露 signal type 与 coupling scope 维度的非正交性——K=4 的 near-uniform allocation (std=0.003) 等价于移除 valley pattern（Appendix T: remove-valley → MMLU=44.0）。论文在 Section 4.4 最后一段承认 50% 下分解\"unreliable\"，但 Abstract 和 Conclusion 中的 claim 无此限定。\n\n**[REBUT] R1-N3: 缺乏实际推理加速，实用贡献为零**\n\n部分反驳。\"实用贡献为零\"过于绝对。(1) 论文明确自定位为 empirical study（Abstract line 8），贡献在于理解训练目标对 mask quality 的影响；(2) Compensation 冗余性发现（Section 4.4, Appendix J, Table 5）实际减少推理开销从 +9.1% 降至 +6.4% 并节省 67.2M 参数；(3) C1 ablation 证明 KL-derived targets 可迁移到更简单的 BCE predictor（Table 3），这对实际部署有工程价值。但同意应增加与 LaRoSA 等已有加速方法的 mask quality 对比。建议将 N3 从 critical 降级为 warning。\n\n## Should-Fix\n\n**[AGREE] R1-W1**: 3 seeds 统计力不足，MMLU 30% global σ=9.5 使结论可信度极低。论文的处理（PPL 为 primary metric，下游仅作 directional evidence，Section 4.2）是诚实的，但 key comparisons 应增加 seeds。\n\n**[AGREE] R1-W2**: Table 2 条件不统一。BCE 30% 用 global（脚注 †），KL 主报告用 uniform；BCE 50% 用 2700 steps。建议 Table 2 增加条件标注列，或将 BCE 30% uniform (PPL 15.71, Table 4) 纳入正表。\n\n**[AGREE] R1-W3**: C1 soft-vs-hard confound 与我的 W5 一致。BCE+Gumbel (32.22) vs standard BCE (27.97) 不足以排除 confound（两者均用 magnitude targets）。需 soft KL-derived targets → regression 的实验。\n\n**[AGREE] R1-W4**: Qwen-14B 缺 50% 结果，scaling 分析不完整。论文声称 cross-scale evidence 为 contribution（Section 1 bullet 2），但 14B 仅覆盖单一 sparsity level。\n\n**[REBUT] R1-W5**: Forward KL vs RevKL 30% 差距小（0.45pp）恰恰支持论文结论——三种 output-distribution losses（KL/RevKL/JSD）之间差距远小于它们与 BCE (15.71) / MSE (18.52) 的差距（Table 4），说明 output-distribution alignment 是 primary factor。50% 处差距扩大至 +8.6% 符合理论预期（Section 3.4, false negatives cascade under global allocation）。但同意 Introduction 中\"8.6%/6.4%\"应标注 sparsity level。\n\n## Questions\n\n**Q1**: 合理，论文仅测试推理时 domain shift（Appendix D），未测试训练数据多样性影响。应在 rebuttal 提供。\n\n**Q2**: 极好的实验建议。强制 K=4 使用 E2E 的 non-uniform allocation 可直接验证 allocation vs coupling 的因果关系。论文有 constraint framework（Appendix T）可支持。\n\n**Q3**: 论文未解释。推测：BCE 无 cross-neuron coupling，penalty 强制 sparsity 但 BCE 的 loss 无法指导 global context 下的 neuron 选择，导致 penalty-driven masks 更差。与论文核心论点一致但应明确讨论。\n\n**Q4**: 论文仅报告 LLaMA 的 per-layer distribution（Appendix U）。如果 valley pattern 非通用，cross-architecture claim 需限定。\n\n**Q5**: 本质即 C1 ablation。Table 3 已证明可行（gap ≤1.70pp at 30%）。用 soft regression targets 替代二值化可进一步改进。\n\n## 两位 Reviewer 的共识总结\n\nR1 和 R2 在以下 critical issues 上完全一致：\n1. **Signal type/coupling 分解的方法论可靠性**（R1-N2 ≈ R2-N1）：50% 下失效，Abstract/Conclusion 的 claim 需限定\n2. **知识任务系统性退步**（R1-N1 ≈ R2-N2）：机制分析不足，\"primary design dimension\" claim 有误导性\n3. **C1 soft-vs-hard confound**（R1-W3 ≈ R2-W5）：未完全解决\n\n唯一分歧在 R1-N3（实际加速缺失）：R1 定性为 critical，R2 认为应降级为 warning——论文的自定位和 compensation 冗余性发现提供了一定实用价值。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1835 · 2026-05-23T01:37:53.344537+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3642
}
```

</details>

---


### Assistant

_source line 1836 · 2026-05-23T01:37:58.428405+00:00_

交叉回应已提交给 Review Director。

两位 Reviewer 在三个核心问题上达成共识：(1) signal type/coupling 分解在 50% 下失效但 claim 未限定；(2) 知识任务退步机制分析不足；(3) C1 soft-vs-hard confound 未解决。唯一分歧是实际加速缺失的严重程度——我认为论文作为 empirical study 的自定位和 compensation 冗余性发现使其不应被定性为 critical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 46

## Round 46

88 recorded events


### User

_source line 1837 · 2026-05-23T07:19:26.775567+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查论文的 **新颖性 + 完整性 + 写作质量**。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）
- **截止日期**: 2026-05-25
- **格式要求**: ACL 模板，Long Paper 正文上限 8 页（不含 references 和 limitations/ethics）
- **匿名规则**: Double-blind
- **评分标准**: ARR Overall Assessment (1-5 scale)，其中 4 = Conference（可被主会议接收），3 = Findings

## 论文文件
- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf`
- 图表目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/figures/paper/`

## 你的审查侧重

**核心关注点**：
1. **新颖性边界**：与 MaskLLM 共享核心 recipe (frozen weights + learnable masks + KL + Gumbel)。三点区分（contextual vs static, global allocation, distribution shift robustness）是否足够？Table 1 taxonomy 分类是否准确（Static×Coupled 仅列 SPON 和 MaskLLM 是否遗漏）？
2. **Contribution framing**：自称 "empirical study"，但 contribution list 包含方法创新暗示（output-distribution alignment ranking, target-swap ablation）。定位是否一致？"primary design dimension" claim 的适用范围是否充分限定？
3. **写作质量**：
   - 术语一致性：output-distribution alignment / distillation / objective 是否交替使用？
   - Abstract 信息密度：是否过度压缩导致误读？14.5% PPL 的引用基准是否清晰？
   - 数字呈现：68% divergence vs 32% Jaccard 是否同句混淆？
   - "stable downstream" 等措辞是否可能误导？
4. **Related Work 完整性**：是否遗漏重要 2025-2026 近期工作？尤其是：
   - Contextual sparsity prediction 领域的新方法
   - KL distillation 在 structured pruning 中的应用
   - 与本文高度相关但未引用的工作
5. **格式合规**：8 页正文限制、ACL 模板、匿名性、References 格式、Appendix 规范
6. **Limitations 和 Ethics 覆盖度**：是否充分讨论了方法的局限性？

**输出格式**：
- Strengths（逐条，带证据）
- Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级，引用具体 Section/Table/Figure）
- Questions（需要作者回答的问题）
- Missing References（如有，搜索 2025-2026 相关工作）
- Excitement（1-5 scale + 简短理由）
- Overall Assessment（1-5 ARR scale + 简短理由）
- Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-23T07:19:33.977805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-23T07:19:34.028687+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-23T07:19:36.792958+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-23T07:19:36.843629+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-23T07:19:38.604545+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14"
  }
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-23T07:19:38.655172+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_14/skills/projects/distill_sparse_swiglu/distilled-research.skill.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/skills/projects/distill_sparse_swiglu/distilled-writing.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-23T07:19:43.874356+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1845 · 2026-05-23T07:19:43.924958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1846 · 2026-05-23T07:19:47.939897+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 1847 · 2026-05-23T07:19:50.348775+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1848 · 2026-05-23T07:19:55.374296+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Assessment Score

The Over
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7434
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-23T07:19:57.235918+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.6}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_p
…[truncated 50 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6887
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-23T07:20:03.172447+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Include: soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Include: soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1851 · 2026-05-23T07:20:03.624234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1852 · 2026-05-23T07:20:04.579490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1853 · 2026-05-23T07:20:04.579919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1854 · 2026-05-23T07:20:05.185987+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 1855 · 2026-05-23T07:20:05.186426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-23T07:20:05.387375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1857 · 2026-05-23T07:20:06.358925+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1172
}
```

</details>

---


### Tool result

_source line 1858 · 2026-05-23T07:20:06.862401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1475
}
```

</details>

---


### Tool result

_source line 1859 · 2026-05-23T07:20:08.822249+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness** (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement** (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others"

## 4. **Overall Assessment** (1-5 scale)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance recommended
- **2**: Resubmit next cycle with revisions
- **1**: Do not resubmit

## Additional Dimensions
- Reproducibility (1-5)
- Datasets value (1-5)
- Software value (1-5)
- Author identity knowledge (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5649
}
```

</details>

---


### Tool call

_source line 1860 · 2026-05-23T07:20:16.450052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1861 · 2026-05-23T07:20:16.803195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1862 · 2026-05-23T07:20:17.257640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1863 · 2026-05-23T07:20:17.358773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1864 · 2026-05-23T07:20:17.912569+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1865 · 2026-05-23T07:20:18.013352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1866 · 2026-05-23T07:20:18.114819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-23T07:20:18.668775+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1868 · 2026-05-23T07:20:33.605864+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "9-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "9-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1869 · 2026-05-23T07:20:34.308353+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.5}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 600.1}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 536.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.5}], \"total_pages\": 20, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1870 · 2026-05-23T07:20:39.190215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1871 · 2026-05-23T07:20:39.944405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1872 · 2026-05-23T07:20:39.997219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1873 · 2026-05-23T07:20:40.551365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1874 · 2026-05-23T07:20:40.551815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1875 · 2026-05-23T07:20:41.053760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1876 · 2026-05-23T07:20:41.406618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1877 · 2026-05-23T07:20:41.507438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1878 · 2026-05-23T07:20:42.160634+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-23T07:20:42.263059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 1880 · 2026-05-23T07:20:42.313613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1881 · 2026-05-23T07:20:42.917657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1882 · 2026-05-23T07:20:48.440171+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "15-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "15-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1883 · 2026-05-23T07:20:49.142771+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 335.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 362.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.7}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 92.6}], \"total_pages\": 20, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1884 · 2026-05-23T07:20:55.866192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1885 · 2026-05-23T07:20:56.872450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1886 · 2026-05-23T07:20:56.872898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1887 · 2026-05-23T07:20:57.327222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1888 · 2026-05-23T07:20:57.779715+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 1889 · 2026-05-23T07:20:57.832264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1890 · 2026-05-23T07:20:57.832755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1891 · 2026-05-23T07:20:58.287406+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1892 · 2026-05-23T07:20:59.132808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1300
}
```

</details>

---


### Tool call

_source line 1893 · 2026-05-23T07:20:59.183416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_24/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1894 · 2026-05-23T07:20:59.187294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool result

_source line 1895 · 2026-05-23T07:20:59.892797+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1605
}
```

</details>

---


### Tool call

_source line 1896 · 2026-05-23T07:21:40.404553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "contextual sparsity prediction LLM 2025 2026 learnable masks activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "contextual sparsity prediction LLM 2025 2026 learnable masks activation sparsity"
  }
}
```

</details>

---


### Tool call

_source line 1897 · 2026-05-23T07:21:40.856565+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KL divergence distillation structured pruning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KL divergence distillation structured pruning LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-23T07:21:41.158160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SwiGLU activation sparsity prediction 2025 2026 efficient inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SwiGLU activation sparsity prediction 2025 2026 efficient inference"
  }
}
```

</details>

---


### Tool result

_source line 1899 · 2026-05-23T07:21:47.581219+00:00_

Web search results for query: "SwiGLU activation sparsity prediction 2025 2026 efficient inference"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2412.01380v1"},{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking","url":"https://arxiv.org/pdf/2412.01380"},{"title":"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models","url":"https://neurips2023-enlsp.github.io/papers/paper_62.pdf"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"RELU STRIKES BACK: EXPLOITING ACTIVATION ...","url":"https://openreview.net/pdf?id=osoWxY8q2E"}]

Based on the search results, here's what I found regarding SwiGLU activation sparsity prediction for efficient inference:

## Key Findings

**The Challenge with SwiGLU:**
Modern LLMs use SwiGLU instead of ReLU, which results in little inherent sparsity. While SwiGLU activations can be pruned based on magnitude, the resulting sparsity patterns are difficult to predict, rendering previous approaches ineffective.

**Recent Approaches to Address This:**
To leverage existing SwiGLU checkpoints for sparse regimes, adaptive activation thresholding and lightweight predictor networks can provide up to 80% sparsity with minimal impact on end-task metrics.

Sparsity predictors such as those introduced in DejaVu can predict which elements in the activation vectors will be zero, allowing weights that generate zero-valued activation elements to also be ignored in the preceding layer.

**Future Architectural Considerations:**
While gated activations such as SwiGLU will persist in dense models prioritizing accuracy, architectural choices for next-generation sparse o
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6423
}
```

</details>

---


### Tool result

_source line 1900 · 2026-05-23T07:21:48.334058+00:00_

Web search results for query: "KL divergence distillation structured pruning LLM 2025 2026"

Links: [{"title":"[2505.18166] Constrained Edge AI Deployment: Fine-Tuning vs Distillation for LLM Compression","url":"https://arxiv.org/abs/2505.18166"},{"title":"Compact Language Models via Pruning and Knowledge Distillation","url":"https://arxiv.org/html/2407.14679v1"},{"title":"LLM Pruning and Distillation in Practice: The Minitron Approach","url":"https://arxiv.org/html/2408.11796v3"},{"title":"Pruning and Distilling LLMs Using NVIDIA TensorRT Model Optimizer | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/pruning-and-distilling-llms-using-nvidia-tensorrt-model-optimizer/"},{"title":"Constrained Edge AI Deployment: Fine-Tuning vs. Distillation for LLM Compression","url":"https://arxiv.org/html/2505.18166v1"},{"title":"Advancing Model Refinement: Muon-Optimized Distillation and Quantization for LLM Deployment","url":"https://arxiv.org/html/2601.09865v1"},{"title":"Constrained Edge AI Deployment: Fine-Tuning vs Distillation for LLM Compression","url":"https://arxiv.org/pdf/2505.18166"}]

I found several relevant research papers and articles on KL divergence distillation and structured pruning for LLMs from 2025-2026:

## Recent Research (2025-2026)

**Constrained Edge AI Deployment Study (May 2025)**
Modern foundational models are often compressed via a combination of structured pruning and re-training to meet the strict compute, memory, and connectivity constraints of edge deployments, with state-of-the-art pruning schemes targeting the entire Transformer or simpler layer-wise L2-norm pruning on MLP blocks. The research compared fine-tuning with Cross-Entropy (which requires labeled data) versus Self-Distillation with KL-divergence (which leverages only teacher logits without labels). Under identical pruning schedules, KL-based distillation matched or exceeded CE fine-tuning in test accuracy, demonstrating that the choice of loss function materially aff
…[truncated 970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7477
}
```

</details>

---


### Tool result

_source line 1901 · 2026-05-23T07:21:49.237789+00:00_

Web search results for query: "contextual sparsity prediction LLM 2025 2026 learnable masks activation sparsity"

Links: [{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v1"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/html/2603.14110"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/0e9a05f5ce62284c91e4a33498899124-Paper-Conference.pdf"}]

I found several relevant research papers on contextual sparsity prediction and learnable masks for LLMs in 2025-2026:

## Key Recent Work

**SVD Contextual Sparsity Predictors (March 2026):** Lightweight, learnable sparsity predictors generate input-specific sparse activation patterns prior to FFN forward passes. Recent experiments on sparse LLMs with 90% activation sparsity in FFNs achieved up to 1.8× reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores.

**ShadowLLM (June 2024):** This predictor-based method shadows LLM behavior and enforces better sparsity patterns, achieving over 15% improvement in end-to-end accuracy without increasing latency compared to previous methods. The sparsity pred
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8833
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-23T07:21:58.067758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SVD-CSP\" OR \"SVD contextual sparsity\" 2026 arxiv LLM predictor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SVD-CSP\" OR \"SVD contextual sparsity\" 2026 arxiv LLM predictor"
  }
}
```

</details>

---


### Tool call

_source line 1903 · 2026-05-23T07:21:58.218733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ProSparse SparseInfer activation sparsity SwiGLU 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ProSparse SparseInfer activation sparsity SwiGLU 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1904 · 2026-05-23T07:22:06.891377+00:00_

Web search results for query: ""SVD-CSP" OR "SVD contextual sparsity" 2026 arxiv LLM predictor"

Links: [{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500"},{"title":"[2406.16635] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/abs/2406.16635"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v2"},{"title":"Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/pdf/2506.16500"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"}]

Based on the search results, I found information about SVD-CSP (SVD Contextual Sparsity Predictors):

SVD Contextual Sparsity Predictors for Fast LLM Inference is a paper by Georgii Serbin, Kirill Koshkin, Zhongao Sun, and others, with a preprint dated March 17, 2026.

The paper presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs. The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math.


REMINDER: You MUST include the sources above in your response to the user us
…[truncated 24 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8823
}
```

</details>

---


### Tool result

_source line 1905 · 2026-05-23T07:22:07.544133+00:00_

Web search results for query: "ProSparse SparseInfer activation sparsity SwiGLU 2024 2025"

Links: [{"title":"Efficient Activation Functions for Sparse LLMs","url":"https://www.emergentmind.com/topics/efficient-activation-functions-for-sparse-llms"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity   within Large Language Models","url":"https://arxiv.org/pdf/2402.13516"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://paperreading.club/page?id=210496"},{"title":"[2402.13516] ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/abs/2402.13516"},{"title":"README.md · SparseLLM/prosparse-llama-2-7b at d298f481c08111bae33c996c6094fad2698744cb","url":"https://huggingface.co/SparseLLM/prosparse-llama-2-7b/blob/d298f481c08111bae33c996c6094fad2698744cb/README.md"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models","url":"https://arxiv.org/html/2402.13516v7"},{"title":"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.180/"},{"title":"SparseLLM/prosparse-llama-2-7b · Hugging Face","url":"https://huggingface.co/SparseLLM/prosparse-llama-2-7b"}]

Based on the web search results, here's what I found about ProSparse, SparseInfer, activation sparsity, and SwiGLU:

## ProSparse Overview

ProSparse is an effective sparsification method to push LLMs for higher activation sparsity without decreasing model performance. After substituting the activation function of LLMs with ReLU, ProSparse adopts progressive sparsity regularization with a factor smoothly increasing along sine curves, which can enhance activation spar
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9325
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-23T07:22:17.818637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1907 · 2026-05-23T07:22:18.471071+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with commonsense gains but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) accounts for the majority of the PPL gap at moderate sparsity (30\%) (upper bound; \S\ref{sec:perlayer}).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-23T07:22:18.621897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1909 · 2026-05-23T07:22:18.672632+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (per-layer Jaccard 32\%).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to PPL but m
…[truncated 3023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1910 · 2026-05-23T07:22:24.442198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1911 · 2026-05-23T07:22:24.743610+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuro
…[truncated 9816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-23T07:22:24.794216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1913 · 2026-05-23T07:22:24.895199+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-23T07:22:30.756250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1915 · 2026-05-23T07:22:31.308968+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1916 · 2026-05-23T07:22:31.309325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1917 · 2026-05-23T07:22:31.811180+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Output-distribution alignment is the primary design dimension at moderate sparsity: signal type accounts for most of the PPL gap (upper bound), with coupling contributing task-dependently (Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A $<$1\% predictor reduces TEAL's PPL by 14.5\% via masks 46--68\% divergent from magnitude; commonsense gains but knowledge regression persist across 7--14B scales.
6	Code and trained predictors will be released upon acceptance.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-23T07:22:31.861893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1919 · 2026-05-23T07:22:31.912502+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three key limitations.
4	\textbf{Sparsity sweet spot.} 30\% appears to be the lowest-degradation level for downstream fidelity; at 40\%, MMLU drops to 35.5\% (vs.\ 40.7\% at 30\%), and at 50\%, all methods collapse to near-random on reasoning tasks. A separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms magnitude-based methods on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting distribution-matching objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Training data homogeneity.} All predictors are trained on WikiText-103 (English Wikipedia). OOD evaluation on C4 shows preserved KL advantage but $31\times$ higher cross-seed variance (CV=6.3\% vs.\ 0.2\% in-domain), indicating domain sensitivity. Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated. All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K--128K) is untested. Our evaluation focuses on perplexity and multiple-choice benchmarks; open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity. The aggravation from 8B to 14B (GSM8K regression deepening from $-$1.3pp to $-$20.1pp) raises concern about scaling to 70B+; wall-clock speedup via sparse kernels also remains future work.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1920 · 2026-05-23T07:22:36.833497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1921 · 2026-05-23T07:22:36.934221+00:00_

1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B~\cite{qwen2024qwen25}) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, HellaSwag, PIQA, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1922 · 2026-05-23T07:26:24.777485+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的实证研究，提供了 KL > BCE 用于稀疏预测训练的有用发现和精心设计的消融实验，但新颖性主要是已知组件的新组合，知识任务上的系统性退化未获充分解释，且缺乏实际加速验证。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支持，但 \"primary design dimension\" 泛化性不足（主要基于 LLaMA-3.1-8B 30%），知识退化机制仅有假说无因果证据 |\n| Excitement | 3/5 (Interesting) | Target-swap ablation 设计巧妙，signal type vs. coupling scope 分解有参考价值，但核心方法是已知技术的直接组合（KL + Gumbel-Sigmoid），实践价值受限于无 wall-clock 加速 |\n| Reproducibility | 4/5 | 实验设置详细（超参数、硬件、seed），承诺开源代码，附录含大量补充实验；部分消融仅 single-seed 略有扣分 |\n| Confidence | 4/5 | 熟悉 activation sparsity prediction 文献，仔细阅读了全文及全部附录 |\n\n---\n\n## 主要优势\n\n**S1. 精心设计的消融框架**\nTarget-swap ablation（C1, Table 3）是本文最突出的实验设计贡献：通过在 BCE 上训练 KL 发现的 oracle masks，成功分离了\"mask 质量\"与\"训练机制\"的贡献。结果令人信服——C1 在 50% 稀疏度下与 KL 仅差 ≤0.79pp（Section 4.4, Table 3），说明 KL 的优势主要来自发现了更好的 mask patterns。\n\n**S2. Signal type vs. coupling scope 分解**\nPer-layer KL 控制实验（K=1, K=4; Section 4.5, Table 4）提供了有价值的分析框架。K=1 per-layer KL 达到 9.05±0.02，仅比 E2E KL（8.81±0.02）差 2.7%，而 per-layer MSE 退化至 18.52±1.68，有力支持了 signal type 是主要因素的论点。\n\n**S3. 诚实的局限性报告**\n论文坦诚报告了 KL 在知识密集任务上的系统性退化（MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B; Section 4.2, Limitations），没有选择性报告。下游指标的统计不确定性（3 seeds, CIs overlap）也被明确说明（Section 4.2: \"we therefore treat PPL as the primary metric and downstream differences as directional evidence\"）。\n\n**S4. 全面的 Related Work**\n引用覆盖了 2024-2026 的主要相关工作，包括 SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA 等近期工作。与 MaskLLM 的区分讨论具体且技术性强（Section 2, three respects a-c）。\n\n**S5. 丰富的附录**\n20 页中有 ~8 页附录（Appendix A-W），涵盖推理延迟、训练收敛、温度敏感性、OOD 评估、mask 可视化等，体现了实验严谨性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Primary design dimension\" claim 泛化性不足\n- 具体位置：Section 5 (Conclusion), Abstract line 5, Section 4.5\n- 问题：结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但主要证据来自 LLaMA-3.1-8B 在 30% 稀疏度下的实验。跨架构验证信号混合：Mistral-7B 确认 PPL 优势但 MMLU 持平（Section 4.6: \"PPL generalizes but MMLU/GSM8K decline\"）；Qwen-2.5-14B 出现严重 GSM8K 退化（−20.1pp）。在论文自己报告的范围内，这个 claim 在知识密集任务上是不成立的——magnitude-based TEAL 在 MMLU/GSM8K 上始终优于 KL predictor（Table 2）。\n- 为什么影响接收：\"primary design dimension\" 是本文的核心结论，如果仅在 PPL + commonsense 维度上成立，需要明确限定适用范围。\n- 建议修改方向：改为 \"primary design dimension *for perplexity and commonsense tasks* at moderate sparsity\"，或更保守地 \"a dominant factor for PPL\" 并讨论为何在知识任务上不成立。\n\n**N2** [critical] 知识任务退化机制缺乏因果解释\n- 具体位置：Section 4.2 \"Knowledge-Task Regression: Hypothesis\", Limitations\n- 问题：论文提出两个假说（训练数据偏差、mode-covering 稀释稀有激活），但 C4 控制实验否定了第一个（Section 4.2: \"confirming the deficit is structural to distribution-matching\"）。第二个假说（mode-covering 稀释 factual knowledge neurons）仅是推测。Constraint experiments（Appendix, remove valley → MMLU +3.4pp）暗示 allocation 而非 loss function 本身是原因，但论文未对此深入追踪。\n- 为什么影响接收：对于自称 \"empirical study characterizing how the training objective shapes sparsity prediction quality\" 的论文，无法解释核心发现中的系统性失败模式是显著的完整性缺陷。\n- 建议修改方向：设计针对性实验区分\"KL loss 本身导致退化\"vs.\"KL 学到的 allocation 分布导致退化\"——例如强制 KL predictor 使用 uniform allocation 并与 constrained allocation 对比 MMLU。（注意：uniform allocation 结果已有，40.7 vs. TEAL 45.86，但未充分分析为何 uniform KL 仍然差 5pp。）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Contribution framing 存在张力\n- 具体位置：Abstract line 8, Introduction line 18 vs. Contribution list (Introduction lines 21-27)\n- 问题：论文反复声明 \"primarily an empirical study\"，但贡献列表包含方法性暗示：\"output-distribution alignment ranking\"（暗示一种新的 ranking 方法）、\"target-swap ablation\"（一种新的实验范式）。更关键的是，论文实际上引入了一个具体的方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），这不仅仅是\"比较现有方法\"。\n- 建议：要么承认方法贡献（\"we introduce a KL-based training framework and conduct the first systematic empirical comparison...\"），要么将贡献列表措辞调整为更明确的实证发现（\"We find that...\"而非 \"An output-distribution alignment ranking...\"）。\n\n**W2** [warning] 术语一致性问题\n- 具体位置：全文\n- 问题：核心概念至少有 5 种表述——\"output-distribution distillation\"（标题）、\"output-distribution alignment\"（Abstract, Conclusion）、\"output-distribution optimization\"（Abstract line 4）、\"KL distillation\"（Section 3 et passim）、\"distribution-matching\"（Limitations）。这些是否指同一概念？如果是，应统一为一个首选术语。\n- 建议：选定一个主术语（建议 \"output-distribution alignment\" 或 \"KL distillation\"），在首次出现时定义并一致使用。\n\n**W3** [warning] Abstract/Introduction 中的数字混淆\n- 具体位置：Introduction line 10\n- 问题：\"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"。68% 和 32% 是同一指标的互补面（Jaccard distance vs. Jaccard similarity），在同一句中出现两个数字造成不必要的混淆。\n- 建议：统一使用一种表述，例如 \"with per-layer Jaccard similarity of only 32%\"。\n\n**W4** [warning] MSE baseline 在 50% 稀疏度下不可靠\n- 具体位置：Table 4, Section 4.5\n- 问题：MSE 50% 报告 PPL 229.26，但脚注 §标注 s123 catastrophic (PPL=15,789)。以此作为 MSE inferiority 的证据（\"$2.05\\times$ worse\"在 30%）是可以的，但 50% 的数字基本不可用。Ablation table 标注了 single-seed，但正文讨论中容易被误解为 robust finding。\n- 建议：在正文讨论 MSE 50% 时明确标注单种子，考虑从主 ablation narrative 中降权或移至附录。\n\n**W5** [warning] 3 seeds 下声称 \"commonsense gains\" 的统计依据不足\n- 具体位置：Abstract line 3 (\"commonsense gains\"), Conclusion line 5, Section 4.2\n- 问题：论文在 Section 4.2 中诚实地指出 \"95% confidence intervals for individual downstream tasks overlap\" 并将下游指标视为 \"directional evidence\"。但 Abstract 和 Conclusion 中 \"commonsense gains\" 的措辞没有这一限定，可能误导读者认为这是统计显著的发现。\n- 建议：Abstract/Conclusion 中加 qualifier，如 \"directional commonsense improvements\" 或 \"commonsense gains (directional; CIs overlap with 3 seeds)\"。\n\n**W6** [warning] Wall-clock speedup 的缺失削弱实际影响力\n- 具体位置：Abstract line 8, Introduction line 18, Appendix A, Limitations\n- 问题：论文坦承 wall-clock speedup 未测量，predictor 本身增加 6.4% latency（Appendix A）。对于一篇关于\"高效推理\"sparsity prediction 的论文，这意味着当前方法 *增加* 而非减少延迟。虽然论文正确地 frame 为 analytical contribution，但 reviewer 和读者期望至少有一个 end-to-end 加速的 feasibility 估算。\n- 建议：即使没有 sparse kernel 实现，也可以基于已有文献（如 TEAL 的 speedup 数据 × KL 的稀疏度优势）给出理论加速估算。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 caption 信息过载（3 个脚注标记 *, †, ‡ + 多个解释条款），建议拆分为 caption 和 table note。\n- **M2**: Figure 2 caption 中 \"82% at 70%\" 这个数据点在正文中几乎未讨论，作为 caption 中的信息显得孤立。\n- **M3**: Section 3.5 (Geometric Penalty Schedule) 中的 deadzone margin ε=0.02 的选择缺乏 justification（仅在附录中有 sensitivity analysis）。\n- **M4**: Introduction line 14 \"with downstream (MMLU 40.7±1.3%, 3-seed)\" 没有 dense baseline 对比（dense MMLU 65.27%），孤立的数字不传达退化幅度。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: 在 50% 稀疏度下，K=4 per-layer KL（44.23）为何 *worse* than K=1（34.85）？论文假说 \"partial coupling amplifies gradient interference\"，但这与 30% 下 coupling 有益的叙事矛盾。是否存在某个 sparsity threshold 使 coupling 从有益变为有害？\n\n**Q2**: K=4 在 MMLU 上超越 E2E KL（42.7 vs. 40.7, Section 4.5）——这是否意味着对知识任务而言，per-layer 训练反而更优？如果是，这对 \"output-distribution alignment is the primary design dimension\" 的结论意味着什么？\n\n**Q3**: Uniform allocation 下 KL predictor MMLU = 40.7% vs. TEAL uniform MMLU = 45.86%（Table 2, 30%）。二者都是 uniform allocation，所以 allocation 策略相同。这 5pp 的差距是否完全归因于 KL loss 本身？如果是，这与 \"allocation contributes\" 的解释（Constraint experiments）矛盾。\n\n**Q4**: Target-swap ablation (C1) 中 s42 oracle 来自 earlier training run (not seed-matched)，而 s123/s456 使用 seed-matched oracles。s42 的 gap (0.65pp) 与 s123/s456 的 gap (≤0.03pp) 差异显著。如何确认 s42 结果不是 oracle provenance artifact？\n\n**Q5**: 论文未测试 reverse KL + Gumbel 在 30% 下的表现（Table 4 标注 \"---\"）。Forward vs. Reverse KL 在 30% 下的差异（8.81 vs. 9.26）是否有统计显著性？考虑到 JSD≈Forward KL (8.90 vs. 8.81)，30% 下 divergence measure 的选择似乎影响不大。\n\n---\n\n## Missing References\n\nRelated Work 覆盖全面，未发现 2025-2026 年的重大遗漏。以下可考虑补充但非必须：\n\n- 无重大遗漏。SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA、COTS、LaRoSA 等近期工作均已引用。\n\n---\n\n## Novelty 边界评估（Director 指定关注点）\n\n**与 MaskLLM 的区分**：\n论文在 Section 2 中清晰区分了三点（a-c: contextual vs static, global allocation, distribution shift robustness），这些是技术上 valid 的区分。Table 1 taxonomy 中 Static×Coupled 仅列 SPON 和 MaskLLM，经查未发现显著遗漏。\n\n**核心问题**：论文的新颖性不在于 KL + Gumbel-Sigmoid 这一 recipe（与 MaskLLM 共享核心组件），而在于 (1) 将其应用于 contextual activation sparsity 这一新领域，以及 (2) 通过 target-swap ablation 和 per-layer KL 控制提供的分析框架。这是 \"empirical + analytical\" 层面的贡献，而非 \"methodological\" 层面的突破。对于 Findings track 足够，但对 Main Conference 可能偏弱。\n\n---\n\n## 评分总结\n\n| 指标 | 分数 |\n|------|------|\n| Overall Assessment | 3.0 (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n**推荐 Findings 的理由**：论文提供了有价值的实证发现（KL > BCE for sparsity prediction, signal type 是 primary factor），实验设计严谨（target-swap ablation 尤为出色），但新颖性局限于已知组件的新应用，核心 claim 的泛化性不足（仅 PPL + commonsense, 非 knowledge tasks），且缺乏实际加速验证。这些发现对 activation sparsity 社区有参考价值，适合 Findings track。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（Round 1）\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的实证研究，提供了 KL > BCE 用于稀疏预测训练的有用发现和精心设计的消融实验，但新颖性主要是已知组件的新组合，知识任务上的系统性退化未获充分解释，且缺乏实际加速验证。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 主要 claim 有实验支持，但 \"primary design dimension\" 泛化性不足（主要基于 LLaMA-3.1-8B 30%），知识退化机制仅有假说无因果证据 |\n| Excitement | 3/5 (Interesting) | Target-swap ablation 设计巧妙，signal type vs. coupling scope 分解有参考价值，但核心方法是已知技术的直接组合（KL + Gumbel-Sigmoid），实践价值受限于无 wall-clock 加速 |\n| Reproducibility | 4/5 | 实验设置详细（超参数、硬件、seed），承诺开源代码，附录含大量补充实验；部分消融仅 single-seed 略有扣分 |\n| Confidence | 4/5 | 熟悉 activation sparsity prediction 文献，仔细阅读了全文及全部附录 |\n\n---\n\n## 主要优势\n\n**S1. 精心设计的消融框架**\nTarget-swap ablation（C1, Table 3）是本文最突出的实验设计贡献：通过在 BCE 上训练 KL 发现的 oracle masks，成功分离了\"mask 质量\"与\"训练机制\"的贡献。结果令人信服——C1 在 50% 稀疏度下与 KL 仅差 ≤0.79pp（Section 4.4, Table 3），说明 KL 的优势主要来自发现了更好的 mask patterns。\n\n**S2. Signal type vs. coupling scope 分解**\nPer-layer KL 控制实验（K=1, K=4; Section 4.5, Table 4）提供了有价值的分析框架。K=1 per-layer KL 达到 9.05±0.02，仅比 E2E KL（8.81±0.02）差 2.7%，而 per-layer MSE 退化至 18.52±1.68，有力支持了 signal type 是主要因素的论点。\n\n**S3. 诚实的局限性报告**\n论文坦诚报告了 KL 在知识密集任务上的系统性退化（MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B; Section 4.2, Limitations），没有选择性报告。下游指标的统计不确定性（3 seeds, CIs overlap）也被明确说明（Section 4.2: \"we therefore treat PPL as the primary metric and downstream differences as directional evidence\"）。\n\n**S4. 全面的 Related Work**\n引用覆盖了 2024-2026 的主要相关工作，包括 SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA 等近期工作。与 MaskLLM 的区分讨论具体且技术性强（Section 2, three respects a-c）。\n\n**S5. 丰富的附录**\n20 页中有 ~8 页附录（Appendix A-W），涵盖推理延迟、训练收敛、温度敏感性、OOD 评估、mask 可视化等，体现了实验严谨性。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"Primary design dimension\" claim 泛化性不足\n- 具体位置：Section 5 (Conclusion), Abstract line 5, Section 4.5\n- 问题：结论称 \"Output-distribution alignment is the primary design dimension at moderate sparsity\"，但主要证据来自 LLaMA-3.1-8B 在 30% 稀疏度下的实验。跨架构验证信号混合：Mistral-7B 确认 PPL 优势但 MMLU 持平（Section 4.6: \"PPL generalizes but MMLU/GSM8K decline\"）；Qwen-2.5-14B 出现严重 GSM8K 退化（−20.1pp）。在论文自己报告的范围内，这个 claim 在知识密集任务上是不成立的——magnitude-based TEAL 在 MMLU/GSM8K 上始终优于 KL predictor（Table 2）。\n- 为什么影响接收：\"primary design dimension\" 是本文的核心结论，如果仅在 PPL + commonsense 维度上成立，需要明确限定适用范围。\n- 建议修改方向：改为 \"primary design dimension *for perplexity and commonsense tasks* at moderate sparsity\"，或更保守地 \"a dominant factor for PPL\" 并讨论为何在知识任务上不成立。\n\n**N2** [critical] 知识任务退化机制缺乏因果解释\n- 具体位置：Section 4.2 \"Knowledge-Task Regression: Hypothesis\", Limitations\n- 问题：论文提出两个假说（训练数据偏差、mode-covering 稀释稀有激活），但 C4 控制实验否定了第一个（Section 4.2: \"confirming the deficit is structural to distribution-matching\"）。第二个假说（mode-covering 稀释 factual knowledge neurons）仅是推测。Constraint experiments（Appendix, remove valley → MMLU +3.4pp）暗示 allocation 而非 loss function 本身是原因，但论文未对此深入追踪。\n- 为什么影响接收：对于自称 \"empirical study characterizing how the training objective shapes sparsity prediction quality\" 的论文，无法解释核心发现中的系统性失败模式是显著的完整性缺陷。\n- 建议修改方向：设计针对性实验区分\"KL loss 本身导致退化\"vs.\"KL 学到的 allocation 分布导致退化\"——例如强制 KL predictor 使用 uniform allocation 并与 constrained allocation 对比 MMLU。（注意：uniform allocation 结果已有，40.7 vs. TEAL 45.86，但未充分分析为何 uniform KL 仍然差 5pp。）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Contribution framing 存在张力\n- 具体位置：Abstract line 8, Introduction line 18 vs. Contribution list (Introduction lines 21-27)\n- 问题：论文反复声明 \"primarily an empirical study\"，但贡献列表包含方法性暗示：\"output-distribution alignment ranking\"（暗示一种新的 ranking 方法）、\"target-swap ablation\"（一种新的实验范式）。更关键的是，论文实际上引入了一个具体的方法（KL predictor + Gumbel-Sigmoid for contextual sparsity），这不仅仅是\"比较现有方法\"。\n- 建议：要么承认方法贡献（\"we introduce a KL-based training framework and conduct the first systematic empirical comparison...\"），要么将贡献列表措辞调整为更明确的实证发现（\"We find that...\"而非 \"An output-distribution alignment ranking...\"）。\n\n**W2** [warning] 术语一致性问题\n- 具体位置：全文\n- 问题：核心概念至少有 5 种表述——\"output-distribution distillation\"（标题）、\"output-distribution alignment\"（Abstract, Conclusion）、\"output-distribution optimization\"（Abstract line 4）、\"KL distillation\"（Section 3 et passim）、\"distribution-matching\"（Limitations）。这些是否指同一概念？如果是，应统一为一个首选术语。\n- 建议：选定一个主术语（建议 \"output-distribution alignment\" 或 \"KL distillation\"），在首次出现时定义并一致使用。\n\n**W3** [warning] Abstract/Introduction 中的数字混淆\n- 具体位置：Introduction line 10\n- 问题：\"KL's coupled gradients discover neuron importance patterns that diverge 68% from magnitude-based masks (per-layer Jaccard 32%)\"。68% 和 32% 是同一指标的互补面（Jaccard distance vs. Jaccard similarity），在同一句中出现两个数字造成不必要的混淆。\n- 建议：统一使用一种表述，例如 \"with per-layer Jaccard similarity of only 32%\"。\n\n**W4** [warning] MSE baseline 在 50% 稀疏度下不可靠\n- 具体位置：Table 4, Section 4.5\n- 问题：MSE 50% 报告 PPL 229.26，但脚注 §标注 s123 catastrophic (PPL=15,789)。以此作为 MSE inferiority 的证据（\"$2.05\\times$ worse\"在 30%）是可以的，但 50% 的数字基本不可用。Ablation table 标注了 single-seed，但正文讨论中容易被误解为 robust finding。\n- 建议：在正文讨论 MSE 50% 时明确标注单种子，考虑从主 ablation narrative 中降权或移至附录。\n\n**W5** [warning] 3 seeds 下声称 \"commonsense gains\" 的统计依据不足\n- 具体位置：Abstract line 3 (\"commonsense gains\"), Conclusion line 5, Section 4.2\n- 问题：论文在 Section 4.2 中诚实地指出 \"95% confidence intervals for individual downstream tasks overlap\" 并将下游指标视为 \"directional evidence\"。但 Abstract 和 Conclusion 中 \"commonsense gains\" 的措辞没有这一限定，可能误导读者认为这是统计显著的发现。\n- 建议：Abstract/Conclusion 中加 qualifier，如 \"directional commonsense improvements\" 或 \"commonsense gains (directional; CIs overlap with 3 seeds)\"。\n\n**W6** [warning] Wall-clock speedup 的缺失削弱实际影响力\n- 具体位置：Abstract line 8, Introduction line 18, Appendix A, Limitations\n- 问题：论文坦承 wall-clock speedup 未测量，predictor 本身增加 6.4% latency（Appendix A）。对于一篇关于\"高效推理\"sparsity prediction 的论文，这意味着当前方法 *增加* 而非减少延迟。虽然论文正确地 frame 为 analytical contribution，但 reviewer 和读者期望至少有一个 end-to-end 加速的 feasibility 估算。\n- 建议：即使没有 sparse kernel 实现，也可以基于已有文献（如 TEAL 的 speedup 数据 × KL 的稀疏度优势）给出理论加速估算。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 caption 信息过载（3 个脚注标记 *, †, ‡ + 多个解释条款），建议拆分为 caption 和 table note。\n- **M2**: Figure 2 caption 中 \"82% at 70%\" 这个数据点在正文中几乎未讨论，作为 caption 中的信息显得孤立。\n- **M3**: Section 3.5 (Geometric Penalty Schedule) 中的 deadzone margin ε=0.02 的选择缺乏 justification（仅在附录中有 sensitivity analysis）。\n- **M4**: Introduction line 14 \"with downstream (MMLU 40.7±1.3%, 3-seed)\" 没有 dense baseline 对比（dense MMLU 65.27%），孤立的数字不传达退化幅度。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: 在 50% 稀疏度下，K=4 per-layer KL（44.23）为何 *worse* than K=1（34.85）？论文假说 \"partial coupling amplifies gradient interference\"，但这与 30% 下 coupling 有益的叙事矛盾。是否存在某个 sparsity threshold 使 coupling 从有益变为有害？\n\n**Q2**: K=4 在 MMLU 上超越 E2E KL（42.7 vs. 40.7, Section 4.5）——这是否意味着对知识任务而言，per-layer 训练反而更优？如果是，这对 \"output-distribution alignment is the primary design dimension\" 的结论意味着什么？\n\n**Q3**: Uniform allocation 下 KL predictor MMLU = 40.7% vs. TEAL uniform MMLU = 45.86%（Table 2, 30%）。二者都是 uniform allocation，所以 allocation 策略相同。这 5pp 的差距是否完全归因于 KL loss 本身？如果是，这与 \"allocation contributes\" 的解释（Constraint experiments）矛盾。\n\n**Q4**: Target-swap ablation (C1) 中 s42 oracle 来自 earlier training run (not seed-matched)，而 s123/s456 使用 seed-matched oracles。s42 的 gap (0.65pp) 与 s123/s456 的 gap (≤0.03pp) 差异显著。如何确认 s42 结果不是 oracle provenance artifact？\n\n**Q5**: 论文未测试 reverse KL + Gumbel 在 30% 下的表现（Table 4 标注 \"---\"）。Forward vs. Reverse KL 在 30% 下的差异（8.81 vs. 9.26）是否有统计显著性？考虑到 JSD≈Forward KL (8.90 vs. 8.81)，30% 下 divergence measure 的选择似乎影响不大。\n\n---\n\n## Missing References\n\nRelated Work 覆盖全面，未发现 2025-2026 年的重大遗漏。以下可考虑补充但非必须：\n\n- 无重大遗漏。SVD-CSP (Serbin et al., 2026)、SparseInfer、ProSparse、SparseLoRA、COTS、LaRoSA 等近期工作均已引用。\n\n---\n\n## Novelty 边界评估（Director 指定关注点）\n\n**与 MaskLLM 的区分**：\n论文在 Section 2 中清晰区分了三点（a-c: contextual vs static, global allocation, distribution shift robustness），这些是技术上 valid 的区分。Table 1 taxonomy 中 Static×Coupled 仅列 SPON 和 MaskLLM，经查未发现显著遗漏。\n\n**核心问题**：论文的新颖性不在于 KL + Gumbel-Sigmoid 这一 recipe（与 MaskLLM 共享核心组件），而在于 (1) 将其应用于 contextual activation sparsity 这一新领域，以及 (2) 通过 target-swap ablation 和 per-layer KL 控制提供的分析框架。这是 \"empirical + analytical\" 层面的贡献，而非 \"methodological\" 层面的突破。对于 Findings track 足够，但对 Main Conference 可能偏弱。\n\n---\n\n## 评分总结\n\n| 指标 | 分数 |\n|------|------|\n| Overall Assessment | 3.0 (Findings) |\n| Soundness | 3/5 |\n| Excitement | 3/5 |\n| Reproducibility | 4/5 |\n| Confidence | 4/5 |\n\n**推荐 Findings 的理由**：论文提供了有价值的实证发现（KL > BCE for sparsity prediction, signal type 是 primary factor），实验设计严谨（target-swap ablation 尤为出色），但新颖性局限于已知组件的新应用，核心 claim 的泛化性不足（仅 PPL + commonsense, 非 knowledge tasks），且缺乏实际加速验证。这些发现对 activation sparsity 社区有参考价值，适合 Findings track。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1923 · 2026-05-23T07:26:28.892574+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4115
}
```

</details>

---


### Assistant

_source line 1924 · 2026-05-23T07:26:38.544992+00:00_

审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings level)

核心判断：
- **优点**：Target-swap ablation 设计精巧，signal type vs. coupling scope 分解有价值，实验诚实全面
- **主要问题**：(1) "primary design dimension" claim 泛化性不足——知识任务上 TEAL 始终优于 KL predictor；(2) 知识退化的因果机制未解释；(3) 核心方法是已知组件（KL + Gumbel-Sigmoid）的新组合而非方法论突破
- **次要问题**：术语不一致（5 种表述指同一概念）、3 seeds 下 "commonsense gains" 措辞过强、MSE 50% 单种子不可靠、无 wall-clock 加速验证
- **格式合规**：8 页正文限制 ✓，ACL 模板 ✓，匿名性 ✓，Limitations/Ethics ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 47

## Round 47

12 recorded events


### User

_source line 1925 · 2026-05-23T07:30:35.726509+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（Round 1）

**Overall**: 3.5 (Borderline Conference)

### 官方维度打分
| 维度 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 3/5 |
| Reproducibility | 4/5 |
| Confidence | 4/5 |

### Must-Fix 问题
**N1** [critical] K=1 per-layer 分解的 train-inference mismatch 严重污染 "signal type accounts for majority" 结论。K=1 训练时仅 1/32 层被 mask，推理时 32/32 层全部 mask。K=4 修正不充分（仍仅 12.5%）。K=4 MMLU 系统性超过 E2E 说明 mismatch 引入不可预测 artifact。K-curve 中 K=1,2,8,16,32 均为 single-seed (s42)。建议：(1) K-curve 全部 3-seed；(2) progressive K-scheduling；(3) 将结论降级为 "exploratory observation"。

**N2** [critical] 3-seed 下游指标统计功效不足。Table 14 显示 50% Global MMLU=35.7±9.5（σ=9.5pp）。30% uniform MMLU σ≈1.3pp 在 n=3 下 95% CI 为 ±2.9pp，KL vs BCE 差异完全落在 CI 内。GSM8K 7.5% 接近 floor。按 ARR guidelines R5 要求 error bars/significance tests，论文未满足。建议：(1) 至少 5 seeds；(2) bootstrap/t-test CI；(3) 下游声明加统计限定语。

### Should-Fix 问题
**W1** [warning] C1 target-swap ablation 存在未隔离混淆变量——soft→hard 二值化同时改变了 mask 来源和 mask 表示。BCE+Gumbel (32.22) vs 标准 BCE (27.97) 差 15% 说明 Gumbel 表示本身有显著影响。

**W2** [warning] Knowledge-task regression 机制分析不充分。C4 控制仅 1 seed。"mode-covering dilutes rare activations" 是推测。跨 scale 退步（8B MMLU −5.2pp, 14B GSM8K −20pp）暗示根本限制但未提供缓解路径。

**W3** [warning] 实验覆盖度缺口且 Limitations 未覆盖：(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估。

**W4** [warning] Table 14 MMLU 数值不一致：Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7。同一条件下均值差 7.4pp、标准差差一个数量级。

### 小问题
- Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低。
- "the first decomposition" 措辞应更审慎。
- Table 1 Taxonomy 暗示方法新颖性来自组合已有技术。
- MSE baseline cherry-pick 风险（仅报告 s42）。

### 主要优势
1. 实用且一致的 PPL 改进（14.5% over TEAL, 跨架构一致）。
2. 罕见的 ablation 深度（20+ 附录部分）。
3. 诚实的负面结果报告。
4. 有用的概念框架（Table 1 taxonomy + gradient analysis）。
5. 充分的可复现性信息。

### Questions
**Q1**: K=4 MMLU 超过 E2E 的机制？如果来自 sparsity distribution artifact，是否削弱 decomposition 结论？
**Q2**: Compensation network 不提升质量的原因？为何不能恢复 knowledge-intensive 性能？
**Q3**: 包含 predictor + sparse FFN 的端到端 wall-clock latency（batch_size ∈ {1,4,16,32}）？
**Q4**: 排除 MMLU σ=9.5 的 outlier seed 后，Global allocation 结论是否仍成立？
**Q5**: 是否考虑 token-level adaptive sparsity 缓解 knowledge regression？

### Missing References
未发现重大遗漏。PowerInfer 可供参考但非必须。

---

请逐条回应上述所有 Must-Fix、Should-Fix、Minor、Strengths、Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1926 · 2026-05-23T07:32:04.278647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": "140",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "offset": "140",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1927 · 2026-05-23T07:32:04.680515+00:00_

140	Per-layer KL ($K{=}4$) & 8.89$\pm$0.01 & 44.23 & +32.44 \\ % exp_id: perlayer_kl_k4_3seed, perlayer_kl_k4_50_s42
141	\midrule
142	\multicolumn{4}{l}{\textit{BCE-based variants}} \\
143	BCE (no compensation) & 15.71 & 27.97 & +16.18 \\ % exp_id: bce30_uniform_s42, eval_bce_v3_s42
144	BCE + Gumbel (no penalty) & --- & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
145	BCE + Gumbel + Penalty & --- & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
146	BCE + STE & --- & 60.54 & +48.75 \\ % exp_id: bce_ste_s42
147	\bottomrule
148	\end{tabular}}
149	\end{table}
150	
151	\paragraph{Relaxation, Divergence, and SPON.}
152	At 50\%, Gumbel-Sigmoid outperforms STE~\cite{bengio2013ste} by 33.8\% (11.79 vs.\ 15.77); forward KL outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with mode-covering~\cite{gu2024minillm}. % exp_id: ste_baseline_s42, jsd_ablation_s42, reverse_kl_ablation_s42
153	At 30\%, forward KL (8.81) and JSD (8.90) are near-identical, both outperforming reverse KL (9.26) and MSE (18.52$\pm$1.68). % exp_id: kl30_ablation_s42, jsd30_ablation_s42, rkl30_ablation_s42, mse30_uniform_s42, mse30_3seed
154	KL--JSD near-equivalence suggests the divergence measure matters less than optimizing through the output distribution; coupling scope provides additional downstream benefits (\S\ref{sec:perlayer}). % exp_id: bce30_uniform_s42, rkl30_downstream_3seed
155	\paragraph{Per-Layer KL: Decomposing Signal Type and Coupling Scope.}
156	\label{sec:perlayer}
157	To isolate cross-layer coupling, we train per-layer KL predictors that mask $K$ random layers per step and compute KL on the full model output, preserving the output-distribution signal without cross-layer gradients.
158	At $K{=}1$, per-layer KL achieves 9.05$\pm$0.02, within 2.7\% of end-to-end KL (8.81$\pm$0.02), while per-layer MSE degrades to 18.52$\pm$1.68 ($2.05\times$ worse). For PPL, signal type\footnote{We use ``signal type'' as shorthand for the training objective's optimization tar
…[truncated 4033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1928 · 2026-05-23T07:32:04.680883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1929 · 2026-05-23T07:32:04.731435+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead
…[truncated 2514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1930 · 2026-05-23T07:32:09.403929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "200",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "200",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 1931 · 2026-05-23T07:32:09.454548+00:00_

200	\end{tabular}
201	\end{table}
202	
203	
204	\section{Per-Layer Retention Analysis}
205	\label{app:retention}
206	
207	\begin{figure}[h]
208	\centering
209	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
210	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
211	\label{fig:retention}
212	\end{figure}
213	
214	
215	\section{Training Stability}
216	\label{app:stability}
217	
218	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
219	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
220	
221	Under global allocation at 50\%, MMLU is $28.3 \pm 0.7$\%; the near-random performance is capacity-limited rather than seed-sensitive ($\sigma$=0.7pp vs.\ 9.5pp at 30\% global). % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
222	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
223	
224	\subsection{Cross-Seed Mask Consistency}
225	\label{app:cross_seed_jaccard}
226	
227	To assess whether KL predictors discover consistent mask patterns across initializations, we compute pairwise Jaccard distances among three independently trained KL predictors (s42/s123/s456) at 30\% uniform allocation (100 sequences, WikiText-2 validation). % exp_id: cross_seed_jaccard_kl30
…[truncated 7448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1932 · 2026-05-23T07:32:15.431416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": "320",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
    "offset": "320",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-23T07:32:15.483633+00:00_

320	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & \textbf{75.01} & \textbf{77.37} \\ % exp_id: qwen14b_kl30_s42
321	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 & 70.51 & 74.70 \\ % exp_id: qwen14b_teal30_eval
322	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} & 53.43 & 68.28 \\ % exp_id: qwen14b_bce30_s42_eval
323	\midrule
324	\multicolumn{8}{l}{\emph{Uniform allocation}} \\
325	KL (Ours) & \textbf{7.90} & 53.50 & \textbf{72.82} & 63.55 & 32.0$\pm$5.2 & \textbf{72.68$\pm$0.2} & \textbf{76.01$\pm$1.1} \\ % exp_id: qwen14b_kl30_uniform (v3/v5 3-seed, HS/PIQA updated from v3/v5)
326	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & \textbf{52.1} & 67.72 & 74.70 \\ % exp_id: qwen14b_teal30_uniform
327	\bottomrule
328	\end{tabular}}
329	\end{table}
330	
331	Under global allocation, BCE's HellaSwag drops to 53.43\% ($-$17pp vs.\ TEAL), indicating that the magnitude-based predictor's mask quality degrades severely when combined with non-uniform budget distribution at 14B scale. % exp_id: qwen14b_bce30_s42_eval, qwen14b_teal30_eval
332	
333	\section{Full Allocation Analysis}
334	\label{app:alloc_full}
335	
336	\begin{table}[t]
337	\centering
338	\caption{Allocation summary (LLaMA-3.1-8B). $\pm$: 3-seed; $^\ast$high seed variance.}
339	\label{tab:phase}
340	\footnotesize
341	\begin{tabular}{llcc}
342	\toprule
343	Sparsity & Allocation & PPL$\downarrow$ & MMLU \\
344	\midrule
345	\multirow{2}{*}{30\%}
346	& Global & 8.96$\pm$0.02 & 35.7$\pm$9.5$^\ast$ \\ % exp_id: kl30_3seed_global
347	& Uniform & \textbf{8.81$\pm$0.02} & \textbf{40.7$\pm$1.3} \\ % exp_id: bench_kl30_uniform
348	\midrule
349	\multirow{2}{*}{50\%}
350	& Global & \textbf{11.84$\pm$0.15} & \textbf{28.3$\pm$0.7} \\ % exp_id: bench_kl50_global, kl50_global_s123_downstream_v2, kl50_global_s456_eval
351	& Uniform & 11.92$\pm$0.07 & 28.0$\pm$0.6 \\ % exp_id: multi_seed_kl50_uniform
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	Table~\ref{tab:phase_full}
…[truncated 10837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1934 · 2026-05-23T07:34:30.242406+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n[AGREE] R1-S1（PPL 改进一致性）: 同意。KL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势（Table 2, Table 16/Appendix N, Table 13/Appendix K），这是本文最 robust 的发现。\n\n[AGREE] R1-S2（罕见的 ablation 深度）: 同意。20 页附录含 Appendix A-W，覆盖推理延迟、bottleneck 敏感性、温度调度、OOD、mask 可视化、cross-seed consistency 等，远超同类工作的通常标准。\n\n[AGREE] R1-S3（诚实的负面结果）: 同意。这是本文的一个显著优点。MMLU −5.2pp (8B)、GSM8K −20.1pp (14B) 均在 Abstract、Section 4.2、Limitations 中明确报告，没有选择性汇报。\n\n[AGREE] R1-S4（概念框架）: 同意。Table 1 taxonomy（signal type × coupling scope）和 Section 3.6 的 gradient analysis 提供了有用的分析框架。但需注意 taxonomy 本身主要是对现有方法的分类整理，而非方法论创新。\n\n[AGREE] R1-S5（可复现性）: 同意。超参数、硬件配置（RTX PRO 6000 Blackwell, 96GB）、训练步数、seed 选择均有明确记录。承诺开源进一步增强可复现性。\n\n---\n\n### Must-Fix 问题回应\n\n[AGREE] R1-N1（K=1 per-layer 分解的 train-inference mismatch）:\n同意这是本文 signal type decomposition 的核心方法论弱点。具体证据：\n\n1. **K=1 confound 论文已承认**：Section 4.5 明确说 \"an upper bound, as the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)\"。\n2. **K=4 修正不充分**：R1 指出 K=4 仍仅 12.5% 层被 mask，这个批评是合理的。论文的 K=4 3-seed 结果（8.89±0.01）接近 E2E（8.81±0.02），PPL gap 为 67% closure，但这并不能完全消除 mismatch confound。\n3. **MMLU anomaly 削弱分解可靠性**：K=4 MMLU（42.7±1.4）系统性超过 E2E（40.7±1.3）across all 3 seeds（Section 4.5），论文将其归因于 \"K=4's near-uniform allocation matching uniform inference\"。如果分解本身产生 artifact（MMLU 反超），那么其他维度的分解结果同样可能受 artifact 影响。\n4. **K-curve single-seed**：Appendix W 的 K-curve（K=1,2,8,16,32）均为 s42 单种子，non-monotonic pattern（K=16 PPL 8.67 < E2E 8.81）可能是 seed-specific artifact。\n\n**补充意见**：我在自己的审稿中（N1）也指出了 \"primary design dimension\" 的泛化性不足。R1 建议 \"(3) 将结论降级为 exploratory observation\" 是合理的最小修改。更理想的修改是在论文中明确标注 K=1 结果为 upper bound，K=4 为 partial deconfounding，并承认在无 K=32（即 E2E，已有）到 K=1 之间的完整 multi-seed K-curve 之前，signal type vs. coupling 的精确分解仍是 tentative。\n\n---\n\n[AGREE] R1-N2（3-seed 下游指标统计功效不足）:\n同意。具体证据：\n\n1. **σ=9.5pp on n=3**：Table 2 中 30% KL global MMLU = 35.7±9.5，意味着 95% CI ≈ ±23.6pp（t-distribution, df=2），基本没有统计信息量。\n2. **KL vs. TEAL 差异在 CI 内**：30% uniform MMLU: KL 40.7±1.3 vs. TEAL 45.86。差异 5.16pp，n=3 下 95% CI for KL ≈ [37.5, 43.9]，不包含 45.86。但这仅是单侧比较（TEAL 是确定性的单次运行，无方差估计），严格来说 p-value 无法计算。\n3. **论文内部承认但外部声明不一致**：Section 4.2 诚实地说 \"directional evidence\"，但 Abstract（\"commonsense gains\"）和 Conclusion（\"commonsense gains\"）未带此限定。\n\n**补充意见**：我在自己的审稿中（W5）也提出了相同关切。R1 的建议 \"(3) 下游声明加统计限定语\" 是必要的。关于 \"(1) 至少 5 seeds\"，这是理想方案但可能受限于计算资源，至少应增加 bootstrap CI 的报告。\n\n---\n\n### Should-Fix 问题回应\n\n[AGREE] R1-W1（C1 target-swap ablation 的 soft→hard 混淆变量）:\n部分同意。论文在 Section 4.4 确实承认了这一 confound：\"binarizing oracle soft logits (>0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask patterns rather than full predictor knowledge.\" BCE+Gumbel（32.22）vs 标准 BCE（27.97）的 15% 差距说明 Gumbel 表示本身有影响。\n\n但 C1 的核心发现仍然成立：即使存在 representation confound，KL-derived hard masks + simple BCE 训练（C1）仍然远优于 magnitude-derived hard masks + BCE（15.71 at 30%），说明 mask 质量（哪些 neuron 被选中）是关键因素。Gumbel 的 representation 效应只部分解释了 KL 优势，不能完全解释。\n\n**建议**：作者应增加一个 \"KL-derived masks + BCE without Gumbel\" 的 ablation 以完全隔离 mask 质量 vs. mask 表示。或者更明确地限定 C1 结论的适用范围。\n\n---\n\n[AGREE] R1-W2（Knowledge-task regression 分析不充分）:\n强烈同意，这与我的 N2 高度一致。C4 控制实验仅 1 seed（Section 4.2: \"MMLU 40.0%, GSM8K 4.1%\"），排除训练数据假说的证据不充分。\"mode-covering dilutes rare activations\" 仍是推测。\n\n关键数据点：KL uniform MMLU = 40.7 vs. TEAL uniform MMLU = 45.86（Table 2, 30%），二者使用相同的 uniform allocation 策略。这 5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身的某种属性。论文未对此进行因果分析。\n\n---\n\n[REBUT] R1-W3（实验覆盖度缺口且 Limitations 未覆盖）:\nR1 声称 \"(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估\" 未被 Limitations 覆盖。这与事实不符。\n\nLimitations 段落（page 9）明确写道：\n- \"open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity\"（覆盖第 1 点）\n- \"All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K-128K) is untested\"（覆盖第 2 点）\n- \"Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated\"（覆盖第 3 点）\n\n三个实验覆盖度缺口均已在 Limitations 中明确承认。R1 的批评在 \"这些是缺口\" 方面是正确的，但 \"Limitations 未覆盖\" 的判断有误。\n\n---\n\n[REBUT] R1-W4（Table 14 MMLU 数值不一致）:\nR1 称 \"Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7\"。\n\n经我核实 LaTeX 源文件（appendix.tex lines 336-354），Table 14（tab:phase）的实际内容是：\n- **30% Global**: MMLU = 35.7±9.5*\n- **30% Uniform**: MMLU = 40.7±1.3\n- **50% Global**: MMLU = 28.3±0.7\n- **50% Uniform**: MMLU = 28.0±0.6\n\n**35.7±9.5 是 30% Global 的数值，不是 50% Global。** R1 误读了表格行标签。Table 14 中 50% Global MMLU = 28.3±0.7，与 Appendix F（Training Stability, appendix.tex line 221: \"Under global allocation at 50%, MMLU is 28.3±0.7%\"）以及 Table 2 主表完全一致。不存在数据不一致。\n\n---\n\n### 小问题回应\n\n[REBUT] R1-Minor-1（Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低）:\nR1 说 \"coupling 应提高 SNR\"，但论文并未做此预测。Section 3.6 明确写道：\"BCE maintains consistently higher SNR than KL throughout training (2.3× at convergence), indicating that KL's quality advantage does not arise from cleaner gradient signals. Rather, KL's end-to-end coupled gradient serves as a search mechanism.\" Figure 5（Appendix H）显示这是 consistent pattern，不是 anomaly。论文的叙事是 \"KL 胜出 despite 更低 SNR\"，而非 \"KL 因更高 SNR 而胜出\"。这是论文的一个 deliberate finding，不是张力。\n\n[AGREE] R1-Minor-2（\"the first decomposition\" 措辞应更审慎）:\n同意。Section 2 写 \"to our knowledge, the first decomposition of signal type vs. coupling scope\"。虽然有 \"to our knowledge\" 限定，但 \"first\" 仍然是强 claim。建议改为 \"a systematic decomposition\" 或 \"we provide what we believe is the first...\"\n\n[AGREE] R1-Minor-3（Table 1 Taxonomy 暗示新颖性来自组合已有技术）:\n同意。这与我的 novelty 边界评估一致。Table 1 诚实地展示了本文方法的位置（Per-token × Coupled），而每个维度上的技术（per-token prediction, KL distillation, Gumbel-Sigmoid）均非新发明。新颖性在于 combination + empirical characterization，这是 Findings 级别的贡献。\n\n[AGREE] R1-Minor-4（MSE baseline cherry-pick 风险）:\n部分同意。MSE 50% 仅报告 s42（PPL 229.26），s123 catastrophic（PPL=15,789, Appendix G, appendix.tex line 244）。论文通过脚注标注了这一点（Table 4: \"§MSE 50%: s42 only; s123 catastrophic\"），保持了透明度。但 30% MSE 3-seed mean 18.52±1.68（s42=20.43, s123=17.73, s456=17.39）是合理的 baseline。风险在于读者可能忽略脚注，误以为 MSE 50% 是 robust result。\n\n---\n\n### Questions 回应\n\n[AGREE] R1-Q1（K=4 MMLU 超过 E2E 的机制）:\n这是我在 Q2 中提出的相同问题。论文归因于 \"K=4's near-uniform allocation matching uniform inference\"（Section 4.5）。如果正确，这意味着 E2E KL 学到的 non-uniform allocation 实际上 *伤害* MMLU，而 per-layer 训练偶然产生了更好的 allocation。这确实削弱了 \"output-distribution alignment is the primary design dimension\" 的全面性——至少对 knowledge tasks，allocation 可能比 signal type 更重要。\n\n[AGREE] R1-Q2（Compensation network 为何无效）:\n有效问题。论文仅说 \"provides no benefit\"（Section 4.5, Appendix J），但未解释 *为什么*。可能的原因：(1) KL predictor 已经优化了 output distribution，compensation network 没有剩余误差可修正；(2) compensation 的 per-layer MSE 目标与 KL 的 output-distribution 目标不兼容。作者应至少讨论机制。\n\n[AGREE] R1-Q3（端到端 wall-clock latency）:\n同意需要更多 batch size 的延迟数据。Appendix A（Table 5）仅报告 batch=1 的结果。对于实际部署，batch>1 的延迟特征可能完全不同（predictor overhead 可能被摊薄，但 mask intersection 成本可能增加）。\n\n[AGREE] R1-Q4（排除 MMLU σ=9.5 的 outlier seed 后 Global allocation 结论是否成立）:\n有效问题。Table 15（Appendix L, tab:phase_full）显示 30% Global MMLU seeds span 25.3--43.5%。如果 25.3% 是 outlier，排除后 mean 会显著上升。但 n=3 下排除 1 个 seed（变成 n=2）更不可靠。这再次印证 R1-N2 的 seed 不足问题。\n\n[AGREE] R1-Q5（token-level adaptive sparsity 缓解 knowledge regression）:\n有趣的方向。当前方法使用 model-level fixed sparsity target。Token-level adaptive sparsity（对 knowledge-intensive tokens 降低 sparsity）可能缓解 MMLU 退化。论文未讨论此方向，可列为 future work。\n\n---\n\n### 总体评价\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：\n1. R1 对 PPL 改进的实用价值评价略高，我认为缺乏 wall-clock speedup 显著削弱实际影响力。\n2. 我对 \"primary design dimension\" claim 的泛化性更为怀疑，尤其是在 knowledge tasks 上的系统性退化。\n\n两位 reviewer 的核心共识：\n- PPL 改进 robust 且一致（共识优势）\n- K=1 decomposition 存在 train-inference mismatch confound（共识弱点）\n- 3 seeds 不足以支持下游 claims（共识弱点）\n- Knowledge regression 缺乏因果解释（共识弱点）\n- Table 1 taxonomy 的新颖性在于组合而非原创技术（共识判断）\n- 适合 Findings track（3.0-3.5 区间）",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Strengths 回应\n\n[AGREE] R1-S1（PPL 改进一致性）: 同意。KL predictor 在 LLaMA-3.1-8B（14.5%）、Mistral-7B（17.3%）、Qwen-2.5-14B 上均展示一致的 PPL 优势（Table 2, Table 16/Appendix N, Table 13/Appendix K），这是本文最 robust 的发现。\n\n[AGREE] R1-S2（罕见的 ablation 深度）: 同意。20 页附录含 Appendix A-W，覆盖推理延迟、bottleneck 敏感性、温度调度、OOD、mask 可视化、cross-seed consistency 等，远超同类工作的通常标准。\n\n[AGREE] R1-S3（诚实的负面结果）: 同意。这是本文的一个显著优点。MMLU −5.2pp (8B)、GSM8K −20.1pp (14B) 均在 Abstract、Section 4.2、Limitations 中明确报告，没有选择性汇报。\n\n[AGREE] R1-S4（概念框架）: 同意。Table 1 taxonomy（signal type × coupling scope）和 Section 3.6 的 gradient analysis 提供了有用的分析框架。但需注意 taxonomy 本身主要是对现有方法的分类整理，而非方法论创新。\n\n[AGREE] R1-S5（可复现性）: 同意。超参数、硬件配置（RTX PRO 6000 Blackwell, 96GB）、训练步数、seed 选择均有明确记录。承诺开源进一步增强可复现性。\n\n---\n\n### Must-Fix 问题回应\n\n[AGREE] R1-N1（K=1 per-layer 分解的 train-inference mismatch）:\n同意这是本文 signal type decomposition 的核心方法论弱点。具体证据：\n\n1. **K=1 confound 论文已承认**：Section 4.5 明确说 \"an upper bound, as the K=1 control conflates coupling removal with train-inference mismatch (training 1/32 layers; inference all 32)\"。\n2. **K=4 修正不充分**：R1 指出 K=4 仍仅 12.5% 层被 mask，这个批评是合理的。论文的 K=4 3-seed 结果（8.89±0.01）接近 E2E（8.81±0.02），PPL gap 为 67% closure，但这并不能完全消除 mismatch confound。\n3. **MMLU anomaly 削弱分解可靠性**：K=4 MMLU（42.7±1.4）系统性超过 E2E（40.7±1.3）across all 3 seeds（Section 4.5），论文将其归因于 \"K=4's near-uniform allocation matching uniform inference\"。如果分解本身产生 artifact（MMLU 反超），那么其他维度的分解结果同样可能受 artifact 影响。\n4. **K-curve single-seed**：Appendix W 的 K-curve（K=1,2,8,16,32）均为 s42 单种子，non-monotonic pattern（K=16 PPL 8.67 < E2E 8.81）可能是 seed-specific artifact。\n\n**补充意见**：我在自己的审稿中（N1）也指出了 \"primary design dimension\" 的泛化性不足。R1 建议 \"(3) 将结论降级为 exploratory observation\" 是合理的最小修改。更理想的修改是在论文中明确标注 K=1 结果为 upper bound，K=4 为 partial deconfounding，并承认在无 K=32（即 E2E，已有）到 K=1 之间的完整 multi-seed K-curve 之前，signal type vs. coupling 的精确分解仍是 tentative。\n\n---\n\n[AGREE] R1-N2（3-seed 下游指标统计功效不足）:\n同意。具体证据：\n\n1. **σ=9.5pp on n=3**：Table 2 中 30% KL global MMLU = 35.7±9.5，意味着 95% CI ≈ ±23.6pp（t-distribution, df=2），基本没有统计信息量。\n2. **KL vs. TEAL 差异在 CI 内**：30% uniform MMLU: KL 40.7±1.3 vs. TEAL 45.86。差异 5.16pp，n=3 下 95% CI for KL ≈ [37.5, 43.9]，不包含 45.86。但这仅是单侧比较（TEAL 是确定性的单次运行，无方差估计），严格来说 p-value 无法计算。\n3. **论文内部承认但外部声明不一致**：Section 4.2 诚实地说 \"directional evidence\"，但 Abstract（\"commonsense gains\"）和 Conclusion（\"commonsense gains\"）未带此限定。\n\n**补充意见**：我在自己的审稿中（W5）也提出了相同关切。R1 的建议 \"(3) 下游声明加统计限定语\" 是必要的。关于 \"(1) 至少 5 seeds\"，这是理想方案但可能受限于计算资源，至少应增加 bootstrap CI 的报告。\n\n---\n\n### Should-Fix 问题回应\n\n[AGREE] R1-W1（C1 target-swap ablation 的 soft→hard 混淆变量）:\n部分同意。论文在 Section 4.4 确实承认了这一 confound：\"binarizing oracle soft logits (>0) into hard masks discards ranking information, so the near-zero delta reflects transferability of binary mask patterns rather than full predictor knowledge.\" BCE+Gumbel（32.22）vs 标准 BCE（27.97）的 15% 差距说明 Gumbel 表示本身有影响。\n\n但 C1 的核心发现仍然成立：即使存在 representation confound，KL-derived hard masks + simple BCE 训练（C1）仍然远优于 magnitude-derived hard masks + BCE（15.71 at 30%），说明 mask 质量（哪些 neuron 被选中）是关键因素。Gumbel 的 representation 效应只部分解释了 KL 优势，不能完全解释。\n\n**建议**：作者应增加一个 \"KL-derived masks + BCE without Gumbel\" 的 ablation 以完全隔离 mask 质量 vs. mask 表示。或者更明确地限定 C1 结论的适用范围。\n\n---\n\n[AGREE] R1-W2（Knowledge-task regression 分析不充分）:\n强烈同意，这与我的 N2 高度一致。C4 控制实验仅 1 seed（Section 4.2: \"MMLU 40.0%, GSM8K 4.1%\"），排除训练数据假说的证据不充分。\"mode-covering dilutes rare activations\" 仍是推测。\n\n关键数据点：KL uniform MMLU = 40.7 vs. TEAL uniform MMLU = 45.86（Table 2, 30%），二者使用相同的 uniform allocation 策略。这 5pp 差距不能用 allocation 解释，必须归因于 KL loss 本身的某种属性。论文未对此进行因果分析。\n\n---\n\n[REBUT] R1-W3（实验覆盖度缺口且 Limitations 未覆盖）:\nR1 声称 \"(1) 无生成任务评估；(2) seq_len 固定 2048；(3) 无 batched inference 评估\" 未被 Limitations 覆盖。这与事实不符。\n\nLimitations 段落（page 9）明确写道：\n- \"open-ended generation quality (e.g., MT-Bench) remains untested and may exhibit different sparsity sensitivity\"（覆盖第 1 点）\n- \"All experiments use sequence length 2048; behavior at longer contexts (e.g., 8K-128K) is untested\"（覆盖第 2 点）\n- \"Batched inference, where sparsity patterns must be intersected across sequences, may reduce effective sparsity and is not evaluated\"（覆盖第 3 点）\n\n三个实验覆盖度缺口均已在 Limitations 中明确承认。R1 的批评在 \"这些是缺口\" 方面是正确的，但 \"Limitations 未覆盖\" 的判断有误。\n\n---\n\n[REBUT] R1-W4（Table 14 MMLU 数值不一致）:\nR1 称 \"Table 14 报告 50% Global MMLU=35.7±9.5，但 Appendix F 正文描述 50% Global MMLU=28.3±0.7\"。\n\n经我核实 LaTeX 源文件（appendix.tex lines 336-354），Table 14（tab:phase）的实际内容是：\n- **30% Global**: MMLU = 35.7±9.5*\n- **30% Uniform**: MMLU = 40.7±1.3\n- **50% Global**: MMLU = 28.3±0.7\n- **50% Uniform**: MMLU = 28.0±0.6\n\n**35.7±9.5 是 30% Global 的数值，不是 50% Global。** R1 误读了表格行标签。Table 14 中 50% Global MMLU = 28.3±0.7，与 Appendix F（Training Stability, appendix.tex line 221: \"Under global allocation at 50%, MMLU is 28.3±0.7%\"）以及 Table 2 主表完全一致。不存在数据不一致。\n\n---\n\n### 小问题回应\n\n[REBUT] R1-Minor-1（Gradient SNR 叙事张力：coupling 应提高 SNR 但实际降低）:\nR1 说 \"coupling 应提高 SNR\"，但论文并未做此预测。Section 3.6 明确写道：\"BCE maintains consistently higher SNR than KL throughout training (2.3× at convergence), indicating that KL's quality advantage does not arise from cleaner gradient signals. Rather, KL's end-to-end coupled gradient serves as a search mechanism.\" Figure 5（Appendix H）显示这是 consistent pattern，不是 anomaly。论文的叙事是 \"KL 胜出 despite 更低 SNR\"，而非 \"KL 因更高 SNR 而胜出\"。这是论文的一个 deliberate finding，不是张力。\n\n[AGREE] R1-Minor-2（\"the first decomposition\" 措辞应更审慎）:\n同意。Section 2 写 \"to our knowledge, the first decomposition of signal type vs. coupling scope\"。虽然有 \"to our knowledge\" 限定，但 \"first\" 仍然是强 claim。建议改为 \"a systematic decomposition\" 或 \"we provide what we believe is the first...\"\n\n[AGREE] R1-Minor-3（Table 1 Taxonomy 暗示新颖性来自组合已有技术）:\n同意。这与我的 novelty 边界评估一致。Table 1 诚实地展示了本文方法的位置（Per-token × Coupled），而每个维度上的技术（per-token prediction, KL distillation, Gumbel-Sigmoid）均非新发明。新颖性在于 combination + empirical characterization，这是 Findings 级别的贡献。\n\n[AGREE] R1-Minor-4（MSE baseline cherry-pick 风险）:\n部分同意。MSE 50% 仅报告 s42（PPL 229.26），s123 catastrophic（PPL=15,789, Appendix G, appendix.tex line 244）。论文通过脚注标注了这一点（Table 4: \"§MSE 50%: s42 only; s123 catastrophic\"），保持了透明度。但 30% MSE 3-seed mean 18.52±1.68（s42=20.43, s123=17.73, s456=17.39）是合理的 baseline。风险在于读者可能忽略脚注，误以为 MSE 50% 是 robust result。\n\n---\n\n### Questions 回应\n\n[AGREE] R1-Q1（K=4 MMLU 超过 E2E 的机制）:\n这是我在 Q2 中提出的相同问题。论文归因于 \"K=4's near-uniform allocation matching uniform inference\"（Section 4.5）。如果正确，这意味着 E2E KL 学到的 non-uniform allocation 实际上 *伤害* MMLU，而 per-layer 训练偶然产生了更好的 allocation。这确实削弱了 \"output-distribution alignment is the primary design dimension\" 的全面性——至少对 knowledge tasks，allocation 可能比 signal type 更重要。\n\n[AGREE] R1-Q2（Compensation network 为何无效）:\n有效问题。论文仅说 \"provides no benefit\"（Section 4.5, Appendix J），但未解释 *为什么*。可能的原因：(1) KL predictor 已经优化了 output distribution，compensation network 没有剩余误差可修正；(2) compensation 的 per-layer MSE 目标与 KL 的 output-distribution 目标不兼容。作者应至少讨论机制。\n\n[AGREE] R1-Q3（端到端 wall-clock latency）:\n同意需要更多 batch size 的延迟数据。Appendix A（Table 5）仅报告 batch=1 的结果。对于实际部署，batch>1 的延迟特征可能完全不同（predictor overhead 可能被摊薄，但 mask intersection 成本可能增加）。\n\n[AGREE] R1-Q4（排除 MMLU σ=9.5 的 outlier seed 后 Global allocation 结论是否成立）:\n有效问题。Table 15（Appendix L, tab:phase_full）显示 30% Global MMLU seeds span 25.3--43.5%。如果 25.3% 是 outlier，排除后 mean 会显著上升。但 n=3 下排除 1 个 seed（变成 n=2）更不可靠。这再次印证 R1-N2 的 seed 不足问题。\n\n[AGREE] R1-Q5（token-level adaptive sparsity 缓解 knowledge regression）:\n有趣的方向。当前方法使用 model-level fixed sparsity target。Token-level adaptive sparsity（对 knowledge-intensive tokens 降低 sparsity）可能缓解 MMLU 退化。论文未讨论此方向，可列为 future work。\n\n---\n\n### 总体评价\n\nR1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：\n1. R1 对 PPL 改进的实用价值评价略高，我认为缺乏 wall-clock speedup 显著削弱实际影响力。\n2. 我对 \"primary design dimension\" claim 的泛化性更为怀疑，尤其是在 knowledge tasks 上的系统性退化。\n\n两位 reviewer 的核心共识：\n- PPL 改进 robust 且一致（共识优势）\n- K=1 decomposition 存在 train-inference mismatch confound（共识弱点）\n- 3 seeds 不足以支持下游 claims（共识弱点）\n- Knowledge regression 缺乏因果解释（共识弱点）\n- Table 1 taxonomy 的新颖性在于组合而非原创技术（共识判断）\n- 适合 Findings track（3.0-3.5 区间）",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1935 · 2026-05-23T07:34:33.975208+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3732
}
```

</details>

---


### Assistant

_source line 1936 · 2026-05-23T07:34:45.217008+00:00_

已向 Review Director 提交逐条回应。

**要点总结**：
- R1 的 5 个 Strengths 全部 **[AGREE]**
- **Must-Fix N1**（K=1 mismatch）: [AGREE]，与我的 N1 高度一致
- **Must-Fix N2**（3-seed 统计功效）: [AGREE]，与我的 W5 一致
- **Should-Fix W1**（C1 soft→hard confound）: [AGREE]，但指出核心发现仍成立
- **Should-Fix W2**（Knowledge regression）: [AGREE]，与我的 N2 一致
- **Should-Fix W3**（Limitations 未覆盖）: **[REBUT]** — Limitations 段落明确覆盖了 R1 提到的全部三个缺口（generation tasks, seq_len, batched inference）
- **Should-Fix W4**（Table 14 数值不一致）: **[REBUT]** — R1 误读了表格行标签，35.7±9.5 是 30% Global 而非 50% Global，数据完全一致
- **Minor 1**（SNR 张力）: **[REBUT]** — 论文叙事是 "KL despite lower SNR"，不是 "KL because of higher SNR"
- 其余 Minor 和 Questions 均 [AGREE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 48

## Round 48

102 recorded events


### User

_source line 1937 · 2026-05-24T02:57:26.249250+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 投稿信息
- **Venue**: EMNLP 2026（通过 ARR 统一审稿）
- **类别**: Long Paper（正文 8 页限制，References 不限，Limitations 不计入页数）
- **模板**: ACL review format（double-blind）
- **Deadline**: 2026-05-25
- **Overall Assessment 评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 论文文件
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf`

## 论文概述
本文是一项实证研究，系统对比了 SwiGLU LLM 上下文稀疏性预测器的不同训练目标（KL/BCE/MSE/JSD/Reverse KL）。核心发现：output-distribution KL 在 PPL 上显著优于 per-neuron BCE 和 per-layer MSE；KL 发现的 mask 模式与 magnitude-based 目标有 46-68% 的 Jaccard distance 偏离；target-swap ablation 显示这些模式可迁移。跨架构（Mistral-7B, Qwen-2.5-14B）验证了 PPL 优势。但知识密集型任务（MMLU, GSM8K）出现系统性退步。

## 你的审查侧重

### 1. 新颖性评估
- 核心组件（KL distillation, Gumbel-Sigmoid, lightweight predictor）均为已有技术。MaskLLM 已将 frozen weights + learnable masks + KL 用于稀疏性。本文的 novelty 边界在哪里？"组合新颖性 + 系统性实证分析" 是否满足 EMNLP 的 novelty bar？
- Table 1 taxonomy 是否有真正的分析价值，还是仅仅是 organizational？空格子是否暗示了未验证的假设？
- "empirical study" 的定位是否 consistent？contribution list 中有 4 条，前 2 条标 Empirical，后 2 条标 Practical——Practical 贡献是否足够 substantial？

### 2. 相关工作完整性
- 是否遗漏了重要的相关工作？特别是：
  - 2025-2026 年发表的 activation sparsity 新工作
  - KL distillation 用于结构化/非结构化稀疏性的其他工作
  - Hardware-aware sparsity（如 Triton block-sparse 实现）
- MaskLLM 的区分是否充分？论文列了 3 点区别（static vs contextual, no cross-layer, input-independent），但是否有实验证据支持这些区别的重要性？

### 3. 写作质量与叙事一致性
- Abstract 信息密度是否过高？是否在 200 words 以内？
- "primarily an empirical study" 但 §3 有 7 个 subsection 的方法描述——这是否造成读者预期错位？
- Conclusion 仅 2 句话是否过于简略？是否遗漏了 broader impact 或 future work？
- Introduction 中数字过多（14.5%, 46-68%, 0.65pp, 28.13±0.20, 68%, 33.8%）是否影响可读性？
- 术语一致性：是否全文统一使用 "output-distribution KL"？

### 4. 格式合规性（EMNLP 2026 / ACL template）
- 正文是否恰好 8 页？Limitations 是否在正文而非 appendix？
- 匿名性：是否有 deanonymization 风险（代码链接、GPU 型号、specific experimental details）？
- 引用格式是否符合 ACL natbib 要求？`\citealp` vs `\cite` 使用是否正确？
- Appendix 是否过长（可能超出审稿人耐心）？有多少个 appendix section？

### 5. Limitations 覆盖度
- 3 个限制是否充分？是否遗漏了：
  - 仅 SwiGLU 架构（不适用于 ReLU/GeLU）
  - 训练数据量极小（1000 steps, WikiText-103）
  - 无实际部署验证
  - Predictor 增加 6.4% latency 但无 wall-clock 加速

### 6. 知识退步的 framing
- MMLU -5.2pp（8B）和 GSM8K -20.1pp（14B）是否被充分 acknowledged？
- "directional commonsense gains" 的措辞是否 understate 了 knowledge regression 的严重性？
- 在 downstream 全面退步的情况下，PPL improvement 作为主要贡献是否足够有说服力？

请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1938 · 2026-05-24T02:57:36.139779+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search ARR review form",
  "prompt": "Search the web for \"ACL ARR review form 2025 2026 reviewer guidelines criteria\" and \"EMNLP 2026 reviewer guidelines review form dimensions\". I need to find the official review form dimensions and scoring criteria used by ACL Rolling Review (ARR) for EMNLP 2026 submissions. Look for the specific dimensions reviewers are asked to score on (e.g., soundness, excitement, reproducibility, etc.) and their scales. Try multiple search queries if needed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search ARR review form",
    "prompt": "Search the web for \"ACL ARR review form 2025 2026 reviewer guidelines criteria\" and \"EMNLP 2026 reviewer guidelines review form dimensions\". I need to find the official review form dimensions and scoring criteria used by ACL Rolling Review (ARR) for EMNLP 2026 submissions. Look for the specific dimensions reviewers are asked to score on (e.g., soundness, excitement, reproducibility, etc.) and their scales. Try multiple search queries if needed."
  }
}
```

</details>

---


### Tool call

_source line 1939 · 2026-05-24T02:57:37.998421+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 reviewer guidelines criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 reviewer guidelines criteria"
  }
}
```

</details>

---


### Tool call

_source line 1940 · 2026-05-24T02:57:37.998894+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1941 · 2026-05-24T02:57:37.999131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR review form scoring dimensions soundness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR review form scoring dimensions soundness"
  }
}
```

</details>

---


### Tool call

_source line 1942 · 2026-05-24T02:57:38.049496+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 1943 · 2026-05-24T02:57:38.049899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1944 · 2026-05-24T02:57:44.032379+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form dimensions"

Links: [{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Instructions for Reviewers for EMNLP 2020","url":"https://2020.emnlp.org/blog/2020-05-26-instructions-for-reviewers/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Are Non-English Papers Reviewed Fairly? Language-of-Study Bias in NLP Peer Reviews","url":"https://arxiv.org/pdf/2604.07119"}]

Based on the search results, I found information about EMNLP 2026 reviewer guidelines and deadlines, but the specific details about review form dimensions were not prominently featured in these results. 

Here's what I found about EMNLP 2026 reviewing:

**Review Deadlines:**
If you receive assignments, your reviews must be completed by July 6, or your meta-reviews by July 29.

**Mandatory Reviewing Workload:**
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications. After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

However, the search results did not contain specific information about the review form dimensions (such as the specific evaluation criteria or scoring scales used for EMNLP 2026). The historical references I found (like EMNLP 2020) mention that review forms have sections for in-depth review, but detailed information about the 2026 form's specific dimensions is not available in these search results. You may wan
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6033
}
```

</details>

---


### Tool result

_source line 1945 · 2026-05-24T02:57:44.083100+00:00_

Web search results for query: "ACL Rolling Review ARR review form scoring dimensions soundness"

Links: [{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL Rolling Review (ARR) form scoring dimensions with a focus on soundness:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Dimension

The soundness dimension asks whether the paper is sufficiently sound and thorough, and whether it clearly states scientific claims and provides adequate support for them. For experimental papers, reviewers should consider the depth and/or breadth of the research questions investigated, technical soundness of experiments, and methodological validity of evaluation. For position papers and surve
…[truncated 694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6083
}
```

</details>

---


### Tool result

_source line 1946 · 2026-05-24T02:57:45.387724+00:00_

Web search results for query: "ACL ARR review form 2025 2026 reviewer guidelines criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here are the key details about the ACL ARR review form, reviewer guidelines, and criteria for 2025-2026:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Reviewer Requirements and Expectations

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and
…[truncated 1157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7389
}
```

</details>

---


### Tool call

_source line 1947 · 2026-05-24T02:57:47.143762+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the specific review form dimensions, scoring scales, and evaluation criteria?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the specific review form dimensions, scoring scales, and evaluation criteria?"
  }
}
```

</details>

---


### Tool call

_source line 1948 · 2026-05-24T02:57:47.446356+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the complete review dimensions, scoring scales, and detailed criteria for each dimension?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the complete review dimensions, scoring scales, and detailed criteria for each dimension?"
  }
}
```

</details>

---


### Tool result

_source line 1949 · 2026-05-24T02:57:51.010007+00:00_

# ACL Rolling Review Form: Dimensions and Scales

## Main Evaluation Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 1: "Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- 5: "Excellent: This study is one of the most thorough"
- 1: "Major Issues: not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-point increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 1: "Not Exciting: does not resonate with me"

**Overall Assessment** (1-5 scale with half-point increments)
- 5: "Consider for Award" (top 2.5%)
- 4: "Conference" acceptance recommendation
- 3: "Findings" track acceptance
- 2: "Resubmit next cycle"
- 1: "Do not resubmit"

## Additional Criteria

**Reproducibility** (1-5 scale): Assesses whether readers can reproduce results

**Datasets & Software** (1-5 scales): Evaluates value of released materials

**Ethics** (binary): Determines if in-depth ethics review is needed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3866
}
```

</details>

---


### Tool result

_source line 1950 · 2026-05-24T02:57:52.717117+00:00_

# ARR Review Dimensions and Scoring

Based on the guidelines provided, ARR reviewers assess papers using **three main dimensions**:

## 1. **Soundness**
Evaluates technical quality and validity. Scores must be justified by the review text. The guidelines note that "low _Soundness_ scores without finding any major faults" indicate the review lacks coherence.

## 2. **Excitement**
Reflects personal interest and subjective appeal, described as "orthogonal to the assessment of the soundness of the paper." This allows reviewers to distinguish between technically sound work that may not personally engage them.

## 3. **Overall Recommendation**
A composite assessment "reflecting your assessment of soundness, excitement, and also other factors like novelty and impact." This is "an explicit recommendation for the outcome of this paper, if it were committed to an \*ACL venue."

## Key Guidance

The document emphasizes that reviewers should recognize "low soundness scores without sufficient justification" may reflect unconscious bias rather than legitimate technical concerns. Additionally, reproducibility scores deserve separate justification from overall soundness assessments.

**Note:** The guidelines don't specify precise numerical scales or detailed point ranges for each dimension—these appear to be defined within the OpenReview platform itself rather than in this document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5270
}
```

</details>

---


### Tool call

_source line 1951 · 2026-05-24T02:57:54.527042+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
  "prompt": "Complete review dimensions, scoring scales, and all criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md",
    "prompt": "Complete review dimensions, scoring scales, and all criteria"
  }
}
```

</details>

---


### Tool call

_source line 1952 · 2026-05-24T02:57:54.778300+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
  "prompt": "Review form dimensions, scoring criteria, and evaluation scales"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/acl-org/aclrollingreview/blob/main/cfp.md",
    "prompt": "Review form dimensions, scoring criteria, and evaluation scales"
  }
}
```

</details>

---


### Tool result

_source line 1953 · 2026-05-24T02:58:01.000795+00:00_

# ARR Reviewer Guidelines: Scoring & Review Dimensions

Based on the document provided, here are the key review dimensions and scoring frameworks:

## Three Primary Scoring Dimensions

**Soundness**: Technical validity and methodological rigor. As stated, "soundness scores must be justified by the text of the review." Low soundness requires substantive justification.

**Excitement**: Personal interest in the work, orthogonal to soundness. This reflects subjective appeal rather than objective quality.

**Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact for conference acceptance.

## Core Review Expectations

Reviewers should evaluate whether papers demonstrate "technical soundness and appropriately scoped" contributions. The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Key Evaluation Criteria

The document outlines several problem categories reviewers should assess:

- **Methodology issues** (M1-M5): reproducibility, data quality, assumptions clarity
- **Experimental results** (R1-R5): statistical validity, claim scope, evidence quality
- **General issues** (G1-G5): research clarity, related work representation, term definitions

## Critical Principle

Reviewers must avoid conflating acknowledged limitations with fundamental flaws. The guidelines note: "most venues require a Limitations section...a good review should not just take the limitations and list them as weaknesses."

The framework prioritizes substantiated, specific feedback over subjective dismissal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6473
}
```

</details>

---


### Tool result

_source line 1954 · 2026-05-24T02:58:05.367365+00:00_

# ACL Rolling Review: Key Information

Based on the Call for Papers document, here are the essential details:

## Review Process Structure

ARR uses a two-step approach: centralized rolling review with bi-monthly deadlines, followed by commitment to publication venues. Reviews are handled through OpenReview (non-open format).

## Submission Requirements

**Long papers:** Up to 8 pages of content plus unlimited references and a required limitations section.

**Short papers:** Up to 4 pages of content plus unlimited references and a required limitations section.

Both must include anonymized author information and a completed Responsible NLP Checklist.

## Key Policies

**Reviewing obligation:** "All authors are expected to contribute to the review process" unless exempt. Authors must register within 48 hours of submission and meet publication history thresholds (at least 2 papers in main ACL events plus 1 additional paper in ACL Anthology or major ML/AI venues).

**Multiple submissions:** Papers cannot be simultaneously under review at ARR and other venues. Violating this results in desk rejection.

**Resubmissions:** Must include links to previous versions and summaries of revisions addressing reviewer feedback.

**Ethics:** Authors must complete the Responsible NLP Checklist accurately; incomplete or misleading information can trigger desk rejection.

## Desk Rejection Triggers

Format violations, anonymity breaches, dual submissions, incomplete limitations sections, and inadequate resubmission revisions all warrant rejection without review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10589
}
```

</details>

---


### Tool call

_source line 1955 · 2026-05-24T02:58:07.028766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR review form soundness excitement overall recommendation 1-5 scale February 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR review form soundness excitement overall recommendation 1-5 scale February 2025"
  }
}
```

</details>

---


### Tool call

_source line 1956 · 2026-05-24T02:58:07.179867+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" review dimensions reproducibility datasets ethics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" review dimensions reproducibility datasets ethics 2026"
  }
}
```

</details>

---


### Tool result

_source line 1957 · 2026-05-24T02:58:13.407198+00:00_

Web search results for query: "ARR review form soundness excitement overall recommendation 1-5 scale February 2025"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ARR 2025 Statistics: February Track - Paper Copilot","url":"https://papercopilot.com/statistics/arr-statistics/arr-2025-statistics-february-track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"}]

Based on the search results, I found information about the ARR review form changes for February 2025:

## ARR Review Form Structure (February 2025)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### The Three Scoring Components:

**Soundness Score:** The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

**Excitement Score:** Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6378
}
```

</details>

---


### Tool result

_source line 1958 · 2026-05-24T02:58:13.458479+00:00_

Web search results for query: ""ACL Rolling Review" review dimensions reproducibility datasets ethics 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsibleNLPresearch/"},{"title":"Guidelines for Ethics Reviewing – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/ethicsreviewertutorial"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"Yes-Yes-Yes: Proactive Data Collection for ACL Rolling Review and Beyond","url":"https://arxiv.org/pdf/2201.11443"}]

Based on the search results, here's information about ACL Rolling Review's review dimensions related to reproducibility, datasets, and ethics:

## Review Dimensions

The review form assesses whether there is enough information in papers for readers to reproduce main results, use results in future work, or build upon the work. Reviewers evaluate reproducibility on a scale where 1 means results cannot be repro
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6278
}
```

</details>

---


### Tool result

_source line 1959 · 2026-05-24T02:58:22.698810+00:00_

Excellent! I have comprehensive information. Let me compile the findings for you.

## Summary of Official ACL ARR Review Form Dimensions and Scoring Criteria

Based on my search of the official ACL Rolling Review resources, here are the official review form dimensions and scoring criteria used for ARR submissions (including EMNLP 2026):

### **Primary Scoring Dimensions (as of February 2025)**

The ARR review form uses **three main scoring dimensions**:

1. **Soundness** (1-5 scale with half-point increments)
   - 5: "Excellent: This study is one of the most thorough"
   - 1: "Major Issues: not yet sufficiently thorough to warrant publication"
   - Key requirement: Soundness scores MUST be justified by the text of the review. Low soundness scores without substantive justification indicate the review lacks coherence.
   - Criteria include: technical soundness of methodology, validity of experiments, appropriateness of scope, reproducibility, and data quality

2. **Excitement** (1-5 scale with half-point increments)
   - 5: "Highly Exciting: I would recommend this paper to others"
   - 4: "Exciting: I would mention this paper to others and/or make an effort to attend its presentation"
   - 1: "Not Exciting: does not resonate with me"
   - Key principle: Orthogonal to soundness assessment—allows reviewers to distinguish technically sound work from subjectively interesting work

3. **Overall Recommendation** (1-5 scale with half-point increments)
   - 5: "Consider for Award" (top 2.5% tier)
   - 4: "Conference" acceptance recommendation
   - 3: "Findings" track acceptance
   - 2: "Resubmit next cycle"
   - 1: "Do not resubmit"
   - Composite score reflecting soundness, excitement, novelty, and impact

### **Secondary Review Dimensions**

4. **Reviewer Confidence** (1-5 scale)
   - 5: "Positive that my evaluation is correct"
   - 1: "Not my area, or paper is very hard to understand"

5. **Reproducibility** (1-5 scale)
   - Assesses whether readers can reproduce main resu
…[truncated 1254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 46559
}
```

</details>

---


### Tool call

_source line 1960 · 2026-05-24T02:58:30.666744+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1961 · 2026-05-24T02:58:31.971216+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1304
}
```

</details>

---


### Tool call

_source line 1962 · 2026-05-24T02:58:34.580585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1963 · 2026-05-24T02:58:35.485011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1964 · 2026-05-24T02:58:35.535769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1965 · 2026-05-24T02:58:36.089528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1966 · 2026-05-24T02:58:36.492051+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1967 · 2026-05-24T02:58:36.492465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1968 · 2026-05-24T02:58:37.045314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1969 · 2026-05-24T02:58:37.045737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1970 · 2026-05-24T02:58:37.399589+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 1971 · 2026-05-24T02:58:37.802052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 1972 · 2026-05-24T02:58:42.217631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1973 · 2026-05-24T02:58:42.620251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1974 · 2026-05-24T02:58:43.074926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1975 · 2026-05-24T02:58:43.075369+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1976 · 2026-05-24T02:58:44.030705+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 1977 · 2026-05-24T02:58:44.031809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1978 · 2026-05-24T02:58:44.032154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1979 · 2026-05-24T02:58:44.334001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1980 · 2026-05-24T02:58:44.839887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool result

_source line 1981 · 2026-05-24T02:58:45.142745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 1982 · 2026-05-24T02:58:53.916911+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1983 · 2026-05-24T02:58:55.024085+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.2}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 324.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 361.7}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p19.png\", \"w
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 1984 · 2026-05-24T02:58:58.284945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1985 · 2026-05-24T02:58:58.889458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1986 · 2026-05-24T02:58:58.890631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool result

_source line 1987 · 2026-05-24T02:58:59.543722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1988 · 2026-05-24T02:58:59.544168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1989 · 2026-05-24T02:59:00.098217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1990 · 2026-05-24T02:59:00.451688+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1991 · 2026-05-24T02:59:00.452076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1992 · 2026-05-24T02:59:00.854429+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool result

_source line 1993 · 2026-05-24T02:59:01.256479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1994 · 2026-05-24T02:59:05.923635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1995 · 2026-05-24T02:59:06.425736+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1996 · 2026-05-24T02:59:06.879146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool result

_source line 1997 · 2026-05-24T02:59:06.882325+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 1998 · 2026-05-24T02:59:06.882701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1999 · 2026-05-24T02:59:07.436002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2000 · 2026-05-24T02:59:07.436463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_25/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 2001 · 2026-05-24T02:59:07.990970+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 2002 · 2026-05-24T02:59:14.816414+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2003 · 2026-05-24T02:59:15.167533+00:00_

1	Learned sparsity predictors for SwiGLU LLMs predominantly use binary cross-entropy (BCE), training each neuron independently, yet inference allocates budgets globally via top-$k$ ranking.
2	We train lightweight predictors ($<$1\% of base parameters) with forward KL divergence, coupling all mask decisions through the output distribution.
3	On LLaMA-3.1-8B at 30\% sparsity, the KL predictor reduces perplexity by 14.5\% over TEAL at matched sparsity, with directional commonsense gains ($n{=}3$) but knowledge-intensive regression (MMLU $-$5.2pp on 8B; GSM8K $-$20.1pp on 14B); post-hoc compensation (+67.2M params) becomes redundant.
4	Output-distribution optimization yields masks that diverge 46--68\% from magnitude-based targets; a target-swap ablation suggests these discovered patterns carry most of the quality information: BCE trained on KL-derived targets approaches KL-level PPL (PPL gap $\leq$0.65pp; 3-seed, 30\%).
5	Signal type (output-distribution vs.\ intermediate loss) may account for a substantial portion of the PPL gap at moderate sparsity (30\%) (upper bound; \S\ref{sec:perlayer}).
6	On downstream tasks, cross-layer coupling contributes substantially for commonsense reasoning but minimally for mathematical reasoning (3-seed $K{=}4$-corrected decomposition).
7	Cross-architecture evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms PPL generalization with scale-dependent downstream effects.
8	This is primarily an empirical study; wall-clock speedup requires sparse kernel support not addressed here.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2004 · 2026-05-24T02:59:15.218397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2005 · 2026-05-24T02:59:15.319099+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	At moderate sparsity (30\%), output-distribution alignment is the primary design dimension: signal type may account for most of the PPL gap (upper bound; Appendices~\ref{app:k4_downstream},~\ref{app:constraint}).
5	A $<$1\% predictor reduces TEAL's PPL by 14.5\% via divergent masks; directional downstream gains but knowledge regression persist across scales.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2006 · 2026-05-24T02:59:15.670761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2007 · 2026-05-24T02:59:16.122980+00:00_

1	\section*{Limitations}
2	
3	Our findings are bounded by three limitations.
4	\textbf{Sparsity sweet spot.} 30\% is the lowest-degradation level; at 50\%, all methods collapse to near-random on reasoning tasks, and a separate predictor must be retrained per target.
5	\textbf{Knowledge-intensive regression.} KL consistently underperforms on MMLU and GSM8K across scales (8B: $-$5.2pp MMLU; 14B: $-$20pp GSM8K), suggesting output-distribution objectives systematically sacrifice reasoning-critical pathways.
6	\textbf{Evaluation scope.} All predictors train on WikiText-103; C4 evaluation shows preserved KL advantage but $31\times$ higher cross-seed variance. Open-ended generation (e.g., MT-Bench) and contexts beyond 2048 tokens remain untested.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2008 · 2026-05-24T02:59:16.123434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2009 · 2026-05-24T02:59:16.173976+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2010 · 2026-05-24T02:59:26.568558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2011 · 2026-05-24T02:59:26.870122+00:00_

1	\section{Introduction}
2	
3	How the training objective shapes learned sparsity prediction quality is an open question for SwiGLU LLMs~\cite{shazeer2020glu}. SwiGLU FFN blocks exhibit high contextual sparsity, but their gated activation makes importance prediction challenging: neuron importance depends on both gate and up-projection values, a target that magnitude-based methods handle suboptimally.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they predominantly rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: the TEAL (training-free activation sparsity;~\citealp{liu2025teal}) top-$k$ mechanism ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	Unlike MaskLLM~\cite{fang2024maskllm}, which applies KL to static N:M weight masks, we address contextual activation sparsity where masks must generalize to unseen inputs, vary per token, and coordinate across layers through global allocation.
8	
9	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
10	KL's coupled gradients discover neuron importance patterns that diverge 68\% from magnitude-based masks (mean per-layer Jaccard distance).
11	A target-swap ablation shows KL-discovered mask targets carry most of the quality information: BCE retrained on KL-derived targets approaches KL PPL ($\leq$0.65pp gap, 3-seed), while magnitude-trained BCE yields 28.13$\pm$0.20. Coupling contributes marginally to 
…[truncated 3012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2012 · 2026-05-24T02:59:26.870548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 2013 · 2026-05-24T02:59:26.921003+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	
18	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
19	\setlength{\floatsep}{8pt plus 2pt minus 2pt}
20	\setlength{\intextsep}{8pt plus 2pt minus 2pt}
21	
22	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	\input{limitations}
39	% \input{ethics}  % removed per submission guidelines
40	
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2014 · 2026-05-24T02:59:33.996257+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/--/-/g' | wc -w",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && cat abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/--/-/g' | wc -w",
    "description": "Count abstract words"
  }
}
```

</details>

---


### Tool result

_source line 2015 · 2026-05-24T02:59:34.799345+00:00_

187
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 2016 · 2026-05-24T02:59:34.799792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity LLM predictor 2025 2026 contextual sparsity SwiGLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity LLM predictor 2025 2026 contextual sparsity SwiGLU"
  }
}
```

</details>

---


### Tool call

_source line 2017 · 2026-05-24T02:59:35.201449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2018 · 2026-05-24T02:59:35.252165+00:00_

1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} and GRASP~\cite{shin2025grasp} predict activation sparsity patterns without additional training.
6	LaRoSA~\cite{huang2025larosa} applies layerwise orthogonal rotations for structured activation sparsity with wall-clock speedup on SiLU models.
7	Wang et al.~\cite{wang2025dynamicsparse}, AWQ~\cite{lin2024awq}, and Outlier Suppression+~\cite{wei2023outlier} address sparsity--quantization interactions and activation-aware quantization.
8	Dhar et al.~\cite{dhar2024activation} characterize activation sparsity opportunities across architectures, showing that SwiGLU models exhibit lower natural sparsity than ReLU counterparts.
9	OWL~\cite{yin2024owl} determines per-layer sparsity ratios from outlier distributions for weight pruning.
10	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
11	
12	\paragraph{Predictor-Based Contextual Sparsity.}
13	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
14	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
15	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
16	SVD-CSP~\cite{serbin2026svdcsp} compre
…[truncated 5026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2019 · 2026-05-24T02:59:42.778659+00:00_

Web search results for query: "activation sparsity LLM predictor 2025 2026 contextual sparsity SwiGLU"

Links: [{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2603.12272"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking","url":"https://arxiv.org/pdf/2412.01380"}]

Based on the search results, here's what I found regarding activation sparsity, LLM predictors, contextual sparsity, and SwiGLU:

## Key Research Areas

**Activation Sparsity in LLMs:**
Large Language Models exhibit significant activation sparsity, where only a subset of neurons are active for a given input, which presents opportunities to reduce computational cost if activation patterns can be efficiently predicted.

**Contextual Sparsity Predictors:**
Contextual sparsity can be leveraged at runtime through sparsity predictors or learned routers that dynamically select the neurons to activate based on the input vectors. Prior work has attempted to model contextual sparsity using neural networks trained to predict activation magnitudes, which can be used to dynamically prune structures with low predicted activation magnitude.

**Recent Predictor Approaches (2025-2026):**
SVD-based predictors are cons
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7978
}
```

</details>

---


### Tool call

_source line 2020 · 2026-05-24T02:59:46.792929+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Polar Sparsity 2025 batched LLM inference activation sparsity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Polar Sparsity 2025 batched LLM inference activation sparsity"
  }
}
```

</details>

---


### Tool call

_source line 2021 · 2026-05-24T02:59:47.596148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SVD-CSP sparsity predictor SVD decomposition 2026 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SVD-CSP sparsity predictor SVD decomposition 2026 LLM"
  }
}
```

</details>

---


### Tool call

_source line 2022 · 2026-05-24T02:59:47.747077+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KL divergence distillation structured pruning sparsity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KL divergence distillation structured pruning sparsity 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 2023 · 2026-05-24T02:59:53.504362+00:00_

Web search results for query: "Polar Sparsity 2025 batched LLM inference activation sparsity"

Links: [{"title":"[PDF] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polar-Sparsity:-High-Throughput-Batched-LLM-with-Shrestha-Settlemyer/328fcf757fa9647ea5eb96d37ee735e52a43df43"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with ...","url":"https://susavlsh10.github.io/files/Polar_Sparsity_NeurIPS_2025_CameraReady.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://openreview.net/pdf/43bf702e03ce0cb3a890cf8a35f3ded98d30b94d.pdf"},{"title":"Polar Sparsity: High Throughput Batched LLM","url":"https://openreview.net/pdf?id=cg2S1qqNSq"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity | OpenReview","url":"https://openreview.net/forum?id=cg2S1qqNSq"},{"title":"[2505.14884] Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/abs/2505.14884"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity","url":"https://arxiv.org/html/2505.14884v1"},{"title":"Polar Sparsity: High Throughput Batched LLM Inferencing ...","url":"https://arxiv.org/pdf/2505.14884"}]

Based on the search results, here's what I found about Polar Sparsity 2025:

## Overview

Polar Sparsity is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes. The work achieves up to 2.2× speedups with minimal accuracy loss.

## The Core Problem and Solution

Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation.

Pola
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6711
}
```

</details>

---


### Tool result

_source line 2024 · 2026-05-24T02:59:54.835604+00:00_

Web search results for query: "KL divergence distillation structured pruning sparsity 2025 2026"

Links: [{"title":"The Model Optimization Revolution: How Pruning, Distillation, and PEFT Are Reshaping AI in 2025 | by Harsh Prakash | Medium","url":"https://medium.com/@hs5492349/the-model-optimization-revolution-how-pruning-distillation-and-peft-are-reshaping-ai-in-2025-c9f79a9e7c2b"},{"title":"Post-Pruning Accuracy Recovery via Data-Free Knowledge Distillation","url":"https://arxiv.org/html/2511.20702v1"},{"title":"Pruning Large Language Models with Semi-Structural Adaptive Sparse Training","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34592/36747"},{"title":"Teacher-Guided One-Shot Pruning via Context-Aware Knowledge Distillation","url":"https://arxiv.org/pdf/2511.16653"},{"title":"Post-Training Probability Manifold Correction via Structured SVD Pruning and Self-Referential Distillation","url":"https://arxiv.org/pdf/2602.00372"},{"title":"Constrained Edge AI Deployment: Fine-Tuning vs. Distillation for LLM Compression","url":"https://arxiv.org/html/2505.18166v1"},{"title":"Robustness-Reinforced Knowledge Distillation with Correlation Distance and Network Pruning","url":"https://arxiv.org/pdf/2311.13934"},{"title":"NIRVANA: Structured pruning reimagined for large language models compression","url":"https://arxiv.org/pdf/2509.14230"},{"title":"Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation","url":"https://arxiv.org/pdf/2604.00223"}]

Based on the web search results, here's what I found about KL divergence, distillation, structured pruning, and sparsity in 2025-2026:

## Structured vs. Unstructured Pruning

Structured pruning removes entire components like neurons, filters, or layers, directly reducing the model's computational complexity and memory footprint, and is particularly valuable for deployment scenarios where hardware acceleration depends on regular computational patterns. Structured pruning removes entire 
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7088
}
```

</details>

---


### Tool result

_source line 2025 · 2026-05-24T02:59:57.993567+00:00_

Web search results for query: "SVD-CSP sparsity predictor SVD decomposition 2026 LLM"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"Predicting LLM Compression Degradation from Spectral Statistics","url":"https://arxiv.org/pdf/2604.18085"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"SVD-LLM: Truncation-aware Singular Value Decomposition for Large   Language Model Compression","url":"https://arxiv.org/pdf/2403.07378"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://openreview.net/pdf?id=z83rodY0Pw"}]

Based on the search results, I found highly relevant information about SVD-CSP (SVD Contextual Sparsity Predictors) and related techniques for LLM inference and compression.

## SVD-CSP: Sparsity Predictors for Fast LLM Inference

The framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs). The research paper on this topic was published in March 2026.

### Performance Results

Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math.
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10397
}
```

</details>

---


### Tool call

_source line 2026 · 2026-05-24T03:00:03.764717+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2027 · 2026-05-24T03:00:03.915572+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We present an output-distribution KL framework for training contextual sparsity predictors in SwiGLU-based language models (Figure~\ref{fig:overview}).
5	The method replaces per-neuron binary classification (BCE) with an output-distribution alignment objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{x}^{(\ell)}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces p
…[truncated 9831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2028 · 2026-05-24T03:00:04.166585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2029 · 2026-05-24T03:00:04.217728+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $1 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (Deja
…[truncated 17382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2030 · 2026-05-24T03:00:09.687069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2031 · 2026-05-24T03:00:09.939069+00:00_

1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); output-distribution KL thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% o
…[truncated 41611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2032 · 2026-05-24T03:01:24.199523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ActTail\" activation sparsity LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ActTail\" activation sparsity LLM 2026"
  }
}
```

</details>

---


### Tool call

_source line 2033 · 2026-05-24T03:01:25.002447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Triton block sparse GPU kernel activation sparsity LLM inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Triton block sparse GPU kernel activation sparsity LLM inference 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 2034 · 2026-05-24T03:01:30.672061+00:00_

Web search results for query: ""ActTail" activation sparsity LLM 2026"

Links: [{"title":"[2603.12272] ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2603.12272"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2603.12272"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/html/2603.12272"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"},{"title":"Universal Properties of Activation Sparsity in Modern Large Language Models","url":"https://arxiv.org/pdf/2509.00454"}]

Based on the search results, I found information about ActTail:

ActTail is a TopK magnitude-based activation sparsity method with global activation sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement.

Existing activation sparsity methods typically apply uniform sparsity across projections, ignoring the heterogeneous statistical properties of Transformer weights and thereby amplifying performance degradation. ActTail captures this heterogeneity via the heavy-tail exponent computed from each projection's empirical spectral density (ESD), which is used as a quantitative indicator to assign projection-specific sparsity budgets.

Experiments on LLaMA and Mistral models show that the method improves both perplexity and downstream task performance at high sparsity compared to uniform allocation. At 80% sparsity, perplexity is reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, and 9.4% on Mistral-7B.

The research paper was submitted on March 16, 2026, making it a very recent contribution to the field of LLM optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6472
}
```

</details>

---


### Tool result

_source line 2035 · 2026-05-24T03:01:31.626036+00:00_

Web search results for query: "Triton block sparse GPU kernel activation sparsity LLM inference 2025 2026"

Links: [{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"From 11% to 88% Peak Bandwidth: Writing Custom Triton Kernels for LLM Inference | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2025/triton-kernels-llm-inference/"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Sparton: Fast and Memory-Efficient Triton Kernel for Learned Sparse Retrieval","url":"https://arxiv.org/html/2603.25011"},{"title":"ENABLING DYNAMIC SPARSITY IN QUANTIZED LLM INFERENCE","url":"https://arxiv.org/pdf/2511.04477"},{"title":"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference","url":"https://arxiv.org/pdf/2504.19449"}]

Based on the search results, here's what I found regarding Triton block sparse GPU kernels, activation sparsity, and LLM inference in 2025-2026:

## Recent Work on Triton Kernels for LLM Inference

For LLM inference optimization, the key shift is from thinking about FLOPS to thinking about memory bandwidth, as most operations are memory-bound, and custom Triton kernels can close performance gaps left by PyTorch.

## Activation Sparsity Approaches

Sparsification has emerged as a mainstream strategy to accelerate LLM inference by reducing the amount of computation required at run time. There are several approaches being explored:

- **Training-free methods**: Training-based activation sparsity methods "relufy" or otherwise modify/fine-tune models to encourage sparse activations under smooth non-linearities.

- **Hardware-friendly implementation**: Activation sparsity dyn
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6623
}
```

</details>

---


### Tool call

_source line 2036 · 2026-05-24T03:05:25.982248+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n### 总体评分\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 方法论上扎实的实证研究揭示了 KL 对 BCE 在稀疏性预测上的 PPL 优势，但新颖性增量有限、无 wall-clock 加速、且知识密集型任务的系统性退步严重削弱了实际价值。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实（3-seed, 多架构, 多消融）；但 1000 步 WikiText-103 训练规模极小，per-layer KL 分解自认有混淆因素（\"upper bound\"），实际稀疏率不完全匹配（28.5% vs 29.3%）虽有补偿分析但增加解读复杂度 |\n| Excitement | 2.5/5 | 核心发现（KL > BCE for sparsity prediction）符合信息论直觉，非高度意外；实际部署场景下无任何加速（+6.4% latency），知识任务全面退步，限制了研究的启发性 |\n| Reproducibility | 4/5 | 超参数完整，exp_id 标注清晰，3-seed 评估，承诺开源代码；但训练数据处理细节（tokenization, 数据划分）不够明确 |\n| Overall | 3.0/5 | 实证贡献达到 Findings 水平但不足以进入主会议：novelty 增量有限、无实际加速、知识退步未解决 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识密集型任务的系统性退步被严重低估（Framing 问题）\n\n- 具体位置：Abstract (\"directional commonsense gains\")、Section 4.2 Knowledge-Task Regression、Conclusion（仅 2 句话）\n- 问题：MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）。Abstract 用 \"directional commonsense gains (n=3) but knowledge-intensive regression\" 的并列结构暗示两者是同量级的 trade-off，但实际上退步幅度远大于提升幅度。Conclusion 仅 2 句话完全没有讨论这个问题的影响和未来研究方向。\n- 为什么影响接收：PPL improvement 虽然显著（14.5%），但 PPL 只是语言模型能力的代理指标。在下游任务（deployment-relevant metrics）上全面退步的方法，其实用性需要更审慎的讨论。\n- 建议修改方向：(1) Abstract 中明确量化退步幅度而非用 \"directional\" 模糊处理；(2) Conclusion 需要扩展到至少一段话，讨论 knowledge regression 的 implications 和 future directions；(3) 在 Section 4.2 中明确区分 PPL improvement 和 downstream improvement 的不同 implications\n\n**N2** [critical] 新颖性边界模糊——与 MaskLLM 的区分不充分\n\n- 具体位置：Section 2 Related Work（MaskLLM 段落）、Section 3.7 Table 1\n- 问题：MaskLLM (Fang et al., 2024) 已经使用 frozen weights + learnable masks + KL divergence 训练稀疏性。论文列出 3 点区别（static vs contextual, no cross-layer, input-independent），但这些区别的重要性缺乏实验验证。论文自己也承认 \"shares the recipe-level principle\"（page 3）。对于一篇定位为 \"primarily an empirical study\" 的论文，如果核心方法的每个组件都已被提出过，且 recipe-level 原则与 MaskLLM 共享，那么 \"组合新颖性\" 的 bar 需要由极强的实证发现来支撑——但知识退步削弱了这一支撑。\n- 为什么影响接收：EMNLP 对 novelty 的要求不仅是技术组件的新颖性，也包括 insight 的新颖性。\"KL 优于 BCE\" 在给定足够 output-level 信息的情况下符合直觉预期（end-to-end optimization over proxy optimization），不够 surprising。\n- 建议修改方向：(1) 加入与 MaskLLM 的直接实验对比；(2) 更清晰地阐述为什么 contextual activation sparsity 下的 KL 行为与 static N:M weight sparsity 下 qualitatively 不同；(3) 讨论 MaskLLM 的 \"学习时动态、推理时静态\" 中间态\n\n**N3** [critical] 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速\n\n- 具体位置：Appendix A (Table 5)、Section 1 (最后一段)、Limitations\n- 问题：当前方法在任何设置下都不提供推理加速。Predictor 增加 6.4% latency，但由于缺乏 sparse kernel 支持，稀疏 FFN 的计算量并未减少。4 条 contributions 中有 2 条标记为 \"Practical\"，但在无法提供任何加速的情况下，\"Practical\" 的标签有误导性。\n- 为什么影响接收：审稿人会合理质疑：如果方法不能提供加速，又在知识任务上退步，那么 \"better sparsity predictor\" 的价值何在？\n- 建议修改方向：(1) 将 contribution C3/C4 改为 \"Analytical\" 而非 \"Practical\"；(2) 在 Introduction 更早、更显著地声明无加速的现状\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Table 1 taxonomy 缺乏分析深度——空格子无分析，本质上只是 literature organization tool\n\n**W2** [warning] 训练规模极小（1000 步, ~8.2M tokens），无法确认更大规模下 KL vs BCE 的相对优势是否保持\n\n**W3** [warning] Per-layer KL 分解（§4.5）的 confound 未充分消除——K=1 混淆 coupling removal 与 train-inference mismatch，K=4 的 MMLU 异常说明分配模式本身就是 confound。\"May account for a substantial portion\" 的 claim 对于 admittedly exploratory 的分析过强\n\n**W4** [warning] Introduction 包含近 20 个数字，信息过载。建议只保留 3-5 个核心数字，其余推到 Section 4\n\n**W5** [warning] Conclusion 仅 2 句话——无 broader impact、future work、或 knowledge regression 解决方向的讨论\n\n**W6** [warning] 附录 25 个 section（A-Y, 9 页），审稿人认知负担大。部分关键数据（HellaSwag/PIQA downstream）本应在主文 Table 2 中\n\n### 小问题\n\n- Abstract ~190 words，合规但信息密度极高\n- Section 3 有 7 个 subsection（~2.5 页），对 \"primarily empirical study\" 而言 method section 偏重\n- Limitations 未显式提及仅验证了 SwiGLU 架构\n- Appendix Y 披露 Claude 用于 \"summarizing related papers\"——建议确认所有引用已人工验证\n\n### 格式合规性\n\n- 正文 8 页：合规\n- Limitations 在正文（page 9）：合规\n- 匿名性：合规（\"Anonymous ACL submission\"，无代码链接）\n- 引用格式：acl_natbib.bst，合规\n\n### 可能遗漏的相关工作\n\n- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配\n- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity\n- 总体 related work 覆盖面良好\n\n### 主要优势\n\n- 实验方法论扎实：3-seed 评估、exp_id 标注、cross-architecture 验证（3 个模型）、多层消融\n- Target-swap ablation (C1) 有独立的 insight 价值——证明 mask patterns 而非 gradient coupling 是 KL 优势的主要来源\n- 诚实的 limitation acknowledgment，比多数论文更透明\n- 补偿网络冗余性发现有工程简化价值\n- K-curve 分析揭示 coupling breadth 的非单调效应\n\n### Questions to Authors\n\n1. TEAL uniform 在 30% 时 MMLU 达到 45.86%（Table 2），显著高于 KL 的 40.7±1.3%。对于实际部署，TEAL 在 knowledge tasks 上是否是更好的选择？\n2. C4 训练控制实验显示 C4-trained predictor PPL 反而更差（11.55 vs 8.82），是否说明 KL predictor 在 overfitting WikiText-103 的 activation patterns？\n3. 能否提供 20-25% sparsity 下的详细 downstream 对比，展示 KL 在 practical regime 中的优势？\n4. Table 1 中 ShadowLLM 被归入 \"Per-token × Intermediate (MSE)\"，但其使用 attention-based routing——分类是否准确？",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n### 总体评分\n\n**Overall**: 3.0 (Findings)\n**Confidence**: 4/5\n**一句话总结**: 方法论上扎实的实证研究揭示了 KL 对 BCE 在稀疏性预测上的 PPL 优势，但新颖性增量有限、无 wall-clock 加速、且知识密集型任务的系统性退步严重削弱了实际价值。\n\n### 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计扎实（3-seed, 多架构, 多消融）；但 1000 步 WikiText-103 训练规模极小，per-layer KL 分解自认有混淆因素（\"upper bound\"），实际稀疏率不完全匹配（28.5% vs 29.3%）虽有补偿分析但增加解读复杂度 |\n| Excitement | 2.5/5 | 核心发现（KL > BCE for sparsity prediction）符合信息论直觉，非高度意外；实际部署场景下无任何加速（+6.4% latency），知识任务全面退步，限制了研究的启发性 |\n| Reproducibility | 4/5 | 超参数完整，exp_id 标注清晰，3-seed 评估，承诺开源代码；但训练数据处理细节（tokenization, 数据划分）不够明确 |\n| Overall | 3.0/5 | 实证贡献达到 Findings 水平但不足以进入主会议：novelty 增量有限、无实际加速、知识退步未解决 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 知识密集型任务的系统性退步被严重低估（Framing 问题）\n\n- 具体位置：Abstract (\"directional commonsense gains\")、Section 4.2 Knowledge-Task Regression、Conclusion（仅 2 句话）\n- 问题：MMLU 在 8B 上从 65.3% 降至 40.7%（-24.6pp，降幅 37.7%），在 14B 上 GSM8K 从 87.6% 降至 32.0±5.2%（-55.6pp，降幅 63.5%）。Abstract 用 \"directional commonsense gains (n=3) but knowledge-intensive regression\" 的并列结构暗示两者是同量级的 trade-off，但实际上退步幅度远大于提升幅度。Conclusion 仅 2 句话完全没有讨论这个问题的影响和未来研究方向。\n- 为什么影响接收：PPL improvement 虽然显著（14.5%），但 PPL 只是语言模型能力的代理指标。在下游任务（deployment-relevant metrics）上全面退步的方法，其实用性需要更审慎的讨论。\n- 建议修改方向：(1) Abstract 中明确量化退步幅度而非用 \"directional\" 模糊处理；(2) Conclusion 需要扩展到至少一段话，讨论 knowledge regression 的 implications 和 future directions；(3) 在 Section 4.2 中明确区分 PPL improvement 和 downstream improvement 的不同 implications\n\n**N2** [critical] 新颖性边界模糊——与 MaskLLM 的区分不充分\n\n- 具体位置：Section 2 Related Work（MaskLLM 段落）、Section 3.7 Table 1\n- 问题：MaskLLM (Fang et al., 2024) 已经使用 frozen weights + learnable masks + KL divergence 训练稀疏性。论文列出 3 点区别（static vs contextual, no cross-layer, input-independent），但这些区别的重要性缺乏实验验证。论文自己也承认 \"shares the recipe-level principle\"（page 3）。对于一篇定位为 \"primarily an empirical study\" 的论文，如果核心方法的每个组件都已被提出过，且 recipe-level 原则与 MaskLLM 共享，那么 \"组合新颖性\" 的 bar 需要由极强的实证发现来支撑——但知识退步削弱了这一支撑。\n- 为什么影响接收：EMNLP 对 novelty 的要求不仅是技术组件的新颖性，也包括 insight 的新颖性。\"KL 优于 BCE\" 在给定足够 output-level 信息的情况下符合直觉预期（end-to-end optimization over proxy optimization），不够 surprising。\n- 建议修改方向：(1) 加入与 MaskLLM 的直接实验对比；(2) 更清晰地阐述为什么 contextual activation sparsity 下的 KL 行为与 static N:M weight sparsity 下 qualitatively 不同；(3) 讨论 MaskLLM 的 \"学习时动态、推理时静态\" 中间态\n\n**N3** [critical] 无 wall-clock 加速 + predictor 增加 6.4% latency = 实际减速\n\n- 具体位置：Appendix A (Table 5)、Section 1 (最后一段)、Limitations\n- 问题：当前方法在任何设置下都不提供推理加速。Predictor 增加 6.4% latency，但由于缺乏 sparse kernel 支持，稀疏 FFN 的计算量并未减少。4 条 contributions 中有 2 条标记为 \"Practical\"，但在无法提供任何加速的情况下，\"Practical\" 的标签有误导性。\n- 为什么影响接收：审稿人会合理质疑：如果方法不能提供加速，又在知识任务上退步，那么 \"better sparsity predictor\" 的价值何在？\n- 建议修改方向：(1) 将 contribution C3/C4 改为 \"Analytical\" 而非 \"Practical\"；(2) 在 Introduction 更早、更显著地声明无加速的现状\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Table 1 taxonomy 缺乏分析深度——空格子无分析，本质上只是 literature organization tool\n\n**W2** [warning] 训练规模极小（1000 步, ~8.2M tokens），无法确认更大规模下 KL vs BCE 的相对优势是否保持\n\n**W3** [warning] Per-layer KL 分解（§4.5）的 confound 未充分消除——K=1 混淆 coupling removal 与 train-inference mismatch，K=4 的 MMLU 异常说明分配模式本身就是 confound。\"May account for a substantial portion\" 的 claim 对于 admittedly exploratory 的分析过强\n\n**W4** [warning] Introduction 包含近 20 个数字，信息过载。建议只保留 3-5 个核心数字，其余推到 Section 4\n\n**W5** [warning] Conclusion 仅 2 句话——无 broader impact、future work、或 knowledge regression 解决方向的讨论\n\n**W6** [warning] 附录 25 个 section（A-Y, 9 页），审稿人认知负担大。部分关键数据（HellaSwag/PIQA downstream）本应在主文 Table 2 中\n\n### 小问题\n\n- Abstract ~190 words，合规但信息密度极高\n- Section 3 有 7 个 subsection（~2.5 页），对 \"primarily empirical study\" 而言 method section 偏重\n- Limitations 未显式提及仅验证了 SwiGLU 架构\n- Appendix Y 披露 Claude 用于 \"summarizing related papers\"——建议确认所有引用已人工验证\n\n### 格式合规性\n\n- 正文 8 页：合规\n- Limitations 在正文（page 9）：合规\n- 匿名性：合规（\"Anonymous ACL submission\"，无代码链接）\n- 引用格式：acl_natbib.bst，合规\n\n### 可能遗漏的相关工作\n\n- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配\n- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity\n- 总体 related work 覆盖面良好\n\n### 主要优势\n\n- 实验方法论扎实：3-seed 评估、exp_id 标注、cross-architecture 验证（3 个模型）、多层消融\n- Target-swap ablation (C1) 有独立的 insight 价值——证明 mask patterns 而非 gradient coupling 是 KL 优势的主要来源\n- 诚实的 limitation acknowledgment，比多数论文更透明\n- 补偿网络冗余性发现有工程简化价值\n- K-curve 分析揭示 coupling breadth 的非单调效应\n\n### Questions to Authors\n\n1. TEAL uniform 在 30% 时 MMLU 达到 45.86%（Table 2），显著高于 KL 的 40.7±1.3%。对于实际部署，TEAL 在 knowledge tasks 上是否是更好的选择？\n2. C4 训练控制实验显示 C4-trained predictor PPL 反而更差（11.55 vs 8.82），是否说明 KL predictor 在 overfitting WikiText-103 的 activation patterns？\n3. 能否提供 20-25% sparsity 下的详细 downstream 对比，展示 KL 在 practical regime 中的优势？\n4. Table 1 中 ShadowLLM 被归入 \"Per-token × Intermediate (MSE)\"，但其使用 attention-based routing——分类是否准确？",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2037 · 2026-05-24T03:05:29.494230+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3511
}
```

</details>

---


### Assistant

_source line 2038 · 2026-05-24T03:05:40.146311+00:00_

审稿意见已提交给 Review Director。

总结：

- **Overall 3.0 (Findings)**，Soundness 3.5, Excitement 2.5, Confidence 4/5
- **3 个 Must-Fix**：(1) 知识退步被 framing 低估（MMLU -24.6pp 却用 "directional" 模糊处理）；(2) 与 MaskLLM 的 novelty 区分不充分（共享 recipe-level 原则）；(3) 无 wall-clock 加速却标注 "Practical" contributions
- **6 个 Should-Fix**：taxonomy 浅、训练规模极小、per-layer KL 分解有 confounds、Introduction 数字过载、Conclusion 仅 2 句、附录 25 节过长
- **主要优势**：实验方法论扎实（3-seed, 3 架构）、target-swap ablation 有 insight 价值、透明的 limitation disclosure

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 49

## Round 49

4 recorded events


### User

_source line 2039 · 2026-05-24T03:07:29.145171+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（方法严谨性 + 实验设计）

### Summary

本文研究 SwiGLU LLM 中上下文稀疏性预测器的训练目标选择。核心提议是用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛实现可微 mask 采样，训练轻量级预测器（<1% 参数）。在 LLaMA-3.1-8B 上，30% 稀疏度下 KL 预测器 PPL 比 TEAL 低 14.5%（8.81 vs 10.30），但 MMLU/GSM8K 出现系统性回退。C1 target-swap ablation 表明 KL 发现的 mask 模式可迁移到 BCE。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。跨架构验证确认 PPL 优势可泛化。

### 总体评分

**Overall**: 3.0 — Findings
**置信度**: 4/5

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法合理；但 per-layer KL 分解存在根本性 train-inference mismatch，下游 metric 统计功效不足 |
| Excitement | 3/5 | 输出分布对齐训练稀疏预测器是有趣的方向；但方法本身是 KL 蒸馏 + Gumbel-Sigmoid 的组合，新颖性有限；下游回退限制实用价值 |
| Reproducibility | 4/5 | 训练细节充分，承诺开源代码和 checkpoint；多 seed 实验增加可信度 |

### Must-Fix 问题

**N1** [critical] Per-layer KL 分解的 train-inference mismatch 使核心 decomposition claim 站不住脚

- §4.5, Table 4, Figure 2
- K=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时被 mask——根本性 train-inference mismatch。K=1 (PPL 9.05) vs E2E (8.81) 只有 2.7% gap 是因为 K=1 近似 dense evaluation。
- 关键证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×）；K=4 在 50% 更差（44.23）；K-curve 非单调（K=2 最差 10.75）
- 建议：(1) 将 K=1 结果标注为 "upper bound only"；(2) 报告 K=4 在 30% 的完整 downstream CI；(3) 讨论为什么 decomposition 在 50% 失效

**N2** [critical] 下游知识任务系统性回退缺乏机制性解释

- Table 2, §4.2, §4.6
- KL 在所有模型/规模上系统性损害 MMLU 和 GSM8K（8B: -5.2pp MMLU, 14B: -20.1pp GSM8K）
- C4 控制排除了训练数据偏差，但 forward KL mode-covering 假设没有直接验证（如分析是否 prune 了 factual neurons）
- 建议：(1) 分析 KL mask 对 factual neurons 的保留率；(2) 讨论 hybrid loss 可能性；(3) 重新框定为 "PPL-optimal but not task-universal"

**N3** [critical] 下游 metric 统计功效严重不足

- Table 2, §4.2, §4.6
- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]
- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，95% CI ≈ ±7.4pp
- 论文承认 "95% CI overlap" 但仍在 abstract/conclusion 以确定性措辞报告 gap
- 建议：(1) 增加 seed 到 ≥5；(2) 对 TEAL 也跑多次；(3) 所有比较报告 CI 和 overlap 标注

### Should-Fix 问题

**W1** [warning] C1 target-swap ablation 的 confound 未充分控制
- s42 oracle 来自 non-seed-matched earlier training run
- BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，confound 未消除
- 建议统一 seed-matched oracle + 增加 "BCE+Gumbel on KL targets" 条件

**W2** [warning] MSE baseline 在 50% 下几乎不可信
- s123 catastrophic (PPL=15,789)，2/3 seed 失败
- 建议移至 Appendix 或仅在 30% 使用

**W3** [warning] 30% 下缺少 BCE isocompute 对比

**W4** [warning] ε=0.02 deadzone margin 缺乏 sensitivity analysis

**W5** [warning] 主评估指标单一（仅 WikiText-2 PPL）

### 小问题

- TEAL 是 deterministic single-run vs KL 3-seed 比较不对等
- Figure 3 只展示 global allocation
- §3.6 Gradient Analysis 是 "suggestive" 但在 introduction 被列为核心贡献
- 推理时 Gumbel-Sigmoid 是否被 hard threshold 替换应明确说明

### 主要优势

1. PPL 改善显著且一致（14.5%-50%）
2. 实验覆盖面广（3 seeds, 5 losses, 3 architectures, 2 sparsity levels）
3. C1 target-swap ablation 设计有创意
4. 诚实报告负面结果
5. Taxonomy 有组织价值
6. 可复现性好

### 缺失引用

- 建议补充 LoRAShear（structured pruning + knowledge recovery）
- 建议补充 ZipLM（data-aware structured pruning）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2040 · 2026-05-24T03:09:43.656471+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n### Must-Fix\n\n[AGREE] R1-N1: Per-layer KL decomposition train-inference mismatch。完全同意。50% 下 K=1 PPL=34.85 vs E2E=11.84（Table 4）提供 decisive evidence——mismatch 加剧时 K=1 的\"信号类型优势\"完全瓦解。K=4 在 50% 反而更差（44.23 vs 34.85），论文自己承认 \"the decomposition is interpretable only at 30%\"（§4.5）。一个仅在 30% 有效且有未消除 confound 的 exploratory analysis 不应作为核心 contribution 呈现。我在自己的审稿中将此列为 W3，但认同 R1 将其提升至 critical 的判断。\n\n[AGREE] R1-N2: 下游知识任务回退缺乏机制性解释。与我的 N1 呼应。补充：Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）说明的是 allocation pattern 影响而非 mode-covering 机制。C4 控制实验排除训练数据偏差后反而强化了\"问题是 structural\"的结论，但论文没有进一步追问 *为什么* 是 structural。R1 建议的 hybrid loss 方向是论文完全缺失的 future direction。\n\n[AGREE] R1-N3: 下游 metric 统计功效不足。KL global 30% MMLU 35.7±9.5（n=3）差异极大。补充：Qwen-14B GSM8K 32.0±5.2（Table 13）CV=16.3%，不足以在 p<0.05 下确认与 TEAL（52.1%）的差异方向。不过 ≥5 seeds 在 14B 上可能有计算预算限制——至少应做 upfront disclosure。\n\n### Should-Fix\n\n[AGREE] R1-W1: C1 confounds。两个问题叠加：s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。不过 s123/s456 seed-matched oracles gap ≤1.18pp 部分缓解了 concern。\n\n[AGREE] R1-W2: MSE 50% 不可信。s123 只达 5.1% sparsity（PPL=15,789），50% MSE 实际是单 seed 结果。\n\n[AGREE] R1-W3: 30% 缺 BCE isocompute。\n\n[REBUT] R1-W4: ε deadzone sensitivity。Appendix C（Table 9, Figure 4）间接展示了 ε=0.02 的稳定收敛。ε 是 auxiliary mechanism，重要性不高。Low-effort improvement 可以做但非 must-fix。\n\n[AGREE] R1-W5: 主指标单一。部分同意——WikiText-2 与 WikiText-103 同源，C4 OOD evaluation（Appendix D）缓解但 cross-seed variance 显著更高（CV=6.3% vs 0.2%）。建议 C4 PPL 纳入主表。\n\n### 小问题\n\n[AGREE] TEAL deterministic vs KL 3-seed 不对等\n[AGREE] Figure 3 只展示 global allocation\n[AGREE] §3.6 Gradient Analysis \"suggestive\" vs 核心贡献的 caveat 不一致\n[REBUT] 推理时 Gumbel→hard threshold 已在 §3.1 和 §3.3 明确说明\n\n### 缺失引用\n\n[REBUT] LoRAShear/ZipLM：两者是 weight pruning 方法，非 activation sparsity prediction。Section 2 已有 Wanda/SparseGPT/SliceGPT 覆盖此类。更相关的遗漏是 ActTail (2026) 和 WiSparse (2026)。\n\n### 与 R1 的分歧\n\n1. R1 未将 novelty/MaskLLM 区分列为 critical——我认为这是核心 weakness（我的 N2）\n2. R1 未将无 wall-clock 加速列为 critical——我认为 \"Practical\" 标签在 +6.4% latency 下 misleading（我的 N3）\n3. Excitement：R1 给 3/5，我给 2.5/5——\"KL > BCE\" 是 information-theoretically expected\n\n### 共识：Overall 3.0 (Findings)",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n### Must-Fix\n\n[AGREE] R1-N1: Per-layer KL decomposition train-inference mismatch。完全同意。50% 下 K=1 PPL=34.85 vs E2E=11.84（Table 4）提供 decisive evidence——mismatch 加剧时 K=1 的\"信号类型优势\"完全瓦解。K=4 在 50% 反而更差（44.23 vs 34.85），论文自己承认 \"the decomposition is interpretable only at 30%\"（§4.5）。一个仅在 30% 有效且有未消除 confound 的 exploratory analysis 不应作为核心 contribution 呈现。我在自己的审稿中将此列为 W3，但认同 R1 将其提升至 critical 的判断。\n\n[AGREE] R1-N2: 下游知识任务回退缺乏机制性解释。与我的 N1 呼应。补充：Appendix T 的 constraint analysis（remove valley → MMLU +3.4pp）说明的是 allocation pattern 影响而非 mode-covering 机制。C4 控制实验排除训练数据偏差后反而强化了\"问题是 structural\"的结论，但论文没有进一步追问 *为什么* 是 structural。R1 建议的 hybrid loss 方向是论文完全缺失的 future direction。\n\n[AGREE] R1-N3: 下游 metric 统计功效不足。KL global 30% MMLU 35.7±9.5（n=3）差异极大。补充：Qwen-14B GSM8K 32.0±5.2（Table 13）CV=16.3%，不足以在 p<0.05 下确认与 TEAL（52.1%）的差异方向。不过 ≥5 seeds 在 14B 上可能有计算预算限制——至少应做 upfront disclosure。\n\n### Should-Fix\n\n[AGREE] R1-W1: C1 confounds。两个问题叠加：s42 non-seed-matched + BCE+Gumbel (32.22) 比 BCE (27.97) 更差说明 Gumbel 对 BCE 有害。不过 s123/s456 seed-matched oracles gap ≤1.18pp 部分缓解了 concern。\n\n[AGREE] R1-W2: MSE 50% 不可信。s123 只达 5.1% sparsity（PPL=15,789），50% MSE 实际是单 seed 结果。\n\n[AGREE] R1-W3: 30% 缺 BCE isocompute。\n\n[REBUT] R1-W4: ε deadzone sensitivity。Appendix C（Table 9, Figure 4）间接展示了 ε=0.02 的稳定收敛。ε 是 auxiliary mechanism，重要性不高。Low-effort improvement 可以做但非 must-fix。\n\n[AGREE] R1-W5: 主指标单一。部分同意——WikiText-2 与 WikiText-103 同源，C4 OOD evaluation（Appendix D）缓解但 cross-seed variance 显著更高（CV=6.3% vs 0.2%）。建议 C4 PPL 纳入主表。\n\n### 小问题\n\n[AGREE] TEAL deterministic vs KL 3-seed 不对等\n[AGREE] Figure 3 只展示 global allocation\n[AGREE] §3.6 Gradient Analysis \"suggestive\" vs 核心贡献的 caveat 不一致\n[REBUT] 推理时 Gumbel→hard threshold 已在 §3.1 和 §3.3 明确说明\n\n### 缺失引用\n\n[REBUT] LoRAShear/ZipLM：两者是 weight pruning 方法，非 activation sparsity prediction。Section 2 已有 Wanda/SparseGPT/SliceGPT 覆盖此类。更相关的遗漏是 ActTail (2026) 和 WiSparse (2026)。\n\n### 与 R1 的分歧\n\n1. R1 未将 novelty/MaskLLM 区分列为 critical——我认为这是核心 weakness（我的 N2）\n2. R1 未将无 wall-clock 加速列为 critical——我认为 \"Practical\" 标签在 +6.4% latency 下 misleading（我的 N3）\n3. Excitement：R1 给 3/5，我给 2.5/5——\"KL > BCE\" 是 information-theoretically expected\n\n### 共识：Overall 3.0 (Findings)",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2041 · 2026-05-24T03:09:47.273104+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3616
}
```

</details>

---


### Assistant

_source line 2042 · 2026-05-24T03:09:54.645485+00:00_

交叉回应已提交。

总结：R1 的 7 个问题中我同意 6 个（N1-N3, W1-W3, W5）、部分反驳 1 个（W4 ε sensitivity 重要性较低）。小问题中反驳了推理时 Gumbel 替换的说明（已在 §3.1/3.3 明确）和缺失引用建议（LoRAShear/ZipLM 是 weight pruning 而非 activation sparsity）。两位 reviewer 在 Overall 3.0 (Findings)、知识退步 framing、统计功效、per-layer decomposition confounds 上形成共识。主要分歧在于我额外将 novelty/MaskLLM 区分和无 wall-clock 加速列为 critical issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 50

## Round 50

58 recorded events


### User

_source line 2043 · 2026-05-24T04:24:08.396210+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。

## 论文信息
- **标题**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
- **路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf

## Venue 要求
- **EMNLP 2026** via ACL Rolling Review (ARR)
- **Deadline**: 2026-05-25
- **页数限制**: Long paper 8 页正文 + unlimited references + Limitations 不计入页数
- **模板**: ACL template with `[review]` option
- **匿名**: Double-blind（不出现作者信息、避免自引）
- **附录**: 在 references 之后，不计入页数，reviewer 不保证会读

## 你的审查侧重

请重点审查以下方面：

1. **新颖性评估**
   - 核心 recipe（frozen model + learnable mask + KL + Gumbel relaxation）与 MaskLLM 共享程度——contextual vs static 的区别是否构成足够新颖性
   - 各组件（KL distillation、Gumbel-Sigmoid、top-k allocation）均为 established techniques，组合新颖性是否达到 EMNLP 标准
   - Taxonomy（Table 1）的 positioning 是否准确，是否遗漏重要相关工作

2. **Claim 与证据匹配**
   - Abstract/Introduction 中的 claim 是否被实验充分支撑
   - "Primary design dimension" claim 的 scope 是否合理限定
   - 知识任务退步（MMLU/GSM8K）的讨论是否充分
   - Contribution list 中 "Empirical" vs "Analytical" 标注是否准确

3. **写作质量**
   - 论文结构和叙事流畅度
   - 信息密度是否合适（是否过度压缩或冗余）
   - Conclusion 是否充分讨论 implications 和 future directions
   - 术语一致性
   - Figure/Table 质量和信息量

4. **完整性**
   - Related Work 覆盖度（是否遗漏 2025-2026 重要工作）
   - Limitations 节是否充分
   - 评估基准覆盖度
   - 可复现性信息是否充足

请以 ACL/EMNLP 审稿标准产出结构化审稿意见：Summary, Strengths (S1-Sn), Weaknesses (W1-Wn), Questions (Q1-Qn), Missing References, Minor Issues, Overall Assessment (1-5 scale per EMNLP 2026 ARR rubric)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2044 · 2026-05-24T04:24:20.429527+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 2045 · 2026-05-24T04:24:20.429950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2046 · 2026-05-24T04:24:30.669968+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2047 · 2026-05-24T04:24:30.670328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 2048 · 2026-05-24T04:24:33.030616+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2049 · 2026-05-24T04:24:37.597637+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form scoring dimensions"

Links: [{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, I found some relevant information about EMNLP 2026 and reviewer guidelines. However, the results don't contain specific details about the EMNLP 2026 review form scoring dimensions themselves.

Here's what I found:

**EMNLP 2026 Reviewer Timeline:**
If you receive assignments, your reviews must be completed by July 6, or your meta-reviews - by July 29.

**General Reviewing Criteria:**
While the search results don't specifically detail EMNLP 2026's exact scoring dimensions, they reference standard reviewing criteria used in the field. Typical criteria include: Is the submission technically sound? Are claims well supported? Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest about evaluating both the strengths and weaknesses of their work? Is the submission clearly written? Is it well organized? Does it adequately inform the reader?

**ARR Review Scores:**
Since EMNLP 2026 uses ACL Rolling Review (ARR) for submissions, starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

For the specific EMNLP 2026 revie
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6927
}
```

</details>

---


### Tool result

_source line 2050 · 2026-05-24T04:24:38.099684+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I've found information about ACL ARR 2026 reviewer guidelines, review forms, and criteria. Here are the key findings:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations ma
…[truncated 1230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7429
}
```

</details>

---


### Tool result

_source line 2051 · 2026-05-24T04:24:39.405587+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 587.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 529.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6374
}
```

</details>

---


### Tool call

_source line 2052 · 2026-05-24T04:24:45.396199+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially look for: soundness, excitement/novelty, overall assessment, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Especially look for: soundness, excitement/novelty, overall assessment, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 2053 · 2026-05-24T04:24:46.851819+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, what constitutes a good/bad review, specific instructions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria, what constitutes a good/bad review, specific instructions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 2054 · 2026-05-24T04:24:47.303985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2055 · 2026-05-24T04:24:47.806653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 2056 · 2026-05-24T04:24:48.711621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 2057 · 2026-05-24T04:24:48.712911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 2058 · 2026-05-24T04:24:48.713235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2059 · 2026-05-24T04:24:49.215744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2060 · 2026-05-24T04:24:49.620845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2061 · 2026-05-24T04:24:49.625651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 2062 · 2026-05-24T04:24:50.180829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool result

_source line 2063 · 2026-05-24T04:24:50.482619+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool result

_source line 2064 · 2026-05-24T04:24:53.040771+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scoring Dimensions

**Soundness**
- Scale: 1-5 (with .5 increments)
- Evaluates scientific rigor, claim support, and methodological validity across paper types

**Excitement**
- Scale: 1-5 (with .5 increments)
- Subjective assessment of innovation, transformational potential, and community impact

**Overall Assessment**
- Scale: 1-5 (with .5 increments)
- Primary recommendation spanning award consideration through rejection

## Secondary Evaluation Dimensions

**Reviewer Confidence**
- Scale: 1-5
- Assesses evaluator familiarity with subject matter and thoroughness of review

**Reproducibility**
- Scale: 1-5
- Measures adequacy of provided details for result replication

**Datasets Value**
- Scale: 1-5
- Rates impact and usefulness of released research data

**Software Value**
- Scale: 1-5
- Rates impact and usefulness of released code

**Author Identity Knowledge**
- Scale: 1-5
- Documents potential double-blind violations

## Qualitative Sections

The form includes narrative components: paper summary, strength/weakness summaries, suggestions, limitations/societal impact, ethical concerns assessment, and ethics review determination.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7644
}
```

</details>

---


### Tool result

_source line 2065 · 2026-05-24T04:25:00.669493+00:00_

# ARR Reviewer Guidelines: Complete Summary

## Core Evaluation Tasks

Reviewers must complete four primary tasks:

1. **Allocate Time**: Block calendar time for reading, writing reviews, and participating in discussions
2. **Check Assignments**: Verify expertise match, conflicts of interest, and desk-rejection criteria
3. **Write Strong Reviews**: Provide detailed, specific feedback on soundness, excitement, and recommendations
4. **Engage in Discussion**: Respond to author rebuttals and colleague reviewers before finalizing assessments

## Scoring Framework

Starting February 2025, ARR uses three scores:

- **Soundness**: Technical validity must be justified by review text; low scores require explicit justification
- **Excitement**: Personal interest independent of soundness; more subjective
- **Overall Assessment**: Composite recommendation reflecting soundness, excitement, novelty, and potential impact

## Strong Review Characteristics

Reviewers should:

- **Be Specific**: Replace vague criticism like "unclear writing" with "Y and Z are missing from the description of X"
- **Read Twice**: First skim to adjust expectations, then deep read for evaluation
- **Avoid Unconscious Biases**: The guidelines list 17 common heuristics that mislead reviewers, from dismissing surprising results to demanding unnecessary experiments
- **Maintain Professional Tone**: "Write the review you would like to get yourself"

## Common Review Pitfalls (H1-H17)

Examples include:
- Dismissing results as "obvious in retrospect" despite being novel
- Requiring SOTA performance when not claimed
- Penalizing negative results
- Treating acknowledged limitations as rejection reasons
- Requesting comparisons to closed-source models without necessity

## NLP-Specific Issues to Flag

Categories include:

- **Methodology (M1-M5)**: LLM evaluation validation, reproducibility details, data quality, assumption clarity
- **Artifacts (T1-T2)**: Ethics compliance, licensing transparency
- **Results (R1
…[truncated 1884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 13817
}
```

</details>

---


### Tool call

_source line 2066 · 2026-05-24T04:25:18.560748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 2067 · 2026-05-24T04:25:18.862325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 2068 · 2026-05-24T04:25:18.964223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2069 · 2026-05-24T04:25:19.065491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 2070 · 2026-05-24T04:25:19.117185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2071 · 2026-05-24T04:25:19.374171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 813
}
```

</details>

---


### Tool result

_source line 2072 · 2026-05-24T04:25:20.934740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2072
}
```

</details>

---


### Tool result

_source line 2073 · 2026-05-24T04:25:21.187540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---


### Tool result

_source line 2074 · 2026-05-24T04:25:21.289123+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2223
}
```

</details>

---


### Tool result

_source line 2075 · 2026-05-24T04:25:21.290439+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2173
}
```

</details>

---


### Tool call

_source line 2076 · 2026-05-24T04:25:29.566774+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2077 · 2026-05-24T04:25:30.719913+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 311.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png\", \"w
…[truncated 510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1153
}
```

</details>

---


### Tool call

_source line 2078 · 2026-05-24T04:25:33.420340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2079 · 2026-05-24T04:25:33.923597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2080 · 2026-05-24T04:25:34.832007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool call

_source line 2081 · 2026-05-24T04:25:34.832519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 2082 · 2026-05-24T04:25:35.587585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2083 · 2026-05-24T04:25:35.792307+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1868
}
```

</details>

---


### Tool call

_source line 2084 · 2026-05-24T04:25:35.792755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 2085 · 2026-05-24T04:25:36.899716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2086 · 2026-05-24T04:25:37.456859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2624
}
```

</details>

---


### Tool call

_source line 2087 · 2026-05-24T04:25:37.457328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2088 · 2026-05-24T04:25:37.861085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2089 · 2026-05-24T04:25:38.820140+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3232
}
```

</details>

---


### Tool call

_source line 2090 · 2026-05-24T04:25:38.820594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 2091 · 2026-05-24T04:25:38.820917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 2092 · 2026-05-24T04:25:39.175769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3383
}
```

</details>

---


### Tool result

_source line 2093 · 2026-05-24T04:25:39.176809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool result

_source line 2094 · 2026-05-24T04:25:39.690651+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2233
}
```

</details>

---


### Tool result

_source line 2095 · 2026-05-24T04:25:40.402143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3502
}
```

</details>

---


### Tool result

_source line 2096 · 2026-05-24T04:25:40.757192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2896
}
```

</details>

---


### Tool result

_source line 2097 · 2026-05-24T04:25:40.958903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2138
}
```

</details>

---


### Tool call

_source line 2098 · 2026-05-24T04:31:48.003134+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## Paper Summary\n\n本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE 来训练 SwiGLU LLM 的上下文稀疏性预测器。核心方法包括：冻结基模型 + 每层独立 2-layer MLP 预测器 + Gumbel-Sigmoid 松弛 + 几何惩罚调度实现目标稀疏度。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下相比 TEAL 降低 14.5% PPL。论文还提出了一个二维分类法（correction granularity × training signal coupling），分析 KL 相对 BCE 的梯度耦合机制，并通过大量消融实验研究了设计空间。\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计与消融分析**\n论文的实验设计非常扎实：3-seed means with standard deviations, target-swap ablation (Table 3), per-layer coupling breadth sweep (Figure 2), compensation冗余性分析 (Table 4), OOD评估 (Appendix D), 以及跨架构验证 (Mistral-7B, Qwen-2.5-14B)。每个 claim 都有对应的 controlled experiment 支撑。附录包含约 20 个补充实验（Appendix A–W），展示了极为彻底的验证工作。\n\n**S2. 有价值的梯度分析（§3.6）**\n§3.6 对比了 BCE 和 KL 的梯度结构：BCE 梯度仅依赖单个 neuron $j$，而 KL 通过下游 Jacobian $\\partial \\hat{p}_v / \\partial g^{(l)}_j$ 将每个 neuron 的 mask 决策与所有其他 neuron 的输出效应耦合。这一分析为\"为什么 KL 能发现更好的 mask\"提供了直觉上的解释，虽然不是严格的理论结果，但对读者理解方法差异很有帮助。\n\n**S3. 实用的二维分类法（Table 1）**\n将已有学习型稀疏方法沿 correction granularity（per-token vs. per-corpus）和 training signal coupling（decomposed/local/coupled）两个维度组织，清晰定位了本文方法的位置，并指出设计空间中未被探索的组合。这对社区有参考价值。\n\n**S4. 诚实的局限性讨论**\n论文坦诚报告了知识任务退化（MMLU -12.7pp, GSM8K 几乎崩塌）、50% 稀疏度下所有方法均失效、以及 wall-clock speedup 未测量等问题。这种透明度值得肯定。\n\n**S5. Target-swap ablation 设计精巧（Table 3）**\n通过让 BCE 预测器使用 KL 发现的 oracle mask 进行训练，巧妙地分离了\"mask 质量\"和\"训练目标\"的贡献。结果表明 KL 发现的 mask targets 可以迁移到 BCE，PPL 从 13.13 降至 11.79，证实了 mask 质量本身是关键因素。\n\n---\n\n## Weaknesses\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 §2 中承认了这一点：*\"Unlike MaskLLM...which applies KL to static N:M weight masks, we address contextual activation sparsity.\"* 但\"contextual vs. static\"的区分未被充分论证为足够的独立贡献：\n\n- MaskLLM 的 KL + Gumbel 训练框架是否可以直接扩展到 contextual 设置，只需将 static mask parameters 替换为 input-dependent predictor？如果是，方法学贡献主要是 engineering 而非 research。\n- §3.6 的梯度分析是 contextual 设置特有的（因为 mask 是 hidden state 的函数），但该分析是基于 chain rule 的直接推导，理论深度有限。\n- 论文未讨论从 static 到 contextual 的扩展中遇到了哪些 non-trivial 的技术挑战。\n\n建议：明确列出 contextual setting 引入的 unique challenges（如泛化到 unseen inputs、cross-layer coordination 的动态性、predictor 容量与表达力的 trade-off），并讨论 MaskLLM 框架无法直接处理这些挑战的原因。\n\n**W2. [Major] 知识任务退化严重但分析不足**\n\nTable 2 显示 30% 稀疏度下：\n- MMLU: 40.7 (dense) → 28.0 (KL uniform)，降幅 31%\n- GSM8K: 19.9 → 0.2，几乎完全崩塌\n\n这是非常严重的实际问题。论文给出的解释主要有两个：\n1. 训练数据组成（§4.3, Appendix V）：C4-trained predictor achieves comparable MMLU (40.6%) but worse GSM8K (4.1% vs. 7.4%)——说明训练数据不是唯一原因。\n2. Task-dependent coupling effects（§4.5）：per-layer controls 显示 commonsense 和 knowledge 任务对 coupling 的敏感度不同。\n\n但论文未回答关键问题：**为什么 output-distribution alignment（KL）这个似乎更优的目标反而导致知识任务严重退化？** 如果 KL 发现了更好的 mask（PPL 更低），为什么这些 mask 不能保留知识能力？这暗示 KL 优化的 PPL 与下游 knowledge task 之间存在根本性的 misalignment，但论文未深入分析。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n\n论文在 §4.5 和 abstract/contributions 中声称 training signal coupling 是 \"the primary design dimension\"。但证据只比较了 Table 1 taxonomy 中的两个维度（correction granularity × signal coupling）。其他潜在重要的设计维度未被系统比较：\n- Predictor capacity（bottleneck dimension d_b, 目前固定为 128）\n- Training data selection（仅在 Appendix V 中简短探索）\n- Training duration（Appendix B.2 显示 convergence，但未探索 over-training effects）\n- Sparsity allocation strategy（global top-k vs. per-layer budgets）\n\n\"Primary\" 这个断言隐含了对所有设计维度的 exhaustive comparison，但实际上只比较了两个。建议改为 \"a key design dimension\" 或限定 scope 为 \"among the two dimensions in our taxonomy\"。\n\n此外，§4.5 自身也承认了 confounding：per-layer KL 实验中 train-inference mismatch（K=1 masks 1/32 layers during training vs. all 32 at inference）、per-layer update count disparity 都可能混淆结论。在 confounding 未完全解决的情况下做出\"primary\"断言不够审慎。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n\n对于以推理效率为动机的论文，完全缺少 wall-clock 测量是显著缺陷。Appendix A 报告了 throughput overhead（KL-sparse pipeline 增加 6.4% 开销），但这是预测器本身的开销，不是最终的端到端加速。论文明确承认 *\"wall-clock speedup requires sparse kernel support not addressed here\"*（page 8），但这使得读者无法评估方法的实际影响力。\n\n与之对比，TEAL 等 training-free 方法虽然质量更差但可以直接在现有 sparse kernels 上运行。一个自然的问题是：KL 预测器发现的 mask patterns（非结构化 top-k）是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\n\nC3 和 C4 被标注为 \"Analytical\"，但其内容分别是 target-swap ablation 和 compensation redundancy 实验——这些是实验性发现，不是形式化分析/理论推导。在 ACL/EMNLP 社区，\"Analytical contribution\" 通常指数学推导、理论 bounds 或 formal analysis。建议改为 \"Empirical\" 或 \"Ablation-based\"，避免误导读者期待理论结果。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n\n所有主要实验（Tables 2-4, Figures 2-3）仅在 LLaMA-3.1-8B 上完成。跨架构验证仅有：\n- Mistral-7B-v0.3: 简短提及 (§4.2)，PPL advantage 确认但 MMLU 下降\n- Qwen-2.5-14B: \"preliminary evaluation\" (§4.2)，PPL 改善但 reasoning decline (GSM8K -19.9pp)\n\n对于声称 *\"characterizing how the training objective shapes sparsity prediction quality across architectures\"* 的论文，需要更系统的跨架构评估。至少应在主实验表格中包含一个完整的第二模型结果。\n\n---\n\n## Questions\n\n**Q1.** KL predictor 发现的 mask patterns 是否与现有 semi-structured sparsity formats (如 2:4 N:M sparsity) 兼容？如果不兼容，实际部署需要什么样的 kernel 支持？\n\n**Q2.** Gumbel temperature τ 的 annealing schedule (1.0 → 0.1 over 1000 steps, Appendix C) 看起来相对 aggressive。作者是否尝试过更慢的退火方案？Figure 4 显示 final ~100 steps 有 mild loss increase，这是否表明退火过快？\n\n**Q3.** 论文提到 predictor 参数量是基模型的 <1%（75.9M vs. 8B）。但在 30% 稀疏度下，predictor 推理需要一次完整 dense forward pass 加上 predictor inference。这是否意味着首次 token 的延迟实际上会增加？\n\n**Q4.** Table 3 (target-swap ablation) 中 KL predictor trained on KL-derived targets 的 PPL (11.79) 和 BCE predictor trained on KL-derived targets 的 PPL (13.13) 之间的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？这似乎暗示 KL 的优势不仅来自发现更好的 masks，还来自训练动态本身。\n\n**Q5.** Abstract 中 \"n=3\" 标注的含义是 3 random seeds。但 3 seeds 对于报告 downstream task variance（尤其是 GSM8K 这种高方差任务）是否足够？Tables 中的 standard deviations 有时相当大。\n\n---\n\n## Missing References\n\n论文的引用覆盖面较广，涵盖了 TEAL, CATS, MaskLLM, SPON, FastForward, DejaVu, ShadowLLM, D2DMoE, ReLU Strikes Back 等主要工作。建议补充考虑：\n\n1. **ProSparse** (Song et al., 2024, EMNLP Findings) — 通过 progressive sparsification 在 SwiGLU 模型上激活稀疏性，与本文方法互补\n2. 若有 2025-2026 年发表的 contextual sparsity + KL distillation 相关工作，应检查是否遗漏\n\n---\n\n## Minor Issues\n\n- **M1.** Table 1 中存在多个 \"empty\" 单元格标注为未探索组合。虽然诚实，但读者可能会质疑 taxonomy 的完整性。建议简要讨论为什么这些组合未被尝试（技术上不可行？或仅是未来工作？）。\n\n- **M2.** Figures 2 和 3 在双栏格式下较小，部分文字标签在打印时可能难以辨认。Figure 3 的 y 轴 \"Wallclock Perplexity Gap\" 标签建议改为更直观的名称。\n\n- **M3.** 脚注使用较多（至少 4 个可见），部分信息（如 TEAL is deterministic, sparsity notation 等）可以整合到正文中，减少阅读碎片化。\n\n- **M4.** §3.5 Geometric Penalty Schedule 中引入了多个超参数（ε, λ, geometric doubling），但主文未提供 sensitivity analysis。虽然 Appendix C 有详细讨论，但主文中应至少提及 robustness。\n\n- **M5.** Conclusion 中 *\"the signal type gap (0.47 PPL)\"*（如果确实是此数值）与 §4.5 中报告的 9.47 PPL gap 不一致。请核实。如果是排版问题，应在camera-ready中修正。[注：此处数字可能是我从 PDF 渲染中误读，但建议作者确认。]\n\n- **M6.** 论文在 §Y 声明使用了 Claude (Anthropic) 进行代码起草和写作辅助。这符合 ARR 2026 政策，但建议确认是否需要在 Responsible NLP Checklist 中额外声明。\n\n---\n\n## 格式合规性检查\n\n- **页数限制**: 主文 8 页 (pp.1-8) ✓；Limitations 在 page 9，不计入页数 ✓；References 和 Appendix 在 page 9 之后 ✓\n- **匿名性**: 标题页显示 \"Anonymous ACL submission\" ✓；未发现明显的自引暴露\n- **Limitations 节**: 存在 ✓，覆盖 4 个要点（sparsity sweet spot, knowledge regression, evaluation scope, baseline coverage）✓\n- **Abstract 长度**: 约 190-200 words，接近 200-word 限制，需确认未超限\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，3-seed means + controlled ablations；但 \"primary dimension\" overclaimed 且 per-layer KL 分析存在未完全解决的 confounding |\n| **Excitement** | 2.5/5 | 核心 recipe 与 MaskLLM 重叠度高，contextual 扩展属 incremental innovation；梯度分析有价值但理论深度有限；知识任务退化限制了实际影响力 |\n| **Reproducibility** | 4/5 | 详细的超参数、训练设置、模型描述；代码承诺在接收后开源；Appendix 提供充分的实验细节 |\n| **Confidence** | 4/5 | 熟悉稀疏性/剪枝文献及本文使用的具体方法 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**一句话总结**: 扎实的实证研究，系统地证明了 KL 蒸馏在上下文稀疏性预测中优于 BCE，但方法新颖性受限于与 MaskLLM 的高度重叠，且知识任务的严重退化未得到充分解释。\n\n**详细判断依据**:\n\n本文的核心贡献是 empirical 的——通过系统实验证明 output-distribution alignment (KL) 优于 per-neuron classification (BCE) 作为 contextual sparsity predictor 的训练目标。实验设计严谨，消融全面，这些都是 Findings 级别工作的优势。\n\n然而，几个因素阻碍了 main conference 接收：\n1. **方法新颖性有限**: 核心技术栈（KL + Gumbel + frozen model）直接来自 MaskLLM，contextual 扩展虽有意义但属增量创新。\n2. **实际影响力受限**: 无 wall-clock 加速、知识任务严重退化、单模型主实验共同削弱了实际价值论证。\n3. **部分 claims overclaimed**: \"primary design dimension\" 在 confounding 未完全解决的情况下使用过于绝对化的表述。\n\n如果作者能补充 (a) 对知识任务退化的机制分析、(b) 至少一个模型的 wall-clock 结果、(c) 更准确的 contribution scope 限定，本文可能提升至 3.5 (Borderline Conference)。\n\n---\n\nSources (Step 0 搜索):\n- [ARR Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 审稿意见：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## Paper Summary\n\n本文提出使用输出分布蒸馏（forward KL divergence）替代传统 per-neuron BCE 来训练 SwiGLU LLM 的上下文稀疏性预测器。核心方法包括：冻结基模型 + 每层独立 2-layer MLP 预测器 + Gumbel-Sigmoid 松弛 + 几何惩罚调度实现目标稀疏度。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下相比 TEAL 降低 14.5% PPL。论文还提出了一个二维分类法（correction granularity × training signal coupling），分析 KL 相对 BCE 的梯度耦合机制，并通过大量消融实验研究了设计空间。\n\n---\n\n## Strengths\n\n**S1. 系统性的实验设计与消融分析**\n论文的实验设计非常扎实：3-seed means with standard deviations, target-swap ablation (Table 3), per-layer coupling breadth sweep (Figure 2), compensation冗余性分析 (Table 4), OOD评估 (Appendix D), 以及跨架构验证 (Mistral-7B, Qwen-2.5-14B)。每个 claim 都有对应的 controlled experiment 支撑。附录包含约 20 个补充实验（Appendix A–W），展示了极为彻底的验证工作。\n\n**S2. 有价值的梯度分析（§3.6）**\n§3.6 对比了 BCE 和 KL 的梯度结构：BCE 梯度仅依赖单个 neuron $j$，而 KL 通过下游 Jacobian $\\partial \\hat{p}_v / \\partial g^{(l)}_j$ 将每个 neuron 的 mask 决策与所有其他 neuron 的输出效应耦合。这一分析为\"为什么 KL 能发现更好的 mask\"提供了直觉上的解释，虽然不是严格的理论结果，但对读者理解方法差异很有帮助。\n\n**S3. 实用的二维分类法（Table 1）**\n将已有学习型稀疏方法沿 correction granularity（per-token vs. per-corpus）和 training signal coupling（decomposed/local/coupled）两个维度组织，清晰定位了本文方法的位置，并指出设计空间中未被探索的组合。这对社区有参考价值。\n\n**S4. 诚实的局限性讨论**\n论文坦诚报告了知识任务退化（MMLU -12.7pp, GSM8K 几乎崩塌）、50% 稀疏度下所有方法均失效、以及 wall-clock speedup 未测量等问题。这种透明度值得肯定。\n\n**S5. Target-swap ablation 设计精巧（Table 3）**\n通过让 BCE 预测器使用 KL 发现的 oracle mask 进行训练，巧妙地分离了\"mask 质量\"和\"训练目标\"的贡献。结果表明 KL 发现的 mask targets 可以迁移到 BCE，PPL 从 13.13 降至 11.79，证实了 mask 质量本身是关键因素。\n\n---\n\n## Weaknesses\n\n**W1. [Major] 与 MaskLLM 的新颖性区分不够充分**\n\n核心 recipe（frozen model + learnable mask + forward KL + Gumbel relaxation）与 MaskLLM (Fang et al., 2024) 高度重合。论文在 §2 中承认了这一点：*\"Unlike MaskLLM...which applies KL to static N:M weight masks, we address contextual activation sparsity.\"* 但\"contextual vs. static\"的区分未被充分论证为足够的独立贡献：\n\n- MaskLLM 的 KL + Gumbel 训练框架是否可以直接扩展到 contextual 设置，只需将 static mask parameters 替换为 input-dependent predictor？如果是，方法学贡献主要是 engineering 而非 research。\n- §3.6 的梯度分析是 contextual 设置特有的（因为 mask 是 hidden state 的函数），但该分析是基于 chain rule 的直接推导，理论深度有限。\n- 论文未讨论从 static 到 contextual 的扩展中遇到了哪些 non-trivial 的技术挑战。\n\n建议：明确列出 contextual setting 引入的 unique challenges（如泛化到 unseen inputs、cross-layer coordination 的动态性、predictor 容量与表达力的 trade-off），并讨论 MaskLLM 框架无法直接处理这些挑战的原因。\n\n**W2. [Major] 知识任务退化严重但分析不足**\n\nTable 2 显示 30% 稀疏度下：\n- MMLU: 40.7 (dense) → 28.0 (KL uniform)，降幅 31%\n- GSM8K: 19.9 → 0.2，几乎完全崩塌\n\n这是非常严重的实际问题。论文给出的解释主要有两个：\n1. 训练数据组成（§4.3, Appendix V）：C4-trained predictor achieves comparable MMLU (40.6%) but worse GSM8K (4.1% vs. 7.4%)——说明训练数据不是唯一原因。\n2. Task-dependent coupling effects（§4.5）：per-layer controls 显示 commonsense 和 knowledge 任务对 coupling 的敏感度不同。\n\n但论文未回答关键问题：**为什么 output-distribution alignment（KL）这个似乎更优的目标反而导致知识任务严重退化？** 如果 KL 发现了更好的 mask（PPL 更低），为什么这些 mask 不能保留知识能力？这暗示 KL 优化的 PPL 与下游 knowledge task 之间存在根本性的 misalignment，但论文未深入分析。\n\n**W3. [Major] \"Primary design dimension\" overclaimed**\n\n论文在 §4.5 和 abstract/contributions 中声称 training signal coupling 是 \"the primary design dimension\"。但证据只比较了 Table 1 taxonomy 中的两个维度（correction granularity × signal coupling）。其他潜在重要的设计维度未被系统比较：\n- Predictor capacity（bottleneck dimension d_b, 目前固定为 128）\n- Training data selection（仅在 Appendix V 中简短探索）\n- Training duration（Appendix B.2 显示 convergence，但未探索 over-training effects）\n- Sparsity allocation strategy（global top-k vs. per-layer budgets）\n\n\"Primary\" 这个断言隐含了对所有设计维度的 exhaustive comparison，但实际上只比较了两个。建议改为 \"a key design dimension\" 或限定 scope 为 \"among the two dimensions in our taxonomy\"。\n\n此外，§4.5 自身也承认了 confounding：per-layer KL 实验中 train-inference mismatch（K=1 masks 1/32 layers during training vs. all 32 at inference）、per-layer update count disparity 都可能混淆结论。在 confounding 未完全解决的情况下做出\"primary\"断言不够审慎。\n\n**W4. [Moderate] 无 wall-clock 推理加速结果**\n\n对于以推理效率为动机的论文，完全缺少 wall-clock 测量是显著缺陷。Appendix A 报告了 throughput overhead（KL-sparse pipeline 增加 6.4% 开销），但这是预测器本身的开销，不是最终的端到端加速。论文明确承认 *\"wall-clock speedup requires sparse kernel support not addressed here\"*（page 8），但这使得读者无法评估方法的实际影响力。\n\n与之对比，TEAL 等 training-free 方法虽然质量更差但可以直接在现有 sparse kernels 上运行。一个自然的问题是：KL 预测器发现的 mask patterns（非结构化 top-k）是否与现有 sparse compute primitives 兼容？\n\n**W5. [Moderate] Contribution labels \"Analytical\" 用法非标准**\n\nC3 和 C4 被标注为 \"Analytical\"，但其内容分别是 target-swap ablation 和 compensation redundancy 实验——这些是实验性发现，不是形式化分析/理论推导。在 ACL/EMNLP 社区，\"Analytical contribution\" 通常指数学推导、理论 bounds 或 formal analysis。建议改为 \"Empirical\" 或 \"Ablation-based\"，避免误导读者期待理论结果。\n\n**W6. [Moderate] 单模型主实验，跨架构泛化不足**\n\n所有主要实验（Tables 2-4, Figures 2-3）仅在 LLaMA-3.1-8B 上完成。跨架构验证仅有：\n- Mistral-7B-v0.3: 简短提及 (§4.2)，PPL advantage 确认但 MMLU 下降\n- Qwen-2.5-14B: \"preliminary evaluation\" (§4.2)，PPL 改善但 reasoning decline (GSM8K -19.9pp)\n\n对于声称 *\"characterizing how the training objective shapes sparsity prediction quality across architectures\"* 的论文，需要更系统的跨架构评估。至少应在主实验表格中包含一个完整的第二模型结果。\n\n---\n\n## Questions\n\n**Q1.** KL predictor 发现的 mask patterns 是否与现有 semi-structured sparsity formats (如 2:4 N:M sparsity) 兼容？如果不兼容，实际部署需要什么样的 kernel 支持？\n\n**Q2.** Gumbel temperature τ 的 annealing schedule (1.0 → 0.1 over 1000 steps, Appendix C) 看起来相对 aggressive。作者是否尝试过更慢的退火方案？Figure 4 显示 final ~100 steps 有 mild loss increase，这是否表明退火过快？\n\n**Q3.** 论文提到 predictor 参数量是基模型的 <1%（75.9M vs. 8B）。但在 30% 稀疏度下，predictor 推理需要一次完整 dense forward pass 加上 predictor inference。这是否意味着首次 token 的延迟实际上会增加？\n\n**Q4.** Table 3 (target-swap ablation) 中 KL predictor trained on KL-derived targets 的 PPL (11.79) 和 BCE predictor trained on KL-derived targets 的 PPL (13.13) 之间的差距如何解释？如果 mask targets 相同，为什么训练目标仍然重要？这似乎暗示 KL 的优势不仅来自发现更好的 masks，还来自训练动态本身。\n\n**Q5.** Abstract 中 \"n=3\" 标注的含义是 3 random seeds。但 3 seeds 对于报告 downstream task variance（尤其是 GSM8K 这种高方差任务）是否足够？Tables 中的 standard deviations 有时相当大。\n\n---\n\n## Missing References\n\n论文的引用覆盖面较广，涵盖了 TEAL, CATS, MaskLLM, SPON, FastForward, DejaVu, ShadowLLM, D2DMoE, ReLU Strikes Back 等主要工作。建议补充考虑：\n\n1. **ProSparse** (Song et al., 2024, EMNLP Findings) — 通过 progressive sparsification 在 SwiGLU 模型上激活稀疏性，与本文方法互补\n2. 若有 2025-2026 年发表的 contextual sparsity + KL distillation 相关工作，应检查是否遗漏\n\n---\n\n## Minor Issues\n\n- **M1.** Table 1 中存在多个 \"empty\" 单元格标注为未探索组合。虽然诚实，但读者可能会质疑 taxonomy 的完整性。建议简要讨论为什么这些组合未被尝试（技术上不可行？或仅是未来工作？）。\n\n- **M2.** Figures 2 和 3 在双栏格式下较小，部分文字标签在打印时可能难以辨认。Figure 3 的 y 轴 \"Wallclock Perplexity Gap\" 标签建议改为更直观的名称。\n\n- **M3.** 脚注使用较多（至少 4 个可见），部分信息（如 TEAL is deterministic, sparsity notation 等）可以整合到正文中，减少阅读碎片化。\n\n- **M4.** §3.5 Geometric Penalty Schedule 中引入了多个超参数（ε, λ, geometric doubling），但主文未提供 sensitivity analysis。虽然 Appendix C 有详细讨论，但主文中应至少提及 robustness。\n\n- **M5.** Conclusion 中 *\"the signal type gap (0.47 PPL)\"*（如果确实是此数值）与 §4.5 中报告的 9.47 PPL gap 不一致。请核实。如果是排版问题，应在camera-ready中修正。[注：此处数字可能是我从 PDF 渲染中误读，但建议作者确认。]\n\n- **M6.** 论文在 §Y 声明使用了 Claude (Anthropic) 进行代码起草和写作辅助。这符合 ARR 2026 政策，但建议确认是否需要在 Responsible NLP Checklist 中额外声明。\n\n---\n\n## 格式合规性检查\n\n- **页数限制**: 主文 8 页 (pp.1-8) ✓；Limitations 在 page 9，不计入页数 ✓；References 和 Appendix 在 page 9 之后 ✓\n- **匿名性**: 标题页显示 \"Anonymous ACL submission\" ✓；未发现明显的自引暴露\n- **Limitations 节**: 存在 ✓，覆盖 4 个要点（sparsity sweet spot, knowledge regression, evaluation scope, baseline coverage）✓\n- **Abstract 长度**: 约 190-200 words，接近 200-word 限制，需确认未超限\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，3-seed means + controlled ablations；但 \"primary dimension\" overclaimed 且 per-layer KL 分析存在未完全解决的 confounding |\n| **Excitement** | 2.5/5 | 核心 recipe 与 MaskLLM 重叠度高，contextual 扩展属 incremental innovation；梯度分析有价值但理论深度有限；知识任务退化限制了实际影响力 |\n| **Reproducibility** | 4/5 | 详细的超参数、训练设置、模型描述；代码承诺在接收后开源；Appendix 提供充分的实验细节 |\n| **Confidence** | 4/5 | 熟悉稀疏性/剪枝文献及本文使用的具体方法 |\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 — Findings**\n\n**一句话总结**: 扎实的实证研究，系统地证明了 KL 蒸馏在上下文稀疏性预测中优于 BCE，但方法新颖性受限于与 MaskLLM 的高度重叠，且知识任务的严重退化未得到充分解释。\n\n**详细判断依据**:\n\n本文的核心贡献是 empirical 的——通过系统实验证明 output-distribution alignment (KL) 优于 per-neuron classification (BCE) 作为 contextual sparsity predictor 的训练目标。实验设计严谨，消融全面，这些都是 Findings 级别工作的优势。\n\n然而，几个因素阻碍了 main conference 接收：\n1. **方法新颖性有限**: 核心技术栈（KL + Gumbel + frozen model）直接来自 MaskLLM，contextual 扩展虽有意义但属增量创新。\n2. **实际影响力受限**: 无 wall-clock 加速、知识任务严重退化、单模型主实验共同削弱了实际价值论证。\n3. **部分 claims overclaimed**: \"primary design dimension\" 在 confounding 未完全解决的情况下使用过于绝对化的表述。\n\n如果作者能补充 (a) 对知识任务退化的机制分析、(b) 至少一个模型的 wall-clock 结果、(c) 更准确的 contribution scope 限定，本文可能提升至 3.5 (Borderline Conference)。\n\n---\n\nSources (Step 0 搜索):\n- [ARR Review Form](https://aclrollingreview.org/reviewform)\n- [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2099 · 2026-05-24T04:31:51.664650+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3661
}
```

</details>

---


### Assistant

_source line 2100 · 2026-05-24T04:32:01.010214+00:00_

审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心评价：
- **Soundness 3.5/5** — 实验设计扎实（3-seed, controlled ablations），但 "primary design dimension" overclaimed 且存在未解决的 confounding
- **Excitement 2.5/5** — 核心 recipe 与 MaskLLM 高度重叠（KL + Gumbel + frozen model），contextual 扩展属增量创新
- **Overall 3.0/5** — 适合 Findings

**三个 Major Weaknesses**：
1. 与 MaskLLM 新颖性区分不足（共享 frozen model + KL + Gumbel recipe，contextual vs. static 的技术挑战未充分论证）
2. 知识任务严重退化（MMLU -31%, GSM8K 几乎崩塌）缺乏机制解释
3. "Primary design dimension" 在 confounding 未解决的前提下 overclaimed

**两个 Moderate Weaknesses**：无 wall-clock 加速结果、单模型主实验限制泛化性论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 51

## Round 51

26 recorded events


### User

_source line 2101 · 2026-05-24T04:33:19.475542+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 的 Must-Fix 问题:

**N1** [critical] §4.5 Per-Layer KL 分解的 claim 超出证据支撑
- Abstract/§4.5/Conclusion 反复强调 "signal type gap (9.47 PPL) exceeds coupling breadth range (2.08 PPL)"。但 train-inference mismatch 严重混淆（K=1 训练 1/32 层 mask vs 推理 32/32 层）。50% 下 K=1 (34.85) 优于 K=4 (44.23) 直接否定了分解在高 sparsity 下的有效性。这是第一条 contribution，但 Abstract/Conclusion 表述未降级。
- 建议：Abstract/Conclusion 加 "confounded by train-inference mismatch" 限定；将 9.47 vs 2.08 从 claim 降级为 observation；设计无 mismatch 控制实验。

**N2** [critical] 知识任务系统性退化未充分分析因果机制
- MMLU −5.2pp、14B GSM8K −19.9pp。归因于 "forward KL mode-covering" 但：
  (a) C4 control 单 seed；
  (b) "mode-covering sacrifices rare activations" 停留在直觉，无实证；
  (c) Constraint 实验显示 remove valley → MMLU +3.4pp，说明 allocation 是部分原因，与 "KL structural property" 解释有张力。
- 建议：C4 control 增至 3-seed；neuron-level 归因分析；区分 allocation-induced vs loss-inherent regression。

## Reviewer 1 的 Should-Fix 问题:

**W1** [warning] C1 Target-Swap Ablation 残余 confound
- Soft→hard binarization 丢失 ranking info；s42 oracle 来自 non-seed-matched checkpoint（gap 0.65pp vs s123/s456 ≤0.03pp）；BCE+Gumbel (32.22) 劣于 BCE (27.97) 暗示 Gumbel 对 BCE 有害但对 KL 有益。

**W2** [warning] MSE baseline 可能未在最优配置下评估
- MSE 50% 2/3 seeds 崩溃。"Same hyperparameters" 可能 unfairly disadvantage MSE。建议为 MSE 做 λ_max 小搜索。

**W3** [warning] n=3 seeds 对部分 claim 支撑不足
- MMLU 30% global σ=9.5pp, 95% CI ≈ [11.9, 59.5]；Qwen-14B GSM8K σ=5.3pp；Mistral ARC-c σ=6.4pp。

**W4** [warning] WikiText-2 eval / WikiText-103 training 同源性
- C4 OOD 30% 仅 2-seed；C4 uniform CV=6.3% vs in-domain 0.2%；C4 缺 TEAL baseline。

## Reviewer 1 的 Questions:

**Q1**: K=1 在 50% 优于 K=4 如何解释？K-curve 在 50% 下是否失效？
**Q2**: BCE+Gumbel (32.22) 劣于 BCE (27.97) 的根本原因？Gumbel 与 KL 有特定协同效应？
**Q3**: 知识退化是否可通过 task-aware allocation（remove-valley）在推理时修复？
**Q4**: STE 若补偿 undershoot（target 40% 以达实际 30%），PPL 是否仍劣于 Gumbel？

## Reviewer 1 的 Overall Assessment:
3.5 (Borderline Conference)。PPL 改进令人信服，但知识退化和 §4.5 confound 削弱贡献。

---

请逐条回应上述 Must-Fix、Should-Fix 问题和 Questions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2102 · 2026-05-24T04:35:45.748828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2103 · 2026-05-24T04:35:46.200763+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2104 · 2026-05-24T04:35:46.251445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2105 · 2026-05-24T04:35:46.753584+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2106 · 2026-05-24T04:35:46.753910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2107 · 2026-05-24T04:35:46.804361+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/review_reviewer_2_1001ef39.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2108 · 2026-05-24T04:35:54.533105+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "5,7,8,14,16,18,19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "5,7,8,14,16,18,19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2109 · 2026-05-24T04:35:55.741584+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.7}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.5}], \"total_pages\": 20, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool call

_source line 2110 · 2026-05-24T04:35:59.605368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2111 · 2026-05-24T04:36:00.560086+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2112 · 2026-05-24T04:36:00.560553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2113 · 2026-05-24T04:36:01.163213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2114 · 2026-05-24T04:36:01.263961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 2115 · 2026-05-24T04:36:01.615767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 2116 · 2026-05-24T04:36:02.520647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool result

_source line 2117 · 2026-05-24T04:36:02.521774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 2118 · 2026-05-24T04:36:02.522108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2119 · 2026-05-24T04:36:02.973824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2120 · 2026-05-24T04:36:03.477711+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 2121 · 2026-05-24T04:36:03.478137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_26/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2122 · 2026-05-24T04:36:03.931394+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 2123 · 2026-05-24T04:36:04.334782+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 2124 · 2026-05-24T04:39:49.484577+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n---\n\n**[AGREE] R1-N1: §4.5 Per-Layer KL 分解 claim 超出证据支撑**\n\n完全同意。这也是我在自己审稿中提出的核心问题之一（我的 W3）。R1 的分析比我更为精确，补充几个要点：\n\n1. **50% 异常是最强反证。** R1 指出 50% 下 K=1 (34.85) 优于 K=4 (44.23)，这直接否定了 \"coupling breadth 单调有益\" 的叙事。如果更多 coupling 在 30% 有利但在 50% 有害，那么 \"signal type is the primary dimension\" 的结论是 sparsity-conditional 的，不能一般化。论文在 §4.5 承认了 \"the 50% failure where TEAL K=1 (14.85) outperforms K=∞ (14.42)\"，但这一承认埋在行文中，未在 Abstract/Conclusion 中体现。\n\n2. **Confounding 比论文承认的更严重。** K=1 训练时每步仅更新 1/32 层的 predictor，而推理时所有 32 层同时激活。这不仅是 train-inference mismatch，还涉及 update frequency 差异（K=1 每个 predictor 仅看到 ~31 updates vs E2E 的 1000 updates）。Appendix S 的 K=4 控制实验部分缓解了这一问题，但 K=4 本身仍有 4/32 vs 32/32 的 mismatch。**要真正分离 signal type 和 coupling scope，需要一个无 mismatch 的实验：例如训练所有 32 层的 predictor 但 loss 仅回传到 K 层。**\n\n3. **数值疑似不一致。** 我在第一轮审稿中已标记（M5）：Conclusion 中 \"signal type gap (0.47 PPL)\" 与 §4.5 中的 \"K=1 KL 9.05 vs. MSE 18.52: 9.47 PPL\" 可能存在排版错误（0.47 vs 9.47）。如果确实是 0.47，则 \"exceeds coupling breadth range (2.08 PPL)\" 的断言在数学上不成立。\n\n**建议与 R1 一致**：Abstract/Conclusion 必须加 \"confounded by train-inference mismatch\" 限定；将结论降级为 observation；设计无 mismatch 的控制实验。\n\n---\n\n**[AGREE] R1-N2: 知识任务退化未充分分析因果机制**\n\n完全同意，并补充 R1 未提及的一个发现：\n\n1. **R1 的三个具体论点均成立。** (a) C4 control 单 seed 不足以支撑因果推断；(b) \"mode-covering sacrifices rare activations\" 仅为直觉猜测；(c) remove-valley → MMLU +3.4pp 说明 allocation pattern 是部分原因。\n\n2. **补充证据：Appendix S 的 K=4 MMLU 异常进一步支持 R1 的判断。** 论文在 Appendix S (Table 19) 中报告 K=4 的 MMLU 系统性超过 E2E (\"MMLU: K=4 systematically exceeds E2E across all 3 seeds\")。论文自身在 Appendix T 中将此归因于 K=4 产生近均匀的 per-layer sparsity (std=0.001)，从而 \"inherently removes the valley, producing MMLU≈43.5 comparable to the remove-valley condition (44.0)\"。**这直接说明知识任务退化的很大一部分原因是 allocation pattern（valley 结构），而非 KL loss 的固有属性。** 论文的两个解释（\"KL mode-covering\" vs \"allocation-induced\"）之间存在未解决的张力。\n\n3. **Seed variance 使分析更加困难。** 从 Table 20 (Appendix T) 可以看到 s42 baseline MMLU = 40.6，而 Table 2 的 3-seed mean 为 ~28.5。这意味着 s42 是一个高 MMLU 异常种子，其他种子的 MMLU 可能低至 ~22。在如此极端的 seed variance 下，任何基于单 seed (s42) 的因果分析都不可靠。\n\n**建议与 R1 一致**：C4 control 增至 3-seed；明确区分 allocation-induced vs loss-inherent regression；neuron-level 归因分析（哪些 neuron 在 KL vs BCE 下被保留/丢弃，这些 neuron 与知识存储的关系）。\n\n---\n\n### Should-Fix 问题\n\n---\n\n**[AGREE] R1-W1: Target-Swap Ablation 残余 confound（部分同意）**\n\n同意 R1 提出的三个 confound 中的两个，对第一个持保留意见：\n\n1. **Soft→hard binarization（部分保留）。** R1 认为 binarization 丢失 ranking info。但推理时 mask 最终都是 hard binary（top-k），所以 binarized oracle 是 inference-relevant 的评估标准。连续 importance scores 的 ranking info 仅在 training 中对梯度有影响，不影响最终 mask 质量评估。不过，如果连续 scores 中包含\"接近 threshold 的 neuron 有歧义\"的信息，那么 binarization 确实丢失了这部分信号。此 confound 存在但可能影响较小。\n\n2. **s42 oracle provenance（同意）。** s42 oracle 来自非 seed-matched checkpoint，gap 0.65pp vs seed-matched ≤0.03pp。论文在 Table 3 脚注中承认了这一问题，但未量化其对结论的影响。建议在 seed-matched 条件下重做 s42 实验。\n\n3. **BCE+Gumbel (32.22) 劣于 BCE (27.97)（同意，且认为重要）。** 这一观察暗示 Gumbel relaxation 与 KL 之间存在特定协同效应，而非 Gumbel 本身的普遍优势。在 BCE 的 decomposed 梯度结构下，Gumbel 引入的随机扰动只增加噪声（每个 neuron 的梯度独立，无法利用邻居的探索信号）；但在 KL 的 coupled 梯度结构下，Gumbel 的探索使得模型能发现组合上更优的 mask patterns。**这个 Gumbel-KL 协同效应本身值得在论文中讨论，因为它实际上是对 §3.6 梯度分析的一个有力补充证据。** 当前论文完全没有讨论这一现象。\n\n---\n\n**[AGREE] R1-W2: MSE baseline 可能未在最优配置下评估**\n\n同意。Appendix G 描述了 MSE baseline 使用与 KL 完全相同的超参数配置。但 MSE 的梯度 magnitude 比 KL 大约 5 倍（Appendix G/H），这意味着 MSE 可能需要更小的学习率。当 2/3 seeds 在 50% 下崩溃时（Appendix F 提及），这更像是超参数不匹配而非 MSE 方法本身的缺陷。\n\n不过，我认为这不影响核心结论的方向性：即使 MSE 在最优超参数下表现更好，KL 的 coupled gradient 结构（§3.6）仍然是理论上更优的选择。但 **PPL 差距的量化（18.52 vs 9.05）可能被高估**，建议为 MSE 至少做一个学习率 sweep。\n\n---\n\n**[AGREE] R1-W3: n=3 seeds 对部分 claim 支撑不足**\n\n完全同意。我在第一轮审稿 Q5 中也提出了相同 concern。R1 提供的具体数字更有说服力：\n\n- MMLU 30% global σ=9.5pp → 95% CI ≈ [11.9, 59.5]（使用 t-distribution, df=2）\n- 这意味着 MMLU 的 seed-level 变异远大于方法间差异\n\n**关键区分：PPL claims 稳健，downstream claims 不稳健。** PPL σ 通常在 0.02-0.15 范围，3 seeds 足以支撑 PPL 结论。但 MMLU/GSM8K 的 σ 高达 5-10pp，3 seeds 不足以对这些 metrics 做可靠推断。论文应当明确标注哪些 claims 是 PPL-based（统计可靠）、哪些是 downstream-based（需更多 seeds）。\n\n---\n\n**[AGREE] R1-W4: WikiText-2 eval / WikiText-103 training 同源性（部分同意）**\n\n同意这是一个 valid concern，但认为严重程度低于 R1 的评估：\n\n1. **同源性是社区标准做法。** TEAL、CATS、MaskLLM 等多数对比工作也使用 WikiText 系列做 train/eval。在公平比较的意义上，使用相同 evaluation 是合理的。\n\n2. **C4 OOD 评估存在但不充分。** Appendix D 报告了 C4 OOD 结果（PPL 16.03±0.01），确认了优势持续。但 R1 正确指出：(a) 仅 2-seed；(b) CV=6.3% 远高于 in-domain 0.2%；(c) **最关键的缺失是 C4 上缺少 TEAL baseline**，无法判断 KL 的 OOD 优势是否依然存在。\n\n---\n\n### Questions\n\n---\n\n**[AGREE] R1-Q1: K=1 在 50% 优于 K=4 如何解释？**\n\nR1 提出了正确的问题。这一异常是 §4.5 分析的最大威胁。结合 Appendix S/T 的信息，我的推测：\n\n在 50% 下，每层丢弃一半 neuron，cross-layer error propagation 被 KL 的 coupled gradients 放大（因为 Jacobian 乘以的 activation 有一半为零）。K=1 通过切断 cross-layer coupling 避免了这种 error cascading。但 30% 下丢弃比例较低，coupling 的信息增益超过 error propagation 的代价。\n\n**如果此推测成立，那么 coupling 的有益性是 sparsity-conditional 的，\"primary design dimension\" 的 claim 需要限定为 \"at moderate sparsity levels\"。**\n\n---\n\n**[AGREE] R1-Q2: BCE+Gumbel 劣于 BCE 的根因？**\n\n如上 W1 第 3 点所述，我认为这揭示了 Gumbel-KL 协同效应：\n- **BCE+Gumbel**：Gumbel 噪声扰动每个 neuron 的独立 sigmoid 决策，但 BCE 的 per-neuron 梯度无法利用这种组合探索——噪声只是噪声。\n- **KL+Gumbel**：Gumbel 噪声改变了 mask 的组合状态，KL 的 coupled gradients（通过 Jacobian）可以感知这些组合变化对输出分布的影响，从而利用噪声进行有意义的 mask space exploration。\n\n**这是一个 R1 发现的重要观察，值得在论文中作为 §3.6 梯度分析的实证佐证加以讨论。**\n\n---\n\n**[AGREE] R1-Q3: 知识退化是否可通过 task-aware allocation 修复？**\n\nAppendix T 的数据表明部分可以：remove-valley → MMLU +3.4pp, GSM8K +1.6pp。但相对 dense baseline 仍有显著差距。此外，Appendix S 显示 K=4 MMLU≈43.5 接近 dense (40.7)，甚至更高——这暗示在适当的 allocation 下知识退化可以被大幅缓解。\n\n但这引出了一个更深层的问题：**如果 allocation 调整就能修复知识退化，那退化的原因就不是 KL loss 的固有属性，而是 E2E KL training 学到的特定 allocation pattern（valley）的副作用。** 论文需要明确区分这两种因果路径。\n\n---\n\n**[AGREE] R1-Q4: STE 若补偿 undershoot，PPL 是否仍劣于 Gumbel？**\n\n同意这是一个必要的控制实验。§3.3 报告 Gumbel 比 STE 改善 33.8%（PPL 15.77→11.79 at 50%），但如果 STE 的实际 sparsity 与目标不匹配（undershoot），则部分 PPL 差距可能来自 sparsity level 差异而非 gradient quality。\n\n论文的 §3.3 理论论证（STE 的 discontinuous gradient signals 导致 oscillation）是合理的，但需要实证支撑：**在 matched actual sparsity 下比较 STE vs Gumbel。** 如果 STE 调整 target 后仍显著劣于 Gumbel，则 gradient quality 论证成立；如果差距大幅缩小，则当前论文高估了 Gumbel 的独立贡献。\n\n---\n\n## 综合判断\n\nR1 的审稿极为细致，大多数 concerns 与我的独立评估一致或互补。关键共识：\n\n1. **§4.5 per-layer KL 分析是论文最大的方法论弱点**——两位 reviewer 均认为 confounding 未解决且 claim overclaimed。\n2. **知识任务退化是第二大问题**——两位 reviewer 均认为因果分析不足，且 allocation vs loss-inherent 未分离。\n3. **n=3 seeds 对高方差 metrics 不足**——PPL claims 稳健但 downstream claims 需更多 seeds。\n\nR1 比我更准确地识别了 BCE+Gumbel anomaly 和 STE undershoot confound——这些在我的第一轮审稿中未涉及。\n\n**我维持 Overall 3.0 (Findings) 的评分。** R1 给出 3.5 (Borderline Conference) 较我乐观半档。区别可能在于：我认为与 MaskLLM 的 novelty overlap（我的 W1）进一步限制了方法贡献，而 R1 似乎未重点关注 novelty 问题。如果仅考虑 R1 评审的维度（claim strength + experimental soundness），3.5 也是合理的。\n",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n---\n\n**[AGREE] R1-N1: §4.5 Per-Layer KL 分解 claim 超出证据支撑**\n\n完全同意。这也是我在自己审稿中提出的核心问题之一（我的 W3）。R1 的分析比我更为精确，补充几个要点：\n\n1. **50% 异常是最强反证。** R1 指出 50% 下 K=1 (34.85) 优于 K=4 (44.23)，这直接否定了 \"coupling breadth 单调有益\" 的叙事。如果更多 coupling 在 30% 有利但在 50% 有害，那么 \"signal type is the primary dimension\" 的结论是 sparsity-conditional 的，不能一般化。论文在 §4.5 承认了 \"the 50% failure where TEAL K=1 (14.85) outperforms K=∞ (14.42)\"，但这一承认埋在行文中，未在 Abstract/Conclusion 中体现。\n\n2. **Confounding 比论文承认的更严重。** K=1 训练时每步仅更新 1/32 层的 predictor，而推理时所有 32 层同时激活。这不仅是 train-inference mismatch，还涉及 update frequency 差异（K=1 每个 predictor 仅看到 ~31 updates vs E2E 的 1000 updates）。Appendix S 的 K=4 控制实验部分缓解了这一问题，但 K=4 本身仍有 4/32 vs 32/32 的 mismatch。**要真正分离 signal type 和 coupling scope，需要一个无 mismatch 的实验：例如训练所有 32 层的 predictor 但 loss 仅回传到 K 层。**\n\n3. **数值疑似不一致。** 我在第一轮审稿中已标记（M5）：Conclusion 中 \"signal type gap (0.47 PPL)\" 与 §4.5 中的 \"K=1 KL 9.05 vs. MSE 18.52: 9.47 PPL\" 可能存在排版错误（0.47 vs 9.47）。如果确实是 0.47，则 \"exceeds coupling breadth range (2.08 PPL)\" 的断言在数学上不成立。\n\n**建议与 R1 一致**：Abstract/Conclusion 必须加 \"confounded by train-inference mismatch\" 限定；将结论降级为 observation；设计无 mismatch 的控制实验。\n\n---\n\n**[AGREE] R1-N2: 知识任务退化未充分分析因果机制**\n\n完全同意，并补充 R1 未提及的一个发现：\n\n1. **R1 的三个具体论点均成立。** (a) C4 control 单 seed 不足以支撑因果推断；(b) \"mode-covering sacrifices rare activations\" 仅为直觉猜测；(c) remove-valley → MMLU +3.4pp 说明 allocation pattern 是部分原因。\n\n2. **补充证据：Appendix S 的 K=4 MMLU 异常进一步支持 R1 的判断。** 论文在 Appendix S (Table 19) 中报告 K=4 的 MMLU 系统性超过 E2E (\"MMLU: K=4 systematically exceeds E2E across all 3 seeds\")。论文自身在 Appendix T 中将此归因于 K=4 产生近均匀的 per-layer sparsity (std=0.001)，从而 \"inherently removes the valley, producing MMLU≈43.5 comparable to the remove-valley condition (44.0)\"。**这直接说明知识任务退化的很大一部分原因是 allocation pattern（valley 结构），而非 KL loss 的固有属性。** 论文的两个解释（\"KL mode-covering\" vs \"allocation-induced\"）之间存在未解决的张力。\n\n3. **Seed variance 使分析更加困难。** 从 Table 20 (Appendix T) 可以看到 s42 baseline MMLU = 40.6，而 Table 2 的 3-seed mean 为 ~28.5。这意味着 s42 是一个高 MMLU 异常种子，其他种子的 MMLU 可能低至 ~22。在如此极端的 seed variance 下，任何基于单 seed (s42) 的因果分析都不可靠。\n\n**建议与 R1 一致**：C4 control 增至 3-seed；明确区分 allocation-induced vs loss-inherent regression；neuron-level 归因分析（哪些 neuron 在 KL vs BCE 下被保留/丢弃，这些 neuron 与知识存储的关系）。\n\n---\n\n### Should-Fix 问题\n\n---\n\n**[AGREE] R1-W1: Target-Swap Ablation 残余 confound（部分同意）**\n\n同意 R1 提出的三个 confound 中的两个，对第一个持保留意见：\n\n1. **Soft→hard binarization（部分保留）。** R1 认为 binarization 丢失 ranking info。但推理时 mask 最终都是 hard binary（top-k），所以 binarized oracle 是 inference-relevant 的评估标准。连续 importance scores 的 ranking info 仅在 training 中对梯度有影响，不影响最终 mask 质量评估。不过，如果连续 scores 中包含\"接近 threshold 的 neuron 有歧义\"的信息，那么 binarization 确实丢失了这部分信号。此 confound 存在但可能影响较小。\n\n2. **s42 oracle provenance（同意）。** s42 oracle 来自非 seed-matched checkpoint，gap 0.65pp vs seed-matched ≤0.03pp。论文在 Table 3 脚注中承认了这一问题，但未量化其对结论的影响。建议在 seed-matched 条件下重做 s42 实验。\n\n3. **BCE+Gumbel (32.22) 劣于 BCE (27.97)（同意，且认为重要）。** 这一观察暗示 Gumbel relaxation 与 KL 之间存在特定协同效应，而非 Gumbel 本身的普遍优势。在 BCE 的 decomposed 梯度结构下，Gumbel 引入的随机扰动只增加噪声（每个 neuron 的梯度独立，无法利用邻居的探索信号）；但在 KL 的 coupled 梯度结构下，Gumbel 的探索使得模型能发现组合上更优的 mask patterns。**这个 Gumbel-KL 协同效应本身值得在论文中讨论，因为它实际上是对 §3.6 梯度分析的一个有力补充证据。** 当前论文完全没有讨论这一现象。\n\n---\n\n**[AGREE] R1-W2: MSE baseline 可能未在最优配置下评估**\n\n同意。Appendix G 描述了 MSE baseline 使用与 KL 完全相同的超参数配置。但 MSE 的梯度 magnitude 比 KL 大约 5 倍（Appendix G/H），这意味着 MSE 可能需要更小的学习率。当 2/3 seeds 在 50% 下崩溃时（Appendix F 提及），这更像是超参数不匹配而非 MSE 方法本身的缺陷。\n\n不过，我认为这不影响核心结论的方向性：即使 MSE 在最优超参数下表现更好，KL 的 coupled gradient 结构（§3.6）仍然是理论上更优的选择。但 **PPL 差距的量化（18.52 vs 9.05）可能被高估**，建议为 MSE 至少做一个学习率 sweep。\n\n---\n\n**[AGREE] R1-W3: n=3 seeds 对部分 claim 支撑不足**\n\n完全同意。我在第一轮审稿 Q5 中也提出了相同 concern。R1 提供的具体数字更有说服力：\n\n- MMLU 30% global σ=9.5pp → 95% CI ≈ [11.9, 59.5]（使用 t-distribution, df=2）\n- 这意味着 MMLU 的 seed-level 变异远大于方法间差异\n\n**关键区分：PPL claims 稳健，downstream claims 不稳健。** PPL σ 通常在 0.02-0.15 范围，3 seeds 足以支撑 PPL 结论。但 MMLU/GSM8K 的 σ 高达 5-10pp，3 seeds 不足以对这些 metrics 做可靠推断。论文应当明确标注哪些 claims 是 PPL-based（统计可靠）、哪些是 downstream-based（需更多 seeds）。\n\n---\n\n**[AGREE] R1-W4: WikiText-2 eval / WikiText-103 training 同源性（部分同意）**\n\n同意这是一个 valid concern，但认为严重程度低于 R1 的评估：\n\n1. **同源性是社区标准做法。** TEAL、CATS、MaskLLM 等多数对比工作也使用 WikiText 系列做 train/eval。在公平比较的意义上，使用相同 evaluation 是合理的。\n\n2. **C4 OOD 评估存在但不充分。** Appendix D 报告了 C4 OOD 结果（PPL 16.03±0.01），确认了优势持续。但 R1 正确指出：(a) 仅 2-seed；(b) CV=6.3% 远高于 in-domain 0.2%；(c) **最关键的缺失是 C4 上缺少 TEAL baseline**，无法判断 KL 的 OOD 优势是否依然存在。\n\n---\n\n### Questions\n\n---\n\n**[AGREE] R1-Q1: K=1 在 50% 优于 K=4 如何解释？**\n\nR1 提出了正确的问题。这一异常是 §4.5 分析的最大威胁。结合 Appendix S/T 的信息，我的推测：\n\n在 50% 下，每层丢弃一半 neuron，cross-layer error propagation 被 KL 的 coupled gradients 放大（因为 Jacobian 乘以的 activation 有一半为零）。K=1 通过切断 cross-layer coupling 避免了这种 error cascading。但 30% 下丢弃比例较低，coupling 的信息增益超过 error propagation 的代价。\n\n**如果此推测成立，那么 coupling 的有益性是 sparsity-conditional 的，\"primary design dimension\" 的 claim 需要限定为 \"at moderate sparsity levels\"。**\n\n---\n\n**[AGREE] R1-Q2: BCE+Gumbel 劣于 BCE 的根因？**\n\n如上 W1 第 3 点所述，我认为这揭示了 Gumbel-KL 协同效应：\n- **BCE+Gumbel**：Gumbel 噪声扰动每个 neuron 的独立 sigmoid 决策，但 BCE 的 per-neuron 梯度无法利用这种组合探索——噪声只是噪声。\n- **KL+Gumbel**：Gumbel 噪声改变了 mask 的组合状态，KL 的 coupled gradients（通过 Jacobian）可以感知这些组合变化对输出分布的影响，从而利用噪声进行有意义的 mask space exploration。\n\n**这是一个 R1 发现的重要观察，值得在论文中作为 §3.6 梯度分析的实证佐证加以讨论。**\n\n---\n\n**[AGREE] R1-Q3: 知识退化是否可通过 task-aware allocation 修复？**\n\nAppendix T 的数据表明部分可以：remove-valley → MMLU +3.4pp, GSM8K +1.6pp。但相对 dense baseline 仍有显著差距。此外，Appendix S 显示 K=4 MMLU≈43.5 接近 dense (40.7)，甚至更高——这暗示在适当的 allocation 下知识退化可以被大幅缓解。\n\n但这引出了一个更深层的问题：**如果 allocation 调整就能修复知识退化，那退化的原因就不是 KL loss 的固有属性，而是 E2E KL training 学到的特定 allocation pattern（valley）的副作用。** 论文需要明确区分这两种因果路径。\n\n---\n\n**[AGREE] R1-Q4: STE 若补偿 undershoot，PPL 是否仍劣于 Gumbel？**\n\n同意这是一个必要的控制实验。§3.3 报告 Gumbel 比 STE 改善 33.8%（PPL 15.77→11.79 at 50%），但如果 STE 的实际 sparsity 与目标不匹配（undershoot），则部分 PPL 差距可能来自 sparsity level 差异而非 gradient quality。\n\n论文的 §3.3 理论论证（STE 的 discontinuous gradient signals 导致 oscillation）是合理的，但需要实证支撑：**在 matched actual sparsity 下比较 STE vs Gumbel。** 如果 STE 调整 target 后仍显著劣于 Gumbel，则 gradient quality 论证成立；如果差距大幅缩小，则当前论文高估了 Gumbel 的独立贡献。\n\n---\n\n## 综合判断\n\nR1 的审稿极为细致，大多数 concerns 与我的独立评估一致或互补。关键共识：\n\n1. **§4.5 per-layer KL 分析是论文最大的方法论弱点**——两位 reviewer 均认为 confounding 未解决且 claim overclaimed。\n2. **知识任务退化是第二大问题**——两位 reviewer 均认为因果分析不足，且 allocation vs loss-inherent 未分离。\n3. **n=3 seeds 对高方差 metrics 不足**——PPL claims 稳健但 downstream claims 需更多 seeds。\n\nR1 比我更准确地识别了 BCE+Gumbel anomaly 和 STE undershoot confound——这些在我的第一轮审稿中未涉及。\n\n**我维持 Overall 3.0 (Findings) 的评分。** R1 给出 3.5 (Borderline Conference) 较我乐观半档。区别可能在于：我认为与 MaskLLM 的 novelty overlap（我的 W1）进一步限制了方法贡献，而 R1 似乎未重点关注 novelty 问题。如果仅考虑 R1 评审的维度（claim strength + experimental soundness），3.5 也是合理的。\n",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2125 · 2026-05-24T04:39:53.250656+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 2126 · 2026-05-24T04:40:03.870343+00:00_

已提交对 Reviewer 1 的逐条回应。核心立场：

- **N1 (per-layer KL overclaimed)**: [AGREE]，50% 异常 (K=1 > K=4) 是最强反证，confounding 比论文承认的更严重
- **N2 (知识退化)**: [AGREE]，补充了 Appendix S 的 K=4 MMLU 异常和 s42 seed variance 证据，进一步说明 allocation 而非 KL 本身可能是主因
- **W1-W4**: 均 [AGREE]（W1 部分保留 soft→hard 问题），特别认同 BCE+Gumbel anomaly 是重要发现
- **Q1-Q4**: 均 [AGREE]，补充了 Gumbel-KL 协同效应的机制解释
- 维持 Overall 3.0 (Findings)，与 R1 的 3.5 差半档，主因是 novelty overlap 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 52

## Round 52

74 recorded events


### User

_source line 2127 · 2026-05-25T09:04:47.480254+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式** 审查。

## Venue 信息
- **目标**: EMNLP 2026 via ACL Rolling Review (ARR May 2026)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + 无限参考文献（Limitations 不计入页数）
- **模板**: ACL template (review mode)
- **匿名**: double-blind

## 论文路径
- LaTeX: `projects/distill_sparse_swiglu/paper/main.tex`
- PDF: `projects/distill_sparse_swiglu/artifacts/review_round_27/submitted.pdf`

## 你的审查侧重

### 1. 新颖性评估
- 核心贡献：KL + Gumbel-Sigmoid + learned predictor 的组合是否具有足够新颖性？各个组件均为已知技术（KL distillation, Gumbel-Sigmoid, learned sparsity prediction）。
- 与 MaskLLM 的区分：两者共享 frozen weights + learnable masks + KL 的核心 recipe。论文声称的区别（static N:M vs contextual per-token, Gumbel-Softmax vs Gumbel-Sigmoid）是否构成 substantial novelty？
- Table 1 taxonomy 的分类是否准确？是否有方法被错误分类或遗漏？
- 贡献列表的 4 条是否恰当？每条是否站得住？是否有 overclaiming？
- "primary design dimension" 声明是否与实验证据匹配（知识任务退步）？

### 2. Related Work 完整性
- 激活稀疏性领域的覆盖是否全面？是否遗漏 2025-2026 年的重要工作？
- 搜索以下关键词确认是否有遗漏：
  - contextual activation sparsity prediction 2025/2026
  - SwiGLU sparsity learned predictor
  - KL divergence activation pruning
  - Gumbel relaxation neural network pruning
- 引用的论文是否真实存在？（重点检查 arXiv preprint 引用）

### 3. 写作质量
- 叙事结构：Abstract → Intro → Method → Experiments → Conclusion 的逻辑链是否连贯？
- Abstract 是否不超过 200 words？
- Contribution 声明是否与实验证据匹配？
- 术语一致性：output-distribution KL / forward KL / KL divergence 等术语是否统一？
- 数值一致性：Abstract、正文、表格中的数值是否一致？14.5% improvement 的基准引用是否清晰？

### 4. 格式合规
- 页数是否在 8 页正文限制内？
- Limitations section 是否存在且内容恰当？
- 匿名性：是否有 de-anonymization 泄漏（作者信息、特定机构标识、非匿名 GitHub）？
- ACL template 使用是否正确？[review] 选项是否正确？
- Figure/Table 格式是否规范？caption 是否信息完整？
- 引用格式是否统一？
- Ethics 声明和 AI assistant disclosure 是否恰当？

请按 Summary → Strengths → Weaknesses → Questions → Missing References 格式输出审稿意见。Weaknesses 按 severity 分为 Must-Fix / Should-Fix / Minor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2128 · 2026-05-25T09:05:06.732178+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
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

_source line 2129 · 2026-05-25T09:05:06.732696+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2130 · 2026-05-25T09:05:11.502196+00:00_

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
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2131 · 2026-05-25T09:05:13.058170+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "1-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "1-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2132 · 2026-05-25T09:05:19.695070+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found information about ACL Rolling Review 2026. Here's what I found:

## Reviewer Guidelines

ARR has developed detailed guidelines and suggestions for each step of the reviewing process, including a list of common problems in both reviews and NLP papers to watch out for. The reviewer and AC guidelines include codes for (meta-)review issues (I1-I12) that can be reported by the authors.

## Reviewer Expectations and Incentives

All authors are expected to sign up to review; whether they will receive assignments depends on their qualifications and the submission pool. 

Starting from May 2025, ACL introduces an awards policy for reviewers & chairs where area chairs or senior area chairs may nominate great reviewers, and the nominees will receive more recog
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8192
}
```

</details>

---


### Tool result

_source line 2133 · 2026-05-25T09:05:21.354721+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 591.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 507.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p9.png\", \"width\": 1241, \"he
…[truncated 937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8296
}
```

</details>

---


### Tool call

_source line 2134 · 2026-05-25T09:05:26.866880+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/submitted.pdf",
  "project": "distill_sparse_swiglu",
  "pages": "13-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/submitted.pdf",
    "project": "distill_sparse_swiglu",
    "pages": "13-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2135 · 2026-05-25T09:05:29.183463+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 349.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 350.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 419.7}], \"total_pages\": 18, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2316
}
```

</details>

---


### Tool call

_source line 2136 · 2026-05-25T09:05:29.183969+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need: 1) All scoring dimensions (e.g., soundness, excitement, novelty, clarity, etc.) 2) The rating scale for each dimension (e.g., 1-5) 3) The overall assessment scale 4) Any specific guidelines about what constitutes each score level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales. I need: 1) All scoring dimensions (e.g., soundness, excitement, novelty, clarity, etc.) 2) The rating scale for each dimension (e.g., 1-5) 3) The overall assessment scale 4) Any specific guidelines about what constitutes each score level"
  }
}
```

</details>

---


### Tool call

_source line 2137 · 2026-05-25T09:05:30.138938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2138 · 2026-05-25T09:05:30.744540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2139 · 2026-05-25T09:05:31.096335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 2140 · 2026-05-25T09:05:31.703742+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1564
}
```

</details>

---


### Tool call

_source line 2141 · 2026-05-25T09:05:31.755165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2142 · 2026-05-25T09:05:35.000431+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4255
}
```

</details>

---


### Tool result

_source line 2143 · 2026-05-25T09:05:35.355424+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4259
}
```

</details>

---


### Tool result

_source line 2144 · 2026-05-25T09:05:35.660035+00:00_

# ARR Review Form Criteria Summary

Based on the provided guidelines, here's what the document specifies about scoring:

## Scoring Dimensions

The guidelines mention **three primary scores** as of February 2025:

1. **Soundness** - Technical validity and methodological rigor
2. **Excitement** - Personal interest and perceived impact value
3. **Overall Recommendation** - Explicit recommendation for paper outcome

## Rating Scales

The document does **not provide specific numerical scales** (like 1-5 or 1-10) for any dimension. Instead, it emphasizes:

- Soundness scores "must be justified by the text of the review"
- Excitement scores are "orthogonal to the assessment of soundness" and "more subjective"
- Overall assessment reflects "a composite score reflecting soundness, excitement, and also other factors like novelty and impact"

## Key Guidance on Scoring

The guidelines stress that "low soundness scores without sufficient justification" indicate the review itself is problematic. Papers recommended for acceptance must be "sufficiently sound and reproducible," though reviewers may find work sound yet personally unexciting.

## Missing Information

The actual numerical scales, specific rubrics for each level (e.g., what distinguishes "4" from "5"), and additional dimensions like novelty or clarity are **not detailed in these reviewer guidelines**. The document references a separate "[ARR review form](https://aclrollingreview.org/reviewform)" post for more specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6476
}
```

</details>

---


### Tool result

_source line 2145 · 2026-05-25T09:05:35.761833+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4006
}
```

</details>

---


### Tool call

_source line 2146 · 2026-05-25T09:05:44.343188+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and descriptions of each score level. I need the exact rating options for: Overall Assessment, Soundness, Excitement, Confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and descriptions of each score level. I need the exact rating options for: Overall Assessment, Soundness, Excitement, Confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 2147 · 2026-05-25T09:05:44.796244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2148 · 2026-05-25T09:05:45.350687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 2149 · 2026-05-25T09:05:46.412902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 2150 · 2026-05-25T09:05:46.864545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2151 · 2026-05-25T09:05:46.966213+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2169
}
```

</details>

---


### Tool result

_source line 2152 · 2026-05-25T09:05:48.278405+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2927
}
```

</details>

---


### Tool result

_source line 2153 · 2026-05-25T09:05:48.483052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2070
}
```

</details>

---


### Tool result

_source line 2154 · 2026-05-25T09:05:48.584650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1720
}
```

</details>

---


### Tool result

_source line 2155 · 2026-05-25T09:05:49.855035+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
- **5**: "Positive that my evaluation is correct. I read the paper very carefully..."
- **4**: Quite sure with unlikely but conceivable missed details
- **3**: Pretty sure but some unchecked details (math, experimental design)
- **2**: Willing to defend but fairly likely missed details or novelty concerns
- **1**: Outside expertise area or paper very difficult to understand

## Soundness
- **5**: Excellent thoroughness given paper type
- **4**: Strong with sufficient claim support
- **3.5, 3**: Acceptable with minor support needed
- **2.5, 2**: Poor with insufficient main claim support
- **1.5, 1**: Major issues; insufficient for publication

## Excitement
- **5**: Highly exciting; would recommend to others
- **4**: Exciting; would mention to peers
- **3**: Interesting; might attend presentation
- **2**: Potentially interesting despite lack of personal resonance
- **1**: Not exciting; lacks community relevance

## Overall Assessment
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings track acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## Additional Dimensions
Reproducibility, Datasets, Software, and Author Identity Recognition use 1-5 scales with context-specific descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5511
}
```

</details>

---


### Tool call

_source line 2156 · 2026-05-25T09:05:54.429264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 2157 · 2026-05-25T09:05:54.931597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2158 · 2026-05-25T09:05:55.838697+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool result

_source line 2159 · 2026-05-25T09:05:55.839426+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2160 · 2026-05-25T09:05:55.889879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2161 · 2026-05-25T09:05:56.341712+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2162 · 2026-05-25T09:05:56.827932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 938
}
```

</details>

---


### Tool call

_source line 2163 · 2026-05-25T09:05:56.828337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 2164 · 2026-05-25T09:05:57.641953+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1300
}
```

</details>

---


### Tool call

_source line 2165 · 2026-05-25T09:05:57.642472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2166 · 2026-05-25T09:05:58.890628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2062
}
```

</details>

---


### Tool result

_source line 2167 · 2026-05-25T09:05:59.343721+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1701
}
```

</details>

---


### Tool call

_source line 2168 · 2026-05-25T09:06:08.902654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 2169 · 2026-05-25T09:06:09.406825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2170 · 2026-05-25T09:06:10.264662+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 2171 · 2026-05-25T09:06:10.281245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 874
}
```

</details>

---


### Tool call

_source line 2172 · 2026-05-25T09:06:10.281746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2173 · 2026-05-25T09:06:10.538544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2174 · 2026-05-25T09:06:11.448280+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1166
}
```

</details>

---


### Tool result

_source line 2175 · 2026-05-25T09:06:11.549632+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1011
}
```

</details>

---


### Tool call

_source line 2176 · 2026-05-25T09:06:30.209066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "contextual activation sparsity prediction LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "contextual activation sparsity prediction LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 2177 · 2026-05-25T09:06:30.359960+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SwiGLU sparsity learned predictor 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SwiGLU sparsity learned predictor 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 2178 · 2026-05-25T09:06:30.811713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KL divergence activation pruning large language model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KL divergence activation pruning large language model 2025"
  }
}
```

</details>

---


### Tool call

_source line 2179 · 2026-05-25T09:06:31.214005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gumbel relaxation neural network pruning structured sparsity 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gumbel relaxation neural network pruning structured sparsity 2025"
  }
}
```

</details>

---


### Tool result

_source line 2180 · 2026-05-25T09:06:36.739231+00:00_

Web search results for query: "KL divergence activation pruning large language model 2025"

Links: [{"title":"Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.383/"},{"title":"$D^2Prune$: Sparsifying Large Language Models via Dual Taylor Expansion and Attention Distribution Awareness","url":"https://arxiv.org/pdf/2601.09176"},{"title":"Rethinking Kullback-Leibler Divergence in Knowledge ...","url":"https://aclanthology.org/2025.coling-main.383.pdf"},{"title":"Gradient Estimation of KL Divergence in Large Language Model Reinforcement Learning | Xiaobo's Blog","url":"https://xiaobo-yang.github.io/posts/kl_grad/"},{"title":"NIRVANA: Structured pruning reimagined for large language models compression","url":"https://arxiv.org/pdf/2509.14230"},{"title":"A Simple and Effective Pruning Approach for Large Language Models","url":"https://arxiv.org/pdf/2306.11695"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"SEAP: Training-free Sparse Expert Activation Pruning Unlock the   Brainpower of Large Language Models","url":"https://arxiv.org/pdf/2503.07605"}]

Based on the search results, here are the key findings related to KL divergence, activation pruning, and large language models in 2025:

## Knowledge Distillation and KL Divergence

Kullback-Leiber divergence has been widely used in Knowledge Distillation (KD) to compress Large Language Models (LLMs). A recent approach proposes an Adaptive Kullback-Leiber (AKL) divergence method, which adaptively allocates weights to combine FKL and RKL.

## Activation Pruning Methods

Several pruning approaches incorporate activation information and KL divergence:

- **D²Prune**: This method proposes an attention-aware dynamic update strategy that preserves the 
…[truncated 763 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5927
}
```

</details>

---


### Tool result

_source line 2181 · 2026-05-25T09:06:37.894905+00:00_

Web search results for query: "SwiGLU sparsity learned predictor 2025 2026"

Links: [{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"Masked Gated Linear Unit | OpenReview","url":"https://openreview.net/forum?id=5OnejG2SQH"},{"title":"dReLU Activation Function: Matching SwiGLU Performance with 90% Sparsity | HackerNoon","url":"https://hackernoon.com/drelu-activation-function-matching-swiglu-performance-with-90percent-sparsity"},{"title":"Track: Session 7: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3153"},{"title":"Dependency-Aware Semi-Structured Sparsity of GLU Variants in Large   Language Models","url":"https://arxiv.org/pdf/2405.01943"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware   Masking","url":"https://arxiv.org/pdf/2412.01380"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/pdf/2406.05955"}]

Based on the web search results, here's what I found about SwiGLU sparsity and learned predictors in 2025-2026:

## Key Research Findings

SwiGLU MLP used in most modern LLMs have little to no natural activation sparsity. This presents a significant challenge for deploying these models efficiently.

### The Predictor Problem

It turns out to be much harder to predict which activations should be pruned in SwiGLU LLMs than in ReLU LLMs. While SwiGLU activations can be pruned based on magnitude, the resulting sparsity patterns are difficult to predict, rendering previous approaches ineffective.

### Recent Solutions (2025-2026)

Several approaches have emerged to address this challenge:

1. **Dynamic Input Pruning (DIP)**: A predictor-free dynamic sparsification approach which preserves accuracy with minimal fine-tuning.

2. **SVD Contextual Sparsity Predictors*
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7534
}
```

</details>

---


### Tool result

_source line 2182 · 2026-05-25T09:06:38.097429+00:00_

Web search results for query: "Gumbel relaxation neural network pruning structured sparsity 2025"

Links: [{"title":"LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models","url":"https://arxiv.org/html/2605.17289"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf"},{"title":"Resource-Efficient Neural Networks for Embedded Systems","url":"https://jmlr.org/papers/volume25/18-566/18-566.pdf"},{"title":"Method of structured network pruning and sparsity speed-up","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11625607"},{"title":"Neural Network Pruning by Gradient Descent","url":"https://arxiv.org/pdf/2311.12526"},{"title":"Intermediate-grained kernel elements pruning with structured sparsity - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608024006324"},{"title":"A Generalization of Continuous Relaxation in Structured Pruning","url":"https://arxiv.org/pdf/2308.14605"}]

Based on the web search results, here's what I found about Gumbel relaxation neural network pruning and structured sparsity in 2025:

## Key Findings

**Gumbel-based Approaches:**
LEAP uses a per-weight Bernoulli-via-Gumbel-sigmoid relaxation to make end-to-end unstructured mask learning tractable. Gumbel softmax has been used as a novel approach for optimizing neural network structures, employing a reparameterization trick that enables direct gradient-based optimization of categorical distribution parameters.

**Structured Sparsity Methods:**
A continuous relaxation of binary gates using a modified binary Gumbel-softmax distribution can be used for structured sparsity. Additionally, efficient and stable convergence up to 93% sparsity and 95% FLOPs reduction without loss of inference accuracy has been demonstrated using continuous relaxation methods.

**Recent 2025 Work:**
PruneNet is a novel structured pruni
…[truncated 531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6883
}
```

</details>

---


### Tool result

_source line 2183 · 2026-05-25T09:06:39.853867+00:00_

Web search results for query: "contextual activation sparsity prediction LLM 2025 2026"

Links: [{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-99854-6_25"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern","url":"https://arxiv.org/pdf/2507.14179"},{"title":"Grasp: Group-Based Prediction of Activation Sparsity for Fast LLM Inference | Proceedings of the 62nd Annual ACM/IEEE Design Automation Conference","url":"https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899"},{"title":"[2406.16635] ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/abs/2406.16635"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2406.16635"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"}]

Based on the web search results, here are recent developments in contextual activation sparsity prediction for LLMs in 2025-2026:

## Key Research Areas

**SVD-Based Contextual Sparsity Predictors**: A March 2026 preprint titled "SVD Contextual Sparsity Predictors for Fast LLM Inference" presents an approach using low-rank SVD approximation with calibrated per-neuron thresholds to construct sparsity predictors for accelerating LLM inference.

**Clustering-Based Activation Pattern Compression**: A 2025 Euro-Par conference paper proposes "A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering". Rather than treating neurons individually, the method groups similar activation patterns into a small set of representative clusters, achieving up to 79.34% clus
…[truncated 851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9644
}
```

</details>

---


### Tool call

_source line 2184 · 2026-05-25T09:06:49.089480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LEAP learnable end-to-end adaptive pruning LLM Gumbel-sigmoid 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LEAP learnable end-to-end adaptive pruning LLM Gumbel-sigmoid 2025 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 2185 · 2026-05-25T09:06:49.089879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SVD contextual sparsity predictors fast LLM inference 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SVD contextual sparsity predictors fast LLM inference 2026 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 2186 · 2026-05-25T09:06:49.390855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MaskLLM learnable pruning mask large language model ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MaskLLM learnable pruning mask large language model ICLR 2025"
  }
}
```

</details>

---


### Tool call

_source line 2187 · 2026-05-25T09:06:49.591879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grasp group-based prediction activation sparsity DAC 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grasp group-based prediction activation sparsity DAC 2025"
  }
}
```

</details>

---


### Tool result

_source line 2188 · 2026-05-25T09:06:55.415221+00:00_

Web search results for query: "Grasp group-based prediction activation sparsity DAC 2025"

Links: [{"title":"Grasp: Group-Based Prediction of Activation Sparsity for Fast LLM Inference | Proceedings of the 62nd Annual ACM/IEEE Design Automation Conference","url":"https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899"},{"title":"Grasp: Group-based Prediction of Activation Sparsity for Fast LLM Inference | Article Information | J-GLOBAL","url":"http://jglobal.jst.go.jp/en/public/202502232322977340"},{"title":"Publication – High Performance AI System Lab","url":"https://aisys.sogang.ac.kr/?page_id=49"},{"title":"Publications - Hoeseok Yang","url":"https://hyang1999.github.io/publications/"},{"title":"dblp: Youngmin Yi","url":"https://dblp.org/pid/45/4951.html"},{"title":"Grasp: Group-based Prediction of Activation Sparsity for Fast LLM Inference | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11132899/"},{"title":"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering","url":"https://arxiv.org/html/2507.14179v1"}]

Based on the search results, here's what I found about this research:

## Grasp: Group-Based Prediction of Activation Sparsity for Fast LLM Inference

Grasp is a paper by Jiho Shin, Hoeseok Yang, and Youngmin Yi presented at the 2025 Design Automation Conference (DAC).

### Overview

The research addresses the optimization of LLM inference, focusing on reducing computational overhead in the MLP components, which account for a significant portion of LLM inference, by using ReLU-fied LLMs to maximize activation sparsity.

### Key Contribution

Grasp is a novel magnitude-based, training-free sparsity prediction technique that builds on the existing sign bit-based method for ReLU-fied LLMs. The method enhances prediction accuracy by grouping values considering the distribution within vectors and explicitly accounting for statistical outliers, which allows for more accurate estimation of
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5823
}
```

</details>

---


### Tool result

_source line 2189 · 2026-05-25T09:06:56.118091+00:00_

Web search results for query: "SVD contextual sparsity predictors fast LLM inference 2026 arxiv"

Links: [{"title":"[2603.14110] SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/abs/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://arxiv.org/pdf/2603.14110"},{"title":"SVD Contextual Sparsity Predictors for Fast LLM Inference","url":"https://www.researchgate.net/publication/402480685_SVD_Contextual_Sparsity_Predictors_for_Fast_LLM_Inference"},{"title":"SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/html/2506.16500v1"},{"title":"Accelerating LLM Fine-Tuning with Contextual Sparsity","url":"https://arxiv.org/pdf/2506.16500"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time","url":"https://arxiv.org/pdf/2310.17157"},{"title":"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity","url":"https://arxiv.org/pdf/2602.00397"},{"title":"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models","url":"https://arxiv.org/html/2406.16635v1"}]

I found the research paper you're looking for. Here are the key details:

## SVD Contextual Sparsity Predictors for Fast LLM Inference

The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices.

**Key Results:**
Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores

**Publication Details:**
- **ArXiv ID:
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7028
}
```

</details>

---


### Tool result

_source line 2190 · 2026-05-25T09:06:57.208339+00:00_

Web search results for query: "LEAP learnable end-to-end adaptive pruning LLM Gumbel-sigmoid 2025 arxiv"

Links: [{"title":"[2605.17289] LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models","url":"https://arxiv.org/abs/2605.17289"},{"title":"LEAP: Learnable End-to-End Adaptive Pruning of LLMs","url":"https://www.cs.toronto.edu/~mmozaffari/compression-trinity/leap/index.html"},{"title":"LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models","url":"https://arxiv.org/html/2605.17289"},{"title":"[2105.14636] LEAP: Learnable Pruning for Transformer-based Models","url":"https://ar5iv.labs.arxiv.org/html/2105.14636"},{"title":"LEAP: Learnable Pruning for Transformer-based Models","url":"https://arxiv.org/pdf/2105.14636"},{"title":"LEAP: Learnable Pruning for Transformer-based Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210514636Y/abstract"}]

I found the paper you're looking for! Here are the key details:

**LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models**

LEAP replaces an intractable parameterization with a per-weight Bernoulli-via-Gumbel-sigmoid relaxation that makes end-to-end unstructured mask learning tractable.

**Key Contributions:**

- State-of-the-art methods for unstructured LLM pruning are layer-wise surrogates derived from the Optimal Brain Surgeon principle, and they sacrifice end-to-end accuracy, especially under aggressive sparsity.

- LEAP replaces complex, heuristic, or fixed pruning rules with a single, learnable, per-weight mask parameter that is optimized directly to minimize the end-to-end model loss.

- Unlike MaskLLM and PATCH, which assign a small set of learnable logits to structured groups, LEAP assigns a dedicated scalar parameter to every weight and lets the model decide which individual weights survive.

**Performance Results:**

Across five LLM families from 0.5B to 8B parameters at 50% and 60% sparsity, LEAP improves six-task average zero-shot accuracy by +2.59 points 
…[truncated 194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8118
}
```

</details>

---


### Tool result

_source line 2191 · 2026-05-25T09:06:57.317760+00:00_

Web search results for query: "MaskLLM learnable pruning mask large language model ICLR 2025"

Links: [{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/pdf/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=Llu9nJal7b"},{"title":"[Literature Review] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://www.themoonlight.io/en/review/maskllm-learnable-semi-structured-sparsity-for-large-language-models"},{"title":"NeurIPS Poster MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://neurips.cc/virtual/2024/poster/95573"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/0e9a05f5ce62284c91e4a33498899124-Paper-Conference.pdf"},{"title":"[2409.17481] MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/abs/2409.17481"},{"title":"MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models","url":"https://arxiv.org/html/2409.17481v2"},{"title":"MaskLLM","url":"https://vainf.github.io/maskllm-project-page/"},{"title":"arXiv:2502.00258v2 [cs.LG] 23 Jun 2025","url":"https://arxiv.org/pdf/2502.00258"}]

Based on the search results, I found comprehensive information about MaskLLM:

## Overview

MaskLLM is a learnable pruning method that establishes Semi-structured (or "N:M") Sparsity in LLMs, aimed at reducing computational overhead during inference.

## Methodology

Instead of developing a new importance criterion, MaskLLM explicitly models N:M patterns as a learnable distribution through Gumbel Softmax sampling. The primary goal is to prune parameters in an LLM so that within any group of M consecutive parameters, only N parameters remain non-zero.

## Key Advantages

This approach facilitates end-to-end training on la
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7926
}
```

</details>

---


### Tool call

_source line 2192 · 2026-05-25T09:13:35.159231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"TEAL\" activation sparsity LLM inference top-k allocation Liu 2025 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"TEAL\" activation sparsity LLM inference top-k allocation Liu 2025 ICLR"
  }
}
```

</details>

---


### Tool call

_source line 2193 · 2026-05-25T09:13:35.565551+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseInfer training-free activation sparsity prediction LLM 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseInfer training-free activation sparsity prediction LLM 2024 arxiv"
  }
}
```

</details>

---


### Tool result

_source line 2194 · 2026-05-25T09:13:41.777648+00:00_

Web search results for query: ""TEAL" activation sparsity LLM inference top-k allocation Liu 2025 ICLR"

Links: [{"title":"Training-Free Activation Sparsity in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=dGVZwyq5tV"},{"title":"[2408.14690] Training-Free Activation Sparsity in Large Language Models","url":"https://arxiv.org/abs/2408.14690"},{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models","url":"https://arxiv.org/html/2508.02128v1"},{"title":"ActTail: Global Activation Sparsity in Large Language Models","url":"https://arxiv.org/pdf/2603.12272"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/pdf/2507.01299"},{"title":"[2507.01299] La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/abs/2507.01299"},{"title":"WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity","url":"https://arxiv.org/pdf/2602.14452"}]

Based on the search results, I found comprehensive information about TEAL:

## Overview

TEAL is a simple training-free method that applies magnitude-based activation sparsity to hidden states throughout the entire model.

## Performance

TEAL achieves 40-50% model-wide sparsity with minimal performance degradation across Llama-2, Llama-3, and Mistral families, with sizes varying from 7B to 70B. The method improves existing sparse kernels and demonstrates wall-clock decoding speed-ups of up to 1.53× and 1.8× at 40% and 50% model-wide sparsity.

## Key Advantages

Unlike some older approaches tailored towards ReLU-based sparsity or methods requiring e
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6618
}
```

</details>

---


### Tool result

_source line 2195 · 2026-05-25T09:13:42.380136+00:00_

Web search results for query: "SparseInfer training-free activation sparsity prediction LLM 2024 arxiv"

Links: [{"title":"[Literature Review] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.themoonlight.io/en/review/sparseinfer-training-free-prediction-of-activation-sparsity-for-fast-llm-inference"},{"title":"[2411.12692] SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/abs/2411.12692"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10992997/"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast   LLM Inference","url":"https://arxiv.org/pdf/2411.12692"},{"title":"(PDF) SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://www.researchgate.net/publication/385944711_SparseInfer_Training-free_Prediction_of_Activation_Sparsity_for_Fast_LLM_Inference"},{"title":"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference","url":"https://arxiv.org/html/2411.12692v1"},{"title":"Activation Sparsity","url":"https://www.aussieai.com/research/activation-sparsity"}]

Based on the search results, here's what I found about SparseInfer:

SparseInfer is a simple, lightweight, and training-free predictor for activation sparsity of ReLU-field LLMs, in which activation sparsity is predicted by comparing only the sign bits of inputs and weights.

**Key Details:**

- **Authors & Publication:** The method was proposed by Jiho Shin, Hoeseok Yang, and Youngmin Yi, and the paper was published on arxiv as arXiv paper 2411.12692 on November 19, 2024.

- **Motivation:** Recent research has proposed replacing SiLU with ReLU to induce significant activation sparsity and showed no downstream task accuracy degradation through fine-tuning. However, taki
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6814
}
```

</details>

---


### Tool call

_source line 2196 · 2026-05-25T09:15:27.370947+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 消融设计出色、分析视角有价值的实证研究，但核心方法是已知组件的组合（KL + Gumbel-Sigmoid + learned predictor），且 Contribution #2 的数值表述存在自相矛盾，Abstract 严重超长。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理，3-seed 评估，消融充分；但 Contribution #2 数值逻辑不自洽，知识任务系统性退化限制实用性 |\n| Excitement | 3/5 | Target-swap ablation 和梯度分析有分析价值，但方法本身是已知技术的工程组合，增量创新 |\n| Reproducibility | 4/5 | 匿名代码、详细超参数、收敛曲线 (Appendix B)、3-seed 评估 |\n| Confidence | 4/5 | 熟悉激活稀疏性和知识蒸馏领域，仔细阅读全文及全部 18 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 严重超过 200-word 限制\n- 具体位置：Page 1, Abstract\n- 问题：Abstract 约 320+ words（含 3 段完整段落、5 个 inline citations），显著超过 ACL/ARR 的 200-word 限制。Abstract 中包含了方法细节（downstream Jacobian 解释）、与 MaskLLM 的详细对比、以及完整的实验数字。\n- 为什么影响接收：格式硬约束违规，存在 desk reject 风险。\n- 建议修改方向：(1) 删除第二段中的 Jacobian 机制解释和 MaskLLM 对比——这些属于 Introduction 内容；(2) 删除 inline citations（abstract 不宜引用）；(3) 第三段保留核心数字（14.5% PPL reduction, 68% mask divergence）但压缩周边描述。目标：一段问题+方法，一段核心结果+limitation，共 ≤180 words。\n\n**N2** [critical] Contribution #2 数值表述自相矛盾\n- 具体位置：Page 2, contribution list item 2; Page 7, Section 4.5 (Per-Layer KL: Signal Type vs. Coupling Scope)\n- 问题：Page 2 声称 \"signal type gap (0.47 PPL) dominates the coupling breadth range (2.08 PPL at 30% sparsity)\"。但 0.47 < 2.08，\"dominates\" 语义要求前者大于后者。Section 4.5 正文中写 \"2.08 PPL between per-layer KL and MSE\"——这是 signal type 之间的差异，不是 coupling breadth range。这说明 Page 2 contribution 声明中将数值错误地归属给了错误的维度。\n- 为什么影响接收：这是四条核心贡献之一，数值逻辑不自洽直接削弱论文的核心论点可信度。\n- 建议修改方向：(1) 明确定义 \"signal type gap\" = 控制 coupling 不变时，切换 loss function 的 PPL 差异；\"coupling breadth range\" = 控制 signal type 不变时，改变 K 的 PPL 差异。(2) 根据 Figure 3 和 Table 4 重新核实数值。(3) 如果实际关系是 signal_type_improvement(9.47 PPL, KL vs MSE at K=1) >> coupling_improvement(0.24 PPL, K=1 vs K=32 within KL)，则清晰表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 MaskLLM 的新颖性区分不够 substantial\n- 具体位置：Section 1 (Introduction), Section 2 (Related Work)\n- 问题：MaskLLM (NeurIPS 2024) 已经使用 frozen weights + learnable masks + KL divergence + Gumbel relaxation 的核心 recipe。本文的区别是：(a) static N:M → contextual per-token masks，(b) Gumbel-Softmax → Gumbel-Sigmoid。(a) 是问题设定的不同（unstructured top-k vs semi-structured N:M），不完全是方法创新；(b) 是自然的技术适配（独立的 per-neuron binary decision 用 Sigmoid 而非 Softmax 是标准选择）。论文未充分论证这些区别为什么构成 substantial methodological novelty 而非 engineering adaptation。\n- 建议：在 Related Work 增加一段深度对比：(1) 说明 contextual per-token prediction 引入了哪些 MaskLLM 不面对的技术挑战（如 cross-layer coordination、inference-time budget allocation），(2) 实验对比或引用 MaskLLM 在相似规模模型上的性能作为参考。\n\n**W2** [warning] 知识任务系统性退化分析不足\n- 具体位置：Table 2 (Page 6), Section 4.2, Limitations (Page 8-9)\n- 问题：MMLU 在 LLaMA-3.1-8B 30% sparsity 下降 ~5.2pp（≤29%），GSM8K 下降 0.2，且在 Mistral-7B 和 Qwen-2.5-14B 上一致出现类似退化 (Appendix N: MMLU -5.2pp 14B)。这是一个系统性问题，限制了方法的实际部署价值。论文在 Limitations 中承认但仅提供推测性解释（\"KL protects high-probability outputs at the expense of rare but critical activations\"），缺乏实证支持。\n- 建议：(1) 分析 KL-trained predictor 在 MMLU/GSM8K 输入上的神经元保留 pattern vs BCE（是否系统性丢弃了知识存储相关的神经元？）；(2) 讨论可能的缓解方向（如 task-aware loss weighting、混合 KL+BCE 策略）。\n\n**W3** [warning] 遗漏直接相关的 2026 年并行工作\n- 具体位置：Section 2 (Related Work)\n- 问题：SVD Contextual Sparsity Predictors (Serbin et al., arXiv:2603.14110, March 2026) 提出了针对 ReGLU/SwiGLU FFN 的 training-free 上下文稀疏预测方法（使用 gate projection 的 SVD 分解 + calibrated per-neuron thresholds），在 90% sparsity 下实现 1.8× 解码加速。该文发表于本文提交截止日前两个月，解决几乎相同的问题（SwiGLU LLM 的 contextual sparsity prediction），应讨论。\n- 建议：在 Related Work 中引用并对比 training-free（SVD-based）vs learned predictor（本文）方案的 trade-off。\n\n**W4** [warning] 实验规模和训练数据限制\n- 具体位置：Section 4.1, Limitations\n- 问题：(1) 主要实验仅在 8B/14B 模型上进行，未讨论方法是否能 scale 到 70B+ 模型（predictor 参数量线性增长到多少？training cost 如何变化？）。(2) 训练数据仅使用 WikiText-103 的 1000 steps，领域覆盖极窄。虽然 Appendix D 提供了 C4 OOD 评估，但训练数据的领域偏差可能是知识任务退化的部分原因（而非纯粹的方法局限）。\n- 建议：(1) 在 Limitations 中明确讨论规模限制；(2) 考虑在 C4 或更多样化的语料上训练 predictor 的消融实验。\n\n**W5** [warning] Table 1 分类体系不完整\n- 具体位置：Page 5, Table 1\n- 问题：二维分类（correction granularity × training signal coupling）遗漏重要维度：(1) training-free vs learned（TEAL 是 training-free，DejaVu 需要训练，但表中未区分）；(2) N:M structured vs unstructured top-k（MaskLLM 应出现在表中但缺失）。此外，Empty cells 标注为 \"unexplored combinations\" 但部分可能并非真正 unexplored，而是不适用（如 static per-neuron + coupled KL 逻辑上不自洽）。\n- 建议：(1) 将 MaskLLM 纳入表中（即使其为 N:M scope）；(2) 区分 empty = unexplored vs empty = not applicable。\n\n---\n\n## 小问题（不影响接收）\n\n- Page 1, Abstract: \"fundamental mismatch\" 在前两句中出现两次，措辞冗余。\n- Abstract 中包含 5 个 inline citations (Fang et al., Grattafiori et al., Jang et al., Jiang et al., Team)，ACL 论文 abstract 一般避免引用。\n- 术语一致性：论文交替使用 \"output-distribution KL\" (Abstract/Intro)、\"forward KL\" (Section 3.4, Table 4)、\"KL divergence\" (Section 3.6)。虽然上下文可辨，建议在首次定义后统一简称。\n- Figure 2 (Page 6) 热力图颜色梯度较浅，黑白打印后可读性存疑。\n- Page 18, Appendix Y (AI Assistants): 声明 Claude 用于 \"drafting and revising paper sections\" 和 \"summarizing related papers to inform related-work section\"。披露坦诚，但建议补充说明作者对所有 AI 生成内容的验证流程。\n\n---\n\n## 主要优势\n\n1. **Target-swap ablation (Table 3)** 是论文最强的分析贡献：通过交换 BCE/KL 训练出的 mask targets，干净地分离了 mask quality vs training objective coupling 的效果。BCE 在 KL-derived masks 上恢复至 ≤0.65pp gap 的发现是非平凡的。\n2. **梯度分析 (§3.6)** 从理论角度解释了 BCE vs KL 的行为差异（per-neuron independent vs downstream Jacobian coupling），提供了超越纯经验比较的 insight。\n3. **实验方法论严谨**：3-seed 评估、cross-architecture validation (LLaMA/Mistral/Qwen)、多维度消融（relaxation type、divergence measure、coupling scope、compensation）、OOD 评估 (C4)。\n4. **Limitations 诚实全面**：不回避 MMLU/GSM8K 退化问题，承认评估范围限制（MT-Bench 未测、训练语料重叠）。\n5. **复现性高**：匿名代码仓库、完整超参数列表、收敛曲线 (Appendix B)、训练 schedule 细节 (Appendix C)。\n\n---\n\n## Questions to Authors\n\n1. **Contribution #2 数值澄清**：请给出 \"signal type gap\" 和 \"coupling breadth range\" 的精确定义及对应数值来源（Table/Figure 编号和具体行），解释为什么 0.47 \"dominates\" 2.08。\n2. **知识退化根因**：如果在更多样化的训练语料（如 C4 或 RedPajama 子集）上训练 predictor，知识任务退化是否会缓解？这能帮助区分是\"方法固有缺陷\"还是\"训练数据偏差\"。\n3. **推理延迟**：Appendix A 报告了 overhead，但未给出 per-token latency breakdown。Predictor 的 32 个独立 MLP (2.37M 参数/层) 在实际 decode 中增加的延迟是否 offset 了稀疏计算的加速？\n4. **MaskLLM baseline 缺失**：为什么没有将 MaskLLM 作为 baseline？即使目标 sparsity pattern 不同（N:M vs top-k），在同等模型和 sparsity budget 下的 PPL/downstream 对比会显著增强新颖性论证。\n\n---\n\n## Missing References\n\n1. **SVD Contextual Sparsity Predictors** (Serbin et al., arXiv:2603.14110, March 2026) — 直接解决 SwiGLU FFN 的上下文稀疏预测，training-free 方案。发表于提交截止日前两个月，高度相关。\n2. **Rethinking Kullback-Leibler Divergence in Knowledge Distillation for LLMs** (ACL Anthology, COLING 2025) — 讨论 forward/reverse KL 在 LLM 知识蒸馏中的选择，与 Section 3.4 的 KL 方向选择讨论直接相关。\n3. **LEAP: Learnable End-to-End Adaptive Pruning** (arXiv:2605.17289, May 2026) — 使用 per-weight Gumbel-Sigmoid relaxation 做 LLM pruning。方法层面高度相关，但为同月并行工作，可在 camera-ready 中加入。\n4. **Grasp** (Shin et al., DAC 2025) — group-based 激活稀疏预测，虽针对 ReLU-fied models 但属于同一问题空间。",
  "reviewer_id": "2",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 消融设计出色、分析视角有价值的实证研究，但核心方法是已知组件的组合（KL + Gumbel-Sigmoid + learned predictor），且 Contribution #2 的数值表述存在自相矛盾，Abstract 严重超长。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计合理，3-seed 评估，消融充分；但 Contribution #2 数值逻辑不自洽，知识任务系统性退化限制实用性 |\n| Excitement | 3/5 | Target-swap ablation 和梯度分析有分析价值，但方法本身是已知技术的工程组合，增量创新 |\n| Reproducibility | 4/5 | 匿名代码、详细超参数、收敛曲线 (Appendix B)、3-seed 评估 |\n| Confidence | 4/5 | 熟悉激活稀疏性和知识蒸馏领域，仔细阅读全文及全部 18 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 严重超过 200-word 限制\n- 具体位置：Page 1, Abstract\n- 问题：Abstract 约 320+ words（含 3 段完整段落、5 个 inline citations），显著超过 ACL/ARR 的 200-word 限制。Abstract 中包含了方法细节（downstream Jacobian 解释）、与 MaskLLM 的详细对比、以及完整的实验数字。\n- 为什么影响接收：格式硬约束违规，存在 desk reject 风险。\n- 建议修改方向：(1) 删除第二段中的 Jacobian 机制解释和 MaskLLM 对比——这些属于 Introduction 内容；(2) 删除 inline citations（abstract 不宜引用）；(3) 第三段保留核心数字（14.5% PPL reduction, 68% mask divergence）但压缩周边描述。目标：一段问题+方法，一段核心结果+limitation，共 ≤180 words。\n\n**N2** [critical] Contribution #2 数值表述自相矛盾\n- 具体位置：Page 2, contribution list item 2; Page 7, Section 4.5 (Per-Layer KL: Signal Type vs. Coupling Scope)\n- 问题：Page 2 声称 \"signal type gap (0.47 PPL) dominates the coupling breadth range (2.08 PPL at 30% sparsity)\"。但 0.47 < 2.08，\"dominates\" 语义要求前者大于后者。Section 4.5 正文中写 \"2.08 PPL between per-layer KL and MSE\"——这是 signal type 之间的差异，不是 coupling breadth range。这说明 Page 2 contribution 声明中将数值错误地归属给了错误的维度。\n- 为什么影响接收：这是四条核心贡献之一，数值逻辑不自洽直接削弱论文的核心论点可信度。\n- 建议修改方向：(1) 明确定义 \"signal type gap\" = 控制 coupling 不变时，切换 loss function 的 PPL 差异；\"coupling breadth range\" = 控制 signal type 不变时，改变 K 的 PPL 差异。(2) 根据 Figure 3 和 Table 4 重新核实数值。(3) 如果实际关系是 signal_type_improvement(9.47 PPL, KL vs MSE at K=1) >> coupling_improvement(0.24 PPL, K=1 vs K=32 within KL)，则清晰表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 与 MaskLLM 的新颖性区分不够 substantial\n- 具体位置：Section 1 (Introduction), Section 2 (Related Work)\n- 问题：MaskLLM (NeurIPS 2024) 已经使用 frozen weights + learnable masks + KL divergence + Gumbel relaxation 的核心 recipe。本文的区别是：(a) static N:M → contextual per-token masks，(b) Gumbel-Softmax → Gumbel-Sigmoid。(a) 是问题设定的不同（unstructured top-k vs semi-structured N:M），不完全是方法创新；(b) 是自然的技术适配（独立的 per-neuron binary decision 用 Sigmoid 而非 Softmax 是标准选择）。论文未充分论证这些区别为什么构成 substantial methodological novelty 而非 engineering adaptation。\n- 建议：在 Related Work 增加一段深度对比：(1) 说明 contextual per-token prediction 引入了哪些 MaskLLM 不面对的技术挑战（如 cross-layer coordination、inference-time budget allocation），(2) 实验对比或引用 MaskLLM 在相似规模模型上的性能作为参考。\n\n**W2** [warning] 知识任务系统性退化分析不足\n- 具体位置：Table 2 (Page 6), Section 4.2, Limitations (Page 8-9)\n- 问题：MMLU 在 LLaMA-3.1-8B 30% sparsity 下降 ~5.2pp（≤29%），GSM8K 下降 0.2，且在 Mistral-7B 和 Qwen-2.5-14B 上一致出现类似退化 (Appendix N: MMLU -5.2pp 14B)。这是一个系统性问题，限制了方法的实际部署价值。论文在 Limitations 中承认但仅提供推测性解释（\"KL protects high-probability outputs at the expense of rare but critical activations\"），缺乏实证支持。\n- 建议：(1) 分析 KL-trained predictor 在 MMLU/GSM8K 输入上的神经元保留 pattern vs BCE（是否系统性丢弃了知识存储相关的神经元？）；(2) 讨论可能的缓解方向（如 task-aware loss weighting、混合 KL+BCE 策略）。\n\n**W3** [warning] 遗漏直接相关的 2026 年并行工作\n- 具体位置：Section 2 (Related Work)\n- 问题：SVD Contextual Sparsity Predictors (Serbin et al., arXiv:2603.14110, March 2026) 提出了针对 ReGLU/SwiGLU FFN 的 training-free 上下文稀疏预测方法（使用 gate projection 的 SVD 分解 + calibrated per-neuron thresholds），在 90% sparsity 下实现 1.8× 解码加速。该文发表于本文提交截止日前两个月，解决几乎相同的问题（SwiGLU LLM 的 contextual sparsity prediction），应讨论。\n- 建议：在 Related Work 中引用并对比 training-free（SVD-based）vs learned predictor（本文）方案的 trade-off。\n\n**W4** [warning] 实验规模和训练数据限制\n- 具体位置：Section 4.1, Limitations\n- 问题：(1) 主要实验仅在 8B/14B 模型上进行，未讨论方法是否能 scale 到 70B+ 模型（predictor 参数量线性增长到多少？training cost 如何变化？）。(2) 训练数据仅使用 WikiText-103 的 1000 steps，领域覆盖极窄。虽然 Appendix D 提供了 C4 OOD 评估，但训练数据的领域偏差可能是知识任务退化的部分原因（而非纯粹的方法局限）。\n- 建议：(1) 在 Limitations 中明确讨论规模限制；(2) 考虑在 C4 或更多样化的语料上训练 predictor 的消融实验。\n\n**W5** [warning] Table 1 分类体系不完整\n- 具体位置：Page 5, Table 1\n- 问题：二维分类（correction granularity × training signal coupling）遗漏重要维度：(1) training-free vs learned（TEAL 是 training-free，DejaVu 需要训练，但表中未区分）；(2) N:M structured vs unstructured top-k（MaskLLM 应出现在表中但缺失）。此外，Empty cells 标注为 \"unexplored combinations\" 但部分可能并非真正 unexplored，而是不适用（如 static per-neuron + coupled KL 逻辑上不自洽）。\n- 建议：(1) 将 MaskLLM 纳入表中（即使其为 N:M scope）；(2) 区分 empty = unexplored vs empty = not applicable。\n\n---\n\n## 小问题（不影响接收）\n\n- Page 1, Abstract: \"fundamental mismatch\" 在前两句中出现两次，措辞冗余。\n- Abstract 中包含 5 个 inline citations (Fang et al., Grattafiori et al., Jang et al., Jiang et al., Team)，ACL 论文 abstract 一般避免引用。\n- 术语一致性：论文交替使用 \"output-distribution KL\" (Abstract/Intro)、\"forward KL\" (Section 3.4, Table 4)、\"KL divergence\" (Section 3.6)。虽然上下文可辨，建议在首次定义后统一简称。\n- Figure 2 (Page 6) 热力图颜色梯度较浅，黑白打印后可读性存疑。\n- Page 18, Appendix Y (AI Assistants): 声明 Claude 用于 \"drafting and revising paper sections\" 和 \"summarizing related papers to inform related-work section\"。披露坦诚，但建议补充说明作者对所有 AI 生成内容的验证流程。\n\n---\n\n## 主要优势\n\n1. **Target-swap ablation (Table 3)** 是论文最强的分析贡献：通过交换 BCE/KL 训练出的 mask targets，干净地分离了 mask quality vs training objective coupling 的效果。BCE 在 KL-derived masks 上恢复至 ≤0.65pp gap 的发现是非平凡的。\n2. **梯度分析 (§3.6)** 从理论角度解释了 BCE vs KL 的行为差异（per-neuron independent vs downstream Jacobian coupling），提供了超越纯经验比较的 insight。\n3. **实验方法论严谨**：3-seed 评估、cross-architecture validation (LLaMA/Mistral/Qwen)、多维度消融（relaxation type、divergence measure、coupling scope、compensation）、OOD 评估 (C4)。\n4. **Limitations 诚实全面**：不回避 MMLU/GSM8K 退化问题，承认评估范围限制（MT-Bench 未测、训练语料重叠）。\n5. **复现性高**：匿名代码仓库、完整超参数列表、收敛曲线 (Appendix B)、训练 schedule 细节 (Appendix C)。\n\n---\n\n## Questions to Authors\n\n1. **Contribution #2 数值澄清**：请给出 \"signal type gap\" 和 \"coupling breadth range\" 的精确定义及对应数值来源（Table/Figure 编号和具体行），解释为什么 0.47 \"dominates\" 2.08。\n2. **知识退化根因**：如果在更多样化的训练语料（如 C4 或 RedPajama 子集）上训练 predictor，知识任务退化是否会缓解？这能帮助区分是\"方法固有缺陷\"还是\"训练数据偏差\"。\n3. **推理延迟**：Appendix A 报告了 overhead，但未给出 per-token latency breakdown。Predictor 的 32 个独立 MLP (2.37M 参数/层) 在实际 decode 中增加的延迟是否 offset 了稀疏计算的加速？\n4. **MaskLLM baseline 缺失**：为什么没有将 MaskLLM 作为 baseline？即使目标 sparsity pattern 不同（N:M vs top-k），在同等模型和 sparsity budget 下的 PPL/downstream 对比会显著增强新颖性论证。\n\n---\n\n## Missing References\n\n1. **SVD Contextual Sparsity Predictors** (Serbin et al., arXiv:2603.14110, March 2026) — 直接解决 SwiGLU FFN 的上下文稀疏预测，training-free 方案。发表于提交截止日前两个月，高度相关。\n2. **Rethinking Kullback-Leibler Divergence in Knowledge Distillation for LLMs** (ACL Anthology, COLING 2025) — 讨论 forward/reverse KL 在 LLM 知识蒸馏中的选择，与 Section 3.4 的 KL 方向选择讨论直接相关。\n3. **LEAP: Learnable End-to-End Adaptive Pruning** (arXiv:2605.17289, May 2026) — 使用 per-weight Gumbel-Sigmoid relaxation 做 LLM pruning。方法层面高度相关，但为同月并行工作，可在 camera-ready 中加入。\n4. **Grasp** (Shin et al., DAC 2025) — group-based 激活稀疏预测，虽针对 ReLU-fied models 但属于同一问题空间。",
    "reviewer_id": "2",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 2197 · 2026-05-25T09:15:31.451687+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4080
}
```

</details>

---


### Tool call

_source line 2198 · 2026-05-25T09:15:39.093202+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 2199 · 2026-05-25T09:15:39.093669+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/review_round_27/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2200 · 2026-05-25T09:15:45.854389+00:00_

Round 1 审稿完成。

**Overall: 3.5 (Borderline Conference)**

核心发现：
- **2 个 Must-Fix**：Abstract 超 200 词限制（~320 词，desk reject 风险）；Contribution #2 数值自相矛盾（"0.47 dominates 2.08"）
- **5 个 Should-Fix**：与 MaskLLM 的新颖性区分不足、知识任务退化分析缺失、遗漏 SVD Contextual Sparsity Predictors (March 2026)、实验规模有限、Table 1 分类不完整
- **主要优势**：target-swap ablation 设计精巧、梯度分析有理论深度、实验方法论严谨（3-seed、cross-architecture、OOD）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2"
}
```

</details>

---


## Round 53

## Round 53

4 recorded events


### User

_source line 2201 · 2026-05-25T09:16:47.117719+00:00_

[Round 1 审稿请求]:
## Step 2：交叉分享 — 请对 Reviewer 1 的审稿意见逐条回应

以下是 Reviewer 1（侧重方法严谨性）的 Round 1 审稿要点。请逐条用 **[AGREE]** 或 **[REBUT]** 回应，并附简要理由。重点关注你们是否存在分歧。

---

**Reviewer 1 — Overall: 3.0 (Findings)**

### Must-Fix（3 个）

**M1** [critical] STE sparsity 不匹配使 25.2% claim 不可靠
- STE（Straight-Through Estimator）baseline 的实际稀疏度与其他方法不匹配，导致论文声称的 25.2% PPL 改善数字不可靠。如果 STE 在不同稀疏度下运行，则与 KL/BCE 的比较不公平。

**M2** [critical] MSE baseline 未调参影响核心 contribution #2
- MSE baseline 使用了未经调参的配置，这使得基于 MSE vs KL 的核心贡献（signal type 的重要性）的论证基础不牢固。如果 MSE 在经过同等调参后表现更好，结论可能需要修正。

**M3** [critical] 缺乏实际推理加速数据与动机矛盾
- 论文动机强调推理效率，但全文缺乏实际推理延迟/加速比的测量数据。仅有 PPL/downstream accuracy 的改善，没有端到端加速验证，与稀疏性研究的核心价值主张矛盾。

### Should-Fix（6 个）

**S1** [warning] 统计可靠性
- 虽然有 3-seed 评估，但部分关键实验缺少置信区间或显著性检验，影响结论稳健性。

**S2** [warning] C1 binarization confound
- Target-swap ablation (C1) 中，binarization 步骤本身可能引入 confound，影响对 mask quality vs training objective 的干净分离。

**S3** [warning] 数据同源性
- 训练数据和评估数据可能存在同源性问题（WikiText-103 训练，WikiText-2 评估），影响 PPL 结果的可靠性。

**S4** [warning] Decomposition confound
- Section 4.5 的 signal type vs coupling scope 分解存在混杂因素，两个维度可能不完全正交。

**S5** [warning] Cross-architecture 评估不足
- 虽然测了 LLaMA/Mistral/Qwen，但消融实验仅在 LLaMA 上完成，cross-architecture 一致性验证不充分。

**S6** [warning] BCE isocompute 缺失
- BCE 和 KL 的训练计算量不对等，缺乏 iso-compute 比较（给 BCE 同等或更多训练资源后是否还有差距）。

### 主要优势（Reviewer 1 肯定的 5 点）
1. C1 target-swap ablation 设计巧妙，干净分离了 mask quality vs training objective coupling
2. 全面的 ablation 体系（relaxation type、divergence measure、coupling scope、compensation）
3. 3-seed 评估、cross-architecture validation
4. 梯度分析提供理论 insight
5. 匿名代码和详细超参数保障复现性

---

请对以上每个 Must-Fix、Should-Fix 逐条回应 [AGREE] 或 [REBUT]，附简要理由。特别关注与你初审意见的重合或分歧之处。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ddde40053945c09c17d4aaa8ca8e5b93:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---
