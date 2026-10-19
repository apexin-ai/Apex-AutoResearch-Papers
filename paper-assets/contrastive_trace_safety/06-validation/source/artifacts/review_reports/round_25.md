---
round: 25
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T13:44:07.777475+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告

## Summary

本文研究 reasoning model 中 hidden-state (HS) vs. text probes 在检测 Safety Commitment Point (CP) 时的层选择敏感性。核心发现是方法论层面的：层选择 metric 的选择（crossing-rate composite vs threshold-based）决定了层选择，进而决定了 HS 是否优于 text 的结论——在 32B 模型上甚至产生定性逆转。HS 优势是"doubly conditional"的：依赖弱 text encoder (384d MiniLM) 且部分与位置信号重叠。七种替代方法均未能匹配监督 probing。

## Strengths

1. **统计实践一流**：Bootstrap CI、Holm-Bonferroni 校正、exact permutation test（32B）、nested 5-fold CV（7-8B）、control task selectivity——远超同领域平均水平。
2. **5-metric taxonomy 有独立方法论价值**：crossing-rate composite vs threshold-based 的分类框架，配合 cosine compression 的几何解释，为后续 probing 研究提供了可操作的诊断工具。
3. **透明度优秀**：M002 bug 公开披露、20+ 页消融分析、per-seed breakdown、evidence gradient 三级分类（cross-validated / significant / exploratory）。
4. **Random-label control 设计巧妙**：在 QwQ-32B (Qwen) 和 R1-8B (Llama) 上的对比揭示了几何偏好的架构依赖性。
5. **系统 negative results 有社区价值**：7 种替代方法的失败模式分析（BOCPD/CUSUM 对渐进转变失效、Mahalanobis 无分离、RepE 模型依赖、cross-model transfer 失败）为后续研究划定了方法边界。
6. **引用覆盖全面**：80 篇引用，经验证无伪造。

## Weaknesses

### Must-Fix（影响接收决定）

**[Critical] W1: 架构多样性严重不足（3/4 Qwen），核心发现的泛化性存疑**
- R1-N1 + R2-W2，**Round 22-25 持续问题**，共识 Critical
- 4 模型中 3 个共享 Qwen 架构。Appendix B.1 的 random-label control 揭示了 Qwen 与 Llama 间机制的质的差异：Qwen 的浅层几何压缩偏好是 label-independent 的，而 R1-8B (Llama) 的浅层偏好是 label-dependent 的。这说明 metric-induced bias 的产生机制可能是 architecture-specific 的，不仅仅是 scope 问题。
- 标题 "Reasoning Models" 和 Abstract 的泛化语气与 3/4 Qwen 的实际覆盖不匹配。
- **要求**：Abstract/Conclusion 收窄为 "primarily Qwen-family (3/4 models), with one Llama model providing cross-architecture evidence"；Discussion 增加对 B.1 架构差异的正面讨论。

**[Critical] W2: 主文 text baseline (MiniLM-384d) 偏弱，HS 优势被系统高估**
- R1-W3 + R2-W1，共识 Critical
- 主文所有 HS vs text 对比使用 384d MiniLM，4/4 模型通过 HB。但 Appendix S/U 显示：BGE-large (1024d) 仅 1/4 HB，E5-Mistral-7B (4096d→PCA 384d) 仅 2/4 HB。主文不呈现 encoder quality gradient 造成过度乐观。
- "Doubly conditional" framing 在 Abstract 已提及，但主文 Section 4.3 的 encoder robustness 讨论仅一小段，核心数据在附录中。
- **要求**：Section 4.3 增加 encoder quality gradient 的正面讨论，至少包含 BGE-large 对比数据。

