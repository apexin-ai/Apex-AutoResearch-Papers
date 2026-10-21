---
round: 8
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-21T14:19:57.790235+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh)

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**目标 Venue**: EMNLP 2026 via ARR May 2026
**审稿模式**: Fresh（无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作质量）

---

## Summary

本文研究 detect-and-reweight 范式在合成污染 continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens（ρ=0.4, 3 seeds）上的控制实验，得出三个发现：(1) Detect-and-Remove 的 PPL 优势 >95% 归因于多 epoch 暴露（epoch confound）而非过滤质量；(2) 有效重加权同时需要检测器的高 AUC 和良好校准（低 ECE）；(3) 提出双约束自适应 b*（α_eff 质量下限 + ESS 稳定性上限），声称 Δ=-0.020 PPL 改善（p=0.025）。扩展至 ρ=0.6 和 1.7B 参数量。

---

## Strengths

**S1. Epoch confound 发现具有独立贡献价值 [R1, R2 共识]**
Table 1 的 epoch-matched 对照实验揭示了 D&R 文献中未被充分讨论的混淆因素：D&R full 的 0.384 PPL 优势在控制内容 epoch 后缩小到 Δ=0.017。该发现对所有使用 D&R 的后续工作有直接指导意义。

**S2. Calibration 必要性是可操作的实践指导 [R1, R2 共识]**
TF-IDF+LR（AUC=0.94, ECE=0.048）有效而 GPT-2 PPL（AUC=0.91, ECE=0.131）失败的对比，清晰隔离了校准作为必要条件。"区分度+校准缺一不可"具有实用性。

**S3. 理论框架设计合理 [R1]**
双约束公式化将 convergence guarantee（Wang et al., 2026）和 importance sampling stability（Kish, 1965）统一。Proposition 1-2 的证明思路清晰。

**S4. 对自身局限性诚实 [R1, R2 共识]**
主动报告 ρ=0.2 退化、1.7B 效果减弱、checkpoint resume artifact，并提供 from-scratch seed 修正。透明度值得肯定。

**S5. 附录分析全面 [R1]**
15 个附录覆盖 grid search、阈值敏感性、constraint regime 分解、proxy 验证、cross-model transfer 等。

**S6. 格式合规性完整 [R2]**
正文 8 页、ACL 模板、double-blind 匿名、Limitations/Ethics/Checklist 齐全、引用格式正确。

---

## Weaknesses

### Critical（影响接收决定）

**C1. 效果规模极小，无下游任务改善 [R1 N2, R2 N2 — 共识]**
核心效果 Δ=-0.020 PPL 在 base ≈17.7 上仅为 0.11% 相对改善。Table 7（Appendix H）明确显示下游任务性能完全无差异（3-seed 均值相同 0.5414，所有差异在 ±0.01 标准误差内）。PPL 微小改进未转化为任何可测量的任务性能提升，方法的实际应用动机存疑。

**C2. N=3 seeds 统计功效不足 [R1 N1, R2 同意 — 共识]**
核心声称 Δ=-0.020, p=0.025 仅基于 3 个随机种子（df=2）。Paired t-test 在 df=2 时对 outlier 和非正态性极度敏感。论文测试了多种方法 × 多个 ρ × 多个评估域 × 多个模型大小的比较，未做多重比较校正。Appendix O 揭示 seed 42 使用 checkpoint-resumed 训练，resume artifact 膨胀了表观效应。

**C3. 相对 Drayson et al. (2025) 方法论新颖性不足 [R2 N1, R1 同意 — 共识]**
论文使用与 Drayson et al. 完全相同的 weighting formula w(x)=(1−q(x))^b，核心区别仅在于 b 的选择方式。双约束中 ESS 是重要性采样文献标准工具（Kish 1965, Owen 2013），α_eff 质量下限为经验性阈值。将两个标准工具组合为自适应选择器，本质上是超参数自动调节方案，技术深度有限。

### Warning（影响评分但不一票否决）

**W1. 自我污染设定生态效度受限 [R1, R2 共识]**
Qwen3-0.6B 生成 + 训练创造了最有利的检测环境。真实 web 污染包含异构多源合成文本。Cross-model transfer（Appendix N, Llama-3.2-3B）仅单 seed 且结果 mixed。

