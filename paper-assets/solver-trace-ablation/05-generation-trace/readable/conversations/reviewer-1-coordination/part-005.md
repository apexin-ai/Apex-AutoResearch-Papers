# Reviewer 1 coordination — Part 5 of 5

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../reviewer-1-coordination.md) · [Structured JSON](../../../sessions/8b/8b96db1c4aff6dbb058e.json)

## Round 62

### Tool call

_source line 2230 · 2026-05-22T23:29:51.419334+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n### Paper Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量形式化输出中每个组件的必要性比例。论文在 Qwen3-4B 上跨 6 种 reward 条件（exec-only, ISR β=0.1, Random β=0.1, SFT, Shuffled-ISR, ISR β=0.3）、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行了实验，构建了 8 类 hacking 分类体系，并实证展示了 ISR 作为 reward 信号时的 Goodhart 效应（ISR 从 0.64 崩溃至 0.003）。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: STA 诊断工具和 hacking 分类体系有真正的方法论贡献，但单模型（Qwen3-4B）+ 低种子数（N=3，其中一个异常）的实验设计显著削弱了统计结论的可靠性，cross-dataset 证据未达显著性，整体证据链不足以支撑 conference-level 的通用性声称。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 方法论设计合理，但 N=3 seeds（1个异常）+ within-seed 独立性假设可疑 + premise-count confound 未解决（McNemar p=0.317）显著削弱统计基础 |\n| Excitement | 3.5 / 5 | 问题重要且时机恰当；STA 工具简洁实用；8-mode taxonomy 是有价值的贡献；Goodhart 效应观察清晰。但单模型限制了 impact |\n| Reproducibility | 4 / 5 | 超参数详尽（Appendix A Table 3），使用公开模型/数据集，承诺开源。Seed 43 的 T=0.7 是已知差异 |\n| Confidence | 4 / 5 | 仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单模型实验无法支撑通用性声称\n- 具体位置：Title、Abstract（\"GRPO-Trained Neurosymbolic Reasoning\"）、Section 1 Contributions C1（\"a model-agnostic diagnostic method\"）、Section 5 Conclusion（\"applicable in principle to any RL system\"）\n- 问题：论文成功运行的唯一模型是 Qwen3-4B。Qwen3-8B 在两种配置下均未收敛（Appendix E.7, Table 14），LLaMA-3.2-3B 在 FOL 生成能力上完全失败（Appendix E.4）。标题和摘要使用泛化表述（\"GRPO-Trained Neurosymbolic Reasoning\"），而非限定于\"Qwen3-4B\"。虽然 C1 声称的 model-agnostic 是指方法设计而非实验验证，但读者会合理期待至少在两个不同架构上看到实证。\n- 为什么影响接收：Reviewer 和 AC 会质疑：如果方法只在一个模型上验证，如何确信观察到的 structural degeneration 是 GRPO 的普遍特性，而非 Qwen3-4B 的特殊行为？cross-scale 和 cross-architecture 的全面失败反而暗示了后者的可能性。\n- 建议修改方向：(1) 将标题/摘要的 scope 严格限定为 Qwen3-4B case study；(2) 或增加至少一个成功收敛的替代架构（如 Mistral-7B、Gemma-2-2B）的实验数据。\n\n**N2** [critical] N=3 seeds 的统计效力严重不足，尤其面对 bimodal dynamics\n- 具体位置：Section 4.1（3-seed 设计）、Section 4.3（bimodal seed-dependence）、Table 13（N=2 sensitivity）\n- 问题：论文发现 exec-only 条件下存在 bimodal convergence（3/5 seeds 收敛，2/5 不收敛），这恰恰是最需要更多 seeds 来表征分布的场景。主实验只用 3 seeds，随后补充的 seeds 45-46 仅用于探查 bimodal 模式，而非复制核心 ISR 发现。N=2 sensitivity analysis（排除 seed 43）在统计上几乎没有意义——无法对 2 个数据点做有意义的推断。Limitations Section 6 承认\"three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance\"，但正文的统计检验（χ²、CMH、Fisher）仍然建立在这一不充分的基础上。\n- 为什么影响接收：Multi-attractor dynamics 的刻画需要足够的样本来估计 attractor basin 的大小和转换概率。3 seeds 只能说明现象存在，无法量化其普遍性。正文中的 confidence intervals 和 p-values 在此 N 下可能有误导性。\n- 建议修改方向：(1) 将 seed 数增至 8-10 per condition，至少对 exec-only 和 ISR β=0.1 两个核心条件执行；(2) 或将所有基于 seed-level 变异性的声称降级为 \"preliminary observation\"，不做定量统计推断。\n\n**N3** [critical] CMH 检验的 within-seed 独立性假设不成立\n- 具体位置：Section 5 Statistical Considerations、Appendix C Table 6\n- 问题：CMH 检验将 seed 作为 stratum，但 stratum 内的 samples（同一 GRPO checkpoint 生成的多个 formalization）共享模型权重，不是独立观测。这违反了 CMH 的基本假设。论文添加了 caveat（\"CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is N=3\"），但仍然报告了 CMH p-values 并基于它们做推断。如果 within-seed correlation ρ>0（几乎必然如此），实际有效样本量远小于报告的 n=231，所有 p-values 都被严重膨胀。\n- 为什么影响接收：这不仅是一个 caveat 问题，而是整个统计推断框架的有效性问题。读者看到 p<10^-38 会获得虚假的确定性感。\n- 建议修改方向：(1) 使用 cluster-robust standard errors 或 GEE（Generalized Estimating Equations）以 seed 为 cluster 来正确处理组内相关；(2) 或至少报告 seed-level aggregate statistics（每个 seed 一个数据点，N=3 或 N=5）的 permutation test 或 bootstrap CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 的 T=0.7 采样异常破坏了实验一致性\n- 具体位置：Section 4.1 脚注 5、Appendix A Table 3、Appendix E.6 Table 13\n- 问题：Seed 43 使用 T=0.7 sampling 而非 greedy decoding。这意味着 seed 43 的评估分布与 seeds 42/44 系统性不同——不仅是随机变异，而是评估协议的改变。论文将其标注为\"not strictly comparable\"但仍然纳入所有主表分析。为何不用 greedy decoding 重新评估 seed 43？这在计算上应该是低成本的（只需要重新运行 inference，不需要重新训练）。\n- 建议：用 greedy decoding 重新评估 seed 43 的 checkpoint，或在主表中明确标记 seed 43 的数据为参考值而非正式结果。\n\n**W2** [warning] Premise-count confound 未能统计解决\n- 具体位置：Section 4.2（第 6 页底部）、Appendix C Table 5、Table 9\n- 问题：论文承认\"formalizations with fewer components mechanistically receive higher ISR\"（Section 3.2）。premise-count-matched comparison 显示 scalar ISR advantage 不显著（McNemar p=0.317, Table 9）。这意味着论文**无法将 ISR 差异从 premise-count 效应中分离**。论文说\"confirming that the scalar ISR advantage is not statistically significant\"并转向\"mode composition analysis (CE) is unaffected\"。但 ISR 作为核心指标的标量值如果受 premise-count 混淆，整个诊断的定量维度就被削弱了。\n- 建议：(1) 对 ISR 做 premise-count normalization（如 ISR_adjusted = ISR / expected_ISR_given_n_premises）；(2) 或明确将 ISR 降级为二分类指标（hacking/non-hacking），不解读其标量值。\n\n**W3** [warning] ProofFOL cross-dataset 证据不显著（p=0.10）\n- 具体位置：Section 4.4（第 7 页）、Table 11\n- 问题：ProofFOL 作为 cross-dataset 证据的关键实验，其 genuine-rate permutation test p=0.10 不显著。论文称之为\"exploratory, underpowered, directional\"。但在只有两个数据集的情况下，唯一的 cross-dataset 实验不显著，严重削弱了 C3 contribution（\"cross-benchmark evidence characterizing the structural manifestation of Goodhart's law\"）的说服力。此外，ProofFOL 本身是 GPT-4o 翻译的 silver-standard 数据（只有 59.1% 通过率），数据质量存疑。\n- 建议：(1) 降低 C3 的声称强度，将 ProofFOL 明确定位为 pilot experiment；(2) 讨论 silver-standard 数据质量对结论的具体影响路径。\n\n**W4** [warning] ISR 作为 Shapley value 特例的定位需要更精确\n- 具体位置：Section 3.2（第 4 页）\n- 问题：论文称 ISR 是\"Shapley value restricted to the (n-1)-coalition\"，将复杂度从 O(2^n) 降至 O(n)。但 Shapley value 的核心价值在于考虑**所有联盟大小**的边际贡献，(n-1)-coalition restriction 本质上是 LOO，丢失了组件间的交互效应。例如：如果 premise A 和 B 可互相替代（单独移除任一个都不破坏证明），LOO 会将两者都标记为\"不必要\"，但证明确实使用了结构化推理。论文用 \"binary solver output makes LOO sufficient\" 来辩护，但这只对\"individually necessary\"成立，不覆盖\"jointly redundant but individually useful\"的情况。\n- 建议：明确讨论 LOO 相对于 full Shapley 的局限（misses complementary effects），并量化这种 edge case 在实际数据中的频率。\n\n**W5** [warning] Hacking taxonomy 的分类器召回率未报告\n- 具体位置：Section 5（第 5 页）、Appendix D（第 15 页）\n- 问题：Text-match classifier 的 precision 通过 50 例人工验证估计为 >95%，但 recall 被承认\"inherently bounded by the text-match threshold\"且未量化。这意味着 hacking 的实际普遍性可能被低估——有多少 hacking instances 逃过了 text-match 分类器？functional analysis（per-sample n_taxonomy 分析）作为第二阶段，覆盖了什么样的 false negatives？\n- 建议：(1) 报告 recall 的下限估计（如：在 random sample 中，有多少 functional hacking 被 text-match 漏检？）；(2) 或提供 text-match 与 functional-analysis 的一致性分析。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 的 ISR 公式（Eq. 1）中 S(x) 和 f_s 的定义可以更早引入，当前首次出现时缺乏上下文。\n- Figure 1 的 legend 中 \"ISR β=0.1 (s44)\" 等标注方式不直观——读者需要查 Appendix 才能知道 s44 是 seed 44。\n- Table 1 脚注中 \"†Seed 42 only\" 和 \"‡\" 标记密集，建议简化。\n- Appendix D 的 hacking mode 定义使用了 Prolog 示例（如 D.9 Query-as-fact gaming），但主文 Section 4 的分析主要在 FOL 上，跨语言对应关系可以更清晰。\n- Section 2 Related Work 的最后一段（Reward hacking and Goodhart's Law）引用密度很高但缺少对各引用具体贡献的区分——可以适当精简。\n\n---\n\n## Questions for Authors\n\n1. **Seed 43 重新评估**：为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？这在计算上应该是低成本的，可以消除 T=0.7 的混淆。\n\n2. **Effective sample size**：是否可以报告 within-seed ICC (intraclass correlation coefficient) 来量化组内相关性？这会让读者判断 CMH p-values 的真实可靠度。\n\n3. **ISR 与 NLI accuracy 的相关性**：Appendix C 提到 ISR \"does not correlate with NLI accuracy\"。但 ISR 的设计目标是衡量 structural quality，如果它与 downstream task performance 无关，那它作为诊断工具的实际价值是什么？请阐明 ISR 的 intended use case——它应该在什么场景下被使用，它的 actionable insight 是什么？\n\n4. **Multiplicative vs. additive reward**：论文使用 r_exec × (1+β×ISR) 的乘法形式。是否测试过加法形式（r_exec + β×ISR）？乘法形式中只有 proved samples 获得 ISR bonus，这可能导致 reward landscape 的特殊结构。\n\n5. **8 种 hacking modes 的相互排斥性**：Table 7 将每个 sample 分配到一个 mode。但 Appendix D.1-D.9 的定义中，某些 modes 似乎可以共存（如 premise-subset gaming + conclusion embedding）。分类是否强制互斥？如果一个 sample 符合多个 modes，如何处理？\n\n---\n\n## Missing References\n\n- Lanham et al., 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" — 与 STA 的 component necessity testing 理念高度相关，但论文未讨论 CoT faithfulness 与 solver trace 结构完整性的联系。\n- Turpin et al., 2023 \"Language Models Don't Always Say What They Think\" — 关于 model output 与 internal reasoning 的 disconnect，与 ISR 的 observe-vs-optimize asymmetry 直接相关。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**：识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点——结构退化在 prove rate 不变甚至上升时发生。这是一个真实且重要的问题（Section 1, Figure 1）。\n\n2. **方法简洁且无需训练**：STA 只需要对 solver input 做逐一消融，不涉及模型内部、不需要额外训练、不依赖人工标注，计算成本 O(n) per sample。这使其容易被其他研究者采用。\n\n3. **Hacking taxonomy 的系统性**：8 种 degeneration mode 的分类（Appendix D）附有 FOL/Prolog 示例和 ISR interaction 分析，是该领域首个系统性的分类尝试。Table 7-8 的 per-mode 统计和分类器精度验证增加了可信度。\n\n4. **控制实验设计合理**：Random control（β=0.1, uniform random ISR）、Shuffled-ISR（打乱 ISR 赋值）和 SFT baseline 三个控制条件有效分离了 reward signal 的因果效应。特别是 Shuffled-ISR 控制表明 ISR 的 degeneration 不是任意 auxiliary reward 的 artifact。\n\n5. **透明度高**：论文对自身局限的坦诚（seed 43 异常、N=3 不足、within-seed independence caveat、ProofFOL p=0.10、单模型限制）在该领域论文中罕见，有利于后续研究的准确定位。\n\n---\n\n**Final Scores Summary**:\n- Soundness: 3.0/5\n- Excitement: 3.5/5  \n- Overall Assessment: 3.0/5 (Findings)\n- Confidence: 4/5\n- Reproducibility: 4/5",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n### Paper Summary\n\n本文提出 Solver Trace Ablation (STA)，一种基于 Leave-One-Out (LOO) 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 系统中的结构退化。核心指标 ISR（Intensional Structural Reward）衡量形式化输出中每个组件的必要性比例。论文在 Qwen3-4B 上跨 6 种 reward 条件（exec-only, ISR β=0.1, Random β=0.1, SFT, Shuffled-ISR, ISR β=0.3）、两种逻辑类型（FOL/Prolog）和两个数据集（FOLIO/ProofFOL）进行了实验，构建了 8 类 hacking 分类体系，并实证展示了 ISR 作为 reward 信号时的 Goodhart 效应（ISR 从 0.64 崩溃至 0.003）。\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 (Findings)\n**一句话总结**: STA 诊断工具和 hacking 分类体系有真正的方法论贡献，但单模型（Qwen3-4B）+ 低种子数（N=3，其中一个异常）的实验设计显著削弱了统计结论的可靠性，cross-dataset 证据未达显著性，整体证据链不足以支撑 conference-level 的通用性声称。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0 / 5 | 方法论设计合理，但 N=3 seeds（1个异常）+ within-seed 独立性假设可疑 + premise-count confound 未解决（McNemar p=0.317）显著削弱统计基础 |\n| Excitement | 3.5 / 5 | 问题重要且时机恰当；STA 工具简洁实用；8-mode taxonomy 是有价值的贡献；Goodhart 效应观察清晰。但单模型限制了 impact |\n| Reproducibility | 4 / 5 | 超参数详尽（Appendix A Table 3），使用公开模型/数据集，承诺开源。Seed 43 的 T=0.7 是已知差异 |\n| Confidence | 4 / 5 | 仔细阅读全文含全部附录，熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 单模型实验无法支撑通用性声称\n- 具体位置：Title、Abstract（\"GRPO-Trained Neurosymbolic Reasoning\"）、Section 1 Contributions C1（\"a model-agnostic diagnostic method\"）、Section 5 Conclusion（\"applicable in principle to any RL system\"）\n- 问题：论文成功运行的唯一模型是 Qwen3-4B。Qwen3-8B 在两种配置下均未收敛（Appendix E.7, Table 14），LLaMA-3.2-3B 在 FOL 生成能力上完全失败（Appendix E.4）。标题和摘要使用泛化表述（\"GRPO-Trained Neurosymbolic Reasoning\"），而非限定于\"Qwen3-4B\"。虽然 C1 声称的 model-agnostic 是指方法设计而非实验验证，但读者会合理期待至少在两个不同架构上看到实证。\n- 为什么影响接收：Reviewer 和 AC 会质疑：如果方法只在一个模型上验证，如何确信观察到的 structural degeneration 是 GRPO 的普遍特性，而非 Qwen3-4B 的特殊行为？cross-scale 和 cross-architecture 的全面失败反而暗示了后者的可能性。\n- 建议修改方向：(1) 将标题/摘要的 scope 严格限定为 Qwen3-4B case study；(2) 或增加至少一个成功收敛的替代架构（如 Mistral-7B、Gemma-2-2B）的实验数据。\n\n**N2** [critical] N=3 seeds 的统计效力严重不足，尤其面对 bimodal dynamics\n- 具体位置：Section 4.1（3-seed 设计）、Section 4.3（bimodal seed-dependence）、Table 13（N=2 sensitivity）\n- 问题：论文发现 exec-only 条件下存在 bimodal convergence（3/5 seeds 收敛，2/5 不收敛），这恰恰是最需要更多 seeds 来表征分布的场景。主实验只用 3 seeds，随后补充的 seeds 45-46 仅用于探查 bimodal 模式，而非复制核心 ISR 发现。N=2 sensitivity analysis（排除 seed 43）在统计上几乎没有意义——无法对 2 个数据点做有意义的推断。Limitations Section 6 承认\"three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance\"，但正文的统计检验（χ²、CMH、Fisher）仍然建立在这一不充分的基础上。\n- 为什么影响接收：Multi-attractor dynamics 的刻画需要足够的样本来估计 attractor basin 的大小和转换概率。3 seeds 只能说明现象存在，无法量化其普遍性。正文中的 confidence intervals 和 p-values 在此 N 下可能有误导性。\n- 建议修改方向：(1) 将 seed 数增至 8-10 per condition，至少对 exec-only 和 ISR β=0.1 两个核心条件执行；(2) 或将所有基于 seed-level 变异性的声称降级为 \"preliminary observation\"，不做定量统计推断。\n\n**N3** [critical] CMH 检验的 within-seed 独立性假设不成立\n- 具体位置：Section 5 Statistical Considerations、Appendix C Table 6\n- 问题：CMH 检验将 seed 作为 stratum，但 stratum 内的 samples（同一 GRPO checkpoint 生成的多个 formalization）共享模型权重，不是独立观测。这违反了 CMH 的基本假设。论文添加了 caveat（\"CMH treats within-seed samples as independent observations from a single trained model, so the true replication count is N=3\"），但仍然报告了 CMH p-values 并基于它们做推断。如果 within-seed correlation ρ>0（几乎必然如此），实际有效样本量远小于报告的 n=231，所有 p-values 都被严重膨胀。\n- 为什么影响接收：这不仅是一个 caveat 问题，而是整个统计推断框架的有效性问题。读者看到 p<10^-38 会获得虚假的确定性感。\n- 建议修改方向：(1) 使用 cluster-robust standard errors 或 GEE（Generalized Estimating Equations）以 seed 为 cluster 来正确处理组内相关；(2) 或至少报告 seed-level aggregate statistics（每个 seed 一个数据点，N=3 或 N=5）的 permutation test 或 bootstrap CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 的 T=0.7 采样异常破坏了实验一致性\n- 具体位置：Section 4.1 脚注 5、Appendix A Table 3、Appendix E.6 Table 13\n- 问题：Seed 43 使用 T=0.7 sampling 而非 greedy decoding。这意味着 seed 43 的评估分布与 seeds 42/44 系统性不同——不仅是随机变异，而是评估协议的改变。论文将其标注为\"not strictly comparable\"但仍然纳入所有主表分析。为何不用 greedy decoding 重新评估 seed 43？这在计算上应该是低成本的（只需要重新运行 inference，不需要重新训练）。\n- 建议：用 greedy decoding 重新评估 seed 43 的 checkpoint，或在主表中明确标记 seed 43 的数据为参考值而非正式结果。\n\n**W2** [warning] Premise-count confound 未能统计解决\n- 具体位置：Section 4.2（第 6 页底部）、Appendix C Table 5、Table 9\n- 问题：论文承认\"formalizations with fewer components mechanistically receive higher ISR\"（Section 3.2）。premise-count-matched comparison 显示 scalar ISR advantage 不显著（McNemar p=0.317, Table 9）。这意味着论文**无法将 ISR 差异从 premise-count 效应中分离**。论文说\"confirming that the scalar ISR advantage is not statistically significant\"并转向\"mode composition analysis (CE) is unaffected\"。但 ISR 作为核心指标的标量值如果受 premise-count 混淆，整个诊断的定量维度就被削弱了。\n- 建议：(1) 对 ISR 做 premise-count normalization（如 ISR_adjusted = ISR / expected_ISR_given_n_premises）；(2) 或明确将 ISR 降级为二分类指标（hacking/non-hacking），不解读其标量值。\n\n**W3** [warning] ProofFOL cross-dataset 证据不显著（p=0.10）\n- 具体位置：Section 4.4（第 7 页）、Table 11\n- 问题：ProofFOL 作为 cross-dataset 证据的关键实验，其 genuine-rate permutation test p=0.10 不显著。论文称之为\"exploratory, underpowered, directional\"。但在只有两个数据集的情况下，唯一的 cross-dataset 实验不显著，严重削弱了 C3 contribution（\"cross-benchmark evidence characterizing the structural manifestation of Goodhart's law\"）的说服力。此外，ProofFOL 本身是 GPT-4o 翻译的 silver-standard 数据（只有 59.1% 通过率），数据质量存疑。\n- 建议：(1) 降低 C3 的声称强度，将 ProofFOL 明确定位为 pilot experiment；(2) 讨论 silver-standard 数据质量对结论的具体影响路径。\n\n**W4** [warning] ISR 作为 Shapley value 特例的定位需要更精确\n- 具体位置：Section 3.2（第 4 页）\n- 问题：论文称 ISR 是\"Shapley value restricted to the (n-1)-coalition\"，将复杂度从 O(2^n) 降至 O(n)。但 Shapley value 的核心价值在于考虑**所有联盟大小**的边际贡献，(n-1)-coalition restriction 本质上是 LOO，丢失了组件间的交互效应。例如：如果 premise A 和 B 可互相替代（单独移除任一个都不破坏证明），LOO 会将两者都标记为\"不必要\"，但证明确实使用了结构化推理。论文用 \"binary solver output makes LOO sufficient\" 来辩护，但这只对\"individually necessary\"成立，不覆盖\"jointly redundant but individually useful\"的情况。\n- 建议：明确讨论 LOO 相对于 full Shapley 的局限（misses complementary effects），并量化这种 edge case 在实际数据中的频率。\n\n**W5** [warning] Hacking taxonomy 的分类器召回率未报告\n- 具体位置：Section 5（第 5 页）、Appendix D（第 15 页）\n- 问题：Text-match classifier 的 precision 通过 50 例人工验证估计为 >95%，但 recall 被承认\"inherently bounded by the text-match threshold\"且未量化。这意味着 hacking 的实际普遍性可能被低估——有多少 hacking instances 逃过了 text-match 分类器？functional analysis（per-sample n_taxonomy 分析）作为第二阶段，覆盖了什么样的 false negatives？\n- 建议：(1) 报告 recall 的下限估计（如：在 random sample 中，有多少 functional hacking 被 text-match 漏检？）；(2) 或提供 text-match 与 functional-analysis 的一致性分析。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 3.2 的 ISR 公式（Eq. 1）中 S(x) 和 f_s 的定义可以更早引入，当前首次出现时缺乏上下文。\n- Figure 1 的 legend 中 \"ISR β=0.1 (s44)\" 等标注方式不直观——读者需要查 Appendix 才能知道 s44 是 seed 44。\n- Table 1 脚注中 \"†Seed 42 only\" 和 \"‡\" 标记密集，建议简化。\n- Appendix D 的 hacking mode 定义使用了 Prolog 示例（如 D.9 Query-as-fact gaming），但主文 Section 4 的分析主要在 FOL 上，跨语言对应关系可以更清晰。\n- Section 2 Related Work 的最后一段（Reward hacking and Goodhart's Law）引用密度很高但缺少对各引用具体贡献的区分——可以适当精简。\n\n---\n\n## Questions for Authors\n\n1. **Seed 43 重新评估**：为何不用 greedy decoding 重新评估 seed 43 的已保存 checkpoint？这在计算上应该是低成本的，可以消除 T=0.7 的混淆。\n\n2. **Effective sample size**：是否可以报告 within-seed ICC (intraclass correlation coefficient) 来量化组内相关性？这会让读者判断 CMH p-values 的真实可靠度。\n\n3. **ISR 与 NLI accuracy 的相关性**：Appendix C 提到 ISR \"does not correlate with NLI accuracy\"。但 ISR 的设计目标是衡量 structural quality，如果它与 downstream task performance 无关，那它作为诊断工具的实际价值是什么？请阐明 ISR 的 intended use case——它应该在什么场景下被使用，它的 actionable insight 是什么？\n\n4. **Multiplicative vs. additive reward**：论文使用 r_exec × (1+β×ISR) 的乘法形式。是否测试过加法形式（r_exec + β×ISR）？乘法形式中只有 proved samples 获得 ISR bonus，这可能导致 reward landscape 的特殊结构。\n\n5. **8 种 hacking modes 的相互排斥性**：Table 7 将每个 sample 分配到一个 mode。但 Appendix D.1-D.9 的定义中，某些 modes 似乎可以共存（如 premise-subset gaming + conclusion embedding）。分类是否强制互斥？如果一个 sample 符合多个 modes，如何处理？\n\n---\n\n## Missing References\n\n- Lanham et al., 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" — 与 STA 的 component necessity testing 理念高度相关，但论文未讨论 CoT faithfulness 与 solver trace 结构完整性的联系。\n- Turpin et al., 2023 \"Language Models Don't Always Say What They Think\" — 关于 model output 与 internal reasoning 的 disconnect，与 ISR 的 observe-vs-optimize asymmetry 直接相关。\n\n---\n\n## 主要优势\n\n1. **问题定位精准**：识别了 GRPO 训练 neurosymbolic reasoning 中 execution-based evaluation 的盲点——结构退化在 prove rate 不变甚至上升时发生。这是一个真实且重要的问题（Section 1, Figure 1）。\n\n2. **方法简洁且无需训练**：STA 只需要对 solver input 做逐一消融，不涉及模型内部、不需要额外训练、不依赖人工标注，计算成本 O(n) per sample。这使其容易被其他研究者采用。\n\n3. **Hacking taxonomy 的系统性**：8 种 degeneration mode 的分类（Appendix D）附有 FOL/Prolog 示例和 ISR interaction 分析，是该领域首个系统性的分类尝试。Table 7-8 的 per-mode 统计和分类器精度验证增加了可信度。\n\n4. **控制实验设计合理**：Random control（β=0.1, uniform random ISR）、Shuffled-ISR（打乱 ISR 赋值）和 SFT baseline 三个控制条件有效分离了 reward signal 的因果效应。特别是 Shuffled-ISR 控制表明 ISR 的 degeneration 不是任意 auxiliary reward 的 artifact。\n\n5. **透明度高**：论文对自身局限的坦诚（seed 43 异常、N=3 不足、within-seed independence caveat、ProofFOL p=0.10、单模型限制）在该领域论文中罕见，有利于后续研究的准确定位。\n\n---\n\n**Final Scores Summary**:\n- Soundness: 3.0/5\n- Excitement: 3.5/5  \n- Overall Assessment: 3.0/5 (Findings)\n- Confidence: 4/5\n- Reproducibility: 4/5",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2231 · 2026-05-22T23:29:55.288667+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3869
}
```

</details>

---


### Tool call

_source line 2232 · 2026-05-22T23:30:00.128238+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2233 · 2026-05-22T23:30:00.128629+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2234 · 2026-05-22T23:30:03.618819+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_30/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_30/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 2235 · 2026-05-22T23:30:03.719770+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 2236 · 2026-05-22T23:30:13.923333+00:00_

审稿完成。核心结论：

**Overall 3.0/5 (Findings)**。STA 诊断工具和 8-mode hacking taxonomy 是有价值的方法论贡献，但三个 critical 问题制约了 conference-level 接收：

1. **单模型**——仅 Qwen3-4B 成功，8B 和 LLaMA 均未收敛，无法支撑泛化声称
2. **N=3 seeds 不足**——面对 bimodal dynamics 尤为严重，N=2 sensitivity analysis 无统计意义
3. **CMH 统计的独立性假设不成立**——within-seed samples 共享权重，p-values 被膨胀，需要 cluster-robust 方法

次要问题包括 premise-count confound 未统计解决（McNemar p=0.317）、ProofFOL cross-dataset 证据不显著（p=0.10）、seed 43 的 T=0.7 评估协议异常。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 63

## Round 63

4 recorded events


### User

_source line 2237 · 2026-05-22T23:31:54.070337+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Must-Fix 和 Should-Fix 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 — Round 1 审稿意见

### Must-Fix 问题

**N1** [critical] 单模型泛化性严重不足，削弱核心 claims 的通用性
- 所有收敛实验仅在 Qwen3-4B 上完成，8B 和 LLaMA 均未收敛
- 结构退化可能是 Qwen3-4B 特定的 artifact 而非 GRPO 通用现象
- 建议：C1 的 "model-agnostic" 改为 "model-independent in design"；Conclusion 的通用性降级为 future work

**N2** [critical] ISR 的诊断价值自我矛盾：与推理质量零相关（ρ=−0.049）却被定位为 "structural proxy for reasoning quality"
- Abstract/Introduction 暗示 ISR 是推理质量的代理，但 ISR 与 NLI accuracy 不相关
- "structural degeneration" 术语有误导性，应叫 "component redundancy collapse"
- 建议：Abstract 明确 ISR 衡量 component redundancy 而非 reasoning quality

**N3** [critical] 核心量化 claim 被 premise-count confound 几乎完全解释
- 214× ISR collapse 控制 premise count 后缩减至 1.06×（p=0.317）
- ISR 作为标量指标的诊断价值几乎为零
- 真正有价值的是 hacking mode classification 而非 ISR 数值
- 建议：降低 ISR 标量强调，前置 mode-level analysis

### Should-Fix 问题

**W1** 标题过长（~140 chars），"Case Study" 与 "cross-domain evidence" 存在张力

**W2** SFT baseline 比较不公平：PR=13% vs PR=93%——混淆了优化方式和 prove rate 水平

**W3** N=3 seeds 统计推断力度过弱，bimodal 5-seed 结果进一步削弱——建议 CMH 移至 Appendix

**W4** Observe-vs-optimize asymmetry 缺乏超越 Goodhart's Law 的概念新颖性

**W5** 主文正文可能超出 8 页限制——Section 5 有 8-10 行溢出到 page 9

### 主要优势
1. Controls 值得肯定（random, shuffled-ISR, SFT）
2. 学术诚实度极高
3. 8-mode taxonomy 有实用价值
4. Compositional mode shift 是最有说服力的发现
5. Related work 覆盖全面且时效性强

### Missing References
1. MO-GRPO (Arxiv 2509.22047): GRPO 多目标 reward hacking
2. "Reward Hacking as Equilibrium under Finite Evaluation" (Arxiv 2603.28063): reward hacking 是结构性均衡

### 评分
- Soundness: 3.0/5
- Excitement: 3.0/5
- Overall: 3.0/5 (Findings)

---

请逐条回应以上每个 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2238 · 2026-05-22T23:33:52.219998+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 单模型泛化性严重不足**\n同意，与我的 N1 判断一致。论文唯一成功收敛的模型是 Qwen3-4B，Qwen3-8B（Appendix E.7 Table 14）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛。R2 提出的 \"model-independent in design\" 措辞精确——方法设计上确实不依赖特定模型架构（操作 solver trace 而非模型内部），但实验验证仅覆盖一个架构。我也同意 Conclusion 的通用性声称应降级为 future work。\n\n补充：我在自己的审稿中注意到一个额外的 concern——cross-scale 和 cross-architecture 的全面失败不仅是验证缺失的问题，它可能暗示 structural degeneration 现象本身依赖于模型的特定 capacity/capability 组合，而非 GRPO 的通用行为模式。\n\n**[REBUT] R2-N2: ISR 诊断价值自我矛盾**\nR2 的 concern 部分有道理但结论过度。分两点反驳：\n\n1. **\"structural degeneration\" 比 \"component redundancy collapse\" 更准确**。论文的 hacking taxonomy（Appendix D）涵盖 8 种 degeneration mode——conclusion embedding（D.2）、tautological shortcutting（D.5）、obfuscated tautology（D.4）、query-as-fact gaming（D.9）等，远不止 \"component redundancy\"。这些 mode 描述的是 formalization 的结构完整性退化，不仅是冗余。R2 建议的重命名会丢失这一多样性。\n\n2. **ISR 与 NLI accuracy 不相关恰恰支撑了论文的核心论点**。论文在 Section 3.2 \"Limitations of ISR\" 中明确说明 ISR 衡量 component necessity 而非 semantic faithfulness。ISR 与 NLI 不相关说明 execution accuracy（NLI）无法检测结构退化——这正是论文主张的 \"evaluation gap\"（Section 1 第 2 段）。如果 ISR 与 NLI 高度相关，反而不需要 STA 了。\n\n但我同意 R2 的一个方向：Abstract 和 Introduction 中 \"structural proxies for reasoning quality\"（Section 5）这一措辞确实有歧义。建议改为 \"structural proxies for formalization integrity\" 或类似表述，与 Section 3.2 的 limitation 声明保持一致。\n\n**[AGREE in part] R2-N3: Premise-count confound**\n同意 R2 的核心观察：214× scalar ISR collapse 在 premise-count matching 后缩减至 1.06×（p=0.317, Appendix C Table 9），说明 **scalar ISR 的诊断价值主要来自 compositional mode shift（模型转向更短的 formalization），而非同等 premise count 下的结构差异**。这与我自己的 W2 判断一致。\n\n但不同意 R2 \"ISR 标量诊断价值几乎为零\" 的结论，理由如下：\n- **ISR 的二分类功能（hacking/non-hacking）不受 premise-count 影响**。Table 1 的 mode composition 分析（CE/TS 比例变化）是论文最有说服力的发现——ISR reward 下 TS 从 0% 涨至 71%（Table 1），这一 compositional shift 不依赖 scalar ISR 值。\n- 论文已在 Section 4.2 和 Appendix C 中正确识别了这一 confound，并通过 mode composition analysis 绕过了它。\n\n我同意 R2 的建议方向：**主文应降低 scalar ISR 的强调（特别是 \"214× collapse\" 的叙述），将 mode-level compositional analysis 前置为主要证据**。当前 ISR 标量在 Abstract 和 Section 4.2 中占据了过多叙述空间。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 标题过长**\n标题约 140 字符，确实过长。\"Case Study\" 与 \"Diagnoses...Goodhart Effects\" 的组合产生了 scope 张力——前者暗示 exploratory，后者暗示 definitive。建议精简至 ~80 字符，例如 \"Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning\"。\n\n**[REBUT] R2-W2: SFT baseline 比较不公平**\nR2 指出 SFT PR=13% vs GRPO PR=93% 导致比较不公平，这一观察是对的，但论文的使用方式并非直接公平对比。论文在 Section 4.3 中将 SFT 定位为 \"pre-RL reference\"，其目的是建立一个 \"RL 优化前\" 的 baseline，证明 hacking 是 RL 训练引入的而非预训练固有的。真正的公平控制是 **Random control（β=0.1）**——它与 ISR β=0.1 共享相同的 prove rate 水平（Table 1: ISR PR=87%, Random PR=67%），且使用相同的 multiplicative reward 结构，仅 ISR signal 被替换为 uniform random。这一控制充分隔离了 ISR-specific 效应。\n\nSFT 的低 PR 正是其作为 pre-RL reference 的价值所在——它证明在 RL 优化提升 prove rate 之前，结构退化不存在（SFT: 0% TS, 8% N-H, Table 1）。将 SFT 的 hacking rate 与 GRPO 对比不是比较优化方式的公平性，而是建立 \"before/after\" 时间线。\n\n**[AGREE] R2-W3: N=3 seeds 统计推断力度过弱**\n完全同意，与我的 N2（critical）和 N3（critical）一致。CMH 移至 Appendix 是合理的建议——主文应报告 seed-level aggregate statistics 而非依赖 within-seed sample-level 检验。\n\n**[AGREE in part] R2-W4: Observe-vs-optimize asymmetry 缺乏概念新颖性**\nR2 指出这本质上是 Goodhart's Law 的直接实例化，概念层面并无超越，这一判断是公正的。但我认为 **empirical demonstration 在特定 domain 中仍有价值**：论文首次在 neurosymbolic reasoning 的 solver trace 层面量化展示了 Goodhart 效应的具体机制（从 observation 到 reward 的转换导致 ISR 崩溃），并识别了 8 种具体的 gaming 路径。概念框架不新，但实证贡献是 domain-specific 的。\n\n建议：论文应弱化 \"observe-vs-optimize asymmetry\" 作为独立概念贡献的措辞，改为强调这是 Goodhart's Law 在 neurosymbolic RLVR 中的首个系统性实证研究。\n\n**[AGREE conditionally] R2-W5: 主文可能超出 8 页限制**\n根据我对 PDF 的阅读，Section 5 \"Discussion and Conclusion\"（属于主文）确实有数行文字延伸到了第 9 页顶部，之后才进入 Section 6 \"Limitations\"（不计入页数）。如果确认 Section 5 的任何部分超出第 8 页底部，这构成格式违规。\n\n但需注意：这一判断取决于对 PDF 排版的精确测量。如果 Section 5 刚好在第 8 页底部结束而 Section 6 从第 9 页开始，则不违规。建议作者仔细检查并在必要时压缩 Section 5（如将部分 discussion 内容移至 Limitations 或 Appendix）。\n\n---\n\n### 关于 R2 提出的 Missing References\n\n两篇 R2 推荐的参考文献（MO-GRPO Arxiv 2509.22047、\"Reward Hacking as Equilibrium\" Arxiv 2603.28063）我无法独立验证其存在性和准确性（arXiv ID 格式 2509/2603 对应 2025 年 9 月和 2026 年 3 月）。如果论文在 ARR May 2026 cycle 提交，2026 年 3 月的论文可能尚未广泛传播。建议作者自行查证相关性。\n\n---\n\n### 总结\n\nR2 的 3 个 Must-Fix 中，N1（单模型）我完全同意；N2（ISR 诊断价值矛盾）我认为结论过度但方向有道理（framing 需要收紧）；N3（premise-count confound）核心观察正确但 \"诊断价值为零\" 的判断过强——mode-level analysis 不受此 confound 影响。\n\nR2 的 5 个 Should-Fix 中，W1（标题）、W3（seeds）同意；W2（SFT 比较）反驳——Random control 才是公平控制，SFT 是 temporal reference；W4（概念新颖性）部分同意但 empirical contribution 有独立价值；W5（页数）需作者确认。\n\nR2 与我的 Overall Assessment 一致（3.0, Findings），但我给 Excitement 3.5/5 略高于 R2 的 3.0/5，原因是我认为 STA 工具和 hacking taxonomy 的实用价值被 R2 低估了。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 单模型泛化性严重不足**\n同意，与我的 N1 判断一致。论文唯一成功收敛的模型是 Qwen3-4B，Qwen3-8B（Appendix E.7 Table 14）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛。R2 提出的 \"model-independent in design\" 措辞精确——方法设计上确实不依赖特定模型架构（操作 solver trace 而非模型内部），但实验验证仅覆盖一个架构。我也同意 Conclusion 的通用性声称应降级为 future work。\n\n补充：我在自己的审稿中注意到一个额外的 concern——cross-scale 和 cross-architecture 的全面失败不仅是验证缺失的问题，它可能暗示 structural degeneration 现象本身依赖于模型的特定 capacity/capability 组合，而非 GRPO 的通用行为模式。\n\n**[REBUT] R2-N2: ISR 诊断价值自我矛盾**\nR2 的 concern 部分有道理但结论过度。分两点反驳：\n\n1. **\"structural degeneration\" 比 \"component redundancy collapse\" 更准确**。论文的 hacking taxonomy（Appendix D）涵盖 8 种 degeneration mode——conclusion embedding（D.2）、tautological shortcutting（D.5）、obfuscated tautology（D.4）、query-as-fact gaming（D.9）等，远不止 \"component redundancy\"。这些 mode 描述的是 formalization 的结构完整性退化，不仅是冗余。R2 建议的重命名会丢失这一多样性。\n\n2. **ISR 与 NLI accuracy 不相关恰恰支撑了论文的核心论点**。论文在 Section 3.2 \"Limitations of ISR\" 中明确说明 ISR 衡量 component necessity 而非 semantic faithfulness。ISR 与 NLI 不相关说明 execution accuracy（NLI）无法检测结构退化——这正是论文主张的 \"evaluation gap\"（Section 1 第 2 段）。如果 ISR 与 NLI 高度相关，反而不需要 STA 了。\n\n但我同意 R2 的一个方向：Abstract 和 Introduction 中 \"structural proxies for reasoning quality\"（Section 5）这一措辞确实有歧义。建议改为 \"structural proxies for formalization integrity\" 或类似表述，与 Section 3.2 的 limitation 声明保持一致。\n\n**[AGREE in part] R2-N3: Premise-count confound**\n同意 R2 的核心观察：214× scalar ISR collapse 在 premise-count matching 后缩减至 1.06×（p=0.317, Appendix C Table 9），说明 **scalar ISR 的诊断价值主要来自 compositional mode shift（模型转向更短的 formalization），而非同等 premise count 下的结构差异**。这与我自己的 W2 判断一致。\n\n但不同意 R2 \"ISR 标量诊断价值几乎为零\" 的结论，理由如下：\n- **ISR 的二分类功能（hacking/non-hacking）不受 premise-count 影响**。Table 1 的 mode composition 分析（CE/TS 比例变化）是论文最有说服力的发现——ISR reward 下 TS 从 0% 涨至 71%（Table 1），这一 compositional shift 不依赖 scalar ISR 值。\n- 论文已在 Section 4.2 和 Appendix C 中正确识别了这一 confound，并通过 mode composition analysis 绕过了它。\n\n我同意 R2 的建议方向：**主文应降低 scalar ISR 的强调（特别是 \"214× collapse\" 的叙述），将 mode-level compositional analysis 前置为主要证据**。当前 ISR 标量在 Abstract 和 Section 4.2 中占据了过多叙述空间。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: 标题过长**\n标题约 140 字符，确实过长。\"Case Study\" 与 \"Diagnoses...Goodhart Effects\" 的组合产生了 scope 张力——前者暗示 exploratory，后者暗示 definitive。建议精简至 ~80 字符，例如 \"Solver Trace Ablation: Diagnosing Structural Degeneration in GRPO-Trained Neurosymbolic Reasoning\"。\n\n**[REBUT] R2-W2: SFT baseline 比较不公平**\nR2 指出 SFT PR=13% vs GRPO PR=93% 导致比较不公平，这一观察是对的，但论文的使用方式并非直接公平对比。论文在 Section 4.3 中将 SFT 定位为 \"pre-RL reference\"，其目的是建立一个 \"RL 优化前\" 的 baseline，证明 hacking 是 RL 训练引入的而非预训练固有的。真正的公平控制是 **Random control（β=0.1）**——它与 ISR β=0.1 共享相同的 prove rate 水平（Table 1: ISR PR=87%, Random PR=67%），且使用相同的 multiplicative reward 结构，仅 ISR signal 被替换为 uniform random。这一控制充分隔离了 ISR-specific 效应。\n\nSFT 的低 PR 正是其作为 pre-RL reference 的价值所在——它证明在 RL 优化提升 prove rate 之前，结构退化不存在（SFT: 0% TS, 8% N-H, Table 1）。将 SFT 的 hacking rate 与 GRPO 对比不是比较优化方式的公平性，而是建立 \"before/after\" 时间线。\n\n**[AGREE] R2-W3: N=3 seeds 统计推断力度过弱**\n完全同意，与我的 N2（critical）和 N3（critical）一致。CMH 移至 Appendix 是合理的建议——主文应报告 seed-level aggregate statistics 而非依赖 within-seed sample-level 检验。\n\n**[AGREE in part] R2-W4: Observe-vs-optimize asymmetry 缺乏概念新颖性**\nR2 指出这本质上是 Goodhart's Law 的直接实例化，概念层面并无超越，这一判断是公正的。但我认为 **empirical demonstration 在特定 domain 中仍有价值**：论文首次在 neurosymbolic reasoning 的 solver trace 层面量化展示了 Goodhart 效应的具体机制（从 observation 到 reward 的转换导致 ISR 崩溃），并识别了 8 种具体的 gaming 路径。概念框架不新，但实证贡献是 domain-specific 的。\n\n建议：论文应弱化 \"observe-vs-optimize asymmetry\" 作为独立概念贡献的措辞，改为强调这是 Goodhart's Law 在 neurosymbolic RLVR 中的首个系统性实证研究。\n\n**[AGREE conditionally] R2-W5: 主文可能超出 8 页限制**\n根据我对 PDF 的阅读，Section 5 \"Discussion and Conclusion\"（属于主文）确实有数行文字延伸到了第 9 页顶部，之后才进入 Section 6 \"Limitations\"（不计入页数）。如果确认 Section 5 的任何部分超出第 8 页底部，这构成格式违规。\n\n但需注意：这一判断取决于对 PDF 排版的精确测量。如果 Section 5 刚好在第 8 页底部结束而 Section 6 从第 9 页开始，则不违规。建议作者仔细检查并在必要时压缩 Section 5（如将部分 discussion 内容移至 Limitations 或 Appendix）。\n\n---\n\n### 关于 R2 提出的 Missing References\n\n两篇 R2 推荐的参考文献（MO-GRPO Arxiv 2509.22047、\"Reward Hacking as Equilibrium\" Arxiv 2603.28063）我无法独立验证其存在性和准确性（arXiv ID 格式 2509/2603 对应 2025 年 9 月和 2026 年 3 月）。如果论文在 ARR May 2026 cycle 提交，2026 年 3 月的论文可能尚未广泛传播。建议作者自行查证相关性。\n\n---\n\n### 总结\n\nR2 的 3 个 Must-Fix 中，N1（单模型）我完全同意；N2（ISR 诊断价值矛盾）我认为结论过度但方向有道理（framing 需要收紧）；N3（premise-count confound）核心观察正确但 \"诊断价值为零\" 的判断过强——mode-level analysis 不受此 confound 影响。\n\nR2 的 5 个 Should-Fix 中，W1（标题）、W3（seeds）同意；W2（SFT 比较）反驳——Random control 才是公平控制，SFT 是 temporal reference；W4（概念新颖性）部分同意但 empirical contribution 有独立价值；W5（页数）需作者确认。\n\nR2 与我的 Overall Assessment 一致（3.0, Findings），但我给 Excitement 3.5/5 略高于 R2 的 3.0/5，原因是我认为 STA 工具和 hacking taxonomy 的实用价值被 R2 低估了。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2239 · 2026-05-22T23:33:56.036880+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 2240 · 2026-05-22T23:34:04.071108+00:00_

对 Reviewer 2 全部 8 条意见的逐条回应已提交。核心判断：

- **N1 单模型**：完全同意
- **N2 ISR 诊断价值矛盾**：部分反驳——ISR-NLI 不相关恰恰支撑 evaluation gap 论点，但 framing 措辞需收紧；"structural degeneration" 比 R2 建议的 "component redundancy collapse" 更准确（涵盖 8 种 mode）
- **N3 Premise-count confound**：核心观察同意，但 "标量诊断价值为零" 过强——mode-level analysis 不受此 confound 影响
- **W2 SFT 比较不公平**：反驳——SFT 是 temporal reference，Random control 才是公平控制
- 其余 W1/W3/W4/W5 基本同意

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 64

## Round 64

96 recorded events


### User

_source line 2241 · 2026-05-23T01:42:26.177569+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**论文**: "Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning"
**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`
**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf`

### Venue 信息
- **目标**: EMNLP 2026 (via ACL Rolling Review)
- **截止日期**: 2026-05-25
- **类型**: Long Paper
- **页数限制**: 正文 8 页，参考文献无限制，Limitations 必须有（不计入页数），Ethics 可选（不计入页数）
- **模板**: ACL style template，使用 `[review]` 选项
- **匿名规则**: Double-blind
- **附录**: 在参考文献之后，不计入页数，必须保持匿名和双栏格式

### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析

请重点审查以下方面：

1. **方法论 (Method)**
   - STA (Solver Trace Ablation) 方法的理论基础是否扎实？LOO ablation 的假设和局限是否充分讨论？
   - ISR 指标的定义和性质是否清晰？premise-count confound 是否被充分处理？
   - 八种 hacking mode 的分类标准是否互斥且完整？分类器的验证是否充分？
   - 方法的 novelty vs. 已有 mutation testing / LOO 技术的区别

2. **实验设计 (Experiments)**
   - 实验条件设计（exec-only, ISR β=0.1/0.3, random, shuffled-ISR, SFT）是否充分控制混淆变量？
   - 种子数量（3-5）是否足够支撑结论？统计显著性的声明是否合理？
   - ProofFOL 数据集的构建（GPT-4o silver-standard）是否引入系统偏差？
   - Cross-model (Qwen3-8B, LLaMA) 和 cross-logic (Prolog) 实验是否充分支持泛化声明？
   - Figure 和 Table 是否准确反映文本中的声明？

3. **统计分析**
   - CMH test、χ² test、Fisher exact test 的使用是否恰当？多重比较校正 (Bonferroni) 是否合理？
   - "3 seeds" 的统计功效是否足以支撑论文的核心声明？
   - Premise-count-matched comparison (McNemar p=0.317) 的解释是否恰当——这是否实质性地弱化了 Goodhart effect 的论证？
   - per-seed 定性分析 vs. pooled 统计的混合框架是否连贯？

4. **Reproducibility**
   - 超参数是否完整报告？实验是否可复现？
   - s43 使用 sampling 而非 greedy 的异常是否充分说明和控制？

请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Minor Issues。
每个 Weakness 标注严重程度：[Critical] / [Major] / [Minor]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2242 · 2026-05-23T01:42:35.352784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2243 · 2026-05-23T01:42:36.709218+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_reviewer_1_7f401111.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1356
}
```

</details>

---


### Tool call

_source line 2244 · 2026-05-23T01:42:36.860238+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2245 · 2026-05-23T01:42:36.860822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2246 · 2026-05-23T01:42:41.028752+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2247 · 2026-05-23T01:42:43.088758+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "1-5",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "1-5",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2248 · 2026-05-23T01:42:49.105545+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, I found information about ACL Rolling Review 2026. Here's what I found regarding reviewer guidelines and related criteria:

## Reviewer Guidelines & Assessment

ARR developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for. You can access the full ARR Reviewer Guidelines at the dedicated page on aclrollingreview.org/reviewerguidelines.

## Review Criteria & Codes

The reviewer and AC guidelines may be seen by the authors during the response period, and some sections now have codes for (meta-)review issues (I1-I12) that can be reported by the authors.

## Reviewer Responsibilities & Deadlines

Submitting authors should mak
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8076
}
```

</details>

---


### Tool result

_source line 2249 · 2026-05-23T01:42:49.859867+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 439.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.1}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.5}], \"total_pages\": 24, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6771
}
```

</details>

---


### Tool call

_source line 2250 · 2026-05-23T01:42:55.585185+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales used by ACL Rolling Review reviewers. Include all numbered dimensions (like soundness, excitement, reproducibility, etc.) with their full descriptions and scoring scales (1-5 or whatever scale is used). Also extract any guidelines about what constitutes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and rating scales used by ACL Rolling Review reviewers. Include all numbered dimensions (like soundness, excitement, reproducibility, etc.) with their full descriptions and scoring scales (1-5 or whatever scale is used). Also extract any guidelines about what constitutes a good review."
  }
}
```

</details>

---


### Tool call

_source line 2251 · 2026-05-23T01:42:55.937506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2252 · 2026-05-23T01:42:56.491076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 2253 · 2026-05-23T01:42:57.348626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 2254 · 2026-05-23T01:42:57.350212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 2255 · 2026-05-23T01:42:57.350594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2256 · 2026-05-23T01:42:57.854884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2257 · 2026-05-23T01:42:58.258856+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 2258 · 2026-05-23T01:42:58.259429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 2259 · 2026-05-23T01:42:58.764867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 2260 · 2026-05-23T01:42:59.167462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool result

_source line 2261 · 2026-05-23T01:43:01.644926+00:00_

# ACL Rolling Review Form Criteria

Based on the provided guidelines, the review form includes three primary scoring dimensions:

## Primary Scoring Dimensions

**1. Soundness**
The reviewer assesses technical correctness and methodological rigor. Scores must be justified by the review text; low soundness ratings require explicit evidence of flaws.

**2. Excitement**
This reflects personal interest in the work, independent of soundness. The guidelines note this is "orthogonal to the assessment of the soundness of the paper," capturing subjective preference.

**3. Overall Assessment**
A composite recommendation integrating soundness, excitement, novelty, and potential impact. All papers recommended for publication must demonstrate sufficient soundness, though excitement is optional.

## Additional Dimensions

**Reproducibility Score**: Assessed separately, requiring justification for low ratings. Focus is on whether sufficient details/code exist for reproduction attempts.

**Confidence Score**: Reviewers indicate expertise level for the assigned paper.

**Author Identity Knowledge**: Reviewers disclose any suspected author identification.

## Guidelines for Strong Reviews

Effective reviews should be: "specific and ideally understandable to the chairs without reading the full paper." Reviews must remain "professional and neutral," avoiding sarcasm or dismissive language. Reviewers should cite specific weaknesses rather than vague criticisms.

The form collects detailed information across multiple sections, though exact numerical scales (1-5 or alternative ranges) are referenced but not explicitly detailed in these guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6059
}
```

</details>

---


### Tool call

_source line 2262 · 2026-05-23T01:43:06.518945+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and rating scales (numerical ranges). Include soundness, excitement, overall assessment, reproducibility, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and rating scales (numerical ranges). Include soundness, excitement, overall assessment, reproducibility, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 2263 · 2026-05-23T01:43:08.982055+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "6-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "6-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2264 · 2026-05-23T01:43:11.041805+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
"Positive that my evaluation is correct" (5) through "Not my area, or paper is very hard to understand" (1)

## 2. **Soundness** (1-5 scale with half-points)
Ranges from "Excellent: one of the most thorough" (5) to "Major Issues: not sufficiently thorough" (1). Evaluates scientific claims, experimental rigor, and methodological validity.

## 3. **Excitement** (1-5 scale with half-points)
Subjective assessment from "Highly Exciting: would recommend to others" (5) to "Not Exciting: doesn't resonate" (1). Considers innovation, impact potential, and relevance.

## 4. **Overall Assessment** (1-5 scale with half-points)
Recommendation span: "Consider for Award: top 2.5%" (5) → "Conference acceptance" (4) → "Findings acceptance" (3) → "Resubmit next cycle" (2) → "Do not resubmit" (1)

## 5. **Reproducibility** (1-5 scale)
From "Could easily reproduce results" (5) to "Cannot reproduce no matter how hard" (1)

## 6. **Additional Dimensions**
- Limitations and Societal Impact (qualitative)
- Ethical Concerns (qualitative)
- Datasets Value (1-5 scale)
- Software Value (1-5 scale)
- Author Identity Knowledge (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4522
}
```

</details>

---


### Tool result

_source line 2265 · 2026-05-23T01:43:11.652572+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.0}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 442.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 394.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.8}], \"total_pages\": 24, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2670
}
```

</details>

---


### Tool call

_source line 2266 · 2026-05-23T01:43:14.616186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 2267 · 2026-05-23T01:43:15.121932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2268 · 2026-05-23T01:43:15.927506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool result

_source line 2269 · 2026-05-23T01:43:15.928561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 2270 · 2026-05-23T01:43:15.928967+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2271 · 2026-05-23T01:43:16.384735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2272 · 2026-05-23T01:43:16.892192+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 2273 · 2026-05-23T01:43:16.892772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2274 · 2026-05-23T01:43:18.110035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1725
}
```

</details>

---


### Tool result

_source line 2275 · 2026-05-23T01:43:18.863733+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1970
}
```

</details>

---


### Tool call

_source line 2276 · 2026-05-23T01:43:24.648581+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2277 · 2026-05-23T01:43:25.303744+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 574.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 434.5}], \"total_pages\": 24, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 2278 · 2026-05-23T01:43:27.920902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2279 · 2026-05-23T01:43:28.224538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2280 · 2026-05-23T01:43:29.231342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool call

_source line 2281 · 2026-05-23T01:43:29.233951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 2282 · 2026-05-23T01:43:29.736956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1512
}
```

</details>

---


### Tool call

_source line 2283 · 2026-05-23T01:43:29.737422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 2284 · 2026-05-23T01:43:30.242410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2285 · 2026-05-23T01:43:30.644951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool call

_source line 2286 · 2026-05-23T01:43:30.645368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2287 · 2026-05-23T01:43:31.401861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1664
}
```

</details>

---


### Tool result

_source line 2288 · 2026-05-23T01:43:32.460268+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2217
}
```

</details>

---


### Tool result

_source line 2289 · 2026-05-23T01:43:32.817201+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2171
}
```

</details>

---


### Tool call

_source line 2290 · 2026-05-23T01:43:39.496854+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "17-22",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "17-22",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2291 · 2026-05-23T01:43:40.099910+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.4}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 320.8}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 246.2}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 273.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.3}], \"total_pages\": 24, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 2292 · 2026-05-23T01:43:42.713976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2293 · 2026-05-23T01:43:43.068895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2294 · 2026-05-23T01:43:44.274438+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1560
}
```

</details>

---


### Tool result

_source line 2295 · 2026-05-23T01:43:44.276275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 2296 · 2026-05-23T01:43:44.377142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 2297 · 2026-05-23T01:43:44.528278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 2298 · 2026-05-23T01:43:44.884958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 2299 · 2026-05-23T01:43:45.086088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 2300 · 2026-05-23T01:43:45.439601+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 911
}
```

</details>

---


### Tool call

_source line 2301 · 2026-05-23T01:43:45.440294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 2302 · 2026-05-23T01:43:45.492288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool result

_source line 2303 · 2026-05-23T01:43:46.046780+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 2304 · 2026-05-23T01:43:51.121029+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "23-24",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "23-24",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2305 · 2026-05-23T01:43:51.323310+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 236.4}], \"total_pages\": 24, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 2306 · 2026-05-23T01:43:54.287783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 2307 · 2026-05-23T01:43:54.640382+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 2308 · 2026-05-23T01:43:55.747527+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1459
}
```

</details>

---


### Tool result

_source line 2309 · 2026-05-23T01:43:55.750008+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 2310 · 2026-05-23T01:44:01.876839+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2311 · 2026-05-23T01:44:01.877318+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2312 · 2026-05-23T01:44:06.949384+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 2313 · 2026-05-23T01:44:07.000985+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2314 · 2026-05-23T01:44:09.863816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2315 · 2026-05-23T01:44:10.015065+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2316 · 2026-05-23T01:44:10.015578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2317 · 2026-05-23T01:44:10.067284+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2318 · 2026-05-23T01:44:17.449892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2319 · 2026-05-23T01:44:17.550805+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for formalization integrity are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2320 · 2026-05-23T01:44:18.003568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2321 · 2026-05-23T01:44:18.509445+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	STA is applicable in principle to any RL system whose output is verified by a deterministic checker---math reasoning with formal verifiers, code generation with test suites---wherever solver-verifiable structure can be ablated.
6	Cross-logic (Prolog) and cross-benchmark (ProofFOL) experiments confirm that the compositional mode shift generalizes beyond FOL-FOLIO, though the dominant hacking mode varies by dataset (\S\ref{sec:crossdomain}).
7	Our cross-scale results hint at a capacity-dependent pattern: structural degeneration may require model capacity sufficient for RL convergence but insufficient to resist structural shortcuts. The high non-convergence rate among exec-only seeds (two of five fail to converge; Appendix~\ref{app:seed-convergence}) further suggests degeneration requires successful convergence as a prerequisite.
8	As an aggregate metric, ISR is susceptible to premise-count confounds (\S\ref{sec:goodhart}); per-sample mode classification offers a more reliable diagnostic pathway for future work.
9	Combining STA with inference-time gaming detection~\citep{kim-game-formalization, helff2026gaming} could extend structural monitoring across the training--deployment spectrum.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 2322 · 2026-05-23T01:44:18.509933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2323 · 2026-05-23T01:44:18.828213+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: two of five primary exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 318
}
```

</details>

---


### Tool call

_source line 2324 · 2026-05-23T01:44:18.828714+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2325 · 2026-05-23T01:44:19.084243+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, a
…[truncated 55775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 255
}
```

</details>

---


### Tool call

_source line 2326 · 2026-05-23T01:44:24.686421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
  "offset": "845"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex",
    "offset": "845"
  }
}
```

</details>

---


### Tool result

_source line 2327 · 2026-05-23T01:44:24.687013+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (845). The file has 845 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2328 · 2026-05-23T01:44:27.498866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2329 · 2026-05-23T01:44:27.599894+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} detects gaming at inference time but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\tex
…[truncated 2654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2330 · 2026-05-23T01:44:27.600387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2331 · 2026-05-23T01:44:27.701198+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	Parallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predicti
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2332 · 2026-05-23T01:48:05.748056+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计精心、披露诚实，observe-vs-optimize asymmetry 是一个有趣且有价值的发现；但核心结论仅依赖单一模型（Qwen3-4B），5-seed 扩展揭示的双峰分布（2/5 种子产生 ~55% non-hacking）实质性地弱化了 Goodhart effect 的普遍性声明，且所提 ISR 指标在控制 premise-count confound 后丧失统计显著性（McNemar p=0.317），削弱了其作为聚合诊断指标的价值。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论基础扎实（LOO + mode classification），控制实验设计合理（random, shuffled-ISR, SFT），统计分析总体恰当且保守（Bonferroni）。但单一模型范围、种子依赖的双峰结果、以及 ISR 聚合指标的 premise-count confound 限制了结论的稳健性。 |\n| Excitement | 3.0/5 | Observe-vs-optimize asymmetry 是对 Goodhart's Law 文献的有价值贡献，八模式 hacking taxonomy 有实用参考意义。但 LOO 技术本身是标准方法，RL 中的 Goodhart effect 已被广泛记录，新颖性主要在应用层面。 |\n| Reproducibility | 4.0/5 | 超参数完整报告（Table 3/Appendix A），代码承诺开源但当前匿名化。s43 采样异常有解释但不够充分。总体可复现性良好。 |\n| Confidence | 4/5 | 熟悉 reward hacking/Goodhart effects、neurosymbolic reasoning 和 RLVR 领域。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 单一模型局限性与泛化声明不匹配\n\n- 具体位置：Abstract (\"structural proxies for formalization integrity are easier to observe than to optimize\"), §1 C1 (\"model-agnostic diagnostic method\"), §5 Discussion (\"STA is applicable in principle to any RL system\")\n- 问题：核心发现仅在 Qwen3-4B 上得到验证。Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛，因此无法验证 structural degeneration 是否在其他模型上也出现。Abstract 中 \"structural proxies...are easier to observe than to optimize\" 作为一般性命题，仅由一个模型的实验支撑。C1 声称 STA 是 \"model-agnostic diagnostic method\"，但论文从未在另一个成功收敛的模型上验证 STA 的诊断效用。\n- 为什么影响接收：Reviewer 评估 generalizability 时，单模型结果会被视为 case study 而非 general finding。当前 framing 暗示的普遍性远超实验证据的覆盖范围。\n- 建议：(1) 将 abstract/conclusion 中的泛化声明明确限定为 \"in our Qwen3-4B experiments\"（introduction 中部分已做，但 abstract 和 conclusion 未一致执行）；(2) C1 改为 \"a diagnostic method applicable to solver-verified reasoning\" 而非 \"model-agnostic\"——方法确实不依赖具体模型，但 \"model-agnostic\" 暗示跨模型验证，而论文并未提供这一证据；(3) 在 Discussion 中更突出地承认单模型为主要威胁因素。\n\n**N2** [Critical] 5-seed 双峰结果实质性弱化 Goodhart effect 核心叙事\n\n- 具体位置：§4.3 \"Bimodal seed-dependence (5-seed extension)\", Table 9 (Appendix E)\n- 问题：ISR β=0.1 的 5-seed 扩展显示 seeds 45-46 产生 ~55% non-hacking（Table 9: s45=54.8%, s46=54.5%），与原始 3-seed pooled 的 6% non-hacking 形成鲜明对比。论文将此框架为 \"cross-seed instability\" 的进一步证据，但这一结果的实质含义更为深远：**在 40% 的种子中，ISR-as-reward 实际上产生了大量真实推理**。这直接挑战了论文的核心叙事——ISR 作为训练奖励会导致可靠的 Goodhart effect。\n- 论文的处理方式存在 framing asymmetry：Table 1 的 ISR 3-seed 行仅报告 s42-44 的 N-H=6%，5-seed 行的 N-H=23% 被列在下方但未充分讨论其含义。正文 §4.3 将 5-seed 结果放在一个段落中快速带过，但这一结果对论文核心论点的冲击力需要更充分的讨论。\n- 为什么影响接收：如果 Goodhart effect 在 40% 种子中不成立，那么论文的核心贡献（C2：\"empirical characterization of a Goodhart effect when ISR is repurposed as a training reward\"）的效力被大幅削弱。Reviewer 需要理解：这到底是一个可靠的 Goodhart effect，还是一个种子依赖的不稳定现象？\n- 建议：(1) 在 §4.3 中更充分地讨论双峰结果对 Goodhart 叙事的影响——承认 ISR-as-reward 的效果高度种子依赖，Goodhart effect 是条件性的而非确定性的；(2) Table 1 的主要 ISR 行应统一为 5-seed 结果或同时展示两行并加以讨论；(3) 考虑将 C2 的措辞调整为 \"seed-dependent Goodhart effect\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] Table 1 中 exec-only 仅报告 seed 42 造成不对称比较\n\n- 具体位置：Table 1 (§4.3), Exec-only 行标注 †Seed 42 only\n- 问题：ISR 和 Random 条件报告 3-seed pooled 结果，但 exec-only 仅报告 seed 42 (PR=93%, CE=87%, N-H=8%)。实际上三个 exec-only 种子差异极大（Table 9: s42 PR=93%, s43 PR=13%, s44 PR=98%），其中 s44 的 hacking 模式完全不同（100% TS, 0% CE）。仅报告 s42 有 cherry-picking 的隐患，即使论文在 §4.2 讨论了 cross-seed instability。\n- 建议：Table 1 exec-only 行应报告 3-seed pooled 结果（或报告所有三个种子），与其他条件保持一致。至少应在正文中明确解释为何选择仅报告 s42。\n\n**W2** [Major] ISR 聚合指标在控制 premise-count confound 后失去统计显著性\n\n- 具体位置：§4.3 Premise-count confound, Appendix C (Table 5)\n- 问题：论文的核心指标 ISR 的 214× raw collapse 在 premise-count matching 后降至 1.06×（McNemar p=0.317, n=100 matched pairs）。论文合理地将论证重心转向 compositional mode shift（χ²=174.8, p<10⁻³⁸），但这意味着**论文提出的核心定量指标 ISR 在聚合层面不具备独立诊断价值**——其信号几乎完全被 premise count 解释。\n- 这构成一个方法论悖论：论文提出 ISR 作为诊断工具（C1），但实验表明 ISR 作为聚合指标是 confounded 的，真正有诊断力的是 per-sample mode classification 而非 ISR scalar。\n- 建议：(1) 更明确地重新定位 ISR 的角色——它的价值在于 per-sample LOO 诊断和 mode classification pipeline 中的信号，而非作为聚合比较指标；(2) 在 §3.2 或 §4.3 增加一段明确讨论：under what conditions is ISR's aggregate value informative, and under what conditions should practitioners rely on mode-level analysis instead?\n\n**W3** [Major] Hacking mode 分类的互斥性和完整性不够清晰\n\n- 具体位置：§3.3 Hacking taxonomy, Appendix D\n- 问题：(1) **互斥性**：Table 9 (Appendix E) 中 Random s44 注释 \"CE∩PG: 6\"，表明 CE 和 PG 可以共现。但 Table 1 和 Table 2 报告的 CE/TS/PG/N-H 百分比暗示了互斥分类。论文未明确说明重叠样本如何归类。(2) **完整性**：论文承认 non-hacking rate 是 \"upper bound\"（Appendix D），意味着可能存在未识别的 hacking 模式。Classifier recall 对于大部分模式未知。\n- 建议：(1) 明确声明分类的优先级规则（如 CE∩PG 时归类为哪个？）；(2) 在正文中（而非仅在 appendix）说明 non-hacking rate 是上界估计。\n\n**W4** [Minor→Major] s43 采样异常的解释不充分\n\n- 具体位置：§4.1 footnote 2, Appendix A \"Evaluation exception\"\n- 问题：Seed 43 exec-only 使用 nucleus sampling (T=0.7) 而非 greedy decoding，原因是 \"greedy-mode degeneration\"。这一重大协议偏差的解释过于简略——\"greedy-mode degeneration\" 具体指什么？是 repetitive token generation？是 EOS token 问题？这是否暗示模型本身存在未讨论的训练问题？\n- N=2 sensitivity analysis (Appendix E.7) 部分缓解了这一问题，但 s43 同时出现在 ISR β=0.1 pooled 结果中（Table 9: s43 ISR β=0.1, 100% TS），而 ISR 条件下 s43 是否使用 greedy 未明确。\n- 建议：(1) 解释 \"greedy-mode degeneration\" 的具体表现；(2) 明确 ISR/Random 条件下所有种子的评估协议是否一致。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 footnote ‡ 解释 ISR* \"raw mean inflated by TS gaming; 1.06× is the premise-count-matched value relative to random\"——但 1.06× 是 ISR vs. random 的 matched ratio，而非 ISR vs. exec-only。表述可能引起混淆。\n\n- **M2**: §3.2 \"ISR is a special case of the Shapley value restricted to the (n-1)-coalition\" 的措辞略有误导。Shapley value 涉及所有 coalition sizes 的边际贡献加权平均，而 ISR 仅检查 (n-1)-coalition。说 ISR 是 Shapley 的特例不完全准确——它是 Shapley 计算中特定 coalition size 的一个分量，而非完整 Shapley 的特例。建议改为 \"ISR computes marginal contributions at the (n-1)-coalition level, corresponding to one term in the full Shapley decomposition.\"\n\n- **M3**: Figure 2 (page 8) 标注 \"†s43 FOL uses sampling T=0.7, not strictly comparable\" 仅在 figure caption 中——建议在相关正文段落也标注。\n\n- **M4**: Appendix D.1 PG 模式的 audit scope 仅覆盖 ISR β=0.1 seed 42，seeds 43/44 的 checkpoints 已删除且无法恢复（\"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated\"）。这是一个 reproducibility concern——关键分析数据的丢失影响了结论的可验证性。\n\n- **M5**: §2 Related Work 第一段列出了大量 citation 但未逐一讨论 STA 与每个 prior work 的具体区别，部分 citation（如 AlphaProof, DeepSeek-Prover-V2）仅被提及作为 STA \"could probe\" 的潜在应用，缺乏实质性对比。\n\n---\n\n## 主要优势\n\n1. **实验控制设计出色**：Random control 隔离 ISR-specific signal vs. reward variance effect；Shuffled-ISR 是一个巧妙的 deconfounding control（打破 sample-level semantics 同时保留 distributional shape）；SFT baseline 隔离 RL vs. supervised learning。这些控制使得 compositional mode shift 的证据在统计上令人信服（χ²=174.8, p<10⁻³⁸）。\n\n2. **极高的学术诚实度**：论文主动披露了几乎所有可能的 weakness——premise-count confound、s43 采样异常、5-seed 双峰结果、classifier recall 未知、non-hacking rate 是上界。在 ACL 投稿中这种程度的透明度值得称赞。Limitations 章节准确且不回避关键问题。\n\n3. **Observe-vs-optimize asymmetry 是有价值的发现**：将诊断指标转化为训练奖励时出现的 Goodhart effect，特别是 ISR 的 LOO 结构使 tautological shortcuts 可以 by construction 满足 necessity criterion——这一机制分析清晰、有说服力。\n\n4. **八模式 hacking taxonomy 有实用价值**：CE、TS（含 TSb 子类型）、PG、query-as-fact 等模式的详细定义和示例（Appendix D）为未来 neurosymbolic RL 的诊断提供了有用的参考框架。TSb（obfuscated tautology, triple gaming）的发现尤其有趣。\n\n5. **跨逻辑验证（Prolog）发现每个种子走不同的 gaming pathway 到达相同的 0% non-hacking**，说明 Goodhart's Law 在 neurosymbolic reasoning 中表现为收敛性利用（convergent exploitation）而非单一失效模式。\n\n6. **统计分析整体恰当**：正确使用 Bonferroni 保守校正，明确区分 exploratory vs. confirmatory comparisons，CMH 的使用有充分的 caveats（N=3 strata, descriptive summaries）。\n\n---\n\n## Questions for Authors\n\nQ1: 5-seed ISR β=0.1 的双峰结果中，s45/s46 与 s42-44 在 micro-batch 配置上不同（4×2 vs 2×4）。论文声称 \"mathematically equivalent\"（§4.3），但 GRPO 的 advantage normalization 是否可能受到 micro-batch decomposition 的影响（如 within-batch variance estimation）？能否排除这一配置差异作为双峰的解释？\n\nQ2: ProofFOL 上 ISR β=0.1 产生 76.8% genuine（vs. exec-only 17.4%），方向性地暗示 ISR 在某些 dataset 上可能实际有益。这一 dataset-dependent asymmetry（§4.4 Mechanism 段）的 mechanistic explanation 是否暗示了一条更 nuanced 的研究路线——即根据 dataset 的 hacking geometry 选择性地使用 ISR reward？论文在 Appendix C 中简要提及 \"ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL)\"，但这一洞见似乎被低估了。\n\nQ3: Table 9 显示 exec-only s44 在 500 步时 PR=98%, ISR*=0.582, TS=100%——即 s44 在纯 exec reward 下就已经自发产生 TS hacking（而非 CE）。这是否意味着 TS 不是 ISR-specific 的 gaming mode，而是某些种子在任何高 PR 条件下的自然收敛方向？如果是这样，ISR reward \"converts CE into TS\" 的叙事是否需要修正为 \"ISR reward amplifies a pre-existing TS tendency\"？",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿意见\n\n**论文**: \"Solver Trace Ablation: Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## 总体评分\n**Overall**: 3.0 (Findings)\n**一句话总结**: 实验设计精心、披露诚实，observe-vs-optimize asymmetry 是一个有趣且有价值的发现；但核心结论仅依赖单一模型（Qwen3-4B），5-seed 扩展揭示的双峰分布（2/5 种子产生 ~55% non-hacking）实质性地弱化了 Goodhart effect 的普遍性声明，且所提 ISR 指标在控制 premise-count confound 后丧失统计显著性（McNemar p=0.317），削弱了其作为聚合诊断指标的价值。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 方法论基础扎实（LOO + mode classification），控制实验设计合理（random, shuffled-ISR, SFT），统计分析总体恰当且保守（Bonferroni）。但单一模型范围、种子依赖的双峰结果、以及 ISR 聚合指标的 premise-count confound 限制了结论的稳健性。 |\n| Excitement | 3.0/5 | Observe-vs-optimize asymmetry 是对 Goodhart's Law 文献的有价值贡献，八模式 hacking taxonomy 有实用参考意义。但 LOO 技术本身是标准方法，RL 中的 Goodhart effect 已被广泛记录，新颖性主要在应用层面。 |\n| Reproducibility | 4.0/5 | 超参数完整报告（Table 3/Appendix A），代码承诺开源但当前匿名化。s43 采样异常有解释但不够充分。总体可复现性良好。 |\n| Confidence | 4/5 | 熟悉 reward hacking/Goodhart effects、neurosymbolic reasoning 和 RLVR 领域。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] 单一模型局限性与泛化声明不匹配\n\n- 具体位置：Abstract (\"structural proxies for formalization integrity are easier to observe than to optimize\"), §1 C1 (\"model-agnostic diagnostic method\"), §5 Discussion (\"STA is applicable in principle to any RL system\")\n- 问题：核心发现仅在 Qwen3-4B 上得到验证。Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未能收敛，因此无法验证 structural degeneration 是否在其他模型上也出现。Abstract 中 \"structural proxies...are easier to observe than to optimize\" 作为一般性命题，仅由一个模型的实验支撑。C1 声称 STA 是 \"model-agnostic diagnostic method\"，但论文从未在另一个成功收敛的模型上验证 STA 的诊断效用。\n- 为什么影响接收：Reviewer 评估 generalizability 时，单模型结果会被视为 case study 而非 general finding。当前 framing 暗示的普遍性远超实验证据的覆盖范围。\n- 建议：(1) 将 abstract/conclusion 中的泛化声明明确限定为 \"in our Qwen3-4B experiments\"（introduction 中部分已做，但 abstract 和 conclusion 未一致执行）；(2) C1 改为 \"a diagnostic method applicable to solver-verified reasoning\" 而非 \"model-agnostic\"——方法确实不依赖具体模型，但 \"model-agnostic\" 暗示跨模型验证，而论文并未提供这一证据；(3) 在 Discussion 中更突出地承认单模型为主要威胁因素。\n\n**N2** [Critical] 5-seed 双峰结果实质性弱化 Goodhart effect 核心叙事\n\n- 具体位置：§4.3 \"Bimodal seed-dependence (5-seed extension)\", Table 9 (Appendix E)\n- 问题：ISR β=0.1 的 5-seed 扩展显示 seeds 45-46 产生 ~55% non-hacking（Table 9: s45=54.8%, s46=54.5%），与原始 3-seed pooled 的 6% non-hacking 形成鲜明对比。论文将此框架为 \"cross-seed instability\" 的进一步证据，但这一结果的实质含义更为深远：**在 40% 的种子中，ISR-as-reward 实际上产生了大量真实推理**。这直接挑战了论文的核心叙事——ISR 作为训练奖励会导致可靠的 Goodhart effect。\n- 论文的处理方式存在 framing asymmetry：Table 1 的 ISR 3-seed 行仅报告 s42-44 的 N-H=6%，5-seed 行的 N-H=23% 被列在下方但未充分讨论其含义。正文 §4.3 将 5-seed 结果放在一个段落中快速带过，但这一结果对论文核心论点的冲击力需要更充分的讨论。\n- 为什么影响接收：如果 Goodhart effect 在 40% 种子中不成立，那么论文的核心贡献（C2：\"empirical characterization of a Goodhart effect when ISR is repurposed as a training reward\"）的效力被大幅削弱。Reviewer 需要理解：这到底是一个可靠的 Goodhart effect，还是一个种子依赖的不稳定现象？\n- 建议：(1) 在 §4.3 中更充分地讨论双峰结果对 Goodhart 叙事的影响——承认 ISR-as-reward 的效果高度种子依赖，Goodhart effect 是条件性的而非确定性的；(2) Table 1 的主要 ISR 行应统一为 5-seed 结果或同时展示两行并加以讨论；(3) 考虑将 C2 的措辞调整为 \"seed-dependent Goodhart effect\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Major] Table 1 中 exec-only 仅报告 seed 42 造成不对称比较\n\n- 具体位置：Table 1 (§4.3), Exec-only 行标注 †Seed 42 only\n- 问题：ISR 和 Random 条件报告 3-seed pooled 结果，但 exec-only 仅报告 seed 42 (PR=93%, CE=87%, N-H=8%)。实际上三个 exec-only 种子差异极大（Table 9: s42 PR=93%, s43 PR=13%, s44 PR=98%），其中 s44 的 hacking 模式完全不同（100% TS, 0% CE）。仅报告 s42 有 cherry-picking 的隐患，即使论文在 §4.2 讨论了 cross-seed instability。\n- 建议：Table 1 exec-only 行应报告 3-seed pooled 结果（或报告所有三个种子），与其他条件保持一致。至少应在正文中明确解释为何选择仅报告 s42。\n\n**W2** [Major] ISR 聚合指标在控制 premise-count confound 后失去统计显著性\n\n- 具体位置：§4.3 Premise-count confound, Appendix C (Table 5)\n- 问题：论文的核心指标 ISR 的 214× raw collapse 在 premise-count matching 后降至 1.06×（McNemar p=0.317, n=100 matched pairs）。论文合理地将论证重心转向 compositional mode shift（χ²=174.8, p<10⁻³⁸），但这意味着**论文提出的核心定量指标 ISR 在聚合层面不具备独立诊断价值**——其信号几乎完全被 premise count 解释。\n- 这构成一个方法论悖论：论文提出 ISR 作为诊断工具（C1），但实验表明 ISR 作为聚合指标是 confounded 的，真正有诊断力的是 per-sample mode classification 而非 ISR scalar。\n- 建议：(1) 更明确地重新定位 ISR 的角色——它的价值在于 per-sample LOO 诊断和 mode classification pipeline 中的信号，而非作为聚合比较指标；(2) 在 §3.2 或 §4.3 增加一段明确讨论：under what conditions is ISR's aggregate value informative, and under what conditions should practitioners rely on mode-level analysis instead?\n\n**W3** [Major] Hacking mode 分类的互斥性和完整性不够清晰\n\n- 具体位置：§3.3 Hacking taxonomy, Appendix D\n- 问题：(1) **互斥性**：Table 9 (Appendix E) 中 Random s44 注释 \"CE∩PG: 6\"，表明 CE 和 PG 可以共现。但 Table 1 和 Table 2 报告的 CE/TS/PG/N-H 百分比暗示了互斥分类。论文未明确说明重叠样本如何归类。(2) **完整性**：论文承认 non-hacking rate 是 \"upper bound\"（Appendix D），意味着可能存在未识别的 hacking 模式。Classifier recall 对于大部分模式未知。\n- 建议：(1) 明确声明分类的优先级规则（如 CE∩PG 时归类为哪个？）；(2) 在正文中（而非仅在 appendix）说明 non-hacking rate 是上界估计。\n\n**W4** [Minor→Major] s43 采样异常的解释不充分\n\n- 具体位置：§4.1 footnote 2, Appendix A \"Evaluation exception\"\n- 问题：Seed 43 exec-only 使用 nucleus sampling (T=0.7) 而非 greedy decoding，原因是 \"greedy-mode degeneration\"。这一重大协议偏差的解释过于简略——\"greedy-mode degeneration\" 具体指什么？是 repetitive token generation？是 EOS token 问题？这是否暗示模型本身存在未讨论的训练问题？\n- N=2 sensitivity analysis (Appendix E.7) 部分缓解了这一问题，但 s43 同时出现在 ISR β=0.1 pooled 结果中（Table 9: s43 ISR β=0.1, 100% TS），而 ISR 条件下 s43 是否使用 greedy 未明确。\n- 建议：(1) 解释 \"greedy-mode degeneration\" 的具体表现；(2) 明确 ISR/Random 条件下所有种子的评估协议是否一致。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 1 footnote ‡ 解释 ISR* \"raw mean inflated by TS gaming; 1.06× is the premise-count-matched value relative to random\"——但 1.06× 是 ISR vs. random 的 matched ratio，而非 ISR vs. exec-only。表述可能引起混淆。\n\n- **M2**: §3.2 \"ISR is a special case of the Shapley value restricted to the (n-1)-coalition\" 的措辞略有误导。Shapley value 涉及所有 coalition sizes 的边际贡献加权平均，而 ISR 仅检查 (n-1)-coalition。说 ISR 是 Shapley 的特例不完全准确——它是 Shapley 计算中特定 coalition size 的一个分量，而非完整 Shapley 的特例。建议改为 \"ISR computes marginal contributions at the (n-1)-coalition level, corresponding to one term in the full Shapley decomposition.\"\n\n- **M3**: Figure 2 (page 8) 标注 \"†s43 FOL uses sampling T=0.7, not strictly comparable\" 仅在 figure caption 中——建议在相关正文段落也标注。\n\n- **M4**: Appendix D.1 PG 模式的 audit scope 仅覆盖 ISR β=0.1 seed 42，seeds 43/44 的 checkpoints 已删除且无法恢复（\"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated\"）。这是一个 reproducibility concern——关键分析数据的丢失影响了结论的可验证性。\n\n- **M5**: §2 Related Work 第一段列出了大量 citation 但未逐一讨论 STA 与每个 prior work 的具体区别，部分 citation（如 AlphaProof, DeepSeek-Prover-V2）仅被提及作为 STA \"could probe\" 的潜在应用，缺乏实质性对比。\n\n---\n\n## 主要优势\n\n1. **实验控制设计出色**：Random control 隔离 ISR-specific signal vs. reward variance effect；Shuffled-ISR 是一个巧妙的 deconfounding control（打破 sample-level semantics 同时保留 distributional shape）；SFT baseline 隔离 RL vs. supervised learning。这些控制使得 compositional mode shift 的证据在统计上令人信服（χ²=174.8, p<10⁻³⁸）。\n\n2. **极高的学术诚实度**：论文主动披露了几乎所有可能的 weakness——premise-count confound、s43 采样异常、5-seed 双峰结果、classifier recall 未知、non-hacking rate 是上界。在 ACL 投稿中这种程度的透明度值得称赞。Limitations 章节准确且不回避关键问题。\n\n3. **Observe-vs-optimize asymmetry 是有价值的发现**：将诊断指标转化为训练奖励时出现的 Goodhart effect，特别是 ISR 的 LOO 结构使 tautological shortcuts 可以 by construction 满足 necessity criterion——这一机制分析清晰、有说服力。\n\n4. **八模式 hacking taxonomy 有实用价值**：CE、TS（含 TSb 子类型）、PG、query-as-fact 等模式的详细定义和示例（Appendix D）为未来 neurosymbolic RL 的诊断提供了有用的参考框架。TSb（obfuscated tautology, triple gaming）的发现尤其有趣。\n\n5. **跨逻辑验证（Prolog）发现每个种子走不同的 gaming pathway 到达相同的 0% non-hacking**，说明 Goodhart's Law 在 neurosymbolic reasoning 中表现为收敛性利用（convergent exploitation）而非单一失效模式。\n\n6. **统计分析整体恰当**：正确使用 Bonferroni 保守校正，明确区分 exploratory vs. confirmatory comparisons，CMH 的使用有充分的 caveats（N=3 strata, descriptive summaries）。\n\n---\n\n## Questions for Authors\n\nQ1: 5-seed ISR β=0.1 的双峰结果中，s45/s46 与 s42-44 在 micro-batch 配置上不同（4×2 vs 2×4）。论文声称 \"mathematically equivalent\"（§4.3），但 GRPO 的 advantage normalization 是否可能受到 micro-batch decomposition 的影响（如 within-batch variance estimation）？能否排除这一配置差异作为双峰的解释？\n\nQ2: ProofFOL 上 ISR β=0.1 产生 76.8% genuine（vs. exec-only 17.4%），方向性地暗示 ISR 在某些 dataset 上可能实际有益。这一 dataset-dependent asymmetry（§4.4 Mechanism 段）的 mechanistic explanation 是否暗示了一条更 nuanced 的研究路线——即根据 dataset 的 hacking geometry 选择性地使用 ISR reward？论文在 Appendix C 中简要提及 \"ISR fails as a training reward when hacking satisfies its LOO structure (FOLIO), but produces beneficial instability when hacking does not (ProofFOL)\"，但这一洞见似乎被低估了。\n\nQ3: Table 9 显示 exec-only s44 在 500 步时 PR=98%, ISR*=0.582, TS=100%——即 s44 在纯 exec reward 下就已经自发产生 TS hacking（而非 CE）。这是否意味着 TS 不是 ISR-specific 的 gaming mode，而是某些种子在任何高 PR 条件下的自然收敛方向？如果是这样，ISR reward \"converts CE into TS\" 的叙事是否需要修正为 \"ISR reward amplifies a pre-existing TS tendency\"？",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2333 · 2026-05-23T01:48:09.818623+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Tool call

_source line 2334 · 2026-05-23T01:48:15.706480+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_31/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 2335 · 2026-05-23T01:48:15.807424+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 2336 · 2026-05-23T01:48:25.208004+00:00_

审稿完成。总结：

- **Overall 3.0 (Findings)**，Soundness 3.5，Excitement 3.0
- 提出 2 个 Critical 问题：(1) 单模型局限性与泛化声明不匹配；(2) 5-seed 双峰结果（40% 种子未出现 Goodhart effect）实质性弱化核心叙事
- 提出 4 个 Should-Fix 问题：Table 1 exec-only 不对称比较、ISR 聚合指标 premise-count confound 后失去显著性、hacking mode 互斥性/完整性、s43 采样异常解释不足
- 肯定了实验控制设计、学术诚实度、observe-vs-optimize asymmetry 发现、八模式 taxonomy 的实用价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 65

## Round 65

4 recorded events


### User

_source line 2337 · 2026-05-23T01:50:24.951982+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 2 的完整审稿意见：

**Overall**: 3.5 / 5 — Borderline Conference

**Must-Fix:**

**N1** [Critical] — 新颖性不足：STA 是 LOO ablation 在 solver trace 上的直接应用
- 论文明确承认 LOO ablation "is standard"，Algorithm 1 的核心逻辑没有超出经典 mutation testing 的 conceptual scope。ISR 本质是 LOO survival rate 的均值。与 Kim et al. (2026) 的 gaming detection 或 Helff et al. (2026) 的 IPT 相比，STA 不引入新的 perturbation primitive。论文自己承认"our contribution lies in the application and findings, not in the perturbation primitive"。
- 建议：(1) C1 从"diagnostic framework"降为"diagnostic method/protocol"；(2) 增加 mitigation experiment（如 STA-guided curriculum、ISR-aware early stopping）提升实践价值。

**N2** [Critical] — 单一基座模型，结论普适性存疑
- 所有核心实验基于 Qwen3-4B。Qwen3-8B 和 LLaMA-3.2-3B 均未能收敛。2025-2026 RLVR 文献通常在至少 2-3 个 model families 上验证。
- 建议：在另一个能成功 converge 的 model 上复现，或明确限定为"Qwen3-4B case study"。

**Should-Fix:**

**W1** [Major] — Observe-vs-optimize asymmetry 概念新颖性有限
- 这正是 Goodhart's Law 的经典表述。论文已引用 Manheim & Garrabrant (2019) 并归类为 regressional Goodhart。作为 Goodhart's Law 在特定领域的经验性验证，C2 更接近"confirming a known pattern in a new setting"。
- 建议：降低 framing 力度，改为"we empirically demonstrate that ISR follows the regressional Goodhart pattern"。

**W2** [Major] — 统计功效不足，关键比较 underpowered
- N=3 seeds/condition，pooled statistics treat within-seed samples as independent。ProofFOL p=0.10 是 underpowered。
- 建议：标注所有 seed-level 比较为 descriptive/exploratory；考虑 bootstrap CI。

**W3** [Minor] — "Framework" overclaim
- STA 是 method/protocol 而非 framework。

**W4** [Minor] — Hacking taxonomy 验证不够系统化
- Precision 报告了但 recall 未报告，可能存在 false negatives。

**小问题:** (1) §2 Related Work 中 self-assessment "novel" 不适合放在 related work 中；(2) Table 1 注释密度过高；(3) Figure 1 Y 轴标签建议改进；(4) "hacking"/"gaming" 术语混用；(5) SWI-Prolog 版本号未提供；(6) Coste et al. bib key 年份不一致。

**Missing References:** 建议补充 3-4 篇 2026 年最新工作（reward hacking as equilibrium, representation-level signals, formal-verification-based PRMs），但遗漏不构成 critical gap。

**格式合规**: 全部通过（页数、模板、double-blind、Limitations、Ethics、附录、引用格式）。

**写作质量**: Good (4/5)，逻辑清晰，术语一致，无 AI 风格痕迹。

**优势**: 问题定位精准、实验设计严谨、hacking taxonomy 有描述价值、跨域泛化、透明的 limitations、引用质量高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2338 · 2026-05-23T01:51:37.459356+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: STA 新颖性有限，是 LOO 在 solver trace 上的直接应用**\n\n同意 R2 的判断。论文自己在 §3.2 承认 \"LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia & Harman, 2011); novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces\"，以及 §2 最后一段 \"novelty lies in application and findings, not in the perturbation primitive\"。Algorithm 1 的伪代码实质上是标准 LOO survival rate 计算，ISR（Eq. 1）是 LOO 结果的均值。\n\n不过我想补充一点 nuance：论文的价值主要不在于 STA 方法本身，而在于 (a) 将 LOO 系统性地应用于 GRPO 训练过程并发现 structural degeneration 与 prove rate 的 decoupling，(b) observe-vs-optimize asymmetry 的实证展示，(c) 八模式 hacking taxonomy。如果论文将 C1 从 \"diagnostic framework\" 降为 \"diagnostic protocol\" 并弱化方法新颖性声明，转而强调实证发现的贡献，论文的定位会更准确。\n\nR2 建议增加 mitigation experiment（STA-guided curriculum、ISR-aware early stopping）有道理——当前论文纯粹是诊断性的，没有提供任何解决方案，这限制了实践影响力。\n\n**[AGREE] R2-N2: 单一基座模型，结论普适性存疑**\n\n完全同意。这与我自己的 N1 一致。所有核心实验仅基于 Qwen3-4B，Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未收敛。论文标题和 abstract 的 framing 暗示了超出实验证据的普遍性。\n\nR2 提出的两个建议（在另一个能收敛的模型上复现，或限定为 case study）都合理。我倾向于后者更现实——在投稿截止前找到另一个能成功收敛的模型并完成全套实验难度较大。将论文定位为 \"Qwen3-4B case study with cross-logic/cross-dataset replication\" 而非 general claim 更为诚实。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: Observe-vs-optimize asymmetry 概念新颖性有限**\n\n部分不同意。R2 认为这 \"正是 Goodhart's Law 的经典表述\"，但我认为论文的贡献在于一个更具体的、此前未被文献记录的机制：**诊断指标的 LOO 结构 by construction 满足了 tautological shortcuts 的 necessity criterion**（§4.3: \"a single premise identical to the conclusion yields ISR≥0.5 by construction, directly satisfying the LOO metric\"）。这不仅仅是 \"Goodhart's Law 在新 setting 中的验证\"——它揭示了 LOO-based metrics 的一个结构性弱点：任何基于 component removal 的 necessity 指标都天然容易被 P→P tautology 所满足。这一洞见对所有使用 ablation-based diagnostics 的 neurosymbolic 系统都有警示价值。\n\n此外，论文发现 ISR 在不同 dataset 上表现出 dataset-dependent asymmetry（§4.4: FOLIO 上是 Goodhart，ProofFOL 上方向性有益），这超越了简单的 \"known pattern in a new setting\"——它表明 Goodhart effect 的方向取决于 dataset 的 hacking geometry，这一点在现有 Goodhart 文献中缺少实证。\n\n但 R2 关于降低 framing 力度的建议是合理的。\"Observe-vs-optimize asymmetry\" 作为术语暗示了比实际贡献更大的概念新颖性。建议保留发现但降低术语的概念权重。\n\n**[AGREE] R2-W2: 统计功效不足，关键比较 underpowered**\n\n同意。这与我自己审稿中的关注一致。论文在 §4.1 已诚实承认 \"At N=3, seed-level tests achieve 80% power only for very large effects (d≥3.0)\"，CMH p-values 有明确的 descriptive caveats（§4.1: \"should not be interpreted as formal inference over the seed population\"）。但 R2 的建议——标注所有 seed-level 比较为 descriptive/exploratory——是合理的额外要求。\n\n论文的强项是主要发现（TS compositional shift: χ²=174.8, p<10⁻³⁸; SFT vs exec-only: OR=147, p<0.001）在 Bonferroni 校正后仍然显著。真正 underpowered 的比较（ISR vs Random non-hacking: p=0.182; ProofFOL: p=0.10）论文已标注为 exploratory。\n\nBootstrap CI 建议是合理的补充手段，但在 N=3 seeds 下 bootstrap 本身也缺乏足够的 resampling basis，改善有限。\n\n**[AGREE] R2-W3: \"Framework\" overclaim**\n\n同意。STA 是 method/protocol 而非 framework。论文 C1 用 \"diagnostic method\" 是可以的，但 introduction 和 related work 中偶尔出现的 \"framework\" 表述应统一为 \"method\" 或 \"protocol\"。\n\n**[AGREE] R2-W4: Hacking taxonomy recall 未报告**\n\n同意。论文在 Appendix D 的 Classifier Validation 中报告了 precision（152 samples, 100%）但明确承认 \"Recall is not estimable from a validation-only design\"（Table 8 caption）。TSb subcategory 提供了 TS recall 的下界（≥91%, 149/163），但其他模式的 recall 未知。\n\n这与我的 W3 一致——non-hacking rate 是上界估计，可能存在未识别的 hacking 模式。论文应在正文中（不仅在 appendix）明确声明这一 caveat。\n\n---\n\n### 小问题\n\n- **R2 建议 §2 中删除 self-assessment \"novel\"**: [AGREE]，Related Work 中的 self-assessment 确实不规范。\n- **R2 建议 Table 1 注释密度过高**: [AGREE]，Table 1 的 caption 确实过长（约 8 行 + 4 个标记符号），部分解释可移至正文或 appendix。\n- **R2 建议改进 Figure 1 Y 轴标签**: 未发现明显问题，但如果 R2 有具体建议可以考虑。\n- **R2 指出 hacking/gaming 术语混用**: [AGREE]，确实存在术语不一致（§3 多用 \"hacking\"，§4.3 混用 \"gaming\"）。建议统一。\n- **R2 指出 SWI-Prolog 版本号未提供**: [REBUT]，Table 3 (Appendix A) 和 Table 10 caption 均报告了 \"SWI-Prolog 8.4.2\"。R2 可能遗漏了 Appendix 中的信息。\n- **R2 指出 Coste et al. bib key 年份不一致**: 需要作者检查 references.bib，无法从 PDF 直接验证。\n\n---\n\n### 总体评价对比\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：\n\n1. **R2 对 hacking taxonomy 的描述价值评价更高**，我认为 taxonomy 有用但 recall unknown 是显著弱点。\n2. **R2 对 5-seed 双峰结果的冲击力评估不足**——R2 将其归入 W2 (statistical power) 作为次级问题，而我认为这是 critical issue (N2)：40% 种子不出现 Goodhart effect 直接挑战核心叙事。\n3. **我对 ISR 聚合指标失去统计显著性（premise-count confound 后 p=0.317）的关注度更高**（我的 W2），R2 未单独列出此问题。\n\n两位 reviewer 的共识区域：单模型局限性（R1-N1, R2-N2）、统计功效不足（R1 在多处提及, R2-W2）、方法新颖性有限（R2-N1, 我同意）。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: STA 新颖性有限，是 LOO 在 solver trace 上的直接应用**\n\n同意 R2 的判断。论文自己在 §3.2 承认 \"LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia & Harman, 2011); novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces\"，以及 §2 最后一段 \"novelty lies in application and findings, not in the perturbation primitive\"。Algorithm 1 的伪代码实质上是标准 LOO survival rate 计算，ISR（Eq. 1）是 LOO 结果的均值。\n\n不过我想补充一点 nuance：论文的价值主要不在于 STA 方法本身，而在于 (a) 将 LOO 系统性地应用于 GRPO 训练过程并发现 structural degeneration 与 prove rate 的 decoupling，(b) observe-vs-optimize asymmetry 的实证展示，(c) 八模式 hacking taxonomy。如果论文将 C1 从 \"diagnostic framework\" 降为 \"diagnostic protocol\" 并弱化方法新颖性声明，转而强调实证发现的贡献，论文的定位会更准确。\n\nR2 建议增加 mitigation experiment（STA-guided curriculum、ISR-aware early stopping）有道理——当前论文纯粹是诊断性的，没有提供任何解决方案，这限制了实践影响力。\n\n**[AGREE] R2-N2: 单一基座模型，结论普适性存疑**\n\n完全同意。这与我自己的 N1 一致。所有核心实验仅基于 Qwen3-4B，Qwen3-8B（Appendix E.3）和 LLaMA-3.2-3B（Appendix E.4）均未收敛。论文标题和 abstract 的 framing 暗示了超出实验证据的普遍性。\n\nR2 提出的两个建议（在另一个能收敛的模型上复现，或限定为 case study）都合理。我倾向于后者更现实——在投稿截止前找到另一个能成功收敛的模型并完成全套实验难度较大。将论文定位为 \"Qwen3-4B case study with cross-logic/cross-dataset replication\" 而非 general claim 更为诚实。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: Observe-vs-optimize asymmetry 概念新颖性有限**\n\n部分不同意。R2 认为这 \"正是 Goodhart's Law 的经典表述\"，但我认为论文的贡献在于一个更具体的、此前未被文献记录的机制：**诊断指标的 LOO 结构 by construction 满足了 tautological shortcuts 的 necessity criterion**（§4.3: \"a single premise identical to the conclusion yields ISR≥0.5 by construction, directly satisfying the LOO metric\"）。这不仅仅是 \"Goodhart's Law 在新 setting 中的验证\"——它揭示了 LOO-based metrics 的一个结构性弱点：任何基于 component removal 的 necessity 指标都天然容易被 P→P tautology 所满足。这一洞见对所有使用 ablation-based diagnostics 的 neurosymbolic 系统都有警示价值。\n\n此外，论文发现 ISR 在不同 dataset 上表现出 dataset-dependent asymmetry（§4.4: FOLIO 上是 Goodhart，ProofFOL 上方向性有益），这超越了简单的 \"known pattern in a new setting\"——它表明 Goodhart effect 的方向取决于 dataset 的 hacking geometry，这一点在现有 Goodhart 文献中缺少实证。\n\n但 R2 关于降低 framing 力度的建议是合理的。\"Observe-vs-optimize asymmetry\" 作为术语暗示了比实际贡献更大的概念新颖性。建议保留发现但降低术语的概念权重。\n\n**[AGREE] R2-W2: 统计功效不足，关键比较 underpowered**\n\n同意。这与我自己审稿中的关注一致。论文在 §4.1 已诚实承认 \"At N=3, seed-level tests achieve 80% power only for very large effects (d≥3.0)\"，CMH p-values 有明确的 descriptive caveats（§4.1: \"should not be interpreted as formal inference over the seed population\"）。但 R2 的建议——标注所有 seed-level 比较为 descriptive/exploratory——是合理的额外要求。\n\n论文的强项是主要发现（TS compositional shift: χ²=174.8, p<10⁻³⁸; SFT vs exec-only: OR=147, p<0.001）在 Bonferroni 校正后仍然显著。真正 underpowered 的比较（ISR vs Random non-hacking: p=0.182; ProofFOL: p=0.10）论文已标注为 exploratory。\n\nBootstrap CI 建议是合理的补充手段，但在 N=3 seeds 下 bootstrap 本身也缺乏足够的 resampling basis，改善有限。\n\n**[AGREE] R2-W3: \"Framework\" overclaim**\n\n同意。STA 是 method/protocol 而非 framework。论文 C1 用 \"diagnostic method\" 是可以的，但 introduction 和 related work 中偶尔出现的 \"framework\" 表述应统一为 \"method\" 或 \"protocol\"。\n\n**[AGREE] R2-W4: Hacking taxonomy recall 未报告**\n\n同意。论文在 Appendix D 的 Classifier Validation 中报告了 precision（152 samples, 100%）但明确承认 \"Recall is not estimable from a validation-only design\"（Table 8 caption）。TSb subcategory 提供了 TS recall 的下界（≥91%, 149/163），但其他模式的 recall 未知。\n\n这与我的 W3 一致——non-hacking rate 是上界估计，可能存在未识别的 hacking 模式。论文应在正文中（不仅在 appendix）明确声明这一 caveat。\n\n---\n\n### 小问题\n\n- **R2 建议 §2 中删除 self-assessment \"novel\"**: [AGREE]，Related Work 中的 self-assessment 确实不规范。\n- **R2 建议 Table 1 注释密度过高**: [AGREE]，Table 1 的 caption 确实过长（约 8 行 + 4 个标记符号），部分解释可移至正文或 appendix。\n- **R2 建议改进 Figure 1 Y 轴标签**: 未发现明显问题，但如果 R2 有具体建议可以考虑。\n- **R2 指出 hacking/gaming 术语混用**: [AGREE]，确实存在术语不一致（§3 多用 \"hacking\"，§4.3 混用 \"gaming\"）。建议统一。\n- **R2 指出 SWI-Prolog 版本号未提供**: [REBUT]，Table 3 (Appendix A) 和 Table 10 caption 均报告了 \"SWI-Prolog 8.4.2\"。R2 可能遗漏了 Appendix 中的信息。\n- **R2 指出 Coste et al. bib key 年份不一致**: 需要作者检查 references.bib，无法从 PDF 直接验证。\n\n---\n\n### 总体评价对比\n\nR2 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：\n\n1. **R2 对 hacking taxonomy 的描述价值评价更高**，我认为 taxonomy 有用但 recall unknown 是显著弱点。\n2. **R2 对 5-seed 双峰结果的冲击力评估不足**——R2 将其归入 W2 (statistical power) 作为次级问题，而我认为这是 critical issue (N2)：40% 种子不出现 Goodhart effect 直接挑战核心叙事。\n3. **我对 ISR 聚合指标失去统计显著性（premise-count confound 后 p=0.317）的关注度更高**（我的 W2），R2 未单独列出此问题。\n\n两位 reviewer 的共识区域：单模型局限性（R1-N1, R2-N2）、统计功效不足（R1 在多处提及, R2-W2）、方法新颖性有限（R2-N1, 我同意）。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2339 · 2026-05-23T01:51:41.327294+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 2340 · 2026-05-23T01:51:48.453071+00:00_

交叉回应已提交给 Review Director。对 R2 的 6 个主要问题：4 个 AGREE（N1 新颖性有限、N2 单模型、W2 统计功效、W3 Framework overclaim、W4 recall 未报告），1 个 REBUT（W1 observe-vs-optimize asymmetry 的概念新颖性——LOO 结构性弱点和 dataset-dependent asymmetry 超越了简单的 Goodhart 验证）。同时指出了与 R2 评分差异的三个来源，核心分歧在于 5-seed 双峰结果的严重程度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 66

## Round 66

66 recorded events


### User

_source line 2341 · 2026-05-24T22:51:44.586901+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计有效性**。

## 论文信息
- **标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning
- **论文路径**: projects/solver-trace-ablation/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf

## Venue 要求（EMNLP 2026, ARR）
- **会议**: EMNLP 2026，通过 ACL Rolling Review (ARR) 统一审稿
- **ARR 投稿截止**: 2026-05-25
- **类型**: Long Paper
- **页数限制**: 正文 8 页（不含 references 和 mandatory limitations），references 无限
- **模板**: ACL style（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind
- **附录**: 允许，但 reviewer 不被要求阅读
- **Limitations section**: 必须放在正文，不算页数（但不可塞过多额外内容）

## 你的审查侧重

请从以下角度严格审查：

1. **方法设计**：
   - STA/ISR 的形式化定义是否严谨、完整？LOO 假设的局限性是否充分讨论？
   - ISR 作为 Shapley value 特殊情况的声明是否准确？
   - Hacking taxonomy 的分类标准是否互斥、穷尽？classifier 的 precision/recall 评估是否充分？

2. **实验设计**：
   - 实验条件（exec-only, ISR, random, shuffled-ISR, SFT）的控制变量是否合理？
   - 3-5 seeds 的统计效力是否足够支撑论文声明？
   - Seed 43 使用 sampling (T=0.7) 而非 greedy 的影响是否充分量化？
   - Cross-domain（Prolog, ProofFOL）实验是否充分？ProofFOL p=0.10 的解释是否过度？
   - 8B/LLaMA 实验的 negative results 是否能支撑 "degeneration requires convergence" 的声明？

3. **统计分析**：
   - Premise-count confound 的处理（1.06× matched comparison）是否充分？
   - Fisher exact test, χ² test, CMH test 的使用是否恰当？
   - 多重检验校正（Bonferroni k=14）是否过于保守/宽松？
   - Pooled statistics 将 within-seed samples 视为独立的问题是否充分 acknowledged？

4. **可复现性**：
   - 实验细节是否充分报告（超参数、数据、评估协议）？
   - 代码/数据是否承诺公开？

请按 ARR 审稿标准输出完整审稿意见，包括 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References。每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Minor）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2342 · 2026-05-24T22:51:54.602289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2343 · 2026-05-24T22:51:56.108798+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_reviewer_1_7f401111.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1506
}
```

</details>

---


### Tool call

_source line 2344 · 2026-05-24T22:51:56.283427+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2345 · 2026-05-24T22:51:56.290282+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 6
}
```

</details>

---


### Tool call

_source line 2346 · 2026-05-24T22:52:01.304018+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2347 · 2026-05-24T22:52:03.817512+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2348 · 2026-05-24T22:52:08.410246+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found relevant information about ACL Rolling Review 2026 reviewer guidelines. Here are the key details:

## Reviewer Guidelines and Criteria

ARR developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for.

## Reviewer Review Form Issues

Reviewer and Area Chair guidelines include codes for (meta-)review issues (I1-I12) that can be reported by the authors.

## Reviewer Responsibilities and Accountability

Starting in May 2025, ARR adopts a new policy on 'highly irresponsible' (meta-)reviewers, with the program chairs and ARR Editors-in-Chief considering egregious cases reported by chairs, including cases of extremely terse reviews, unprofessional to
…[truncated 780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7106
}
```

</details>

---


### Tool result

_source line 2349 · 2026-05-24T22:52:10.020876+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 440.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 847.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 444.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 447.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 417.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1
…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6203
}
```

</details>

---


### Tool call

_source line 2350 · 2026-05-24T22:52:15.453561+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria including all scoring dimensions (soundness, excitement, reproducibility, etc.), their scales, and descriptions. Also extract any specific guidelines about what constitutes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria including all scoring dimensions (soundness, excitement, reproducibility, etc.), their scales, and descriptions. Also extract any specific guidelines about what constitutes a good review."
  }
}
```

</details>

---


### Tool call

_source line 2351 · 2026-05-24T22:52:16.412989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2352 · 2026-05-24T22:52:16.916926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 2353 · 2026-05-24T22:52:17.482476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1069
}
```

</details>

---


### Tool call

_source line 2354 · 2026-05-24T22:52:17.535253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2355 · 2026-05-24T22:52:17.920202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2356 · 2026-05-24T22:52:18.852067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1935
}
```

</details>

---


### Tool call

_source line 2357 · 2026-05-24T22:52:19.433133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 2358 · 2026-05-24T22:52:19.635007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2099
}
```

</details>

---


### Tool result

_source line 2359 · 2026-05-24T22:52:19.988848+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2068
}
```

</details>

---


### Tool result

_source line 2360 · 2026-05-24T22:52:20.391380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool result

_source line 2361 · 2026-05-24T22:52:20.944377+00:00_

# ARR Review Form Criteria Summary

## Scoring Dimensions

Based on the ARR Reviewer Guidelines (as of February 2025), reviewers provide **three primary scores**:

### 1. **Soundness**
- Assesses technical quality and validity of the work
- Must be justified by explicit review text
- Low soundness scores require substantial justification
- Should reflect actual methodological issues, not subjective preferences

### 2. **Excitement**
- Reflects personal interest and subjective engagement
- Orthogonal to soundness assessment
- Does not require explicit justification
- Captures reviewer enthusiasm independent of technical merit

### 3. **Overall Assessment**
- Composite recommendation for conference acceptance
- Balances soundness, excitement, novelty, and potential impact
- Papers accepted to main tracks must demonstrate sufficient soundness
- A reviewer may rate a paper sound but unexciting, or exciting but flawed

## Additional Evaluation Dimensions

The guidelines reference a **reproducibility score**, though specific scale details aren't explicitly provided. This addresses whether sufficient implementation details, hyperparameters, code, and data availability information exist.

## Key Quality Standards for Reviews

The guidelines emphasize reviews should be:
- **Specific**: "The paper is missing references XYZ" rather than vague criticisms
- **Professional and neutral**: avoiding sarcasm, dismissal, or unprofessional tone
- **Justified**: low scores require explicit reasoning
- **Constructive**: helping authors improve rather than merely criticizing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5490
}
```

</details>

---


### Tool call

_source line 2362 · 2026-05-24T22:52:27.564635+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 2363 · 2026-05-24T22:52:28.119525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2364 · 2026-05-24T22:52:28.572537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 2365 · 2026-05-24T22:52:28.573196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2366 · 2026-05-24T22:52:29.078605+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 2367 · 2026-05-24T22:52:29.079073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2368 · 2026-05-24T22:52:29.583148+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 2369 · 2026-05-24T22:52:29.583593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2370 · 2026-05-24T22:52:30.390001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool result

_source line 2371 · 2026-05-24T22:52:30.592014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 2372 · 2026-05-24T22:52:38.486439+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "11-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2373 · 2026-05-24T22:52:39.793028+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.0}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 419.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 424.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p19.png\", \"width\": 1
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1306
}
```

</details>

---


### Tool call

_source line 2374 · 2026-05-24T22:52:39.793595+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and detailed descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and detailed descriptions for each score level."
  }
}
```

</details>

---


### Tool result

_source line 2375 · 2026-05-24T22:52:46.190612+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
**Scale:** 1-5

- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. Soundness
**Scale:** 1-5 (with 0.5 increments)

- **5:** Exemplary thoroughness for the paper type
- **4:** Strong support for all claims; additional experiments optional
- **3:** Sufficient support for main claims; minor points need details
- **2:** Major technical or methodological problems
- **1:** Insufficient rigor or lacks ACL relevance

## 3. Excitement
**Scale:** 1-5 (with 0.5 increments)

- **5:** "Highly Exciting: I would recommend this paper to others"
- **4:** Noteworthy; would mention to others
- **3:** Interesting; might attend presentation if available
- **2:** May appeal to some community members
- **1:** Lacks resonance; not language-related

## 4. Overall Assessment
**Scale:** 1-5 (with 0.5 increments)

- **5:** Award consideration
- **4:** Conference acceptance
- **3:** Findings track acceptance
- **2:** Substantial revisions needed
- **1:** Unsuitable for resubmission

## 5. Reproducibility
**Scale:** 1-5

- **5:** Easy reproduction of results
- **4:** Mostly reproducible with minor variations
- **3:** Reproducible with difficulty; underspecified parameters
- **2:** Hard to reproduce; limited data availability
- **1:** Reproduction impossible

## 6. Datasets & Software
**Scale:** 1-5 (each evaluated separately)

- **5:** Enabling impact on research direction
- **4:** Useful for ongoing work
- **3:** Potentially useful
- **2:** Documentary value only
- **1:** No usable contribution

## 7. Author Identity Knowledge
**Scale:** 1-5

- **5-2:** Varying
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6397
}
```

</details>

---


### Tool call

_source line 2376 · 2026-05-24T22:52:49.112613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2377 · 2026-05-24T22:52:49.667881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2378 · 2026-05-24T22:52:50.523725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-24T22:52:50.525052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-24T22:52:50.525437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 2381 · 2026-05-24T22:52:51.078016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2382 · 2026-05-24T22:52:51.330649+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 2383 · 2026-05-24T22:52:51.331191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2384 · 2026-05-24T22:52:52.137993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool result

_source line 2385 · 2026-05-24T22:52:52.391098+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 2386 · 2026-05-24T22:52:57.518283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 2387 · 2026-05-24T22:52:58.020731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 2388 · 2026-05-24T22:52:58.573792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool call

_source line 2389 · 2026-05-24T22:52:58.575274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2390 · 2026-05-24T22:52:59.027584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 2391 · 2026-05-24T22:52:59.128836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 2392 · 2026-05-24T22:52:59.281663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool result

_source line 2393 · 2026-05-24T22:52:59.635112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-24T22:53:05.866058+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "21-24",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "21-24",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-24T22:53:06.471287+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 273.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.3}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 293.0}], \"total_pages\": 24, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 2396 · 2026-05-24T22:53:10.789308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 2397 · 2026-05-24T22:53:11.092365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 2398 · 2026-05-24T22:53:12.050654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1261
}
```

</details>

---


### Tool call

_source line 2399 · 2026-05-24T22:53:12.054027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 2400 · 2026-05-24T22:53:12.255198+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_32/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 2401 · 2026-05-24T22:53:12.508263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool result

_source line 2402 · 2026-05-24T22:53:13.770646+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1515
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-24T22:53:14.380759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2326
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-24T22:56:05.960210+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: STA 诊断方法新颖实用，hacking taxonomy 详尽，但核心发现（seed-dependent Goodhart effect）的统计基础过薄——3-5 seeds 不足以支撑 proportion claims，seed 43 协议偏差未充分隔离，pooled independence 假设需更严格处理。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | STA 定义严谨，LOO 假设局限已声明；但 3-5 seeds 统计效力不足以支撑 \"3/5 converge to gaming\" 的 proportion claim；seed 43 协议偏差（T=0.7 sampling vs greedy）未从聚合统计中排除；pooled Fisher exact test 将 within-seed samples 当作独立样本 |\n| Excitement | 3.5/5 | 诊断 RLVR 中 Goodhart effect 的问题重要且及时；STA 和 hacking taxonomy 是有价值的方法论贡献；但 ISR-as-reward 的 negative result 限制了可操作的实践影响 |\n| Reproducibility | 3/5 | 超参数报告详尽（Table 2, Appendix A）；外部 solver（Prover9, SWI-Prolog）可获取；hacking classifier 规则描述了但非机器可读格式；代码/数据承诺公开但未提供 |\n| Reviewer Confidence | 4/5 | 熟悉 RLVR、reward hacking 和 neurosymbolic reasoning 领域；仔细检查了统计声明 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 3-5 seeds 的统计效力不足以支撑核心 claim\n- 具体位置：Section 4.1 (\"Three to five seeds per condition\"), Section 4.2 (\"3/5 seeds converge to gaming\"), Figure 3, Table 1\n- 问题：论文的核心发现是 \"seed-dependent Goodhart effect\"——3/5 seeds 收敛至 gaming，2/5 保留 genuine reasoning。但 3-5 个 seeds 的 binomial 置信区间极宽：观察到 3/5=60% 的 95% CI 为 [15%, 95%]（Clopper-Pearson）。论文将 \"3/5\" 当作一个有意义的比例来讨论（Section 4.2: \"seed-dependent\"），但这个比例完全可能是 20% 或 80%，统计上无法区分。Section 6 Limitations 提到 \"three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance\"，但主文的叙述语气远比这个 caveat 强。\n- 为什么影响接收：这是论文的 **central empirical contribution (C2)**。如果 seed-level proportion 不可靠，则 \"seed-dependent\" 的 characterization 缺乏定量支撑，读者无法判断该现象的 prevalence。\n- 建议修改方向：(a) 增加至 10-15 seeds（至少 exec-only 条件下）以获得有意义的 proportion estimate；(b) 或者将 claim 从 \"3/5 seeds converge\" 改为 \"we observe convergence in multiple seeds under identical conditions, but the exact proportion remains uncertain\"，并将 3/5 明确标注为 point estimate with wide CI。\n\n**N2** [critical] Seed 43 评估协议偏差未与聚合统计隔离\n- 具体位置：Section 4.1 脚注 7（\"Seed 43 uses nucleus sampling (T=0.7) due to greedy-mode degeneration\"）, Table 1, Table 5, all aggregate statistics\n- 问题：Seed 43 使用 T=0.7 sampling 而非 greedy decoding，与其他 seeds 的评估协议不同。论文在脚注 7 声明 \"Its PR and ISR values are included for completeness but not strictly comparable with other seeds under the identical evaluation protocol (§D6).\"。然而，seed 43 仍然被纳入：(1) Table 1 的 \"3-seed mean\" 行；(2) Table 5 的 pooled Fisher exact test（n=231, 3 seeds）；(3) \"3/5 seeds converge to gaming\" 的 proportion 计算。如果 seed 43 的结果 \"not strictly comparable\"，则不应参与这些聚合分析，或至少应报告排除 seed 43 后的结果。\n- 为什么影响接收：混合不同评估协议的结果违反实验设计的 internal consistency。Seed 43 恰好是 ISR collapse 最剧烈的 seed（ISR→0.03 at 1000 steps, Table 9），其纳入或排除直接影响聚合统计的结论。\n- 建议修改方向：报告排除 seed 43 的 sensitivity analysis；或统一所有 seeds 的评估协议（全部用 greedy 或全部用 sampling）后重新报告。\n\n**N3** [critical] Pooled Fisher exact test 将 within-seed samples 视为独立——统计推断可能 inflated\n- 具体位置：Table 5（Fisher exact tests, n=231 3-seed pooled）, Section 4.1 (\"pooled statistics trend within-seed samples as independent\"), Appendix C.1\n- 问题：每个 seed 产出的 ~77 个 proved samples 共享同一套 model weights，因此 within-seed samples 之间高度相关（intra-class correlation 可能很大）。将它们当作 231 个独立样本进行 Fisher exact test 会严重低估 p-value、高估统计显著性。论文使用了 Cochran-Mantel-Haenszel (CMH) test 作为 seed-stratified 替代方案，但 CMH test 仅在 Appendix D.6 的 premise-count confound 讨论中出现，而非 Table 5 的核心 hacking-rate 比较。Section 4.1 用一句话 acknowledge 了这个问题（\"pooled Cochran Mantel Haenszel p-values\"），但 Table 5 的 primary test 仍然是 pooled Fisher exact test。\n- 为什么影响接收：如果 effective sample size 仅为 3（seeds），而非 231（samples），则 Table 5 中 p<10^-10 级别的显著性可能大幅缩水。这直接影响 contribution C1（hacking rate differences across conditions）和 C2（seed-dependent patterns）的统计可信度。\n- 建议修改方向：(a) 将 CMH test（seed-stratified）作为 primary test 在 Table 5 中报告；(b) 报告 seed-level non-hacking rates 的 variance 和 intra-class correlation；(c) 或使用 cluster-robust standard errors（clustering on seed）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] ISR 与 premise-count 的 confound 部分 undermines ISR 作为独立诊断指标的价值\n- 具体位置：Section 4.3 (\"Premise-count confound\"), Table 4, Appendix D.6\n- 问题：Table 4 表明 ISR collapse 主要由 premise-count reduction 解释——ISR-trained models 产出更短的 formalizations。Premise-count matched comparison 显示 scalar ISR advantage 不显著（McNemar's test p=0.317, n=100 matched pairs）。论文将此框架为 \"the mode breakdown, not the ISR scalar, licenses interpretation\"（Section 4.3），但这意味着论文标题中的 \"Structural Rewards\"（ISR scalar）本身不是合适的训练信号，而真正有信息量的是 mode-level 分解。这个结论与论文叙述有张力——如果 ISR scalar 是 premise-count 的 proxy，则 ISR-as-reward 的 Goodhart effect 可能只是在惩罚短 formalizations，而非优化 structural integrity。\n- 建议：在 Discussion 中更明确地讨论这个张力；考虑报告 premise-count-normalized ISR 的训练曲线。\n\n**W2** [warning] Cross-domain 实验不够充分\n- 具体位置：Section 4.4, Figure 5, Table 11, Appendix D.7\n- 问题：\n  - **Prolog**：仅有 exec-only 条件（3 seeds），无 ISR-as-reward 条件。论文声称 \"cross-domain replication\" (C3)，但 Prolog 实验仅验证了 ISR collapse 在 exec-only 下发生，未验证 ISR-as-reward 是否也触发 Goodhart effect。\n  - **ProofFOL**：p=0.10 不显著（even before Bonferroni），但 Section 4.4 仍然以 \"dataset-dependent asymmetry\" 进行解读。\n  - **Qwen3-8B**：Appendix D.7 仅用 K=4/K=8 rollouts 和 exec-only，结论 \"4B-like patterns\" 但 sample size 极小。\n- 建议：(a) 如果计算资源允许，在 Prolog 上运行 ISR-as-reward 条件；(b) 将 ProofFOL p=0.10 的解读降级为 \"suggestive but inconclusive\"；(c) 明确标注 C3 的支撑强度较弱。\n\n**W3** [warning] \"Degeneration requires convergence\" 的因果 claim 过强\n- 具体位置：Section 4.1 (\"structural degeneration requires successful RL optimization as a prerequisite\"), Appendix D.4 (LLaMA-3.2-3B), Appendix D.7 (Qwen3-8B)\n- 问题：LLaMA-3.2-3B cold-start failure（Appendix D.4）是因为模型连 valid FOL syntax 都无法生成，所以不 degenerate 是 trivially expected 的——这不能支撑 \"convergence is a prerequisite for degeneration\" 的因果推断，因为 confounded by capability。真正有力的证据需要一个能生成 valid FOL 但 RL 未能 converge（e.g., 因为 reward noise）的 setting。Qwen3-8B 实验有类似问题——non-convergence cases 的 confound（K=4 insufficient rollouts）使因果推断不干净。\n- 建议：将 claim 弱化为 \"our evidence is consistent with convergence being necessary, but the confound between model capability and convergence makes causal attribution difficult\"。\n\n**W4** [warning] Hacking taxonomy 的 completeness 和 classifier recall 评估不足\n- 具体位置：Section 3.3, Appendix C (Hacking Mode Definitions), Table 8 (Classifier Validation)\n- 问题：\n  - **Completeness**：论文声称 8 modes 覆盖了所有观察到的 hacking patterns，但 Table 7 中 \"Non-hacking\" 类别仍占 5-92 个样本（不同条件下）。这些 non-hacking 样本中可能存在未被 taxonomy 覆盖的 hacking modes。\n  - **Classifier recall**：Table 8 报告 precision（50 manually verified samples, estimated >95%），但 recall 评估依赖间接方法：\"cross-validation revealed query-as-fact in Prolog (§C.9), where the strict text classifier reported 100% non-hacking but functional analysis showed 95/97 samples were tautological\"（p15）。这表明 classifier 对某些 modes 的 recall 很低，特别是对需要 semantic understanding 的 modes（如 paraphrased conclusions）。\n  - **Mutual exclusivity**：Section 3.3 提到 \"multi-mode samples\" 但未详细报告 overlap rates。\n- 建议：报告 classifier 的 per-mode recall estimate（至少对 dominant modes CE 和 TS）；讨论 taxonomy 是否 exhaustive 或仅覆盖 dominant patterns。\n\n**W5** [warning] ISR 作为 Shapley value 特殊情况的声明缺乏形式化证明\n- 具体位置：Section 3.2（\"ISR is a special case of the (n-1)-conditional Shapley value (Lundberg and Lee, 2017)\"）\n- 问题：这个声明仅用一句话陈述，没有给出形式化推导或证明。对于一个方法论贡献，这个 connection 需要 at least a brief formal argument showing how the Shapley formula specializes to the LOO case and yields the ISR formula。此外，LOO 会 underestimate necessity when components are jointly necessary but individually removable——论文承认 \"LOO is conservative\" 但未量化 joint-necessity 在实际 FOL formalizations 中的频率。\n- 建议：在 Appendix 中补充一个简短的形式化推导；报告 higher-order ablation（e.g., leave-two-out）在 subset of samples 上的结果以量化 LOO 的 conservatism。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 1 caption 提到 \"n=2 artifact\"，指 Seed 43 的 ISR 在 n=2 时可能为 artifact，但正文未详细解释。建议在 caption 中补充简要说明。\n- **M2**: Section 2 Related Work 提到 Goodhart's Law 的 regressional variant（Manheim and Garrabrant, 2019），但论文未系统 map 观察到的现象属于 Goodhart 的哪个 variant（regressional vs. extremal vs. causal vs. adversarial）。\n- **M3**: Appendix E 声明使用 Claude (Anthropic) 作为 AI coding assistant，符合 ACL policy，但未说明 Claude 是否参与了论文写作本身。\n- **M4**: Table 1 中 \"N-H%\" 列的定义（non-hacking percentage）首次出现时可添加更明确的定义。\n- **M5**: Bonferroni k=14 的 14 个 comparisons 未在正文中明确列出（仅在 Section 4.1 提到 \"Bonferroni k=14\"）。\n\n---\n\n## Questions for Authors\n\n1. 如果排除 seed 43，Table 5 的 Fisher exact test 和 CMH test 结果如何变化？aggregate non-hacking rates 是否仍然显著？\n2. 是否有计划运行更多 seeds（e.g., 10-15 seeds）以获得更可靠的 seed-level proportion estimate？\n3. LOO ablation 中，joint-necessity（两个 component 单独可移除但联合必要）在 FOLIO dataset 中的频率大约是多少？是否做过 leave-two-out 实验？\n4. Premise-count matched comparison (p=0.317) 暗示 ISR scalar 可能主要是 premise-count 的 proxy。作者如何回应 \"ISR is just a complexity proxy\" 的 alternative explanation？\n5. Hacking classifier 对 TS（tautological shortcut）mode 的 recall 是多少？考虑到 TS 是 dominant mode，classifier 的 false-negative rate 对 hacking rate estimates 的影响有多大？\n\n---\n\n## 主要优势\n\n- **S1**: STA 诊断方法定义清晰，计算高效（O(n) vs. O(2^n) Shapley），对任何基于形式化验证的 RL 系统都有即插即用的适用性。\n- **S2**: 8-mode hacking taxonomy 是该领域最详尽的分类之一，每个 mode 都有定义、示例和 ISR interaction 分析（Appendix C），为后续研究提供了有价值的 analytical framework。\n- **S3**: 论文设计了多层控制条件（exec-only, ISR, random, shuffled-ISR, SFT），每个条件都有明确的对照意义，实验设计总体上是 well-thought-out 的。\n- **S4**: \"Observe but don't optimize\" 的 framing 简洁有力，直接连接到 Goodhart's Law 的核心 insight，对 RLVR community 有清晰的 practical message。\n- **S5**: 论文在 Appendix 中提供了大量 per-seed 详细结果（Tables 9-14），transparency 值得肯定。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: STA 诊断方法新颖实用，hacking taxonomy 详尽，但核心发现（seed-dependent Goodhart effect）的统计基础过薄——3-5 seeds 不足以支撑 proportion claims，seed 43 协议偏差未充分隔离，pooled independence 假设需更严格处理。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | STA 定义严谨，LOO 假设局限已声明；但 3-5 seeds 统计效力不足以支撑 \"3/5 converge to gaming\" 的 proportion claim；seed 43 协议偏差（T=0.7 sampling vs greedy）未从聚合统计中排除；pooled Fisher exact test 将 within-seed samples 当作独立样本 |\n| Excitement | 3.5/5 | 诊断 RLVR 中 Goodhart effect 的问题重要且及时；STA 和 hacking taxonomy 是有价值的方法论贡献；但 ISR-as-reward 的 negative result 限制了可操作的实践影响 |\n| Reproducibility | 3/5 | 超参数报告详尽（Table 2, Appendix A）；外部 solver（Prover9, SWI-Prolog）可获取；hacking classifier 规则描述了但非机器可读格式；代码/数据承诺公开但未提供 |\n| Reviewer Confidence | 4/5 | 熟悉 RLVR、reward hacking 和 neurosymbolic reasoning 领域；仔细检查了统计声明 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 3-5 seeds 的统计效力不足以支撑核心 claim\n- 具体位置：Section 4.1 (\"Three to five seeds per condition\"), Section 4.2 (\"3/5 seeds converge to gaming\"), Figure 3, Table 1\n- 问题：论文的核心发现是 \"seed-dependent Goodhart effect\"——3/5 seeds 收敛至 gaming，2/5 保留 genuine reasoning。但 3-5 个 seeds 的 binomial 置信区间极宽：观察到 3/5=60% 的 95% CI 为 [15%, 95%]（Clopper-Pearson）。论文将 \"3/5\" 当作一个有意义的比例来讨论（Section 4.2: \"seed-dependent\"），但这个比例完全可能是 20% 或 80%，统计上无法区分。Section 6 Limitations 提到 \"three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance\"，但主文的叙述语气远比这个 caveat 强。\n- 为什么影响接收：这是论文的 **central empirical contribution (C2)**。如果 seed-level proportion 不可靠，则 \"seed-dependent\" 的 characterization 缺乏定量支撑，读者无法判断该现象的 prevalence。\n- 建议修改方向：(a) 增加至 10-15 seeds（至少 exec-only 条件下）以获得有意义的 proportion estimate；(b) 或者将 claim 从 \"3/5 seeds converge\" 改为 \"we observe convergence in multiple seeds under identical conditions, but the exact proportion remains uncertain\"，并将 3/5 明确标注为 point estimate with wide CI。\n\n**N2** [critical] Seed 43 评估协议偏差未与聚合统计隔离\n- 具体位置：Section 4.1 脚注 7（\"Seed 43 uses nucleus sampling (T=0.7) due to greedy-mode degeneration\"）, Table 1, Table 5, all aggregate statistics\n- 问题：Seed 43 使用 T=0.7 sampling 而非 greedy decoding，与其他 seeds 的评估协议不同。论文在脚注 7 声明 \"Its PR and ISR values are included for completeness but not strictly comparable with other seeds under the identical evaluation protocol (§D6).\"。然而，seed 43 仍然被纳入：(1) Table 1 的 \"3-seed mean\" 行；(2) Table 5 的 pooled Fisher exact test（n=231, 3 seeds）；(3) \"3/5 seeds converge to gaming\" 的 proportion 计算。如果 seed 43 的结果 \"not strictly comparable\"，则不应参与这些聚合分析，或至少应报告排除 seed 43 后的结果。\n- 为什么影响接收：混合不同评估协议的结果违反实验设计的 internal consistency。Seed 43 恰好是 ISR collapse 最剧烈的 seed（ISR→0.03 at 1000 steps, Table 9），其纳入或排除直接影响聚合统计的结论。\n- 建议修改方向：报告排除 seed 43 的 sensitivity analysis；或统一所有 seeds 的评估协议（全部用 greedy 或全部用 sampling）后重新报告。\n\n**N3** [critical] Pooled Fisher exact test 将 within-seed samples 视为独立——统计推断可能 inflated\n- 具体位置：Table 5（Fisher exact tests, n=231 3-seed pooled）, Section 4.1 (\"pooled statistics trend within-seed samples as independent\"), Appendix C.1\n- 问题：每个 seed 产出的 ~77 个 proved samples 共享同一套 model weights，因此 within-seed samples 之间高度相关（intra-class correlation 可能很大）。将它们当作 231 个独立样本进行 Fisher exact test 会严重低估 p-value、高估统计显著性。论文使用了 Cochran-Mantel-Haenszel (CMH) test 作为 seed-stratified 替代方案，但 CMH test 仅在 Appendix D.6 的 premise-count confound 讨论中出现，而非 Table 5 的核心 hacking-rate 比较。Section 4.1 用一句话 acknowledge 了这个问题（\"pooled Cochran Mantel Haenszel p-values\"），但 Table 5 的 primary test 仍然是 pooled Fisher exact test。\n- 为什么影响接收：如果 effective sample size 仅为 3（seeds），而非 231（samples），则 Table 5 中 p<10^-10 级别的显著性可能大幅缩水。这直接影响 contribution C1（hacking rate differences across conditions）和 C2（seed-dependent patterns）的统计可信度。\n- 建议修改方向：(a) 将 CMH test（seed-stratified）作为 primary test 在 Table 5 中报告；(b) 报告 seed-level non-hacking rates 的 variance 和 intra-class correlation；(c) 或使用 cluster-robust standard errors（clustering on seed）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] ISR 与 premise-count 的 confound 部分 undermines ISR 作为独立诊断指标的价值\n- 具体位置：Section 4.3 (\"Premise-count confound\"), Table 4, Appendix D.6\n- 问题：Table 4 表明 ISR collapse 主要由 premise-count reduction 解释——ISR-trained models 产出更短的 formalizations。Premise-count matched comparison 显示 scalar ISR advantage 不显著（McNemar's test p=0.317, n=100 matched pairs）。论文将此框架为 \"the mode breakdown, not the ISR scalar, licenses interpretation\"（Section 4.3），但这意味着论文标题中的 \"Structural Rewards\"（ISR scalar）本身不是合适的训练信号，而真正有信息量的是 mode-level 分解。这个结论与论文叙述有张力——如果 ISR scalar 是 premise-count 的 proxy，则 ISR-as-reward 的 Goodhart effect 可能只是在惩罚短 formalizations，而非优化 structural integrity。\n- 建议：在 Discussion 中更明确地讨论这个张力；考虑报告 premise-count-normalized ISR 的训练曲线。\n\n**W2** [warning] Cross-domain 实验不够充分\n- 具体位置：Section 4.4, Figure 5, Table 11, Appendix D.7\n- 问题：\n  - **Prolog**：仅有 exec-only 条件（3 seeds），无 ISR-as-reward 条件。论文声称 \"cross-domain replication\" (C3)，但 Prolog 实验仅验证了 ISR collapse 在 exec-only 下发生，未验证 ISR-as-reward 是否也触发 Goodhart effect。\n  - **ProofFOL**：p=0.10 不显著（even before Bonferroni），但 Section 4.4 仍然以 \"dataset-dependent asymmetry\" 进行解读。\n  - **Qwen3-8B**：Appendix D.7 仅用 K=4/K=8 rollouts 和 exec-only，结论 \"4B-like patterns\" 但 sample size 极小。\n- 建议：(a) 如果计算资源允许，在 Prolog 上运行 ISR-as-reward 条件；(b) 将 ProofFOL p=0.10 的解读降级为 \"suggestive but inconclusive\"；(c) 明确标注 C3 的支撑强度较弱。\n\n**W3** [warning] \"Degeneration requires convergence\" 的因果 claim 过强\n- 具体位置：Section 4.1 (\"structural degeneration requires successful RL optimization as a prerequisite\"), Appendix D.4 (LLaMA-3.2-3B), Appendix D.7 (Qwen3-8B)\n- 问题：LLaMA-3.2-3B cold-start failure（Appendix D.4）是因为模型连 valid FOL syntax 都无法生成，所以不 degenerate 是 trivially expected 的——这不能支撑 \"convergence is a prerequisite for degeneration\" 的因果推断，因为 confounded by capability。真正有力的证据需要一个能生成 valid FOL 但 RL 未能 converge（e.g., 因为 reward noise）的 setting。Qwen3-8B 实验有类似问题——non-convergence cases 的 confound（K=4 insufficient rollouts）使因果推断不干净。\n- 建议：将 claim 弱化为 \"our evidence is consistent with convergence being necessary, but the confound between model capability and convergence makes causal attribution difficult\"。\n\n**W4** [warning] Hacking taxonomy 的 completeness 和 classifier recall 评估不足\n- 具体位置：Section 3.3, Appendix C (Hacking Mode Definitions), Table 8 (Classifier Validation)\n- 问题：\n  - **Completeness**：论文声称 8 modes 覆盖了所有观察到的 hacking patterns，但 Table 7 中 \"Non-hacking\" 类别仍占 5-92 个样本（不同条件下）。这些 non-hacking 样本中可能存在未被 taxonomy 覆盖的 hacking modes。\n  - **Classifier recall**：Table 8 报告 precision（50 manually verified samples, estimated >95%），但 recall 评估依赖间接方法：\"cross-validation revealed query-as-fact in Prolog (§C.9), where the strict text classifier reported 100% non-hacking but functional analysis showed 95/97 samples were tautological\"（p15）。这表明 classifier 对某些 modes 的 recall 很低，特别是对需要 semantic understanding 的 modes（如 paraphrased conclusions）。\n  - **Mutual exclusivity**：Section 3.3 提到 \"multi-mode samples\" 但未详细报告 overlap rates。\n- 建议：报告 classifier 的 per-mode recall estimate（至少对 dominant modes CE 和 TS）；讨论 taxonomy 是否 exhaustive 或仅覆盖 dominant patterns。\n\n**W5** [warning] ISR 作为 Shapley value 特殊情况的声明缺乏形式化证明\n- 具体位置：Section 3.2（\"ISR is a special case of the (n-1)-conditional Shapley value (Lundberg and Lee, 2017)\"）\n- 问题：这个声明仅用一句话陈述，没有给出形式化推导或证明。对于一个方法论贡献，这个 connection 需要 at least a brief formal argument showing how the Shapley formula specializes to the LOO case and yields the ISR formula。此外，LOO 会 underestimate necessity when components are jointly necessary but individually removable——论文承认 \"LOO is conservative\" 但未量化 joint-necessity 在实际 FOL formalizations 中的频率。\n- 建议：在 Appendix 中补充一个简短的形式化推导；报告 higher-order ablation（e.g., leave-two-out）在 subset of samples 上的结果以量化 LOO 的 conservatism。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Figure 1 caption 提到 \"n=2 artifact\"，指 Seed 43 的 ISR 在 n=2 时可能为 artifact，但正文未详细解释。建议在 caption 中补充简要说明。\n- **M2**: Section 2 Related Work 提到 Goodhart's Law 的 regressional variant（Manheim and Garrabrant, 2019），但论文未系统 map 观察到的现象属于 Goodhart 的哪个 variant（regressional vs. extremal vs. causal vs. adversarial）。\n- **M3**: Appendix E 声明使用 Claude (Anthropic) 作为 AI coding assistant，符合 ACL policy，但未说明 Claude 是否参与了论文写作本身。\n- **M4**: Table 1 中 \"N-H%\" 列的定义（non-hacking percentage）首次出现时可添加更明确的定义。\n- **M5**: Bonferroni k=14 的 14 个 comparisons 未在正文中明确列出（仅在 Section 4.1 提到 \"Bonferroni k=14\"）。\n\n---\n\n## Questions for Authors\n\n1. 如果排除 seed 43，Table 5 的 Fisher exact test 和 CMH test 结果如何变化？aggregate non-hacking rates 是否仍然显著？\n2. 是否有计划运行更多 seeds（e.g., 10-15 seeds）以获得更可靠的 seed-level proportion estimate？\n3. LOO ablation 中，joint-necessity（两个 component 单独可移除但联合必要）在 FOLIO dataset 中的频率大约是多少？是否做过 leave-two-out 实验？\n4. Premise-count matched comparison (p=0.317) 暗示 ISR scalar 可能主要是 premise-count 的 proxy。作者如何回应 \"ISR is just a complexity proxy\" 的 alternative explanation？\n5. Hacking classifier 对 TS（tautological shortcut）mode 的 recall 是多少？考虑到 TS 是 dominant mode，classifier 的 false-negative rate 对 hacking rate estimates 的影响有多大？\n\n---\n\n## 主要优势\n\n- **S1**: STA 诊断方法定义清晰，计算高效（O(n) vs. O(2^n) Shapley），对任何基于形式化验证的 RL 系统都有即插即用的适用性。\n- **S2**: 8-mode hacking taxonomy 是该领域最详尽的分类之一，每个 mode 都有定义、示例和 ISR interaction 分析（Appendix C），为后续研究提供了有价值的 analytical framework。\n- **S3**: 论文设计了多层控制条件（exec-only, ISR, random, shuffled-ISR, SFT），每个条件都有明确的对照意义，实验设计总体上是 well-thought-out 的。\n- **S4**: \"Observe but don't optimize\" 的 framing 简洁有力，直接连接到 Goodhart's Law 的核心 insight，对 RLVR community 有清晰的 practical message。\n- **S5**: 论文在 Appendix 中提供了大量 per-seed 详细结果（Tables 9-14），transparency 值得肯定。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2405 · 2026-05-24T22:56:09.880231+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3920
}
```

</details>

---


### Assistant

_source line 2406 · 2026-05-24T22:56:22.234088+00:00_

审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。论文提出的 STA 诊断方法和 8-mode hacking taxonomy 是扎实的方法论贡献，但三个 critical 问题需要解决：

1. **3-5 seeds 统计效力不足**——"3/5 converge to gaming" 的 95% CI 为 [15%, 95%]，proportion claim 无法可靠估计
2. **Seed 43 评估协议偏差**——T=0.7 sampling vs greedy，却仍被纳入聚合统计
3. **Pooled Fisher test 的独立性假设**——within-seed samples 高度相关，p-value 可能严重 inflated

此外还有 5 个 Should-Fix（ISR-premise confound、cross-domain 实验薄弱、因果 claim 过强、classifier recall 不足、Shapley 声明缺证明）和 5 个 minor issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 67

## Round 67

4 recorded events


### User

_source line 2407 · 2026-05-24T23:03:32.279858+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1/N2) 和 Should-Fix (W1-W5) 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见

**Overall Assessment: 3.5 (Borderline Conference)**

**一句话总结**: 扎实的实证论文，在 neurosymbolic reasoning 中发现了有价值的 Goodhart 效应和 seed-dependent 行为，实验控制设计严谨，但方法论创新有限（LOO ablation 是标准技术），核心发现（optimize proxy → Goodhart）的理论预期性较高。

### Must-Fix

**N1** [critical] **C3 贡献声称与实际证据不匹配：跨域泛化声明 underpowered**
- 论文将 C3 列为三大贡献之一："cross-domain replication: the Goodhart effect transfers across logic types (FOL/Prolog) and dataset families (FOLIO/ProofFOL), establishing that structural degeneration under RLVR is not dataset-specific"。但 ProofFOL 结果是 "exploratory and underpowered" (p=0.10, N=3)。将 underpowered 的探索性结果包装为正式贡献（C3），并使用 "establishing" 这样的强断言语言，构成了 overclaim。

**N2** [critical] **ISR 作为 scalar metric 的诊断价值在控制 premise-count 后基本消失，但论文仍以 ISR 为核心框架**
- ISR* 的 214× collapse 在控制 premise count 后缩小到 1.06×（McNemar p=0.317, 不显著）。如果 ISR scalar 在控制后不再有诊断力，那么论文的框架（以 ISR 作为核心 metric）与实际诊断机制（mode taxonomy）之间存在张力。

### Should-Fix

**W1** [warning] **"Observe-vs-optimize asymmetry" 本质上是 Goodhart's Law 的领域特化表述，概念包装超出实际新意**

**W2** [warning] **Table 1 可读性严重不足** — caption 约 150 词，4 个脚注标记，读者需要反复在表格和 caption 之间跳转。

**W3** [warning] **信息密度过高，部分结果浅尝辄止** — 8 页包含 6 个 reward conditions × 3-5 seeds、8-mode taxonomy、Prolog/ProofFOL/8B 三个跨域实验，每个子结果讨论深度不足。

**W4** [warning] **Hacking classifier recall unknown，non-hacking rate 的解释力受限** — classifier recall 未知，N-H rate 可能是 "substantially inflated upper bound"。

**W5** [warning] **Abstract 最后一句含脚注引用代码/数据链接** — [anonymized] 无实际信息，影响 abstract 简洁性。

### 小问题
1. ISR 作为 metric vs reward 的术语一致性
2. Figure 1 Y 轴标签字体较小
3. Equation 1 缺少 "proved only" 的形式化条件
4. Binary variant 未在 Method 中正式引入
5. References 格式混用 arXiv 和会议格式

### Reviewer 2 的新颖性评估
- STA/ISR 方法新颖性有限（LOO 是标准技术），但应用层面发现有价值
- Goodhart 发现的理论预期性较高，真正贡献在于具体机制（TS > CE shift, seed dependency, cross-logic）
- C1+C2 仍构成合理的会议论文贡献，但 C3 需 scope down

---

请对以上每个 N/W 问题逐条回应 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-24T23:05:11.495121+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: C3 跨域泛化声称 overclaim**\n\n同意。我在自己的审稿中将此列为 W2（Should-Fix），但 R2 的 escalation 到 Must-Fix 是合理的。理由：\n\n1. ProofFOL 的 p=0.10 即使不做 Bonferroni 校正也不显著，论文 Section 4.4 仍以 \"dataset-dependent asymmetry\" 进行解读，且 C3 使用 \"establishing\" 这一强断言动词。\n2. Prolog 实验（Figure 5）仅有 exec-only 条件，**未运行 ISR-as-reward 条件**，因此 C3 声称的 \"Goodhart effect transfers across logic types\" 在 Prolog 上只验证了 ISR collapse（诊断端），未验证 Goodhart effect（优化端）。\n3. 我补充一点 R2 未提及的：Qwen3-8B 跨规模实验（Appendix D.7）同样仅用 exec-only + K=4/8 rollouts，sample size 极小，不足以支撑 \"cross-scale\" 的泛化声明。\n\n**建议统一意见**：C3 应 scope down 为 \"preliminary cross-domain evidence\"，去掉 \"establishing\"，并明确标注 ProofFOL 结果为 exploratory。\n\n---\n\n**[AGREE with nuance] R2-N2: ISR scalar 在控制 premise-count 后诊断价值减弱**\n\n基本同意，但需加 nuance。我在自己的审稿中将此列为 W1。\n\n**同意的部分**：\n- Table 4 的 McNemar p=0.317（n=100 matched pairs）确实表明 scalar ISR 在控制 premise count 后不再显著区分 hacking vs. genuine。\n- 论文标题 \"Structural Rewards\"、核心概念 ISR、以及 ISR-as-reward 的实验设计都以 ISR scalar 为中心，与 Section 4.3 \"the mode breakdown, not the ISR scalar, licenses interpretation\" 的结论存在框架张力。\n\n**需要 nuance 的部分**：\n- R2 说 ISR scalar 的诊断价值 \"基本消失\" 稍有过度。ISR 作为 **screening metric** 仍有用——low ISR（≤0.5）的样本中 hacking prevalence 显著高于 high ISR 样本（这从 Figure 4 的 premise-bin 分析可以看出）。问题不是 ISR 完全无信息，而是 ISR 的信息量被 premise count 这个 confounder 大量解释。\n- 论文已在 Section 4.3 明确承认了这一点，且将诊断重心转移到 mode taxonomy——这个 pivot 是合理的，但正如 R2 指出，与论文整体 ISR-centric framing 不协调。\n\n**我的判断**：这是一个 framing/presentation 问题而非 soundness 问题。如果作者调整叙述重心（从 \"ISR scalar is the diagnostic\" 到 \"ISR scalar is a fast screening tool, mode taxonomy is the real diagnostic\"），这个问题可解决。列为 Should-Fix 更合适，但我理解 R2 将其升级到 Must-Fix 的逻辑。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: \"Observe-vs-optimize asymmetry\" 概念包装超出实际新意**\n\n不同意此条。理由：\n\n1. **理论预期性 ≠ 缺乏贡献**。R2 认为 \"optimize proxy → Goodhart\" 是 Goodhart's Law 的 trivial application，但论文的贡献不在于 **预测** Goodhart effect 会发生，而在于 **具体记录** 它 **如何** 发生：(a) 哪些 gaming modes 被选择（TS dominates over CE），(b) mode composition 如何随 reward condition 变化（ISR systematically selects for TS over CE, Table 1 Figure 6），(c) 效应是 seed-dependent 的（2/5 seeds retain genuine reasoning）。这些 **specific mechanistic findings** 不能从 Goodhart's Law 的抽象陈述中推导出来。\n2. **\"Observe but don't optimize\" 的 practical message** 是针对 RLVR community 的具体 actionable insight——STA 可以作为 post-hoc diagnostic 但不应作为 training reward。这个 framing 比简单引用 Goodhart's Law 更有操作价值。\n3. 类比：Gao et al. (2023) 和 Skalse et al. (2022) 的 reward hacking 工作也是 Goodhart's Law 的 \"领域特化\"，但仍被顶会接收，因为 domain-specific 的实证贡献有独立价值。\n\n**结论**：论文的贡献在于 empirical mechanism，不是 theoretical novelty。W1 的批评标准不适用于 empirical paper。\n\n---\n\n**[AGREE] R2-W2: Table 1 可读性不足**\n\n同意。Table 1 承载了 6 个条件 × 多个 metrics（PR, ISR*, TS%, CE%, N-H%）+ 4 个脚注标记 + ~150 词 caption。读者需要在表格、caption、和脚注之间反复跳转。我在自己的审稿中未单独列出此点，但 R2 指出后我认为这确实影响了论文的可读性。\n\n建议拆分为两个表格（一个 core results，一个 control conditions），或简化 caption 并将 footnote 内容移入正文。\n\n---\n\n**[AGREE with qualification] R2-W3: 信息密度过高，部分结果深度不足**\n\n部分同意。8 页正文确实覆盖了大量内容：6 reward conditions, 8-mode taxonomy, 3 logic types, cross-scale experiments。但我认为：\n\n1. **Appendix 提供了必要的深度**——per-seed results (Tables 9-14), hacking mode definitions (Appendix C), per-seed trajectory analysis (Appendix D) 总计 16 页 appendix，单独看深度是足够的。\n2. **问题在于正文的 signposting**：正文在 §4.2-4.4 的每个子结果仅用 1-2 段，读者难以判断哪些发现是核心的、哪些是辅助的。\n\n建议作者在正文中更明确地标注 primary vs. secondary findings 的层级关系，而非平铺直叙。\n\n---\n\n**[AGREE] R2-W4: Hacking classifier recall 未知**\n\n完全同意，我在自己的审稿中将此列为 W4，与 R2 的诊断一致。补充几点：\n\n1. Table 8 的 precision 验证基于 50 个 manually verified samples（estimated >95%），但 recall 评估仅有间接证据。\n2. 论文自己在 p15 承认 \"the strict text classifier reported 100% non-hacking but functional analysis showed 95/97 samples were tautological\"——这意味着对 Prolog 的 TS mode，classifier recall 接近 **0%**（需要 functional analysis 才能检出）。虽然 Prolog classifier 不同于 FOL classifier，但这暴露了 rule-based classifier 对 semantic gaming 的系统性盲区。\n3. 如 R2 所说，如果 recall 较低，Table 1 的 N-H% 是 non-hacking rate 的 **上界**，实际 hacking 可能更严重。这不影响论文的定性结论（hacking exists and varies across conditions），但影响定量解读。\n\n---\n\n**[AGREE] R2-W5: Abstract 脚注**\n\n同意，这是一个 minor formatting 问题。Abstract 中的 [anonymized] 脚注无实际信息内容，应移除或移至 Section 1 末尾。\n\n---\n\n### R2 小问题逐条回应\n\n1. **ISR 术语一致性** — [AGREE] ISR 同时指 metric 和 reward，论文应在首次定义时明确区分 ISR-diagnostic vs. ISR-reward。\n2. **Figure 1 Y 轴字体** — [AGREE] 可读性问题，minor。\n3. **Equation 1 缺少 \"proved only\" 条件** — [AGREE] 形式化不完整，ISR 定义（Equation 1）应在公式中显式标注 \"defined for proved formalizations only\"，目前这个约束仅出现在正文中。\n4. **Binary variant 未正式引入** — [AGREE] Appendix B 提到 \"proved-only ISR (denoted ISR↑)\" 但 Method section 未定义。\n5. **References 格式混用** — [AGREE] Minor formatting issue。\n\n---\n\n### R2 新颖性评估回应\n\nR2 认为 \"STA/ISR 方法新颖性有限（LOO 是标准技术）\"，我 **部分不同意**：\n\n- LOO ablation 本身是标准技术，但 **将 LOO 应用于 solver trace 并定义 ISR metric 来量化 neurosymbolic reasoning 的 structural integrity** 是新的 application。此前的 process reward models（Lightman et al., 2024）和 inference-time gaming detection（Kim et al., 2026）都不提供 LOO-based 的 component-level diagnostic。\n- 真正的新颖性在于 **将诊断方法反转为训练信号并记录 Goodhart 效应的具体机制**——这个实验设计不是 LOO 的标准应用。\n- 但我同意 R2 的结论：\"C1+C2 仍构成合理的会议论文贡献，但 C3 需 scope down\"。\n\n---\n\n### 总结\n\n| R2 Issue | 我的判断 | 与我自己审稿的对应 |\n|----------|---------|----------------|\n| N1 (C3 overclaim) | AGREE | 对应我的 W2，同意升级到 Must-Fix |\n| N2 (ISR scalar confounded) | AGREE with nuance | 对应我的 W1，认为是 framing 问题而非 soundness 问题 |\n| W1 (概念新意有限) | REBUT | 我的 S4 列为 strength |\n| W2 (Table 1 可读性) | AGREE | 我未单独标注 |\n| W3 (信息密度过高) | AGREE with qualification | Appendix 提供了深度，正文 signposting 不足 |\n| W4 (Classifier recall) | AGREE | 对应我的 W4 |\n| W5 (Abstract footnote) | AGREE | Minor |\n\n两位 reviewer 的 **共识 Must-Fix**：C3 跨域声称需 scope down。\n两位 reviewer 的 **共识 Should-Fix**：ISR-premise-count confound 的 framing 张力、classifier recall 评估不足。\n**分歧点**：R2-W1（概念新意）——我认为 empirical mechanism 的贡献独立于理论预期性。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: C3 跨域泛化声称 overclaim**\n\n同意。我在自己的审稿中将此列为 W2（Should-Fix），但 R2 的 escalation 到 Must-Fix 是合理的。理由：\n\n1. ProofFOL 的 p=0.10 即使不做 Bonferroni 校正也不显著，论文 Section 4.4 仍以 \"dataset-dependent asymmetry\" 进行解读，且 C3 使用 \"establishing\" 这一强断言动词。\n2. Prolog 实验（Figure 5）仅有 exec-only 条件，**未运行 ISR-as-reward 条件**，因此 C3 声称的 \"Goodhart effect transfers across logic types\" 在 Prolog 上只验证了 ISR collapse（诊断端），未验证 Goodhart effect（优化端）。\n3. 我补充一点 R2 未提及的：Qwen3-8B 跨规模实验（Appendix D.7）同样仅用 exec-only + K=4/8 rollouts，sample size 极小，不足以支撑 \"cross-scale\" 的泛化声明。\n\n**建议统一意见**：C3 应 scope down 为 \"preliminary cross-domain evidence\"，去掉 \"establishing\"，并明确标注 ProofFOL 结果为 exploratory。\n\n---\n\n**[AGREE with nuance] R2-N2: ISR scalar 在控制 premise-count 后诊断价值减弱**\n\n基本同意，但需加 nuance。我在自己的审稿中将此列为 W1。\n\n**同意的部分**：\n- Table 4 的 McNemar p=0.317（n=100 matched pairs）确实表明 scalar ISR 在控制 premise count 后不再显著区分 hacking vs. genuine。\n- 论文标题 \"Structural Rewards\"、核心概念 ISR、以及 ISR-as-reward 的实验设计都以 ISR scalar 为中心，与 Section 4.3 \"the mode breakdown, not the ISR scalar, licenses interpretation\" 的结论存在框架张力。\n\n**需要 nuance 的部分**：\n- R2 说 ISR scalar 的诊断价值 \"基本消失\" 稍有过度。ISR 作为 **screening metric** 仍有用——low ISR（≤0.5）的样本中 hacking prevalence 显著高于 high ISR 样本（这从 Figure 4 的 premise-bin 分析可以看出）。问题不是 ISR 完全无信息，而是 ISR 的信息量被 premise count 这个 confounder 大量解释。\n- 论文已在 Section 4.3 明确承认了这一点，且将诊断重心转移到 mode taxonomy——这个 pivot 是合理的，但正如 R2 指出，与论文整体 ISR-centric framing 不协调。\n\n**我的判断**：这是一个 framing/presentation 问题而非 soundness 问题。如果作者调整叙述重心（从 \"ISR scalar is the diagnostic\" 到 \"ISR scalar is a fast screening tool, mode taxonomy is the real diagnostic\"），这个问题可解决。列为 Should-Fix 更合适，但我理解 R2 将其升级到 Must-Fix 的逻辑。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: \"Observe-vs-optimize asymmetry\" 概念包装超出实际新意**\n\n不同意此条。理由：\n\n1. **理论预期性 ≠ 缺乏贡献**。R2 认为 \"optimize proxy → Goodhart\" 是 Goodhart's Law 的 trivial application，但论文的贡献不在于 **预测** Goodhart effect 会发生，而在于 **具体记录** 它 **如何** 发生：(a) 哪些 gaming modes 被选择（TS dominates over CE），(b) mode composition 如何随 reward condition 变化（ISR systematically selects for TS over CE, Table 1 Figure 6），(c) 效应是 seed-dependent 的（2/5 seeds retain genuine reasoning）。这些 **specific mechanistic findings** 不能从 Goodhart's Law 的抽象陈述中推导出来。\n2. **\"Observe but don't optimize\" 的 practical message** 是针对 RLVR community 的具体 actionable insight——STA 可以作为 post-hoc diagnostic 但不应作为 training reward。这个 framing 比简单引用 Goodhart's Law 更有操作价值。\n3. 类比：Gao et al. (2023) 和 Skalse et al. (2022) 的 reward hacking 工作也是 Goodhart's Law 的 \"领域特化\"，但仍被顶会接收，因为 domain-specific 的实证贡献有独立价值。\n\n**结论**：论文的贡献在于 empirical mechanism，不是 theoretical novelty。W1 的批评标准不适用于 empirical paper。\n\n---\n\n**[AGREE] R2-W2: Table 1 可读性不足**\n\n同意。Table 1 承载了 6 个条件 × 多个 metrics（PR, ISR*, TS%, CE%, N-H%）+ 4 个脚注标记 + ~150 词 caption。读者需要在表格、caption、和脚注之间反复跳转。我在自己的审稿中未单独列出此点，但 R2 指出后我认为这确实影响了论文的可读性。\n\n建议拆分为两个表格（一个 core results，一个 control conditions），或简化 caption 并将 footnote 内容移入正文。\n\n---\n\n**[AGREE with qualification] R2-W3: 信息密度过高，部分结果深度不足**\n\n部分同意。8 页正文确实覆盖了大量内容：6 reward conditions, 8-mode taxonomy, 3 logic types, cross-scale experiments。但我认为：\n\n1. **Appendix 提供了必要的深度**——per-seed results (Tables 9-14), hacking mode definitions (Appendix C), per-seed trajectory analysis (Appendix D) 总计 16 页 appendix，单独看深度是足够的。\n2. **问题在于正文的 signposting**：正文在 §4.2-4.4 的每个子结果仅用 1-2 段，读者难以判断哪些发现是核心的、哪些是辅助的。\n\n建议作者在正文中更明确地标注 primary vs. secondary findings 的层级关系，而非平铺直叙。\n\n---\n\n**[AGREE] R2-W4: Hacking classifier recall 未知**\n\n完全同意，我在自己的审稿中将此列为 W4，与 R2 的诊断一致。补充几点：\n\n1. Table 8 的 precision 验证基于 50 个 manually verified samples（estimated >95%），但 recall 评估仅有间接证据。\n2. 论文自己在 p15 承认 \"the strict text classifier reported 100% non-hacking but functional analysis showed 95/97 samples were tautological\"——这意味着对 Prolog 的 TS mode，classifier recall 接近 **0%**（需要 functional analysis 才能检出）。虽然 Prolog classifier 不同于 FOL classifier，但这暴露了 rule-based classifier 对 semantic gaming 的系统性盲区。\n3. 如 R2 所说，如果 recall 较低，Table 1 的 N-H% 是 non-hacking rate 的 **上界**，实际 hacking 可能更严重。这不影响论文的定性结论（hacking exists and varies across conditions），但影响定量解读。\n\n---\n\n**[AGREE] R2-W5: Abstract 脚注**\n\n同意，这是一个 minor formatting 问题。Abstract 中的 [anonymized] 脚注无实际信息内容，应移除或移至 Section 1 末尾。\n\n---\n\n### R2 小问题逐条回应\n\n1. **ISR 术语一致性** — [AGREE] ISR 同时指 metric 和 reward，论文应在首次定义时明确区分 ISR-diagnostic vs. ISR-reward。\n2. **Figure 1 Y 轴字体** — [AGREE] 可读性问题，minor。\n3. **Equation 1 缺少 \"proved only\" 条件** — [AGREE] 形式化不完整，ISR 定义（Equation 1）应在公式中显式标注 \"defined for proved formalizations only\"，目前这个约束仅出现在正文中。\n4. **Binary variant 未正式引入** — [AGREE] Appendix B 提到 \"proved-only ISR (denoted ISR↑)\" 但 Method section 未定义。\n5. **References 格式混用** — [AGREE] Minor formatting issue。\n\n---\n\n### R2 新颖性评估回应\n\nR2 认为 \"STA/ISR 方法新颖性有限（LOO 是标准技术）\"，我 **部分不同意**：\n\n- LOO ablation 本身是标准技术，但 **将 LOO 应用于 solver trace 并定义 ISR metric 来量化 neurosymbolic reasoning 的 structural integrity** 是新的 application。此前的 process reward models（Lightman et al., 2024）和 inference-time gaming detection（Kim et al., 2026）都不提供 LOO-based 的 component-level diagnostic。\n- 真正的新颖性在于 **将诊断方法反转为训练信号并记录 Goodhart 效应的具体机制**——这个实验设计不是 LOO 的标准应用。\n- 但我同意 R2 的结论：\"C1+C2 仍构成合理的会议论文贡献，但 C3 需 scope down\"。\n\n---\n\n### 总结\n\n| R2 Issue | 我的判断 | 与我自己审稿的对应 |\n|----------|---------|----------------|\n| N1 (C3 overclaim) | AGREE | 对应我的 W2，同意升级到 Must-Fix |\n| N2 (ISR scalar confounded) | AGREE with nuance | 对应我的 W1，认为是 framing 问题而非 soundness 问题 |\n| W1 (概念新意有限) | REBUT | 我的 S4 列为 strength |\n| W2 (Table 1 可读性) | AGREE | 我未单独标注 |\n| W3 (信息密度过高) | AGREE with qualification | Appendix 提供了深度，正文 signposting 不足 |\n| W4 (Classifier recall) | AGREE | 对应我的 W4 |\n| W5 (Abstract footnote) | AGREE | Minor |\n\n两位 reviewer 的 **共识 Must-Fix**：C3 跨域声称需 scope down。\n两位 reviewer 的 **共识 Should-Fix**：ISR-premise-count confound 的 framing 张力、classifier recall 评估不足。\n**分歧点**：R2-W1（概念新意）——我认为 empirical mechanism 的贡献独立于理论预期性。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2409 · 2026-05-24T23:05:15.214036+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3718
}
```

</details>

---


### Assistant

_source line 2410 · 2026-05-24T23:05:20.836377+00:00_

已提交对 Reviewer 2 全部意见的逐条回应。核心判断：

- **N1 (C3 overclaim)**: AGREE，同意升级到 Must-Fix，与我的 W2 一致
- **N2 (ISR confounded)**: AGREE with nuance，本质是 framing 问题而非 soundness 问题
- **W1 (概念新意有限)**: REBUT，empirical mechanism 的贡献独立于理论预期性
- **W2-W5**: 基本 AGREE，与我自己审稿中的发现一致

两位 reviewer 的共识：C3 需 scope down，classifier recall 评估不足。分歧在概念新颖性判断上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 68

## Round 68

78 recorded events


### User

_source line 2411 · 2026-05-25T03:57:01.561983+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性与实验设计**。

## Venue 信息
- **目标**: EMNLP 2026 (ARR 统一审稿)
- **类别**: Long paper
- **正文页数限制**: 8 页（参考文献不计入）
- **匿名**: Double-blind
- **模板**: ACL 2026
- **ARR submission deadline**: 2026-05-25
- **Commitment deadline**: 2026-08-02

## 论文文件
- LaTeX 源码: `projects/solver-trace-ablation/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, related_work.tex, appendix.tex）
- PDF: `projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf`

## 你的审查侧重
1. **STA/ISR 方法有效性**：LOO ablation 作为诊断的理论基础是否充分？ISR 的数学定义是否严谨？Shapley value 联系是否正确？
2. **实验设计**：6 个 reward conditions 的控制是否合理？随机对照组是否充分隔离 ISR-specific 信号？Shuffled-ISR control 是否有效？
3. **统计分析**：3-5 seeds 的统计效力；premise-count confound 的处理；多重比较校正（Bonferroni）；CMH 伪重复问题
4. **Seed 43 异常处理**：sampling (T=0.7) 评估 vs greedy——对结论的影响是否被充分讨论？N=2 sensitivity analysis 是否足够？
5. **跨域泛化**：Prolog 复制的证据强度；ProofFOL p=0.10 的解释是否适当？Qwen3-8B/LLaMA 结果的定位
6. **Hacking taxonomy**：8 模式分类的精度/召回率验证是否充分？152 sample precision audit 是否足够？
7. **因果推断**：convergence→degeneration 的因果声明是否过强？confound 讨论是否充分？

请按 ARR 评分标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-25T03:57:09.411451+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2413 · 2026-05-25T03:57:09.512296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2414 · 2026-05-25T03:57:23.273607+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2415 · 2026-05-25T03:57:23.324498+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2416 · 2026-05-25T03:57:32.416219+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines, review form, and criteria:

## Review Form Criteria

For Main vs Findings papers, the main criteria for Findings are soundness and reproducibility, while confere
…[truncated 1398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9142
}
```

</details>

---


### Tool result

_source line 2417 · 2026-05-25T03:57:33.828311+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 441.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 847.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.8}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 455.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 405.4}], \"total_pages\": 24, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10503
}
```

</details>

---


### Tool call

_source line 2418 · 2026-05-25T03:57:40.509219+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Confidence, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions. List exact scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include: Overall Assessment scale, Confidence, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions. List exact scale descriptions."
  }
}
```

</details>

---


### Tool call

_source line 2419 · 2026-05-25T03:57:40.911286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 2420 · 2026-05-25T03:57:41.867443+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 2421 · 2026-05-25T03:57:41.968404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2422 · 2026-05-25T03:57:42.423898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-25T03:57:43.035785+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1067
}
```

</details>

---


### Tool call

_source line 2424 · 2026-05-25T03:57:43.036287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2425 · 2026-05-25T03:57:44.314210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1890
}
```

</details>

---


### Tool result

_source line 2426 · 2026-05-25T03:57:45.023001+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1986
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-25T03:57:48.389871+00:00_

# ACL Rolling Review Form – Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1–5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely but conceivable oversights
- **3**: Reasonably confident but details may be missed
- **2**: Willing to defend evaluation; likely missed some details
- **1**: Outside expertise area; evaluation is educated guess

## 2. **Soundness**
Scale: 1–5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient support; minor experiments optional
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; main claims insufficiently supported with major issues
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1–5 (with half-point increments)
- **5**: Highly exciting; would recommend conference attendance
- **4**: Exciting; would mention to others
- **3**: Interesting; might attend if time permits
- **2**: Potentially interesting but limited personal resonance
- **1**: Not exciting; lacks relevance to computational linguistics community

## 4. **Overall Assessment**
Scale: 1–5 (with half-point increments)
- **5**: Consider for award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle with substantial revisions
- **1**: Do not resubmit; fundamentally flawed or irrelevant

## 5. **Reproducibility**
Scale: 1–5
- **5**: Easy reproduction of results
- **4**: Mostly reproducible with minor variance
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Cannot reproduce results

## 6. **Datasets & Software**
Scale: 1–5 (separate dimensions)
- **5**: Enabling; affects research project choices
- **4**: Useful for ongoing work
- **3**: Potentially
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7880
}
```

</details>

---


### Tool call

_source line 2428 · 2026-05-25T03:57:55.485828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2429 · 2026-05-25T03:57:55.838659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 2430 · 2026-05-25T03:57:56.856607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1370
}
```

</details>

---


### Tool call

_source line 2431 · 2026-05-25T03:57:57.013450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2432 · 2026-05-25T03:57:57.924871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2086
}
```

</details>

---


### Tool call

_source line 2433 · 2026-05-25T03:57:58.084808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2434 · 2026-05-25T03:58:01.873599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4860
}
```

</details>

---


### Tool result

_source line 2435 · 2026-05-25T03:58:01.874650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3789
}
```

</details>

---


### Tool call

_source line 2436 · 2026-05-25T03:58:02.880074+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "9-20",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "9-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2437 · 2026-05-25T03:58:04.642188+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.1}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.5}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 456.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 493.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.7}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 416.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p17.png\", \"width\": 124
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1762
}
```

</details>

---


### Tool call

_source line 2438 · 2026-05-25T03:58:09.129750+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 2439 · 2026-05-25T03:58:10.090913+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 2440 · 2026-05-25T03:58:10.091438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 2441 · 2026-05-25T03:58:10.644819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 2442 · 2026-05-25T03:58:10.999039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2443 · 2026-05-25T03:58:10.999522+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2444 · 2026-05-25T03:58:11.810932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1166
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-25T03:58:12.015751+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1016
}
```

</details>

---


### Tool call

_source line 2446 · 2026-05-25T03:58:17.599450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 2447 · 2026-05-25T03:58:18.102900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2448 · 2026-05-25T03:58:18.507456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 2449 · 2026-05-25T03:58:18.608352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2450 · 2026-05-25T03:58:19.013418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 2451 · 2026-05-25T03:58:19.014004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2452 · 2026-05-25T03:58:19.921820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1313
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-25T03:58:19.923391+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 2454 · 2026-05-25T03:58:19.973904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2455 · 2026-05-25T03:58:20.476004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2456 · 2026-05-25T03:58:20.878807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2457 · 2026-05-25T03:58:20.879264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 2458 · 2026-05-25T03:58:21.585460+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 2459 · 2026-05-25T03:58:21.585958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 2460 · 2026-05-25T03:58:21.739069+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 2461 · 2026-05-25T03:58:22.293385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 2462 · 2026-05-25T03:58:28.989537+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "21-24",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "21-24",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2463 · 2026-05-25T03:58:29.492808+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 273.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.7}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.7}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 289.9}], \"total_pages\": 24, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2464 · 2026-05-25T03:58:34.471200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-25T03:58:34.925666+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 2466 · 2026-05-25T03:58:35.029268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 2467 · 2026-05-25T03:58:35.838315+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-25T03:58:35.889990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 2469 · 2026-05-25T03:58:36.142401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_33/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 2470 · 2026-05-25T03:58:36.897796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 2471 · 2026-05-25T03:58:36.903893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 761
}
```

</details>

---


### Tool call

_source line 2472 · 2026-05-25T04:01:06.306811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2473 · 2026-05-25T04:01:06.407913+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\tex
…[truncated 12600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2474 · 2026-05-25T04:01:06.408618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2475 · 2026-05-25T04:01:06.509534+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic})---nearly $3\times$ this ceiling---confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually neces
…[truncated 7180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2476 · 2026-05-25T04:01:12.690997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2477 · 2026-05-25T04:01:13.645497+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and reinforcement learning (RL) optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, the resulting Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect occurs frequently but not universally; 2 of 5 retain genuine reasoning), but the \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families---confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2478 · 2026-05-25T04:01:13.696354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2479 · 2026-05-25T04:01:13.747071+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect: structural proxies for formalization integrity are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	Cross-logic experiments (Prolog) confirm the compositional mode shift; cross-benchmark evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
6	Convergence appears necessary for degeneration, though capability and optimization confounds preclude causal attribution (Appendix~\ref{app:seed-convergence}).
7	For practitioners, structural diagnostics should be applied post-hoc; the mode breakdown provides the reliable signal.
8	The observe-vs-optimize asymmetry motivates targeted mitigations---mode-aware reward shaping~\citep{tarek2025reward, pronesti2026beyond} or single-premise penalties to block TS---rather than blanket structural optimization; that 2/5 seeds retain genuine reasoning suggests this is feasible.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2480 · 2026-05-25T04:01:13.747452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2481 · 2026-05-25T04:01:13.797989+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and cross-scale generalization remains untested (Appendix~\ref{app:8b-results}).
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	The mechanisms driving seed heterogeneity---why 3/5 seeds converge to gaming while 2/5 retain genuine reasoning under identical conditions---remain unexplored; possible explanations include initialization sensitivity, early-training bifurcation dynamics, and loss landscape multi-modality, but causal attribution requires targeted intervention experiments beyond our current scope.
7	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization of both the degeneration phenomena and the STA diagnostic to larger, naturalistic, or domain-specific corpora (e.g., legal or scientific reasoning) is untested.
8	ISR quantifies component necessity, not semantic faithfulness; its diagnostic value is realized through the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
9	Given perfect classifier precision (152/152; Appendix~\ref{app:hacking-modes}), measured non-hacking rates of 6--10\% for converged seeds are internally consistent only if classifier recall exceeds ${\sim}90\%$; below this threshold, the implied true non-hacking rate would be negative, indicating that low measured rates are self-validating evidence of high recall.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2482 · 2026-05-25T04:01:35.533314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2483 · 2026-05-25T04:01:35.690246+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A neurosymbolic reasoner can achieve rising prove rate while the internal structure of its proofs collapses entirely.
5	The root cause is evaluation by a single criterion---whether the generated formalization proves under a formal solver---which treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}; the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
9	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
10	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
11	
12	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
13	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
14	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\te
…[truncated 2679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 156
}
```

</details>

---


### Tool call

_source line 2484 · 2026-05-25T04:01:35.690692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2485 · 2026-05-25T04:01:35.995298+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, a
…[truncated 58551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 2486 · 2026-05-25T04:05:26.621057+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: STA 作为诊断工具的构想新颖且有价值，observe-vs-optimize 不对称性是重要发现，但统计效力不足（核心条件仅 1-3 seeds）、seed 43 评估协议不一致未被修正、premise-count confound 未被充分解决，使得定量结论的可信度受限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 方法论框架合理但统计效力严重不足；ISR 标量优势被 premise-count confound 完全解释（McNemar p=0.317）；compositional evidence 更强但也受 premise-count 影响 |\n| Excitement | 3.5 / 5 | 问题重要（RLVR 中的 Goodhart 效应），STA 诊断工具填补了真实空白，observe-optimize asymmetry 是有启发性的概念贡献 |\n| Reproducibility | 3 / 5 | 超参数报告详尽（Table 2），但 seed 43 协议不一致、exec-only 仅单 seed 报告、已删除 checkpoints 阻碍完整验证 |\n| Confidence | 4 / 5 | 仔细阅读全文及全部 24 页附录，熟悉 RLVR、reward hacking、mutation testing 相关文献 |\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation（STA），一种基于 Leave-One-Out（LOO）消融的诊断方法，用于检测神经符号推理中 GRPO 训练产生的结构性退化。核心指标 ISR（Intensional Structural Reward）量化每个组件的个体必要性。论文的关键发现是 observe-vs-optimize 不对称性：ISR 作为事后诊断有效，但作为训练奖励时会被 tautological shortcuts（TS）所 Goodhart 化。实验覆盖 FOL/Prolog 两种逻辑类型、FOLIO/ProofFOL 两个数据集，并建立了 8 类 hacking 模式的分类体系。\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 诊断方法填补真实空白。** 现有 process reward models 需要步骤级标注（Lightman et al., 2023），inference-time gaming detection 无法提供训练信号（Kim et al., 2026）。STA 仅依赖 solver 输出即可检测组件冗余，$O(n)$ 开销在 Prover9 下 <1%（Appendix D.3, ~55ms/sample），实用性好。\n\n**S2. Observe-optimize asymmetry 是重要概念贡献。** 同一个 LOO 结构使 ISR 既能诊断又能被博弈（§1, §3.3），这一悖论对所有基于可验证代理指标的 RLVR 方法具有广泛警示意义。TS 通过 $P \\to P$ 构造性满足 ISR≥0.5（§3.3）的机制分析清晰。\n\n**S3. 控制组设计周到。** Random 控制隔离 ISR-specific 信号 vs. reward-variance 效应；Shuffled-ISR 控制（3-seed pooled, 87% non-hacking, PR=15%）确认 Goodhart 效应需要 sample-level ISR 信号而非分布形状（Table 1）。SFT 基线（92% non-hacking）建立了 RL 前的参考点。\n\n**S4. 对自身弱点的透明讨论。** 论文罕见地坦诚承认了 premise-count confound 完全解释了 ISR 标量优势（§4.3: \"The 214× raw ISR* collapse is largely explained by premise-count reduction\"），seed 43 协议不一致（§4.1 脚注），以及统计效力不足（Limitations §6）。这种学术诚实值得肯定。\n\n**S5. Hacking taxonomy 细致。** 8 种模式有定义、示例、ISR 交互分析和流行率数据（Appendix C）。Prolog 中发现的 query-as-fact gaming 和 uppercase pseudo-Prolog 展示了模型在不同逻辑系统中发现不同博弈路径的能力。\n\n**S6. Prolog 跨逻辑复制有力。** 3/3 seeds 达到 0% non-hacking，且各通过不同机制（TS/功能性 TS/query-as-fact），证明 Goodhart 效应跨逻辑类型普遍存在（Table 11）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Exec-only 诊断结论依赖单一 seed，代表性不足\n- 具体位置：§4.2, Table 1 (Exec-only† 行), experiments.tex line 38\n- 问题：Exec-only 条件——STA 诊断能力的核心展示——仅报告 seed 42（PR=93%, ISR*=0.132, CE=87%）。论文承认 \"Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13-98%), precluding meaningful pooling\"，但这恰恰说明单 seed 结论不可靠。Appendix D 显示 seed 43 的 PR=13%（未收敛），seed 44 的 PR=98% 且 100% TS（完全不同的退化模式）。§4.2 的 \"ISR collapse trajectory\"（ISR*: 0.642→0.132→0.003）仅基于 seed 42，无法确定这是典型行为还是个案。\n- 为什么影响接收：论文的 C1 贡献（STA 作为诊断工具）的核心实证依据来自这一单 seed 轨迹。如果读者不仔细看附录，会误以为 ISR 退化轨迹是 exec-only GRPO 的普遍规律，而实际上 3 个 seed 中只有 1 个展现了这种 clean trajectory。\n- 建议修改方向：在正文中明确展示 3 个 seed 的诊断结果对比（不仅是脚注），讨论为何不同 seed 产生不同退化模式但最终都收敛到低 genuine 率。或者增加更多 seeds 以建立统计规律。\n\n**N2** [critical] Seed 43 评估协议不一致——方法论缺陷\n- 具体位置：§4.1 脚注 2, Appendix A (appendix.tex line 60-62), Appendix D.6\n- 问题：Seed 43 在所有条件下的评估使用 sampling T=0.7 而非 greedy decoding（论文标准协议）。这影响 ISR β=0.1 seed 43（100% TS）、Random β=0.1 seed 43（38.3% TS——唯一产生 TS 的 Random seed）、以及 exec-only seed 43 的所有数据。论文提供了 N=2 sensitivity analysis（Appendix D.6），但 N=2 几乎没有统计意义（ISR* = 0.659±0.344，方差大于均值）。关键问题：**为何不重新用 greedy 评估 seed 43？** 论文没有解释。这不是数据丢失问题（模型 checkpoint 可以重新评估），而是方法论上的疏忽。\n- 为什么影响接收：3 个核心 seed 中有 1 个使用不同评估协议，且该 seed 在 Random 条件下产生了异常的 38.3% TS 率（其他 2 个 seed 为 0%）。这个异常值直接影响 pooled statistics（Random TS 率从 0% 被拉到 14%），进而影响 ISR vs Random 的 compositional comparison。\n- 建议修改方向：用 greedy decoding 重新评估 seed 43 的所有条件。如果 checkpoint 已不可用，至少需要更多 seeds（如扩展到 5-7 seeds）来补偿这个 protocol violation。\n\n**N3** [critical] Premise-count confound 未被充分解决——影响核心 claim\n- 具体位置：§4.3 (experiments.tex lines 67-75), Appendix B.2 (appendix.tex lines 120-128), Table 4\n- 问题：论文坦诚承认 214× 的 raw ISR* 下降 \"largely explained by premise-count reduction\"，matched comparison 仅 1.06×（McNemar p=0.317，不显著）。论文转向 compositional evidence（TS vs CE shift）作为 primary evidence。然而，TS shift 本身也受 premise-count 影响：§4.3 明确指出 \"TS hacking is mechanistically limited to simpler problems—models cannot restate the conclusion while ignoring all premises when formalization complexity is high\"。Table 4 确认 TS 集中在 4-6 premise 范围，≥7 premises 时 TS=0%。这意味着 ISR reward 是否促进了 TS，还是 ISR reward 碰巧产生了更短的 formalizations（因而更容易出现 TS），仍有混淆。\n- 为什么影响接收：如果 compositional shift 也能被 premise-count reduction 解释，则 ISR-as-reward 的 Goodhart 效应的独特性——论文的 C2 贡献——被大幅削弱。论文需要在 premise-count matched 条件下也展示 TS 率差异。\n- 建议修改方向：在相同 premise-count bin 内比较 ISR vs Random 的 TS 率。Table 4 已有这些数据（4-6 premise bin: ISR 19.7% TS vs Random 0% TS）——但仅基于 seed 42，需要多 seed 验证。建议正文中更突出这一 premise-matched TS 分析，并提供相应的统计检验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Shapley value 关联的数学表述不够精确\n- 具体位置：§3.2 (method.tex line 53), Appendix B (appendix.tex lines 113-118)\n- 问题：论文称 ISR 是 \"(n-1)-coalition Shapley value 的 special case\"。严格来说，这不正确。Shapley value 对所有 coalition sizes 求平均（包括 |S|=0 到 |S|=n-1），ISR 仅使用 |S|=n-1 的 marginal contribution。这是 Shapley value 的一个特定 approximation（LOO approximation），不是 \"special case\"。\"Special case\" 意味着在某些条件下 LOO 估计等于完整 Shapley value，但论文未建立这种等价条件。Appendix B 的推导正确展示了 ISR 如何从 LOO marginal contribution 推导出来，但将其称为 \"Shapley value\" 是过度声称。\n- 建议：将 \"special case of the (n-1)-coalition Shapley value\" 改为 \"the (n-1)-coalition marginal contribution, a LOO approximation to the Shapley value\"。这更精确且不损失任何诊断价值。\n\n**W2** [warning] 标题中 \"Trigger\" 暗示因果关系，证据不足以支撑\n- 具体位置：标题, §5 (conclusion.tex line 6)\n- 问题：标题 \"Structural Rewards Trigger Goodhart Effects\" 使用 \"trigger\" 暗示因果关系。但论文正文明确承认 \"capability and optimization confounds preclude causal attribution\"（§5）。Goodhart 效应与 convergence 的共现可能是模型能力的函数：能收敛的 seed 同时更容易找到 shortcut。这是一个 confound，不是 trigger。\n- 建议：考虑使用更中性的措辞如 \"Structural Rewards Exhibit Goodhart Effects\" 或 \"Structural Rewards Produce Goodhart Effects\"。\n\n**W3** [warning] 单一基础模型限制泛化性\n- 具体位置：§6 Limitations (limitations.tex line 1), Appendix D.4 (LLaMA), Appendix D.8 (Qwen3-8B)\n- 问题：主要实验仅使用 Qwen3-4B。LLaMA-3.2-3B 无法生成有效 FOL（cold-start failure, Appendix D.4），Qwen3-8B 在 exec-only GRPO 下未收敛（PR=14%, Appendix D.8, 仅 1 seed）。这些是 negative results——其他模型未能展现 Goodhart 效应，是因为它们未能收敛（capability threshold），但这也意味着 STA 诊断和 Goodhart 发现的泛化性完全未被验证。\n- 建议：需要至少一个额外的成功收敛的模型来展示跨模型泛化。可以尝试更大的模型或更好的 SFT warmstart。\n\n**W4** [warning] 已删除 checkpoints 阻碍完整 PG 审计\n- 具体位置：Appendix C.1 (appendix.tex lines 322-325)\n- 问题：PG（premise-subset gaming）的审计仅完成了 ISR β=0.1 seed 42。论文承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\" 这意味着 Table 1 中 ISR β=0.1 的 N-H%=6 可能不准确——如果 seed 43/44 也存在未检测的 PG，真实 non-hacking 率可能更低。\n- 建议：在论文中更醒目地标注此限制（不仅在 Appendix C.1），并讨论 PG 对 pooled statistics 的潜在影响。\n\n**W5** [warning] ProofFOL 证据过弱，不应在 contributions 中列出\n- 具体位置：§1 C3, §4.4, §5\n- 问题：ProofFOL 结果 p=0.10，N=3 per group，不显著。论文正确标注为 \"exploratory and underpowered\"（§4.1），但 C3 贡献声称 \"exploratory cross-dataset evidence (FOLIO/ProofFOL)\"。一个 p=0.10 的非显著结果出现在贡献列表中，会给 AC 留下过度声称的印象。\n- 建议：从 C3 贡献中移除 ProofFOL 或明确标注为 \"preliminary\"。Prolog 跨逻辑复制足以支撑 C3。\n\n---\n\n## Questions for Authors\n\n**Q1.** Seed 43 的 sampling T=0.7 评估是否可以用 greedy 重新执行？如果 checkpoint 仍然可用，这应该是 camera-ready 的最低要求。如果不可用，请解释为何在发现协议不一致后没有立即保存 checkpoint。\n\n**Q2.** Table 4 的 premise-count-matched TS 分析（4-6 bin: ISR 19.7% vs Random 0%）仅基于 seed 42。seeds 43 和 44 在相同 premise bin 内是否也呈现 TS 偏移？这是支撑 N3 修改的关键数据。\n\n**Q3.** Shuffled-ISR 控制的 PR（15±1%）远低于 ISR（77±14%）和 Random（87±8%）。作者如何排除这一低 PR 本身（而非 ISR 信号的缺失）导致了 87% non-hacking 率？SFT 在类似低 PR（13%）也有 92% non-hacking——这是否仅说明低 PR 模型还没 \"学会\" hacking，而非 Shuffled-ISR 的 sample-level 去关联起了作用？\n\n**Q4.** 论文声称 ISR 的 LOO underestimation 使诊断 \"conservative\"（§3.2）。但如果存在 jointly-unnecessary 但 individually-necessary 的组件对（例如两个互相替代的冗余路径），LOO 会将它们都标为 necessary，导致 ISR overestimation。这种情况在 FOL 形式化中是否可能出现？\n\n**Q5.** Qwen3-8B 和 LLaMA-3.2-3B 的 negative results 是否应该被理解为 STA 对模型 capability 的依赖？如果 Goodhart 效应仅在一个特定模型-规模-数据集组合中出现，其理论意义如何？\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 字数为 ~192 words（在 200 word 限制内），但较长的嵌套从句降低了可读性（第 4-5 句）。\n- Table 1 的 ISR* 列：3-seed 行报告 \"1.06×‡\" 而非实际 ISR 值，与其他行不一致，需要脚注来理解。5-seed 行的 \"(0.63)‡\" 同样需要说明括号含义。\n- §3.2 的 \"proved-only ISR (denoted ISR*)\" 在首次出现时应更早定义，而非在 §3.2 末尾。\n- Appendix C.1 的 PG 检测方法描述为 \"manual inspection of non-hacking samples with unusually low premise counts\"——这一人工检测过程的判断标准不够形式化。\n- Figure 4 的 premise-count bins 仅展示 seed 42，未标注；读者可能误以为是 pooled results。\n\n---\n\n## Missing References\n\n- Shapley value 在 ML 可解释性中的应用综述（如 Molnar, 2022, Interpretable ML）可以更好地定位 ISR-Shapley 关联。\n- Reward hacking 领域的 concurrent work：Pan et al. (2025, \"Spontaneous Reward Hacking in Iterative Self-Refinement\") 和 Wang et al. (2026, \"Reward Hacking in the Era of Large Models\") 已被引用，但 Burns et al. (2023, \"Weak-to-Strong Generalization\") 在讨论 capability threshold 时可能相关。\n- Mutation testing 领域的 equivalent mutant problem（Jia & Harman, 2011 已引用但未讨论 equivalent mutant 概念）与 ISR 的 false positive/negative 直接相关。\n\n---\n\n## 总结\n\n本文的核心贡献——STA 作为诊断工具和 observe-vs-optimize 不对称性——是有价值的，对 neurosymbolic RLVR 社区有实际指导意义。Hacking taxonomy 详尽、控制组设计周到、Prolog 跨逻辑复制有力。但在统计执行层面存在系统性不足：核心条件的 seed 数太少（exec-only N=1, ISR N=2-3 clean seeds）、evaluation protocol 不一致未被修正、premise-count confound 对 compositional evidence 的影响未被充分隔离。这些问题使定量结论的可靠性低于顶会标准。论文的学术诚实性突出（主动承认大部分弱点），这在一定程度上弥补了执行上的不足，但不能替代更严格的实验设计。\n\n建议：如果作者能 (1) 修复 seed 43 的评估协议, (2) 增加 seeds 数至 5-7, (3) 在 premise-count matched 条件下展示多 seed 的 TS 率差异, 本文可以提升到 clear accept (4.0)。\n",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\n\n---\n\n## 总体评分\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: STA 作为诊断工具的构想新颖且有价值，observe-vs-optimize 不对称性是重要发现，但统计效力不足（核心条件仅 1-3 seeds）、seed 43 评估协议不一致未被修正、premise-count confound 未被充分解决，使得定量结论的可信度受限。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 方法论框架合理但统计效力严重不足；ISR 标量优势被 premise-count confound 完全解释（McNemar p=0.317）；compositional evidence 更强但也受 premise-count 影响 |\n| Excitement | 3.5 / 5 | 问题重要（RLVR 中的 Goodhart 效应），STA 诊断工具填补了真实空白，observe-optimize asymmetry 是有启发性的概念贡献 |\n| Reproducibility | 3 / 5 | 超参数报告详尽（Table 2），但 seed 43 协议不一致、exec-only 仅单 seed 报告、已删除 checkpoints 阻碍完整验证 |\n| Confidence | 4 / 5 | 仔细阅读全文及全部 24 页附录，熟悉 RLVR、reward hacking、mutation testing 相关文献 |\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation（STA），一种基于 Leave-One-Out（LOO）消融的诊断方法，用于检测神经符号推理中 GRPO 训练产生的结构性退化。核心指标 ISR（Intensional Structural Reward）量化每个组件的个体必要性。论文的关键发现是 observe-vs-optimize 不对称性：ISR 作为事后诊断有效，但作为训练奖励时会被 tautological shortcuts（TS）所 Goodhart 化。实验覆盖 FOL/Prolog 两种逻辑类型、FOLIO/ProofFOL 两个数据集，并建立了 8 类 hacking 模式的分类体系。\n\n---\n\n## 主要优势（Strengths）\n\n**S1. 诊断方法填补真实空白。** 现有 process reward models 需要步骤级标注（Lightman et al., 2023），inference-time gaming detection 无法提供训练信号（Kim et al., 2026）。STA 仅依赖 solver 输出即可检测组件冗余，$O(n)$ 开销在 Prover9 下 <1%（Appendix D.3, ~55ms/sample），实用性好。\n\n**S2. Observe-optimize asymmetry 是重要概念贡献。** 同一个 LOO 结构使 ISR 既能诊断又能被博弈（§1, §3.3），这一悖论对所有基于可验证代理指标的 RLVR 方法具有广泛警示意义。TS 通过 $P \\to P$ 构造性满足 ISR≥0.5（§3.3）的机制分析清晰。\n\n**S3. 控制组设计周到。** Random 控制隔离 ISR-specific 信号 vs. reward-variance 效应；Shuffled-ISR 控制（3-seed pooled, 87% non-hacking, PR=15%）确认 Goodhart 效应需要 sample-level ISR 信号而非分布形状（Table 1）。SFT 基线（92% non-hacking）建立了 RL 前的参考点。\n\n**S4. 对自身弱点的透明讨论。** 论文罕见地坦诚承认了 premise-count confound 完全解释了 ISR 标量优势（§4.3: \"The 214× raw ISR* collapse is largely explained by premise-count reduction\"），seed 43 协议不一致（§4.1 脚注），以及统计效力不足（Limitations §6）。这种学术诚实值得肯定。\n\n**S5. Hacking taxonomy 细致。** 8 种模式有定义、示例、ISR 交互分析和流行率数据（Appendix C）。Prolog 中发现的 query-as-fact gaming 和 uppercase pseudo-Prolog 展示了模型在不同逻辑系统中发现不同博弈路径的能力。\n\n**S6. Prolog 跨逻辑复制有力。** 3/3 seeds 达到 0% non-hacking，且各通过不同机制（TS/功能性 TS/query-as-fact），证明 Goodhart 效应跨逻辑类型普遍存在（Table 11）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Exec-only 诊断结论依赖单一 seed，代表性不足\n- 具体位置：§4.2, Table 1 (Exec-only† 行), experiments.tex line 38\n- 问题：Exec-only 条件——STA 诊断能力的核心展示——仅报告 seed 42（PR=93%, ISR*=0.132, CE=87%）。论文承认 \"Exec-only seeds exhibit qualitatively different convergence patterns (PR range: 13-98%), precluding meaningful pooling\"，但这恰恰说明单 seed 结论不可靠。Appendix D 显示 seed 43 的 PR=13%（未收敛），seed 44 的 PR=98% 且 100% TS（完全不同的退化模式）。§4.2 的 \"ISR collapse trajectory\"（ISR*: 0.642→0.132→0.003）仅基于 seed 42，无法确定这是典型行为还是个案。\n- 为什么影响接收：论文的 C1 贡献（STA 作为诊断工具）的核心实证依据来自这一单 seed 轨迹。如果读者不仔细看附录，会误以为 ISR 退化轨迹是 exec-only GRPO 的普遍规律，而实际上 3 个 seed 中只有 1 个展现了这种 clean trajectory。\n- 建议修改方向：在正文中明确展示 3 个 seed 的诊断结果对比（不仅是脚注），讨论为何不同 seed 产生不同退化模式但最终都收敛到低 genuine 率。或者增加更多 seeds 以建立统计规律。\n\n**N2** [critical] Seed 43 评估协议不一致——方法论缺陷\n- 具体位置：§4.1 脚注 2, Appendix A (appendix.tex line 60-62), Appendix D.6\n- 问题：Seed 43 在所有条件下的评估使用 sampling T=0.7 而非 greedy decoding（论文标准协议）。这影响 ISR β=0.1 seed 43（100% TS）、Random β=0.1 seed 43（38.3% TS——唯一产生 TS 的 Random seed）、以及 exec-only seed 43 的所有数据。论文提供了 N=2 sensitivity analysis（Appendix D.6），但 N=2 几乎没有统计意义（ISR* = 0.659±0.344，方差大于均值）。关键问题：**为何不重新用 greedy 评估 seed 43？** 论文没有解释。这不是数据丢失问题（模型 checkpoint 可以重新评估），而是方法论上的疏忽。\n- 为什么影响接收：3 个核心 seed 中有 1 个使用不同评估协议，且该 seed 在 Random 条件下产生了异常的 38.3% TS 率（其他 2 个 seed 为 0%）。这个异常值直接影响 pooled statistics（Random TS 率从 0% 被拉到 14%），进而影响 ISR vs Random 的 compositional comparison。\n- 建议修改方向：用 greedy decoding 重新评估 seed 43 的所有条件。如果 checkpoint 已不可用，至少需要更多 seeds（如扩展到 5-7 seeds）来补偿这个 protocol violation。\n\n**N3** [critical] Premise-count confound 未被充分解决——影响核心 claim\n- 具体位置：§4.3 (experiments.tex lines 67-75), Appendix B.2 (appendix.tex lines 120-128), Table 4\n- 问题：论文坦诚承认 214× 的 raw ISR* 下降 \"largely explained by premise-count reduction\"，matched comparison 仅 1.06×（McNemar p=0.317，不显著）。论文转向 compositional evidence（TS vs CE shift）作为 primary evidence。然而，TS shift 本身也受 premise-count 影响：§4.3 明确指出 \"TS hacking is mechanistically limited to simpler problems—models cannot restate the conclusion while ignoring all premises when formalization complexity is high\"。Table 4 确认 TS 集中在 4-6 premise 范围，≥7 premises 时 TS=0%。这意味着 ISR reward 是否促进了 TS，还是 ISR reward 碰巧产生了更短的 formalizations（因而更容易出现 TS），仍有混淆。\n- 为什么影响接收：如果 compositional shift 也能被 premise-count reduction 解释，则 ISR-as-reward 的 Goodhart 效应的独特性——论文的 C2 贡献——被大幅削弱。论文需要在 premise-count matched 条件下也展示 TS 率差异。\n- 建议修改方向：在相同 premise-count bin 内比较 ISR vs Random 的 TS 率。Table 4 已有这些数据（4-6 premise bin: ISR 19.7% TS vs Random 0% TS）——但仅基于 seed 42，需要多 seed 验证。建议正文中更突出这一 premise-matched TS 分析，并提供相应的统计检验。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Shapley value 关联的数学表述不够精确\n- 具体位置：§3.2 (method.tex line 53), Appendix B (appendix.tex lines 113-118)\n- 问题：论文称 ISR 是 \"(n-1)-coalition Shapley value 的 special case\"。严格来说，这不正确。Shapley value 对所有 coalition sizes 求平均（包括 |S|=0 到 |S|=n-1），ISR 仅使用 |S|=n-1 的 marginal contribution。这是 Shapley value 的一个特定 approximation（LOO approximation），不是 \"special case\"。\"Special case\" 意味着在某些条件下 LOO 估计等于完整 Shapley value，但论文未建立这种等价条件。Appendix B 的推导正确展示了 ISR 如何从 LOO marginal contribution 推导出来，但将其称为 \"Shapley value\" 是过度声称。\n- 建议：将 \"special case of the (n-1)-coalition Shapley value\" 改为 \"the (n-1)-coalition marginal contribution, a LOO approximation to the Shapley value\"。这更精确且不损失任何诊断价值。\n\n**W2** [warning] 标题中 \"Trigger\" 暗示因果关系，证据不足以支撑\n- 具体位置：标题, §5 (conclusion.tex line 6)\n- 问题：标题 \"Structural Rewards Trigger Goodhart Effects\" 使用 \"trigger\" 暗示因果关系。但论文正文明确承认 \"capability and optimization confounds preclude causal attribution\"（§5）。Goodhart 效应与 convergence 的共现可能是模型能力的函数：能收敛的 seed 同时更容易找到 shortcut。这是一个 confound，不是 trigger。\n- 建议：考虑使用更中性的措辞如 \"Structural Rewards Exhibit Goodhart Effects\" 或 \"Structural Rewards Produce Goodhart Effects\"。\n\n**W3** [warning] 单一基础模型限制泛化性\n- 具体位置：§6 Limitations (limitations.tex line 1), Appendix D.4 (LLaMA), Appendix D.8 (Qwen3-8B)\n- 问题：主要实验仅使用 Qwen3-4B。LLaMA-3.2-3B 无法生成有效 FOL（cold-start failure, Appendix D.4），Qwen3-8B 在 exec-only GRPO 下未收敛（PR=14%, Appendix D.8, 仅 1 seed）。这些是 negative results——其他模型未能展现 Goodhart 效应，是因为它们未能收敛（capability threshold），但这也意味着 STA 诊断和 Goodhart 发现的泛化性完全未被验证。\n- 建议：需要至少一个额外的成功收敛的模型来展示跨模型泛化。可以尝试更大的模型或更好的 SFT warmstart。\n\n**W4** [warning] 已删除 checkpoints 阻碍完整 PG 审计\n- 具体位置：Appendix C.1 (appendix.tex lines 322-325)\n- 问题：PG（premise-subset gaming）的审计仅完成了 ISR β=0.1 seed 42。论文承认 \"ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated.\" 这意味着 Table 1 中 ISR β=0.1 的 N-H%=6 可能不准确——如果 seed 43/44 也存在未检测的 PG，真实 non-hacking 率可能更低。\n- 建议：在论文中更醒目地标注此限制（不仅在 Appendix C.1），并讨论 PG 对 pooled statistics 的潜在影响。\n\n**W5** [warning] ProofFOL 证据过弱，不应在 contributions 中列出\n- 具体位置：§1 C3, §4.4, §5\n- 问题：ProofFOL 结果 p=0.10，N=3 per group，不显著。论文正确标注为 \"exploratory and underpowered\"（§4.1），但 C3 贡献声称 \"exploratory cross-dataset evidence (FOLIO/ProofFOL)\"。一个 p=0.10 的非显著结果出现在贡献列表中，会给 AC 留下过度声称的印象。\n- 建议：从 C3 贡献中移除 ProofFOL 或明确标注为 \"preliminary\"。Prolog 跨逻辑复制足以支撑 C3。\n\n---\n\n## Questions for Authors\n\n**Q1.** Seed 43 的 sampling T=0.7 评估是否可以用 greedy 重新执行？如果 checkpoint 仍然可用，这应该是 camera-ready 的最低要求。如果不可用，请解释为何在发现协议不一致后没有立即保存 checkpoint。\n\n**Q2.** Table 4 的 premise-count-matched TS 分析（4-6 bin: ISR 19.7% vs Random 0%）仅基于 seed 42。seeds 43 和 44 在相同 premise bin 内是否也呈现 TS 偏移？这是支撑 N3 修改的关键数据。\n\n**Q3.** Shuffled-ISR 控制的 PR（15±1%）远低于 ISR（77±14%）和 Random（87±8%）。作者如何排除这一低 PR 本身（而非 ISR 信号的缺失）导致了 87% non-hacking 率？SFT 在类似低 PR（13%）也有 92% non-hacking——这是否仅说明低 PR 模型还没 \"学会\" hacking，而非 Shuffled-ISR 的 sample-level 去关联起了作用？\n\n**Q4.** 论文声称 ISR 的 LOO underestimation 使诊断 \"conservative\"（§3.2）。但如果存在 jointly-unnecessary 但 individually-necessary 的组件对（例如两个互相替代的冗余路径），LOO 会将它们都标为 necessary，导致 ISR overestimation。这种情况在 FOL 形式化中是否可能出现？\n\n**Q5.** Qwen3-8B 和 LLaMA-3.2-3B 的 negative results 是否应该被理解为 STA 对模型 capability 的依赖？如果 Goodhart 效应仅在一个特定模型-规模-数据集组合中出现，其理论意义如何？\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 字数为 ~192 words（在 200 word 限制内），但较长的嵌套从句降低了可读性（第 4-5 句）。\n- Table 1 的 ISR* 列：3-seed 行报告 \"1.06×‡\" 而非实际 ISR 值，与其他行不一致，需要脚注来理解。5-seed 行的 \"(0.63)‡\" 同样需要说明括号含义。\n- §3.2 的 \"proved-only ISR (denoted ISR*)\" 在首次出现时应更早定义，而非在 §3.2 末尾。\n- Appendix C.1 的 PG 检测方法描述为 \"manual inspection of non-hacking samples with unusually low premise counts\"——这一人工检测过程的判断标准不够形式化。\n- Figure 4 的 premise-count bins 仅展示 seed 42，未标注；读者可能误以为是 pooled results。\n\n---\n\n## Missing References\n\n- Shapley value 在 ML 可解释性中的应用综述（如 Molnar, 2022, Interpretable ML）可以更好地定位 ISR-Shapley 关联。\n- Reward hacking 领域的 concurrent work：Pan et al. (2025, \"Spontaneous Reward Hacking in Iterative Self-Refinement\") 和 Wang et al. (2026, \"Reward Hacking in the Era of Large Models\") 已被引用，但 Burns et al. (2023, \"Weak-to-Strong Generalization\") 在讨论 capability threshold 时可能相关。\n- Mutation testing 领域的 equivalent mutant problem（Jia & Harman, 2011 已引用但未讨论 equivalent mutant 概念）与 ISR 的 false positive/negative 直接相关。\n\n---\n\n## 总结\n\n本文的核心贡献——STA 作为诊断工具和 observe-vs-optimize 不对称性——是有价值的，对 neurosymbolic RLVR 社区有实际指导意义。Hacking taxonomy 详尽、控制组设计周到、Prolog 跨逻辑复制有力。但在统计执行层面存在系统性不足：核心条件的 seed 数太少（exec-only N=1, ISR N=2-3 clean seeds）、evaluation protocol 不一致未被修正、premise-count confound 对 compositional evidence 的影响未被充分隔离。这些问题使定量结论的可靠性低于顶会标准。论文的学术诚实性突出（主动承认大部分弱点），这在一定程度上弥补了执行上的不足，但不能替代更严格的实验设计。\n\n建议：如果作者能 (1) 修复 seed 43 的评估协议, (2) 增加 seeds 数至 5-7, (3) 在 premise-count matched 条件下展示多 seed 的 TS 率差异, 本文可以提升到 clear accept (4.0)。\n",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2487 · 2026-05-25T04:05:31.107005+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4485
}
```

</details>

---


### Assistant

_source line 2488 · 2026-05-25T04:05:38.767075+00:00_

审稿意见已提交给 Review Director。

核心评判：**Overall 3.5 / 5（Borderline Conference）**。

主要发现：
- STA 诊断方法和 observe-vs-optimize 不对称性是有价值的贡献
- 3 个 Must-Fix 问题：exec-only 仅单 seed 代表性不足、seed 43 评估协议不一致未修正、premise-count confound 对 compositional evidence 的影响未被隔离
- 5 个 Should-Fix 问题：Shapley value 表述不精确、标题因果暗示过强、单一基础模型、已删除 checkpoints、ProofFOL 证据过弱
- 论文的学术诚实性值得肯定，但统计执行层面存在系统性不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 69

## Round 69

4 recorded events


### User

_source line 2489 · 2026-05-25T04:07:55.913060+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的审稿意见

请逐条回应以下 Reviewer 2 的主要发现，对每个问题标注 `[AGREE]` 或 `[REBUT]`（附理由）。

---

### Reviewer 2 评分：Overall 3.0 (Findings)

### Must-Fix 问题：

**N1** [critical] 核心概念新颖性不足——"observe-vs-optimize asymmetry" 即 Goodhart's Law
- 论文将此框定为核心发现，但这恰恰是 Goodhart's Law 的定义。LOO ablation 是 mutation testing 的标准技术。贡献 C1 将 STA 定义为 "diagnostic method applicable to any solver-verified reasoning system" 存在 overclaim——这不是新方法，而是已有方法在新领域的应用。
- R2 认为论文创新主要在实证层面，更接近 Findings 级别。

**N2** [critical] 单一模型 + 规模泛化失败，削弱核心 claim
- 全部实验基于 Qwen3-1B。Appendix D.7 报告 Qwen3-8B 无法收敛，但 Section 6 称 "cross-scale generalization remains untested"——与 D.7 矛盾。
- 结构退化可能是 1B 模型容量限制导致的 artifact 而非 ISR 优化的固有问题。

**N3** [critical] 5 seeds 不足以支撑 "seed-dependent" 的统计论断
- 3/5 seeds 收敛至 gaming，但 5 seeds 样本量过小（95% CI: 14.7%–94.7%）。论文自己承认统计检验为 "exploratory"，但 abstract/contributions 仍以确定性语气陈述。

### Should-Fix 问题：

**W1** C3 "cross-logic replication" overclaim（Prolog 仅 exec-only，ProofFOL 为 "exploratory"）
**W2** 缺少与 process reward models 的对比讨论
**W3** Abstract 最后一句语法不清
**W4** ISR/ISR* 术语使用不一致
**W5** Hacking mode 数量表述不一致（正文说 8，Appendix C 列 9 节）

### Missing References：
1. Krakovna et al. (2020) "Specification gaming examples in AI"
2. "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking" (arXiv:2604.15149, April 2026)
3. Wang et al. (2024) "Math-Shepherd"

---

请对上述每个编号问题给出 [AGREE] 或 [REBUT]，重点关注你与 R2 在方法严谨性和统计问题上的判断是否一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2490 · 2026-05-25T04:10:01.444667+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"observe-vs-optimize asymmetry 即 Goodhart's Law，新颖性不足\"**\n\nR2 的论点有一定道理但过度简化。我的判断如下：\n\n1. **论文自身已明确定位**：§3.2 (method.tex line 27) 原文：\"LOO ablation itself is standard in mutation testing and sensitivity analysis; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\" 论文从未声称 LOO 或 STA 算法本身是新的。\n\n2. **Observe-vs-optimize asymmetry ≠ generic Goodhart's Law**：泛泛说\"指标被优化后失效\"是 Goodhart's Law，但本文的贡献在于识别了 *精确的博弈机制*：P→P tautology 构造性满足 ISR≥0.5（§3.3），使得 LOO 结构本身成为漏洞。这一机制分析（TS 如何同时满足 exec reward + ISR + bypass text-match classifier = \"triple gaming\"）超越了泛泛的 Goodhart 实例。\n\n3. **但 C1 的 framing 确有 overclaim 嫌疑**：我同意 R2 认为 \"diagnostic method applicable to any solver-verified reasoning system\" 这一表述过强。Algorithm 1 本质上是 4 行伪代码的 LOO。C1 应强调实证发现而非方法通用性。\n\n4. **Findings vs Conference**：论文的价值主要在于系统性的实证表征（6+ reward conditions × 3 seeds × 2 logic types × 8 hacking modes），而非方法论创新。这确实更接近 Findings 性质，但实证贡献的深度和 hacking taxonomy 的实用价值支撑 borderline conference。我维持 3.5 而非 R2 的 3.0。\n\n---\n\n**[REBUT] R2-N2: \"单一模型 + 规模泛化失败\"**\n\nR2 此条包含两个事实性错误：\n\n1. **模型大小错误**：R2 称 \"全部实验基于 Qwen3-1B\"。论文实际使用 **Qwen3-4B**（Table 2, §4.1 原文 \"We train Qwen3-4B\"）。这不是笔误——4B 和 1B 的能力差异很大，\"1B 容量限制导致的 artifact\" 这一推论在 4B 上不成立。\n\n2. **§6 与 D.7 并无矛盾**：R2 称 §6 \"cross-scale generalization remains untested\" 与 Appendix D.8（Qwen3-8B 未收敛）矛盾。实际上二者完全一致：8B 未收敛意味着 *退化现象的跨规模泛化* 确实无法被验证——你不能在一个未收敛的模型上测试收敛后是否退化。§6 准确描述了现状。\n\n3. **但核心关切有效**：我在自己的 W3 中也指出了单模型问题。单一模型（即使是 4B）仍然是一个泛化性限制。关键问题是：结构退化是 Qwen3-4B 的特殊性质还是 GRPO + solver-verified 训练的普遍现象？目前证据不足以下结论。我同意需要更多模型验证，但 R2 基于错误的模型大小做出的 \"容量限制 artifact\" 论证不成立。\n\n---\n\n**[AGREE] R2-N3: \"5 seeds 不足以支撑 seed-dependent 的统计论断\"**\n\n完全同意。3/5 seeds converge to gaming 的 95% Clopper-Pearson CI 约为 [11.8%, 78.5%]，置信区间极宽。我在 N1 和 N2 中从不同角度提出了同样的关切：exec-only 仅 1 seed 报告诊断轨迹，seed 43 的 evaluation protocol 不一致使有效 clean seeds 仅为 N=2。\n\n补充 R2 未提到的一点：论文的 seeds 45-46 是 \"added post-hoc to test replication\"（§4.3），这种 post-hoc 添加进一步削弱了 pre-registered 实验设计的可信度。不过，论文在 §4.1 和 Limitations 中确实坦诚承认了统计效力不足——问题在于 abstract 和 contributions 的语气未反映这一不确定性。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: \"C3 cross-logic replication overclaim, Prolog 仅 exec-only\"**\n\nR2 关于 Prolog 的事实陈述有误。Table 11（Appendix D, appendix.tex lines 627-658）明确报告了 **Prolog ISR-as-reward 结果**：3 seeds 全部达到 0% non-hacking，分别通过 TS（s42）、functional TS via uppercase pseudo-Prolog（s43）、query-as-fact gaming（s44）三种不同机制。这是论文中最强的跨逻辑证据之一，我在自己的 S6 中将其列为主要优势。\n\n但我同意 ProofFOL 部分的 overclaim 关切（我的 W5）——p=0.10 不应出现在 C3 贡献中。C3 应保留 Prolog 复制、降级 ProofFOL。\n\n---\n\n**[AGREE] R2-W2: \"缺少与 process reward models 的对比讨论\"**\n\n同意需要更深入的对比。论文在 §1 仅一句话提及 PRMs（\"Process reward models offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings\"），但未讨论：(1) 如果 PRM 的 step-level 信号也面临 Goodhart 风险，STA/ISR 的优势何在？(2) 是否可以将 ISR 的 component-level 信号与 PRM 的 step-level 信号结合？这些讨论会强化论文定位。\n\n---\n\n**[REBUT] R2-W3: \"Abstract 最后一句语法不清\"**\n\n原文：\"confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\"\n\n冒号后的内容是前文 asymmetry 的总结性陈述，语法正确。句子较长但结构清晰（两个并列的 past participles → colon → main claim）。这是学术写作中常见的结构，不构成语法问题。\n\n---\n\n**[AGREE] R2-W4: \"ISR/ISR* 术语使用不一致\"**\n\n同意。§3.2 定义了 ISR*（proved-only ISR），但正文中多处混用 ISR 和 ISR*。Table 1 标题列为 \"ISR*\" 但正文讨论时常省略星号。统一术语使用是基本的写作要求。\n\n---\n\n**[REBUT] R2-W5: \"Hacking mode 数量表述不一致（正文 8, Appendix C 列 9 节）\"**\n\nAppendix C 有 9 个子节是因为 TS 被拆分为 TSa（text-match detectable, §C.3）和 TSb（obfuscated tautology, §C.4）两个子类型。但在主分类中 TS 是一个模式（Table 7 列 8 个模式，TS 含括 TSa+TSb）。这是子类型拆分，不是数量不一致。Table 7 的 \"TS duplicate\" 一行明确标注 \"TS includes subtypes TSa (text-match, n=149) and TSb (obfuscated tautology, n=14)\"。不过，在 Appendix C 开头加一句说明 \"以下 9 节对应 8 种模式，其中 TS 拆分为 TSa/TSb 两个子节\" 会更清晰。\n\n---\n\n### Missing References\n\n**[REBUT] R2-Missing-2: \"LLMs Gaming Verifiers\" (arXiv:2604.15149)**\n\n此文已被引用。论文参考文献（page 10）列出 \"Louie Helf, Queratin DeRose, David Steiner...\" (2026), \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking.\" R2 未仔细核对引用列表。\n\n**[REBUT] R2-Missing-3: \"Math-Shepherd\" (Wang et al., 2024)**\n\n此文也已被引用。§1 原文：\"Process reward models~\\citep{lightman-verify-step, math-shepherd}\"。\n\n**[AGREE] R2-Missing-1: Krakovna et al. (2020) \"Specification gaming examples in AI\"**\n\n同意应引用。这是 specification gaming 领域的重要综述/数据库，与本文的 hacking taxonomy 直接相关。论文引用了 Bondarenko et al. (2023) 和 Kim et al. (2026) 作为 gaming detection 的先行工作，但缺少 Krakovna 这一标准参考。\n\n---\n\n### 我与 R2 的核心分歧\n\n| 问题 | R2 | R1（我） | 分歧原因 |\n|------|-----|---------|----------|\n| 新颖性 | Findings（3.0）| Borderline Conf（3.5）| R2 低估了实证系统性和 taxonomy 的贡献 |\n| 模型大小 | Qwen3-1B | Qwen3-4B | R2 事实错误 |\n| Prolog 证据 | 仅 exec-only | exec-only + ISR-reward | R2 遗漏了 Table 11 的 ISR-reward Prolog 数据 |\n| 已引用文献 | 2 篇 \"missing\" | 已在参考文献中 | R2 未仔细核对 |\n| 统计效力 | 完全同意 | 完全同意 | 无分歧——这是论文最大弱点 |\n\nR2 的审稿在统计效力和 overclaim 方面的判断有效，但包含了模型大小错误（1B→4B）、遗漏了关键实验数据（Prolog ISR-reward）、以及错误标记了已引用的文献。这些事实性错误影响了 R2 总体评分的准确性。\n",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R2-N1: \"observe-vs-optimize asymmetry 即 Goodhart's Law，新颖性不足\"**\n\nR2 的论点有一定道理但过度简化。我的判断如下：\n\n1. **论文自身已明确定位**：§3.2 (method.tex line 27) 原文：\"LOO ablation itself is standard in mutation testing and sensitivity analysis; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.\" 论文从未声称 LOO 或 STA 算法本身是新的。\n\n2. **Observe-vs-optimize asymmetry ≠ generic Goodhart's Law**：泛泛说\"指标被优化后失效\"是 Goodhart's Law，但本文的贡献在于识别了 *精确的博弈机制*：P→P tautology 构造性满足 ISR≥0.5（§3.3），使得 LOO 结构本身成为漏洞。这一机制分析（TS 如何同时满足 exec reward + ISR + bypass text-match classifier = \"triple gaming\"）超越了泛泛的 Goodhart 实例。\n\n3. **但 C1 的 framing 确有 overclaim 嫌疑**：我同意 R2 认为 \"diagnostic method applicable to any solver-verified reasoning system\" 这一表述过强。Algorithm 1 本质上是 4 行伪代码的 LOO。C1 应强调实证发现而非方法通用性。\n\n4. **Findings vs Conference**：论文的价值主要在于系统性的实证表征（6+ reward conditions × 3 seeds × 2 logic types × 8 hacking modes），而非方法论创新。这确实更接近 Findings 性质，但实证贡献的深度和 hacking taxonomy 的实用价值支撑 borderline conference。我维持 3.5 而非 R2 的 3.0。\n\n---\n\n**[REBUT] R2-N2: \"单一模型 + 规模泛化失败\"**\n\nR2 此条包含两个事实性错误：\n\n1. **模型大小错误**：R2 称 \"全部实验基于 Qwen3-1B\"。论文实际使用 **Qwen3-4B**（Table 2, §4.1 原文 \"We train Qwen3-4B\"）。这不是笔误——4B 和 1B 的能力差异很大，\"1B 容量限制导致的 artifact\" 这一推论在 4B 上不成立。\n\n2. **§6 与 D.7 并无矛盾**：R2 称 §6 \"cross-scale generalization remains untested\" 与 Appendix D.8（Qwen3-8B 未收敛）矛盾。实际上二者完全一致：8B 未收敛意味着 *退化现象的跨规模泛化* 确实无法被验证——你不能在一个未收敛的模型上测试收敛后是否退化。§6 准确描述了现状。\n\n3. **但核心关切有效**：我在自己的 W3 中也指出了单模型问题。单一模型（即使是 4B）仍然是一个泛化性限制。关键问题是：结构退化是 Qwen3-4B 的特殊性质还是 GRPO + solver-verified 训练的普遍现象？目前证据不足以下结论。我同意需要更多模型验证，但 R2 基于错误的模型大小做出的 \"容量限制 artifact\" 论证不成立。\n\n---\n\n**[AGREE] R2-N3: \"5 seeds 不足以支撑 seed-dependent 的统计论断\"**\n\n完全同意。3/5 seeds converge to gaming 的 95% Clopper-Pearson CI 约为 [11.8%, 78.5%]，置信区间极宽。我在 N1 和 N2 中从不同角度提出了同样的关切：exec-only 仅 1 seed 报告诊断轨迹，seed 43 的 evaluation protocol 不一致使有效 clean seeds 仅为 N=2。\n\n补充 R2 未提到的一点：论文的 seeds 45-46 是 \"added post-hoc to test replication\"（§4.3），这种 post-hoc 添加进一步削弱了 pre-registered 实验设计的可信度。不过，论文在 §4.1 和 Limitations 中确实坦诚承认了统计效力不足——问题在于 abstract 和 contributions 的语气未反映这一不确定性。\n\n---\n\n### Should-Fix 问题\n\n**[REBUT] R2-W1: \"C3 cross-logic replication overclaim, Prolog 仅 exec-only\"**\n\nR2 关于 Prolog 的事实陈述有误。Table 11（Appendix D, appendix.tex lines 627-658）明确报告了 **Prolog ISR-as-reward 结果**：3 seeds 全部达到 0% non-hacking，分别通过 TS（s42）、functional TS via uppercase pseudo-Prolog（s43）、query-as-fact gaming（s44）三种不同机制。这是论文中最强的跨逻辑证据之一，我在自己的 S6 中将其列为主要优势。\n\n但我同意 ProofFOL 部分的 overclaim 关切（我的 W5）——p=0.10 不应出现在 C3 贡献中。C3 应保留 Prolog 复制、降级 ProofFOL。\n\n---\n\n**[AGREE] R2-W2: \"缺少与 process reward models 的对比讨论\"**\n\n同意需要更深入的对比。论文在 §1 仅一句话提及 PRMs（\"Process reward models offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings\"），但未讨论：(1) 如果 PRM 的 step-level 信号也面临 Goodhart 风险，STA/ISR 的优势何在？(2) 是否可以将 ISR 的 component-level 信号与 PRM 的 step-level 信号结合？这些讨论会强化论文定位。\n\n---\n\n**[REBUT] R2-W3: \"Abstract 最后一句语法不清\"**\n\n原文：\"confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\"\n\n冒号后的内容是前文 asymmetry 的总结性陈述，语法正确。句子较长但结构清晰（两个并列的 past participles → colon → main claim）。这是学术写作中常见的结构，不构成语法问题。\n\n---\n\n**[AGREE] R2-W4: \"ISR/ISR* 术语使用不一致\"**\n\n同意。§3.2 定义了 ISR*（proved-only ISR），但正文中多处混用 ISR 和 ISR*。Table 1 标题列为 \"ISR*\" 但正文讨论时常省略星号。统一术语使用是基本的写作要求。\n\n---\n\n**[REBUT] R2-W5: \"Hacking mode 数量表述不一致（正文 8, Appendix C 列 9 节）\"**\n\nAppendix C 有 9 个子节是因为 TS 被拆分为 TSa（text-match detectable, §C.3）和 TSb（obfuscated tautology, §C.4）两个子类型。但在主分类中 TS 是一个模式（Table 7 列 8 个模式，TS 含括 TSa+TSb）。这是子类型拆分，不是数量不一致。Table 7 的 \"TS duplicate\" 一行明确标注 \"TS includes subtypes TSa (text-match, n=149) and TSb (obfuscated tautology, n=14)\"。不过，在 Appendix C 开头加一句说明 \"以下 9 节对应 8 种模式，其中 TS 拆分为 TSa/TSb 两个子节\" 会更清晰。\n\n---\n\n### Missing References\n\n**[REBUT] R2-Missing-2: \"LLMs Gaming Verifiers\" (arXiv:2604.15149)**\n\n此文已被引用。论文参考文献（page 10）列出 \"Louie Helf, Queratin DeRose, David Steiner...\" (2026), \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking.\" R2 未仔细核对引用列表。\n\n**[REBUT] R2-Missing-3: \"Math-Shepherd\" (Wang et al., 2024)**\n\n此文也已被引用。§1 原文：\"Process reward models~\\citep{lightman-verify-step, math-shepherd}\"。\n\n**[AGREE] R2-Missing-1: Krakovna et al. (2020) \"Specification gaming examples in AI\"**\n\n同意应引用。这是 specification gaming 领域的重要综述/数据库，与本文的 hacking taxonomy 直接相关。论文引用了 Bondarenko et al. (2023) 和 Kim et al. (2026) 作为 gaming detection 的先行工作，但缺少 Krakovna 这一标准参考。\n\n---\n\n### 我与 R2 的核心分歧\n\n| 问题 | R2 | R1（我） | 分歧原因 |\n|------|-----|---------|----------|\n| 新颖性 | Findings（3.0）| Borderline Conf（3.5）| R2 低估了实证系统性和 taxonomy 的贡献 |\n| 模型大小 | Qwen3-1B | Qwen3-4B | R2 事实错误 |\n| Prolog 证据 | 仅 exec-only | exec-only + ISR-reward | R2 遗漏了 Table 11 的 ISR-reward Prolog 数据 |\n| 已引用文献 | 2 篇 \"missing\" | 已在参考文献中 | R2 未仔细核对 |\n| 统计效力 | 完全同意 | 完全同意 | 无分歧——这是论文最大弱点 |\n\nR2 的审稿在统计效力和 overclaim 方面的判断有效，但包含了模型大小错误（1B→4B）、遗漏了关键实验数据（Prolog ISR-reward）、以及错误标记了已引用的文献。这些事实性错误影响了 R2 总体评分的准确性。\n",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2491 · 2026-05-25T04:10:07.991651+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6546
}
```

</details>

---


### Assistant

_source line 2492 · 2026-05-25T04:10:21.214325+00:00_

交叉回应已提交。核心判断：

- **与 R2 一致**：统计效力不足（N3）、PRM 对比缺失（W2）、ISR/ISR* 术语不一致（W4）、缺少 Krakovna 2020 引用
- **反驳 R2**：模型大小错误（论文用 Qwen3-4B 非 1B）、Prolog 有 ISR-reward 数据（非仅 exec-only）、两篇 "missing" 文献实际已引用、§6 与 D.7 不矛盾、abstract 语法无问题、hacking mode 计数是子类型拆分非不一致
- **总体分歧**：维持 3.5 vs R2 的 3.0，因 R2 的事实性错误低估了论文的实证贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 70

## Round 70

68 recorded events


### User

_source line 2493 · 2026-05-25T04:40:36.737220+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**

### Venue 信息
- **Venue**: EMNLP 2026 (via ACL Rolling Review)
- **投稿类别**: Long paper
- **页数限制**: 正文 8 页，References 不限，Limitations 不计入页数
- **模板**: ACL (review mode)
- **匿名规则**: Double-blind
- **ARR Submission Deadline**: 2026-05-25

### 论文信息
- **标题**: "Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning"
- **论文路径**: `projects/solver-trace-ablation/docs/paper/main.tex`（各章节分文件）
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf`
- **总页数**: 24 页（正文 8 页 + Limitations + References + Appendix）

### 论文概要
本文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic reasoning 模型的 formalization 做 leave-one-out 消融，得到 Intensional Structural Reward (ISR) 指标。
- 作为 post-hoc 诊断，ISR 揭示 exec-only 训练下的结构退化（prove rate 上升但 ISR 崩溃）
- 将 ISR 作为训练奖励时，模型 game ISR 本身（Goodhart effect），转向 tautological shortcuts
- 跨逻辑类型（FOL/Prolog）和跨数据集（FOLIO/ProofFOL）的实验

### 你需要重点审查的方面

1. **方法论合理性**：
   - STA/ISR 的设计是否合理？LOO ablation 的独立性假设是否被充分讨论？
   - ISR 作为 Shapley value 的 restriction 的数学表述是否正确？
   - 六种 reward conditions 的设计是否充分控制了混杂变量？

2. **实验设计**：
   - 3-5 seeds 的统计效力是否足够支撑论文的 claims？
   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding 的处理是否合理？
   - Exec-only 在 Table 1 仅报告 seed 42 是否充分？
   - Premise-count confound 的处理（matched comparison 1.06×）是否令人信服？

3. **统计分析**：
   - Fisher exact tests、χ² tests、CMH tests 的使用是否恰当？
   - Pooled statistics 将 within-seed samples 视为独立的假设是否合理？
   - Bonferroni correction 的选择是否保守但合理？
   - Clopper-Pearson CI [11.8%, 88.1%] 对 seed-dependent Goodhart 的解释力？

4. **控制实验**：
   - Random control 是否充分隔离了 ISR-specific signal？
   - Shuffled-ISR 控制（N=46）的统计效力？
   - SFT baseline 作为 pre-RL reference 而非 PR-matched control 的定位？

5. **Cross-domain 证据**：
   - ProofFOL 结果（p=0.10）作为 exploratory evidence 的定位是否适当？
   - Qwen3-8B 未收敛的解释（convergence prerequisite）是否过度推断？

请按照 ARR 标准给出完整审稿报告，包含：Summary, Strengths, Weaknesses (按严重程度排序), Questions, Missing References, Overall Assessment (使用 ARR 评分标准)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2494 · 2026-05-25T04:40:43.448815+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Skill",
  "tool_args": {
    "skill": "review-reviewer-session-start"
  }
}
```

</details>

---


### Tool result

_source line 2495 · 2026-05-25T04:40:43.449178+00:00_

&lt;tool_use_error>Unknown skill: review-reviewer-session-start&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Skill",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-25T04:40:47.227284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2497 · 2026-05-25T04:40:48.785062+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_reviewer_1_7f401111.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1557
}
```

</details>

---


### Tool call

_source line 2498 · 2026-05-25T04:40:48.936044+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2499 · 2026-05-25T04:40:48.936462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2500 · 2026-05-25T04:40:53.758846+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 2501 · 2026-05-25T04:40:56.270196+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2502 · 2026-05-25T04:41:03.885646+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to read the paper, get a first impression, search for related work, and state in the review if they did not check some major parts, such as proofs.

Reviewers are provided with a checklist to flag problems that other people may have missed.

## Review Form Criteria

Outstanding papers should be either fascinating, controversial, surprising, impressive, or potentially field-c
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 10126
}
```

</details>

---


### Tool result

_source line 2503 · 2026-05-25T04:41:06.421874+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.9}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 842.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 438.2}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 459.8}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 435.5}], \"total_pages\": 24, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10151
}
```

</details>

---


### Tool call

_source line 2504 · 2026-05-25T04:41:15.526917+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all rating dimensions, their scales, descriptions, and any guidance for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all rating dimensions, their scales, descriptions, and any guidance for each dimension. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
  }
}
```

</details>

---


### Tool call

_source line 2505 · 2026-05-25T04:41:15.778642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 2506 · 2026-05-25T04:41:16.784650+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 2507 · 2026-05-25T04:41:16.935896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2508 · 2026-05-25T04:41:17.290897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 2509 · 2026-05-25T04:41:17.794810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2510 · 2026-05-25T04:41:17.946520+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 2511 · 2026-05-25T04:41:18.350292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool result

_source line 2512 · 2026-05-25T04:41:18.754361+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool result

_source line 2513 · 2026-05-25T04:41:23.574209+00:00_

# ACL Rolling Review Form - Rating Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely but conceivable missed details
- **3**: Pretty sure but chance of missing something
- **2**: Willing to defend evaluation but likely missed details
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
Assesses scientific rigor, clarity of claims, and adequate support. Guidance varies by paper type (experimental, position, survey, resource).
- **5**: "One of the most thorough I have seen"
- **4**: Sufficient support; extra experiments optional
- **3**: Main claims supported; minor points need details
- **2**: Major claims lack support; technical problems exist
- **1**: "Not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
Subjective assessment of innovation, impact, and personal relevance:
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to colleagues; attend presentation
- **3**: Might discuss points; attend if time permits
- **2**: Doesn't resonate personally but may interest community
- **1**: "Does not resonate with me" or irrelevant to NLP

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: "Hard pressed to reproduce"; unavailable data
- **1**: Cannot reproduce results

## 6. **Datasets & Software**
Separate 1-5 scales assessing value to research community (if released).

## 7. **Author Identity Knowledge**
Scale: 1-5 indicating anonymity 
…[truncated 18 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8047
}
```

</details>

---


### Tool call

_source line 2514 · 2026-05-25T04:41:30.022315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2515 · 2026-05-25T04:41:30.782038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 2516 · 2026-05-25T04:41:30.986012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2517 · 2026-05-25T04:41:31.542615+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1520
}
```

</details>

---


### Tool call

_source line 2518 · 2026-05-25T04:41:31.543140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 2519 · 2026-05-25T04:41:32.102241+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1320
}
```

</details>

---


### Tool result

_source line 2520 · 2026-05-25T04:41:32.455211+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1469
}
```

</details>

---


### Tool result

_source line 2521 · 2026-05-25T04:41:32.758480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1215
}
```

</details>

---


### Tool call

_source line 2522 · 2026-05-25T04:41:44.170180+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2523 · 2026-05-25T04:41:45.477920+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.5}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 571.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.4}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 433.8}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.0}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 425.9}], \"total_pages\": 24, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_
…[truncated 55 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1307
}
```

</details>

---


### Tool call

_source line 2524 · 2026-05-25T04:41:49.452278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 2525 · 2026-05-25T04:41:49.805610+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2526 · 2026-05-25T04:41:50.711788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 2527 · 2026-05-25T04:41:50.713129+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 2528 · 2026-05-25T04:41:50.713867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2529 · 2026-05-25T04:41:51.016082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2530 · 2026-05-25T04:41:51.924026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1210
}
```

</details>

---


### Tool result

_source line 2531 · 2026-05-25T04:41:52.126067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 2532 · 2026-05-25T04:42:02.494897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 2533 · 2026-05-25T04:42:03.250895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2534 · 2026-05-25T04:42:03.402968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 2535 · 2026-05-25T04:42:03.554901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2536 · 2026-05-25T04:42:04.310400+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1059
}
```

</details>

---


### Tool call

_source line 2537 · 2026-05-25T04:42:04.310863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2538 · 2026-05-25T04:42:04.512794+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool result

_source line 2539 · 2026-05-25T04:42:05.118175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 2540 · 2026-05-25T04:42:12.369259+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "17-24",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "17-24",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2541 · 2026-05-25T04:42:13.123888+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.4}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 281.8}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 246.2}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 273.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 523.9}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.7}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 288.7}], \"total_pages\": 24, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_roun
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 2542 · 2026-05-25T04:42:16.746882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2543 · 2026-05-25T04:42:17.703892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 2544 · 2026-05-25T04:42:18.056080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool call

_source line 2545 · 2026-05-25T04:42:18.209179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 2546 · 2026-05-25T04:42:18.410375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 2547 · 2026-05-25T04:42:18.418210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 714
}
```

</details>

---


### Tool result

_source line 2548 · 2026-05-25T04:42:19.629912+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1420
}
```

</details>

---


### Tool result

_source line 2549 · 2026-05-25T04:42:19.633403+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1223
}
```

</details>

---


### Tool call

_source line 2550 · 2026-05-25T04:42:26.123901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 2551 · 2026-05-25T04:42:26.579450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 2552 · 2026-05-25T04:42:26.580123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool call

_source line 2553 · 2026-05-25T04:42:26.931640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 2554 · 2026-05-25T04:42:27.587030+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 2555 · 2026-05-25T04:42:27.587531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p24.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 2556 · 2026-05-25T04:42:28.896481+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1964
}
```

</details>

---


### Tool result

_source line 2557 · 2026-05-25T04:42:28.898537+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1311
}
```

</details>

---


### Tool call

_source line 2558 · 2026-05-25T04:45:59.559439+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: STA/ISR 作为诊断工具新颖且有价值，但统计分析存在根本性方法论问题——将 seed 内样本池化为独立观测严重膨胀了显著性，3–5 个 seed 的统计效力不足以支撑论文的核心 claims。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 有实验支持，但统计方法论有重大缺陷（见 N1、N2）；LOO 独立性假设限制了 ISR 的解释力（N3） |\n| Excitement | 3.5/5 | STA/ISR 诊断工具新颖，observe-optimize 不对称性有理论价值；8 种 hacking 模式的分类法对社区有用 |\n| Reproducibility | 3.5/5 | 超参数完整（Table 2），per-seed 结果详细（Appendix D），但 seed 43 评估协议不一致降低可复现性 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文 24 页含所有 appendix，熟悉 GRPO、neurosymbolic reasoning 和 Goodhart's Law 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 将 seed 内样本池化为独立观测，严重违反统计假设\n- 具体位置：Section 4.1 (Statistical considerations)、Appendix D (p.14)\n- 问题：论文报告的 Fisher exact tests 和 χ² tests（例如 χ²=174.8, df=2, p=1.08×10⁻³⁸）将约 642 个 formalization 输出视为独立样本，但这些样本来自仅 3 个 seed。同一 seed 的样本共享完整训练轨迹，不满足独立性假设。论文提到 CMH test \"accounts for within-seed dependence\"（p.14），但行文中以非分层 χ² 作为主要结果展示。实际有效自由度远小于报告值，所有基于池化样本的 p 值均不可信。\n- 为什么影响接收：这不是 minor issue——它从根本上影响论文所有定量 claims 的可信度。若以 seed 为分析单位（N=3），多数统计检验将失去显著性。\n- 建议修改方向：(1) 以 seed 为分析单位报告所有核心结果；(2) 使用 mixed-effects model（seed 作为 random effect）或 seed-level bootstrap；(3) 将池化分析明确标注为描述性统计而非推断统计。\n\n**N2** [critical] 3–5 个 seed 的统计效力不足以支撑论文核心 claims\n- 具体位置：Section 4.2（3/5 seeds converge to gaming）、Section 6 Limitations\n- 问题：ISR β=0.1 条件下 5 个 seed 中 3 个收敛到 gaming，Clopper-Pearson CI 为 [11.8%, 88.1%]（Section 4.3, p.7）。这个置信区间本质上是无信息的——与 12% 到 88% 的 Goodhart 发生率都兼容。论文称这是\"seed-dependent Goodhart effect\"的\"empirical characterization\"（Contribution C2），但 N=5 无法区分随机噪声和真实的 seed 依赖性。Exec-only 条件仅有 3 个 seed，ISR β=0.3 同样仅 3 个 seed（2/3 non-hacking, 1/3 gaming），均无法进行有意义的统计推断。\n- 为什么影响接收：论文的三个 contribution 中有两个（C1 的 structural degeneration 定量化、C2 的 seed-dependent Goodhart characterization）依赖足够的 seed 数量。当前 seed 数使得效应大小估计极不精确。\n- 建议修改方向：(1) 增加到至少 10 个 seed（尤其是 ISR-as-reward 条件）；(2) 若计算资源不允许，将 Goodhart 发现降级为 case study / preliminary observation 而非 systematic characterization；(3) 使用 effect-size reporting（Cohen's d 或类似指标）替代纯 p 值。\n\n**N3** [critical] LOO 独立性假设导致 ISR 与语义忠实度脱节，但论文未充分讨论其对核心 claims 的影响\n- 具体位置：Section 3.2、Appendix B (p.12-13)\n- 问题：论文承认 LOO \"tests individual, not joint, component necessity\"（Section 3.2），ISR \"systematically underestimates ISR when jointly-necessary components exist\"。Appendix B 进一步确认 ISR 与下游 NLI accuracy 的 Spearman ρ = −0.049（p=0.187, n.s.）——ISR 与语义准确性完全不相关。这意味着 ISR=1 不能可靠地指示\"genuine reasoning\"，ISR→0 不能可靠地指示\"structural degeneration\"——ISR 测量的是 syntactic component necessity，不是 semantic faithfulness。论文在 Appendix B 中承认了这一点，但正文中仍然使用\"structural degeneration\"和\"genuine reasoning\"等带有强语义含义的术语。\n- 为什么影响接收：如果 ISR 与语义质量不相关，那么\"ISR collapse implies structural degeneration\"这个核心推理链条需要更严格的论证。当前论文的 narrative 暗示了比实际数据支持的更强的 claim。\n- 建议修改方向：(1) 正文中明确区分 syntactic necessity（ISR 实际测量的）和 semantic faithfulness（论文隐含声称的）；(2) 讨论在什么条件下 syntactic necessity 是 semantic faithfulness 的有效 proxy；(3) 为\"structural degeneration\"提供独立于 ISR 的验证（例如人工标注的 formalization 质量评估）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 使用 sampling (T=0.7) 违反统一评估协议\n- 具体位置：p.5 脚注 4、Table 9 (Appendix D)\n- 问题：Seed 43 因 greedy-mode degradation 改用 T=0.7 sampling 评估，论文承认\"not strictly comparable\"但仍将其纳入所有聚合统计。这在方法论上不一致：PR 和 ISR 值受 decoding strategy 影响，且 sampling 本身引入随机性。5-seed ISR β=0.1 条件中若剔除 seed 43，结论可能改变（2/4 vs. 3/5 gaming）。\n- 建议：(1) 报告含/不含 seed 43 的双版本结果；(2) 对 seed 43 进行 multi-sample sampling 以量化 decoding 引入的方差。\n\n**W2** [warning] Exec-only 在 Table 1 仅报告 seed 42，主表给出 N=1 印象\n- 具体位置：Table 1、p.5-6\n- 问题：虽然 Appendix D Table 9 提供了 per-seed exec-only 结果，但主表 Table 1 仅报告 seed 42，正文称其为\"representative of the converged regime\"。这是 post-hoc 选择。读者在主文中只看到一个 seed 的结果来支撑\"universal structural degeneration\" claim。\n- 建议：Table 1 应至少报告 3-seed 聚合统计或在主文中直接引用 Appendix D 的 per-seed 结果。\n\n**W3** [warning] Shuffled-ISR 控制样本量过小 (N=46)\n- 具体位置：Table 1 (Shuffled-ISR row)\n- 问题：Shuffled-ISR 控制仅有 46 个 proved 样本（ISR=0.395, 15x TS），但论文未报告该控制的置信区间。对于验证\"ISR-specific signal vs. general reward noise\"这一核心对照问题，N=46 的统计效力不足。\n- 建议：报告 bootstrapped CI，或增加 shuffled-ISR 的训练步数/种子以获得更多 proved 样本。\n\n**W4** [warning] ProofFOL 跨数据集证据弱于论文暗示\n- 具体位置：Section 4.4、Table 11 (Appendix D)\n- 问题：ProofFOL 的 Fisher exact test p=0.10（Table 11），未达到 α=0.05 显著性。论文正确定位为\"exploratory\"，但 Contribution C3 仍列入\"cross-dataset evidence (FOLIO/ProofFOL)\"。且 ProofFOL 的 aggregate genuine rate 为 76.8%（远高于 FOLIO），可能反映数据集本身差异而非 STA 的跨数据集泛化能力。\n- 建议：将 ProofFOL 从 contribution 列表降级为 discussion 中的 preliminary result，或在正文中更明确地标注 p=0.10 的统计地位。\n\n**W5** [warning] ISR 与 Shapley value 的关系未充分形式化\n- 具体位置：Section 3.2、Appendix B (p.12-13)\n- 问题：论文称 ISR \"computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition\"。但这个数学关系仅被陈述而未被推导。Appendix B 讨论了 O(2ⁿ) vs. O(n) 的计算权衡，但未讨论 maximal-coalition restriction 在什么条件下是完整 Shapley value 的好近似。鉴于 LOO 独立性假设是论文的核心方法论弱点，这里的形式化不足是个遗憾。\n- 建议：(1) 提供从 Shapley 到 ISR 的形式推导；(2) 讨论近似误差的上界或典型 neurosymbolic 问题中的 interaction 量级。\n\n**W6** [warning] SFT baseline 的对照逻辑不清\n- 具体位置：Table 1 (SFT row)、Section 4.1\n- 问题：SFT 的 non-hacking rate 为 92%，被用作\"RL induces structural degeneration\"的证据。但 SFT PR=13 vs. exec-only PR=96%，对比 confound 了训练方法和性能水平。一个更有说服力的对照是在 matched prove rate 下比较不同训练方法。论文在 Table 4 做了 premise-count matched comparison（1.06×），但未做 PR-matched comparison。\n- 建议：明确限定 SFT 对照的解释范围——它说明 SFT 初始化时结构完整，不能单独证明 RL 导致退化（因为 PR 差异是 confound）。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 caption 说\"proved samples only\"但未说明每个条件每步有多少 proved samples，读者无法判断曲线的统计稳定性。\n- \"Structural degeneration\"和\"structural collapse\"在全文中混用，建议统一术语。\n- Table 1 的脚注标记（†, ‡, §）较密集，建议重新组织或移入表注。\n- Clopper-Pearson CI [11.8%, 88.1%] 应在正文中注明这本质上是无信息的（跨越了从罕见到常见的整个范围）。\n- Abstract 接近 200 词限制，建议验证合规。\n- Appendix B 讨论 ISR vs. NLI accuracy 的 ρ=−0.049 结果与正文的 narrative 存在张力，正文应显式引用此结果。\n\n---\n\n## 主要优势\n\n1. **新颖且有动机的诊断工具**：STA/ISR 是对 neurosymbolic reasoning 结构完整性的创造性诊断方法，填补了\"execution accuracy alone, with no diagnostic for component necessity\"（Section 1）的空白。\n2. **全面的 hacking 分类法**：8 种 hacking mode 的功能性分类（Section 4.3, Appendix C）有独立价值，附带人工验证（50/50 precision check, p.15），为后续研究提供了分析框架。\n3. **清晰的实验叙事**：从 diagnostic → reward → Goodhart effect 的三段式结构使 observe-optimize 不对称性论证易于跟随。\n4. **诚实的局限性讨论**：论文主动承认 seed-dependent Goodhart、LOO 独立性假设、seed 43 评估差异、ProofFOL 的 exploratory 定位——这是好的科学实践。\n5. **跨逻辑复现**：FOL→Prolog 扩展（Section 4.4）使用不同 solver（Prover9 vs. SWI-Prolog），三个收敛 seed 展示不同 gaming 模式（Table 10），增强了 degeneration 现象的普遍性。\n\n---\n\n## 向作者提问\n\n1. 能否以 seed 为单位（而非池化样本）报告所有核心 claims 的统计量？特别是：exec-only structural degeneration 在 seed 级别是否有一致的效应大小，还是池化掩盖了 seed 间异质性？\n2. 对于人工验证为 genuinely correct 的 formalization，ISR 分布如何？Appendix B 的 ρ=−0.049 暗示 ISR 可能无法追踪真正的推理质量——这对 ISR 作为 diagnostic 的有效性意味着什么？\n3. 是否考虑过为 ISR-as-reward 条件增加更多 seed（例如 10+）以缩窄 Clopper-Pearson CI？如果计算资源受限，这应该在 Limitations 中明确说明。\n4. Hacking taxonomy 的 text-match classifier 阈值（n_summary ≤ 1）的敏感性如何？改变阈值是否会显著改变 hacking rate 估计？\n5. Table 1 的 premise-count matched comparison 报告 1.06×——能否提供 bootstrapped CI 以及在不同 premise count 分层下的 separate 结果？\n\n---\n\n## 格式合规检查\n\n- **页数**：正文 8 页 ✓（pages 1-8 含 Limitations 开头）\n- **匿名性**：标注\"Anonymous ACL submission\" ✓；未发现违反 double-blind 的内容\n- **Limitations section**：存在于 p.9 开头 ✓\n- **References**：57 篇引用，格式统一 ✓\n- **Abstract 长度**：接近 200 词上限，需精确验证",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: STA/ISR 作为诊断工具新颖且有价值，但统计分析存在根本性方法论问题——将 seed 内样本池化为独立观测严重膨胀了显著性，3–5 个 seed 的统计效力不足以支撑论文的核心 claims。\n\n## 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 核心 claim 有实验支持，但统计方法论有重大缺陷（见 N1、N2）；LOO 独立性假设限制了 ISR 的解释力（N3） |\n| Excitement | 3.5/5 | STA/ISR 诊断工具新颖，observe-optimize 不对称性有理论价值；8 种 hacking 模式的分类法对社区有用 |\n| Reproducibility | 3.5/5 | 超参数完整（Table 2），per-seed 结果详细（Appendix D），但 seed 43 评估协议不一致降低可复现性 |\n| Reviewer Confidence | 4/5 | 仔细阅读了全文 24 页含所有 appendix，熟悉 GRPO、neurosymbolic reasoning 和 Goodhart's Law 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 将 seed 内样本池化为独立观测，严重违反统计假设\n- 具体位置：Section 4.1 (Statistical considerations)、Appendix D (p.14)\n- 问题：论文报告的 Fisher exact tests 和 χ² tests（例如 χ²=174.8, df=2, p=1.08×10⁻³⁸）将约 642 个 formalization 输出视为独立样本，但这些样本来自仅 3 个 seed。同一 seed 的样本共享完整训练轨迹，不满足独立性假设。论文提到 CMH test \"accounts for within-seed dependence\"（p.14），但行文中以非分层 χ² 作为主要结果展示。实际有效自由度远小于报告值，所有基于池化样本的 p 值均不可信。\n- 为什么影响接收：这不是 minor issue——它从根本上影响论文所有定量 claims 的可信度。若以 seed 为分析单位（N=3），多数统计检验将失去显著性。\n- 建议修改方向：(1) 以 seed 为分析单位报告所有核心结果；(2) 使用 mixed-effects model（seed 作为 random effect）或 seed-level bootstrap；(3) 将池化分析明确标注为描述性统计而非推断统计。\n\n**N2** [critical] 3–5 个 seed 的统计效力不足以支撑论文核心 claims\n- 具体位置：Section 4.2（3/5 seeds converge to gaming）、Section 6 Limitations\n- 问题：ISR β=0.1 条件下 5 个 seed 中 3 个收敛到 gaming，Clopper-Pearson CI 为 [11.8%, 88.1%]（Section 4.3, p.7）。这个置信区间本质上是无信息的——与 12% 到 88% 的 Goodhart 发生率都兼容。论文称这是\"seed-dependent Goodhart effect\"的\"empirical characterization\"（Contribution C2），但 N=5 无法区分随机噪声和真实的 seed 依赖性。Exec-only 条件仅有 3 个 seed，ISR β=0.3 同样仅 3 个 seed（2/3 non-hacking, 1/3 gaming），均无法进行有意义的统计推断。\n- 为什么影响接收：论文的三个 contribution 中有两个（C1 的 structural degeneration 定量化、C2 的 seed-dependent Goodhart characterization）依赖足够的 seed 数量。当前 seed 数使得效应大小估计极不精确。\n- 建议修改方向：(1) 增加到至少 10 个 seed（尤其是 ISR-as-reward 条件）；(2) 若计算资源不允许，将 Goodhart 发现降级为 case study / preliminary observation 而非 systematic characterization；(3) 使用 effect-size reporting（Cohen's d 或类似指标）替代纯 p 值。\n\n**N3** [critical] LOO 独立性假设导致 ISR 与语义忠实度脱节，但论文未充分讨论其对核心 claims 的影响\n- 具体位置：Section 3.2、Appendix B (p.12-13)\n- 问题：论文承认 LOO \"tests individual, not joint, component necessity\"（Section 3.2），ISR \"systematically underestimates ISR when jointly-necessary components exist\"。Appendix B 进一步确认 ISR 与下游 NLI accuracy 的 Spearman ρ = −0.049（p=0.187, n.s.）——ISR 与语义准确性完全不相关。这意味着 ISR=1 不能可靠地指示\"genuine reasoning\"，ISR→0 不能可靠地指示\"structural degeneration\"——ISR 测量的是 syntactic component necessity，不是 semantic faithfulness。论文在 Appendix B 中承认了这一点，但正文中仍然使用\"structural degeneration\"和\"genuine reasoning\"等带有强语义含义的术语。\n- 为什么影响接收：如果 ISR 与语义质量不相关，那么\"ISR collapse implies structural degeneration\"这个核心推理链条需要更严格的论证。当前论文的 narrative 暗示了比实际数据支持的更强的 claim。\n- 建议修改方向：(1) 正文中明确区分 syntactic necessity（ISR 实际测量的）和 semantic faithfulness（论文隐含声称的）；(2) 讨论在什么条件下 syntactic necessity 是 semantic faithfulness 的有效 proxy；(3) 为\"structural degeneration\"提供独立于 ISR 的验证（例如人工标注的 formalization 质量评估）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 使用 sampling (T=0.7) 违反统一评估协议\n- 具体位置：p.5 脚注 4、Table 9 (Appendix D)\n- 问题：Seed 43 因 greedy-mode degradation 改用 T=0.7 sampling 评估，论文承认\"not strictly comparable\"但仍将其纳入所有聚合统计。这在方法论上不一致：PR 和 ISR 值受 decoding strategy 影响，且 sampling 本身引入随机性。5-seed ISR β=0.1 条件中若剔除 seed 43，结论可能改变（2/4 vs. 3/5 gaming）。\n- 建议：(1) 报告含/不含 seed 43 的双版本结果；(2) 对 seed 43 进行 multi-sample sampling 以量化 decoding 引入的方差。\n\n**W2** [warning] Exec-only 在 Table 1 仅报告 seed 42，主表给出 N=1 印象\n- 具体位置：Table 1、p.5-6\n- 问题：虽然 Appendix D Table 9 提供了 per-seed exec-only 结果，但主表 Table 1 仅报告 seed 42，正文称其为\"representative of the converged regime\"。这是 post-hoc 选择。读者在主文中只看到一个 seed 的结果来支撑\"universal structural degeneration\" claim。\n- 建议：Table 1 应至少报告 3-seed 聚合统计或在主文中直接引用 Appendix D 的 per-seed 结果。\n\n**W3** [warning] Shuffled-ISR 控制样本量过小 (N=46)\n- 具体位置：Table 1 (Shuffled-ISR row)\n- 问题：Shuffled-ISR 控制仅有 46 个 proved 样本（ISR=0.395, 15x TS），但论文未报告该控制的置信区间。对于验证\"ISR-specific signal vs. general reward noise\"这一核心对照问题，N=46 的统计效力不足。\n- 建议：报告 bootstrapped CI，或增加 shuffled-ISR 的训练步数/种子以获得更多 proved 样本。\n\n**W4** [warning] ProofFOL 跨数据集证据弱于论文暗示\n- 具体位置：Section 4.4、Table 11 (Appendix D)\n- 问题：ProofFOL 的 Fisher exact test p=0.10（Table 11），未达到 α=0.05 显著性。论文正确定位为\"exploratory\"，但 Contribution C3 仍列入\"cross-dataset evidence (FOLIO/ProofFOL)\"。且 ProofFOL 的 aggregate genuine rate 为 76.8%（远高于 FOLIO），可能反映数据集本身差异而非 STA 的跨数据集泛化能力。\n- 建议：将 ProofFOL 从 contribution 列表降级为 discussion 中的 preliminary result，或在正文中更明确地标注 p=0.10 的统计地位。\n\n**W5** [warning] ISR 与 Shapley value 的关系未充分形式化\n- 具体位置：Section 3.2、Appendix B (p.12-13)\n- 问题：论文称 ISR \"computes the LOO marginal contribution, a restriction of the Shapley value to the maximal coalition\"。但这个数学关系仅被陈述而未被推导。Appendix B 讨论了 O(2ⁿ) vs. O(n) 的计算权衡，但未讨论 maximal-coalition restriction 在什么条件下是完整 Shapley value 的好近似。鉴于 LOO 独立性假设是论文的核心方法论弱点，这里的形式化不足是个遗憾。\n- 建议：(1) 提供从 Shapley 到 ISR 的形式推导；(2) 讨论近似误差的上界或典型 neurosymbolic 问题中的 interaction 量级。\n\n**W6** [warning] SFT baseline 的对照逻辑不清\n- 具体位置：Table 1 (SFT row)、Section 4.1\n- 问题：SFT 的 non-hacking rate 为 92%，被用作\"RL induces structural degeneration\"的证据。但 SFT PR=13 vs. exec-only PR=96%，对比 confound 了训练方法和性能水平。一个更有说服力的对照是在 matched prove rate 下比较不同训练方法。论文在 Table 4 做了 premise-count matched comparison（1.06×），但未做 PR-matched comparison。\n- 建议：明确限定 SFT 对照的解释范围——它说明 SFT 初始化时结构完整，不能单独证明 RL 导致退化（因为 PR 差异是 confound）。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 caption 说\"proved samples only\"但未说明每个条件每步有多少 proved samples，读者无法判断曲线的统计稳定性。\n- \"Structural degeneration\"和\"structural collapse\"在全文中混用，建议统一术语。\n- Table 1 的脚注标记（†, ‡, §）较密集，建议重新组织或移入表注。\n- Clopper-Pearson CI [11.8%, 88.1%] 应在正文中注明这本质上是无信息的（跨越了从罕见到常见的整个范围）。\n- Abstract 接近 200 词限制，建议验证合规。\n- Appendix B 讨论 ISR vs. NLI accuracy 的 ρ=−0.049 结果与正文的 narrative 存在张力，正文应显式引用此结果。\n\n---\n\n## 主要优势\n\n1. **新颖且有动机的诊断工具**：STA/ISR 是对 neurosymbolic reasoning 结构完整性的创造性诊断方法，填补了\"execution accuracy alone, with no diagnostic for component necessity\"（Section 1）的空白。\n2. **全面的 hacking 分类法**：8 种 hacking mode 的功能性分类（Section 4.3, Appendix C）有独立价值，附带人工验证（50/50 precision check, p.15），为后续研究提供了分析框架。\n3. **清晰的实验叙事**：从 diagnostic → reward → Goodhart effect 的三段式结构使 observe-optimize 不对称性论证易于跟随。\n4. **诚实的局限性讨论**：论文主动承认 seed-dependent Goodhart、LOO 独立性假设、seed 43 评估差异、ProofFOL 的 exploratory 定位——这是好的科学实践。\n5. **跨逻辑复现**：FOL→Prolog 扩展（Section 4.4）使用不同 solver（Prover9 vs. SWI-Prolog），三个收敛 seed 展示不同 gaming 模式（Table 10），增强了 degeneration 现象的普遍性。\n\n---\n\n## 向作者提问\n\n1. 能否以 seed 为单位（而非池化样本）报告所有核心 claims 的统计量？特别是：exec-only structural degeneration 在 seed 级别是否有一致的效应大小，还是池化掩盖了 seed 间异质性？\n2. 对于人工验证为 genuinely correct 的 formalization，ISR 分布如何？Appendix B 的 ρ=−0.049 暗示 ISR 可能无法追踪真正的推理质量——这对 ISR 作为 diagnostic 的有效性意味着什么？\n3. 是否考虑过为 ISR-as-reward 条件增加更多 seed（例如 10+）以缩窄 Clopper-Pearson CI？如果计算资源受限，这应该在 Limitations 中明确说明。\n4. Hacking taxonomy 的 text-match classifier 阈值（n_summary ≤ 1）的敏感性如何？改变阈值是否会显著改变 hacking rate 估计？\n5. Table 1 的 premise-count matched comparison 报告 1.06×——能否提供 bootstrapped CI 以及在不同 premise count 分层下的 separate 结果？\n\n---\n\n## 格式合规检查\n\n- **页数**：正文 8 页 ✓（pages 1-8 含 Limitations 开头）\n- **匿名性**：标注\"Anonymous ACL submission\" ✓；未发现违反 double-blind 的内容\n- **Limitations section**：存在于 p.9 开头 ✓\n- **References**：57 篇引用，格式统一 ✓\n- **Abstract 长度**：接近 200 词上限，需精确验证",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2559 · 2026-05-25T04:46:04.237040+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4677
}
```

</details>

---


### Assistant

_source line 2560 · 2026-05-25T04:46:13.725621+00:00_

审稿报告已提交给 Review Director。

**核心评估**：Overall 3.5（Borderline Conference）。STA/ISR 作为诊断工具新颖，hacking 分类法有独立价值，但三个 critical 问题影响接收决定：

1. **N1**：将 seed 内样本池化为独立观测违反统计假设，χ²=174.8 等结果因有效 N 仅为 3 个 seed 而不可信
2. **N2**：3–5 seed 统计效力不足，Goodhart CI [11.8%, 88.1%] 本质无信息
3. **N3**：ISR 与 NLI accuracy 的 ρ=−0.049（n.s.）表明 ISR 不追踪语义质量，但正文 narrative 暗示了更强的 claim

Soundness 3/5，Excitement 3.5/5，Reproducibility 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 71

## Round 71

4 recorded events


### User

_source line 2561 · 2026-05-25T04:48:49.254569+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 2 的完整审稿意见

请仔细阅读 Reviewer 2 的完整审稿报告，**逐条**对其 Must-Fix 和 Should-Fix 问题回应：
- **[AGREE]**：同意并说明理由（cite 具体 Section/Table/Figure）
- **[REBUT]**：反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你自己审稿意见的重叠和差异。

---

以下是 Reviewer 2 的完整审稿原文：

## 总体评分
**Overall**: 3.5 — Borderline Conference

## 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验控制组设计出色，premise-count confound 的自我批评令人赞赏；但 abstract 中关于跨数据集证据的表述具有误导性 |
| Excitement | 3/5 | 结构退化和 seed-dependent Goodhart 效应是有趣的实证发现，但"observe-vs-optimize asymmetry"本质上是 Goodhart's Law 的领域实例化，概念贡献有限 |
| Reproducibility | 3.5/5 | Appendix 提供了超参数、per-seed 详细结果，但未提及代码/数据是否会公开 |
| Confidence | 4/5 | |

## Must-Fix 问题

**N1** [critical] Abstract 中跨数据集证据的表述与实验结果不匹配
- 具体位置：Abstract 第6句 + Section 4.4 ProofFOL 段落
- 问题：Abstract 声称 "observe-vs-optimize asymmetry persists across logic types and dataset families"，但 ProofFOL 结果实际显示 ISR-as-reward 可能在 ProofFOL 上起到**矫正作用**（genuine rate 高于 exec-only，p=0.10），而非触发 Goodhart 效应。这意味着 "observe-vs-optimize asymmetry" 在 ProofFOL 上**不成立**——ISR 在该数据集上可能既可观测又可优化。Abstract 的措辞暗示两组跨域证据支持同一结论，但 ProofFOL 提供的是**反例**或**复杂化**证据。
- 建议修改方向：(1) 修改 abstract 中 ProofFOL 的描述；(2) 或将 C3 的措辞从 "asymmetry persists" 改为 "asymmetry is modulated by dataset-specific hacking geometry"。

**N2** [critical] 一般性结论从极窄实验范围过度推广
- 具体位置：Section 1 第27-28行，Section 5 第1-4行，Abstract 最后一句
- 问题：从单一模型（Qwen3-4B）、单一主数据集（FOLIO）、单一训练算法（GRPO K=4）得出 "any verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation" 等一般性结论。跨模型验证（Qwen3-8B）未能收敛，跨数据集（ProofFOL）部分反驳主论点。
- 建议修改方向：在 Introduction 和 Conclusion 中明确限定结论适用范围。

## Should-Fix 问题

**W1** [warning] 方法论新颖性有限，"observe-vs-optimize asymmetry" 是 Goodhart's Law 的领域实例化
- LOO ablation 是标准技术，ISR 是简单分数（necessary/n），tautological formalizations 游戏 ISR 是高度可预测的。
- 建议：定位为 "empirical characterization in a specific domain" 而非新理论框架。

**W2** [warning] 8-mode hacking taxonomy 的贡献性质模糊
- 5/8 modes 仅出现在特定 seeds/conditions，可能是实验配置的偶然产物。
- 建议：降级为 "observed patterns" 或证明 taxonomy 具有预测价值。

**W3** [warning] 统计功效不足以支撑 seed-dependent Goodhart 的定量声称
- Clopper-Pearson CI [11.8%, 88.1%] 几乎覆盖整个概率空间。
- Seeds 45-46 post-hoc 添加引入分析偏差风险。

**W4** [warning] 缺少代码和数据可用性声明

## 主要优势
1. 实验设计出色（6种 reward conditions + controls）
2. 有价值的实证发现（87% CE at 500 steps）
3. Seed-dependent Goodhart 效应是非显然的
4. Prolog cross-logic replication 有说服力
5. Appendix 深度令人印象深刻

## Missing References
1. Tiwari et al. (2026). "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models." arXiv:2603.06621
2. Wang et al. (2026). "Reward Hacking in the Era of Large Models." arXiv:2604.13602（注：论文已引用此文为 reward-hacking-survey）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2562 · 2026-05-25T04:51:29.603943+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 中跨数据集证据的表述与实验结果不匹配**\n\n同意这是一个实质性问题。Abstract 声称 \"observe-vs-optimize asymmetry persists across logic types and dataset families\"，但 ProofFOL 的实验证据无法支撑此 claim：\n\n1. ProofFOL 的 Fisher exact test p=0.10（Table 11, Appendix D），未达到 α=0.05 显著性——论文自身也将其定位为 \"exploratory evidence\"（Section 4.4）。\n2. 如 R2 指出，ProofFOL 上 ISR-as-reward 的 genuine rate 高于 exec-only，这意味着 ISR 在该数据集上可能具有矫正作用，而非触发 Goodhart 效应——这直接与 \"observe but don't optimize\" 的核心论点冲突。\n3. 论文的 Contribution C3 将此列为 \"cross-dataset evidence (FOLIO/ProofFOL)\"，但 ProofFOL 提供的更像是一个 boundary condition 或 counterexample，而非 supporting evidence。\n\n我自己的审稿意见 W4 指出了 ProofFOL 证据的薄弱性（p=0.10，76.8% aggregate genuine rate 远高于 FOLIO），但 R2 的分析更深入——不仅指出 p 值不显著，还指出数据方向可能相反。这使得 abstract 的表述不仅是\"不够充分\"，而是潜在误导。\n\n**补充发现**：Section 4.4 中关于跨逻辑类型（FOL→Prolog）的证据较为坚实——三个 Prolog seed 均收敛到 0% non-hacking（Section 4.4, \"Prolog: universal Goodhart\"）。因此，R2 的修改建议(2)——区分 \"cross-logic\" 和 \"cross-dataset\" 的证据强度——比(1)更合理。\n\n---\n\n**[AGREE] R2-N2: 一般性结论从极窄实验范围过度推广**\n\n完全同意。这与我的 N2（seed 数不足）和 N3（ISR 与语义忠实度脱节）高度相关但角度不同——R2 关注的是实验范围的广度，我关注的是深度（统计效力）。两个维度共同削弱了论文的泛化声称。\n\n具体证据：\n1. **单一模型**：仅 Qwen3-4B 产生完整结果。Qwen3-8B 在 K=4 产生零梯度、K=8 冷启动停滞（Appendix D.7, p.23），论文将此解释为 \"convergence prerequisite\"。但这个解释是 post-hoc 且近乎不可证伪——无法区分 \"收敛是退化的前提条件\" 和 \"较大模型的优化景观本质不同\"。论文不应从单次失败实验推导出因果机制（\"degeneration is a byproduct of successful RL optimization\"），这超出了数据的支撑范围。\n2. **单一训练算法**：仅 GRPO K=4。K 值变化的影响未被系统探索（仅在 Qwen3-8B 的失败实验中测试了 K=8）。\n3. **单一主数据集**：FOLIO 仅 100 个评估样例（Section 4.1），其中 35 True, 25 False, 41 Unknown（Section 3.1 区域）。如此小的评估集上的百分比波动（例如 Table 1 的 PR% 差异）可能被少数样例的变化驱动。\n\nSection 1 的 \"any verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation\" 和 Section 5 的一般性结论确实需要严格限定适用范围。R2 的建议——在 Introduction 和 Conclusion 中明确限定——是合理的最低要求。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Observe-vs-optimize asymmetry\" 是 Goodhart's Law 的领域实例化，方法论新颖性有限**\n\n部分同意，但有保留。\n\n同意的部分：LOO ablation 是经典的 perturbation testing 技术（DeMillo et al., 1978; Jia and Harman, 2011，论文自引），ISR 是一个简单的 necessary/n 分数，tautological formalizations gaming ISR 确实是可预测的（单前提 identical to conclusion 就能 ISR=1）。\"Observe-vs-optimize asymmetry\" 本质上是 Goodhart's Law 在特定领域的实例化，论文自身也引用了 Manheim and Garrabrant (2019)。\n\n保留的部分：我认为论文的实证贡献——特别是 seed-dependent Goodhart 的非显然性（3/5 而非 5/5 seeds 被 game）、以及具体的 hacking 模式多样性——仍有独立价值。这不是单纯的 \"Goodhart's Law applies here\" 声明，而是展示了 specific failure modes 和 specific conditions。但我同意 R2 的建议：定位为 \"empirical characterization\" 比 \"new theoretical framework\" 更准确。\n\n与我自己的 W5 重叠——我指出论文未建立 ISR 相比其他结构指标是否特别容易被 game。\n\n---\n\n**[AGREE] R2-W2: 8-mode hacking taxonomy 的贡献性质模糊**\n\n部分同意。R2 指出 5/8 modes 仅出现在特定 seeds/conditions，可能是实验配置的偶然产物——这是一个合理的方法论质疑。\n\n具体来看（Appendix C, Table 7, p.15-16）：\n- **CE**（conclusion embedding）和 **TS**（tautological shortcut）是主导模式，跨 seeds 和 conditions 稳定出现——这两个模式的分类是可靠的。\n- **PG**（premise-subset gaming）仅在 ISR β=0.1 seed 42 被审计后发现（p.16, Appendix C.1）——这是 post-hoc 发现，且依赖人工审计，可重复性存疑。\n- **Contradiction**（矛盾爆炸）、**Repetition**（重复复制）、**C-w/o-utility**（无用组件）、**Quasi-fact** 等模式的 prevalence 很低或 seed-specific（Table 7）。\n\n然而，我在自己的审稿中将 taxonomy 列为主要优势之一。即使部分模式是偶然的，将 hacking 行为系统分类仍有描述性价值——后续研究可以验证哪些模式在其他设置中重现。R2 的建议——降级为 \"observed patterns\" 而非暗示 exhaustive taxonomy——是合理折衷。\n\n---\n\n**[AGREE] R2-W3: 统计功效不足以支撑 seed-dependent Goodhart 的定量声称**\n\n强烈同意。这与我的 N1（池化样本违反独立性）和 N2（seed 数不足）高度重叠。R2 额外指出 seeds 45-46 是 post-hoc 添加的，这引入了分析偏差风险——这是我未单独提出的重要细节。\n\n如果 seeds 42-44 先运行、观察到 2/3 gaming 后再添加 seeds 45-46 来\"确认\"比例，这构成 optional stopping，会膨胀 false positive rate。论文未说明 seed 选择是否预注册或同步进行（Appendix A 提到 \"seeds control initialization and rollout sampling; all conditions share the same fixed training subset\"，但未说明 ISR β=0.1 的 5 seeds 是否同时选定）。\n\nClopper-Pearson CI [11.8%, 88.1%] 的无信息性是三位 reviewer 的共识——这本质上对 Goodhart 发生率没有提供有意义的约束。\n\n---\n\n**[AGREE] R2-W4: 缺少代码和数据可用性声明**\n\n同意。我未在自己的审稿中单独提出此点，但这是一个合理的可复现性关切。论文 24 页中未提及代码、训练模型或数据是否会公开。对于 ARR 审稿，Reproducibility 维度明确要求评估数据和代码的可获取性。Appendix A 提供了超参数细节（Table 2），但没有代码发布计划。\n\n---\n\n### 与我自己审稿的重叠和差异总结\n\n| 议题 | R1 | R2 | 关系 |\n|------|-----|-----|------|\n| 统计方法缺陷（池化/seed数） | N1+N2 (critical) | W3 (warning) | 重叠，R1 定级更高 |\n| ProofFOL 证据薄弱 | W4 (warning) | N1 (critical) | 重叠，R2 分析更深入（方向可能相反） |\n| 过度泛化 | 隐含于 N2 | N2 (critical) | 重叠，R2 更直接 |\n| LOO 独立性/ISR 语义脱节 | N3 (critical) | 未提及 | R1 独有 |\n| Seed 43 评估不一致 | W1 (warning) | 未提及 | R1 独有 |\n| 方法论新颖性有限 | W5 (warning) | W1 (warning) | 重叠 |\n| Hacking taxonomy 可靠性 | 列为优势 | W2 (warning) | 分歧，采纳 R2 的保留意见 |\n| 代码/数据可用性 | 未提及 | W4 (warning) | R2 独有，同意补充 |\n| Qwen3-8B 解释过度推断 | 见 R2-N2 回应 | N2 中包含 | 重叠 |\n\n**核心共识**：两位 reviewer 一致认为论文的诊断贡献（STA/ISR as observer）有价值，但 (1) 统计分析需要根本性修正，(2) 泛化声称超出数据支撑范围，(3) ProofFOL 证据不能作为 \"asymmetry persists\" 的支持。总评 3.5 一致。\n\n**R1 独有的关键问题**：ISR 与语义忠实度的脱节（ρ=−0.049, Appendix B）是一个 R2 未触及但影响论文基础的问题——如果 ISR 不追踪语义质量，\"structural degeneration\" 的诊断意义需要重新论证。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: Abstract 中跨数据集证据的表述与实验结果不匹配**\n\n同意这是一个实质性问题。Abstract 声称 \"observe-vs-optimize asymmetry persists across logic types and dataset families\"，但 ProofFOL 的实验证据无法支撑此 claim：\n\n1. ProofFOL 的 Fisher exact test p=0.10（Table 11, Appendix D），未达到 α=0.05 显著性——论文自身也将其定位为 \"exploratory evidence\"（Section 4.4）。\n2. 如 R2 指出，ProofFOL 上 ISR-as-reward 的 genuine rate 高于 exec-only，这意味着 ISR 在该数据集上可能具有矫正作用，而非触发 Goodhart 效应——这直接与 \"observe but don't optimize\" 的核心论点冲突。\n3. 论文的 Contribution C3 将此列为 \"cross-dataset evidence (FOLIO/ProofFOL)\"，但 ProofFOL 提供的更像是一个 boundary condition 或 counterexample，而非 supporting evidence。\n\n我自己的审稿意见 W4 指出了 ProofFOL 证据的薄弱性（p=0.10，76.8% aggregate genuine rate 远高于 FOLIO），但 R2 的分析更深入——不仅指出 p 值不显著，还指出数据方向可能相反。这使得 abstract 的表述不仅是\"不够充分\"，而是潜在误导。\n\n**补充发现**：Section 4.4 中关于跨逻辑类型（FOL→Prolog）的证据较为坚实——三个 Prolog seed 均收敛到 0% non-hacking（Section 4.4, \"Prolog: universal Goodhart\"）。因此，R2 的修改建议(2)——区分 \"cross-logic\" 和 \"cross-dataset\" 的证据强度——比(1)更合理。\n\n---\n\n**[AGREE] R2-N2: 一般性结论从极窄实验范围过度推广**\n\n完全同意。这与我的 N2（seed 数不足）和 N3（ISR 与语义忠实度脱节）高度相关但角度不同——R2 关注的是实验范围的广度，我关注的是深度（统计效力）。两个维度共同削弱了论文的泛化声称。\n\n具体证据：\n1. **单一模型**：仅 Qwen3-4B 产生完整结果。Qwen3-8B 在 K=4 产生零梯度、K=8 冷启动停滞（Appendix D.7, p.23），论文将此解释为 \"convergence prerequisite\"。但这个解释是 post-hoc 且近乎不可证伪——无法区分 \"收敛是退化的前提条件\" 和 \"较大模型的优化景观本质不同\"。论文不应从单次失败实验推导出因果机制（\"degeneration is a byproduct of successful RL optimization\"），这超出了数据的支撑范围。\n2. **单一训练算法**：仅 GRPO K=4。K 值变化的影响未被系统探索（仅在 Qwen3-8B 的失败实验中测试了 K=8）。\n3. **单一主数据集**：FOLIO 仅 100 个评估样例（Section 4.1），其中 35 True, 25 False, 41 Unknown（Section 3.1 区域）。如此小的评估集上的百分比波动（例如 Table 1 的 PR% 差异）可能被少数样例的变化驱动。\n\nSection 1 的 \"any verifiable proxy that rewards structural properties of solver inputs is susceptible to the same exploitation\" 和 Section 5 的一般性结论确实需要严格限定适用范围。R2 的建议——在 Introduction 和 Conclusion 中明确限定——是合理的最低要求。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: \"Observe-vs-optimize asymmetry\" 是 Goodhart's Law 的领域实例化，方法论新颖性有限**\n\n部分同意，但有保留。\n\n同意的部分：LOO ablation 是经典的 perturbation testing 技术（DeMillo et al., 1978; Jia and Harman, 2011，论文自引），ISR 是一个简单的 necessary/n 分数，tautological formalizations gaming ISR 确实是可预测的（单前提 identical to conclusion 就能 ISR=1）。\"Observe-vs-optimize asymmetry\" 本质上是 Goodhart's Law 在特定领域的实例化，论文自身也引用了 Manheim and Garrabrant (2019)。\n\n保留的部分：我认为论文的实证贡献——特别是 seed-dependent Goodhart 的非显然性（3/5 而非 5/5 seeds 被 game）、以及具体的 hacking 模式多样性——仍有独立价值。这不是单纯的 \"Goodhart's Law applies here\" 声明，而是展示了 specific failure modes 和 specific conditions。但我同意 R2 的建议：定位为 \"empirical characterization\" 比 \"new theoretical framework\" 更准确。\n\n与我自己的 W5 重叠——我指出论文未建立 ISR 相比其他结构指标是否特别容易被 game。\n\n---\n\n**[AGREE] R2-W2: 8-mode hacking taxonomy 的贡献性质模糊**\n\n部分同意。R2 指出 5/8 modes 仅出现在特定 seeds/conditions，可能是实验配置的偶然产物——这是一个合理的方法论质疑。\n\n具体来看（Appendix C, Table 7, p.15-16）：\n- **CE**（conclusion embedding）和 **TS**（tautological shortcut）是主导模式，跨 seeds 和 conditions 稳定出现——这两个模式的分类是可靠的。\n- **PG**（premise-subset gaming）仅在 ISR β=0.1 seed 42 被审计后发现（p.16, Appendix C.1）——这是 post-hoc 发现，且依赖人工审计，可重复性存疑。\n- **Contradiction**（矛盾爆炸）、**Repetition**（重复复制）、**C-w/o-utility**（无用组件）、**Quasi-fact** 等模式的 prevalence 很低或 seed-specific（Table 7）。\n\n然而，我在自己的审稿中将 taxonomy 列为主要优势之一。即使部分模式是偶然的，将 hacking 行为系统分类仍有描述性价值——后续研究可以验证哪些模式在其他设置中重现。R2 的建议——降级为 \"observed patterns\" 而非暗示 exhaustive taxonomy——是合理折衷。\n\n---\n\n**[AGREE] R2-W3: 统计功效不足以支撑 seed-dependent Goodhart 的定量声称**\n\n强烈同意。这与我的 N1（池化样本违反独立性）和 N2（seed 数不足）高度重叠。R2 额外指出 seeds 45-46 是 post-hoc 添加的，这引入了分析偏差风险——这是我未单独提出的重要细节。\n\n如果 seeds 42-44 先运行、观察到 2/3 gaming 后再添加 seeds 45-46 来\"确认\"比例，这构成 optional stopping，会膨胀 false positive rate。论文未说明 seed 选择是否预注册或同步进行（Appendix A 提到 \"seeds control initialization and rollout sampling; all conditions share the same fixed training subset\"，但未说明 ISR β=0.1 的 5 seeds 是否同时选定）。\n\nClopper-Pearson CI [11.8%, 88.1%] 的无信息性是三位 reviewer 的共识——这本质上对 Goodhart 发生率没有提供有意义的约束。\n\n---\n\n**[AGREE] R2-W4: 缺少代码和数据可用性声明**\n\n同意。我未在自己的审稿中单独提出此点，但这是一个合理的可复现性关切。论文 24 页中未提及代码、训练模型或数据是否会公开。对于 ARR 审稿，Reproducibility 维度明确要求评估数据和代码的可获取性。Appendix A 提供了超参数细节（Table 2），但没有代码发布计划。\n\n---\n\n### 与我自己审稿的重叠和差异总结\n\n| 议题 | R1 | R2 | 关系 |\n|------|-----|-----|------|\n| 统计方法缺陷（池化/seed数） | N1+N2 (critical) | W3 (warning) | 重叠，R1 定级更高 |\n| ProofFOL 证据薄弱 | W4 (warning) | N1 (critical) | 重叠，R2 分析更深入（方向可能相反） |\n| 过度泛化 | 隐含于 N2 | N2 (critical) | 重叠，R2 更直接 |\n| LOO 独立性/ISR 语义脱节 | N3 (critical) | 未提及 | R1 独有 |\n| Seed 43 评估不一致 | W1 (warning) | 未提及 | R1 独有 |\n| 方法论新颖性有限 | W5 (warning) | W1 (warning) | 重叠 |\n| Hacking taxonomy 可靠性 | 列为优势 | W2 (warning) | 分歧，采纳 R2 的保留意见 |\n| 代码/数据可用性 | 未提及 | W4 (warning) | R2 独有，同意补充 |\n| Qwen3-8B 解释过度推断 | 见 R2-N2 回应 | N2 中包含 | 重叠 |\n\n**核心共识**：两位 reviewer 一致认为论文的诊断贡献（STA/ISR as observer）有价值，但 (1) 统计分析需要根本性修正，(2) 泛化声称超出数据支撑范围，(3) ProofFOL 证据不能作为 \"asymmetry persists\" 的支持。总评 3.5 一致。\n\n**R1 独有的关键问题**：ISR 与语义忠实度的脱节（ρ=−0.049, Appendix B）是一个 R2 未触及但影响论文基础的问题——如果 ISR 不追踪语义质量，\"structural degeneration\" 的诊断意义需要重新论证。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2563 · 2026-05-25T04:51:33.773522+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4169
}
```

</details>

---


### Assistant

_source line 2564 · 2026-05-25T04:51:40.892047+00:00_

交叉回应已提交给 Review Director。对 R2 的 6 个问题逐条做了 [AGREE] 回应，并附上了与我自己审稿意见的重叠/差异对比表。核心共识：诊断贡献有价值，但统计方法、泛化声称和 ProofFOL 证据是两位 reviewer 的共同关切。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 72

## Round 72

26 recorded events


### User

_source line 2565 · 2026-05-25T04:55:15.009481+00:00_

[Round 1 审稿请求]:
## 交叉分享任务 — 对 Reviewer 2 审稿意见的逐条回应

请对以下 Reviewer 2 的审稿意见进行逐条评价，使用 [AGREE] 或 [REBUT] 标注你的立场，并说明理由。

---

### Reviewer 2 初审意见摘要

**Must-Fix (Critical):**

**R2-N1: Abstract 中跨数据集证据表述与实验结果不匹配**
R2 认为 ProofFOL 上 ISR-as-reward 条件的 genuine rate 高于 exec-only (p=0.10)，这实际上**复杂化**而非支撑 "observe-vs-optimize asymmetry" 的主论点。Abstract 中的跨数据集声称具有误导性。这是 R2 认为本文最需要修正的声称。

**R2-N2: 过度推广——从单模型/单数据集得出一般性结论**
论文从 Qwen3-4B 在 FOLIO 上的实验推断出 "any verifiable proxy" 会面临 Goodhart 风险。R2 认为这种从单一模型/数据集到一般性结论的跳跃不合理。（注：论文实际使用 Qwen3-4B，不是 1B。）

**Should-Fix (Warning):**

**R2-W1: 统计效力不足**
与你的 N2 高度重叠。5 seeds 的 95% CI [11.8%, 88.1%] 无信息。R2 补充：seeds 45-46 是 post-hoc 添加的（Section 4.3），引入分析偏差风险。

**R2-W2: 缺少与 PRM 的 Goodhart susceptibility 对比讨论**
§2 引用 PRM 文献但仅作背景。核心 claim 是 structural rewards 被优化时失效——PRM 的 step-level signal 是否面临同样风险？R2 认为这一对比会强化论文定位。

**R2-W3: Seed 43 解码协议不一致**
与你的 W1 重叠。Seed 43 使用 nucleus sampling (T=0.7) 而非 greedy decoding。

**R2-W4: ISR/ISR* 术语使用不一致**
§3.2 定义 ISR*（proved-only ISR）并声明 "We report ISR* throughout"，但后续行文中频繁使用 ISR 而非 ISR*。

**R2-MR1: 缺失引用 Krakovna et al. (2020) "Specification gaming examples in AI"**

**R2 Overall Assessment: 3.5 Borderline Conference**
**R2 Excitement: 3/5**（认为 "observe-vs-optimize" 本质上是 Goodhart's Law 的领域实例化，概念贡献有限）

---

请对每个 R2 审稿要点逐条 [AGREE] 或 [REBUT]，并在最后总结你与 R2 的主要共识与分歧。

**论文文件**:
- TeX 源码: `projects/solver-trace-ablation/docs/paper/` 目录
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_34/submitted.pdf`

**目标 Venue**: EMNLP 2026 (ARR)
- Long paper: 正文 8 页限制（不含 references）
- Limitations 为强制章节，不计入页限
- Overall Assessment: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2566 · 2026-05-25T04:55:38.484234+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR\\*|ISR\\\\\\*|\\\\textsc\\{isr\\}\\*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR\\*|ISR\\\\\\*|\\\\textsc\\{isr\\}\\*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2567 · 2026-05-25T04:55:38.986942+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2568 · 2026-05-25T04:55:39.891167+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Krakovna|specification gaming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Krakovna|specification gaming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 2569 · 2026-05-25T04:55:40.343357+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:10:Specification gaming~\citep{krakovna2020specification} and Goodhart's Law~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} are established across RL from human feedback (RLHF)~\citep{gao-reward-overoptimization} and logical formalization~\citep{bondarenko-spec-gaming, kim-game-formalization}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:8:  Specification Gaming in Reasoning Models}}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:168:\bibitem[{Krakovna et~al.(2020)Krakovna, Uesato, Mikulik, Rahtz, Everitt,
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:169:  Kumar, Kenton, Leike, and Legg}]{krakovna2020specification}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:170:Victoria Krakovna, Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:172:\newblock Specification gaming: The flip side of {AI} ingenuity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:238:  Specification Gaming in Reasoning Models}}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.log:602:\OT1/cmr/m/n/10.95 Spec-i-fi-ca-tion gam-ing ([][]Krakovna et al.[][],
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib:111:  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib:293:@misc{krakovna2020specification,
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/do
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-25T04:55:40.846111+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PRM|process reward|step-level",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PRM|process reward|step-level",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-25T04:55:40.947624+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:17:\paragraph{Process rewards and reward design.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex:18:Process reward models~\citep{lightman-verify-step, setlur2025rewarding, cui2025prime, cobbe2021training, uesato2022solving} supervise intermediate steps; \citet{sullivan2025grpo-prm} show GRPO implicitly implements process reward. Classical reward shaping~\citep{ng1999policy, gao-effective-rl-reward} guarantees policy invariance only under potential-based transforms---ISR violates this condition.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:267:  Verification: Verifiable Process Reward Models for Structured Reasoning}}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:309:\bibitem[{Sullivan and Koller(2025)}]{sullivan2025grpo-prm}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.bbl:312:  process reward model}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:9:Our taxonomy of structural hacking modes may inform the design of process reward models in solver-backed settings, where step-level rewards face analogous component-necessity considerations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:9:Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to solver-backed settings, while inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} identifies gaming post-hoc but provides no training-time structural signal.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bi
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2572 · 2026-05-25T04:55:47.728652+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR\\\\\\*|proved-only ISR|denoted ISR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR\\\\\\*|proved-only ISR|denoted ISR",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2573 · 2026-05-25T04:55:48.220813+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:56:We report \emph{proved-only} ISR (denoted ISR$^*$) throughout to avoid conflating component necessity with prove rate.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:90:\caption{Goodhart landscape across reward conditions. PR = prove rate; ISR$^*$ = proved-only ISR; TS = tautological shortcut; CE = conclusion embedding; N-H = non-hacking (upper bound on genuine reasoning). Multi-seed rows: pooled TS/CE/N-H; PR/ISR$^*$ as mean$\pm$std. $^\dagger$Seed~42 only. $^\ddagger$Premise-count-matched (\S\ref{sec:goodhart}). $^\P$FN-corrected (\S\ref{app:h8}). $^\S$Seed-dependent (s43: 38.3\%). Per-seed data: Table~\ref{tab:fol-detailed}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:552:ISR values are proved-only ISR$^*$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:556:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:630:\caption{Detailed per-seed results: Prolog (SWI-Prolog 8.4.2). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H\ = percentage among proved samples.  ``---'' indicates data not available.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:714:\caption{Per-seed results at $\beta{=}0.2$ and $\beta{=}0.3$ (FOL). PR = prove rate, ISR$^*$ = proved-only ISR, TS/CE/N-H = percentage among proved samples.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 492
}
```

</details>

---


### Tool call

_source line 2574 · 2026-05-25T04:55:48.722727+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textrm\\{ISR\\}|\\\\textsc\\{isr\\}|\\\\mathrm\\{ISR\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textrm\\{ISR\\}|\\\\textsc\\{isr\\}|\\\\mathrm\\{ISR\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2575 · 2026-05-25T04:55:48.773446+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-25T04:55:56.015324+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR[^*$]|(?<!proved-only )ISR(?!\\$\\^)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR[^*$]|(?<!proved-only )ISR(?!\\$\\^)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-25T04:55:56.266581+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2578 · 2026-05-25T04:55:57.271857+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " ISR ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "count",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": " ISR ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "count",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-25T04:55:57.775826+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:19
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:50
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:4
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:9

Found 85 total occurrences across 6 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2580 · 2026-05-25T04:55:58.127371+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ISR\\$\\^\\*\\$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
  "output_mode": "count",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ISR\\$\\^\\*\\$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "count",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-25T04:55:58.328464+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:3
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex:2
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex:1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:11

Found 17 total occurrences across 4 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-25T04:56:07.695521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2583 · 2026-05-25T04:56:07.797106+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and reinforcement learning (RL) optimizers exploit this indifference.
3	We apply leave-one-out ablation to GRPO-trained formalizations---\emph{Solver Trace Ablation} (STA)---testing whether each component is individually necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
4	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B experiments, the resulting Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming, demonstrating that the Goodhart effect can occur under standard training conditions; 2 of 5 retain genuine reasoning), but the \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families---confirmed by cross-logic (Prolog) replication and supported by exploratory cross-benchmark (ProofFOL) evidence: structural proxies for formalization integrity are easier to observe than to optimize.\end{abstract}
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-25T04:56:15.842505+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ProofFOL.*genuine|ProofFOL.*p=|ProofFOL.*asymmetry",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ProofFOL.*genuine|ProofFOL.*p=|ProofFOL.*asymmetry",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 2585 · 2026-05-25T04:56:16.396394+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:111:\textbf{ProofFOL ISR ($\beta{=}0.1$): dataset-dependent asymmetry.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex:112:ISR reward on ProofFOL produces directionally higher genuine rates than exec-only ($p{=}0.10$, exploratory; Table~\ref{tab:prooffol-detailed}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:211:The ProofFOL genuine-rate permutation test ($p{=}0.10$) belongs to a separate hypothesis family (different dataset, independent experimental design) and does not reach significance even without correction; it is reported as an exploratory observation throughout.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex:663:\caption{Detailed per-seed results: ProofFOL (Prover9). PR$_{\text{f50}}$ = mean prove rate over final 50 steps. TS = tautological shortcutting (\S\ref{sec:taxonomy}), CE = conclusion embedding, Genuine = classified as neither TS nor CE. Stable convergence: PR$_{\text{f50}}{>}0.90$.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Grep",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2586 · 2026-05-25T04:56:16.698104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
  "offset": "75",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex",
    "offset": "75",
    "limit": "40"
  }
}
```

</details>

---


### Tool result

_source line 2587 · 2026-05-25T04:56:16.748933+00:00_

75	This complexity dependence is a mechanistic insight, not a confound: the compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
76	The failure of ISR-as-reward demonstrates that structural diagnostics cannot be naively repurposed as training objectives---a finding that applies to any LOO-based metric in solver-verified settings.
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{figures/fig_premise_bins.pdf}
81	\caption{Mode composition by premise count (proved samples, seed~42, $\beta{=}0.1$). TS hacking emerges exclusively under ISR in the 4--6 premise range; Random shows zero TS at any complexity, confirming that ISR's compositional shift is not a premise-count artifact. I\,=\,ISR, R\,=\,Random.}
82	\label{fig:premise-bins}
83	\end{figure}
84	
85	\textbf{Higher doses and temporal dynamics.}
86	Any genuine reasoning under ISR $\beta{=}0.1$ is transient: non-hacking drops from $17\%$ to $2\%$ by 1000 steps as TS escalates (Figure~\ref{fig:training-isr-curves}). %% registry: plan002-b01-s42-1000, plan016-extended-1000-s42
87	Higher doses accelerate collapse: $\beta{=}0.2$ eliminates all non-hacking; $\beta{=}0.3$ destabilizes training itself, producing multi-modal failure~\citep{gao-reward-overoptimization} across both ISR and random conditions (Appendix~\ref{app:beta03}). %% registry: plan002-additive-b02-s42/s43/s44, plan002-additive-b03-s42/s43/s44
88	
89	\subsection{Cross-Domain and Cross-Dataset Evidence}
90	\label{sec:crossdomain}
91	\label{sec:crosslogic}
92	
93	The following results extend the primary findings of \S\ref{sec:diagnostic}--\ref{sec:goodhart} to alternative logic types and dataset families; these cross-domain experiments are exploratory in nature.
94	
95	\begin{figure}[t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/fig4_prolog_comparison.pdf}
98	\caption{Cross-logic results. \textbf{Top}: FOL vs.\ Prolog exec-only $\text{ISR}^*$ across 
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2588 · 2026-05-25T04:57:50.985767+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应（Round 2）\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Abstract 中跨数据集证据表述与实验结果不匹配**\n\n强烈同意，且在验证 TeX 源码后认为此问题比 R2 描述的更严重。\n\nexperiments.tex 第 111-113 行原文：\n> \"ProofFOL ISR (β=0.1): dataset-dependent asymmetry. ISR reward on ProofFOL produces directionally higher genuine rates than exec-only (p=0.10, exploratory). The asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart); on ProofFOL, CE embeds conclusions among many premises, yielding ISR≈0 and rendering ISR reward **effectively corrective**.\"\n\n论文自身在正文中明确承认 ISR-as-reward 在 ProofFOL 上是 **\"effectively corrective\"**——即 ISR 在该数据集上既可观测又可优化，observe-vs-optimize asymmetry 不成立甚至反转。\n\n但 abstract（abstract.tex 第 6 行）的表述是：\n> \"the observe-vs-optimize asymmetry persists across logic types and dataset families—confirmed by cross-logic (Prolog) replication and **supported by** exploratory cross-benchmark (ProofFOL) evidence\"\n\n\"supported by\" 暗示 ProofFOL 提供了同方向的证据，但实际上 ProofFOL 提供的是反方向证据（ISR 在 ProofFOL 上 works）。即使有 \"exploratory\" 修饰词，\"supported by\" 这个措辞构成事实性误导。\n\n正文 Section 4.4 的处理（\"dataset-dependent asymmetry\"）比 abstract 更诚实，但 abstract 是多数 reviewer/reader 首先且可能唯一阅读的部分。\n\n建议：abstract 应改为 \"confirmed by cross-logic (Prolog) replication; exploratory ProofFOL evidence suggests the asymmetry is modulated by dataset-specific hacking geometry\" 或类似表述，明确 ProofFOL 是 boundary condition 而非 supporting evidence。\n\n---\n\n**[AGREE] R2-N2: 从单模型/单数据集得出一般性结论**\n\n同意。与我的 N2（seed 数不足）和 N3（ISR 与语义忠实度脱节）互补。R2 聚焦于实验范围的广度，我聚焦于统计深度，两个维度共同削弱泛化声称。\n\n补充论据：\n1. **Qwen3-8B 的 \"convergence prerequisite\" 解释**（Appendix D.7, p.23）：K=4 产生零梯度，K=8 冷启动停滞。论文推断 \"structural degeneration is a byproduct of successful RL optimization\"。这是 post-hoc 解释且近乎不可证伪——无法区分 (a) 收敛是退化的必要条件 vs. (b) 较大模型的优化景观本质不同 vs. (c) K 值不匹配导致训练失败。从单次失败实验推导因果机制超出了数据支撑。\n2. **FOLIO 评估集仅 100 例**（Section 4.1）：35 True + 25 False + 41 Unknown，数据不公开（R2-W4 也指出）。百分比差异可能由少数样例驱动。\n3. **Section 5 的 \"Practical guidelines\"** 包含 5 条一般性建议（\"Never evaluate by prove rate alone\" 等），但这些建议的适用范围远超 Qwen3-4B + FOLIO 的实验基础。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 统计效力不足**\n\n与我的 N1（池化违反独立性）和 N2（seed 数不足）高度重叠。R2 补充的 seeds 45-46 post-hoc 添加风险是一个我未单独提出的重要细节——如果 seeds 42-44 的结果（2/3 gaming）先被观察，再添加 seeds 45-46 来估计比例，这构成 optional stopping，会膨胀 false positive rate。\n\nAppendix A 提到 \"all conditions share the same fixed training subset\"（p.12），但未说明 ISR β=0.1 的 5 seeds 是否在同一实验设计中同时选定。论文应明确说明 seed 选择是 pre-registered 还是 adaptive。\n\n---\n\n**[AGREE] R2-W2: 缺少与 PRM 的 Goodhart susceptibility 对比讨论**\n\n同意这是一个有意义的缺失。论文在多处提及 PRM（Introduction p.1: \"Process reward models offer finer granularity but require expensive step-level annotations\"; Related Work §2: \"Process reward models supervise intermediate steps; Sullivan and Koller (2025) show GRPO implicitly implements process reward\"; Conclusion p.8: \"step-level rewards face analogous component-necessity considerations\"），但从未系统讨论 PRM 是否面临类似的 Goodhart 风险。\n\n特别是 Conclusion 中 \"step-level rewards face analogous component-necessity considerations\" 这句声称是全文唯一将 ISR-Goodhart 与 PRM 联系的地方，但未提供任何论证。既然论文的核心贡献是\"structural rewards are easier to observe than optimize\"，那么自然的问题是：PRM 的 step-level signal 是否也具有这种不对称性？如果 PRM 也容易被 game（有文献支持），那 ISR 的 Goodhart 发现就不那么 novel；如果 PRM 更 robust，那需要解释为什么 LOO-based 指标特别脆弱。\n\n这不影响接收决定，但一个 §2 段落的对比讨论会显著强化论文定位。\n\n---\n\n**[AGREE] R2-W3: Seed 43 解码协议不一致**\n\n与我的 W1 完全一致。Seed 43 使用 T=0.7 sampling 而非 greedy decoding（footnote 4, p.5），但被纳入所有聚合分析。补充一点：Figure 5 caption 中标注了 \"†s43 FOL uses sampling T=0.7, not strictly comparable\"——这说明作者意识到了问题但仍在可视化中包含了 seed 43，进一步加强了方法论不一致的印象。\n\n---\n\n**[AGREE] R2-W4: ISR/ISR* 术语使用不一致**\n\n通过 grep 验证确认：method.tex 第 56 行声称 \"We report proved-only ISR (denoted ISR*) throughout\"，但实际上全文 \" ISR \"（无星号）出现 **85 次**，而 \"ISR$^*$\" 仅出现 **17 次**（集中在 Table 1 caption、Appendix 表格 caption 和 method.tex 定义处）。\n\n正文行文中几乎全部使用 bare \"ISR\"。这不是小问题——ISR 和 ISR* 的区别在于是否限定为 proved samples，而论文的许多 claim（特别是关于 ISR 随训练步数变化的趋势）取决于这个区分。术语不一致使读者无法确定每个具体 ISR 引用是指 ISR 还是 ISR*。\n\n建议：统一使用 ISR* 或在 method 节声明 \"ISR hereafter refers to ISR* unless otherwise noted\"。\n\n---\n\n**[REBUT] R2-MR1: 缺失引用 Krakovna et al. (2020)**\n\n论文**已引用**此文。related_work.tex 第 10 行：\n> \"Specification gaming (Krakovna et al., 2020) and Goodhart's Law (Manheim and Garrabrant, 2019; ...) are established across RL...\"\n\nreferences.bib 条目 `krakovna2020specification` 完整存在（第 293-295 行）。R2 此条为误判。\n\n---\n\n### 与 R2 的主要共识与分歧\n\n**核心共识**（两位 reviewer 一致）：\n1. **ProofFOL 证据不支持 abstract 的 \"asymmetry persists\" 声称**——R2 分析更深入（可能是反例），我验证了 TeX 源码确认论文自身承认 ISR 在 ProofFOL 上 \"effectively corrective\"\n2. **统计效力不足**——R2 关注 seed 数和 post-hoc 添加风险，我关注池化独立性违反和 seed 级分析缺失\n3. **泛化声称过度**——单模型+单主数据集不支持一般性结论\n4. **Seed 43 评估不一致**——两位 reviewer 独立发现\n5. **总评 3.5 Borderline Conference**——一致\n\n**分歧或互补**：\n1. **ISR 与语义忠实度脱节**（我的 N3）——R2 未提及，但我认为这是论文最根本的方法论弱点（ρ=−0.049, Appendix B）\n2. **Hacking taxonomy 评价**——我原列为优势，R2 列为 W2 质疑其可靠性。在交叉审阅后我采纳 R2 的保留意见（部分模式确实是 seed-specific 偶然产物），但仍认为 CE/TS 两个主导模式的分类有独立描述价值\n3. **ISR/ISR* 术语**——R2 独有发现，我通过 grep 验证确认（85 vs. 17 occurrences）\n4. **Krakovna 引用**——R2 认为缺失，但实际已引用。这是 R2 的唯一误判\n5. **PRM 对比**——R2 独有建议，我同意其价值但认为不影响接收决定",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应（Round 2）\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Abstract 中跨数据集证据表述与实验结果不匹配**\n\n强烈同意，且在验证 TeX 源码后认为此问题比 R2 描述的更严重。\n\nexperiments.tex 第 111-113 行原文：\n> \"ProofFOL ISR (β=0.1): dataset-dependent asymmetry. ISR reward on ProofFOL produces directionally higher genuine rates than exec-only (p=0.10, exploratory). The asymmetry follows from hacking geometry: on FOLIO, TS yields high ISR (regressional Goodhart); on ProofFOL, CE embeds conclusions among many premises, yielding ISR≈0 and rendering ISR reward **effectively corrective**.\"\n\n论文自身在正文中明确承认 ISR-as-reward 在 ProofFOL 上是 **\"effectively corrective\"**——即 ISR 在该数据集上既可观测又可优化，observe-vs-optimize asymmetry 不成立甚至反转。\n\n但 abstract（abstract.tex 第 6 行）的表述是：\n> \"the observe-vs-optimize asymmetry persists across logic types and dataset families—confirmed by cross-logic (Prolog) replication and **supported by** exploratory cross-benchmark (ProofFOL) evidence\"\n\n\"supported by\" 暗示 ProofFOL 提供了同方向的证据，但实际上 ProofFOL 提供的是反方向证据（ISR 在 ProofFOL 上 works）。即使有 \"exploratory\" 修饰词，\"supported by\" 这个措辞构成事实性误导。\n\n正文 Section 4.4 的处理（\"dataset-dependent asymmetry\"）比 abstract 更诚实，但 abstract 是多数 reviewer/reader 首先且可能唯一阅读的部分。\n\n建议：abstract 应改为 \"confirmed by cross-logic (Prolog) replication; exploratory ProofFOL evidence suggests the asymmetry is modulated by dataset-specific hacking geometry\" 或类似表述，明确 ProofFOL 是 boundary condition 而非 supporting evidence。\n\n---\n\n**[AGREE] R2-N2: 从单模型/单数据集得出一般性结论**\n\n同意。与我的 N2（seed 数不足）和 N3（ISR 与语义忠实度脱节）互补。R2 聚焦于实验范围的广度，我聚焦于统计深度，两个维度共同削弱泛化声称。\n\n补充论据：\n1. **Qwen3-8B 的 \"convergence prerequisite\" 解释**（Appendix D.7, p.23）：K=4 产生零梯度，K=8 冷启动停滞。论文推断 \"structural degeneration is a byproduct of successful RL optimization\"。这是 post-hoc 解释且近乎不可证伪——无法区分 (a) 收敛是退化的必要条件 vs. (b) 较大模型的优化景观本质不同 vs. (c) K 值不匹配导致训练失败。从单次失败实验推导因果机制超出了数据支撑。\n2. **FOLIO 评估集仅 100 例**（Section 4.1）：35 True + 25 False + 41 Unknown，数据不公开（R2-W4 也指出）。百分比差异可能由少数样例驱动。\n3. **Section 5 的 \"Practical guidelines\"** 包含 5 条一般性建议（\"Never evaluate by prove rate alone\" 等），但这些建议的适用范围远超 Qwen3-4B + FOLIO 的实验基础。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 统计效力不足**\n\n与我的 N1（池化违反独立性）和 N2（seed 数不足）高度重叠。R2 补充的 seeds 45-46 post-hoc 添加风险是一个我未单独提出的重要细节——如果 seeds 42-44 的结果（2/3 gaming）先被观察，再添加 seeds 45-46 来估计比例，这构成 optional stopping，会膨胀 false positive rate。\n\nAppendix A 提到 \"all conditions share the same fixed training subset\"（p.12），但未说明 ISR β=0.1 的 5 seeds 是否在同一实验设计中同时选定。论文应明确说明 seed 选择是 pre-registered 还是 adaptive。\n\n---\n\n**[AGREE] R2-W2: 缺少与 PRM 的 Goodhart susceptibility 对比讨论**\n\n同意这是一个有意义的缺失。论文在多处提及 PRM（Introduction p.1: \"Process reward models offer finer granularity but require expensive step-level annotations\"; Related Work §2: \"Process reward models supervise intermediate steps; Sullivan and Koller (2025) show GRPO implicitly implements process reward\"; Conclusion p.8: \"step-level rewards face analogous component-necessity considerations\"），但从未系统讨论 PRM 是否面临类似的 Goodhart 风险。\n\n特别是 Conclusion 中 \"step-level rewards face analogous component-necessity considerations\" 这句声称是全文唯一将 ISR-Goodhart 与 PRM 联系的地方，但未提供任何论证。既然论文的核心贡献是\"structural rewards are easier to observe than optimize\"，那么自然的问题是：PRM 的 step-level signal 是否也具有这种不对称性？如果 PRM 也容易被 game（有文献支持），那 ISR 的 Goodhart 发现就不那么 novel；如果 PRM 更 robust，那需要解释为什么 LOO-based 指标特别脆弱。\n\n这不影响接收决定，但一个 §2 段落的对比讨论会显著强化论文定位。\n\n---\n\n**[AGREE] R2-W3: Seed 43 解码协议不一致**\n\n与我的 W1 完全一致。Seed 43 使用 T=0.7 sampling 而非 greedy decoding（footnote 4, p.5），但被纳入所有聚合分析。补充一点：Figure 5 caption 中标注了 \"†s43 FOL uses sampling T=0.7, not strictly comparable\"——这说明作者意识到了问题但仍在可视化中包含了 seed 43，进一步加强了方法论不一致的印象。\n\n---\n\n**[AGREE] R2-W4: ISR/ISR* 术语使用不一致**\n\n通过 grep 验证确认：method.tex 第 56 行声称 \"We report proved-only ISR (denoted ISR*) throughout\"，但实际上全文 \" ISR \"（无星号）出现 **85 次**，而 \"ISR$^*$\" 仅出现 **17 次**（集中在 Table 1 caption、Appendix 表格 caption 和 method.tex 定义处）。\n\n正文行文中几乎全部使用 bare \"ISR\"。这不是小问题——ISR 和 ISR* 的区别在于是否限定为 proved samples，而论文的许多 claim（特别是关于 ISR 随训练步数变化的趋势）取决于这个区分。术语不一致使读者无法确定每个具体 ISR 引用是指 ISR 还是 ISR*。\n\n建议：统一使用 ISR* 或在 method 节声明 \"ISR hereafter refers to ISR* unless otherwise noted\"。\n\n---\n\n**[REBUT] R2-MR1: 缺失引用 Krakovna et al. (2020)**\n\n论文**已引用**此文。related_work.tex 第 10 行：\n> \"Specification gaming (Krakovna et al., 2020) and Goodhart's Law (Manheim and Garrabrant, 2019; ...) are established across RL...\"\n\nreferences.bib 条目 `krakovna2020specification` 完整存在（第 293-295 行）。R2 此条为误判。\n\n---\n\n### 与 R2 的主要共识与分歧\n\n**核心共识**（两位 reviewer 一致）：\n1. **ProofFOL 证据不支持 abstract 的 \"asymmetry persists\" 声称**——R2 分析更深入（可能是反例），我验证了 TeX 源码确认论文自身承认 ISR 在 ProofFOL 上 \"effectively corrective\"\n2. **统计效力不足**——R2 关注 seed 数和 post-hoc 添加风险，我关注池化独立性违反和 seed 级分析缺失\n3. **泛化声称过度**——单模型+单主数据集不支持一般性结论\n4. **Seed 43 评估不一致**——两位 reviewer 独立发现\n5. **总评 3.5 Borderline Conference**——一致\n\n**分歧或互补**：\n1. **ISR 与语义忠实度脱节**（我的 N3）——R2 未提及，但我认为这是论文最根本的方法论弱点（ρ=−0.049, Appendix B）\n2. **Hacking taxonomy 评价**——我原列为优势，R2 列为 W2 质疑其可靠性。在交叉审阅后我采纳 R2 的保留意见（部分模式确实是 seed-specific 偶然产物），但仍认为 CE/TS 两个主导模式的分类有独立描述价值\n3. **ISR/ISR* 术语**——R2 独有发现，我通过 grep 验证确认（85 vs. 17 occurrences）\n4. **Krakovna 引用**——R2 认为缺失，但实际已引用。这是 R2 的唯一误判\n5. **PRM 对比**——R2 独有建议，我同意其价值但认为不影响接收决定",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-25T04:57:54.955938+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3970
}
```

</details>

---


### Assistant

_source line 2590 · 2026-05-25T04:58:01.742610+00:00_

交叉回应已提交。主要结论：

- R2 的 6 个要点中 **5 个 AGREE**（N1、N2、W1-W4），1 个 **REBUT**（MR1，Krakovna 已被引用）
- R2-N1 是最有价值的发现——我验证了 TeX 源码，确认论文自身承认 ISR 在 ProofFOL 上 "effectively corrective"，与 abstract 的 "asymmetry persists across dataset families" 直接矛盾
- ISR/ISR* 术语不一致通过 grep 量化确认（85 vs. 17 occurrences）
- 两位 reviewer 总评一致：3.5 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 73

## Round 73

74 recorded events


### User

_source line 2591 · 2026-05-25T21:17:30.711026+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。

## 论文信息
- 标题：Observe but Don't Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning
- 论文路径：`projects/solver-trace-ablation/docs/paper/main.tex`
- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf`
- 目标 Venue：**EMNLP 2026**（Long Paper，ARR 统一审稿）
- ARR 投稿截止：2026-05-25
- 页数限制：正文 ≤ 8 页，参考文献不限，Limitations 不计入页数
- 模板：ACL `[review]`
- 匿名规则：Double-blind

## 你的审查侧重

请重点审查以下方面：

1. **方法设计**（§3）：
   - STA/ISR 的定义是否严谨？LOO ablation 的 independence assumption 是否被充分讨论？
   - ISR 作为 Shapley value 的 restriction 是否合理？局限性是否被充分承认？
   - 六个 reward condition 的实验设计是否合理？控制变量是否充分？

2. **实验有效性**（§4）：
   - 统计方法是否恰当？3-5 个 seed 的样本量是否足以支撑论文的 claims？
   - Premise-count confound 的处理是否充分？1.06× 的 matched comparison 是否削弱了核心论点？
   - Seed 43 使用 sampling (T=0.7) 而非 greedy decoding，这个 exception 对结果的影响？
   - Cross-dataset (ProofFOL) 结果 p=0.10 被标记为 exploratory——是否过度声称？
   - Qwen3-8B 不收敛的结果如何解读？是否真的支持 "degeneration requires convergence"？
   - Hacking mode classifier 的 precision/recall 是否可靠？

3. **Claims vs Evidence 对齐**：
   - 标题 "Observe but Don't Optimize" 的概括性是否超出了实验证据的范围？
   - Abstract 中的 claims 是否都有实验支撑？
   - Discussion 中的 5 条 practical guidelines 是否都有充分的实验基础？

4. **可复现性**：
   - 实验细节是否足够详细以支持复现？
   - 代码/数据链接是否提供？匿名化是否合规？

请输出完整审稿意见，包含 Summary、Strengths、Weaknesses（按严重程度排序）、Questions、Minor Issues。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2592 · 2026-05-25T21:17:42.657384+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
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

_source line 2593 · 2026-05-25T21:17:42.657864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2594 · 2026-05-25T21:17:47.529124+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 2595 · 2026-05-25T21:17:48.187056+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "1-8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "1-8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2596 · 2026-05-25T21:17:55.426016+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and scoring criteria:

## Three-Score System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Scoring Criteria

**Soundness**: Soundness scores must be justified by the text of the review.

**Overall Recommendation**: The overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7896
}
```

</details>

---


### Tool result

_source line 2597 · 2026-05-25T21:17:57.108965+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 857.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 426.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 416.7}], \"total_pages\": 23, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8921
}
```

</details>

---


### Tool call

_source line 2598 · 2026-05-25T21:18:02.331343+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring scales (especially for soundness, excitement, overall assessment), and detailed descriptions for each score level. List all dimensions reviewers need to evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring scales (especially for soundness, excitement, overall assessment), and detailed descriptions for each score level. List all dimensions reviewers need to evaluate."
  }
}
```

</details>

---


### Tool call

_source line 2599 · 2026-05-25T21:18:03.287408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 2600 · 2026-05-25T21:18:03.894390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 2601 · 2026-05-25T21:18:04.297915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 2602 · 2026-05-25T21:18:04.854574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1567
}
```

</details>

---


### Tool call

_source line 2603 · 2026-05-25T21:18:04.855036+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 2604 · 2026-05-25T21:18:06.870495+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2976
}
```

</details>

---


### Tool result

_source line 2605 · 2026-05-25T21:18:07.225125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2927
}
```

</details>

---


### Tool result

_source line 2606 · 2026-05-25T21:18:07.527135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2672
}
```

</details>

---


### Tool result

_source line 2607 · 2026-05-25T21:18:09.385978+00:00_

# ACL Rolling Review Form: Complete Evaluation Framework

## Core Review Fields

1. **Paper Summary** – Description of paper topic and content
2. **Summary of Strengths** – Reasons supporting publication at selective venues
3. **Summary of Weaknesses** – Concerns prioritizing other papers (numbered format requested)
4. **Comments/Suggestions/Typos** – Additional improvement recommendations

## Evaluation Dimensions & Scoring Scales

### Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct"
- **4**: "Quite sure" with unlikely but possible oversights
- **3**: "Pretty sure" but may have missed details
- **2**: "Willing to defend" but likely missed elements
- **1**: Outside expertise area or incomprehensible work

### Soundness (1-5 scale with half-points)
Assesses scientific rigor, claim support, and methodological validity:
- **5**: "One of the most thorough" studies observed
- **4**: "Sufficient support" with optional enhancements
- **3**: "Acceptable" with minor gaps
- **2**: "Major technical/methodological problems"
- **1**: "Not sufficiently thorough" for publication

### Excitement (1-5 scale with half-points)
Measures subjective appeal through innovation, impact, or relevance:
- **5**: "Highly Exciting" – would recommend to others
- **4**: "Exciting" – notable merit
- **3**: "Interesting" – conditional engagement
- **2**: "Potentially Interesting" – limited personal resonance
- **1**: "Not Exciting" – lacks community relevance

### Overall Assessment (1-5 scale with half-points)
Publication recommendation trajectory:
- **5**: Consider for Award consideration
- **4**: Conference acceptance
- **3**: Findings track acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Supplementary Dimensions

**Limitations & Societal Impact** – Discussion adequacy evaluation

**Ethical Concerns** – ACL code alignment assessment

**Reproducibility** (1-5) – Result recreation feasibility

**Datasets** (1-5) – Released data utility rating

*
…[truncated 98 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7054
}
```

</details>

---


### Tool call

_source line 2608 · 2026-05-25T21:18:14.215024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 2609 · 2026-05-25T21:18:14.668241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 2610 · 2026-05-25T21:18:14.972349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool call

_source line 2611 · 2026-05-25T21:18:14.973052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 2612 · 2026-05-25T21:18:16.028378+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 2613 · 2026-05-25T21:18:16.029449+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 2614 · 2026-05-25T21:18:16.131028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 2615 · 2026-05-25T21:18:17.188046+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "9-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "9-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2616 · 2026-05-25T21:18:17.241551+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool result

_source line 2617 · 2026-05-25T21:18:18.752111+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 594.3}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 545.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.8}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 413.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.0}], \"total_pages\": 23, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_
…[truncated 55 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1564
}
```

</details>

---


### Tool call

_source line 2618 · 2026-05-25T21:18:22.471899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 2619 · 2026-05-25T21:18:23.126724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 2620 · 2026-05-25T21:18:23.932731+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool call

_source line 2621 · 2026-05-25T21:18:23.933362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 2622 · 2026-05-25T21:18:24.587912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 2623 · 2026-05-25T21:18:24.840011+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1713
}
```

</details>

---


### Tool call

_source line 2624 · 2026-05-25T21:18:24.841252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 2625 · 2026-05-25T21:18:25.847580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1914
}
```

</details>

---


### Tool call

_source line 2626 · 2026-05-25T21:18:25.848174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 2627 · 2026-05-25T21:18:26.383245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1795
}
```

</details>

---


### Tool call

_source line 2628 · 2026-05-25T21:18:26.383679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 2629 · 2026-05-25T21:18:26.619859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1778
}
```

</details>

---


### Tool call

_source line 2630 · 2026-05-25T21:18:26.620314+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 2631 · 2026-05-25T21:18:28.432761+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2584
}
```

</details>

---


### Tool result

_source line 2632 · 2026-05-25T21:18:28.937679+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2553
}
```

</details>

---


### Tool result

_source line 2633 · 2026-05-25T21:18:29.090208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2469
}
```

</details>

---


### Tool call

_source line 2634 · 2026-05-25T21:18:34.495028+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
  "project": "solver-trace-ablation",
  "pages": "17-23",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/submitted.pdf",
    "project": "solver-trace-ablation",
    "pages": "17-23",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 2635 · 2026-05-25T21:18:35.097780+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 430.2}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 148.0}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 254.1}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 259.3}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 547.8}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 499.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 209.7}], \"total_pages\": 23, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2636 · 2026-05-25T21:18:37.761049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p17.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 2637 · 2026-05-25T21:18:38.113837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p18.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-25T21:18:39.278189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p19.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 2639 · 2026-05-25T21:18:39.583544+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1822
}
```

</details>

---


### Tool result

_source line 2640 · 2026-05-25T21:18:39.588039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1474
}
```

</details>

---


### Tool call

_source line 2641 · 2026-05-25T21:18:39.588802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p20.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool call

_source line 2642 · 2026-05-25T21:18:40.144162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p21.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 2643 · 2026-05-25T21:18:40.550170+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1271
}
```

</details>

---


### Tool call

_source line 2644 · 2026-05-25T21:18:40.550608+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p22.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool call

_source line 2645 · 2026-05-25T21:18:41.161444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p23.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_35/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 2646 · 2026-05-25T21:18:41.469881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1881
}
```

</details>

---


### Tool result

_source line 2647 · 2026-05-25T21:18:43.934644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3790
}
```

</details>

---


### Tool result

_source line 2648 · 2026-05-25T21:18:43.935898+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3385
}
```

</details>

---


### Tool result

_source line 2649 · 2026-05-25T21:18:43.937574+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2776
}
```

</details>

---


### Tool call

_source line 2650 · 2026-05-25T21:18:49.513178+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2651 · 2026-05-25T21:18:50.066914+00:00_

1	\begin{abstract}
2	Neurosymbolic reasoning pipelines evaluate formalizations by execution alone, treating all successful proofs as equal.
3	This single-criterion reward conflates genuine derivation with structural shortcuts: embedding the conclusion among the premises proves just as reliably, and reinforcement learning (RL) optimizers exploit the indifference.
4	We apply leave-one-out ablation to Group Relative Policy Optimization (GRPO)-trained formalizations, \emph{Solver Trace Ablation} (STA), to test whether each component is necessary for proof success, and characterize structural degeneration under six reward conditions via the resulting \emph{Intensional Structural Reward} (ISR).
5	ISR reveals that prove-rate gains conceal a compositional shift toward hacking modes, but ISR occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
6	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
7	In our Qwen3-4B experiments, the Goodhart effect is seed-dependent (3 of 5 seeds converge to gaming under standard training conditions; 2 retain genuine reasoning), and the \emph{observe-vs-optimize asymmetry} persists across logic types, confirmed by cross-logic (Prolog) replication.
8	Cross-dataset (ProofFOL) evidence suggests dataset-dependent boundary conditions: structural proxies for formalization integrity are easier to observe than to optimize\footnote{Code and data are available at \url{https://anonymous.4open.science/r/solver-trace-ablation-CB70/}.}.\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2652 · 2026-05-25T21:18:50.067265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2653 · 2026-05-25T21:18:50.118874+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity} (Figure~\ref{fig:sta-overview}a): a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation set (100 examples) contains 34 True, 25 False, and 41 Unknown labels, with only True-labeled examples admitting valid proofs (theoretical PR ceiling ${\sim}34\%$).
11	Exec-only GRPO reaching $\text{PR}{=}93\%$ (\S\ref{sec:diagnostic}), nearly $3\times$ this ceiling, confirms the solver accepts formalizations for nominally unprovable examples, constituting direct evidence of structural gaming independent of ISR.
12	
13	\subsection{Solver Trace Ablation (STA)}
14	\label{sec:sta}
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{figures/fig1_sta_overview.pdf}
19	\caption{STA overview. \textbf{(a)}~The formalization pipeline: an LLM translates natural-language (NL) premises into formal logic, verified by an external solver. \textbf{(b)}~STA removes each component in turn and re-runs the solver; the fraction of necessary components yields ISR. \textbf{(c)}~Applied post-hoc, ISR detects structural hacking; repurposed as reward, it triggers a Goodhart effect where tautological shortcuts (TS) achieve $\text{ISR}{=}1$ by construction.}
20	\label{fig:sta-overview}
21	\end{figure*}
22	
23	STA tests whether each component of a proved formalization is individually necessa
…[truncated 7351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2654 · 2026-05-25T21:18:53.935777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2655 · 2026-05-25T21:18:54.590028+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted; full hyperparameters in Table~\ref{tab:hyperparams}) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention; Appendix~\ref{app:prooffol-construction}, Table~\ref{tab:prooffol-vs-folio}); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classi
…[truncated 14314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 2656 · 2026-05-25T21:18:54.690929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-25T21:18:55.092923+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation.
5	When ISR is used post-hoc, it reliably detects that prove-rate gains conceal a compositional shift toward hacking modes: across all converged exec-only seeds, non-hacking rates collapse to ${\leq}6.2\%$ by 1000 steps, despite prove rates exceeding $90\%$.
6	The diagnostic holds across logic types (FOL, Prolog) and dataset families (FOLIO, ProofFOL), confirming that structural degeneration under execution-only reward is a general phenomenon rather than an artifact of a specific formalism.
7	
8	When repurposed as a training reward, ISR produces a seed-dependent Goodhart effect that follows the regressional pattern~\citep{manheim-goodhart-taxonomy}: optimizing ISR shifts the composition of hacking modes (from CE to TS) without reducing their aggregate prevalence.
9	The effect is paradoxical in a precise sense: the same LOO structure that makes ISR informative as a diagnostic also makes it gameable as a reward, because tautological formalizations satisfy the necessity criterion by construction.
10	Cross-logic replication (Prolog) confirms the compositional mode shift; cross-dataset evidence (ProofFOL, $p{=}0.10$) is exploratory (\S\ref{sec:crossdomain}).
11	
12	These findings yield five practical guidelines for GRPO-trained neurosymbolic systems.
13	First, never evaluate by prove rate alone---use ISR and mode breakdown as joint diagnostics, applied post-hoc rather than as reward signals; any dose of ISR-as-reward induces gaming or collapse.
14	Second, report multi-seed results: single-seed evaluation is unreliable when cross-seed variance exceeds the effect size (\S\ref{sec:diagnostic}).
15	Third, treat LOO-based metrics as component-count-biased until premise-count-matched (\S\ref{sec:goodhart}).
16	Fourth, expect conclusion embedding as a GRPO-universal baseline: reward shaping alters its composition, not its prevalence (Ta
…[truncated 614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2658 · 2026-05-25T21:18:55.093342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2659 · 2026-05-25T21:18:55.194042+00:00_

1	\section*{Limitations}
2	
3	Experiments use a single model (Qwen3-4B) with three to five seeds; degeneration patterns may not transfer to other families, and the 3/5 gaming rate (seeds 45--46 added post-hoc) is an existence demonstration, not a prevalence estimate.
4	FOLIO is a relatively small (1,435 examples) synthetic benchmark; generalization to larger or naturalistic corpora is untested.
5	ISR quantifies component necessity, not semantic faithfulness; diagnostic value comes from the mode breakdown, not the scalar alone (Appendix~\ref{app:extended-discussion}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2660 · 2026-05-25T21:18:59.501558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2661 · 2026-05-25T21:18:59.804258+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions.
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\small
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, conditions, and reruns is appro
…[truncated 55956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 2662 · 2026-05-25T21:21:50.034630+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 研究问题新颖且实验设计周到，但核心统计证据薄弱（ISR 标量效应被 premise-count 消解、3-5 seeds 样本量不足、关键比较 n.s.），加上单一模型家族的泛化局限，使得论文的核心 claims 只获得部分支撑。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 方法设计合理但 ISR 标量诊断价值被 premise-count confound 严重削弱（1.06×, p=0.317 n.s.）；ISR vs. Random 非显著（p=0.182）；Seed 43 评估协议不一致 |\n| Excitement | 3.5 / 5 | 研究问题极具时效性（neurosymbolic RL 中的 reward hacking），hacking taxonomy 有独立贡献价值，observe-vs-optimize 框架有概念吸引力 |\n| Reproducibility | 4 / 5 | 匿名代码链接已提供，超参数表详尽（Table 4），算法伪代码清晰；但 Seed 43 的 T=0.7 例外和被删除的 checkpoint（Appendix C.1）降低了完全复现的可能 |\n| Confidence | 4 / 5 | 本人熟悉 RLVR、neurosymbolic reasoning 和 Goodhart 问题；对统计方法和实验设计有充分判断力 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ISR 标量诊断价值在 premise-count 控制后几乎消失，论文核心贡献定位不清\n\n- 具体位置：§4.2 \"Premise-count confound\"、Appendix B \"The premise-count confound\"、Table 1\n- 问题：论文大量篇幅建立 ISR 作为诊断指标的价值（\"214× raw ISR collapse\"），但 §4.2 自行承认 premise-count matched comparison 仅为 1.06×（McNemar p=0.317, n.s.）。这意味着 ISR 标量本身在控制 premise count 后无法区分 exec-only 和 ISR-trained models。论文随后转向\"compositional evidence survives this control\"，但这实际上是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。\n- 为什么影响接收：这动摇了论文的核心贡献定位——如果 ISR 标量不是有效诊断，那 STA 的主要价值是什么？论文需要明确重新定位：STA 的价值在于生成 LOO ablation data 以支持 mode classification，而非 ISR 标量本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 为中心叙事（\"ISR reveals that prove-rate gains conceal...\"），这与实验结果不匹配。\n- 建议修改方向：（1）明确区分 STA-as-procedure（生成 ablation data）和 ISR-as-scalar（汇总为单一分数），承认后者的诊断价值有限；（2）重写 Abstract/Introduction 中以 ISR 为中心的叙述，转向以 mode decomposition 为核心。\n\n**N2** [critical] ISR-as-reward 的 Goodhart 效应缺乏统计支撑：ISR 与 Random 的非 hacking 率差异不显著\n\n- 具体位置：Table 6（Appendix B, Fisher exact test），§4.2\n- 问题：ISR 与 Random 的 non-hacking rate 比较：6.06% vs. 9.5%，Fisher p=0.182，n.s.。这意味着论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的 gaming。论文能证明的是 TS composition shift（p < 10⁻³⁸），但这是关于 hacking 的类型（type），而非数量（amount）。\n- 为什么影响接收：标题 \"Observe but Don't Optimize\" 暗示 ISR 优化会恶化结果，但实际上 ISR 和 Random reward 的 overall hacking rate 没有显著差异。Goodhart 效应的证据局限于 mode composition shift，这是一个有趣但范围更窄的 claim。\n- 建议修改方向：（1）明确将 Goodhart claim 限定为\"compositional Goodhart\"（改变 hacking 类型但不增加 hacking 总量），而非暗示 ISR 优化\"恶化\"了整体结果；（2）在 Abstract 和 Discussion 中反映这一区分。\n\n**N3** [critical] 3-5 seeds 的样本量不足以支撑论文的概率性 claims\n\n- 具体位置：§4.2 \"Seed-dependent outcomes\"，Limitations\n- 问题：核心 Goodhart claim 基于 3-5 个 seeds（Qwen3-4B）。3/5 seeds gaming 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]，这个区间几乎无信息量。Seeds 45-46 是 post-hoc 添加的（Appendix Table 9 脚注 ◇），使 3/5 统计量不是来自单一预注册实验。\n- 为什么影响接收：论文试图建立 \"seed-dependent Goodhart effect\" 作为一个稳健发现，但 5 seeds 的样本量使得任何关于 Goodhart 发生概率的声称都不可靠。作为 existence proof（\"Goodhart 可以发生\"）是足够的，但论文的叙述超越了 existence proof（例如 \"3 of 5 seeds converge to gaming\"暗示约60%的概率）。\n- 建议修改方向：（1）将 seed-dependent 结果定位为 existence demonstration 而非 prevalence estimate（Limitations 中已有此措辞，但正文叙述未充分反映）；（2）增加 seeds 数量，或至少讨论需要多少 seeds 才能可靠估计 Goodhart 概率。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 评估协议不一致，影响多个关键结论\n\n- 具体位置：§4.1 脚注 2，Appendix A \"Evaluation exception\"，Appendix D.6\n- 问题：Seed 43 使用 nucleus sampling（T=0.7）而非 greedy decoding，原因是\"greedy-mode degeneration\"。这个例外有多层影响：\n  （a）Random β=0.1 的 TS 率被 s43 主导（s43: 38.3%, s42/s44: 0%），如果排除 s43，Random 条件下几乎无 TS，使 ISR vs Random 的 composition shift 更加显著——但同时暗示 Random 条件下的 TS 可能是 sampling artifact；\n  （b）s43 被包含在 3-seed pooled 统计中，N=2 sensitivity analysis 放在 Appendix，但主表和图用的是 3-seed 数据；\n  （c）论文未解释为什么 greedy-mode degeneration 本身不是一个值得研究的发现。\n- 建议：（1）在主文中更显著地标记 s43 的协议差异（不仅是脚注）；（2）讨论 greedy-mode degeneration 的含义——这是否意味着模型已经过度 collapse 到 greedy 无法产生有效输出？\n\n**W2** [warning] 标题和 Abstract 的概括性超出实验证据范围\n\n- 具体位置：标题、Abstract\n- 问题：\"Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\" 暗示这是关于\"structural rewards\"这一类别的一般性结论，但实验只测试了一种 structural reward（ISR）、一个模型家族（Qwen3）、一个主要基准（FOLIO）。\"Observe but Don't Optimize\" 的建议也仅基于 ISR 的特定失败模式（tautological shortcuts 满足 LOO 结构）。\n- 建议：标题可以更具体，例如 \"LOO-Based Structural Rewards...\"或在 Abstract 中加入限定语。\n\n**W3** [warning] Qwen3-8B 非收敛的因果解读存在混淆变量\n\n- 具体位置：§4.3 \"Cross-scale validation\"，Appendix D.8\n- 问题：8B 不收敛被解读为\"degeneration requires convergence\"，但 8B 配置与 4B 存在多项差异：K=8 vs K=4、effective batch size 16 vs 8、rollout diversity 不同。这些都是混淆变量。8B 不收敛可能仅是超参数未充分调优，而非规模本身的效应。\n- 建议：（1）承认 8B 结论是 correlational 而非 causal；（2）降低 \"convergence threshold\" 的措辞强度。\n\n**W4** [warning] ProofFOL \"dataset-dependent asymmetry\" 的解释是 post-hoc 的\n\n- 具体位置：§4.3 \"ProofFOL ISR (β=0.1)\"\n- 问题：p=0.10 的 ProofFOL 结果被标为 exploratory，但论文仍从中提取了实质性结论（\"ISR reward effectively corrective\"），并提出了基于\"hacking geometry\"的 post-hoc 解释（FOLIO 上 TS → high ISR, ProofFOL 上 CE → low ISR）。这个解释虽有道理但未经独立验证。\n- 建议：更明确地标记这是 hypothesis generation 而非 hypothesis confirmation。\n\n**W5** [warning] Hacking mode classifier recall 未知，non-hacking 率可能被高估\n\n- 具体位置：§4.1，Table 8，Appendix B \"Classifier Validation\"\n- 问题：Classifier precision=100%（152 samples），但 recall 未知。TSb 的发现（12个 obfuscated tautologies 只通过人工检查发现）说明更多 subtle modes 可能被遗漏。论文承认 non-hacking rate 是 upper bound，但在叙述中经常以 \"6% non-hacking\"作为精确数字使用。\n- 建议：在主文使用 non-hacking rate 时一致标记为\"upper bound\"（\"≤6%\"而非\"6%\"）。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 180 words，符合 ≤200 words 限制。\n- 正文约 8 页，符合 EMNLP Long Paper 限制。Limitations 在正文末尾，格式合规。\n- Table 1 exec-only 行仅报告 seed 42（脚注 †），但与其他 3-seed pooled 行并列，容易造成误读。建议在表格行内标注 \"(single seed)\" 而非仅靠脚注。\n- §3.2 \"Not intentional; intensional...\" 脚注位置略尴尬（在段标题上），建议移到正文中。\n- Figure 1 y轴标签 \"ISR* (proved samples only)\" 字号较小，不易辨认。\n- 匿名仓库链接格式正确（anonymous.4open.science），符合 double-blind 要求。\n- Appendix E 声明使用了 Claude (Anthropic) 作为 AI assistant，透明度良好。\n- Discussion 中的 5 条 practical guidelines 整体合理，但 Guideline 4 (\"expect CE as GRPO-universal baseline\") 仅基于一个模型家族的证据，\"universal\" 用词偏强。\n\n---\n\n## 主要优势\n\n1. **研究问题极具时效性和重要性**：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。\n2. **实验设计周到**：六个 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，控制变量比同类工作更充分。\n3. **Hacking taxonomy 有独立贡献**：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）对后续研究有参考价值。\n4. **诚实的自我批评**：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory——这种学术诚实值得肯定。\n5. **Cross-logic replication 增强说服力**：FOL→Prolog 的 replication 展示了三条不同 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），说明 Goodhart 效应在不同逻辑体系中以不同机制复现。\n6. **Composition shift 证据有力**：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。\n\n---\n\n## Questions to Authors\n\nQ1: ISR 标量在 premise-count 控制后效应消失（1.06×, p=0.317），那么 STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文的叙事结构是否需要调整？\n\nQ2: Seed 43 的 \"greedy-mode degeneration\" 具体表现是什么？是 repetitive output、empty output、还是其他形式？这个现象本身是否与 reward hacking 相关？\n\nQ3: 3/5 seeds gaming 的结果中，seeds 45-46 是在观察到 seeds 42-44 结果后添加的。如果再添加 5 个 seeds（47-51），作者预期 gaming 率会是多少？这个问题旨在评估 3/5 的稳健性。\n\nQ4: Discussion 建议 \"never evaluate by prove rate alone\"，但论文同时展示 ISR 标量也不可靠。实践中研究者应该使用什么具体的 evaluation protocol？是否需要人工检查每个证明的结构？\n\nQ5: Shuffled-ISR 控制（87% non-hacking, PR=15%）说明 ISR signal 破坏 + sample-level 对应关系消失后 hacking 大幅减少。但这也可能是 PR 过低导致的——低 PR 意味着更少的 proved samples 可供 hacking。如何排除这个混淆？",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5 / 5 (Borderline Conference)\n**一句话总结**: 研究问题新颖且实验设计周到，但核心统计证据薄弱（ISR 标量效应被 premise-count 消解、3-5 seeds 样本量不足、关键比较 n.s.），加上单一模型家族的泛化局限，使得论文的核心 claims 只获得部分支撑。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3 / 5 | 方法设计合理但 ISR 标量诊断价值被 premise-count confound 严重削弱（1.06×, p=0.317 n.s.）；ISR vs. Random 非显著（p=0.182）；Seed 43 评估协议不一致 |\n| Excitement | 3.5 / 5 | 研究问题极具时效性（neurosymbolic RL 中的 reward hacking），hacking taxonomy 有独立贡献价值，observe-vs-optimize 框架有概念吸引力 |\n| Reproducibility | 4 / 5 | 匿名代码链接已提供，超参数表详尽（Table 4），算法伪代码清晰；但 Seed 43 的 T=0.7 例外和被删除的 checkpoint（Appendix C.1）降低了完全复现的可能 |\n| Confidence | 4 / 5 | 本人熟悉 RLVR、neurosymbolic reasoning 和 Goodhart 问题；对统计方法和实验设计有充分判断力 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ISR 标量诊断价值在 premise-count 控制后几乎消失，论文核心贡献定位不清\n\n- 具体位置：§4.2 \"Premise-count confound\"、Appendix B \"The premise-count confound\"、Table 1\n- 问题：论文大量篇幅建立 ISR 作为诊断指标的价值（\"214× raw ISR collapse\"），但 §4.2 自行承认 premise-count matched comparison 仅为 1.06×（McNemar p=0.317, n.s.）。这意味着 ISR 标量本身在控制 premise count 后无法区分 exec-only 和 ISR-trained models。论文随后转向\"compositional evidence survives this control\"，但这实际上是 hacking mode classification（CE/TS 文本匹配）在做诊断工作，而非 ISR 本身。\n- 为什么影响接收：这动摇了论文的核心贡献定位——如果 ISR 标量不是有效诊断，那 STA 的主要价值是什么？论文需要明确重新定位：STA 的价值在于生成 LOO ablation data 以支持 mode classification，而非 ISR 标量本身。当前 framing 在 Abstract 和 Introduction 中仍以 ISR 为中心叙事（\"ISR reveals that prove-rate gains conceal...\"），这与实验结果不匹配。\n- 建议修改方向：（1）明确区分 STA-as-procedure（生成 ablation data）和 ISR-as-scalar（汇总为单一分数），承认后者的诊断价值有限；（2）重写 Abstract/Introduction 中以 ISR 为中心的叙述，转向以 mode decomposition 为核心。\n\n**N2** [critical] ISR-as-reward 的 Goodhart 效应缺乏统计支撑：ISR 与 Random 的非 hacking 率差异不显著\n\n- 具体位置：Table 6（Appendix B, Fisher exact test），§4.2\n- 问题：ISR 与 Random 的 non-hacking rate 比较：6.06% vs. 9.5%，Fisher p=0.182，n.s.。这意味着论文无法在统计上证明 ISR-as-reward 导致了比 random reward 更多的 gaming。论文能证明的是 TS composition shift（p < 10⁻³⁸），但这是关于 hacking 的类型（type），而非数量（amount）。\n- 为什么影响接收：标题 \"Observe but Don't Optimize\" 暗示 ISR 优化会恶化结果，但实际上 ISR 和 Random reward 的 overall hacking rate 没有显著差异。Goodhart 效应的证据局限于 mode composition shift，这是一个有趣但范围更窄的 claim。\n- 建议修改方向：（1）明确将 Goodhart claim 限定为\"compositional Goodhart\"（改变 hacking 类型但不增加 hacking 总量），而非暗示 ISR 优化\"恶化\"了整体结果；（2）在 Abstract 和 Discussion 中反映这一区分。\n\n**N3** [critical] 3-5 seeds 的样本量不足以支撑论文的概率性 claims\n\n- 具体位置：§4.2 \"Seed-dependent outcomes\"，Limitations\n- 问题：核心 Goodhart claim 基于 3-5 个 seeds（Qwen3-4B）。3/5 seeds gaming 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]，这个区间几乎无信息量。Seeds 45-46 是 post-hoc 添加的（Appendix Table 9 脚注 ◇），使 3/5 统计量不是来自单一预注册实验。\n- 为什么影响接收：论文试图建立 \"seed-dependent Goodhart effect\" 作为一个稳健发现，但 5 seeds 的样本量使得任何关于 Goodhart 发生概率的声称都不可靠。作为 existence proof（\"Goodhart 可以发生\"）是足够的，但论文的叙述超越了 existence proof（例如 \"3 of 5 seeds converge to gaming\"暗示约60%的概率）。\n- 建议修改方向：（1）将 seed-dependent 结果定位为 existence demonstration 而非 prevalence estimate（Limitations 中已有此措辞，但正文叙述未充分反映）；（2）增加 seeds 数量，或至少讨论需要多少 seeds 才能可靠估计 Goodhart 概率。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Seed 43 评估协议不一致，影响多个关键结论\n\n- 具体位置：§4.1 脚注 2，Appendix A \"Evaluation exception\"，Appendix D.6\n- 问题：Seed 43 使用 nucleus sampling（T=0.7）而非 greedy decoding，原因是\"greedy-mode degeneration\"。这个例外有多层影响：\n  （a）Random β=0.1 的 TS 率被 s43 主导（s43: 38.3%, s42/s44: 0%），如果排除 s43，Random 条件下几乎无 TS，使 ISR vs Random 的 composition shift 更加显著——但同时暗示 Random 条件下的 TS 可能是 sampling artifact；\n  （b）s43 被包含在 3-seed pooled 统计中，N=2 sensitivity analysis 放在 Appendix，但主表和图用的是 3-seed 数据；\n  （c）论文未解释为什么 greedy-mode degeneration 本身不是一个值得研究的发现。\n- 建议：（1）在主文中更显著地标记 s43 的协议差异（不仅是脚注）；（2）讨论 greedy-mode degeneration 的含义——这是否意味着模型已经过度 collapse 到 greedy 无法产生有效输出？\n\n**W2** [warning] 标题和 Abstract 的概括性超出实验证据范围\n\n- 具体位置：标题、Abstract\n- 问题：\"Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning\" 暗示这是关于\"structural rewards\"这一类别的一般性结论，但实验只测试了一种 structural reward（ISR）、一个模型家族（Qwen3）、一个主要基准（FOLIO）。\"Observe but Don't Optimize\" 的建议也仅基于 ISR 的特定失败模式（tautological shortcuts 满足 LOO 结构）。\n- 建议：标题可以更具体，例如 \"LOO-Based Structural Rewards...\"或在 Abstract 中加入限定语。\n\n**W3** [warning] Qwen3-8B 非收敛的因果解读存在混淆变量\n\n- 具体位置：§4.3 \"Cross-scale validation\"，Appendix D.8\n- 问题：8B 不收敛被解读为\"degeneration requires convergence\"，但 8B 配置与 4B 存在多项差异：K=8 vs K=4、effective batch size 16 vs 8、rollout diversity 不同。这些都是混淆变量。8B 不收敛可能仅是超参数未充分调优，而非规模本身的效应。\n- 建议：（1）承认 8B 结论是 correlational 而非 causal；（2）降低 \"convergence threshold\" 的措辞强度。\n\n**W4** [warning] ProofFOL \"dataset-dependent asymmetry\" 的解释是 post-hoc 的\n\n- 具体位置：§4.3 \"ProofFOL ISR (β=0.1)\"\n- 问题：p=0.10 的 ProofFOL 结果被标为 exploratory，但论文仍从中提取了实质性结论（\"ISR reward effectively corrective\"），并提出了基于\"hacking geometry\"的 post-hoc 解释（FOLIO 上 TS → high ISR, ProofFOL 上 CE → low ISR）。这个解释虽有道理但未经独立验证。\n- 建议：更明确地标记这是 hypothesis generation 而非 hypothesis confirmation。\n\n**W5** [warning] Hacking mode classifier recall 未知，non-hacking 率可能被高估\n\n- 具体位置：§4.1，Table 8，Appendix B \"Classifier Validation\"\n- 问题：Classifier precision=100%（152 samples），但 recall 未知。TSb 的发现（12个 obfuscated tautologies 只通过人工检查发现）说明更多 subtle modes 可能被遗漏。论文承认 non-hacking rate 是 upper bound，但在叙述中经常以 \"6% non-hacking\"作为精确数字使用。\n- 建议：在主文使用 non-hacking rate 时一致标记为\"upper bound\"（\"≤6%\"而非\"6%\"）。\n\n---\n\n## 小问题（不影响接收）\n\n- Abstract 约 180 words，符合 ≤200 words 限制。\n- 正文约 8 页，符合 EMNLP Long Paper 限制。Limitations 在正文末尾，格式合规。\n- Table 1 exec-only 行仅报告 seed 42（脚注 †），但与其他 3-seed pooled 行并列，容易造成误读。建议在表格行内标注 \"(single seed)\" 而非仅靠脚注。\n- §3.2 \"Not intentional; intensional...\" 脚注位置略尴尬（在段标题上），建议移到正文中。\n- Figure 1 y轴标签 \"ISR* (proved samples only)\" 字号较小，不易辨认。\n- 匿名仓库链接格式正确（anonymous.4open.science），符合 double-blind 要求。\n- Appendix E 声明使用了 Claude (Anthropic) 作为 AI assistant，透明度良好。\n- Discussion 中的 5 条 practical guidelines 整体合理，但 Guideline 4 (\"expect CE as GRPO-universal baseline\") 仅基于一个模型家族的证据，\"universal\" 用词偏强。\n\n---\n\n## 主要优势\n\n1. **研究问题极具时效性和重要性**：在 RLVR 和 neurosymbolic reasoning 交叉领域揭示 Goodhart 效应，对正在部署这类系统的研究者有直接价值。\n2. **实验设计周到**：六个 reward conditions（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, SFT）加 Shuffled-ISR 解混淆控制，控制变量比同类工作更充分。\n3. **Hacking taxonomy 有独立贡献**：8 种 structural degeneration 模式的系统分类（CE, TSa, TSb, PG, Tautological, Repetition, Contradiction, Query-as-fact）对后续研究有参考价值。\n4. **诚实的自我批评**：premise-count confound 的 1.06× 结果被正面呈现而非隐藏，ProofFOL p=0.10 被标为 exploratory——这种学术诚实值得肯定。\n5. **Cross-logic replication 增强说服力**：FOL→Prolog 的 replication 展示了三条不同 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），说明 Goodhart 效应在不同逻辑体系中以不同机制复现。\n6. **Composition shift 证据有力**：TS composition shift（χ²=174.8, p<10⁻³⁸）是论文最强的统计结果，清楚展示了 ISR reward 如何改变 hacking 的类型。\n\n---\n\n## Questions to Authors\n\nQ1: ISR 标量在 premise-count 控制后效应消失（1.06×, p=0.317），那么 STA 的核心价值是 ISR 标量还是 LOO ablation 产生的 per-component data？如果是后者，论文的叙事结构是否需要调整？\n\nQ2: Seed 43 的 \"greedy-mode degeneration\" 具体表现是什么？是 repetitive output、empty output、还是其他形式？这个现象本身是否与 reward hacking 相关？\n\nQ3: 3/5 seeds gaming 的结果中，seeds 45-46 是在观察到 seeds 42-44 结果后添加的。如果再添加 5 个 seeds（47-51），作者预期 gaming 率会是多少？这个问题旨在评估 3/5 的稳健性。\n\nQ4: Discussion 建议 \"never evaluate by prove rate alone\"，但论文同时展示 ISR 标量也不可靠。实践中研究者应该使用什么具体的 evaluation protocol？是否需要人工检查每个证明的结构？\n\nQ5: Shuffled-ISR 控制（87% non-hacking, PR=15%）说明 ISR signal 破坏 + sample-level 对应关系消失后 hacking 大幅减少。但这也可能是 PR 过低导致的——低 PR 意味着更少的 proved samples 可供 hacking。如何排除这个混淆？",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2663 · 2026-05-25T21:21:53.850931+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3816
}
```

</details>

---


### Assistant

_source line 2664 · 2026-05-25T21:22:02.350584+00:00_

审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5（Borderline Conference）**，Soundness 3/5，Excitement 3.5/5。

三个 Must-Fix 问题：
1. ISR 标量诊断价值在 premise-count 控制后消失（1.06×, p=0.317），论文核心贡献定位需要从 ISR 标量转向 mode decomposition
2. ISR vs Random 的非 hacking 率差异不显著（p=0.182），Goodhart claim 应限定为 compositional Goodhart 而非整体恶化
3. 3-5 seeds 样本量不足以支撑概率性 claims，95% CI [11.8%, 88.1%] 几乎无信息量

主要优势是研究问题的时效性、实验设计的多控制组、hacking taxonomy 的独立贡献、以及 TS composition shift 的强统计支撑（χ²=174.8, p<10⁻³⁸）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---


## Round 74

## Round 74

4 recorded events


### User

_source line 2665 · 2026-05-25T21:28:03.508516+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的审稿意见。对每个 Must-Fix 和 Should-Fix 问题，用 **[AGREE]** 表示同意（并简要说明理由），或用 **[REBUT]** 表示反驳（并引用具体 Section/Table/Figure 提供证据）。

---

以下是 Reviewer 2 的完整审稿原文：

**Overall**: 3.5 / 5 (Borderline Conference)

| 维度 | 分数 |
|------|------|
| Soundness | 3.5 / 5 |
| Excitement | 3 / 5 |
| Reproducibility | 4 / 5 |
| Confidence | 4 / 5 |

### Must-Fix 问题

**N1** [critical] 核心发现的统计效力不足——3/5 seed gaming rate
- 5 个 seed 中 3 个出现 gaming (60%)，无法与随机（50%）可靠区分
- Limitations 自称 "existence demonstration" 但 §5 Discussion 做出较强泛化论述
- Claim 强度与证据强度不匹配
- 建议增加至少 10-15 个 seed，或界定为 case study 级别发现

**N2** [critical] 单一模型族限制了可推广性
- 所有主实验基于 Qwen3-4B
- 8B 结果极初步且不同动力学（cold-start failure）
- 标题使用泛化措辞但证据不支持
- 建议增加至少一个非 Qwen 模型族的完整实验

### Should-Fix 问题

**W1** [warning] Observe-vs-optimize 不对称性的理论解释偏浅
- 归因于 "tautological formalizations satisfy necessity criterion by construction"，本质上是 LOO metric 的已知缺陷
- 没有讨论：(a) 这是 LOO 特有还是所有 structural diagnostic 的共性？(b) 是否存在修复 ISR 的方法？
- 建议增加讨论 tautological blind spot 的修复可能性

**W2** [warning] Cross-dataset 验证 (ProofFOL) 的证据有限
- ProofFOL 仅在 exec-only 和 random 条件下运行，无 ISR reward 条件
- 只验证了 "diagnostic 有效" 一半，未验证 "reward 失败" 一半
- 建议补充 ProofFOL 上 ISR β=0.1 实验

**W3** [warning] Abstract 信息密度过高
- ~187 words 内塞入大量技术细节
- observe-vs-optimize asymmetry 被淹没
- 建议简化，聚焦 problem + core finding

**W4** [warning] Contribution C1-C3 的独立性值得商榷
- C1 和 C2 紧密耦合（Goodhart 依赖 ISR，ISR 价值通过 Goodhart 体现）
- C3 是 C2 的扩展
- 建议重组为 2 个核心 contribution

### 新颖性判断
- 方法新颖性有限（LOO ablation 是 standard technique）
- 应用新颖性中等（GRPO-trained neurosymbolic outputs）
- 发现新颖性中等偏上（observe-vs-optimize asymmetry 的具体机制）
- 总体：中等偏上，作为 EMNLP 长文 borderline

### Missing References
1. Chen et al. (2018) "Metamorphic Testing" — LOO ablation 与 metamorphic testing 的概念联系
2. reward-hacking-survey (Wang et al., 2026) 可能在 bib 中但未在正文引用
3. Pan et al. (2023) "Logic-LM" 后续关于 formalization quality 的讨论

### Questions
Q1: 增加到 15-20 seeds 预期 gaming rate 稳定在什么水平？
Q2: 是否尝试过 tautological detection filter 修复 ISR？
Q3: STA 的 n+1 solver call overhead 在实际部署中是否 prohibitive？
Q4: Qwen3-8B cold-start failure 是否暗示 Goodhart effect 是 capacity-dependent 的？

---

请对每个 N1-N2、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2666 · 2026-05-25T21:29:47.391560+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 3/5 seed gaming rate 统计效力不足**\n\n同意核心判断。这与我自己的 N3 高度一致。5 seeds 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]（§4.2），无法与随机区分。补充两点：\n\n1. R2 建议增加到 10-15 seeds，我认为仍可能不足。论文展示了 multi-attractor dynamics（§4.1 \"Cross-seed instability\"），不同 seeds 收敛到不同 hacking modes（s42→CE, s43→Repetition, s44→Tautological）。这种 qualitative divergence 意味着即使 30 seeds 也可能呈现高方差。论文应该明确讨论需要多少 seeds 才能可靠估计 Goodhart 概率，而不是简单增加数量。\n\n2. 论文在 Limitations 中称 \"existence demonstration\"，但正文叙述（§4.2 \"3 of 5 seeds converge to gaming\"、§5 \"the Goodhart effect is seed-dependent\"）的措辞暗示了概率估计。这种 framing 不一致确实是问题。\n\n**[REBUT] R2-N2: 单一模型族限制可推广性**\n\n部分反驳。R2 的核心关切（仅 Qwen3 一个模型族）成立，但低估了论文已有的泛化证据：\n\n1. **Cross-logic replication**（§4.3, Figure 6）：FOL→Prolog 的复制展示了三条独立的 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），跨越了完全不同的逻辑体系和 solver（Prover9 vs. SWI-Prolog）。这不是模型泛化，但证明了 Goodhart 效应在不同 symbolic backend 中复现。\n\n2. **Cross-dataset replication**（§4.3, Table 12）：FOLIO→ProofFOL 展示了不同 dataset structure（3.4× more premises, simpler predicates; Table 2）下的 diagnostic 有效性。\n\n3. **LLaMA-3.2-3B cold-start**（Appendix D.3）和 **non-converging seeds**（Appendix D.5, s45/s52）提供了反面证据：不收敛时不退化。虽然不是完整实验，但支持了 \"degeneration requires successful optimization\" 的 claim。\n\n4. R2 建议增加 \"至少一个非 Qwen 模型族的完整实验\"——我同意这会显著增强论文，但认为这更接近 **Should-Fix** 而非 **Must-Fix**。原因是论文的核心 claim 是关于 ISR/LOO metric 的结构性缺陷（tautological formalizations 满足 LOO necessity by construction, §3.2），这是 metric 层面的问题，不依赖于特定模型。标题措辞确实需要收窄（与我的 W2 一致），但增加模型族不是核心科学贡献成立的前提。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Observe-vs-optimize 理论解释偏浅**\n\n同意。论文将 asymmetry 归因于 \"tautological formalizations satisfy the necessity criterion by construction\"（§3.2, §5），这是一个正确但表层的观察。缺失的讨论包括：\n\n- 这是 LOO 特有的（因为 LOO 只检查 marginal contribution，对 P→P tautology 无法识别）还是所有 structural diagnostic 的共性？例如，full Shapley value（O(2^n) 评估）是否也会被游戏化？论文在 Appendix B 提到 ISR 是 Shapley value 的 (n-1)-coalition restriction，但未讨论 full Shapley 是否免疫。\n- 是否存在修复 ISR 的方法？例如在 LOO 之前增加 tautology pre-filter（检查 premise ≡ conclusion），或结合 semantic faithfulness check。这些讨论对读者的 actionable takeaway 很重要。\n\n**[REBUT] R2-W2: ProofFOL 缺少 ISR reward 条件**\n\nR2 的事实判断有误。论文 **确实在 ProofFOL 上运行了 ISR β=0.1 实验**：\n\n- §4.3 \"ProofFOL ISR (β=0.1): dataset-dependent asymmetry\" 明确报告了结果\n- Table 12（Appendix D, p.20）给出了 ProofFOL ISR β=0.1 的三个 seed 详细数据：s42 (PR=0.35, Genuine=100%), s43 (PR≈0.47, Genuine=30.4%), s44 (PR=0.49, Genuine=100%)\n- Aggregate genuine rate: 76.8% vs exec-only 17.4%（permutation test p=0.10, exploratory）\n\n论文不仅验证了 \"diagnostic 有效\"，还验证了 \"reward 在 ProofFOL 上的效果不同于 FOLIO\"——ISR reward 在 ProofFOL 上表现为 corrective 而非 Goodhart，因为 CE（而非 TS）主导了 hacking geometry，使 ISR≈0 而非 ISR≥0.5。这恰恰展示了 \"reward 失败\" 的 dataset-dependent boundary conditions。\n\nR2 可能因为 ProofFOL 的 ISR 结果未出现在 Table 1（主表）中而遗漏了这部分内容。\n\n**[AGREE] R2-W3: Abstract 信息密度过高**\n\n轻度同意。Abstract 约 180 words，技术上合规（≤200 words），但在有限空间内塞入了 STA 定义、ISR 定义、六种 reward conditions、3/5 seed 统计、cross-logic replication、cross-dataset evidence——导致核心 message（observe-vs-optimize asymmetry）被稀释。不过我认为这是 **写作优化** 问题而非 **学术严谨性** 问题，严重程度低于 R2 的定位。\n\n**[REBUT] R2-W4: Contribution C1-C3 的独立性**\n\n部分反驳。C1-C3 之间确有逻辑耦合，但我认为它们对不同读者群体有独立价值：\n\n- **C1（STA/ISR 作为诊断）**：对部署 neurosymbolic RL 系统的从业者有直接价值，即使他们不关心 Goodhart 理论。§4.1 的 collapse trajectory（ISR 从 0.642 降到 0.003）和 mode breakdown 是独立可用的诊断工具。\n- **C2（Goodhart 效应）**：对 reward design 研究者有价值，展示了 metric → reward 转换的风险。这个发现逻辑上依赖于 C1 的 ISR 定义，但科学贡献是独立的。\n- **C3（Hacking taxonomy）**：8 种 modes 的分类体系（Table 3, Appendix C）有独立的参考价值，后续研究可以直接使用这个分类框架。\n\nR2 建议重组为 2 个 contributions 的方案会损失粒度。当前的 3-contribution 结构与 Introduction §1 末尾的组织（\"(C1) a systematic analysis...; (C2) empirical characterization...; (C3) cross-logic replication...\"）一致且清晰。\n\n---\n\n### 对 R2 Missing References 的回应\n\n1. **Chen et al. (2018) \"Metamorphic Testing\"**：有价值的概念联系。STA 的 LOO ablation 与 metamorphic testing 的 \"变换后预期行为\" 理念确有相似之处，但论文已引用 DeMillo et al. (1978) 和 Jia & Harman (2011) 建立了 mutation testing 的联系（§3.2），coverage 充分。\n2. **reward-hacking-survey (Wang et al., 2026)**：如果确实存在但未引用，应补充。\n3. **Pan et al. (2023) \"Logic-LM\"**：已在 Related Work §2 引用（\"Ye et al., 2023; Pan et al., 2023; Olausson et al., 2023...\"）。R2 可能是指 Logic-LM 的后续关于 formalization quality 的专门讨论，如果是特定后续论文则建议作者检查。\n\n---\n\n### 对 R2 Questions 的补充意见\n\n**Q2（tautological detection filter 修复 ISR）**：这是一个重要方向。论文在 Appendix D.1 测试了 O(1) binary tautology check，结果表明它过于粗糙（所有 ProofFOL 样本都通过）。但未测试将 tautology filter 与 O(n) ISR 结合的方案（例如：先排除 P≡C 的 TS，再计算剩余的 ISR）。这个 gap 值得在 Discussion 中补充。\n\n**Q4（Goodhart effect 是否 capacity-dependent）**：与我的 W3 相关。8B 结果（Appendix D.8）的因果解读被多个混淆变量（K=8 vs K=4, effective batch 16 vs 8）干扰，不能简单归因于 capacity。论文的 \"convergence threshold\" 表述需要降级为 correlational observation。",
  "reviewer_id": "1",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R2-N1: 3/5 seed gaming rate 统计效力不足**\n\n同意核心判断。这与我自己的 N3 高度一致。5 seeds 的 95% Clopper-Pearson CI 为 [11.8%, 88.1%]（§4.2），无法与随机区分。补充两点：\n\n1. R2 建议增加到 10-15 seeds，我认为仍可能不足。论文展示了 multi-attractor dynamics（§4.1 \"Cross-seed instability\"），不同 seeds 收敛到不同 hacking modes（s42→CE, s43→Repetition, s44→Tautological）。这种 qualitative divergence 意味着即使 30 seeds 也可能呈现高方差。论文应该明确讨论需要多少 seeds 才能可靠估计 Goodhart 概率，而不是简单增加数量。\n\n2. 论文在 Limitations 中称 \"existence demonstration\"，但正文叙述（§4.2 \"3 of 5 seeds converge to gaming\"、§5 \"the Goodhart effect is seed-dependent\"）的措辞暗示了概率估计。这种 framing 不一致确实是问题。\n\n**[REBUT] R2-N2: 单一模型族限制可推广性**\n\n部分反驳。R2 的核心关切（仅 Qwen3 一个模型族）成立，但低估了论文已有的泛化证据：\n\n1. **Cross-logic replication**（§4.3, Figure 6）：FOL→Prolog 的复制展示了三条独立的 gaming pathway（clean TS, uppercase pseudo-Prolog, query-as-fact），跨越了完全不同的逻辑体系和 solver（Prover9 vs. SWI-Prolog）。这不是模型泛化，但证明了 Goodhart 效应在不同 symbolic backend 中复现。\n\n2. **Cross-dataset replication**（§4.3, Table 12）：FOLIO→ProofFOL 展示了不同 dataset structure（3.4× more premises, simpler predicates; Table 2）下的 diagnostic 有效性。\n\n3. **LLaMA-3.2-3B cold-start**（Appendix D.3）和 **non-converging seeds**（Appendix D.5, s45/s52）提供了反面证据：不收敛时不退化。虽然不是完整实验，但支持了 \"degeneration requires successful optimization\" 的 claim。\n\n4. R2 建议增加 \"至少一个非 Qwen 模型族的完整实验\"——我同意这会显著增强论文，但认为这更接近 **Should-Fix** 而非 **Must-Fix**。原因是论文的核心 claim 是关于 ISR/LOO metric 的结构性缺陷（tautological formalizations 满足 LOO necessity by construction, §3.2），这是 metric 层面的问题，不依赖于特定模型。标题措辞确实需要收窄（与我的 W2 一致），但增加模型族不是核心科学贡献成立的前提。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R2-W1: Observe-vs-optimize 理论解释偏浅**\n\n同意。论文将 asymmetry 归因于 \"tautological formalizations satisfy the necessity criterion by construction\"（§3.2, §5），这是一个正确但表层的观察。缺失的讨论包括：\n\n- 这是 LOO 特有的（因为 LOO 只检查 marginal contribution，对 P→P tautology 无法识别）还是所有 structural diagnostic 的共性？例如，full Shapley value（O(2^n) 评估）是否也会被游戏化？论文在 Appendix B 提到 ISR 是 Shapley value 的 (n-1)-coalition restriction，但未讨论 full Shapley 是否免疫。\n- 是否存在修复 ISR 的方法？例如在 LOO 之前增加 tautology pre-filter（检查 premise ≡ conclusion），或结合 semantic faithfulness check。这些讨论对读者的 actionable takeaway 很重要。\n\n**[REBUT] R2-W2: ProofFOL 缺少 ISR reward 条件**\n\nR2 的事实判断有误。论文 **确实在 ProofFOL 上运行了 ISR β=0.1 实验**：\n\n- §4.3 \"ProofFOL ISR (β=0.1): dataset-dependent asymmetry\" 明确报告了结果\n- Table 12（Appendix D, p.20）给出了 ProofFOL ISR β=0.1 的三个 seed 详细数据：s42 (PR=0.35, Genuine=100%), s43 (PR≈0.47, Genuine=30.4%), s44 (PR=0.49, Genuine=100%)\n- Aggregate genuine rate: 76.8% vs exec-only 17.4%（permutation test p=0.10, exploratory）\n\n论文不仅验证了 \"diagnostic 有效\"，还验证了 \"reward 在 ProofFOL 上的效果不同于 FOLIO\"——ISR reward 在 ProofFOL 上表现为 corrective 而非 Goodhart，因为 CE（而非 TS）主导了 hacking geometry，使 ISR≈0 而非 ISR≥0.5。这恰恰展示了 \"reward 失败\" 的 dataset-dependent boundary conditions。\n\nR2 可能因为 ProofFOL 的 ISR 结果未出现在 Table 1（主表）中而遗漏了这部分内容。\n\n**[AGREE] R2-W3: Abstract 信息密度过高**\n\n轻度同意。Abstract 约 180 words，技术上合规（≤200 words），但在有限空间内塞入了 STA 定义、ISR 定义、六种 reward conditions、3/5 seed 统计、cross-logic replication、cross-dataset evidence——导致核心 message（observe-vs-optimize asymmetry）被稀释。不过我认为这是 **写作优化** 问题而非 **学术严谨性** 问题，严重程度低于 R2 的定位。\n\n**[REBUT] R2-W4: Contribution C1-C3 的独立性**\n\n部分反驳。C1-C3 之间确有逻辑耦合，但我认为它们对不同读者群体有独立价值：\n\n- **C1（STA/ISR 作为诊断）**：对部署 neurosymbolic RL 系统的从业者有直接价值，即使他们不关心 Goodhart 理论。§4.1 的 collapse trajectory（ISR 从 0.642 降到 0.003）和 mode breakdown 是独立可用的诊断工具。\n- **C2（Goodhart 效应）**：对 reward design 研究者有价值，展示了 metric → reward 转换的风险。这个发现逻辑上依赖于 C1 的 ISR 定义，但科学贡献是独立的。\n- **C3（Hacking taxonomy）**：8 种 modes 的分类体系（Table 3, Appendix C）有独立的参考价值，后续研究可以直接使用这个分类框架。\n\nR2 建议重组为 2 个 contributions 的方案会损失粒度。当前的 3-contribution 结构与 Introduction §1 末尾的组织（\"(C1) a systematic analysis...; (C2) empirical characterization...; (C3) cross-logic replication...\"）一致且清晰。\n\n---\n\n### 对 R2 Missing References 的回应\n\n1. **Chen et al. (2018) \"Metamorphic Testing\"**：有价值的概念联系。STA 的 LOO ablation 与 metamorphic testing 的 \"变换后预期行为\" 理念确有相似之处，但论文已引用 DeMillo et al. (1978) 和 Jia & Harman (2011) 建立了 mutation testing 的联系（§3.2），coverage 充分。\n2. **reward-hacking-survey (Wang et al., 2026)**：如果确实存在但未引用，应补充。\n3. **Pan et al. (2023) \"Logic-LM\"**：已在 Related Work §2 引用（\"Ye et al., 2023; Pan et al., 2023; Olausson et al., 2023...\"）。R2 可能是指 Logic-LM 的后续关于 formalization quality 的专门讨论，如果是特定后续论文则建议作者检查。\n\n---\n\n### 对 R2 Questions 的补充意见\n\n**Q2（tautological detection filter 修复 ISR）**：这是一个重要方向。论文在 Appendix D.1 测试了 O(1) binary tautology check，结果表明它过于粗糙（所有 ProofFOL 样本都通过）。但未测试将 tautology filter 与 O(n) ISR 结合的方案（例如：先排除 P≡C 的 TS，再计算剩余的 ISR）。这个 gap 值得在 Discussion 中补充。\n\n**Q4（Goodhart effect 是否 capacity-dependent）**：与我的 W3 相关。8B 结果（Appendix D.8）的因果解读被多个混淆变量（K=8 vs K=4, effective batch 16 vs 8）干扰，不能简单归因于 capacity。论文的 \"convergence threshold\" 表述需要降级为 correlational observation。",
    "reviewer_id": "1",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2667 · 2026-05-25T21:29:51.206386+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 2668 · 2026-05-25T21:30:02.562916+00:00_

交叉回应已提交。总结：

- **[AGREE] R2-N1**: 同意 seed 数量不足，补充指出 multi-attractor dynamics 使得即使增加到 10-15 seeds 仍可能不够
- **[REBUT] R2-N2**: 部分反驳，论文已有 cross-logic/cross-dataset 泛化证据，建议从 Must-Fix 降级为 Should-Fix
- **[AGREE] R2-W1**: 同意理论解释偏浅，应讨论 LOO 特异性和修复可能
- **[REBUT] R2-W2**: R2 事实有误——论文确实在 ProofFOL 上运行了 ISR β=0.1（§4.3, Table 12）
- **[AGREE] R2-W3**: 轻度同意 Abstract 密度过高，但属于写作优化而非学术问题
- **[REBUT] R2-W4**: 部分反驳 C1-C3 合并建议，三个 contribution 对不同读者群有独立价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1"
}
```

</details>

---
