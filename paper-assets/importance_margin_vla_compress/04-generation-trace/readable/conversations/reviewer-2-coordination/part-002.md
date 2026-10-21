# Reviewer 2 coordination — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/65/651e71cd0460b6874c29.json)

## Round 11

### Tool call

_source line 538 · 2026-05-23T05:49:58.233534+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**审查侧重**：新颖性、相关工作覆盖、Contribution Claims 合理性、论文定位、CoRL Community 价值\n\n---\n\n## 总体评分\n\n**Overall**: 5/10（Borderline — 有价值的 empirical observations 但 contributions 各自不够深入）\n\n**一句话总结**：论文提出了有意义的 empirical 发现（connector coupling 决定 pruning robustness），但三个 contribution 各自的 evidence base 都偏薄——two-axis framework 是合理的 organizational lens 而非 intellectual contribution，CV diagnostic 只有 3 个有效数据点，VTR 只在一个模型上验证。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | Two-axis framework 是 organizing principle 而非发现；CV 是标准统计量的直接应用；VTR 的 cross-attention 机制在 Perceiver/Q-Former/BLIP-2 中已广泛使用 |\n| Quality | 3/5 | 实验设计系统但有明显空缺（Table 2 大量 \"--\" 数据、OpenVLA 只评了 Object suite）；CV diagnostic 的 correlation 证据不足 |\n| Clarity | 4/5 | 写作清晰，结构合理，Figure 1 teaser 有效传达核心信息；附录详尽 |\n| Significance | 2/5 | 对 CoRL 的 actionable impact 有限——仅 simulation，CV diagnostic 的实用门槛不明确，practitioner 难以直接使用 |\n| Relevance | 3/5 | 与 robot learning 相关但缺乏 real-robot 验证；LIBERO simulation 是合理 benchmark 但不足以支撑 CoRL 级别的 significance |\n| Limitations | 4/5 | 论文诚实承认了 simulation-only 和 causal isolation 的局限；Appendix A 的 extended discussion 有价值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool\n\n- 具体位置：Section 4.4 (CV as Sensitivity Indicator)、Table 1\n- 问题：论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\"（Introduction, C2），但支撑这一 claim 的 closed-loop 数据仅来自 3 个模型（π₀.5 CV=0.055, X-VLA CV=0.151, OpenVLA CV=0.215）。SmolVLA (CV=0.314) 在所有条件下均为 0% SR，无法提供 method sensitivity 信息。离线模型 π₀ 和 OFT 贡献了 CV 值但无 closed-loop 验证。用 3 个数据点建立\"无需下游评估即可选择压缩策略\"的 diagnostic tool，在统计上不可靠，在实践中不可用。\n- 为什么影响接收：C2 是论文的核心 contribution 之一。如果 CV diagnostic 的 evidence 不足以支撑其 claim，论文的 contribution 显著缩水。一个需要 CoRL 读者信任但只有 3 个 calibration 点的 diagnostic tool，在 rigorous review 下难以通过。\n- 建议修改方向：(a) 大幅降低 CV diagnostic 的 claim 强度，将其定位为 \"preliminary observation\" 而非 \"enabling diagnostic\"；(b) 增加更多 VLA 架构的 closed-loop 评估（如 RT-2, CogACT 等），至少达到 6+ 个数据点；(c) 或者将 CV 从核心 contribution 降级为 analysis tool。\n\n**N2** [critical] 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入\n\n- 具体位置：Contributions list (Introduction, lines 19-24)\n- 问题：论文同时声称三个 contribution：(C1) two-axis compressibility analysis, (C2) CV diagnostic, (C3) VTR method。但每个都不够深入独立成文：C1 只在 LIBERO 上测了 4 个 closed-loop 模型，Table 2 大量 \"--\" 缺失数据；C2 只有 3 个有效数据点（见 N1）；C3 只在 SmolVLA 一个模型上验证，且 MLP adapter 达到 comparable 性能（63.4% vs 60.1%, p=0.15, Section 4.5）说明 cross-attention 并非关键机制。这种\"三个 shallow contribution 拼凑\"的结构容易被 reviewer 认为每个 contribution 都是 incremental。\n- 为什么影响接收：CoRL reviewer 期望看到一个 deep contribution 或一个 thorough empirical study。当前状态下论文两头不靠——method contribution 太薄（单模型验证 + MLP adapter 平替），empirical study 不够 thorough（数据缺失 + 模型数量少）。\n- 建议修改方向：选定一个 primary identity 并深化。如果定位为 empirical study，补全 Table 2 所有缺失数据并增加模型/benchmark；如果定位为 method paper，在多个 entangling-connector 模型上验证 VTR。\n\n**N3** [critical] Table 2 数据大量缺失，削弱 cross-architecture analysis 的可信度\n\n- 具体位置：Table 2 (Section 4.2)\n- 问题：Table 2 是论文核心实验表格，但存在大量 \"--\" 条目：π₀.5 的 Goal suite 在 k=0.9 (Random) 和 k=0.7 (L2) 缺失；X-VLA 的 Long suite 在 k=0.9, 0.7, 0.5 大部分缺失；X-VLA 的 Goal 和 Spatial 也有缺失；OpenVLA 只评估了 Object 一个 suite。论文声称进行 \"cross-architecture analysis across four LIBERO suites\"，但实际数据矩阵的填充率不足 70%。\n- 为什么影响接收：数据缺失直接损害论文的核心 claim。\"Two-axis framework\" 需要 connector × complexity 的完整交叉数据来验证。缺失的恰恰是高复杂度任务（Long, Goal）的数据，而这些正是 task-complexity axis 的关键证据。\n- 建议修改方向：补全所有缺失的实验数据。这是一篇 empirical 论文，数据完整性是底线。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] VTR 的 novelty 不足——cross-attention re-encoding 是已知技术，MLP adapter 达到 comparable 性能\n\n- 具体位置：Section 3.4, Section 4.5\n- 问题：VTR 使用 learned queries 通过 cross-attention 聚合源 tokens——这与 Perceiver（Jaegle et al. 2021, 论文已引用）、Q-Former/BLIP-2（Li et al. 2023, 已引用）的机制本质相同。论文自身的消融实验显示 parameter-matched MLP adapter 达到 63.4% vs VTR 的 60.1%（p=0.15），说明 cross-attention 并非关键——任何 re-encoding 都能恢复。VTR 的 contribution 因此降级为\"对 pixel-shuffle VLA 应用已知 re-encoding 技术\"。\n- 建议：(a) 诚实承认 VTR 的 mechanism novelty 有限，强调 finding 的价值（即\"pixel-shuffle collapse 可通过任何 re-encoding 恢复\"）；(b) 探索 VTR 是否可以泛化到 X-VLA 的 BART encoder 等其他 entangling connector。\n\n**W2** [warning] 与 \"Don't Run with Scissors\" (Jabbour et al. 2025) 的差异化讨论不足\n\n- 具体位置：Section 2 (Related Work), Section 1 (Introduction)\n- 问题：Jabbour et al. 也发现 pruning breaks VLA 并提出 recovery method (GLUESTICK)。当前论文在 Related Work 中仅列出引用（Section 2, paragraph 2 中与其他 VLA-specific methods 一起提及），没有专门的比较段落。两篇论文的核心发现重叠度高：都发现 pruning 对 VLA 有破坏性影响。本文的差异化（connector architecture 作为 root cause 解释、CV diagnostic、VTR vs GLUESTICK 的不同 recovery 路线）应在正文中明确讨论。\n- 建议：在 Related Work 或 Introduction 中增加一个专门段落，对比本文与 Jabbour et al. 在 (1) 问题诊断维度、(2) recovery 方法、(3) 实验范围 上的差异。\n\n**W3** [warning] Two-axis framework 可能是对已知现象的 re-packaging\n\n- 具体位置：Section 4.2, Figure 1\n- 问题：(a) Connector coupling axis：\"pixel-shuffle 破坏空间信息因此不可 pruning\"——这从 pixel-shuffle 的定义就可以直接推导出来（4×4 folding 使每个 token 编码 16 个 patch，任何移除都丢失 6.25% 的空间场），Section 4.3 实际上确认了这一点。(b) Task complexity axis：\"多步任务比单步任务对 pruning 更敏感\"——这是 error compounding 的标准结论。将这两个已知现象组合成 \"two-axis framework\" 并声称为 contribution，有过度包装之嫌。\n- 建议：(a) 承认各轴的 individual observation 并非完全新颖，强调 cross-architecture systematic validation 和两轴交互的量化（如 20× amplification）才是贡献；(b) 讨论为什么 practitioner 之前没有系统验证过这些假设。\n\n**W4** [warning] 仅在 LIBERO simulation 上评估，缺乏 real-robot 验证——对 CoRL 论文价值有折扣\n\n- 具体位置：Section 4.1, Limitations (Section 4.5 末尾)\n- 问题：CoRL 的核心受众关心 real robot deployment。论文完全基于 LIBERO simulation benchmark（4 个 task suite × 10 tasks × 50 episodes）。虽然 Limitations 中承认了这一点，但缺乏任何对 sim-to-real transfer 的讨论。Compressor-VLA（concurrent work）已包含 real-robot 验证，这使得本文在 practical relevance 上处于劣势。\n- 建议：至少在 1-2 个真实机器人任务上验证核心发现（即 connector type 确实影响 pruning robustness），或详细讨论为什么 LIBERO 上的发现应该 transfer 到真实场景。\n\n**W5** [warning] OpenVLA 仅评估了 Object suite，未扩展到其他 LIBERO suites\n\n- 具体位置：Table 2\n- 问题：OpenVLA 是论文中唯一的 high-CV independent-connector 模型（CV=0.215），对于验证 \"independent connector degrade gracefully across task complexity\" 至关重要。但 Table 2 仅报告了 Object suite 的结果。缺少 Spatial/Goal/Long 数据意味着 OpenVLA 在 task-complexity axis 上完全没有验证。\n- 建议：补全 OpenVLA 在 Spatial、Goal、Long suites 的数据。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 中 π₀.5 在 k=0.9 的 Random SR 为 12.0%（Object），但在 k=0.7 反弹至 77.2%，k=0.5 为 69.4%。这种非单调性在正文中简要提及但未充分解释。建议讨论是否为统计波动（单 seed）或系统性现象。\n- **M2**: 论文使用 \"single-seed\" 评估（500 episodes per condition），但部分结论（如 20× amplification）依赖于精确的 SR 数值。建议报告多 seed 结果或至少在附录中验证关键发现的 seed 稳定性。Section 4.5 VTR 用了 3 seeds，但主实验没有。\n- **M3**: Abstract 中说 \"six VLA architectures (450M to 7B)\"，但只有 4 个做了 closed-loop 评估，另外 2 个（π₀, OFT）仅有 offline metrics。应在 abstract 中更精确地描述。\n- **M4**: 引用格式小问题——π₀.5 在论文中写作 \"$\\pi_0.5$\"，但标准写法应为 \"$\\pi_{0.5}$\"（下标）。当前形式在某些渲染中可能出现歧义。\n\n---\n\n## Questions to Authors\n\n**Q1**: Table 2 中 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 和 k=0.5 时 Random SR 反弹到 77.2% 和 69.4%。这是否为单一 seed 的随机波动？是否在其他 seed 上复现？\n\n**Q2**: MLP adapter 达到与 VTR comparable 的性能（63.4% vs 60.1%, p=0.15）。作者如何看待这一结果？这是否说明 cross-attention 机制并非关键，而是\"任何 re-encoding 都足以恢复 pixel-shuffle collapse\"？如果是这样，VTR 作为 contribution 的 value proposition 是什么？\n\n**Q3**: CV diagnostic 的 practical workflow 是什么？一个 practitioner 拿到新的 VLA 模型，计算了 CV 值，然后呢？具体的 decision threshold 是多少？论文是否建议 CV < X 用 L2 norm, X < CV < Y 用 random, CV > Y 不要 prune？3 个数据点如何确定这些 threshold？\n\n**Q4**: \"Don't Run with Scissors\" 的 GLUESTICK 是 training-free 的 recovery 方法，VTR 需要训练。作者是否在 SmolVLA 上比较过 GLUESTICK 和 VTR？如果没有，为什么？\n\n**Q5**: 论文在 Section 4.2 报告 X-VLA Long suite 在 k=0.95 就从 94.0% 崩溃到 47.0%（仅移除 3 个 token 中的约 2.5 个），但 BART encoder 的 50 token 序列长度本身就很短。是否有可能 X-VLA 的脆弱性主要来自极短的 token 序列（50 tokens, 移除 2-3 个即占 5%），而非 BART entangling 本身？\n\n---\n\n## Missing References\n\n所有 16 个 Director 指定检查的 concurrent work 均已引用。以下为建议补充：\n\n1. **A Survey on Efficient Vision-Language-Action Models** (2025, arXiv:2510.24795) — 提供 VLA efficiency 方向的全景综述，有助于读者定位本文。\n2. **ATP-LLaVA** (Adaptive Token Pruning for Large Vision Language Models) — 与 FastV/PruMerge 同方向的 VLM pruning work，可在 ViT token pruning 段落补充。\n\n---\n\n## 主要优势\n\n- **S1**: 系统性的 cross-architecture 实验设计（6 个模型 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio），在 VLA pruning 文献中范围最广。\n- **S2**: SmolVLA pixel-shuffle 在 5% pruning 即 catastrophic collapse 的发现是 non-trivial 的，对 practitioners 有直接预警价值。\n- **S3**: 写作质量高，结构清晰，Figure 1 teaser 有效传达核心信息，附录详尽（27 页包括大量 per-task 分析）。\n- **S4**: Limitations section 诚实且有实质内容，承认了 simulation-only 和 confounders 的问题。\n- **S5**: VTR 在 SmolVLA 上从 0% 恢复到 ~60% SR（与 baseline 59.2% 持平），在 75% compression 下实现，这是一个有价值的 proof-of-concept。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Why Token Pruning Crashes Some Robot Policies but Not Others\n\n**审查侧重**：新颖性、相关工作覆盖、Contribution Claims 合理性、论文定位、CoRL Community 价值\n\n---\n\n## 总体评分\n\n**Overall**: 5/10（Borderline — 有价值的 empirical observations 但 contributions 各自不够深入）\n\n**一句话总结**：论文提出了有意义的 empirical 发现（connector coupling 决定 pruning robustness），但三个 contribution 各自的 evidence base 都偏薄——two-axis framework 是合理的 organizational lens 而非 intellectual contribution，CV diagnostic 只有 3 个有效数据点，VTR 只在一个模型上验证。\n\n---\n\n## 官方维度打分（基于 CoRL 2023 Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Originality | 2/5 | Two-axis framework 是 organizing principle 而非发现；CV 是标准统计量的直接应用；VTR 的 cross-attention 机制在 Perceiver/Q-Former/BLIP-2 中已广泛使用 |\n| Quality | 3/5 | 实验设计系统但有明显空缺（Table 2 大量 \"--\" 数据、OpenVLA 只评了 Object suite）；CV diagnostic 的 correlation 证据不足 |\n| Clarity | 4/5 | 写作清晰，结构合理，Figure 1 teaser 有效传达核心信息；附录详尽 |\n| Significance | 2/5 | 对 CoRL 的 actionable impact 有限——仅 simulation，CV diagnostic 的实用门槛不明确，practitioner 难以直接使用 |\n| Relevance | 3/5 | 与 robot learning 相关但缺乏 real-robot 验证；LIBERO simulation 是合理 benchmark 但不足以支撑 CoRL 级别的 significance |\n| Limitations | 4/5 | 论文诚实承认了 simulation-only 和 causal isolation 的局限；Appendix A 的 extended discussion 有价值 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] CV Diagnostic 的 Evidence Base 严重不足——3 个数据点不能建立可靠的 diagnostic tool\n\n- 具体位置：Section 4.4 (CV as Sensitivity Indicator)、Table 1\n- 问题：论文声称 CV \"enables connector-appropriate compression strategy selection without downstream evaluation\"（Introduction, C2），但支撑这一 claim 的 closed-loop 数据仅来自 3 个模型（π₀.5 CV=0.055, X-VLA CV=0.151, OpenVLA CV=0.215）。SmolVLA (CV=0.314) 在所有条件下均为 0% SR，无法提供 method sensitivity 信息。离线模型 π₀ 和 OFT 贡献了 CV 值但无 closed-loop 验证。用 3 个数据点建立\"无需下游评估即可选择压缩策略\"的 diagnostic tool，在统计上不可靠，在实践中不可用。\n- 为什么影响接收：C2 是论文的核心 contribution 之一。如果 CV diagnostic 的 evidence 不足以支撑其 claim，论文的 contribution 显著缩水。一个需要 CoRL 读者信任但只有 3 个 calibration 点的 diagnostic tool，在 rigorous review 下难以通过。\n- 建议修改方向：(a) 大幅降低 CV diagnostic 的 claim 强度，将其定位为 \"preliminary observation\" 而非 \"enabling diagnostic\"；(b) 增加更多 VLA 架构的 closed-loop 评估（如 RT-2, CogACT 等），至少达到 6+ 个数据点；(c) 或者将 CV 从核心 contribution 降级为 analysis tool。\n\n**N2** [critical] 论文 identity 分裂——empirical study / diagnostic tool / method 三者均不够深入\n\n- 具体位置：Contributions list (Introduction, lines 19-24)\n- 问题：论文同时声称三个 contribution：(C1) two-axis compressibility analysis, (C2) CV diagnostic, (C3) VTR method。但每个都不够深入独立成文：C1 只在 LIBERO 上测了 4 个 closed-loop 模型，Table 2 大量 \"--\" 缺失数据；C2 只有 3 个有效数据点（见 N1）；C3 只在 SmolVLA 一个模型上验证，且 MLP adapter 达到 comparable 性能（63.4% vs 60.1%, p=0.15, Section 4.5）说明 cross-attention 并非关键机制。这种\"三个 shallow contribution 拼凑\"的结构容易被 reviewer 认为每个 contribution 都是 incremental。\n- 为什么影响接收：CoRL reviewer 期望看到一个 deep contribution 或一个 thorough empirical study。当前状态下论文两头不靠——method contribution 太薄（单模型验证 + MLP adapter 平替），empirical study 不够 thorough（数据缺失 + 模型数量少）。\n- 建议修改方向：选定一个 primary identity 并深化。如果定位为 empirical study，补全 Table 2 所有缺失数据并增加模型/benchmark；如果定位为 method paper，在多个 entangling-connector 模型上验证 VTR。\n\n**N3** [critical] Table 2 数据大量缺失，削弱 cross-architecture analysis 的可信度\n\n- 具体位置：Table 2 (Section 4.2)\n- 问题：Table 2 是论文核心实验表格，但存在大量 \"--\" 条目：π₀.5 的 Goal suite 在 k=0.9 (Random) 和 k=0.7 (L2) 缺失；X-VLA 的 Long suite 在 k=0.9, 0.7, 0.5 大部分缺失；X-VLA 的 Goal 和 Spatial 也有缺失；OpenVLA 只评估了 Object 一个 suite。论文声称进行 \"cross-architecture analysis across four LIBERO suites\"，但实际数据矩阵的填充率不足 70%。\n- 为什么影响接收：数据缺失直接损害论文的核心 claim。\"Two-axis framework\" 需要 connector × complexity 的完整交叉数据来验证。缺失的恰恰是高复杂度任务（Long, Goal）的数据，而这些正是 task-complexity axis 的关键证据。\n- 建议修改方向：补全所有缺失的实验数据。这是一篇 empirical 论文，数据完整性是底线。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] VTR 的 novelty 不足——cross-attention re-encoding 是已知技术，MLP adapter 达到 comparable 性能\n\n- 具体位置：Section 3.4, Section 4.5\n- 问题：VTR 使用 learned queries 通过 cross-attention 聚合源 tokens——这与 Perceiver（Jaegle et al. 2021, 论文已引用）、Q-Former/BLIP-2（Li et al. 2023, 已引用）的机制本质相同。论文自身的消融实验显示 parameter-matched MLP adapter 达到 63.4% vs VTR 的 60.1%（p=0.15），说明 cross-attention 并非关键——任何 re-encoding 都能恢复。VTR 的 contribution 因此降级为\"对 pixel-shuffle VLA 应用已知 re-encoding 技术\"。\n- 建议：(a) 诚实承认 VTR 的 mechanism novelty 有限，强调 finding 的价值（即\"pixel-shuffle collapse 可通过任何 re-encoding 恢复\"）；(b) 探索 VTR 是否可以泛化到 X-VLA 的 BART encoder 等其他 entangling connector。\n\n**W2** [warning] 与 \"Don't Run with Scissors\" (Jabbour et al. 2025) 的差异化讨论不足\n\n- 具体位置：Section 2 (Related Work), Section 1 (Introduction)\n- 问题：Jabbour et al. 也发现 pruning breaks VLA 并提出 recovery method (GLUESTICK)。当前论文在 Related Work 中仅列出引用（Section 2, paragraph 2 中与其他 VLA-specific methods 一起提及），没有专门的比较段落。两篇论文的核心发现重叠度高：都发现 pruning 对 VLA 有破坏性影响。本文的差异化（connector architecture 作为 root cause 解释、CV diagnostic、VTR vs GLUESTICK 的不同 recovery 路线）应在正文中明确讨论。\n- 建议：在 Related Work 或 Introduction 中增加一个专门段落，对比本文与 Jabbour et al. 在 (1) 问题诊断维度、(2) recovery 方法、(3) 实验范围 上的差异。\n\n**W3** [warning] Two-axis framework 可能是对已知现象的 re-packaging\n\n- 具体位置：Section 4.2, Figure 1\n- 问题：(a) Connector coupling axis：\"pixel-shuffle 破坏空间信息因此不可 pruning\"——这从 pixel-shuffle 的定义就可以直接推导出来（4×4 folding 使每个 token 编码 16 个 patch，任何移除都丢失 6.25% 的空间场），Section 4.3 实际上确认了这一点。(b) Task complexity axis：\"多步任务比单步任务对 pruning 更敏感\"——这是 error compounding 的标准结论。将这两个已知现象组合成 \"two-axis framework\" 并声称为 contribution，有过度包装之嫌。\n- 建议：(a) 承认各轴的 individual observation 并非完全新颖，强调 cross-architecture systematic validation 和两轴交互的量化（如 20× amplification）才是贡献；(b) 讨论为什么 practitioner 之前没有系统验证过这些假设。\n\n**W4** [warning] 仅在 LIBERO simulation 上评估，缺乏 real-robot 验证——对 CoRL 论文价值有折扣\n\n- 具体位置：Section 4.1, Limitations (Section 4.5 末尾)\n- 问题：CoRL 的核心受众关心 real robot deployment。论文完全基于 LIBERO simulation benchmark（4 个 task suite × 10 tasks × 50 episodes）。虽然 Limitations 中承认了这一点，但缺乏任何对 sim-to-real transfer 的讨论。Compressor-VLA（concurrent work）已包含 real-robot 验证，这使得本文在 practical relevance 上处于劣势。\n- 建议：至少在 1-2 个真实机器人任务上验证核心发现（即 connector type 确实影响 pruning robustness），或详细讨论为什么 LIBERO 上的发现应该 transfer 到真实场景。\n\n**W5** [warning] OpenVLA 仅评估了 Object suite，未扩展到其他 LIBERO suites\n\n- 具体位置：Table 2\n- 问题：OpenVLA 是论文中唯一的 high-CV independent-connector 模型（CV=0.215），对于验证 \"independent connector degrade gracefully across task complexity\" 至关重要。但 Table 2 仅报告了 Object suite 的结果。缺少 Spatial/Goal/Long 数据意味着 OpenVLA 在 task-complexity axis 上完全没有验证。\n- 建议：补全 OpenVLA 在 Spatial、Goal、Long suites 的数据。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 中 π₀.5 在 k=0.9 的 Random SR 为 12.0%（Object），但在 k=0.7 反弹至 77.2%，k=0.5 为 69.4%。这种非单调性在正文中简要提及但未充分解释。建议讨论是否为统计波动（单 seed）或系统性现象。\n- **M2**: 论文使用 \"single-seed\" 评估（500 episodes per condition），但部分结论（如 20× amplification）依赖于精确的 SR 数值。建议报告多 seed 结果或至少在附录中验证关键发现的 seed 稳定性。Section 4.5 VTR 用了 3 seeds，但主实验没有。\n- **M3**: Abstract 中说 \"six VLA architectures (450M to 7B)\"，但只有 4 个做了 closed-loop 评估，另外 2 个（π₀, OFT）仅有 offline metrics。应在 abstract 中更精确地描述。\n- **M4**: 引用格式小问题——π₀.5 在论文中写作 \"$\\pi_0.5$\"，但标准写法应为 \"$\\pi_{0.5}$\"（下标）。当前形式在某些渲染中可能出现歧义。\n\n---\n\n## Questions to Authors\n\n**Q1**: Table 2 中 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0%，但 k=0.7 和 k=0.5 时 Random SR 反弹到 77.2% 和 69.4%。这是否为单一 seed 的随机波动？是否在其他 seed 上复现？\n\n**Q2**: MLP adapter 达到与 VTR comparable 的性能（63.4% vs 60.1%, p=0.15）。作者如何看待这一结果？这是否说明 cross-attention 机制并非关键，而是\"任何 re-encoding 都足以恢复 pixel-shuffle collapse\"？如果是这样，VTR 作为 contribution 的 value proposition 是什么？\n\n**Q3**: CV diagnostic 的 practical workflow 是什么？一个 practitioner 拿到新的 VLA 模型，计算了 CV 值，然后呢？具体的 decision threshold 是多少？论文是否建议 CV < X 用 L2 norm, X < CV < Y 用 random, CV > Y 不要 prune？3 个数据点如何确定这些 threshold？\n\n**Q4**: \"Don't Run with Scissors\" 的 GLUESTICK 是 training-free 的 recovery 方法，VTR 需要训练。作者是否在 SmolVLA 上比较过 GLUESTICK 和 VTR？如果没有，为什么？\n\n**Q5**: 论文在 Section 4.2 报告 X-VLA Long suite 在 k=0.95 就从 94.0% 崩溃到 47.0%（仅移除 3 个 token 中的约 2.5 个），但 BART encoder 的 50 token 序列长度本身就很短。是否有可能 X-VLA 的脆弱性主要来自极短的 token 序列（50 tokens, 移除 2-3 个即占 5%），而非 BART entangling 本身？\n\n---\n\n## Missing References\n\n所有 16 个 Director 指定检查的 concurrent work 均已引用。以下为建议补充：\n\n1. **A Survey on Efficient Vision-Language-Action Models** (2025, arXiv:2510.24795) — 提供 VLA efficiency 方向的全景综述，有助于读者定位本文。\n2. **ATP-LLaVA** (Adaptive Token Pruning for Large Vision Language Models) — 与 FastV/PruMerge 同方向的 VLM pruning work，可在 ViT token pruning 段落补充。\n\n---\n\n## 主要优势\n\n- **S1**: 系统性的 cross-architecture 实验设计（6 个模型 × 3 种 connector family × 2 种 pruning 策略 × 6 个 retention ratio），在 VLA pruning 文献中范围最广。\n- **S2**: SmolVLA pixel-shuffle 在 5% pruning 即 catastrophic collapse 的发现是 non-trivial 的，对 practitioners 有直接预警价值。\n- **S3**: 写作质量高，结构清晰，Figure 1 teaser 有效传达核心信息，附录详尽（27 页包括大量 per-task 分析）。\n- **S4**: Limitations section 诚实且有实质内容，承认了 simulation-only 和 confounders 的问题。\n- **S5**: VTR 在 SmolVLA 上从 0% 恢复到 ~60% SR（与 baseline 59.2% 持平），在 75% compression 下实现，这是一个有价值的 proof-of-concept。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-23T05:50:02.152084+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 540 · 2026-05-23T05:50:12.919121+00:00_