**[Critical-Major] W3: 与 Chan & Yong (2025) 的区分严重不足**
- R2-N2，R1 降级为 Major；综合判定 Critical-Major
- 这是最相近的 concurrent work（同样研究 reasoning model 上的 hidden-state linear probes 用于 safety/alignment 预测），Related Work 末尾仅一句话。未讨论：(a) probe 设计差异；(b) layer selection sensitivity 是否适用于他们的设置；(c) temporal windowing vs early-segment probing 的关系。
- Reviewer/AC 会直接质疑相对于这篇最相近 concurrent work 的增量贡献。
- **要求**：增加 1-2 段专门对比分析。

### Should-Fix（影响评分但不一票否决）

**[Major] W4: "Metric-induced layer selection bias" 的新颖性定位需要更诚实**
- R2-N3 (Critical) vs R1 (Minor)；综合判定 Major
- Layer selection sensitivity 是 Belinkov (2022) 已知问题。本文的增量是：(a) safety domain 的 empirical instantiation；(b) 定量展示了结论逆转（非渐进差异）；(c) cosine compression 的几何解释机制。
- Abstract/Introduction 的 framing 暗示是新发现，Discussion 的定位更准确。两处不一致。
- **要求**：C1 在 Introduction 明确 acknowledge Belinkov (2022) 已知 concern，然后清晰定位本文的 domain-specific quantification + mechanism identification 作为增量。

**[Major] W5: CP annotation 噪声对层选择结论的影响未量化**
- R1-W1，R2 AGREE
- κ=0.606, ±8.5 步偏差。Section J 的 CP 扰动分析仅测试了 BA 稳定性，未分析扰动后最优层是否变化——而层选择稳定性是本文核心声称。
- **要求**：在 Section J 增加 CP 扰动对层选择指标（而非仅 BA）的稳定性分析。

**[Major] W6: 两阶段设计中 Stage 1 搜索空间 (~2,240 configurations) 不受 HB 保护**
- R1-W2，R2 AGREE
- 7-8B 有 nested CV 缓解，但 32B (n=19-20) 仅有 split-half (~10 条/半)，统计效力极弱。论文的 evidence gradient 三级分类（cross-validated / significant / exploratory）是好的，但 32B 的 "exploratory" 标记在正文中不够醒目。
- **要求**：32B 相关结论在正文中增加更显著的 exploratory/provisional 标注。

**[Major] W7: C2 贡献归属——CP 由 HarmThoughts 定义，本文仅应用**
- R2-N1 (Critical) vs R1 REBUT (Major)；综合判定 Major
- R1 的反驳有道理：C2 核心在 boundary conditions 的发现（encoder quality + position），非 CP 定义本身。但当前 C2 措辞 "grounded in CP" 模糊了归属。
- **要求**：C2 重新措辞为 "empirical characterization of boundary conditions for HS advantage"，明确 CP 定义来自 HarmThoughts。

**[Major] W8: AUROC 排除理由不充分，二分 taxonomy 需扩展**
- R1-N2 (Critical) vs R2 REBUT (非循环论证但应主文讨论)；综合判定 Major
- AUROC 作为 threshold-free metric 选择 mid-deep 层，是二分 taxonomy 的独立第三视角。排除理由 "threshold-free, cannot diagnose layer selection bias" 方法论上自洽，但主文不讨论造成 taxonomy 不完整。
- **要求**：Discussion 增加 AUROC 层选择结果；taxonomy 从二分扩展为三类。

**[Moderate] W9: Negative results 配置公平性**
- R1-W4，R2 部分 REBUT
- MLP 128d hidden 在 n=20 上过参数化的批评有争议（R2 认为失败模式非简单过拟合），但 RepE/CCS 实现细节确实不足。
- **要求**：补充 RepE/CCS 实现细节。

**[Moderate] W10: Position residualization 可能移除 safety-position 混合信号**
- R1-W5，R2 AGREE (Moderate)
- 移除 9-20pp BA 但未分析 "纯位置" vs "位置-安全混合信号" 的比例。残余信号显著说明至少部分 HS advantage 非位置 artifact，但量化不足。
- **要求**：Discussion 讨论 residualization 的 conservative nature。

### Minor Issues