**W2. Discussion 过于单薄 [R2 N3]**
Section 6 仅约 11 行。对于分析型论文，缺少对已发表 D&R 工作的影响评估、多生成器场景的 calibration 挑战、adaptive b* 的理论最优性讨论、adversarial 条件下的鲁棒性分析等。

**W3. 论文定位模糊 [R2 W4, R1 隐含同意]**
在"分析论文"与"方法论文"之间定位模糊。若为方法论文，效果太小（0.11%）且无下游改善；若为分析论文，adaptive b* 篇幅占比过高。双重定位削弱了两个维度的说服力。

**W4. Epoch-matched 比较可能引入 LR schedule confound [R1 W2]**
完全控制 epoch+LR 后，D&R 过滤（PPL=18.78）反而劣于 uniform（18.06, Δ=+0.72）。论文将此描述为"warm LR from multi-epoch exposure"，但未直面其对重加权机制核心动机的冲击。

**W5. 检测器覆盖面窄 [R1 W3]**
仅 3 个检测器来自 2 个家族。缺少 fine-tuned 神经分类器（RoBERTa/DeBERTa）、DetectGPT/Fast-DetectGPT 等。"calibration matters" 发现可能是检测器家族特异性的。

**W6. α_eff 代理质量中等 [R1 W4]**
Pearson r≈0.70（r²=0.49），超过一半的真实人类比例方差未被捕获。未讨论残差来源及其对方法可靠性的影响。

**W7. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围 [R1, R2 共识]**
方法仅在 ρ≥0.4 + 小模型 + 校准判别式检测器交集下有效。ρ=0.2 退化 +0.046，1.7B OOD 部分不一致。

**W8. B=4 离散空间与连续理论的脱节 [R1 W6]**
Micro-batch B=4 时 α_eff 仅取 5 个离散值，bisection 在 5 点上运行。Propositions 的连续单调性保证与离散实现之间的 gap 未被讨论。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成共识：

1. **效果规模 + 无下游改善是最核心问题** — 两人均标 critical，认为 0.11% PPL 改进且无下游 transfer 严重限制了方法论文的价值。
2. **N=3 统计功效不足** — 两人均认为 df=2 下的 p 值不够可靠，需增加 seeds 或 bootstrap CI。
3. **Epoch confound 是论文最有价值的发现** — 两人均肯定此发现的社区诊断价值。
4. **Calibration 必要性有实用意义** — 两人均肯定。
5. **自我污染场景限制了泛化声称** — 两人均认为需更多 cross-model 实验或更严格限定 scope。
6. **论文定位需明确** — 建议明确为分析论文并降低方法贡献的 claim 强度。

---

## Reviewer Divergence

无重大分歧。两位 Reviewer 的唯一差异在于权重分配：
- R1 更关注统计严谨性（统计功效、α_eff 代理质量、B=4 离散化）
- R2 更关注新颖性和叙事完整性（与 Drayson 的区分、Discussion 深度、论文定位）

两者互补，无矛盾。

---

## Questions

1. 三个 from-scratch seeds 在 adaptive vs. uniform (ρ=0.4) 下各自的逐 seed PPL 值？改善是否跨 seed 一致？
2. Table 7 显示下游任务零改善。在无下游改善的情况下，方法的实际应用动机如何论证？
3. 完全控制 epoch+LR 后 D&R 劣于 uniform (Δ=+0.72)。如何调和这一发现与"重加权机制独立于 epoch 效应有贡献"的声称？
4. 是否考虑过异构多源污染（如混合 GPT-4+Llama+Qwen 生成文本）的实验？
5. α_eff 与真实人类比例仅 r=0.70。剩余 51% 方差中，检测器噪声 vs. 公式系统偏差各占多少？
6. 双约束的选择是经验性的还是有理论最优性依据？为何不考虑其他约束组合（如 KL divergence bound）？

---

## Missing References

论文 Related Work 覆盖面较广。以下可考虑补充：
- Mindermann et al. (2022) "Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt" — 已在 bib 中但可在 Instance-Level Reweighting 段落更显著地讨论其与 provenance-based reweighting 的关系。
- 无重大遗漏被两位 Reviewer 共同指出。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），本轮未请求外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: done（耗时约 3 分钟）

