# Reviewer 2 coordination — Part 2 of 4

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/d6/d6e6323219bc00f03388.json)

## Round 14

### Tool call

_source line 562 · 2026-05-22T05:25:00.509944+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n### R1-N1: Bonferroni 显著性结构性不可达 + Limitations 中 0.008 事实性错误\n\n**[AGREE]** 完全同意，且此点比我自己的 N1 更精确。\n\nR1 的数学推导无懈可击：n=5 的 exact permutation test 最小两尾 p = 2/120 = 0.017，Bonferroni 校正 ×6 后 adjusted p = 0.100，**在当前实验设计下永远无法达到常规显著性**。这不是统计效力不足的问题（power 可以通过增大样本量改善），而是设计的结构性天花板——无论观测结果多极端，都不可能 reject null。\n\nLimitations 中 \"minimum achievable two-tailed p-value is approximately 0.008\" 确实是事实性错误。1/120 ≈ 0.008 是单尾值；两尾应为 2/120 ≈ 0.017。Table 1 中 LAMBADA 报告的 p = .017 是正确的，说明作者在实际计算中用了正确方法，但 Limitations 的文字表述出了错。**这必须修正。**\n\nR1 的建议（将叙事重心转移到 Contribution 1）与我自己的判断一致。我在自己的 N1 中建议合并 Contribution 2 & 3，R1 的方案更进一步——直接降级为 \"suggestive finding\"。我支持这个方向。Per-example multiplicity 的 task-dependent variation（Contribution 1）是论文最扎实的发现，不依赖于 convergence 的 p 值。\n\n### R1-N2: Decoupling 形式化（Equation 1）的三个技术问题\n\n**[AGREE]** 三个子问题均成立，但我对严重程度有细微不同看法。\n\n**Condition (i) 的 brittleness**：同意。ρ = −1.0 是精确值判据——n=5 时任何 rank 的微小扰动就会使 ρ < 1.0。论文没有讨论 \"近似 decoupling\"（例如 ρ ≤ −0.9）是否也有意义。这使得 formalization 看起来是 post-hoc 地拟合 LAMBADA 数据，而非提出一个可推广的判据。\n\n**Condition (ii) 的区分力问题**：这是 R1 最精锐的技术观察。如果 bootstrap CI 足够宽（n=3 architectures 确实会产生宽 CI），那么即使 Jaccard 呈单调递增趋势，相邻 attention ratio 的 CI 仍可能重叠——此时 condition (ii) 的 \"overlap = saturation\" 解读就不成立了。**论文需要报告各 attention ratio 下的 CI 宽度**以证明 overlap 确实反映 saturation 而非 imprecision。\n\n**唯一拟合案例**：同意。Equation 1 对 LAMBADA 的拟合是完美的——因为它就是从 LAMBADA 的数据中归纳出来的。没有第二个 benchmark 满足条件来验证这个 formalization 的泛化性。这削弱了将其作为独立 contribution 的说服力。\n\n不过，我想补充一点：decoupling 作为一个**定性观察**（aggregate σ 下降但 per-example Jaccard 不变）本身是有信息量的，即使 formalization 有问题。问题出在将一个 reasonable 的观察 over-formalize 为一个看似严格但实际 fragile 的条件。**建议保留定性描述，弱化或移除 Equation 1 的形式化。**\n\n---\n\n## Should-Fix\n\n### R1-W1: 单一训练 run 的混淆效应\n\n**[AGREE]** R1 的表述比我自己的 W1 更精确。\n\n关键洞察：within-arch Jaccard ≈ 0.33 **不是** seed-only baseline，因为 \"within-arch\" 的不同配置之间 attention ratio 不同（例如 h3-1 vs. h24-1 虽然都是 GDN，但 attention layer 数量不同）。所以 within-arch Jaccard 混合了 attention ratio variation + seed variation（如果有的话），而 cross-arch Jaccard 混合了 architecture variation + attention ratio variation + seed variation。\n\n论文用 \"within-arch Jaccard ≈ 0.33 vs. cross-arch Jaccard ≈ 0.10\" 的 3× gap 来论证 architecture 是主要 driver（§4.3），但这个对比的两端都不是纯 seed baseline。**真正需要的是相同 architecture + 相同 ratio + 不同 seed 的 Jaccard**，这在当前 zoo 中不存在。\n\n论文在 Limitations 中提到了 multi-seed 作为 future work，但应更明确说明 within-arch Jaccard 不等于 seed baseline。\n\n### R1-W2: LAMBADA 收敛依赖于 GDN\n\n**[AGREE]** R1 的 \"partially dependent understates the situation\" 判断准确。\n\n§4.4 使用 \"partially dependent on GDN\" 表述。但数据说的是：有 GDN 时 ρ = −1.0（p = .017），无 GDN 时 ρ = −0.7（p = .233）。从统计推断角度看，移除 GDN 后 convergence 完全不显著——这不是 \"partial\" 依赖，而是 **GDN 是 convergence 信号的必要条件**（至少在当前数据中）。\n\n更严重的是，如 R1 所指出，decoupling 的 condition (i) 就是 convergence。如果 convergence 在移除 GDN 后不成立，decoupling 也连带失效。这进一步支持了我和 R1 共同的建议：降低 convergence 和 decoupling 在 contribution hierarchy 中的地位。\n\n### R1-W3: Binary decomposition 在多选题上的信息损失\n\n**[AGREE]** 这是一个合理的指向。\n\n论文的 Cohen's d 验证（d = 0.73–0.92 between helped and hurt）仅在 LAMBADA 上报告。LAMBADA 是 open-ended retrieval 任务，binary correctness 有自然含义。但对 HellaSwag/PIQA 等 multiple-choice 任务，Appendix O 显示 effect size 更弱，这与 binary decomposition 在 multiple-choice 设置下信息损失更大的预期一致。\n\n不过我认为这是 **Minor** 而非 Major 问题，因为 binary decomposition 与 Marx (2020) multiplicity 框架保持一致，且作者已在 Limitations 中承认 accuracy-only 限制。\n\n### R1-W4: Confidence margin 分析是描述性的，非因果性的\n\n**[AGREE]** \"rescue\" 和 \"disruption\" 确实是因果性语言（X rescues/disrupts Y 暗示 X causes change in Y），但分析仅显示 attention 配置与 example 正确性变化之间的相关性。\n\n具体来说，\"helped\" 只意味着 example 在 hybrid 中正确而在 pure recurrent 中不正确——这是 observational comparison，不是 intervention。称其为 \"rescue\" 隐含了 attention 作为 causal agent 的框架，但在没有 do-calculus 或 ablation 的情况下，这只是 association。\n\n建议将 \"rescue\"/\"disruption\" 改为更中性的 \"positive/negative attention effect\" 或 \"helped/hurt\"（后者论文在其他地方已经使用）。\n\n---\n\n## Questions\n\n### R1-Q1: Limitations 的 0.008 是否为笔误？\n\n**[AGREE]** 是事实性错误，应为 0.017（两尾）。见 N1 的回应。\n\n### R1-Q2: Equation 1 condition (ii) 的 CI 宽度？单调递增 Jaccard 是否仍满足 overlap？\n\n**[AGREE]** 这是关于 condition (ii) discriminative power 的关键技术问题。如果 n=3 的 bootstrap CI 宽到足以让任何趋势（包括单调递增）都产生 overlap，那么 condition (ii) 就是 vacuously true，不提供任何信息。**论文必须报告各 ratio 下的 CI 宽度才能回应此质疑。**\n\n### R1-Q3: Attention cosine 0.995 不保证 per-example 行为相同\n\n**[AGREE]** 这是一个好的技术追问。Cosine similarity 0.995 是在 attention weight 的 **aggregate** distribution 上计算的（§F, across all 5,153 LAMBADA examples）。但两个 globally 近似的 attention distribution 完全可以在特定 examples 上有显著差异——而这些特定 examples 可能恰好是 helped/hurt set 中的成员。\n\n建议作者在 divergent examples（helped/hurt set 的成员）上单独计算 attention output similarity，看是否低于 overall 0.995。如果是，则说明 per-example divergence 确实集中在 attention 行为不同的 examples 上，这会大大加强 \"recurrent layer drives divergence\" 的论证。\n\n### R1-Q4: 是否考虑过基于 α/Jaccard 的 oracle-selected ensemble？\n\n**[REBUT]** 部分反驳。这是一个有趣的方向，但我认为论文当前的 ensemble POC（majority vote + oracle upper bound）已经提供了关键信息：oracle accuracy 比 best individual 高 +7–14pp（§5），说明 complementary information 确实存在。问题是**如何 access 它**，而非是否存在。\n\n基于 α/Jaccard 的 oracle selection 预设了知道哪个架构在哪个 example 上正确——这在 deployment 时不可用。更现实的方向是 confidence-based routing（论文的 practical recommendation 2 已经指向这个方向）。但我同意这应该在 future work 中讨论。\n\n### R1-Q5: Normalized ES 5–7% 是否说明 per-example divergence 实际规模很小？\n\n**[REBUT]** 部分反驳。R1 提出了一个合理的 alternative interpretation，但我认为 5–7% of achievable range 的 normalized ES 需要结合 base rate 理解。\n\n论文的 helped/hurt set 大约占总 examples 的 14–30%（α = 0.14–0.30）。在这些 affected examples 中，cross-architecture Jaccard ≈ 0.10 意味着 ~90% non-overlap。所以问题不是 \"有多少 examples 被影响\"（这由 α 回答），而是 \"被影响的 examples 在不同架构间有多大重合\"（这由 Jaccard 回答）。\n\nNormalized ES 低（5–7%）确认了 Jaccard 接近 chance level（即架构影响近乎不重叠的 example sets），这是论文的核心 claim。如果 normalized ES 高（比如 50%），反而说明架构间有显著重合，multiplicity 不那么严重。所以 **低 ES 支持而非削弱论文的 narrative**。\n\n但 R1 的 framing 也有道理——如果读者关注的是 \"per-example divergence 有多大实际影响\"，5–7% 可能暗示影响有限。建议论文更明确区分两个不同问题：(1) divergence 的**覆盖面**（α）vs. (2) divergence 的**独特性**（Jaccard/normalized ES）。\n\n---\n\n## 总体评估\n\nReviewer 1 的审稿意见技术深度很高，尤其是 N1 的 Bonferroni 结构性不可达论证和 N2 中 condition (ii) discriminative power 的质疑。我在 12/14 个子项上与 R1 一致（[AGREE]），仅在 Q4 和 Q5 上部分反驳。\n\n**与 R1 的共识点：**\n- Contribution 2（convergence）和 Contribution 3（decoupling）的 statistical foundation 不够 robust，应降级或合并\n- Contribution 1（per-example multiplicity 的 task-dependent variation）是论文最有力的发现\n- 单次训练运行是根本性限制，within-arch Jaccard 不是纯 seed baseline\n- Limitations 中 0.008 是事实性错误\n- Overall 3.0（Findings）\n\n**与 R1 的分歧点：**\n- R1 未指出 Fehlauer et al. (2025) 的遗漏（我认为这是 Related Work 的重要缺失）\n- 对 Q5 normalized ES 的解读：R1 倾向于 \"divergence 规模小\"，我认为低 ES 恰好支持论文的 non-overlap claim\n",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n### R1-N1: Bonferroni 显著性结构性不可达 + Limitations 中 0.008 事实性错误\n\n**[AGREE]** 完全同意，且此点比我自己的 N1 更精确。\n\nR1 的数学推导无懈可击：n=5 的 exact permutation test 最小两尾 p = 2/120 = 0.017，Bonferroni 校正 ×6 后 adjusted p = 0.100，**在当前实验设计下永远无法达到常规显著性**。这不是统计效力不足的问题（power 可以通过增大样本量改善），而是设计的结构性天花板——无论观测结果多极端，都不可能 reject null。\n\nLimitations 中 \"minimum achievable two-tailed p-value is approximately 0.008\" 确实是事实性错误。1/120 ≈ 0.008 是单尾值；两尾应为 2/120 ≈ 0.017。Table 1 中 LAMBADA 报告的 p = .017 是正确的，说明作者在实际计算中用了正确方法，但 Limitations 的文字表述出了错。**这必须修正。**\n\nR1 的建议（将叙事重心转移到 Contribution 1）与我自己的判断一致。我在自己的 N1 中建议合并 Contribution 2 & 3，R1 的方案更进一步——直接降级为 \"suggestive finding\"。我支持这个方向。Per-example multiplicity 的 task-dependent variation（Contribution 1）是论文最扎实的发现，不依赖于 convergence 的 p 值。\n\n### R1-N2: Decoupling 形式化（Equation 1）的三个技术问题\n\n**[AGREE]** 三个子问题均成立，但我对严重程度有细微不同看法。\n\n**Condition (i) 的 brittleness**：同意。ρ = −1.0 是精确值判据——n=5 时任何 rank 的微小扰动就会使 ρ < 1.0。论文没有讨论 \"近似 decoupling\"（例如 ρ ≤ −0.9）是否也有意义。这使得 formalization 看起来是 post-hoc 地拟合 LAMBADA 数据，而非提出一个可推广的判据。\n\n**Condition (ii) 的区分力问题**：这是 R1 最精锐的技术观察。如果 bootstrap CI 足够宽（n=3 architectures 确实会产生宽 CI），那么即使 Jaccard 呈单调递增趋势，相邻 attention ratio 的 CI 仍可能重叠——此时 condition (ii) 的 \"overlap = saturation\" 解读就不成立了。**论文需要报告各 attention ratio 下的 CI 宽度**以证明 overlap 确实反映 saturation 而非 imprecision。\n\n**唯一拟合案例**：同意。Equation 1 对 LAMBADA 的拟合是完美的——因为它就是从 LAMBADA 的数据中归纳出来的。没有第二个 benchmark 满足条件来验证这个 formalization 的泛化性。这削弱了将其作为独立 contribution 的说服力。\n\n不过，我想补充一点：decoupling 作为一个**定性观察**（aggregate σ 下降但 per-example Jaccard 不变）本身是有信息量的，即使 formalization 有问题。问题出在将一个 reasonable 的观察 over-formalize 为一个看似严格但实际 fragile 的条件。**建议保留定性描述，弱化或移除 Equation 1 的形式化。**\n\n---\n\n## Should-Fix\n\n### R1-W1: 单一训练 run 的混淆效应\n\n**[AGREE]** R1 的表述比我自己的 W1 更精确。\n\n关键洞察：within-arch Jaccard ≈ 0.33 **不是** seed-only baseline，因为 \"within-arch\" 的不同配置之间 attention ratio 不同（例如 h3-1 vs. h24-1 虽然都是 GDN，但 attention layer 数量不同）。所以 within-arch Jaccard 混合了 attention ratio variation + seed variation（如果有的话），而 cross-arch Jaccard 混合了 architecture variation + attention ratio variation + seed variation。\n\n论文用 \"within-arch Jaccard ≈ 0.33 vs. cross-arch Jaccard ≈ 0.10\" 的 3× gap 来论证 architecture 是主要 driver（§4.3），但这个对比的两端都不是纯 seed baseline。**真正需要的是相同 architecture + 相同 ratio + 不同 seed 的 Jaccard**，这在当前 zoo 中不存在。\n\n论文在 Limitations 中提到了 multi-seed 作为 future work，但应更明确说明 within-arch Jaccard 不等于 seed baseline。\n\n### R1-W2: LAMBADA 收敛依赖于 GDN\n\n**[AGREE]** R1 的 \"partially dependent understates the situation\" 判断准确。\n\n§4.4 使用 \"partially dependent on GDN\" 表述。但数据说的是：有 GDN 时 ρ = −1.0（p = .017），无 GDN 时 ρ = −0.7（p = .233）。从统计推断角度看，移除 GDN 后 convergence 完全不显著——这不是 \"partial\" 依赖，而是 **GDN 是 convergence 信号的必要条件**（至少在当前数据中）。\n\n更严重的是，如 R1 所指出，decoupling 的 condition (i) 就是 convergence。如果 convergence 在移除 GDN 后不成立，decoupling 也连带失效。这进一步支持了我和 R1 共同的建议：降低 convergence 和 decoupling 在 contribution hierarchy 中的地位。\n\n### R1-W3: Binary decomposition 在多选题上的信息损失\n\n**[AGREE]** 这是一个合理的指向。\n\n论文的 Cohen's d 验证（d = 0.73–0.92 between helped and hurt）仅在 LAMBADA 上报告。LAMBADA 是 open-ended retrieval 任务，binary correctness 有自然含义。但对 HellaSwag/PIQA 等 multiple-choice 任务，Appendix O 显示 effect size 更弱，这与 binary decomposition 在 multiple-choice 设置下信息损失更大的预期一致。\n\n不过我认为这是 **Minor** 而非 Major 问题，因为 binary decomposition 与 Marx (2020) multiplicity 框架保持一致，且作者已在 Limitations 中承认 accuracy-only 限制。\n\n### R1-W4: Confidence margin 分析是描述性的，非因果性的\n\n**[AGREE]** \"rescue\" 和 \"disruption\" 确实是因果性语言（X rescues/disrupts Y 暗示 X causes change in Y），但分析仅显示 attention 配置与 example 正确性变化之间的相关性。\n\n具体来说，\"helped\" 只意味着 example 在 hybrid 中正确而在 pure recurrent 中不正确——这是 observational comparison，不是 intervention。称其为 \"rescue\" 隐含了 attention 作为 causal agent 的框架，但在没有 do-calculus 或 ablation 的情况下，这只是 association。\n\n建议将 \"rescue\"/\"disruption\" 改为更中性的 \"positive/negative attention effect\" 或 \"helped/hurt\"（后者论文在其他地方已经使用）。\n\n---\n\n## Questions\n\n### R1-Q1: Limitations 的 0.008 是否为笔误？\n\n**[AGREE]** 是事实性错误，应为 0.017（两尾）。见 N1 的回应。\n\n### R1-Q2: Equation 1 condition (ii) 的 CI 宽度？单调递增 Jaccard 是否仍满足 overlap？\n\n**[AGREE]** 这是关于 condition (ii) discriminative power 的关键技术问题。如果 n=3 的 bootstrap CI 宽到足以让任何趋势（包括单调递增）都产生 overlap，那么 condition (ii) 就是 vacuously true，不提供任何信息。**论文必须报告各 ratio 下的 CI 宽度才能回应此质疑。**\n\n### R1-Q3: Attention cosine 0.995 不保证 per-example 行为相同\n\n**[AGREE]** 这是一个好的技术追问。Cosine similarity 0.995 是在 attention weight 的 **aggregate** distribution 上计算的（§F, across all 5,153 LAMBADA examples）。但两个 globally 近似的 attention distribution 完全可以在特定 examples 上有显著差异——而这些特定 examples 可能恰好是 helped/hurt set 中的成员。\n\n建议作者在 divergent examples（helped/hurt set 的成员）上单独计算 attention output similarity，看是否低于 overall 0.995。如果是，则说明 per-example divergence 确实集中在 attention 行为不同的 examples 上，这会大大加强 \"recurrent layer drives divergence\" 的论证。\n\n### R1-Q4: 是否考虑过基于 α/Jaccard 的 oracle-selected ensemble？\n\n**[REBUT]** 部分反驳。这是一个有趣的方向，但我认为论文当前的 ensemble POC（majority vote + oracle upper bound）已经提供了关键信息：oracle accuracy 比 best individual 高 +7–14pp（§5），说明 complementary information 确实存在。问题是**如何 access 它**，而非是否存在。\n\n基于 α/Jaccard 的 oracle selection 预设了知道哪个架构在哪个 example 上正确——这在 deployment 时不可用。更现实的方向是 confidence-based routing（论文的 practical recommendation 2 已经指向这个方向）。但我同意这应该在 future work 中讨论。\n\n### R1-Q5: Normalized ES 5–7% 是否说明 per-example divergence 实际规模很小？\n\n**[REBUT]** 部分反驳。R1 提出了一个合理的 alternative interpretation，但我认为 5–7% of achievable range 的 normalized ES 需要结合 base rate 理解。\n\n论文的 helped/hurt set 大约占总 examples 的 14–30%（α = 0.14–0.30）。在这些 affected examples 中，cross-architecture Jaccard ≈ 0.10 意味着 ~90% non-overlap。所以问题不是 \"有多少 examples 被影响\"（这由 α 回答），而是 \"被影响的 examples 在不同架构间有多大重合\"（这由 Jaccard 回答）。\n\nNormalized ES 低（5–7%）确认了 Jaccard 接近 chance level（即架构影响近乎不重叠的 example sets），这是论文的核心 claim。如果 normalized ES 高（比如 50%），反而说明架构间有显著重合，multiplicity 不那么严重。所以 **低 ES 支持而非削弱论文的 narrative**。\n\n但 R1 的 framing 也有道理——如果读者关注的是 \"per-example divergence 有多大实际影响\"，5–7% 可能暗示影响有限。建议论文更明确区分两个不同问题：(1) divergence 的**覆盖面**（α）vs. (2) divergence 的**独特性**（Jaccard/normalized ES）。\n\n---\n\n## 总体评估\n\nReviewer 1 的审稿意见技术深度很高，尤其是 N1 的 Bonferroni 结构性不可达论证和 N2 中 condition (ii) discriminative power 的质疑。我在 12/14 个子项上与 R1 一致（[AGREE]），仅在 Q4 和 Q5 上部分反驳。\n\n**与 R1 的共识点：**\n- Contribution 2（convergence）和 Contribution 3（decoupling）的 statistical foundation 不够 robust，应降级或合并\n- Contribution 1（per-example multiplicity 的 task-dependent variation）是论文最有力的发现\n- 单次训练运行是根本性限制，within-arch Jaccard 不是纯 seed baseline\n- Limitations 中 0.008 是事实性错误\n- Overall 3.0（Findings）\n\n**与 R1 的分歧点：**\n- R1 未指出 Fehlauer et al. (2025) 的遗漏（我认为这是 Related Work 的重要缺失）\n- 对 Q5 normalized ES 的解读：R1 倾向于 \"divergence 规模小\"，我认为低 ES 恰好支持论文的 non-overlap claim\n",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-22T05:25:04.442832+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3932
}
```

</details>

---


### Assistant

_source line 564 · 2026-05-22T05:25:09.957952+00:00_

交叉回应已提交。

总结：14 个子项中 12 个 [AGREE]，2 个 [REBUT]（Q4 oracle ensemble 和 Q5 normalized ES 解读）。与 R1 的核心共识是：Contribution 1 是最扎实的发现，Contribution 2/3 的统计基础不够 robust，应降级。主要分歧在于我额外指出了 Fehlauer et al. (2025) 的遗漏，以及对 normalized ES 低值的解读方向不同——我认为低 ES 支持（而非削弱）论文的 non-overlap claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

80 recorded events


### User

_source line 565 · 2026-05-22T05:51:32.094013+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式合规）

### Venue 信息
- **目标 venue**: EMNLP 2026 via ARR May cycle
- **截止日期**: 2026-05-25
- **类型**: Long Paper（正文 8 页 + unlimited references）
- **模板**: ACL style（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind
- **Limitations**: 必需，不计入页数；Ethics Statement 可选，不计入页数

### 论文路径
- **LaTeX 源码**: `projects/entrainment_gated_ft/docs/paper/main.tex`（含 `\input` 引用的 sections/）
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/submitted.pdf`（18 页：8 正文 + 10 appendix/references）
- **补充材料**: `projects/entrainment_gated_ft/docs/paper/author_response_r7.tex`（作者对先前审稿意见的回应，仅作参考）

### 你的审查侧重：新颖性 + 完整性 + 格式合规

请重点审查以下方面：

1. **新颖性评估**
   - 相对于 Marx et al. (2020) predictive multiplicity 和 D'Amour et al. (2022) underspecification，本文的增量贡献是什么？
   - 核心发现（task-dependent α variation、low Jaccard、LAMBADA convergence、decoupling）是否可从现有文献直接预期？还是提供了意外的 empirical insights？
   - "Apply existing metrics to new domain" 的贡献水平——是否有超出 metric application 的分析深度？
   - McCoy et al. (2020) 研究 seed-driven disagreement，本文扩展到 architecture-driven：这是方法论贡献还是仅是 setting 的自然延伸？

2. **Related Work 完整性**
   - 是否遗漏了重要相关工作？特别关注：
     - Hybrid architecture 评估的最新工作（2024-2026）
     - Predictive multiplicity / underspecification 的后续工作
     - Per-example analysis 方法论（beyond Swayamdipta et al. 2020）
   - 现有引用的定位是否准确？是否有 mischaracterization？

3. **写作质量**
   - Abstract 是否准确反映论文内容？信息密度是否合适？
   - Introduction 的 claim 是否与 Experiments 中的证据匹配？是否有 overclaiming？
   - Contribution list 是否清晰、层次分明？
   - §4 各 subsection 的逻辑流是否连贯？
   - Limitations 是否充分（EMNLP 要求覆盖 ~3 点，一小段即可）？

4. **EMNLP 格式合规**
   - 正文页数是否 ≤ 8 页（不含 Limitations/Ethics/References）？
   - 匿名处理：是否有 de-anonymizing 信息（作者名、机构、自引暴露、代码仓库链接等）？
   - Figure/Table 格式：分辨率、字号（≥ 80% body text）、caption 完整性
   - References 格式：一致性、完整性（有无 arXiv-only 可替换为 venue 版本？）

5. **Excitement / Impact**
   - 论文对 NLP 社区的潜在影响？
   - 结果是否会改变 practitioners 的行为？
   - 适合 Main Conference 还是 Findings？

请按 ARR 审稿标准输出完整审稿报告，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-22T05:51:40.057492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-22T05:51:40.763268+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-22T05:51:40.914167+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 569 · 2026-05-22T05:51:40.914581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-22T05:51:45.533141+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-22T05:51:46.838241+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T05:51:47.541325+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-18",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-18",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T05:51:52.989966+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and scoring criteria:

## Reviewer Scoring

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Assessment Criteria

The Overall assessment score 
…[truncated 1269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7456
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-22T05:51:55.284302+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 
…[truncated 460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8446
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-22T05:51:56.390174+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 428.6}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.7}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.2}], \"total_pages\": 18, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images\"
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8848
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-22T05:52:02.013470+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other scoring fields. List all score values and their meanings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other scoring fields. List all score values and their meanings."
  }
}
```

</details>

---


### Tool call

_source line 577 · 2026-05-22T05:52:02.314767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T05:52:03.269684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 579 · 2026-05-22T05:52:03.420600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-22T05:52:03.723865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-22T05:52:04.328456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-22T05:52:04.379104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-22T05:52:04.884188+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-22T05:52:04.884602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-22T05:52:05.188824+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool result

_source line 586 · 2026-05-22T05:52:05.691409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T05:52:09.914536+00:00_

# ARR Review Form Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite certain; unlikely to have missed important details
- **3**: Reasonably confident but possible oversight of specifics
- **2**: Can defend evaluation but likely missed some details or novelty assessment
- **1**: Outside expertise area; evaluation is an educated guess

## Soundness
Scale: 1-5 (with half-point increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: Strong support for claims; additional experiments optional
- **3**: Main claims adequately supported; minor details may need strengthening
- **2**: Insufficient support for main claims; major technical/methodological problems
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point increments)
- **5**: Highly exciting; would recommend and attend presentation
- **4**: Exciting; would mention to others and prioritize attending
- **3**: Interesting; might mention points or attend if time permits
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: Not exciting; lacks relevance to computational linguistics

## Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5% papers)
- **4.5**: Borderline Award
- **4**: Conference acceptance recommended
- **3.5**: Borderline Conference
- **3**: Accept to Findings track
- **2.5**: Borderline Findings
- **2**: Substantial revisions needed; resubmit next cycle
- **1.5**: Major revisions required; resubmit after next cycle
- **1**: Do not resubmit; not relevant to computational linguistics

## Additional Scoring Dimensions

**Reproducibility** (1-5): From easily reproducible to unable to reproduce

**Datasets** (1-5): From enabling
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7901
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T05:52:14.130865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 589 · 2026-05-22T05:52:14.181565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-22T05:52:14.433828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-22T05:52:15.448480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool result

_source line 592 · 2026-05-22T05:52:15.450150+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1268
}
```

</details>

---


### Tool call

_source line 593 · 2026-05-22T05:52:15.454654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 594 · 2026-05-22T05:52:15.909786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1475
}
```

</details>

---


### Tool call

_source line 595 · 2026-05-22T05:52:15.910246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 596 · 2026-05-22T05:52:16.315542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-22T05:52:16.316029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-22T05:52:17.021422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-22T05:52:17.223615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-22T05:52:21.138702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T05:52:21.992910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-22T05:52:21.993331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T05:52:22.531718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-22T05:52:22.984486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 991
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-22T05:52:22.984914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-22T05:52:23.838881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-22T05:52:23.840033+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-22T05:52:23.840359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-22T05:52:24.393817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T05:52:24.746243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-22T05:52:24.746693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-22T05:52:25.200311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-22T05:52:25.553288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-22T05:52:41.102947+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "predictive multiplicity language models 2024 2025 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "predictive multiplicity language models 2024 2025 NLP"
  }
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-22T05:52:41.204013+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hybrid linear recurrent attention architecture evaluation comparison 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hybrid linear recurrent attention architecture evaluation comparison 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-22T05:52:41.706142+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "McCoy et al 2020 \"BERTs of a feather\" seed variability NLP models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "McCoy et al 2020 \"BERTs of a feather\" seed variability NLP models"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-22T05:52:47.629922+00:00_

Web search results for query: "predictive multiplicity language models 2024 2025 NLP"

Links: [{"title":"Better & Faster Large Language Models via Multi-token Prediction","url":"https://arxiv.org/pdf/2404.19737"},{"title":"Multimodal Language Models with Modality-Specific Experts for Financial","url":"https://www.arxiv.org/pdf/2509.19628"},{"title":"Predicting the Performance of Multilingual NLP Models","url":"https://arxiv.org/pdf/2110.08875"},{"title":"Learning to vary: Teaching LMs to reproduce human linguistic variability in next-word prediction","url":"https://arxiv.org/pdf/2509.17794"},{"title":"Large Language Models 2024 Year in Review and 2025 Trends | Psychology Today","url":"https://www.psychologytoday.com/us/blog/the-future-brain/202501/large-language-models-2024-year-in-review-and-2025-trends"},{"title":"The Future of NLP: Key Trends for 2025 & Beyond","url":"https://mediusware.com/blog/the-future-of-nlp-key-trends-for-2026"},{"title":"ProxyLM: Predicting Language Model Performance on Multilingual Tasks via   Proxy Models","url":"https://arxiv.org/pdf/2406.09334"}]

Based on the search results, here's what I found regarding predictive multiplicity in language models during 2024-2025:

## Multi-Token Prediction

Multi-token prediction implicitly assigns weights to training tokens depending on how closely they are correlated with their successors. This represents a key development in 2024 for improving language model efficiency and performance.

## Multi-Label Learning in NLP

Recent work has explored multi-label approaches in language modeling. Multi-label fine-tuning has been adopted in NLP, primarily for classification tasks. More specifically, recent work has applied instruction fine-tuning for multi-label text classification tasks and tasks with restricted outcome spaces, such as sampling from discrete distributions.

Additionally, work has focused on generative tasks of predicting complete wordforms by stringing together tokens, with a countably infi
…[truncated 758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6526
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-22T05:52:48.483090+00:00_

Web search results for query: "McCoy et al 2020 "BERTs of a feather" seed variability NLP models"

Links: [{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance - ACL Anthology","url":"https://aclanthology.org/2020.blackboxnlp-1.21/"},{"title":"BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Request PDF","url":"https://www.researchgate.net/publication/347236013_BERTs_of_a_feather_do_not_generalize_together_Large_variability_in_generalization_across_models_with_similar_test_set_performance"},{"title":"[1911.02969] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance","url":"https://arxiv.org/abs/1911.02969"},{"title":"Home - Tom McCoy","url":"https://rtmccoy.com/pubs/"},{"title":"BERTs of a feather do not generalize together: Large variability in","url":"https://tallinzen.net/media/papers/mccoy_min_linzen_2019_berts_of_a_feather.pdf"},{"title":"BERTs of a feather do not generalize together: Large variability in   generalization across models with similar test set performance","url":"https://arxiv.org/pdf/1911.02969"},{"title":"[PDF] BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BERTs-of-a-feather-do-not-generalize-together:-in-McCoy-Min/48689c4bb52a45c0bc97d1421d72d11bab6c346b"},{"title":"dblp: BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance.","url":"https://dblp.org/rec/journals/corr/abs-1911-02969.html"}]

I found the paper! Here's information about McCoy et al. 2020's "BERTs of a feather" research:

## Paper Details

The paper is titled "BERTs of a feather do not generalize together: Large 
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6776
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-22T05:52:49.286274+00:00_

Web search results for query: "hybrid linear recurrent attention architecture evaluation comparison 2025 2026"

Links: [{"title":"Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://arxiv.org/html/2601.22156v1"},{"title":"(PDF) Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://www.researchgate.net/publication/400236907_Hybrid_Linear_Attention_Done_Right_Efficient_Distillation_and_Effective_Architectures_for_Extremely_Long_Contexts"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"Hybrid RNN-Attention: Efficiency Gains Are Real, Revolution Isn't | Brain Bytes Lab","url":"https://brainbyteslab.org/articles/olmo-hybrid-rnn-attention-architecture/"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE","url":"https://arxiv.org/pdf/2510.26692"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention","url":"https://arxiv.org/html/2602.01763v1"}]

Based on the search results, here are the key findings on hybrid linear recurrent attention architecture evaluations and comparisons from 2025-2026:

## Recent Research and Approaches

Multiple approaches have emerged for selecting which attention layers to convert to RNN layers: Yang et al. (2026) use output distribution shift metrics, Hoshino et al. (2025) propose a redundancy metric, and Gu et al. (2025) rely on performance drop on certain tasks. KL-guided layer selection (KL-LS) by Li et al. (2025) proposes using KL-divergence from the teacher model as the importance metric.

## Performance Recommendations

Language modeling remains stable
…[truncated 961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8082
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-22T05:52:56.288000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Finley Macdonald Pimentel 2025 \"convergence and divergence\" language models seeds EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Finley Macdonald Pimentel 2025 \"convergence and divergence\" language models seeds EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-22T05:52:56.591816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hsu Calmon 2022 \"Rashomon capacity\" predictive multiplicity classification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hsu Calmon 2022 \"Rashomon capacity\" predictive multiplicity classification"
  }
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-22T05:52:57.043872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "per-example disagreement model comparison NLP 2024 2025 instance-level prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "per-example disagreement model comparison NLP 2024 2025 instance-level prediction"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-22T05:53:02.113550+00:00_

Web search results for query: "Hsu Calmon 2022 "Rashomon capacity" predictive multiplicity classification"

Links: [{"title":"[PDF] Rashomon Capacity: A Metric for Predictive Multiplicity in Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Rashomon-Capacity:-A-Metric-for-Predictive-in-Hsu-Calmon/a7c5505ecf92a1a7fa31c9e7142014da817411be"},{"title":"Rashomon Capacity: A Metric for Predictive Multiplicity in Probabilistic Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Rashomon-Capacity:-A-Metric-for-Predictive-in-Hsu-Calmon/8628a8e308e9b0fe43fa426d9461d1de1ba2c284"},{"title":"GitHub - HsiangHsu/rashomon-capacity: Measure how near-equivalent classifiers disagree through Rashomon Capacity and predictive multiplicity estimation. · GitHub","url":"https://github.com/HsiangHsu/rashomon-capacity"},{"title":"Rashomon Capacity: A Metric for Predictive Multiplicity in Classification","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/ba4caa85ecdcafbf9102ab8ec384182d-Abstract-Conference.html"},{"title":"[2206.01295v1] Rashomon Capacity: A Metric for Predictive Multiplicity in Probabilistic Classification","url":"https://arxiv.org/abs/2206.01295v1"},{"title":"[2206.01295] Rashomon Capacity: A Metric for Predictive Multiplicity in Classification","url":"https://arxiv.org/abs/2206.01295"},{"title":"ICML Rashomon Capacity: Measuring Predictive Multiplicity in Probabilistic Classification","url":"https://icml.cc/virtual/2022/21391"},{"title":"[2206.01295v2] Rashomon Capacity: A Metric for Predictive Multiplicity in Classification","url":"https://arxiv.org/abs/2206.01295v2"},{"title":"Rashomon Capacity: A Metric for Predictive Multiplicity in Classification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220601295H/abstract"},{"title":"Rashomon Capacity: A Metric for Predictive Multiplicity in   Classification","url":"https://arxiv.org/pdf/2206.01295"}]

Based on the search results, I found detailed
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5521
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-22T05:53:02.264715+00:00_

Web search results for query: "Finley Macdonald Pimentel 2025 "convergence and divergence" language models seeds EMNLP"

Links: [{"title":"Convergence and Divergence of Language Models under Different Random Seeds - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1675/"},{"title":"Convergence and Divergence of Language Models under Different Random Seeds | Request PDF","url":"https://www.researchgate.net/publication/397424372_Convergence_and_Divergence_of_Language_Models_under_Different_Random_Seeds"},{"title":"Convergence and Divergence of Language Models under Different Random Seeds","url":"https://arxiv.org/pdf/2509.26643"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13100&show=100"},{"title":"Convergence and Divergence of Language Models under Different Random Seeds - Paper Detail","url":"https://deeplearn.org/arxiv/640820/convergence-and-divergence-of-language-models-under-different-random-seeds"},{"title":"CV - Tiago Pimentel","url":"https://tpimentelms.github.io/cv/"},{"title":"[2509.26643v1] Convergence and Divergence of Language Models under Different Random Seeds","url":"https://arxiv.org/abs/2509.26643v1"},{"title":"[2509.26643] Convergence and Divergence of Language Models under Different Random Seeds","url":"https://arxiv.org/abs/2509.26643"}]

I found the paper you're looking for! Here are the key details:

**Title:** Convergence and Divergence of Language Models under Different Random Seeds

**Authors:** Finlay Fehlauer, Kyle Mahowald, and Tiago Pimentel

**Publication:** Published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 32982–32991, Suzhou, China

**Main Focus:** The paper investigates the convergence of language models trained under different random seeds, measuring convergence as the expected per-token Kullback–Leibler (KL) divergence across seeds.

**Key Findings:** The authors identify a four-phase convergence pattern: (i) an initial
…[truncated 669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5976
}
```

</details>

---


### Tool result

_source line 625 · 2026-05-22T05:53:04.222196+00:00_

Web search results for query: "per-example disagreement model comparison NLP 2024 2025 instance-level prediction"

Links: [{"title":"MSA at BEA 2025 Shared Task: Disagreement-Aware ...","url":"https://aclanthology.org/2025.bea-1.95.pdf"},{"title":"Modeling disagreement in automatic data labeling for semi-supervised learning in Clinical Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11480042/"},{"title":"Frontiers | Modeling disagreement in automatic data labeling for semi-supervised learning in Clinical Natural Language Processing","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1374162/full"},{"title":"Hypernetworks for Perspectivist Adaptation","url":"https://aclanthology.org/2025.nlperspectives-1.10.pdf"},{"title":"Opt-ICL at LeWiDi-2025: Maximizing In-Context Signal from Rater Examples via Meta-Learning","url":"https://arxiv.org/pdf/2510.07105"},{"title":"Learning-From-Disagreement: A Model Comparison and Visual Analytics   Framework","url":"https://arxiv.org/pdf/2201.07849"},{"title":"Can Large Language Models Capture Dissenting Human Voices?","url":"https://arxiv.org/pdf/2305.13788"},{"title":"Effective Proxy for Human Labeling: Ensemble Disagreement Scores in   Large Language Models for Industrial NLP","url":"https://arxiv.org/pdf/2309.05619"}]

Based on the web search results, I found several relevant papers and research related to disagreement modeling and NLP in 2024-2025:

## Key Findings:

**Recent Disagreement-Aware NLP Work (2024-2025):**

A BEA 2025 shared task paper presents disagreement-aware instruction tuning for evaluating LLMs, with a framework including LoRA-based fine-tuning and disagreement-aware ensemble inference.

The LeWiDi-2025 competition addressed NLP tasks involving subjectivity and annotator disagreement, with a system leveraging language models' in-context learning abilities and meta-learning for modeling human variation.

**Disagreement Modeling Appr
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7178
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-22T05:53:09.793057+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Bai Zhe 2025 \"systematic analysis\" hybrid linear attention model zoo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Bai Zhe 2025 \"systematic analysis\" hybrid linear attention model zoo"
  }
}
```

</details>

---


### Tool call

_source line 627 · 2026-05-22T05:53:10.746809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sellam et al 2022 \"multiberts\" multiverse analysis BERT training variance ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sellam et al 2022 \"multiberts\" multiverse analysis BERT training variance ICLR"
  }
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-22T05:53:10.847564+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Swayamdipta et al 2020 \"dataset cartography\" per-example dynamics training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Swayamdipta et al 2020 \"dataset cartography\" per-example dynamics training"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T05:53:18.127203+00:00_

Web search results for query: "Wang Bai Zhe 2025 "systematic analysis" hybrid linear attention model zoo"

Links: [{"title":"[Quick Review] A Systematic Analysis of Hybrid Linear Attention","url":"https://liner.com/review/systematic-analysis-hybrid-linear-attention"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"}]

I found the research paper you're looking for! The paper "A Systematic Analysis of Hybrid Linear Attention" was authored by Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, and Jason Eshraghian.

Here are the key details about this 2025 research:

**Paper Overview:**
The paper addresses how transformers face quadratic complexity and memory issues with long sequences, with linear attention mechanisms using fixed-size hidden states, though linear models often suffer from limited recall performance. Despite extensive hybrid architecture research, the choice of linear attention component had not been deeply explored.

**Method
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8334
}
```

</details>

---


### Tool result

_source line 630 · 2026-05-22T05:53:18.178011+00:00_

Web search results for query: "Sellam et al 2022 "multiberts" multiverse analysis BERT training variance ICLR"

Links: [{"title":"Under review as a conference paper at ICLR 2022","url":"https://openreview.net/references/pdf?id=xppEu5lixO"},{"title":"Published as a conference paper at ICLR 2022","url":"https://openreview.net/pdf?id=K0E_F0gFDgA"},{"title":"ICLR 2022 The MultiBERTs: BERT Reproductions for Robustness Analysis Spotlight","url":"https://iclr.cc/virtual/2022/spotlight/6292"},{"title":"THE MULTIBERTS: BERT REPRODUCTIONS FOR ROBUSTNESS ANALYSIS - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/the-multiberts-bert-reproductions-for-robustness-analysis"},{"title":"Google at ICLR 2022 – Google Research Blog","url":"https://ai.googleblog.com/2022/04/google-at-iclr-2022.html"},{"title":"[PDF] The MultiBERTs: BERT Reproductions for Robustness Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-MultiBERTs%3A-BERT-Reproductions-for-Robustness-Sellam-Yadlowsky/646fc03a20a6a00304d9768621a8b864aa769f21"},{"title":"[2106.16163] The MultiBERTs: BERT Reproductions for Robustness Analysis","url":"https://arxiv.org/abs/2106.16163"},{"title":"the multiberts: bert reproductions for robustness analysis","url":"https://arxiv.org/pdf/2106.16163"}]

Based on the search results, I found comprehensive information about this paper:

## Summary of Sellam et al. 2022 - "The MultiBERTs"

The MultiBERTs paper introduces a set of 25 BERT-Base checkpoints, trained with similar hyper-parameters as the original BERT model but differing in random weight initialization and shuffling of training data.

### Key Contributions

The paper defines the Multi-Bootstrap, a non-parametric bootstrap method for statistical inference designed for settings where there are multiple pre-trained models and limited test data.

### Motivation

Experiments with pre-trained models such as BERT are often based on a single checkpoint, while the conclusions drawn apply to t
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7431
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-22T05:53:24.222362+00:00_

Web search results for query: "Swayamdipta et al 2020 "dataset cartography" per-example dynamics training"

Links: [{"title":"Dataset cartography: Mapping and diagnosing datasets with training dynamics","url":"https://www.mendeley.com/catalogue/5ef551f0-f6e4-3329-a092-e574463bf2b6/"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.746/"},{"title":"Dataset cartography: Mapping and diagnosing datasets with training dynamics - The Hebrew University of Jerusalem","url":"https://cris.huji.ac.il/en/publications/dataset-cartography-mapping-and-diagnosing-datasets-with-training/"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Request PDF","url":"https://www.researchgate.net/publication/347237029_Dataset_Cartography_Mapping_and_Diagnosing_Datasets_with_Training_Dynamics"},{"title":"[2009.10795] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics","url":"https://arxiv.org/abs/2009.10795"},{"title":"[PDF] Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dataset-Cartography:-Mapping-and-Diagnosing-with-Swayamdipta-Schwartz/ee5fff85d3ec62698eddba162f054b7e73670b2a"},{"title":"Diagnosing Medical Datasets with Training Dynamics","url":"https://arxiv.org/html/2411.01653v1"},{"title":"GitHub - beyondguo/TrainingDynamics: Compute training dynamics, plot data cartography, analysing data quality...","url":"https://github.com/beyondguo/TrainingDynamics"},{"title":"GitHub - allenai/cartography: Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics · GitHub","url":"https://github.com/allenai/cartography"},{"title":"Dataset Cartography: Mapping and Diagnosing Datasets with Training   Dynamics","url":"https://arxiv.org/pdf/2009.10795"}]

I found the paper you're looking for! Here's what I found:

Swayamdipta et a
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 13374
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-22T05:54:58.184438+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, how to evaluate soundness, excitement, novelty, and any specific guidance about what constitutes a good vs. poor review. Include any guidance about Findings vs Main Conference criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including what reviewers should focus on, how to evaluate soundness, excitement, novelty, and any specific guidance about what constitutes a good vs. poor review. Include any guidance about Findings vs Main Conference criteria."
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-22T05:55:08.477852+00:00_

# ARR Reviewer Guidelines: Core Evaluation Framework

## Primary Review Tasks

Reviewers complete four essential tasks:

1. **Calendar allocation** for both reviewing and discussion periods
2. **Assignment verification** (expertise, conflicts of interest, desk-rejection criteria)
3. **Review composition** with specific quality standards
4. **Post-response assessment** incorporating author clarifications

## Evaluation Dimensions

### Soundness Assessment
Reviewers provide soundness scores that must align with review content. Low soundness ratings require explicit justification through identified technical flaws. This prevents unconscious bias from inflating or deflating assessments without supporting evidence.

### Excitement vs. Soundness
These represent orthogonal dimensions. A technically sound paper may lack personal interest (lower excitement), while an exciting paper could have methodological concerns. The guidelines emphasize that "excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons."

### Overall Recommendation
This composite score balances soundness, excitement, novelty, and potential impact. Importantly, papers can merit main conference acceptance despite low personal excitement if they offer significant contributions like efficiency improvements or resources for underserved languages.

## Key Review Quality Standards

**Specificity Requirements:**
Vague critiques like "missing relevant references" must become "missing references XYZ." Reviews should be understandable to area chairs without requiring full paper re-reading.

**Common Review Pitfalls (H1-H17):**
The guidelines identify problematic patterns including:
- Dismissing results as "unsurprising" despite lacking community awareness
- Requiring SOTA results when novelty exists in other dimensions
- Criticizing appropriate simplicity
- Suggesting unnecessary experiments beyond claim scope

**Professional Tone:**
"Write the review you would like to get you
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10293
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-22T05:55:23.298519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model multiplicity\" \"architecture comparison\" per-instance disagreement language model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model multiplicity\" \"architecture comparison\" per-instance disagreement language model 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 635 · 2026-05-22T05:55:23.298890+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ding Ngo Du 2025 \"reconciling model multiplicity\" downstream decision ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ding Ngo Du 2025 \"reconciling model multiplicity\" downstream decision ICLR"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-22T05:55:29.510841+00:00_

Web search results for query: "Ding Ngo Du 2025 "reconciling model multiplicity" downstream decision ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2025 RECONCILING MODEL MULTIPLICITY","url":"https://openreview.net/pdf?id=uy4EavBEwl"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making | OpenReview","url":"https://openreview.net/forum?id=uy4EavBEwl"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making","url":"https://arxiv.org/html/2405.19667v1"},{"title":"[2405.19667] Reconciling Model Multiplicity for Downstream Decision Making","url":"https://arxiv.org/abs/2405.19667"},{"title":"[Quick Review] Reconciling Model Multiplicity for Downstream Decision Making","url":"https://liner.com/review/reconciling-model-multiplicity-for-downstream-decision-making"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making | Request PDF","url":"https://www.researchgate.net/publication/381006777_Reconciling_Model_Multiplicity_for_Downstream_Decision_Making"},{"title":"Reconciling Predictive Multiplicity in Practice","url":"https://arxiv.org/html/2501.16549v1"},{"title":"Carnegie Mellon University at ICLR 2025 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2025/04/23/carnegie-mellon-university-at-iclr-2025/"},{"title":"Reconciling Predictive Multiplicity in Practice | Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/10.1145/3715275.3732216"}]

I found the paper you're looking for. Here's what I found:

"Reconciling Model Multiplicity for Downstream Decision Making" addresses the problem where decision-makers have multiple predictive models with nearly equivalent squared loss but may lead to vastly different best-response actions for a significant number of individuals in the population.

The paper is authored by Ally Yalei Du (Carnegie Mellon University), Daniel Ngo (University of Minnesota), and Zh
…[truncated 783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6211
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T05:55:31.475438+00:00_

Web search results for query: ""model multiplicity" "architecture comparison" per-instance disagreement language model 2024 2025"

Links: [{"title":"Architectural and Methodological Advancements in Large Language Models","url":"https://www.mdpi.com/2673-4591/97/1/8"},{"title":"The Big LLM Architecture Comparison - Ahead of AI","url":"https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison"},{"title":"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights","url":"https://arxiv.org/html/2510.04800v1"},{"title":"Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12707437/"},{"title":"DeMeVa at LeWiDi-2025: Modeling Perspectives with In-Context Learning and Label Distribution Learning","url":"https://arxiv.org/pdf/2509.09524"},{"title":"Large language model - Wikipedia","url":"https://en.wikipedia.org/wiki/Large_language_model"},{"title":"What Makes Two Language Models Think Alike?","url":"https://arxiv.org/pdf/2406.12620"}]

Based on the search results, here's what I found regarding your query about "model multiplicity," "architecture comparison," and per-instance disagreement in language models for 2024-2025:

## Architecture Comparisons

The current literature lacks openly shared, in-depth analysis of hybridization strategies in hybrid architectures, with most prior works focusing on introducing specific hybrid architectures rather than providing detailed, systematic comparisons across possible hybridization approaches. Recent work addresses this by conducting a holistic evaluation of hybrid architectures via comprehensive, multi-faceted comparisons.

Looking back at GPT-2 (2019) and forward to DeepSeek V3 and Llama 4 (2024-2025), one might be surprised at how structurally similar these models still are.

## Per-Instance Disagreement & Learning with Disagreement

Customary approaches that aggregate d
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8176
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T05:57:54.105966+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文标题**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 via ARR May cycle\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规 + Excitement\n\n---\n\n## Paper Summary\n\n本文研究 hybrid linear recurrent architectures（将 attention 与线性递归结合的模型）在 per-example 级别的预测行为差异。利用 Wang et al. (2025) 提供的 controlled model zoo（3种架构：GatedDeltaNet, RetNet, HGRN2；5种 attention ratio；2种 scale：340M, 1.3B），在 10 个 benchmark 上系统评估 per-example predictive multiplicity。主要发现：(1) ambiguity α 随任务类型在 0.14–0.30 之间变化；(2) pairwise Jaccard 始终很低（≤ 0.10）；(3) 在 LAMBADA 上，aggregate variance 随 attention 递减但 per-example overlap 在首个 attention level 即饱和（decoupling 现象）；(4) 不同架构影响不同的 example 子集，但 attention weight 分析未显示 helped/hurt examples 的系统性差异。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 主要 claims 有充分的统计支撑（permutation test, Bonferroni correction, bootstrap CI），但最核心的 confound（架构 vs. 随机种子，每个配置仅单次训练）未被充分解决，显著削弱了\"architecture-driven\"的因果推断 |\n| **Excitement** | 2.5 / 5 | 对 hybrid architecture 选型的实践者有一定价值，但主要结果（不同架构在 per-example 级别不一致）在 predictive multiplicity 文献框架下可预期；最核心的 decoupling 发现仅在 LAMBADA 上成立 |\n| **Reproducibility** | 4 / 5 | 使用公开 model zoo，实验设置详细（§3），统计方法清晰（§3.5），Appendix 提供大量补充分析。但未提供代码/数据处理脚本 |\n| **Overall Assessment** | **3.0** — Findings | 扎实的 empirical study，分析深度和覆盖面值得肯定，但新颖性有限（将现有 metrics 应用于新 domain），且架构-种子 confound 和 LAMBADA-centric 的核心发现限制了 impact |\n| **Confidence** | 4 / 5 | 熟悉 predictive multiplicity、hybrid architecture、per-example analysis 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 架构效应 vs. 种子效应的 confound 未充分处理\n\n- **具体位置**: §3 Method（整体实验设计）、§5 Limitations（第2段 \"Methodological constraints\"）\n- **问题**: 每个 architecture × attention ratio × scale 配置仅有一次训练（single training run）。论文声称研究的是 architecture-driven multiplicity，但无法排除观察到的 per-example 差异部分来自随机初始化差异。论文在 Limitations 中承认 \"we cannot fully disentangle architectural from seed-specific effects\"，并用 §4.3 的 \"3× Jaccard gap\"（cross-architecture Jaccard ≈ 0.03–0.07 vs. within-architecture ≈ 0.10）作为 proxy evidence。然而，within-architecture 比较中只改变了 attention ratio 而共享同一 backbone，这本身就预期会有更高 overlap，因此 3× gap 并不能排除 seed 的贡献。\n- **为什么影响接收**: 这是论文核心 claim 的因果推断基础。Predictive multiplicity 文献（D'Amour et al., 2022; McCoy et al., 2020; Finley et al., 2025）已充分证明 seed 可导致显著 per-example 差异。没有多 seed 对照，读者无法判断架构差异的 effect size 占多大比例。\n- **建议修改方向**: (a) 即使只对少数配置（如 h3-1 at 1.3B）补充 2-3 个不同 seed 的训练，即可给出 within-architecture cross-seed Jaccard 作为 baseline；(b) 若无法获取额外训练 run，应在正文（不仅 Limitations）显著弱化因果表述，将 framing 从 \"architecture-driven multiplicity\" 调整为 \"multiplicity observed across architectures under fixed zoo conditions\"。\n\n**N2** [critical] 核心发现（decoupling）的 generalizability 不足\n\n- **具体位置**: §4.1 (Table 1), §4.3 (Decoupling), §5 Conclusion\n- **问题**: 论文最具新颖性的发现是 aggregate convergence 与 per-example divergence 的 decoupling——aggregate σ 随 attention 递减但 Jaccard 不随之增加。然而这一 pattern 主要基于 LAMBADA 一个 benchmark。论文自己在 §4.1 明确指出：\"LAMBADA (ρ = 0.30) is the only benchmark exhibiting monotonic convergence\"（Table 1 中 BoolQ ρ=−1.0，PIQA 无显著趋势，HellaSwag 无单调性）。Conclusion 将此描述为一般性发现 (\"aggregate variance decreases with attention while per-example overlap saturates\")，但这仅在 LAMBADA 上成立。\n- **为什么影响接收**: 单一 benchmark 上的 finding 难以支撑论文的 general claim。如果 decoupling 仅在特定 task type（long-range cloze completion）上出现，这是一个 task-specific observation 而非 general principle。\n- **建议修改方向**: (a) 在 Conclusion 中明确限定 decoupling 发现的适用范围（specifically LAMBADA/retrieval tasks）；(b) 分析为什么 LAMBADA 特殊——论文在 §4.1 提到 LAMBADA \"requires predicting a final word from long-range context\"，可以将此作为 mechanistic hypothesis 深入讨论；(c) 检验 decoupling 是否在其他 retrieval-like tasks 上复现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 新颖性定位需要更精确的 framing\n\n- **具体位置**: §1 Introduction（\"We present the first systematic per-example analysis...\"）, Abstract\n- **问题**: 论文的主要方法论（α metric from Marx et al. 2020, Jaccard similarity, helped/hurt decomposition）均为现有工具的直接应用。核心贡献在于 \"applying existing metrics to a new domain\"（hybrid recurrent architectures）。这本身有价值，但论文的 framing 有时暗示了更大的方法论贡献。McCoy et al. (2020) 已在 seed-driven 设置下做了类似的 per-example divergence 分析（albeit 在 BERT/MNLI 上）；Finley et al. (2025) 研究了 seed 下的 convergence/divergence pattern。本文的增量是扩展到 architecture-driven variation 和 hybrid recurrent models，但许多发现（不同模型在 per-example 级别不一致）在先验上并不令人意外。\n- **建议**: Introduction 和 Abstract 中更诚实地定位 novelty：\"We are the first to quantify per-example multiplicity across hybrid architectures\"（而非暗示全新的分析框架）。突出真正 unexpected 的发现（如 LAMBADA decoupling、attention saturation at h3-1）。\n\n**W2** [major] 缺少与 seed-driven multiplicity 的 quantitative comparison\n\n- **具体位置**: §2 Related Work, §4 Experiments\n- **问题**: 论文讨论了 McCoy et al. (2020), Finley et al. (2025), Sellam et al. (2022) 等 seed-driven 工作，但未提供 quantitative comparison。读者无法判断：architecture-driven multiplicity 相比 seed-driven multiplicity 有多大？α = 0.14–0.30 相比同架构不同 seed 的 α 是更大还是更小？这个对比对于评估论文的 practical significance 至关重要。\n- **建议**: 至少引用上述文献中报告的 seed-driven multiplicity 数值进行 contextual comparison，即使实验设置不完全可比。\n\n**W3** [minor-to-major] Predictive multiplicity 概念在本文语境下的适用性\n\n- **具体位置**: Title, §1, §2\n- **问题**: Predictive multiplicity（Marx et al., 2020）最初定义为\"models with near-identical aggregate performance that give conflicting per-example predictions\"，通常指同一 pipeline/hypothesis class 内的模型。本文比较的是不同架构的模型（GatedDeltaNet vs. RetNet vs. HGRN2），它们在设计上就不同。将此称为 \"predictive multiplicity\" 虽不错误，但可能引起概念混淆——这更接近 \"cross-architecture disagreement\" 或 \"model comparison\"。\n- **建议**: 在 §1 或 §2 早期明确讨论这一概念延伸的合理性和边界。\n\n**W4** [minor] 实践指导不足\n\n- **具体位置**: §5 Conclusion\n- **问题**: 论文在 Conclusion 中简要提到 \"per-example analysis tools ... may inform practitioners\"，但未给出具体指导。发现了 per-example multiplicity 之后，practitioners 应该怎么做？是用 ensemble？选特定架构？在特定 task 上用特定 attention ratio？\n- **建议**: 添加 1-2 段具体的 practical recommendations 或 future directions。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 信息密度过高**: \"the ambiguity α (Marx et al., 2020) ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA)\" 过于具体，可改为更高层次的概括（如 \"varies 2× across tasks\"）。\n\n2. **Table 1 可读性**: 10 个 benchmark × 多个指标，信息量大但 pattern 难以一眼看出。考虑增加 heatmap 或 visual summary。\n\n3. **§3.4 per-example decomposition 的 binary threshold**: Helped/hurt 的二元分类（correct in hybrid but not pure, or vice versa）丢失了连续性信息（如 probability 变化幅度）。论文在 §4.2 提到 \"the binarization discards continuous probability information\"，但可以考虑补充 continuous measure 的结果。\n\n4. **部分引用可能需要更新**: 若部分 arXiv preprint（如 Arora et al., 2024a/b; Yang et al., 2024）已在 venue 发表，应更新为正式版本。\n\n5. **Appendix F.2 (Helped vs. Hurt Attention Entropy)**: Table 5 显示 entropy difference negligible（GDN -0.0009, RetNet -0.0179, HGRN2 +0.0020）。这一 null result 可在正文 §4.2 中更显著地讨论，因为它约束了\"attention mechanism drives per-example effects\"这一 hypothesis。\n\n---\n\n## Missing References（可能遗漏的相关工作）\n\n1. **Lindström et al. (2024) \"What Makes Two Language Models Think Alike?\"** — 跨架构（encoder, decoder, Mamba）per-layer representation 相似性比较，与本文的 cross-architecture per-example 比较直接相关。\n\n2. **\"Reconciling Predictive Multiplicity in Practice\" (FAccT 2025)** — predictive multiplicity 的实践解决方案，与本文发现的 multiplicity 问题互补。\n\n3. **\"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights\" (arXiv:2510.04800, 2025)** — 另一 hybrid architecture 系统分析，可能在实验设计上有可借鉴之处。\n\n4. 论文引用了 Swayamdipta et al. (2020) dataset cartography，但 per-example analysis 领域还有 **Pleiss et al. (2020) \"Identifying Mislabeled Data\"** 等使用 training dynamics 的工作，可作为方法论 context。\n\n---\n\n## 主要优势\n\n1. **问题选择及时且实践相关**: 随着 hybrid linear recurrent architectures（Mamba, RWKV, Griffin 等）日益普及，理解它们在 per-example 级别的行为差异对模型选型和 deployment 至关重要。\n\n2. **实验设计严谨**: 利用 controlled model zoo（matched training data, tokenizer, hyperparameters）有效控制了混淆变量，使 architecture 成为主要变量（seed confound 除外）。\n\n3. **统计方法全面**: Permutation test（§3.5）、Bonferroni correction（Appendix A）、bootstrap CI、多种 effect size measures 的组合使用体现了统计严谨性。\n\n4. **分析深度超越 metric application**: 不仅报告 α 和 Jaccard，还进行了 helped/hurt decomposition（§4.2）、cross-scale comparison（Appendix Q）、attention weight analysis（Appendix E-F）、robustness analysis（§4.4）等，形成了比较完整的分析链。\n\n5. **写作清晰**: Section 结构逻辑清楚，从 aggregate 到 per-example 到 decoupling 的递进叙事有效。\n\n6. **Limitations 诚实**: 三个 limitation points（coverage, methodological constraints, pre-training only）覆盖了主要弱点，符合 EMNLP 要求。\n\n---\n\n## EMNLP 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ✅ 合规 | §1-5 (Conclusion) 在第 8 页结束，Limitations 开始于第 8 页底部 |\n| Limitations 必需 | ✅ 合规 | 第 8-9 页，覆盖 3 个 points |\n| Ethics Statement | ✅ 合规 | 第 9 页，简短但充分 |\n| 匿名处理 | ✅ 合规 | \"Anonymous ACL submission\"，未见 de-anonymizing 信息 |\n| Figure/Table 字号 | ✅ 合规 | 图表文字可读，≥ 80% body text |\n| References 格式 | ⚠️ 部分 | 部分 arXiv preprint 可能已有正式 venue 版本需更新 |\n| ACL style template | ✅ 合规 | 使用 `\\usepackage[review]{acl}` |\n\n---\n\n## 总体评分\n\n**Overall**: **3.0 — Findings**\n\n**一句话总结**: 一篇扎实的 empirical study，系统性地将 predictive multiplicity 分析框架应用于 hybrid recurrent architectures，分析深度值得肯定，但架构-种子 confound 削弱了核心 claim 的因果推断，且最具新颖性的 decoupling 发现仅在 LAMBADA 上成立，新颖性和 impact 更适合 Findings track。\n\n**Confidence**: 4/5",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文标题**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 via ARR May cycle\n**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + 格式合规 + Excitement\n\n---\n\n## Paper Summary\n\n本文研究 hybrid linear recurrent architectures（将 attention 与线性递归结合的模型）在 per-example 级别的预测行为差异。利用 Wang et al. (2025) 提供的 controlled model zoo（3种架构：GatedDeltaNet, RetNet, HGRN2；5种 attention ratio；2种 scale：340M, 1.3B），在 10 个 benchmark 上系统评估 per-example predictive multiplicity。主要发现：(1) ambiguity α 随任务类型在 0.14–0.30 之间变化；(2) pairwise Jaccard 始终很低（≤ 0.10）；(3) 在 LAMBADA 上，aggregate variance 随 attention 递减但 per-example overlap 在首个 attention level 即饱和（decoupling 现象）；(4) 不同架构影响不同的 example 子集，但 attention weight 分析未显示 helped/hurt examples 的系统性差异。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3 / 5 | 主要 claims 有充分的统计支撑（permutation test, Bonferroni correction, bootstrap CI），但最核心的 confound（架构 vs. 随机种子，每个配置仅单次训练）未被充分解决，显著削弱了\"architecture-driven\"的因果推断 |\n| **Excitement** | 2.5 / 5 | 对 hybrid architecture 选型的实践者有一定价值，但主要结果（不同架构在 per-example 级别不一致）在 predictive multiplicity 文献框架下可预期；最核心的 decoupling 发现仅在 LAMBADA 上成立 |\n| **Reproducibility** | 4 / 5 | 使用公开 model zoo，实验设置详细（§3），统计方法清晰（§3.5），Appendix 提供大量补充分析。但未提供代码/数据处理脚本 |\n| **Overall Assessment** | **3.0** — Findings | 扎实的 empirical study，分析深度和覆盖面值得肯定，但新颖性有限（将现有 metrics 应用于新 domain），且架构-种子 confound 和 LAMBADA-centric 的核心发现限制了 impact |\n| **Confidence** | 4 / 5 | 熟悉 predictive multiplicity、hybrid architecture、per-example analysis 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 架构效应 vs. 种子效应的 confound 未充分处理\n\n- **具体位置**: §3 Method（整体实验设计）、§5 Limitations（第2段 \"Methodological constraints\"）\n- **问题**: 每个 architecture × attention ratio × scale 配置仅有一次训练（single training run）。论文声称研究的是 architecture-driven multiplicity，但无法排除观察到的 per-example 差异部分来自随机初始化差异。论文在 Limitations 中承认 \"we cannot fully disentangle architectural from seed-specific effects\"，并用 §4.3 的 \"3× Jaccard gap\"（cross-architecture Jaccard ≈ 0.03–0.07 vs. within-architecture ≈ 0.10）作为 proxy evidence。然而，within-architecture 比较中只改变了 attention ratio 而共享同一 backbone，这本身就预期会有更高 overlap，因此 3× gap 并不能排除 seed 的贡献。\n- **为什么影响接收**: 这是论文核心 claim 的因果推断基础。Predictive multiplicity 文献（D'Amour et al., 2022; McCoy et al., 2020; Finley et al., 2025）已充分证明 seed 可导致显著 per-example 差异。没有多 seed 对照，读者无法判断架构差异的 effect size 占多大比例。\n- **建议修改方向**: (a) 即使只对少数配置（如 h3-1 at 1.3B）补充 2-3 个不同 seed 的训练，即可给出 within-architecture cross-seed Jaccard 作为 baseline；(b) 若无法获取额外训练 run，应在正文（不仅 Limitations）显著弱化因果表述，将 framing 从 \"architecture-driven multiplicity\" 调整为 \"multiplicity observed across architectures under fixed zoo conditions\"。\n\n**N2** [critical] 核心发现（decoupling）的 generalizability 不足\n\n- **具体位置**: §4.1 (Table 1), §4.3 (Decoupling), §5 Conclusion\n- **问题**: 论文最具新颖性的发现是 aggregate convergence 与 per-example divergence 的 decoupling——aggregate σ 随 attention 递减但 Jaccard 不随之增加。然而这一 pattern 主要基于 LAMBADA 一个 benchmark。论文自己在 §4.1 明确指出：\"LAMBADA (ρ = 0.30) is the only benchmark exhibiting monotonic convergence\"（Table 1 中 BoolQ ρ=−1.0，PIQA 无显著趋势，HellaSwag 无单调性）。Conclusion 将此描述为一般性发现 (\"aggregate variance decreases with attention while per-example overlap saturates\")，但这仅在 LAMBADA 上成立。\n- **为什么影响接收**: 单一 benchmark 上的 finding 难以支撑论文的 general claim。如果 decoupling 仅在特定 task type（long-range cloze completion）上出现，这是一个 task-specific observation 而非 general principle。\n- **建议修改方向**: (a) 在 Conclusion 中明确限定 decoupling 发现的适用范围（specifically LAMBADA/retrieval tasks）；(b) 分析为什么 LAMBADA 特殊——论文在 §4.1 提到 LAMBADA \"requires predicting a final word from long-range context\"，可以将此作为 mechanistic hypothesis 深入讨论；(c) 检验 decoupling 是否在其他 retrieval-like tasks 上复现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] 新颖性定位需要更精确的 framing\n\n- **具体位置**: §1 Introduction（\"We present the first systematic per-example analysis...\"）, Abstract\n- **问题**: 论文的主要方法论（α metric from Marx et al. 2020, Jaccard similarity, helped/hurt decomposition）均为现有工具的直接应用。核心贡献在于 \"applying existing metrics to a new domain\"（hybrid recurrent architectures）。这本身有价值，但论文的 framing 有时暗示了更大的方法论贡献。McCoy et al. (2020) 已在 seed-driven 设置下做了类似的 per-example divergence 分析（albeit 在 BERT/MNLI 上）；Finley et al. (2025) 研究了 seed 下的 convergence/divergence pattern。本文的增量是扩展到 architecture-driven variation 和 hybrid recurrent models，但许多发现（不同模型在 per-example 级别不一致）在先验上并不令人意外。\n- **建议**: Introduction 和 Abstract 中更诚实地定位 novelty：\"We are the first to quantify per-example multiplicity across hybrid architectures\"（而非暗示全新的分析框架）。突出真正 unexpected 的发现（如 LAMBADA decoupling、attention saturation at h3-1）。\n\n**W2** [major] 缺少与 seed-driven multiplicity 的 quantitative comparison\n\n- **具体位置**: §2 Related Work, §4 Experiments\n- **问题**: 论文讨论了 McCoy et al. (2020), Finley et al. (2025), Sellam et al. (2022) 等 seed-driven 工作，但未提供 quantitative comparison。读者无法判断：architecture-driven multiplicity 相比 seed-driven multiplicity 有多大？α = 0.14–0.30 相比同架构不同 seed 的 α 是更大还是更小？这个对比对于评估论文的 practical significance 至关重要。\n- **建议**: 至少引用上述文献中报告的 seed-driven multiplicity 数值进行 contextual comparison，即使实验设置不完全可比。\n\n**W3** [minor-to-major] Predictive multiplicity 概念在本文语境下的适用性\n\n- **具体位置**: Title, §1, §2\n- **问题**: Predictive multiplicity（Marx et al., 2020）最初定义为\"models with near-identical aggregate performance that give conflicting per-example predictions\"，通常指同一 pipeline/hypothesis class 内的模型。本文比较的是不同架构的模型（GatedDeltaNet vs. RetNet vs. HGRN2），它们在设计上就不同。将此称为 \"predictive multiplicity\" 虽不错误，但可能引起概念混淆——这更接近 \"cross-architecture disagreement\" 或 \"model comparison\"。\n- **建议**: 在 §1 或 §2 早期明确讨论这一概念延伸的合理性和边界。\n\n**W4** [minor] 实践指导不足\n\n- **具体位置**: §5 Conclusion\n- **问题**: 论文在 Conclusion 中简要提到 \"per-example analysis tools ... may inform practitioners\"，但未给出具体指导。发现了 per-example multiplicity 之后，practitioners 应该怎么做？是用 ensemble？选特定架构？在特定 task 上用特定 attention ratio？\n- **建议**: 添加 1-2 段具体的 practical recommendations 或 future directions。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract 信息密度过高**: \"the ambiguity α (Marx et al., 2020) ranges from 0.14 (PIQA) through 0.15 (HellaSwag) and 0.21 (ARC-Easy) to 0.30 (LAMBADA)\" 过于具体，可改为更高层次的概括（如 \"varies 2× across tasks\"）。\n\n2. **Table 1 可读性**: 10 个 benchmark × 多个指标，信息量大但 pattern 难以一眼看出。考虑增加 heatmap 或 visual summary。\n\n3. **§3.4 per-example decomposition 的 binary threshold**: Helped/hurt 的二元分类（correct in hybrid but not pure, or vice versa）丢失了连续性信息（如 probability 变化幅度）。论文在 §4.2 提到 \"the binarization discards continuous probability information\"，但可以考虑补充 continuous measure 的结果。\n\n4. **部分引用可能需要更新**: 若部分 arXiv preprint（如 Arora et al., 2024a/b; Yang et al., 2024）已在 venue 发表，应更新为正式版本。\n\n5. **Appendix F.2 (Helped vs. Hurt Attention Entropy)**: Table 5 显示 entropy difference negligible（GDN -0.0009, RetNet -0.0179, HGRN2 +0.0020）。这一 null result 可在正文 §4.2 中更显著地讨论，因为它约束了\"attention mechanism drives per-example effects\"这一 hypothesis。\n\n---\n\n## Missing References（可能遗漏的相关工作）\n\n1. **Lindström et al. (2024) \"What Makes Two Language Models Think Alike?\"** — 跨架构（encoder, decoder, Mamba）per-layer representation 相似性比较，与本文的 cross-architecture per-example 比较直接相关。\n\n2. **\"Reconciling Predictive Multiplicity in Practice\" (FAccT 2025)** — predictive multiplicity 的实践解决方案，与本文发现的 multiplicity 问题互补。\n\n3. **\"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights\" (arXiv:2510.04800, 2025)** — 另一 hybrid architecture 系统分析，可能在实验设计上有可借鉴之处。\n\n4. 论文引用了 Swayamdipta et al. (2020) dataset cartography，但 per-example analysis 领域还有 **Pleiss et al. (2020) \"Identifying Mislabeled Data\"** 等使用 training dynamics 的工作，可作为方法论 context。\n\n---\n\n## 主要优势\n\n1. **问题选择及时且实践相关**: 随着 hybrid linear recurrent architectures（Mamba, RWKV, Griffin 等）日益普及，理解它们在 per-example 级别的行为差异对模型选型和 deployment 至关重要。\n\n2. **实验设计严谨**: 利用 controlled model zoo（matched training data, tokenizer, hyperparameters）有效控制了混淆变量，使 architecture 成为主要变量（seed confound 除外）。\n\n3. **统计方法全面**: Permutation test（§3.5）、Bonferroni correction（Appendix A）、bootstrap CI、多种 effect size measures 的组合使用体现了统计严谨性。\n\n4. **分析深度超越 metric application**: 不仅报告 α 和 Jaccard，还进行了 helped/hurt decomposition（§4.2）、cross-scale comparison（Appendix Q）、attention weight analysis（Appendix E-F）、robustness analysis（§4.4）等，形成了比较完整的分析链。\n\n5. **写作清晰**: Section 结构逻辑清楚，从 aggregate 到 per-example 到 decoupling 的递进叙事有效。\n\n6. **Limitations 诚实**: 三个 limitation points（coverage, methodological constraints, pre-training only）覆盖了主要弱点，符合 EMNLP 要求。\n\n---\n\n## EMNLP 格式合规检查\n\n| 检查项 | 状态 | 备注 |\n|--------|------|------|\n| 正文 ≤ 8 页 | ✅ 合规 | §1-5 (Conclusion) 在第 8 页结束，Limitations 开始于第 8 页底部 |\n| Limitations 必需 | ✅ 合规 | 第 8-9 页，覆盖 3 个 points |\n| Ethics Statement | ✅ 合规 | 第 9 页，简短但充分 |\n| 匿名处理 | ✅ 合规 | \"Anonymous ACL submission\"，未见 de-anonymizing 信息 |\n| Figure/Table 字号 | ✅ 合规 | 图表文字可读，≥ 80% body text |\n| References 格式 | ⚠️ 部分 | 部分 arXiv preprint 可能已有正式 venue 版本需更新 |\n| ACL style template | ✅ 合规 | 使用 `\\usepackage[review]{acl}` |\n\n---\n\n## 总体评分\n\n**Overall**: **3.0 — Findings**\n\n**一句话总结**: 一篇扎实的 empirical study，系统性地将 predictive multiplicity 分析框架应用于 hybrid recurrent architectures，分析深度值得肯定，但架构-种子 confound 削弱了核心 claim 的因果推断，且最具新颖性的 decoupling 发现仅在 LAMBADA 上成立，新颖性和 impact 更适合 Findings track。\n\n**Confidence**: 4/5",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T05:57:58.021417+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T05:58:02.799420+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 641 · 2026-05-22T05:58:02.902914+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-22T05:58:06.820809+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-22T05:58:06.871449+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 644 · 2026-05-22T05:58:13.042356+00:00_

Round 1 审稿报告已提交给 Review Director。

核心评判：**Overall 3.0 (Findings)**。两个 critical 问题：(1) 每个配置仅单次训练，无法分离 architecture effect 与 seed effect 的 confound；(2) 最核心的 decoupling 发现仅在 LAMBADA 一个 benchmark 上成立，generalizability 不足。论文分析深度和统计严谨性值得肯定，但新颖性有限（现有 metrics 应用于新 domain），更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

2 recorded events


### User

_source line 645 · 2026-05-22T05:59:37.708022+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 评分
Overall: 3.0 (Findings) | Soundness 3.0/5 | Excitement 3.0/5 | Reproducibility 4/5 | Confidence 4/5

### Must-Fix 问题

**R1-N1** [Critical] 单次训练 confound 与 architecture-specificity claims 之间的根本矛盾
- Wang et al. model zoo 每个配置仅一次训练。核心 claim "不同架构影响不同 example 子集"（low Jaccard）无法区分来自 architecture 还是 seed。Appendix K 的 permutation test 证明 J > random baseline，但此 baseline 是对 example identity 的 random permutation，非 seed variation baseline。真正需要的是同一架构不同 seed 的 Jaccard（seed-level J）。

**R1-N2** [Critical] LAMBADA convergence 统计证据不足以支撑其突出地位
- Bonferroni-adjusted p = .100（未达 α=.05）
- 排除 GDN 后 ρ 从 -1.0 降至 -0.7, p = .233（完全不显著）
- 10 个 benchmark 仅此一个显示 pattern
- GDN h3-1 用 16 heads vs 其他 32 heads
- 综合看，convergence 应定位为 "exploratory observation" 而非 "suggestive evidence"

### Should-Fix 问题

**R1-W1** [Major] Confirmatory/exploratory benchmark split 缺乏 pre-registration
- 论文承认无外部时间戳。选择哪些进入 confirmatory set 可能受数据影响。对全部 10 个 benchmark 做 Bonferroni 则 LAMBADA adj-p = 0.17。

**R1-W2** [Major] Format confound 未被系统分析
- Task taxonomy 可能反映 evaluation format 差异而非 cognitive demand。LAMBADA（open-ended）α=0.30 vs PIQA（2-choice）α=0.14。缺乏 format × task type 交叉分析。

**R1-W3** [Major] Bootstrap CIs 实际覆盖率问题
- n=3 的 BCa bootstrap 最多 27 个唯一 resamples，coverage 远低于名义 95%。§4.1 引用 CI [-1.0, -0.7] 时未附 heuristic caveat。

**R1-W4** [Major] Per-example decomposition 的 binary 信息损失
- Binary 分类丢弃 confidence margin 信息。Appendix I normalized ES < 0.10。Cohen's d cross-validation 的 near-zero 可能反映 binary decomposition 分辨力不足而非真实 effect 小。

**R1-W5** [Minor-Major] Decoupling "saturation" 缺乏形式化定义
- "Saturates at first attention level" 未形式化——无 plateau detection test、无 change-point analysis。可能只是 floor effect（J 本就很低无下降空间）。

### 小问题
- M1: Table 1 LAMBADA Cohen's d = 2.41 异常高
- M2: §3.4 correct 定义（argmax vs threshold）
- M3: Appendix R α stability 应在主文引用
- M4: Fehlauer (2025) seed-level Jaccard 未讨论
- M5: Figure 2 y-axis 标注 clarification

### Questions
Q1. 能否获取 model zoo 额外 seed 训练结果？
Q2. LAMBADA 改为 perplexity-based ranking 后 convergence 是否持续？
Q3. 排除 GDN 后 convergence 不显著，结论应如何修订？
Q4. Decoupling practical implication 前提是否依赖 seed confound？
Q5. 不同 prompt templates 是否改变 multiplicity pattern？

### Missing References
- Jiang et al. (2024) fine-tuning per-example behavior
- Bai et al. (2024) per-example reasoning behavior
- Sellam et al. (2022) 可进一步讨论 multi-seed 设计

### Strengths
S1. 新颖且重要的研究问题
S2. 分析框架全面且透明（18 个附录）
S3. 统计方法选择总体恰当
S4. 对自身局限性坦诚度高
S5. Decoupling 发现最有说服力
S6. Cross-scale 分析增加维度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 646 · 2026-05-22T06:01:07.454866+00:00_

逐条回应 Reviewer 1 的审稿意见。

---

## 交叉回应：Reviewer 2 → Reviewer 1

### Must-Fix 问题

**[AGREE] R1-N1: 单次训练 confound**

完全同意。这也是我在 R2-N1 中独立提出的最核心问题。R1 进一步指出 Appendix K 的 permutation test baseline 是 example identity random permutation 而非 seed variation baseline，这个区分非常精准。论文中 §4.3 给出的 "3× Jaccard gap"（cross-architecture J ≈ 0.03–0.07 vs. within-architecture J ≈ 0.10）作为 proxy evidence 不充分——within-architecture 比较共享同一 backbone 且仅变 attention ratio，本身就预期有更高 overlap，无法将差额归因于 architecture。两位 Reviewer 独立达成一致，说明这是 blocking issue。

**[AGREE with nuance] R1-N2: LAMBADA convergence 统计证据不足**

基本同意 R1 的判断，与我的 R2-N2 一致。补充几点：

1. R1 提到 Bonferroni-adjusted p = .100 未达显著。论文 §4.1 确实在报告时用了 "suggestive evidence" 而非 "significant"，在措辞上有一定克制。但 Conclusion（§5）将此上升为论文核心发现之一时弱化了这一限定。
2. R1 关于排除 GDN 后 ρ = -0.7, p = .233 的观察非常关键——说明 convergence pattern 依赖 GDN 这一个架构的行为。
3. GDN h3-1 使用 16 heads vs. 其他架构 32 heads 的 confound（R1 指出，论文在 Appendix E 讨论）确实是一个 technical concern。不过我补充一点：即使头数不同，这仍是 Wang et al. (2025) zoo 的设计选择，反映了各架构的 "natural" 配置。将此作为 confound 有道理，但也可以论证这是 ecological validity 的一部分。
4. 我同意应将 convergence 定位为 "exploratory observation"，但不必完全否定——结合 Appendix C（scale-dependent convergence）的补充分析，这仍是一个值得报告的 pattern，只是不应作为论文 headline finding。

### Should-Fix 问题

**[AGREE] R1-W1: Confirmatory/exploratory split 缺乏 pre-registration**

同意。论文在 Appendix A/B 中承认 "we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists"，但对全部 10 个 benchmark 做 Bonferroni 的话 LAMBADA adj-p = 0.17，进一步削弱 §4.1 的 confirmatory claim。这是一个合理的 concern，尤其在 ARR 审稿标准中对 statistical rigor 的要求下。

**[REBUT] R1-W2: Format confound 未被系统分析**

部分不同意。R1 指出 LAMBADA（open-ended）α=0.30 vs PIQA（2-choice）α=0.14 可能反映 format 差异而非 cognitive demand。但论文在 §3.2 和 Table 1 中的数据并不完全支持 format-driven 的解释：

- ARC-Easy 是 4-choice format，α = 0.21（Table 2），介于 LAMBADA 和 PIQA 之间——如果 format 是主因，4-choice 应更接近 2-choice 而非 open-ended。
- HellaSwag 是 4-choice（§3.2 注明 "its small sample size renders σ estimation unreliable"），α = 0.15，也不严格按 choice 数排列。
- 更关键的是，论文 §4.1 的 Spearman ρ 分析表明 cross-architecture σ variation 与 attention ratio 的关系是 task-specific 的——BoolQ（yes/no, 2-choice）的 ρ = -1.0（完美单调递减），而 PIQA（也是 2-choice）ρ = 0.13（无趋势）。如果 format 是主因，同为 2-choice 的 BoolQ 和 PIQA 应有相似 pattern。

因此，task type（retrieval vs. reasoning vs. comprehension）比 evaluation format 更可能解释 α 差异。不过我同意 R1 的建议，补充 format × task type 交叉分析会增强论文。

**[AGREE] R1-W3: Bootstrap CI 覆盖率问题**

同意。n=3 architectures 下 BCa bootstrap 的有效 resamples 极为有限（最多 27 个唯一 triples），覆盖率必然远低于名义 95%。论文 §3.5 提到 "these intervals should be interpreted as heuristic indicators of effect direction rather than intervals with formal coverage guarantees"，但 §4.1 引用 CI [-1.0, -0.7] 时未重复此 caveat。建议在每次引用 CI 时附带 heuristic 标注，或改用 percentile CI 并明确报告 resamples 数量。

**[AGREE with nuance] R1-W4: Binary decomposition 信息损失**

同意核心关切。我在 R2 小问题 #3 中也提到了这一点。Appendix I 的 normalized effect size < 0.10 和 Appendix F 的 attention entropy 差异 negligible（Table 5）确实可能部分归因于 binary decomposition 的分辨力不足。

不过，有一个 counterpoint：论文 §4.2 使用 binary classification 的目的不是量化 effect magnitude，而是识别 "哪些 examples 被哪个架构影响"——对于 Jaccard analysis 来说，binary 分类是自然选择。真正的信息损失在于：如果一个 example 从 confidence 0.49 变为 0.51（刚过 argmax threshold），它被计为 "helped"，与从 0.01 变为 0.99 的 example 等权。这确实值得用连续 measure（如 probability shift magnitude）补充分析。

**[AGREE] R1-W5: Decoupling "saturation" 缺乏形式化**

同意。"Saturates at first attention level" 确实缺乏形式化定义。R1 提出的 floor effect 解释（J 本身很低，无下降空间）是一个非常 plausible 的 alternative explanation。论文 Table 2 显示 J_helped 和 J_hurt 值均在 0.03–0.09 范围，已接近 random baseline（Appendix K null 值约 0.01-0.03）。因此 "saturation" 可能只是 "already near floor, nowhere to go"。建议补充 change-point detection 或至少报告 h3-1 到 h24-1 的 Jaccard 变化是否在 noise band 内。

### 小问题

**[AGREE] R1-M1**: Table 1 LAMBADA Cohen's d = 2.41 确实异常高。论文应讨论这是否反映了 LAMBADA 的特殊性质（variance 小但 mean shift 大）还是统计 artifact。

**[AGREE] R1-M2**: §3.4 中 "correct" 的定义（argmax-based binary）应在首次使用时明确说明，对 LAMBADA 这种 open-ended generation task 尤其重要。

**[AGREE] R1-M3**: Appendix R 的 α stability 分析（不同 subsample 下 α 的稳定性）确实应在主文引用，增强 §4 结论的 robustness。

**[REBUT] R1-M4**: R1 建议讨论 Fehlauer (2025) 的 seed-level Jaccard。但据我了解 Fehlauer et al. (2025) 研究的是 KL divergence across seeds，而非 Jaccard similarity——他们的度量维度不同，直接对比需要注意 metric 差异。不过同意应更充分讨论 seed-driven 文献中可比较的 per-example disagreement 量化结果。

**[AGREE] R1-M5**: Figure 2 y-axis 标注需要 clarification（是 Jaccard? fraction? 哪一种？）。

### Questions

**Q1**: 同意这是最关键的问题。即使 2-3 个额外 seed 也能大幅增强 claims。

**Q2**: 有趣的问题。LAMBADA 改为 perplexity-based ranking 可以验证 convergence finding 是否依赖 argmax threshold。

**Q3**: 排除 GDN 后 convergence 不显著——这要求论文至少讨论 convergence 对 GDN 的依赖性，并弱化 general claim。

**Q4**: 同意 decoupling 的 practical implication 部分依赖于能区分 architecture vs. seed effect。

**Q5**: Prompt template 敏感性是一个合理的 robustness concern，但论文使用 lm-evaluation-harness 的 default prompts 是标准做法。

### Missing References

**[AGREE]** R1 建议的 Jiang et al. (2024) 和 Bai et al. (2024) 如果确实研究 fine-tuning/reasoning 的 per-example behavior，则值得引用。Sellam et al. (2022) 已在 §2 中引用，但同意应更深入讨论其 multi-seed 设计对本文的启示。

### Strengths

**[AGREE]** R1 的 S1-S6 与我的评估高度一致。特别同意 S2（18 个附录的分析透明度）和 S4（对自身局限性的坦诚度）。这些优势使论文在 Findings track 有坚实的位置。

---

### 总结

两位 Reviewer 在以下核心问题上达成一致：
1. **Architecture-seed confound**（R1-N1 = R2-N1）：blocking issue
2. **LAMBADA-centric findings**（R1-N2 ≈ R2-N2）：generalizability 不足
3. **统计方法的局限性**（R1-W1/W3 ≈ R2 小问题）：需要更审慎的表述

唯一实质性分歧在 **R1-W2 (format confound)**：我认为论文数据不完全支持 format-driven 解释，task type 是更可能的 driver，但补充交叉分析仍有价值。

维持评分：**Overall 3.0 (Findings)**，与 R1 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

58 recorded events


### User

_source line 647 · 2026-05-22T07:35:33.916483+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**审查。

## Venue 信息
- **目标 venue**: EMNLP 2026（via ACL Rolling Review）
- **投稿类别**: Long Paper
- **截止日期**: 2026-05-25
- **页数限制**: 正文严格 8 页，参考文献不限；Limitations 和 Ethics 不计入页数（不得包含过多额外内容）
- **模板**: ACL 格式（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind
- **附录**: 允许，不限长度，但不应滥用

## 论文信息
- **标题**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/submitted.pdf`
- sections 在 `sections/` 子目录下：introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex
- 参考文献：references.bib

## 你的审查侧重

请重点关注以下方面：

1. **新颖性与贡献**
   - 论文的核心贡献是什么？是方法创新还是实证发现？
   - 将 predictive multiplicity 概念应用到 hybrid recurrent architectures 是否构成足够的新颖性？
   - 与已有工作（Marx 2020, D'Amour 2022, McCoy 2020, Swayamdipta 2020）的差异化是否清晰？
   - "decoupling" 是一个 finding 还是一个 contribution？
   - 对 EMNLP 社区的价值和影响力评估

2. **Related Work 覆盖与定位**
   - 是否遗漏重要相关工作（predictive multiplicity、hybrid architectures、per-example analysis 领域）
   - 与 Zoology (Arora et al. 2024)、Based、Mamba-2/3 的关系是否充分讨论
   - 论文定位是否准确（empirical study vs. new method）

3. **写作质量**
   - Abstract 信息密度是否合适
   - Introduction 的叙事逻辑是否清晰
   - 术语使用一致性（multiplicity, divergence, decoupling 等）
   - 图表质量和信息传达效率
   - Limitations 章节是否充分但不冗长（用户规则要求 ~3 points）
   - Conclusion 的 practical protocol 建议是否有足够支撑

4. **格式合规**
   - 正文是否在 8 页以内
   - Double-blind 匿名是否合规
   - ACL 模板使用是否正确
   - 引用格式是否一致
   - Ethics Statement 是否到位

5. **完整性**
   - 实验覆盖是否充分（benchmark 数量、scale 变化、sensitivity analysis）
   - Appendix 内容是否必要且不冗余
   - 主文是否自包含（不依赖 appendix 才能理解核心论点）

请按以下格式输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 severity: Critical/Major/Minor）
## Questions（需要作者回答的问题）
## Missing References（如有）
## Detailed Comments（逐节细评）
## Overall Assessment（评分 + 置信度）
```

评分标准（EMNLP 2026 ARR）：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T07:35:44.270551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T07:35:45.676009+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-22T07:35:45.827138+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 651 · 2026-05-22T07:35:45.877851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-22T07:35:50.552721+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-22T07:35:52.921139+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-22T07:35:57.444839+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL Rolling Review 2026 reviewer guidelines, review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If qualified to review only some aspects of the paper, reviewers should state in the review if they did not check some major parts, such as proofs, as this information is helpful for the AC to tell wha
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6892
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-22T07:35:58.802575+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5881
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-22T07:36:05.896579+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions. List every question/field in the form."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions. List every question/field in the form."
  }
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-22T07:36:06.399898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 658 · 2026-05-22T07:36:07.255938+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-22T07:36:07.256418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T07:36:07.509837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T07:36:08.567822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-22T07:36:09.120395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1610
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-22T07:36:13.250861+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Scoring Dimensions

**1. Reviewer Confidence**
- 5: Positive evaluation is correct; thoroughly read paper and familiar with related work
- 4: Quite sure; checked important points carefully
- 3: Pretty sure; good area knowledge but didn't verify all details
- 2: Willing to defend evaluation; likely missed some details
- 1: Not area expertise; evaluation is educated guess

**2. Soundness**
- 5: "one of the most thorough" studies for its type
- 4: Provides sufficient support; extra experiments optional
- 3.5, 3: Acceptable with minor support needed
- 2.5, 2: Main claims lack adequate support; technical problems
- 1.5, 1: Insufficient rigor or irrelevant to ACL

**3. Excitement**
- 5: Highly exciting; would recommend or attend presentation
- 4: Would mention to others; effort to attend
- 3: Might mention points; attend if time permits
- 2: Potentially interesting but doesn't resonate personally
- 1: Not exciting; lacks computational linguistics relevance

**4. Overall Assessment**
- 5: Award consideration (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

**5. Reproducibility**
- 5: Results easily reproduced
- 4: Mostly reproducible; minor variations possible
- 3: Reproducible with difficulty
- 2: Hard to reproduce; unavailable data or missing details
- 1: Cannot reproduce

**6. Datasets Quality**
- 5: Enabling impact on research projects
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable datasets

**7. Software Quality**
- 5: Enabling impact
- 4: Useful for researchers
- 3: Potentially useful
- 2: Documentary value
- 1: No usable software

**8. Author Identity Knowledge**
- 5: Violation of double-blind rules
- 4: Known from preprint/workshop
- 3: Identifiable from submission content
- 2: Known from
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7354
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T07:36:18.826774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-22T07:36:19.178467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-22T07:36:20.132479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1305
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T07:36:20.133499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-22T07:36:20.284490+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-22T07:36:20.435845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-22T07:36:20.640175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-22T07:36:21.243374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-22T07:36:25.759489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-22T07:36:26.364959+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-22T07:36:26.365403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-22T07:36:26.719430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-22T07:36:27.274577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-22T07:36:27.576540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-22T07:36:35.257784+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-19",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-19",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-22T07:36:36.160762+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.5}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 443.0}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 364.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.9}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 268 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-22T07:36:39.276823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-22T07:36:39.629054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-22T07:36:40.534986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-22T07:36:40.536868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-22T07:36:40.537220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-22T07:36:41.089793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-22T07:36:41.442335+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-22T07:36:41.442775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-22T07:36:41.497242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-22T07:36:42.049989+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-22T07:36:56.300314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-22T07:36:56.754814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-22T07:36:57.209210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-22T07:36:57.310803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-22T07:36:57.764298+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-22T07:36:57.869040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-22T07:36:57.871479+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-22T07:36:57.974951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 664
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-22T07:40:32.041814+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewer guidelines: what makes a good review, what reviewers should look for, specific criteria for evaluating papers, any guidance on novelty, soundness, and how to distinguish conference-worthy vs findings-worthy papers. Also extract any guidance on empirical papers vs method papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewer guidelines: what makes a good review, what reviewers should look for, specific criteria for evaluating papers, any guidance on novelty, soundness, and how to distinguish conference-worthy vs findings-worthy papers. Also extract any guidance on empirical papers vs method papers."
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-22T07:40:39.664583+00:00_

# Key Reviewer Guidelines for ARR

## What Makes a Good Review

Reviews should be **specific and actionable**. Rather than stating "the paper is missing relevant references," identify which references are needed. The guidance emphasizes that "a good review should be professional and neutral, if not kind," recognizing reviewers' power in an anonymous system.

## Core Evaluation Framework

Reviewers must **read papers twice**: first for context-setting (research question, methodology fit), then for in-depth technical assessment. This prevents confirmation bias and hindsight bias from tainting initial impressions.

Three scoring dimensions are required:
- **Soundness**: Technical validity, justified by explicit review text
- **Excitement**: Personal interest (orthogonal to soundness)
- **Overall Assessment**: Composite recommendation reflecting soundness, novelty, and potential impact

## Critical Biases to Avoid

The guidelines identify 17 common problematic heuristics (H1-H17), including:

- Dismissing work as "not novel" without evidence
- Rejecting papers for lacking SOTA results (irrelevant to scientific contribution)
- Criticizing negative results or simple solutions
- Demanding extra experiments beyond what claims require
- Penalizing work on non-English languages or niche topics

The core principle: "a paper only needs to present sufficient evidence for the claim that the authors are making."

## Common NLP Paper Problems

Categories reviewers should flag (M1-G5):

**Methodology**: LLM-only evaluation without validation, reproducibility gaps, unmotivated sampling, incomplete proofs

**Results**: Statistical significance missing, overclaiming, inappropriate scope, misleading framing

**General**: Unclear research questions, missing related work, vague terminology, hallucinated citations

## Conference vs. Findings Distinction

All papers must be "sufficiently sound and reproducible." Main conference papers warrant acceptance despite personal disinterest if they 
…[truncated 135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7622
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-22T07:43:13.009227+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n### 总体评分\n**Overall**: 3.0（Findings）\n**一句话总结**: 执行严谨的实证度量研究，揭示了混合线性递归架构之间per-example级别的预测分歧现象，但核心发现（decoupling）仅在单一benchmark上成立且受GDN架构混淆，新颖性和影响力不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（置换检验、Bootstrap CI、Bonferroni校正），但单次训练运行无法分离架构vs.种子效应，decoupling发现受GDN混淆 |\n| Excitement | 2.5/5 | 问题有实践价值，但发现偏描述性，缺乏机制解释，decoupling仅限LAMBADA，practical protocol支撑薄弱 |\n| Reproducibility | 4/5 | 使用公开model zoo（Wang et al. 2025），标准benchmark，统计方法详细描述 |\n| Confidence | 4/5 | 熟悉predictive multiplicity文献和hybrid architecture领域 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心发现\"decoupling\"范围过窄且受混淆变量影响\n- 位置：§4.3 (p7), §4.4 (p8), Appendix D (p12)\n- aggregate convergence与per-example divergence的decoupling仅在LAMBADA上观察到（论文自己在p2-3承认\"does not replicate on other benchmarks\"）。§4.4 sensitivity analysis显示移除GDN后收敛相关性从ρ=−1.0降至ρ=−0.7，Appendix E揭示GDN在h3-1配置中使用16个attention heads而非其他架构的32个——这一架构不对称性可能是decoupling的真正驱动因素。\n- 建议：（1）显式讨论GDN head数量不对称是否解释decoupling；（2）将claim限定为\"GDN-driven, LAMBADA-specific observation\"或在更多benchmark上复现。\n\n**N2** [critical] 新颖性定位模糊——方法全部借用，贡献纯描述性\n- 位置：§1 contributions (p2), §3 Method (p3-4)\n- 所有工具均来自已有工作——metrics来自Marx et al. (2020)，模型来自Wang et al. (2025)，benchmark来自lm-eval-harness。论文未提出新方法/指标/理论框架。Appendix F的attention weight analysis显示helped/hurt examples之间entropy差异negligible（ΔH ≤ 0.002），论文自己承认分析是\"descriptive, not causal\"。\n- 建议：深入挖掘机制（为什么某些examples flip？recurrent层记忆长度差异？gate机制？），或提出可验证的理论框架。\n\n### Should-Fix 问题\n\n**W1** [major] 单次训练运行无法支撑因果性声明\n- 位置：§1 p1, §4.2 p6, Limitations p9\n- 每个配置仅一次训练运行，无法分离architecture effect与seed effect。正文多处使用因果语言（\"architectural differences produce per-example multiplicity\"），但Limitations承认无法排除seed contribution。\n- 建议：明确所有claims为\"conditioned on single training runs\"，或运行多seeds calibration。\n\n**W2** [major] Scale分析不足以支撑practical protocol\n- 位置：§5 p8, Appendix Q p18\n- 仅340M和1.3B两个scale，340M上convergence完全不存在。两个数据点无法外推scaling trend，但§5提出面向practitioners的protocol。\n- 建议：将protocol限定为\"≤1.3B scale\"，或讨论transfer到更大scale的理由。\n\n**W3** [major] 术语\"predictive multiplicity\"被拉伸\n- 位置：标题、Abstract、§1-2\n- Marx et al. (2020)的predictive multiplicity定义在Rashomon set内。本文研究结构不同的架构在不同attention配置下的表现差异，并非Rashomon set意义下的分析。σ metric更准确应称为\"cross-architecture per-example disagreement\"。\n- 建议：明确区分本文的分析与形式化的Rashomon-set multiplicity。\n\n**W4** [warning] Task taxonomy事前性质弱\n- 位置：§3.2 p4, Appendix A p11\n- Appendix A声称taxonomy是\"fixed prior to analysis\"但又说不是formal pre-registration。\n- 建议：提供时间戳/commit hash，或承认弱约束性质。\n\n### 小问题\n- Figure 2子图过小，confidence band难以辨识\n- Table 2信息密度高，helped/hurt对比可用shading增强\n- Appendix F的结论未在主文中引用\n- Limitations section覆盖5-6点，稍长但内容实质\n\n### Questions\n1. GDN h3-1使用16 heads vs.其他架构32 heads，这一不对称是否足以解释LAMBADA decoupling？\n2. 是否考虑运行多random seeds建立per-example disagreement的seed baseline？\n3. Practical protocol在什么scale上具有可操作性？\n4. 为什么Appendix F无法找到helped/hurt的attention weight discriminative pattern？\n5. 是否探索过连续指标（log-probability, calibrated confidence）？\n\n### Missing References\n1. Fort et al. (2019), \"Deep Ensembles: A Loss Landscape Perspective\" — cross-architecture disagreement的理论视角\n2. Niven and Kao (2019), \"Probing Neural Network Comprehension of Natural Language Arguments\" — 与helped/hurt decomposition相关\n3. 建议在Related Work中显式讨论Arora et al. (2024b, Based)的linear attention方法\n\n### 主要优势\n1. 实验设计严谨，controlled zoo有效隔离attention ratio效应\n2. 统计方法规范（permutation test + bootstrap CI + Bonferroni + percentile CI fallback）\n3. 主文自包含，appendix（A-R）提供全面sensitivity analysis\n4. 诚实的Limitations讨论\n5. Per-example decomposition (helped/hurt/unchanged) 设计合理\n\n### 写作质量评估\n- Abstract信息密度合适，但\"78-92% theoretical maximum\"缺乏上下文\n- Introduction叙事逻辑清晰\n- \"decoupling\"在contributions中被列为核心发现但仅LAMBADA成立，存在over-promise\n- Related Work覆盖合理但缺少Based显式讨论\n- 格式合规：正文8页，double-blind，ACL模板正确\n\n### Overall Assessment\n**3.0 — Findings**。执行良好的实证研究，选题有实践意义，统计严谨。但：（1）无方法创新；（2）decoupling仅单一benchmark+受GDN confound；（3）缺乏机制解释。更适合Findings。若能提供decoupling机制解释或在更多benchmarks复现，可上调至3.5。",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）\n\n### 总体评分\n**Overall**: 3.0（Findings）\n**一句话总结**: 执行严谨的实证度量研究，揭示了混合线性递归架构之间per-example级别的预测分歧现象，但核心发现（decoupling）仅在单一benchmark上成立且受GDN架构混淆，新颖性和影响力不足以支撑主会议接收。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（置换检验、Bootstrap CI、Bonferroni校正），但单次训练运行无法分离架构vs.种子效应，decoupling发现受GDN混淆 |\n| Excitement | 2.5/5 | 问题有实践价值，但发现偏描述性，缺乏机制解释，decoupling仅限LAMBADA，practical protocol支撑薄弱 |\n| Reproducibility | 4/5 | 使用公开model zoo（Wang et al. 2025），标准benchmark，统计方法详细描述 |\n| Confidence | 4/5 | 熟悉predictive multiplicity文献和hybrid architecture领域 |\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心发现\"decoupling\"范围过窄且受混淆变量影响\n- 位置：§4.3 (p7), §4.4 (p8), Appendix D (p12)\n- aggregate convergence与per-example divergence的decoupling仅在LAMBADA上观察到（论文自己在p2-3承认\"does not replicate on other benchmarks\"）。§4.4 sensitivity analysis显示移除GDN后收敛相关性从ρ=−1.0降至ρ=−0.7，Appendix E揭示GDN在h3-1配置中使用16个attention heads而非其他架构的32个——这一架构不对称性可能是decoupling的真正驱动因素。\n- 建议：（1）显式讨论GDN head数量不对称是否解释decoupling；（2）将claim限定为\"GDN-driven, LAMBADA-specific observation\"或在更多benchmark上复现。\n\n**N2** [critical] 新颖性定位模糊——方法全部借用，贡献纯描述性\n- 位置：§1 contributions (p2), §3 Method (p3-4)\n- 所有工具均来自已有工作——metrics来自Marx et al. (2020)，模型来自Wang et al. (2025)，benchmark来自lm-eval-harness。论文未提出新方法/指标/理论框架。Appendix F的attention weight analysis显示helped/hurt examples之间entropy差异negligible（ΔH ≤ 0.002），论文自己承认分析是\"descriptive, not causal\"。\n- 建议：深入挖掘机制（为什么某些examples flip？recurrent层记忆长度差异？gate机制？），或提出可验证的理论框架。\n\n### Should-Fix 问题\n\n**W1** [major] 单次训练运行无法支撑因果性声明\n- 位置：§1 p1, §4.2 p6, Limitations p9\n- 每个配置仅一次训练运行，无法分离architecture effect与seed effect。正文多处使用因果语言（\"architectural differences produce per-example multiplicity\"），但Limitations承认无法排除seed contribution。\n- 建议：明确所有claims为\"conditioned on single training runs\"，或运行多seeds calibration。\n\n**W2** [major] Scale分析不足以支撑practical protocol\n- 位置：§5 p8, Appendix Q p18\n- 仅340M和1.3B两个scale，340M上convergence完全不存在。两个数据点无法外推scaling trend，但§5提出面向practitioners的protocol。\n- 建议：将protocol限定为\"≤1.3B scale\"，或讨论transfer到更大scale的理由。\n\n**W3** [major] 术语\"predictive multiplicity\"被拉伸\n- 位置：标题、Abstract、§1-2\n- Marx et al. (2020)的predictive multiplicity定义在Rashomon set内。本文研究结构不同的架构在不同attention配置下的表现差异，并非Rashomon set意义下的分析。σ metric更准确应称为\"cross-architecture per-example disagreement\"。\n- 建议：明确区分本文的分析与形式化的Rashomon-set multiplicity。\n\n**W4** [warning] Task taxonomy事前性质弱\n- 位置：§3.2 p4, Appendix A p11\n- Appendix A声称taxonomy是\"fixed prior to analysis\"但又说不是formal pre-registration。\n- 建议：提供时间戳/commit hash，或承认弱约束性质。\n\n### 小问题\n- Figure 2子图过小，confidence band难以辨识\n- Table 2信息密度高，helped/hurt对比可用shading增强\n- Appendix F的结论未在主文中引用\n- Limitations section覆盖5-6点，稍长但内容实质\n\n### Questions\n1. GDN h3-1使用16 heads vs.其他架构32 heads，这一不对称是否足以解释LAMBADA decoupling？\n2. 是否考虑运行多random seeds建立per-example disagreement的seed baseline？\n3. Practical protocol在什么scale上具有可操作性？\n4. 为什么Appendix F无法找到helped/hurt的attention weight discriminative pattern？\n5. 是否探索过连续指标（log-probability, calibrated confidence）？\n\n### Missing References\n1. Fort et al. (2019), \"Deep Ensembles: A Loss Landscape Perspective\" — cross-architecture disagreement的理论视角\n2. Niven and Kao (2019), \"Probing Neural Network Comprehension of Natural Language Arguments\" — 与helped/hurt decomposition相关\n3. 建议在Related Work中显式讨论Arora et al. (2024b, Based)的linear attention方法\n\n### 主要优势\n1. 实验设计严谨，controlled zoo有效隔离attention ratio效应\n2. 统计方法规范（permutation test + bootstrap CI + Bonferroni + percentile CI fallback）\n3. 主文自包含，appendix（A-R）提供全面sensitivity analysis\n4. 诚实的Limitations讨论\n5. Per-example decomposition (helped/hurt/unchanged) 设计合理\n\n### 写作质量评估\n- Abstract信息密度合适，但\"78-92% theoretical maximum\"缺乏上下文\n- Introduction叙事逻辑清晰\n- \"decoupling\"在contributions中被列为核心发现但仅LAMBADA成立，存在over-promise\n- Related Work覆盖合理但缺少Based显式讨论\n- 格式合规：正文8页，double-blind，ACL模板正确\n\n### Overall Assessment\n**3.0 — Findings**。执行良好的实证研究，选题有实践意义，统计严谨。但：（1）无方法创新；（2）decoupling仅单一benchmark+受GDN confound；（3）缺乏机制解释。更适合Findings。若能提供decoupling机制解释或在更多benchmarks复现，可上调至3.5。",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-22T07:43:16.923384+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3914
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-22T07:43:21.011852+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-22T07:43:21.062598+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-22T07:43:26.246261+00:00_

审稿完成，已提交给 Review Director。

核心判断：**Overall 3.0（Findings）**。论文实验设计和统计方法执行良好，但存在两个关键问题：（1）核心decoupling发现仅在LAMBADA上成立且受GDN架构confound影响，generalizability不足；（2）所有分析工具均借用自已有工作，缺乏方法创新和机制解释。更适合Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 705 · 2026-05-22T07:44:39.764221+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 的完整审稿意见：

**Overall**: 3.0（Findings），Confidence 4/5
**维度打分**：Soundness 3.0/5, Excitement 3.0/5, Reproducibility 3.5/5

**Weaknesses：**

**W1 [Critical]** 核心 convergence claim 统计证据不足，但仍承担过多叙事权重。
- LAMBADA 的 convergence（ρ=−1.0）Bonferroni-adjusted p=.100，不达 0.05 显著性水平。对全部 10 个 benchmark 校正，p=.170。
- 去掉 GDN 后 ρ 从 −1.0 降到 −0.7（p=.233），MMLU 甚至翻转（ρ: −0.7 → +0.6）。
- convergence 在 340M 上完全缺失。
- convergence 只在"1.3B + 包含 GDN + LAMBADA"条件下成立，但论文叙事的 ~40% 围绕此展开。
- Contribution 2（decoupling）完全依赖 convergence 的成立。
- 建议：将 convergence 明确降级为 exploratory observation，将 Contribution 2 重新表述为 "per-example multiplicity persists regardless of aggregate trend"。

**W2 [Critical]** Single training run 根本性地限制了 architecture vs. seed 的区分。
- Within-arch Jaccard (~0.33) vs. cross-arch Jaccard (~0.10) 的 3× gap 被用作 proxy，但 within-arch 比较的是不同 attention ratio 的模型，cross-arch 比较的是相同 ratio 的不同架构。这两个比较不在同一维度上。
- 没有 multiple seeds，无法知道 seed-driven Jaccard 是 ~0.10 还是 ~0.33 或其他值。
- 建议：加强 Contribution 1 的 caveat，不使用 within-arch Jaccard 作为 architecture-dominance proxy。

**W3 [Major]** Bootstrap CI 在 n=3 上信息量极低，但被频繁引用。
- n=3 bootstrap 最多 27 unique resamples，11.25% degenerate。BCa 在 ρ=−1.0 boundary degenerate。
- CI 在 Abstract、Introduction、§4.1、§4.3、Figure 2 caption 被大量使用，给读者 convergence "well-characterized" 的印象。
- 建议：减少 CI 引用频率，或每次标注 "heuristic"；Abstract 中移除 CI 数字。

**W4 [Major]** Spearman ρ 在 n=5 上的解释力问题。
- 5 个 ordinal data points 的分辨能力有限。能达到 p<.05 的 ρ 值只有 ρ=±1.0。
- permutation test 是 all-or-nothing：只有 perfect monotonicity 能通过。
- 建议：明确指出 power analysis 限制。

**W5 [Major]** LAMBADA 作为唯一 converge 的 benchmark 缺乏充分讨论。
- mechanistic reasoning 像 post-hoc explanation。为什么 ARC-Easy (Mixed, ρ=−0.7) 不 converge？
- ρ=−1.0 vs ρ=−0.7 的区别在 n=5 上可能是 noise。
- 建议：讨论 LAMBADA 结果的 fragility。

**W6 [Major]** Binary decomposition 对 multiple-choice 的 limitation 讨论不足。
- 在 4-choice tasks 上，binary decomposition 可能高估 Jaccard（different wrong answers 都 counted as "hurt"）。
- 建议：讨论 bias 方向。

**W7 [Minor]** 可重复性：lm-eval-harness 版本、decoding strategy、bootstrap seed、code/data availability 缺失。

**W8 [Minor]** 因果语言偶有越界（"attention disrupts"、"attention compensating"）。

**Questions：**
Q1. One-sided permutation test 的 p-value？
Q2. Within-arch Jaccard 的计算维度？
Q3. 是否计算过 choice-level Jaccard？
Q4. 是否尝试过 confidence-weighted ensemble？
Q5. Helped 和 hurt 集合在不同 attention ratios 下的重叠？
Q6. Wang et al. model zoo 是否公开？

**Missing References：**
1. Jiang et al. (2024), "Characterizing model multiplicity in foundation models"
2. Pham et al. (2023) or similar on ensemble methods for hybrid architectures
3. 确认 Gorbett and Jana (2026) 和 Haghighat et al. (2026) 的状态

---

请逐条回应上述所有 Weakness（W1-W8）。对每条用 [AGREE] 或 [REBUT] 标注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-22T07:46:29.827845+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### 逐条回应\n\n**[AGREE] R1-W1: 核心 convergence claim 统计证据不足**\n与我的 N1 高度一致。补充：（1）Limitations (p9) 作者自己承认 Bonferroni-adjusted p=.100 不显著；（2）MMLU 翻转（ρ: −0.7→+0.6 after GDN exclusion）说明 convergence 方向性都不稳定；（3）GDN h3-1 使用 16 heads vs. 其他 32 heads（Appendix E）可能是实质驱动因素。R1 建议将 Contribution 2 重新表述为 \"per-example multiplicity persists regardless of aggregate trend\" 合理。\n\n**[AGREE] R1-W2: Single run + proxy 维度不匹配**\nR1 精确指出 within-arch Jaccard（不同 attention ratio）与 cross-arch Jaccard（不同架构）比较改变了不同变量，3× gap 不能作为 architecture-dominance proxy。需要的 baseline 是同架构同 ratio 不同 seed 的 Jaccard。\n\n**[AGREE] R1-W3: n=3 Bootstrap CI 信息量极低**\nn=3 CI 本质上是 3 个点的 range。Abstract 中 \"BCA 95% CI [−1.0, −0.7]\" 给读者 well-characterized 的假象。标注 \"heuristic\" 更合适。\n\n**[AGREE] R1-W4: Spearman ρ 在 n=5 上解释力有限**\n数学事实：只有 ρ=±1.0 能达到 p<.05。ρ=−1.0 vs. ρ=−0.7 仅差 1-2 个 rank swap，resolution 不足以支撑 \"LAMBADA uniquely converges\"。\n\n**[AGREE] R1-W5: LAMBADA 唯一 converge 缺乏充分讨论**\nARC-Easy (Mixed, ρ=−0.7) 也有中等负相关但不 converge，论文未解释差异。mechanistic reasoning (retrieval) 像 post-hoc。\n\n**[AGREE] R1-W6: Binary decomposition 对 multiple-choice 的 limitation**\n我未覆盖的有价值观察。Bias 方向：高估 agreement，实际上加强了 multiplicity claim（真实 Jaccard 更低）。但论文应显式讨论。\n\n**[AGREE] R1-W7: 可重复性细节缺失**\nlm-eval-harness 版本、decoding strategy、bootstrap seed、code/data availability 均缺失。\n\n**[AGREE] R1-W8: 因果语言越界**\n与我的 W1 一致。补充发现：\"architectural differences produce\"(§1)、\"attention-driven\"(§4.3)、\"attention disrupts\"(§5) 均应替换为 associative language。\n\n### 总结\n8/8 AGREE。两份审稿核心判断一致：convergence claim 统计基础不足、GDN confound、single run limitation。R1 在 W2（proxy 维度不匹配）、W3（n=3 CI）、W6（binary decomposition bias）提供了我未覆盖的精确分析。共同指向 **Overall 3.0（Findings）**。",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### 逐条回应\n\n**[AGREE] R1-W1: 核心 convergence claim 统计证据不足**\n与我的 N1 高度一致。补充：（1）Limitations (p9) 作者自己承认 Bonferroni-adjusted p=.100 不显著；（2）MMLU 翻转（ρ: −0.7→+0.6 after GDN exclusion）说明 convergence 方向性都不稳定；（3）GDN h3-1 使用 16 heads vs. 其他 32 heads（Appendix E）可能是实质驱动因素。R1 建议将 Contribution 2 重新表述为 \"per-example multiplicity persists regardless of aggregate trend\" 合理。\n\n**[AGREE] R1-W2: Single run + proxy 维度不匹配**\nR1 精确指出 within-arch Jaccard（不同 attention ratio）与 cross-arch Jaccard（不同架构）比较改变了不同变量，3× gap 不能作为 architecture-dominance proxy。需要的 baseline 是同架构同 ratio 不同 seed 的 Jaccard。\n\n**[AGREE] R1-W3: n=3 Bootstrap CI 信息量极低**\nn=3 CI 本质上是 3 个点的 range。Abstract 中 \"BCA 95% CI [−1.0, −0.7]\" 给读者 well-characterized 的假象。标注 \"heuristic\" 更合适。\n\n**[AGREE] R1-W4: Spearman ρ 在 n=5 上解释力有限**\n数学事实：只有 ρ=±1.0 能达到 p<.05。ρ=−1.0 vs. ρ=−0.7 仅差 1-2 个 rank swap，resolution 不足以支撑 \"LAMBADA uniquely converges\"。\n\n**[AGREE] R1-W5: LAMBADA 唯一 converge 缺乏充分讨论**\nARC-Easy (Mixed, ρ=−0.7) 也有中等负相关但不 converge，论文未解释差异。mechanistic reasoning (retrieval) 像 post-hoc。\n\n**[AGREE] R1-W6: Binary decomposition 对 multiple-choice 的 limitation**\n我未覆盖的有价值观察。Bias 方向：高估 agreement，实际上加强了 multiplicity claim（真实 Jaccard 更低）。但论文应显式讨论。\n\n**[AGREE] R1-W7: 可重复性细节缺失**\nlm-eval-harness 版本、decoding strategy、bootstrap seed、code/data availability 均缺失。\n\n**[AGREE] R1-W8: 因果语言越界**\n与我的 W1 一致。补充发现：\"architectural differences produce\"(§1)、\"attention-driven\"(§4.3)、\"attention disrupts\"(§5) 均应替换为 associative language。\n\n### 总结\n8/8 AGREE。两份审稿核心判断一致：convergence claim 统计基础不足、GDN confound、single run limitation。R1 在 W2（proxy 维度不匹配）、W3（n=3 CI）、W6（binary decomposition bias）提供了我未覆盖的精确分析。共同指向 **Overall 3.0（Findings）**。",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-22T07:46:33.591864+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 708 · 2026-05-22T07:46:39.156018+00:00_

交叉回应已提交。8条 Weakness 全部 [AGREE]——R1 和我的审查在核心判断上高度一致（convergence 统计不足、GDN confound、single run、scale 限制），R1 在 proxy 维度不匹配（W2）、n=3 CI 信息量（W3）、binary decomposition bias（W6）上补充了我未覆盖的精确分析。两份审稿共同指向 Overall 3.0（Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

88 recorded events


### User

_source line 709 · 2026-05-22T08:27:18.369041+00:00_

[Round 1 审稿请求]:
你负责**新颖性 + 完整性 + 写作质量 + 格式合规**方向的审查。

## Venue 信息
- **会议**: EMNLP 2026（通过 ARR 统一审稿）
- **投稿类别**: Long Paper
- **ARR Submission Deadline**: 2026-05-25
- **正文页数限制**: 严格 8 页（参考文献不限，Limitations/Ethics 不计入但不得含过多额外内容）
- **模板**: ACL style files（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind（作者标注 "Anonymous"）
- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

## 论文信息
- **标题**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`
- 各章节在 `sections/` 子目录：introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex

## 你的审查侧重

### 1. 新颖性评估
- 论文的 intellectual contribution 是什么？是新方法/新理论/新发现？还是已有指标（Jaccard, α）在新 setting 的直接套用？
- Predictive multiplicity 文献（Marx 2020, D'Amour 2022, McCoy 2020）中，本文的增量贡献有多大？
- "Decoupling" finding 是否为 convergence 的直接推论（而非独立发现）？
- 对 NLP 社区的实际影响和启发性如何？

### 2. Related Work 覆盖
- Hybrid architecture 文献是否充分？（Jamba, Griffin, RWKV-6, Mamba-2/3 等）
- Predictive multiplicity / underspecification 文献链是否完整？
- 是否有遗漏的关键相关工作？特别关注：
  - Deep ensemble 和 cross-architecture disagreement（如 Fort et al. 2019）
  - Benchmark artifact 相关（如 Niven & Kao 2019）
  - Foundation model multiplicity 的最新进展
- 与现有工作的 differentiation 是否清晰？

### 3. 写作质量
- Abstract 信息密度是否合适？是否过于统计量堆砌？
- Introduction 的 narrative flow——从 motivation 到 contribution 的逻辑链是否清晰？
- 术语使用是否一致？是否有因果语言越界（descriptive study 中使用 causal language）？
- 各章节的篇幅分配是否合理？Convergence 的叙事权重是否过高？
- Limitations 是否简洁且覆盖关键点（EMNLP 用户规则：约 3 点即可）？

### 4. 格式合规（EMNLP 2026 硬约束）
- 正文是否在 8 页以内？
- 是否使用 ACL 模板？
- 是否 double-blind compliant（无作者信息泄露）？
- Limitations section 是否存在且位置正确？
- 引用格式是否正确？

### 5. 论文完整性
- 实验是否充分支撑所有 claims？
- Appendix 是否提供了必要的补充但不含应在主文中的关键信息？
- Conclusion 是否过度 claim？practical protocol 的建议是否有充分支撑？
- Ethics Statement 是否充分？

请按以下格式输出审稿意见：

```
## Summary（2-3 句）

## Strengths（逐条，标注 S1, S2, ...）

## Weaknesses（逐条，标注 W1, W2, ...，每条标注 severity: Critical/Major/Minor）

## Questions（需要作者回答的）

## Missing References（如有）

## Overall Assessment
- Score: X (按 EMNLP 2026 评分标准)
- Confidence: X/5
- 一句话总结
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-22T08:27:48.126990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-22T08:27:48.177857+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-22T08:27:50.437794+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-22T08:27:50.488465+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-22T08:27:55.356948+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-22T08:27:55.709164+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-22T08:28:01.839812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-22T08:28:01.840498+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-22T08:28:13.203187+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 719 · 2026-05-22T08:28:13.203598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-22T08:28:33.379499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"
  }
}
```

</details>

---


### Tool call

_source line 721 · 2026-05-22T08:28:35.790114+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 722 · 2026-05-22T08:28:39.101744+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026 reviewer guidelines dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR review form criteria and reviewer guidelines for 2025-2026:

## Review Score Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Additional Reviewer Guidelines

Starting in May 2025, ARR also adopts a new policy on 'highly irresponsible' (meta-)reviewers, with program chairs and ARR editors-in-chief considering egregious cases including extremely terse reviews, unprofessional tone, and LLM-generated reviews.

After the author response period, area chairs can report both great and irresponsible reviews via a new form on reviews or by listing them in the meta-review form.

## Expectations for Papers

All papers recommended for Findings or main conference are expected to be sound and reproducible.

The search results provide information about the three review dimensions and general guidelines, but for more detai
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5722
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-22T08:28:40.205901+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}], \"total_pages\": 20, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images\"}, \"er
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4415
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-22T08:28:48.176598+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions, scoring scales (1-5 for each dimension), and what each score level means. Focus on: soundness, excitement, overall assessment, confidence, and any other scored dimensions. Also extract any specific guidelines about what reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions, scoring scales (1-5 for each dimension), and what each score level means. Focus on: soundness, excitement, overall assessment, confidence, and any other scored dimensions. Also extract any specific guidelines about what reviewers should evaluate."
  }
}
```

</details>

---


### Tool call

_source line 725 · 2026-05-22T08:28:48.530862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-22T08:28:49.485608+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 727 · 2026-05-22T08:28:49.636454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-22T08:28:50.188150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 729 · 2026-05-22T08:28:50.391685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-22T08:28:50.392096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-22T08:28:51.250589+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-22T08:28:51.454560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1062
}
```

</details>

---


### Tool result

_source line 733 · 2026-05-22T08:28:53.812662+00:00_

# ARR Review Form Dimensions and Scoring

Based on the guidelines provided, ARR uses **three primary scored dimensions**:

## Scoring Dimensions

**1. Soundness**
The document states reviewers should ensure "soundness scores must be justified by the text of the review." Low soundness scores require explicit justification in the review content.

**2. Excitement**
Described as a subjective dimension "orthogonal to the assessment of the soundness of the paper," reflecting personal interest rather than technical validity.

**3. Overall Assessment**
A composite recommendation score reflecting "soundness, excitement, and also other factors like novelty and impact."

## Additional Dimensions

**Confidence**: Reviewers indicate confidence levels in their assessments, with guidance to specify when expertise doesn't cover certain submission aspects.

**Reproducibility**: Scored separately, with justification requirements for low scores.

## Evaluation Guidelines

Reviewers should assess:
- Technical soundness and proof validity
- Novelty relative to publication standards (3+ months prior)
- Appropriate scoping of claims
- Statistical significance reporting
- Clarity of research questions and contributions

The guidelines emphasize that **all scores must align with review justifications**—low scores without documented issues indicate insufficient review quality. Reviewers should distinguish between technical merit (soundness) and subjective preference (excitement) when forming recommendations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5636
}
```

</details>

---


### Tool call

_source line 734 · 2026-05-22T08:29:04.621456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-22T08:29:05.474769+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 736 · 2026-05-22T08:29:05.625695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-22T08:29:05.927139+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-22T08:29:05.927569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-22T08:29:06.329344+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-22T08:29:06.329899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-22T08:29:06.480789+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-22T08:29:28.300049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-22T08:29:28.451310+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-22T08:29:31.719778+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "5-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "5-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-22T08:29:32.522346+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.4}], \"total_pages\": 20, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-22T08:29:35.233132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-22T08:29:36.237902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-22T08:29:36.388661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-22T08:29:36.790745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-22T08:29:37.142626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-22T08:29:37.143087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-22T08:29:37.796755+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool result

_source line 753 · 2026-05-22T08:29:38.100411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T08:30:00.652816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-22T08:30:01.305865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 756 · 2026-05-22T08:30:01.307121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-22T08:30:02.013258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-22T08:30:06.583290+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-22T08:30:07.740510+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 398.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.9}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.3}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.4}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-22T08:30:13.911965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 761 · 2026-05-22T08:30:14.415070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-22T08:30:15.319338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-22T08:30:15.322365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T08:30:15.322936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-22T08:30:15.627852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-22T08:30:16.188525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 865
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-22T08:30:16.490269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 862
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-22T08:30:40.157775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-22T08:30:40.509517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-22T08:30:40.712679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-22T08:30:41.164990+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-22T08:30:41.466437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-22T08:30:42.069552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-22T08:30:42.270757+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-22T08:30:42.875349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-22T08:30:48.631855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-22T08:30:49.133382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-22T08:30:49.235032+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool result

_source line 779 · 2026-05-22T08:30:49.588618+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 780 · 2026-05-22T08:35:42.197518+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the exact scoring scales for: (1) Soundness - what does each score 1-5 mean, (2) Excitement/Novelty - what does each score 1-5 mean, (3) Overall Assessment - what does each score 1-5 mean, (4) Confidence - what does each score 1-5 mean, (5) Reproducibility scoring. Give me the exact text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the exact scoring scales for: (1) Soundness - what does each score 1-5 mean, (2) Excitement/Novelty - what does each score 1-5 mean, (3) Overall Assessment - what does each score 1-5 mean, (4) Confidence - what does each score 1-5 mean, (5) Reproducibility scoring. Give me the exact text for each score level."
  }
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-22T08:35:46.063963+00:00_

# ARR Review Scoring Scales

I've searched the provided document thoroughly, but **the exact scoring scales (1-5 definitions) for Soundness, Excitement/Novelty, Overall Assessment, Confidence, and Reproducibility are not explicitly detailed in this reviewer guidelines page**.

The document mentions that reviewers must provide three scores:

- **"Soundness scores must be justified by the text of the review"** (Section 5)
- **"Excitement scores reflect our personal taste"** and differ from soundness assessment (Section 5)
- **"Overall assessment score is an explicit recommendation for the outcome"** (Section 5)

However, **the specific 1-5 point definitions for each scale are not included in this content**. These may be located in:
- The actual OpenReview review form interface
- A separate [ARR review form documentation](https://aclrollingreview.org/reviewform) referenced in the FAQ
- The linked presentation slides about OpenReview usage

To obtain the exact scoring rubrics, you would need to consult those additional resources or access the live OpenReview platform itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3866
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-22T08:35:55.049783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form soundness excitement score scale 1 2 3 4 5 definition OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form soundness excitement score scale 1 2 3 4 5 definition OpenReview"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-22T08:36:02.228543+00:00_

Web search results for query: "ACL ARR review form soundness excitement score scale 1 2 3 4 5 definition OpenReview"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"aclrollingreview/acguidelines.md at main · yoshitomo-matsubara/aclrollingreview","url":"https://github.com/yoshitomo-matsubara/aclrollingreview/blob/main/acguidelines.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL ARR review form soundness and excitement score scales:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score

Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a sepa
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7178
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-22T08:36:06.296065+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring scales with their exact definitions. I need the complete 1-5 scale for: Soundness, Excitement, Overall Assessment, Confidence, and Reproducibility. Give me every single score level definition (1, 2, 3, 4, 5 for each dimension)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract ALL scoring scales with their exact definitions. I need the complete 1-5 scale for: Soundness, Excitement, Overall Assessment, Confidence, and Reproducibility. Give me every single score level definition (1, 2, 3, 4, 5 for each dimension)."
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-22T08:36:15.478943+00:00_

# ACL Rolling Review: Scoring Scales

## Reviewer Confidence
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully. It's unlikely, though conceivable, that I missed something that should affect my ratings."
- **3:** "Pretty sure, but there's a chance I missed something. Although I have a good feel for this area in general, I did not carefully check the paper's details, e.g., the math or experimental design."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details, didn't understand some central points, or can't be sure about the novelty of the work."
- **1:** "Not my area, or paper is very hard to understand. My evaluation is just an educated guess."

## Soundness
- **5:** "Excellent: This study is one of the most thorough I have seen, given its type."
- **4:** "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3:** "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."
- **2:** "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## Excitement
- **5:** "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4:** "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3:** "Interesting: I might mention some points of this paper to others and/or attend its presentation in a conference if there's time."
- **2:** "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."
- **1:** "Not Exciting: this pap
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9182
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-22T08:36:41.365116+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-22T08:36:41.466115+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	When attention layers are added to linear recurrent architectures, they help and hurt almost entirely different examples across backbones: pairwise overlap among three controlled hybrid designs is at most 10\%, far below the 78--92\% theoretical maximum. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales, single training runs per configuration), we decompose per-example effects on four benchmarks and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$ for reasoning, $0.30$ for retrieval) rather than attention dose. Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction (Bonferroni-adjusted $p = .100$). On this benchmark, aggregate variance decreases gradually while per-example overlap saturates at the first attention level, a saturation pattern that generalizes to all four benchmarks regardless of aggregate convergence. A proof-of-concept majority vote across architectures fails to outperform the best individual model despite 15--45\% per-example disagreement, while oracle accuracy reveals 7--14\,pp of untapped complementarity, suggesting that architectures interchangeable by aggregate metrics may carry hidden consequences for per-example reliability.
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections
…[truncated 1932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-22T08:36:55.927792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 789 · 2026-05-22T08:36:55.978525+00:00_

1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA, aggregate variance decreases with attention while per-example overlap saturates, consistent with architecture-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Aggregate benchmark equivalence thus masks per-example divergence: each backbone develops architecture-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect nearly disjoint examples. A majority vote across three architectures fails to consistently outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp; gains on other benchmarks $< 0.2$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-22T08:37:59.881138+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 791 · 2026-05-22T08:37:59.934595+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-22T08:38:08.616953+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-22T08:38:08.629072+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_11/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 12
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-22T08:39:57.718419+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：新颖性 + 完整性 + 写作质量 + 格式合规\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n---\n\n## Summary（2-3 句）\n\n本文利用 Wang et al. (2025) 的受控 model zoo，对三种 hybrid linear recurrent 架构（GatedDeltaNet、RetNet、HGRN2）在五个 attention ratio 和两个模型规模下的 per-example predictive multiplicity 进行系统分析。核心发现包括：task-dependent 的 per-example variation（σ = 0.14–0.30）、aggregate convergence 与 per-example divergence 的 decoupling、以及 per-example Jaccard 在首个 attention level 即饱和。论文推荐在 hybrid 架构选型时进行 per-example audit。\n\n---\n\n## Strengths\n\n**S1. 受控实验设计出色。** 基于 Wang et al. (2025) 的 model zoo，训练数据、超参数完全匹配，仅以架构和 attention ratio 为变量，提供了干净的因果隔离。这显著优于使用不同训练流程的模型对比（Section 3.1）。\n\n**S2. 统计方法论扎实。** 综合使用 permutation test（Section 3.5, Appendix J）、accelerated bootstrap CI、Bonferroni 校正、Mann-Whitney U 和 Kruskal-Wallis 非参数检验，方法论上体现了统计严谨性。Power considerations（Section 3.5, n=5 ordinal levels, 无法检测小效应）的明确说明是负责任的做法。\n\n**S3. Per-example 分解直觉且实用。** Helped/Hurt/Unchanged 三分法（Section 3.4）清晰直观，per-example effect 的分类体系让 \"15–45% 的 individual predictions 不一致\" 这个发现具有部署层面的实际意义。\n\n**S4. Appendix 极其充实。** 10 页 appendix 覆盖了 GDN confound 分析（Appendix E）、attention weight 分析（Appendix F）、cross-scale 对比（Appendix G）、complementarity decomposition（Appendix T）等，为主文claims 提供了扎实的补充支撑。GDN head confound 的专门分析（Appendix E）体现了良好的研究实践。\n\n**S5. Decoupling 的具体实证有价值。** Per-example Jaccard 在首个 attention level（~4%）即饱和至 ~0.095，而 aggregate variance 继续下降（Section 4.3, Figure 1）——这一具体的 saturation pattern 跨越四个 benchmark 成立，具有实践意义：增加更多 attention 并不进一步同质化 per-example predictions。\n\n**S6. Confidence margin 分析增加深度。** Section 4.2 的 helped vs. hurt 分析（target-token probability、rescue/disruption pattern）超越了单纯的 agreement counting，揭示了 architecture-specific 的 confidence profile 差异。\n\n---\n\n## Weaknesses\n\n**W1 [Critical] 正文超过 8 页限制。**\n- 具体位置：Section 5 (Conclusion) 起始于 page 8 右栏底部，延续至 page 9 左栏约 1/3 处\n- 问题：EMNLP 2026 要求正文（Sections 1–5）严格 ≤ 8 页，Limitations/Ethics 不计入但 Conclusion 计入。当前正文约 8.1–8.2 页，超出限制。\n- 为什么影响接收：这是 hard formatting constraint，可能导致 desk reject\n- 建议修改方向：压缩 Section 4.1（Task-Specific Convergence）和 Section 4.3（Decoupling）的叙述，将部分 convergence 细节移至 appendix；或精简 Table 2 的文字讨论\n\n**W2 [Major] 新颖性有限——核心贡献是已有指标在新 setting 的应用。**\n- 具体位置：Section 3.3–3.4（Convergence Metrics, Pre-Example Decomposition）\n- 问题：论文的核心分析工具——Jaccard similarity（Marx et al. 2020）、ambiguity σ、permutation test、helped/hurt 分类——全部来自先前工作。方法论上的增量贡献薄弱。论文的价值在于 setting（hybrid architectures + controlled attention variation）的时效性，而非在 metrics、theory 或 methodology 上的创新。\n- 为什么影响接收：对于 main conference，\"已有指标 × 新 setting\" 的组合通常被认为增量较小，除非产出了意料之外的深刻洞见\n- 建议修改方向：（1）提出针对 hybrid 架构的新指标或分析方法；（2）深入解释 saturation 的机制（为什么恰好在首个 attention level 即饱和？Section 4.3 描述了现象但未解释原因）；（3）或提供理论分析（如从 gating mechanism 的数学性质推导 multiplicity 的 bound）\n\n**W3 [Major] \"Decoupling\" 发现部分可预期。**\n- 具体位置：Section 4.3\n- 问题：Aggregate means 收敛但 individual-level variation 持续——这是基本统计现象（ecological fallacy 的变体）。论文将此框架为 \"finding\"（Section 4.3 标题 \"Decoupling\"），但更准确的说法是 \"empirical confirmation of a known statistical possibility\"。真正新颖的是 Jaccard 在首个 attention level 饱和的具体 pattern，但这一发现被更宽泛的 \"decoupling\" 叙事淹没了。\n- 建议修改方向：降低 decoupling 作为 \"发现\" 的权重，突出 saturation 的具体 pattern 和可能的机制解释\n\n**W4 [Major] 从窄实验基础过度泛化。**\n- 具体位置：Section 5（Conclusion）\n- 问题：论文从 3 个架构、1 个 model zoo、pre-training only、4 个主 benchmark 的实验中得出宽泛的实践建议（\"per-example audits are warranted whenever multiple hybrid designs achieve comparable aggregate scores\"）。最强的 findings 集中在 LAMBADA——唯一展现单调 convergence 的 benchmark（Table 1, ρ = −1.0）。LAMBADA 是纯 retrieval task，其特殊性（long-range dependency, direct token-level access）在多大程度上驱动了结论？其他三个 benchmark 的 convergence 不显著（Bonferroni-adjusted p > 0.100, Table 1），generalization claim 的支撑不足。\n- 建议修改方向：明确限定结论的适用范围；区分 LAMBADA-specific 与 generalizable 的 findings；将 practical protocol 定位为 \"preliminary evidence suggests\" 而非 \"results warrant\"\n\n**W5 [Minor] Abstract 信息过载。**\n- 问题：Abstract 堆砌了大量数字（σ = 0.14, 0.30, 78–92%, 15–45%, 7–14pp），缺乏叙事脉络。α = 0.14 和 0.30 的含义在没有 context 的情况下不可解读。\"78–92% theoretical maximum\" 未经解释难以理解。\n- 建议：减少数字，加强 narrative flow——先建立 intuition（what & why），再给关键 evidence\n\n**W6 [Minor] Convergence 叙事占比过高。**\n- 问题：Section 4.1（Task-Specific Convergence）+ Section 4.3（Decoupling）+ Appendix B–C 在 convergence 主题上花费了过多篇幅，但如 W3 所述，这一发现的新颖性有限。这些空间可以更好地用于深化 per-example 分析（如 Section 4.2 的 confidence margin 分析）或探讨机制。\n\n**W7 [Minor] Appendix L 使用未定义术语 \"entrainment\"。**\n- 具体位置：Appendix L 标题 \"Transformer Entrainment Comparison\"\n- 问题：\"Entrainment\" 在语音学、流体力学中有专门含义，此处未定义。应替换为更明确的术语（如 \"Transformer Convergence Comparison\"）或添加定义。\n\n**W8 [Minor] Table 1 可读性。**\n- 问题：Table 1 的五列指标（ρ, σ, σ_pure, ρ_{h3-1}, Ratio）密度高，列名 \"Ratio\" 过于模糊。需要反复参照 caption 才能理解。\n- 建议：使用更具描述性的列名（如 \"σ Reduction\" 替代 \"Ratio\"），或拆分为两个小表\n\n---\n\n## Questions\n\n**Q1.** Section 4.3 的 decoupling——aggregate convergence 与 per-example Jaccard saturation 的关系是否可从数学上推导？即：在什么条件下，pairwise accuracy agreement 可以增加而 pairwise Jaccard 保持不变？这是否简单地因为 Jaccard 对 small probability shifts 不敏感（考虑到 binarization threshold at 0.5/0.69, Appendix O.1）？\n\n**Q2.** Jaccard 在首个 attention level（~4%）即饱和至 ~0.095（Section 4.3）：是否有关于 hybrid architecture 中 gating mechanism 的结构性解释？Appendix F 的 attention weight 分析显示 layer-wise convergence，但这如何 translate 到 per-example prediction agreement 的 saturation？\n\n**Q3.** Majority vote 失败（Section 5: LAMBADA −0.2pp, ARC-Easy −1.1pp）而 oracle accuracy 显示 +7–14pp complementarity——这暗示存在 learnable selection function。是否尝试过任何 learned combination method（如 stacking, routing）？如果没有，为什么不作为 future work 更明确地提出？\n\n**Q4.** 论文的 BoolQ 和 WinoGrande 分析（Appendix P, Q）提供了重要的 supplementary evidence。为什么这两个 benchmark 被降为 supplementary 而非包含在主文中？如果 4 个主 benchmark 中 convergence 仅在 LAMBADA 显著，加入 BoolQ/WinoGrande 的 non-convergence 结果是否会改变 overall narrative？\n\n**Q5.** Section 4.2 的 confidence margin 分析使用 target-token probability 作为 proxy。对于 multiple-choice benchmarks（HellaSwag, ARC-Easy），accuracy 基于 option ranking 而非 token probability——confidence margin 的定义在这些 benchmarks 上是否保持一致？\n\n---\n\n## Missing References\n\n1. **Ensemble diversity measures（Kuncheva & Whitaker, 2003）。** 论文的核心指标（pairwise Jaccard）本质上是 ensemble diversity measure，但未与 ensemble learning 文献中的多种 diversity metrics（Q-statistic, disagreement measure, double-fault measure）做对比或讨论选择理由。解释为何选择 Jaccard 而非这些替代指标会加强 Section 3.3 的方法论。\n\n2. **Rashomon set 的理论框架。** Marx et al. (2020) 虽已引用，但未讨论 Rashomon set 的更广泛理论背景（Fisher et al. 2019; Semenova et al. 2022）。这些工作为 multiplicity 何时出现以及如何系统化地刻画提供了理论基础，可以加强 Section 2 的 Related Work。\n\n3. **Cross-architecture agreement 的 scaling law 视角。** 论文有两个 scale points（340M, 1.3B）但未与 scaling law 文献对接。如果 per-example multiplicity 有可预测的 scaling behavior，这将大大增加论文的理论贡献。\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实（统计检验、robustness check、confound 分析），但 single training run 限制了因果推断，部分 generalization claims 超出数据支撑范围 |\n| Excitement | 2.5/5 | Setting 时效性好（hybrid architectures 是当前热点），但核心贡献是已有指标的应用，insights 部分可预期（decoupling），缺乏方法论或理论创新 |\n| Reproducibility | 4/5 | 使用公开 model zoo，statistical methods 标准且详细描述，代码承诺发布。单一训练 run 意味着精确复现可行 |\n| Confidence | 4/5 | 熟悉 predictive multiplicity 文献、hybrid architecture 领域和所用统计方法 |\n\n### Overall Assessment\n\n- **Score: 3.0**（Findings: 可被 Findings 接收）\n- **一句话总结**: 实验设计严谨、统计分析扎实的 empirical study，但核心贡献停留在已有指标对新 setting 的应用层面，新颖性不足以达到 main conference 标准；需先修复页数超限问题。\n\n### 详细理由\n\n**支持 3.0 的因素：**\n- 受控实验设计和扎实的统计方法论（S1, S2）\n- Per-example audit 的实践价值（S3）\n- Saturation pattern 跨 benchmark 一致性（S5）\n- 极其充实的 appendix（S4）\n\n**限制 3.0 的因素：**\n- 新颖性主要在 setting 而非 method/theory（W2）\n- Decoupling 部分可预期（W3）\n- 从 LAMBADA-dominant 的 evidence 过度泛化（W4）\n- 正文超页（W1, 需修复）\n\n**从 3.0 提升至 3.5+ 的路径：**\n- 提出 hybrid architecture 特有的新 multiplicity metric 或 theoretical bound\n- 为 Jaccard saturation 提供 mechanistic explanation（不仅仅是描述现象）\n- 扩展到 fine-tuned models 或更多架构以加强 generalizability\n- 或展示 per-example multiplicity 信息在实际任务（如 model selection, selective prediction）中的 utility",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：新颖性 + 完整性 + 写作质量 + 格式合规\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n---\n\n## Summary（2-3 句）\n\n本文利用 Wang et al. (2025) 的受控 model zoo，对三种 hybrid linear recurrent 架构（GatedDeltaNet、RetNet、HGRN2）在五个 attention ratio 和两个模型规模下的 per-example predictive multiplicity 进行系统分析。核心发现包括：task-dependent 的 per-example variation（σ = 0.14–0.30）、aggregate convergence 与 per-example divergence 的 decoupling、以及 per-example Jaccard 在首个 attention level 即饱和。论文推荐在 hybrid 架构选型时进行 per-example audit。\n\n---\n\n## Strengths\n\n**S1. 受控实验设计出色。** 基于 Wang et al. (2025) 的 model zoo，训练数据、超参数完全匹配，仅以架构和 attention ratio 为变量，提供了干净的因果隔离。这显著优于使用不同训练流程的模型对比（Section 3.1）。\n\n**S2. 统计方法论扎实。** 综合使用 permutation test（Section 3.5, Appendix J）、accelerated bootstrap CI、Bonferroni 校正、Mann-Whitney U 和 Kruskal-Wallis 非参数检验，方法论上体现了统计严谨性。Power considerations（Section 3.5, n=5 ordinal levels, 无法检测小效应）的明确说明是负责任的做法。\n\n**S3. Per-example 分解直觉且实用。** Helped/Hurt/Unchanged 三分法（Section 3.4）清晰直观，per-example effect 的分类体系让 \"15–45% 的 individual predictions 不一致\" 这个发现具有部署层面的实际意义。\n\n**S4. Appendix 极其充实。** 10 页 appendix 覆盖了 GDN confound 分析（Appendix E）、attention weight 分析（Appendix F）、cross-scale 对比（Appendix G）、complementarity decomposition（Appendix T）等，为主文claims 提供了扎实的补充支撑。GDN head confound 的专门分析（Appendix E）体现了良好的研究实践。\n\n**S5. Decoupling 的具体实证有价值。** Per-example Jaccard 在首个 attention level（~4%）即饱和至 ~0.095，而 aggregate variance 继续下降（Section 4.3, Figure 1）——这一具体的 saturation pattern 跨越四个 benchmark 成立，具有实践意义：增加更多 attention 并不进一步同质化 per-example predictions。\n\n**S6. Confidence margin 分析增加深度。** Section 4.2 的 helped vs. hurt 分析（target-token probability、rescue/disruption pattern）超越了单纯的 agreement counting，揭示了 architecture-specific 的 confidence profile 差异。\n\n---\n\n## Weaknesses\n\n**W1 [Critical] 正文超过 8 页限制。**\n- 具体位置：Section 5 (Conclusion) 起始于 page 8 右栏底部，延续至 page 9 左栏约 1/3 处\n- 问题：EMNLP 2026 要求正文（Sections 1–5）严格 ≤ 8 页，Limitations/Ethics 不计入但 Conclusion 计入。当前正文约 8.1–8.2 页，超出限制。\n- 为什么影响接收：这是 hard formatting constraint，可能导致 desk reject\n- 建议修改方向：压缩 Section 4.1（Task-Specific Convergence）和 Section 4.3（Decoupling）的叙述，将部分 convergence 细节移至 appendix；或精简 Table 2 的文字讨论\n\n**W2 [Major] 新颖性有限——核心贡献是已有指标在新 setting 的应用。**\n- 具体位置：Section 3.3–3.4（Convergence Metrics, Pre-Example Decomposition）\n- 问题：论文的核心分析工具——Jaccard similarity（Marx et al. 2020）、ambiguity σ、permutation test、helped/hurt 分类——全部来自先前工作。方法论上的增量贡献薄弱。论文的价值在于 setting（hybrid architectures + controlled attention variation）的时效性，而非在 metrics、theory 或 methodology 上的创新。\n- 为什么影响接收：对于 main conference，\"已有指标 × 新 setting\" 的组合通常被认为增量较小，除非产出了意料之外的深刻洞见\n- 建议修改方向：（1）提出针对 hybrid 架构的新指标或分析方法；（2）深入解释 saturation 的机制（为什么恰好在首个 attention level 即饱和？Section 4.3 描述了现象但未解释原因）；（3）或提供理论分析（如从 gating mechanism 的数学性质推导 multiplicity 的 bound）\n\n**W3 [Major] \"Decoupling\" 发现部分可预期。**\n- 具体位置：Section 4.3\n- 问题：Aggregate means 收敛但 individual-level variation 持续——这是基本统计现象（ecological fallacy 的变体）。论文将此框架为 \"finding\"（Section 4.3 标题 \"Decoupling\"），但更准确的说法是 \"empirical confirmation of a known statistical possibility\"。真正新颖的是 Jaccard 在首个 attention level 饱和的具体 pattern，但这一发现被更宽泛的 \"decoupling\" 叙事淹没了。\n- 建议修改方向：降低 decoupling 作为 \"发现\" 的权重，突出 saturation 的具体 pattern 和可能的机制解释\n\n**W4 [Major] 从窄实验基础过度泛化。**\n- 具体位置：Section 5（Conclusion）\n- 问题：论文从 3 个架构、1 个 model zoo、pre-training only、4 个主 benchmark 的实验中得出宽泛的实践建议（\"per-example audits are warranted whenever multiple hybrid designs achieve comparable aggregate scores\"）。最强的 findings 集中在 LAMBADA——唯一展现单调 convergence 的 benchmark（Table 1, ρ = −1.0）。LAMBADA 是纯 retrieval task，其特殊性（long-range dependency, direct token-level access）在多大程度上驱动了结论？其他三个 benchmark 的 convergence 不显著（Bonferroni-adjusted p > 0.100, Table 1），generalization claim 的支撑不足。\n- 建议修改方向：明确限定结论的适用范围；区分 LAMBADA-specific 与 generalizable 的 findings；将 practical protocol 定位为 \"preliminary evidence suggests\" 而非 \"results warrant\"\n\n**W5 [Minor] Abstract 信息过载。**\n- 问题：Abstract 堆砌了大量数字（σ = 0.14, 0.30, 78–92%, 15–45%, 7–14pp），缺乏叙事脉络。α = 0.14 和 0.30 的含义在没有 context 的情况下不可解读。\"78–92% theoretical maximum\" 未经解释难以理解。\n- 建议：减少数字，加强 narrative flow——先建立 intuition（what & why），再给关键 evidence\n\n**W6 [Minor] Convergence 叙事占比过高。**\n- 问题：Section 4.1（Task-Specific Convergence）+ Section 4.3（Decoupling）+ Appendix B–C 在 convergence 主题上花费了过多篇幅，但如 W3 所述，这一发现的新颖性有限。这些空间可以更好地用于深化 per-example 分析（如 Section 4.2 的 confidence margin 分析）或探讨机制。\n\n**W7 [Minor] Appendix L 使用未定义术语 \"entrainment\"。**\n- 具体位置：Appendix L 标题 \"Transformer Entrainment Comparison\"\n- 问题：\"Entrainment\" 在语音学、流体力学中有专门含义，此处未定义。应替换为更明确的术语（如 \"Transformer Convergence Comparison\"）或添加定义。\n\n**W8 [Minor] Table 1 可读性。**\n- 问题：Table 1 的五列指标（ρ, σ, σ_pure, ρ_{h3-1}, Ratio）密度高，列名 \"Ratio\" 过于模糊。需要反复参照 caption 才能理解。\n- 建议：使用更具描述性的列名（如 \"σ Reduction\" 替代 \"Ratio\"），或拆分为两个小表\n\n---\n\n## Questions\n\n**Q1.** Section 4.3 的 decoupling——aggregate convergence 与 per-example Jaccard saturation 的关系是否可从数学上推导？即：在什么条件下，pairwise accuracy agreement 可以增加而 pairwise Jaccard 保持不变？这是否简单地因为 Jaccard 对 small probability shifts 不敏感（考虑到 binarization threshold at 0.5/0.69, Appendix O.1）？\n\n**Q2.** Jaccard 在首个 attention level（~4%）即饱和至 ~0.095（Section 4.3）：是否有关于 hybrid architecture 中 gating mechanism 的结构性解释？Appendix F 的 attention weight 分析显示 layer-wise convergence，但这如何 translate 到 per-example prediction agreement 的 saturation？\n\n**Q3.** Majority vote 失败（Section 5: LAMBADA −0.2pp, ARC-Easy −1.1pp）而 oracle accuracy 显示 +7–14pp complementarity——这暗示存在 learnable selection function。是否尝试过任何 learned combination method（如 stacking, routing）？如果没有，为什么不作为 future work 更明确地提出？\n\n**Q4.** 论文的 BoolQ 和 WinoGrande 分析（Appendix P, Q）提供了重要的 supplementary evidence。为什么这两个 benchmark 被降为 supplementary 而非包含在主文中？如果 4 个主 benchmark 中 convergence 仅在 LAMBADA 显著，加入 BoolQ/WinoGrande 的 non-convergence 结果是否会改变 overall narrative？\n\n**Q5.** Section 4.2 的 confidence margin 分析使用 target-token probability 作为 proxy。对于 multiple-choice benchmarks（HellaSwag, ARC-Easy），accuracy 基于 option ranking 而非 token probability——confidence margin 的定义在这些 benchmarks 上是否保持一致？\n\n---\n\n## Missing References\n\n1. **Ensemble diversity measures（Kuncheva & Whitaker, 2003）。** 论文的核心指标（pairwise Jaccard）本质上是 ensemble diversity measure，但未与 ensemble learning 文献中的多种 diversity metrics（Q-statistic, disagreement measure, double-fault measure）做对比或讨论选择理由。解释为何选择 Jaccard 而非这些替代指标会加强 Section 3.3 的方法论。\n\n2. **Rashomon set 的理论框架。** Marx et al. (2020) 虽已引用，但未讨论 Rashomon set 的更广泛理论背景（Fisher et al. 2019; Semenova et al. 2022）。这些工作为 multiplicity 何时出现以及如何系统化地刻画提供了理论基础，可以加强 Section 2 的 Related Work。\n\n3. **Cross-architecture agreement 的 scaling law 视角。** 论文有两个 scale points（340M, 1.3B）但未与 scaling law 文献对接。如果 per-example multiplicity 有可预测的 scaling behavior，这将大大增加论文的理论贡献。\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论扎实（统计检验、robustness check、confound 分析），但 single training run 限制了因果推断，部分 generalization claims 超出数据支撑范围 |\n| Excitement | 2.5/5 | Setting 时效性好（hybrid architectures 是当前热点），但核心贡献是已有指标的应用，insights 部分可预期（decoupling），缺乏方法论或理论创新 |\n| Reproducibility | 4/5 | 使用公开 model zoo，statistical methods 标准且详细描述，代码承诺发布。单一训练 run 意味着精确复现可行 |\n| Confidence | 4/5 | 熟悉 predictive multiplicity 文献、hybrid architecture 领域和所用统计方法 |\n\n### Overall Assessment\n\n- **Score: 3.0**（Findings: 可被 Findings 接收）\n- **一句话总结**: 实验设计严谨、统计分析扎实的 empirical study，但核心贡献停留在已有指标对新 setting 的应用层面，新颖性不足以达到 main conference 标准；需先修复页数超限问题。\n\n### 详细理由\n\n**支持 3.0 的因素：**\n- 受控实验设计和扎实的统计方法论（S1, S2）\n- Per-example audit 的实践价值（S3）\n- Saturation pattern 跨 benchmark 一致性（S5）\n- 极其充实的 appendix（S4）\n\n**限制 3.0 的因素：**\n- 新颖性主要在 setting 而非 method/theory（W2）\n- Decoupling 部分可预期（W3）\n- 从 LAMBADA-dominant 的 evidence 过度泛化（W4）\n- 正文超页（W1, 需修复）\n\n**从 3.0 提升至 3.5+ 的路径：**\n- 提出 hybrid architecture 特有的新 multiplicity metric 或 theoretical bound\n- 为 Jaccard saturation 提供 mechanistic explanation（不仅仅是描述现象）\n- 扩展到 fine-tuned models 或更多架构以加强 generalizability\n- 或展示 per-example multiplicity 信息在实际任务（如 model selection, selective prediction）中的 utility",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-22T08:40:02.403081+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4684
}
```

</details>

---


### Assistant

_source line 796 · 2026-05-22T08:40:11.029121+00:00_

审稿意见已提交给 Review Director。

**核心判断：Overall 3.0（Findings）。**

关键问题：
- **Critical**：正文超 8 页限制（Conclusion 溢出至 page 9）
- **Major**：新颖性有限（已有指标 × 新 setting）、decoupling 发现部分可预期、从 LAMBADA-dominant 的 evidence 过度泛化
- **主要优势**：受控实验设计出色、统计方法论扎实、saturation pattern 有实践意义、appendix 极充实

提升路径：需要在方法论/理论上有增量创新（如 hybrid 架构特有的 multiplicity metric 或 saturation 的 mechanistic explanation），而非仅停留在指标应用层面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

76 recorded events


### User

_source line 797 · 2026-05-22T08:44:21.540691+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 审查。

## Venue 信息
- **会议**: EMNLP 2026（通过 ARR May 2026 cycle 投稿）
- **类别**: Long Paper
- **正文页数限制**: 8 页（参考文献不限）
- **Limitations**: 必须有，不计入页数
- **模板**: ACL（\usepackage[review]{acl}）
- **匿名规则**: Double-blind
- **Deadline**: 2026-05-25
- **评分标准**: ARR Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf`

## 你的审查侧重

1. **新颖性评估**：
   - 核心贡献——将 predictive multiplicity (Marx 2020) 框架应用于 hybrid recurrent 架构——方法学新颖性有多少？
   - "Decoupling" 发现（aggregate convergence vs per-example divergence）是否构成 non-trivial insight？
   - 与 underspecification (D'Amour 2022)、seed-based multiplicity (McCoy 2020, MultiBERTs) 的区分是否充分？
   - 对该领域的贡献是否达到 EMNLP 主会议/Findings 水平？

2. **完整性检查**：
   - Related Work 是否覆盖关键文献？是否有重要遗漏？
   - 实验范围（3 architectures, 2 scales, 10 benchmarks）是否足够支撑 claims？
   - Practical implications（ensemble failure, oracle gap）是否有足够支撑？
   - Limitations 的坦诚度和覆盖面

3. **写作质量**：
   - Abstract 信息密度是否过高（数字堆砌）？
   - Contribution 的表述是否匹配证据强度？
   - 叙事结构：convergence 占的叙事权重（~40% 主文）是否与其 exploratory 定位匹配？
   - 因果语言 vs associative 语言的使用
   - 术语 "predictive multiplicity" 的使用是否技术准确？

4. **格式合规**：
   - 正文是否在 8 页内？
   - Limitations 格式是否合规？
   - 匿名性是否满足 double-blind？

请提供结构化审稿报告：Summary → Strengths → Weaknesses（按 Critical/Major/Minor 分级）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-22T08:44:29.302963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-22T08:44:30.007002+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-22T08:44:30.007424+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 801 · 2026-05-22T08:44:30.058818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-22T08:44:34.978477+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-22T08:44:35.732330+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 804 · 2026-05-22T08:44:42.986886+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key details about ACL ARR 2026 reviewer guidelines, review form, and scoring criteria:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Score

The Overall assessment score is an explicit recommendation for the outcome o
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8008
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-22T08:44:44.748039+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9015
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-22T08:44:49.568742+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other fields. List the exact scale descriptions for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: soundness, excitement, overall assessment, confidence, and any other fields. List the exact scale descriptions for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-22T08:44:50.456466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-22T08:44:50.869065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-22T08:44:51.323630+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 867
}
```

</details>

---


### Tool call

_source line 810 · 2026-05-22T08:44:51.324102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 811 · 2026-05-22T08:44:52.233433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-22T08:44:52.234216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-22T08:44:52.435855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 814 · 2026-05-22T08:44:53.543003+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2218
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-22T08:44:53.997382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1763
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-22T08:44:54.098786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1662
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-22T08:44:55.453997+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully"
- **4:** "Quite sure. I tried to check the important points carefully"
- **3:** "Pretty sure, but there's a chance I missed something"
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1:** "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5:** "Excellent: This study is one of the most thorough I have seen"
- **4:** "Strong: This study provides sufficient support for all claims"
- **3:** "Acceptable: This study provides sufficient support for main claims"
- **2:** "Poor: Some main claims not sufficiently supported"
- **1:** "Major Issues: This study is not yet sufficiently thorough"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5:** "Highly Exciting: I would recommend this paper to others"
- **4:** "Exciting: I would mention this paper to others"
- **3:** "Interesting: I might mention some points"
- **2:** "Potentially Interesting: does not resonate with me"
- **1:** "Not Exciting: does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5:** Consider for Award
- **4:** Conference acceptance
- **3:** Findings of the ACL
- **2:** Resubmit next cycle
- **1:** Do not resubmit

## 5. **Additional Dimensions**

**Reproducibility** (1-5): Details availability for result replication

**Datasets** (1-5): Value of newly released datasets

**Software** (1-5): Value of newly released software

**Author Identity Knowledge** (1-5): Anonymity assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5885
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-22T08:45:00.180057+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-22T08:45:00.482083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-22T08:45:01.435944+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-22T08:45:01.438164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-22T08:45:01.438600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-22T08:45:01.941221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-22T08:45:02.946089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1507
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-22T08:45:02.946865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-22T08:45:03.047886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T08:45:03.650338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-22T08:45:03.902268+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-22T08:45:05.585041+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 410.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 401.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1682
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-22T08:45:10.608818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 831 · 2026-05-22T08:45:11.162038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 832 · 2026-05-22T08:45:11.715559+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1106
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-22T08:45:11.716847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-22T08:45:11.768817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-22T08:45:12.071231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-22T08:45:12.978977+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-22T08:45:12.981266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-22T08:45:12.981714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-22T08:45:13.533888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-22T08:45:13.936463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-22T08:45:14.038288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-22T08:45:14.892611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-22T08:45:14.893876+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-22T08:45:14.894199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-22T08:45:15.447786+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-22T08:45:15.498362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 847 · 2026-05-22T08:45:15.800817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-22T08:45:15.853502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-22T08:45:16.105572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-22T08:45:25.294964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-22T08:45:25.696462+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	When attention layers are added to linear recurrent architectures, they help and hurt almost entirely different examples across backbones: pairwise overlap among three controlled hybrid designs is at most 10\%, far below the 78--92\% theoretical maximum. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales, single training runs per configuration), we decompose per-example effects on four benchmarks and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$ for reasoning, $0.30$ for retrieval) rather than attention dose. Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction (Bonferroni-adjusted $p = .100$). On this benchmark, aggregate variance decreases gradually while per-example overlap saturates at the first attention level, a saturation pattern that generalizes to all four benchmarks regardless of aggregate convergence. A proof-of-concept majority vote across architectures fails to outperform the best individual model despite 15--45\% per-example disagreement, while oracle accuracy reveals 7--14\,pp of untapped complementarity, suggesting that architectures interchangeable by aggregate metrics may carry hidden consequences for per-example reliability.
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections
…[truncated 1932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-22T08:45:29.060275+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL fields, scoring dimensions, their exact scales and descriptions. I need every single field including: paper summary, soundness (full scale 1-5 with descriptions), excitement (full scale 1-5), overall assessment (full scale 1-5 with all intermediate values like 3.5, 2.5 etc), confidence, reproducibility, limitations, ethical concerns, best paper nomination, and any other fields. Give me the exact text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL fields, scoring dimensions, their exact scales and descriptions. I need every single field including: paper summary, soundness (full scale 1-5 with descriptions), excitement (full scale 1-5), overall assessment (full scale 1-5 with all intermediate values like 3.5, 2.5 etc), confidence, reproducibility, limitations, ethical concerns, best paper nomination, and any other fields. Give me the exact text for each score level."
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-22T08:45:38.295946+00:00_

# ACL Rolling Review - Complete Review Form Structure

## Main Review Fields

**Paper Summary**: Describe paper topic to help editors understand work and clarify potential misunderstandings.

**Summary of Strengths**: Identify major publication reasons—novel methodology, empirical results, theoretical analysis, clear literature organization.

**Summary of Weaknesses**: List numbered concerns about correctness, impact, clarity, or other factors affecting publication priority.

**Comments/Suggestions/Typos**: Additional improvement suggestions beyond addressing main concerns.

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale):
- 5: "Positive that my evaluation is correct. I read the paper very carefully..."
- 4: "Quite sure. I tried to check the important points carefully..."
- 3: "Pretty sure, but there's a chance I missed something..."
- 2: "Willing to defend my evaluation, but it is fairly likely..."
- 1: "Not my area, or paper is very hard to understand..."

**Soundness** (1-5 with .5 increments):
- 5: "Excellent: This study is one of the most thorough..."
- 4: "Strong: This study provides sufficient support..."
- 3: "Acceptable: This study provides sufficient support..."
- 2: "Poor: Some of the main claims are not sufficiently supported..."
- 1: "Major Issues: This study is not yet sufficiently thorough..."

**Excitement** (1-5 with .5 increments):
- 5: "Highly Exciting: I would recommend this paper to others..."
- 4: "Exciting: I would mention this paper to others..."
- 3: "Interesting: I might mention some points..."
- 2: "Potentially Interesting: this paper does not resonate with me..."
- 1: "Not Exciting: this paper does not resonate with me..."

**Overall Assessment** (1-5 with .5 increments):
- 5: "Consider for Award: up to top 2.5% papers"
- 4.5: "Borderline Award"
- 4: "Conference: I think this paper could be accepted..."
- 3.5: "Borderline Conference"
- 3: "Findings: I think this paper could be accepted to Findings..."
- 2.5: "Borderline Finding
…[truncated 1379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9235
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-22T08:45:43.317731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-22T08:45:43.368608+00:00_

1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: on LAMBADA, cross-architecture standard deviation drops 79\% as attention increases (Bonferroni-adjusted $p = .100$; the heuristic BCa 95\% CI excludes zero), but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Our results show that architectures scoring identically in aggregate may nonetheless differ on 15--45\% of individual predictions, meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{mar
…[truncated 5400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-22T08:45:43.469872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-22T08:45:43.470430+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} achieves near-Transformer quality with gated convolutions and SSMs, establishing an early design point in the hybrid space. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification: equivalent a
…[truncated 1804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-22T08:45:48.840982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-22T08:45:49.092496+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\subsection{Task Taxonomy}\label{ssec:task_taxonomy}
10	
11	We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy was fixed prior to analysis following established distinctions in the hybrid architecture literature \citep{arora2024zoology} (see Appendix~A for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test 
…[truncated 7056 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-22T08:45:49.143308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-22T08:45:49.194009+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\subsection{Task-Specific Convergence}\label{ssec:task_convergence}
6	
7	Table~\ref{tab:convergence} reports cross-architecture $\sigma$ at each attention ratio for all benchmarks at 1.3B scale. LAMBADA is the only benchmark exhibiting monotonic convergence: $\rho = -1.0$ ($p = .017$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic given $n = 3$ architectures, \S\ref{ssec:statistical_methods}; $\sigma$ drops 79\%; Bonferroni-adjusted $p = .100$; excluding GDN: $\rho = -0.7$, $p = .233$, \S\ref{ssec:robustness}). This is consistent with attention reducing differences in how recurrent architectures retrieve from context \citep{arora2024zoology}: LAMBADA requires predicting a final word from long-range dependencies, and attention provides direct token-level access that narrows architectural differences in recall capacity \citep{arora2024based}. The three recurrent backbones differ in how they compress sequential context (exponential decay in RetNet, gated expansion in HGRN2, delta rules in GDN), creating divergent retrieval capacities that attention may bypass via direct token access. For reasoning and comprehension tasks, the bottleneck likely lies in multi-step inference rather than context retrieval, so attention is not associated with similar variance reduction. No other benchmark shows significant convergence (all $|\rho| \leq 0.7$, $p \geq .233$; Figure~\ref{fig:task_specificity}). Full convergence discussion appears in Appendix~\ref{app:convergence_detail}. Scale analysis (Appendix~\ref{app:scale_convergence}) shows this convergence is present at 1.3B but absent at 340M. Statistical power is inherently lim
…[truncated 13244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-22T08:45:56.709494+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-22T08:45:56.810227+00:00_

1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA, aggregate variance decreases with attention while per-example overlap saturates, consistent with architecture-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Aggregate benchmark equivalence thus masks per-example divergence: each backbone develops architecture-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect nearly disjoint examples. A majority vote across three architectures fails to consistently outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp; gains on other benchmarks $< 0.2$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-22T08:45:57.011815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-22T08:45:57.062757+00:00_

1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The Bonferroni-adjusted significance threshold is $\alpha / 6 = 0.0083$. \textbf{Sensitivity:} correcting across all 10 benchmarks yields adjusted $p = 0.017 \times 10 = 0.170$, further from significance; the main text reports the confirmatory-set correction ($\times 6 = 0.100$).
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 6-benchmark Bonferroni correction, this yields an adjusted $p = 0.050$, exactly at the conventional threshold. We report two-sided test
…[truncated 12193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-22T08:47:12.455551+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 867 · 2026-05-22T08:47:12.456093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-22T08:47:18.077490+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-22T08:47:18.078040+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-22T08:49:14.325101+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的实证分析揭示了 hybrid recurrent 架构在 aggregate 指标等价下存在结构化的 per-example 分歧，但核心新颖性为观察性发现而非方法创新，convergence claim 统计证据不足且依赖单一 benchmark，practical implications 缺乏验证。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Per-example divergence 的主要 claim（低 Jaccard、task-dependent α）有充分支撑；但 convergence claim Bonferroni-adjusted p=.100 未达显著、依赖 GDN 包含且有 head confound，单训练 run 无法区分 seed vs architecture 效应 |\n| Excitement | 2.5/5 | \"Decoupling\" 发现有价值但偏 observational；将 predictive multiplicity 扩展到架构变体是合理延伸但非 paradigm shift；缺乏 actionable 的实践指导 |\n| Reproducibility | 4/5 | 使用公开 model zoo、标准 lm-eval-harness、详述统计方法；代码承诺 release |\n| Confidence | 4/5 | 仔细阅读了全文及全部附录，熟悉 predictive multiplicity 和 hybrid architecture 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Convergence claim 的叙事权重与证据强度严重不匹配\n- 具体位置：§4.1 (整节)、§4.3 大量篇幅、§4.4、Abstract、Introduction\n- 问题：LAMBADA convergence（ρ = −1.0）是论文的核心 narrative 之一，但：\n  - Bonferroni-adjusted p = .100，**未达 α = 0.05 常规显著性水平**\n  - 排除 GDN 后降至 ρ = −0.7, p = .233（§4.4）\n  - GDN h3-1 使用 16 个 attention heads（其他配置均为 32），存在 confound（Appendix E）\n  - 在 340M scale 上不成立（Appendix C: ρ = −0.50, p = .45）\n  - 10 个 benchmarks 中仅 LAMBADA 一个显示此趋势\n  - 论文却将约 40% 的正文空间用于 convergence 分析（§4.1 + §4.3/§4.4 的 convergence 部分）\n- 为什么影响接收：一个仅基于单一 benchmark、未达显著性、依赖特定架构（且该架构有 confound）的 exploratory finding，占据了与 robust 的 per-example divergence finding 几乎对等的叙事地位。这会误导读者高估 convergence 证据的可靠性。\n- 建议修改方向：(1) 大幅压缩 §4.1 的 convergence 讨论，明确标记为 exploratory observation；(2) 将叙事重心转移到更 robust 的 per-example multiplicity findings（低 Jaccard、task-dependent α）；(3) \"Decoupling\"（§4.3）可以保留，但应以 per-example saturation 为主线，convergence 作为对比背景而非并列发现。\n\n**N2** [critical] 单训练 run 对核心 claim 的限制未被充分讨论\n- 具体位置：Limitations 段落 2、Introduction contributions\n- 问题：每个配置仅一次训练 run。论文用 within- vs cross-architecture Jaccard 的 3× gap（§4.3）作为 proxy evidence，但这是间接证据。McCoy et al. (2020) 和 MultiBERTs (Sellam et al., 2022) 已经证明 **同一架构不同 seed 之间也存在显著的 per-example disagreement**。论文未与这些 seed-based multiplicity 基线做定量对比。因此无法确定：\n  - 观察到的 cross-architecture α = 0.14–0.30 是否显著大于 within-architecture seed variation 所产生的 α\n  - 低 Jaccard（≤0.10）是否也会出现在同一架构的不同 seed 之间\n  - \"架构身份是 per-example 分歧的主要来源\" 这一隐含 claim 是否成立\n- 为什么影响接收：如果 seed variation 本身就能产生类似的 per-example multiplicity，那么论文的核心贡献——\"architectural variation drives structured per-example divergence\"——的增量价值就大打折扣。\n- 建议修改方向：(1) 在 Limitations 中明确承认这一 gap，而非仅一句 \"single training runs prevent full disentanglement\"；(2) 最好能引用 MultiBERTs 等工作报告的 seed-based α 值做定量对比；(3) 如果做不到定量对比，至少将 contribution 的措辞从 \"architectural variation is associated with structured per-example predictive multiplicity\" 软化为更 conditional 的表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Predictive multiplicity\" 术语的技术准确性\n- 具体位置：Title、Abstract、§2 (Related Work)、§4.2、全文\n- 问题：Marx et al. (2020) 将 predictive multiplicity 定义为 **Rashomon set 内近最优模型之间的分歧**——即在相同训练 pipeline 下、aggregate 性能近似等价的模型集合。本文将其应用于 **不同架构** 的比较，这些架构有不同的 inductive biases、不同的 recurrence 机制，甚至不同的 aggregate 准确率（Table 1 显示 σ_pure = 2.41，意味着架构间存在 non-trivial 的 aggregate 差异）。虽然 α 指标本身的计算是正确的，但 \"predictive multiplicity\" 这一术语暗示了 Rashomon set 的语境，可能误导读者认为这与 Marx (2020) 的现象同质。\n- 建议：在 §2 或 §3 中明确区分：Marx (2020) 的 multiplicity 来自 near-optimal 模型集合中的 underspecification，而本文的 multiplicity 来自 architectural variation under matched training conditions。可以继续使用 α 指标，但建议加一句 \"We adopt the ambiguity metric α from Marx et al. (2020) while noting that our source of variation (architecture) differs from the original setting (model selection within the Rashomon set).\"\n\n**W2** [warning] Practical implications 缺乏验证\n- 具体位置：§5 Conclusion 第 2 段、Abstract 最后一句\n- 问题：论文声称 majority vote 失败（LAMBADA: −0.2pp, ARC-Easy: −1.1pp）而 oracle accuracy 有 +7–14pp gap，但：\n  - MV 和 oracle 分析仅在 pre-trained 模型上进行，无 fine-tuning\n  - 仅使用 3 个架构的 naive MV，未尝试任何 informed selection 方法\n  - Oracle gap 的 \"untapped complementarity\" 被用于支撑 \"selection methods beyond naive ensembling\" 的建议，但论文未提供任何此类方法的实证\n- 建议：要么删减 practical implications 的强度，要么至少尝试一个简单的 confidence-based selection 方法（论文已有 confidence margin 分析，AUC 0.70–0.74，这是 natural 的下一步）。\n\n**W3** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（整段）\n- 问题：Abstract 在约 200 词内塞入了至少 15 个具体数字（10%, 78–92%, 0.14, 0.30, p = .100, 79%, 15–45%, 7–14pp 等），使得第一次阅读几乎无法提取核心 message。对于一篇以 insight 为主而非数值 benchmark 为主的论文，这种密度适得其反。\n- 建议：(1) 删减至多保留 5–6 个关键数字；(2) 用一句清晰的 high-level statement 开头（如 \"Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples\"——这句话已经在 Introduction 里了，但 Abstract 里被数字淹没了）。\n\n**W4** [warning] 因果语言 vs 关联语言的不一致使用\n- 具体位置：多处\n- 问题：论文在大部分地方谨慎使用 \"associated with\"、\"consistent with\" 等关联性语言（如 §4.1 \"attention is not associated with similar variance reduction\"），但在某些关键位置滑入因果性表述：\n  - §4.3: \"convergence arose from attention uniformly rescuing the same difficult examples\"（虽然是反事实条件句，但暗示了因果机制）\n  - §5: \"each backbone develops architecture-specific response patterns\"（\"develops\" 暗示因果/生成过程）\n  - §4.2: \"architecture-specific thresholds that produce the observed cross-architecture divergence\"（\"produce\"）\n- 建议：统一使用 associative language，或明确标注哪些是 mechanistic hypotheses vs empirical observations。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 脚注标记不一致**：LAMBADA 标记为 ‡（GDN head confound），COPA 标记为 †（supplementary），但 Bonferroni 校正说明在脚注最后一行，容易遗漏。建议将 Bonferroni 信息移入正文。\n\n2. **§3.4 per-example decomposition 的二值化丢失信息**：论文承认 \"a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01\"（§4.2），并用 Cohen's d = 0.73–0.92 验证了分离度。但 Appendix O（Confidence Margin）的分析似乎比主文的二值化分析更有信息量——考虑在主文中给予更多篇幅。\n\n3. **Figure 1 可读性**：Figure 1(b) 的 y 轴范围（约 0.05–0.12）使得 saturation 在视觉上不够明显。建议调整 y 轴起点或添加参考线。\n\n4. **§3.5 power considerations 的放置位置**：关于 n=5 ordinal levels 导致 binary resolution 的讨论放在 Method 中很好，但建议在 §4.1 首次报告 LAMBADA p = .017 时再次提醒读者这一限制。\n\n5. **Appendix 标签**：Appendix 使用字母标签（A–T），但某些交叉引用在主文中使用 section 编号格式，可能造成困惑。\n\n---\n\n## 主要优势\n\n1. **研究问题的价值**：揭示 aggregate metric 等价性掩盖 per-example 分歧是一个重要且 under-explored 的问题，对 hybrid architecture 选型有实际意义。\n\n2. **实验设计的严谨性**：利用 Wang et al. (2025) 的 controlled model zoo（匹配 training data/tokenizer/hyperparams，仅变化架构和 attention ratio）是该研究问题的理想实验设置。\n\n3. **统计方法的透明度**：n=5 ordinal levels 的 power limitation、BCa CI 的 degeneracy、Bonferroni 校正的 exact calculation、one-sided vs two-sided test 的对比——统计处理的诚实和透明度远超 NLP 论文的平均水平。\n\n4. **\"Decoupling\" 发现**：aggregate σ 逐渐下降而 per-example Jaccard 在 4% attention 即饱和——这是一个 non-trivial 的 empirical insight，如果 framing 得当可以成为论文最强贡献。\n\n5. **Confidence margin mechanism**：AUC 0.70–0.74 的 predictive power + rescue thresholds architecture-invariant vs disruption thresholds vary 47% 的不对称性是一个有趣的 mechanistic finding。\n\n6. **Limitations 的坦诚度**：三段 limitations 覆盖了 generalization、single runs、pre-training only，且不回避核心弱点（如 \"minimum achievable p-value is 0.017\"）。\n\n---\n\n## Questions for Authors\n\nQ1. 能否提供 MultiBERTs (Sellam et al., 2022) 或 McCoy et al. (2020) 报告的 within-architecture seed-based α 或 Jaccard 值，与本文的 cross-architecture 值做定量对比？这是区分 \"architectural variation matters above seed noise\" 的关键证据。\n\nQ2. GDN h3-1 的 16-head confound：是否可以在 GDN 的其他 attention ratios（h6-1, h12-1, h24-1）上检查 head count？如果只有 h3-1 是 16-head，那么 convergence 的 endpoint（ρ = −1.0 而非 −0.9）可能主要由这个 confound 驱动。\n\nQ3. 论文报告 confidence margin AUC = 0.70–0.74。是否尝试过用 confidence-based 选择代替 naive majority vote？鉴于 oracle gap 有 7–14pp，即使是简单的 max-confidence 选择也可能部分弥合这个 gap，从而大幅增强 practical relevance。\n\nQ4. Task taxonomy（§3.2）声称是 pre-registered (\"fixed prior to analysis\")，但无外部 timestamp。能否提供更强的证据（如 commit history、pre-registration record）？如果不能，建议更明确地标注为 \"pre-specified but not formally pre-registered\"。\n\nQ5. 关于 scale effect：340M 的 α 系统性高于 1.3B（Δ ≤ 8pp），但 convergence 在 340M 上消失。这是否暗示 convergence 是 sufficient capacity 的 emergent property 而 multiplicity 是 fundamental？如果是，这对实践的含义是什么——更大模型是否可能同时展示更强的 convergence 和更低的 multiplicity？\n\n---\n\n## Missing References\n\n1. **Model soups / weight averaging**: Wortsman et al. (2022) \"Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time\"——论文讨论了 ensemble failure 和 oracle gap，但未引用 model merging/soups 文献。这些方法提供了 naive MV 之外的架构组合策略，直接相关于 §5 的 practical implications。\n\n2. **Calibration**: Guo et al. (2017) \"On Calibration of Modern Neural Networks\"——confidence margin analysis（§4.2, Appendix O）是论文的重要贡献之一，但未引用 calibration 文献。Confidence threshold 的 architecture-specific 差异可能部分由 calibration 差异解释。\n\n3. **Dodge et al. (2020)** \"Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping\"——seed variation 在 fine-tuning 中对 per-example 行为的影响，与论文的 seed-vs-architecture 讨论直接相关。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n这是一篇方法论上严谨、统计处理透明的实证研究，提出了一个有价值的观察：hybrid recurrent 架构在 aggregate 性能等价下存在结构化的 per-example 分歧。\"Decoupling\" 发现（aggregate convergence vs per-example Jaccard saturation）是 non-trivial 的 insight。\n\n但我认为达不到主会议标准（4.0）的原因是：\n1. **新颖性主要是 observational**——核心方法（Jaccard on helped/hurt sets + permutation tests）是标准工具的组合应用，insight 虽有价值但未推进方法论\n2. **Convergence claim 证据不足**——仅一个 benchmark、marginal significance、GDN confound、scale-dependent——却占据 ~40% 叙事空间\n3. **Single run limitation** 使得核心 claim（architecture vs seed）缺乏 definitive evidence\n4. **Practical implications 未 closed**——发现了 oracle gap 但未提供任何 actionable 的解决方案\n5. **\"Predictive multiplicity\" framing** 虽然合理但并非技术精确的扩展，更像是将已有 framework 重新应用于新 domain\n\n论文的统计诚实度、实验覆盖度（30 configurations × 10 benchmarks × 2 scales）、以及丰富的 sensitivity analyses 使其达到 Findings 水平。如果能补充 seed baseline 对比、压缩 convergence 叙事权重、并增加一个 confidence-based selection 的 proof-of-concept，有潜力升至 3.5。\n\n**Confidence: 4/5** — 仔细阅读了全文及全部 10 页附录，熟悉 predictive multiplicity、underspecification 和 hybrid architecture 相关文献。",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 扎实的实证分析揭示了 hybrid recurrent 架构在 aggregate 指标等价下存在结构化的 per-example 分歧，但核心新颖性为观察性发现而非方法创新，convergence claim 统计证据不足且依赖单一 benchmark，practical implications 缺乏验证。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Per-example divergence 的主要 claim（低 Jaccard、task-dependent α）有充分支撑；但 convergence claim Bonferroni-adjusted p=.100 未达显著、依赖 GDN 包含且有 head confound，单训练 run 无法区分 seed vs architecture 效应 |\n| Excitement | 2.5/5 | \"Decoupling\" 发现有价值但偏 observational；将 predictive multiplicity 扩展到架构变体是合理延伸但非 paradigm shift；缺乏 actionable 的实践指导 |\n| Reproducibility | 4/5 | 使用公开 model zoo、标准 lm-eval-harness、详述统计方法；代码承诺 release |\n| Confidence | 4/5 | 仔细阅读了全文及全部附录，熟悉 predictive multiplicity 和 hybrid architecture 相关文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Convergence claim 的叙事权重与证据强度严重不匹配\n- 具体位置：§4.1 (整节)、§4.3 大量篇幅、§4.4、Abstract、Introduction\n- 问题：LAMBADA convergence（ρ = −1.0）是论文的核心 narrative 之一，但：\n  - Bonferroni-adjusted p = .100，**未达 α = 0.05 常规显著性水平**\n  - 排除 GDN 后降至 ρ = −0.7, p = .233（§4.4）\n  - GDN h3-1 使用 16 个 attention heads（其他配置均为 32），存在 confound（Appendix E）\n  - 在 340M scale 上不成立（Appendix C: ρ = −0.50, p = .45）\n  - 10 个 benchmarks 中仅 LAMBADA 一个显示此趋势\n  - 论文却将约 40% 的正文空间用于 convergence 分析（§4.1 + §4.3/§4.4 的 convergence 部分）\n- 为什么影响接收：一个仅基于单一 benchmark、未达显著性、依赖特定架构（且该架构有 confound）的 exploratory finding，占据了与 robust 的 per-example divergence finding 几乎对等的叙事地位。这会误导读者高估 convergence 证据的可靠性。\n- 建议修改方向：(1) 大幅压缩 §4.1 的 convergence 讨论，明确标记为 exploratory observation；(2) 将叙事重心转移到更 robust 的 per-example multiplicity findings（低 Jaccard、task-dependent α）；(3) \"Decoupling\"（§4.3）可以保留，但应以 per-example saturation 为主线，convergence 作为对比背景而非并列发现。\n\n**N2** [critical] 单训练 run 对核心 claim 的限制未被充分讨论\n- 具体位置：Limitations 段落 2、Introduction contributions\n- 问题：每个配置仅一次训练 run。论文用 within- vs cross-architecture Jaccard 的 3× gap（§4.3）作为 proxy evidence，但这是间接证据。McCoy et al. (2020) 和 MultiBERTs (Sellam et al., 2022) 已经证明 **同一架构不同 seed 之间也存在显著的 per-example disagreement**。论文未与这些 seed-based multiplicity 基线做定量对比。因此无法确定：\n  - 观察到的 cross-architecture α = 0.14–0.30 是否显著大于 within-architecture seed variation 所产生的 α\n  - 低 Jaccard（≤0.10）是否也会出现在同一架构的不同 seed 之间\n  - \"架构身份是 per-example 分歧的主要来源\" 这一隐含 claim 是否成立\n- 为什么影响接收：如果 seed variation 本身就能产生类似的 per-example multiplicity，那么论文的核心贡献——\"architectural variation drives structured per-example divergence\"——的增量价值就大打折扣。\n- 建议修改方向：(1) 在 Limitations 中明确承认这一 gap，而非仅一句 \"single training runs prevent full disentanglement\"；(2) 最好能引用 MultiBERTs 等工作报告的 seed-based α 值做定量对比；(3) 如果做不到定量对比，至少将 contribution 的措辞从 \"architectural variation is associated with structured per-example predictive multiplicity\" 软化为更 conditional 的表述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"Predictive multiplicity\" 术语的技术准确性\n- 具体位置：Title、Abstract、§2 (Related Work)、§4.2、全文\n- 问题：Marx et al. (2020) 将 predictive multiplicity 定义为 **Rashomon set 内近最优模型之间的分歧**——即在相同训练 pipeline 下、aggregate 性能近似等价的模型集合。本文将其应用于 **不同架构** 的比较，这些架构有不同的 inductive biases、不同的 recurrence 机制，甚至不同的 aggregate 准确率（Table 1 显示 σ_pure = 2.41，意味着架构间存在 non-trivial 的 aggregate 差异）。虽然 α 指标本身的计算是正确的，但 \"predictive multiplicity\" 这一术语暗示了 Rashomon set 的语境，可能误导读者认为这与 Marx (2020) 的现象同质。\n- 建议：在 §2 或 §3 中明确区分：Marx (2020) 的 multiplicity 来自 near-optimal 模型集合中的 underspecification，而本文的 multiplicity 来自 architectural variation under matched training conditions。可以继续使用 α 指标，但建议加一句 \"We adopt the ambiguity metric α from Marx et al. (2020) while noting that our source of variation (architecture) differs from the original setting (model selection within the Rashomon set).\"\n\n**W2** [warning] Practical implications 缺乏验证\n- 具体位置：§5 Conclusion 第 2 段、Abstract 最后一句\n- 问题：论文声称 majority vote 失败（LAMBADA: −0.2pp, ARC-Easy: −1.1pp）而 oracle accuracy 有 +7–14pp gap，但：\n  - MV 和 oracle 分析仅在 pre-trained 模型上进行，无 fine-tuning\n  - 仅使用 3 个架构的 naive MV，未尝试任何 informed selection 方法\n  - Oracle gap 的 \"untapped complementarity\" 被用于支撑 \"selection methods beyond naive ensembling\" 的建议，但论文未提供任何此类方法的实证\n- 建议：要么删减 practical implications 的强度，要么至少尝试一个简单的 confidence-based selection 方法（论文已有 confidence margin 分析，AUC 0.70–0.74，这是 natural 的下一步）。\n\n**W3** [warning] Abstract 信息密度过高\n- 具体位置：Abstract（整段）\n- 问题：Abstract 在约 200 词内塞入了至少 15 个具体数字（10%, 78–92%, 0.14, 0.30, p = .100, 79%, 15–45%, 7–14pp 等），使得第一次阅读几乎无法提取核心 message。对于一篇以 insight 为主而非数值 benchmark 为主的论文，这种密度适得其反。\n- 建议：(1) 删减至多保留 5–6 个关键数字；(2) 用一句清晰的 high-level statement 开头（如 \"Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples\"——这句话已经在 Introduction 里了，但 Abstract 里被数字淹没了）。\n\n**W4** [warning] 因果语言 vs 关联语言的不一致使用\n- 具体位置：多处\n- 问题：论文在大部分地方谨慎使用 \"associated with\"、\"consistent with\" 等关联性语言（如 §4.1 \"attention is not associated with similar variance reduction\"），但在某些关键位置滑入因果性表述：\n  - §4.3: \"convergence arose from attention uniformly rescuing the same difficult examples\"（虽然是反事实条件句，但暗示了因果机制）\n  - §5: \"each backbone develops architecture-specific response patterns\"（\"develops\" 暗示因果/生成过程）\n  - §4.2: \"architecture-specific thresholds that produce the observed cross-architecture divergence\"（\"produce\"）\n- 建议：统一使用 associative language，或明确标注哪些是 mechanistic hypotheses vs empirical observations。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 脚注标记不一致**：LAMBADA 标记为 ‡（GDN head confound），COPA 标记为 †（supplementary），但 Bonferroni 校正说明在脚注最后一行，容易遗漏。建议将 Bonferroni 信息移入正文。\n\n2. **§3.4 per-example decomposition 的二值化丢失信息**：论文承认 \"a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01\"（§4.2），并用 Cohen's d = 0.73–0.92 验证了分离度。但 Appendix O（Confidence Margin）的分析似乎比主文的二值化分析更有信息量——考虑在主文中给予更多篇幅。\n\n3. **Figure 1 可读性**：Figure 1(b) 的 y 轴范围（约 0.05–0.12）使得 saturation 在视觉上不够明显。建议调整 y 轴起点或添加参考线。\n\n4. **§3.5 power considerations 的放置位置**：关于 n=5 ordinal levels 导致 binary resolution 的讨论放在 Method 中很好，但建议在 §4.1 首次报告 LAMBADA p = .017 时再次提醒读者这一限制。\n\n5. **Appendix 标签**：Appendix 使用字母标签（A–T），但某些交叉引用在主文中使用 section 编号格式，可能造成困惑。\n\n---\n\n## 主要优势\n\n1. **研究问题的价值**：揭示 aggregate metric 等价性掩盖 per-example 分歧是一个重要且 under-explored 的问题，对 hybrid architecture 选型有实际意义。\n\n2. **实验设计的严谨性**：利用 Wang et al. (2025) 的 controlled model zoo（匹配 training data/tokenizer/hyperparams，仅变化架构和 attention ratio）是该研究问题的理想实验设置。\n\n3. **统计方法的透明度**：n=5 ordinal levels 的 power limitation、BCa CI 的 degeneracy、Bonferroni 校正的 exact calculation、one-sided vs two-sided test 的对比——统计处理的诚实和透明度远超 NLP 论文的平均水平。\n\n4. **\"Decoupling\" 发现**：aggregate σ 逐渐下降而 per-example Jaccard 在 4% attention 即饱和——这是一个 non-trivial 的 empirical insight，如果 framing 得当可以成为论文最强贡献。\n\n5. **Confidence margin mechanism**：AUC 0.70–0.74 的 predictive power + rescue thresholds architecture-invariant vs disruption thresholds vary 47% 的不对称性是一个有趣的 mechanistic finding。\n\n6. **Limitations 的坦诚度**：三段 limitations 覆盖了 generalization、single runs、pre-training only，且不回避核心弱点（如 \"minimum achievable p-value is 0.017\"）。\n\n---\n\n## Questions for Authors\n\nQ1. 能否提供 MultiBERTs (Sellam et al., 2022) 或 McCoy et al. (2020) 报告的 within-architecture seed-based α 或 Jaccard 值，与本文的 cross-architecture 值做定量对比？这是区分 \"architectural variation matters above seed noise\" 的关键证据。\n\nQ2. GDN h3-1 的 16-head confound：是否可以在 GDN 的其他 attention ratios（h6-1, h12-1, h24-1）上检查 head count？如果只有 h3-1 是 16-head，那么 convergence 的 endpoint（ρ = −1.0 而非 −0.9）可能主要由这个 confound 驱动。\n\nQ3. 论文报告 confidence margin AUC = 0.70–0.74。是否尝试过用 confidence-based 选择代替 naive majority vote？鉴于 oracle gap 有 7–14pp，即使是简单的 max-confidence 选择也可能部分弥合这个 gap，从而大幅增强 practical relevance。\n\nQ4. Task taxonomy（§3.2）声称是 pre-registered (\"fixed prior to analysis\")，但无外部 timestamp。能否提供更强的证据（如 commit history、pre-registration record）？如果不能，建议更明确地标注为 \"pre-specified but not formally pre-registered\"。\n\nQ5. 关于 scale effect：340M 的 α 系统性高于 1.3B（Δ ≤ 8pp），但 convergence 在 340M 上消失。这是否暗示 convergence 是 sufficient capacity 的 emergent property 而 multiplicity 是 fundamental？如果是，这对实践的含义是什么——更大模型是否可能同时展示更强的 convergence 和更低的 multiplicity？\n\n---\n\n## Missing References\n\n1. **Model soups / weight averaging**: Wortsman et al. (2022) \"Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time\"——论文讨论了 ensemble failure 和 oracle gap，但未引用 model merging/soups 文献。这些方法提供了 naive MV 之外的架构组合策略，直接相关于 §5 的 practical implications。\n\n2. **Calibration**: Guo et al. (2017) \"On Calibration of Modern Neural Networks\"——confidence margin analysis（§4.2, Appendix O）是论文的重要贡献之一，但未引用 calibration 文献。Confidence threshold 的 architecture-specific 差异可能部分由 calibration 差异解释。\n\n3. **Dodge et al. (2020)** \"Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping\"——seed variation 在 fine-tuning 中对 per-example 行为的影响，与论文的 seed-vs-architecture 讨论直接相关。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n\n这是一篇方法论上严谨、统计处理透明的实证研究，提出了一个有价值的观察：hybrid recurrent 架构在 aggregate 性能等价下存在结构化的 per-example 分歧。\"Decoupling\" 发现（aggregate convergence vs per-example Jaccard saturation）是 non-trivial 的 insight。\n\n但我认为达不到主会议标准（4.0）的原因是：\n1. **新颖性主要是 observational**——核心方法（Jaccard on helped/hurt sets + permutation tests）是标准工具的组合应用，insight 虽有价值但未推进方法论\n2. **Convergence claim 证据不足**——仅一个 benchmark、marginal significance、GDN confound、scale-dependent——却占据 ~40% 叙事空间\n3. **Single run limitation** 使得核心 claim（architecture vs seed）缺乏 definitive evidence\n4. **Practical implications 未 closed**——发现了 oracle gap 但未提供任何 actionable 的解决方案\n5. **\"Predictive multiplicity\" framing** 虽然合理但并非技术精确的扩展，更像是将已有 framework 重新应用于新 domain\n\n论文的统计诚实度、实验覆盖度（30 configurations × 10 benchmarks × 2 scales）、以及丰富的 sensitivity analyses 使其达到 Findings 水平。如果能补充 seed baseline 对比、压缩 convergence 叙事权重、并增加一个 confidence-based selection 的 proof-of-concept，有潜力升至 3.5。\n\n**Confidence: 4/5** — 仔细阅读了全文及全部 10 页附录，熟悉 predictive multiplicity、underspecification 和 hybrid architecture 相关文献。",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-22T08:49:18.341477+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 872 · 2026-05-22T08:49:26.934626+00:00_

审稿报告已提交给 Review Director。

**审稿结论：Overall 3.0 (Findings)**

核心评价：
- **2 个 Critical 问题**：(1) Convergence claim 占 ~40% 叙事但仅基于单一 benchmark 且 Bonferroni-adjusted p=.100 未达显著、依赖有 confound 的 GDN；(2) 单训练 run 无法区分 seed vs architecture 效应，缺乏与 MultiBERTs 等 seed-based baseline 的定量对比
- **4 个 Warning 问题**：predictive multiplicity 术语精确性、practical implications 未验证、Abstract 数字堆砌、因果 vs 关联语言不一致
- **主要优势**：实验设计利用 controlled model zoo 十分契合、统计透明度高、"decoupling" 发现有价值、confidence margin mechanism 有趣

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

4 recorded events


### User

_source line 873 · 2026-05-22T08:50:35.755586+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见（完整原文）

**Overall Score: 3.5 (Borderline Conference)**
**Soundness 3/5 | Excitement 4/5 | Reproducibility 3/5 | Confidence 4/5**

### Must-Fix 问题
**N1 [Critical] Spearman ρ 在 n=5 上统计推断力根本性不足，正文过度依赖不显著趋势。** Table 1 中 10 个 benchmark 只有 LAMBADA (ρ=−1.0) 达显著。其余 9 个 p>0.05（HellaSwag ρ=0.4 p=.517, PIQA ρ=−0.5 p=.450）。但正文 §4.1 大量讨论非显著趋势。建议：Table 1 醒目区分显著/不显著；正文严格区分 "significant convergence (LAMBADA only)" 和 "descriptive trends"。

**N2 [Critical] 单次训练 run 导致 architecture 与 seed 效应完全混淆。** 每个 configuration 仅一次 run，无法区分 architecture-specific vs seed-specific 效应。Within- vs cross-architecture Jaccard gap (3×) 作为间接证据本身也可能受 seed 影响。建议：讨论 seed variance 典型量级；最好提供 multi-seed 验证。

### Should-Fix 问题
**W1 [Warning] GDN h3-1 的 16-head confound 正文处理不充分。** 移除 GDN 后 LAMBADA ρ 从 −1.0 弱化到 −0.7，MMLU 从 −0.7 反转到 +0.7。正文 §4.4 仅一句带过。

**W2 [Warning] 二值化 per-example 分解丢弃 continuous confidence 信息。** confidence 0.49→0.51 算 "helped"，0.51→0.99 算 "unchanged"。建议补充 continuous threshold sensitivity analysis。

**W3 [Warning] Bonferroni 校正的 confirmatory/exploratory 划分缺乏预注册。** 事后声明 6 confirmatory benchmarks。全 10 benchmarks Bonferroni (α/10=0.005) 下 LAMBADA p=0.017 也不显著。

**W4 [Warning] 因果语言在 observational design 下时有越界。** Abstract/§1/§4.1/§4.3 多处使用因果表述（"attention reduces"、"attention shifts"）。建议改为关联表述。

### 小问题
- lm-eval-harness 版本号缺失
- Greedy decoding 说明不完整
- Table 2 中 α 的 scale 不直观
- Appendix S subsample sensitivity 正文未提及

### Questions
Q1. Model zoo 中是否有不同 seed 同架构 pairs 可报告 within-architecture Jaccard？
Q2. 全 10 benchmarks Bonferroni 校正下整篇论文没有显著结果，如何回应？
Q3. 是否分析过 raw log-likelihood（非 binary acc_norm）的 per-example 效应？
Q4. MMLU exclusion-GDN 后 ρ 从 −0.7 到 +0.7——MMLU convergence 是否完全由 GDN 16-head confound 驱动？
Q5. 340M 下 convergence 消失，是否应限定 convergence claim 为 "1.3B scale only"？

### Missing References
- Jiang et al. (2022) per-example model behavior differences
- Black et al. (2022) 关于 seed variance 的讨论

---

请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W4)、小问题、Question (Q1-Q5)、Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-22T08:52:00.722876+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Spearman ρ 在 n=5 上统计推断力不足，正文过度依赖不显著趋势**\n\n同意，且我在自己的 N1 中提出了本质相同的问题。补充几点：\n\n1. 论文 §3.5 Power considerations 已诚实披露 \"only ρ = ±1.0 achieves p < .05\"，这是加分项，但这一限制的后果在 §4.1 的叙事中未被充分体现。§4.1 用了一整段讨论 LAMBADA convergence 的机制（\"attention provides direct token-level access...\"），给一个 Bonferroni-adjusted p = .100 的结果赋予了不匹配的 mechanistic certainty。\n2. R1 建议 \"Table 1 醒目区分显著/不显著\" 是好建议。目前 Table 1 仅用 bold 标记 ρ = −1.0，但 Bonferroni-adjusted p = .100 本身也不显著——bold 可能误导读者。\n3. 我进一步认为，即便区分了显著/不显著，**convergence 在叙事中的权重也应大幅压缩**（我的 N1），因为 10 个 benchmark 中仅 1 个显示趋势、且该趋势依赖 GDN 包含。\n\n**[AGREE] R1-N2: 单次训练 run 导致 architecture 与 seed 效应混淆**\n\n完全同意，这也是我的 N2。补充 R1 未明确提到的一点：\n\n论文用 within- vs cross-architecture Jaccard 的 3× gap（§4.3: ~0.33 vs ~0.10）作为 proxy evidence。但这个对比的含义是 **within-architecture across attention ratios** vs **cross-architecture at matched ratio**，即它衡量的是 \"同一架构在不同 attention dose 下的 per-example 变化\" vs \"不同架构在相同 attention dose 下的 per-example 变化\"。这**不等于** seed-vs-architecture 的对比。如果同一架构的不同 seed 产生的 Jaccard 也在 ~0.10 水平（McCoy et al. 2020 和 MultiBERTs 的结果暗示这是可能的），那么 3× gap 可能仅仅反映了 attention dose 变化是一个比 architecture 切换更 \"温和\" 的 perturbation——不能用来支撑 \"architecture is the primary driver\" 的论点。\n\nR1 建议 \"讨论 seed variance 典型量级\" 是最低限度的要求；multi-seed 验证是理想方案但可能超出 revision scope（model zoo 是外部资源）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: GDN h3-1 的 16-head confound 正文处理不充分**\n\n同意。§4.4 的处理确实过于简略。我补充两点 R1 未提到的：\n\n1. MMLU 从 ρ = −0.7 反转到 +0.6（非 R1 所述的 +0.7；见 Table 3, Appendix D）是一个严重的 instability signal——说明即使在 3 个架构的小样本下，单一架构的 confound 就能完全翻转相关方向。这强化了 convergence finding 的脆弱性。\n2. 更关键的是，GDN confound 不仅影响 convergence，也可能影响 per-example 分析：如果 GDN h3-1 的 attention capacity 因为 head 数不同而系统性偏低，那么 GDN 的 helped/hurt profile 可能部分由 capacity 差异驱动，而非纯粹的 architectural divergence。论文未分析排除 GDN 后的 per-example Jaccard 是否发生显著变化。\n\n**[REBUT] R1-W2: 二值化 per-example 分解丢弃 continuous confidence 信息**\n\n部分不同意。R1 的担忧有道理，但论文实际上已经提供了相当充分的回应：\n\n1. §4.2 明确承认了二值化的局限性（\"a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01\"）\n2. §4.2 报告了 helped/hurt 之间的 Cohen's d = 0.73–0.92，证明二值化确实捕捉到了 continuous confidence space 中的真实分离\n3. Appendix O (Confidence Margin) 提供了 continuous 分析：AUC 0.70–0.74、rescue/disruption thresholds 的非对称性\n4. Appendix P (BoolQ Supplementary) 和 cross-benchmark 分析进一步验证了 continuous patterns\n\n我认为论文已有的 continuous 分析是充分的。R1 建议的 \"continuous threshold sensitivity analysis\" 可以作为改进，但不是 should-fix 级别的问题。**建议降级为 minor。**\n\n**[AGREE] R1-W3: Bonferroni 校正的 confirmatory/exploratory 划分缺乏预注册**\n\n同意。Appendix A 明确承认 \"no external timestamp exists\"，但仍使用 \"confirmatory\" 一词。这在措辞上有误导性。\n\n补充：论文使用 6-benchmark Bonferroni 得到 adjusted p = .100，但如果用全 10-benchmark Bonferroni（Appendix A 自己计算了：adjusted p = .170），LAMBADA 更远离显著性。论文选择报告 6-benchmark 校正而非 10-benchmark 校正，在缺乏真正预注册的情况下，这个选择本身就是一种 researcher degree of freedom。\n\n建议：删除 \"confirmatory\" 标签，统一报告 10-benchmark Bonferroni（adjusted p = .170），并将 6-benchmark 版本作为 sensitivity check 放入附录。\n\n**[AGREE] R1-W4: 因果语言在 observational design 下时有越界**\n\n同意，这与我的 W4 完全一致。论文的 controlled design（matched training conditions）确实比纯 observational 研究有更强的因果推断基础，但 single run + 无 intervention 仍然不足以支撑因果表述。\n\n补充一个 R1 未提到的例子：§5 Conclusion 中 \"each backbone develops architecture-specific response patterns\" 的 \"develops\" 暗示了一个 generative/causal 过程，但论文只观察到了 cross-sectional association。\n\n---\n\n### 小问题\n\n**[AGREE] lm-eval-harness 版本号缺失**：§3.2 提到 \"v0.4.x\"——x 应该明确为具体版本号（如 v0.4.2），因为不同 minor 版本之间 prompt templates 可能有差异。\n\n**[REBUT] Greedy decoding 说明不完整**：§3.2 明确写了 \"default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks\"。这对于 lm-eval-harness 来说是标准且充分的说明。不清楚 R1 认为还需要什么额外信息。\n\n**[AGREE] Table 2 中 α 的 scale 不直观**：α = .14 表示 14% 的 examples 受影响，但读者可能需要一秒才能 parse。建议在 Table caption 或脚注中加一句 \"α represents the fraction of examples on which architectures disagree\"。\n\n**[AGREE] Appendix S subsample sensitivity 正文未提及**：Appendix S 分析了 σ estimation 在不同 subsample sizes 下的稳定性（95% CI），这是一个有价值的 robustness check。正文 §4.2 或 §3.5 应该至少引用一次。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: Model zoo 中是否有不同 seed 同架构 pairs？**\n这是最关键的问题。如果 Wang et al. (2025) 的 model zoo 没有 multi-seed 配置，作者应明确说明并讨论获取此类数据的可行性。\n\n**[AGREE] R1-Q2: 全 10 benchmarks Bonferroni 下无显著结果**\n这是对论文的重要挑战。如果最严格的校正下整篇论文没有一个 convergence result 是显著的，那么 convergence 作为论文核心 narrative 之一的合理性就更成问题了。论文应该正面回应这一点，而非将其藏在 Appendix A。\n\n**[REBUT] R1-Q3: 是否分析过 raw log-likelihood 的 per-example 效应？**\n论文在 Appendix O 已经分析了 continuous confidence margin（基于 target-token probability），这本质上就是 log-likelihood 层面的分析。Cohen's d = 0.73–0.92 和 AUC 0.70–0.74 都基于 continuous values。R1 可能未充分阅读 Appendix O。不过，如果 R1 指的是直接用 log-likelihood difference（而非 binary correctness）替代 Jaccard 的分析，那确实是论文未做的——可以用 continuous overlap metrics（如 distribution overlap 或 rank correlation）补充。\n\n**[AGREE] R1-Q4: MMLU convergence 是否完全由 GDN 16-head confound 驱动？**\nTable 3 (Appendix D) 已经回答了这个问题：是的，MMLU 的 negative correlation 完全由 GDN 驱动（排除后从 ρ = −0.7 反转到 +0.6）。这一结果应在正文 §4.4 或 §4.1 中更明确地呈现，而非仅在附录。\n\n**[AGREE] R1-Q5: 340M 下 convergence 消失，应限定为 \"1.3B scale only\"**\nAppendix C 清楚显示 340M 的 LAMBADA convergence 是 non-monotonic 且最终 reduction 仅 36%（vs 1.3B 的 79%），ρ = −0.50, p = .45。论文的 convergence claim 确实应该在 Abstract 和 Introduction 中明确限定为 1.3B scale。目前 Abstract 说 \"Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction\" 但未提及 scale 限定。\n\n---\n\n### Missing References\n\n**[AGREE] Jiang et al. (2022) per-example model behavior differences**：相关但非关键遗漏。\n\n**[REBUT] Black et al. (2022) 关于 seed variance 的讨论**：论文 §2 Related Work 已经引用了 Black et al. (2022): \"Black et al. (2022) survey the model multiplicity landscape\"。R1 可能未注意到这一引用。\n\n补充我自己建议的 missing references：\n1. **Wortsman et al. (2022) Model Soups**——与 ensemble/MV 讨论直接相关\n2. **Guo et al. (2017) On Calibration**——与 confidence margin analysis 直接相关\n3. **Dodge et al. (2020) Fine-Tuning**——seed variation 在 fine-tuning 中的影响\n\n---\n\n### 总结\n\n与 R1 的 8 个主要意见中，我 **AGREE 6 个、REBUT 2 个**（W2 二值化问题已有充分回应、Q3 log-likelihood 分析已在附录中完成）。\n\nR1 和我（R2）在以下核心问题上高度一致：\n1. **Convergence claim 证据不足 + 叙事权重过高**（R1-N1 ≈ R2-N1）\n2. **单 seed 无法区分 architecture vs seed 效应**（R1-N2 ≈ R2-N2）\n3. **GDN confound 处理不充分**（R1-W1，R2 也在 N1 中提及）\n4. **因果语言越界**（R1-W4 ≈ R2-W4）\n\n主要分歧：\n- R1 给 Excitement 4/5（我给 2.5/5）——我认为 observational finding + 缺乏 actionable implications 限制了 excitement\n- R1 给 Soundness 3/5（我给 3.5/5）——我认为 per-example divergence 的 claims 有充分支撑，统计处理的透明度也应加分\n- R1 给 Reproducibility 3/5（我给 4/5）——公开 model zoo + 标准 lm-eval-harness + 详述统计方法，reproducibility 应该较高\n\n**我维持 Overall 3.0 (Findings) 的评分。**",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Spearman ρ 在 n=5 上统计推断力不足，正文过度依赖不显著趋势**\n\n同意，且我在自己的 N1 中提出了本质相同的问题。补充几点：\n\n1. 论文 §3.5 Power considerations 已诚实披露 \"only ρ = ±1.0 achieves p < .05\"，这是加分项，但这一限制的后果在 §4.1 的叙事中未被充分体现。§4.1 用了一整段讨论 LAMBADA convergence 的机制（\"attention provides direct token-level access...\"），给一个 Bonferroni-adjusted p = .100 的结果赋予了不匹配的 mechanistic certainty。\n2. R1 建议 \"Table 1 醒目区分显著/不显著\" 是好建议。目前 Table 1 仅用 bold 标记 ρ = −1.0，但 Bonferroni-adjusted p = .100 本身也不显著——bold 可能误导读者。\n3. 我进一步认为，即便区分了显著/不显著，**convergence 在叙事中的权重也应大幅压缩**（我的 N1），因为 10 个 benchmark 中仅 1 个显示趋势、且该趋势依赖 GDN 包含。\n\n**[AGREE] R1-N2: 单次训练 run 导致 architecture 与 seed 效应混淆**\n\n完全同意，这也是我的 N2。补充 R1 未明确提到的一点：\n\n论文用 within- vs cross-architecture Jaccard 的 3× gap（§4.3: ~0.33 vs ~0.10）作为 proxy evidence。但这个对比的含义是 **within-architecture across attention ratios** vs **cross-architecture at matched ratio**，即它衡量的是 \"同一架构在不同 attention dose 下的 per-example 变化\" vs \"不同架构在相同 attention dose 下的 per-example 变化\"。这**不等于** seed-vs-architecture 的对比。如果同一架构的不同 seed 产生的 Jaccard 也在 ~0.10 水平（McCoy et al. 2020 和 MultiBERTs 的结果暗示这是可能的），那么 3× gap 可能仅仅反映了 attention dose 变化是一个比 architecture 切换更 \"温和\" 的 perturbation——不能用来支撑 \"architecture is the primary driver\" 的论点。\n\nR1 建议 \"讨论 seed variance 典型量级\" 是最低限度的要求；multi-seed 验证是理想方案但可能超出 revision scope（model zoo 是外部资源）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: GDN h3-1 的 16-head confound 正文处理不充分**\n\n同意。§4.4 的处理确实过于简略。我补充两点 R1 未提到的：\n\n1. MMLU 从 ρ = −0.7 反转到 +0.6（非 R1 所述的 +0.7；见 Table 3, Appendix D）是一个严重的 instability signal——说明即使在 3 个架构的小样本下，单一架构的 confound 就能完全翻转相关方向。这强化了 convergence finding 的脆弱性。\n2. 更关键的是，GDN confound 不仅影响 convergence，也可能影响 per-example 分析：如果 GDN h3-1 的 attention capacity 因为 head 数不同而系统性偏低，那么 GDN 的 helped/hurt profile 可能部分由 capacity 差异驱动，而非纯粹的 architectural divergence。论文未分析排除 GDN 后的 per-example Jaccard 是否发生显著变化。\n\n**[REBUT] R1-W2: 二值化 per-example 分解丢弃 continuous confidence 信息**\n\n部分不同意。R1 的担忧有道理，但论文实际上已经提供了相当充分的回应：\n\n1. §4.2 明确承认了二值化的局限性（\"a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01\"）\n2. §4.2 报告了 helped/hurt 之间的 Cohen's d = 0.73–0.92，证明二值化确实捕捉到了 continuous confidence space 中的真实分离\n3. Appendix O (Confidence Margin) 提供了 continuous 分析：AUC 0.70–0.74、rescue/disruption thresholds 的非对称性\n4. Appendix P (BoolQ Supplementary) 和 cross-benchmark 分析进一步验证了 continuous patterns\n\n我认为论文已有的 continuous 分析是充分的。R1 建议的 \"continuous threshold sensitivity analysis\" 可以作为改进，但不是 should-fix 级别的问题。**建议降级为 minor。**\n\n**[AGREE] R1-W3: Bonferroni 校正的 confirmatory/exploratory 划分缺乏预注册**\n\n同意。Appendix A 明确承认 \"no external timestamp exists\"，但仍使用 \"confirmatory\" 一词。这在措辞上有误导性。\n\n补充：论文使用 6-benchmark Bonferroni 得到 adjusted p = .100，但如果用全 10-benchmark Bonferroni（Appendix A 自己计算了：adjusted p = .170），LAMBADA 更远离显著性。论文选择报告 6-benchmark 校正而非 10-benchmark 校正，在缺乏真正预注册的情况下，这个选择本身就是一种 researcher degree of freedom。\n\n建议：删除 \"confirmatory\" 标签，统一报告 10-benchmark Bonferroni（adjusted p = .170），并将 6-benchmark 版本作为 sensitivity check 放入附录。\n\n**[AGREE] R1-W4: 因果语言在 observational design 下时有越界**\n\n同意，这与我的 W4 完全一致。论文的 controlled design（matched training conditions）确实比纯 observational 研究有更强的因果推断基础，但 single run + 无 intervention 仍然不足以支撑因果表述。\n\n补充一个 R1 未提到的例子：§5 Conclusion 中 \"each backbone develops architecture-specific response patterns\" 的 \"develops\" 暗示了一个 generative/causal 过程，但论文只观察到了 cross-sectional association。\n\n---\n\n### 小问题\n\n**[AGREE] lm-eval-harness 版本号缺失**：§3.2 提到 \"v0.4.x\"——x 应该明确为具体版本号（如 v0.4.2），因为不同 minor 版本之间 prompt templates 可能有差异。\n\n**[REBUT] Greedy decoding 说明不完整**：§3.2 明确写了 \"default prompts and greedy decoding; accuracy serves as the primary metric for all benchmarks\"。这对于 lm-eval-harness 来说是标准且充分的说明。不清楚 R1 认为还需要什么额外信息。\n\n**[AGREE] Table 2 中 α 的 scale 不直观**：α = .14 表示 14% 的 examples 受影响，但读者可能需要一秒才能 parse。建议在 Table caption 或脚注中加一句 \"α represents the fraction of examples on which architectures disagree\"。\n\n**[AGREE] Appendix S subsample sensitivity 正文未提及**：Appendix S 分析了 σ estimation 在不同 subsample sizes 下的稳定性（95% CI），这是一个有价值的 robustness check。正文 §4.2 或 §3.5 应该至少引用一次。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: Model zoo 中是否有不同 seed 同架构 pairs？**\n这是最关键的问题。如果 Wang et al. (2025) 的 model zoo 没有 multi-seed 配置，作者应明确说明并讨论获取此类数据的可行性。\n\n**[AGREE] R1-Q2: 全 10 benchmarks Bonferroni 下无显著结果**\n这是对论文的重要挑战。如果最严格的校正下整篇论文没有一个 convergence result 是显著的，那么 convergence 作为论文核心 narrative 之一的合理性就更成问题了。论文应该正面回应这一点，而非将其藏在 Appendix A。\n\n**[REBUT] R1-Q3: 是否分析过 raw log-likelihood 的 per-example 效应？**\n论文在 Appendix O 已经分析了 continuous confidence margin（基于 target-token probability），这本质上就是 log-likelihood 层面的分析。Cohen's d = 0.73–0.92 和 AUC 0.70–0.74 都基于 continuous values。R1 可能未充分阅读 Appendix O。不过，如果 R1 指的是直接用 log-likelihood difference（而非 binary correctness）替代 Jaccard 的分析，那确实是论文未做的——可以用 continuous overlap metrics（如 distribution overlap 或 rank correlation）补充。\n\n**[AGREE] R1-Q4: MMLU convergence 是否完全由 GDN 16-head confound 驱动？**\nTable 3 (Appendix D) 已经回答了这个问题：是的，MMLU 的 negative correlation 完全由 GDN 驱动（排除后从 ρ = −0.7 反转到 +0.6）。这一结果应在正文 §4.4 或 §4.1 中更明确地呈现，而非仅在附录。\n\n**[AGREE] R1-Q5: 340M 下 convergence 消失，应限定为 \"1.3B scale only\"**\nAppendix C 清楚显示 340M 的 LAMBADA convergence 是 non-monotonic 且最终 reduction 仅 36%（vs 1.3B 的 79%），ρ = −0.50, p = .45。论文的 convergence claim 确实应该在 Abstract 和 Introduction 中明确限定为 1.3B scale。目前 Abstract 说 \"Aggregate convergence is task-specific: only LAMBADA provides exploratory evidence for monotonic variance reduction\" 但未提及 scale 限定。\n\n---\n\n### Missing References\n\n**[AGREE] Jiang et al. (2022) per-example model behavior differences**：相关但非关键遗漏。\n\n**[REBUT] Black et al. (2022) 关于 seed variance 的讨论**：论文 §2 Related Work 已经引用了 Black et al. (2022): \"Black et al. (2022) survey the model multiplicity landscape\"。R1 可能未注意到这一引用。\n\n补充我自己建议的 missing references：\n1. **Wortsman et al. (2022) Model Soups**——与 ensemble/MV 讨论直接相关\n2. **Guo et al. (2017) On Calibration**——与 confidence margin analysis 直接相关\n3. **Dodge et al. (2020) Fine-Tuning**——seed variation 在 fine-tuning 中的影响\n\n---\n\n### 总结\n\n与 R1 的 8 个主要意见中，我 **AGREE 6 个、REBUT 2 个**（W2 二值化问题已有充分回应、Q3 log-likelihood 分析已在附录中完成）。\n\nR1 和我（R2）在以下核心问题上高度一致：\n1. **Convergence claim 证据不足 + 叙事权重过高**（R1-N1 ≈ R2-N1）\n2. **单 seed 无法区分 architecture vs seed 效应**（R1-N2 ≈ R2-N2）\n3. **GDN confound 处理不充分**（R1-W1，R2 也在 N1 中提及）\n4. **因果语言越界**（R1-W4 ≈ R2-W4）\n\n主要分歧：\n- R1 给 Excitement 4/5（我给 2.5/5）——我认为 observational finding + 缺乏 actionable implications 限制了 excitement\n- R1 给 Soundness 3/5（我给 3.5/5）——我认为 per-example divergence 的 claims 有充分支撑，统计处理的透明度也应加分\n- R1 给 Reproducibility 3/5（我给 4/5）——公开 model zoo + 标准 lm-eval-harness + 详述统计方法，reproducibility 应该较高\n\n**我维持 Overall 3.0 (Findings) 的评分。**",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-22T08:52:04.993467+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Assistant

_source line 876 · 2026-05-22T08:52:09.698855+00:00_

交叉回应已提交。与 R1 在 8 个主要意见中 AGREE 6 个、REBUT 2 个（W2 二值化和 Q3 log-likelihood 已有附录回应）。两位 reviewer 在 convergence 证据不足、single seed 限制、GDN confound、因果语言四个核心问题上高度一致。我维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

70 recorded events


### User

_source line 877 · 2026-05-22T09:46:40.735060+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查新颖性、完整性和写作质量。

## 论文信息
- 标题: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
- 论文路径: projects/entrainment_gated_ft/docs/paper/main.tex
- PDF 路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/submitted.pdf
- 目标 venue: EMNLP 2026 (ARR Long Paper)
- 截止日期: 2026-05-25

## Venue 要求
- 正文 8 页限制（参考文献不限）
- ACL 模板（double-blind review）
- Limitations 和 Ethics 不计入页数
- ARR 统一审稿，Overall Assessment 评分: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit
- EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿，Long/Short 走同一审稿系统

## 你的审查侧重
1. **新颖性与贡献**：
   - 核心 research question 的新颖性如何？
   - 方法论是否有创新？还是已有指标（Jaccard, α, permutation test）的直接套用？
   - Decoupling finding 是否可从 ecological fallacy 角度预期？
   - 相比 MultiBERTs/McCoy (seed variation) 和 underspecification 文献，增量贡献是什么？

2. **Related Work 覆盖**：
   - 相关工作引用是否全面？
   - 与 predictive multiplicity (Marx 2020)、underspecification (D'Amour 2022)、Rashomon set (Fisher 2019) 文献的区分是否清晰？
   - 是否遗漏重要 ensemble diversity 文献？

3. **论述框架与写作**：
   - Abstract 信息密度和可读性
   - Introduction 中 contributions 的表述是否清晰、准确？
   - 因果语言 vs 关联语言——是否存在残余因果表述？
   - Conclusion 的 practical implications 是否有过度泛化？
   - 整体叙事结构和逻辑流畅度

4. **格式合规**：
   - 正文是否在 8 页内？
   - Limitations 是否简洁（~3 点）？
   - 匿名规则是否遵守？
   - 引用格式是否正确？

请严格按照 ARR 审稿标准评审，给出：Strengths、Weaknesses（逐条标注 Critical/Major/Minor/Warning）、Questions、Missing References、Soundness (1-5)、Excitement (1-5)、Reproducibility (1-5)、Overall Assessment (1-5, 按 EMNLP 2026 标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-22T09:46:53.819242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-22T09:46:54.020668+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-22T09:46:57.242234+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-22T09:46:57.343517+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-22T09:46:59.868942+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-22T09:46:59.919559+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-22T09:47:05.446825+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-22T09:47:05.547704+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-22T09:47:09.964007+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 887 · 2026-05-22T09:47:11.322819+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-22T09:47:11.524026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-22T09:47:16.352804+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Excitement is a separate score which is orthogonal to the assessment of the soundness of the paper. This allows reviewers to separately express subjective preferences from technical soundness.

### Area Chair Meta-Review Scoring
The meta-review score options are: 5 = Consider for Award; ... 2 = Resubmit next cycle; 1.5 = Resubmit after next cycle; 1 = Do not resubmit (for papers that need full redoing or are not relevant to the *ACL community).

Like with reviews, the score should be backed up by the
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6388
}
```

</details>

---


### Tool result

_source line 890 · 2026-05-22T09:47:17.961709+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 448.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6638
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-22T09:47:17.962438+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	When attention layers are added to linear recurrent architectures, they help and hurt almost entirely different examples across backbones: pairwise overlap among three controlled hybrid designs is at most 10\%. Using the model zoo of \citet{wang2025hybrid} (30 configurations spanning three architectures, five attention ratios, and two scales), we decompose per-example effects and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) rather than attention dose. Only LAMBADA shows exploratory evidence for aggregate convergence (Bonferroni-adjusted $p = .100$), yet per-example overlap saturates at the first attention level across all four benchmarks. A majority vote fails to outperform the best individual model despite 15--45\% disagreement, while oracle accuracy reveals 7--14\,pp of untapped complementarity, suggesting that architectures interchangeable by aggregate metrics carry hidden consequences for per-example reliability.
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	
40	Our analysis has several limitations.
41	
42	\paragraph{Coverage and generalization.} We examine three architectures from one model zoo on four main benchmarks (two supplementary). The controlled design isolates architectural effects but limits gene
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6438
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-22T09:47:22.289719+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-22T09:47:22.440507+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-22T09:47:22.892020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-22T09:47:23.696281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-22T09:47:23.847159+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 897 · 2026-05-22T09:47:24.349093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 898 · 2026-05-22T09:47:24.752466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 899 · 2026-05-22T09:47:24.752944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 900 · 2026-05-22T09:47:25.206709+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 901 · 2026-05-22T09:47:25.207162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 902 · 2026-05-22T09:47:26.113454+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-22T09:47:26.214908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 904 · 2026-05-22T09:47:26.215223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 905 · 2026-05-22T09:47:26.566812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 906 · 2026-05-22T09:47:27.076548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 907 · 2026-05-22T09:47:27.128491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 908 · 2026-05-22T09:47:28.134806+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1567
}
```

</details>

---


### Tool result

_source line 909 · 2026-05-22T09:47:28.640265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---


### Tool call

_source line 910 · 2026-05-22T09:47:36.105770+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 911 · 2026-05-22T09:47:39.028253+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 482.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 406.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 428.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.9}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2922
}
```

</details>

---


### Tool call

_source line 912 · 2026-05-22T09:47:39.134094+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria: all scoring dimensions (soundness, excitement, overall assessment, reproducibility, etc.), their scales (1-5), and the description of each score level. Also extract any guidelines about what constitutes a good review, how to assess novelty, soundness, and significance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria: all scoring dimensions (soundness, excitement, overall assessment, reproducibility, etc.), their scales (1-5), and the description of each score level. Also extract any guidelines about what constitutes a good review, how to assess novelty, soundness, and significance."
  }
}
```

</details>

---


### Tool call

_source line 913 · 2026-05-22T09:47:39.839530+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 914 · 2026-05-22T09:47:39.990516+00:00_

1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: on LAMBADA, cross-architecture standard deviation drops 79\% as attention increases (Bonferroni-adjusted $p = .100$; the heuristic BCa 95\% CI excludes zero), but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Our results show that architectures scoring identically in aggregate may nonetheless differ on 15--45\% of individual predictions, meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{mar
…[truncated 4575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 915 · 2026-05-22T09:47:40.141397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 916 · 2026-05-22T09:47:40.897887+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} achieves near-Transformer quality with gated convolutions and SSMs, establishing an early design point in the hybrid space. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification: equivalent a
…[truncated 2164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 917 · 2026-05-22T09:47:41.049214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 918 · 2026-05-22T09:47:41.452950+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\subsection{Task Taxonomy}\label{ssec:task_taxonomy}
10	
11	We evaluate on 10 benchmarks grouped into four categories defined by the primary cognitive demand of each task. This taxonomy was fixed prior to analysis following established distinctions in the hybrid architecture literature \citep{arora2024zoology} (see Appendix~A for the confirmatory/exploratory split), not derived post hoc from observed results. The categories test 
…[truncated 7088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 919 · 2026-05-22T09:47:41.604007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 920 · 2026-05-22T09:47:44.464135+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\subsection{Task-Specific Convergence}\label{ssec:task_convergence}
6	
7	Table~\ref{tab:convergence} reports cross-architecture $\sigma$ at each attention ratio for all benchmarks at 1.3B scale. LAMBADA is the only benchmark exhibiting monotonic convergence: $\rho = -1.0$ ($p = .017$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic given $n = 3$, \S\ref{ssec:statistical_methods}; $\sigma$ drops 79\%; Bonferroni-adjusted $p = .100$, under all-10-benchmark correction adj-$p = .170$, Appendix~A; excluding GDN: $\rho = -0.7$, $p = .233$, \S\ref{ssec:robustness}). No other benchmark shows significant convergence (all $|\rho| \leq 0.7$, $p \geq .233$; Figure~\ref{fig:task_specificity}; Appendix~\ref{app:convergence_detail}). This convergence is observed at 1.3B scale but absent at 340M (Appendix~\ref{app:scale_convergence}), and is best interpreted as exploratory given limited statistical power ($n = 5$ ordinal levels).
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig2_task_specificity.pdf}
12	\caption{Spearman $\rho$ between attention ratio and cross-architecture $\sigma$ for each benchmark at 1.3B scale. LAMBADA ($\rho = -1.0$; BCa 95\% CI $[-1.0,\,-0.7]$, heuristic) is the only benchmark with a negative correlation whose confidence interval excludes zero. Benchmarks are grouped by task category.}
13	\label{fig:task_specificity}
14	\end{figure}
15	
16	\begin{table*}[t]
17	\centering
18	\caption{Cross-architecture convergence across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture $\sigma$ across five configurations. $p$: ex
…[truncated 12709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2860
}
```

</details>

---


### Tool call

_source line 921 · 2026-05-22T09:47:44.665165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 922 · 2026-05-22T09:47:44.665519+00:00_

1	\section{Conclusion}
2	
3	We present the first systematic per-example analysis of attention effects in hybrid recurrent models. Per-example multiplicity spans a task-dependent variation ($\alpha = 0.14$--$0.30$) across four benchmarks, with Jaccard uniformly low ($\leq 0.10$) regardless of aggregate convergence. On LAMBADA at 1.3B, aggregate variance decreases with attention while per-example overlap saturates, consistent with architecture-specific pathways rather than uniform rescue (dependent on GDN inclusion; does not replicate on other benchmarks). Aggregate benchmark equivalence thus masks per-example divergence: each backbone exhibits architecture-specific response patterns invisible to standard evaluation. Within each architecture, pure-model confidence partially predicts which examples will be affected (AUC 0.70--0.74), though disruption thresholds vary 47\% across architectures (\S\ref{ssec:per_example}).
4	
5	For practitioners, these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores: the ${\sim}90\%$ non-overlap means architectures interchangeable by aggregate metrics affect nearly disjoint examples. A majority vote across three architectures fails to consistently outperform the best individual model (LAMBADA: $-0.2$\,pp; ARC-Easy: $-1.1$\,pp; gains on other benchmarks $< 0.2$\,pp) despite 15--45\% disagreement, because roughly half of disagreement examples have only one correct architecture (Appendix~\ref{app:complementarity}). Oracle accuracy reveals $+7$--$14$\,pp of untapped complementarity, but accessing it requires selection methods beyond naive ensembling---whether through weight-space approaches \citep{wortsman2022model} or confidence-informed routing.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 923 · 2026-05-22T09:47:45.017269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 924 · 2026-05-22T09:47:45.319446+00:00_

1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The Bonferroni-adjusted significance threshold is $\alpha / 6 = 0.0083$. \textbf{Sensitivity:} correcting across all 10 benchmarks yields adjusted $p = 0.017 \times 10 = 0.170$, further from significance; the main text reports the confirmatory-set correction ($\times 6 = 0.100$).
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 6-benchmark Bonferroni correction, this yields an adjusted $p = 0.050$, exactly at the conventional threshold. We report two-sided test
…[truncated 49145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 925 · 2026-05-22T09:47:46.524827+00:00_

# ARR Review Form Criteria and Guidelines

## Scoring Dimensions

Based on the guidelines provided, ARR reviewers use **three main scores** (as of February 2025):

1. **Soundness** - Assesses technical rigor and validity
2. **Excitement** - Reflects personal interest and engagement
3. **Overall Assessment** - Composite recommendation for acceptance

The document mentions a **reproducibility score** but does not specify its exact scale in the provided content.

## Key Guidance on Assessment

**Soundness Requirements:**
"The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation."

**Excitement vs. Soundness:**
These are orthogonal dimensions. A paper can be technically sound but personally unexciting, or vice versa. The overall recommendation should consider "soundness, excitement, and also other factors like novelty and impact."

**What Constitutes Good Reviews:**

- Be specific with concrete examples rather than vague criticisms
- Maintain professional, neutral tone
- Adjust expectations based on paper type before evaluating results
- Read papers twice (skim for context, then in-depth analysis)
- Justify all scoring decisions with evidence from the review text

**Key Assessment Principles:**

The guidelines emphasize avoiding common reviewer biases (H1-H17) and checking for common NLP paper problems (M1-G5) across methodology, artifact sourcing, results, and general issues.

*Note: The document does not provide explicit numerical scales (1-5) for individual dimensions.*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7390
}
```

</details>

---


### Tool call

_source line 926 · 2026-05-22T09:47:54.204462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 927 · 2026-05-22T09:47:54.757492+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 928 · 2026-05-22T09:47:55.059932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 929 · 2026-05-22T09:47:55.060370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 930 · 2026-05-22T09:47:56.014585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1257
}
```

</details>

---


### Tool result

_source line 931 · 2026-05-22T09:47:56.015920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 932 · 2026-05-22T09:47:56.016292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 933 · 2026-05-22T09:47:56.268820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 934 · 2026-05-22T09:47:56.371826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 935 · 2026-05-22T09:47:56.573931+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 557
}
```

</details>

---


### Tool call

_source line 936 · 2026-05-22T09:48:02.909918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 description each level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 soundness excitement scoring scale 1-5 description each level"
  }
}
```

</details>

---


### Tool call

_source line 937 · 2026-05-22T09:48:03.512613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 938 · 2026-05-22T09:48:03.613566+00:00_

1	% References for entrainment_gated_ft paper
2	% Generated from literature_map.yaml (all verified=true entries)
3	
4	% ============================================================
5	% Per-Example Analysis / Dataset Cartography
6	
7	@article{fort2019deep,
8	  title={Deep Ensembles: A Loss Landscape Perspective},
9	  author={Fort, Stanislav and Hu, Huiyi and Lakshminarayanan, Balaji},
10	  journal={arXiv preprint arXiv:1912.02757},
11	  year={2019}
12	}
13	
14	@inproceedings{niven2019probing,
15	  title={Probing Neural Network Comprehension of Natural Language Arguments},
16	  author={Niven, Timothy and Kao, Hung-Yu},
17	  booktitle={Proceedings of ACL},
18	  year={2019}
19	}
20	
21	@inproceedings{swayamdipta2020dataset,
22	  title={Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics},
23	  author={Swayamdipta, Swabha and Chandrasekaran, Roy and Wieting, John and Hajishirzi, Hannaneh and Smith, Noah A.},
24	  booktitle={Proceedings of EMNLP},
25	  year={2020}
26	}
27	
28	% ============================================================
29	% Model Multiplicity Surveys and Fairness
30	
31	@inproceedings{black2022model,
32	  title={Model Multiplicity: Opportunities, Concerns, and Solutions},
33	  author={Black, Emily and Raghavan, Manish and Barocas, Solon},
34	  booktitle={Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (FAccT)},
35	  year={2022}
36	}
37	
38	@inproceedings{cooper2024arbitrariness,
39	  title={Arbitrariness and Social Prediction: The Confounding Role of Variance in Fair Classification},
40	  author={Cooper, A. Feder and Abrams, Katherine and Barocas, Solon},
41	  booktitle={Proceedings of AAAI},
42	  year={2024}
43	}
44	
45	% ============================================================
46	% Hybrid Architectures
47	
48	@inproceedings{fu2023hungry,
49	  title={Hungry Hungry Hippos: Towards Language Modeling with State Space Models},
50	  author={Fu, Daniel Y. and Dao, Tri and Saab, Khaled K. and Thomas,
…[truncated 12805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 939 · 2026-05-22T09:48:11.595248+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement scoring scale 1-5 description each level"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Can LLM feedback enhance review quality? A randomized study of 20K   reviews at ICLR 2025","url":"https://arxiv.org/pdf/2504.09737"}]

I found information about the 2025 ARR review form. Based on the search results, here's what I found about the scoring scales:

## Excitement Scoring Scale (1-5)

5 = Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference.

4 = Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference.

The search results also mention 1 = Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community (e.g. it is in no way related to computational processing of language).

## Soundness 
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8685
}
```

</details>

---


### Tool call

_source line 940 · 2026-05-22T09:48:18.393056+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5), and the exact description of each score level. I need: 1) Soundness scale with all levels, 2) Excitement scale with all levels, 3) Overall Assessment scale with all levels, 4) Any other dimensions like reproducibility, confidence, etc. Give me the exact text for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their exact scales (1-5), and the exact description of each score level. I need: 1) Soundness scale with all levels, 2) Excitement scale with all levels, 3) Overall Assessment scale with all levels, 4) Any other dimensions like reproducibility, confidence, etc. Give me the exact text for each score level."
  }
}
```

</details>

---


### Tool result

_source line 941 · 2026-05-22T09:48:24.514844+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. Soundness (1-5 scale)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement (1-5 scale)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others"

## 4. Overall Assessment (1-5 scale)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings of ACL acceptance
- **2**: Resubmit next cycle with substantial revisions
- **1**: Do not resubmit

## 5. Reproducibility (1-5 scale)
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be able to reproduce the results"

## 6. Datasets & Software (1-5 scale)
- **5**: Enabling—affects research direction
- **4**: Useful—recommended for ongoing work
- **3**: Potentially 
…[truncated 121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6121
}
```

</details>

---


### Tool call

_source line 942 · 2026-05-22T09:52:10.701738+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n## 总体评分\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 一篇方法论扎实但新颖性有限的实证分析——将已有概念（predictive multiplicity）应用于新场景（hybrid recurrent architectures），核心发现（aggregate convergence ≠ per-example convergence）可从 ecological fallacy 角度预期，且唯一统计显著的收敛结果（LAMBADA）在多重比较校正后未达传统显著性水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | multiplicity 主张有充分支撑（α = 0.14–0.30, J ≤ 0.10 均 p < .01），但 convergence 主张脆弱（仅 LAMBADA, 依赖 GDN, Bonferroni-adjusted p = .100）；single training runs 无法分离 architecture vs. seed effects |\n| Excitement | 2/5 | 核心发现（aggregate ≈ but per-example ≠）是已知现象的新场景验证，无方法论创新，实际可操作建议有限 |\n| Reproducibility | 4/5 | 使用公开 model zoo、lm-evaluation-harness v0.4.x、固定 seed 42、详细统计方法；承诺发布代码 |\n| Overall Assessment | 3.0 | Findings 水平：分析彻底、统计透明，但新颖性和影响力不足以支撑主会议接收 |\n| Confidence | 4/5 | 仔细阅读全文含附录，对 predictive multiplicity 和 hybrid architecture 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Decoupling finding 缺乏对 Ecological Fallacy 的讨论\n- 具体位置：§4.3 Decoupling（全节）及 §1 Introduction 第1段\n- 问题：论文的核心发现——aggregate convergence 与 per-example divergence 的脱耦——是 ecological fallacy (Robinson, 1950) 的一个具体实例：aggregate-level 的相关/趋同不蕴含 individual-level 的趋同。这一原理在统计学和社会科学中已有 70+ 年历史。论文未引用、未讨论 ecological fallacy，也未论证为什么在这个已知原理下，实证验证仍然有价值。\n- 为什么影响接收：缺少这一讨论使得论文的核心贡献看起来是在\"发现\"一个已知现象，而非在已知框架下提供有价值的新证据。Reviewer 和 AC 会质疑 novelty。\n- 建议修改方向：在 §2 Related Work 或 §4.3 中明确讨论 ecological fallacy，承认 decoupling 在概念上可预期，然后论证为什么在 hybrid recurrent 场景下的 *quantitative characterization*（如 Jaccard 的具体数值、α 的 task-dependent variation）仍提供了超越概念预期的实证价值。\n\n**N2** [critical] 唯一的 convergence 结果统计上不足，但论文叙事给予其过高权重\n- 具体位置：§4.1 Table 1; §4.3; Abstract; §1 Introduction\n- 问题：LAMBADA 的 convergence 结果 (ρ = −1.0) 在 6-benchmark Bonferroni 校正后 p = .100，在 10-benchmark 校正后 p = .170，均未达 conventional significance (α = 0.05)。更严重的是，该结果依赖 GDN 的包含（排除 GDN 后 ρ = −0.7, p = .233，§4.4），而 GDN h3-1 的 16-head 配置与其他模型的 32-head 不一致（Appendix E），构成 confound。然而，论文在 Abstract 第2句、Introduction 第1段、§4.3 全节都围绕这一结果展开叙事，给读者留下了 convergence 是 established finding 的印象。\n- 为什么影响接收：一个 p = .100 的结果被置于论文叙事的核心位置，与其统计强度不匹配。即使论文在各处添加了 \"exploratory\" 标注，叙事结构仍暗示 convergence 是主要发现之一。\n- 建议修改方向：(1) 将 convergence 明确降格为 exploratory/secondary finding，不在 Abstract 和 Introduction 中作为主要叙事支柱；(2) 重新组织论文结构，以 per-example multiplicity（统计上更 robust 的发现）为核心，convergence 作为补充上下文；(3) 在 GDN confound 讨论中更明确地承认 convergence 可能是 artifactual。\n\n**N3** [critical] 新颖性有限——方法论层面无创新，核心发现是已知现象的新场景验证\n- 具体位置：全文\n- 问题：论文使用的所有分析工具（Jaccard similarity, ambiguity α, Spearman ρ, permutation test, bootstrap CI, confidence margin）均为已有方法的直接套用，无任何方法论创新。核心发现可分解为：(1) 不同架构在 per-example 层面行为不同（已由 McCoy et al. 2020 / D'Amour et al. 2022 在 seed variation 中建立），(2) aggregate ≠ per-example（ecological fallacy），(3) multiplicity magnitude 与 task type 相关（与 Gorbett & Jana 2026 的 cross-model disagreement as correctness signal 方向一致）。相对于 MultiBERTs (seed variation within architecture) 和 underspecification literature，本文的 incremental contribution 是将已知现象从 seed variation 扩展到 cross-architecture variation in hybrid recurrents。\n- 为什么影响接收：对于 Conference 级别论文，通常期望至少在 (a) 新方法, (b) 意外发现, 或 (c) 显著实际影响 中有一项。本文在三方面均有限。\n- 建议修改方向：(1) 更清晰地论述 cross-architecture variation 比 seed variation 在什么维度上提供了不可从已有文献推断的新信息；(2) 考虑引入新的分析工具（如 architecture-conditional prediction model, ensemble selection method），使论文超越纯粹的现象描述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 残余因果语言与 observational study 设计不匹配\n- 具体位置：Abstract 第1句 \"they help and hurt almost entirely different examples\"; §1 第1句 \"adding attention...yields helped and hurt sets\"; §4.2 \"attention consistently rescues near-miss errors\"\n- 问题：论文基于现有 model zoo，每个配置仅一次训练，无法控制随机种子。在 Limitations 中承认 \"we cannot fully disentangle architectural from seed-specific effects\"，但 Abstract 和 Introduction 中使用 \"help,\" \"hurt,\" \"yields,\" \"rescues\" 等因果语言，暗示 attention 是 per-example 效应的原因。Contributions 部分 (§1) 使用了较准确的 \"associated with\"，但高可见度位置的因果表述可能误导读者。\n- 建议：统一使用关联语言（\"is associated with,\" \"co-occurs with\"），或在首次使用因果表述时明确注明这是在 matched training conditions 下的 controlled comparison, 并引用 limitations 中的 caveat。\n\n**W2** [warning] Abstract 信息密度过高，可读性受损\n- 具体位置：Abstract（第24-26行，main.tex）\n- 问题：Abstract 在 ~150 词内包含 α 值范围、Bonferroni-adjusted p 值、Jaccard 阈值、百分比差异、oracle accuracy 数值，导致首次阅读时难以提取核心信息。对比同领域论文（如 McCoy et al. 2020 的 abstract），本文 abstract 的数值密度显著更高。\n- 建议：保留 1-2 个关键数字（如 α range 和 Jaccard），其余移至 Introduction 或 Results。Abstract 应优先传达 *what* and *why it matters*，而非 *exact numbers*。\n\n**W3** [warning] Practical implications 泛化过度\n- 具体位置：§5 Conclusion 第2段 \"these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores\"\n- 问题：建议 \"whenever hybrid designs achieve comparable aggregate scores\" 都做 per-example audit，但实证基础是 3 个架构、2 个 scale、4 个 benchmark、pre-training only、no fine-tuning。从这一有限数据集泛化到所有 hybrid designs 的所有场景（包括 fine-tuned、deployment 场景）是过度泛化。\n- 建议：将 practical implication 限定到论文实际覆盖的场景（pre-trained hybrid recurrent models at 340M–1.3B scale），并明确 fine-tuning 后是否 persist 是 open question（Limitations 中已提及但 Conclusion 中未体现）。\n\n**W4** [warning] Introduction 与 Abstract 内容高度重复\n- 具体位置：§1 Introduction 前3段 vs. Abstract\n- 问题：Introduction 第1段几乎逐句重复 Abstract 的内容（同样的 10% overlap, 79% σ reduction, Bonferroni-adjusted p = .100, BCa 95% CI 等数字）。这浪费了宝贵的页面空间（在 8 页限制下），且降低阅读体验。\n- 建议：Introduction 应 *expand on* abstract 而非 *repeat* it——提供更多动机、背景和论文结构说明，将具体数字留给 Results。\n\n**W5** [warning] Ensemble diversity 文献连接不充分\n- 具体位置：§2 Related Work\n- 问题：论文本质上在测量 cross-architecture diversity，但仅引用 Kuncheva & Whitaker (2003) 一篇 ensemble diversity 文献。该领域有丰富的 diversity measures（Q-statistic, disagreement measure, double-fault measure, κ-statistic）和理论（bias-variance-covariance decomposition for ensembles），与本文的 Jaccard-based analysis 直接相关。Fort et al. (2019) 被引用但未充分讨论其 loss landscape perspective 如何解释 cross-architecture divergence。\n- 建议：添加 2-3 句讨论 ensemble diversity 理论如何预期/解释本文的 per-example divergence 发现，以及 Jaccard 与其他 diversity measures 的关系。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** §3.4 \"All statistical tests are two-tailed unless otherwise noted\" 后紧接 Appendix A 讨论 one-sided test (p = 0.0083)。建议在正文中简要提及 one-sided 结果的存在，避免 reviewers 质疑 cherry-picking。\n- **M2** references.bib 中 `dodge2020finetuning` 的 `booktitle` 字段设为 arXiv 链接而非 venue，应修正为 `journal = {arXiv preprint arXiv:2002.06305}` 或引用已发表版本。\n- **M3** Table 1 脚注提到 \"Bonferroni-adjusted p = 6 × 2/120 = 0.100 (exact); 0.102 arises from rounding\" — 两个数字 (0.100 vs 0.102) 同时出现造成混淆。选择一个并解释即可。\n- **M4** §4.2 \"normalized ES 0.065 helped, 0.062 hurt\" 中 ES 缩写首次出现未定义（effect size），虽从上下文可推断，但建议在首次使用时展开。\n- **M5** Conclusion 中 \"confidence-informed routing\" 被提出作为利用 complementarity 的方向，但全文未提供任何 routing 的初步实验或 feasibility analysis，使得这一建议悬浮。\n\n---\n\n## 主要优势\n\n1. **统计方法论的透明度和严谨性出色**：论文在每一步都提供了 exact p-values、power analysis、bootstrap CIs，并坦诚 n = 3 architectures 和 n = 5 attention ratios 的统计局限性。GDN confound 的 sensitivity analysis (§4.4, Appendix D-E) 是特别好的做法。\n2. **附录极其详尽**（12 页，17+ 张表）：covering cross-scale analysis, supplementary benchmarks (BoolQ, WinoGrande), within-architecture stability, normalized Jaccard effect sizes, confidence margin analysis, complementarity decomposition——每个 claim 都有 backup evidence。\n3. **实验设计利用了 controlled model zoo**：固定 training data / hyperparameters / tokenizer 仅变化 architecture 和 attention ratio，是研究 architectural effects 的理想设置（在 single-run limitation 下）。\n4. **Per-example decomposition 和 confidence margin analysis** 提供了超越简单 aggregate comparison 的分析粒度，confidence margin 作为 within-architecture predictor (AUC 0.70–0.74) 是一个有用的发现。\n5. **格式完全合规**：8 页正文、ACL 模板、double-blind、Limitations 简洁覆盖 3 点、Ethics Statement 存在。\n\n---\n\n## Questions to Authors\n\n1. 你们如何将 decoupling finding 与 ecological fallacy (Robinson, 1950) 区分开？Aggregate convergence 不蕴含 per-example convergence 这一事实是否可以在不做任何实验的情况下从统计原理预期？\n2. 如果 GDN 的 16-head configuration 是 convergence 结果的主要驱动因素（而非 architecture 本身），那么 §4.1 的 convergence 主张是否应被完全撤回而非仅标注为 \"exploratory\"？\n3. 论文建议做 \"per-example audits\"，但具体如何操作？在没有 oracle 标签的 deployment 场景下，practitioners 能做什么？\n4. Single training runs 使 architecture vs. seed effects 无法区分。α = 0.14–0.30 中有多少可能来自 seed noise 而非 architectural difference？3× within- vs. cross-architecture Jaccard gap 能否定量 bound 这一比例？\n\n---\n\n## Missing References\n\n- Robinson, W.S. (1950). \"Ecological Correlations and the Behavior of Individuals.\" — ecological fallacy 的经典参考，直接关联 decoupling finding\n- Brown, G., Wyatt, J., Harris, R., & Yao, X. (2005). \"Diversity Creation Methods: A Survey and Categorisation.\" — ensemble diversity measures 综述，与 cross-architecture diversity analysis 相关\n- Jiang, Z., Araki, J., Ding, H., & Neubig, G. (2021). \"How Can We Know When Language Models Know? Measuring and Bridging the Calibration Gap.\" — 与 confidence margin analysis (§4.2, Appendix H) 相关\n",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n## 总体评分\n**Overall Assessment**: 3.0 (Findings)\n**一句话总结**: 一篇方法论扎实但新颖性有限的实证分析——将已有概念（predictive multiplicity）应用于新场景（hybrid recurrent architectures），核心发现（aggregate convergence ≠ per-example convergence）可从 ecological fallacy 角度预期，且唯一统计显著的收敛结果（LAMBADA）在多重比较校正后未达传统显著性水平。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | multiplicity 主张有充分支撑（α = 0.14–0.30, J ≤ 0.10 均 p < .01），但 convergence 主张脆弱（仅 LAMBADA, 依赖 GDN, Bonferroni-adjusted p = .100）；single training runs 无法分离 architecture vs. seed effects |\n| Excitement | 2/5 | 核心发现（aggregate ≈ but per-example ≠）是已知现象的新场景验证，无方法论创新，实际可操作建议有限 |\n| Reproducibility | 4/5 | 使用公开 model zoo、lm-evaluation-harness v0.4.x、固定 seed 42、详细统计方法；承诺发布代码 |\n| Overall Assessment | 3.0 | Findings 水平：分析彻底、统计透明，但新颖性和影响力不足以支撑主会议接收 |\n| Confidence | 4/5 | 仔细阅读全文含附录，对 predictive multiplicity 和 hybrid architecture 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Decoupling finding 缺乏对 Ecological Fallacy 的讨论\n- 具体位置：§4.3 Decoupling（全节）及 §1 Introduction 第1段\n- 问题：论文的核心发现——aggregate convergence 与 per-example divergence 的脱耦——是 ecological fallacy (Robinson, 1950) 的一个具体实例：aggregate-level 的相关/趋同不蕴含 individual-level 的趋同。这一原理在统计学和社会科学中已有 70+ 年历史。论文未引用、未讨论 ecological fallacy，也未论证为什么在这个已知原理下，实证验证仍然有价值。\n- 为什么影响接收：缺少这一讨论使得论文的核心贡献看起来是在\"发现\"一个已知现象，而非在已知框架下提供有价值的新证据。Reviewer 和 AC 会质疑 novelty。\n- 建议修改方向：在 §2 Related Work 或 §4.3 中明确讨论 ecological fallacy，承认 decoupling 在概念上可预期，然后论证为什么在 hybrid recurrent 场景下的 *quantitative characterization*（如 Jaccard 的具体数值、α 的 task-dependent variation）仍提供了超越概念预期的实证价值。\n\n**N2** [critical] 唯一的 convergence 结果统计上不足，但论文叙事给予其过高权重\n- 具体位置：§4.1 Table 1; §4.3; Abstract; §1 Introduction\n- 问题：LAMBADA 的 convergence 结果 (ρ = −1.0) 在 6-benchmark Bonferroni 校正后 p = .100，在 10-benchmark 校正后 p = .170，均未达 conventional significance (α = 0.05)。更严重的是，该结果依赖 GDN 的包含（排除 GDN 后 ρ = −0.7, p = .233，§4.4），而 GDN h3-1 的 16-head 配置与其他模型的 32-head 不一致（Appendix E），构成 confound。然而，论文在 Abstract 第2句、Introduction 第1段、§4.3 全节都围绕这一结果展开叙事，给读者留下了 convergence 是 established finding 的印象。\n- 为什么影响接收：一个 p = .100 的结果被置于论文叙事的核心位置，与其统计强度不匹配。即使论文在各处添加了 \"exploratory\" 标注，叙事结构仍暗示 convergence 是主要发现之一。\n- 建议修改方向：(1) 将 convergence 明确降格为 exploratory/secondary finding，不在 Abstract 和 Introduction 中作为主要叙事支柱；(2) 重新组织论文结构，以 per-example multiplicity（统计上更 robust 的发现）为核心，convergence 作为补充上下文；(3) 在 GDN confound 讨论中更明确地承认 convergence 可能是 artifactual。\n\n**N3** [critical] 新颖性有限——方法论层面无创新，核心发现是已知现象的新场景验证\n- 具体位置：全文\n- 问题：论文使用的所有分析工具（Jaccard similarity, ambiguity α, Spearman ρ, permutation test, bootstrap CI, confidence margin）均为已有方法的直接套用，无任何方法论创新。核心发现可分解为：(1) 不同架构在 per-example 层面行为不同（已由 McCoy et al. 2020 / D'Amour et al. 2022 在 seed variation 中建立），(2) aggregate ≠ per-example（ecological fallacy），(3) multiplicity magnitude 与 task type 相关（与 Gorbett & Jana 2026 的 cross-model disagreement as correctness signal 方向一致）。相对于 MultiBERTs (seed variation within architecture) 和 underspecification literature，本文的 incremental contribution 是将已知现象从 seed variation 扩展到 cross-architecture variation in hybrid recurrents。\n- 为什么影响接收：对于 Conference 级别论文，通常期望至少在 (a) 新方法, (b) 意外发现, 或 (c) 显著实际影响 中有一项。本文在三方面均有限。\n- 建议修改方向：(1) 更清晰地论述 cross-architecture variation 比 seed variation 在什么维度上提供了不可从已有文献推断的新信息；(2) 考虑引入新的分析工具（如 architecture-conditional prediction model, ensemble selection method），使论文超越纯粹的现象描述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 残余因果语言与 observational study 设计不匹配\n- 具体位置：Abstract 第1句 \"they help and hurt almost entirely different examples\"; §1 第1句 \"adding attention...yields helped and hurt sets\"; §4.2 \"attention consistently rescues near-miss errors\"\n- 问题：论文基于现有 model zoo，每个配置仅一次训练，无法控制随机种子。在 Limitations 中承认 \"we cannot fully disentangle architectural from seed-specific effects\"，但 Abstract 和 Introduction 中使用 \"help,\" \"hurt,\" \"yields,\" \"rescues\" 等因果语言，暗示 attention 是 per-example 效应的原因。Contributions 部分 (§1) 使用了较准确的 \"associated with\"，但高可见度位置的因果表述可能误导读者。\n- 建议：统一使用关联语言（\"is associated with,\" \"co-occurs with\"），或在首次使用因果表述时明确注明这是在 matched training conditions 下的 controlled comparison, 并引用 limitations 中的 caveat。\n\n**W2** [warning] Abstract 信息密度过高，可读性受损\n- 具体位置：Abstract（第24-26行，main.tex）\n- 问题：Abstract 在 ~150 词内包含 α 值范围、Bonferroni-adjusted p 值、Jaccard 阈值、百分比差异、oracle accuracy 数值，导致首次阅读时难以提取核心信息。对比同领域论文（如 McCoy et al. 2020 的 abstract），本文 abstract 的数值密度显著更高。\n- 建议：保留 1-2 个关键数字（如 α range 和 Jaccard），其余移至 Introduction 或 Results。Abstract 应优先传达 *what* and *why it matters*，而非 *exact numbers*。\n\n**W3** [warning] Practical implications 泛化过度\n- 具体位置：§5 Conclusion 第2段 \"these results motivate per-example audits whenever hybrid designs achieve comparable aggregate scores\"\n- 问题：建议 \"whenever hybrid designs achieve comparable aggregate scores\" 都做 per-example audit，但实证基础是 3 个架构、2 个 scale、4 个 benchmark、pre-training only、no fine-tuning。从这一有限数据集泛化到所有 hybrid designs 的所有场景（包括 fine-tuned、deployment 场景）是过度泛化。\n- 建议：将 practical implication 限定到论文实际覆盖的场景（pre-trained hybrid recurrent models at 340M–1.3B scale），并明确 fine-tuning 后是否 persist 是 open question（Limitations 中已提及但 Conclusion 中未体现）。\n\n**W4** [warning] Introduction 与 Abstract 内容高度重复\n- 具体位置：§1 Introduction 前3段 vs. Abstract\n- 问题：Introduction 第1段几乎逐句重复 Abstract 的内容（同样的 10% overlap, 79% σ reduction, Bonferroni-adjusted p = .100, BCa 95% CI 等数字）。这浪费了宝贵的页面空间（在 8 页限制下），且降低阅读体验。\n- 建议：Introduction 应 *expand on* abstract 而非 *repeat* it——提供更多动机、背景和论文结构说明，将具体数字留给 Results。\n\n**W5** [warning] Ensemble diversity 文献连接不充分\n- 具体位置：§2 Related Work\n- 问题：论文本质上在测量 cross-architecture diversity，但仅引用 Kuncheva & Whitaker (2003) 一篇 ensemble diversity 文献。该领域有丰富的 diversity measures（Q-statistic, disagreement measure, double-fault measure, κ-statistic）和理论（bias-variance-covariance decomposition for ensembles），与本文的 Jaccard-based analysis 直接相关。Fort et al. (2019) 被引用但未充分讨论其 loss landscape perspective 如何解释 cross-architecture divergence。\n- 建议：添加 2-3 句讨论 ensemble diversity 理论如何预期/解释本文的 per-example divergence 发现，以及 Jaccard 与其他 diversity measures 的关系。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1** §3.4 \"All statistical tests are two-tailed unless otherwise noted\" 后紧接 Appendix A 讨论 one-sided test (p = 0.0083)。建议在正文中简要提及 one-sided 结果的存在，避免 reviewers 质疑 cherry-picking。\n- **M2** references.bib 中 `dodge2020finetuning` 的 `booktitle` 字段设为 arXiv 链接而非 venue，应修正为 `journal = {arXiv preprint arXiv:2002.06305}` 或引用已发表版本。\n- **M3** Table 1 脚注提到 \"Bonferroni-adjusted p = 6 × 2/120 = 0.100 (exact); 0.102 arises from rounding\" — 两个数字 (0.100 vs 0.102) 同时出现造成混淆。选择一个并解释即可。\n- **M4** §4.2 \"normalized ES 0.065 helped, 0.062 hurt\" 中 ES 缩写首次出现未定义（effect size），虽从上下文可推断，但建议在首次使用时展开。\n- **M5** Conclusion 中 \"confidence-informed routing\" 被提出作为利用 complementarity 的方向，但全文未提供任何 routing 的初步实验或 feasibility analysis，使得这一建议悬浮。\n\n---\n\n## 主要优势\n\n1. **统计方法论的透明度和严谨性出色**：论文在每一步都提供了 exact p-values、power analysis、bootstrap CIs，并坦诚 n = 3 architectures 和 n = 5 attention ratios 的统计局限性。GDN confound 的 sensitivity analysis (§4.4, Appendix D-E) 是特别好的做法。\n2. **附录极其详尽**（12 页，17+ 张表）：covering cross-scale analysis, supplementary benchmarks (BoolQ, WinoGrande), within-architecture stability, normalized Jaccard effect sizes, confidence margin analysis, complementarity decomposition——每个 claim 都有 backup evidence。\n3. **实验设计利用了 controlled model zoo**：固定 training data / hyperparameters / tokenizer 仅变化 architecture 和 attention ratio，是研究 architectural effects 的理想设置（在 single-run limitation 下）。\n4. **Per-example decomposition 和 confidence margin analysis** 提供了超越简单 aggregate comparison 的分析粒度，confidence margin 作为 within-architecture predictor (AUC 0.70–0.74) 是一个有用的发现。\n5. **格式完全合规**：8 页正文、ACL 模板、double-blind、Limitations 简洁覆盖 3 点、Ethics Statement 存在。\n\n---\n\n## Questions to Authors\n\n1. 你们如何将 decoupling finding 与 ecological fallacy (Robinson, 1950) 区分开？Aggregate convergence 不蕴含 per-example convergence 这一事实是否可以在不做任何实验的情况下从统计原理预期？\n2. 如果 GDN 的 16-head configuration 是 convergence 结果的主要驱动因素（而非 architecture 本身），那么 §4.1 的 convergence 主张是否应被完全撤回而非仅标注为 \"exploratory\"？\n3. 论文建议做 \"per-example audits\"，但具体如何操作？在没有 oracle 标签的 deployment 场景下，practitioners 能做什么？\n4. Single training runs 使 architecture vs. seed effects 无法区分。α = 0.14–0.30 中有多少可能来自 seed noise 而非 architectural difference？3× within- vs. cross-architecture Jaccard gap 能否定量 bound 这一比例？\n\n---\n\n## Missing References\n\n- Robinson, W.S. (1950). \"Ecological Correlations and the Behavior of Individuals.\" — ecological fallacy 的经典参考，直接关联 decoupling finding\n- Brown, G., Wyatt, J., Harris, R., & Yao, X. (2005). \"Diversity Creation Methods: A Survey and Categorisation.\" — ensemble diversity measures 综述，与 cross-architecture diversity analysis 相关\n- Jiang, Z., Araki, J., Ding, H., & Neubig, G. (2021). \"How Can We Know When Language Models Know? Measuring and Bridging the Calibration Gap.\" — 与 confidence margin analysis (§4.2, Appendix H) 相关\n",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 943 · 2026-05-22T09:52:14.770459+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4068
}
```

</details>

---


### Tool call

_source line 944 · 2026-05-22T09:52:24.164790+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_13/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 945 · 2026-05-22T09:52:24.165213+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 946 · 2026-05-22T09:52:34.312348+00:00_

审稿完成，已提交至 Review Director。

**核心评判**：Overall 3.0 (Findings)。

三个 Must-Fix 问题：
1. **Ecological fallacy 未讨论** — decoupling finding 是该已知统计原理的具体实例，论文完全未提及
2. **Convergence 结果统计不足却占据核心叙事位置** — LAMBADA p = .100 (Bonferroni后)、依赖 GDN (有 16-head confound)，但在 Abstract/Introduction 中作为主要发现呈现
3. **新颖性有限** — 所有分析工具（Jaccard, α, permutation test）均为已有方法直接套用，核心发现是将 seed-variation 文献中的已知现象扩展到 cross-architecture 场景

主要优势：统计方法透明严谨、附录极其详尽（12页17+张表）、controlled model zoo 设计合理、confidence margin analysis 提供了有用的 within-architecture predictor。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 947 · 2026-05-22T09:53:09.699405+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每一个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions (Q1-Q4)，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.0 (Findings)
**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5

### Must-Fix

**N1** [critical] Convergence claim 的统计基础不足：仅 LAMBADA 一个 benchmark 的边际显著结果
- §4.1, Table 1, Abstract: LAMBADA Spearman ρ = −1.0, Bonferroni 校正后 p = .100，不显著。其余 5 个 confirmatory benchmark 均不显著。Abstract 将 p ≈ .100 作为 convergence 证据呈现有误导性。"Decoupling" 是核心 claim，如果 convergence 这半不成立，decoupling 退化为"无 convergence，per-example 也无 convergence"，叙事价值大幅下降。
- 建议：将 convergence 定位为 exploratory 发现，不与 decoupling 并列作为 key contribution。

**N2** [critical] n=5 Spearman 检验的 power 缺陷使全文多数相关性分析不可解读
- §3.3, §4.1, Table 1: n=5 exact Spearman 只有 |ρ| = 1.0 才能 p < .05。|ρ| = 0.9 无法检测。"No other benchmark shows significant convergence" 是 absence of evidence 被当作 evidence of absence。
- 建议：报告 power analysis，明确 non-significant ≠ 无效应，考虑 Bayesian 分析。

**N3** [critical] 单次训练 run 无法分离架构效应与种子效应
- Limitations, §4.2, §4.3: 每个配置仅一次训练。within-architecture Jaccard ~3× cross-architecture Jaccard 作为间接证据不够。如果 per-example profiles 在不同 seed 下不可复现，核心发现就不成立。
- 建议：补充 2-3 个 seed 的 replicate，或将 "architecture-specific" 全面降级为 "configuration-specific"。

### Should-Fix

**W1** [major] GDN h3-1 的 16-head confound 直接威胁唯一显著的 convergence 结果
- Appendix E, D: 排除 GDN 后 LAMBADA convergence 从 ρ = −1.0 弱化到 ρ = −0.7（不再显著）。
- 建议：在主文讨论此 confound，报告排除 GDN 后的等价结果。

**W2** [major] Bootstrap CI (n=3) 提供的统计信息量极低
- §3.3, Figure 2: n=3 仅 27 个唯一 resample，Figure 2 中 CI 可能被当作标准置信区间解读。
- 建议：Figure 2 caption 更显著注明限制，改用 strip plot 展示个体值。

**W3** [major] Binary decomposition (helped/hurt/unchanged) 丢失效应量信息
- §3.4, §4.2: 0.51→0.49 和 0.99→0.01 被同等对待。Jaccard 对边界翻转和确信翻转一视同仁。
- 建议：引入 continuous metric 补充，报告 confidence margin 分布。

**W4** [warning] Confirmatory/exploratory split 缺乏外部时间戳验证
- §3.2, Appendix A: 无 pre-registration 证据。
- 建议：标注为 informal pre-analysis plan。

**W5** [warning] 评估覆盖范围有限：3 架构、2 scale、4 主 benchmark
- §3.1, Limitations: 不含 Mamba/Mamba-2/RWKV，无 generation tasks。
- 建议：Limitations 中更具体讨论 generalization 边界。

### Questions

**Q1**: 补充 2-3 个 seed replicate 后，within-seed vs cross-seed Jaccard 预期比值？
**Q2**: MMLU 和 ARC-Easy 的 non-significance 完全由 power 限制解释？n=10 是否会显著？
**Q3**: Jaccard 在 4% attention 饱和的发现在 340M 是否成立？
**Q4**: 3× within/cross Jaccard 比率在控制 GDN 16-head confound 后是否成立？

### Missing References
- Wen et al. (2024) BatchEnsemble
- Barocas et al. (2023) predictive multiplicity in fairness
- Peng et al. (2025) RWKV-7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 948 · 2026-05-22T09:54:41.675234+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Convergence claim 统计基础不足**\n同意。这与我的 N2 一致。LAMBADA 的 Bonferroni-adjusted p = .100 未达传统显著性（Table 1），且依赖 GDN 包含（§4.4: 排除后 ρ = −0.7, p = .233）。我进一步认为，论文的叙事结构给予 convergence 过高权重——Abstract 第2句、Introduction 第1段均围绕此展开。R1 提出的 \"无 convergence 则 decoupling 退化为无意义\" 是精准的批评：如果 convergence 本身就不成立，那么 \"convergence 与 per-example divergence 脱耦\" 这一 framing 失去了对比的一半。建议作者将论文核心叙事重构为 \"per-example multiplicity 在 hybrid recurrent architectures 中的系统性表征\"，将 convergence 作为可选的附加观察。\n\n**[AGREE with nuance] R1-N2: n=5 Spearman power 缺陷**\n基本同意但有补充。R1 指出 n=5 时仅 |ρ| = 1.0 能达 p < .05——论文自身在 §3.3 Power considerations 段已明确承认这一点（\"only ρ = ±1.0 achieves p < .05 (exact p = .017); the test has no power to detect strong but imperfect monotonic trends\"）。所以论文 *aware* of this limitation，并非忽略。但 R1 的核心批评仍然成立：Table 1 中 9 个 non-significant benchmarks 的 \"no significant convergence\" 表述确实容易被误读为 evidence of absence。论文在 §4.1 最后一句 (\"No other benchmark shows significant convergence\") 没有附加 power caveat，这是疏漏。\n\n然而，我**不认为** Bayesian analysis 是必要的修改。论文已经提供了 BCa bootstrap CIs 和 effect sizes（convergence ratio σ_pure/σ_h3-1）作为 p-value 的补充（Table 1），这在功能上等同于 R1 要求的信息。更 practical 的修改是：(1) 在 Table 1 旁添加一句 \"Non-significance should not be interpreted as evidence against convergence given the limited power\"；(2) 将 non-significant benchmarks 的讨论聚焦于 effect size direction 而非 p-value。\n\n**[AGREE] R1-N3: 单次训练无法分离架构与种子效应**\n同意，这也是我的关注点。3× within- vs. cross-architecture Jaccard gap（§4.3, Appendix K: within ~0.33 vs. cross ~0.10）是有信息量的间接证据，但 R1 正确指出这不充分——within-architecture 比较跨 attention ratio 本身引入了第二个变量（attention dose），不是纯粹的 \"same architecture, different conditions\" vs. \"different architecture, same conditions\" 对比。\n\n不过，\"补充 2-3 个 seed replicate\" 的建议可能不现实。论文使用的是 Wang et al. (2025) 的公开 model zoo（§3.1），作者并未自行训练模型。补充 seed replicates 意味着重新 pre-train 30 个 1.3B 参数模型，计算成本极高。更可行的修改是：(1) 将全文的 \"architecture-specific\" 系统性替换为 \"configuration-specific\"（R1 建议），在 claims 成立不依赖 architecture vs. seed 区分的地方（如 multiplicity 的存在性和 task-dependent variation）保持原表述；(2) 在 Limitations 中更量化地讨论 seed contribution 的 upper bound。\n\n---\n\n## Should-Fix\n\n**[AGREE] R1-W1: GDN 16-head confound 应在主文讨论**\n完全同意。当前 confound 仅在 §4.4 Robustness 的一小段和 Appendix E 中处理。鉴于排除 GDN 使唯一显著结果消失，这一 confound 的讨论应在 §4.1 首次报告 LAMBADA 结果时就出现，而非延后到 §4.4。这是 presentation 问题，不需要新实验。\n\n**[REBUT with partial agree] R1-W2: Bootstrap CI (n=3) 信息量低**\n部分反驳。论文已在 §3.3 明确标注 \"these intervals should be interpreted as heuristic indicators of effect direction rather than intervals with formal coverage guarantees\"，并在 Figure 2 caption 中标注 \"BCa 95% CI [−1.0, −0.7], heuristic\"。作者的 \"heuristic\" 标签准确反映了 n=3 的限制。\n\n但 R1 说得对，Figure 2 中的 CI bars 视觉上容易被误读为标准置信区间。R1 建议的 strip plot（展示 3 个 individual architecture 值）是更好的可视化方案——3 个点本身就是完整的数据，不需要 summary statistics。这是一个值得采纳的 *visualization* 建议，但我不认为它构成 \"major\" 级别问题。\n\n**[REBUT] R1-W3: Binary decomposition 丢失效应量信息**\n不同意这是一个 Should-Fix。论文在 §4.2 第一段已明确承认 binary decomposition 的局限（\"This binarization discards confidence magnitude (a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01)\"），并提供了两层补充证据：\n1. §4.2 reports Cohen's d = 0.73–0.92 between helped and hurt on LAMBADA，证明 binary categories 对应 *genuine* continuous separation\n2. Appendix H (Target-Token Confidence Margin) 是完整的 continuous analysis：Tables 12-13 报告 within-category |log p| 分布, Tables 14-15 报告 cross-benchmark extension, Table 16 报告 AUC-based prediction framework\n\n这恰恰是 R1 建议的 \"引入 continuous metric 补充\"——论文已经做了，且做得相当彻底。R1 可能遗漏了 Appendix H 的内容。\n\n**[AGREE] R1-W4: Confirmatory/exploratory split 缺乏时间戳**\n同意，但论文已经在 Appendix A 第一段承认 \"we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists\"。R1 建议的 \"informal pre-analysis plan\" 标签与论文现有表述一致。这是一个 minor 修改（措辞调整），非 major 问题。\n\n**[AGREE] R1-W5: 覆盖范围有限**\n同意。Limitations 中 \"three architectures from one model zoo\" 的表述过于简略。应具体讨论：(1) 缺少 Mamba/Mamba-2 这类 dominant SSM architectures（model zoo 不含它们）；(2) 所有 benchmark 都是 discriminative/classification tasks，无 generation 评估；(3) 仅 pre-training evaluation，无 instruction-tuning 或 RLHF 后的评估。这些是 generalization 的真实边界。\n\n---\n\n## Questions\n\n**R1-Q1**: 关于 seed replicate 后 within-seed vs. cross-seed Jaccard 预期比值。\n无法从论文数据直接回答（没有 seed replicates）。但从 MultiBERTs (Sellam et al. 2022) 的数据可以类比：seed variation 在 BERT 中产生的 per-example disagreement 约 5-15%，与本文的 cross-architecture 15-45% disagreement 相比较小。如果 cross-architecture multiplicity 中 seed 贡献显著，我们预期 within-architecture Jaccard (~0.33, Appendix K Table 11) 应更接近 cross-architecture Jaccard (~0.10)，但 3× gap 暗示 architecture 是主要因素。这不是 definitive evidence，但方向一致。\n\n**R1-Q2**: MMLU/ARC-Easy 的 non-significance 是否仅因 power 不足。\n从 Table 1 effect sizes 看：ARC-Easy σ ratio = 7.70（最高），MMLU σ ratio = 2.27。ARC-Easy 的 effect direction 强且 stable（排除 GDN 后 ρ 不变，per Appendix D），暗示 n=10 可能达到 significance。MMLU 则 artifactual（排除 GDN 后 ρ 从 −0.7 反转为 +0.6，Table 3）。所以 power 不是唯一解释——至少 MMLU 的 non-significance 反映了 true null（GDN-driven artifact）。\n\n**R1-Q3**: Jaccard 在 4% 饱和的发现是否在 340M 成立。\n论文在 Appendix N (Table 17) 报告了 4 个 benchmark 的跨 attention-ratio Jaccard 轨迹，但仅限 1.3B。Appendix J (§J.1) 报告 340M 与 1.3B 的 mean Jaccard 相似（~0.089 vs. ~0.095），但未报告 340M 的 ratio-by-ratio 轨迹。这是一个合理的数据缺口，建议作者补充。\n\n**R1-Q4**: 3× within/cross Jaccard 比率在控制 GDN 后是否成立。\n§4.4 报告 RetNet–HGRN2 pair preserves decoupling（Jaccard 0.086–0.108），Appendix K Table 11 的 within-architecture Jaccard 为 ~0.33。排除 GDN 后 cross-architecture Jaccard（仅 RetNet-HGRN2）在 Table 5 (Appendix F) 为 0.108 (helped) 和 0.087 (hurt)。因此 within/cross ratio 大约 0.33/0.10 ≈ 3×，在排除 GDN 后近似成立。但 n=1 pair 使这一估计非常不稳定。\n\n---\n\n## Missing References\n\n**Wen et al. (2024) BatchEnsemble**: [REBUT] 相关性低。BatchEnsemble 是一种 parameter-efficient ensemble method，解决的是如何廉价构建 ensembles，与本文研究的 cross-architecture multiplicity 现象无直接关联。本文不构建 ensembles，而是分析已有 single models 的 per-example 行为。\n\n**Barocas et al. (2023) predictive multiplicity in fairness**: [AGREE] 如果指的是 Cooper et al. (2024) \"Arbitrariness and Social Prediction\"——论文已引用（references.bib line 38-43, §2 Related Work）。如果 R1 指的是另一篇 Barocas 2023 fairness 文献，需要具体 title 才能评估。\n\n**Peng et al. (2025) RWKV-7**: [AGREE with caveat] RWKV-7 是 linear recurrent architecture 的重要进展，在 §2 Hybrid Recurrent Architectures 或 §2 Linear Recurrent Models 中提及是合理的。但 RWKV-7 不在 Wang et al. (2025) model zoo 中，因此对论文的实证分析无影响。建议在 Related Work 中添加一句提及，并在 Limitations 中注明 coverage 不含 RWKV 系列。\n",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix\n\n**[AGREE] R1-N1: Convergence claim 统计基础不足**\n同意。这与我的 N2 一致。LAMBADA 的 Bonferroni-adjusted p = .100 未达传统显著性（Table 1），且依赖 GDN 包含（§4.4: 排除后 ρ = −0.7, p = .233）。我进一步认为，论文的叙事结构给予 convergence 过高权重——Abstract 第2句、Introduction 第1段均围绕此展开。R1 提出的 \"无 convergence 则 decoupling 退化为无意义\" 是精准的批评：如果 convergence 本身就不成立，那么 \"convergence 与 per-example divergence 脱耦\" 这一 framing 失去了对比的一半。建议作者将论文核心叙事重构为 \"per-example multiplicity 在 hybrid recurrent architectures 中的系统性表征\"，将 convergence 作为可选的附加观察。\n\n**[AGREE with nuance] R1-N2: n=5 Spearman power 缺陷**\n基本同意但有补充。R1 指出 n=5 时仅 |ρ| = 1.0 能达 p < .05——论文自身在 §3.3 Power considerations 段已明确承认这一点（\"only ρ = ±1.0 achieves p < .05 (exact p = .017); the test has no power to detect strong but imperfect monotonic trends\"）。所以论文 *aware* of this limitation，并非忽略。但 R1 的核心批评仍然成立：Table 1 中 9 个 non-significant benchmarks 的 \"no significant convergence\" 表述确实容易被误读为 evidence of absence。论文在 §4.1 最后一句 (\"No other benchmark shows significant convergence\") 没有附加 power caveat，这是疏漏。\n\n然而，我**不认为** Bayesian analysis 是必要的修改。论文已经提供了 BCa bootstrap CIs 和 effect sizes（convergence ratio σ_pure/σ_h3-1）作为 p-value 的补充（Table 1），这在功能上等同于 R1 要求的信息。更 practical 的修改是：(1) 在 Table 1 旁添加一句 \"Non-significance should not be interpreted as evidence against convergence given the limited power\"；(2) 将 non-significant benchmarks 的讨论聚焦于 effect size direction 而非 p-value。\n\n**[AGREE] R1-N3: 单次训练无法分离架构与种子效应**\n同意，这也是我的关注点。3× within- vs. cross-architecture Jaccard gap（§4.3, Appendix K: within ~0.33 vs. cross ~0.10）是有信息量的间接证据，但 R1 正确指出这不充分——within-architecture 比较跨 attention ratio 本身引入了第二个变量（attention dose），不是纯粹的 \"same architecture, different conditions\" vs. \"different architecture, same conditions\" 对比。\n\n不过，\"补充 2-3 个 seed replicate\" 的建议可能不现实。论文使用的是 Wang et al. (2025) 的公开 model zoo（§3.1），作者并未自行训练模型。补充 seed replicates 意味着重新 pre-train 30 个 1.3B 参数模型，计算成本极高。更可行的修改是：(1) 将全文的 \"architecture-specific\" 系统性替换为 \"configuration-specific\"（R1 建议），在 claims 成立不依赖 architecture vs. seed 区分的地方（如 multiplicity 的存在性和 task-dependent variation）保持原表述；(2) 在 Limitations 中更量化地讨论 seed contribution 的 upper bound。\n\n---\n\n## Should-Fix\n\n**[AGREE] R1-W1: GDN 16-head confound 应在主文讨论**\n完全同意。当前 confound 仅在 §4.4 Robustness 的一小段和 Appendix E 中处理。鉴于排除 GDN 使唯一显著结果消失，这一 confound 的讨论应在 §4.1 首次报告 LAMBADA 结果时就出现，而非延后到 §4.4。这是 presentation 问题，不需要新实验。\n\n**[REBUT with partial agree] R1-W2: Bootstrap CI (n=3) 信息量低**\n部分反驳。论文已在 §3.3 明确标注 \"these intervals should be interpreted as heuristic indicators of effect direction rather than intervals with formal coverage guarantees\"，并在 Figure 2 caption 中标注 \"BCa 95% CI [−1.0, −0.7], heuristic\"。作者的 \"heuristic\" 标签准确反映了 n=3 的限制。\n\n但 R1 说得对，Figure 2 中的 CI bars 视觉上容易被误读为标准置信区间。R1 建议的 strip plot（展示 3 个 individual architecture 值）是更好的可视化方案——3 个点本身就是完整的数据，不需要 summary statistics。这是一个值得采纳的 *visualization* 建议，但我不认为它构成 \"major\" 级别问题。\n\n**[REBUT] R1-W3: Binary decomposition 丢失效应量信息**\n不同意这是一个 Should-Fix。论文在 §4.2 第一段已明确承认 binary decomposition 的局限（\"This binarization discards confidence magnitude (a transition from 0.51 to 0.49 is treated identically to one from 0.99 to 0.01)\"），并提供了两层补充证据：\n1. §4.2 reports Cohen's d = 0.73–0.92 between helped and hurt on LAMBADA，证明 binary categories 对应 *genuine* continuous separation\n2. Appendix H (Target-Token Confidence Margin) 是完整的 continuous analysis：Tables 12-13 报告 within-category |log p| 分布, Tables 14-15 报告 cross-benchmark extension, Table 16 报告 AUC-based prediction framework\n\n这恰恰是 R1 建议的 \"引入 continuous metric 补充\"——论文已经做了，且做得相当彻底。R1 可能遗漏了 Appendix H 的内容。\n\n**[AGREE] R1-W4: Confirmatory/exploratory split 缺乏时间戳**\n同意，但论文已经在 Appendix A 第一段承认 \"we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists\"。R1 建议的 \"informal pre-analysis plan\" 标签与论文现有表述一致。这是一个 minor 修改（措辞调整），非 major 问题。\n\n**[AGREE] R1-W5: 覆盖范围有限**\n同意。Limitations 中 \"three architectures from one model zoo\" 的表述过于简略。应具体讨论：(1) 缺少 Mamba/Mamba-2 这类 dominant SSM architectures（model zoo 不含它们）；(2) 所有 benchmark 都是 discriminative/classification tasks，无 generation 评估；(3) 仅 pre-training evaluation，无 instruction-tuning 或 RLHF 后的评估。这些是 generalization 的真实边界。\n\n---\n\n## Questions\n\n**R1-Q1**: 关于 seed replicate 后 within-seed vs. cross-seed Jaccard 预期比值。\n无法从论文数据直接回答（没有 seed replicates）。但从 MultiBERTs (Sellam et al. 2022) 的数据可以类比：seed variation 在 BERT 中产生的 per-example disagreement 约 5-15%，与本文的 cross-architecture 15-45% disagreement 相比较小。如果 cross-architecture multiplicity 中 seed 贡献显著，我们预期 within-architecture Jaccard (~0.33, Appendix K Table 11) 应更接近 cross-architecture Jaccard (~0.10)，但 3× gap 暗示 architecture 是主要因素。这不是 definitive evidence，但方向一致。\n\n**R1-Q2**: MMLU/ARC-Easy 的 non-significance 是否仅因 power 不足。\n从 Table 1 effect sizes 看：ARC-Easy σ ratio = 7.70（最高），MMLU σ ratio = 2.27。ARC-Easy 的 effect direction 强且 stable（排除 GDN 后 ρ 不变，per Appendix D），暗示 n=10 可能达到 significance。MMLU 则 artifactual（排除 GDN 后 ρ 从 −0.7 反转为 +0.6，Table 3）。所以 power 不是唯一解释——至少 MMLU 的 non-significance 反映了 true null（GDN-driven artifact）。\n\n**R1-Q3**: Jaccard 在 4% 饱和的发现是否在 340M 成立。\n论文在 Appendix N (Table 17) 报告了 4 个 benchmark 的跨 attention-ratio Jaccard 轨迹，但仅限 1.3B。Appendix J (§J.1) 报告 340M 与 1.3B 的 mean Jaccard 相似（~0.089 vs. ~0.095），但未报告 340M 的 ratio-by-ratio 轨迹。这是一个合理的数据缺口，建议作者补充。\n\n**R1-Q4**: 3× within/cross Jaccard 比率在控制 GDN 后是否成立。\n§4.4 报告 RetNet–HGRN2 pair preserves decoupling（Jaccard 0.086–0.108），Appendix K Table 11 的 within-architecture Jaccard 为 ~0.33。排除 GDN 后 cross-architecture Jaccard（仅 RetNet-HGRN2）在 Table 5 (Appendix F) 为 0.108 (helped) 和 0.087 (hurt)。因此 within/cross ratio 大约 0.33/0.10 ≈ 3×，在排除 GDN 后近似成立。但 n=1 pair 使这一估计非常不稳定。\n\n---\n\n## Missing References\n\n**Wen et al. (2024) BatchEnsemble**: [REBUT] 相关性低。BatchEnsemble 是一种 parameter-efficient ensemble method，解决的是如何廉价构建 ensembles，与本文研究的 cross-architecture multiplicity 现象无直接关联。本文不构建 ensembles，而是分析已有 single models 的 per-example 行为。\n\n**Barocas et al. (2023) predictive multiplicity in fairness**: [AGREE] 如果指的是 Cooper et al. (2024) \"Arbitrariness and Social Prediction\"——论文已引用（references.bib line 38-43, §2 Related Work）。如果 R1 指的是另一篇 Barocas 2023 fairness 文献，需要具体 title 才能评估。\n\n**Peng et al. (2025) RWKV-7**: [AGREE with caveat] RWKV-7 是 linear recurrent architecture 的重要进展，在 §2 Hybrid Recurrent Architectures 或 §2 Linear Recurrent Models 中提及是合理的。但 RWKV-7 不在 Wang et al. (2025) model zoo 中，因此对论文的实证分析无影响。建议在 Related Work 中添加一句提及，并在 Limitations 中注明 coverage 不含 RWKV 系列。\n",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 949 · 2026-05-22T09:54:45.596839+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3921
}
```

</details>

---


### Assistant

_source line 950 · 2026-05-22T09:54:54.624170+00:00_

已完成对 Reviewer 1 全部意见的逐条回应，已提交至 Director。总结：

- **N1 (convergence 统计不足)**: AGREE — 与我的 N2 一致
- **N2 (n=5 power)**: AGREE with nuance — 论文已在 §3.3 承认，但 Table 1 讨论中缺少 power caveat；不认为 Bayesian analysis 是必要的
- **N3 (single runs)**: AGREE — 但补充 seed replicates 不现实（公开 model zoo），建议改用 "configuration-specific" 措辞
- **W1 (GDN confound)**: AGREE
- **W2 (bootstrap CI n=3)**: REBUT (partial) — 论文已标注 "heuristic"，但同意改用 strip plot
- **W3 (binary decomposition)**: REBUT — Appendix H 已提供完整的 continuous confidence margin analysis，R1 可能遗漏
- **W4 (pre-registration)**: AGREE — 论文已承认，minor 修改
- **W5 (coverage)**: AGREE
- **Q1-Q4**: 基于论文数据逐一回答，指出 Q3 存在数据缺口（缺 340M ratio-by-ratio Jaccard 轨迹）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 24

## Round 24

74 recorded events


### User

_source line 951 · 2026-05-22T11:55:13.579869+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 方向的审稿。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR May 2026 cycle）
- **投稿类别**: Long Paper
- **正文页数限制**: 8 页（参考文献不限，Limitations/Ethics 不计页数）
- **模板**: ACL（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind
- **截止日期**: 2026-05-25

## 论文信息
- **标题**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
- **论文路径**: `docs/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf`

## 你的审查侧重

请重点从以下角度审查：

1. **新颖性评估**：
   - 将 predictive multiplicity 框架应用于 hybrid recurrent architectures 是否构成足够的学术贡献
   - 核心发现（per-example divergence despite aggregate convergence）相对于已有 underspecification / multiplicity 文献的增量贡献
   - 是否只是在新数据上重复已知现象
   - 对 NLP 社区的潜在影响和实用价值

2. **Related Work 完整性**：
   - 是否遗漏了重要的相关工作
   - 与 ensemble diversity、model disagreement、Rashomon set 文献的区分是否清晰
   - 与最新 hybrid architecture 文献的关系

3. **写作质量**：
   - 论文结构是否清晰
   - Claims 是否与证据匹配（是否存在 overclaiming 或 hedging 不足）
   - 术语使用是否一致
   - Figure 和 Table 是否有效传达信息
   - Abstract 是否准确反映论文内容

4. **完整性**：
   - 实验结果是否完整呈现（正面和负面结果）
   - Limitations 是否充分
   - 是否有 cherry-picking 嫌疑
   - Appendix 是否必要且信息量足够

5. **格式合规**：
   - 是否符合 8 页正文限制
   - ACL 模板使用是否正确
   - 匿名是否完整
   - 参考文献格式

按 ARR 标准输出审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，标注 Critical/Major/Minor）、Questions、Missing References、Overall Assessment（使用 EMNLP 2026 评分标准 1-5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 952 · 2026-05-22T11:55:24.122457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 953 · 2026-05-22T11:55:24.925015+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 954 · 2026-05-22T11:55:25.076112+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 955 · 2026-05-22T11:55:25.076586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 956 · 2026-05-22T11:55:30.050086+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 957 · 2026-05-22T11:55:30.853242+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
  "pages": "1-8",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
    "pages": "1-8",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 958 · 2026-05-22T11:55:36.879996+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on my search results, here's what I found about ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also
…[truncated 1273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6829
}
```

</details>

---


### Tool result

_source line 959 · 2026-05-22T11:55:38.237548+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 450.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.6}], \"total_pages\": 21, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images\"}, \"er
…[truncated 32 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7384
}
```

</details>

---


### Tool call

_source line 960 · 2026-05-22T11:55:44.765797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 961 · 2026-05-22T11:55:45.270128+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 962 · 2026-05-22T11:55:46.276883+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---


### Tool call

_source line 963 · 2026-05-22T11:55:46.277280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 964 · 2026-05-22T11:55:46.682125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 965 · 2026-05-22T11:55:47.489532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2219
}
```

</details>

---


### Tool call

_source line 966 · 2026-05-22T11:55:47.489978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 967 · 2026-05-22T11:55:48.143823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 968 · 2026-05-22T11:55:48.749825+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool call

_source line 969 · 2026-05-22T11:55:48.750216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 970 · 2026-05-22T11:55:49.103902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2421
}
```

</details>

---


### Tool call

_source line 971 · 2026-05-22T11:55:49.104482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 972 · 2026-05-22T11:55:49.863130+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form dimensions soundness excitement clarity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review review form dimensions soundness excitement clarity 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 973 · 2026-05-22T11:55:50.277101+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2787
}
```

</details>

---


### Tool result

_source line 974 · 2026-05-22T11:55:50.785506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2641
}
```

</details>

---


### Tool result

_source line 975 · 2026-05-22T11:55:50.987967+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2237
}
```

</details>

---


### Tool result

_source line 976 · 2026-05-22T11:55:51.089265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1984
}
```

</details>

---


### Tool result

_source line 977 · 2026-05-22T11:55:56.328427+00:00_

Web search results for query: "ACL Rolling Review review form dimensions soundness excitement clarity 2025 2026"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the web search results, here's information about the ACL Rolling Review (ARR) review form dimensions:

## Review Form Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness

Reviewers assess whether papers are sufficiently sound and thorough, clearly state scientific claims and provide adequate support for them, and consider the depth and/or breadth of research questions, technical soundness of experiments, and methodological validity of evaluation. The soundness scores must be justified by the text of the review.

### Excitement

Excitement is subjective and does not necessar
…[truncated 651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6465
}
```

</details>

---


### Tool call

_source line 978 · 2026-05-22T11:56:03.350246+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
  "pages": "9-20",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
    "pages": "9-20",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool call

_source line 979 · 2026-05-22T11:56:03.707198+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 980 · 2026-05-22T11:56:06.270726+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.8}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.2}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 472.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 389.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 401.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 458.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p17.png\", \"width\": 1241, \"heig
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2920
}
```

</details>

---


### Tool result

_source line 981 · 2026-05-22T11:56:06.271074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 2563
}
```

</details>

---


### Tool call

_source line 982 · 2026-05-22T11:56:10.136824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 983 · 2026-05-22T11:56:10.639426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 984 · 2026-05-22T11:56:11.094264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 985 · 2026-05-22T11:56:11.094688+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 986 · 2026-05-22T11:56:12.001867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 987 · 2026-05-22T11:56:12.002804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 988 · 2026-05-22T11:56:12.053822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 989 · 2026-05-22T11:56:12.508817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 990 · 2026-05-22T11:56:13.013735+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 991 · 2026-05-22T11:56:13.014153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 992 · 2026-05-22T11:56:13.920403+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 993 · 2026-05-22T11:56:13.923342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 994 · 2026-05-22T11:56:13.923831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 995 · 2026-05-22T11:56:14.380536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 996 · 2026-05-22T11:56:14.382882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 997 · 2026-05-22T11:56:14.885366+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 998 · 2026-05-22T11:56:16.094288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1711
}
```

</details>

---


### Tool result

_source line 999 · 2026-05-22T11:56:16.496770+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1611
}
```

</details>

---


### Tool call

_source line 1000 · 2026-05-22T11:56:16.597583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1001 · 2026-05-22T11:56:16.648328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1002 · 2026-05-22T11:56:16.800811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1003 · 2026-05-22T11:56:18.359699+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1762
}
```

</details>

---


### Tool result

_source line 1004 · 2026-05-22T11:56:18.360684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1712
}
```

</details>

---


### Tool result

_source line 1005 · 2026-05-22T11:56:18.361300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool call

_source line 1006 · 2026-05-22T11:56:18.361493+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. Include soundness, excitement, overall assessment, and any other fields reviewers must fill out. List the exact score labels for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. Include soundness, excitement, overall assessment, and any other fields reviewers must fill out. List the exact score labels for each dimension."
  }
}
```

</details>

---


### Tool result

_source line 1007 · 2026-05-22T11:56:25.648673+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Dimensions

**Paper Summary**
Brief description of paper topic and content to clarify understanding.

**Summary of Strengths**
Major reasons supporting publication, including novel methodology, empirical results, or clarity.

**Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other publication obstacles.

**Comments/Suggestions/Typos**
Additional improvement recommendations beyond main concerns.

## Scoring Dimensions

### Reviewer Confidence
- 5: Positive evaluation; careful reading with familiarity of related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area knowledge but incomplete detail verification
- 2: Willing to defend but likely missed details or novelty assessment uncertain
- 1: Outside expertise area or paper very difficult to understand

### Soundness
- 5: Excellent; one of most thorough studies of its type
- 4–4.5: Strong; sufficient support for claims
- 3–3.5: Acceptable; main claims supported with minor gaps
- 2–2.5: Poor; insufficient support or major technical problems
- 1–1.5: Major issues; insufficient for publication or irrelevant to ACL

### Excitement
- 5: Highly exciting; would recommend to others
- 4–4.5: Exciting; would mention to others
- 3–3.5: Interesting; might mention selectively
- 2–2.5: Potentially interesting but limited personal resonance
- 1–1.5: Not exciting; unlikely community appeal

### Overall Assessment
- 5: Award consideration (top 2.5%)
- 4–4.5: Conference acceptance
- 3–3.5: Findings acceptance
- 2–2.5: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Additional Evaluation Areas

- **Limitations and Societal Impact**
- **Ethical Concerns** (per ACL Code of Ethics)
- **Needs Ethics Review** (flag if required)
- **Reproducibility** (5-point scale)
- **Datasets** (5-point value assessment)
- **Software** (5-point value assessment)
- **Author Identity Knowledge** (5-p
…[truncated 11 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7287
}
```

</details>

---


### Tool call

_source line 1008 · 2026-05-22T11:56:31.874612+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
  "pages": "21",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/submitted.pdf",
    "pages": "21",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1009 · 2026-05-22T11:56:31.975347+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 294.4}], \"total_pages\": 21, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1010 · 2026-05-22T11:56:35.243834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1011 · 2026-05-22T11:56:35.848202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1012 · 2026-05-22T11:59:21.225160+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "predictive multiplicity hybrid recurrent architectures SSM per-example divergence 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "predictive multiplicity hybrid recurrent architectures SSM per-example divergence 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 1013 · 2026-05-22T11:59:22.304494+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Milani Fard prediction churn model instability 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Milani Fard prediction churn model instability 2016"
  }
}
```

</details>

---


### Tool call

_source line 1014 · 2026-05-22T11:59:22.355072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Garipov loss surface mode connectivity ensembling 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Garipov loss surface mode connectivity ensembling 2018"
  }
}
```

</details>

---


### Tool result

_source line 1015 · 2026-05-22T11:59:27.780097+00:00_

Web search results for query: "predictive multiplicity hybrid recurrent architectures SSM per-example divergence 2024 2025"

Links: [{"title":"Understanding the Skill Gap in Recurrent Language Models:","url":"https://arxiv.org/pdf/2504.18574v1"},{"title":"A Search Framework for Hybrid Neural Architecture Design","url":"https://arxiv.org/pdf/2510.00379"},{"title":"A Survey on Structured State Space Sequence (S4) Models","url":"https://arxiv.org/pdf/2503.18970"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2512.23824"},{"title":"Balancing Computation Load and Representation Expressivity in Parallel Hybrid Neural Networks","url":"https://arxiv.org/html/2505.19472v2"},{"title":"When to Think Fast and Slow? AMOR: Entropy-Based Metacognitive Gate for Dynamic SSM-Attention Switching","url":"https://arxiv.org/pdf/2602.13215"},{"title":"Some Attention is All You Need for Retrieval","url":"https://arxiv.org/pdf/2510.19861"}]

I found several relevant research papers and sources related to hybrid recurrent architectures and SSMs from 2024-2025. Here's what the search returned:

**Key Findings:**

Park et al. [2024] benchmarked Mamba and Transformer models across a range of in-context learning tasks, showing that SSMs underperform on tasks requiring non-standard retrieval, and proposed a hybrid architecture to address this limitation.

Recent hybrid models like Qwen3-Next (2025), Mamba-2 (2024), Jamba (2024) and MAD (2024) adjust the ratio of Transformer and State Space Model (SSM) primitives within a block.

Hybrid SSM-Transformer architectures combine linearly scaling state-space models with quadratically scaling attention mechanisms, promising efficient processing of long sequences without sacrificing performance.

AMOR is an architecture where an SSM processes each token, producing predictions and hidden states, and an entropy gate monitors prediction entropy to trigger sparse attention when confidence is low.

The search results incl
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6554
}
```

</details>

---


### Tool result

_source line 1016 · 2026-05-22T11:59:29.185401+00:00_

Web search results for query: "Garipov loss surface mode connectivity ensembling 2018"

Links: [{"title":"Loss Surface Simplexes for Mode Connecting Volumes and Fast Ensembling","url":"http://proceedings.mlr.press/v139/benton21a/benton21a.pdf"},{"title":"(PDF) Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs","url":"https://www.researchgate.net/publication/323444298_Loss_Surfaces_Mode_Connectivity_and_Fast_Ensembling_of_DNNs"},{"title":"Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs Timur Garipov∗1,2","url":"https://arxiv.org/pdf/1802.10026"},{"title":"GitHub - timgaripov/dnn-mode-connectivity: Mode Connectivity and Fast Geometric Ensembles in PyTorch · GitHub","url":"https://github.com/timgaripov/dnn-mode-connectivity"},{"title":"[PDF] Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Loss-Surfaces,-Mode-Connectivity,-and-Fast-of-DNNs-Garipov-Izmailov/f6195d8dc6aad8231e97b563246f2585842bc68b"},{"title":"Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs | Pavel's Blog","url":"https://izmailovpavel.github.io/curves_blogpost/"},{"title":"Using Mode Connectivity for Loss Landscape Analysis","url":"https://arxiv.org/pdf/1806.06977"},{"title":"Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs","url":"https://proceedings.neurips.cc/paper/2018/hash/be3087e74e9100d4bc4c6268cdbe8456-Abstract.html"}]

Based on the search results, here's what I found about the Garipov 2018 paper on loss surface mode connectivity and ensembling:

The paper is titled "Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs" by Timur Garipov, Pavel Izmailov, Dmitrii Podoprikhin, Dmitry P. Vetrov, and Andrew Gordon Wilson, published at the Advances in Neural Information Processing Systems conference in 2018.

**Main Contributions:**

The paper challenges the traditional view that deep neural network loss surfaces have multiple isolated local optima, instead showing
…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6830
}
```

</details>

---


### Tool result

_source line 1017 · 2026-05-22T11:59:30.038252+00:00_

Web search results for query: "Milani Fard prediction churn model instability 2016"

Links: [{"title":"Launch and Iterate: Reducing Prediction Churn","url":"https://proceedings.neurips.cc/paper/2016/hash/dc5c768b5dc76a084531934b34601977-Abstract.html"},{"title":"Launch and Iterate: Reducing Prediction Churn","url":"https://ai.google/research/pubs/pub46326/"},{"title":"Churn Prediction Model: How to Spot Risk Before It's Too Late","url":"https://www.june.so/blog/churn-prediction-model"},{"title":"Maintaining Stability and Plasticity for Predictive Churn Reduction","url":"https://arxiv.org/pdf/2305.04135"},{"title":"A Comprehensive Evaluation of Machine Learning and Deep Learning Models for Churn Prediction | MDPI","url":"https://www.mdpi.com/2078-2489/16/7/537"},{"title":"A Simplified and Numerically Stable Approach to the BG/NBD Churn   Prediction model","url":"https://arxiv.org/pdf/2502.12912"}]

Based on the search results, I found the relevant paper. Mahdi Milani Fard, along with Quentin Cormier, Kevin Canini, and Maya Gupta, published "Launch and Iterate: Reducing Prediction Churn" at NIPS 2016.

The paper addresses the problem of "prediction churn" — when changes in a new model's output result in predictions that change neutrally for many examples, creating unnecessary changes that are neither improvements nor regressions. These changes in predictions are problematic for usability in some applications and make it harder to measure if a change is statistically significant.

To address this, the authors formulated the problem and presented a stabilization operator to regularize a classifier towards a previous classifier, using a Markov chain Monte Carlo stabilization operator to produce a model with more consistent predictions without adversely affecting accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7733
}
```

</details>

---


### Tool call

_source line 1018 · 2026-05-22T11:59:43.442937+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 1019 · 2026-05-22T11:59:43.844539+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-22T12:01:32.293795+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Paper Summary\n\n本文研究 hybrid linear recurrent architectures（GatedDeltaNet, ReNet, HGRN2）中 attention ratio 对 cross-architecture agreement 的影响，分别在 aggregate 和 per-example 层面进行分析。使用 Wang et al. (2025) 的 30-configuration model zoo（3 架构 × 5 attention ratios × 2 scales），在 10 个 benchmarks 上发现：(1) aggregate cross-architecture variance 随 attention 增加而下降，但 per-example Jaccard overlap 在最低 attention level（4%）即饱和；(2) aggregate 评分相近的架构在 15–45% 的个体预测上存在分歧；(3) confidence-based routing 在 LAMBADA 上有效（~66% accuracy），但在其他 benchmark 上无改善。论文主张 aggregate metrics 不足以比较 hybrid recurrent architectures。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 扎实的实证分析，清晰展示了 aggregate convergence 与 per-example divergence 的解耦现象，但核心发现相对于已有 multiplicity 文献的增量贡献有限，且 single-seed 设计和 GDN confound 削弱了因果推断的说服力。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 统计方法论合理（permutation test, bootstrap CI, Bonferroni correction），但 single-seed 设计无法分离 seed noise 与 architecture effect；GDN confound 在 MMLU 上导致 aggregate convergence 结论反转（Appendix D） |\n| **Excitement** | 2.5/5 | Per-example Jaccard 在 4% attention 即饱和是有趣的经验发现，但 \"aggregate convergence masks per-example divergence\" 在 multiplicity/underspecification 文献中已是 well-established insight；routing 的实用价值仅限于 LAMBADA |\n| **Reproducibility** | 4/5 | 使用公开 model zoo，方法描述详尽，承诺 release code；但因 single seed 且未提供完整的 evaluation pipeline，第三方精确复现仍有门槛 |\n| **Reviewer Confidence** | 4/5 | 熟悉 multiplicity/underspecification 文献和 hybrid recurrent architecture 领域，仔细阅读了正文及全部 13 页 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：在已有框架上的应用而非方法论创新\n\n- 具体位置：Section 2 (page 3), 作者自述 \"The contribution lies not in the conceptual observation but in its quantitative characterization across architectures and task types\"\n- 问题：论文的核心分析工具（predictive multiplicity / Jaccard decomposition / confidence margin）全部来自已有文献（Marx et al., 2020; D'Amour et al., 2022; Black et al., 2022）。核心发现——\"aggregate 表现相近的模型在 per-example 层面可能大相径庭\"——在 underspecification 和 multiplicity 文献中已被充分建立。论文将这些工具应用于 hybrid recurrent architectures 是有价值的，但未引入新方法、新理论框架或产生违反直觉的发现。\n- 为什么影响接收：对于 main conference 而言，纯应用性的实证研究需要在 findings 的 surprise factor 或 practical impact 上有足够补偿。本文的 routing 应用仅在 LAMBADA 上有效（§4.2），practical impact 有限。\n- 建议修改方向：(a) 开发利用 per-example multiplicity 的新方法（如 architecture-aware routing algorithm, 或 multiplicity-informed ensemble strategy）并在多个 benchmark 上展示有效性；(b) 提供关于 *为什么* 4% attention 即饱和的 mechanistic explanation，而非仅报告现象；(c) 更清晰地 articulate 什么发现是 surprising 的（如果有的话）。\n\n**N2** [critical] Single-seed 设计无法分离 architectural effect 与 seed noise\n\n- 具体位置：Section 3.1 (page 3), Limitations (page 8)\n- 问题：每个 architecture-attention configuration 仅有单次训练，per-example variability 可能部分源于 seed-specific effects 而非 architectural differences。论文在 Limitations 中用 \"the 3× within vs. cross-architecture Jaccard gap (§4.2) provides proxy evidence\" 来辩护，但 Appendix W 的 Pythia 70M 对比存在严重局限：(a) Pythia 是 Transformer 而非 hybrid recurrent model；(b) 规模差异巨大（70M vs. 340M/1.3B）；(c) 仅一个对比点。这不足以排除 seed variation 也能产生 structured, architecture-correlated patterns 的可能。\n- 为什么影响接收：论文的核心 claim 是 \"backbone choice determines which examples are affected\"，但 single-seed 设计下这一 claim 的 causal validity 存疑。\n- 建议修改方向：对至少一个 architecture（如 GDN h3-1）训练 3–5 个 seeds，计算 within-seed vs. cross-architecture Jaccard，直接量化 seed noise 的贡献。即使只对一个 configuration 做此验证也能大幅增强说服力。\n\n**N3** [critical] GDN confound 严重削弱 aggregate convergence 的 generality\n\n- 具体位置：Appendix D (page 12, Table 3), §4.3 (page 8)\n- 问题：移除 GDN 后，MMLU 上的 Spearman ρ 从 −0.7 反转为 +0.6；LAMBADA 从 −1.0 削弱为 −0.7。主文 §4.3 仅轻描淡写地提及 LAMBADA 的变化，而 MMLU 的方向反转 buried 在 Appendix D。这意味着 aggregate convergence finding 在很大程度上由 GDN 的特殊行为驱动，而非三种架构的普遍规律。\n- 为什么影响接收：如果 aggregate convergence 仅在包含特定架构时成立，那么论文关于 \"attention increases aggregate convergence\" 的 general claim（Abstract, §1, §4.2）需要大幅 qualify。\n- 建议修改方向：在主文 §4.3 中明确讨论 MMLU 反转现象，将 aggregate convergence 重新定性为 \"architecture-dependent\" 而非 \"general trend\"。或者扩展架构集以测试 robustness。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 架构覆盖面不足，标题/表述过度泛化\n\n- 具体位置：Title, Abstract, Section 1\n- 问题：论文仅研究 3 种架构（GDN, ReNet, HGRN2），但标题 \"Hybrid Linear Recurrent Architectures\" 和 Abstract 中 \"adding attention to linear recurrent architectures\" 的表述暗示更广泛的 generality。Mamba/Mamba-2, RWKV-v6, Jamba 等重要 hybrid architectures 均未涉及（Limitations 承认），且这些架构使用不同的 recurrence mechanism（selective scan vs. gated delta rule vs. exponential decay），per-example multiplicity pattern 可能不同。\n- 建议：标题改为更精确的表述（如 \"...in Three Hybrid Linear Recurrent Architectures\" 或 \"...in Gated Linear Recurrent Models\"），并在 Abstract/Introduction 中更明确地限定 scope。\n\n**W2** [warning] Overclaiming：因果语言用于相关性证据\n\n- 具体位置：Abstract (page 1), Section 1 (page 1-2)\n- 问题：多处使用暗示因果关系的措辞描述相关性发现：\n  - Abstract: \"adding attention...is associated with per-example changes on almost entirely different examples across backbones\" — \"almost entirely different\" 过度概括了 ~10% pairwise Jaccard overlap\n  - §1: \"the choice of backbone is associated with which specific inputs a deployed system handles correctly\" — 从 3 种架构的 correlational evidence 推向 deployment 建议\n  - Abstract: \"configurations interchangeable by aggregate metrics carry hidden consequences for per-example reliability\" — 暗示 practical warning，但 routing 仅在 LAMBADA 有效\n- 建议：使用更审慎的 hedging（\"in our three studied architectures\", \"under the configurations we evaluated\"），明确区分 observation 和 causal claim。\n\n**W3** [warning] Confidence-based routing 分析深度不足\n\n- 具体位置：§4.2 (pages 5-6)\n- 问题：Routing 在 LAMBADA 上 66% accuracy（50/50 split）但在 HellaSwag 和 PIQA 上无改善。论文将此归因于 multiplicity 程度差异，但未深入分析 *为什么* LAMBADA 特殊——是 task structure（long-range retrieval）还是 multiplicity magnitude 的阈值效应？此外，10-repeat cross-validated splits 的方法细节不足（如何划分 train/test，使用什么 features）。\n- 建议：补充 routing failure 的分析，讨论 task properties 与 routing effectiveness 的关系。\n\n**W4** [warning] Related Work 中与 prediction churn 文献的联系缺失\n\n- 具体位置：Section 2 (page 3)\n- 问题：Milani Fard et al. (2016) \"Launch and Iterate: Reducing Prediction Churn\" 直接研究了 model update 时 per-example prediction 的不稳定性，与本文的 per-example divergence across architectures 在 framing 上高度相关。论文未引用此工作。此外，Garipov et al. (2018) \"Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs\" 关于 loss landscape connectivity 的发现可为 per-example agreement patterns 提供 theoretical grounding（architecturally similar models 可能 share mode connectivity，从而解释 higher per-example overlap）。\n- 建议：在 Related Work 中增加 prediction churn 和 mode connectivity 的讨论，clarify 本文贡献相对于这些 perspectives 的定位。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 过于密集**: 200+ 词的 abstract 中塞入了过多具体数字（σ = 0.14–0.30, p < .100, 10% 等），首次阅读难以抓住 key message。建议精简数字，突出 narrative。\n- **Table 1 (page 6) 难以解析**: 7 列 + 多个脚注 + 上标注释，信息量大但 readability 差。考虑拆分为两个 table 或使用 heatmap visualization。\n- **Appendix 与正文比例失衡**: 13 页 appendix 对应 8 页正文（Appendix A–W），部分关键证据（如 GDN confound, seed comparison）被 relegated 到 appendix 中。如果这些分析对 core claims 至关重要，应在正文中更充分讨论。\n- **§3.3 convergence ratio σ_pure/σ_h3-1 定义 (page 4)**: 简洁但首次阅读时容易混淆——\"values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance\" 需要 reader pause to verify。考虑用更直觉的命名。\n- **Figure 1(b)**: Y 轴标签 \"Pairwise Jaccard similarity\" 但 caption 说 \"per-example overlap\"——terminology 应统一。\n\n---\n\n## 主要优势\n\n- **S1**: 问题意识好——随着 hybrid recurrent architectures 快速增殖，理解其 per-example behavior 差异对 deployment 有实际意义。\n- **S2**: 统计方法论严谨——permutation tests, bootstrap CIs, Bonferroni correction 的使用恰当，并坦诚承认各方法的局限（如 n=5 ordinal levels 的低 power, §3.5）。\n- **S3**: 核心发现展示清晰——Figure 1 有效传达了 aggregate convergence vs. per-example saturation 的 decoupling；该现象在 4 个主要 benchmark 上一致。\n- **S4**: Helped/hurt/unchanged 分解（§3.4）和 confidence margin 分析（§4.2, Appendix P-Q）为理解 architecture-specific effects 提供了 structured framework。\n- **S5**: 学术诚信——主动进行 GDN exclusion sensitivity analysis（Appendix D）、seed comparison（Appendix W）、confound discussion（Appendix E），展示了 intellectual honesty。\n- **S6**: Appendix 极为详尽（A–W），为 main text 的每个 claim 提供了补充证据。\n\n---\n\n## Questions to Authors\n\n**Q1**: 是否考虑过对至少一个 configuration 训练多个 seeds 以直接量化 seed vs. architecture 对 per-example variability 的贡献？即使 2-3 seeds 也能大幅增强 causal claim。\n\n**Q2**: Appendix E 指出 GDN b3-1 使用 16 attention heads（其他 hybrid 用 32）。您多大程度上确信观察到的 effects 不受此 head count confound 驱动？\n\n**Q3**: Per-example Jaccard 在 4% attention 即饱和是本文最 striking 的发现。能否提供 mechanistic intuition？是否 any attention 即触发 divergence，而 more attention 不增加 architectural distinctiveness？\n\n**Q4**: Routing 仅在 LAMBADA 有效——这是否暗示 per-example multiplicity 的 practical exploitation 本质上受限于高 multiplicity 场景？如果是，该如何向 practitioners 传达这一发现的应用范围？\n\n---\n\n## Missing References\n\n- Milani Fard, M., Cormier, Q., Canini, K., & Gupta, M. (2016). Launch and Iterate: Reducing Prediction Churn. NeurIPS 2016. — 直接研究 per-example prediction instability across model variants。\n- Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D., & Wilson, A.G. (2018). Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs. NeurIPS 2018. — Mode connectivity 可为 architecturally similar models 的 per-example overlap patterns 提供 theoretical grounding。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 ≤ 8 | ✅ | 正文结束于第 8 页（Limitations + Conclusion） |\n| ACL 模板 | ✅ | 双栏 ACL 格式，\"Anonymous ACL submission\" header |\n| Double-blind 匿名 | ✅ | 未发现 de-anonymization 线索；使用公开 model zoo，code \"released upon publication\" |\n| 参考文献格式 | ✅ | 标准 natbib/ACL 格式，pages 9-10 |\n| Limitations 章节 | ✅ | Page 8，覆盖 3 个主要 limitation，篇幅适当 |\n| Ethics Statement | ✅ | Page 9，声明无 human subjects / 新数据收集 |\n",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — Round 1 审稿意见\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## Paper Summary\n\n本文研究 hybrid linear recurrent architectures（GatedDeltaNet, ReNet, HGRN2）中 attention ratio 对 cross-architecture agreement 的影响，分别在 aggregate 和 per-example 层面进行分析。使用 Wang et al. (2025) 的 30-configuration model zoo（3 架构 × 5 attention ratios × 2 scales），在 10 个 benchmarks 上发现：(1) aggregate cross-architecture variance 随 attention 增加而下降，但 per-example Jaccard overlap 在最低 attention level（4%）即饱和；(2) aggregate 评分相近的架构在 15–45% 的个体预测上存在分歧；(3) confidence-based routing 在 LAMBADA 上有效（~66% accuracy），但在其他 benchmark 上无改善。论文主张 aggregate metrics 不足以比较 hybrid recurrent architectures。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 — Findings\n**一句话总结**: 扎实的实证分析，清晰展示了 aggregate convergence 与 per-example divergence 的解耦现象，但核心发现相对于已有 multiplicity 文献的增量贡献有限，且 single-seed 设计和 GDN confound 削弱了因果推断的说服力。\n\n---\n\n## 官方维度打分（ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 统计方法论合理（permutation test, bootstrap CI, Bonferroni correction），但 single-seed 设计无法分离 seed noise 与 architecture effect；GDN confound 在 MMLU 上导致 aggregate convergence 结论反转（Appendix D） |\n| **Excitement** | 2.5/5 | Per-example Jaccard 在 4% attention 即饱和是有趣的经验发现，但 \"aggregate convergence masks per-example divergence\" 在 multiplicity/underspecification 文献中已是 well-established insight；routing 的实用价值仅限于 LAMBADA |\n| **Reproducibility** | 4/5 | 使用公开 model zoo，方法描述详尽，承诺 release code；但因 single seed 且未提供完整的 evaluation pipeline，第三方精确复现仍有门槛 |\n| **Reviewer Confidence** | 4/5 | 熟悉 multiplicity/underspecification 文献和 hybrid recurrent architecture 领域，仔细阅读了正文及全部 13 页 appendix |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：在已有框架上的应用而非方法论创新\n\n- 具体位置：Section 2 (page 3), 作者自述 \"The contribution lies not in the conceptual observation but in its quantitative characterization across architectures and task types\"\n- 问题：论文的核心分析工具（predictive multiplicity / Jaccard decomposition / confidence margin）全部来自已有文献（Marx et al., 2020; D'Amour et al., 2022; Black et al., 2022）。核心发现——\"aggregate 表现相近的模型在 per-example 层面可能大相径庭\"——在 underspecification 和 multiplicity 文献中已被充分建立。论文将这些工具应用于 hybrid recurrent architectures 是有价值的，但未引入新方法、新理论框架或产生违反直觉的发现。\n- 为什么影响接收：对于 main conference 而言，纯应用性的实证研究需要在 findings 的 surprise factor 或 practical impact 上有足够补偿。本文的 routing 应用仅在 LAMBADA 上有效（§4.2），practical impact 有限。\n- 建议修改方向：(a) 开发利用 per-example multiplicity 的新方法（如 architecture-aware routing algorithm, 或 multiplicity-informed ensemble strategy）并在多个 benchmark 上展示有效性；(b) 提供关于 *为什么* 4% attention 即饱和的 mechanistic explanation，而非仅报告现象；(c) 更清晰地 articulate 什么发现是 surprising 的（如果有的话）。\n\n**N2** [critical] Single-seed 设计无法分离 architectural effect 与 seed noise\n\n- 具体位置：Section 3.1 (page 3), Limitations (page 8)\n- 问题：每个 architecture-attention configuration 仅有单次训练，per-example variability 可能部分源于 seed-specific effects 而非 architectural differences。论文在 Limitations 中用 \"the 3× within vs. cross-architecture Jaccard gap (§4.2) provides proxy evidence\" 来辩护，但 Appendix W 的 Pythia 70M 对比存在严重局限：(a) Pythia 是 Transformer 而非 hybrid recurrent model；(b) 规模差异巨大（70M vs. 340M/1.3B）；(c) 仅一个对比点。这不足以排除 seed variation 也能产生 structured, architecture-correlated patterns 的可能。\n- 为什么影响接收：论文的核心 claim 是 \"backbone choice determines which examples are affected\"，但 single-seed 设计下这一 claim 的 causal validity 存疑。\n- 建议修改方向：对至少一个 architecture（如 GDN h3-1）训练 3–5 个 seeds，计算 within-seed vs. cross-architecture Jaccard，直接量化 seed noise 的贡献。即使只对一个 configuration 做此验证也能大幅增强说服力。\n\n**N3** [critical] GDN confound 严重削弱 aggregate convergence 的 generality\n\n- 具体位置：Appendix D (page 12, Table 3), §4.3 (page 8)\n- 问题：移除 GDN 后，MMLU 上的 Spearman ρ 从 −0.7 反转为 +0.6；LAMBADA 从 −1.0 削弱为 −0.7。主文 §4.3 仅轻描淡写地提及 LAMBADA 的变化，而 MMLU 的方向反转 buried 在 Appendix D。这意味着 aggregate convergence finding 在很大程度上由 GDN 的特殊行为驱动，而非三种架构的普遍规律。\n- 为什么影响接收：如果 aggregate convergence 仅在包含特定架构时成立，那么论文关于 \"attention increases aggregate convergence\" 的 general claim（Abstract, §1, §4.2）需要大幅 qualify。\n- 建议修改方向：在主文 §4.3 中明确讨论 MMLU 反转现象，将 aggregate convergence 重新定性为 \"architecture-dependent\" 而非 \"general trend\"。或者扩展架构集以测试 robustness。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 架构覆盖面不足，标题/表述过度泛化\n\n- 具体位置：Title, Abstract, Section 1\n- 问题：论文仅研究 3 种架构（GDN, ReNet, HGRN2），但标题 \"Hybrid Linear Recurrent Architectures\" 和 Abstract 中 \"adding attention to linear recurrent architectures\" 的表述暗示更广泛的 generality。Mamba/Mamba-2, RWKV-v6, Jamba 等重要 hybrid architectures 均未涉及（Limitations 承认），且这些架构使用不同的 recurrence mechanism（selective scan vs. gated delta rule vs. exponential decay），per-example multiplicity pattern 可能不同。\n- 建议：标题改为更精确的表述（如 \"...in Three Hybrid Linear Recurrent Architectures\" 或 \"...in Gated Linear Recurrent Models\"），并在 Abstract/Introduction 中更明确地限定 scope。\n\n**W2** [warning] Overclaiming：因果语言用于相关性证据\n\n- 具体位置：Abstract (page 1), Section 1 (page 1-2)\n- 问题：多处使用暗示因果关系的措辞描述相关性发现：\n  - Abstract: \"adding attention...is associated with per-example changes on almost entirely different examples across backbones\" — \"almost entirely different\" 过度概括了 ~10% pairwise Jaccard overlap\n  - §1: \"the choice of backbone is associated with which specific inputs a deployed system handles correctly\" — 从 3 种架构的 correlational evidence 推向 deployment 建议\n  - Abstract: \"configurations interchangeable by aggregate metrics carry hidden consequences for per-example reliability\" — 暗示 practical warning，但 routing 仅在 LAMBADA 有效\n- 建议：使用更审慎的 hedging（\"in our three studied architectures\", \"under the configurations we evaluated\"），明确区分 observation 和 causal claim。\n\n**W3** [warning] Confidence-based routing 分析深度不足\n\n- 具体位置：§4.2 (pages 5-6)\n- 问题：Routing 在 LAMBADA 上 66% accuracy（50/50 split）但在 HellaSwag 和 PIQA 上无改善。论文将此归因于 multiplicity 程度差异，但未深入分析 *为什么* LAMBADA 特殊——是 task structure（long-range retrieval）还是 multiplicity magnitude 的阈值效应？此外，10-repeat cross-validated splits 的方法细节不足（如何划分 train/test，使用什么 features）。\n- 建议：补充 routing failure 的分析，讨论 task properties 与 routing effectiveness 的关系。\n\n**W4** [warning] Related Work 中与 prediction churn 文献的联系缺失\n\n- 具体位置：Section 2 (page 3)\n- 问题：Milani Fard et al. (2016) \"Launch and Iterate: Reducing Prediction Churn\" 直接研究了 model update 时 per-example prediction 的不稳定性，与本文的 per-example divergence across architectures 在 framing 上高度相关。论文未引用此工作。此外，Garipov et al. (2018) \"Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs\" 关于 loss landscape connectivity 的发现可为 per-example agreement patterns 提供 theoretical grounding（architecturally similar models 可能 share mode connectivity，从而解释 higher per-example overlap）。\n- 建议：在 Related Work 中增加 prediction churn 和 mode connectivity 的讨论，clarify 本文贡献相对于这些 perspectives 的定位。\n\n---\n\n## 小问题（不影响接收）\n\n- **Abstract 过于密集**: 200+ 词的 abstract 中塞入了过多具体数字（σ = 0.14–0.30, p < .100, 10% 等），首次阅读难以抓住 key message。建议精简数字，突出 narrative。\n- **Table 1 (page 6) 难以解析**: 7 列 + 多个脚注 + 上标注释，信息量大但 readability 差。考虑拆分为两个 table 或使用 heatmap visualization。\n- **Appendix 与正文比例失衡**: 13 页 appendix 对应 8 页正文（Appendix A–W），部分关键证据（如 GDN confound, seed comparison）被 relegated 到 appendix 中。如果这些分析对 core claims 至关重要，应在正文中更充分讨论。\n- **§3.3 convergence ratio σ_pure/σ_h3-1 定义 (page 4)**: 简洁但首次阅读时容易混淆——\"values greater than 1 indicate that higher attention ratios are associated with lower cross-architecture variance\" 需要 reader pause to verify。考虑用更直觉的命名。\n- **Figure 1(b)**: Y 轴标签 \"Pairwise Jaccard similarity\" 但 caption 说 \"per-example overlap\"——terminology 应统一。\n\n---\n\n## 主要优势\n\n- **S1**: 问题意识好——随着 hybrid recurrent architectures 快速增殖，理解其 per-example behavior 差异对 deployment 有实际意义。\n- **S2**: 统计方法论严谨——permutation tests, bootstrap CIs, Bonferroni correction 的使用恰当，并坦诚承认各方法的局限（如 n=5 ordinal levels 的低 power, §3.5）。\n- **S3**: 核心发现展示清晰——Figure 1 有效传达了 aggregate convergence vs. per-example saturation 的 decoupling；该现象在 4 个主要 benchmark 上一致。\n- **S4**: Helped/hurt/unchanged 分解（§3.4）和 confidence margin 分析（§4.2, Appendix P-Q）为理解 architecture-specific effects 提供了 structured framework。\n- **S5**: 学术诚信——主动进行 GDN exclusion sensitivity analysis（Appendix D）、seed comparison（Appendix W）、confound discussion（Appendix E），展示了 intellectual honesty。\n- **S6**: Appendix 极为详尽（A–W），为 main text 的每个 claim 提供了补充证据。\n\n---\n\n## Questions to Authors\n\n**Q1**: 是否考虑过对至少一个 configuration 训练多个 seeds 以直接量化 seed vs. architecture 对 per-example variability 的贡献？即使 2-3 seeds 也能大幅增强 causal claim。\n\n**Q2**: Appendix E 指出 GDN b3-1 使用 16 attention heads（其他 hybrid 用 32）。您多大程度上确信观察到的 effects 不受此 head count confound 驱动？\n\n**Q3**: Per-example Jaccard 在 4% attention 即饱和是本文最 striking 的发现。能否提供 mechanistic intuition？是否 any attention 即触发 divergence，而 more attention 不增加 architectural distinctiveness？\n\n**Q4**: Routing 仅在 LAMBADA 有效——这是否暗示 per-example multiplicity 的 practical exploitation 本质上受限于高 multiplicity 场景？如果是，该如何向 practitioners 传达这一发现的应用范围？\n\n---\n\n## Missing References\n\n- Milani Fard, M., Cormier, Q., Canini, K., & Gupta, M. (2016). Launch and Iterate: Reducing Prediction Churn. NeurIPS 2016. — 直接研究 per-example prediction instability across model variants。\n- Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D., & Wilson, A.G. (2018). Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs. NeurIPS 2018. — Mode connectivity 可为 architecturally similar models 的 per-example overlap patterns 提供 theoretical grounding。\n\n---\n\n## 格式合规检查\n\n| 项目 | 状态 | 备注 |\n|------|------|------|\n| 正文页数 ≤ 8 | ✅ | 正文结束于第 8 页（Limitations + Conclusion） |\n| ACL 模板 | ✅ | 双栏 ACL 格式，\"Anonymous ACL submission\" header |\n| Double-blind 匿名 | ✅ | 未发现 de-anonymization 线索；使用公开 model zoo，code \"released upon publication\" |\n| 参考文献格式 | ✅ | 标准 natbib/ACL 格式，pages 9-10 |\n| Limitations 章节 | ✅ | Page 8，覆盖 3 个主要 limitation，篇幅适当 |\n| Ethics Statement | ✅ | Page 9，声明无 human subjects / 新数据收集 |\n",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool call

_source line 1021 · 2026-05-22T12:01:33.599298+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_14/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1022 · 2026-05-22T12:01:36.159548+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Tool result

_source line 1023 · 2026-05-22T12:01:36.160002+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 2560
}
```

</details>

---


### Assistant

_source line 1024 · 2026-05-22T12:01:43.694208+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0（Findings level）。

三个 critical 问题：
1. **新颖性不足** — 将已有 multiplicity 框架应用于新模型族，无方法论创新，practical routing 仅 LAMBADA 有效
2. **Single-seed 设计** — 无法分离 seed noise 与 architectural effect，核心因果 claim 存疑
3. **GDN confound** — 移除 GDN 后 MMLU aggregate convergence 方向反转（ρ: −0.7 → +0.6），被 buried 在 Appendix D

主要优势：统计方法严谨、核心 decoupling 现象展示清晰、appendix 极为详尽。格式完全合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 25

## Round 25

4 recorded events


### User

_source line 1025 · 2026-05-22T12:02:55.122463+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.0 — Findings

### Must-Fix 问题

**R1-N1** [Critical] Single training run 根本性地限制了因果推断
- 每个 configuration 仅一次训练运行。无法区分 architecture effect 与 seed effect。Pythia 70M PolyPythias 对比存在三重不匹配（scale, architecture family, accuracy regime）。Within-architecture Jaccard (~0.33) vs cross-architecture Jaccard (~0.10) 的 3× gap 比较的是不同维度（同一架构不同 attention ratio vs 不同架构），不是直接的 seed vs architecture 对比。

**R1-N2** [Critical] Aggregate convergence 的证据不足以支撑其在论文中的权重
- LAMBADA Bonferroni-adjusted p = .100 未达 conventional significance；9/10 benchmarks 无显著 convergence；仅 1.3B 观察到，340M 不存在；依赖 GDN 包含。但 Abstract 和 Introduction 将 convergence 作为核心叙事。建议重新聚焦到 per-example multiplicity 本身。

### Should-Fix 问题

**R1-W1** [Major] GDN attention head confound 对结果的影响被低估
- GDN h3-1 使用 16 heads vs 其他配置 32 heads。排除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7，MMLU 从 -0.7 反转至 +0.6。Table 1 主要呈现仍包含 GDN。

**R1-W2** [Major] n=5 attention ratios 使 permutation test 本质上是 binary outcome
- 只有 ρ = ±1.0 能达到 p < .05。Table 1 中 9 个 non-significant ρ 不能被解释为 "no convergence"，只能说 "no power"。

**R1-W3** [Major] Bootstrap CI (n=3) 不应被赋予高权重
- Resampling space 极其有限，11.25% degenerate resamples。Introduction 中 "the heuristic BCa 95% CI excludes zero" 给读者过强的统计保证。

**R1-W4** [Major] Confidence margin mechanism 的因果推断过度
- "Confidence margin mechanism" 标题暗示因果性，但证据是 correlational。ECE 是粗粒度度量，可能无法捕捉 threshold 附近的 fine-grained calibration 差异。

**R1-W5** [Minor] 3 architectures 覆盖度有限
- 仅 GDN/RetNet/HGRN2，Mamba/RWKV-6 未涵盖。标题泛称 "Hybrid Linear Recurrent Architectures"。

**R1-W6** [Minor] Routing 分析的实践意义有限
- 仅 LAMBADA 有效，HellaSwag/PIQA 无改进。

### Questions
Q1: 能否获取 model zoo 的多 seed 权重？
Q2: GDN 16 heads 是否有 architectural motivation？
Q3: 为何 per-example decomposition 仅在 4/10 benchmark 上？BoolQ/WinoGrande 的 mixed significance 是否削弱 generality？
Q4: Greedy decoding 下的结果是否在 sampling decoding 下持续？
Q5: Within-architecture Jaccard (~0.33) 是否因 structural overlap 而被 inflate，从而夸大 3× gap？

### Missing References
- Poli et al. (2023) "Hyena Hierarchy"
- Jelassi et al. (2024) attention 与 in-context learning in hybrid models

---

请对以上每个编号观点（R1-N1, R1-N2, R1-W1, R1-W2, R1-W3, R1-W4, R1-W5, R1-W6, Q1-Q5）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1026 · 2026-05-22T12:04:59.034115+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: Single training run 根本性地限制了因果推断**\n\n完全同意，这也是我独立审查中的 N2。R1 的分析比我更精准地指出了 3× gap 的论证缺陷：within-architecture Jaccard (~0.33) 比较的是同一架构不同 attention ratios，cross-architecture Jaccard (~0.10) 比较的是不同架构——这两个维度不可直接比较，不构成 seed vs. architecture 的对照。\n\nR1 对 Pythia 70M PolyPythias 对比的三重不匹配（scale: 70M vs. 340M/1.3B; architecture family: Transformer vs. hybrid recurrent; accuracy regime）总结到位。我在 Appendix W (page 21) 中注意到作者自己也承认 \"These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects\"，但主文 Limitations (page 8) 的措辞对此 caveat 的传达不够充分。\n\n补充一点：即使 3× gap 在数值上看起来 substantial，seed variation 也可能产生 structured patterns（不同 seed 可能系统性地影响不同 difficulty levels 的 examples），因此 gap 的 magnitude 本身不能排除 seed confound。\n\n**[AGREE with nuance] R1-N2: Aggregate convergence 的证据不足以支撑其在论文中的权重**\n\n大方向同意 R1 的判断——aggregate convergence 的证据确实薄弱：\n- LAMBADA Bonferroni-adjusted p = .100 未达 conventional α = .05（§3.5, page 5 确认 \"the text has no power to detect strong but imperfect monotonic trends\"）\n- 9/10 benchmarks 无显著 convergence（Table 1, page 6）\n- 仅 1.3B scale 观察到（§4.2, page 7: \"convergence is absent at 340M\"）\n- 依赖 GDN 包含（Appendix D, Table 3: MMLU ρ 反转）\n\n但我想补充一个 nuance：aggregate convergence 在论文叙事中的作用不仅是一个独立 claim，更是 per-example divergence 的 **对照背景**。论文的核心 insight 是 decoupling——\"aggregate converges but per-example diverges\"。如果完全删除 aggregate convergence，per-example multiplicity 的发现就缺少了 \"despite apparent similarity\" 这个 framing，影响力会下降。\n\n建议方案：不是彻底删除 aggregate convergence 叙事，而是 (a) 将其从 \"core finding\" 降级为 \"motivating observation\"；(b) 在 Abstract 和 Introduction 中用更审慎的语言（\"on the one benchmark showing marginal aggregate convergence\" 而非暗示 general trend）；(c) 明确说明 LAMBADA 的特殊性。这比 R1 建议的 \"重新聚焦\" 更可行，因为完全放弃 aggregate 叙事会改变论文的核心架构。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: GDN attention head confound 对结果的影响被低估**\n\n完全同意。我在 N3 中独立 flagged 了同一问题。GDN h3-1 使用 16 heads（Appendix E, page 13）而其他 hybrid 使用 32 heads，这不仅仅是一个 \"confound to note\" 而是一个 **systematic architectural difference**，可能驱动了 GDN 在 Table 1 中表现出的 distinctive pattern（如 LAMBADA 上 GDN 是唯一 ρ = -1.0 的架构）。\n\n关键证据：Appendix D Table 3 (page 12) 显示排除 GDN 后：\n- LAMBADA: ρ 从 -1.0 降至 -0.7（方向不变但幅度减半）\n- MMLU: ρ 从 -0.7 **反转**至 +0.6（方向完全反转）\n\nMMLU 的方向反转尤其值得关注——这意味着在 ReNet 和 HGRN2 之间，更多 attention 实际上 *增加* 而非减少 MMLU 上的 cross-architecture divergence。主文 §4.3 (page 8) 未提及此反转。\n\n**[AGREE] R1-W2: n=5 permutation test 本质上是 binary outcome**\n\n同意。这是一个重要的方法论观察。120 permutations（5!）中，只有 ρ = ±1.0 能达到 p = 1/120 ≈ .008 < .05。任何非完美单调关系都无法 reject null。因此 Table 1 (page 6) 中的 9 个 non-significant results 不能区分 \"no effect\" 和 \"moderate effect with insufficient power\"。\n\n论文在 §3.5 (page 5) 确实承认了这一点（\"a single rank swap suffices to shift the verdict from significant to non-significant\"），但 Table 1 的呈现方式——bolding only significant ρ——仍可能给读者 \"9 benchmarks show no convergence\" 的错误印象。\n\n建议：Table 1 应增加注释明确说明 non-significant ρ 的 interpretation ambiguity，或报告 effect size（如 ρ 本身）而非仅依赖 p-value。\n\n**[AGREE] R1-W3: Bootstrap CI (n=3) 不应被赋予高权重**\n\n同意。3 architectures 的 bootstrap resampling space 极其有限（3³ = 27 unique resamples，其中 3 个 degenerate = 11.1%，与 R1 的 11.25% 估计一致）。BCa correction 在如此小的 resampling space 上不可靠。\n\n论文在 Appendix B (page 12) 确实承认 resampling space 受限，并用 percentile CI 替代 full BCa，这是合理的 downgrade。但 Introduction (page 2) 中 \"the heuristic BCa 95% CI excludes zero\" 的表述确实给读者过强的统计保证，因为 95% CI 在 n=3 bootstrap 中的 coverage probability 远低于 nominal 95%。\n\n建议与 R1 一致：主文中对 bootstrap CI 的引用应加 caveat，或改为报告 percentile CI 并注明其 exploratory nature。\n\n**[REBUT with partial agreement] R1-W4: Confidence margin mechanism 的因果推断过度**\n\n部分同意 R1 的 \"mechanism\" 命名问题，但认为 R1 低估了论文提供的证据层次。\n\n同意的部分：§4.2 中将 confidence margin 分析称为 \"mechanism\" 确实暗示了因果性，而证据本质上是 correlational。标题措辞应改为 \"Confidence margin pattern\" 或 \"Confidence margin analysis\"。\n\n反驳的部分：R1 说 \"ECE 是粗粒度度量\"——但论文的 confidence margin 分析并不仅依赖 ECE。核心证据来自 per-example level 的 target-token probability 分析：\n- Appendix P Table 18 (page 17): Pure-correct hurt samples 的 |log p| 显著高于 stayed-right（即 lower target-token probability），across all three architectures\n- Appendix P Table 19 (page 17): Pure-wrong helped samples 的 |log p| 显著低于 stayed-wrong（即 higher target-token probability）\n- 这是 per-example 粒度的分析，比 ECE 精细得多\n\nECE 分析（Appendix Q, page 18）是 *补充* 证据，用于排除 calibration difference 作为 alternative explanation。论文在 page 6 说 \"calibration differences are insufficient to account for the observed threshold divergence\"——这是在排除 confound，不是核心证据。\n\n因此，我认为 \"mechanism\" 一词需改为更中性的表述，但 R1 对证据质量的批评过重。\n\n**[AGREE] R1-W5: 3 architectures 覆盖度有限**\n\n同意，与我的 W1 一致。标题应更精确地反映实际研究的架构范围。\n\n**[AGREE] R1-W6: Routing 分析的实践意义有限**\n\n同意，与我的 W5 一致。LAMBADA 上 66% accuracy（§4.2, page 6）虽高于 random，但 HellaSwag/PIQA 上无改善表明 routing 的适用条件很窄。\n\n---\n\n## Questions\n\n**[AGREE] Q1: 能否获取 model zoo 的多 seed 权重？**\n\n合理的问题。Wang et al. (2025) 的 model zoo 仅提供 single runs，获取多 seed 需要 retrain。但即使 retrain 一个 configuration 的 3-5 seeds 也能显著增强论文说服力。这与我的 Q1 一致。\n\n**[AGREE] Q2: GDN 16 heads 的 architectural motivation**\n\n与我的 Q2 一致。Appendix E (page 13) 解释这是原始 model zoo 的 design choice 而非 error，但这意味着 GDN 的 per-head capacity 与其他架构不同，可能系统性地影响 attention pattern 和 per-example behavior。\n\n**[REBUT] Q3: Per-example decomposition 仅在 4/10 benchmarks 上是否削弱 generality**\n\nR1 对此的 concern 有一定道理，但论文的处理比 R1 暗示的更完整：\n- 4 个主要 benchmarks（LAMBADA, HellaSwag, PIQA, ARC-Easy）覆盖了全部 4 个 task categories（retrieval, comprehension, reasoning, mixed）——这是 deliberate 的 category-representative sampling，不是 cherry-picking（§3.2, page 3-4, 引用 Arora et al. 2024a）\n- BoolQ 作为 supplementary benchmark 在 Appendix R (page 18) 有分析；WinoGrande 在 Appendix S (page 19)\n- §4.1 (page 5) 报告了 *全部* 10 benchmarks 的 aggregate results（Table 1）\n\nBoolQ/WinoGrande 的 mixed significance 确实值得讨论，但不一定削弱 generality——它可能反映 task-specific differences，这本身是论文的一个发现（multiplicity magnitude is task-dependent）。\n\n**[AGREE] Q4: Greedy decoding 下结果是否在 sampling 下持续**\n\n合理的 concern。Greedy decoding 产生 deterministic outputs，per-example effects 在 sampling decoding 下可能被 stochasticity 稀释。不过，大多数 NLP benchmarks 的 standard evaluation 使用 greedy/argmax decoding，且论文使用 lm-evaluation-harness (§3.2, page 4) 的 default 设置。这更多是一个 scope limitation 而非 flaw。\n\n**[REBUT with partial agreement] Q5: Within-architecture Jaccard (~0.33) 是否被 structural overlap inflate**\n\nR1 的 concern 有道理——同一架构的不同 attention ratios 共享 recurrence mechanism，可能因此有更高的 per-example overlap。但这种 \"structural overlap\" 恰恰是论文的分析对象之一：论文在 §4.1 (page 5) 中说 \"Within each benchmark, σ is stable across attention ratios (variation < 0.033)\"，Figure 1(b) 显示 Jaccard 在不同 attention ratios 间变化不大。\n\n更重要的是，3× gap 不是论文的 core claim——论文的核心发现是 *per-example Jaccard saturation at 4% attention despite aggregate convergence*（Figure 1, §4.1），这一发现不依赖 within- vs cross-architecture 的对比。即使 3× gap 被 inflate，per-example saturation 仍然成立。\n\n但我同意 R1 的隐含建议：论文应明确讨论 structural overlap 对 within-architecture Jaccard 的可能影响，而非将 3× gap 作为 seed vs. architecture 的间接证据。\n\n---\n\n## Missing References\n\n**[REBUT] Poli et al. (2023) \"Hyena Hierarchy\"**\n\nHyena 不是 gated linear recurrence 架构（它基于 long convolution），与论文研究的 GDN/ReNet/HGRN2 family 有本质区别。论文的 scope 是 \"hybrid linear recurrent architectures\"，Hyena 不属于此类别。除非论文扩展到更广泛的 efficient architecture 比较，否则不引用 Hyena 是合理的。\n\n**[AGREE] Jelassi et al. (2024) attention 与 in-context learning in hybrid models**\n\n同意这是一个相关 reference。Jelassi et al. 研究 attention 在 hybrid models 中对 in-context learning 的作用，与本文关于 attention ratio 影响 per-example behavior 的分析在 motivation 上有交叉。应在 Related Work §2 中讨论。\n",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 — 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R1-N1: Single training run 根本性地限制了因果推断**\n\n完全同意，这也是我独立审查中的 N2。R1 的分析比我更精准地指出了 3× gap 的论证缺陷：within-architecture Jaccard (~0.33) 比较的是同一架构不同 attention ratios，cross-architecture Jaccard (~0.10) 比较的是不同架构——这两个维度不可直接比较，不构成 seed vs. architecture 的对照。\n\nR1 对 Pythia 70M PolyPythias 对比的三重不匹配（scale: 70M vs. 340M/1.3B; architecture family: Transformer vs. hybrid recurrent; accuracy regime）总结到位。我在 Appendix W (page 21) 中注意到作者自己也承认 \"These limitations restrict the comparison to a reference point for seed-variation magnitude rather than definitive evidence for architecture-driven effects\"，但主文 Limitations (page 8) 的措辞对此 caveat 的传达不够充分。\n\n补充一点：即使 3× gap 在数值上看起来 substantial，seed variation 也可能产生 structured patterns（不同 seed 可能系统性地影响不同 difficulty levels 的 examples），因此 gap 的 magnitude 本身不能排除 seed confound。\n\n**[AGREE with nuance] R1-N2: Aggregate convergence 的证据不足以支撑其在论文中的权重**\n\n大方向同意 R1 的判断——aggregate convergence 的证据确实薄弱：\n- LAMBADA Bonferroni-adjusted p = .100 未达 conventional α = .05（§3.5, page 5 确认 \"the text has no power to detect strong but imperfect monotonic trends\"）\n- 9/10 benchmarks 无显著 convergence（Table 1, page 6）\n- 仅 1.3B scale 观察到（§4.2, page 7: \"convergence is absent at 340M\"）\n- 依赖 GDN 包含（Appendix D, Table 3: MMLU ρ 反转）\n\n但我想补充一个 nuance：aggregate convergence 在论文叙事中的作用不仅是一个独立 claim，更是 per-example divergence 的 **对照背景**。论文的核心 insight 是 decoupling——\"aggregate converges but per-example diverges\"。如果完全删除 aggregate convergence，per-example multiplicity 的发现就缺少了 \"despite apparent similarity\" 这个 framing，影响力会下降。\n\n建议方案：不是彻底删除 aggregate convergence 叙事，而是 (a) 将其从 \"core finding\" 降级为 \"motivating observation\"；(b) 在 Abstract 和 Introduction 中用更审慎的语言（\"on the one benchmark showing marginal aggregate convergence\" 而非暗示 general trend）；(c) 明确说明 LAMBADA 的特殊性。这比 R1 建议的 \"重新聚焦\" 更可行，因为完全放弃 aggregate 叙事会改变论文的核心架构。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R1-W1: GDN attention head confound 对结果的影响被低估**\n\n完全同意。我在 N3 中独立 flagged 了同一问题。GDN h3-1 使用 16 heads（Appendix E, page 13）而其他 hybrid 使用 32 heads，这不仅仅是一个 \"confound to note\" 而是一个 **systematic architectural difference**，可能驱动了 GDN 在 Table 1 中表现出的 distinctive pattern（如 LAMBADA 上 GDN 是唯一 ρ = -1.0 的架构）。\n\n关键证据：Appendix D Table 3 (page 12) 显示排除 GDN 后：\n- LAMBADA: ρ 从 -1.0 降至 -0.7（方向不变但幅度减半）\n- MMLU: ρ 从 -0.7 **反转**至 +0.6（方向完全反转）\n\nMMLU 的方向反转尤其值得关注——这意味着在 ReNet 和 HGRN2 之间，更多 attention 实际上 *增加* 而非减少 MMLU 上的 cross-architecture divergence。主文 §4.3 (page 8) 未提及此反转。\n\n**[AGREE] R1-W2: n=5 permutation test 本质上是 binary outcome**\n\n同意。这是一个重要的方法论观察。120 permutations（5!）中，只有 ρ = ±1.0 能达到 p = 1/120 ≈ .008 < .05。任何非完美单调关系都无法 reject null。因此 Table 1 (page 6) 中的 9 个 non-significant results 不能区分 \"no effect\" 和 \"moderate effect with insufficient power\"。\n\n论文在 §3.5 (page 5) 确实承认了这一点（\"a single rank swap suffices to shift the verdict from significant to non-significant\"），但 Table 1 的呈现方式——bolding only significant ρ——仍可能给读者 \"9 benchmarks show no convergence\" 的错误印象。\n\n建议：Table 1 应增加注释明确说明 non-significant ρ 的 interpretation ambiguity，或报告 effect size（如 ρ 本身）而非仅依赖 p-value。\n\n**[AGREE] R1-W3: Bootstrap CI (n=3) 不应被赋予高权重**\n\n同意。3 architectures 的 bootstrap resampling space 极其有限（3³ = 27 unique resamples，其中 3 个 degenerate = 11.1%，与 R1 的 11.25% 估计一致）。BCa correction 在如此小的 resampling space 上不可靠。\n\n论文在 Appendix B (page 12) 确实承认 resampling space 受限，并用 percentile CI 替代 full BCa，这是合理的 downgrade。但 Introduction (page 2) 中 \"the heuristic BCa 95% CI excludes zero\" 的表述确实给读者过强的统计保证，因为 95% CI 在 n=3 bootstrap 中的 coverage probability 远低于 nominal 95%。\n\n建议与 R1 一致：主文中对 bootstrap CI 的引用应加 caveat，或改为报告 percentile CI 并注明其 exploratory nature。\n\n**[REBUT with partial agreement] R1-W4: Confidence margin mechanism 的因果推断过度**\n\n部分同意 R1 的 \"mechanism\" 命名问题，但认为 R1 低估了论文提供的证据层次。\n\n同意的部分：§4.2 中将 confidence margin 分析称为 \"mechanism\" 确实暗示了因果性，而证据本质上是 correlational。标题措辞应改为 \"Confidence margin pattern\" 或 \"Confidence margin analysis\"。\n\n反驳的部分：R1 说 \"ECE 是粗粒度度量\"——但论文的 confidence margin 分析并不仅依赖 ECE。核心证据来自 per-example level 的 target-token probability 分析：\n- Appendix P Table 18 (page 17): Pure-correct hurt samples 的 |log p| 显著高于 stayed-right（即 lower target-token probability），across all three architectures\n- Appendix P Table 19 (page 17): Pure-wrong helped samples 的 |log p| 显著低于 stayed-wrong（即 higher target-token probability）\n- 这是 per-example 粒度的分析，比 ECE 精细得多\n\nECE 分析（Appendix Q, page 18）是 *补充* 证据，用于排除 calibration difference 作为 alternative explanation。论文在 page 6 说 \"calibration differences are insufficient to account for the observed threshold divergence\"——这是在排除 confound，不是核心证据。\n\n因此，我认为 \"mechanism\" 一词需改为更中性的表述，但 R1 对证据质量的批评过重。\n\n**[AGREE] R1-W5: 3 architectures 覆盖度有限**\n\n同意，与我的 W1 一致。标题应更精确地反映实际研究的架构范围。\n\n**[AGREE] R1-W6: Routing 分析的实践意义有限**\n\n同意，与我的 W5 一致。LAMBADA 上 66% accuracy（§4.2, page 6）虽高于 random，但 HellaSwag/PIQA 上无改善表明 routing 的适用条件很窄。\n\n---\n\n## Questions\n\n**[AGREE] Q1: 能否获取 model zoo 的多 seed 权重？**\n\n合理的问题。Wang et al. (2025) 的 model zoo 仅提供 single runs，获取多 seed 需要 retrain。但即使 retrain 一个 configuration 的 3-5 seeds 也能显著增强论文说服力。这与我的 Q1 一致。\n\n**[AGREE] Q2: GDN 16 heads 的 architectural motivation**\n\n与我的 Q2 一致。Appendix E (page 13) 解释这是原始 model zoo 的 design choice 而非 error，但这意味着 GDN 的 per-head capacity 与其他架构不同，可能系统性地影响 attention pattern 和 per-example behavior。\n\n**[REBUT] Q3: Per-example decomposition 仅在 4/10 benchmarks 上是否削弱 generality**\n\nR1 对此的 concern 有一定道理，但论文的处理比 R1 暗示的更完整：\n- 4 个主要 benchmarks（LAMBADA, HellaSwag, PIQA, ARC-Easy）覆盖了全部 4 个 task categories（retrieval, comprehension, reasoning, mixed）——这是 deliberate 的 category-representative sampling，不是 cherry-picking（§3.2, page 3-4, 引用 Arora et al. 2024a）\n- BoolQ 作为 supplementary benchmark 在 Appendix R (page 18) 有分析；WinoGrande 在 Appendix S (page 19)\n- §4.1 (page 5) 报告了 *全部* 10 benchmarks 的 aggregate results（Table 1）\n\nBoolQ/WinoGrande 的 mixed significance 确实值得讨论，但不一定削弱 generality——它可能反映 task-specific differences，这本身是论文的一个发现（multiplicity magnitude is task-dependent）。\n\n**[AGREE] Q4: Greedy decoding 下结果是否在 sampling 下持续**\n\n合理的 concern。Greedy decoding 产生 deterministic outputs，per-example effects 在 sampling decoding 下可能被 stochasticity 稀释。不过，大多数 NLP benchmarks 的 standard evaluation 使用 greedy/argmax decoding，且论文使用 lm-evaluation-harness (§3.2, page 4) 的 default 设置。这更多是一个 scope limitation 而非 flaw。\n\n**[REBUT with partial agreement] Q5: Within-architecture Jaccard (~0.33) 是否被 structural overlap inflate**\n\nR1 的 concern 有道理——同一架构的不同 attention ratios 共享 recurrence mechanism，可能因此有更高的 per-example overlap。但这种 \"structural overlap\" 恰恰是论文的分析对象之一：论文在 §4.1 (page 5) 中说 \"Within each benchmark, σ is stable across attention ratios (variation < 0.033)\"，Figure 1(b) 显示 Jaccard 在不同 attention ratios 间变化不大。\n\n更重要的是，3× gap 不是论文的 core claim——论文的核心发现是 *per-example Jaccard saturation at 4% attention despite aggregate convergence*（Figure 1, §4.1），这一发现不依赖 within- vs cross-architecture 的对比。即使 3× gap 被 inflate，per-example saturation 仍然成立。\n\n但我同意 R1 的隐含建议：论文应明确讨论 structural overlap 对 within-architecture Jaccard 的可能影响，而非将 3× gap 作为 seed vs. architecture 的间接证据。\n\n---\n\n## Missing References\n\n**[REBUT] Poli et al. (2023) \"Hyena Hierarchy\"**\n\nHyena 不是 gated linear recurrence 架构（它基于 long convolution），与论文研究的 GDN/ReNet/HGRN2 family 有本质区别。论文的 scope 是 \"hybrid linear recurrent architectures\"，Hyena 不属于此类别。除非论文扩展到更广泛的 efficient architecture 比较，否则不引用 Hyena 是合理的。\n\n**[AGREE] Jelassi et al. (2024) attention 与 in-context learning in hybrid models**\n\n同意这是一个相关 reference。Jelassi et al. 研究 attention 在 hybrid models 中对 in-context learning 的作用，与本文关于 attention ratio 影响 per-example behavior 的分析在 motivation 上有交叉。应在 Related Work §2 中讨论。\n",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1027 · 2026-05-22T12:05:02.908005+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3873
}
```

</details>

---


### Assistant

_source line 1028 · 2026-05-22T12:05:11.004159+00:00_

已提交对 Reviewer 1 的逐条回应。总结：

- **N1 (single seed)**: [AGREE]，补充了 seed variation 也可产生 structured patterns 的论点
- **N2 (aggregate convergence over-weighted)**: [AGREE with nuance]，建议将 aggregate convergence 从 "core finding" 降级为 "motivating observation" 而非彻底删除
- **W1 (GDN head confound)**: [AGREE]，强调 MMLU 方向反转未在主文提及
- **W2 (permutation test binary)**: [AGREE]
- **W3 (bootstrap CI n=3)**: [AGREE]
- **W4 (confidence margin overclaiming)**: [REBUT with partial agreement]——"mechanism" 命名确需修改，但 R1 低估了 per-example token probability 分析的证据粒度（Tables 18-19 非 ECE）
- **W5, W6**: [AGREE]
- **Q3 (4/10 benchmarks)**: [REBUT]——4 benchmarks 覆盖全部 4 个 task categories，是 deliberate sampling
- **Q5 (Jaccard inflation)**: [REBUT with partial agreement]——structural overlap concern 有效，但核心发现（saturation at 4%）不依赖此对比

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 26

## Round 26

86 recorded events


### User

_source line 1029 · 2026-05-22T17:18:09.257806+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 相关工作完整性 + 写作质量 + 格式合规**。

## Venue 信息
- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）
- **投稿类别**：Long Paper
- **截止日期**：2026-05-25
- **页数限制**：正文 ≤ 8 页，参考文献无限制，Limitations/Ethics 不计入页数
- **模板**：ACL 模板，须使用 `[review]` 选项
- **匿名规则**：Double-blind
- **评分标准**：Overall Assessment 1-5 分制（5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）

## 论文文件
- LaTeX 源码：`projects/entrainment_gated_ft/docs/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/submitted.pdf`

## 你的审查侧重

请重点审查以下方面：

1. **新颖性评估**：
   - Predictive multiplicity 概念已有（Marx et al. 2020），underspecification 已有（D'Amour et al. 2022）——本文将其扩展到 hybrid recurrent architectures 的贡献是否足够构成一篇 EMNLP long paper？
   - "aggregate convergence 和 per-example divergence 的 decoupling" 是否是一个真正新颖的发现，还是 ecological fallacy 的已知实例？
   - Confidence-based routing 作为 application 是否足够有意义？只在 LAMBADA 上有效。

2. **相关工作完整性**：
   - 是否遗漏了重要的相关工作？特别是：
     a) 近期 hybrid architecture 文献（2025-2026）
     b) Model disagreement / ensemble diversity 文献
     c) Per-example analysis 的其他方法论文献
   - 对已引用工作的定位是否准确？

3. **写作质量**：
   - Abstract 是否准确概括了论文的贡献和局限？
   - Introduction 的叙事逻辑是否清晰？
   - 论文的 claim 强度是否与证据匹配（hedging 是否恰当）？
   - 数学符号是否一致？
   - 是否有冗余或重复的内容？

4. **格式合规**：
   - 正文是否在 8 页以内（不含 references、limitations、ethics）？
   - 匿名性是否完整（无作者信息泄露、无 deanonymizing self-citation）？
   - Limitations 和 Ethics Statement 是否充分？
   - 表格和图片的质量和可读性如何？
   - 引用格式是否符合 ACL 规范？

请以 EMNLP 2026 审稿标准严格评审，逐条列出 Strengths 和 Weaknesses，给出初步评分建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1030 · 2026-05-22T17:18:16.080904+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 1031 · 2026-05-22T17:18:16.131470+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Skill",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1032 · 2026-05-22T17:18:20.411328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1033 · 2026-05-22T17:18:21.765462+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/.claude/sessions/review_reviewer_2_fe7a65fc.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1354
}
```

</details>

---


### Tool call

_source line 1034 · 2026-05-22T17:18:21.765929+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 1035 · 2026-05-22T17:18:21.916695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-22T17:18:29.212928+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1037 · 2026-05-22T17:18:30.154858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form scoring dimensions soundness excitement"
  }
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-22T17:18:32.398569+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-22T17:18:38.547167+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here are the key details:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference reco
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9334
}
```

</details>

---


### Tool result

_source line 1040 · 2026-05-22T17:18:40.253359+00:00_

Web search results for query: "EMNLP 2026 ARR review form scoring dimensions soundness excitement"

Links: [{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Improving Patient Experience: BMBA","url":"https://cdn.clinicaltrials.gov/large-docs/30/NCT05690230/Prot_SAP_000.pdf"}]

Based on the search results, I found relevant information about the ARR review form scoring dimensions:

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

The two scoring dimensions you mentioned—**soundness** and **excitement**—are distinct evaluation criteria:

- **Soundness**: Soundness scores must be justified by the text of the review, and if you give a low Soundness score without finding any major faults, your review is not a faithful explanation of your recommendation.

- **Excitement**: The excitement score is orthogonal to the assessment of the soundness of the paper and reflects reviewers' personal taste without necessarily coming with explicit reasons. Sometimes reviewers may find work sound but not personally interesting, and such subjective preferences should be reflected in a separate excitement score.

- **Overall Assessment**: The Overall assessment score is an explicit recommendation for the outcome of the paper if it were committed to an *ACL venue, reflecting the assessment of soundness, excitement, and also other factors like novelty an
…[truncated 112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10098
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-22T17:18:42.111601+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 433.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 535.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9713
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-22T17:18:49.688810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1043 · 2026-05-22T17:18:50.241773+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1044 · 2026-05-22T17:18:50.545910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1045 · 2026-05-22T17:18:50.999630+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-22T17:18:51.000053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1047 · 2026-05-22T17:18:52.157149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1048 · 2026-05-22T17:18:52.862109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1049 · 2026-05-22T17:18:53.414749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1050 · 2026-05-22T17:18:54.428531+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4186
}
```

</details>

---


### Tool call

_source line 1051 · 2026-05-22T17:18:54.429001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1052 · 2026-05-22T17:18:54.533963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1053 · 2026-05-22T17:18:55.443819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1054 · 2026-05-22T17:18:57.863402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6863
}
```

</details>

---


### Tool result

_source line 1055 · 2026-05-22T17:18:57.866694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6866
}
```

</details>

---


### Tool call

_source line 1056 · 2026-05-22T17:18:57.867129+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include the Overall Assessment scale, Soundness scale, Excitement scale, and any other scoring criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include the Overall Assessment scale, Soundness scale, Excitement scale, and any other scoring criteria."
  }
}
```

</details>

---


### Tool call

_source line 1057 · 2026-05-22T17:18:58.673089+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-22",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-22",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-22T17:19:00.485548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 8328
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-22T17:19:00.687237+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7825
}
```

</details>

---


### Tool result

_source line 1060 · 2026-05-22T17:19:01.095263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7680
}
```

</details>

---


### Tool result

_source line 1061 · 2026-05-22T17:19:01.350739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6921
}
```

</details>

---


### Tool result

_source line 1062 · 2026-05-22T17:19:01.402107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6868
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-22T17:19:01.457706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6013
}
```

</details>

---


### Tool result

_source line 1064 · 2026-05-22T17:19:06.379830+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
5-point scale with 0.5 increments (5 = Consider for Award down to 1 = Do not resubmit)
- "Consider for Award: I think this paper could be considered for an outstanding paper award"
- Conference recommendation available
- Findings tier option
- Resubmit options for papers needing revisions

## Soundness
1-5 scale with 0.5 increments evaluating scientific rigor:
- 5 = "Excellent: This study is one of the most thorough I have seen"
- 4 = "Strong: This study provides sufficient support for all of its claims"
- 3 = "Acceptable: This study provides sufficient support for its main claims"
- 2 = "Poor: Some of the main claims are not sufficiently supported"
- 1 = "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
1-5 scale with 0.5 increments measuring subjective appeal:
- 5 = "Highly Exciting: I would recommend this paper to others"
- 4 = "Exciting: I would mention this paper to others"
- 3 = "Interesting: I might mention some points of this paper"
- 2 = "Potentially Interesting: does not resonate with me, but it might with others"
- 1 = "Not Exciting: does not resonate with me"

## Additional Dimensions
- **Reviewer Confidence** (1-5 scale)
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale)
- **Software** (1-5 scale)
- **Author Identity Knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8512
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-22T17:19:07.797339+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.7}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 385.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 414.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.0}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 453.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9124
}
```

</details>

---


### Tool call

_source line 1066 · 2026-05-22T17:19:41.335784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1067 · 2026-05-22T17:19:41.987515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1068 · 2026-05-22T17:19:41.989293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 1069 · 2026-05-22T17:19:42.744626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 1070 · 2026-05-22T17:19:42.945689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 1071 · 2026-05-22T17:19:43.298817+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1072 · 2026-05-22T17:19:43.753562+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1073 · 2026-05-22T17:19:43.753994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1074 · 2026-05-22T17:19:44.660314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 1075 · 2026-05-22T17:19:44.663019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-22T17:19:44.663420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1077 · 2026-05-22T17:19:45.216405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1078 · 2026-05-22T17:19:45.669011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1079 · 2026-05-22T17:19:45.669416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-22T17:19:46.574218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-22T17:19:46.575262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-22T17:19:46.575556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-22T17:19:47.107863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-22T17:19:47.510689+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 935
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-22T17:19:47.511093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_15/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1086 · 2026-05-22T17:19:48.014568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-22T17:19:48.366433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-22T17:20:04.627093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1089 · 2026-05-22T17:20:05.482706+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Adding attention to linear recurrent architectures is associated with per-example changes on almost entirely different examples across three controlled hybrid linear recurrent designs: pairwise overlap is at most 10\%. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) rather than attention dose. Aggregate trends do not reach statistical significance ($n = 5$; Bonferroni-adjusted $p = .170$), yet per-example overlap saturates at 4\% attention and remains flat across all four benchmarks. Naive majority vote fails to exploit this complementarity, suggesting that configurations interchangeable by aggregate metrics carry hidden consequences for per-example reliability.
26	\end{abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	
40	Our analysis has several limitations.
41	
42	\paragraph{Single training runs.} Each configuration corresponds to a single training run; we cannot fully disentangle architectural from seed-specific effects, though the $3\times$ within- vs.\ cross-architecture Jaccard gap (\S\ref{ssec:decoupling}) provides proxy evidence. All per-example claims are conditioned on this li
…[truncated 2157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1090 · 2026-05-22T17:20:05.483174+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "predictive multiplicity per-example analysis language models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "predictive multiplicity per-example analysis language models 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-22T17:20:05.985277+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hybrid recurrent architecture Mamba attention comparison 2025 2026 analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hybrid recurrent architecture Mamba attention comparison 2025 2026 analysis"
  }
}
```

</details>

---


### Tool call

_source line 1092 · 2026-05-22T17:20:06.488282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model disagreement ensemble diversity per-example prediction NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model disagreement ensemble diversity per-example prediction NLP 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-22T17:20:13.774451+00:00_

Web search results for query: "model disagreement ensemble diversity per-example prediction NLP 2025 2026"

Links: [{"title":"Ensemble Large Language Models: A Survey","url":"https://www.mdpi.com/2078-2489/16/8/688"},{"title":"LeWiDi-2025 at NLPerspectives: Third Edition of the Learning with Disagreements Shared Task","url":"https://arxiv.org/html/2510.08460"},{"title":"Agree to Disagree: Diversity through Disagreement for Better   Transferability","url":"https://arxiv.org/pdf/2202.04414"},{"title":"MSA at BEA 2025 Shared Task: Disagreement-Aware Instruction Tuning for Multi-Dimensional Evaluation of LLMs as Math Tutors","url":"https://arxiv.org/html/2505.18549"},{"title":"Effective Proxy for Human Labeling: Ensemble Disagreement Scores in   Large Language Models for Industrial NLP","url":"https://arxiv.org/pdf/2309.05619"},{"title":"Bridging the Gap: In-Context Learning for Modeling Human Disagreement","url":"https://arxiv.org/pdf/2506.06113"},{"title":"Weak Ensemble Learning from Multiple Annotators for ...","url":"https://aclanthology.org/2025.nlperspectives-1.8.pdf"}]

Based on the web search results, here are the relevant findings for model disagreement, ensemble diversity, and per-example prediction in NLP for 2025-2026:

## Recent Research (2025-2026)

**Ensemble Learning Approaches:**
Ensemble learning, which combines multiple models to improve performance, presents a promising approach for addressing limitations in large language models. Recent work has focused on leveraging model disagreement strategically.

**Disagreement-Aware Ensemble Strategies:**
Researchers have introduced disagreement-aware ensemble inference strategies that enhance coverage of minority labels by leveraging model disagreement and uncertainty for robust prediction. While this improves recall for minority labels, the benefit may diminish if base models exhibit correlated predictions, and ensembles are most effective when model predictions are diverse and independent.

**Modeling Human
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7286
}
```

</details>

---


### Tool result

_source line 1094 · 2026-05-22T17:20:15.581996+00:00_

Web search results for query: "hybrid recurrent architecture Mamba attention comparison 2025 2026 analysis"

Links: [{"title":"Mamba-LSTM-Attention (MLA): A Hybrid Architecture for ...","url":"https://www.preprints.org/manuscript/202601.1709/v1/download"},{"title":"Hybrid Mamba-Attention Architectures","url":"https://www.emergentmind.com/topics/hybrid-mamba-attention-architectures"},{"title":"Published as a conference paper at ICLR 2026 MAMBA-3:","url":"https://openreview.net/pdf?id=HwCvaJOiCj"},{"title":"Understanding and Enhancing Mamba-Transformer Hybrids for Memory Recall and Language Modeling","url":"https://arxiv.org/html/2510.26912v1"},{"title":"HYBRID TRANSFORMER-MAMBA LANGUAGE MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf"},{"title":"Tiny Recursive Reasoning with Mamba-2 Attention Hybrid","url":"https://arxiv.org/pdf/2602.12078"},{"title":"How Effective are State Space Models for Machine Translation?","url":"https://arxiv.org/pdf/2407.05489"}]

Based on the web search results, here's what I found about hybrid recurrent architectures, Mamba, and attention comparisons in 2025-2026:

## Key Findings

**Hybrid Architecture Performance:**
Empirical studies consistently show that hybrids outperform pure SSM or pure attention architectures on benchmarks requiring both long-range context and local pattern discrimination.

**Recent Hybrid Designs:**
Recent research shows inter-layer ("sequential") fusion approaches that alternate blocks of SSM and attention in a deep stack, with examples using 2 attention and 11 Mamba layers in 16 layers for a 1:5 ratio, with best performance when attention blocks are in the middle layers. Intra-layer ("parallel") fusion approaches split model dimensions or attention heads within a given layer, routing inputs to SSM and attention, fusing outputs via concatenation and projection or weighted sum.

**Mamba-Specific Advantages:**
Excluding the Mamba module (L
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9596
}
```

</details>

---


### Tool result

_source line 1095 · 2026-05-22T17:20:32.302022+00:00_

Web search results for query: "predictive multiplicity per-example analysis language models 2025 2026"

Links: [{"title":"Predictive Multiplicity in Classification | alphaXiv","url":"https://www.alphaxiv.org/abs/1909.06677"},{"title":"Better & Faster Large Language Models via Multi-token Prediction","url":"https://arxiv.org/pdf/2404.19737"},{"title":"Predictive Multiplicity in Survival Models: A Method for Quantifying Model Uncertainty in Predictive Maintenance Applications","url":"https://arxiv.org/html/2504.12156v1"},{"title":"Predictive Multiplicity in Probabilistic Classification","url":"https://arxiv.org/pdf/2206.01131"},{"title":"Large Language Models for Predictive Analysis: How Far Are They?","url":"https://arxiv.org/html/2505.17149v1"},{"title":"Learning to vary: Teaching LMs to reproduce human linguistic variability in next-word prediction","url":"https://arxiv.org/pdf/2509.17794"},{"title":"Predictive Multiplicity in Classiﬁcation","url":"https://proceedings.mlr.press/v119/marx20a/marx20a.pdf"}]

Based on the search results, here's what I found regarding predictive multiplicity and language models:

## Recent Research on Predictive Multiplicity

Predictive multiplicity is defined as the ability of a prediction problem to admit competing models with conflicting predictions. The phenomenon has been recognized as a key contributor to model uncertainty and mistrust, where multiple, equally well-performing models make diverging predictions.

## 2025 Research on Language Models and Predictive Analysis

More recent work from 2025 focuses on language models' capabilities in predictive analysis. A study examines predictive analysis tasks where the input consists of a query requesting future predictions, identifies data patterns associated with corresponding data.

## Per-Example Analysis in Related Work

While the search results don't contain specific papers on "per-example analysis" of predictive multiplicity in language models from 2025-2026, the broader concept
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 26818
}
```

</details>

---


### Tool call

_source line 1096 · 2026-05-22T17:20:48.369208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rashomon set model multiplicity fairness 2024 2025 NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rashomon set model multiplicity fairness 2024 2025 NeurIPS ICML"
  }
}
```

</details>

---


### Tool call

_source line 1097 · 2026-05-22T17:20:49.021824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ecological fallacy machine learning individual prediction aggregate performance 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ecological fallacy machine learning individual prediction aggregate performance 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-22T17:20:49.373614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jamba hybrid Mamba Transformer architecture 2024 2025 per-example analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jamba hybrid Mamba Transformer architecture 2024 2025 per-example analysis"
  }
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-22T17:20:51.332933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-22T17:20:51.383527+00:00_

1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: on LAMBADA, cross-architecture standard deviation drops 79\% as attention increases (Bonferroni-adjusted $p = .170$, BCa CI $[-1.0, -0.7]$), but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Our results show that architectures scoring identically in aggregate may nonetheless differ on 15--45\% of individual predictions, meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{marx2020predictive} a
…[truncated 4249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1101 · 2026-05-22T17:20:55.849335+00:00_

Web search results for query: "ecological fallacy machine learning individual prediction aggregate performance 2024 2025"

Links: [{"title":"An evaluation of the performance and suitability of R × C methods for ecological inference with known true values","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5847155/"},{"title":"Ecological inference and the ecological fallacy | Department of Statistics","url":"https://statistics.berkeley.edu/tech-reports/549"},{"title":"Ecological Fallacy - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/computer-science/ecological-fallacy"},{"title":"Ecological fallacy - Wikipedia","url":"https://en.wikipedia.org/wiki/Ecological_fallacy"},{"title":"Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare","url":"https://arxiv.org/pdf/2603.00192"},{"title":"Ecological fallacy | Epidemiology & Data Analysis | Britannica","url":"https://www.britannica.com/science/ecological-fallacy"},{"title":"Data leakage in machine learning studies creep into meta-analytic estimates of predictive performance","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12602356/"},{"title":"AI-Powered Fall Risk Prediction in Nursing Care","url":"https://cdn.clinicaltrials.gov/large-docs/81/NCT07000981/Prot_SAP_000.pdf"},{"title":"The Ecological Fallacy in Annotation: Modelling Human Label Variation   goes beyond Sociodemographics","url":"https://arxiv.org/pdf/2306.11559"}]

Based on the search results, here's what I found on the topic of ecological fallacy, machine learning, and the relationship between individual prediction and aggregate performance:

## Key Findings

**Definition and Core Issue:**
An ecological fallacy is a formal fallacy in the interpretation of statistical data that occurs when inferences about the nature of individuals are deduced from inferences about the group to which those individuals belong. It refers to the practice of making untested inferences about individual-level
…[truncated 1377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6827
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-22T17:20:56.902974+00:00_

Web search results for query: "Jamba hybrid Mamba Transformer architecture 2024 2025 per-example analysis"

Links: [{"title":"Jamba: A Hybrid Transformer-Mamba Language Model with Mixture-of-Experts | by Sulbha Jain | Nov, 2025 | Medium","url":"https://medium.com/@sulbha.jindal/jamba-a-hybrid-transformer-mamba-language-model-with-mixture-of-experts-506281f2398e"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model Opher Lieber∗ Barak Lenz∗","url":"https://arxiv.org/pdf/2403.19887"},{"title":"Architectural Evolution in Large Language Models: A Deep Dive into Jamba’s Hybrid Transformer-Mamba Design | by Greg Robison | Medium","url":"https://gregrobison.medium.com/architectural-evolution-in-large-language-models-a-deep-dive-into-jambas-hybrid-transformer-mamba-c3efa8ca8cae"},{"title":"Jamba: Hybrid Transformer-Mamba Language Models | OpenReview","url":"https://openreview.net/forum?id=JFPaD7lpBD"},{"title":"[2403.19887] Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://arxiv.org/abs/2403.19887"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://arxiv.org/html/2403.19887v1"},{"title":"Jamba Model: An Innovative Fusion of Transformer and Mamba in Artificial Intelligence","url":"https://deepfa.ir/en/blog/jamba-model-hybrid-transformer-mamba-architecture"},{"title":"[2408.12570] Jamba-1.5: Hybrid Transformer-Mamba Models at Scale","url":"https://arxiv.org/abs/2408.12570"},{"title":"Jamba-1.5: Hybrid Transformer-Mamba Models at Scale","url":"https://arxiv.org/pdf/2408.12570"}]

I've found comprehensive information about Jamba's hybrid Transformer-Mamba architecture. Here's what the search results reveal:

## Architecture Overview

Jamba is a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture that interleaves blocks of Transformer and Mamba layers, with MoE added in some layers to increase model capacity while keeping active parameter usage manageable.

## Design and Performance

The architecture interleaves sta
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7529
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-22T17:20:59.662468+00:00_

Web search results for query: "Rashomon set model multiplicity fairness 2024 2025 NeurIPS ICML"

Links: [{"title":"Be Intentional About Fairness!: Fairness, Size, and Multiplicity in the   Rashomon Set","url":"https://arxiv.org/pdf/2501.15634"},{"title":"Allocation Multiplicity: Evaluating the Promises of the Rashomon Set | Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/10.1145/3715275.3732138"},{"title":"Allocation Multiplicity: Evaluating the Promises of the Rashomon Set","url":"https://arxiv.org/html/2503.16621"},{"title":"Resolving Predictive Multiplicity for the Rashomon Set","url":"https://arxiv.org/pdf/2601.09071"},{"title":"Publications","url":"https://chudizhong.github.io/research.html"},{"title":"Systemizing Multiplicity: The Curious Case of Arbitrariness in Machine Learning","url":"https://ojs.aaai.org/index.php/AIES/article/download/36609/38747/40684"},{"title":"The Rashomon Set Has It All: Analyzing Trustworthiness of Trees under Multiplicity | OpenReview","url":"https://openreview.net/forum?id=RXsDPn3toF"},{"title":"Shomik Jain, Margaret Wang, Kathleen Creel & Ashia Wilson, Allocation Multiplicity: Evaluating the Promises of the Rashomon Set - PhilPapers","url":"https://philpapers.org/rec/JAIAME"}]

I found several relevant papers on Rashomon sets, model multiplicity, and fairness from recent conferences. Here's what the search revealed:

## Key Papers and Results

**Recent ICML Work (2024):**
"The Amazing Things that Come From Having Many Good Models" was published at ICML 2024 as a Spotlight paper by Cynthia Rudin, Chudi Zhong, and colleagues.

**NeurIPS 2025 Work:**
"The Rashomon Set Has It All: Analyzing Trustworthiness of Trees under Multiplicity" introduces a framework for systematically analyzing trustworthiness within Rashomon sets and shows that near-optimal sparse decision trees from the Rashomon set can perform as well as models explicitly optimized for fairness, robustness
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11293
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-22T17:21:08.807160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1105 · 2026-05-22T17:21:09.158860+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear attention \citep{katharopoulos2020transformers} through the state-space--attention duality of Mamba-2.
8	
9	\paragraph{Underspecification and Predictive Multiplicity.}
10	\citet{damour2022underspecification} formalized underspecification: eq
…[truncated 2746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1106 · 2026-05-22T17:21:09.159210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-22T17:21:09.868028+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture convergence across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.4$ & .517 & 1.17 & 1.22 & 0.96 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\footnotesize $^{\dagger}$Supplementary ($n = 100$); excluded from multiple comparison correction.} \\
28	\multicolumn{7}{l}{
…[truncated 13889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-22T17:21:09.868572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"prediction instability\" individual-level machine learning model comparison 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"prediction instability\" individual-level machine learning model comparison 2025 2026 arxiv"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-22T17:21:17.202318+00:00_

Web search results for query: ""prediction instability" individual-level machine learning model comparison 2025 2026 arxiv"

Links: [{"title":"[2603.00192] Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare","url":"https://arxiv.org/abs/2603.00192"},{"title":"Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare","url":"https://arxiv.org/pdf/2603.00192"},{"title":"Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare","url":"https://arxiv.org/html/2603.00192"},{"title":"Quantifying the Prediction Uncertainty of Machine Learning Models for   Individual Data","url":"https://arxiv.org/pdf/2412.07520"},{"title":"Stability of clinical prediction models developed using statistical or machine learning methods","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10952221/"}]

Based on the search results, I found a highly relevant recent paper on this topic:

In healthcare, predictive models increasingly inform patient-level decisions, yet little attention is paid to the variability in individual risk estimates and its impact on treatment decisions. A paper titled "Diagnostics for Individual-Level Prediction Instability in Machine Learning for Healthcare" by Elizabeth W. Miller and Jeffrey D. Blume from the University of Virginia addresses this issue.

The research identifies a critical problem: Even when the data and model architecture are held fixed, randomness introduced by optimization and initialization can lead to materially different risk estimates for the same patient. This problem is largely obscured by standard evaluation practices, which rely on aggregate performance metrics (e.g., log-loss, accuracy) that are agnostic to individual-level stability.

To diagnose the problem, the authors propose an evaluation framework that quantifies individual-level prediction instability across repeated instantiations of an otherwise fixed learning pipeline, introduc
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7333
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-22T17:22:59.821826+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the key reviewing guidelines, especially: what should reviewers look for, how to assess novelty, what constitutes a good vs weak paper, any specific guidance on empirical analysis papers, and the relationship between soundness, excitement, and overall assessment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the key reviewing guidelines, especially: what should reviewers look for, how to assess novelty, what constitutes a good vs weak paper, any specific guidance on empirical analysis papers, and the relationship between soundness, excitement, and overall assessment."
  }
}
```

</details>

---


### Tool result

_source line 1111 · 2026-05-22T17:23:10.630999+00:00_

# ARR Reviewer Guidelines: Key Takeaways

## What Reviewers Should Look For

Reviewers should assess papers across multiple dimensions:

**Soundness & Technical Quality**: Verify that methodology is rigorous, assumptions are clearly stated, and proofs are complete. Check for "undisclosed data quality issues" and ensure reproducibility details are provided.

**Novelty Assessment**: The guidelines caution against dismissing work as "not novel" without evidence. Reviewers must cite specific prior work if claiming similarity. The document notes that "highly similar work" must have been "published 3+ months prior to submission deadline" to disqualify a paper.

**Contribution Type**: Papers may contribute through models, resources, surveys, analysis, or theory—not just achieving state-of-the-art results. Negative results addressing gaps in knowledge are valuable.

## Common Reviewer Mistakes to Avoid

The guidelines identify seventeen heuristics that often lead to unfair reviews:

- **H5**: Demanding SOTA results when papers contribute on other dimensions (efficiency, interpretability, fairness)
- **H6**: Dismissing negative results (bias toward positive findings harms the field)
- **H7**: Preferring unnecessarily complex solutions over simpler ones
- **H13**: Requesting experiments beyond what's needed to support the paper's claims

## Three-Score Framework

Starting February 2025, reviewers provide three orthogonal assessments:

1. **Soundness**: Technical validity. Must be justified by review text.
2. **Excitement**: Personal interest level (subjective, doesn't require justification)
3. **Overall Assessment**: Composite recommendation considering soundness, novelty, and potential impact

A paper can be sound but unexciting, or exciting but methodologically flawed. These scores serve different purposes in editorial decisions.

## Guidance for Empirical Papers

Key issues to identify:

- **M1**: LLM-only evaluation requires validation that the LLM is reliable for that sp
…[truncated 1322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10809
}
```

</details>

---


### Tool call

_source line 1112 · 2026-05-22T17:26:13.099938+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 级别）\n**一句话总结**: 方法论严谨的经验性分析，系统记录了 hybrid recurrent architectures 间的 per-example 差异，但核心发现是 ecological fallacy 的一个已知实例，最重要的 convergence claim 统计效力不足（n=5, Bonferroni-adjusted p=.170），且唯一有效的应用（routing）仅在 1/4 基准上有效，整体新颖性和影响力不足以支撑 EMNLP 主会议长文。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法得当（permutation test, bootstrap CI），但核心 convergence result 依赖 GDN inclusion 且 n=5 严重欠统计功效；单次训练无法分离 architecture 与 seed effects |\n| Excitement | 2.5/5 | 问题有实际意义，但核心发现（aggregate ≠ individual）是 ecological fallacy 的已知实例，论文自己也承认（Section 2, p.3）；实际应用（routing）效果有限 |\n| Reproducibility | 4/5 | 使用公开 model zoo，方法描述充分，代码承诺公开 |\n| Reviewer Confidence | 4/5 | 熟悉 predictive multiplicity 文献和 hybrid architecture 领域 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心 convergence claim 统计效力严重不足\n- 具体位置：Table 1（p.6）、Section 4.2（p.7）、Abstract\n- 问题：论文的核心叙事之一是 \"aggregate convergence vs. per-example divergence 的 decoupling\"。但 aggregate convergence 仅在 LAMBADA 上呈现 ρ = −1.0，Bonferroni 校正后 p = .170，未达到常规统计显著性。论文在方法部分（Section 3.5, p.5）也承认 \"with n = 5 ordinal levels, only ρ = ±1.0 achieves p < .05\"。这意味着论文无法在 10 个基准中的 9 个上检测任何趋势，且唯一 \"显著\" 的 LAMBADA 在校正后也不显著。然而 Abstract 和 Introduction 的叙事结构将 decoupling 呈现为一个稳健发现（\"Aggregate trends do not reach statistical significance... yet per-example overlap saturates\"），这种并置暗示了一个比数据支持更强的 pattern。\n- 为什么影响接收：论文的两大贡献之一（per-example saturation + aggregate convergence 的解耦）建立在一个不显著的统计结果上。如果 convergence 本身都不确定，decoupling 的论证基础就不成立。\n- 建议修改方向：(1) 将 decoupling 明确降级为 exploratory/suggestive observation，而非 main contribution；(2) 在 Abstract 中更直接地陈述 convergence result 不显著；(3) 增加 power analysis 说明需要多少 attention ratio 水平才能可靠检测中等效应。\n\n**N2** [critical] GDN 头数混杂变量污染 convergence result\n- 具体位置：Section 4.3（p.8）、Table 1 脚注‡\n- 问题：LAMBADA 上 ρ = −1.0 的 convergence result 依赖于 GDN 的包含。GDN h3-1 使用 16 个 attention head 而所有其他配置使用 32 个。移除 GDN 后，ρ 从 −1.0 降至 −0.7（p = .233），MMLU 的趋势甚至反转（ρ = −0.7 → +0.6）。论文在 Section 4.3 讨论了这一问题，但没有充分论证为何在存在这一混杂变量的情况下仍然可以信任 convergence result。16 vs 32 head 的差异可能单独解释 GDN 的 faster convergence（通过限制 attention capacity），而非反映真正的架构趋势。\n- 为什么影响接收：如果核心 convergence 发现的存废取决于一个有已知混杂变量的架构，那么 decoupling 叙事的基础更加脆弱。论文的第二个贡献（Section 1, 第二个 bullet point）明确将 Jaccard saturation 与 aggregate convergence 的 decoupling 列为贡献，但 convergence 一侧不可靠。\n- 建议修改方向：(1) 将 convergence claim 限定为 conditional on GDN inclusion，并在 contribution statement 中反映；(2) 考虑以 RetNet-HGRN2 pair 的 decoupling 作为 primary evidence（论文提到这个 pair \"preserves the decoupling\"），虽然这会削弱一般性。\n\n**N3** [critical] 单次训练无法分离架构效应与随机种子效应\n- 具体位置：Limitations（p.8-9）、Appendix W（p.21）\n- 问题：每个配置仅有一次训练运行。论文声称观察到的 per-example divergence 来自架构差异，但无法排除训练随机性（不同种子）的贡献。论文的缓解措施——Pythia 70M PolyPythias 的 within-seed Jaccard（0.27-0.39）vs. cross-architecture Jaccard（0.09-0.10）的 3-4× 差异——是有用的校准，但存在严重局限：(a) Pythia 是纯 Transformer 而非 hybrid recurrent model；(b) 70M 与 340M/1.3B 规模差异巨大；(c) 不同模型族的比较不能替代 matched-seed 实验。\n- 为什么影响接收：这是区分 \"architectures cause per-example divergence\" 和 \"any variation in training produces per-example divergence\" 的关键。如果后者为真，本文的贡献就从 \"architectures matter at per-example level\" 降级为 \"training variation matters at per-example level\"，后者已被 D'Amour et al. (2022) 和 McCoy et al. (2020) 充分记录。\n- 建议修改方向：(1) 在至少一个架构上进行 3-5 次不同种子的训练，计算 within-architecture cross-seed Jaccard 作为基线；(2) 如果无法新增实验，至少将所有因果性语言替换为关联性语言（\"is associated with\" vs. \"causes\"），并在 contribution statement 中明确标注此限制。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 新颖性定位：ecological fallacy 的已知实例\n- 具体位置：Section 2（p.3, 最后一段）\n- 问题：论文诚实地承认 \"The observation that aggregate-level associations can diverge from individual-level patterns is a well-known statistical phenomenon (ecological fallacy; Robinson 1950)\"，并说 \"The contribution lies not in the conceptual observation but in its quantitative characterization.\" 这是准确的自我定位，但也恰好说明了新颖性的局限：本文本质上是用一个 specific model zoo 量化了一个已知现象。将 predictive multiplicity（Marx et al. 2020，原本针对 Rashomon set 内 near-optimal models）的概念扩展到不同架构族是一个合理的延伸，但不够 surprising。\n- 建议：在 Introduction 中更早、更明确地区分 \"what we show for the first time\"（quantitative characterization in hybrid recurrent models）和 \"what is conceptually known\"（ecological fallacy, underspecification），避免读者产生过高的新颖性预期。\n\n**W2** [warning] Confidence-based routing 作为应用价值不足\n- 具体位置：Section 4.1, \"Confidence-based routing\" 段（p.6）\n- 问题：Routing 仅在 LAMBADA 上有效（+5.3pp over majority vote），在 ARC-Easy 上 marginal（+1.0pp），在 HellaSwag 和 PIQA 上无改善。这意味着实际应用仅在 α 最高的 benchmark（0.30）上有效，而在 reasoning tasks（α = 0.14-0.15）上完全失败。论文对此有所讨论，但 routing 仍然被列为 \"proof-of-concept application\"，这对于仅在 1/4 基准上有效的方法而言定位过高。\n- 建议：将 routing 降级为一个 case study / illustrative example，明确讨论为何它在低-α 任务上失败，以及什么条件下 per-example multiplicity 才有实际可利用的价值。\n\n**W3** [warning] Introduction 第一句话过度声称\n- 具体位置：Section 1, 第一句（p.1）\n- 问题：\"Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples\" 中 \"nearly disjoint\" 暗示极低的重叠。但实际 Jaccard ≈ 0.10 vs. independence baseline ≈ 0.05，即观测重叠约为独立基线的 2 倍。\"Nearly disjoint\" 在集合论意义上可辩护（90% 非重叠），但忽略了 base rate：random pairs 也会 \"nearly disjoint\"（95% 非重叠）。超出独立基线的 excess overlap 仅约 5 个百分点，且统计显著地高于独立（z > 5.9），这说明架构间有结构化但微弱的共享，而非 \"nearly disjoint\"。\n- 建议：将 \"nearly disjoint\" 替换为更精确的表述，如 \"largely non-overlapping (J ≈ 0.10, approximately 2× independence baseline)\"。\n\n**W4** [warning] 缺乏可操作的实践建议\n- 问题：论文详细记录了 per-example divergence 的存在和量级，但对 practitioners 的 actionable takeaways 不够具体。Conclusion（Section 5, p.8）提到 \"aggregate benchmark equivalence does not guarantee per-example agreement\" 但没有说在什么场景下这 matters enough to change decisions。论文未讨论：(a) 对于什么样的下游任务，15-45% 的 individual prediction 差异是 practically significant 的？(b) 如果用户已经在做 ensemble/multi-seed evaluation，本文的发现是否提供增量信息？\n- 建议：在 Conclusion 或 Discussion 中加入一小段具体指导。\n\n## 小问题（不影响接收）\n- Abstract 中 \"almost entirely different examples\" 与正文 \"at most 10%\" 的表述不一致——前者暗示接近 0% 重叠，但 10% Jaccard 仍然意味着有统计显著的共享结构。\n- Section 3.4 的 helped/hurt/unchanged 分解将 0.51→0.49 的微小变化与 0.99→0.01 的大幅变化等同看待。虽然论文在正文中提到了这一局限并在 Appendix 做了 continuous 分析，但主体叙事完全依赖 binary decomposition。\n- 340M 的分析（Section 4.2, p.8）显示 convergence absent（ρ = −0.50, p = .45），进一步削弱 convergence 发现的普遍性，但这一事实在论文中处理得较为低调。\n- Figure 1 panel (b) y 轴范围较窄（0.06-0.12），视觉上可能夸大 Jaccard 的稳定性。\n- 格式合规：正文 8 页以内 ✓；使用 [review] 模板 ✓；匿名性完整（\\author{Anonymous}，无 self-identifying URL）✓；Limitations 和 Ethics Statement 存在且不计入页数 ✓。\n- 引用格式基本符合 ACL 规范，Related Work 覆盖了 2026 年最新工作。未发现重大遗漏——可能的补充包括 Miller & Blume (2026) 关于 healthcare ML 中 individual-level prediction instability 的诊断框架，以及 Jain et al. (2025, FAccT) 关于 Rashomon set 的 allocation multiplicity 实证研究。\n\n## 主要优势\n- **统计方法诚实透明**：论文始终如一地报告统计限制（power analysis, Bonferroni correction, bootstrap CIs），在 NLP 经验性研究中难能可贵。特别是主动报告 p = .170 不显著而非忽略，体现了良好的学术规范。\n- **实验设计严密**：使用 Wang et al. (2025) 的 controlled model zoo（matched training conditions）是研究架构效应的正确方法，避免了训练数据/超参数差异的混杂。\n- **Appendix 充实**：22 页中 12 页是附录，覆盖了 Jaccard permutation tests、seed calibration、GDN exclusion sensitivity、cross-benchmark analyses、continuous Jaccard、attention weight analysis 等，展示了全面的 robustness checking。\n- **Related Work 全面且定位准确**：引用了 2026 年的最新工作（Mamba-3, Gorbett et al., Haghighat et al.），对 ecological fallacy 和 Rashomon set 的关联讨论得体。\n- **Per-example Jaccard 的 saturation 发现**（Section 4.2）确实有趣：4% attention 即建立完整的 per-example divergence pattern，额外 attention 不改变哪些 examples 被影响。这是一个 clean, well-supported 的经验发现。",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings 级别）\n**一句话总结**: 方法论严谨的经验性分析，系统记录了 hybrid recurrent architectures 间的 per-example 差异，但核心发现是 ecological fallacy 的一个已知实例，最重要的 convergence claim 统计效力不足（n=5, Bonferroni-adjusted p=.170），且唯一有效的应用（routing）仅在 1/4 基准上有效，整体新颖性和影响力不足以支撑 EMNLP 主会议长文。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法得当（permutation test, bootstrap CI），但核心 convergence result 依赖 GDN inclusion 且 n=5 严重欠统计功效；单次训练无法分离 architecture 与 seed effects |\n| Excitement | 2.5/5 | 问题有实际意义，但核心发现（aggregate ≠ individual）是 ecological fallacy 的已知实例，论文自己也承认（Section 2, p.3）；实际应用（routing）效果有限 |\n| Reproducibility | 4/5 | 使用公开 model zoo，方法描述充分，代码承诺公开 |\n| Reviewer Confidence | 4/5 | 熟悉 predictive multiplicity 文献和 hybrid architecture 领域 |\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 核心 convergence claim 统计效力严重不足\n- 具体位置：Table 1（p.6）、Section 4.2（p.7）、Abstract\n- 问题：论文的核心叙事之一是 \"aggregate convergence vs. per-example divergence 的 decoupling\"。但 aggregate convergence 仅在 LAMBADA 上呈现 ρ = −1.0，Bonferroni 校正后 p = .170，未达到常规统计显著性。论文在方法部分（Section 3.5, p.5）也承认 \"with n = 5 ordinal levels, only ρ = ±1.0 achieves p < .05\"。这意味着论文无法在 10 个基准中的 9 个上检测任何趋势，且唯一 \"显著\" 的 LAMBADA 在校正后也不显著。然而 Abstract 和 Introduction 的叙事结构将 decoupling 呈现为一个稳健发现（\"Aggregate trends do not reach statistical significance... yet per-example overlap saturates\"），这种并置暗示了一个比数据支持更强的 pattern。\n- 为什么影响接收：论文的两大贡献之一（per-example saturation + aggregate convergence 的解耦）建立在一个不显著的统计结果上。如果 convergence 本身都不确定，decoupling 的论证基础就不成立。\n- 建议修改方向：(1) 将 decoupling 明确降级为 exploratory/suggestive observation，而非 main contribution；(2) 在 Abstract 中更直接地陈述 convergence result 不显著；(3) 增加 power analysis 说明需要多少 attention ratio 水平才能可靠检测中等效应。\n\n**N2** [critical] GDN 头数混杂变量污染 convergence result\n- 具体位置：Section 4.3（p.8）、Table 1 脚注‡\n- 问题：LAMBADA 上 ρ = −1.0 的 convergence result 依赖于 GDN 的包含。GDN h3-1 使用 16 个 attention head 而所有其他配置使用 32 个。移除 GDN 后，ρ 从 −1.0 降至 −0.7（p = .233），MMLU 的趋势甚至反转（ρ = −0.7 → +0.6）。论文在 Section 4.3 讨论了这一问题，但没有充分论证为何在存在这一混杂变量的情况下仍然可以信任 convergence result。16 vs 32 head 的差异可能单独解释 GDN 的 faster convergence（通过限制 attention capacity），而非反映真正的架构趋势。\n- 为什么影响接收：如果核心 convergence 发现的存废取决于一个有已知混杂变量的架构，那么 decoupling 叙事的基础更加脆弱。论文的第二个贡献（Section 1, 第二个 bullet point）明确将 Jaccard saturation 与 aggregate convergence 的 decoupling 列为贡献，但 convergence 一侧不可靠。\n- 建议修改方向：(1) 将 convergence claim 限定为 conditional on GDN inclusion，并在 contribution statement 中反映；(2) 考虑以 RetNet-HGRN2 pair 的 decoupling 作为 primary evidence（论文提到这个 pair \"preserves the decoupling\"），虽然这会削弱一般性。\n\n**N3** [critical] 单次训练无法分离架构效应与随机种子效应\n- 具体位置：Limitations（p.8-9）、Appendix W（p.21）\n- 问题：每个配置仅有一次训练运行。论文声称观察到的 per-example divergence 来自架构差异，但无法排除训练随机性（不同种子）的贡献。论文的缓解措施——Pythia 70M PolyPythias 的 within-seed Jaccard（0.27-0.39）vs. cross-architecture Jaccard（0.09-0.10）的 3-4× 差异——是有用的校准，但存在严重局限：(a) Pythia 是纯 Transformer 而非 hybrid recurrent model；(b) 70M 与 340M/1.3B 规模差异巨大；(c) 不同模型族的比较不能替代 matched-seed 实验。\n- 为什么影响接收：这是区分 \"architectures cause per-example divergence\" 和 \"any variation in training produces per-example divergence\" 的关键。如果后者为真，本文的贡献就从 \"architectures matter at per-example level\" 降级为 \"training variation matters at per-example level\"，后者已被 D'Amour et al. (2022) 和 McCoy et al. (2020) 充分记录。\n- 建议修改方向：(1) 在至少一个架构上进行 3-5 次不同种子的训练，计算 within-architecture cross-seed Jaccard 作为基线；(2) 如果无法新增实验，至少将所有因果性语言替换为关联性语言（\"is associated with\" vs. \"causes\"），并在 contribution statement 中明确标注此限制。\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 新颖性定位：ecological fallacy 的已知实例\n- 具体位置：Section 2（p.3, 最后一段）\n- 问题：论文诚实地承认 \"The observation that aggregate-level associations can diverge from individual-level patterns is a well-known statistical phenomenon (ecological fallacy; Robinson 1950)\"，并说 \"The contribution lies not in the conceptual observation but in its quantitative characterization.\" 这是准确的自我定位，但也恰好说明了新颖性的局限：本文本质上是用一个 specific model zoo 量化了一个已知现象。将 predictive multiplicity（Marx et al. 2020，原本针对 Rashomon set 内 near-optimal models）的概念扩展到不同架构族是一个合理的延伸，但不够 surprising。\n- 建议：在 Introduction 中更早、更明确地区分 \"what we show for the first time\"（quantitative characterization in hybrid recurrent models）和 \"what is conceptually known\"（ecological fallacy, underspecification），避免读者产生过高的新颖性预期。\n\n**W2** [warning] Confidence-based routing 作为应用价值不足\n- 具体位置：Section 4.1, \"Confidence-based routing\" 段（p.6）\n- 问题：Routing 仅在 LAMBADA 上有效（+5.3pp over majority vote），在 ARC-Easy 上 marginal（+1.0pp），在 HellaSwag 和 PIQA 上无改善。这意味着实际应用仅在 α 最高的 benchmark（0.30）上有效，而在 reasoning tasks（α = 0.14-0.15）上完全失败。论文对此有所讨论，但 routing 仍然被列为 \"proof-of-concept application\"，这对于仅在 1/4 基准上有效的方法而言定位过高。\n- 建议：将 routing 降级为一个 case study / illustrative example，明确讨论为何它在低-α 任务上失败，以及什么条件下 per-example multiplicity 才有实际可利用的价值。\n\n**W3** [warning] Introduction 第一句话过度声称\n- 具体位置：Section 1, 第一句（p.1）\n- 问题：\"Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect nearly disjoint sets of individual examples\" 中 \"nearly disjoint\" 暗示极低的重叠。但实际 Jaccard ≈ 0.10 vs. independence baseline ≈ 0.05，即观测重叠约为独立基线的 2 倍。\"Nearly disjoint\" 在集合论意义上可辩护（90% 非重叠），但忽略了 base rate：random pairs 也会 \"nearly disjoint\"（95% 非重叠）。超出独立基线的 excess overlap 仅约 5 个百分点，且统计显著地高于独立（z > 5.9），这说明架构间有结构化但微弱的共享，而非 \"nearly disjoint\"。\n- 建议：将 \"nearly disjoint\" 替换为更精确的表述，如 \"largely non-overlapping (J ≈ 0.10, approximately 2× independence baseline)\"。\n\n**W4** [warning] 缺乏可操作的实践建议\n- 问题：论文详细记录了 per-example divergence 的存在和量级，但对 practitioners 的 actionable takeaways 不够具体。Conclusion（Section 5, p.8）提到 \"aggregate benchmark equivalence does not guarantee per-example agreement\" 但没有说在什么场景下这 matters enough to change decisions。论文未讨论：(a) 对于什么样的下游任务，15-45% 的 individual prediction 差异是 practically significant 的？(b) 如果用户已经在做 ensemble/multi-seed evaluation，本文的发现是否提供增量信息？\n- 建议：在 Conclusion 或 Discussion 中加入一小段具体指导。\n\n## 小问题（不影响接收）\n- Abstract 中 \"almost entirely different examples\" 与正文 \"at most 10%\" 的表述不一致——前者暗示接近 0% 重叠，但 10% Jaccard 仍然意味着有统计显著的共享结构。\n- Section 3.4 的 helped/hurt/unchanged 分解将 0.51→0.49 的微小变化与 0.99→0.01 的大幅变化等同看待。虽然论文在正文中提到了这一局限并在 Appendix 做了 continuous 分析，但主体叙事完全依赖 binary decomposition。\n- 340M 的分析（Section 4.2, p.8）显示 convergence absent（ρ = −0.50, p = .45），进一步削弱 convergence 发现的普遍性，但这一事实在论文中处理得较为低调。\n- Figure 1 panel (b) y 轴范围较窄（0.06-0.12），视觉上可能夸大 Jaccard 的稳定性。\n- 格式合规：正文 8 页以内 ✓；使用 [review] 模板 ✓；匿名性完整（\\author{Anonymous}，无 self-identifying URL）✓；Limitations 和 Ethics Statement 存在且不计入页数 ✓。\n- 引用格式基本符合 ACL 规范，Related Work 覆盖了 2026 年最新工作。未发现重大遗漏——可能的补充包括 Miller & Blume (2026) 关于 healthcare ML 中 individual-level prediction instability 的诊断框架，以及 Jain et al. (2025, FAccT) 关于 Rashomon set 的 allocation multiplicity 实证研究。\n\n## 主要优势\n- **统计方法诚实透明**：论文始终如一地报告统计限制（power analysis, Bonferroni correction, bootstrap CIs），在 NLP 经验性研究中难能可贵。特别是主动报告 p = .170 不显著而非忽略，体现了良好的学术规范。\n- **实验设计严密**：使用 Wang et al. (2025) 的 controlled model zoo（matched training conditions）是研究架构效应的正确方法，避免了训练数据/超参数差异的混杂。\n- **Appendix 充实**：22 页中 12 页是附录，覆盖了 Jaccard permutation tests、seed calibration、GDN exclusion sensitivity、cross-benchmark analyses、continuous Jaccard、attention weight analysis 等，展示了全面的 robustness checking。\n- **Related Work 全面且定位准确**：引用了 2026 年的最新工作（Mamba-3, Gorbett et al., Haghighat et al.），对 ecological fallacy 和 Rashomon set 的关联讨论得体。\n- **Per-example Jaccard 的 saturation 发现**（Section 4.2）确实有趣：4% attention 即建立完整的 per-example divergence pattern，额外 attention 不改变哪些 examples 被影响。这是一个 clean, well-supported 的经验发现。",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-22T17:26:16.918894+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3818
}
```

</details>

---


### Assistant

_source line 1114 · 2026-05-22T17:26:33.537341+00:00_

审稿意见已提交给 Review Director。

**总结**：Overall 3.0（Findings 级别）。论文的经验分析方法论扎实，统计报告诚实透明，但三个核心问题制约接收：(1) convergence claim 统计效力不足且 Bonferroni 校正后不显著；(2) GDN 头数混杂变量污染主要发现；(3) 单次训练无法分离架构 vs. 种子效应。新颖性方面，core insight 是 ecological fallacy 的已知实例，应用端 routing 仅在 1/4 基准有效。建议修改 convergence claim 的强度定位，补充 multi-seed 实验或改用关联性语言后，可达到 Findings 接收标准。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

4 recorded events


### User

_source line 1115 · 2026-05-22T17:27:48.553024+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见

**Overall**: 3.0 / 5（Findings）
**一句话总结**: 描述性发现有启发性，但核心推断性 claims 受限于极小样本量（n=3 架构、n=5 attention ratios），且主要展示案例 LAMBADA 的 Bonferroni 校正后 p=.170 不显著，构成 overclaiming 风险。

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 描述性分析方法论合理，推断性分析受 n=3~5 严重限制 |
| Excitement | 3/5 | 研究问题新颖且实践相关，但结论多为 suggestive |
| Reproducibility | 4/5 | 公开 model zoo，报告了版本和 seed |

## Must-Fix 问题

**N1** [critical] LAMBADA 作为主要展示案例但统计不显著，存在 overclaiming
- Abstract、§4.2、Table 1、Figures 1-2
- Bonferroni 校正后 p = .170 不显著。即使单侧检验校正后仍为 p = .083。论文在承认不显著的同时将 LAMBADA 作为标题级发现的主要证据，构成 framing 层面的 overclaiming。
- 建议：(1) 弱化 LAMBADA convergence 叙述，强调 per-example Jaccard saturation 的描述性发现；(2) 将四个 benchmark 的平均效应作为主要证据；(3) 明确标注为 "suggestive but not statistically significant after correction"。

**N2** [critical] GDN h3-1 的 16-head confound
- §4.3、Appendix D.2, Table 3
- 排除 GDN 后 LAMBADA ρ 从 −1.0 弱化为 −0.7（p=.233），MMLU 反转为 +0.6。
- 建议：将 sensitivity analysis 提升到主文，同时报告 with/without GDN 结果。

**N3** [critical] Bootstrap CI 基于 n=3 架构 resampling 统计可靠性存疑
- §3.5、Appendix D.1、Figure 2
- Resampling pool 仅 3³=27 种组合，排除退化样本后有效样本约 24 个。CI 给读者统计严谨的错觉但可靠性极低。
- 建议：明确声明 n=3 bootstrap CI 仅供参考，Figure 2 的 CI band 附注 "illustrative only"。

## Should-Fix 问题

**W1** n=5 permutation test power limitation 应更突出
- §3.5
- 完全无法检测 |ρ|=0.8-0.9 的强相关。建议声明所有 Spearman correlation 推断应视为 descriptive/exploratory。

**W2** 单次训练 run 无法分离 architecture 和 seed effect
- Limitations
- Pythia/PolyPythias 校准有局限（不同架构族、不同规模）。

**W3** 二值化 decomposition 的信息损失
- §3.4、Appendix O
- 0.51→0.49 与 0.99→0.01 被等同对待。主文应讨论 trade-off 并指向 Appendix O。

**W4** 架构覆盖面有限，标题暗示更广泛适用性
- 只有 3 个架构，缺 Mamba/RWKV/生成任务。标题建议加限定词。

**W5** Routing 分析实验设计较弱
- §6 第二段
- 仅 LAMBADA 有效（+5.3pp），缺少 ensemble averaging 或 random routing baseline。

## 小问题
- §3.3 convergence ratio 分母为零时的处理未说明
- Table 1 脚注对 ratio 列的影响未明确
- Figure 1(b) y 轴未指明是 helped 还是 hurt 的 Jaccard
- HGRN2 net benefit claim 仅在 LAMBADA 上验证
- Appendix X 的 GLA 分析使用 340M 与主实验 1.3B 不完全可比

## 主要优势
- 研究问题新颖重要
- 方法论透明度高（主动报告统计局限）
- 描述性发现扎实（Jaccard saturation 不依赖小 n）
- 实验控制质量高
- 附录深度突出（13 页，多方向 robustness check）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1116 · 2026-05-22T17:29:52.384035+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n### Must-Fix 交叉回应\n\n**[AGREE] R1-N1: LAMBADA convergence 的 overclaiming**\n与我的 N1 完全一致。Bonferroni 校正后 p = .170 不显著。补充：即使论文数值上诚实报告了 p = .170，Abstract 中 \"Aggregate trends do not reach statistical significance... yet per-example overlap saturates\" 的并置结构在修辞上仍暗示了 robust decoupling。R1 建议以四个 benchmark 平均效应作为主要证据是建设性的。Per-example Jaccard saturation 本身（Section 4.2: \"approximately 0.095 for helped, with no further increase\"）是描述性发现，不依赖 convergence 显著性，可独立成立。建议重构叙事以 Jaccard saturation 为主线。\n\n**[AGREE] R1-N2: GDN 16-head confound**\n与我的 N2 完全一致。补充：Table 1 脚注‡的 16-head 信息过于隐蔽，但它直接决定了 ρ 从 −1.0 变为 −0.7。应在主文中并列 report with/without GDN 结果。\n\n**[AGREE] R1-N3: Bootstrap CI 基于 n=3 resampling 可靠性存疑**\nR1 独到发现，我未独立提出。论文在 Section 3.5 有声明 \"heuristic indicators\"，但 Figure 2 的 CI band 视觉上给人统计严谨的印象。27 个 bootstrap 样本的 CI 几乎无可靠覆盖率保证。建议 Figure 2 标注 \"illustrative only\"。\n\n### Should-Fix 交叉回应\n\n**[AGREE] R1-W1**: 与我的 N1 子论点一致。\n**[AGREE] R1-W2**: 与我的 N3 一致。我列为 Must-Fix，R1 列为 Should-Fix，我认为这是更严重的问题。\n**[AGREE] R1-W3**: 与我的小问题一致。建议主文加一段总结 Appendix O continuous 分析。\n**[REBUT] R1-W4**: 标题本身符合 NLP 论文惯例（参考 D'Amour et al. 2022 标题）。真正需要修改的是正文中的泛化性措辞——在 Introduction 和 Conclusion 中更频繁限定为 \"the three architectures studied\"。\n**[AGREE] R1-W5**: 与我的 W2 一致。R1 补充了缺少 ensemble averaging 和 random routing baseline 的具体问题，有价值。\n\n### 总结\nR1 与 R2 核心判断高度一致：Overall 3.0, Findings。独立识别出相同三个核心问题。R1 额外的 bootstrap CI 发现（N3）是有价值的补充。主要分歧仅在 W4（标题）。\n\n建议作者修改重点：(1) 重构叙事以 Jaccard saturation 描述性发现为主线；(2) 主文并列 with/without GDN 结果；(3) 补充 multi-seed baseline 或全面弱化因果性语言。",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n### Must-Fix 交叉回应\n\n**[AGREE] R1-N1: LAMBADA convergence 的 overclaiming**\n与我的 N1 完全一致。Bonferroni 校正后 p = .170 不显著。补充：即使论文数值上诚实报告了 p = .170，Abstract 中 \"Aggregate trends do not reach statistical significance... yet per-example overlap saturates\" 的并置结构在修辞上仍暗示了 robust decoupling。R1 建议以四个 benchmark 平均效应作为主要证据是建设性的。Per-example Jaccard saturation 本身（Section 4.2: \"approximately 0.095 for helped, with no further increase\"）是描述性发现，不依赖 convergence 显著性，可独立成立。建议重构叙事以 Jaccard saturation 为主线。\n\n**[AGREE] R1-N2: GDN 16-head confound**\n与我的 N2 完全一致。补充：Table 1 脚注‡的 16-head 信息过于隐蔽，但它直接决定了 ρ 从 −1.0 变为 −0.7。应在主文中并列 report with/without GDN 结果。\n\n**[AGREE] R1-N3: Bootstrap CI 基于 n=3 resampling 可靠性存疑**\nR1 独到发现，我未独立提出。论文在 Section 3.5 有声明 \"heuristic indicators\"，但 Figure 2 的 CI band 视觉上给人统计严谨的印象。27 个 bootstrap 样本的 CI 几乎无可靠覆盖率保证。建议 Figure 2 标注 \"illustrative only\"。\n\n### Should-Fix 交叉回应\n\n**[AGREE] R1-W1**: 与我的 N1 子论点一致。\n**[AGREE] R1-W2**: 与我的 N3 一致。我列为 Must-Fix，R1 列为 Should-Fix，我认为这是更严重的问题。\n**[AGREE] R1-W3**: 与我的小问题一致。建议主文加一段总结 Appendix O continuous 分析。\n**[REBUT] R1-W4**: 标题本身符合 NLP 论文惯例（参考 D'Amour et al. 2022 标题）。真正需要修改的是正文中的泛化性措辞——在 Introduction 和 Conclusion 中更频繁限定为 \"the three architectures studied\"。\n**[AGREE] R1-W5**: 与我的 W2 一致。R1 补充了缺少 ensemble averaging 和 random routing baseline 的具体问题，有价值。\n\n### 总结\nR1 与 R2 核心判断高度一致：Overall 3.0, Findings。独立识别出相同三个核心问题。R1 额外的 bootstrap CI 发现（N3）是有价值的补充。主要分歧仅在 W4（标题）。\n\n建议作者修改重点：(1) 重构叙事以 Jaccard saturation 描述性发现为主线；(2) 主文并列 with/without GDN 结果；(3) 补充 multi-seed baseline 或全面弱化因果性语言。",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1117 · 2026-05-22T17:29:56.048577+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3664
}
```

</details>

---


### Assistant

_source line 1118 · 2026-05-22T17:30:01.718276+00:00_

交叉回应已提交。

与 R1 在核心判断上高度一致（Overall 3.0, Findings），7 条 Must-Fix/Should-Fix 中 6 条 AGREE，唯一 REBUT 是标题问题（W4）——标题本身符合惯例，需要修改的是正文措辞而非标题。R1 的 bootstrap CI 可靠性问题（N3）是我未独立发现的有价值补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

96 recorded events


### User

_source line 1119 · 2026-05-23T13:13:16.808442+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work + 写作质量**。

## Venue 信息
- **目标**: EMNLP 2026 (Long Paper, via ACL Rolling Review)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入页数（但不能含过多额外内容）
- **模板**: ACL 两栏格式，必须使用 `[review]` 选项
- **匿名规则**: Double-blind
- **附录**: 允许，不参与审稿评分

## 论文路径
- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`
- 各章节在 `sections/` 子目录: `introduction.tex`, `method.tex`, `experiments.tex`, `related_work.tex`, `conclusion.tex`, `appendix.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/submitted.pdf`

## 你的审查侧重

请从新颖性、学术贡献、完整性和写作质量角度审查，重点关注：

1. **新颖性与贡献**：
   - 核心发现（per-example multiplicity across architectures）相对于已有文献（Marx 2020, D'Amour 2022, McCoy 2020）的增量贡献有多大？
   - 论文是否只是将已知框架（predictive multiplicity）应用到新数据（hybrid recurrent models）？这是否构成足够的贡献？
   - "Ecological fallacy" 的承认是否削弱了贡献的新颖性？
   - 对 EMNLP 社区的影响力和实际价值如何？

2. **Related Work 覆盖**：
   - 是否遗漏了重要的相关工作？特别注意：
     - Model multiplicity / Rashomon set 领域的最新进展
     - Hybrid architecture 评估的最新进展
     - Ensemble diversity 文献
     - 2025-2026 年的新论文
   - 引用是否真实？是否有可能的幻觉引用？
   - 与现有工作的差异化是否清晰？

3. **写作质量**：
   - 论述逻辑是否清晰连贯？
   - Abstract 是否准确反映论文内容？是否在 200 words 以内？
   - 因果 vs 相关性语言的使用是否恰当？（论文已做大量修改，是否仍有遗漏？）
   - 术语是否一致？定义是否清晰？
   - 结论是否与证据匹配（避免 overclaiming）？

4. **完整性**：
   - 是否有重要但缺失的实验或分析？
   - Limitations 是否充分覆盖主要局限？（注意 EMNLP 规则：~3 点即可）
   - 主文与附录的分工是否合理？
   - Conclusion 的 practitioner implications 是否有实验支撑？

5. **格式合规**：
   - 正文是否在 8 页以内？
   - Limitations section 是否存在且格式正确？
   - 匿名要求是否满足？
   - ACL 模板使用是否正确？

请输出结构化审稿意见：Summary → Strengths → Weaknesses（按严重程度排序：Must-Fix / Should-Fix / Nice-to-Have）→ Questions → Missing References → Overall Assessment（含评分和置信度）。

评分参考（EMNLP 2026 ARR 标准）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1120 · 2026-05-23T13:13:27.369422+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
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

_source line 1121 · 2026-05-23T13:13:27.721175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-23T13:13:33.653817+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-23T13:13:34.611829+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-23T13:13:35.063602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1125 · 2026-05-23T13:13:35.817934+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.0}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.4}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 476.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 395.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"si
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2164
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-23T13:13:35.818429+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{caption}
17	
18	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Practitioners select among hybrid linear recurrent architectures using aggregate benchmarks, but these scores can mask per-example consequences. Across three controlled designs, adding attention affects substantially different examples per architecture (Jaccard $\approx$ 0.10, approximately twice the independence baseline); validation across five architectures and ten pairwise comparisons confirms this on all four benchmarks (all $p < .01$). Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects and find that this predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) rather than attention dose. Aggregate trends do not reach statistical significance ($n = 5$; Bonferroni-adjusted $p = .170$), yet per-example overlap saturates at 4\% attention and remains flat across all four benchmarks. Majority vote fails to exploit this complementarity, confirming that configurations interchangeable by aggregate metrics carry hidden per-example consequences. Confidence-informed routing extracts 36\% of oracle complementarity on LAMBADA ($+5.3$\,pp), suggesting these differences are partially actionable.
27	\end{abstract}
28	
29	\input{sections/introduction}
30	
31	\input{sections/related_work}
32	
33	\input{sections/method}
34	
35	\input{sections/experiments}
36	
37	\input{sections/conclusion}
38	
39	\section*{Limitations}
4
…[truncated 1407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 1127 · 2026-05-23T13:13:43.074029+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here are the key details:

## Reviewer Guidelines

Reviewers are asked to: (1) read the paper and get the first impression, (2) search for related work, and should state in the review if they did not check some major parts. There is a check on academic conflicts of interest, and reviewers should recuse themselves if the submission is very close to their own work.

Reviewers are provided with a checklist to flag problems that other people m
…[truncated 972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8462
}
```

</details>

---


### Tool call

_source line 1128 · 2026-05-23T13:13:49.861841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-23T13:13:50.519399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-23T13:13:50.519840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-23T13:13:50.971709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1132 · 2026-05-23T13:13:51.826091+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-23T13:13:51.827338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-23T13:13:51.827679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-23T13:13:52.380039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-23T13:13:52.782773+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1137 · 2026-05-23T13:13:52.783170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1138 · 2026-05-23T13:13:53.737545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-23T13:13:53.740712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-23T13:13:53.741103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 1141 · 2026-05-23T13:13:54.293315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1142 · 2026-05-23T13:13:54.746046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1143 · 2026-05-23T13:13:54.746478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1144 · 2026-05-23T13:13:55.600030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool result

_source line 1145 · 2026-05-23T13:13:55.600792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 1146 · 2026-05-23T13:13:55.651271+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-23T13:13:57.108611+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1148 · 2026-05-23T13:13:57.159343+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. I need the exact criteria names, score ranges, and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. I need the exact criteria names, score ranges, and what each score means."
  }
}
```

</details>

---


### Tool result

_source line 1149 · 2026-05-23T13:14:04.202135+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments: 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all claims."
- **3**: "Acceptable: Sufficient support for main claims with minor gaps."
- **2**: "Poor: Main claims lack sufficient support; major technical problems."
- **1**: "Major Issues: Not sufficiently thorough for publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points."
- **2**: "Potentially Interesting: does not resonate with me personally."
- **1**: "Not Exciting: limited relevance to computational linguistics."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce results."
- **3**: "Could reproduce with some difficulty."
- **2**: "Would be hard pressed to reproduce."
- **1**: "Would not be able to reproduce."

## 6. **Dataset
…[truncated 513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7042
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-23T13:14:21.808731+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/submitted.pdf",
  "project": "entrainment_gated_ft",
  "pages": "11-21",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/submitted.pdf",
    "project": "entrainment_gated_ft",
    "pages": "11-21",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1151 · 2026-05-23T13:14:22.914227+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1152 · 2026-05-23T13:14:23.366371+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 417.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 424.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.2}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.2}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_16/_pdf_images/submitted_p19.png\", \"width\": 1241, \"he
…[truncated 709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1557
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-23T13:14:23.366991+00:00_

1	\section{Introduction}
2	
3	Hybrid recurrent architectures that appear equivalent by aggregate benchmarks affect largely non-overlapping sets of individual examples: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: on LAMBADA, cross-architecture standard deviation drops 79\% as attention increases (Bonferroni-adjusted $p = .170$, BCa CI $[-1.0, -0.7]$), but each architecture reaches similar accuracy by gaining and losing accuracy on different inputs. Practitioners increasingly choose between recurrent backbones based on aggregate benchmark scores. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Most evaluations of hybrid architectures compare aggregate accuracy, which can mask per-example behavioral diversity. Prior work on predictive multiplicity \citep{marx2020predict
…[truncated 4576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-23T13:14:23.417517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---