审稿报告已提交给 Review Director。

核心评价：论文提出了有价值的 empirical 发现（connector coupling 是 pruning robustness 的主要决定因素），但三个 contribution 各自证据不足：

1. **CV diagnostic 只有 3 个有效数据点**，不足以建立可靠的 diagnostic tool
2. **Table 2 数据大量缺失**（填充率不足 70%），削弱 cross-architecture analysis 的说服力
3. **VTR 仅在 SmolVLA 一个模型上验证**，且 MLP adapter 达到 comparable 性能（p=0.15），说明 cross-attention 并非关键机制

总体评分 5/10（Borderline），主要因为论文 identity 分裂（empirical study / diagnostic / method 三者均不够深），且纯 simulation 评估对 CoRL 的 practical relevance 打折。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

26 recorded events


### User

_source line 541 · 2026-05-23T05:52:34.909446+00:00_

[Round 1 审稿请求]:
## 交叉分享：请逐条回应 Reviewer 1 和 Reviewer 3 的审稿意见

请对以下两份审稿报告中的每个 Must-Fix 和 Should-Fix 条目逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 的审稿报告（方法严谨性/实验有效性）

### Must-Fix:
**R1-N1**: CV diagnostic 的统计基础不足：N=4 闭环模型无法建立可靠的诊断关系。4 个单调排列的数据点的概率 ≤ 1/4! = 1/24。未提供 Spearman rank correlation 及 p-value。

**R1-N2**: 因果叙事超出证据范围：Connector → pruning tolerance 因果推断缺乏控制。模型同时在 backbone、预训练数据、token 数量上不同。正文 Section 5 使用"primary determinant"。

**R1-N3**: 缺少关键 pruning baseline：L2 norm 和 random 不构成充分的方法 bracket。Attention-based scoring（VLA-Cache/FastV 采用）和 gradient-based importance 完全缺失。

### Should-Fix:
**R1-W1**: VTR 贡献被 MLP adapter 控制实验严重削弱（p=0.15）。
**R1-W2**: VTR 训练条件不公平：batch size 4 vs. 64。
**R1-W3**: 跨条件使用不同 seed 引入潜在混淆。
**R1-W4**: Table 2 大量缺失数据限制跨模型比较。
**R1-W5**: Post-connector pruning 缺乏系统 justification。
**R1-W6**: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini。

---

## Reviewer 3 的审稿报告（写作/格式/Limitations）

### Must-Fix:
**R3-N1**: 缺少 Generative AI 使用披露。
**R3-N2**: "VTR" 与 "Smart Compress" 命名不一致。
**R3-N3**: Table 2 缺失数据过多。

### Should-Fix:
**R3-W1**: LaTeX 渲染错误 `$\pi_0.5$` 全文 50+ 处。
**R3-W2**: Limitations section 过于简短（3 句话）。
**R3-W3**: 缺少代码/数据发布计划。
**R3-W4**: Abstract 信息密度过高。
**R3-W5**: Figure 3 可读性问题。

---

