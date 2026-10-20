# Reviewer 1 coordination — Part 3 of 3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/b2/b215da93b17f67da3030.json)

## Round 31

### Tool call

_source line 1090 · 2026-05-25T21:26:56.859512+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 核心任务接近 trivially solvable**\n同意 R2 的核心判断，但需要 nuance。\n\n1. **同意的部分**：exception_only 下 verdict prediction 确实接近 trivial——B5 format marker baseline 99.33% vs SFT 99.83% 仅差 0.50pp，这是事实。8 个 boundary samples 的统计效力不足以支撑 \"semantic understanding\" claim（我在 R1-W5 中也独立指出了这一点）。\n\n2. **需要补充的 nuance**：论文标题和核心 framing 实际上已经是关于 \"how verbosity degrades SFT\"，而非 \"how to achieve high accuracy\"。真正的贡献不是 exception_only 的高准确率本身，而是 (a) full_trace 仅 81.76% 这个负面结果，以及 (b) 7 条件的系统消融揭示的 tier hierarchy。此外，nomarker 实验（Section 4.3）移除所有 format markers 后仍达 ~97.8%，比最强 regex B4（93.61%）高出 4pp+，说明并非纯粹 surface-level pattern matching。R2 称 \"信号的绝大部分仍来自 surface-level 模式\" 过于绝对。\n\n3. **赞同 R2 的 reframing 建议**：论文应弱化 \"exception events as the minimal sufficient signal\" 的贡献表述，将重心更明确地放在 \"verbose trace input actively impairs SFT learning\" 这一更有价值的发现上。\n\n---\n\n**[AGREE] R2-N2: \"Information density as the binding constraint\" claim 超出证据**\n完全同意，与我的 R1-N1 一致。补充两点：\n\n1. R2 指出剩余 76% 被归为 \"inference-time input complexity\" 本质上是 Shi et al. (2023) 的 \"irrelevant context distraction\"——这个观察是准确的。论文在 Related Work（Section 2.1）引用了 Shi et al.，但在 Discussion 中未充分承认 density decomposition 中 76% 部分与 Shi et al. 发现的关系。这使得 \"density\" framing 看起来比实际更原创。\n\n2. 不过，论文仍有超越 Shi et al. 的增量贡献：(a) 在 SFT 设定下（而非 in-context learning）量化了 distraction effect；(b) 提供了 24% backward-pass / 76% inference-time 的分解（即使有限）；(c) tail-truncation budget curve 空间定位了 diagnostic signal（Section 4.5, Figure 4）。这些是 Shi et al. 没有做的。\n\n3. 但 \"binding constraint\" 的表述确实过强，应降级为 \"a key factor\" 或 \"the dominant factor in our setting\"。\n\n---\n\n**[REBUT] R2-N3: 泛化证据不足（部分反驳）**\n部分同意但认为 R2 的要求超出了合理的单篇论文范围。\n\n1. **跨任务**：R2 批评 Discussion 声称 \"should transfer to any trace-based task where compact diagnostic events exist\"。但这是 Discussion 中的推测性表述（用了 \"should\"），而非 claim。论文标题和 Contribution 明确限定为 verdict prediction。要求单篇论文覆盖多个任务（verdict prediction + code generation + program repair）不现实——这是 future work 而非本文缺陷。\n\n2. **跨数据集**：同意 DebugBench ceiling effect 是问题（我在 R1-W3 中也指出），但论文在 Appendix A.12 中坦诚承认 \"narrow margins are insufficient to independently validate trace importance\"。论文同时提供了 HumanEval+MBPP 的 24.70pp trace lift 作为主要证据，DebugBench 是补充验证。\n\n3. **跨语言**：同意 Python 的结构化 exception hierarchy 是方法高效的前提，但这已在 Limitations 中明确讨论（\"languages with less structured error reporting may exhibit different signal distributions\"）。跨语言验证需要为每种语言构建 trace 基础设施，这是独立的工程和研究工作。\n\n4. **总结**：N3 中的每个点在隔离来看都是合理的 limitation，但合在一起要求跨任务+跨数据集+跨语言的验证，对一篇聚焦 ablation study 的论文而言标准过高。论文的 scope 是明确的：verdict prediction + Python + 4 models。在这个 scope 内，证据是充分的。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 与 wang2025dcsh 和 ferrando2025execute 的区分不够**\n论文在 Section 2.1 已提供明确区分：\"relative to their work, we contribute a two-tier signal hierarchy, a phase transition in trace-length budgets, calibration analysis, and cross-architecture validation\"（Related Work, 第 6-7 行）。具体来说：\n- wang2025dcsh 研究了 trace utility 的 task/format dependency 但**未分解单个 trace component**；本文贡献的是 component-level ablation（7 conditions）\n- ferrando2025execute 发现 compact traces ≈ full traces 但**未量化为什么**；本文提供了 gradient masking decomposition（即使有限）和 tail-truncation 空间定位\n- 两篇工作均未做 cross-architecture validation（4 models × 3 families）\n\n区分已经足够清晰。如果 R2 有具体的 overlap 点认为未被覆盖，应指出。\n\n---\n\n**[AGREE] R2-W2: Discussion 过长**\n同意。Discussion（Section 5）约占 2 页（pages 6-8），对 8 页论文比例偏高。特别是：\n- \"Exception events capture test verdicts, not just crashes\" 段落（Discussion 第 53-57 行）本质上是实验发现的补充说明，更适合放在 Section 4（Experiments）\n- \"Alternative explanations\" 段落（Discussion 第 59-63 行）也可以精简或移至 Appendix\n- 节省的空间可用于加强实验（如更多 boundary case 分析或额外的种子实验）\n\n---\n\n**[AGREE] R2-W3: Figure 1 (fig:cross_scale) 未在正文中被引用**\n经验证，`\\ref{fig:cross_scale}` 确实未出现在任何 .tex 文件中。Figure 1 定义在 introduction.tex（line 29-34），有 `\\label{fig:cross_scale}`，但全文无 `\\ref` 引用。这是一个明确的格式错误，ACL 模板要求所有 figures 在正文中被引用。\n\n---\n\n**[AGREE] R2-W4: \"Scale invariance\" claim 需要 qualification**\n同意，与我的判断一致。1.5B–13B（8.7×）不足以支撑 \"scale invariance\" 的 claim。更大的模型（30B+, 70B+）可能有更强的 long-context 处理能力，从而降低 information dilution 的影响。论文应将表述改为 \"scale independence within the 1.5B–13B range\" 或类似限定。\n\n---\n\n**[AGREE] R2-W5: CI 计算假设存在问题**\n同意，与 R1-N3 一致，不再重复。\n\n---\n\n### 关于遗漏引用\n\n- **LongLLMLingua (Jiang et al., 2024)**：合理建议。论文已引用 LLMLingua (2023) 但未引用其后续工作 LongLLMLingua，后者更直接处理 long-context compression，与本文的 trace compression 发现相关。\n- **FisherSFT (2025) 和 Bruni et al. (2025)**：无法确认这两篇引用的真实性。R2 应提供完整的引用信息（标题、作者、venue）以便验证。如果为真实引用，需评估相关性后决定是否添加。",
  "reviewer_id": "1",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 核心任务接近 trivially solvable**\n同意 R2 的核心判断，但需要 nuance。\n\n1. **同意的部分**：exception_only 下 verdict prediction 确实接近 trivial——B5 format marker baseline 99.33% vs SFT 99.83% 仅差 0.50pp，这是事实。8 个 boundary samples 的统计效力不足以支撑 \"semantic understanding\" claim（我在 R1-W5 中也独立指出了这一点）。\n\n2. **需要补充的 nuance**：论文标题和核心 framing 实际上已经是关于 \"how verbosity degrades SFT\"，而非 \"how to achieve high accuracy\"。真正的贡献不是 exception_only 的高准确率本身，而是 (a) full_trace 仅 81.76% 这个负面结果，以及 (b) 7 条件的系统消融揭示的 tier hierarchy。此外，nomarker 实验（Section 4.3）移除所有 format markers 后仍达 ~97.8%，比最强 regex B4（93.61%）高出 4pp+，说明并非纯粹 surface-level pattern matching。R2 称 \"信号的绝大部分仍来自 surface-level 模式\" 过于绝对。\n\n3. **赞同 R2 的 reframing 建议**：论文应弱化 \"exception events as the minimal sufficient signal\" 的贡献表述，将重心更明确地放在 \"verbose trace input actively impairs SFT learning\" 这一更有价值的发现上。\n\n---\n\n**[AGREE] R2-N2: \"Information density as the binding constraint\" claim 超出证据**\n完全同意，与我的 R1-N1 一致。补充两点：\n\n1. R2 指出剩余 76% 被归为 \"inference-time input complexity\" 本质上是 Shi et al. (2023) 的 \"irrelevant context distraction\"——这个观察是准确的。论文在 Related Work（Section 2.1）引用了 Shi et al.，但在 Discussion 中未充分承认 density decomposition 中 76% 部分与 Shi et al. 发现的关系。这使得 \"density\" framing 看起来比实际更原创。\n\n2. 不过，论文仍有超越 Shi et al. 的增量贡献：(a) 在 SFT 设定下（而非 in-context learning）量化了 distraction effect；(b) 提供了 24% backward-pass / 76% inference-time 的分解（即使有限）；(c) tail-truncation budget curve 空间定位了 diagnostic signal（Section 4.5, Figure 4）。这些是 Shi et al. 没有做的。\n\n3. 但 \"binding constraint\" 的表述确实过强，应降级为 \"a key factor\" 或 \"the dominant factor in our setting\"。\n\n---\n\n**[REBUT] R2-N3: 泛化证据不足（部分反驳）**\n部分同意但认为 R2 的要求超出了合理的单篇论文范围。\n\n1. **跨任务**：R2 批评 Discussion 声称 \"should transfer to any trace-based task where compact diagnostic events exist\"。但这是 Discussion 中的推测性表述（用了 \"should\"），而非 claim。论文标题和 Contribution 明确限定为 verdict prediction。要求单篇论文覆盖多个任务（verdict prediction + code generation + program repair）不现实——这是 future work 而非本文缺陷。\n\n2. **跨数据集**：同意 DebugBench ceiling effect 是问题（我在 R1-W3 中也指出），但论文在 Appendix A.12 中坦诚承认 \"narrow margins are insufficient to independently validate trace importance\"。论文同时提供了 HumanEval+MBPP 的 24.70pp trace lift 作为主要证据，DebugBench 是补充验证。\n\n3. **跨语言**：同意 Python 的结构化 exception hierarchy 是方法高效的前提，但这已在 Limitations 中明确讨论（\"languages with less structured error reporting may exhibit different signal distributions\"）。跨语言验证需要为每种语言构建 trace 基础设施，这是独立的工程和研究工作。\n\n4. **总结**：N3 中的每个点在隔离来看都是合理的 limitation，但合在一起要求跨任务+跨数据集+跨语言的验证，对一篇聚焦 ablation study 的论文而言标准过高。论文的 scope 是明确的：verdict prediction + Python + 4 models。在这个 scope 内，证据是充分的。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: 与 wang2025dcsh 和 ferrando2025execute 的区分不够**\n论文在 Section 2.1 已提供明确区分：\"relative to their work, we contribute a two-tier signal hierarchy, a phase transition in trace-length budgets, calibration analysis, and cross-architecture validation\"（Related Work, 第 6-7 行）。具体来说：\n- wang2025dcsh 研究了 trace utility 的 task/format dependency 但**未分解单个 trace component**；本文贡献的是 component-level ablation（7 conditions）\n- ferrando2025execute 发现 compact traces ≈ full traces 但**未量化为什么**；本文提供了 gradient masking decomposition（即使有限）和 tail-truncation 空间定位\n- 两篇工作均未做 cross-architecture validation（4 models × 3 families）\n\n区分已经足够清晰。如果 R2 有具体的 overlap 点认为未被覆盖，应指出。\n\n---\n\n**[AGREE] R2-W2: Discussion 过长**\n同意。Discussion（Section 5）约占 2 页（pages 6-8），对 8 页论文比例偏高。特别是：\n- \"Exception events capture test verdicts, not just crashes\" 段落（Discussion 第 53-57 行）本质上是实验发现的补充说明，更适合放在 Section 4（Experiments）\n- \"Alternative explanations\" 段落（Discussion 第 59-63 行）也可以精简或移至 Appendix\n- 节省的空间可用于加强实验（如更多 boundary case 分析或额外的种子实验）\n\n---\n\n**[AGREE] R2-W3: Figure 1 (fig:cross_scale) 未在正文中被引用**\n经验证，`\\ref{fig:cross_scale}` 确实未出现在任何 .tex 文件中。Figure 1 定义在 introduction.tex（line 29-34），有 `\\label{fig:cross_scale}`，但全文无 `\\ref` 引用。这是一个明确的格式错误，ACL 模板要求所有 figures 在正文中被引用。\n\n---\n\n**[AGREE] R2-W4: \"Scale invariance\" claim 需要 qualification**\n同意，与我的判断一致。1.5B–13B（8.7×）不足以支撑 \"scale invariance\" 的 claim。更大的模型（30B+, 70B+）可能有更强的 long-context 处理能力，从而降低 information dilution 的影响。论文应将表述改为 \"scale independence within the 1.5B–13B range\" 或类似限定。\n\n---\n\n**[AGREE] R2-W5: CI 计算假设存在问题**\n同意，与 R1-N3 一致，不再重复。\n\n---\n\n### 关于遗漏引用\n\n- **LongLLMLingua (Jiang et al., 2024)**：合理建议。论文已引用 LLMLingua (2023) 但未引用其后续工作 LongLLMLingua，后者更直接处理 long-context compression，与本文的 trace compression 发现相关。\n- **FisherSFT (2025) 和 Bruni et al. (2025)**：无法确认这两篇引用的真实性。R2 应提供完整的引用信息（标题、作者、venue）以便验证。如果为真实引用，需评估相关性后决定是否添加。",
    "reviewer_id": "1",
    "project": "trace-verdict-study"
  }
}
```

</details>

---


### Tool result

_source line 1091 · 2026-05-25T21:27:00.778510+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 1092 · 2026-05-25T21:27:11.117638+00:00_

交叉回应已提交。总结：

- **R2-N1**（任务 trivial）：[AGREE]，但补充了 nomarker 实验仍高于 regex 4pp+ 的 nuance，赞同 reframing 建议
- **R2-N2**（binding constraint overclaim）：[AGREE]，与 R1-N1 一致，但指出论文仍有超越 Shi et al. 的增量贡献
- **R2-N3**（泛化不足）：[REBUT]，每个点单独合理但合在一起标准过高，论文 scope 明确且 Limitations 已覆盖
- **R2-W1**（与 prior work 区分）：[REBUT]，Section 2.1 已提供 4 点明确区分
- **R2-W2**（Discussion 过长）：[AGREE]
- **R2-W3**（Figure 1 未引用）：[AGREE]，经 grep 验证确认
- **R2-W4**（scale invariance 需限定）：[AGREE]
- **R2-W5**（CI 假设问题）：[AGREE]，与 R1-N3 一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_47a2f37b5c77af2e2351362f8def77a1:reviewer_1"
}
```

</details>

---