**Findings**（2 warnings, 14 info）:
- **[warning]** 第 3-6 页（Method + Experiments）4 页跨度内仅 Algorithm 1 作为 display item，主结果表格直到第 7 页才出现。审稿人在 §5.1 阅读结果讨论时看不到对应表格。建议将实验设置摘要表或关键 figure 前移。
- **[warning]** 末页（p.16）下半部约 40% 为空白，可重排附录内容减少浪费。
- **[info]** Figure 1（分析概览）在第 2 页顶部，若能提至第 1 页底部审稿体验更好。
- **[info]** 正文 8 页含 2 figure + 2 table + 1 algorithm = 5 个 display items，处于可接受下限。建议从附录提升 1-2 个关键 figure 到主文。
- **[info]** Table 1/2 使用 booktabs 风格，排版质量高。Figure 2 颜色语义清晰，色盲友好。
- **[info]** 未发现 margin 溢出、公式渲染错误或 LaTeX 残留问题。整体排版专业。

---

## Overall Assessment

**评分: 3.0 — Findings（可被 Findings 接收）**

**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，评分完全一致）

**理由**: 论文包含两个有独立价值的诊断发现（epoch confound 和 calibration 必要性），实验控制严谨，对自身局限性诚实。但存在三个 critical 问题制约主会议接收：(1) 核心方法效果极小（Δ=-0.020 PPL, 0.11%）且无下游任务改善；(2) N=3 seeds 统计支撑力有限；(3) 相对 Drayson et al. 的方法论新颖性为增量式（同一公式，仅改变超参数选择）。方法的适用范围也受限（ρ≥0.4 + 小模型 + 校准判别式检测器）。

**改进建议优先级**:
1. **明确论文定位为分析论文**：将 adaptive b* 降格为分析结论的自然推论，重心放在 F1-F3 的发现上
2. **扩展 Discussion**：当前 11 行远远不够，至少增加 1 页讨论
3. **增加统计可信度**：更多 seeds（≥5）或 bootstrap CI，对多重比较做 FDR 校正
4. **正文讨论下游零改善**：将 Table 7 的负面结果从附录移至正文 Discussion
5. **考虑 cross-model 污染实验**：至少 1-2 个异构生成器的完整实验

**注**: Reviewer 1 在 Round 1 报告中声称 "主文 §5.1 报告 p=0.025 而 Checklist §C3 报告 p=0.0425"。经 Review Director 逐文件验证，论文全文（abstract.tex、results.tex、checklist.tex）一致报告 p=0.025，不存在 p 值矛盾。该 issue 为 Reviewer 幻觉，未纳入本报告的 Weaknesses。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 准确反映论文内容，但 "improving over uniform at ρ≥0.4" 的措辞在实际效果仅 0.11% 且无下游改善时可能构成 overclaim。建议加入限定语。

**Introduction (§1)**: 4 个 findings 的组织逻辑清晰，Figure 1 有效传达论文结构。但从 F1-F3（分析发现）到 F4（adaptive b* 方法）的过渡缺乏足够动机——为什么分析发现自然导向这个特定的双约束设计？

**Related Work (§2)**: 覆盖全面，与 Drayson et al. 的三点区分（per-batch vs per-model、loss reweighting vs SIR、lightweight detector）清晰。Domain-level vs instance-level 的区分合理。

**Method (§3)**: 理论框架自洽。但 B=4 离散化问题需在正文讨论（当前仅在 §3.3 简要提及）。α_eff 作为真实人类比例代理的 r=0.70 限制应更显著地声明。

**Experiments (§4)**: 设置清晰完整。自我污染设定的局限应在此处（而非仅在 §8）预告。

**Results (§5)**: 实验结果呈现严谨（3 seeds、paired t-test、effect sizes）。但 Δ=-0.020 的实际意义需更多论证。Epoch confound 分析（§5.1, Table 1）是最强贡献。

**Discussion (§6)**: 严重不足。11 行无法覆盖论文发现的 implications。需讨论：(a) epoch confound 对已发表 D&R 文献的影响；(b) 何时应选择 uniform 而非 reweighting；(c) 下游零改善的含义；(d) 方法的理论局限。

**Conclusion (§7)**: 过于简短（~3 行），缺乏前瞻性讨论。

**Limitations (§8)**: 涵盖了主要局限（单模型族、单数据域、self-contamination、ρ=0.2 失败）。长度适当（符合 EMNLP 要求的简洁 Limitations）。

**Appendix**: 全面且有价值。建议将 Appendix O（checkpoint resume artifact）的关键信息移至正文 §5.1。