请逐条回应，重点关注你的专长领域（新颖性/定位/相关工作）的交叉点。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-23T05:52:42.847320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 543 · 2026-05-23T05:52:43.853914+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-23T05:52:43.854359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-23T05:52:44.310074+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-23T05:52:44.310605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-23T05:52:44.812727+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-23T05:52:44.813172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-23T05:52:45.767284+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-23T05:52:45.767716+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-23T05:52:46.219520+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-23T05:52:46.219957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-23T05:52:47.174766+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-23T05:52:47.175114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-23T05:52:47.376321+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-23T05:52:47.376779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-23T05:52:47.428001+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/sessions/review_reviewer_2_29d69ba3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-23T05:52:52.534584+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "7-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/submitted.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "7-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-23T05:52:52.990522+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 340.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 236.3}], \"total_pages\": 27, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-23T05:52:56.153063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-23T05:52:56.607379+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-23T05:52:56.607876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-23T05:52:56.961960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-23T05:54:47.685775+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：逐条回应 Reviewer 1 和 Reviewer 3\n\n---\n\n## 回应 Reviewer 1（方法严谨性/实验有效性）\n\n### Must-Fix\n\n**[AGREE] R1-N1: CV diagnostic 的统计基础不足**\n\n完全同意。这与我的 R2-N1 一致。N=4 闭环模型（实际有效数据点仅 3 个，SmolVLA 全 0% 无 method sensitivity 信息）不足以建立可靠 diagnostic。R1 提出的 1/4!=1/24 概率分析进一步量化了这一问题——4 个单调排列的数据点在随机排列下出现概率约 4.2%，即使算作\"显著\"也处于边缘。补充一点：即使增加 Spearman rank correlation，N=4 时的 p-value 在统计意义上也极为有限（Spearman N=4 的最小可能 p-value 约 0.083，无法达到 0.05 显著性水平）。这意味着仅靠当前 4 个模型，CV diagnostic 在统计上**原则上不可能**被严格验证。必须增加模型数量至 6+ 才有意义。\n\n**[AGREE] R1-N2: 因果叙事超出证据范围**\n\n同意，且与我的审查侧重（论文定位）直接相关。论文在 Conclusion（Section 5）使用 \"connector coupling is the primary determinant of pruning robustness\" 这样的因果语言，但实验设计无法支撑因果推断。6 个模型在 backbone 架构（Qwen2-VL 0.5B vs. PaliGemma 3B vs. LLaMA 7B）、参数量（450M-7B，16× 范围）、预训练数据、vision encoder（SigLIP vs. DINOv2 vs. SigLIP-SO400M）、token 数量（50-768，15× 范围）上全部不同。Connector 是其中一个变量，但 confounders 使得无法分离其因果效应。\n\n从定位角度补充：如果论文降级为 \"observational study\"（观察到 connector 与 pruning robustness 的 correlation），而非 \"causal analysis\"，其 contribution 就更加诚实但也更弱——这进一步加剧了我在 R2-N2 中指出的 identity 问题。\n\n**[AGREE] R1-N3: 缺少关键 pruning baseline**\n\n同意，从 novelty/positioning 角度补充。论文将自己定位为 \"cross-architecture analysis of token compressibility\"，但只用了两种最简单的 pruning 策略（L2 norm 和 random）。这相当于用最粗糙的工具来做精细诊断。具体而言：\n\n- **Attention-based scoring**（FastV、VLA-Cache 采用）：论文在 Related Work 中引用了 FastV 和 VLA-Cache（Section 2），但自己不用 attention-based scoring，这在 related work positioning 上造成矛盾——既认可这些方法的重要性又不将其纳入 baseline。\n- **Gradient-based importance**：完全缺失。对于声称研究 \"which tokens matter\" 的论文，不测试 gradient-based 方法是重大遗漏。\n- 从 novelty 角度看，如果 attention-based scoring 在 entangling connectors 上也同样失败，这将大幅加强论文的核心 narrative（\"问题在 connector 而非 scoring function\"）。缺少这一 baseline 反而削弱了论文的说服力。\n\n### Should-Fix\n\n**[AGREE] R1-W1: VTR 贡献被 MLP adapter 控制实验削弱**\n\n同意，这与我的 R2-W1 完全一致。Section 4.5 报告 MLP adapter 63.4% vs VTR 60.1%（p=0.15），不仅无法拒绝零假设，MLP adapter 的点估计还更高。这说明 VTR 的 contribution 不是 cross-attention 机制本身，而是 \"re-encoding 这一类操作对 pixel-shuffle collapse 有效\" 这一 finding。从 novelty 角度看，这实际上是一个更有趣但更弱的 contribution——它说明 pixel-shuffle 的 catastrophic failure 可被几乎任何参数量匹配的 re-encoding 模块修复。\n\n**[REBUT] R1-W2: VTR 训练条件不公平（batch size 4 vs. 64）**\n\n部分不同意。R1 指出 VTR 使用 batch size 4 而基线 SmolVLA fine-tuning 使用 batch size 64，认为这构成不公平比较。但这里需要区分两个问题：(1) VTR 的比较对象不是 SmolVLA baseline（59.2%），而是 pruning 后的 SmolVLA（0.0%）。VTR 从 0.0% 恢复到 60.1%，无论 batch size 如何，这个 recovery 都是实质性的。(2) VTR 与 MLP adapter 的消融比较中，二者使用相同训练条件（Section 4.5 \"parameter-matched\"），这个内部比较是公平的。\n\n不过 R1 的关切仍有价值：如果 VTR 在 batch size 64 下训练，其性能可能更高，这会改变与 MLP adapter 的比较结论。建议作者在附录中补充 batch size sensitivity 分析。\n\n**[AGREE] R1-W3: 跨条件使用不同 seed 引入混淆**\n\n同意。这与我的 Minor issue M2 一致。Table 2 的主实验为单 seed（500 episodes），而 VTR 用了 3 seeds。跨条件的 seed 不一致使得跨模型比较的精确数值（如 \"20× amplification\"）的可靠性存疑。特别是 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0% 这一异常值（我在 R2 Q1 中也提出了质疑），可能就是单 seed 波动。\n\n**[AGREE] R1-W4: Table 2 大量缺失数据**\n\n完全同意，这与我的 R2-N3 一致。Table 2 的数据缺失严重影响 cross-architecture claim 的可信度。不再重复。\n\n**[AGREE] R1-W5: Post-connector pruning 缺乏系统 justification**\n\n同意，从 positioning 角度补充一个重要观点。论文选择在 post-connector 位置 pruning，但 concurrent work（VLA-Cache、EfficientVLA）在 KV-cache 或 pre-connector 位置操作。论文没有解释为什么 post-connector pruning 是 the right level of abstraction。\n\n从 novelty 角度看：如果 pre-connector pruning 和 post-connector pruning 的行为不同（例如 pre-connector pruning 对 pixel-shuffle 可能不那么 catastrophic），那么论文的核心发现（\"pixel-shuffle = catastrophic collapse\"）就只适用于 post-connector pruning 这一特定设定，generality 大打折扣。论文应至少讨论这一 limitation。\n\n**[REBUT] R1-W6: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini**\n\n部分不同意。R1 要求比较 CV 与 entropy/kurtosis/Gini 等替代指标。但鉴于 N=4（实际 N=3）的数据量，任何指标比较都缺乏统计意义——在 3 个数据点上比较不同 metric 的 correlation 是 overfitting，不是 validation。我认为问题不在于\"该选哪个 metric\"而在于\"sample size 太小以至于任何 metric 都无法被验证\"。这回到 R1-N1/R2-N1 的核心问题。\n\n如果作者增加到 6+ 模型，那么 R1-W6 的比较就变得有意义且必要。在当前 N=3 下，补充其他 metric 的比较只是增加了复杂度而非证据。\n\n---\n\n## 回应 Reviewer 3（写作/格式/Limitations）\n\n### Must-Fix\n\n**[AGREE] R3-N1: 缺少 Generative AI 使用披露**\n\n同意。CoRL 2026 如果遵循 NeurIPS/ICML 的趋势，很可能要求 AI usage disclosure。这是一个 checkbox 级别的合规问题，容易修复但不应遗漏。从 reviewer 角度，缺少 disclosure 不影响技术评价，但在审稿流程中可能被标记为 non-compliance。\n\n**[AGREE] R3-N2: \"VTR\" 与 \"Smart Compress\" 命名不一致**\n\n同意。我在阅读论文时也注意到附录中出现 \"Smart Compress\" 和 \"Smart Compressor\"（Appendix E.12, E.13, G, H），但正文只使用 \"VTR\"。这造成混淆——读者无法确定这是同一方法还是不同方法。从 positioning 角度看，统一命名对论文的 contribution 清晰度至关重要：如果 \"Smart Compress\" 是 VTR 的扩展（加入了 pruning 策略选择逻辑），那是一个额外 contribution 但未在正文中 claim；如果只是别名，应统一为 \"VTR\"。\n\n**[AGREE] R3-N3: Table 2 缺失数据过多**\n\n同意，与 R1-W4 和 R2-N3 一致。三位 reviewer 均提出同一问题，说明这是 consensus issue。\n\n### Should-Fix\n\n**[AGREE] R3-W1: `$\\pi_0.5$` LaTeX 渲染错误**\n\n同意。这与我的 Minor M4 一致。正确写法为 `$\\pi_{0.5}$`。全文 50+ 处出现说明是 systematic error，但修复简单。\n\n**[AGREE] R3-W2: Limitations section 过于简短**\n\n同意。Section 4.5 末尾的 Limitations 段落确实只有 3 句话（约 60 words）。对于一篇 empirical 论文，应该更充分地讨论以下限制：(a) simulation-only，无 real-robot 验证（我在 R2-W4 中也提出）；(b) confounders 使因果推断不可能（R1-N2）；(c) CV diagnostic 的 N=3 evidence base（R1-N1/R2-N1）；(d) post-connector pruning 作为唯一 pruning point 的局限性（R1-W5）。当前的 Limitations 仅提及 (a) 和 (b)，遗漏了对论文核心 contribution 的 self-critique。\n\n但我在 R2 评分中已给 Limitations 维度 4/5，因为 Appendix A 包含了更详细的 extended discussion，补充了正文中的不足。问题是 reviewer 和读者可能只看正文而不翻附录。\n\n**[AGREE] R3-W3: 缺少代码/数据发布计划**\n\n同意。可复现性对 empirical 论文至关重要。CoRL 虽然没有 mandatory code release 要求，但在 anonymous review 期间声明\"camera-ready 后发布代码和 checkpoint\"是标准做法。特别是本文包含 VTR 训练和 SmolVLA fine-tuning 等需要精确复现的实验。\n\n**[REBUT] R3-W4: Abstract 信息密度过高**\n\n部分不同意。R3 认为 abstract 塞入了太多具体数字（\"5%\"、\"0.0%\"、\"98.2%\"、\"20×\"、\"22M\"、\"60%\"、\"75%\"等），建议精简。但从 novelty/positioning 角度看，这些具体数字恰恰是论文最有冲击力的卖点——\"移除 5% token 即从 59.2% 崩溃到 0.0%\" 比 \"少量 pruning 导致 catastrophic failure\" 在传达效果上强得多。对于一篇 empirical 论文，abstract 中的具体量化是优势而非劣势。\n\n我的建议是保持核心数字（5% → 0.0% collapse, 20× amplification, VTR recovery to 60%），但删减次要数字（22M parameters, 三种 connector family 的详细枚举），以在信息密度和可读性之间取得平衡。\n\n**[AGREE] R3-W5: Figure 3 可读性问题**\n\n同意。Figure 3（page 8, \"Method sensitivity at k=0.95\"）使用柱状图显示 method gap，但 π₀.5 的两个 bar（Object 28.8pp 和 Spatial 21.4pp）与 X-VLA/OpenVLA 的 bar（0.2-1.4pp）尺度差异约 20×，导致后者在视觉上几乎不可见。从 positioning 角度看，这张图应该是论文的 key selling point（CV 低 → method sensitivity 高），但当前可视化反而让 X-VLA 和 OpenVLA 的数据难以辨认。建议使用 log scale y-axis 或 broken axis。\n\n---\n\n## 三位 Reviewer 的共识总结\n\n以下问题被 2-3 位 reviewer 共同指出，应视为 high-confidence 共识：\n\n| 问题 | R1 | R2 | R3 | 共识强度 |\n|------|-----|-----|-----|---------|\n| CV diagnostic evidence 不足 (N=3/4) | N1 | N1 | — | 2/3 |\n| Table 2 数据大量缺失 | W4 | N3 | N3 | 3/3 |\n| VTR 被 MLP adapter 平替 | W1 | W1 | — | 2/3 |\n| `π_0.5` 渲染错误 | — | M4 | W1 | 2/3 |\n| Limitations 讨论不足 | — | — | W2 | 1/3（但 R1-N2 和 R2-W4 间接触及）|\n| 缺少代码发布计划 | — | — | W3 | 1/3 |\n\n最强共识（3/3）：**Table 2 数据缺失**——这是所有 reviewer 的底线问题，必须在 revision 中完全解决。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应：逐条回应 Reviewer 1 和 Reviewer 3\n\n---\n\n## 回应 Reviewer 1（方法严谨性/实验有效性）\n\n### Must-Fix\n\n**[AGREE] R1-N1: CV diagnostic 的统计基础不足**\n\n完全同意。这与我的 R2-N1 一致。N=4 闭环模型（实际有效数据点仅 3 个，SmolVLA 全 0% 无 method sensitivity 信息）不足以建立可靠 diagnostic。R1 提出的 1/4!=1/24 概率分析进一步量化了这一问题——4 个单调排列的数据点在随机排列下出现概率约 4.2%，即使算作\"显著\"也处于边缘。补充一点：即使增加 Spearman rank correlation，N=4 时的 p-value 在统计意义上也极为有限（Spearman N=4 的最小可能 p-value 约 0.083，无法达到 0.05 显著性水平）。这意味着仅靠当前 4 个模型，CV diagnostic 在统计上**原则上不可能**被严格验证。必须增加模型数量至 6+ 才有意义。\n\n**[AGREE] R1-N2: 因果叙事超出证据范围**\n\n同意，且与我的审查侧重（论文定位）直接相关。论文在 Conclusion（Section 5）使用 \"connector coupling is the primary determinant of pruning robustness\" 这样的因果语言，但实验设计无法支撑因果推断。6 个模型在 backbone 架构（Qwen2-VL 0.5B vs. PaliGemma 3B vs. LLaMA 7B）、参数量（450M-7B，16× 范围）、预训练数据、vision encoder（SigLIP vs. DINOv2 vs. SigLIP-SO400M）、token 数量（50-768，15× 范围）上全部不同。Connector 是其中一个变量，但 confounders 使得无法分离其因果效应。\n\n从定位角度补充：如果论文降级为 \"observational study\"（观察到 connector 与 pruning robustness 的 correlation），而非 \"causal analysis\"，其 contribution 就更加诚实但也更弱——这进一步加剧了我在 R2-N2 中指出的 identity 问题。\n\n**[AGREE] R1-N3: 缺少关键 pruning baseline**\n\n同意，从 novelty/positioning 角度补充。论文将自己定位为 \"cross-architecture analysis of token compressibility\"，但只用了两种最简单的 pruning 策略（L2 norm 和 random）。这相当于用最粗糙的工具来做精细诊断。具体而言：\n\n- **Attention-based scoring**（FastV、VLA-Cache 采用）：论文在 Related Work 中引用了 FastV 和 VLA-Cache（Section 2），但自己不用 attention-based scoring，这在 related work positioning 上造成矛盾——既认可这些方法的重要性又不将其纳入 baseline。\n- **Gradient-based importance**：完全缺失。对于声称研究 \"which tokens matter\" 的论文，不测试 gradient-based 方法是重大遗漏。\n- 从 novelty 角度看，如果 attention-based scoring 在 entangling connectors 上也同样失败，这将大幅加强论文的核心 narrative（\"问题在 connector 而非 scoring function\"）。缺少这一 baseline 反而削弱了论文的说服力。\n\n### Should-Fix\n\n**[AGREE] R1-W1: VTR 贡献被 MLP adapter 控制实验削弱**\n\n同意，这与我的 R2-W1 完全一致。Section 4.5 报告 MLP adapter 63.4% vs VTR 60.1%（p=0.15），不仅无法拒绝零假设，MLP adapter 的点估计还更高。这说明 VTR 的 contribution 不是 cross-attention 机制本身，而是 \"re-encoding 这一类操作对 pixel-shuffle collapse 有效\" 这一 finding。从 novelty 角度看，这实际上是一个更有趣但更弱的 contribution——它说明 pixel-shuffle 的 catastrophic failure 可被几乎任何参数量匹配的 re-encoding 模块修复。\n\n**[REBUT] R1-W2: VTR 训练条件不公平（batch size 4 vs. 64）**\n\n部分不同意。R1 指出 VTR 使用 batch size 4 而基线 SmolVLA fine-tuning 使用 batch size 64，认为这构成不公平比较。但这里需要区分两个问题：(1) VTR 的比较对象不是 SmolVLA baseline（59.2%），而是 pruning 后的 SmolVLA（0.0%）。VTR 从 0.0% 恢复到 60.1%，无论 batch size 如何，这个 recovery 都是实质性的。(2) VTR 与 MLP adapter 的消融比较中，二者使用相同训练条件（Section 4.5 \"parameter-matched\"），这个内部比较是公平的。\n\n不过 R1 的关切仍有价值：如果 VTR 在 batch size 64 下训练，其性能可能更高，这会改变与 MLP adapter 的比较结论。建议作者在附录中补充 batch size sensitivity 分析。\n\n**[AGREE] R1-W3: 跨条件使用不同 seed 引入混淆**\n\n同意。这与我的 Minor issue M2 一致。Table 2 的主实验为单 seed（500 episodes），而 VTR 用了 3 seeds。跨条件的 seed 不一致使得跨模型比较的精确数值（如 \"20× amplification\"）的可靠性存疑。特别是 π₀.5 在 k=0.9 Random 下 Object SR 仅 12.0% 这一异常值（我在 R2 Q1 中也提出了质疑），可能就是单 seed 波动。\n\n**[AGREE] R1-W4: Table 2 大量缺失数据**\n\n完全同意，这与我的 R2-N3 一致。Table 2 的数据缺失严重影响 cross-architecture claim 的可信度。不再重复。\n\n**[AGREE] R1-W5: Post-connector pruning 缺乏系统 justification**\n\n同意，从 positioning 角度补充一个重要观点。论文选择在 post-connector 位置 pruning，但 concurrent work（VLA-Cache、EfficientVLA）在 KV-cache 或 pre-connector 位置操作。论文没有解释为什么 post-connector pruning 是 the right level of abstraction。\n\n从 novelty 角度看：如果 pre-connector pruning 和 post-connector pruning 的行为不同（例如 pre-connector pruning 对 pixel-shuffle 可能不那么 catastrophic），那么论文的核心发现（\"pixel-shuffle = catastrophic collapse\"）就只适用于 post-connector pruning 这一特定设定，generality 大打折扣。论文应至少讨论这一 limitation。\n\n**[REBUT] R1-W6: CV 选择的理论动机不足——未比较 CV vs. entropy/kurtosis/Gini**\n\n部分不同意。R1 要求比较 CV 与 entropy/kurtosis/Gini 等替代指标。但鉴于 N=4（实际 N=3）的数据量，任何指标比较都缺乏统计意义——在 3 个数据点上比较不同 metric 的 correlation 是 overfitting，不是 validation。我认为问题不在于\"该选哪个 metric\"而在于\"sample size 太小以至于任何 metric 都无法被验证\"。这回到 R1-N1/R2-N1 的核心问题。\n\n如果作者增加到 6+ 模型，那么 R1-W6 的比较就变得有意义且必要。在当前 N=3 下，补充其他 metric 的比较只是增加了复杂度而非证据。\n\n---\n\n## 回应 Reviewer 3（写作/格式/Limitations）\n\n### Must-Fix\n\n**[AGREE] R3-N1: 缺少 Generative AI 使用披露**\n\n同意。CoRL 2026 如果遵循 NeurIPS/ICML 的趋势，很可能要求 AI usage disclosure。这是一个 checkbox 级别的合规问题，容易修复但不应遗漏。从 reviewer 角度，缺少 disclosure 不影响技术评价，但在审稿流程中可能被标记为 non-compliance。\n\n**[AGREE] R3-N2: \"VTR\" 与 \"Smart Compress\" 命名不一致**\n\n同意。我在阅读论文时也注意到附录中出现 \"Smart Compress\" 和 \"Smart Compressor\"（Appendix E.12, E.13, G, H），但正文只使用 \"VTR\"。这造成混淆——读者无法确定这是同一方法还是不同方法。从 positioning 角度看，统一命名对论文的 contribution 清晰度至关重要：如果 \"Smart Compress\" 是 VTR 的扩展（加入了 pruning 策略选择逻辑），那是一个额外 contribution 但未在正文中 claim；如果只是别名，应统一为 \"VTR\"。\n\n**[AGREE] R3-N3: Table 2 缺失数据过多**\n\n同意，与 R1-W4 和 R2-N3 一致。三位 reviewer 均提出同一问题，说明这是 consensus issue。\n\n### Should-Fix\n\n**[AGREE] R3-W1: `$\\pi_0.5$` LaTeX 渲染错误**\n\n同意。这与我的 Minor M4 一致。正确写法为 `$\\pi_{0.5}$`。全文 50+ 处出现说明是 systematic error，但修复简单。\n\n**[AGREE] R3-W2: Limitations section 过于简短**\n\n同意。Section 4.5 末尾的 Limitations 段落确实只有 3 句话（约 60 words）。对于一篇 empirical 论文，应该更充分地讨论以下限制：(a) simulation-only，无 real-robot 验证（我在 R2-W4 中也提出）；(b) confounders 使因果推断不可能（R1-N2）；(c) CV diagnostic 的 N=3 evidence base（R1-N1/R2-N1）；(d) post-connector pruning 作为唯一 pruning point 的局限性（R1-W5）。当前的 Limitations 仅提及 (a) 和 (b)，遗漏了对论文核心 contribution 的 self-critique。\n\n但我在 R2 评分中已给 Limitations 维度 4/5，因为 Appendix A 包含了更详细的 extended discussion，补充了正文中的不足。问题是 reviewer 和读者可能只看正文而不翻附录。\n\n**[AGREE] R3-W3: 缺少代码/数据发布计划**\n\n同意。可复现性对 empirical 论文至关重要。CoRL 虽然没有 mandatory code release 要求，但在 anonymous review 期间声明\"camera-ready 后发布代码和 checkpoint\"是标准做法。特别是本文包含 VTR 训练和 SmolVLA fine-tuning 等需要精确复现的实验。\n\n**[REBUT] R3-W4: Abstract 信息密度过高**\n\n部分不同意。R3 认为 abstract 塞入了太多具体数字（\"5%\"、\"0.0%\"、\"98.2%\"、\"20×\"、\"22M\"、\"60%\"、\"75%\"等），建议精简。但从 novelty/positioning 角度看，这些具体数字恰恰是论文最有冲击力的卖点——\"移除 5% token 即从 59.2% 崩溃到 0.0%\" 比 \"少量 pruning 导致 catastrophic failure\" 在传达效果上强得多。对于一篇 empirical 论文，abstract 中的具体量化是优势而非劣势。\n\n我的建议是保持核心数字（5% → 0.0% collapse, 20× amplification, VTR recovery to 60%），但删减次要数字（22M parameters, 三种 connector family 的详细枚举），以在信息密度和可读性之间取得平衡。\n\n**[AGREE] R3-W5: Figure 3 可读性问题**\n\n同意。Figure 3（page 8, \"Method sensitivity at k=0.95\"）使用柱状图显示 method gap，但 π₀.5 的两个 bar（Object 28.8pp 和 Spatial 21.4pp）与 X-VLA/OpenVLA 的 bar（0.2-1.4pp）尺度差异约 20×，导致后者在视觉上几乎不可见。从 positioning 角度看，这张图应该是论文的 key selling point（CV 低 → method sensitivity 高），但当前可视化反而让 X-VLA 和 OpenVLA 的数据难以辨认。建议使用 log scale y-axis 或 broken axis。\n\n---\n\n## 三位 Reviewer 的共识总结\n\n以下问题被 2-3 位 reviewer 共同指出，应视为 high-confidence 共识：\n\n| 问题 | R1 | R2 | R3 | 共识强度 |\n|------|-----|-----|-----|---------|\n| CV diagnostic evidence 不足 (N=3/4) | N1 | N1 | — | 2/3 |\n| Table 2 数据大量缺失 | W4 | N3 | N3 | 3/3 |\n| VTR 被 MLP adapter 平替 | W1 | W1 | — | 2/3 |\n| `π_0.5` 渲染错误 | — | M4 | W1 | 2/3 |\n| Limitations 讨论不足 | — | — | W2 | 1/3（但 R1-N2 和 R2-W4 间接触及）|\n| 缺少代码发布计划 | — | — | W3 | 1/3 |\n\n最强共识（3/3）：**Table 2 数据缺失**——这是所有 reviewer 的底线问题，必须在 revision 中完全解决。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-23T05:54:53.655333+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5969
}
```

</details>

---


### Assistant

_source line 566 · 2026-05-23T05:55:00.634036+00:00_

交叉回应已提交给 Director。

总结：在 R1 的 9 个条目中，我 AGREE 了 7 个、REBUT 了 2 个（R1-W2 VTR batch size 公平性——部分反驳因 VTR 的比较对象是 0% 而非 baseline；R1-W6 替代 metric 比较——在 N=3 下无统计意义）。在 R3 的 8 个条目中，AGREE 了 7 个、REBUT 了 1 个（R3-W4 Abstract 信息密度——具体数字是 empirical 论文的卖点）。三位 reviewer 最强共识是 Table 2 数据缺失（3/3），其次是 CV diagnostic evidence 不足和 VTR 被 MLP adapter 平替（均 2/3）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

66 recorded events


### User

_source line 567 · 2026-05-29T00:43:23.296047+00:00_

[Round 7 审稿请求]:
## Round 7 继续审稿 — Reviewer 2 任务

**角色**：新增内容质量 + 整体叙事连贯性审查
**Venue**：CoRL 2026（8 页正文限制，双盲，需 Limitations section + AI disclosure）

你是 Round 7 继续审稿的 Reviewer 2。上一轮（Round 6）给出 Weak Reject 5/10。论文已进行大幅修改，新增了多个实验和分析。你的核心任务是**评估新增内容的质量和论文整体连贯性**。

### 论文文件
- LaTeX 源文件目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/`
- 主文件：`main.tex`（入口），各章节：`abstract.tex`, `introduction.tex`, `related_work.tex`, `method.tex`, `experiments.tex`, `conclusion.tex`, `limitations.tex`, `appendix.tex`
- PDF：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf`

### 审查重点 1：新增实验内容质量

**A. Zero-mask ablation（Section 4.3）**
- 这是 Round 7 新增的核心贡献之一
- 检查：实验设计是否 sound？"89pp gap entirely attributable to position disruption" 的声明是否 justified？是否有替代解释未讨论？仅在 π₀.5 Object 上验证是否够？

**B. Attention-based scoring（Section 4.4 + Appendix）**
- 检查：Table tab:attention_pruning 数据质量。X-VLA Goal 为何合并为单个值 "98.2*"？
- 检查：π₀.5 attention 结果（tab:pi05_attention_crosssuite）是否讨论了 Object 上 attention 失败的机制？
- 检查："architecture-dependent scoring" 的结论是否有足够证据支撑？

**C. Importance margin 分析**
- 检查：Δ(k) 的 inverted-U 形状是否有 π₀.5 Long 以外的验证？
- 检查：fig_cliff_highlight 和 fig_margin_profile 是否与文字描述一致？

**D. π₀.5 Long multi-seed（n=5）**
- 检查：5-seed 结果（Table tab:pi05_long_multiseed）s.d. 是否合理？是否所有 claim 都正确引用了 n=5？

### 审查重点 2：叙事连贯性和 Contribution 清晰度

**E. 三个 Contribution 的清晰度**
- C1：六架构 compressibility 分析 → 是否清楚说明了什么新发现？
- C2：CV 单次诊断 → 是否过度声明？"validated on four closed-loop architectures" 是否准确？
- C3：Zero-mask + VTR → 两个不同的结果绑定在一个 contribution 是否合理？

**F. 主表 vs 附录分配**
- OpenVLA 移至附录是否合理？是否导致主文叙事不完整？
- 主文 Table 2 只有 3 个模型（π₀.5, X-VLA, SmolVLA），是否足以支撑 "six architectures" 的声明？

**G. 页数合规**
- 检查 PDF 页数：正文是否 ≤ 8 页（不含 references 和 appendix）？
- 检查正文密度：是否有挤压排版的痕迹（float spacing 调整、过小字号等）？

**H. Abstract 质量**
- Round 6 要求减少数字密度（从 17 个降到 ~5 个）。检查现版本数字数量和可读性。

### 审查重点 3：写作质量

- 全文扫描：是否有 AI 生成痕迹（过度结构化、"delve into"、"it is worth noting" 等短语）？
- 术语一致性：VTR 命名是否全文一致？"importance margin" 是否有清晰定义后一致使用？
- 图表引用完整性：所有 Figure/Table 是否在正文中被引用？

### 输出格式
```
## 新增内容质量