**[Minor] W11: Abstract 信息过载** — CP 定义、4 模型名、具体数字、metric 名称同时出现，核心 message 被淹没（R2-W4, R1 AGREE）。

**[Minor] W12: 统计报告风格不统一** — p-value、CI、effect size 报告方式跨 section 不一致（R2-W5, R1 AGREE）。

**[Minor] W13: 附录 23 页 vs 正文 8 页** — Random-Label Decomposition (B.1)、Position-Residualized Probing 等核心方法论内容在附录中。R1 认为 8 页限制下合理，R2 认为 B.1 关键发现应在 Discussion 更突出。综合判定 Minor，因 8 页限制是硬约束。

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：
- [AGREE] 架构多样性不足是最关键的问题（Critical）
- [AGREE] 主文 text baseline 偏弱导致 HS 优势被高估（Critical）
- [AGREE] Chan & Yong 对比不足（Major-Critical）
- [AGREE] CP 标注噪声对层选择未量化（Major）
- [AGREE] Stage 1 搜索空间保护不足 / 32B 缺 nested CV（Major）
- [AGREE] AUROC 应在主文讨论 + taxonomy 扩展（Major）
- [AGREE] Abstract 信息过载、统计报告不统一（Minor）

## Reviewer Divergence

| 问题 | R1 判定 | R2 判定 | 分歧核心 |
|------|---------|---------|----------|
| CP 原创性 (C2 归属) | Major | Critical | R1 认为 C2 核心在 boundary conditions，非 CP 定义 |
| Metric-induced bias 新颖性 | Minor | Critical | R1 认为 Section 1 p.2 已正确定位；R2 认为 Abstract framing 过度 |
| 附录比例 | Minor | Major | R1 认为 8 页限制下合理；R2 认为核心方法论应在正文 |
| Negative results 配置 (MLP) | Major | Moderate | R2 认为 MLP 批评过度，失败模式非简单过拟合 |

**评分分歧**：R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)。核心分歧在新颖性评估——R2 认为 metric-induced bias 是已知问题的 case study，novelty 不足以弥补条件性过强；R1 认为 5-metric taxonomy + 几何机制解释 + 社区指导价值提供了足够的方法论贡献。

## Questions

1. AUROC 选择的中层在 HS vs text 对比中结果如何？是否形成 threshold-based / crossing-rate / threshold-free 三级 taxonomy？
2. Chan & Yong (2025) 的 layer selection strategy 是什么？metric-induced bias 是否适用于他们的 experimental setup？
3. CP ±8.5 步偏差在 W=1 实验中如何影响层选择稳定性（不仅是 BA）？
4. 非 Qwen 架构的 32B reasoning model（如 Llama-3 70B distilled、Mixtral reasoning variant）上核心结论是否会改变？
5. Appendix Z.1 的 multi-metric ensemble 为什么没在正文更突出呈现？是否可作为 actionable solution？
6. 32B MDE 5.3-5.5pp 是否足以排除 CR-composite 层上较小但真实的 HS 优势？

## Missing References

两位 Reviewer 未报告新的遗漏引用。Round 24 遗留的 arXiv:2601.13288 (layer-selective probes) 仍待添加。建议验证 Chan & Yong (2025) 的 bib 条目是否已修正（Round 24 发现 title/author 错误）。

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置）。

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 17 info）。关键发现：

- **[Warning] Figure 1 首次出现在 p7**：9 页主文中前 6 页无 figure，"文字墙"印象明显。建议将 heatmap 或概念图提前到 p3-4。
- **[Warning] Pages 3-4 连续纯文本**（Related Work → Methods 开头），无 figure/table/equation 穿插，视觉疲劳。
- **[Warning] 主文 Display items 偏少**：仅 2 Figure + 4 Table = 6 items（同类论文通常 7-10）。前半部分（pages 1-5）仅 Table 1。
- **[Info]** Figure 2 (forest plot) 色盲友好设计良好；booktabs 表格风格规范；无 LaTeX 错误残留；页面边距无溢出。
- **[Info]** 附录 20 页含 42 table 但仅 3 figure，表图比极度失衡。