### A. Zero-mask ablation
评价：...

### B. Attention-based scoring
评价：...

### C. Importance margin
评价：...

### D. Multi-seed
评价：...

## 叙事连贯性

### E. Contributions
评价：...

### F. 主表 vs 附录
评价：...

### G. 页数合规
评价：...

### H. Abstract
评价：...

## 写作质量
评价：...

## 新发现问题（Must-Fix / Should-Fix / Info）
...

## 评分建议
Round 7 建议评分：X/10
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-29T00:43:40.155427+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf",
  "project": "importance_margin_vla_compress",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/submitted.pdf",
    "project": "importance_margin_vla_compress",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-29T00:43:41.138807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-29T00:43:41.374363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-29T00:43:42.357394+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 300.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 508.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 455.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 326.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 261.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 285.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 278.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 323.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_v
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2201
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-29T00:43:42.357847+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns (up to $20{\times}$ from Object to Goal at $k{=}0.9$). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1219
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-29T00:43:42.358200+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA 
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 983
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-29T00:43:49.926467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-29T00:43:50.882579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-29T00:43:50.933251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-29T00:43:51.387033+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-29T00:43:51.437641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-29T00:43:51.891260+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-29T00:43:51.892605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-29T00:43:52.798661+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-29T00:43:52.849310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-29T00:43:53.303602+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-29T00:43:53.304101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-29T00:43:53.810631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-29T00:43:53.811096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-29T00:43:54.466026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-29T00:43:54.466540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-29T00:43:54.870683+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-29T00:44:02.356243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-29T00:44:02.808352+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean SR over 500 episodes. Multi-seed results ($\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\pm$ s.d.\ with per-seed breakdowns in the appendix.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
19	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
20	\label{fig:pruning_overview}
21	\end{figure}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Obje
…[truncated 7667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-29T00:44:02.808910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-29T00:44:02.909973+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). \textbf{Linear projection} applies a per-patch matrix multiplication ($\pi_{0}$~\cite{black2024pi0}, $\pi_{0.5}$~\cite{black2025pi05}; CV$\,{<}\,$0.06). \textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\cite{kim2024openvla}, OFT~\cite{kim2025openoft}; CV$\,{\approx}\,$0.22). \textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\cite{zheng2025xvla} uses a 12-layer BART encoder~\cite{lewis2020bart} (CV$\,{=}\,$0.151); SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 patches per token (CV$\,{=}\,$0.314). We classify coupling as \emph{independent} (one patch per output) or \emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
12	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}
13	\label{fig:architecture}
14	\end{figure*}
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{VLA models evaluated. Coupling indicates independent vs.\ cross-token processing. $N$ = vision tokens input to the LLM. $^\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
20	\label{tab:model_properties}
21	\begin{tabular}{lrlcrll}
22	\toprule
23	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
24	\midrule
25	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 
…[truncated 5703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-29T00:44:09.130408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-29T00:44:09.581869+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluation with domain shift would strengthen practical applicability. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing full causal isolation of the connector effect; controlled studies varying only the connector within a fixed backbone would sharpen causal claims. The CV--SR correlation relies on four closed-loop models, too few for a general law; expanding the model pool as new VLA architectures emerge will test whether CV generalizes as a universal diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g., cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and random scoring are systematically compared; gradient-based importance scoring or learned pruning masks could yield better token selection. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, s.d.\ ${\leq}$2.7\,pp); future work should adopt multi-seed evaluation across all conditions to quantify variance. \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-29T00:44:09.632487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-29T00:44:10.034319+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity (up to $20{\times}$ from Object to Goal at $k{=}0.9$). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-29T00:44:10.034812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-29T00:44:10.236475+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-29T00:44:16.434880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-29T00:44:16.786945+00:00_

File content (27322 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-29T00:44:21.270100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-29T00:44:21.372808+00:00_

0	\appendix
1	
2	\section{Full Pruning Results}
3	\label{app:full_results}
4	
5	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
6	
7	\begin{table*}[ht]
8	\centering
9	\footnotesize
10	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
11	\label{tab:full_results}
12	\setlength{\tabcolsep}{4pt}
13	\begin{tabular}{llccccc}
14	\toprule
15	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
16	\midrule
17	\multirow{4}{*}{$\pi_{0.5}$}
18	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
19	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
20	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
21	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
22	\midrule
23	\multirow{4}{*}{X-VLA}
24	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
25	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
26	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
27	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
28	\midrule
29	\multirow{4}{*}{OpenVLA}
30	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
31	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\textsu
…[truncated 18864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-29T00:44:27.907293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-29T00:44:27.958149+00:00_

200	milk & 62 \\
201	orange\_juice & 38 \\
202	salad\_dressing & 50 \\
203	tomato\_sauce & 52 \\
204	\midrule
205	\textbf{Overall} & \textbf{44.8} \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\subsection{Official SmolVLA Checkpoint Per-Task Results}
211	
212	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
213	
214	\begin{table}[ht]
215	\centering
216	\small
217	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
218	\label{tab:smolvla_official_pertask}
219	\begin{tabular}{lcc}
220	\toprule
221	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
222	\midrule
223	alphabet\_soup & 64 & 0 \\
224	bbq\_sauce & 38 & 0 \\
225	butter & 78 & 0 \\
226	chocolate\_pudding & 90 & 0 \\
227	cream\_cheese & 40 & 0 \\
228	ketchup & 60 & 0 \\
229	milk & 52 & 0 \\
230	orange\_juice & 80 & 0 \\
231	salad\_dressing & 44 & 0 \\
232	tomato\_sauce & 46 & 0 \\
233	\midrule
234	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	\subsection{OpenVLA Per-Task Results Under Pruning}
240	
241	\begin{table}[ht]
242	\centering
243	\small
244	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
245	\label{tab:openvla_pertask}
246	\begin{tabular}{lccccc}
247	\toprule
248	Task
…[truncated 11306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-29T00:44:32.979663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "400",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "400",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-29T00:44:33.030581+00:00_

400	\small
401	\caption{OpenVLA success rates (\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\ref{tab:main_results}) uses seed 42 for both L2 and random.}
402	\label{tab:openvla_multiseed}
403	\begin{tabular}{cccc}
404	\toprule
405	$k$ & Seed 7 (\%) & Seed 43 (\%) & $\Delta$ (pp) \\
406	\midrule
407	0.90 & 62.0 & 62.2 & $+$0.2 \\
408	0.70 & 49.0 & 44.4 & $-$4.6 \\
409	0.50 & 37.4 & 35.6 & $-$1.8 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\subsection{L2 Norm vs.\ Random Scoring on OpenVLA}
415	\label{app:l2_vs_random}
416	
417	\begin{table}[ht]
418	\centering
419	\small
420	\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\,{=}\,$42; random uses seed$\,{=}\,$7. Main text (Table~\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\%, $k{=}0.5$: 35.8\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\% (L2 outperforms by 3.6\,pp); same-seed at $k{=}0.7$ yields 44.4\% (L2 outperforms by 5.4\,pp). $\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}
421	\label{tab:openvla_l2_vs_random}
422	\begin{tabular}{cccc}
423	\toprule
424	$k$ & L2 Norm SR (\%) & Random SR (\%) & $\Delta$ (pp) \\
425	\midrule
426	0.95 & 70.6 & 69.4 & $+$1.2 \\
427	0.90 & 70.6 & 62.0 & $+$8.6 \\
428	0.70 & 49.8 & 49.0 & $+$0.8 \\
429	0.50 & 39.2 & 37.4 & $+$1.8 \\
430	0.30 & 25.0 & 20.6 & $+$4.4 \\
431	\bottomrule
432	\end{tabular}
433	\end{table}
434	
435	\subsection{X-VLA Cliff Localization: Per-Task Analysis}
436	\label{app:xvla_cliff}
437	
438	\begin{table}[ht]
439	\centering
440	\small
441	\caption{X-VLA per-task success rates (\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seed
…[truncated 11904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-29T00:44:40.559067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "650",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "650",
    "limit": "250"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-29T00:44:40.911800+00:00_

650	{\footnotesize $^\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\% vs.\ 87.3\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}
651	\end{table}
652	
653	The loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\ 0.045) but lower eval loss (0.052 vs.\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\ref{sec:metric_disconnect}).
654	
655	\subsection{MLP Adapter Control}
656	\label{app:mlp_adapter}
657	
658	To verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \times d_{\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\% reduction), the MLP adapter achieves $63.4 \pm 2.6$\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \pm 1.3$\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.
659	
660	
661	\section{Offline Single-Step Action Error Analysis}
662	\label{app:offline_error}
663	
664	Table~\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 d
…[truncated 28735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-29T00:44:47.062623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "900",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "900",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-29T00:44:47.163388+00:00_

900	\begin{table}[ht]
901	\centering
902	\small
903	\caption{$\pi_{0.5}$ attention vs.\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}
904	\label{tab:pi05_attention_crosssuite}
905	\begin{tabular}{lccc}
906	\toprule
907	Suite & Attention (\%) & Random (\%) & $\Delta$ (pp) \\
908	\midrule
909	Goal & 71.2 & 73.6 & $-$2.4 \\
910	Spatial & 72.6 & 71.6 & $+$1.0 \\
911	Long & 49.4 & 46.8 & $+$2.6 \\
912	Object & 37.8 & 69.4 & $-$31.6 \\
913	\bottomrule
914	\end{tabular}
915	\end{table} By contrast, $\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\,pp at $k{=}0.85$, decaying to $+$5.6\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\ref{fig:scoring_crossover}).
916	
917	\begin{table}[h]
918	\centering
919	\small
920	\caption{Scoring reversal summary: $\Delta$ vs.\ random at $k{=}0.5$, except \textsuperscript{*}Goal suite across $k \in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\ref{fig:scoring_crossover}.}
921	\label{tab:scoring_crossover_summary}
922	\begin{tabular}{lcc}
923	\toprule
924	& Attention & L2 norm \\
925	\midrule
926	Entangling (X-VLA) & Effective ($+$31\,pp) & Anti-inform.\ ($-$8 to $-$27\,pp) \\
927	Token-indep.\ ($\pi_{0.5}$) & Ineffective\textsuperscript{$\dagger$} ($-$2 to $-$30\,pp) & Effective\textsuperscript{*} ($+$35.2$\to$$+$5.6\,pp) \\
928	\bottomrule
929	\multicolumn{3}{l}{\footnotesize\textsuperscript{$\dagger$}Neutral on 3/4 suites ($\pm$3\,pp); harmful on Object ($-$30.4\,pp).}
930	\end{tabular}
931	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-29T00:44:53.719738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "932",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "932",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-29T00:44:53.858257+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (932). The file has 931 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 138
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-29T00:45:00.097289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-29T00:45:00.700968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-29T00:45:00.777407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-29T00:45:01.657244+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 879
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-29T00:46:34.241095+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jabbour|scissors|dontrun",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jabbour|scissors|dontrun",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-29T00:46:34.744299+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib:76:@article{jabbour2025dontrun,
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib.prev:64:@article{jabbour2025dontrun,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-29T00:46:34.895299+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Smart.?Compress",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Smart.?Compress",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-29T00:46:34.946419+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/related_work_draft.tex:30:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis_draft.tex:29:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/notes/narrative_options.md:31:## Direction B: Negative Motivation + Positive Smart Compression
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/notes/narrative_options.md:36:### 可能的 Smart Compression 方法
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/gen_figures.py:88:    # Smart Compress — 3-seed means from Table 2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-29T00:46:39.966386+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jabbour|dontrun",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jabbour|dontrun",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-29T00:46:40.016961+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-29T00:46:46.905040+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-29T00:46:46.955655+00:00_

5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
8:[Omitted long matching line]
11:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-29T00:46:56.251826+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "specprune|seewhat|sparsevlm|sparsevila|fitprune|crossget",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "specprune|seewhat|sparsevlm|sparsevila|fitprune|crossget",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-29T00:46:56.302480+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-29T00:49:38.639504+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 7 审稿报告\n\n**角色**：新颖性 / 相关工作 / 论文定位（延续 Round 6 职责）+ 新增内容质量 + 叙事连贯性\n**Round 6 评分**：5/10 (Weak Reject)\n\n---\n\n## 新增内容质量\n\n### A. Zero-mask ablation（Section 4.3）\n\n**评价：Strong addition。** 实验设计清晰地分离了两个因素：信息丢失 vs. 位置扰动。Zero-masking 将 10% token 的 embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR；hard pruning 移除相同 token 并 re-index（部分信息损失 + 位置变化）崩溃到 9.0%。89pp 的差距归因于位置扰动而非信息丢失，这一结论在实验设计上是 justified 的——如果信息丢失是主因，zero-masking 应该比 hard pruning 更差（信息丢失更严重），但实际结果相反。\n\n**局限性**：仅在 π₀.5 Object k=0.9 一个条件上验证。该发现与 RoPE positional encoding 高度相关（论文在 Appendix 中承认了这一点），因此可能不 generalize 到非 RoPE 架构（如 X-VLA 的 BART encoder 使用 learned positional embeddings）。Section 4.3 的声明 \"entirely attributable to position disruption\" 应加限定语 \"on π₀.5\"。不过作为 diagnostic finding 而非 general claim，在单个模型上的验证已足够。\n\n### B. Attention-based scoring（Section 4.4 + Appendix）\n\n**评价：Substantial improvement。** 这是 Round 6 R1-N3（缺少 attention baseline）的直接回应。\n\n**X-VLA 结果（Table tab:attention_pruning）**：Attention scoring 在 k=0.5 恢复 ≥92.8% SR（所有 suite），而 L2 在所有 suite 上低于 random（-8.2 到 -27.2pp）。这个 double dissociation 是论文最强的新发现之一：L2 对 independent connectors 有效，attention 对 entangling connectors 有效，且两者不可互换。\n\n**问题：X-VLA Goal 合并为 \"98.2*\"**：Table tab:attention_pruning 中 Goal 行将三种 attention variant 合并为单一数值 \"98.2*\"（标注 \"Best of three attention variants\"），而其他三个 suite 分别报告了三种 variant 的结果。这种不一致可能暗示：(a) 三种 variant 在 Goal 上差异极小不值得展开，或 (b) 某些 variant 在 Goal 上表现较差被隐藏。如果是 (a)，应标注 \"all three variants ≥X%\"；如果三种 variant 结果一致，应和其他行一样展开。当前处理方式有 cherry-picking 嫌疑（Should-Fix）。\n\n**π₀.5 attention 结果（Table tab:pi05_attention_crosssuite）**：Attention 在 Object 上 catastrophic (-31.6pp vs random)，3/4 suite 中性。论文给出了机制解释（linear connector 的 attention score 范围极窄 [2×10⁻⁶, 3.6×10⁻³]，systematic position bias），但解释仅在附录中。主文 Section 4.4 对 π₀.5 attention 的讨论非常简略（\"attention is catastrophically harmful on Object (−30.4pp)\"），未解释为什么。\n\n**\"Architecture-dependent scoring\" 结论**：Table tab:scoring_crossover_summary 的 double dissociation 提供了清晰证据。这个发现比 Round 6 论文提供的任何 contribution 都更有 insight。\n\n### C. Importance margin 分析\n\n**评价：Adequate。** Importance margin Δ(k) 的 inverted-U 形状在 π₀.5 Long 上有 n=5 seed 验证（Table tab:pi05_long_multiseed），峰值在 k=0.9 (+46.9pp)，k≈0.71 处 cross zero。Figure fig_margin_profile 与文字描述一致。\n\n**局限**：inverted-U 仅在 π₀.5 Long 上有完整验证。Appendix 提到 OpenVLA 也有类似模式（L2 在 Object 上 leads at k=0.9 but staggered cliffs），但没有系统的 Δ(k) profile。π₀.5 Object 的 Δ(k) profile 也缺失（从 Table 数据可推断：k=0.95 Δ=+24.2, k=0.9 Δ=+89.2, k=0.5 Δ=−36.0，形状与 Long 类似但峰值更尖锐）。作为 observation 是 ok 的，但如果要作为 contribution 的一部分，需要更多 cross-model 验证。\n\n### D. π₀.5 Long multi-seed（n=5）\n\n**评价：Good。** Table tab:pi05_long_multiseed 的 s.d. 在 0.5–2.7pp 之间，对 500-episode 评估合理。关键 claims 正确标注了 n=5：\n- 主文 Table 2 caption：\"π₀.5 Long: five-seed mean (n=5)\" ✓\n- 主文 Section 4.1 Protocol：\"Multi-seed results (π₀.5 Long: n=5; VTR: n=3)\" ✓\n- Figure 5 caption：\"n=5, mean ± s.d.\" ✓\n\nMulti-seed validation 消除了 Round 6 中关于 π₀.5 Long random 非单调性是否为统计波动的质疑（Round 6 R2-Q1）。k=0.9 random 的 33.6±1.2% 和 k=0.7 的 64.6±1.8% 的非单调性在所有 5 个 seed 中一致复现，确认为 structural property。\n\n---\n\n## 叙事连贯性\n\n### E. Contributions 清晰度\n\n**C1**：\"A compressibility analysis across six VLA architectures...\"\n- 仍使用 \"identifying connector architecture as the primary determinant\"——这是 Round 6 R1-N2 指出的因果语言问题，Round 7 Limitations 虽然承认了 confounders 但 C1 的措辞没有软化。建议改为 \"associated with\" 或 \"the strongest predictor of\"。\n- \"six architectures\" 准确但有误导：只有 4 个 closed-loop，2 个仅 offline。\n\n**C2**：\"CV of token L2 norms as a single-pass diagnostic... validated on four closed-loop architectures\"\n- 相比 Round 6 的 \"enabling connector-appropriate compression strategy selection without downstream evaluation\"，claim 大幅收窄。这是正确方向。\n- \"validated on four\" 诚实但也暴露了 sample size 仍然有限。\n\n**C3** 将 zero-mask 发现和 VTR 绑在一起：\n- 逻辑连接是：\"pruning 失败有两种机制——position disruption (π₀.5) 和 spatial entanglement (SmolVLA)——C3 分别提供了诊断 (zero-mask) 和修复 (VTR)\"\n- 作为叙事是连贯的，但作为 contribution 有点 overloaded。Zero-mask 发现足以独立成 contribution。\n\n### F. 主表 vs 附录分配\n\n**问题：OpenVLA 移至附录造成主文叙事断裂。**\n\nTable 2（主文）仅包含 π₀.5, X-VLA, SmolVLA 三个模型。OpenVLA 是唯一的 high-CV independent connector 模型（CV=0.215），对验证 \"CV predicts compressibility\" 的连续谱至关重要。将其移至附录意味着：\n- 主文中 CV 连续谱 (0.055 → 0.151 → 0.314) 缺少 0.215 的 calibration 点\n- Section 4.2 对 OpenVLA 的讨论只有一句话，读者无法从主文判断 MLP connector 的行为\n- 论文声称 \"six architectures\" 但主表仅 3 个模型（50% 模型在附录中）\n\n建议：至少在 Table 2 中加入 OpenVLA Object 行（一行数据不影响页数）。\n\n### G. 页数合规\n\n**合规。** 正文 8 页（p1-p8），References 从 p9 开始，Appendix 从 p10 开始。正文包含 Limitations section（Section 6，含 AI disclosure）。\n\n排版检查：\n- 无明显字号压缩\n- Float spacing 正常\n- Table/Figure 大小合理\n- \\begin{itemize}[nosep] 用于 contributions list 是标准做法\n\n### H. Abstract 质量\n\n**仍然 number-dense。** 我数了约 16 个不同的数值（k=0.95, 98%, 0%, 0.038, 0.314, 450M-7B, 6/128, 93pp, 5%, 98%, 36pp, 20×, 10%, 98.0%, 9.0%, 89pp, ~5%, >60%, 75%）。Round 6 R3-W4 要求从 ~17 个减少到 ~5 个，当前版本几乎未减少。\n\n正面变化：Abstract 新增了 zero-mask 发现的描述（\"zeroing 10% of tokens preserves 98.0% SR while physical removal collapses to 9.0%\"），和 scoring reversal（\"random outperforms L2 by up to 36pp\"），这些是有价值的新信息。但整体信息密度仍然过高。\n\n---\n\n## 写作质量\n\n**术语一致性**：\n- \"VTR\" 在正文和附录中一致使用 ✓（Round 6 R3-N2 已修复）\n- \"importance margin\" 在 Section 3.2 有清晰定义（Δ(k) = SR_L2(k) − SR_Random(k)），后续使用一致 ✓\n- $\\pi_{0.5}$ 渲染已修复（不再是 $\\pi_0.5$）✓（Round 6 R3-W1 已修复）\n\n**AI 痕迹**：未发现典型 AI 生成短语（\"delve into\", \"it is worth noting\", \"in conclusion\"）。写作风格紧凑、技术化。\n\n**图表引用完整性**：所有 main text Figure (1, 2, 3, 4, 5) 和 Table (1, 2, 3) 均在正文中引用 ✓\n\n**代码/数据发布**：未提及代码发布计划（Round 6 R3-W3 未解决）。\n\n---\n\n## 新发现问题\n\n### Must-Fix\n\n**N1** [critical] **7+ concurrent works 从引用中被删除——相关工作覆盖严重退化**\n\n- 具体位置：Section 2 (Related Work), references.bib\n- 问题：Round 6 论文引用了所有 16 个 Director 指定的 concurrent work。Round 7 中以下引用被完全移除（.bib 中存在但正文无 \\cite{}）：\n  - **\"Don't Run with Scissors\" (Jabbour et al. 2025)** — 这是最关键的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method。我在 Round 6 R2-W2 中明确要求**增加**讨论，而非删除引用。\n  - **SpecPrune-VLA** — 2025 VLA pruning 方法\n  - **\"See What Matters\" (ICML 2026)** — ICML 2026 VLA pruning concurrent work\n  - **SparseVLM, SparseVILA** — VLM token sparsification\n  - **FitPrune, CrossGET** — VLM/ViT token pruning\n- 为什么影响接收：删除 7+ concurrent work 的引用在 blind review 中是危险操作。如果有 reviewer 了解这些工作（尤其是 \"Don't Run with Scissors\"），论文会被视为故意回避比较。CoRL reviewers 期望 thorough related work coverage。\n- 建议：立即恢复所有被删除的引用。\"Don't Run with Scissors\" 需要专门段落对比差异。\n\n### Should-Fix\n\n**W1** [warning] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 \"98.2*\"**\n- Table 中 Object/Spatial/Long 都分别列出了 attn_last/attn_mean/attn_rollout，但 Goal 合并为单一值 \"98.2*\" (best of three variants)。\n- 这种不一致暗示数据选择性报告。应展开为三列或标注 \"all three ≥X%\"。\n\n**W2** [warning] **C1 仍使用因果语言 \"primary determinant\"**\n- Introduction line 18 和 Conclusion 都写 \"identifying the vision-language connector as the primary determinant of pruning robustness\"\n- Round 6 R1-N2 已指出无法做因果推断（confounders）。Round 7 Limitations 承认了这一问题但 C1 措辞未修改。\n- 建议：\"the strongest predictor of\" 或 \"the primary architectural factor associated with\"\n\n**W3** [warning] **OpenVLA 附录 full results 仍有大量 \"--\" 缺失数据**\n- Appendix Table tab:full_results 中 OpenVLA 的 Goal/Spatial/Long 在 k=0.95, 0.7, 0.5 均为 \"--\"。仅有 k=0.9 的数据（含 attention）。\n- 主文 Table 2 现已完整（GOOD），但 Appendix 承诺 \"Full results including OpenVLA\" 却数据不全。\n- 建议：要么补全，要么将 table caption 改为 \"available results\" 而非 \"full results\"。\n\n**W4** [warning] **Appendix full_results table 中 X-VLA 仍有 \"--\"**\n- X-VLA k=0.7 Spatial 和 Long 仍为 \"--\"。主文 Table 2 省略了 k=0.7（只报告 k=0.95, 0.9, 0.5），但 Appendix 表格标题暗示 \"complete\" results。\n\n### Info\n\n**I1** Zero-mask ablation 的声明 \"entirely attributable to position disruption\" 应限定为 \"on π₀.5\"，因为机制与 RoPE 高度相关，不一定 generalize 到所有 VLA 架构。\n\n**I2** Abstract 数字密度仍高（~16 个数值），Round 6 R3-W4 未充分回应。\n\n**I3** 代码/数据发布计划仍缺失（Round 6 R3-W3 未回应）。\n\n---\n\n## Round 6 问题修复状态\n\n| Round 6 问题 | 状态 | 说明 |\n|---|---|---|\n| R2-N1: CV diagnostic N=3 数据点 | ⚠️ 部分改善 | Claim 收窄为 \"validated on four\"，但 sample size 未增加 |\n| R2-N2: 论文 identity 分裂 | ✅ 改善 | Zero-mask + attention scoring 使三个 contribution 各有实质内容 |\n| R2-N3: Table 2 数据缺失 | ✅ 修复 | 主文 Table 2 现已完整 |\n| R2-W1: VTR 被 MLP 平替 | ⚠️ 未变 | p=0.15 事实不变，但论文现在诚实表述为 \"re-encoding, not cross-attention\" |\n| R2-W2: \"Don't Run with Scissors\" 讨论不足 | ❌ 退化 | 引用被完全删除！ |\n| R2-W3: Two-axis framework 可能是 re-packaging | ⚠️ 部分改善 | 新增 attention scoring + zero-mask 使分析更有深度 |\n| R2-W4: 仅 LIBERO simulation | ⚠️ 未变 | Limitations 承认但无行动 |\n| R2-W5: OpenVLA 仅 Object suite | ✅ 改善 | OpenVLA 现有全 4 suite 数据（Appendix Table tab:full_results k=0.9） |\n| R3-N1: AI disclosure | ✅ 修复 | Limitations 末尾包含 AI disclosure |\n| R3-N2: VTR/Smart Compress 命名 | ✅ 修复 | 全文统一为 VTR |\n| R3-W1: π₀.5 渲染错误 | ✅ 修复 | 现为 $\\pi_{0.5}$ |\n| R3-W2: Limitations 过短 | ✅ 修复 | 现为 7 句话 + AI disclosure + extended discussion in Appendix |\n| R3-W3: 代码发布计划 | ❌ 未回应 | |\n| R3-W4: Abstract 数字密度 | ⚠️ 微改 | 新增内容使 Abstract 更丰富但数字未减少 |\n\n---\n\n## 主要优势（Round 7 新增或增强）\n\n- **S1-NEW**: Zero-mask ablation 提供了 position disruption vs. information loss 的清晰分离，是论文最 elegant 的实验设计。\n- **S2-NEW**: Attention scoring double dissociation（Table tab:scoring_crossover_summary）是论文最有 insight 的发现：connector type 决定了哪种 scoring method 有效，没有 universal winner。\n- **S3-IMPROVED**: Table 2 主文现已完整，不再有 \"--\" 缺失数据。\n- **S4-IMPROVED**: Multi-seed validation (n=5) 消除了关键数据点的统计疑虑。\n- **S5-IMPROVED**: Limitations section 诚实且全面，CV diagnostic claim 适当收窄。\n- **S6-IMPROVED**: 论文 identity 更清晰——empirical study 定位明确，不再过度 claim methodological contribution。\n\n---\n\n## 评分建议\n\n**Round 7 建议评分：6/10（Borderline Accept）**\n\n**从 5/10 → 6/10 的理由**：\n- Zero-mask ablation 和 attention scoring double dissociation 是两个 genuine insights，使论文从 \"观察到 connector 影响 pruning\" 提升为 \"理解了 why 和 how\"\n- Table 2 完整化和 multi-seed validation 大幅提高了实验可信度\n- Limitations section 和 CV claim 的收窄表明了学术诚实\n\n**未达 7/10 的理由**：\n- 7+ concurrent works 被删除是 unacceptable regression——必须在提交前修复\n- 仍然 simulation-only，对 CoRL community 的 practical impact 有限\n- CV diagnostic 仍然只有 4 个 closed-loop 模型的 validation\n- VTR 仍然只在 SmolVLA 上验证，MLP adapter 平替问题未解决\n- OpenVLA 移至附录使主文叙事不完整\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 7 审稿报告\n\n**角色**：新颖性 / 相关工作 / 论文定位（延续 Round 6 职责）+ 新增内容质量 + 叙事连贯性\n**Round 6 评分**：5/10 (Weak Reject)\n\n---\n\n## 新增内容质量\n\n### A. Zero-mask ablation（Section 4.3）\n\n**评价：Strong addition。** 实验设计清晰地分离了两个因素：信息丢失 vs. 位置扰动。Zero-masking 将 10% token 的 embedding 置零（100% 信息损失，0% 位置变化）保留 98.0% SR；hard pruning 移除相同 token 并 re-index（部分信息损失 + 位置变化）崩溃到 9.0%。89pp 的差距归因于位置扰动而非信息丢失，这一结论在实验设计上是 justified 的——如果信息丢失是主因，zero-masking 应该比 hard pruning 更差（信息丢失更严重），但实际结果相反。\n\n**局限性**：仅在 π₀.5 Object k=0.9 一个条件上验证。该发现与 RoPE positional encoding 高度相关（论文在 Appendix 中承认了这一点），因此可能不 generalize 到非 RoPE 架构（如 X-VLA 的 BART encoder 使用 learned positional embeddings）。Section 4.3 的声明 \"entirely attributable to position disruption\" 应加限定语 \"on π₀.5\"。不过作为 diagnostic finding 而非 general claim，在单个模型上的验证已足够。\n\n### B. Attention-based scoring（Section 4.4 + Appendix）\n\n**评价：Substantial improvement。** 这是 Round 6 R1-N3（缺少 attention baseline）的直接回应。\n\n**X-VLA 结果（Table tab:attention_pruning）**：Attention scoring 在 k=0.5 恢复 ≥92.8% SR（所有 suite），而 L2 在所有 suite 上低于 random（-8.2 到 -27.2pp）。这个 double dissociation 是论文最强的新发现之一：L2 对 independent connectors 有效，attention 对 entangling connectors 有效，且两者不可互换。\n\n**问题：X-VLA Goal 合并为 \"98.2*\"**：Table tab:attention_pruning 中 Goal 行将三种 attention variant 合并为单一数值 \"98.2*\"（标注 \"Best of three attention variants\"），而其他三个 suite 分别报告了三种 variant 的结果。这种不一致可能暗示：(a) 三种 variant 在 Goal 上差异极小不值得展开，或 (b) 某些 variant 在 Goal 上表现较差被隐藏。如果是 (a)，应标注 \"all three variants ≥X%\"；如果三种 variant 结果一致，应和其他行一样展开。当前处理方式有 cherry-picking 嫌疑（Should-Fix）。\n\n**π₀.5 attention 结果（Table tab:pi05_attention_crosssuite）**：Attention 在 Object 上 catastrophic (-31.6pp vs random)，3/4 suite 中性。论文给出了机制解释（linear connector 的 attention score 范围极窄 [2×10⁻⁶, 3.6×10⁻³]，systematic position bias），但解释仅在附录中。主文 Section 4.4 对 π₀.5 attention 的讨论非常简略（\"attention is catastrophically harmful on Object (−30.4pp)\"），未解释为什么。\n\n**\"Architecture-dependent scoring\" 结论**：Table tab:scoring_crossover_summary 的 double dissociation 提供了清晰证据。这个发现比 Round 6 论文提供的任何 contribution 都更有 insight。\n\n### C. Importance margin 分析\n\n**评价：Adequate。** Importance margin Δ(k) 的 inverted-U 形状在 π₀.5 Long 上有 n=5 seed 验证（Table tab:pi05_long_multiseed），峰值在 k=0.9 (+46.9pp)，k≈0.71 处 cross zero。Figure fig_margin_profile 与文字描述一致。\n\n**局限**：inverted-U 仅在 π₀.5 Long 上有完整验证。Appendix 提到 OpenVLA 也有类似模式（L2 在 Object 上 leads at k=0.9 but staggered cliffs），但没有系统的 Δ(k) profile。π₀.5 Object 的 Δ(k) profile 也缺失（从 Table 数据可推断：k=0.95 Δ=+24.2, k=0.9 Δ=+89.2, k=0.5 Δ=−36.0，形状与 Long 类似但峰值更尖锐）。作为 observation 是 ok 的，但如果要作为 contribution 的一部分，需要更多 cross-model 验证。\n\n### D. π₀.5 Long multi-seed（n=5）\n\n**评价：Good。** Table tab:pi05_long_multiseed 的 s.d. 在 0.5–2.7pp 之间，对 500-episode 评估合理。关键 claims 正确标注了 n=5：\n- 主文 Table 2 caption：\"π₀.5 Long: five-seed mean (n=5)\" ✓\n- 主文 Section 4.1 Protocol：\"Multi-seed results (π₀.5 Long: n=5; VTR: n=3)\" ✓\n- Figure 5 caption：\"n=5, mean ± s.d.\" ✓\n\nMulti-seed validation 消除了 Round 6 中关于 π₀.5 Long random 非单调性是否为统计波动的质疑（Round 6 R2-Q1）。k=0.9 random 的 33.6±1.2% 和 k=0.7 的 64.6±1.8% 的非单调性在所有 5 个 seed 中一致复现，确认为 structural property。\n\n---\n\n## 叙事连贯性\n\n### E. Contributions 清晰度\n\n**C1**：\"A compressibility analysis across six VLA architectures...\"\n- 仍使用 \"identifying connector architecture as the primary determinant\"——这是 Round 6 R1-N2 指出的因果语言问题，Round 7 Limitations 虽然承认了 confounders 但 C1 的措辞没有软化。建议改为 \"associated with\" 或 \"the strongest predictor of\"。\n- \"six architectures\" 准确但有误导：只有 4 个 closed-loop，2 个仅 offline。\n\n**C2**：\"CV of token L2 norms as a single-pass diagnostic... validated on four closed-loop architectures\"\n- 相比 Round 6 的 \"enabling connector-appropriate compression strategy selection without downstream evaluation\"，claim 大幅收窄。这是正确方向。\n- \"validated on four\" 诚实但也暴露了 sample size 仍然有限。\n\n**C3** 将 zero-mask 发现和 VTR 绑在一起：\n- 逻辑连接是：\"pruning 失败有两种机制——position disruption (π₀.5) 和 spatial entanglement (SmolVLA)——C3 分别提供了诊断 (zero-mask) 和修复 (VTR)\"\n- 作为叙事是连贯的，但作为 contribution 有点 overloaded。Zero-mask 发现足以独立成 contribution。\n\n### F. 主表 vs 附录分配\n\n**问题：OpenVLA 移至附录造成主文叙事断裂。**\n\nTable 2（主文）仅包含 π₀.5, X-VLA, SmolVLA 三个模型。OpenVLA 是唯一的 high-CV independent connector 模型（CV=0.215），对验证 \"CV predicts compressibility\" 的连续谱至关重要。将其移至附录意味着：\n- 主文中 CV 连续谱 (0.055 → 0.151 → 0.314) 缺少 0.215 的 calibration 点\n- Section 4.2 对 OpenVLA 的讨论只有一句话，读者无法从主文判断 MLP connector 的行为\n- 论文声称 \"six architectures\" 但主表仅 3 个模型（50% 模型在附录中）\n\n建议：至少在 Table 2 中加入 OpenVLA Object 行（一行数据不影响页数）。\n\n### G. 页数合规\n\n**合规。** 正文 8 页（p1-p8），References 从 p9 开始，Appendix 从 p10 开始。正文包含 Limitations section（Section 6，含 AI disclosure）。\n\n排版检查：\n- 无明显字号压缩\n- Float spacing 正常\n- Table/Figure 大小合理\n- \\begin{itemize}[nosep] 用于 contributions list 是标准做法\n\n### H. Abstract 质量\n\n**仍然 number-dense。** 我数了约 16 个不同的数值（k=0.95, 98%, 0%, 0.038, 0.314, 450M-7B, 6/128, 93pp, 5%, 98%, 36pp, 20×, 10%, 98.0%, 9.0%, 89pp, ~5%, >60%, 75%）。Round 6 R3-W4 要求从 ~17 个减少到 ~5 个，当前版本几乎未减少。\n\n正面变化：Abstract 新增了 zero-mask 发现的描述（\"zeroing 10% of tokens preserves 98.0% SR while physical removal collapses to 9.0%\"），和 scoring reversal（\"random outperforms L2 by up to 36pp\"），这些是有价值的新信息。但整体信息密度仍然过高。\n\n---\n\n## 写作质量\n\n**术语一致性**：\n- \"VTR\" 在正文和附录中一致使用 ✓（Round 6 R3-N2 已修复）\n- \"importance margin\" 在 Section 3.2 有清晰定义（Δ(k) = SR_L2(k) − SR_Random(k)），后续使用一致 ✓\n- $\\pi_{0.5}$ 渲染已修复（不再是 $\\pi_0.5$）✓（Round 6 R3-W1 已修复）\n\n**AI 痕迹**：未发现典型 AI 生成短语（\"delve into\", \"it is worth noting\", \"in conclusion\"）。写作风格紧凑、技术化。\n\n**图表引用完整性**：所有 main text Figure (1, 2, 3, 4, 5) 和 Table (1, 2, 3) 均在正文中引用 ✓\n\n**代码/数据发布**：未提及代码发布计划（Round 6 R3-W3 未解决）。\n\n---\n\n## 新发现问题\n\n### Must-Fix\n\n**N1** [critical] **7+ concurrent works 从引用中被删除——相关工作覆盖严重退化**\n\n- 具体位置：Section 2 (Related Work), references.bib\n- 问题：Round 6 论文引用了所有 16 个 Director 指定的 concurrent work。Round 7 中以下引用被完全移除（.bib 中存在但正文无 \\cite{}）：\n  - **\"Don't Run with Scissors\" (Jabbour et al. 2025)** — 这是最关键的 concurrent work，也发现 pruning breaks VLA 并提出 recovery method。我在 Round 6 R2-W2 中明确要求**增加**讨论，而非删除引用。\n  - **SpecPrune-VLA** — 2025 VLA pruning 方法\n  - **\"See What Matters\" (ICML 2026)** — ICML 2026 VLA pruning concurrent work\n  - **SparseVLM, SparseVILA** — VLM token sparsification\n  - **FitPrune, CrossGET** — VLM/ViT token pruning\n- 为什么影响接收：删除 7+ concurrent work 的引用在 blind review 中是危险操作。如果有 reviewer 了解这些工作（尤其是 \"Don't Run with Scissors\"），论文会被视为故意回避比较。CoRL reviewers 期望 thorough related work coverage。\n- 建议：立即恢复所有被删除的引用。\"Don't Run with Scissors\" 需要专门段落对比差异。\n\n### Should-Fix\n\n**W1** [warning] **X-VLA Goal attention 结果在 Table tab:attention_pruning 中合并为 \"98.2*\"**\n- Table 中 Object/Spatial/Long 都分别列出了 attn_last/attn_mean/attn_rollout，但 Goal 合并为单一值 \"98.2*\" (best of three variants)。\n- 这种不一致暗示数据选择性报告。应展开为三列或标注 \"all three ≥X%\"。\n\n**W2** [warning] **C1 仍使用因果语言 \"primary determinant\"**\n- Introduction line 18 和 Conclusion 都写 \"identifying the vision-language connector as the primary determinant of pruning robustness\"\n- Round 6 R1-N2 已指出无法做因果推断（confounders）。Round 7 Limitations 承认了这一问题但 C1 措辞未修改。\n- 建议：\"the strongest predictor of\" 或 \"the primary architectural factor associated with\"\n\n**W3** [warning] **OpenVLA 附录 full results 仍有大量 \"--\" 缺失数据**\n- Appendix Table tab:full_results 中 OpenVLA 的 Goal/Spatial/Long 在 k=0.95, 0.7, 0.5 均为 \"--\"。仅有 k=0.9 的数据（含 attention）。\n- 主文 Table 2 现已完整（GOOD），但 Appendix 承诺 \"Full results including OpenVLA\" 却数据不全。\n- 建议：要么补全，要么将 table caption 改为 \"available results\" 而非 \"full results\"。\n\n**W4** [warning] **Appendix full_results table 中 X-VLA 仍有 \"--\"**\n- X-VLA k=0.7 Spatial 和 Long 仍为 \"--\"。主文 Table 2 省略了 k=0.7（只报告 k=0.95, 0.9, 0.5），但 Appendix 表格标题暗示 \"complete\" results。\n\n### Info\n\n**I1** Zero-mask ablation 的声明 \"entirely attributable to position disruption\" 应限定为 \"on π₀.5\"，因为机制与 RoPE 高度相关，不一定 generalize 到所有 VLA 架构。\n\n**I2** Abstract 数字密度仍高（~16 个数值），Round 6 R3-W4 未充分回应。\n\n**I3** 代码/数据发布计划仍缺失（Round 6 R3-W3 未回应）。\n\n---\n\n## Round 6 问题修复状态\n\n| Round 6 问题 | 状态 | 说明 |\n|---|---|---|\n| R2-N1: CV diagnostic N=3 数据点 | ⚠️ 部分改善 | Claim 收窄为 \"validated on four\"，但 sample size 未增加 |\n| R2-N2: 论文 identity 分裂 | ✅ 改善 | Zero-mask + attention scoring 使三个 contribution 各有实质内容 |\n| R2-N3: Table 2 数据缺失 | ✅ 修复 | 主文 Table 2 现已完整 |\n| R2-W1: VTR 被 MLP 平替 | ⚠️ 未变 | p=0.15 事实不变，但论文现在诚实表述为 \"re-encoding, not cross-attention\" |\n| R2-W2: \"Don't Run with Scissors\" 讨论不足 | ❌ 退化 | 引用被完全删除！ |\n| R2-W3: Two-axis framework 可能是 re-packaging | ⚠️ 部分改善 | 新增 attention scoring + zero-mask 使分析更有深度 |\n| R2-W4: 仅 LIBERO simulation | ⚠️ 未变 | Limitations 承认但无行动 |\n| R2-W5: OpenVLA 仅 Object suite | ✅ 改善 | OpenVLA 现有全 4 suite 数据（Appendix Table tab:full_results k=0.9） |\n| R3-N1: AI disclosure | ✅ 修复 | Limitations 末尾包含 AI disclosure |\n| R3-N2: VTR/Smart Compress 命名 | ✅ 修复 | 全文统一为 VTR |\n| R3-W1: π₀.5 渲染错误 | ✅ 修复 | 现为 $\\pi_{0.5}$ |\n| R3-W2: Limitations 过短 | ✅ 修复 | 现为 7 句话 + AI disclosure + extended discussion in Appendix |\n| R3-W3: 代码发布计划 | ❌ 未回应 | |\n| R3-W4: Abstract 数字密度 | ⚠️ 微改 | 新增内容使 Abstract 更丰富但数字未减少 |\n\n---\n\n## 主要优势（Round 7 新增或增强）\n\n- **S1-NEW**: Zero-mask ablation 提供了 position disruption vs. information loss 的清晰分离，是论文最 elegant 的实验设计。\n- **S2-NEW**: Attention scoring double dissociation（Table tab:scoring_crossover_summary）是论文最有 insight 的发现：connector type 决定了哪种 scoring method 有效，没有 universal winner。\n- **S3-IMPROVED**: Table 2 主文现已完整，不再有 \"--\" 缺失数据。\n- **S4-IMPROVED**: Multi-seed validation (n=5) 消除了关键数据点的统计疑虑。\n- **S5-IMPROVED**: Limitations section 诚实且全面，CV diagnostic claim 适当收窄。\n- **S6-IMPROVED**: 论文 identity 更清晰——empirical study 定位明确，不再过度 claim methodological contribution。\n\n---\n\n## 评分建议\n\n**Round 7 建议评分：6/10（Borderline Accept）**\n\n**从 5/10 → 6/10 的理由**：\n- Zero-mask ablation 和 attention scoring double dissociation 是两个 genuine insights，使论文从 \"观察到 connector 影响 pruning\" 提升为 \"理解了 why 和 how\"\n- Table 2 完整化和 multi-seed validation 大幅提高了实验可信度\n- Limitations section 和 CV claim 的收窄表明了学术诚实\n\n**未达 7/10 的理由**：\n- 7+ concurrent works 被删除是 unacceptable regression——必须在提交前修复\n- 仍然 simulation-only，对 CoRL community 的 practical impact 有限\n- CV diagnostic 仍然只有 4 个 closed-loop 模型的 validation\n- VTR 仍然只在 SmolVLA 上验证，MLP adapter 平替问题未解决\n- OpenVLA 移至附录使主文叙事不完整\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-29T00:49:44.512630+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5873
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-29T00:49:49.587995+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-29T00:49:49.774366+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 186
}
```

</details>

---


### Assistant

_source line 632 · 2026-05-29T00:49:56.338589+00:00_

Round 7 审稿报告已提交。

核心结论：论文从 5/10 提升至 6/10。Zero-mask ablation 和 attention scoring double dissociation 是两个实质性新贡献，Table 2 完整化和 multi-seed 验证大幅提高可信度。但发现一个严重退化——7+ concurrent works（包括 "Don't Run with Scissors"）被从引用中删除，这是 Must-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 633 · 2026-05-29T00:50:58.980048+00:00_

[Round 7 审稿请求]:
## Round 7 交叉分享 — Reviewer 2 请回应 Reviewer 1 的发现

以下是 Reviewer 1 的完整审稿意见。请逐条回应关键发现，标注 [AGREE] 或 [REBUT] + 理由。

---

### Reviewer 1 核心发现

**R6-C1: [STILL_OPEN] — CV diagnostic N 扩展未完成**
Table 1 仍为 6 个模型（4 closed-loop + 2 offline），未新增任何 VLA 架构。Reviewer 1 将严重程度从 critical 降级为 major weakness，因为措辞已收窄（"validated on four closed-loop architectures"）且 Limitations 承认了局限。
你是否同意降级？还是认为应保持 critical？

**R6-C2: [PARTIALLY_RESOLVED] — Table 2 主表改善，附录仍有 ~14% "--"**
主表 3 个模型完整无 "--"。Appendix Table 4 仍有约 23/160 个 "--"（集中在 OpenVLA k=0.95/0.7/0.5）。Reviewer 1 将此降级为 minor。
你是否同意？你的 W3/W4 发现与此相关——附录 caption 说 "Full results" 但数据不全。

**R6-C4: [RESOLVED] — Attention baseline 已添加**
覆盖 3 个 closed-loop 模型（X-VLA/π₀.5/OpenVLA），主文 Section 4.5 + 附录 Table 8。
你同意 RESOLVED 吗？

**R6-W5: [RESOLVED] — OpenVLA multi-suite 数据已添加**
Appendix Table 4 含 4 suite 完整 k=0.9 数据 + Figure 6 跨 suite 比较图。
你同意 RESOLVED 吗？

**R6-C3: [REGRESSION] — 因果语言未修正**
- abstract.tex: "primary architectural factor"
- introduction.tex ×2: "primary determinant of pruning robustness"
- conclusion.tex: "primary factor governing"
你已独立发现（W2）。是否有补充意见？

**[SmolVLA k=0.95 残余值]**
Reviewer 1 未专门提及，但 Table 2 SmolVLA k=0.95 现在显示 Spatial 6.6/4.2, Goal 3.4/4.2（非全 0.0%）。你认为这些非零残余值是改善还是可能的实验噪声？

**[新增 minor: Abstract 使用 π₀ (offline-only) 的 CV=0.038 作为 spectrum 下界]**
Reviewer 1 指出 Abstract 未标注 π₀ 是 offline-only 模型。你同意这是问题吗？

### 输出格式
```
## 交叉回应

### R6-C1 降级为 major: [AGREE / REBUT]
理由：...

### R6-C2 降级为 minor: [AGREE / REBUT]
理由：...

### R6-C4 RESOLVED: [AGREE / REBUT]
理由：...

### R6-W5 RESOLVED: [AGREE / REBUT]
理由：...

### R6-C3 REGRESSION: [AGREE / REBUT]
理由：...

### SmolVLA 残余值: 评价
...

### π₀ offline 标注: [AGREE / REBUT]
理由：...

### 是否调整评分？
原评分：6/10
调整后：X/10
理由：...
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-29T00:52:16.052553+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 — 回应 Reviewer 1 Round 7 发现\n\n---\n\n## 交叉回应\n\n### R6-C1 降级为 major: [AGREE]\n\n同意降级。理由：\n\n1. **措辞收窄是实质性改善**。Round 6 C2 声称 \"enabling connector-appropriate compression strategy selection without downstream evaluation\"——这是一个 general diagnostic tool 的 claim，N=4 完全不够。Round 7 改为 \"validated on four closed-loop architectures\"——这是一个 observation scope 的描述，N=4 是事实而非 overclaim。\n2. **Limitations 明确承认了局限**（Section 6: \"The CV–SR correlation relies on four closed-loop models, too few for a general law\"）。自我限定比外部质疑的杀伤力小得多。\n3. **统计上 N=4 仍无法做 formal validation**（Spearman N=4 最小 p≈0.083），但论文不再 claim formal validation——它 claim observation + directional consistency，这在 empirical study 中是可接受的。\n\n保留为 major weakness 而非 minor 的理由：即使措辞收窄，CV diagnostic 仍是论文三个 contribution 之一（C2）。一个只在 4 个模型上 \"validated\" 的 diagnostic 作为 CoRL contribution，其 significance 仍然有限。如果降为 observation/analysis tool 而非 contribution，可以进一步降级为 minor。\n\n### R6-C2 降级为 minor: [AGREE]\n\n同意。主文 Table 2 是读者的 primary reference，现已完整——这是 Round 6 三位 reviewer 的共识 Must-Fix，已修复。附录 \"--\" 集中在 OpenVLA 的非 k=0.9 retention ratios，不影响核心 claims。\n\n补充我的 W3/W4：附录 Table caption 仍写 \"Full closed-loop success rates\"（Appendix Table 4），但 OpenVLA 在 k=0.95/0.7/0.5 以及 X-VLA k=0.7 Long/Spatial 仍为 \"--\"。建议将 caption 改为 \"Available closed-loop success rates\" 或在脚注说明 \"OpenVLA conditions beyond k=0.9 are pending\"。这是 editorial fix，不影响评分。\n\n### R6-C4 RESOLVED: [AGREE]\n\n同意。Attention-based scoring 是 Round 6 R1-N3 的直接回应，覆盖了三个 closed-loop 模型：\n- X-VLA: 三种 attention variant（last/mean/rollout）在 k=0.5 四个 suite 上（Table tab:attention_pruning）\n- π₀.5: attention vs random 在 k=0.5 四个 suite 上（Table tab:pi05_attention_crosssuite）\n- OpenVLA: attention 在 k=0.9 四个 suite 上（Appendix Table 4 脚注 †）\n\n关键发现——attention 对 entangling connectors 有效但对 independent connectors 无效（甚至 harmful），L2 反之——是论文 Round 7 最有价值的新贡献之一。完全同意 RESOLVED。\n\n我保留一个 minor concern：X-VLA Goal 在 Table tab:attention_pruning 中合并为 \"98.2*\"（best of three variants），未展开三种 variant 的具体数值。其他三个 suite 都分别列出了三种 variant，Goal 的合并处理不一致。但这不影响 RESOLVED 判定。\n\n### R6-W5 RESOLVED: [AGREE]\n\n同意。OpenVLA 现有全 4 suite k=0.9 数据（Appendix Table 4），包括 L2/Random/Attention 三种 scoring。Figure fig_openvla_sweep 提供了跨 suite 比较的可视化。这满足了 Round 6 R2-W5 \"补全 OpenVLA Spatial/Goal/Long 数据\" 的要求。\n\n唯一保留意见：OpenVLA 仍不在主文 Table 2 中，我认为至少 Object 行应在主文出现（我的 review 中 F 部分已提出）。但这是叙事选择而非数据完整性问题。\n\n### R6-C3 REGRESSION: [AGREE]\n\n完全同意，且我独立发现了同一问题（我的 W2）。\n\n补充具体位置：\n- Introduction line 18: \"identifying the vision-language connector as **the primary determinant** of pruning robustness\"\n- Introduction C1: \"identifying connector architecture as **the primary determinant** of pruning robustness\"\n- Conclusion: \"Connector architecture is **the primary factor governing** VLA token compressibility\"\n- Abstract: \"the vision-language connector as **the primary architectural factor** governing pruning tolerance\"\n\n四处使用了因果性语言。Limitations Section 6 承认 \"preventing full causal isolation of the connector effect\"，与正文的因果 claim 直接矛盾。\n\n建议统一修改为 \"the strongest predictor of\" 或 \"the primary architectural correlate of\"。这是文字替换，不需要新实验。\n\n### SmolVLA 残余值: 评价\n\nSmolVLA k=0.95 的非零值（Spatial 6.6/4.2, Goal 3.4/4.2）**更可能是 genuine 但接近 noise floor 的真实信号，而非实验噪声**。理由：\n\n1. **模式一致**：非零值只出现在 k=0.95（最温和的 pruning），k=0.9 及以下全为 0.0%。如果是纯噪声，应在各 retention ratio 随机出现。\n2. **数值与 Wilson CI 一致**：6.6% 在 500 episodes 中对应 33/500 成功，Wilson 95% CI ≈ [4.7%, 9.2%]，与 0% 基线有统计学差异。\n3. **Suite 差异合理**：Object 和 Long 仍为 0.0%，而 Spatial 和 Goal 有残余——Spatial/Goal 的部分 task 可能对少量 token 丢失有更高容忍度（某些 task 可能不依赖被移除的特定空间区域）。\n\n**影响**：这使论文的核心 narrative 更精确——从 \"SmolVLA 在任何 pruning 下 catastrophic collapse 到 0%\" 变为 \"SmolVLA 在 k≤0.9 下 collapse 到 0%，k=0.95 下有 ≤6.6% 的残余\"。论文已适当更新措辞为 \"≤6.6%\"（Introduction）和 \"collapses to near-zero\" 而非 \"0.0%\"。这是一个改善——更诚实的数据报告。\n\n### π₀ offline 标注: [AGREE]\n\n同意这是问题。Abstract 写 \"The coefficient of variation (CV) of post-connector token norms captures this on a continuous spectrum (0.038 to 0.314)\"。0.038 来自 π₀，一个仅有 offline evaluation 的模型——没有 closed-loop SR 数据来验证其 pruning tolerance。将 offline-only 模型的 CV 作为 spectrum 下界，在 Abstract 中不加标注，会让读者认为 0.038 也有 closed-loop 验证。\n\n建议：将 Abstract 中的 spectrum 范围改为 closed-loop 模型的范围（0.055 到 0.314），或标注 \"0.038 [offline] to 0.314\"。考虑到 0.055 和 0.038 差异很小，使用 closed-loop 范围 (0.055–0.314) 更干净且不损失 narrative impact。\n\n### 是否调整评分？\n\n**原评分：6/10**\n**调整后：6/10（维持不变）**\n\n理由：Reviewer 1 的发现与我的独立评估高度一致。交叉审查没有揭示我遗漏的重大问题，也没有发现我过度严厉的地方。关键共识点：\n\n- Table 2 完整化 + attention baseline + multi-seed = 实质性改善 → 从 5 到 6 ✓\n- 因果语言未修正 = persistent but fixable weakness → 不影响评分\n- CV diagnostic N=4 = major but appropriately scoped weakness → 不影响评分\n- 我独立发现的 7+ concurrent works 被删除（N1 Must-Fix）是唯一可能影响评分的新问题，但因为这是 fixable editorial issue（恢复引用即可），我暂不因此降分。如果最终提交仍缺少这些引用，我会降至 5/10。\n\n6/10 = Borderline Accept，含义是：论文有 genuine insights（zero-mask, scoring double dissociation）但 evidence base 仍偏薄（4 models, 1 benchmark, simulation-only），且有 fixable-but-unacceptable editorial issues（missing citations, causal language）。\n",
  "reviewer_id": "2",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应 — 回应 Reviewer 1 Round 7 发现\n\n---\n\n## 交叉回应\n\n### R6-C1 降级为 major: [AGREE]\n\n同意降级。理由：\n\n1. **措辞收窄是实质性改善**。Round 6 C2 声称 \"enabling connector-appropriate compression strategy selection without downstream evaluation\"——这是一个 general diagnostic tool 的 claim，N=4 完全不够。Round 7 改为 \"validated on four closed-loop architectures\"——这是一个 observation scope 的描述，N=4 是事实而非 overclaim。\n2. **Limitations 明确承认了局限**（Section 6: \"The CV–SR correlation relies on four closed-loop models, too few for a general law\"）。自我限定比外部质疑的杀伤力小得多。\n3. **统计上 N=4 仍无法做 formal validation**（Spearman N=4 最小 p≈0.083），但论文不再 claim formal validation——它 claim observation + directional consistency，这在 empirical study 中是可接受的。\n\n保留为 major weakness 而非 minor 的理由：即使措辞收窄，CV diagnostic 仍是论文三个 contribution 之一（C2）。一个只在 4 个模型上 \"validated\" 的 diagnostic 作为 CoRL contribution，其 significance 仍然有限。如果降为 observation/analysis tool 而非 contribution，可以进一步降级为 minor。\n\n### R6-C2 降级为 minor: [AGREE]\n\n同意。主文 Table 2 是读者的 primary reference，现已完整——这是 Round 6 三位 reviewer 的共识 Must-Fix，已修复。附录 \"--\" 集中在 OpenVLA 的非 k=0.9 retention ratios，不影响核心 claims。\n\n补充我的 W3/W4：附录 Table caption 仍写 \"Full closed-loop success rates\"（Appendix Table 4），但 OpenVLA 在 k=0.95/0.7/0.5 以及 X-VLA k=0.7 Long/Spatial 仍为 \"--\"。建议将 caption 改为 \"Available closed-loop success rates\" 或在脚注说明 \"OpenVLA conditions beyond k=0.9 are pending\"。这是 editorial fix，不影响评分。\n\n### R6-C4 RESOLVED: [AGREE]\n\n同意。Attention-based scoring 是 Round 6 R1-N3 的直接回应，覆盖了三个 closed-loop 模型：\n- X-VLA: 三种 attention variant（last/mean/rollout）在 k=0.5 四个 suite 上（Table tab:attention_pruning）\n- π₀.5: attention vs random 在 k=0.5 四个 suite 上（Table tab:pi05_attention_crosssuite）\n- OpenVLA: attention 在 k=0.9 四个 suite 上（Appendix Table 4 脚注 †）\n\n关键发现——attention 对 entangling connectors 有效但对 independent connectors 无效（甚至 harmful），L2 反之——是论文 Round 7 最有价值的新贡献之一。完全同意 RESOLVED。\n\n我保留一个 minor concern：X-VLA Goal 在 Table tab:attention_pruning 中合并为 \"98.2*\"（best of three variants），未展开三种 variant 的具体数值。其他三个 suite 都分别列出了三种 variant，Goal 的合并处理不一致。但这不影响 RESOLVED 判定。\n\n### R6-W5 RESOLVED: [AGREE]\n\n同意。OpenVLA 现有全 4 suite k=0.9 数据（Appendix Table 4），包括 L2/Random/Attention 三种 scoring。Figure fig_openvla_sweep 提供了跨 suite 比较的可视化。这满足了 Round 6 R2-W5 \"补全 OpenVLA Spatial/Goal/Long 数据\" 的要求。\n\n唯一保留意见：OpenVLA 仍不在主文 Table 2 中，我认为至少 Object 行应在主文出现（我的 review 中 F 部分已提出）。但这是叙事选择而非数据完整性问题。\n\n### R6-C3 REGRESSION: [AGREE]\n\n完全同意，且我独立发现了同一问题（我的 W2）。\n\n补充具体位置：\n- Introduction line 18: \"identifying the vision-language connector as **the primary determinant** of pruning robustness\"\n- Introduction C1: \"identifying connector architecture as **the primary determinant** of pruning robustness\"\n- Conclusion: \"Connector architecture is **the primary factor governing** VLA token compressibility\"\n- Abstract: \"the vision-language connector as **the primary architectural factor** governing pruning tolerance\"\n\n四处使用了因果性语言。Limitations Section 6 承认 \"preventing full causal isolation of the connector effect\"，与正文的因果 claim 直接矛盾。\n\n建议统一修改为 \"the strongest predictor of\" 或 \"the primary architectural correlate of\"。这是文字替换，不需要新实验。\n\n### SmolVLA 残余值: 评价\n\nSmolVLA k=0.95 的非零值（Spatial 6.6/4.2, Goal 3.4/4.2）**更可能是 genuine 但接近 noise floor 的真实信号，而非实验噪声**。理由：\n\n1. **模式一致**：非零值只出现在 k=0.95（最温和的 pruning），k=0.9 及以下全为 0.0%。如果是纯噪声，应在各 retention ratio 随机出现。\n2. **数值与 Wilson CI 一致**：6.6% 在 500 episodes 中对应 33/500 成功，Wilson 95% CI ≈ [4.7%, 9.2%]，与 0% 基线有统计学差异。\n3. **Suite 差异合理**：Object 和 Long 仍为 0.0%，而 Spatial 和 Goal 有残余——Spatial/Goal 的部分 task 可能对少量 token 丢失有更高容忍度（某些 task 可能不依赖被移除的特定空间区域）。\n\n**影响**：这使论文的核心 narrative 更精确——从 \"SmolVLA 在任何 pruning 下 catastrophic collapse 到 0%\" 变为 \"SmolVLA 在 k≤0.9 下 collapse 到 0%，k=0.95 下有 ≤6.6% 的残余\"。论文已适当更新措辞为 \"≤6.6%\"（Introduction）和 \"collapses to near-zero\" 而非 \"0.0%\"。这是一个改善——更诚实的数据报告。\n\n### π₀ offline 标注: [AGREE]\n\n同意这是问题。Abstract 写 \"The coefficient of variation (CV) of post-connector token norms captures this on a continuous spectrum (0.038 to 0.314)\"。0.038 来自 π₀，一个仅有 offline evaluation 的模型——没有 closed-loop SR 数据来验证其 pruning tolerance。将 offline-only 模型的 CV 作为 spectrum 下界，在 Abstract 中不加标注，会让读者认为 0.038 也有 closed-loop 验证。\n\n建议：将 Abstract 中的 spectrum 范围改为 closed-loop 模型的范围（0.055 到 0.314），或标注 \"0.038 [offline] to 0.314\"。考虑到 0.055 和 0.038 差异很小，使用 closed-loop 范围 (0.055–0.314) 更干净且不损失 narrative impact。\n\n### 是否调整评分？\n\n**原评分：6/10**\n**调整后：6/10（维持不变）**\n\n理由：Reviewer 1 的发现与我的独立评估高度一致。交叉审查没有揭示我遗漏的重大问题，也没有发现我过度严厉的地方。关键共识点：\n\n- Table 2 完整化 + attention baseline + multi-seed = 实质性改善 → 从 5 到 6 ✓\n- 因果语言未修正 = persistent but fixable weakness → 不影响评分\n- CV diagnostic N=4 = major but appropriately scoped weakness → 不影响评分\n- 我独立发现的 7+ concurrent works 被删除（N1 Must-Fix）是唯一可能影响评分的新问题，但因为这是 fixable editorial issue（恢复引用即可），我暂不因此降分。如果最终提交仍缺少这些引用，我会降至 5/10。\n\n6/10 = Borderline Accept，含义是：论文有 genuine insights（zero-mask, scoring double dissociation）但 evidence base 仍偏薄（4 models, 1 benchmark, simulation-only），且有 fixable-but-unacceptable editorial issues（missing citations, causal language）。\n",
    "reviewer_id": "2",
    "project": "importance_margin_vla_compress"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-29T00:52:21.155286+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5102
}
```

</details>

---


### Assistant

_source line 636 · 2026-05-29T00:52:27.201767+00:00_

交叉回应已提交。评分维持 6/10 不变。与 Reviewer 1 的判断高度一致：Table 2 完整化和 attention baseline 是实质改善，因果语言和 CV diagnostic sample size 是 persistent weaknesses。我独立发现的 7+ missing citations 是最严重的 editorial regression，但因可修复而暂不降分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_83179cdc26b856fbbaf531d145edb3bd:reviewer_2"
}
```

</details>

---