## Overall Assessment

**Overall: 3.0 (Findings)**
**置信度: 4/5**

**理由**：

论文提供了一个有价值的方法论警告——层选择 metric 的选择可以定性逆转 HS probe 的模态比较结论——配合优秀的统计实践和系统的 negative results。这对 probing 和 safety monitoring 社区都有指导意义。

但以下因素限制了 main conference 接收：

1. **架构覆盖不足**（3/4 Qwen）且 B.1 揭示了 Qwen/Llama 间质的机制差异，核心发现的泛化性存疑。
2. **HS 优势过度条件化**：仅在弱 encoder (384d) + 特定层 + 排除位置后成立；against BGE-large 仅 1/4 模型通过 HB。主文不呈现 encoder gradient 造成过度乐观。
3. **增量新颖性有争议**：metric-induced layer selection bias 是 Belinkov (2022) 已知问题的 domain-specific case study（R2 观点）vs 有独立方法论价值的定量展示 + 机制解释（R1 观点）。
4. **与最相近 concurrent work (Chan & Yong 2025) 区分不足**。

适合 Findings track：方法论贡献 solid，实验严谨，社区价值明确，但 excitement 和 scope 不足以支撑 main conference。Rebuttal 中如能 (1) 收窄架构泛化 claim + 正面讨论 B.1 差异、(2) 主文增加 encoder gradient、(3) 充分对比 Chan & Yong，有可能提升至 3.5。

## Detailed Comments

### Section 1 (Introduction)
- C1 "Layer selection sensitivity" 需在首次出现时 acknowledge Belinkov (2022) 的 general concern，然后定位 domain-specific quantification + mechanism 作为增量。当前 framing 暗示完全新发现。
- C2 措辞 "grounded in CP" 模糊了 CP 定义归属（HarmThoughts vs 本文）。建议改为 "empirical characterization of boundary conditions for HS advantage"。
- Table 1 caption 中 "Data: HarmThoughts with step-level CP annotations" 准确，但应在正文中更早声明 CP 定义来自 HarmThoughts。

### Section 2 (Related Work)
- Chan & Yong (2025) 仅一句话，需扩展为 1-2 段专门对比。
- 整体覆盖全面，引用真实。

### Section 3 (Method)
- Section 3.5 的 metric taxonomy（threshold-based vs crossing-rate composite）缺少 AUROC 作为第三类的讨论。
- 排除 AUROC 的脚注理由方法论自洽但不够透明——读者需要翻到附录才能看到 AUROC 实际支持深层。

### Section 4 (Experiments)
- Section 4.3 encoder robustness 仅一小段，BGE-large 和 E5-Mistral 结果在附录。建议至少将 Table (HS vs text at 1024d) 放入主文或增加数据讨论。
- Section 4.6 negative results：RepE/CCS 实现细节不足；MLP 配置在小样本上的公平性值得讨论。
- 32B "exploratory" 标记在正文中存在但不够醒目，容易被快速阅读的 reviewer 忽略。

### Section 5 (Discussion)
- "Guidance for future research" 的 multi-metric audit 建议有实用价值，但缺少 actionable decision criteria（diverge >20% depth 的阈值依据？）。
- B.1 random-label control 的架构差异发现应在 Discussion 正面讨论，当前仅在 Limitations 侧面提及。

### Limitations
- 覆盖合理（single dataset, 32B power, architecture coverage, causal status）。
- 建议增加 encoder-quality boundary 作为显式 limitation。

### Format/Writing
- Abstract 信息密度偏高，建议精简具体数字，保留核心 message。
- 统计报告风格建议统一（Section 3.5 增加约定）。
- 主文 display items 偏少（6 个），前 6 页仅 1 个 table，建议增加概念图或提前 Figure 1。