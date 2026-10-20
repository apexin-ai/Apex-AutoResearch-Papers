# Director coordination — Part 3 of 7

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/0d/0d5b5d57f8a45f2c2330.json)

## Round 52

### Tool call

_source line 635 · 2026-05-22T13:52:24.487882+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "exec-sim-repair-verifier",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness/Question，使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 也请简要标注是否同意。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告（Novelty + Completeness + Writing Quality）\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation：per-test classification (CLS)、execution output generation (CWM)、trajectory-level scoring (TRAJ)。实验在两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）上进行，使用 ≤8B LoRA fine-tuning。主要发现：(1) function level 三种 formulation 统计等价；(2) repo level CLS 大幅优于 CWM（18–26pp gap），主因是 CWM 的 format collapse；(3) 错误互补性暗示 formulation routing 的潜力。论文还提出了一个 failure mode taxonomy（format collapse, decision collapse, aggregation penalty）。\n\n---\n\n## Strengths（逐条）\n\n**S1. 实验方法论严谨。** 使用 TOST 等价检验、clustered bootstrap（按 problem 聚类）、ICC、Holm-Bonferroni 多重比较校正、SESOI framework 设定等价阈值——统计方法论远超同类 empirical study 的平均水平。这是论文最突出的优势。\n\n**S2. Matched experimental design。** 控制变量设计合理：相同训练数据、相同 LoRA 配置、相同模型家族，只改变 formulation。这使得 formulation 效果的归因具有较高可信度（虽然仍有 confound，见 W2）。\n\n**S3. Failure mode taxonomy 有实用价值。** Table 4 的三类 failure mode（format collapse / decision collapse / aggregation penalty）对 practitioner 选择 formulation 有直接指导意义，比单纯报告准确率差异更有信息量。\n\n**S4. 透明的 limitations 讨论。** §3.7 Threats to Validity 和 Limitations 对几乎所有 confound 进行了系统讨论（checkpoint selection、preprocessing、eval sequence length、CWM scale 限制等），hedging 恰当，没有过度声称因果关系。\n\n**S5. 丰富的 appendix。** 10+ 页附录覆盖 ablation、sensitivity analysis、qualitative examples、power analysis，审稿过程中几乎所有追问都能在附录找到答案。\n\n**S6. 写作整体干净。** 主文几乎没有 AI 痕迹（\"Furthermore\"/\"Moreover\"/\"Notably\" 仅出现在 appendix 中 3 次），术语体系（CLS/CWM/TRAJ）一致，claim 的 hedging 恰当（大量使用 \"under our protocol\"、\"conditional on the ≤8B LoRA regime\" 等限定语）。\n\n---\n\n## Weaknesses（逐条，标注 severity）\n\n**W1. [Must-Fix] CWM baseline 严重偏弱，削弱了核心结论的说服力。**\n\n- **具体位置**：§3.1 (Models and training), §3.5 (Repo-Level), Limitations\n- **问题**：论文的 CWM 是 ≤8B LoRA fine-tuned model，而非原始 CWM（Meta, 32B, execution trace mid-training）。这两个设置的差距是根本性的：原始 CWM 专门在 execution trace 数据上做了 mid-training 来学习输出格式，而本文的 CWM 只是普通 LLM + LoRA，从未见过 execution trace。repo-level 的 18–26pp gap 和 format collapse（53–74% unparseable）很可能主要归因于 pretraining 数据差异而非 formulation 本身的固有缺陷。\n- **为什么影响接收**：论文的核心 claim 是 \"formulation choice is governed by code complexity\"，但如果 CWM 的失败主要是因为 baseline 不充分（缺少 execution trace pretraining），那这个 claim 变成 \"inadequately pretrained generation models fail at repo level\"——这是 trivial 的。论文虽然承认了这个 limitation，但 abstract 和 introduction 的措辞（\"the CLS–CWM gap widens to 18–26pp\"）没有充分限定这一点。\n- **建议修改方向**：(1) Abstract 和 Introduction 中所有提到 CWM 18–26pp gap 的地方必须加上 \"under ≤8B LoRA fine-tuning without execution trace pretraining\" 限定；(2) 讨论 GenRM（Zhang et al., 2024, ICLR 2025）等工作中 generative verifier 在数学推理领域优于 discriminative verifier 的发现，分析为什么代码验证可能呈现相反模式（或承认 scale 不足以下定论）；(3) 理想情况下补充一个 32B 规模的实验（即使只有 1 seed）来检验 format collapse 是否是 scale-dependent。\n\n**W2. [Must-Fix] Novelty 不足以达到 Conference 水平——对已有 formulation 的比较缺少新方法论或新洞见。**\n\n- **问题**：论文不提出任何新方法，而是比较三种已有 formulation。这本身不是问题（systematic empirical study 有其价值），但前提是比较的结论必须超越直觉、提供 surprising 或 actionable 的 insight。让我逐一审视三个核心发现：\n  - **Finding 1（function-level equivalence）**：当输出是 1 个 token（integer/boolean）时，generation ≈ classification——这基本是 trivial 的。输出空间极小时，generation 不会比 classification 差，这不需要实验验证。\n  - **Finding 2（repo-level divergence via format collapse）**：长输出的 generation 模型容易产生格式错误——这也是广泛已知的。任何使用过 LLM 生成结构化输出的 practitioner 都经历过这个问题。\n  - **Finding 3（error complementarity）**：oracle routing 达到 95.83%，但 (a) 这是 single-seed estimate（n=48 variants），(b) re-repair pilot（n=44, p=0.42）显示 per-test diagnostics 没有下游收益，直接削弱了 complementarity 的实用价值。\n- **为什么影响接收**：这三个发现都没有超越一个有经验的 practitioner 的直觉。Failure mode taxonomy（S3）是相对新颖的贡献，但它是 descriptive 的，没有 prescriptive 价值（论文没有提出如何利用 taxonomy 来改进 verification）。\n- **建议修改方向**：(1) 在 taxonomy 基础上提出 complexity-aware routing algorithm 并验证其效果（哪怕是 oracle analysis 之外的 heuristic）；(2) 深入分析 WHY CLS 和 CWM 在 function level 等价——是因为 function-level 代码语义简单，还是因为输出空间小？一个 ablation 可以用 CWM 预测 short structured output（如 JSON {pass: true/false}）vs. full execution trace，以区分两个假设；(3) 如果无法增加新贡献，需要更诚实地将论文定位为 \"benchmark/replication study\" 而非 \"systematic empirical study with actionable insights\"。\n\n**W3. [Should-Fix] z=−23.7 interaction statistic 仅基于 DeepSeek-Coder，但在 abstract/intro 中被作为核心发现呈现。**\n\n- **具体位置**：Abstract（\"a significant interaction (z=−23.7)\"），§1 Introduction（同），§3.5（\"A mixed-effects linear probability model... DeepSeek-Coder\"）\n- **问题**：§3.5 明确说明 interaction 分析只用了 DeepSeek-Coder（\"the only family with both function- and repo-level CWM evaluations under matched conditions\"），但 abstract 和 introduction 没有提及这个限制。读者会自然认为这是跨模型的结论。\n- **建议**：Abstract 中改为 \"a significant interaction (z=−23.7, DeepSeek-Coder)\" 或至少在 introduction 中明确标注。\n\n**W4. [Should-Fix] Oracle routing 结果（90.63%/95.83%）均为 single-seed estimate，统计可靠性不足。**\n\n- **具体位置**：§1 contribution 3、§3.6 Error complementarity、§5 Conclusion\n- **问题**：Function-level oracle 90.63% 是 single-seed estimate；repo-level 95.83% 基于 n=48 variants。这些数字被反复在 abstract、introduction、conclusion 中引用，但没有 confidence interval 或多 seed 验证。given function-level per-seed accuracy 的 std 为 0.37–0.97pp，oracle combination 的 variance 可能更大。\n- **建议**：提供 oracle 结果的 bootstrap CI，或至少在引用时明确标注 \"(single-seed estimate)\"。\n\n**W5. [Should-Fix] 遗漏关键相关工作：GenRM（Zhang et al., 2024）。**\n\n- **具体位置**：§4 Related Work\n- **问题**：GenRM / \"Generative Verifiers: Reward Modeling as Next-Token Prediction\"（Zhang et al., ICLR 2025）直接研究了 discriminative vs. generative formulation 在 verification/reward modeling 中的效果，发现 generative verifier 在数学推理任务上显著优于 discriminative verifier（GSM8K 上 73%→93.4%）。这与本文在 repo-level 代码验证上的发现形成直接对比/矛盾。论文的 §4 \"Process vs. Outcome Supervision\" 段讨论了 PRM/ORM，但完全没有提到 GenRM 这个最直接的相关工作。\n- **为什么重要**：GenRM 的发现暗示 generative formulation 在 sufficient scale 下可能优于 classification——这恰好支持本文 CWM 失败可能是 scale 问题而非 formulation 固有缺陷的假设。不讨论这个工作是 related work 的显著遗漏。\n- **额外遗漏**：CVeDRL（2026, arXiv 2601.22803）——difficulty-aware RL for code verification，与本文的 per-test difficulty 分析相关。\n\n**W6. [Should-Fix] TRAJ 的实验设置不公平，削弱了 TRAJ 相关结论的可信度。**\n\n- **具体位置**：§3.1 (Datasets), Appendix §N (TRAJ training regime)\n- **问题**：TRAJ 使用 ~400 repo-level variants 训练，而 CLS 和 CWM 使用 ~70K per-test instances。虽然这是 formulation 固有的（trajectory-level labels 只有 variant 粒度），但训练数据量相差 175×，这使得 TRAJ 的 repo-level 表现（72.91–77.08%）可能主要受限于数据量而非 formulation。Downsample ablation（80.74% vs 72.92%）控制了 CLS 的数据量但没有控制 label granularity。\n- **建议**：讨论 data augmentation for TRAJ（如对每个 variant 生成多个 prompt 变体）是否可能缩小差距。\n\n**W7. [Minor] 信息密度不均匀：§3.5 过度压缩，§3.3 Scaling Behavior 价值有限。**\n\n- §3.5 (Repo-Level) 在不到 1.5 页内塞入了 formulation divergence、cross-model consistency、failure mode taxonomy、default assignment artifact、complexity as moderator、formulation×complexity interaction——每个都值得更多讨论空间。\n- §3.3 (Scaling Behavior) 仅比较 4B vs 8B 两个 size，n=2 seeds，结论有限（\"CLS and TRAJ scale, CWM doesn't\"），可以压缩为一段，腾出空间给 §3.5。\n\n**W8. [Minor] Figure 2 信息冗余。**\n\n- Figure 2 展示的信息（function→repo gap amplification）已经在 Table 1、Table 3 和正文中充分表达。作为唯一的 figure（除 Figure 1 架构图），这个位置可以更好地用于展示 failure mode taxonomy 的可视化或 error complementarity 的 Venn diagram。\n\n**W9. [Minor] Limitations 段过于简短。**\n\n- Limitations 只有一小段（约 10 行），仅覆盖 3 个点。鉴于本文有大量 confound（W1-W6），建议至少增加：(a) synthetic mutation 与 real bug 的 gap 讨论；(b) 仅 2 个模型家族的 generalizability 限制。虽然 §3.7 讨论了 threats，但 Limitations section 本身应该是 self-contained 的。\n\n---\n\n## Questions for Authors\n\n**Q1.** GenRM (Zhang et al., ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative verifier。你们如何解释代码验证领域呈现相反趋势？是 domain difference、scale difference、还是 pretraining difference？\n\n**Q2.** 如果将 CWM 的输出改为 short structured format（如 JSON `{\"result\": \"PASS\", \"output\": \"42\"}`）而非 free-form execution trace，format collapse 是否会显著减少？这个 ablation 可以区分 \"输出长度\" 和 \"generation formulation\" 两个因素的贡献。\n\n**Q3.** Re-repair pilot (n=44, p=0.42) 显示 per-test diagnostics 没有下游收益。这是否意味着 CLS 的 diagnostic advantage 是 theoretical 的而非 practical 的？如果是，\"error complementarity\" 作为核心贡献之一的地位是否需要降低？\n\n**Q4.** 论文在 Appendix 中提到 accidental training artifact（CWM model trained on classification-format data, 86.05% accuracy with 0% unparseable）。这个发现是否暗示 format 是唯一瓶颈，只要解决 format compliance 就能恢复 CWM 的性能？如果是，constrained decoding 为什么没有被尝试？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024/2025)**, \"Generative Verifiers: Reward Modeling as Next-Token Prediction,\" ICLR 2025. 直接比较 discriminative vs. generative formulation for verification。\n2. **CVeDRL** (2026, arXiv 2601.22803), difficulty-aware RL for code verification。\n3. **GenPRM** (2025, arXiv 2504.00891), \"Process Reward Models That Think\" — generative PRM with CoT。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "exec-sim-repair-verifier",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness/Question，使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 也请简要标注是否同意。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n## Reviewer 2 审稿报告（Novelty + Completeness + Writing Quality）\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation：per-test classification (CLS)、execution output generation (CWM)、trajectory-level scoring (TRAJ)。实验在两个模型家族（Qwen3、DeepSeek-Coder）、两个复杂度级别（function-level、repo-level）上进行，使用 ≤8B LoRA fine-tuning。主要发现：(1) function level 三种 formulation 统计等价；(2) repo level CLS 大幅优于 CWM（18–26pp gap），主因是 CWM 的 format collapse；(3) 错误互补性暗示 formulation routing 的潜力。论文还提出了一个 failure mode taxonomy（format collapse, decision collapse, aggregation penalty）。\n\n---\n\n## Strengths（逐条）\n\n**S1. 实验方法论严谨。** 使用 TOST 等价检验、clustered bootstrap（按 problem 聚类）、ICC、Holm-Bonferroni 多重比较校正、SESOI framework 设定等价阈值——统计方法论远超同类 empirical study 的平均水平。这是论文最突出的优势。\n\n**S2. Matched experimental design。** 控制变量设计合理：相同训练数据、相同 LoRA 配置、相同模型家族，只改变 formulation。这使得 formulation 效果的归因具有较高可信度（虽然仍有 confound，见 W2）。\n\n**S3. Failure mode taxonomy 有实用价值。** Table 4 的三类 failure mode（format collapse / decision collapse / aggregation penalty）对 practitioner 选择 formulation 有直接指导意义，比单纯报告准确率差异更有信息量。\n\n**S4. 透明的 limitations 讨论。** §3.7 Threats to Validity 和 Limitations 对几乎所有 confound 进行了系统讨论（checkpoint selection、preprocessing、eval sequence length、CWM scale 限制等），hedging 恰当，没有过度声称因果关系。\n\n**S5. 丰富的 appendix。** 10+ 页附录覆盖 ablation、sensitivity analysis、qualitative examples、power analysis，审稿过程中几乎所有追问都能在附录找到答案。\n\n**S6. 写作整体干净。** 主文几乎没有 AI 痕迹（\"Furthermore\"/\"Moreover\"/\"Notably\" 仅出现在 appendix 中 3 次），术语体系（CLS/CWM/TRAJ）一致，claim 的 hedging 恰当（大量使用 \"under our protocol\"、\"conditional on the ≤8B LoRA regime\" 等限定语）。\n\n---\n\n## Weaknesses（逐条，标注 severity）\n\n**W1. [Must-Fix] CWM baseline 严重偏弱，削弱了核心结论的说服力。**\n\n- **具体位置**：§3.1 (Models and training), §3.5 (Repo-Level), Limitations\n- **问题**：论文的 CWM 是 ≤8B LoRA fine-tuned model，而非原始 CWM（Meta, 32B, execution trace mid-training）。这两个设置的差距是根本性的：原始 CWM 专门在 execution trace 数据上做了 mid-training 来学习输出格式，而本文的 CWM 只是普通 LLM + LoRA，从未见过 execution trace。repo-level 的 18–26pp gap 和 format collapse（53–74% unparseable）很可能主要归因于 pretraining 数据差异而非 formulation 本身的固有缺陷。\n- **为什么影响接收**：论文的核心 claim 是 \"formulation choice is governed by code complexity\"，但如果 CWM 的失败主要是因为 baseline 不充分（缺少 execution trace pretraining），那这个 claim 变成 \"inadequately pretrained generation models fail at repo level\"——这是 trivial 的。论文虽然承认了这个 limitation，但 abstract 和 introduction 的措辞（\"the CLS–CWM gap widens to 18–26pp\"）没有充分限定这一点。\n- **建议修改方向**：(1) Abstract 和 Introduction 中所有提到 CWM 18–26pp gap 的地方必须加上 \"under ≤8B LoRA fine-tuning without execution trace pretraining\" 限定；(2) 讨论 GenRM（Zhang et al., 2024, ICLR 2025）等工作中 generative verifier 在数学推理领域优于 discriminative verifier 的发现，分析为什么代码验证可能呈现相反模式（或承认 scale 不足以下定论）；(3) 理想情况下补充一个 32B 规模的实验（即使只有 1 seed）来检验 format collapse 是否是 scale-dependent。\n\n**W2. [Must-Fix] Novelty 不足以达到 Conference 水平——对已有 formulation 的比较缺少新方法论或新洞见。**\n\n- **问题**：论文不提出任何新方法，而是比较三种已有 formulation。这本身不是问题（systematic empirical study 有其价值），但前提是比较的结论必须超越直觉、提供 surprising 或 actionable 的 insight。让我逐一审视三个核心发现：\n  - **Finding 1（function-level equivalence）**：当输出是 1 个 token（integer/boolean）时，generation ≈ classification——这基本是 trivial 的。输出空间极小时，generation 不会比 classification 差，这不需要实验验证。\n  - **Finding 2（repo-level divergence via format collapse）**：长输出的 generation 模型容易产生格式错误——这也是广泛已知的。任何使用过 LLM 生成结构化输出的 practitioner 都经历过这个问题。\n  - **Finding 3（error complementarity）**：oracle routing 达到 95.83%，但 (a) 这是 single-seed estimate（n=48 variants），(b) re-repair pilot（n=44, p=0.42）显示 per-test diagnostics 没有下游收益，直接削弱了 complementarity 的实用价值。\n- **为什么影响接收**：这三个发现都没有超越一个有经验的 practitioner 的直觉。Failure mode taxonomy（S3）是相对新颖的贡献，但它是 descriptive 的，没有 prescriptive 价值（论文没有提出如何利用 taxonomy 来改进 verification）。\n- **建议修改方向**：(1) 在 taxonomy 基础上提出 complexity-aware routing algorithm 并验证其效果（哪怕是 oracle analysis 之外的 heuristic）；(2) 深入分析 WHY CLS 和 CWM 在 function level 等价——是因为 function-level 代码语义简单，还是因为输出空间小？一个 ablation 可以用 CWM 预测 short structured output（如 JSON {pass: true/false}）vs. full execution trace，以区分两个假设；(3) 如果无法增加新贡献，需要更诚实地将论文定位为 \"benchmark/replication study\" 而非 \"systematic empirical study with actionable insights\"。\n\n**W3. [Should-Fix] z=−23.7 interaction statistic 仅基于 DeepSeek-Coder，但在 abstract/intro 中被作为核心发现呈现。**\n\n- **具体位置**：Abstract（\"a significant interaction (z=−23.7)\"），§1 Introduction（同），§3.5（\"A mixed-effects linear probability model... DeepSeek-Coder\"）\n- **问题**：§3.5 明确说明 interaction 分析只用了 DeepSeek-Coder（\"the only family with both function- and repo-level CWM evaluations under matched conditions\"），但 abstract 和 introduction 没有提及这个限制。读者会自然认为这是跨模型的结论。\n- **建议**：Abstract 中改为 \"a significant interaction (z=−23.7, DeepSeek-Coder)\" 或至少在 introduction 中明确标注。\n\n**W4. [Should-Fix] Oracle routing 结果（90.63%/95.83%）均为 single-seed estimate，统计可靠性不足。**\n\n- **具体位置**：§1 contribution 3、§3.6 Error complementarity、§5 Conclusion\n- **问题**：Function-level oracle 90.63% 是 single-seed estimate；repo-level 95.83% 基于 n=48 variants。这些数字被反复在 abstract、introduction、conclusion 中引用，但没有 confidence interval 或多 seed 验证。given function-level per-seed accuracy 的 std 为 0.37–0.97pp，oracle combination 的 variance 可能更大。\n- **建议**：提供 oracle 结果的 bootstrap CI，或至少在引用时明确标注 \"(single-seed estimate)\"。\n\n**W5. [Should-Fix] 遗漏关键相关工作：GenRM（Zhang et al., 2024）。**\n\n- **具体位置**：§4 Related Work\n- **问题**：GenRM / \"Generative Verifiers: Reward Modeling as Next-Token Prediction\"（Zhang et al., ICLR 2025）直接研究了 discriminative vs. generative formulation 在 verification/reward modeling 中的效果，发现 generative verifier 在数学推理任务上显著优于 discriminative verifier（GSM8K 上 73%→93.4%）。这与本文在 repo-level 代码验证上的发现形成直接对比/矛盾。论文的 §4 \"Process vs. Outcome Supervision\" 段讨论了 PRM/ORM，但完全没有提到 GenRM 这个最直接的相关工作。\n- **为什么重要**：GenRM 的发现暗示 generative formulation 在 sufficient scale 下可能优于 classification——这恰好支持本文 CWM 失败可能是 scale 问题而非 formulation 固有缺陷的假设。不讨论这个工作是 related work 的显著遗漏。\n- **额外遗漏**：CVeDRL（2026, arXiv 2601.22803）——difficulty-aware RL for code verification，与本文的 per-test difficulty 分析相关。\n\n**W6. [Should-Fix] TRAJ 的实验设置不公平，削弱了 TRAJ 相关结论的可信度。**\n\n- **具体位置**：§3.1 (Datasets), Appendix §N (TRAJ training regime)\n- **问题**：TRAJ 使用 ~400 repo-level variants 训练，而 CLS 和 CWM 使用 ~70K per-test instances。虽然这是 formulation 固有的（trajectory-level labels 只有 variant 粒度），但训练数据量相差 175×，这使得 TRAJ 的 repo-level 表现（72.91–77.08%）可能主要受限于数据量而非 formulation。Downsample ablation（80.74% vs 72.92%）控制了 CLS 的数据量但没有控制 label granularity。\n- **建议**：讨论 data augmentation for TRAJ（如对每个 variant 生成多个 prompt 变体）是否可能缩小差距。\n\n**W7. [Minor] 信息密度不均匀：§3.5 过度压缩，§3.3 Scaling Behavior 价值有限。**\n\n- §3.5 (Repo-Level) 在不到 1.5 页内塞入了 formulation divergence、cross-model consistency、failure mode taxonomy、default assignment artifact、complexity as moderator、formulation×complexity interaction——每个都值得更多讨论空间。\n- §3.3 (Scaling Behavior) 仅比较 4B vs 8B 两个 size，n=2 seeds，结论有限（\"CLS and TRAJ scale, CWM doesn't\"），可以压缩为一段，腾出空间给 §3.5。\n\n**W8. [Minor] Figure 2 信息冗余。**\n\n- Figure 2 展示的信息（function→repo gap amplification）已经在 Table 1、Table 3 和正文中充分表达。作为唯一的 figure（除 Figure 1 架构图），这个位置可以更好地用于展示 failure mode taxonomy 的可视化或 error complementarity 的 Venn diagram。\n\n**W9. [Minor] Limitations 段过于简短。**\n\n- Limitations 只有一小段（约 10 行），仅覆盖 3 个点。鉴于本文有大量 confound（W1-W6），建议至少增加：(a) synthetic mutation 与 real bug 的 gap 讨论；(b) 仅 2 个模型家族的 generalizability 限制。虽然 §3.7 讨论了 threats，但 Limitations section 本身应该是 self-contained 的。\n\n---\n\n## Questions for Authors\n\n**Q1.** GenRM (Zhang et al., ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative verifier。你们如何解释代码验证领域呈现相反趋势？是 domain difference、scale difference、还是 pretraining difference？\n\n**Q2.** 如果将 CWM 的输出改为 short structured format（如 JSON `{\"result\": \"PASS\", \"output\": \"42\"}`）而非 free-form execution trace，format collapse 是否会显著减少？这个 ablation 可以区分 \"输出长度\" 和 \"generation formulation\" 两个因素的贡献。\n\n**Q3.** Re-repair pilot (n=44, p=0.42) 显示 per-test diagnostics 没有下游收益。这是否意味着 CLS 的 diagnostic advantage 是 theoretical 的而非 practical 的？如果是，\"error complementarity\" 作为核心贡献之一的地位是否需要降低？\n\n**Q4.** 论文在 Appendix 中提到 accidental training artifact（CWM model trained on classification-format data, 86.05% accuracy with 0% unparseable）。这个发现是否暗示 format 是唯一瓶颈，只要解决 format compliance 就能恢复 CWM 的性能？如果是，constrained decoding 为什么没有被尝试？\n\n---\n\n## Missing References\n\n1. **Zhang et al. (2024/2025)**, \"Generative Verifiers: Reward Modeling as Next-Token Prediction,\" ICLR 2025. 直接比较 discriminative vs. generative formulation for verification。\n2. **CVeDRL** (2026, arXiv 2601.22803), difficulty-aware RL for code verification。\n3. **GenPRM** (2025, arXiv 2504.00891), \"Process Reward Models That Think\" — generative PRM with CoT。"
  }
}
```

</details>

---


### Tool result

_source line 636 · 2026-05-22T13:52:26.069015+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1581
}
```

</details>

---


### Assistant

_source line 637 · 2026-05-22T13:52:38.764756+00:00_

交叉分享已发出。两位 Reviewer 正在互阅对方报告并准备逐条回应，等待交叉回应返回后进入收敛判断。

**当前进度**：
- Round 1 独立审稿 ✅（R1: 3.0, R2: 3.0，均为 Findings）
- Step 2 交叉分享 ✅（已发出）
- 等待：两位 Reviewer 的 [AGREE]/[REBUT] 回应

**初步观察**——两位 Reviewer 在以下问题上高度重叠：
1. CWM baseline 偏弱 / 条件不对等（R1-N2 ≈ R2-W1）
2. Oracle 单种子无 CI（R1-W2 ≈ R2-W4）
3. GenRM 等相关工作遗漏（R2-W5，R1 未提但 R2 论证充分）
4. TOST 误归属（R1-N1，R2 未独立提出但属事实性错误）

R2 额外提出了 novelty 不足（W2）和 TRAJ 训练数据量不对等（W6），这两个是 R1 没有覆盖的角度，交叉讨论中值得关注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 638 · 2026-05-22T13:55:37.406982+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Strengths 回应

**S1** [AGREE]: 同意。matched comparison 框架确实是本文最核心的方法论贡献，固定模型/数据/compute 仅变 formulation 的设计在该领域此前未见。

**S2** [AGREE]: 同意。四层统计工具（clustered bootstrap → TOST → mixed-effects LPM → Holm-Bonferroni）的组合使用合理且层次分明。

**S3** [AGREE]: 同意。Failure mode taxonomy（Table 4）提供了超越准确率数字的可操作诊断框架。

**S4** [AGREE]: 同意。CWM 退化诊断的四种干预 + 意外 artifact（CWM 模型在 CLS 格式数据上恢复 86.05%）形成了有说服力的排除链。

**S5** [AGREE]: 同意。量化式 threats 分析（worst-case ~11.5pp vs. 18–26pp gap → ≥7.5pp margin）在实证论文中非常少见，增强了结论的可信度。

**S6** [AGREE]: 同意。Oracle accuracy-utility framework 从理论推导到实验验证（T=2 贡献 55.3%）的闭环令人信服。

---

### Must-Fix 问题回应

**[AGREE] R1-N1: TOST p=0.007 的归属确实存在错误**

R1 的发现经我独立验证完全成立。这是本轮审稿中最重要的事实性问题：

- **Abstract**（第4行）声称 "CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)"
- **Conclusion**（第4行）进一步给出 "CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)"
- 但 **§3.4 标题**明确为 "Per-Test vs. Trajectory-Level Equivalence"，正文写 "We compare CLS (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds"，得到 p=0.007
- **Appendix I**（Table 13 标题）明确写 "TOST margin sensitivity for CLS–TRAJ variant-level equivalence"
- **Table 15**（Holm-Bonferroni）Rank 2 标注为 "Func: CLS vs TRAJ (TOST ±2pp)"

全文没有任何位置报告 CLS–CWM 的正式 TOST 检验。§3.4 末尾确实提到 "the observed CLS–CWM gap of 0.02pp is consistent with equivalence, but with only 2 seeds the comparison is underpowered"——这说明作者知道 CLS-CWM gap 很小，但**没有执行正式检验**。

**我的补充**：这个问题比 R1 描述的可能更严重。Abstract 不仅将 CLS–TRAJ 的 p 值错误归给了 CLS–CWM，而且 Abstract 说的是 "5 seeds" 但 CLS–CWM 在 DeepSeek 上只有 2 seeds（underpowered），Qwen3 上虽有 5 seeds 但同样没做 TOST。这意味着论文的**第一条 contribution（formulation near-equivalence at low complexity）**的核心统计证据存在 misattribution。

R1 的建议（补做 CLS–CWM TOST + 修正 abstract/conclusion 标注）完全合理。考虑到 Table 1 中 CLS–CWM gap 仅 0.02–1.24pp，补做 TOST 预期能通过 ±2pp margin，修复成本不高。

---

**[AGREE with nuance] R1-N2: CWM 实验条件系统性不利**

R1 的核心论点成立，但我认为严重程度需要分级讨论：

**同意部分**：
- Abstract 确实比 Conclusion 更缺乏 qualifier。Abstract 说 "the CLS–CWM gap widens to 18–26pp" 而没有像 Conclusion 那样加上 "under ≤8B LoRA fine-tuning"
- CWM 面临的 NaN validation loss（被迫用 final epoch checkpoint）是一个系统性劣势。DeepSeek epoch-1 CWM 达到 75.45% vs epoch-3 的 57.31%，差异达 +18.14pp，这确实表明 checkpoint selection 对 CWM 的影响远大于对 CLS 的影响（<1pp）
- max_new_tokens=512 对有效上下文的压缩是一个合理的关切

**部分反驳**：
- 但论文并非完全忽略这些问题。§3.7 Threats to Validity 逐条量化了五个 confound，包括 checkpoint selection 和 eval sequence length 的影响。Appendix N 进一步计算了 worst-case compounding (~11.5pp)，论证 18–26pp gap 即使扣除所有已知 confound 仍有 ≥7.5pp residual。这个 residual 分析已经部分回应了 R1 的关切
- 论文标题说 "Design Space" 而非 "Definitive Ranking"，研究定位本身就是 systematic empirical study 而非一般性理论
- Conclusion 中的推荐语 "at repository level under ≤8B LoRA, CLS is recommended" 已包含 regime 限定

**我的建议**：将此从 critical 降为 strong warning。Abstract 需要加上 "under our ≤8B LoRA protocol" 限定 repo-level 结论——这只需约 5 个词的修改。但无需要求论文改变整体 framing：在明确标注实验范围后，结论在其所覆盖的 regime 内是 well-supported 的。R1 建议的 "如果 CWM 用 early-stopped checkpoint，gap 从 ~26pp 缩至 ~9pp" 的讨论有价值，但这属于 deepening analysis 而非纠正错误。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: n=48 导致 repo-level 比较 underpowered**

同意。MDE ≈ 25pp 意味着 CLS–TRAJ 在 repo-level 的 gap（<10pp）无法被统计检验。Conclusion 推荐 CLS "for both accuracy and throughput" 中 accuracy 部分的证据不足。建议修改为明确指出推荐主要基于 throughput 优势（217×）和 per-test 诊断能力，而 accuracy 比较在 variant level 是 underpowered 的。

但补充一点：per-test level n=9,784 的分析（Table 3）power 是充足的，CLS vs CWM 的差异在 per-test level 是显著的。问题仅出在 variant-level 聚合后 n 太小。

**[AGREE] R1-W2: Oracle 互补性缺少置信区间**

同意。95.83% 在 n=48 上的 binomial 95% CI 约为 [85.7%, 99.5%]，非常宽。论文将此作为 "the strongest practical argument for exploring the formulation design space"（§1），但数字的不确定性太大，不足以支撑如此强的措辞。

**我的补充**：function-level oracle（90.63%）同样是单种子估计，但 n=1,890（per-test）提供了更窄的 CI。论文至少应在 function level 做多种子 oracle（数据已有），并为 repo-level 单种子结果加上 binomial CI。

**[REBUT] R1-W3: TOST 混合精度问题——影响被高估**

R1 关切混合 bfloat16 和 NF4 种子可能引入 precision × formulation 交互。但：

1. 论文 Appendix O（Extended Limitations, p22）明确讨论了这一点："NF4 seeds contribute precision (narrowing the CI) without shifting the mean, consistent with precision being comparable across both quantization levels at function level." 这表明 NF4 对均值没有系统性偏移，仅增加了 precision（缩窄 CI）
2. bfloat16-only 子集的 p=0.128（vs 全集 0.007）完全符合 power 下降的预期：从 5 seeds 减到 3 seeds，自由度从 4 降到 2。均值 gap（-0.45pp）在 bfloat16-only 中方向一致（论文注释说 "consistent in direction"），p 值上升纯粹是 power 不足
3. 如果 NF4 系统性地缩小了 CLS–TRAJ gap，那 bfloat16-only 的 gap 应该更大，但论文说 gap 方向一致。这与 R1 担心的 "NF4 可能系统性缩小 gap" 不符

建议降为 minor。在 Appendix 中增加 bfloat16 vs NF4 子集的均值 gap 对比即可完全消除疑虑。

**[AGREE] R1-W4: CWM checkpoint 消融不对称**

同意。CLS checkpoint 消融（<1pp range）只覆盖了一半的故事。CWM 在 DeepSeek 上的 epoch-1 vs epoch-3 差异达 18.14pp，但 Qwen3（primary model family）没有做同样的消融。如果 Qwen3 CWM early-stopped 也能达到 ~75%，则 CLS–CWM gap 从 ~18pp 缩至 ~10pp——虽然 CLS 仍优于 CWM，但 effect size 定性解读会变化（从 "crushing" 变为 "moderate"）。

补充一个 epoch-1 的 Qwen3 CWM 评估是合理且成本不高的要求。

---

### Minor 问题回应

**[AGREE] R1-M1**: 同意。LPM 应报告 robust SEs，即使影响可能很小。一句话的改动。

**[AGREE] R1-M2**: 同意。至少在 Appendix 中展示每种 formulation 的一个完整 prompt 示例。当前指向 code repository 不够——审稿阶段代码不可访问。

**[REBUT] R1-M3**: 部分反驳。Figure 2 的 y 轴从 ~55% 起始，但 caption 标题已明确标注 "Gap amplification from function to repo level"——这正是论文要传达的信息。截断 y 轴是常见的可视化手法，只要 caption 中提示即可。不过，在 caption 中加一句 "y-axis begins at 55%" 确实是低成本的改进。

**[AGREE] R1-M4**: 同意。2 种子的 scaling 分析 power 极低，"CWM flat scaling" 的解读应标注为 exploratory observation。

**[REBUT] R1-M5**: 需要具体核实。论文中 Xia et al. 的 Agentless 如果最初是 arXiv 2024 preprint 但正式发表于 2025（如 ICSE 2025），则 bib 使用 2025 年份是正确的。需要检查具体引用格式——如果 bib 中 year=2025 对应的是正式出版物，而引用文本中出现 "2024" 则可能是 natbib 根据 sort key 生成的。但如果确实不一致，应统一。

---

### Questions 回应

**Q1**: R1 的质疑完全合理。如上文 N1 分析，TOST p=0.007 确实是 CLS–TRAJ 而非 CLS–CWM。

**Q2**: 同意这是关键实验。Qwen3-8B CWM epoch-1 的结果对理解 gap 的 "真实" 大小至关重要。

**Q3**: 同意。Function-level 有 5 个种子的数据，多种子 oracle 分析应该可以直接计算。

**Q4**: 有价值但非必须。Angrist & Pischke 理论保证已经相当强。作为 robustness check 可以加在 Appendix 中。

---

### Missing References 回应

- **Ding et al. (2024) RepoExec**: 同意应引用。RepoExec 提供 repo-level executable benchmark，与本文的 repo-level verification 高度相关。
- **Chen et al. (2024) "Benchmarking the Role of LLM-based Verifiers"**: 同意。如果该工作直接比较不同 verifier formulations，则是 direct prior work，必须在 Related Work 中讨论并说明本文方法论上的差异（matched comparison vs. 非 matched）。

---

### 总体判断

R1 的审稿质量非常高，对论文的技术细节把握精准。N1（TOST 归属错误）是我独立验证后完全同意的 critical issue——这是一个需要修复的事实性错误，但修复成本低（补做检验 + 修正引用）。N2 的严重程度我认为略低于 R1 的判断（strong warning 而非 critical），因为论文在 body text 中已有相当程度的 hedging，主要问题在 Abstract 缺乏 qualifier。

W1–W4 中，W3（混合精度）我认为影响被高估，论文已有初步回应且证据方向一致；其余三条（W1, W2, W4）我均同意。

**如果 N1 被修复（补做 CLS–CWM TOST）且 Abstract 加上 regime qualifier**，论文的核心贡献——matched comparison 框架、failure mode taxonomy、统计方法论——仍然扎实，值得接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 639 · 2026-05-22T13:55:47.941082+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 审稿意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 640 · 2026-05-22T13:55:50.476084+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R1 的 6 条 Strengths 全部同意；2 条 Must-Fix 中 N1（TOST p 值错误归属 CLS–CWM 而实际测的是 CLS–TRAJ）经独立验证完全同意为 critical，N2（CWM 实验条件不利但结论 framing 过于一般化）建议降为 strong warning（论文 body text 已有 hedging，主要问题在 Abstract 缺少 regime qualifier）；4 条 Should-Fix 中 W1/W2/W4 同意，W3（混合精度对 TOST 的影响）我认为被高估并给出了反驳；5 条 Minor 中 M1/M2/M4 同意，M3/M5 部分反驳。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 641 · 2026-05-22T13:55:55.896130+00:00_

Reviewer 1 的交叉回应还未到达，等待中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 55

## Round 55

8 recorded events


### User

_source line 642 · 2026-05-22T13:58:49.938332+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条交叉回应

---

### Strengths 回应

**[AGREE] S1（统计方法论严谨）**：完全同意。TOST 等价检验、clustered bootstrap、ICC、Holm-Bonferroni 校正的组合在 NLP empirical study 中极为少见，这确实是论文最突出的优势。

**[AGREE] S2（Matched experimental design）**：同意控制变量设计合理。

**[AGREE] S3（Failure mode taxonomy）**：同意 Table 4 的实用价值，但补充一点：taxonomy 不仅是 descriptive 的（见 W2 反驳）。

**[AGREE] S4（Threats to Validity 讨论）**：同意。§3.7 的 hedging 确实恰当。

**[AGREE] S5（Appendix 丰富）**：同意。10+ 页附录覆盖了绝大多数可预见的追问。

**[AGREE] S6（写作干净）**：同意。术语一致，claim hedging 恰当。

---

### Weaknesses 逐条回应

**[REBUT] R2-W1: CWM baseline 严重偏弱**

R2 的核心论点是 CWM 的 18–26pp gap 可能主要归因于缺少 execution trace pretraining 而非 formulation 固有缺陷。我认为 R2 **高估了这个问题的严重性**，理由如下：

1. **论文已充分限定**：Abstract 明确写了 "under ≤8B LoRA fine-tuning"；§5 Conclusion 重复了 "under ≤8B LoRA fine-tuning"；Limitations 段明确说 "Our CWM baseline uses ≤8B LoRA fine-tuning, not the original 32B CWM with execution trace mid-training"。R2 要求加上 "without execution trace pretraining" 属于冗余——"≤8B LoRA fine-tuning" 已经逻辑蕴含了没有做 mid-training。

2. **关键证据：parseable CWM 输出的准确率同样很低**：Appendix C (Table 8) 和 §3.5 报告，repo-level CWM 中即使是成功解析的输出，准确率也只有 38–43%（vs. CLS 85%+）。如果问题仅仅是 pretraining 不足导致的 format collapse，那么 parseable 输出的准确率应该接近 CLS。但实际数据显示 parseable CWM 的语义准确率也远低于 CLS，说明问题不仅仅是格式合规，而是 trace generation 本身的复杂性。

3. **Accidental training artifact 提供了强反事实证据**：Appendix H item (c) / §3.5 报告了一个 CWM 模型意外在 CLS 格式数据上训练后，在 repo-level 达到 86.05% 准确率且 0% unparseable。这证明同一模型架构在不需要生成 execution trace 时完全有能力做 repo-level verification。CWM 的失败来自 trace generation 复杂度，而非模型能力不足。

4. **四项 intervention 全部失败**（Appendix N(g)）：增大 LoRA capacity（rank 32→64）、majority voting（k=3）、relaxed matching（I.0–I.4）、model scaling（4B→8B）均未改善 CWM repo-level 性能。如果问题主要是 scale/pretraining 不足，至少 scaling 和 capacity 增加应该有边际收益，但数据显示没有。

5. **R2 要求补充 32B 实验不切实际**：论文的 compute budget 已是 ~370 GPU-hours（Appendix E）。在 ≤8B LoRA 的 scope 内，结论已经被充分 hedge。要求一个审稿修改中加入 32B 实验超出了合理修改范围。

**结论**：R2-W1 应降级为 Should-Fix（在 abstract 加一句关于 parseable accuracy 也低的 caveat 即可），而非 Must-Fix。论文现有 hedging 和证据链已经足够支撑其限定性结论。

---

**[REBUT] R2-W2: Novelty 不足**

R2 的论点是三个发现都"不超越有经验 practitioner 的直觉"。我认为 R2 **误解了部分发现的实质，且对 empirical study 的 novelty 标准要求过高**：

1. **Finding 1 不是 trivial**：R2 说 "当输出是 1 个 token 时，generation ≈ classification"，但这错误描述了 CWM。Function-level CWM 的输出不是 1 个 token——它生成完整的执行输出（§2.1 定义 output cost 为 Σ|oᵢ| tokens），可以是数字、字符串、数据结构等。CWM 在做一个严格更难的任务（预测实际执行输出），却与只做二分类的 CLS 统计等价（TOST p=0.007, ±2pp），这不是直觉能预测的。实际上，如果直觉成立，那 GenRM（R2 自己在 W5 推荐的论文）在数学推理上发现 generative verifier 显著优于 discriminative verifier 就不应该发生——但它发生了。这恰恰说明 formulation 效果是 domain-dependent 的，需要实验验证。

2. **Finding 2 的贡献在于量化和分类，而非现象本身**：R2 说 format collapse "广泛已知"。知道 LLM 有时格式错误 ≠ 知道 repo-level code verification 中 53–74% 输出不可解析、parseable 输出准确率仍比 CLS 低 40pp+、failure modes 可被分为三个独立机制（format collapse / decision collapse / aggregation penalty）。从 "有时出错" 到 "系统性定量分析" 的距离正是 empirical study 的价值所在。

3. **Finding 3 的 re-repair pilot 是诚实的 negative result**：R2 用 re-repair pilot (p=0.42) 来削弱 complementarity 的地位，但这恰恰体现了论文的学术诚信。论文没有声称 complementarity 已经有实际收益——§3.6 的措辞是 "the strongest practical argument for exploring the formulation design space"（强调 exploring）。Negative pilot 结果本身也是有信息量的：它区分了 "structural complementarity" 和 "downstream utility"，这对后续研究有指导意义。

4. **对 empirical study 的 novelty 标准**：R2 要求论文提出 "complexity-aware routing algorithm" 或新的 ablation。但 ARR/EMNLP 的审稿标准并不要求每篇论文都提出新方法。Systematic empirical studies 在顶会中有其定位（如 "Are Emergent Abilities of Large Language Models a Mirage?" NeurIPS 2023 等）。本文的贡献在于方法论驱动的实验设计（TOST + bootstrap + ICC）应用于一个重要的实际问题，而非方法发明。

**结论**：W2 不应为 Must-Fix。论文的 novelty 来自严谨的实验方法论 + 量化发现，这对 EMNLP empirical track 是足够的。但建议作者在 §5 更明确地强调方法论贡献（为什么选 TOST 而非 NHST 等）。

---

**[AGREE] R2-W3: z=−23.7 仅基于 DeepSeek-Coder**

同意这是一个合理的 Should-Fix。Abstract 中确实应标注 "(DeepSeek-Coder)" 以避免读者误认为是跨模型结论。§3.5 的正文虽有解释，但 abstract 是独立阅读的。

不过需要注意：这个限制是数据驱动的（Qwen3 没有 repo-level CWM 评估），不是 cherry-picking。论文在 §3.5 清楚解释了原因。

---

**[AGREE] R2-W4: Oracle routing 缺少 CI**

部分同意。repo-level oracle 95.83% 基于 n=48 variants，应提供 bootstrap CI。但 function-level oracle 90.63% 已在 Appendix H(a) 中有更详细的分析（per-seed breakdown），且 §3.6 明确标注了 "single-seed estimate"。

建议降低 severity：这是 Should-Fix 而非 Must-Fix，因为 oracle 结果在论文中的角色是 motivational（"最强的实际论据是 explore formulation design space"），而非核心 claim。

---

**[AGREE with nuance] R2-W5: 遗漏 GenRM**

同意 GenRM (Zhang et al., ICLR 2025) 是一个重要的相关工作遗漏。它直接比较了 discriminative vs. generative formulation 用于 verification，与本文的 CLS vs. CWM 对比高度相关。

但我不同意 R2 的推论，即 GenRM 的发现 "暗示 generative formulation 在 sufficient scale 下可能优于 classification"。GenRM 在数学推理上的成功恰恰凸显了本文的贡献：代码验证领域呈现了不同的模式（CLS ≥ CWM），这个 domain difference 本身就是有信息量的。引用 GenRM 并讨论这种差异会增强论文的 positioning，而非削弱它。

建议：Should-Fix。在 §4 Related Work 中增加 GenRM 讨论，分析 domain difference（数学推理的输出空间更结构化，代码执行输出更多变）。

对于 CVeDRL 和 GenPRM 两篇，R2 未提供足够信息让我判断其相关性强度，不予评论。

---

**[REBUT] R2-W6: TRAJ 实验设置不公平**

R2 说 TRAJ 用 ~400 variants 训练 vs. CLS/CWM 用 ~70K instances，差距 175×。但论文已在 §3.4 直接回应了这个问题：

1. **Downsample ablation 已经做了**：CLS downsampled 到 TRAJ 的数据量后仍达 80.74%（高于 TRAJ 的 72.91%），且论文承认"this does not control for label granularity"——论文对 confound 的 awareness 是明确的。

2. **数据量差异是 formulation 固有的**：trajectory-level labels 只有 variant 粒度，这不是实验设计缺陷，而是 formulation 的结构性特征。论文在 §3.4 明确指出 "this asymmetry is inherent to the formulation"。

3. **TRAJ 在 function-level 的表现**：TRAJ 在 function-level 达到 86.30% ± 0.97（Table 1），与 CLS 和 CWM 统计等价。如果数据量是主要瓶颈，TRAJ 在 function-level 也应该差——但它没有。

R2 建议的 "data augmentation for TRAJ" 超出了审稿修改的合理范围。这应该是 future work 而非 revision requirement。

**结论**：降级为 Minor。论文对此 confound 的处理已经到位。

---

**[AGREE] R2-W7: §3.5 过度压缩**

同意 §3.5 信息密度过高。但对 §3.3 的压缩建议持保留意见：scaling behavior（4B vs. 8B）虽然只有 2 个 size，但提供了 CWM 不随 scale 改善的关键证据（这反驳了"只是 scale 不够"的假设），不应大幅压缩。

建议：如果需要在 8 页限制内重新分配空间，可以考虑压缩 §3.2 (Function-Level Results) 而非 §3.3，因为 function-level equivalence 的论证相对简洁。

---

**[REBUT] R2-W8: Figure 2 信息冗余**

不同意 Figure 2 冗余。Figure 2 提供的是从 function→repo 的 gap amplification 的视觉直觉——Table 1 和 Table 3 是精确数字，而 Figure 2 的 bar chart 让读者一眼看到 divergence pattern。对于一篇 8 页 empirical study，一张核心 data figure 是必要的。

R2 建议改用 failure mode taxonomy 可视化或 error complementarity Venn diagram，但这些不是论文的核心 claim（core claim 是 "formulation choice is governed by code complexity"），Figure 2 直接支撑这个 claim。

---

**[REBUT] R2-W9: Limitations 段过于简短**

R2 说 Limitations 只有约 10 行、3 个点太少。但：

1. **EMNLP 2026 的要求**：Limitations 章节只需要写一小段覆盖 3 个点左右即可（这是 venue 的 norm），过长的 Limitations 会被视为在 mandatory section 塞入额外内容。

2. **§3.7 Threats to Validity 已覆盖 R2 要求的内容**：synthetic mutation vs. real bug 的 gap 在 §3.7 讨论了（"the coupling effect underlying these results supports relative ranking validity"）；模型家族 generalizability 的限制也在 §3.7 讨论了（"confined to two representative LLM families"）。R2 要求 Limitations 段 "self-contained" 但这会导致与 §3.7 大量重复。

3. **论文实际 Limitations 段覆盖了**：(a) repo-level coverage 有限, (b) synthetic-to-real transfer gap, (c) downsample-to-repair validation。加上 §3.7 的 5 个 confound 讨论，总覆盖面已经很全。

**结论**：不应为 Should-Fix。现有结构（§3.7 + Limitations）已充分覆盖。

---

### Questions 回应

**Q1（GenRM vs. 代码验证的趋势差异）**：好问题。建议作者在修改中讨论。我的初步分析：数学推理的输出空间高度结构化（数字/公式），而代码执行输出高度多变（字符串、数据结构、报错信息），这使得 generation 在代码领域更容易 collapse。

**Q2（Short structured CWM output）**：论文已部分回答——accidental training artifact (Appendix H, item c) 中 CWM 模型在 CLS 格式数据上训练后达到 86.05%/0% unparseable，证明 format 简化确实能恢复性能。但这同时说明此时 CWM 本质上退化成了 CLS，削弱了 generation formulation 的独立价值。

**Q3（re-repair pilot 的影响）**：论文对 complementarity 的定位是 "structural observation + motivation for future work"，不是 "practical method"。re-repair pilot 的 negative result 不影响 structural complementarity 的事实存在（不同 formulation 确实在不同 instance 上出错），只是说明当前的 diagnostic-to-repair pipeline 尚不成熟。

**Q4（Constrained decoding）**：Appendix N(c) 已明确讨论："Constrained decoding could enforce formal compliance but would not address the semantic accuracy deficit among parseable outputs." parseable CWM 输出的准确率仅 38–43%，即使强制格式合规也无法弥补语义准确率差距。

---

### Missing References 回应

**GenRM (Zhang et al., ICLR 2025)**：同意应引用并讨论。见 W5 回应。

**CVeDRL / GenPRM**：无法独立验证这两篇的相关性强度和存在性，不予评论。建议 Director 独立核实。

---

### 总结

R2 的审稿整体质量高，统计和方法论方面的关注点准确。但两个 Must-Fix 的 severity 被高估：

| R2 评级 | 我的评级 | 理由 |
|--------|--------|------|
| W1 Must-Fix | **Should-Fix** | 论文已充分 hedge；parseable accuracy 数据 + accidental artifact 证明问题是 formulation-level 而非 scale-level |
| W2 Must-Fix | **Should-Fix** | 对 empirical study novelty 标准要求过高；三个 findings 中至少 Finding 1 和 Finding 2 的量化分析不是 trivial |
| W3 Should-Fix | **Should-Fix** | 同意 |
| W4 Should-Fix | **Should-Fix** | 同意但 oracle 是 motivational 而非 core claim |
| W5 Should-Fix | **Should-Fix** | 同意 GenRM 应被引用 |
| W6 Should-Fix | **Minor** | 论文已有 downsample ablation |
| W7 Minor | **Minor** | 同意 §3.5 压缩 |
| W8 Minor | **不同意** | Figure 2 直接支撑 core claim |
| W9 Minor | **不同意** | §3.7 + Limitations 已充分覆盖，符合 venue norm |

**核心分歧**：R2 的两个 Must-Fix（W1, W2）如果成立，论文应 borderline reject。但我基于论文中的具体证据（parseable accuracy 38–43%、accidental artifact 86.05%、四项 intervention 全部失败）认为这些问题已被充分 address 或 hedge，不构成 rejection-level 缺陷。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-22T14:04:33.413504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-22T14:04:33.464319+00:00_

1	# === Round 6 Issues ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 6
11	  last_seen_round: 7
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23)."
19	  action_items:
20	    - round: 6
21	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
22	      assigned_to: "paper"
23	      status: in_progress
24	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅. CWM training: DeepSeek s123-v2 ~May 21 09:30, Qwen s123+s456 ~May 22 22:00."
25	  resolution_round: null
26	
27	- id: "R6-N2"
28	  summary: "Checkpoint selection 系统性偏向 CLS"
29	  category: method
30	  severity: critical
31	  status: resolved
32	  first_raised_round: 6
33	  last_seen_round: 7
34	  mentions:
35	    - round: 6
36	      reviewers: [1, 2]
37	      note: "系统性偏差方向与 observed effect 一致。"
38	    - round: 7
39	      reviewers: [pre-review]
40	      note: "Reviewer 确认修复充分。"
41	  action_items:
42	    - round: 6
43	      action: "CLS epoch ablation + matched epoch-3 解释"
44	      assigned_to: "paper"
45	      status: resolved
46	  resolution: "CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4."
47	  resolution_round: 7
48	
49	- id: "R6-N3"
50	  summary: "Oracle ensemble accuracy 数值矛盾"
51	  category: experiment
52	  severity: critical
53	  status: resolved
54	  first_raised_round: 6
55	  last_seen_round: 6
56	  action_items:
57	    - round: 6
58	      action: "核实并统一数字"
59	      assigned_to: "paper"
60	      status: resolved
61	  resolution: "Oracle 90.63% 验证正确。96.03% 已删除。Error direction 6 处修正。"
62	  resolution_round: 7
63	
64	- id: "R6-
…[truncated 7713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-22T14:06:27.799356+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23).\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp, CLS-TRAJ gap <10pp 无法被检验. See also R8-W1.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅. CWM training: DeepSeek s123-v2 ~May 21 09:30, Qwen s123+s456 ~May 22 22:00.\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。Error direction 6 处修正。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 发现概念上可预期\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。Reviewer 复查确认 z=-23.7 在论文 4 处一致。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises: 三个 finding 均未超越 practitioner 直觉. R1 反驳. See R8-W7. 本轮不改 resolved 状态——divergent issue, R1 defense 有理.\"\n  action_items:\n    - round: 6\n      action: \"Reframe + W5 interaction test\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Reframe 完成 + W5 cross-complexity z=-23.7 p<0.001. Cross-model: CWM deficit z=-64.4. 论文 4 处引用一致。\"\n  resolution_round: 7\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 循环论证 + headroom 误导\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"重写 SESOI justification\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"SESOI 基于训练噪声量级独立于 observed gap. Headroom 改绝对值.\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review re-raises: Abstract 仍比 Conclusion 缺 qualifier ('CLS-CWM gap widens to 18-26pp' 无 regime 限定). See R8-C2. 此前 resolved 但当前文本仍有问题，重新打开.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Conclusion 加 ≤8B LoRA qualifier\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol' 限定 repo-level CWM 结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation. n=44, p=0.42 数据来源: Appendix (j).\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W6 re-raises: 175× 数据量差异. R1 反驳 (formulation 固有 + downsample ablation 已做 + TRAJ function-level 表现不差). Director 降级为 minor.\"\n  action_items:\n    - round: 6\n      action: \"讨论 volume vs granularity 区别\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Appendix Threats to Validity 已扩展讨论。待 Round 7 正式验证。\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review: interaction test z=-23.7 已完成但仅 DeepSeek-Coder. R2-W3 + R1 agree: Abstract 需标注 '(DeepSeek-Coder)'. See R8-W4.\"\n  action_items:\n    - round: 6\n      action: \"Mixed-effects regression\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"W5 DeepSeek 已完成 (z=-23.7). 需 CWM multi-seed 后跑完整版。\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"扩展 Andrews/Just 讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"扩展至 ~180 词\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 提出 Aletheia/VeRPO/ExecVerify。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇均已验证真实并加入 Related Work。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 新增遗漏: GenRM (ICLR 2025), RepoExec, Chen et al. Benchmarking Verifiers. See R8-W5.\"\n  action_items:\n    - round: 6\n      action: \"验证并补入 Related Work\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Aletheia + VeRPO (2601.03525) + ExecVerify (2603.11226) 全部加入 Related Work。Agent 确认三篇均真实。\"\n  resolution_round: 7\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出 Transformers ≥4.44, PEFT ≥0.12, PyTorch ≥2.0, bitsandbytes ≥0.43, Python 3.10.\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review R2-W8 称信息冗余, R1 反驳 (直接支撑 core claim). Visual check: bar labels 偏小.\"\n  action_items:\n    - round: 7\n      action: \"CWM multi-seed 后加 error bars + per-model breakdown\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n# --- Critical (Consensus) ---\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 被错误归属于 CLS-CWM（实际测的是 CLS-TRAJ）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical. Abstract/Conclusion 声称 CLS-CWM equivalent (TOST p=0.007, 5 seeds), 但 §3.4 标题 'Per-Test vs Trajectory-Level Equivalence', 正文比较 CLS vs TRAJ, Table 15 Holm-Bonferroni 标注 'CLS vs TRAJ'. 全文无 CLS-CWM 正式 TOST. R2 补充: Abstract 说 5 seeds 但 CLS-CWM 在 DeepSeek 仅 2 seeds.\"\n  action_items:\n    - round: 8\n      action: \"补做 CLS-CWM TOST 并报告 p 值 (gap 0.02-1.24pp, 预期通过 ±2pp margin)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"修正 Abstract/Conclusion 中 p=0.007 的归属 (标注为 CLS-TRAJ 或同时报告两个 TOST)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"Holm-Bonferroni 表加入 CLS-CWM 条目, 更新 k 值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier（与 R6-W2 相关但针对当前文本）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 rated strong warning. Abstract 'CLS-CWM gap widens to 18-26pp' 无 '≤8B LoRA' qualifier. Conclusion 有此 qualifier 但 Abstract 独立阅读时缺失. Director 裁定 critical (修复成本低).\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol' 限定 repo-level 结论\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"§3.5 讨论 early-stopped CWM 对 gap 的影响 (DeepSeek epoch-1 75.45% vs epoch-3 57.31%, gap 缩至 ~9pp)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Should-Fix (Consensus or majority) ---\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 repo-level CLS-TRAJ 比较严重欠 power\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. MDE≈25pp, CLS-TRAJ gap <10pp 无法检验. Conclusion 推荐 CLS 'for both accuracy and throughput' 中 accuracy 部分证据不足.\"\n  action_items:\n    - round: 8\n      action: \"Conclusion 明确 CLS-TRAJ accuracy 比较在 variant-level underpowered, 推荐主要基于 throughput (217×) + per-test 诊断能力\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. Repo-level 95.83% binomial CI ~[85.7%, 99.5%]. Function-level 90.63% 同为单种子. 论文用作 'strongest practical argument' 但不确定性量化缺失.\"\n  action_items:\n    - round: 8\n      action: \"加 bootstrap/binomial CI; Abstract 标注 single-seed; function-level 做多种子 oracle (数据已有)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. DeepSeek CWM epoch-1 75.45% vs epoch-3 57.31% (+18.14pp), 但 Qwen3 (primary family) 无同等消融. 补一个 Qwen3 CWM epoch-1 eval 即可.\"\n  action_items:\n    - round: 8\n      action: \"Qwen3-8B CWM epoch-1 评估 (至少一个种子)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"§3.7 量化 CWM checkpoint selection confound upper bound\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. §3.5 解释了原因 (Qwen3 无 repo-level CWM), 但 Abstract/Intro 未标注.\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 '(DeepSeek-Coder)' 标注 z=-23.7\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (Zhang et al., ICLR 2025) + RepoExec + Chen et al. Benchmarking Verifiers\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意 GenRM must-cite: discriminative vs generative verification, 数学推理上 generative 优于 discriminative, 与本文代码验证结论形成对比. R1 补充: domain difference 有信息量. 另: RepoExec (repo-level benchmark), Chen et al. (verifier formulation comparison). R2 还提 CVeDRL/GenPRM 待核实.\"\n  action_items:\n    - round: 8\n      action: \"§4 Related Work 加入 GenRM 讨论 + domain difference 分析; 引用 RepoExec 和 Chen et al.\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Should-Fix (Divergent — Director 裁定) ---\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training) 削弱 formulation-level 结论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2: Must-Fix (18-26pp gap 可能归因于 pretraining 不足). R1: REBUT Should-Fix (parseable accuracy 38-43% + artifact 86.05% + 四项 intervention 全败 = formulation-level 问题). Director 裁定 Should-Fix.\"\n  action_items:\n    - round: 8\n      action: \"与 R8-C2 合并: Abstract 加更明确 regime 限定\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平——三个 finding 是否超越 practitioner 直觉\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2: Must-Fix (findings trivial, no new method, re-repair p=0.42 削弱 complementarity). R1: REBUT (CWM function-level 非 1-token 输出, 量化分析 ≠ trivial, negative result 有信息量, empirical study novelty 标准不同). Director: 不作独立 Must-Fix, 影响 excitement 评分, Findings track 合适.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# --- Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 REBUT Minor (direction consistent, Appendix O 已讨论). Director 降为 Minor.\"\n  action_items:\n    - round: 8\n      action: \"Appendix 增加 bfloat16 vs NF4 子集均值 gap 对比\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M1 robust SEs (同意), R1-M2 prompt templates (同意), R1-M4 scaling power (同意). 均为低成本修复.\"\n  action_items:\n    - round: 8\n      action: \"Appendix L 加 robust SEs 说明; Appendix 展示每种 formulation 完整 prompt 示例; scaling 标注 exploratory\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23).\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp, CLS-TRAJ gap <10pp 无法被检验. See also R8-W1.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅. CWM training: DeepSeek s123-v2 ~May 21 09:30, Qwen s123+s456 ~May 22 22:00.\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4.\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。Error direction 6 处修正。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 发现概念上可预期\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。Reviewer 复查确认 z=-23.7 在论文 4 处一致。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises: 三个 finding 均未超越 practitioner 直觉. R1 反驳. See R8-W7. 本轮不改 resolved 状态——divergent issue, R1 defense 有理.\"\n  action_items:\n    - round: 6\n      action: \"Reframe + W5 interaction test\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Reframe 完成 + W5 cross-complexity z=-23.7 p<0.001. Cross-model: CWM deficit z=-64.4. 论文 4 处引用一致。\"\n  resolution_round: 7\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 循环论证 + headroom 误导\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"重写 SESOI justification\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"SESOI 基于训练噪声量级独立于 observed gap. Headroom 改绝对值.\"\n  resolution_round: 7\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review re-raises: Abstract 仍比 Conclusion 缺 qualifier ('CLS-CWM gap widens to 18-26pp' 无 regime 限定). See R8-C2. 此前 resolved 但当前文本仍有问题，重新打开.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Conclusion 加 ≤8B LoRA qualifier\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol' 限定 repo-level CWM 结论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation. n=44, p=0.42 数据来源: Appendix (j).\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W6 re-raises: 175× 数据量差异. R1 反驳 (formulation 固有 + downsample ablation 已做 + TRAJ function-level 表现不差). Director 降级为 minor.\"\n  action_items:\n    - round: 6\n      action: \"讨论 volume vs granularity 区别\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"Appendix Threats to Validity 已扩展讨论。待 Round 7 正式验证。\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review: interaction test z=-23.7 已完成但仅 DeepSeek-Coder. R2-W3 + R1 agree: Abstract 需标注 '(DeepSeek-Coder)'. See R8-W4.\"\n  action_items:\n    - round: 6\n      action: \"Mixed-effects regression\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"W5 DeepSeek 已完成 (z=-23.7). 需 CWM multi-seed 后跑完整版。\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"扩展 Andrews/Just 讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"扩展至 ~180 词\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"R2 提出 Aletheia/VeRPO/ExecVerify。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇均已验证真实并加入 Related Work。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review 新增遗漏: GenRM (ICLR 2025), RepoExec, Chen et al. Benchmarking Verifiers. See R8-W5.\"\n  action_items:\n    - round: 6\n      action: \"验证并补入 Related Work\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Aletheia + VeRPO (2601.03525) + ExecVerify (2603.11226) 全部加入 Related Work。Agent 确认三篇均真实。\"\n  resolution_round: 7\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出 Transformers ≥4.44, PEFT ≥0.12, PyTorch ≥2.0, bitsandbytes ≥0.43, Python 3.10.\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review R2-W8 称信息冗余, R1 反驳 (直接支撑 core claim). Visual check: bar labels 偏小.\"\n  action_items:\n    - round: 7\n      action: \"CWM multi-seed 后加 error bars + per-model breakdown\"\n      assigned_to: \"paper\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n# --- Critical (Consensus) ---\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 被错误归属于 CLS-CWM（实际测的是 CLS-TRAJ）\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical. Abstract/Conclusion 声称 CLS-CWM equivalent (TOST p=0.007, 5 seeds), 但 §3.4 标题 'Per-Test vs Trajectory-Level Equivalence', 正文比较 CLS vs TRAJ, Table 15 Holm-Bonferroni 标注 'CLS vs TRAJ'. 全文无 CLS-CWM 正式 TOST. R2 补充: Abstract 说 5 seeds 但 CLS-CWM 在 DeepSeek 仅 2 seeds.\"\n  action_items:\n    - round: 8\n      action: \"补做 CLS-CWM TOST 并报告 p 值 (gap 0.02-1.24pp, 预期通过 ±2pp margin)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"修正 Abstract/Conclusion 中 p=0.007 的归属 (标注为 CLS-TRAJ 或同时报告两个 TOST)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"Holm-Bonferroni 表加入 CLS-CWM 条目, 更新 k 值\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier（与 R6-W2 相关但针对当前文本）\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 rated strong warning. Abstract 'CLS-CWM gap widens to 18-26pp' 无 '≤8B LoRA' qualifier. Conclusion 有此 qualifier 但 Abstract 独立阅读时缺失. Director 裁定 critical (修复成本低).\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol' 限定 repo-level 结论\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"§3.5 讨论 early-stopped CWM 对 gap 的影响 (DeepSeek epoch-1 75.45% vs epoch-3 57.31%, gap 缩至 ~9pp)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Should-Fix (Consensus or majority) ---\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 repo-level CLS-TRAJ 比较严重欠 power\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. MDE≈25pp, CLS-TRAJ gap <10pp 无法检验. Conclusion 推荐 CLS 'for both accuracy and throughput' 中 accuracy 部分证据不足.\"\n  action_items:\n    - round: 8\n      action: \"Conclusion 明确 CLS-TRAJ accuracy 比较在 variant-level underpowered, 推荐主要基于 throughput (217×) + per-test 诊断能力\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. Repo-level 95.83% binomial CI ~[85.7%, 99.5%]. Function-level 90.63% 同为单种子. 论文用作 'strongest practical argument' 但不确定性量化缺失.\"\n  action_items:\n    - round: 8\n      action: \"加 bootstrap/binomial CI; Abstract 标注 single-seed; function-level 做多种子 oracle (数据已有)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. DeepSeek CWM epoch-1 75.45% vs epoch-3 57.31% (+18.14pp), 但 Qwen3 (primary family) 无同等消融. 补一个 Qwen3 CWM epoch-1 eval 即可.\"\n  action_items:\n    - round: 8\n      action: \"Qwen3-8B CWM epoch-1 评估 (至少一个种子)\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 8\n      action: \"§3.7 量化 CWM checkpoint selection confound upper bound\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意. §3.5 解释了原因 (Qwen3 无 repo-level CWM), 但 Abstract/Intro 未标注.\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 '(DeepSeek-Coder)' 标注 z=-23.7\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (Zhang et al., ICLR 2025) + RepoExec + Chen et al. Benchmarking Verifiers\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票同意 GenRM must-cite: discriminative vs generative verification, 数学推理上 generative 优于 discriminative, 与本文代码验证结论形成对比. R1 补充: domain difference 有信息量. 另: RepoExec (repo-level benchmark), Chen et al. (verifier formulation comparison). R2 还提 CVeDRL/GenPRM 待核实.\"\n  action_items:\n    - round: 8\n      action: \"§4 Related Work 加入 GenRM 讨论 + domain difference 分析; 引用 RepoExec 和 Chen et al.\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Should-Fix (Divergent — Director 裁定) ---\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training) 削弱 formulation-level 结论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2: Must-Fix (18-26pp gap 可能归因于 pretraining 不足). R1: REBUT Should-Fix (parseable accuracy 38-43% + artifact 86.05% + 四项 intervention 全败 = formulation-level 问题). Director 裁定 Should-Fix.\"\n  action_items:\n    - round: 8\n      action: \"与 R8-C2 合并: Abstract 加更明确 regime 限定\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平——三个 finding 是否超越 practitioner 直觉\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2: Must-Fix (findings trivial, no new method, re-repair p=0.42 削弱 complementarity). R1: REBUT (CWM function-level 非 1-token 输出, 量化分析 ≠ trivial, negative result 有信息量, empirical study novelty 标准不同). Director: 不作独立 Must-Fix, 影响 excitement 评分, Findings track 合适.\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# --- Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 Should-Fix, R2 REBUT Minor (direction consistent, Appendix O 已讨论). Director 降为 Minor.\"\n  action_items:\n    - round: 8\n      action: \"Appendix 增加 bfloat16 vs NF4 子集均值 gap 对比\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1-M1 robust SEs (同意), R1-M2 prompt templates (同意), R1-M4 scaling power (同意). 均为低成本修复.\"\n  action_items:\n    - round: 8\n      action: \"Appendix L 加 robust SEs 说明; Appendix 展示每种 formulation 完整 prompt 示例; scaling 标注 exploratory\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-22T14:06:27.900506+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 17123}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-22T14:08:59.904152+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
  "report": "# 圆桌审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: Novelty + Completeness + Writing Quality）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation（CLS 分类、CWM 输出生成、TRAJ 轨迹评分），在 matched conditions（≤8B LoRA、相同数据/compute/模型家族）下的效果差异。核心发现：(1) 函数级三种 formulation 统计等价；(2) 仓库级 CLS 大幅优于 CWM（18–26pp），主因 format collapse；(3) 错误互补性暗示集成潜力。统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），附丰富消融和 threats-to-validity 分析。\n\n---\n\n## Strengths（全票共识）\n\n**S1. Matched experimental design 填补重要空白。** 固定模型容量、训练数据、compute 仅改变 formulation，在该领域首次实现真正的 matched comparison。[R1-S1, R2-S2, 全票 AGREE]\n\n**S2. 统计方法论远超同类 empirical study。** 四层工具（clustered bootstrap with ICC=0.191/DEFF=3.97 → TOST with SESOI ±2pp → mixed-effects LPM → Holm-Bonferroni k=4）形成完整证据链。[R1-S2, R2-S1, 全票 AGREE]\n\n**S3. Failure mode taxonomy 有实用价值。** Table 4（format collapse / decision collapse / aggregation penalty）为每种 formulation 的适用边界提供可操作的诊断标准。[R1-S3, R2-S3, 全票 AGREE]\n\n**S4. CWM 退化诊断链有说服力。** 四种干预全部失败 + accidental training artifact（CWM 在 CLS 格式数据上 86.05%/0% unparseable）+ convergence analysis，排除多种替代解释。[R1-S4, R2 implicit, 全票 AGREE]\n\n**S5. Threats to Validity 量化分析罕见。** 五个 confound 逐一量化，worst-case compounding ~11.5pp，显示 18–26pp gap 仍有 ≥7.5pp residual margin。[R1-S5, R2-S4, 全票 AGREE]\n\n**S6. 写作干净、hedging 恰当。** 几乎无 AI 痕迹，术语一致，大量使用 \"under our protocol\"、\"conditional on ≤8B LoRA regime\" 等限定语。[R2-S6, R1 implicit, 全票 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. TOST p=0.007 被错误归属于 CLS–CWM 比较** [R1-N1, R2 独立验证 AGREE]\n\n- Abstract 声称 \"CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)\"\n- Conclusion 给出 \"CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)\"\n- 但 §3.4 标题 \"Per-Test vs. Trajectory-Level Equivalence\"，执行 TOST 对象是 **CLS vs TRAJ**（p=0.007）\n- Table 15 Holm-Bonferroni Rank 2 标注 \"Func: CLS vs TRAJ (TOST ±2pp)\"\n- **全文没有 CLS–CWM 的正式 TOST 检验**\n- R2 补充：Abstract 说 \"5 seeds\" 但 CLS–CWM 在 DeepSeek 仅 2 seeds，Qwen3 虽有 5 seeds 但同样未做 TOST\n- **影响**：论文第一条 contribution 的核心统计证据存在 misattribution。这是事实性错误。\n- **修复路径**：(1) 补做 CLS–CWM TOST（Table 1 gap 仅 0.02–1.24pp，预期通过 ±2pp margin）；(2) 修正 Abstract/Conclusion 中 p 值归属；(3) Holm-Bonferroni 表加入 CLS–CWM 条目并更新 k\n\n**C2. Abstract 对 repo-level CWM 结论缺少 regime qualifier** [R1-N2 Critical, R2 Strong Warning, Director 裁定 Critical]\n\n- CWM 在 repo-level 面临多重系统性劣势：(a) NaN val loss 被迫用 final epoch checkpoint（eval loss 达最优值 1.8×）；(b) max_new_tokens=512 限制有效上下文至 ~1,536 tokens（vs CLS 5,120–8,192）；(c) 原始 CWM（Meta, 32B + execution trace mid-training）与本文 ≤8B LoRA 条件根本不同\n- Abstract 说 \"the CLS–CWM gap widens to 18–26pp\" 但未像 Conclusion 那样加上 \"under ≤8B LoRA fine-tuning\"\n- **分歧**：R1 认为 critical（Abstract 是独立阅读入口），R2 认为 strong warning（body text 已有 hedging，只需 ~5 词修改）\n- **Director 裁定**：保持 critical——修复成本极低但影响大。额外建议：§3.5 讨论 early-stopped CWM 对 gap 的影响（DeepSeek epoch-1 75.45% vs epoch-3 57.31%，gap 从 ~26pp 缩至 ~9pp）\n\n---\n\n### Should-Fix（共识或多数同意）\n\n**W1. n=48 variant 样本量导致 repo-level 比较严重欠 power** [R1-W1, R2 AGREE]\n\nMDE ≈ 25pp，CLS–TRAJ repo-level gap（<10pp）无法被统计检验。Conclusion 推荐 CLS \"for both accuracy and throughput\" 中 accuracy 部分证据不足。建议明确推荐主要基于 throughput（217×）和 per-test 诊断能力，而非 accuracy 优势。\n\n**W2. Oracle 互补性估计为单种子、无置信区间** [R1-W2, R2-W4, 全票 AGREE]\n\nRepo-level oracle 95.83% 在 n=48 上 binomial 95% CI 约 [85.7%, 99.5%]，非常宽。Function-level oracle 90.63% 同为单种子。论文将此作为 \"the strongest practical argument for exploring the formulation design space\"（§1），但不确定性量化缺失。至少应提供 bootstrap/binomial CI 并在 Abstract 标注 \"single-seed estimate\"。Function-level 有 5 种子数据，多种子 oracle 可直接计算。\n\n**W3. CWM checkpoint 消融不对称** [R1-W4, R2 AGREE]\n\nCLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 在 DeepSeek 上 epoch-1 vs epoch-3 差 +18.14pp（75.45% vs 57.31%），但 Qwen3（primary model family）没做同样消融。如果 Qwen3 CWM early-stopped 也达 ~75%，CLS–CWM gap 从 ~18pp 缩至 ~10pp，effect size 定性解读从 \"crushing\" 变为 \"moderate\"。建议补一个 Qwen3 CWM epoch-1 评估。\n\n**W4. z=−23.7 interaction 仅基于 DeepSeek-Coder，Abstract 未标注** [R2-W3, R1 AGREE]\n\n§3.5 明确说明仅用 DeepSeek-Coder（\"the only family with both function- and repo-level CWM evaluations under matched conditions\"），但 Abstract/Introduction 未标注。建议 Abstract 改为 \"a significant interaction (z=−23.7, DeepSeek-Coder)\"。\n\n**W5. 遗漏 GenRM 等关键相关工作** [R2-W5, R1 AGREE on citation]\n\nGenRM (Zhang et al., ICLR 2025) 直接比较 discriminative vs. generative formulation for verification，发现 generative 在数学推理上显著优于 discriminative（GSM8K 73%→93.4%）。与本文 repo-level 代码验证的相反发现形成重要对比。R1 补充：这个 domain difference 本身有信息量，引用并讨论会增强论文 positioning。另遗漏 RepoExec (Ding et al., 2024) 和 Chen et al. (2024) \"Benchmarking LLM-based Verifiers\"。\n\n---\n\n### Should-Fix（有分歧，Director 裁定降级）\n\n**W6. CWM baseline 偏弱削弱核心结论** [R2-W1 Must-Fix, R1 REBUT → Director 裁定 Should-Fix]\n\n- **R2**：≤8B LoRA CWM vs 原始 32B+mid-training 差距根本性，18–26pp gap 可能主要归因于 pretraining 不足\n- **R1 反驳**：(1) parseable CWM 准确率仅 38–43%（vs CLS 85%+），问题不仅是格式；(2) accidental artifact 86.05% 证明同一架构在不需 trace generation 时完全胜任；(3) 四项 intervention 全部失败（rank 增加、majority voting、relaxed matching、model scaling）；(4) 要求 32B 实验超出合理修改范围\n- **Director 裁定**：降为 Should-Fix。R1 引用的 parseable accuracy 和 artifact 证据构成强有力的反事实论证。与 C2 合并处理：Abstract 加明确 regime 限定即可，无需补 32B 实验。\n\n---\n\n### Novelty 分歧（记录，不作为独立 Must-Fix）\n\n**R2-W2: Novelty 不足以达 Conference 水平**\n\n- **R2**：三个 finding 均未超越 practitioner 直觉——(1) 短输出 generation≈classification trivial；(2) 长输出 format collapse 广泛已知；(3) re-repair p=0.42 削弱 complementarity。没有新方法或 surprising insight。\n- **R1 反驳**：(1) CWM function-level 生成完整执行输出非 1 token，与 CLS 等价不是 trivial（GenRM 在数学推理上发现相反结果恰恰说明需要实验验证）；(2) 从 \"有时出错\" 到 \"53–74% unparseable + parseable 准确率比 CLS 低 40pp+\" 的系统性量化是 empirical study 的价值；(3) negative re-repair result 区分了 structural complementarity 和 downstream utility，对后续研究有指导意义\n- **Director 评估**：R2 的 novelty 关切对 main conference 有道理（excitement 2.5 反映了这一点），但 R1 的反驳在 Findings track 语境下成立。论文的价值在于方法论驱动的量化分析。不作为独立 Must-Fix，但影响 excitement 评分和 overall 定位。\n\n---\n\n### Minor\n\n| ID | 问题 | 共识 |\n|----|------|------|\n| M1 | LPM 未报告 robust standard errors（R1-M1）| R2 AGREE |\n| M2 | Prompt templates 未在论文中展示，仅指向 code repo（R1-M2）| R2 AGREE |\n| M3 | Figure 2 y 轴截断 ~55%（R1-M3）| R2 部分 REBUT（caption 已暗示，加一句 \"y-axis begins at 55%\" 即可）|\n| M4 | Scaling 分析 2 种子 power 极低，\"CWM flat scaling\" 应标注 exploratory（R1-M4）| R2 AGREE |\n| M5 | Xia et al. 年份不一致（R1-M5）| R2 需核实 |\n| M6 | §3.5 过度压缩，信息密度过高（R2-W7）| R1 AGREE（但反对压缩 §3.3）|\n| M7 | TOST 混合精度 bfloat16/NF4 交互（R1-W3）| R2 REBUT 降为 Minor（direction consistent），Director 同意降级 |\n| M8 | Figure 2 信息冗余（R2-W8）| R1 REBUT（直接支撑 core claim）|\n| M9 | Limitations 过短（R2-W9）| R1 REBUT（§3.7 已覆盖，符合 EMNLP norm）|\n| M10 | TRAJ 训练数据量差异 175×（R2-W6）| R1 REBUT 降为 Minor（formulation 固有 + downsample ablation 已做）|\n\n---\n\n## Reviewer Consensus\n\n1. **TOST 归属错误是 critical 事实性错误**——两人独立验证，全票同意\n2. **Abstract 需要更强的 regime qualifier**——两人均认为 repo-level 结论表述不够限定\n3. **Oracle 结果需要 CI**——两人均同意至少加 binomial/bootstrap CI\n4. **CWM checkpoint 消融不对称需补充**——两人均同意 Qwen3 CWM epoch-1 评估有价值\n5. **GenRM 是重要遗漏**——两人均同意应在 Related Work 中引用并讨论\n6. **统计方法论和 matched design 是最突出优势**——全票认可\n7. **Findings track (3.0) 适合本文定位**——两人均给 3.0\n\n## Reviewer Divergence\n\n1. **Novelty 是否足够**：R2 认为 Must-Fix（三个 finding 不超越直觉），R1 认为 empirical study 标准下 novelty 足够（量化分析 ≠ trivial）\n2. **CWM baseline 偏弱的严重性**：R2 认为 Must-Fix（可能归因于 scale/pretraining），R1 引用 parseable accuracy + artifact 证据反驳为 Should-Fix\n3. **N2 severity**：R1 认为 critical，R2 认为 strong warning（body text 已有 hedging）\n4. **混合精度对 TOST 的影响**：R1 认为 Should-Fix，R2 认为 Minor（direction consistent + Appendix O）\n5. **TRAJ 训练数据不公平**：R2 认为 Should-Fix，R1 认为 Minor（formulation 固有 + 已有 ablation）\n\n---\n\n## Questions to Authors\n\n**Q1** [共识 — 最高优先级]: TOST p=0.007 究竟是 CLS–CWM 还是 CLS–TRAJ 的结果？CLS–CWM 是否有单独的 TOST 检验？\n\n**Q2** [共识]: Qwen3-8B CWM epoch-1 或 step ~400 checkpoint 的 repo-level 评估结果？\n\n**Q3** [共识]: Oracle 互补性能否扩展到多种子（至少 function-level 有 5 种子数据）？\n\n**Q4** [R2]: GenRM (ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative。如何解释代码验证领域的相反趋势？\n\n**Q5** [R2]: CWM 输出改为 short structured format（如 JSON）后 format collapse 是否会显著减少？\n\n**Q6** [R2]: Re-repair pilot p=0.42 是否意味着 CLS 的 diagnostic advantage 仅是 theoretical？\n\n**Q7** [R1]: Mixed-effects LPM 是否检验过 logistic regression 结果的一致性？\n\n---\n\n## Missing References\n\n| 论文 | 推荐者 | 共识 | 优先级 |\n|------|--------|------|--------|\n| Zhang et al. (2024/2025) \"Generative Verifiers\" (GenRM), ICLR 2025 | R2, R1 同意 | **Must-cite** | 高 |\n| Ding et al. (2024) \"RepoExec\" | R1, R2 同意 | Should-cite | 中 |\n| Chen et al. (2024) \"Benchmarking LLM-based Verifiers\" | R1, R2 同意 | Should-cite | 中 |\n| CVeDRL (2026, arXiv 2601.22803) | R2 | 待核实 | 低 |\n| GenPRM (2025, arXiv 2504.00891) | R2 | 待核实 | 低 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（2026-05-22 13:40–13:43 UTC）| 0 critical, 1 warning, 4 info\n\n| Severity | 位置 | 发现 |\n|----------|------|------|\n| Warning | Page 22 | 附录最后一页仅 ~10% 填充（17 行），~90% 空白。建议合并 Appendix O 或调整附录顺序 |\n| Info | Pages 1-2 | 连续 2 页纯文本无 display item（Abstract + Intro）。Figure 1 在 page 3。ACL 格式常见 |\n| Info | Page 7 | Figure 2 axis/bar labels 偏小（约正文字号 65-70%），建议放大 |\n| Info | Page 4 | Tables 1+2 紧密排布，密度高但可读 |\n| Info | Pages 13-14 | 附录 Tables 5-9 集中 2 页，密度极高但无溢出 |\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（合成）\n\n| 维度 | R1 | R2 | 合成 | 理由 |\n|------|----|----|------|------|\n| **Soundness** | 3.5 | 3.0 | **3.0** | 统计框架整体严谨，但 TOST 误归属（C1）是事实性错误，CWM 比较条件不对等（C2）削弱 formulation-level claims。修复 C1+C2 后可达 3.5+ |\n| **Excitement** | ~3.0 | 2.5 | **2.5** | 研究问题填补实际空白，failure mode taxonomy 有洞察力，但核心发现的 surprise factor 有限（R2 novelty 关切部分成立），结论受限于 ≤8B regime |\n| **Reproducibility** | 4.0 | 4.0 | **4.0** | 超参数完整（Table 11）、compute 明确（~370 GPU-hrs）、承诺 release all。扣分：prompt templates 未在论文中给出，部分 repo-level 结果 seed 数不足 |\n\n### Overall: **3.0 — Findings**\n\n### 判断依据\n\n1. **核心硬伤（C1）修复成本低但影响大**：TOST p 值 misattribution 构成事实性错误，直接影响论文第一条 contribution 的证据基础。预期补做 CLS–CWM TOST 可通过（gap 仅 0.02–1.24pp），但在修复前 soundness 有裂缝。\n\n2. **CWM 比较公平性（C2 + W3 + W6）形成系统性关切**：checkpoint 不对称、context length 不对称、与原始 CWM 设定差距巨大——虽在 body text 中被讨论，但 Abstract 级别 framing 不够谨慎。R1 引用的 parseable accuracy 和 artifact 证据表明问题确实不仅是 scale，但 effect size 的定性解读仍受影响。\n\n3. **Novelty 处于 Findings 合理区间**：matched experimental design + 统计方法论 + failure mode taxonomy 是有价值的 methodological contributions，但三个核心 finding 的 surprise factor 有限。对 main conference 来说 novelty 不够突出，但符合 Findings track 标准。\n\n4. **修复后上限**：修复 C1 + C2 + W1-W5 后，论文可达 **3.5 (Borderline Conference)**。Failure mode taxonomy、interaction 分析（z=−23.7）和 oracle framework 是有价值贡献，但 novelty ceiling 使其难以达到 4.0。\n\n---\n\n## Detailed Comments（按论文结构）\n\n### Abstract\n- **[C1]** \"CLS and CWM are statistically equivalent (TOST, 5 seeds)\" → 需修正为 CLS–TRAJ，或补做 CLS–CWM TOST 后同时报告\n- **[C2]** \"the CLS–CWM gap widens to 18–26pp\" → 加 \"under our ≤8B LoRA protocol\"\n- **[W4]** \"a significant interaction (z=−23.7)\" → 加 \"(DeepSeek-Coder)\"\n- **[W2]** Oracle 数字引用时标注 \"single-seed estimate\"\n\n### §3.4 Per-Test vs. Trajectory-Level Equivalence\n- **[C1]** 补做 CLS–CWM TOST 检验并报告结果\n- **[M7]** 增加 bfloat16 vs NF4 子集的均值 gap 对比数据\n\n### §3.5 Repository-Level Results\n- **[C2]** 增加一段讨论 early-stopped CWM 的 gap 影响（epoch-1 75.45% → gap ~9pp）\n- **[W3]** 补 Qwen3-8B CWM epoch-1 评估\n\n### §3.6 Error Complementarity\n- **[W2]** Oracle 结果加 bootstrap/binomial CI；function-level 做多种子 oracle\n\n### §3.7 Threats to Validity\n- **[W3]** 量化 CWM checkpoint selection confound 的 upper bound\n\n### §4 Related Work\n- **[W5]** 加入 GenRM (Zhang et al., ICLR 2025) 讨论 + domain difference 分析\n- **[W5]** 引用 RepoExec、Chen et al.\n\n### §5 Conclusion\n- **[C1]** 修正 TOST p 值归属\n- **[W1]** CLS 推荐明确基于 throughput + per-test 诊断，非 accuracy 优势\n\n### Appendix\n- **[M2]** 展示每种 formulation 完整 prompt 示例\n- **[M1]** Appendix L 加 robust SEs 说明\n- **[C1]** Holm-Bonferroni 表加入 CLS–CWM 条目，更新 k\n\n### Table 15 (Holm-Bonferroni)\n- **[C1]** 加入 CLS–CWM TOST 行，更新 k 值和 adjusted α"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff",
    "report": "# 圆桌审稿报告 — Round 8 (Fresh Review)\n\n**论文**: \"The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: Novelty + Completeness + Writing Quality）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 1 轮收敛\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free 代码验证 formulation（CLS 分类、CWM 输出生成、TRAJ 轨迹评分），在 matched conditions（≤8B LoRA、相同数据/compute/模型家族）下的效果差异。核心发现：(1) 函数级三种 formulation 统计等价；(2) 仓库级 CLS 大幅优于 CWM（18–26pp），主因 format collapse；(3) 错误互补性暗示集成潜力。统计方法论全面（TOST、clustered bootstrap、mixed-effects LPM、Holm-Bonferroni），附丰富消融和 threats-to-validity 分析。\n\n---\n\n## Strengths（全票共识）\n\n**S1. Matched experimental design 填补重要空白。** 固定模型容量、训练数据、compute 仅改变 formulation，在该领域首次实现真正的 matched comparison。[R1-S1, R2-S2, 全票 AGREE]\n\n**S2. 统计方法论远超同类 empirical study。** 四层工具（clustered bootstrap with ICC=0.191/DEFF=3.97 → TOST with SESOI ±2pp → mixed-effects LPM → Holm-Bonferroni k=4）形成完整证据链。[R1-S2, R2-S1, 全票 AGREE]\n\n**S3. Failure mode taxonomy 有实用价值。** Table 4（format collapse / decision collapse / aggregation penalty）为每种 formulation 的适用边界提供可操作的诊断标准。[R1-S3, R2-S3, 全票 AGREE]\n\n**S4. CWM 退化诊断链有说服力。** 四种干预全部失败 + accidental training artifact（CWM 在 CLS 格式数据上 86.05%/0% unparseable）+ convergence analysis，排除多种替代解释。[R1-S4, R2 implicit, 全票 AGREE]\n\n**S5. Threats to Validity 量化分析罕见。** 五个 confound 逐一量化，worst-case compounding ~11.5pp，显示 18–26pp gap 仍有 ≥7.5pp residual margin。[R1-S5, R2-S4, 全票 AGREE]\n\n**S6. 写作干净、hedging 恰当。** 几乎无 AI 痕迹，术语一致，大量使用 \"under our protocol\"、\"conditional on ≤8B LoRA regime\" 等限定语。[R2-S6, R1 implicit, 全票 AGREE]\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. TOST p=0.007 被错误归属于 CLS–CWM 比较** [R1-N1, R2 独立验证 AGREE]\n\n- Abstract 声称 \"CLS and CWM are statistically equivalent across both families (TOST, 5 seeds)\"\n- Conclusion 给出 \"CLS and CWM are statistically equivalent (TOST p=0.007, 5 seeds)\"\n- 但 §3.4 标题 \"Per-Test vs. Trajectory-Level Equivalence\"，执行 TOST 对象是 **CLS vs TRAJ**（p=0.007）\n- Table 15 Holm-Bonferroni Rank 2 标注 \"Func: CLS vs TRAJ (TOST ±2pp)\"\n- **全文没有 CLS–CWM 的正式 TOST 检验**\n- R2 补充：Abstract 说 \"5 seeds\" 但 CLS–CWM 在 DeepSeek 仅 2 seeds，Qwen3 虽有 5 seeds 但同样未做 TOST\n- **影响**：论文第一条 contribution 的核心统计证据存在 misattribution。这是事实性错误。\n- **修复路径**：(1) 补做 CLS–CWM TOST（Table 1 gap 仅 0.02–1.24pp，预期通过 ±2pp margin）；(2) 修正 Abstract/Conclusion 中 p 值归属；(3) Holm-Bonferroni 表加入 CLS–CWM 条目并更新 k\n\n**C2. Abstract 对 repo-level CWM 结论缺少 regime qualifier** [R1-N2 Critical, R2 Strong Warning, Director 裁定 Critical]\n\n- CWM 在 repo-level 面临多重系统性劣势：(a) NaN val loss 被迫用 final epoch checkpoint（eval loss 达最优值 1.8×）；(b) max_new_tokens=512 限制有效上下文至 ~1,536 tokens（vs CLS 5,120–8,192）；(c) 原始 CWM（Meta, 32B + execution trace mid-training）与本文 ≤8B LoRA 条件根本不同\n- Abstract 说 \"the CLS–CWM gap widens to 18–26pp\" 但未像 Conclusion 那样加上 \"under ≤8B LoRA fine-tuning\"\n- **分歧**：R1 认为 critical（Abstract 是独立阅读入口），R2 认为 strong warning（body text 已有 hedging，只需 ~5 词修改）\n- **Director 裁定**：保持 critical——修复成本极低但影响大。额外建议：§3.5 讨论 early-stopped CWM 对 gap 的影响（DeepSeek epoch-1 75.45% vs epoch-3 57.31%，gap 从 ~26pp 缩至 ~9pp）\n\n---\n\n### Should-Fix（共识或多数同意）\n\n**W1. n=48 variant 样本量导致 repo-level 比较严重欠 power** [R1-W1, R2 AGREE]\n\nMDE ≈ 25pp，CLS–TRAJ repo-level gap（<10pp）无法被统计检验。Conclusion 推荐 CLS \"for both accuracy and throughput\" 中 accuracy 部分证据不足。建议明确推荐主要基于 throughput（217×）和 per-test 诊断能力，而非 accuracy 优势。\n\n**W2. Oracle 互补性估计为单种子、无置信区间** [R1-W2, R2-W4, 全票 AGREE]\n\nRepo-level oracle 95.83% 在 n=48 上 binomial 95% CI 约 [85.7%, 99.5%]，非常宽。Function-level oracle 90.63% 同为单种子。论文将此作为 \"the strongest practical argument for exploring the formulation design space\"（§1），但不确定性量化缺失。至少应提供 bootstrap/binomial CI 并在 Abstract 标注 \"single-seed estimate\"。Function-level 有 5 种子数据，多种子 oracle 可直接计算。\n\n**W3. CWM checkpoint 消融不对称** [R1-W4, R2 AGREE]\n\nCLS 有 checkpoint 消融（epoch 1/val-selected/final，range <1pp）。CWM 在 DeepSeek 上 epoch-1 vs epoch-3 差 +18.14pp（75.45% vs 57.31%），但 Qwen3（primary model family）没做同样消融。如果 Qwen3 CWM early-stopped 也达 ~75%，CLS–CWM gap 从 ~18pp 缩至 ~10pp，effect size 定性解读从 \"crushing\" 变为 \"moderate\"。建议补一个 Qwen3 CWM epoch-1 评估。\n\n**W4. z=−23.7 interaction 仅基于 DeepSeek-Coder，Abstract 未标注** [R2-W3, R1 AGREE]\n\n§3.5 明确说明仅用 DeepSeek-Coder（\"the only family with both function- and repo-level CWM evaluations under matched conditions\"），但 Abstract/Introduction 未标注。建议 Abstract 改为 \"a significant interaction (z=−23.7, DeepSeek-Coder)\"。\n\n**W5. 遗漏 GenRM 等关键相关工作** [R2-W5, R1 AGREE on citation]\n\nGenRM (Zhang et al., ICLR 2025) 直接比较 discriminative vs. generative formulation for verification，发现 generative 在数学推理上显著优于 discriminative（GSM8K 73%→93.4%）。与本文 repo-level 代码验证的相反发现形成重要对比。R1 补充：这个 domain difference 本身有信息量，引用并讨论会增强论文 positioning。另遗漏 RepoExec (Ding et al., 2024) 和 Chen et al. (2024) \"Benchmarking LLM-based Verifiers\"。\n\n---\n\n### Should-Fix（有分歧，Director 裁定降级）\n\n**W6. CWM baseline 偏弱削弱核心结论** [R2-W1 Must-Fix, R1 REBUT → Director 裁定 Should-Fix]\n\n- **R2**：≤8B LoRA CWM vs 原始 32B+mid-training 差距根本性，18–26pp gap 可能主要归因于 pretraining 不足\n- **R1 反驳**：(1) parseable CWM 准确率仅 38–43%（vs CLS 85%+），问题不仅是格式；(2) accidental artifact 86.05% 证明同一架构在不需 trace generation 时完全胜任；(3) 四项 intervention 全部失败（rank 增加、majority voting、relaxed matching、model scaling）；(4) 要求 32B 实验超出合理修改范围\n- **Director 裁定**：降为 Should-Fix。R1 引用的 parseable accuracy 和 artifact 证据构成强有力的反事实论证。与 C2 合并处理：Abstract 加明确 regime 限定即可，无需补 32B 实验。\n\n---\n\n### Novelty 分歧（记录，不作为独立 Must-Fix）\n\n**R2-W2: Novelty 不足以达 Conference 水平**\n\n- **R2**：三个 finding 均未超越 practitioner 直觉——(1) 短输出 generation≈classification trivial；(2) 长输出 format collapse 广泛已知；(3) re-repair p=0.42 削弱 complementarity。没有新方法或 surprising insight。\n- **R1 反驳**：(1) CWM function-level 生成完整执行输出非 1 token，与 CLS 等价不是 trivial（GenRM 在数学推理上发现相反结果恰恰说明需要实验验证）；(2) 从 \"有时出错\" 到 \"53–74% unparseable + parseable 准确率比 CLS 低 40pp+\" 的系统性量化是 empirical study 的价值；(3) negative re-repair result 区分了 structural complementarity 和 downstream utility，对后续研究有指导意义\n- **Director 评估**：R2 的 novelty 关切对 main conference 有道理（excitement 2.5 反映了这一点），但 R1 的反驳在 Findings track 语境下成立。论文的价值在于方法论驱动的量化分析。不作为独立 Must-Fix，但影响 excitement 评分和 overall 定位。\n\n---\n\n### Minor\n\n| ID | 问题 | 共识 |\n|----|------|------|\n| M1 | LPM 未报告 robust standard errors（R1-M1）| R2 AGREE |\n| M2 | Prompt templates 未在论文中展示，仅指向 code repo（R1-M2）| R2 AGREE |\n| M3 | Figure 2 y 轴截断 ~55%（R1-M3）| R2 部分 REBUT（caption 已暗示，加一句 \"y-axis begins at 55%\" 即可）|\n| M4 | Scaling 分析 2 种子 power 极低，\"CWM flat scaling\" 应标注 exploratory（R1-M4）| R2 AGREE |\n| M5 | Xia et al. 年份不一致（R1-M5）| R2 需核实 |\n| M6 | §3.5 过度压缩，信息密度过高（R2-W7）| R1 AGREE（但反对压缩 §3.3）|\n| M7 | TOST 混合精度 bfloat16/NF4 交互（R1-W3）| R2 REBUT 降为 Minor（direction consistent），Director 同意降级 |\n| M8 | Figure 2 信息冗余（R2-W8）| R1 REBUT（直接支撑 core claim）|\n| M9 | Limitations 过短（R2-W9）| R1 REBUT（§3.7 已覆盖，符合 EMNLP norm）|\n| M10 | TRAJ 训练数据量差异 175×（R2-W6）| R1 REBUT 降为 Minor（formulation 固有 + downsample ablation 已做）|\n\n---\n\n## Reviewer Consensus\n\n1. **TOST 归属错误是 critical 事实性错误**——两人独立验证，全票同意\n2. **Abstract 需要更强的 regime qualifier**——两人均认为 repo-level 结论表述不够限定\n3. **Oracle 结果需要 CI**——两人均同意至少加 binomial/bootstrap CI\n4. **CWM checkpoint 消融不对称需补充**——两人均同意 Qwen3 CWM epoch-1 评估有价值\n5. **GenRM 是重要遗漏**——两人均同意应在 Related Work 中引用并讨论\n6. **统计方法论和 matched design 是最突出优势**——全票认可\n7. **Findings track (3.0) 适合本文定位**——两人均给 3.0\n\n## Reviewer Divergence\n\n1. **Novelty 是否足够**：R2 认为 Must-Fix（三个 finding 不超越直觉），R1 认为 empirical study 标准下 novelty 足够（量化分析 ≠ trivial）\n2. **CWM baseline 偏弱的严重性**：R2 认为 Must-Fix（可能归因于 scale/pretraining），R1 引用 parseable accuracy + artifact 证据反驳为 Should-Fix\n3. **N2 severity**：R1 认为 critical，R2 认为 strong warning（body text 已有 hedging）\n4. **混合精度对 TOST 的影响**：R1 认为 Should-Fix，R2 认为 Minor（direction consistent + Appendix O）\n5. **TRAJ 训练数据不公平**：R2 认为 Should-Fix，R1 认为 Minor（formulation 固有 + 已有 ablation）\n\n---\n\n## Questions to Authors\n\n**Q1** [共识 — 最高优先级]: TOST p=0.007 究竟是 CLS–CWM 还是 CLS–TRAJ 的结果？CLS–CWM 是否有单独的 TOST 检验？\n\n**Q2** [共识]: Qwen3-8B CWM epoch-1 或 step ~400 checkpoint 的 repo-level 评估结果？\n\n**Q3** [共识]: Oracle 互补性能否扩展到多种子（至少 function-level 有 5 种子数据）？\n\n**Q4** [R2]: GenRM (ICLR 2025) 发现 generative verifier 在数学推理上优于 discriminative。如何解释代码验证领域的相反趋势？\n\n**Q5** [R2]: CWM 输出改为 short structured format（如 JSON）后 format collapse 是否会显著减少？\n\n**Q6** [R2]: Re-repair pilot p=0.42 是否意味着 CLS 的 diagnostic advantage 仅是 theoretical？\n\n**Q7** [R1]: Mixed-effects LPM 是否检验过 logistic regression 结果的一致性？\n\n---\n\n## Missing References\n\n| 论文 | 推荐者 | 共识 | 优先级 |\n|------|--------|------|--------|\n| Zhang et al. (2024/2025) \"Generative Verifiers\" (GenRM), ICLR 2025 | R2, R1 同意 | **Must-cite** | 高 |\n| Ding et al. (2024) \"RepoExec\" | R1, R2 同意 | Should-cite | 中 |\n| Chen et al. (2024) \"Benchmarking LLM-based Verifiers\" | R1, R2 同意 | Should-cite | 中 |\n| CVeDRL (2026, arXiv 2601.22803) | R2 | 待核实 | 低 |\n| GenPRM (2025, arXiv 2504.00891) | R2 | 待核实 | 低 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（2026-05-22 13:40–13:43 UTC）| 0 critical, 1 warning, 4 info\n\n| Severity | 位置 | 发现 |\n|----------|------|------|\n| Warning | Page 22 | 附录最后一页仅 ~10% 填充（17 行），~90% 空白。建议合并 Appendix O 或调整附录顺序 |\n| Info | Pages 1-2 | 连续 2 页纯文本无 display item（Abstract + Intro）。Figure 1 在 page 3。ACL 格式常见 |\n| Info | Page 7 | Figure 2 axis/bar labels 偏小（约正文字号 65-70%），建议放大 |\n| Info | Page 4 | Tables 1+2 紧密排布，密度高但可读 |\n| Info | Pages 13-14 | 附录 Tables 5-9 集中 2 页，密度极高但无溢出 |\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（合成）\n\n| 维度 | R1 | R2 | 合成 | 理由 |\n|------|----|----|------|------|\n| **Soundness** | 3.5 | 3.0 | **3.0** | 统计框架整体严谨，但 TOST 误归属（C1）是事实性错误，CWM 比较条件不对等（C2）削弱 formulation-level claims。修复 C1+C2 后可达 3.5+ |\n| **Excitement** | ~3.0 | 2.5 | **2.5** | 研究问题填补实际空白，failure mode taxonomy 有洞察力，但核心发现的 surprise factor 有限（R2 novelty 关切部分成立），结论受限于 ≤8B regime |\n| **Reproducibility** | 4.0 | 4.0 | **4.0** | 超参数完整（Table 11）、compute 明确（~370 GPU-hrs）、承诺 release all。扣分：prompt templates 未在论文中给出，部分 repo-level 结果 seed 数不足 |\n\n### Overall: **3.0 — Findings**\n\n### 判断依据\n\n1. **核心硬伤（C1）修复成本低但影响大**：TOST p 值 misattribution 构成事实性错误，直接影响论文第一条 contribution 的证据基础。预期补做 CLS–CWM TOST 可通过（gap 仅 0.02–1.24pp），但在修复前 soundness 有裂缝。\n\n2. **CWM 比较公平性（C2 + W3 + W6）形成系统性关切**：checkpoint 不对称、context length 不对称、与原始 CWM 设定差距巨大——虽在 body text 中被讨论，但 Abstract 级别 framing 不够谨慎。R1 引用的 parseable accuracy 和 artifact 证据表明问题确实不仅是 scale，但 effect size 的定性解读仍受影响。\n\n3. **Novelty 处于 Findings 合理区间**：matched experimental design + 统计方法论 + failure mode taxonomy 是有价值的 methodological contributions，但三个核心 finding 的 surprise factor 有限。对 main conference 来说 novelty 不够突出，但符合 Findings track 标准。\n\n4. **修复后上限**：修复 C1 + C2 + W1-W5 后，论文可达 **3.5 (Borderline Conference)**。Failure mode taxonomy、interaction 分析（z=−23.7）和 oracle framework 是有价值贡献，但 novelty ceiling 使其难以达到 4.0。\n\n---\n\n## Detailed Comments（按论文结构）\n\n### Abstract\n- **[C1]** \"CLS and CWM are statistically equivalent (TOST, 5 seeds)\" → 需修正为 CLS–TRAJ，或补做 CLS–CWM TOST 后同时报告\n- **[C2]** \"the CLS–CWM gap widens to 18–26pp\" → 加 \"under our ≤8B LoRA protocol\"\n- **[W4]** \"a significant interaction (z=−23.7)\" → 加 \"(DeepSeek-Coder)\"\n- **[W2]** Oracle 数字引用时标注 \"single-seed estimate\"\n\n### §3.4 Per-Test vs. Trajectory-Level Equivalence\n- **[C1]** 补做 CLS–CWM TOST 检验并报告结果\n- **[M7]** 增加 bfloat16 vs NF4 子集的均值 gap 对比数据\n\n### §3.5 Repository-Level Results\n- **[C2]** 增加一段讨论 early-stopped CWM 的 gap 影响（epoch-1 75.45% → gap ~9pp）\n- **[W3]** 补 Qwen3-8B CWM epoch-1 评估\n\n### §3.6 Error Complementarity\n- **[W2]** Oracle 结果加 bootstrap/binomial CI；function-level 做多种子 oracle\n\n### §3.7 Threats to Validity\n- **[W3]** 量化 CWM checkpoint selection confound 的 upper bound\n\n### §4 Related Work\n- **[W5]** 加入 GenRM (Zhang et al., ICLR 2025) 讨论 + domain difference 分析\n- **[W5]** 引用 RepoExec、Chen et al.\n\n### §5 Conclusion\n- **[C1]** 修正 TOST p 值归属\n- **[W1]** CLS 推荐明确基于 throughput + per-test 诊断，非 accuracy 优势\n\n### Appendix\n- **[M2]** 展示每种 formulation 完整 prompt 示例\n- **[M1]** Appendix L 加 robust SEs 说明\n- **[C1]** Holm-Bonferroni 表加入 CLS–CWM 条目，更新 k\n\n### Table 15 (Holm-Bonferroni)\n- **[C1]** 加入 CLS–CWM TOST 行，更新 k 值和 adjusted α"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-22T14:09:04.019943+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4115
}
```

</details>

---


### Assistant

_source line 649 · 2026-05-22T14:09:13.402095+00:00_

---

**圆桌审稿报告已投递。**

本轮审稿要点：

**2 条 Critical Must-Fix**：
- **C1**：TOST p=0.007 被错误归属为 CLS–CWM 结果（实际是 CLS–TRAJ），全文无 CLS–CWM 正式 TOST 检验。两位 Reviewer 独立验证一致。
- **C2**：Abstract 对 repo-level CWM 结论缺少 "≤8B LoRA" regime qualifier。

**5 条共识 Should-Fix**：n=48 underpowered、Oracle 无 CI、CWM checkpoint 消融不对称、z=-23.7 未标注 DeepSeek-only、遗漏 GenRM。

**2 条核心分歧**（已充分记录）：
- R2 认为 CWM baseline 偏弱构成 Must-Fix，R1 引用 parseable accuracy + artifact 证据反驳→Director 裁定 Should-Fix
- R2 认为 novelty 不足以达 Conference 水平，R1 反驳 empirical study 标准下 novelty 足够→Director 不作独立 Must-Fix，影响 excitement 评分

**Overall：3.0（Findings）**，修复 C1+C2 后上限 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 650 · 2026-05-22T14:09:15.975542+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：R2 的审稿质量高，但两个 Must-Fix（W1 CWM baseline 偏弱、W2 novelty 不足）的 severity 被高估。

- **W1**：论文已通过 parseable accuracy 数据（38–43% vs CLS 85%+）和 accidental training artifact（86.05%/0% unparseable）充分证明 gap 来自 formulation-level trace generation 复杂度，而非 scale/pretraining 不足。四项 intervention 全部失败进一步支撑这一点。建议降为 Should-Fix。
- **W2**：R2 误解了 Finding 1（CWM 不是单 token 输出）和 Finding 2（量化分析 ≠ 直觉已知）。对 empirical study 要求提出新算法超出了文体定位。建议降为 Should-Fix。
- **W3–W5**：同意为 Should-Fix。
- **W6–W9**：部分降级或不同意。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 651 · 2026-05-22T14:09:27.107157+00:00_

审稿报告已成功投递给 Research Director。

**本轮审稿总结**：

- **Overall: 3.0（Findings）**
- **2 条 Must-Fix**：C1 TOST p=0.007 误归属（全票共识 critical）、C2 Abstract 缺 regime qualifier（Director 裁定 critical）
- **7 条 Should-Fix**：n=48 欠 power、Oracle 无 CI、CWM checkpoint 消融不对称、z=-23.7 仅 DeepSeek 未标注、GenRM 遗漏、CWM baseline 偏弱（降级）、混合精度（降级）
- **核心分歧**：Novelty 是否足够（R2 Must-Fix vs R1 反驳），Director 不作独立 Must-Fix 但反映在 excitement 2.5 评分中
- **修复后上限**：3.5（Borderline Conference）

Issue Tracker 已同步更新（13 条新增/更新条目）。视觉审查结果（1 warning + 4 info）已纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 57

## Round 57

62 recorded events


### User

_source line 652 · 2026-05-22T14:46:56.203669+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 653 · 2026-05-22T14:47:03.672634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 654 · 2026-05-22T14:47:03.723841+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-22T14:47:08.894480+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-22T14:47:08.945236+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 657 · 2026-05-22T14:47:12.358963+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-22T14:47:12.810966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-22T14:47:14.417385+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s123-eval-1epoch | Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。 | — | — | — |\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- 
…[truncated 1818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2058
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-22T14:47:14.467975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-22T14:47:14.669167+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{The Formulation Design Space for Execution-Free Code Verification:\\A Systematic Empirical Study}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline. Note: $y$-axis begins at 55\% to emphasize formulation differences.}
58	\label{fig:scaling_
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-22T14:47:21.702827+00:00_

Web search results for query: "EMNLP 2026 ACL Rolling Review call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about EMNLP 2026 submission guidelines and ACL Rolling Review:

## EMNLP 2026 Overview

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

## Submission Process

Authors will follow a two-step process: Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; Authors commit their reviewed articles to a publication venue (e.g., EMNLP 2026), where Senior Area Chairs and P
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 8891
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-22T14:47:27.423871+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines anonymity policy appendix rules page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines anonymity policy appendix rules page limit"
  }
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-22T14:47:29.008678+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-22T14:47:29.360403+00:00_

-rw-r--r-- 1 ubuntu ubuntu 424746 May 22 14:42 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-22T14:47:29.461170+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-22T14:47:40.902449+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines anonymity policy appendix rules page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Now let me search for more specific information about page limits and appendix rules:

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLP
…[truncated 2641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 13478
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-22T14:47:40.953190+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11492
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-22T14:47:54.456533+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-22T14:47:54.457034+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-22T14:47:57.819956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-22T14:47:58.784403+00:00_

1	# === Round 6 Issues (Original) ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 6
11	  last_seen_round: 8
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress. Blocked on CWM data (~May 22-23)."
19	    - round: 8
20	      reviewers: [1, 2]
21	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp, CLS-TRAJ gap <10pp 无法被检验. See also R8-W1."
22	  action_items:
23	    - round: 6
24	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
25	      assigned_to: "paper"
26	      status: in_progress
27	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅. CWM 3-seed ✅ (Qwen s42/s123/s456, DS s42/s123/s456). Table 3 filled."
28	  resolution_round: null
29	
30	- id: "R6-N2"
31	  summary: "Checkpoint selection 系统性偏向 CLS"
32	  category: method
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 6
36	  last_seen_round: 7
37	  mentions:
38	    - round: 6
39	      reviewers: [1, 2]
40	      note: "系统性偏差方向与 observed effect 一致。"
41	    - round: 7
42	      reviewers: [pre-review]
43	      note: "Reviewer 确认修复充分。"
44	  action_items:
45	    - round: 6
46	      action: "CLS epoch ablation + matched epoch-3 解释"
47	      assigned_to: "paper"
48	      status: resolved
49	  resolution: "CLS epoch ablation <1pp range. Matched epoch-3 cross-model gap ~2pp. Written in §4.4."
50	  resolution_round: 7
51	
52	- id: "R6-N3"
53	  summary: "Oracle ensemble accuracy 数值矛盾"
54	  category: experiment
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 6
58	  last_seen_round: 6
59	  action_items:
60	    - round: 6
61	      action: "核实并统一数字"
62	     
…[truncated 16251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 964
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-22T14:47:58.784775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 674 · 2026-05-22T14:47:59.236584+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 675 · 2026-05-22T14:47:59.236994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 676 · 2026-05-22T14:47:59.438016+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimenta
…[truncated 2705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 677 · 2026-05-22T14:47:59.438387+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-22T14:47:59.488888+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-22T14:48:07.455821+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-22T14:48:07.506744+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation design space for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss due to length-mismatched sequences, which defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check, we additionally fine-tune DeepSeek-Coder-6.7B~\cite{guo2024deepseekcoder} with identical LoRA configuration (2 seeds each for \cls{} and \cwm{}). Our \cwm{} baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Mo
…[truncated 20130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-22T14:48:07.708039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-22T14:48:08.110032+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. Verification formulations span trajectory-level reward~\cite{shum2025swerm,zhu2026codescaler}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} shows that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formulation (\cwm{}) does not outperform the discriminative one (\cls{}), suggesting that the generation advantage may be domain
…[truncated 1498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-22T14:48:08.261194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-22T14:48:08.362022+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} parity is model-dependent. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}).
5	
6	Three directions follow. First, oracle gains motivate complexity-aware routing; the failure mode taxonomy provides candidate routing features. Second, the generation bottleneck is semantic---four interventions fail (Appendix~\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Repo-level \cwm{} uses 3 seeds per model (Qwen3-8B, DeepSeek-6.7B); the gap (18--26\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds mean definitive causal attribution requires further replication. Our \cwm{} baseline uses ${\leq}$8B LoRA fine-
…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-22T14:48:14.888538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-22T14:48:15.190984+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: limited seed coverage for repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and seed coverage.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified 
…[truncated 4347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 687 · 2026-05-22T14:48:15.191485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 688 · 2026-05-22T14:48:15.343259+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage).}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by the $T \geq 2$ minority. Block correlat
…[truncated 12583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-22T14:48:22.773000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-22T14:48:22.824084+00:00_

200	\small
201	\caption{Training hyperparameters for \cls{}/\cwm{} configurations. \traj{} models use lr $= 2{\times}10^{-4}$ due to the smaller training set (${\sim}$8K function-level instances vs.\ ${\sim}$70K for \cls{}/\cwm{}); other hyperparameters are shared.}
202	\label{tab:hyperparams}
203	\resizebox{\columnwidth}{!}{%
204	\begin{tabular}{ll}
205	\toprule
206	\multicolumn{2}{l}{\textbf{Shared across all configurations}} \\
207	\midrule
208	LoRA rank / alpha / dropout & 16 / 32 / 0.05 \\
209	LoRA targets & \texttt{q/k/v/o\_proj} \\
210	Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.999$) \\
211	LR scheduler & Linear \\
212	Effective batch size & 32 \\
213	Max sequence length & 2,048 \\
214	Epochs & 3 \\
215	Precision & bf16 \\
216	Gradient checkpointing & \checkmark \\
217	Seeds (function) & \{42, 123, 456, 789, 0\}\textsuperscript{$b$} \\
218	Seeds (repo) & \{42, 123, 456\}\textsuperscript{$c$} \\
219	\bottomrule
220	\end{tabular}}
221	
222	\vspace{6pt}
223	
224	\resizebox{\columnwidth}{!}{%
225	\begin{tabular}{lccc}
226	\toprule
227	\multicolumn{4}{l}{\textbf{Model-family--specific parameters}} \\
228	\midrule
229	& \textbf{Qwen3-4B} & \textbf{Qwen3-8B} & \textbf{DS-6.7B} \\
230	\midrule
231	Learning rate & 5e-5 & 5e-5 & 2e-4 \\
232	Weight decay & 0.01 & 0.01 & 0.0 \\
233	Warmup ratio & 0.05 & 0.05 & 0.1 \\
234	Batch / grad.\ accum.\ (\cls{}) & 2 / 16 & 1 / 32 & 2 / 16 \\
235	Batch / grad.\ accum.\ (\cwm{}) & 1 / 32 & 1 / 32 & 1 / 32 \\
236	Training samples & 70,748 & 70,748 & 67,343--70,748\textsuperscript{$a$} \\
237	\bottomrule
238	\end{tabular}}
239	
240	\vspace{2pt}
241	{\footnotesize $^a$DeepSeek \cls{} canonical run (s42) uses drop preprocessing, which excludes 3,405 sequences exceeding max length (67,343 of 70,748). The s123 run uses truncate preprocessing (70,748 samples) but produces NaN validation loss. See \S\ref{sec:setup}. $^b$Seeds 789 and 0 use NF4 quantization; others use bf16. $^c$Repo-level seed coverage varies by configuration; see Tab
…[truncated 23940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 691 · 2026-05-22T14:48:27.391731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "499",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "499",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 692 · 2026-05-22T14:48:27.392475+00:00_

499	We fit mixed-effects linear probability models (LPM) with heteroskedasticity-robust standard errors (HC1) to test the formulation$\times$complexity interaction formally. We choose LPM because coefficients are directly interpretable as probability differences (percentage points), consistent with the reporting units in the main text; at these sample sizes ($n{\approx}56$K cross-complexity, repo-level pooled cross-model) and base rate range (0.6--0.9), LPM and logistic regression yield identical significance conclusions~\cite{angrist2009mostly}.
500	
501	\paragraph{Cross-complexity model (DeepSeek-Coder).} \texttt{correct $\sim$ formulation $\times$ complexity + (1|problem\_id)}, $n{=}56{,}480$ observations (\cls{} + \cwm{} $\times$ function + repo), 139 problem clusters. The \cwm{} main effect at function level is non-significant ($\hat{\beta}{=}-0.002$, $z{=}-0.25$, $p{=}0.805$); the \cwm{}$\times$repo interaction is highly significant ($\hat{\beta}{=}-0.219$, $z{=}-23.7$, $p{<}0.001$). \cwm{} and \cls{} are statistically indistinguishable at function level ($\Delta{=}-0.2$\pp{}, $p{=}0.805$) but diverge by 22\pp{} at repo level, confirming the complexity-dependent divergence is not an artifact of aggregation.
502	
503	\paragraph{Repo-level cross-model model.} \texttt{correct $\sim$ formulation $\times$ model + (1|problem\_id)}, both model families, repo level only. \cwm{} deficit: $\hat{\beta}{=}-0.22$ ($-$22\pp{}, $z{=}-64.4$, $p{<}0.001$). Model effect: +1.1\pp{} for Qwen3 ($z{=}3.1$, $p{=}0.002$). Formulation$\times$model interaction: +1.6\pp{} less \cwm{} degradation on Qwen3 ($z{=}2.8$, $p{=}0.006$). Formulation explains $>$95\% of the predictable variance; model identity modulates gap magnitude without changing direction. The 25-cluster random intercept structure limits effective degrees of freedom for the random effects; inferences on fixed effects (formulation, complexity) are robust as they pool across the full observation count.
504	
505	\section{CWM P
…[truncated 11406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-22T14:48:38.911691+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf 2>/dev/null | grep -i pages",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf 2>/dev/null | grep -i pages",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-22T14:48:38.962385+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-22T14:48:39.013049+00:00_

Pages:           22

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-22T14:48:39.615625+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s123-eval-1epoch | Eval DeepSeek CWM repo-level s123 1-epoch checkpoint (checkpoint-4209)。验证 appendix cwm_convergence 中引用的 early-stopping 数据 (75.45% acc / 66.4% unparseable) 是否在干净 eval 下可复现。 | — | — | — |\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- 
…[truncated 1818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-22T14:48:47.396057+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/exec-sim-repair-verifier/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/exec-sim-repair-verifier/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-22T14:48:47.446628+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 699 · 2026-05-22T14:48:47.547473+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/exec-sim-repair-verifier/**/project*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/exec-sim-repair-verifier/**/project*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16"
  }
}
```

</details>

---


### Tool result

_source line 700 · 2026-05-22T14:48:47.598420+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 701 · 2026-05-22T14:48:50.258468+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 702 · 2026-05-22T14:48:50.309157+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-22T14:49:17.796754+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-22T14:49:17.947842+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-22T14:49:20.518118+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch visual check",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch visual check",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-22T14:49:20.568686+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 707 · 2026-05-22T14:49:26.592951+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 708 · 2026-05-22T14:49:44.474008+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 17881
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-22T14:49:44.625490+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（long paper），参考文献不限\n- **Limitations**: 必须有，不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（不能出现作者身份信息）\n- **附录**: 允许，随论文提交，Reviewer 可选择是否阅读\n\n## 论文路径\n- LaTeX: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（及其 `\\input` 的各子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**实验设计与统计方法**：\n1. **统计检验的正确性**：TOST 等价检验的参数选择（±2pp SESOI）是否合理？clustered bootstrap 的实施（114 clusters, 10K resamples）是否正确？Holm-Bonferroni 校正（k=5）是否恰当？ICC/DEFF 的使用是否正确？\n2. **实验设计的公平性**：三种 formulation 的训练条件（数据量、超参数、checkpoint selection）是否真正 matched？TRAJ 的 ~400 样本 vs CLS/CWM 的 ~70K 是否构成致命 confound？CWM 使用 ≤8B LoRA 而非原始 32B CWM 是否公平？\n3. **Claims 与证据的匹配**：每个 claim 是否有充分的统计支撑？特别注意 n=48 variant-level 比较的 power、single-seed estimates（oracle）、cross-model 结论基于 2-seed 的可靠性。\n4. **Threats to Validity**：§5.5 识别的 5 个 confound 是否充分？是否遗漏了重要 confound？confound 之间的相关性讨论是否充分？\n5. **可复现性**：超参数报告是否完整？实验条件是否可复现？数据处理流程是否透明？\n\n**输出格式**：\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的方法论相关文献）\n- Overall Assessment（1-5 分，参照 ARR 标准）+ Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（long paper），参考文献不限\n- **Limitations**: 必须有，不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（不能出现作者身份信息）\n- **附录**: 允许，随论文提交，Reviewer 可选择是否阅读\n\n## 论文路径\n- LaTeX: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（及其 `\\input` 的各子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**实验设计与统计方法**：\n1. **统计检验的正确性**：TOST 等价检验的参数选择（±2pp SESOI）是否合理？clustered bootstrap 的实施（114 clusters, 10K resamples）是否正确？Holm-Bonferroni 校正（k=5）是否恰当？ICC/DEFF 的使用是否正确？\n2. **实验设计的公平性**：三种 formulation 的训练条件（数据量、超参数、checkpoint selection）是否真正 matched？TRAJ 的 ~400 样本 vs CLS/CWM 的 ~70K 是否构成致命 confound？CWM 使用 ≤8B LoRA 而非原始 32B CWM 是否公平？\n3. **Claims 与证据的匹配**：每个 claim 是否有充分的统计支撑？特别注意 n=48 variant-level 比较的 power、single-seed estimates（oracle）、cross-model 结论基于 2-seed 的可靠性。\n4. **Threats to Validity**：§5.5 识别的 5 个 confound 是否充分？是否遗漏了重要 confound？confound 之间的相关性讨论是否充分？\n5. **可复现性**：超参数报告是否完整？实验条件是否可复现？数据处理流程是否透明？\n\n**输出格式**：\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的方法论相关文献）\n- Overall Assessment（1-5 分，参照 ARR 标准）+ Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 710 · 2026-05-22T14:49:56.754379+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12128
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-22T14:49:56.905351+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（long paper），参考文献不限\n- **Limitations**: 必须有，不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（不能出现作者身份信息）\n- **附录**: 允许，随论文提交，Reviewer 可选择是否阅读\n\n## 论文路径\n- LaTeX: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（及其 `\\input` 的各子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性、完整性与写作质量**：\n1. **Contribution Novelty**：三种 formulation 的系统比较是否构成足够的贡献？\"function-level equivalence\" 和 \"repo-level divergence\" 是否超越 practitioner 直觉？failure mode taxonomy 和 error complementarity 的价值？对 EMNLP 2026 Main/Findings 的定位是否恰当？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注：(a) generative verification/GenRM 方向, (b) code verification 最新工作（2025-2026）, (c) process vs outcome supervision 文献, (d) repo-level code understanding 基准。是否有引用存疑或幻觉引用？\n3. **写作质量**：Abstract 是否准确反映论文内容和 claims 强度？叙事结构是否清晰？claims 的 qualifier 是否充分（特别是 ≤8B LoRA regime 的限定）？术语使用是否一致？\n4. **格式合规**：是否满足 8 页正文限制？Figure/Table 排版质量？References 格式？Checklist 是否完整？匿名性是否满足 double-blind？\n5. **Completeness**：实验是否覆盖了论文 claims 所需的全部条件？是否有明显的实验空白？Appendix 信息是否应移入正文？\n\n**输出格式**：\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的相关工作）\n- Overall Assessment（1-5 分，参照 ARR 标准）+ Confidence（1-5）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **截止日期**: 2026-05-25\n- **正文页数限制**: 8 页（long paper），参考文献不限\n- **Limitations**: 必须有，不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（不能出现作者身份信息）\n- **附录**: 允许，随论文提交，Reviewer 可选择是否阅读\n\n## 论文路径\n- LaTeX: `projects/exec-sim-repair-verifier/docs/paper/main.tex`（及其 `\\input` 的各子文件）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_7/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性、完整性与写作质量**：\n1. **Contribution Novelty**：三种 formulation 的系统比较是否构成足够的贡献？\"function-level equivalence\" 和 \"repo-level divergence\" 是否超越 practitioner 直觉？failure mode taxonomy 和 error complementarity 的价值？对 EMNLP 2026 Main/Findings 的定位是否恰当？\n2. **Related Work 覆盖**：是否遗漏重要相关工作？特别关注：(a) generative verification/GenRM 方向, (b) code verification 最新工作（2025-2026）, (c) process vs outcome supervision 文献, (d) repo-level code understanding 基准。是否有引用存疑或幻觉引用？\n3. **写作质量**：Abstract 是否准确反映论文内容和 claims 强度？叙事结构是否清晰？claims 的 qualifier 是否充分（特别是 ≤8B LoRA regime 的限定）？术语使用是否一致？\n4. **格式合规**：是否满足 8 页正文限制？Figure/Table 排版质量？References 格式？Checklist 是否完整？匿名性是否满足 double-blind？\n5. **Completeness**：实验是否覆盖了论文 claims 所需的全部条件？是否有明显的实验空白？Appendix 信息是否应移入正文？\n\n**输出格式**：\n- Strengths（逐条）\n- Weaknesses（逐条，标注 [Must-Fix] / [Should-Fix] / [Minor]）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的相关工作）\n- Overall Assessment（1-5 分，参照 ARR 标准）+ Confidence（1-5）"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-22T14:49:58.269847+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 713 · 2026-05-22T14:50:10.575944+00:00_

已完成 Round 9 初始化：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（fire-and-forget） |
| Reviewer 1（方法严谨性） | ✅ 已分配，独立审稿中 |
| Reviewer 2（新颖性/完整性） | ✅ 已分配，独立审稿中 |
| 外部审稿 | ⏭️ 未配置，跳过 |

等待两位 Reviewer 返回 Round 1 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 58

## Round 58

2 recorded events


### User

_source line 714 · 2026-05-22T14:57:17.491671+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性、完整性与写作质量

**论文标题**: The Formulation Design Space for Execution-Free Code Verification: A Systematic Empirical Study

---

## 总体评分

**Overall**: 3/5 — Findings（可被 Findings 接收）
**一句话总结**: 方法论扎实的实证研究，通过匹配实验设计系统比较了三种 execution-free 验证 formulation，但核心发现（function-level 等价性、repo-level generation 格式崩溃）在较大程度上符合 practitioner 直觉，novelty 不足以支撑 Main conference。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 匹配实验设计严谨（同数据/同 LoRA/同 seed），统计检验充分（TOST、ICC、clustered bootstrap、Holm-Bonferroni）。但 repo-level 仅 3 seeds（8B）、多个未解决的 confounds（§3.7）削弱了部分结论的可靠性。 |
| **Excitement** | 2.5/5 | 实用性有余但惊喜不足。Function-level 等价性可预期；repo-level divergence 的根因（format collapse）对 generation 模型来说是已知挑战。Failure mode taxonomy 有一定价值但属 observational。 |
| **Reproducibility** | 4/5 | Appendix E 提供完整超参数，承诺开源代码/数据/checkpoint。Prompt templates 在 Appendix F 中给出。训练细节充分。 |
| **Overall Assessment** | 3/5 | Findings |
| **Confidence** | 4/5 | 熟悉 code verification、LLM fine-tuning 和 reward modeling 相关文献，仔细阅读了正文和全部附录。 |

---

## 主要优势（Strengths）

**S1. 匹配实验框架设计出色。** 三种 formulation 共享相同训练数据、LoRA 配置、seed 和 evaluation protocol，这是隔离 formulation effect 的正确做法。据我所知这确实是首个此类 head-to-head controlled comparison（Section 3.1, Table 1）。

**S2. 统计方法严谨且多层次。** TOST 等价检验（§3.4）、ICC within-problem correlation（§3.4）、clustered bootstrap CIs（Section 3.1）、Holm-Bonferroni 校正（Table 15）、mixed-effects regression（Appendix M）——统计工具选择合理且层层递进。这在 NLP 实证论文中属于较高水准。

**S3. Failure mode taxonomy 有实际指导价值。** Format collapse、decision collapse、aggregation penalty（Section 3.2, Table 4）三种失败模式有清晰的定义和实例支撑（Appendix H），为 practitioner 选择 formulation 提供了具体的 decision criteria。

**S4. Error complementarity 是最有洞察力的发现。** Oracle combination 在 function-level 达到 90.63%、repo-level variant-level 达到 95.83%（Section 3.6），表明不同 formulation 的错误模式是互补的。这为 ensemble/routing 方法提供了实证基础，且不可从单一 formulation 的结果中推导出来。

**S5. 附录极其充分。** 14 页附录覆盖 ablation（B, C, K）、error analysis（H, I）、statistical tests（J, K, L）、confound analysis（O）、extended limitations（P）等，展现了扎实的实验工作量。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution novelty 不足以支撑"design space"的定位

- **具体位置**: Title, Abstract, Section 1 (Introduction)
- **问题**: 论文标题声称探索 "formulation design space"，但实际只比较了三个具体 formulation（CLS/CWM/TRAJ），且这三者本质上是已知的 prediction target 变体（binary classification、output generation、sequence-level classification）。真正的 "design space" 探索应包含更多维度：loss function 变体、output format 设计、training objective 组合、解码策略等。当前工作更准确地说是 "formulation comparison" 而非 "design space exploration"。
- **为什么影响接收**: 标题/framing 与实际贡献的错位会让 reviewer 和读者产生 over-promise 的印象。对于 Main conference，novelty 不仅要求实验扎实，还需要 insight 超越 practitioner 直觉。
- **建议修改方向**: (1) 将 framing 从 "design space" 调整为 "systematic comparison"——这更准确地反映贡献；(2) 或者真正扩展到 design space 维度（如加入 loss function ablation、output format variants），但这可能超出当前工作范围。

**N2** [critical] Function-level 等价性发现的 novelty 和 surprise value 有限

- **具体位置**: Section 3.4, Contribution 1 (page 2)
- **问题**: Function-level verification 的输出空间很小（PASS/FAIL token 或短字符串），在此条件下不同 formulation 达到相似精度是可预期的。当 task 足够简单、输出足够短时，classification 和 generation 的区别被最小化。论文将此作为三个核心 contribution 之一（"Formulation near-equivalence at low complexity"），但这更像是一个 sanity check 而非 insight。
- **为什么影响接收**: EMNLP Main 期望 contribution 提供 non-trivial insight。如果主要发现之一在很大程度上是符合预期的，则总体贡献的 novelty bar 难以达到 conference 水准。
- **建议修改方向**: 弱化此发现作为独立 contribution 的地位，将其重新定位为 experimental validation / baseline establishment，以更强调 repo-level divergence 和 error complementarity 的 novelty。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Repo-level 结论受多重 confounds 严重限制

- **具体位置**: Section 3.5, Section 3.7, Appendix O
- **问题**: 论文诚实地在 §3.7 和 Appendix O 识别了 5 个 confounds（checkpoint selection、NaN validation loss、evaluation sequence length、preprocessing、CWM scale/pretraining），但 Appendix M 的 mixed-effects regression 显示 model identity（random effect）解释了 >95% 的 predictable variance。这意味着 formulation effect 虽然统计显著（interaction z=−23.7），但在实际变异中被 model selection effect 淹没。加上 8B 模型仅 3 seeds（Section 3.1 footnote），repo-level 结论的 robustness 存疑。
- **建议**: (1) 在正文中更突出地讨论 model identity dominance（目前仅在 Appendix M）；(2) 增加 8B repo-level 的 seed 数量（至少 5 seeds）以匹配 function-level 的统计标准。

**W2** [warning] TOST 等价检验的 ±2pp margin 缺乏 justification

- **具体位置**: Section 3.4, Appendix J
- **问题**: TOST 使用 ±2pp 作为等价 margin，但未解释为什么 2pp 是 "practically equivalent" 的合理阈值。在某些应用场景中（如安全关键代码验证），2pp 的差异可能是 practically significant。论文预设了 ±2pp 然后论证 "Bonferroni-corrected TOST all pass"，但这个 pre-specified margin 的选择本身需要 domain-grounded 的 justification。
- **建议**: 报告多个 margin（±1pp, ±2pp, ±3pp）下的 TOST 结果作为 sensitivity analysis，或引用 code verification 领域的 prior work 来 justify ±2pp 的选择。

**W3** [warning] CWM "code world model" 术语与更广泛的 world model 文献脱节

- **具体位置**: Section 2.1, throughout
- **问题**: 论文将 output generation formulation 命名为 "code world model (CWM)"，但未讨论这与 AI/ML 中 "world model" 概念的关系。CWM 本质上是 output prediction（给定代码和输入，预测输出字符串），称之为 "world model" 暗示模型构建了代码执行的内部模拟，但论文未提供证据表明这种内部模拟确实存在（而非简单的 pattern matching）。这个术语选择可能误导读者。
- **建议**: (1) 简短讨论 CWM 与 world model 概念的关系和区别；(2) 或者使用更中性的术语如 "output prediction" / "execution output generation"。

**W4** [warning] 缺少与 execution-based verification 的直接精度对比

- **具体位置**: Section 1, Section 5
- **问题**: 论文动机是 execution-based verification "reliable but expensive"，execution-free 是更高效的替代。但全文未直接对比 execution-based verification 的精度，读者无法量化 execution-free 方法的 accuracy gap。没有这个 anchor point，很难评估 88% function-level 精度或 ~55% repo-level 精度在实际中是否 "good enough"。
- **建议**: 在 Table 1 或 Table 3 中增加 execution-based verification 的精度作为 oracle upper bound。

**W5** [warning] 遗漏高度相关的近期工作 CodeScaler

- **具体位置**: Section 4 (Related Work)
- **问题**: CodeScaler（arXiv 2602.17684, Feb 2026）是一个 execution-free reward model，训练在代码偏好数据上，在 5 个 coding benchmark 上实现了与 execution-based RL 可比的性能，并提供 10× latency 减少。这与本文的 execution-free verification 主题直接相关，且提出了 reward shaping 和 syntax-aware extraction 等本文未探索的技术。此外，Self-Execution Simulation（arXiv 2604.03253, April 2026）提出联合建模代码语法和执行动态，与 CWM formulation 高度相关。
- **建议**: 在 Related Work 中讨论 CodeScaler 和相关并发工作，分析其与本文三种 formulation 的关系。

---

## 小问题（Minor，不影响接收）

**M1** [minor] Table 1 中 TRAJ 标记为 "not informational"，但 §3.2 中又讨论了 TRAJ 的 per-test diagnostic 价值（通过 variant-level analysis）。这两处的措辞有轻微矛盾——建议统一表述。

**M2** [minor] Figure 2 的 y-axis 标注 "Note: y-axis begins at 55% to emphasize formulation differences"——这是好的实践。但 Figure 3（Appendix A, page 13）的 y-axis 似乎也不从 0 开始，却未注明。

**M3** [minor] Abstract 第一句 "LLM-based program repair increasingly relies on generating multiple candidate patches and selecting the best via a verifier" 过于绝对——并非所有 LLM-based repair 方法都使用 verifier（有些依赖 self-debugging 或 iterative refinement）。建议加 qualifier。

**M4** [minor] §2.2 中 "three failure modes" 的定义仅覆盖 CWM 的 generation failure modes。CLS 和 TRAJ 的典型失败模式（如 class imbalance sensitivity、threshold sensitivity）未被讨论，这使得 taxonomy 看起来不够 balanced。

**M5** [minor] Appendix P "Extended Limitations" 的存在暗示正文 Limitations 可能不够完整。建议将最关键的 extended limitations（特别是 CWM scale and pretraining 的讨论）移入正文 Limitations。

---

## Questions（需要作者回答的问题）

**Q1**: Mixed-effects regression（Appendix M）显示 model identity 解释了 >95% 的 predictable variance。如果换用不同的 base model（如 Llama-3、CodeLlama），formulation ranking 是否可能完全反转？作者是否有证据表明 formulation effect 在更多 model families 上是稳定的？

**Q2**: TOST ±2pp equivalence margin 是 pre-registered 的还是 post-hoc 选择的？如果是 post-hoc，是否尝试过其他 margin 值？

**Q3**: CWM 在 repo-level 的 format collapse（53-74% unparseable）——这是否主要是一个 training data quantity 问题？如果将 CWM 的 repo-level training data 增加 5-10×，format collapse 率是否会显著下降？

**Q4**: Error complementarity（oracle 90.63% function, 95.83% repo variant）是从 single-seed 还是 multi-seed 聚合中计算的？如果是 single-seed，这个结论在不同 seed 下是否稳定？

**Q5**: 论文限定在 ≤8B LoRA regime。是否有初步实验或 pilot data 暗示在 >8B 或 full fine-tuning 设置下结论会不同？这对论文发现的 generalizability 影响如何？

---

## Missing References（遗漏的相关工作）

1. **CodeScaler** (arXiv 2602.17684, Feb 2026) — Execution-free reward model for code LLMs, directly addresses the same problem space with reward shaping and syntax-aware extraction. 应在 §4 讨论。
2. **Self-Execution Simulation** (arXiv 2604.03253, April 2026) — Joint modeling of code syntax and execution dynamics, highly relevant to CWM formulation. 并发工作，应提及。
3. **GenPRM** (AAAI 2026, arXiv 2504.00891) — Generative PRM with code verification for math reasoning. 与 GenRM 讨论相关，可补充。
4. **ExecVerify** (arXiv 2603.11226) — White-box RL with verifiable stepwise rewards for code execution reasoning. 与 process supervision 讨论相关。

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤8 页 | ✅ 合规（Section 1-5 在 pages 1-8 内） |
| Limitations 存在 | ✅ 存在（page 8 底部开始） |
| 匿名性（double-blind） | ✅ "Anonymous ACL submission"，未发现去匿名信息 |
| ACL template with [review] | ✅ |
| References 格式 | ✅ 基本一致 |
| Checklist 完整 | ✅ Pages 11-12，覆盖 A-F 各 section |
| Appendix 附论文提交 | ✅ Pages 13-22 |

---

## 总结

这是一篇方法论严谨的实证研究，实验设计（matched training framework）和统计方法（多层次检验）都达到了较高水准。Failure mode taxonomy 和 error complementarity 发现有实用价值。

但 novelty 存在不足：(1) "design space" framing 与 "三个已知 formulation 的比较" 之间存在张力；(2) 核心发现中 function-level 等价性符合预期，repo-level divergence 受多重 confounds 限制；(3) ≤8B LoRA 的 scope 限制了结论的 generalizability。

**建议评级：3/5 (Findings)**。论文的实验严谨性和实用建议适合 Findings of ACL，但 novelty 和 excitement 不足以进入 Main conference。如果能扩展至更多 model families 或解决 repo-level confounds，评级可能提升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 715 · 2026-05-22T14:57:24.361057+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 716 · 2026-05-22T14:57:37.382839+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3/5 (Findings)，Soundness 3.5，Excitement 2.5，Confidence 4。

核心判断：
- 实验设计和统计方法扎实（matched framework + TOST/ICC/bootstrap），附录充分
- 但 novelty 不足以支撑 Main：(1) "design space" framing 过度，实际只比较了三个已知 formulation；(2) function-level 等价性可预期；(3) repo-level 结论受 confounds 限制且 model identity 解释了 >95% variance
- 2 个 Must-Fix（contribution novelty 定位、function-level 发现的 surprise value），5 个 Should-Fix（repo-level confounds、TOST margin justification、CWM 术语、缺少 execution-based 对比、遗漏 CodeScaler），5 个 Minor
- 遗漏 4 篇相关工作（CodeScaler、Self-Execution Simulation、GenPRM、ExecVerify）
- 格式合规，无匿名性问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 717 · 2026-05-22T14:57:43.204209+00:00_

Reviewer 2 意见已收到。等待 Reviewer 1 的审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 60

## Round 60

6 recorded events


### User

_source line 718 · 2026-05-22T14:58:23.283646+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查（Round 1）

### 总体评分

**Overall**: 3.5 (Borderline Conference)
**Confidence**: 4/5 (Checked important points carefully, familiar with statistical methodology)

**一句话总结**: 一项设计严谨的系统性实验研究，统计框架选择优于该领域大多数 empirical papers，但 CWM 评估指标的非对称性、SESOI 论证不足、以及 variant-level 统计功效有限，使部分核心 claim 的证据支撑存在缺口。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计框架整体合理（TOST + clustered bootstrap + ICC + Holm-Bonferroni），但 CWM 评估指标非对称性和 SESOI 论证不足削弱了等价性 claim |
| Excitement | 2.5/5 | 研究问题实用但结论大体在预期之内（不同粒度 formulation 在不同复杂度下表现不同），三层结构框架有一定但有限的概念贡献 |
| Reproducibility | 4/5 | 超参数报告详尽（Table 11, Appendix E），prompt 模板公开（Appendix F），承诺释放代码和数据 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] CWM 评估指标的非对称性构成未量化的 confound，影响等价性 claim

- **具体位置**：§2.1 footnote 2, §3.5, Appendix N
- **问题**：CWM 使用 exact string matching 评估（footnote 2: "Exact string matching is conservative"），而 CLS 仅需预测 PASS/FAIL 二分类。这造成两个方向的系统性偏差：
  - **(a) 惩罚方向**：CWM 语义正确但格式不同的输出被判错。论文未量化有多少 CWM "failures" 实际上是语义正确的。
  - **(b) 补偿方向**：不可解析的 CWM 输出默认为 majority class (PASS)。Appendix N 显示不可解析实例的 pass rate 显著更高 (74.6% vs 68.3%, p < 10⁻¹⁹)。
  
  这两个偏差可能恰好相互抵消，使 CLS-CWM 在 function level "看起来"等价（TOST p=0.007, §3.4），但这种等价可能是评估 artifacts 的产物而非 formulation 本身的性质。
- **为什么影响接收**：论文核心 claim 之一是"CLS and CWM are statistically equivalent at function level"（Abstract）。若此等价源于评估偏差的巧合抵消，则该结论不可靠，进而影响论文的三层结构框架。
- **建议修改方向**：(a) 实施 relaxed matching（语义等价判定）并重新运行 TOST；或 (b) 提供 sensitivity analysis 量化 exact match vs relaxed match 对等价结论的影响范围；或 (c) 至少对一个 seed 做 manual inspection 统计 CWM 的 "false negative" 比例。

**N2** [critical] TOST ±2pp SESOI 的论证不充分，缺乏 domain-specific justification

- **具体位置**：§3.1, §3.4
- **问题**：论文将 SESOI 设为 ±2pp，理由是"at 85–88% accuracy, 2pp corresponds to ~2–3 problems out of 114"（§3.1/§3.4）。但在等价检验中，SESOI 是最关键的参数选择——它直接决定了 TOST 能否拒绝非等价 H₀。当前论证存在三个不足：
  - (a) 在代码验证场景中，漏检一个 critical bug 的成本可能远高于 false positive——flat ±2pp 可能不反映实际部署中的不对称 cost structure。
  - (b) 不同 complexity level 的实际意义不同：function-level 少判对 2 个问题 vs repo-level 少判对 2 个问题的工程后果完全不同，但 SESOI 未区分。
  - (c) 论文未引用 SE/testing 领域关于 "practically equivalent accuracy" 的先行文献来支撑此选择。
- **为什么影响接收**：SESOI 选择直接决定 TOST 结论。缺乏严谨论证使 reviewer 无法判断等价性 claim 的可靠性——这是该 claim 的前提条件而非附加细节。
- **建议修改方向**：(a) 提供 sensitivity analysis 展示 SESOI 在 ±1pp 到 ±3pp 范围内 TOST 结论的变化（是否存在 tipping point）；(b) 引用 equivalence testing 方法论文献（如 Wellek, 2010）中对 SESOI 选择的讨论框架。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Variant-level 分析统计功效不足（n=48, MDE≈25pp），多项 variant-level 结论缺乏 power 支撑

- **具体位置**：§3.5 Table 4, Appendix K Table 14
- **问题**：Variant-level 比较仅有 n=48（Table 10, Appendix D），Appendix K 报告 MDE≈25pp。这意味着只能检测 >25pp 的大效应。但论文仍从 variant-level 数据得出多项结论：Table 4 failure mode taxonomy 的比例分布（format collapse 54.17%）、§3.5"three distinct failure modes consistent across model families"均基于极小样本。
- **建议**：明确标注 variant-level 分析为 "exploratory/descriptive" 而非 inferential；或增加 variant 数量。

**W2** [warning] Cross-model 泛化性有限：DeepSeek 仅 2 seeds，不支持 inferential claims

- **具体位置**：Table 1 (s=2 for DeepSeek), Abstract
- **问题**：DeepSeek-Coder function-level 实验仅用 2 seeds，论文标注 "reported for descriptive comparison, not inferential"（Table 1 footnote）。但 Abstract 仍声称 "TRAJ parity is model-dependent"——此 claim 的一半证据（DeepSeek 端）来自 non-inferential 数据。两个 model family 也不足以支撑 "model-dependent" 这一带有一般性的结论。
- **建议**：将 "model-dependent" 改为更谨慎的表述（如 "observed to vary between Qwen3 and DeepSeek-Coder"），或为 DeepSeek 补充至少 3 seeds。

**W3** [warning] Checkpoint selection 不一致引入系统性 confound

- **具体位置**：Appendix O (Checkpoint selection), Appendix E
- **问题**：CWM 所有 repo-level runs 因 NaN validation loss 使用 final epoch checkpoint，CLS 使用 val-best selection。虽然 Appendix O 论证 "val-selected checkpoint is the lowest"（即 final epoch 不比 val-best 差），但这仅说明方向性——未排除 checkpoint selection × formulation 的 interaction effect。更重要的是：**CWM 出现 NaN val loss 本身可能就是 formulation 的固有训练不稳定性**，这是一个值得在正文讨论的 negative finding。
- **建议**：(a) 解释 CWM NaN val loss 的原因（formulation 固有还是实现 issue）；(b) 对 CLS 也使用 final epoch checkpoint 做 robustness check。

**W4** [warning] TRAJ 数据量 ablation 仅覆盖 1 model × 1 seed × 1 level

- **具体位置**：§3.7, Appendix B
- **问题**：TRAJ 训练数据（~400 variant-level）与 CLS/CWM（~70K per-test）存在 ~180× 差异。Appendix B 提供了 downsample ablation（Qwen3-4B, seed 42, repo-level 仅），显示 CLS 降采样后仍优于 TRAJ 7.52pp。但此 ablation 仅 1 个数据点——既不跨 model 也不跨 level，不足以排除 data volume 作为主要 confound。
- **建议**：至少在 function-level 和另一个 model 上补充 downsample ablation，或更充分讨论此限制。

**W5** [warning] Mixed-effects LPM 的标准误处理

- **具体位置**：Appendix M
- **问题**：Appendix M 使用 LPM + HC1 (Huber-White) robust SEs + random intercepts (1|problem_id)。HC1 纠正异方差但不 account for residual within-cluster correlation beyond the random intercept。对于 clustered binary data，cluster-robust SEs (CR) 更为 appropriate。论文提到 logistic regression 作为 robustness check 得到一致结论，但未报告具体系数和 p-values。
- **建议**：(a) 补充 cluster-robust SEs 作为 robustness check；(b) 报告 logistic regression 的具体系数而非仅声称 "一致"。

---

### 小问题（不影响接收）

- §3.4 clustered bootstrap 的具体实施细节（resample clusters with replacement? resample observations within resampled clusters?）未在正文或附录说明，建议补充精确的 bootstrap procedure 描述。
- Table 1 中 TRAJ 的评估子集（1,012 2-sample subset, 447 matched pairs）与 CLS/CWM 评估集不完全对齐，可能影响直接比较的解读。
- Figure 2 的 y 轴从 55% 截断（已有 note），但视觉上仍可能夸大 CWM 在 repo-level 的下降幅度。
- Repo-level DEFF=114.3（Appendix A）意味着 effective n≈86（9,784/114.3），论文未显式讨论此 reduced effective sample size 对 repo-level 推断的限制。

---

### Questions（需要作者回答）

**Q1**: CWM exact string matching 中有多少比例的 "错误" 实际上是语义正确但格式不同？是否做过 manual inspection 或 fuzzy matching 统计？

**Q2**: 若将 SESOI 从 ±2pp 调整为 ±1pp 或 ±3pp，TOST 结论是否改变？是否存在 tipping point？

**Q3**: CWM repo-level runs 出现 NaN validation loss 的原因是什么？是 formulation 固有的训练不稳定性还是特定实现 issue？若为前者，这本身是值得在正文讨论的 negative finding。

**Q4**: Appendix M 报告 β_interaction = 0.219, z = −23.7——此 β 是否在 percentage point scale 上可直接解读？random effects 的 variance component 是多少？

**Q5**: Table 15 的 k=5 comparisons 是如何选定的？为什么不包括 repo-level equivalence test？comparison family 的选择是否有 pre-registration？

---

### Missing References

- **Moulton (1990)**: "An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units" — clustered data 中忽略 within-cluster correlation 的经典文献，与本文 ICC/DEFF 讨论直接相关。
- **Wellek (2010)**: "Testing Statistical Hypotheses of Equivalence and Noninferiority" — 等价检验标准教材，包含 SESOI 选择的系统性讨论框架。

---

### 主要优势

1. **匹配实验设计的严谨性**：shared LoRA configuration, identical training data, multi-seed evaluation, 统一数据分割——在 formulation comparison 中达到了罕见的 controlled comparison 水平。
2. **统计方法论的完整性**：正确使用 TOST（而非依赖 NHST non-significance），clustered bootstrap for correlated errors，ICC/DEFF 量化 cluster effects，Holm-Bonferroni for multiple comparisons——整体框架优于该领域大多数 empirical papers。
3. **Threats to validity 的透明度**：§3.7 和 Appendix O 逐一识别并量化讨论 5 个 confound，多数有 empirical evidence 而非仅做定性讨论。
4. **Failure mode taxonomy 的实用价值**：Table 4 的三类 failure mode（format collapse, decision collapse, aggregation penalty）为 practitioners 提供可操作的诊断框架。
5. **三层结构框架**：fine-tuning → formulation 选择（仅在 repo-level matters）→ complexity——用 rigorous evidence 确认直觉性结构，有实际指导价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 719 · 2026-05-22T14:58:57.289493+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查（Round 1）\n\n### Overall: 3.5 (Borderline Conference), Confidence: 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n### Must-Fix\n\n**N1** [critical] CWM 评估指标的非对称性构成未量化的 confound，影响等价性 claim\n- CWM 使用 exact string matching，CLS 仅需 PASS/FAIL 二分类。两个方向的系统偏差：(a) CWM 语义正确但格式不同被判错；(b) 不可解析输出默认为 majority class (PASS)，Appendix N 显示不可解析实例 pass rate 更高 (74.6% vs 68.3%)。\n- 这两个偏差可能巧合抵消，使 function-level 等价性是评估 artifacts 的产物。\n- 建议：实施 relaxed matching 并重新运行 TOST；或对一个 seed 做 manual inspection。\n\n**N2** [critical] TOST ±2pp SESOI 论证不充分\n- (a) 代码验证中漏检 critical bug 的成本可能远高于 FP——flat ±2pp 不反映不对称 cost；(b) function-level vs repo-level 的实际意义不同但 SESOI 未区分；(c) 未引用 SE/testing 领域文献支撑选择。\n- 建议：提供 sensitivity analysis（±1pp 到 ±3pp）；引用 Wellek (2010) 等等价检验方法论文献。\n\n---\n\n### Should-Fix\n\n**W1** [warning] Variant-level 分析 n=48, MDE≈25pp，多项 variant-level 结论缺乏 power 支撑（Table 4 failure mode taxonomy 的比例分布均基于极小样本）。\n\n**W2** [warning] DeepSeek 仅 2 seeds，Abstract 声称 \"TRAJ parity is model-dependent\" 的一半证据来自 non-inferential 数据。两个 model family 不足以支撑 \"model-dependent\" 的一般性结论。\n\n**W3** [warning] Checkpoint selection 不一致：CWM 全部使用 final epoch（NaN val loss），CLS 使用 val-best。CWM NaN val loss 本身可能是 formulation 固有的训练不稳定性。\n\n**W4** [warning] TRAJ downsample ablation 仅 1 model × 1 seed × 1 level，不足以排除 data volume 作为主要 confound。\n\n**W5** [warning] LPM + HC1 robust SEs 不 account for residual within-cluster correlation beyond random intercept。应补充 cluster-robust SEs。\n\n---\n\n### Minor\n- clustered bootstrap 实施细节未说明\n- TRAJ 评估子集与 CLS/CWM 不完全对齐\n- Figure 2 y-轴截断可能夸大 CWM 下降\n- Repo-level DEFF=114.3 意味着 effective n≈86，未讨论对推断的限制\n\n---\n\n### Questions\nQ1: CWM exact match 中有多少比例的\"错误\"实际上是语义正确的？\nQ2: SESOI 从 ±2pp 调整为 ±1pp/±3pp 时 TOST 结论是否改变？\nQ3: CWM NaN val loss 的原因？formulation 固有还是实现 issue？\nQ4: Appendix M β_interaction=0.219 是否在 pp scale 上直接可读？random effects variance？\nQ5: Table 15 k=5 comparisons 如何选定？为何不包括 repo-level equivalence？\n\n### Missing References\n- Moulton (1990): clustered data 经典文献\n- Wellek (2010): 等价检验标准教材"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — 方法严谨性审查（Round 1）\n\n### Overall: 3.5 (Borderline Conference), Confidence: 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n### Must-Fix\n\n**N1** [critical] CWM 评估指标的非对称性构成未量化的 confound，影响等价性 claim\n- CWM 使用 exact string matching，CLS 仅需 PASS/FAIL 二分类。两个方向的系统偏差：(a) CWM 语义正确但格式不同被判错；(b) 不可解析输出默认为 majority class (PASS)，Appendix N 显示不可解析实例 pass rate 更高 (74.6% vs 68.3%)。\n- 这两个偏差可能巧合抵消，使 function-level 等价性是评估 artifacts 的产物。\n- 建议：实施 relaxed matching 并重新运行 TOST；或对一个 seed 做 manual inspection。\n\n**N2** [critical] TOST ±2pp SESOI 论证不充分\n- (a) 代码验证中漏检 critical bug 的成本可能远高于 FP——flat ±2pp 不反映不对称 cost；(b) function-level vs repo-level 的实际意义不同但 SESOI 未区分；(c) 未引用 SE/testing 领域文献支撑选择。\n- 建议：提供 sensitivity analysis（±1pp 到 ±3pp）；引用 Wellek (2010) 等等价检验方法论文献。\n\n---\n\n### Should-Fix\n\n**W1** [warning] Variant-level 分析 n=48, MDE≈25pp，多项 variant-level 结论缺乏 power 支撑（Table 4 failure mode taxonomy 的比例分布均基于极小样本）。\n\n**W2** [warning] DeepSeek 仅 2 seeds，Abstract 声称 \"TRAJ parity is model-dependent\" 的一半证据来自 non-inferential 数据。两个 model family 不足以支撑 \"model-dependent\" 的一般性结论。\n\n**W3** [warning] Checkpoint selection 不一致：CWM 全部使用 final epoch（NaN val loss），CLS 使用 val-best。CWM NaN val loss 本身可能是 formulation 固有的训练不稳定性。\n\n**W4** [warning] TRAJ downsample ablation 仅 1 model × 1 seed × 1 level，不足以排除 data volume 作为主要 confound。\n\n**W5** [warning] LPM + HC1 robust SEs 不 account for residual within-cluster correlation beyond random intercept。应补充 cluster-robust SEs。\n\n---\n\n### Minor\n- clustered bootstrap 实施细节未说明\n- TRAJ 评估子集与 CLS/CWM 不完全对齐\n- Figure 2 y-轴截断可能夸大 CWM 下降\n- Repo-level DEFF=114.3 意味着 effective n≈86，未讨论对推断的限制\n\n---\n\n### Questions\nQ1: CWM exact match 中有多少比例的\"错误\"实际上是语义正确的？\nQ2: SESOI 从 ±2pp 调整为 ±1pp/±3pp 时 TOST 结论是否改变？\nQ3: CWM NaN val loss 的原因？formulation 固有还是实现 issue？\nQ4: Appendix M β_interaction=0.219 是否在 pp scale 上直接可读？random effects variance？\nQ5: Table 15 k=5 comparisons 如何选定？为何不包括 repo-level equivalence？\n\n### Missing References\n- Moulton (1990): clustered data 经典文献\n- Wellek (2010): 等价检验标准教材"
  }
}
```

</details>

---


### Tool result

_source line 720 · 2026-05-22T14:59:21.165373+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23875
}
```

</details>

---


### Tool call

_source line 721 · 2026-05-22T14:59:21.316460+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查（Round 1）\n\n### Overall: 3/5 (Findings), Confidence: 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n### Must-Fix\n\n**N1** [critical] Contribution novelty 不足以支撑 \"design space\" 定位\n- 标题声称 \"formulation design space\"，但只比较了三个具体 formulation（CLS/CWM/TRAJ）。真正的 design space 探索应包含 loss function 变体、output format 设计、training objective 组合、解码策略等。当前工作更准确地说是 \"formulation comparison\"。\n- 建议：将 framing 从 \"design space\" 调整为 \"systematic comparison\"。\n\n**N2** [critical] Function-level 等价性发现的 novelty/surprise value 有限\n- 当 task 足够简单、输出足够短时，classification 和 generation 的区别被最小化。将此作为核心 contribution 之一 (\"Formulation near-equivalence at low complexity\") 更像 sanity check 而非 insight。\n- 建议：弱化此发现作为独立 contribution 的地位。\n\n---\n\n### Should-Fix\n\n**W1** [warning] Repo-level 结论受多重 confounds 严重限制。Appendix M 显示 model identity 解释了 >95% 的 predictable variance，formulation effect 被 model selection effect 淹没。加上 8B 仅 3 seeds，robustness 存疑。\n\n**W2** [warning] TOST ±2pp margin 缺乏 justification。在安全关键代码验证中 2pp 差异可能 practically significant。建议报告多个 margin 下的结果。\n\n**W3** [warning] CWM 术语与 world model 文献脱节。\"code world model\" 暗示内部模拟，但论文未提供证据。\n\n**W4** [warning] 缺少与 execution-based verification 的直接精度对比。读者无法量化 execution-free 方法的 accuracy gap。\n\n**W5** [warning] 遗漏 CodeScaler (arXiv 2602.17684) — execution-free reward model，与本文主题直接相关。\n\n---\n\n### Minor\n- M1: Table 1 中 TRAJ \"not informational\" 与 §3.2 中讨论 TRAJ per-test diagnostic 价值矛盾。\n- M2: Figure 3 y-axis 不从 0 开始但未注明。\n- M3: Abstract 第一句过于绝对（并非所有 repair 方法都用 verifier）。\n- M4: §2.2 failure mode taxonomy 偏向 CWM，CLS/TRAJ 失败模式讨论不足。\n- M5: Appendix P \"Extended Limitations\" 存在暗示正文 Limitations 不够完整。\n\n---\n\n### Questions\nQ1: Mixed-effects regression 显示 model identity 解释 >95% variance。换用不同 base model 时 formulation ranking 是否可能反转？\nQ2: TOST ±2pp 是 pre-registered 还是 post-hoc？\nQ3: CWM format collapse 是否主要是 training data quantity 问题？增加 5-10× 是否会改善？\nQ4: Error complementarity (oracle 90.63%/95.83%) 是 single-seed 还是 multi-seed？不同 seed 下是否稳定？\nQ5: 是否有 >8B 或 full fine-tuning 的 pilot data？\n\n### Missing References\n1. CodeScaler (arXiv 2602.17684)\n2. Self-Execution Simulation (arXiv 2604.03253)\n3. GenPRM (AAAI 2026)\n4. ExecVerify (arXiv 2603.11226)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix / Should-Fix / Minor 和 Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 — 新颖性与完整性审查（Round 1）\n\n### Overall: 3/5 (Findings), Confidence: 4/5\nSoundness 3.5, Excitement 2.5, Reproducibility 4\n\n---\n\n### Must-Fix\n\n**N1** [critical] Contribution novelty 不足以支撑 \"design space\" 定位\n- 标题声称 \"formulation design space\"，但只比较了三个具体 formulation（CLS/CWM/TRAJ）。真正的 design space 探索应包含 loss function 变体、output format 设计、training objective 组合、解码策略等。当前工作更准确地说是 \"formulation comparison\"。\n- 建议：将 framing 从 \"design space\" 调整为 \"systematic comparison\"。\n\n**N2** [critical] Function-level 等价性发现的 novelty/surprise value 有限\n- 当 task 足够简单、输出足够短时，classification 和 generation 的区别被最小化。将此作为核心 contribution 之一 (\"Formulation near-equivalence at low complexity\") 更像 sanity check 而非 insight。\n- 建议：弱化此发现作为独立 contribution 的地位。\n\n---\n\n### Should-Fix\n\n**W1** [warning] Repo-level 结论受多重 confounds 严重限制。Appendix M 显示 model identity 解释了 >95% 的 predictable variance，formulation effect 被 model selection effect 淹没。加上 8B 仅 3 seeds，robustness 存疑。\n\n**W2** [warning] TOST ±2pp margin 缺乏 justification。在安全关键代码验证中 2pp 差异可能 practically significant。建议报告多个 margin 下的结果。\n\n**W3** [warning] CWM 术语与 world model 文献脱节。\"code world model\" 暗示内部模拟，但论文未提供证据。\n\n**W4** [warning] 缺少与 execution-based verification 的直接精度对比。读者无法量化 execution-free 方法的 accuracy gap。\n\n**W5** [warning] 遗漏 CodeScaler (arXiv 2602.17684) — execution-free reward model，与本文主题直接相关。\n\n---\n\n### Minor\n- M1: Table 1 中 TRAJ \"not informational\" 与 §3.2 中讨论 TRAJ per-test diagnostic 价值矛盾。\n- M2: Figure 3 y-axis 不从 0 开始但未注明。\n- M3: Abstract 第一句过于绝对（并非所有 repair 方法都用 verifier）。\n- M4: §2.2 failure mode taxonomy 偏向 CWM，CLS/TRAJ 失败模式讨论不足。\n- M5: Appendix P \"Extended Limitations\" 存在暗示正文 Limitations 不够完整。\n\n---\n\n### Questions\nQ1: Mixed-effects regression 显示 model identity 解释 >95% variance。换用不同 base model 时 formulation ranking 是否可能反转？\nQ2: TOST ±2pp 是 pre-registered 还是 post-hoc？\nQ3: CWM format collapse 是否主要是 training data quantity 问题？增加 5-10× 是否会改善？\nQ4: Error complementarity (oracle 90.63%/95.83%) 是 single-seed 还是 multi-seed？不同 seed 下是否稳定？\nQ5: 是否有 >8B 或 full fine-tuning 的 pilot data？\n\n### Missing References\n1. CodeScaler (arXiv 2602.17684)\n2. Self-Execution Simulation (arXiv 2604.03253)\n3. GenPRM (AAAI 2026)\n4. ExecVerify (arXiv 2603.11226)"
  }
}
```

</details>

---


### Tool result

_source line 722 · 2026-05-22T14:59:22.683203+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1366
}
```

</details>

---


### Assistant

_source line 723 · 2026-05-22T14:59:25.193170+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 724 · 2026-05-22T14:59:27.725030+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

**评分**: Overall 3.5 (Borderline Conference), Soundness 3.5, Excitement 2.5, Reproducibility 4.0, Confidence 4/5。

**两个 Must-Fix**：
1. CWM 的 exact string matching 与 majority-class default 构成非对称评估偏差，可能使 CLS-CWM 等价性成为 artifact 的巧合抵消——需要 relaxed matching 或 sensitivity analysis
2. TOST ±2pp SESOI 缺乏 domain-specific 论证，需要 sensitivity analysis（±1pp~±3pp）

**五个 Should-Fix**：variant-level 功效不足(n=48)、DeepSeek 仅 2 seeds 却声称 model-dependent、checkpoint selection 不一致（CWM NaN val loss）、TRAJ 数据量 ablation 覆盖不足、mixed-effects LPM 标准误处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 725 · 2026-05-22T14:59:32.693269+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 726 · 2026-05-22T15:02:19.025912+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 (Round 1)

---

### Must-Fix 回应

**[AGREE] R1-N1: CWM exact matching 的非对称偏差是合理关切，但严重程度应从 critical 降为 warning**

R1 正确指出 CWM 存在两个方向的评估偏差：(a) exact matching 保守性低估 CWM（语义正确但格式不同被判错），(b) 不可解析输出默认 majority class 可能高估 CWM。

但我认为这不应是 must-fix：

1. **论文已部分回应**：Appendix N 专门分析了 parseable bias，报告了 parseable-only accuracy 和 unparseable instance 的 pass rate 分布（74.6% vs 68.3%）。这不是被忽视的问题。
2. **Function-level 影响量级有限**：Section 2.1 明确指出 function-level 输出是 "short strings (integers, booleans)"，format mismatch 在短输出上发生概率远低于 repo-level（后者的 53–74% unparseable rate 才是问题所在）。论文报告 function-level 仅 1.39% unparseable（page 14, "truncation introduces 136 unparseable outputs (1.39% of test samples)"），偏差的实际影响 ≪1pp。
3. **评估协议遵循领域标准**：footnote 2 明确引用 FAIR CodeGen team et al. (2025) 的 exact matching 协议。偏离标准评估可能反而引入新的 confound。

**但我同意 relaxed matching 作为 robustness check 有价值**。建议作者对 1 个 seed 实施 fuzzy/semantic matching 作为附录补充，量化 bias magnitude。将此从 critical 调整为 warning 更合适。

---

**[AGREE] R1-N2: TOST ±2pp SESOI 论证不充分——但需注意论文已含 sensitivity analysis**

我在自己的审稿中也提出了同样的关切（我的 W2）。R1 关于不对称 cost 和 function/repo 应区分 SESOI 的观点完全正确。

**但 R1 可能遗漏了 Appendix J（Table 13）**——论文实际上已经提供了 ±1pp 到 ±5pp 的 sensitivity analysis。Table 13 显示最小等价 margin 为 ±1.52pp，在 ±2pp 时 TOST p=0.027。这说明即使将 margin 收紧到 ±1.52pp，等价结论仍然成立（尽管 p 值变为边界值 0.05）。在 ±1pp 时确实不通过（p=0.05, not significant after correction）。

所以 R1 的核心关切（SESOI justification 不充分、缺少 Wellek 2010 等方法论引用）我完全同意，但 "缺少 sensitivity analysis" 的具体建议——**论文已在 Appendix J 中完成**。应要求作者在正文中 reference Appendix J 并加强 SESOI 选择的理论论证。

---

### Should-Fix 回应

**[AGREE] R1-W1: Variant-level n=48, MDE≈25pp，power 严重不足**

论文在 page 5 底部承认 "functionally but underpowered (n=18, MDE≈25pp, Appendix K)"，但 Table 4 的 failure mode 比例分布（format collapse: 30/44=68.2%, decision collapse: 4/44=9.1% 等）仍被当作稳健发现来呈现。以 n=44 为例，68.2% 的 95% Wilson CI 约为 [53%, 80%]——置信区间宽达 27pp。这个 taxonomy 作为 descriptive observation 可以接受，但论文的叙述语气暗示了超出数据支撑的确定性。

**[AGREE] R1-W2: DeepSeek 仅 2 seeds 不足以支撑 "model-dependent" 的一般性结论**

完全同意。两个 model families × 有限 seeds 无法支撑 "model-dependent" 这样的一般性声明。这个 claim 需要 (a) 更多 model families（如 Llama-3、CodeLlama）或 (b) 将措辞从 "model-dependent" 弱化为 "observed to differ between our two tested model families"。我在自己的 Q1 中也提出了类似关切——model identity 解释了 >95% 的 predictable variance（Appendix M），这意味着 model selection 远比 formulation choice 重要。

**[AGREE] R1-W3: Checkpoint selection 不一致是实质性 confound**

CWM 使用 final epoch（因 NaN val loss 导致无法做 val-best selection）而 CLS 使用 val-best，确实使对比不完全公平。但我要补充一个 nuance：**NaN val loss 可能是 CWM formulation 的固有特征**，而非实现缺陷。Generation 模型在输出长度可变的 task 上出现 validation loss 不稳定是已知现象。如果 CWM 的 "最佳" checkpoint 恰好是 final epoch，这本身就是 formulation behavior 的一部分。

建议：(1) 报告 CWM 在 epoch 1-3 各 checkpoint 的精度曲线以证明 final epoch 确实最优；(2) 讨论 NaN val loss 是 formulation-specific 还是 hyperparameter-specific（如 learning rate、batch size 调整后是否消失）。

**[AGREE] R1-W4: TRAJ downsample ablation 范围过窄**

1 model × 1 seed × 1 level 确实不足。至少应覆盖 2 models × 2 seeds × 2 levels 才能初步排除 data volume 作为主要 confound。

**[AGREE] R1-W5: 应补充 cluster-robust SEs**

技术上正确。HC1 对 residual within-cluster correlation 的处理不如 cluster-robust SEs 或 wild cluster bootstrap。鉴于 DEFF 高达 114.3（repo-level），这不是 pedantic 的统计要求。

---

### Minor 回应

**[AGREE] R1-Minor-1**: clustered bootstrap 实施细节（block size、resample unit、iteration count）应在 Appendix 中记录。

**[AGREE] R1-Minor-2**: TRAJ 评估子集对齐问题值得标注——即使差异小，也应明确说明。

**[REBUT] R1-Minor-3**: Figure 2 y-axis 截断——论文已在 Figure 2 caption 中明确标注 "Note: y-axis begins at 55% to emphasize formulation differences"（page 7）。这是可视化的 best practice（截断 + 标注），不应被视为问题。R1 可能未注意到 caption 中的标注。

**[AGREE] R1-Minor-4**: DEFF=114.3 → effective n≈86 的含义应在正文或附录中明确讨论，包括对 Type II error rate 的影响。

---

### Questions 回应

**R1-Q1（CWM exact match 中多少"错误"是语义正确的？）**: 好问题。Appendix N 的 parseable bias analysis 部分回应了此问题（将 unparseable 和 parseable 分离），但未直接量化 "语义正确但格式不同" 的比例。Manual inspection 一个 seed 确实是最直接的验证方式。[AGREE] 应补充。

**R1-Q2（SESOI sensitivity）**: **论文已回答——见 Appendix J, Table 13**。最小等价 margin = ±1.52pp。R1 的 ±1pp 到 ±3pp 范围恰好被覆盖。但此结果仅出现在附录中，应在正文 §3.4 中至少 reference 一句。

**R1-Q3（CWM NaN val loss 原因）**: 值得深入分析。我推测原因是 CWM 的 output length variance 导致 per-token loss 在不同 batch 间波动剧烈，积累到 epoch-level 后 val loss 不稳定。如果确认是 formulation 固有的，这本身就是 CWM formulation 的一个 documented weakness。[AGREE] 作者应回答。

**R1-Q4（β_interaction=0.219 的 scale 和 random effects variance）**: 技术上重要。β=0.219 的 log-odds scale 换算为 pp 取决于 baseline probability，在 ~85% accuracy 附近约对应 ~2-3pp 的 marginal effect。Random effects variance 的报告对评估 model-level heterogeneity 至关重要。[AGREE] 应补充。

**R1-Q5（Table 15 k=5 comparisons 的选择依据）**: 合理的方法论问题。如果是 post-hoc 选择的 5 个比较，Holm-Bonferroni 的校正可能不够保守（应基于所有可能的 pairwise comparisons）。如果包括 repo-level equivalence comparisons，校正后的 p 值会更高。[AGREE] 应澄清。

---

### Missing References 回应

**[AGREE] Moulton (1990)**: 经典 clustered data 文献，鉴于论文大量使用 clustered 分析（bootstrap、ICC、DEFF），引用此文作为方法论基础是合理的。

**[AGREE] Wellek (2010)**: TOST 是论文的核心统计方法之一，引用等价检验的标准教材是必要的。当前仅引用了 Schuirmann (1987) 和 TOST 原始文献，Wellek 的综合性教材可加强方法论背景。

---

### 综合评价

R1 的审稿在统计方法论上极为细致，提出的问题大多数是有实质性的。我同意 R1 12 条意见中的 10 条（包括两条 must-fix 的核心关切），仅在 Figure 2 y-axis（已有标注）和 SESOI sensitivity（Appendix J 已覆盖）上有不同看法。

**但我对 N1 的严重程度评估与 R1 不同**：鉴于 function-level unparseable rate 仅 1.39%，exact matching 偏差的实际影响极小。建议将 N1 从 critical 降为 warning，配合 relaxed matching robustness check。

**整体来看，R1 的 3.5 (Borderline Conference) 评分比我的 3.0 (Findings) 更乐观**。考虑到 R1 自己识别的这些方法论问题（特别是 repo-level confounds、limited seeds、checkpoint inconsistency），这些问题的累积效应应该对评分有更大的 downward pressure。我认为在这些问题解决之前，3.0 (Findings) 是更准确的定位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 727 · 2026-05-22T15:02:25.115075+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 63

## Round 63

14 recorded events


### User

_source line 728 · 2026-05-22T15:02:27.640397+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: "Design space" framing 过度**

同意实质性判断。论文探索的维度是 {CLS, CWM, TRAJ} × {4B, 8B} × {function, repo} × {Qwen3, DeepSeek}——这是一个 formulation comparison matrix，不是通常意义上的 "design space exploration"（后者应涵盖 loss function 变体、decoding 策略、output format 设计等）。§3.3–§3.7 分析了 formulation × complexity × scale 的交互，但自变量仍是 3 个离散 formulations。

不过，我认为此问题的严重性是 **framing/presentation 级别**而非方法论缺陷——调整标题和 §1 的 contribution 表述（如改为 "systematic comparison"）即可解决，不应算作 Must-Fix。建议降级为 Should-Fix。

**[AGREE with nuance] R2-N2: Function-level 等价性发现的 novelty 有限**

部分同意。在 function-level task 上 classification 和 generation 趋同确实在预期之内，单独作为 contribution 偏弱。但有两点补充：
1. 论文的贡献不仅是 *发现* 等价性，而是用 TOST equivalence test（而非 NHST non-significance）**严格证明**等价性——这在 NLP empirical 研究中罕见且方法论上有价值（§3.4）。
2. 更核心的贡献是精确刻画 *等价性在何处崩溃*（§3.5 repo-level divergence, §3.3 complexity-dependent behavior）。等价性本身是三层结构的 baseline，而非独立 insight。

建议：弱化 "near-equivalence" 作为独立 contribution 的措辞，将其融入三层结构框架的叙述中。同意方向，但 Must-Fix severity 过高。

---

### Should-Fix

**[AGREE] R2-W1: Repo-level 结论受 model identity 主导**

完全同意。Appendix M 明确报告 model identity 解释 >95% predictable variance（formulation × complexity interaction 的 β=0.219, z=−23.7, p<0.001，但 formulation main effect 在 function level 不显著）。这意味着选择 base model 远比选择 formulation 重要。结合 8B 仅 3 seeds，repo-level 的 formulation-specific 结论确实脆弱。此发现与我的 variant-level power 担忧（R1-W1, MDE≈25pp at n=48）指向同一问题：repo-level 证据不足以支撑 strong causal claims。

**[AGREE] R2-W2: TOST ±2pp 缺乏 justification**

完全同意——此点与我的 R1-N2 重叠。两位 reviewer 独立标记同一问题增加了其权重。特别支持 R2 提出的"在安全关键场景中 2pp 可能 practically significant"这一论点。

**[REBUT] R2-W3: CWM 术语与 world model 文献脱节**

不同意。"Code World Model" 是 FAIR CodeGen team et al. (2025) 的原始术语（§2.1 引用），论文作者是在沿用已发表工作的established terminology，而非自行命名。§3.1 明确声明："Our CWM baseline is a LoRA fine-tuned variant for matched comparison, not a reproduction of the 32B Code World Model."——论文既没有对 CWM 做超出原文的 "internal simulation" 声称，也没有试图重新定义这一术语。要求作者为他人的命名负责不太合理。如果 R2 的担忧是术语可能误导不熟悉该文献的读者，一句脚注澄清即可（如 "CWM refers to the output-generation formulation of FAIR CodeGen team et al., 2025, not a general-purpose world model"），但这至多是 Minor issue。

**[REBUT] R2-W4: 缺少与 execution-based verification 的直接精度对比**

不同意这是一个缺陷。论文的研究问题明确限定在 execution-FREE formulations 之间的比较（Title, Abstract, §1），不是关于 execution-free vs execution-based 的 gap。引入 execution-based baseline 会改变核心研究问题。

此外，论文已提供了间接参照点：
- §3.6 报告 oracle combination accuracy 90.63%（seed 42），代表 execution-free formulations 的理论上限
- Appendix A Table 5 提供了 per-test advantage 的分层分析
- §4 Related Work 讨论了 FAIR CodeGen team et al. (2025)、RepoExec (Hai et al., 2025) 等 execution-based 工作

如果 R2 认为需要量化 gap，可以建议在 §4 或 §5 增加一段引用文献中已报告的 execution-based accuracy 作为 reference point，但这不应是 Should-Fix。

**[PARTIAL AGREE] R2-W5: 遗漏 CodeScaler (arXiv 2602.17684)**

我无法独立验证此引用的存在性和相关性。如果该工作确实是 execution-free reward model 且在本文提交前已公开，则应在 §4 Related Work 中引用。但需要作者核实引用真实性。

---

### Minor

**[REBUT] R2-M1: Table 1 TRAJ "not informational" 与 §3.2 矛盾**

不矛盾。Table 1 footnote 中 "not informational" 指的是 DeepSeek-Coder 的 2-seed TRAJ 结果**在统计推断层面**不具信息量（样本不足以做 inference）。§3.2 讨论的是 TRAJ formulation **固有的 per-test diagnostic 能力**作为一种 formulation property。前者是关于特定实验配置的统计功效，后者是关于 formulation 设计的结构性特征——概念上是不同层面的陈述。不过，措辞上确实可能造成混淆，建议将 Table 1 footnote 改为 "insufficient seeds for statistical inference" 以消除歧义。

**[AGREE] R2-M2: Figure 3 y-axis 不从 0 开始**

同意。Figure 2 有 y-axis 截断的 note（"Note: y-axis begins at 55%"），但 Figure 3（Appendix A, page 13）的 bar chart 似乎也未从 0 开始且缺少类似注释。应保持一致。

**[AGREE] R2-M3: Abstract 第一句过于绝对**

同意。"LLM-based program repair increasingly relies on..." 中 "relies" 过于绝对。部分 repair 方法使用 direct generation 或 ranking 策略而不依赖 verifier。建议改为 "increasingly leverages" 或 "often uses"。

**[REBUT] R2-M4: §2.2 failure mode taxonomy 偏向 CWM**

不同意这是 bias。CWM 作为 generation formulation，其 failure mode 天然比 CLS（binary misclassification）和 TRAJ（aggregation of CLS/CWM predictions）更复杂——format collapse、truncation、hallucinated output 等 generation-specific 问题需要更多篇幅来定义。CLS 的 failure mode 本质上就是 FP/FN，不需要等量的 taxonomic 复杂度。§3.6 的 error complementarity 分析确实覆盖了 CLS 和 CWM 的双向错误模式，Appendix H 的 qualitative analysis 也分析了两者。

但建议在 §2.2 增加一句话明确 CLS 和 TRAJ 的 failure mode 特征（即使简短），以改善表述平衡。

**[REBUT] R2-M5: Appendix P "Extended Limitations" 暗示正文 Limitations 不完整**

这是 *ACL 系 venue 在严格页数限制下的标准做法。正文 Limitations（page 8）覆盖了核心限制（model scale, CWM baseline, seed coverage, synthetic mutations, confounds），Appendix P 提供了因正文空间限制无法展开的细节（如 CWM scale/pretraining, matched-sequence evaluation 等）。这是负责任的学术写作，不是正文不完整的信号。

---

### Questions

**[AGREE] R2-Q1**: 完全同意这是关键问题。Appendix M 的 model identity dominance 意味着 formulation ranking 在不同 base model 上的稳定性存疑。论文仅覆盖 2 个 model family，不足以排除 ranking reversal。

**[AGREE] R2-Q2**: 同意，且此点与我的 R1-N2 和 R2-W2 一致。论文应明确声明 ±2pp 是否为 pre-registered。

**[AGREE] R2-Q3**: CWM format collapse 是否主要是 data quantity 问题值得追问。Appendix I 报告 "four targeted interventions—increased LoRA rank, majority voting, relaxed output matching, and model scaling (4B→8B)—all fail to close the gap"，这暗示问题不完全是 data quantity，但论文未直接测试增加 CWM training data 的效果。

**[AGREE] R2-Q4**: §3.6 明确报告 oracle accuracy 是 single-seed（seed 42）估计。这一数字的跨 seed 稳定性未验证，是一个合理的关注点。

**[AGREE] R2-Q5**: 论文确认无 >8B 或 full fine-tuning 数据（Limitations, page 8）。在 ≤8B LoRA 范围内的结论能否泛化到更大规模是 open question。

---

### Missing References

**[REBUT] Self-Execution Simulation (arXiv 2604.03253)**: 此文**已被引用**。References 第 10 页明确列出："Gulib Maussion, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, and Yossi Adi. 2025. Self-execution simulation improves coding models. arXiv preprint arXiv:2604.03253." R2 似乎遗漏了此引用。

其余三篇（CodeScaler, GenPRM, ExecVerify）我无法独立验证其存在性和相关性，建议作者核实后按相关性决定是否补充引用。

---

### 总结

R2 的意见整体合理。我们在以下问题上 **高度一致**：
1. TOST ±2pp SESOI 论证不足（R2-W2 = R1-N2）——两位 reviewer 独立标记
2. Repo-level 结论的 robustness 受限于 model identity dominance 和 limited seeds（R2-W1 ≈ R1-W1/W2）
3. Function-level 等价性的 novelty 有限（R2-N2，我部分同意）

我们 **分歧** 最大的是：
1. R2-W3 CWM 术语问题——我认为这是沿用 established terminology，不是论文的问题
2. R2-W4 缺少 execution-based 对比——我认为超出论文 scope
3. R2-N1 的严重性——framing issue 不应算 Must-Fix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-22T15:02:56.420781+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 730 · 2026-05-22T15:02:56.471627+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T14:49:30.133884+00:00\", \"completed_at\": \"2026-05-22T14:52:08.545460+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前两页连续纯文本，无任何 display item。第一个视觉锚点（Figure 1）直到第 3 页才出现。审稿人翻开论文后需要读完近 2 整页密集文字才能看到第一张图，延迟了锚定效应。建议：若空间允许，可将 Figure 1 提前至第 2 页（如将部分 §2 正文推后），或在第 1 页末尾加入一个概览性的 teaser figure\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Related Work（§4）+ Conclusion（§5）+ Limitations 三个章节全部挤在第 8 页。文字极度密集，段间距被压缩到最小，给审稿人\\\"赶工\\\"的印象。这是 8 页限制的必然结果，但 Related Work 若能再压缩 3-5 行可显著改善呼吸感\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 内部文字（如 \\\"Token\\\", \\\"Model\\\", \\\"Output Length\\\" 等标签和箱内示例文本）字号偏小，约为正文 60-65%。在打印或低分辨率屏幕上可能需要审稿人放大阅读\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 采用单栏宽度，y 轴从 55% 起始并有文字标注（良好实践）。柱状图颜色为单色蓝，区分度不成问题。但图注文字 \\\"Note: y-axis begins at 55%...\\\" 字号较小\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix Figure 3 使用蓝/绿/青三色柱状图，这三种颜色对 deuteranopia（红绿色盲）用户区分度有限。建议改用 Okabe-Ito 色板或增加 hatch pattern 辅助区分\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 和 Table 3 紧密堆叠在同一页，间距合理，无溢出。两表均使用 booktabs + 粗体最优标记，格式统一\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 4（failure mode taxonomy）文字密集，百分比数据多，但排版清晰。\\\"Representative\\\" 列的示例文字较长，保持了可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段落紧凑，覆盖了 3 个关键点（repo-level CWM 条件性、synthetic mutation、fine-tuning 必要性），符合 EMNLP 要求的简洁 limitations\"}], \"counts\": {\"critical\": 0, \"warning\": 2, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-22T15:02:56.472139+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-22T15:02:56.472406+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-22T15:05:11.596669+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues,submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues,submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-22T15:05:11.647274+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-22T15:05:16.666239+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update review issues submit report",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update review issues submit report",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-22T15:05:16.716835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-22T15:07:32.370405+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. 但 model identity dominance 和 variant-level power 仍未在正文充分讨论。\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS epoch ablation <1pp. CWM NaN val loss 原因未在正文讨论。\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 发现概念上可预期\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度, 实际只比较了三个 formulation. R2-N2: function-level 等价性可预期. R1 部分同意 (framing issue not methodological). Director 裁定: design space framing 为 Must-Fix, function-level novelty 为 Should-Fix.\"\n  action_items:\n    - round: 6\n      action: \"Reframe + W5 interaction test\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"标题和 §1 framing 从 'design space' 调整为 'systematic comparison'; function-level equivalence 融入三层结构叙述而非独立 contribution\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Interaction test 完成但 framing 仍需调整。\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 循环论证 + headroom 误导\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap. 修复确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。R1-N2: 缺 domain-specific justification, 不对称 cost structure, 未区分 complexity level. R2-W2: 安全关键场景中 2pp 可能 significant. Appendix J 有 sensitivity analysis 但正文未引用。\"\n  action_items:\n    - round: 6\n      action: \"重写 SESOI justification\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity; 引用 Wellek (2010)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"R7 修复了循环论证，但 R9 发现 domain-specific justification 仍不足。\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level. 不足以排除 data volume 作为 confound.\"\n  action_items:\n    - round: 6\n      action: \"讨论 volume vs granularity 区别\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"interaction test z=-23.7 已完成.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被提出。interaction test 已完成并在正文中出现。视为已修复。\"\n  action_items:\n    - round: 6\n      action: \"Mixed-effects regression\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler (arXiv 2602.17684). 另提 GenPRM (AAAI 2026), ExecVerify (arXiv 2603.11226). Self-Execution Simulation 已在 references 中。R1 要求核实引用真实性。\"\n  action_items:\n    - round: 8\n      action: \"GenRM + RepoExec + Chen et al.\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"WebSearch 验证 CodeScaler, GenPRM, ExecVerify 真实性后按相关性加入\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Figure 2 已有 y-axis 截断标注。视觉审查未标记 Figure 2 为问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被提出。§3.4 现在分开呈现 CLS-CWM TOST (p=0.007) 和 CLS-TRAJ TOST (p=0.025)。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"§5.2 重构分开呈现\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 裁定 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Abstract 现含 '≤8B LoRA protocol' 和 'DeepSeek-Coder' 标注。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 regime qualifier + model 标注\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 repo-level CLS-TRAJ 比较严重欠 power\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n  action_items:\n    - round: 8\n      action: \"Conclusion reframe\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。两人共识。\"\n  action_items:\n    - round: 8\n      action: \"正文 oracle mentions 加 binomial CI\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Qwen3 CWM 无 epoch-1 checkpoint.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 加 Qwen3 CWM convergence 交叉验证\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 C2 合并处理.\"\n    - round: 9\n      reviewers: []\n      note: \"Abstract 现含 'DeepSeek-Coder' 标注。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract + Intro 加 (DeepSeek-Coder)\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"GenRM must-cite.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2 额外提出 CodeScaler, GenPRM, ExecVerify. 合并至 R6-W8.\"\n  action_items:\n    - round: 8\n      action: \"WebSearch 验证后加入\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Abstract 已含 regime qualifier。Limitations 讨论了 scale 限制。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 regime qualifier\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference). 共识: novelty 不足 Main, Findings 合适。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提出。§3.4 footnote 已讨论 NF4 vs bfloat16。\"\n  action_items:\n    - round: 8\n      action: \"§5.2 脚注标注 bfloat16-only TOST 子集结果\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation. 应补充 cluster-robust SEs.\"\n  action_items:\n    - round: 8\n      action: \"Appendix: robust SEs + prompt templates + scaling exploratory 标注\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"Appendix M 补充 cluster-robust SEs 和 logistic regression 具体系数\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 9 (Fresh Review) New Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 rated critical, R1 agrees as Should-Fix (framing not methodology). Director 裁定 Must-Fix: 影响 reviewer 第一印象。合并至 R6-N4 action items.\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 改为 'systematic comparison' 或同等表述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 降为 warning (function-level unparseable 仅 1.39%, bias <1pp). Director 裁定 Should-Fix.\"\n  action_items:\n    - round: 9\n      action: \"对 1 个 function-level seed 做 relaxed matching 或 manual inspection 作为 robustness check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人共识。'model-dependent' 应改为 'observed to differ between Qwen3 and DeepSeek-Coder'.\"\n  action_items:\n    - round: 9\n      action: \"Abstract/正文 'model-dependent' 改为描述性表述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注（Figure 2 有标注）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M2, R1 agrees.\"\n  action_items:\n    - round: 9\n      action: \"Figure 3 加 y-axis 截断标注\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M3, R1 agrees. 建议改为 'increasingly leverages'.\"\n  action_items:\n    - round: 9\n      action: \"Abstract 第一句 'relies on' → 'increasingly leverages'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Missing References.\"\n  action_items:\n    - round: 9\n      action: \"加入 Wellek (2010) 和 Moulton (1990)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Minor.\"\n  action_items:\n    - round: 9\n      action: \"Appendix 补充 bootstrap procedure 描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Minor.\"\n  action_items:\n    - round: 9\n      action: \"正文或附录讨论 effective sample size 对 repo-level 推断的限制\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. 但 model identity dominance 和 variant-level power 仍未在正文充分讨论。\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS epoch ablation <1pp. CWM NaN val loss 原因未在正文讨论。\"\n  resolution_round: 7\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：repo-level 发现概念上可预期\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度, 实际只比较了三个 formulation. R2-N2: function-level 等价性可预期. R1 部分同意 (framing issue not methodological). Director 裁定: design space framing 为 Must-Fix, function-level novelty 为 Should-Fix.\"\n  action_items:\n    - round: 6\n      action: \"Reframe + W5 interaction test\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"标题和 §1 framing 从 'design space' 调整为 'systematic comparison'; function-level equivalence 融入三层结构叙述而非独立 contribution\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Interaction test 完成但 framing 仍需调整。\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 循环论证 + headroom 误导\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap. 修复确认。\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。R1-N2: 缺 domain-specific justification, 不对称 cost structure, 未区分 complexity level. R2-W2: 安全关键场景中 2pp 可能 significant. Appendix J 有 sensitivity analysis 但正文未引用。\"\n  action_items:\n    - round: 6\n      action: \"重写 SESOI justification\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity; 引用 Wellek (2010)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"R7 修复了循环论证，但 R9 发现 domain-specific justification 仍不足。\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level. 不足以排除 data volume 作为 confound.\"\n  action_items:\n    - round: 6\n      action: \"讨论 volume vs granularity 区别\"\n      assigned_to: \"paper\"\n      status: in_progress\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"interaction test z=-23.7 已完成.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被提出。interaction test 已完成并在正文中出现。视为已修复。\"\n  action_items:\n    - round: 6\n      action: \"Mixed-effects regression\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler (arXiv 2602.17684). 另提 GenPRM (AAAI 2026), ExecVerify (arXiv 2603.11226). Self-Execution Simulation 已在 references 中。R1 要求核实引用真实性。\"\n  action_items:\n    - round: 8\n      action: \"GenRM + RepoExec + Chen et al.\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"WebSearch 验证 CodeScaler, GenPRM, ExecVerify 真实性后按相关性加入\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Figure 2 已有 y-axis 截断标注。视觉审查未标记 Figure 2 为问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被提出。§3.4 现在分开呈现 CLS-CWM TOST (p=0.007) 和 CLS-TRAJ TOST (p=0.025)。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"§5.2 重构分开呈现\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 裁定 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Abstract 现含 '≤8B LoRA protocol' 和 'DeepSeek-Coder' 标注。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 regime qualifier + model 标注\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 repo-level CLS-TRAJ 比较严重欠 power\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n  action_items:\n    - round: 8\n      action: \"Conclusion reframe\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。两人共识。\"\n  action_items:\n    - round: 8\n      action: \"正文 oracle mentions 加 binomial CI\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Qwen3 CWM 无 epoch-1 checkpoint.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n  action_items:\n    - round: 8\n      action: \"Appendix 加 Qwen3 CWM convergence 交叉验证\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 C2 合并处理.\"\n    - round: 9\n      reviewers: []\n      note: \"Abstract 现含 'DeepSeek-Coder' 标注。可能已修复，待确认。\"\n  action_items:\n    - round: 8\n      action: \"Abstract + Intro 加 (DeepSeek-Coder)\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"GenRM must-cite.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2 额外提出 CodeScaler, GenPRM, ExecVerify. 合并至 R6-W8.\"\n  action_items:\n    - round: 8\n      action: \"WebSearch 验证后加入\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未独立提出。Abstract 已含 regime qualifier。Limitations 讨论了 scale 限制。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 regime qualifier\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference). 共识: novelty 不足 Main, Findings 合适。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"本轮未提出。§3.4 footnote 已讨论 NF4 vs bfloat16。\"\n  action_items:\n    - round: 8\n      action: \"§5.2 脚注标注 bfloat16-only TOST 子集结果\"\n      assigned_to: \"agent\"\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation. 应补充 cluster-robust SEs.\"\n  action_items:\n    - round: 8\n      action: \"Appendix: robust SEs + prompt templates + scaling exploratory 标注\"\n      assigned_to: \"agent\"\n      status: in_progress\n    - round: 9\n      action: \"Appendix M 补充 cluster-robust SEs 和 logistic regression 具体系数\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 9 (Fresh Review) New Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 rated critical, R1 agrees as Should-Fix (framing not methodology). Director 裁定 Must-Fix: 影响 reviewer 第一印象。合并至 R6-N4 action items.\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 改为 'systematic comparison' 或同等表述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 降为 warning (function-level unparseable 仅 1.39%, bias <1pp). Director 裁定 Should-Fix.\"\n  action_items:\n    - round: 9\n      action: \"对 1 个 function-level seed 做 relaxed matching 或 manual inspection 作为 robustness check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人共识。'model-dependent' 应改为 'observed to differ between Qwen3 and DeepSeek-Coder'.\"\n  action_items:\n    - round: 9\n      action: \"Abstract/正文 'model-dependent' 改为描述性表述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注（Figure 2 有标注）\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M2, R1 agrees.\"\n  action_items:\n    - round: 9\n      action: \"Figure 3 加 y-axis 截断标注\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-M3, R1 agrees. 建议改为 'increasingly leverages'.\"\n  action_items:\n    - round: 9\n      action: \"Abstract 第一句 'relies on' → 'increasingly leverages'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Missing References.\"\n  action_items:\n    - round: 9\n      action: \"加入 Wellek (2010) 和 Moulton (1990)\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Minor.\"\n  action_items:\n    - round: 9\n      action: \"Appendix 补充 bootstrap procedure 描述\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1 Minor.\"\n  action_items:\n    - round: 9\n      action: \"正文或附录讨论 effective sample size 对 repo-level 推断的限制\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
  }
}
```

</details>

---


### Tool result

_source line 738 · 2026-05-22T15:07:32.473530+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 21120}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 739 · 2026-05-22T15:09:38.737101+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "\n# 审稿报告 — Round 9 (Fresh Review)\n\n**项目**: exec-sim-repair-verifier\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿轮次**: 1 轮独立审稿 + 1 轮交叉分享（关键问题已收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在匹配 LoRA 微调条件下跨两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多种随机种子进行实验。主要发现：function-level CLS-CWM 统计等价（TOST p=0.007），repo-level 在 ≤8B LoRA 下出现 18-26pp 分歧（z=−23.7），识别三种失败模式（format collapse、decision collapse、aggregation penalty），以及错误互补性（oracle 90.63%/95.83%）。实验设计和统计方法在 NLP 实证研究中属上乘水平，但核心发现的 novelty 有限，repo-level 结论受多重 confounds 限制。\n\n---\n\n## Strengths\n\n**S1. 匹配实验设计的严谨性** [consensus]\n三种 formulation 共享相同训练数据、LoRA 配置、seed 和 evaluation protocol。在 formulation comparison 中达到了罕见的 controlled comparison 水平。这是论文最核心的方法论贡献。\n\n**S2. 统计方法论完整且优于领域平均** [consensus]\nTOST 等价检验（非 NHST non-significance）、clustered bootstrap with ICC/DEFF、Holm-Bonferroni 校正、mixed-effects regression——层层递进，正确选择且正确应用。\n\n**S3. Threats to Validity 透明度高** [consensus]\n§5.5 和 Appendix O 逐一识别并用实验证据量化 5 个 confound，超过大多数 NLP 论文仅做定性承认的水平。\n\n**S4. Failure Mode Taxonomy 有实用价值** [consensus]\nTable 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）定义清晰、有实例支撑，为 practitioner 选择 formulation 提供可操作的诊断框架。\n\n**S5. Error Complementarity 是最具洞察力的发现** [consensus]\nOracle 组合在 function-level 达 90.63%、repo-level variant-level 达 95.83%，表明不同 formulation 的错误模式是互补的。此发现不可从单一 formulation 结果推导，为 ensemble/routing 提供了实证基础。\n\n**S6. 附录极其充分** [consensus]\n14 页附录覆盖 ablations、error analysis、statistical tests、qualitative examples、convergence analysis，展现扎实实验工作量。可复现性评分 4/5。\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. TOST ±2pp SESOI 论证不充分** [全票共识: R1-N2, R2-W2]\n两位 Reviewer 独立标记。±2pp 是等价检验框架中最关键的参数——直接决定 TOST 能否拒绝 H₀。当前论证（\"2pp ≈ 2-3 problems out of 114, comparable to seed noise\"）存在循环论证风险（seed noise 是实验属性而非领域阈值）。三个不足：(a) 代码验证中漏检 critical bug vs FP 成本不对称，flat ±2pp 不反映此结构；(b) function-level 和 repo-level 的 2pp 含义完全不同但 SESOI 未区分；(c) 未引用等价检验方法论文献（如 Wellek, 2010）。Appendix J 已有 sensitivity analysis（±1pp~±5pp，最小等价 margin ±1.52pp），但正文未引用。\n**修复**: §3.4 加 domain-grounded SESOI justification；正文引用 Appendix J；引用 Wellek (2010)。\n\n**C2. Contribution Novelty 与 \"Design Space\" Framing 不匹配** [R2 critical, R1 agrees Should-Fix; Director 裁定 Must-Fix]\n标题声称 \"Formulation Design Space\"，但实际只比较三个已知 formulation（二分类、输出生成、序列分类）。真正的 design space 应涵盖 loss function 变体、decoding 策略、output format 设计等更多维度。这是 presentation issue（非方法论缺陷），但影响 reviewer 第一印象。\n**修复**: 标题和 §1 从 \"design space\" 调整为 \"systematic comparison\"。\n\n### Should-Fix（共识或多数）\n\n**W1. Repo-level 因果性 claims 被 model identity dominance 削弱** [全票: R1-W1/W2, R2-W1]\nAppendix M 报告 model identity 解释 >95% predictable variance；formulation×complexity interaction (z=−23.7) 统计显著但相对 model effects 较小。结合 8B repo-level 仅 3 seeds/model、variant-level n=48 (MDE≈25pp)，repo-level 结论不支持 strong causal claims。Abstract \"model-dependent\" 从 2 个 model family 过度泛化。\n**修复**: (a) 正文讨论 model identity dominance（当前仅在 Appendix M）；(b) \"model-dependent\" 改为描述性表述；(c) variant-level 分析标注为 exploratory/descriptive。\n\n**W2. CWM 评估指标非对称性未量化** [R1 critical, R2 warning; Director 裁定 Should-Fix]\nCWM 使用 exact matching（保守）+ 不可解析输出默认 majority class (PASS)。两个偏差方向可能部分抵消。R2 指出 function-level unparseable 仅 1.39%，实际偏差 <1pp，不足以推翻 TOST 结论。Repo-level 的 parseable bias 在 Appendix N 已有分析。但 relaxed matching robustness check 可进一步加强 function-level 等价性证据。\n**修复**: 对 1 个 function-level seed 做 relaxed matching 或 manual inspection 作为 appendix robustness check。\n\n**W3. Function-level 等价性作为独立 Contribution 偏弱** [R2 critical, R1 部分同意]\n分类与生成在短输出 task 上趋同可预期。方法论贡献（TOST 严格证明等价性）有价值，但发现本身不构成 surprise。\n**修复**: 融入三层结构叙述，不作独立 contribution 列出；强调 TOST 方法论而非结论的贡献。\n\n**W4. Checkpoint Selection 不一致** [全票: R1-W3]\nCWM 所有 repo-level runs 因 NaN validation loss 使用 final epoch checkpoint；CLS 使用 val-best。CWM NaN val loss 可能是 formulation-inherent（可变输出长度导致 per-token loss 不稳定）——这本身是值得在正文讨论的 formulation weakness。\n**修复**: (a) 解释 CWM NaN val loss 原因；(b) 讨论是否 formulation-inherent；(c) 如可能，报告 CWM 多 checkpoint 精度。\n\n**W5. TRAJ Downsample Ablation 覆盖不足** [全票: R1-W4]\n1 model × 1 seed × 1 level 不足以排除 ~180× 数据量差异作为主要 confound。\n**修复**: 扩展至 ≥2 models 或明确标注为 limitation。\n\n**W6. 遗漏相关工作** [R2-W5, R1 部分同意]\n需验证并按相关性补充：CodeScaler (arXiv 2602.17684)、GenPRM (AAAI 2026)、ExecVerify (arXiv 2603.11226)。Self-Execution Simulation 已在 references 中（R2 误报遗漏）。\n**修复**: WebSearch 验证真实性后加入。\n\n### Minor\n\n**M1.** Appendix M 补充 cluster-robust SEs 和 logistic regression 具体系数（R1-W5, R2 agrees）。\n**M2.** Clustered bootstrap 实施细节（resample unit, block size）未说明（R1）。\n**M3.** Figure 3 (Appendix) y-axis 不从 0 开始但未标注，不同于 Figure 2 的良好实践（R2-M2, R1 agrees）。\n**M4.** Abstract 第一句 \"relies on\" 过于绝对，建议改为 \"increasingly leverages\"（R2-M3, R1 agrees）。\n**M5.** Repo-level DEFF=114.3 → effective n≈86 未讨论对推断的限制（R1）。\n**M6.** 缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data 经典文献（R1）。\n**M7.** Figure 1 内部文字偏小（~60-65% 正文），打印时可能需放大（视觉审查）。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立达成共识的关键判断：\n- [AGREE] TOST ±2pp SESOI 需更强论证（最高权重共识 issue）\n- [AGREE] Repo-level 结论受 model identity dominance、limited seeds、variant-level power 限制\n- [AGREE] Function-level 等价性 novelty 有限\n- [AGREE] DeepSeek 2-seed 不足以支撑 \"model-dependent\" 泛化\n- [AGREE] Checkpoint selection 不一致是实质性 confound\n- [AGREE] 统计方法论超过领域平均水平\n- [AGREE] 匹配实验设计是核心优势\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 裁定 |\n|-------|----|----|--------------|\n| CWM 评估非对称性严重性 | Must-Fix | Warning (func-level bias <1pp) | **Should-Fix** — function-level 偏差可忽略 |\n| \"Design space\" framing 严重性 | Should-Fix | Must-Fix | **Must-Fix** — 影响第一印象 |\n| CWM 术语 (R2-W3) | Rebut (沿用已发表术语) | Should-Fix | **Dismissed** — 作者使用 established terminology |\n| 缺 execution-based 对比 (R2-W4) | Rebut (超出论文 scope) | Should-Fix | **Dismissed** — 超出论文明确界定的研究问题 |\n| Failure mode taxonomy 偏向 CWM (R2-M4) | Rebut (CWM 天然更复杂) | Minor | **Dismissed** — R1 论证有说服力 |\n| Extended Limitations (R2-M5) | Rebut (ACL 标准做法) | Minor | **Dismissed** — 页数限制下的标准做法 |\n\n---\n\n## Questions for Authors\n\n1. CWM function-level exact match 中有多少比例的 \"错误\" 实际上是语义正确但格式不同？manual inspection 一个 seed 即可回答。[全票]\n2. ±2pp SESOI 是 pre-registered 还是 post-hoc？如果 post-hoc，TOST 框架的效力减弱。[全票]\n3. CWM repo-level runs 出现 NaN validation loss 的原因？formulation-inherent 还是 implementation issue？如果前者，是值得在正文讨论的 formulation weakness。[全票]\n4. Oracle complementarity (90.63%/95.83%) 为 single-seed 估计——跨 seed 是否稳定？[全票]\n5. 是否有 >8B 或 full fine-tuning 的 pilot data 暗示结论可能不同？[全票]\n\n---\n\n## Missing References\n\n**已确认需要**:\n- Wellek, S. (2010). \"Testing Statistical Hypotheses of Equivalence and Noninferiority.\" — TOST 方法论标准教材\n- Moulton, B. R. (1990). \"An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units.\" — clustered data 经典文献\n\n**需作者验证真实性后补充**:\n- CodeScaler (arXiv 2602.17684, Feb 2026) — execution-free reward model\n- GenPRM (AAAI 2026, arXiv 2504.00891) — generative PRM with code verification\n- ExecVerify (arXiv 2603.11226) — RL with verifiable stepwise rewards\n- Self-Execution Simulation — **已在 references 中引用**（R2 误报遗漏）\n\n---\n\n## External Review\n\n外部审稿：未请求（项目未启用 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 6 info）：\n\n**Warning**:\n- 前两页连续纯文本无 display item，Figure 1 直到第 3 页才出现。审稿人需读完 ~2 页密集文字才看到第一张图，延迟锚定效应。建议将 Figure 1 提前或增加 teaser figure。\n- 第 8 页 Related Work + Conclusion + Limitations 三节挤压，文字极度密集，给审稿人\"赶工\"印象。若 Related Work 能再压缩 3-5 行可改善呼吸感。\n\n**Info**:\n- Figure 1 内部文字 ~60-65% 正文字号，打印可能需放大\n- Figure 2 y-axis 截断已标注（良好实践）\n- Figure 3 (Appendix) 蓝/绿/青三色对色盲用户区分度有限，建议 Okabe-Ito 色板或 hatch pattern\n- Table 2/3 排版清晰，Table 4 可读性良好\n- Limitations 简洁覆盖 3 点，符合 EMNLP 要求\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**定位：Findings of ACL，不足以进入 Main Conference。**\n\n这是一篇方法论严谨度超过该领域平均水平的实证研究。匹配实验设计、多层统计检验、透明的 threats to validity 在 NLP empirical papers 中属上乘。Failure mode taxonomy 和 error complementarity 有实用价值。\n\n但 novelty 和 excitement 不足以支撑 Main conference：\n1. \"Design space\" framing 与实际三 formulation 比较之间有张力——论文是 rigorous formulation comparison，不是 design space exploration\n2. Function-level 等价性在很大程度上可预期（短输出下分类与生成趋同）\n3. Repo-level 结论严重受限于 ≤8B LoRA regime、model identity dominance (>95% variance)、limited seeds、n=48 variant-level power\n4. 核心发现（generation 在复杂输出上格式崩溃）对 practitioner 而言不意外\n\n**Findings 接收合适**。实验框架和统计方法论对领域有参考价值，failure mode taxonomy 和 error complementarity 可供后续工作引用。若能扩展至更多 model families、增加 repo-level seeds、解决 SESOI domain justification，有潜力提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"formulation design space\" → \"systematic formulation comparison\" 更准确\n- Contribution 1 (function-level equivalence) 可融入三层结构叙述，不必独立列出\n- \"model-dependent\" (TRAJ parity) 应弱化为 \"observed to differ between tested families\"\n\n### §2 Method\n- §2.2 failure mode taxonomy：可增加 1-2 句 CLS/TRAJ 的失败模式特征描述\n- SESOI ±2pp 在 §3.4 应有 domain-grounded justification 并 reference Appendix J\n\n### §3 Experiments\n- Table 1 footnote \"not informational\" → \"insufficient seeds for statistical inference\" 更清晰\n- §3.4 应在正文引用 Appendix J 的 TOST sensitivity analysis\n- §3.5 应讨论 model identity dominance（当前仅在 Appendix M）\n- §3.7 CWM NaN val loss 值得作为 formulation-specific weakness 在正文讨论\n- Variant-level 分析（Table 4, §3.5）应明确标注为 exploratory/descriptive\n\n### §4 Related Work\n- 核实并按相关性补充 CodeScaler、GenPRM、ExecVerify\n- 加入 Wellek (2010) 和 Moulton (1990) 方法论引用\n\n### §5 Conclusion\n- \"CLS is recommended primarily for its throughput advantage\" 定位合理 ✓\n- ≤8B LoRA regime qualifier 已出现 ✓\n\n### Appendix\n- Appendix J (TOST sensitivity) 应在正文 §3.4 被引用\n- Appendix M 应补充 cluster-robust SEs 和 logistic regression 具体系数\n- Clustered bootstrap 实施细节应补充（resample unit, block size, iteration count）\n- DEFF=114.3 → effective n≈86 的含义应在正文或附录讨论\n",
  "project": "exec-sim-repair-verifier",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "\n# 审稿报告 — Round 9 (Fresh Review)\n\n**项目**: exec-sim-repair-verifier\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性与完整性）\n**审稿轮次**: 1 轮独立审稿 + 1 轮交叉分享（关键问题已收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文系统比较了三种 execution-free code verification formulation（CLS 二分类、CWM 输出生成、TRAJ 轨迹评分），在匹配 LoRA 微调条件下跨两个代码 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度层级和多种随机种子进行实验。主要发现：function-level CLS-CWM 统计等价（TOST p=0.007），repo-level 在 ≤8B LoRA 下出现 18-26pp 分歧（z=−23.7），识别三种失败模式（format collapse、decision collapse、aggregation penalty），以及错误互补性（oracle 90.63%/95.83%）。实验设计和统计方法在 NLP 实证研究中属上乘水平，但核心发现的 novelty 有限，repo-level 结论受多重 confounds 限制。\n\n---\n\n## Strengths\n\n**S1. 匹配实验设计的严谨性** [consensus]\n三种 formulation 共享相同训练数据、LoRA 配置、seed 和 evaluation protocol。在 formulation comparison 中达到了罕见的 controlled comparison 水平。这是论文最核心的方法论贡献。\n\n**S2. 统计方法论完整且优于领域平均** [consensus]\nTOST 等价检验（非 NHST non-significance）、clustered bootstrap with ICC/DEFF、Holm-Bonferroni 校正、mixed-effects regression——层层递进，正确选择且正确应用。\n\n**S3. Threats to Validity 透明度高** [consensus]\n§5.5 和 Appendix O 逐一识别并用实验证据量化 5 个 confound，超过大多数 NLP 论文仅做定性承认的水平。\n\n**S4. Failure Mode Taxonomy 有实用价值** [consensus]\nTable 4 的三类失败模式（format collapse, decision collapse, aggregation penalty）定义清晰、有实例支撑，为 practitioner 选择 formulation 提供可操作的诊断框架。\n\n**S5. Error Complementarity 是最具洞察力的发现** [consensus]\nOracle 组合在 function-level 达 90.63%、repo-level variant-level 达 95.83%，表明不同 formulation 的错误模式是互补的。此发现不可从单一 formulation 结果推导，为 ensemble/routing 提供了实证基础。\n\n**S6. 附录极其充分** [consensus]\n14 页附录覆盖 ablations、error analysis、statistical tests、qualitative examples、convergence analysis，展现扎实实验工作量。可复现性评分 4/5。\n\n---\n\n## Weaknesses\n\n### Must-Fix（共识 Critical）\n\n**C1. TOST ±2pp SESOI 论证不充分** [全票共识: R1-N2, R2-W2]\n两位 Reviewer 独立标记。±2pp 是等价检验框架中最关键的参数——直接决定 TOST 能否拒绝 H₀。当前论证（\"2pp ≈ 2-3 problems out of 114, comparable to seed noise\"）存在循环论证风险（seed noise 是实验属性而非领域阈值）。三个不足：(a) 代码验证中漏检 critical bug vs FP 成本不对称，flat ±2pp 不反映此结构；(b) function-level 和 repo-level 的 2pp 含义完全不同但 SESOI 未区分；(c) 未引用等价检验方法论文献（如 Wellek, 2010）。Appendix J 已有 sensitivity analysis（±1pp~±5pp，最小等价 margin ±1.52pp），但正文未引用。\n**修复**: §3.4 加 domain-grounded SESOI justification；正文引用 Appendix J；引用 Wellek (2010)。\n\n**C2. Contribution Novelty 与 \"Design Space\" Framing 不匹配** [R2 critical, R1 agrees Should-Fix; Director 裁定 Must-Fix]\n标题声称 \"Formulation Design Space\"，但实际只比较三个已知 formulation（二分类、输出生成、序列分类）。真正的 design space 应涵盖 loss function 变体、decoding 策略、output format 设计等更多维度。这是 presentation issue（非方法论缺陷），但影响 reviewer 第一印象。\n**修复**: 标题和 §1 从 \"design space\" 调整为 \"systematic comparison\"。\n\n### Should-Fix（共识或多数）\n\n**W1. Repo-level 因果性 claims 被 model identity dominance 削弱** [全票: R1-W1/W2, R2-W1]\nAppendix M 报告 model identity 解释 >95% predictable variance；formulation×complexity interaction (z=−23.7) 统计显著但相对 model effects 较小。结合 8B repo-level 仅 3 seeds/model、variant-level n=48 (MDE≈25pp)，repo-level 结论不支持 strong causal claims。Abstract \"model-dependent\" 从 2 个 model family 过度泛化。\n**修复**: (a) 正文讨论 model identity dominance（当前仅在 Appendix M）；(b) \"model-dependent\" 改为描述性表述；(c) variant-level 分析标注为 exploratory/descriptive。\n\n**W2. CWM 评估指标非对称性未量化** [R1 critical, R2 warning; Director 裁定 Should-Fix]\nCWM 使用 exact matching（保守）+ 不可解析输出默认 majority class (PASS)。两个偏差方向可能部分抵消。R2 指出 function-level unparseable 仅 1.39%，实际偏差 <1pp，不足以推翻 TOST 结论。Repo-level 的 parseable bias 在 Appendix N 已有分析。但 relaxed matching robustness check 可进一步加强 function-level 等价性证据。\n**修复**: 对 1 个 function-level seed 做 relaxed matching 或 manual inspection 作为 appendix robustness check。\n\n**W3. Function-level 等价性作为独立 Contribution 偏弱** [R2 critical, R1 部分同意]\n分类与生成在短输出 task 上趋同可预期。方法论贡献（TOST 严格证明等价性）有价值，但发现本身不构成 surprise。\n**修复**: 融入三层结构叙述，不作独立 contribution 列出；强调 TOST 方法论而非结论的贡献。\n\n**W4. Checkpoint Selection 不一致** [全票: R1-W3]\nCWM 所有 repo-level runs 因 NaN validation loss 使用 final epoch checkpoint；CLS 使用 val-best。CWM NaN val loss 可能是 formulation-inherent（可变输出长度导致 per-token loss 不稳定）——这本身是值得在正文讨论的 formulation weakness。\n**修复**: (a) 解释 CWM NaN val loss 原因；(b) 讨论是否 formulation-inherent；(c) 如可能，报告 CWM 多 checkpoint 精度。\n\n**W5. TRAJ Downsample Ablation 覆盖不足** [全票: R1-W4]\n1 model × 1 seed × 1 level 不足以排除 ~180× 数据量差异作为主要 confound。\n**修复**: 扩展至 ≥2 models 或明确标注为 limitation。\n\n**W6. 遗漏相关工作** [R2-W5, R1 部分同意]\n需验证并按相关性补充：CodeScaler (arXiv 2602.17684)、GenPRM (AAAI 2026)、ExecVerify (arXiv 2603.11226)。Self-Execution Simulation 已在 references 中（R2 误报遗漏）。\n**修复**: WebSearch 验证真实性后加入。\n\n### Minor\n\n**M1.** Appendix M 补充 cluster-robust SEs 和 logistic regression 具体系数（R1-W5, R2 agrees）。\n**M2.** Clustered bootstrap 实施细节（resample unit, block size）未说明（R1）。\n**M3.** Figure 3 (Appendix) y-axis 不从 0 开始但未标注，不同于 Figure 2 的良好实践（R2-M2, R1 agrees）。\n**M4.** Abstract 第一句 \"relies on\" 过于绝对，建议改为 \"increasingly leverages\"（R2-M3, R1 agrees）。\n**M5.** Repo-level DEFF=114.3 → effective n≈86 未讨论对推断的限制（R1）。\n**M6.** 缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data 经典文献（R1）。\n**M7.** Figure 1 内部文字偏小（~60-65% 正文），打印时可能需放大（视觉审查）。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立达成共识的关键判断：\n- [AGREE] TOST ±2pp SESOI 需更强论证（最高权重共识 issue）\n- [AGREE] Repo-level 结论受 model identity dominance、limited seeds、variant-level power 限制\n- [AGREE] Function-level 等价性 novelty 有限\n- [AGREE] DeepSeek 2-seed 不足以支撑 \"model-dependent\" 泛化\n- [AGREE] Checkpoint selection 不一致是实质性 confound\n- [AGREE] 统计方法论超过领域平均水平\n- [AGREE] 匹配实验设计是核心优势\n\n## Reviewer Divergence\n\n| Issue | R1 | R2 | Director 裁定 |\n|-------|----|----|--------------|\n| CWM 评估非对称性严重性 | Must-Fix | Warning (func-level bias <1pp) | **Should-Fix** — function-level 偏差可忽略 |\n| \"Design space\" framing 严重性 | Should-Fix | Must-Fix | **Must-Fix** — 影响第一印象 |\n| CWM 术语 (R2-W3) | Rebut (沿用已发表术语) | Should-Fix | **Dismissed** — 作者使用 established terminology |\n| 缺 execution-based 对比 (R2-W4) | Rebut (超出论文 scope) | Should-Fix | **Dismissed** — 超出论文明确界定的研究问题 |\n| Failure mode taxonomy 偏向 CWM (R2-M4) | Rebut (CWM 天然更复杂) | Minor | **Dismissed** — R1 论证有说服力 |\n| Extended Limitations (R2-M5) | Rebut (ACL 标准做法) | Minor | **Dismissed** — 页数限制下的标准做法 |\n\n---\n\n## Questions for Authors\n\n1. CWM function-level exact match 中有多少比例的 \"错误\" 实际上是语义正确但格式不同？manual inspection 一个 seed 即可回答。[全票]\n2. ±2pp SESOI 是 pre-registered 还是 post-hoc？如果 post-hoc，TOST 框架的效力减弱。[全票]\n3. CWM repo-level runs 出现 NaN validation loss 的原因？formulation-inherent 还是 implementation issue？如果前者，是值得在正文讨论的 formulation weakness。[全票]\n4. Oracle complementarity (90.63%/95.83%) 为 single-seed 估计——跨 seed 是否稳定？[全票]\n5. 是否有 >8B 或 full fine-tuning 的 pilot data 暗示结论可能不同？[全票]\n\n---\n\n## Missing References\n\n**已确认需要**:\n- Wellek, S. (2010). \"Testing Statistical Hypotheses of Equivalence and Noninferiority.\" — TOST 方法论标准教材\n- Moulton, B. R. (1990). \"An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units.\" — clustered data 经典文献\n\n**需作者验证真实性后补充**:\n- CodeScaler (arXiv 2602.17684, Feb 2026) — execution-free reward model\n- GenPRM (AAAI 2026, arXiv 2504.00891) — generative PRM with code verification\n- ExecVerify (arXiv 2603.11226) — RL with verifiable stepwise rewards\n- Self-Execution Simulation — **已在 references 中引用**（R2 误报遗漏）\n\n---\n\n## External Review\n\n外部审稿：未请求（项目未启用 external_review）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 6 info）：\n\n**Warning**:\n- 前两页连续纯文本无 display item，Figure 1 直到第 3 页才出现。审稿人需读完 ~2 页密集文字才看到第一张图，延迟锚定效应。建议将 Figure 1 提前或增加 teaser figure。\n- 第 8 页 Related Work + Conclusion + Limitations 三节挤压，文字极度密集，给审稿人\"赶工\"印象。若 Related Work 能再压缩 3-5 行可改善呼吸感。\n\n**Info**:\n- Figure 1 内部文字 ~60-65% 正文字号，打印可能需放大\n- Figure 2 y-axis 截断已标注（良好实践）\n- Figure 3 (Appendix) 蓝/绿/青三色对色盲用户区分度有限，建议 Okabe-Ito 色板或 hatch pattern\n- Table 2/3 排版清晰，Table 4 可读性良好\n- Limitations 简洁覆盖 3 点，符合 EMNLP 要求\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 / 5 (Findings)**\n**置信度: 4 / 5**\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 2.5 | 2.5 | 2.5 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\n**定位：Findings of ACL，不足以进入 Main Conference。**\n\n这是一篇方法论严谨度超过该领域平均水平的实证研究。匹配实验设计、多层统计检验、透明的 threats to validity 在 NLP empirical papers 中属上乘。Failure mode taxonomy 和 error complementarity 有实用价值。\n\n但 novelty 和 excitement 不足以支撑 Main conference：\n1. \"Design space\" framing 与实际三 formulation 比较之间有张力——论文是 rigorous formulation comparison，不是 design space exploration\n2. Function-level 等价性在很大程度上可预期（短输出下分类与生成趋同）\n3. Repo-level 结论严重受限于 ≤8B LoRA regime、model identity dominance (>95% variance)、limited seeds、n=48 variant-level power\n4. 核心发现（generation 在复杂输出上格式崩溃）对 practitioner 而言不意外\n\n**Findings 接收合适**。实验框架和统计方法论对领域有参考价值，failure mode taxonomy 和 error complementarity 可供后续工作引用。若能扩展至更多 model families、增加 repo-level seeds、解决 SESOI domain justification，有潜力提升至 3.5 (Borderline Conference)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"formulation design space\" → \"systematic formulation comparison\" 更准确\n- Contribution 1 (function-level equivalence) 可融入三层结构叙述，不必独立列出\n- \"model-dependent\" (TRAJ parity) 应弱化为 \"observed to differ between tested families\"\n\n### §2 Method\n- §2.2 failure mode taxonomy：可增加 1-2 句 CLS/TRAJ 的失败模式特征描述\n- SESOI ±2pp 在 §3.4 应有 domain-grounded justification 并 reference Appendix J\n\n### §3 Experiments\n- Table 1 footnote \"not informational\" → \"insufficient seeds for statistical inference\" 更清晰\n- §3.4 应在正文引用 Appendix J 的 TOST sensitivity analysis\n- §3.5 应讨论 model identity dominance（当前仅在 Appendix M）\n- §3.7 CWM NaN val loss 值得作为 formulation-specific weakness 在正文讨论\n- Variant-level 分析（Table 4, §3.5）应明确标注为 exploratory/descriptive\n\n### §4 Related Work\n- 核实并按相关性补充 CodeScaler、GenPRM、ExecVerify\n- 加入 Wellek (2010) 和 Moulton (1990) 方法论引用\n\n### §5 Conclusion\n- \"CLS is recommended primarily for its throughput advantage\" 定位合理 ✓\n- ≤8B LoRA regime qualifier 已出现 ✓\n\n### Appendix\n- Appendix J (TOST sensitivity) 应在正文 §3.4 被引用\n- Appendix M 应补充 cluster-robust SEs 和 logistic regression 具体系数\n- Clustered bootstrap 实施细节应补充（resample unit, block size, iteration count）\n- DEFF=114.3 → effective n≈86 的含义应在正文或附录讨论\n",
    "project": "exec-sim-repair-verifier",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 740 · 2026-05-22T15:09:42.601896+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 741 · 2026-05-22T15:09:52.887707+00:00_

**Round 9 审稿完成。报告已投递至 Research Director。**

**最终评分：3.0 / 5 (Findings)**

核心判断摘要：

**优势**：匹配实验设计严谨（同数据/同LoRA/同seed）、统计方法论超过领域平均（TOST/ICC/clustered bootstrap/Holm-Bonferroni）、threats to validity 透明、failure mode taxonomy 有实用价值、error complementarity 发现有洞察力。

**Must-Fix（2 项）**：
- C1：TOST ±2pp SESOI 论证不充分——缺 domain-grounded justification、不对称 cost、Wellek 引用（两人独立标记，最高共识）
- C2："Design space" framing 过度——实际是三 formulation 比较，标题需调整

**Should-Fix（6 项）**：repo-level 因果性受 model identity dominance 削弱 + variant-level power 不足、CWM 评估非对称性需 robustness check、function-level 等价性需弱化为非独立 contribution、checkpoint selection 不一致（CWM NaN val loss）、TRAJ downsample 覆盖不足、遗漏引用需验证补充

**定位**：Findings of ACL。方法论严谨但 novelty 和 excitement 不足 Main conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 742 · 2026-05-22T15:09:53.914579+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 的逐条交叉回应。总结：

- **12 条意见中同意 10 条**，包括 TOST SESOI 论证不足（N2）、variant-level underpowered（W1）、DeepSeek 仅 2 seeds（W2）、checkpoint 不一致（W3）等
- **部分反驳 N1 的严重程度**：CWM exact matching 偏差在 function-level 的实际影响极小（unparseable rate 仅 1.39%），建议从 critical 降为 warning
- **纠正 R1 的一个遗漏**：R1 建议提供 SESOI sensitivity analysis，但论文 Appendix J Table 13 已包含 ±1pp 到 ±5pp 的完整 sensitivity 结果
- **维持我的 3.0 (Findings) 评分**，认为 R1 的 3.5 在其自身识别的方法论问题累积下偏高

---

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心判断：

- **高度一致**：SESOI 论证不足（两人独立标记）、repo-level robustness 受限、function-level novelty 有限
- **主要分歧**：CWM 术语（我认为是沿用 established terminology）、缺少 execution-based 对比（我认为超出 scope）、"design space" framing 的严重性（我认为是 Should-Fix 而非 Must-Fix）
- **R2 的一个事实错误**：Self-Execution Simulation (2604.03253) 已被论文引用，R2 遗漏了这一引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 743 · 2026-05-22T15:10:04.357111+00:00_

审稿报告已投递至 Research Director。

**Round 9 审稿总结：**

- **评分：3.0 / 5 (Findings)**，Soundness 3.5，Excitement 2.5，Confidence 4
- **2 个 Must-Fix**：TOST ±2pp SESOI 论证不充分（全票共识）；"design space" framing 与实际贡献不匹配
- **6 个 Should-Fix**：repo-level causal claims 弱化（model identity dominance）、CWM 评估非对称性、function-level novelty 弱化、checkpoint 不一致、TRAJ downsample 不足、遗漏相关工作
- **7 个 Minor**：cluster-robust SEs、bootstrap 细节、Figure 3 y-axis、Abstract 措辞、DEFF 讨论、方法论引用、Figure 1 字号
- Issue Tracker 已同步更新（含 R9 新发现 + 历史 issue 状态追踪）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 65

## Round 65

58 recorded events


### User

_source line 744 · 2026-05-22T15:37:30.053494+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR Long Paper
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-22T15:37:35.790639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-22T15:37:35.841785+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 747 · 2026-05-22T15:37:44.926305+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 748 · 2026-05-22T15:37:45.177534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-22T15:37:48.041997+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-22T15:37:48.092558+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 751 · 2026-05-22T15:37:55.319507+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 752 · 2026-05-22T15:37:56.223181+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- deepseek-cls-repo-re
…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 753 · 2026-05-22T15:37:56.374226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 754 · 2026-05-22T15:37:58.038013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 755 · 2026-05-22T15:37:58.038748+00:00_

1	\documentclass[11pt]{article}
2	
3	% ACL style (review mode for anonymous ARR submission)
4	\usepackage[review]{acl}
5	
6	% Fonts — Times Roman (required by ACL/ARR template)
7	\usepackage{times}
8	
9	% Math
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	
13	% Tables
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{tabularx}
17	
18	% Graphics
19	\usepackage{graphicx}
20	\graphicspath{{../../artifacts/}}
21	
22	% Lists
23	\usepackage{enumitem}
24	
25	% Custom commands
26	\newcommand{\cls}{\textsc{Cls}}
27	\newcommand{\cwm}{\textsc{Cwm}}
28	\newcommand{\traj}{\textsc{Traj}}
29	\newcommand{\fone}{F\textsubscript{1}}
30	\newcommand{\pp}{\,\text{pp}}
31	\newcommand{\tbd}{\textsc{tbd}}
32	
33	\title{A Systematic Comparison of Execution-Free Verification Formulations for Code Repair}
34	\author{Anonymous}
35	
36	\begin{document}
37	\maketitle
38	
39	\input{abstract}
40	
41	\input{introduction}
42	
43	\begin{figure*}[t]
44	\centering
45	\includegraphics[width=\textwidth]{figures/paper/fig1_reformulation.pdf}
46	\caption{Three verification formulations. \textbf{Left:} \cls{} predicts binary pass/fail per test (1 output token). \textbf{Center:} \cwm{} generates execution output, derives verdict by exact match ($O(L)$ tokens). \textbf{Right:} Trajectory-level scoring predicts patch-level resolved/unresolved (1 token, no per-test signal). Each formulation makes different tradeoffs between output complexity, diagnostic granularity, and inference cost.}
47	\label{fig:reformulation}
48	\end{figure*}
49	
50	\input{method}
51	
52	\input{experiments}
53	
54	\begin{figure}[t]
55	\centering
56	\includegraphics[width=\columnwidth]{figures/paper/fig2_scaling_gap.pdf}
57	\caption{Gap amplification from function to repo level. At function level, the \cls{}--\cwm{} gap is 1--3\pp{}; at repo level, it widens to 18--26\pp{} with \cwm{} falling below majority baseline. Note: $y$-axis begins at 55\% to emphasize formulation differences.}
58	\label{fig:scaling_gap}
59	\end{
…[truncated 173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 756 · 2026-05-22T15:38:02.963027+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found some relevant results about E
…[truncated 1373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 6588
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-22T15:38:10.647113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-22T15:38:13.561127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-22T15:38:14.315220+00:00_

-rw-r--r-- 1 ubuntu ubuntu 428096 May 22 15:35 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-22T15:38:14.466294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-22T15:38:14.516969+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-22T15:38:18.940653+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results from the ACL Rolling Review website, here are the key submission guidelines for 2026:

## Paper Length Requirements

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Short papers have a maximum of 4 content pages, long papers have a maximum of
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "WebSearch",
  "elapsed_ms": 8293
}
```

</details>

---


### Tool call

_source line 763 · 2026-05-22T15:38:30.397044+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-22T15:38:30.447729+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 765 · 2026-05-22T15:38:30.448166+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-22T15:38:31.100765+00:00_

{"result":"# 项目 exec-sim-repair-verifier 概况\n\n## 实验状态 (252 个)\n\n- **per-test-majority-voting**: DONE (negative) — \n- **block-corr-empirical**: DONE (success) — \n- **model-size-scaling-cwm8b**: DONE (success) — \n- **model-size-scaling-cls8b**: DONE (success) — \n- **llm-judge-32b-zeroshot**: DONE (success) — \n- **llm-judge-8b-zeroshot**: DONE (success) — \n- **traj-level-seed123**: DONE (success) — \n- **oracle-f2p-stratified**: DONE (success) — \n- **trace-then-judge**: DONE (failed) — \n- **mvp-b-train**: DONE (success) — \n- **multi-seed-core**: DONE (success) — \n- **cwm-baseline**: DONE (negative) — \n- **mvp-a-oracle-sim**: DONE (success) — \n- **p2p-regression-rate**: DONE (negative) — \n- **mvp-b-data-prep**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| deepseek-cwm-repo-s456-train-v2 | DeepSeek CWM repo-level s456-v2：第 3 seed，与 s42/s123-v2 对齐（train_unified.py + --train_file swebench_full/swebench_train.jsonl, 70748 行）。组成完整 3-seed coverage (42/123/456)。使用 epoch 3 final checkpoint 评估。 | — | — | — |\n\n## 待处理\n- deepseek-cls-repo-resume: Resume deepseek-cls-repo from checkpoint-2211 after SIGHUP crash at step 3747/6633（已分配 ? GPU:?，等待提交）\n- qwen_cwm_s456_resume2（准备中）\n- qwen_cwm_s456_resume（准备中）\n- deepseek-cwm-repo-s42-e3-seq4096-eval（准备中）\n- exp-downsample-cls-func-v3-eval-v2: Eval downsample CLS (Qwen3-4B, ~8K训练数据) on repo-level test set. 如果 accuracy 接近全量训练的 CLS (83.63%), 则证明 CLS formulation 优势不来自数据量（准备中）\n- exp-e-qwen3-3shot-baseline: Qwen3-8B 3-shot few-shot CLS baseline 在 repo-level 表现差于 fine-tuned models，与 DeepSeek 3-shot 一致，证明 fine-tuning 的必要性跨模型成立（准备中）\n- D131-cwm-s42-epoch3-seq2048（准备中）\n- D133-cwm-s42-e2-seq2048-home-resume（准备中）\n- deepseek-cwm-repo-s42-epoch2-eval: Eval CWM s42 epoch 2 checkpoint 解耦过拟合 vs seed 差异：如果 epoch 2 accuracy >> epoch 3 (56.7%)，则 CWM repo-level 在 epoch 3 过拟合（准备中）\n- deepseek-cls-repo-re
…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-22T15:38:43.702500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-22T15:38:44.607005+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 6
12	  last_seen_round: 9
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	  action_items:
27	    - round: 6
28	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
29	      assigned_to: "paper"
30	      status: resolved
31	    - round: 9
32	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
33	      assigned_to: "paper"
34	      status: open
35	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. 但 model identity dominance 和 variant-level power 仍未在正文充分讨论。"
36	  resolution_round: null
37	
38	- id: "R6-N2"
39	  summary: "Checkpoint selection 系统性偏向 CLS"
40	  category: method
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 6
44	  last_seen_round: 9
45	  mentions:
46	    - round: 6
47	      reviewers: [1, 2]
48	      note: "系统性偏差方向与 observed effect 一致。"
49	    - round: 7
50	      reviewers: [pre-review]
51	      note: "Reviewer 确认修复充分。"
52	    - round: 9
53	      reviewers: [1]
54	      note: "R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → fi
…[truncated 22252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-22T15:38:44.808251+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 770 · 2026-05-22T15:38:44.858957+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 771 · 2026-05-22T15:39:17.820489+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-22T15:39:31.343102+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 13522
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-22T15:39:31.493994+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- 标题: \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\"\n- Venue: EMNLP 2026 via ACL Rolling Review (ARR)\n- 类别: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计页数)\n- 模板: ACL template, `\\usepackage[review]{acl}`, double-blind\n- 匿名规则: 作者姓名/机构不可出现，补充材料也需匿名\n- 论文路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n1. **实验设计**：变量控制、对照组设置、消融实验充分性\n2. **统计方法**：TOST 等价检验设置（SESOI 合理性、power analysis）、bootstrap CI、interaction test、多重比较校正\n3. **Checkpoint 一致性**：各 formulation 之间的 checkpoint selection 是否公平\n4. **数据量控制**：CLS/CWM/TRAJ 训练数据量差异是否被充分讨论和控制\n5. **Multi-seed 覆盖**：repo-level claims 是否有足够的 seed 支撑\n6. **结果可复现性**：超参数报告是否完整，实验细节是否充分\n\n## 输出格式\n\n请按以下结构输出：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，按严重程度标注 [CRITICAL] / [WARNING] / [MINOR])\n- **Questions** (需要作者澄清的问题)\n- **Missing References** (遗漏的重要方法论引用)\n- **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5), Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性** 审查。\n\n## 论文信息\n- 标题: \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\"\n- Venue: EMNLP 2026 via ACL Rolling Review (ARR)\n- 类别: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计页数)\n- 模板: ACL template, `\\usepackage[review]{acl}`, double-blind\n- 匿名规则: 作者姓名/机构不可出现，补充材料也需匿名\n- 论文路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n1. **实验设计**：变量控制、对照组设置、消融实验充分性\n2. **统计方法**：TOST 等价检验设置（SESOI 合理性、power analysis）、bootstrap CI、interaction test、多重比较校正\n3. **Checkpoint 一致性**：各 formulation 之间的 checkpoint selection 是否公平\n4. **数据量控制**：CLS/CWM/TRAJ 训练数据量差异是否被充分讨论和控制\n5. **Multi-seed 覆盖**：repo-level claims 是否有足够的 seed 支撑\n6. **结果可复现性**：超参数报告是否完整，实验细节是否充分\n\n## 输出格式\n\n请按以下结构输出：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，按严重程度标注 [CRITICAL] / [WARNING] / [MINOR])\n- **Questions** (需要作者澄清的问题)\n- **Missing References** (遗漏的重要方法论引用)\n- **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5), Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-22T15:39:39.443062+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 7949
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-22T15:39:39.645625+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- 标题: \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\"\n- Venue: EMNLP 2026 via ACL Rolling Review (ARR)\n- 类别: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计页数)\n- 模板: ACL template, `\\usepackage[review]{acl}`, double-blind\n- 匿名规则: 作者姓名/机构不可出现，补充材料也需匿名\n- 论文路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n1. **贡献定位与新颖性**：论文的核心 contribution 是否清晰、是否 significant enough for EMNLP (Main or Findings)\n2. **Framing 准确性**：标题/Abstract/Introduction 中的 claims 是否与实验结果匹配，是否有 overclaim\n3. **Related Work 覆盖**：是否遗漏了关键相关工作（特别是 execution-free verification、code repair verification 方向的近期工作）\n4. **写作质量**：叙事逻辑、段落衔接、术语一致性、信息密度\n5. **格式合规**：正文是否 ≤8 页、ARR checklist 是否完整、匿名是否合规\n6. **Limitations 与 Ethics**：是否充分讨论了方法的局限性\n\n## 输出格式\n\n请按以下结构输出：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，按严重程度标注 [CRITICAL] / [WARNING] / [MINOR])\n- **Questions** (需要作者澄清的问题)\n- **Missing References** (遗漏的重要相关工作)\n- **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5), Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性与完整性** 审查。\n\n## 论文信息\n- 标题: \"A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\"\n- Venue: EMNLP 2026 via ACL Rolling Review (ARR)\n- 类别: Long Paper (正文 ≤8 页, 参考文献不限, Limitations/Ethics 不计页数)\n- 模板: ACL template, `\\usepackage[review]{acl}`, double-blind\n- 匿名规则: 作者姓名/机构不可出现，补充材料也需匿名\n- 论文路径: `projects/exec-sim-repair-verifier/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf`\n\n## 你的审查侧重\n\n1. **贡献定位与新颖性**：论文的核心 contribution 是否清晰、是否 significant enough for EMNLP (Main or Findings)\n2. **Framing 准确性**：标题/Abstract/Introduction 中的 claims 是否与实验结果匹配，是否有 overclaim\n3. **Related Work 覆盖**：是否遗漏了关键相关工作（特别是 execution-free verification、code repair verification 方向的近期工作）\n4. **写作质量**：叙事逻辑、段落衔接、术语一致性、信息密度\n5. **格式合规**：正文是否 ≤8 页、ARR checklist 是否完整、匿名是否合规\n6. **Limitations 与 Ethics**：是否充分讨论了方法的局限性\n\n## 输出格式\n\n请按以下结构输出：\n- **Summary** (2-3句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，按严重程度标注 [CRITICAL] / [WARNING] / [MINOR])\n- **Questions** (需要作者澄清的问题)\n- **Missing References** (遗漏的重要相关工作)\n- **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5), Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-22T15:39:41.109051+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1463
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-22T15:39:54.123145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-22T15:39:54.224041+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity differs between the two tested families. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-22T15:39:54.575685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-22T15:39:54.877197+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM-based automated program repair systems increasingly rely on test-time compute scaling: generating $K$ candidate patches and selecting the best via a verifier~\cite{snell2024scaling}. Full execution verification is reliable but expensive (\$1--3 per candidate at repository scale\footnote{Based on per-instance costs reported by \citet{yang2024sweagent} and \citet{xia2024agentless}.}), driving demand for execution-free alternatives. Three distinct formulations have emerged for this task: \textbf{generation-based simulation}~\cite{meta2025cwm,maimon2026selfexecution} predicts execution output strings per test; \textbf{trajectory-level scoring}~\cite{shum2025swerm} predicts a binary patch verdict without per-test decomposition; and \textbf{per-test classification}~\cite{ni2023lever,chen2023codet} predicts a pass/fail token per test. Each makes different tradeoffs between diagnostic granularity, output complexity, and inference cost.
5	
6	Despite active development along each axis, no prior work provides a systematic comparison holding model capacity, training data, and compute constant. Practitioners choosing a formulation for their verification pipeline must rely on results from different models, different datasets, and different evaluation protocols. Whether one formulation is uniformly preferable, or whether the choice depends on properties of the code being verified, remains an open empirical question. A related question is whether formulation choice matters at all relative to more basic decisions: at what complexity level does fine-tuning become necessary, and does formulation selection add value beyond what fine-tuning alone provides?
7	
8	We present the first systematic empirical comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels (function-level and repository-level), and multiple seeds. Our contribution is primarily methodological: a matched experimenta
…[truncated 2347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-22T15:39:54.877615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 782 · 2026-05-22T15:39:54.928153+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Let $p$ denote a candidate patch and $T = \{t_1, \ldots, t_n\}$ its test suite, where each $t_i$ has label $y_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ from execution. Tests decompose into \emph{fail-to-pass} ($T_{\text{f2p}}$) and \emph{pass-to-pass} ($T_{\text{p2p}}$) subsets; a patch is correct iff $\forall\, t_i{:}\ y_i = \text{\textsc{Pass}}$. We compare three formulations for predicting correctness without execution.
5	
6	\subsection{Verification Formulations}
7	\label{sec:formulations}
8	
9	Let $c_p$ denote the code context (unified diff) of patch $p$.
10	
11	\paragraph{\cls{} (per-test classification).} $f(c_p, t_i) \rightarrow \hat{y}_i \in \{\text{\textsc{Pass}}, \text{\textsc{Fail}}\}$ predicts a single binary token per test (cross-entropy loss). Patch verdict: $\hat{y}_p = \bigwedge_{i} [\hat{y}_i = \text{\textsc{Pass}}]$. Output cost: one token per test.
12	
13	\paragraph{\cwm{} (output generation).} $g(c_p, t_i) \rightarrow \hat{o}_i \in \Sigma^*$ generates the execution output string (language modeling loss). Verdict by exact match: $\hat{y}_i = \text{\textsc{Pass}}$ iff $\hat{o}_i = o_i^*$.\footnote{Exact string matching is conservative, consistent with \citet{meta2025cwm}. Semantic equivalences are not counted.} When the generated output is unparseable (i.e., does not conform to the expected structured format), the prediction defaults to the majority class verdict. Output cost: $\sum_i |\hat{o}_i|$ tokens.
14	
15	\paragraph{\traj{} (trajectory-level).} $h(c_p, T) \rightarrow \hat{y}_p \in \{\text{\textsc{Resolved}}, \text{\textsc{Unresolved}}\}$ predicts a single patch verdict from all tests and provides no per-test signal. \traj{} serves as a granularity control: \cls{}--\traj{} differences isolate the value of per-test decomposition independent of the classification formulation itself.
16	
17	\subsection{Formulation-Specific Failure Modes}
18	\label{sec:failure-modes}
19	
20	Each formulation
…[truncated 3353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 783 · 2026-05-22T15:40:02.375308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
  "offset": "34"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/method.tex",
    "offset": "34"
  }
}
```

</details>

---


### Tool result

_source line 784 · 2026-05-22T15:40:02.576868+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (34). The file has 34 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 785 · 2026-05-22T15:40:02.728172+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 786 · 2026-05-22T15:40:02.833969+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 21030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 787 · 2026-05-22T15:40:08.876970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 788 · 2026-05-22T15:40:09.280048+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Execution Simulation and Verification.}
5	Execution trace generation improves code reasoning~\cite{nye2021scratchpad}, with extensions to output prediction~\cite{meta2025cwm,maimon2026selfexecution,liu2024codemind,liu2023codeexecutor,lee2026solidcoder}, failure analysis~\cite{abdollahi2025demystifying}, and error detection~\cite{li2024redo}. CRUXEval~\citep{gu2024cruxeval} benchmarks code execution prediction at function level; RepoExec~\citep{nam2025repoexec} evaluates repo-level code generation with execution-based correctness checks. Our work extends execution prediction to repo-level repair verification. CodeScaler~\cite{zhu2026codescaler} trains execution-free reward models for both RL and test-time scaling. Verification formulations span trajectory-level reward~\cite{shum2025swerm}, process-level feedback~\cite{li2025codeprm,xu2025patchreasoner}, per-test classification~\cite{ni2023lever,chen2023codet}, learned metrics~\cite{zhuo2024icescore,dong2024codescore,zhou2023codebertscore}, and RL with execution-based rewards~\cite{wang2026verpo,tang2026execverify}. Aletheia~\cite{venkatkrishna2026aletheia} compares training recipes; we compare \emph{formulations}. Test-time scaling~\cite{snell2024scaling,li2025sstar,chen2025vgsearch} and self-consistency~\cite{wang2023selfconsistency} demonstrate verification value; none compare formulations at matched capacity.
6	
7	\paragraph{Process vs.\ Outcome Supervision.}
8	PRMs outperform ORMs for math reasoning~\cite{lightman2023letsverify,uesato2022solving}, with automated annotation~\cite{wang2024mathshepherd,luo2024omegaprm} and code-specific extensions~\cite{dreamprm2025code,ye2025prlcoder,zhang2026funprm,jiang2025coderlplus}. GenRM~\cite{hosseini2025genrm} and GenPRM~\cite{zhao2026genprm} show that generative verifiers outperform discriminative ones for math reasoning; our results reveal a domain difference---in code verification, the generative formula
…[truncated 1619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 789 · 2026-05-22T15:40:09.280650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 790 · 2026-05-22T15:40:09.331419+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented the first systematic comparison of three execution-free verification formulations (\cls{}, \cwm{}, \traj{}). At function level, \cls{} and \cwm{} are statistically equivalent (TOST $p{=}0.007$, 5 seeds); \traj{} parity differs between the two tested families. Per-test classification achieves 217$\times$ higher throughput while providing diagnostic signal. Complementary errors (oracle: 90.63\%/95.83\%; single-seed) motivate complexity-aware routing. At repository level under ${\leq}$8B LoRA, divergence reaches 18--26\pp{} ($z{=}-23.7$, 3 seeds per model), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}). Three failure modes (format collapse, decision collapse, aggregation penalty) are consistent across families. \cls{} is recommended primarily for its throughput advantage and diagnostic capability; the accuracy advantage over \traj{} is directional but underpowered ($n{=}48$, MDE${\approx}$25\pp{}; Appendix~\ref{app:power}).
5	
6	Three directions follow. First, oracle gains motivate complexity-aware routing; the failure mode taxonomy provides candidate routing features. Second, the generation bottleneck is semantic---four interventions fail (Appendix~\ref{app:extended_analysis}(g))---suggesting that closing the gap requires capacity scaling or execution trace pretraining~\cite{meta2025cwm}; testing at 32B+ scale would resolve the primary open question. Third, larger-scale evaluation of per-test diagnostics for downstream repair ($n{=}44$ in our pilot) would test whether \cls{}'s throughput advantage extends to repair pipelines.
7	
8	\section*{Limitations}
9	
10	Repo-level \cwm{} uses 3 seeds per model (Qwen3-8B, DeepSeek-6.7B); the gap (18--26\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds mean definitive causal attribution requires further replication. Our \cwm{} baseline uses 
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 791 · 2026-05-22T15:40:14.573475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 792 · 2026-05-22T15:40:15.326721+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Reference: https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	This paper follows the ARR Responsible NLP Research checklist.
7	
8	\subsection*{A. For Every Submission}
9	
10	\paragraph{A1. Did you describe the limitations of your work?}
11	Yes. Section~\ref{sec:conclusion} (Limitations paragraph) discusses: limited seed coverage for repo-level comparisons, synthetic-to-real transfer gap, lack of downstream re-repair validation, and val-test mutation distribution mismatch. Section~\ref{sec:repo} (Limitations paragraph) discusses val-best checkpoint selection variance and seed coverage.
12	
13	\paragraph{A2. Did you discuss any potential risks of your work?}
14	This work compares formulations for execution-free code verification on public benchmarks. The primary application is improving automated program repair pipelines. We identify no significant risks: the methods predict test outcomes rather than generating executable code, the datasets are derived from open-source repositories, and no personally identifiable information is involved. Misuse potential is limited because the verifiers require task-specific fine-tuning on labeled data and do not generalize to arbitrary code generation.
15	
16	\subsection*{B. Did You Use or Create Scientific Artifacts?}
17	
18	\paragraph{B1. Did you cite the creators of artifacts you used?}
19	Yes. All datasets (HumanEval~\cite{chen2021humaneval}, MBPP~\cite{austin2021mbpp}, SWE-bench Verified~\cite{chowdhury2024swebenchverified}), models (Qwen3~\cite{qwen2025qwen3}, DeepSeek-Coder~\cite{guo2024deepseekcoder}), and methods (LoRA~\cite{hu2022lora}, QLoRA~\cite{dettmers2024qlora}) are cited in Sections~\ref{sec:setup} and~\ref{sec:formulations}.
20	
21	\paragraph{B2. Did you discuss the license or terms for use and/or distribution of any artifacts?}
22	HumanEval is released under MIT license; MBPP under CC-BY-4.0; SWE-bench Verified 
…[truncated 4347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 793 · 2026-05-22T15:40:15.327109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 794 · 2026-05-22T15:40:15.377620+00:00_

1	\appendix
2	
3	\section{Oracle Accuracy-Utility Analysis}
4	\label{app:oracle}
5	
6	We stratify SWE-bench Verified instances by F2P test count $T$, comparing per-test vs.\ trajectory-level oracle resolve rates under i.i.d.\ and block-correlated error models (ICC $= 0.191$, from function-level analysis; \S\ref{sec:equivalence}).
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses function-level ICC $= 0.191$ (from function-level analysis, \S\ref{sec:equivalence}). P2P regression rate: 1.04\% mean, 0\% median.}
12	\label{tab:oracle}
13	\resizebox{\columnwidth}{!}{%
14	\setlength{\tabcolsep}{3pt}
15	\begin{tabular}{lcccc}
16	\toprule
17	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
18	\midrule
19	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
20	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
21	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
22	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
23	\midrule
24	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
25	\bottomrule
26	\end{tabular}}
27	\end{table}
28	
29	\begin{figure}[h]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig3_oracle_stratified.pdf}
32	\caption{Oracle per-test advantage by F2P test count $T$. Advantage is zero at $T{=}1$ (68.7\%) and concentrates at $T{=}2$ (19.1\%, contributing 55.3\% of total advantage). Note: $y$-axis does not start at zero.}
33	\label{fig:oracle_stratified}
34	\end{figure}
35	
36	Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_stratified} reveal a sharp concentration: at $T = 1$ (68.7\% of instances), per-test and trajectory-level are informationally equivalent. The advantage materializes at $T = 2$ (19.1\%), where block-correlated advantage reaches 31.69\pp{} (55.3\% of total). The overall block-correlated advantage is 10.93\pp{}, driven by 
…[truncated 6599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 795 · 2026-05-22T15:40:21.488260+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/appendix.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-22T15:40:21.840891+00:00_

100	Both models converge to exactly 45.83\% variant-level accuracy under 3-shot prompting, below majority baseline (54.17\%). Variant-level analysis reveals this is not a coincidence: both models correctly classify all 22 unresolved variants and zero resolved variants, equivalent to an always-predict-unresolved baseline with 100\% prediction overlap. Per-test accuracy diverges sharply (Qwen3-8B 71.61\% vs.\ DeepSeek 46.28\%), but this divergence is entirely superficial: Qwen3-8B predicts pass on nearly all tests, inflating per-test accuracy on a pass-heavy dataset (72.96\% pass rate) without genuine discriminative ability. Per-test metrics can thus severely misrepresent baseline capability; variant-level evaluation is necessary to detect complete degradation. Neither 0-shot nor few-shot prompting approaches fine-tuned performance (82--84\% per-test); fine-tuning is a necessary condition for repo-level verification.
101	
102	\section{Repo-Level Per-Mutation Breakdown}
103	\label{app:repo_mutation}
104	
105	Table~\ref{tab:mutation_breakdown} compares per-mutation accuracy at repo level. \cls{} produces 0\% unparseable outputs; all values are direct classification accuracy. \cwm{} overall accuracy includes default-pass assignment for unparseable outputs (see \S\ref{sec:repo}).
106	
107	\begin{table}[h]
108	\centering
109	\small
110	\caption{Per-mutation test accuracy (\%) at repo level (SWE-bench Verified, $n{=}9{,}784$). \cls{} 8B reports two seeds; $\Delta$ is mean 4B$\to$8B gain for \cls{}. \cwm{} 4B per-mutation overall accuracy omitted for non-gold mutations due to low parse rates (4.4--56.9\%, Table~\ref{tab:cwm_mutation_parse}); gold overall accuracy derived from parse rate 43.5\% and parseable accuracy 23.5\%.}
111	\label{tab:mutation_breakdown}
112	\resizebox{\columnwidth}{!}{%
113	\setlength{\tabcolsep}{3pt}
114	\begin{tabular}{lccccccc}
115	\toprule
116	\textbf{Mutation} & \textbf{$n$} & \textbf{CLS 4B} & \textbf{CLS 8B s42} & \textbf{CLS 8B s123} & \textbf{
…[truncated 44551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 797 · 2026-05-22T15:40:27.593811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool result

_source line 798 · 2026-05-22T15:40:28.260768+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf (418.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 666
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-22T15:40:36.570147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf",
  "pages": "11-18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf",
    "pages": "11-18"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-22T15:40:37.074771+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_8/submitted.pdf (418.1KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Assistant

_source line 801 · 2026-05-22T15:41:01.148570+00:00_

已完成论文全文阅读（18 页 PDF：8 页正文 + 参考文献 + Checklist + 附录）。正文恰好 8 页，符合 EMNLP 2026 页数限制。

**页面结构确认：**
- Pages 1-8: 正文（Abstract → Conclusion + Limitations）
- Pages 9-11: References
- Pages 12-13: ARR Responsible NLP Research Checklist  
- Pages 14-18: Appendix (A-P)

等待 Reviewer 1 和 Reviewer 2 的初审结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 802 · 2026-05-22T15:46:07.776115+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性审查

### Summary

本文是首个在匹配实验条件下系统比较三种 execution-free verification formulations（CLS/CWM/TRAJ）的研究。实验框架设计总体严谨（相同 base model、LoRA 配置、训练 schedule、多 seed），统计方法论显著优于 NLP 领域平均水平（TOST 等价检验、clustered bootstrap、ICC、mixed-effects regression）。但在 repo-level 比较中存在关键混杂变量（checkpoint 选择不公平），以及 TOST 检验的统计功效不足，使得两个核心 claim 的支撑力度打了折扣。

---

### Strengths

**S1. 匹配实验框架设计良好。** 使用相同 base model（Qwen3-4B/8B）、相同 LoRA rank（16）、相同训练 schedule 和 optimizer、5 seeds（function-level），是 NLP empirical comparison 论文中少见的严谨控制。DeepSeek-Coder-6.7B 作为 cross-model consistency check 进一步增强了可推广性（Section 3.1, Table 1）。

**S2. 统计方法论选择恰当且罕见。** TOST 等价检验（而非仅 NHST）、ICC-based clustered bootstrap（ICC=0.191, 114 clusters, 10K resamples）、Holm-Bonferroni 多重比较校正、mixed-effects LPM with heteroskedasticity-robust errors——这套统计工具链在 NLP 论文中极为少见，显示了作者的方法论素养（Section 3.1, 3.4, Appendix A, J, M）。

**S3. Failure mode taxonomy 有独立价值。** Section 3.5 + Appendix H 的三类 failure modes（formal collapse、decision collapse、aggregation penalty）有具体的定性例证和定量分析（Table 4），为从业者选择 formulation 提供了可操作的指导。

**S4. 附录极其详尽。** 15 个附录（A-P）覆盖了 ablation、convergence analysis、power analysis、prompt templates、per-mutation breakdown 等，使得审稿人可以验证几乎所有 claim 的支撑证据。

**S5. 自我批评诚实。** Limitations section 和 Appendix 中明确承认了 seed 覆盖不足、因果归因困难、checkpoint 混杂等问题，这在投稿论文中是正面信号。

---

### Weaknesses

**N1 [CRITICAL] Repo-level checkpoint selection 在 formulations 之间不公平**
- 具体位置：Section 3.1（"Repo-level models use val-selected checkpoints where available"）、Appendix O
- 问题：Appendix O 披露 **所有 CWM repo-level runs 因 NaN validation loss 而退化为 final-epoch checkpoint**，而 CLS 使用 val-selected checkpoint。Appendix N 的 convergence analysis 显示 CWM repo-level eval loss 持续上升（overfitting），final-epoch 并非最优。这意味着 CWM 在 repo level 系统性地使用了一个劣质 checkpoint，而 CLS 使用的是早停的优质 checkpoint。
- 为什么影响接收：论文最核心的 finding 是"formulation choice matters only at repo level"（Section 3.3），但如果 CWM 的 repo-level 劣势部分来自 checkpoint 选择偏差而非 formulation 本身的局限性，这个 claim 就被严重削弱了。论文虽在 Appendix O 承认此问题（"Val-based checkpoint selection biases toward per-test accuracy ... which amplifies the CWM penalty"），但未提供使用 early-stopped checkpoint 的 CWM repo-level 结果作为对照。
- 建议修改方向：(1) 用 Appendix O 提到的 epoch-3 checkpoint 重跑 CWM repo-level evaluation，或 (2) 在 main text 的 repo-level 比较中明确标注此混杂变量，并将 CWM repo-level 的劣势 claim 降级为"受 checkpoint 选择混杂影响的初步观察"。

**N2 [CRITICAL] TOST 等价检验统计功效不足，且 CLS-TRAJ 等价未通过多重比较校正**
- 具体位置：Appendix J（power ≈ 0.3 for medium effect）、Section 3.4（CLS-TRAJ adjusted p=0.075）、Table 15
- 问题：
  - (a) Appendix J 报告 n_eff ≈ 86，对 medium effect size 的 TOST 功效仅 ~0.3。功效 0.3 意味着有 70% 概率将真实的中等差异误判为等价。这使得 CLS-CWM 的 TOST 结论（虽然 p=0.007）也需审慎解读。
  - (b) CLS-TRAJ 的 TOST p=0.025 未通过 Holm-Bonferroni 校正（adjusted p=0.075）。论文在 Section 3.4 准确报告了这一点，但 abstract 的措辞"CLS and CWM are statistically equivalent ... TRAJ parity differs"可能被读者误解为 TRAJ 显著不等价，而实际上是等价检验功效不足、无法下结论。
- 为什么影响接收：Function-level equivalence 是论文的第一个核心 claim。如果等价检验本身功效不足，该 claim 的证据力从"强支撑"降级为"弱支撑/inconclusive"。
- 建议修改方向：(1) 在 main text 明确讨论 TOST 功效限制（目前仅在 Appendix J），(2) 考虑补充 Bayesian equivalence test（如 ROPE-based）以提供更有信息量的等价证据，(3) 将 function-level equivalence claim 的措辞从"are statistically equivalent"软化为"show no detectable difference within our ±2pp margin, though the test is underpowered"。

**W1 [WARNING] 训练数据量在 formulations 之间差异巨大且未充分控制**
- 具体位置：Section 3.1, Section 6（Appendix B downsampling ablation）, Appendix E
- 问题：CLS ~70K samples，CWM ~70K（但有 truncation），TRAJ 仅 386 variant-level instances——相差 ~180×。论文进行了 downsampling ablation（Section 6）显示匹配 volume 的 CLS 仍比 TRAJ 高 7.82pp，但这并不能证明 TRAJ 的 formulation 本身（而非数据量/信号粒度）是劣势来源。TRAJ 的训练信号粒度（variant-level vs. per-test）与 CLS/CWM 有本质区别，使得这不仅是 volume 问题，更是 signal structure 问题。
- 建议：(1) 明确将 TRAJ 的数据量/信号粒度限制框架为 formulation 的固有属性（"TRAJ by design has coarser training signal"），而非可控的实验变量；(2) 或者尝试通过 per-test pseudo-label expansion 来增加 TRAJ 训练数据。

**W2 [WARNING] Repo-level seed 覆盖不足以支撑 definitive claims**
- 具体位置：Table 3（3 seeds, DeepSeek CLS 仅 2 seeds）
- 问题：Repo-level 结果仅用 2-3 seeds，而 repo-level variance 远大于 function-level。CLS-CWM gap 在不同配置间从 18pp 到 26pp 变化。论文 main text 中的 repo-level claims（如"formulation choice matters only at repo level"）读起来像 definitive 结论，但支撑数据仅 2-3 个独立观测。
- 建议：在 main text（而非仅 Limitations）中显式标注 repo-level 分析的 seed 数和相应的不确定性。

**W3 [WARNING] CWM exact string matching verdict 系统性地惩罚 generation formulation**
- 具体位置：Section 2.1（footnote 2）, Appendix H, Appendix I
- 问题：CWM 使用 exact string matching 判定 verdict，formal collapse rates 达 53-74%（Table 4, unparseable outputs）。虽然此标准沿袭 FAIR CodeGen team 的协议，但它系统性地将"语义正确但格式不同"的输出判为失败。Appendix I 讨论了 parseable accuracy，但 main text 的所有比较表均使用 strict exact match。这使得 CLS vs. CWM 的比较实际上混淆了 formulation difference 和 verdict criterion strictness。
- 建议：在 Table 1/3 旁增加 CWM parseable-only accuracy（已在 Appendix I 计算）作为 sensitivity analysis，或讨论 fuzzy/semantic matching 下差距如何变化。

**W4 [WARNING] SESOI (±2pp) 的 a priori 属性值得商榷**
- 具体位置：Section 3.4, Appendix J
- 问题：论文声称 SESOI"set a priori based on deployment relevance"，但 ±2pp 的具体值实际上依赖于本研究的 accuracy range（85-89%）和 test set size（114 problems）。真正 a priori 的 SESOI 应在观察结果前确定。这更接近于 post-hoc rationalization。
- 建议：透明地描述 SESOI 的设定过程——是在观察任何结果前就固定为 ±2pp，还是在初步结果出来后确定的？Appendix J 的 TOST sensitivity analysis（Table 13）部分缓解了此问题，但 main text 应明确说明。

**M1 [MINOR] Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析**
- 具体位置：Appendix M
- 问题：LPM 在二元因变量下有已知的异方差和越界预测问题。论文提到 logistic regression 确认了结果，但仅展示了 LPM 的完整系数。
- 建议：在 Appendix M 中并列展示 logistic regression 的 odds ratios 或 marginal effects。

**M2 [MINOR] Figure 2 的 y-axis 不从零开始**
- 具体位置：Figure 2（p.7）
- 问题：Figure 2 bar chart 的 y-axis 起点约为 55%，视觉上夸大了 CLS-CWM gap。Note 中标注了"y-axis begins at 55%"，但对快速浏览的读者可能造成误导。

---

### Questions for Authors

**Q1.** 能否提供 CWM repo-level 使用 early-stopped checkpoint（如 Appendix O 提到的 epoch-3）的评估结果？这将直接解答 N1 的混杂问题。

**Q2.** 鉴于 TOST 功效仅 ~0.3（Appendix J），是否考虑过使用 Bayesian equivalence test（如 ROPE-based posterior estimation）来提供更有信息量的等价证据？

**Q3.** Abstract 中"TRAJ parity differs between the two tested families"——是否可以更精确地说明 TRAJ 不等价的方向（TRAJ 更差还是 inconclusive）？目前的措辞可能被误读为 TRAJ 显著不等价。

**Q4.** Section 3.6 的 cross-seed oracle（90.63%）是基于 any-correct 还是 majority voting？如果是 any-correct，请标注这一点。

**Q5.** CWM 的 formal collapse（53-74% unparseable）中，有多大比例是"语义正确但格式不匹配"vs."完全错误的生成"？这将量化 exact-match criterion 对 CWM 的系统性惩罚程度。

**Q6.** Table 11 显示 CWM 和 CLS 使用不同的 data processing scripts（train_unified.py vs. train_repo_cwm.py），前者 drop samples、后者 truncate。这个差异是否被纳入了消融分析？

---

### Missing References

- **Cohen (1988)** *Statistical Power Analysis for the Behavioral Sciences*: 论文在 Appendix J 讨论 power analysis 时使用了 "medium effect size" 但未引用 Cohen 的经典效应量分类标准。
- **Kruschke (2013/2018)** Bayesian estimation / ROPE methods: 作为 TOST 的替代方案，考虑到 TOST 功效不足，Bayesian equivalence 方法值得讨论和引用。

---

### Scores

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | Main claims（function-level equivalence, repo-level divergence）有证据支撑但不完整：checkpoint 混杂（N1）削弱 repo-level claims，TOST 功效不足（N2）削弱 equivalence claims。Failure mode taxonomy 支撑较好。 |
| **Excitement** | 3/5 | 实用价值明确（首个 matched comparison），failure mode taxonomy 有独立贡献，但本质是 empirical comparison 而非方法创新，findings 符合直觉（复杂 formulation 在复杂任务上退化）。 |
| **Reproducibility** | 4/5 | 超参数报告极为详尽（Table 11, Appendix E/F），代码仓库已提供，compute budget 明确。唯一缺口是 CWM repo-level 的 checkpoint 选择细节。 |
| **Overall** | 3.5 | Borderline Conference。实验框架设计和统计方法论的深度在 NLP empirical papers 中属上乘，failure mode taxonomy 有实用价值。但两个 CRITICAL 问题（checkpoint 公平性 N1、TOST 功效 N2）使得两个核心 claim 的支撑力度不够 Conference 水准。如果作者能解答 Q1（提供 early-stopped CWM 结果）和 Q2（补充 Bayesian equivalence test），评分可上调至 4。 |
| **Confidence** | 4/5 | 仔细阅读了全部 23 页含附录，熟悉所涉统计方法（TOST, ICC, clustered bootstrap, mixed-effects models）。 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 803 · 2026-05-22T15:46:34.373945+00:00_

Reviewer 1 审稿完成。评分 3.5/5（Borderline Conference），2 个 CRITICAL + 4 个 WARNING。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 67

## Round 67

2 recorded events


### User

_source line 804 · 2026-05-22T15:46:36.889717+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心发现：

- **2 个 CRITICAL 问题**：(1) CWM repo-level 全部使用 final-epoch checkpoint（因 NaN val loss），而 CLS 使用 val-selected checkpoint，系统性地不公平；(2) TOST 统计功效仅 ~0.3，且 CLS-TRAJ 等价未通过 Holm-Bonferroni 校正。
- **4 个 WARNING 问题**：训练数据量 180× 差异未充分控制、repo-level 仅 2-3 seeds、CWM exact-match verdict 过严、SESOI 的 a priori 属性可疑。
- **Overall 3.5**（Borderline Conference）：实验框架和统计方法论深度在 NLP 论文中属上乘，但两个 CRITICAL 混杂变量使核心 claims 支撑力度不够。若作者补充 early-stopped CWM repo 结果 + Bayesian equivalence test，可上调至 4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 805 · 2026-05-22T15:46:53.590326+00:00_

Reviewer 1 审稿结果已收到。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 68

## Round 68

6 recorded events


### User

_source line 806 · 2026-05-22T15:47:28.668996+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：新颖性与完整性

## 论文信息
- **标题**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
- **Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文对三种 execution-free 代码修复验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级 patch 评分）进行了首次系统性匹配比较，使用相同数据、相同计算资源和相同模型。核心发现是一个"三层结构"：(1) fine-tuning 是必要的（35-36pp 提升）；(2) 在 function level 三种公式统计等价（TOST p=0.007）；(3) 在 repo level CWM 显著退化（低于 CLS 18-26pp）。论文还提供了一个 failure mode 分类体系来解释 CWM 的退化机制。

---

## Strengths

**S1. 实验设计严谨且方法论贡献突出。** 使用 TOST 等价性检验（而非仅看显著性差异）来评估公式间是否"等价"，这在 NLP 论文中非常少见且恰当。ICC 用于衡量 within-problem 相关性也很有见地。匹配实验设计（相同 LoRA rank、相同训练数据构造、相同 seed）使得结论有高可信度（Section 3.1, 3.4）。

**S2. 实用性强的结论。** "function level 不需要纠结公式选择，repo level 优先 CLS" 这一结论对实践者有直接指导价值。CLS 的吞吐量优势（1 token/test vs. CWM ~477 tokens）和诊断能力也被明确量化。

**S3. Failure mode 分类体系提供了超越表面准确率比较的机制性洞察。** 将 CWM 失败分为 formal collapse（格式崩溃）、decision collapse（决策崩溃）和 aggregation penalty（聚合惩罚）（Section 3.5, Table 4, Appendix H），为理解*为什么* CWM 在 repo level 退化提供了可操作的分析框架。

**S4. Error complementarity 发现有价值。** CLS 和 CWM 的 oracle combination 达到 90.63%（vs. 单最优 84.16%），证明两种公式犯互补类型的错误（Section 3.7），为 ensemble 或 routing 策略提供了实证基础。

**S5. 附录极其详尽。** 14 页附录覆盖 LoRA rank ablation、majority voting、sequence length、training data control、few-shot prompting、convergence analysis、qualitative error analysis、mixed-effects regression 等。Appendix O "Threats to Validity" 系统性地讨论了潜在问题。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [CRITICAL] 核心贡献为比较已有公式，novelty 有限**
- 具体位置：Section 1 (contribution list), Section 5 (Conclusion)
- 问题：三种公式（CLS、CWM、TRAJ）均为已有方法，论文的贡献完全是实验比较框架本身。核心发现"更复杂的任务→公式选择更重要"虽然数据支撑充分，但从直觉上可以预期——repo-level 输出更长、更结构化，生成式公式自然面临更大挑战。论文描述了*what happens*但没有提供深层*why*的理论理解——为什么恰好在 repo level 而非某个中间复杂度出现分歧？是否存在复杂度阈值？"三层结构"是描述性的而非解释性的。
- 为什么影响接收：对于 EMNLP main conference (Overall ≥ 4)，需要 excitement 层面的贡献（新方法、新理论框架、或令人意外的发现）。一个确认"直觉上可预期结论"的比较研究，即使执行极为严谨，excitement 也受限。
- 建议修改方向：(a) 尝试提出一个基于 error complementarity 的轻量 routing/ensemble 方法并实验验证，将贡献从"比较"提升为"比较+方案"；(b) 或提供关于 complexity threshold 的理论分析——在什么条件下 CWM 开始退化（而非仅报告"repo level 退化了"）。

**N2 [CRITICAL] ≤8B LoRA 规模限制严重威胁结论的泛化性**
- 具体位置：Section 3.1 (models), Limitations (p.9)
- 问题：所有实验使用 ≤8B 参数模型 + LoRA fine-tuning。论文自己提到原始 CWM 是 32B 全参数 mid-training，性能远优于其 ≤8B LoRA 复现版。CWM 的 repo-level 退化很可能根本上是容量问题（生成 ~477 tokens 的执行输出需要更强的模型），而非公式本身的固有缺陷。如果 32B CWM 在 repo level 不退化，则"公式选择在 repo level 至关重要"这一核心结论不成立。
- 论文在 Limitations 中简短提及此问题，但 abstract 和 conclusion 中的主张并未附加此关键限定（"在 ≤8B LoRA 条件下"）。
- 为什么影响接收：核心结论的外部效度受到质疑。Reviewer 和 AC 会问：这些发现是关于 verification formulation 的，还是仅关于 small-model LoRA fine-tuning 的？
- 建议修改方向：(a) 即使仅增加一个 14B 或 32B 配置的单点验证也会极大增强说服力；(b) 如果计算资源不允许，应在 abstract 和 conclusion 中明确限定"our findings apply to the ≤8B LoRA regime"并讨论在更大规模下结论可能如何变化。

### Should-Fix 问题（影响评分但不一票否决）

**W1 [WARNING] 单一语言（Python-only）评估，但 Limitations 未提及**
- 具体位置：Section 3.1 (Datasets), Limitations (p.9)
- 问题：Function-level 使用 HumanEval+MBPP（Python），repo-level 使用 SWE-bench（Python）。验证公式在静态类型语言（Java/C++）或不同测试范式下的行为可能不同——例如 CLS 的 per-test 预测在 Java 的更细粒度测试中可能表现不同；CWM 的 execution trace 生成对不同语言的执行模型可能有不同难度。
- Limitations 段没有讨论语言单一性这一问题。
- 建议：在 Limitations 中增加一句关于语言覆盖的讨论。

**W2 [WARNING] 与 reward model 文献的联系不够充分**
- 具体位置：Section 4 (Related Work, "Process vs. Outcome Supervision")
- 问题：CLS/CWM/TRAJ 与 ORM/PRM 之间存在自然映射（CLS ≈ per-step ORM，CWM ≈ generative verifier / PRM-like，TRAJ ≈ sequence-level ORM），但论文仅简短提及 CodePRM 和 FuncPRM，没有深入讨论这一映射关系。特别是 **CodeRM** (Diao et al., ACL 2025 main, "Dynamic Scaling of Unit Tests for Code Reward Modeling") 研究了 test-level 粒度对 reward signal 质量的影响，与 CLS 的 per-test prediction 设计直接相关，但未被引用。
- 建议：增加半段讨论，将三种公式显式映射到 ORM/PRM 框架，并引用 CodeRM。

**W3 [WARNING] "complexity-aware formulation routing" 仅为未验证假设**
- 具体位置：Abstract (最后一句), Section 3.7, Section 5
- 问题：Abstract 声称 "Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection"，但论文没有实现或评估任何 routing 机制。从 oracle combination (90.63%) 到可实际部署的 routing 策略之间存在显著 gap，论文没有验证简单的 routing heuristic（如基于输入长度或预测复杂度）是否有效。
- 建议：要么降低 abstract 中的措辞（从 "motivate routing" 改为 "suggest the potential of routing"），要么增加一个简单的 routing 实验（即使是 heuristic-based）。

**W4 [WARNING] TRAJ 公式探索不充分**
- 具体位置：Section 2.1, Section 3.3
- 问题：TRAJ 将所有 per-test 信息压缩为一个 binary verdict，丢失了诊断粒度。论文讨论了这一限制（Section 2.2 "trajectory-level failure modes"）但没有探索中间方案——例如 per-test TRAJ（对每个测试生成轨迹级预测然后聚合）。这意味着 TRAJ 的劣势可能部分是设计选择的结果，而非轨迹级方法的固有限制。
- 建议：至少讨论这种中间变体的可能性，或解释为什么没有测试它。

### 小问题（不影响接收）

**M1 [MINOR]** Abstract 中 "formulation choice is governed by code complexity" (p.1 最后一句) 用词过强——数据展示的是相关性（function vs. repo level 的差异），而非 "governed by" 所暗示的因果机制。

**M2 [MINOR]** Section 3.3 提到 "few-shot prompting (3-shot ICL) collapses to an always-predict-unresolved baseline" 但这一重要发现仅在正文中一句带过，主要讨论在 Appendix B。考虑到这说明了 fine-tuning 的必要性，值得在正文多给半段篇幅。

**M3 [MINOR]** Appendix 从 A 到 P 共 16 个，达 14 页。虽然内容详实，但组织上可以考虑合并相关的 ablation studies 以降低读者的导航成本。

---

## Questions（需要作者澄清）

**Q1.** CWM 在 repo level 的退化是否主要是 model capacity 问题？如果将原始 32B CWM（FAIR CodeGen team）在 SWE-bench Verified 上评估 per-test accuracy，是否能恢复与 CLS 的等价性？

**Q2.** Oracle combination 达到 90.63%——是否尝试过不依赖 oracle 的简单 routing 启发式（例如基于输入 token 数、测试数量、或 CLS 预测置信度）？

**Q3.** TRAJ 为何设计为 single binary output 而非 per-test trajectory prediction + aggregation？是否有计算或数据构造方面的限制？

**Q4.** 论文聚焦 code repair verification——结论是否可推广到 code generation（无 buggy source 对比）的场景？CLS 的 per-test 预测在没有 original code 作为输入时如何 formulate？

**Q5.** CLS（1 token/test）vs. CWM（~477 tokens average）的实际推理时间差距是多少？在 repo level 的 SWE-bench 上，端到端 wall-clock time 差异是否显著？

---

## Missing References

1. **CodeRM** — Diao et al., "Dynamic Scaling of Unit Tests for Code Reward Modeling", ACL 2025 Main Conference. 研究 test-level 粒度对 code reward signal 质量的影响，直接相关于 CLS 的 per-test prediction 设计。

2. 建议加强与 ORM/PRM 文献的显式映射讨论（已有引用 CodePRM、FuncPRM，但缺少框架层面的对应分析）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论严谨（TOST、ICC、matched design），但 ≤8B LoRA 规模和 Python-only 评估限制了结论的泛化性。CWM 退化可能是容量问题而非公式固有缺陷，论文未能排除此混淆变量。 |
| **Excitement** | 2.5/5 | 回答了一个实用问题（哪种验证公式更好），但核心发现（"复杂任务→公式选择更重要"）可从直觉预期。无新方法提出，failure mode 分类体系有价值但属增量贡献。 |
| **Reproducibility** | 4/5 | 训练配置、超参数、数据构造均详细记录（Appendix E），代码/数据承诺在录用后释放。Responsible NLP Checklist 完整。 |
| **Overall** | 3/5 (Findings) | 执行严谨的比较研究，对实践者有价值。Failure mode 分析和 error complementarity 增加了深度。但 novelty 受限于"比较已有方法"，excitement 不足以达到 main conference (≥4)。Findings 级别合适。 |
| **Confidence** | 4/5 | 熟悉 code generation verification、reward modeling、program repair 文献，对统计方法论有足够判断力。 |

---

## 总体评分

**Overall**: 3/5 — Findings

**一句话总结**: 一项方法论严谨但 novelty 受限的系统比较研究——实验设计值得学习，failure mode 分析有洞察力，但核心发现在直觉上可预期，且 ≤8B LoRA 规模限制严重威胁结论对更大模型的泛化性。

---

## 主要优势（总结）
- 匹配实验设计 + TOST 等价性检验，方法论贡献突出
- 可直接指导实践的结论（CLS 优先推荐 at repo level）
- Failure mode 分类体系提供机制性理解
- Error complementarity 发现为 ensemble/routing 提供实证基础
- 极其详尽的附录（16 个 appendix，14 页）

## 格式合规检查
- ✅ 正文 8 页（Section 1-5，pp.1-8）
- ✅ Limitations 在正文之后（p.9），不计入页数限制
- ✅ Anonymous ACL submission header，无作者姓名/机构
- ✅ Responsible NLP Research Checklist 完整（p.12）
- ✅ References 格式符合 ACL 模板


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 807 · 2026-05-22T15:48:21.302012+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1（方法严谨性审查）的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Summary\n本文是首个在匹配实验条件下系统比较三种 execution-free verification formulations（CLS/CWM/TRAJ）的研究。实验框架设计总体严谨，统计方法论显著优于 NLP 领域平均水平。但在 repo-level 比较中存在关键混杂变量（checkpoint 选择不公平），以及 TOST 检验的统计功效不足，使得两个核心 claim 的支撑力度打了折扣。\n\n### Weaknesses\n\n**N1 [CRITICAL] Repo-level checkpoint selection 在 formulations 之间不公平**\n所有 CWM repo-level runs 因 NaN validation loss 而退化为 final-epoch checkpoint，而 CLS 使用 val-selected checkpoint。CWM repo-level eval loss 持续上升（overfitting），final-epoch 并非最优。CWM 系统性地使用劣质 checkpoint，而 CLS 使用早停的优质 checkpoint。论文核心 finding \"formulation choice matters only at repo level\" 被严重削弱。\n\n**N2 [CRITICAL] TOST 等价检验统计功效不足**\nn_eff ≈ 86，对 medium effect size 的 TOST 功效仅 ~0.3。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。Abstract \"TRAJ parity differs\" 可能被误读为 TRAJ 显著不等价，而实际上是等价检验功效不足。\n\n**W1 [WARNING] 训练数据量差异巨大（CLS ~70K vs TRAJ ~386, ~180×）且未充分控制**\nDownsampling ablation 控制了 volume 但未控制 signal granularity（per-test vs variant-level）。\n\n**W2 [WARNING] Repo-level seed 覆盖不足（2-3 seeds）**\nRepo-level variance 远大于 function-level，main text 中 claims 读起来像 definitive 结论但仅 2-3 独立观测。\n\n**W3 [WARNING] CWM exact string matching verdict 系统性惩罚 generation formulation**\nFormal collapse rates 达 53-74%。使得 CLS vs CWM 混淆了 formulation difference 和 verdict criterion strictness。\n\n**W4 [WARNING] SESOI (±2pp) 的 a priori 属性值得商榷**\n±2pp 实际依赖于研究的 accuracy range 和 test set size，更接近 post-hoc rationalization。\n\n**M1 [MINOR]** Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析。\n**M2 [MINOR]** Figure 2 y-axis 不从零开始。\n\n### Questions\nQ1. 能否提供 CWM repo-level 使用 early-stopped checkpoint 的评估结果？\nQ2. 是否考虑 Bayesian equivalence test（ROPE-based）？\nQ3. \"TRAJ parity differs\" 是否可更精确？\nQ4. Cross-seed oracle（90.63%）是 any-correct 还是 majority voting？\nQ5. CWM formal collapse 中\"语义正确但格式不匹配\"vs\"完全错误\"的比例？\nQ6. CWM/CLS 使用不同 data processing scripts，是否纳入消融分析？\n\n### Missing References\nCohen (1988), Kruschke (2013/2018) Bayesian ROPE methods\n\n### Scores\nSoundness 3/5, Excitement 3/5, Reproducibility 4/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1（方法严谨性审查）的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的完整审稿意见\n\n### Summary\n本文是首个在匹配实验条件下系统比较三种 execution-free verification formulations（CLS/CWM/TRAJ）的研究。实验框架设计总体严谨，统计方法论显著优于 NLP 领域平均水平。但在 repo-level 比较中存在关键混杂变量（checkpoint 选择不公平），以及 TOST 检验的统计功效不足，使得两个核心 claim 的支撑力度打了折扣。\n\n### Weaknesses\n\n**N1 [CRITICAL] Repo-level checkpoint selection 在 formulations 之间不公平**\n所有 CWM repo-level runs 因 NaN validation loss 而退化为 final-epoch checkpoint，而 CLS 使用 val-selected checkpoint。CWM repo-level eval loss 持续上升（overfitting），final-epoch 并非最优。CWM 系统性地使用劣质 checkpoint，而 CLS 使用早停的优质 checkpoint。论文核心 finding \"formulation choice matters only at repo level\" 被严重削弱。\n\n**N2 [CRITICAL] TOST 等价检验统计功效不足**\nn_eff ≈ 86，对 medium effect size 的 TOST 功效仅 ~0.3。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。Abstract \"TRAJ parity differs\" 可能被误读为 TRAJ 显著不等价，而实际上是等价检验功效不足。\n\n**W1 [WARNING] 训练数据量差异巨大（CLS ~70K vs TRAJ ~386, ~180×）且未充分控制**\nDownsampling ablation 控制了 volume 但未控制 signal granularity（per-test vs variant-level）。\n\n**W2 [WARNING] Repo-level seed 覆盖不足（2-3 seeds）**\nRepo-level variance 远大于 function-level，main text 中 claims 读起来像 definitive 结论但仅 2-3 独立观测。\n\n**W3 [WARNING] CWM exact string matching verdict 系统性惩罚 generation formulation**\nFormal collapse rates 达 53-74%。使得 CLS vs CWM 混淆了 formulation difference 和 verdict criterion strictness。\n\n**W4 [WARNING] SESOI (±2pp) 的 a priori 属性值得商榷**\n±2pp 实际依赖于研究的 accuracy range 和 test set size，更接近 post-hoc rationalization。\n\n**M1 [MINOR]** Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析。\n**M2 [MINOR]** Figure 2 y-axis 不从零开始。\n\n### Questions\nQ1. 能否提供 CWM repo-level 使用 early-stopped checkpoint 的评估结果？\nQ2. 是否考虑 Bayesian equivalence test（ROPE-based）？\nQ3. \"TRAJ parity differs\" 是否可更精确？\nQ4. Cross-seed oracle（90.63%）是 any-correct 还是 majority voting？\nQ5. CWM formal collapse 中\"语义正确但格式不匹配\"vs\"完全错误\"的比例？\nQ6. CWM/CLS 使用不同 data processing scripts，是否纳入消融分析？\n\n### Missing References\nCohen (1988), Kruschke (2013/2018) Bayesian ROPE methods\n\n### Scores\nSoundness 3/5, Excitement 3/5, Reproducibility 4/5, Overall 3.5 (Borderline Conference), Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 808 · 2026-05-22T15:48:44.060660+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22758
}
```

</details>

---


### Tool call

_source line 809 · 2026-05-22T15:48:44.261773+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2（新颖性与完整性审查）的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Summary\n本文对三种 execution-free 代码修复验证公式进行了首次系统性匹配比较。核心发现是\"三层结构\"。论文还提供了一个 failure mode 分类体系。\n\n### Weaknesses\n\n**N1 [CRITICAL] 核心贡献为比较已有公式，novelty 有限**\n三种公式均为已有方法，论文贡献完全是实验比较框架本身。核心发现\"更复杂的任务→公式选择更重要\"虽然数据支撑充分，但从直觉上可以预期。论文描述了 what happens 但没有提供深层 why 的理论理解。对 EMNLP main conference 需要 excitement 层面的贡献。建议提出轻量 routing/ensemble 方法或 complexity threshold 理论分析。\n\n**N2 [CRITICAL] ≤8B LoRA 规模限制严重威胁结论的泛化性**\nCWM 的 repo-level 退化很可能根本上是容量问题，而非公式本身固有缺陷。如果 32B CWM 在 repo level 不退化，则\"公式选择在 repo level 至关重要\"这一核心结论不成立。Abstract 和 conclusion 中主张未附加此关键限定。\n\n**W1 [WARNING] 单一语言（Python-only）评估，但 Limitations 未提及**\n验证公式在 Java/C++ 或不同测试范式下的行为可能不同。Limitations 段没有讨论语言单一性。\n\n**W2 [WARNING] 与 reward model 文献联系不够充分**\nCLS/CWM/TRAJ 与 ORM/PRM 之间存在自然映射，但论文未深入讨论。遗漏 CodeRM (Diao et al., ACL 2025)。\n\n**W3 [WARNING] \"complexity-aware formulation routing\" 仅为未验证假设**\nAbstract 声称 motivate routing 但没有实现或评估任何 routing 机制。\n\n**W4 [WARNING] TRAJ 公式探索不充分**\n没有探索中间方案（per-test TRAJ + aggregation）。TRAJ 劣势可能部分是设计选择的结果。\n\n**M1 [MINOR]** \"formulation choice is governed by code complexity\" 用词过强。\n**M2 [MINOR]** 3-shot ICL collapse 发现仅在正文一句带过。\n**M3 [MINOR]** 16 个 Appendix 组织可改善。\n\n### Questions\nQ1. CWM repo-level 退化是否主要是 model capacity 问题？32B CWM 是否能恢复等价性？\nQ2. 是否尝试过不依赖 oracle 的简单 routing 启发式？\nQ3. TRAJ 为何设计为 single binary output 而非 per-test trajectory + aggregation？\nQ4. 结论是否可推广到 code generation（无 buggy source 对比）场景？\nQ5. CLS vs CWM 实际推理时间差距是多少？端到端 wall-clock time？\n\n### Missing References\nCodeRM (Diao et al., ACL 2025), ORM/PRM 框架映射讨论\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Overall 3.0 (Findings), Confidence 4/5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2（新颖性与完整性审查）的完整审稿意见。请逐条回应：对每个 Weakness/Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的完整审稿意见\n\n### Summary\n本文对三种 execution-free 代码修复验证公式进行了首次系统性匹配比较。核心发现是\"三层结构\"。论文还提供了一个 failure mode 分类体系。\n\n### Weaknesses\n\n**N1 [CRITICAL] 核心贡献为比较已有公式，novelty 有限**\n三种公式均为已有方法，论文贡献完全是实验比较框架本身。核心发现\"更复杂的任务→公式选择更重要\"虽然数据支撑充分，但从直觉上可以预期。论文描述了 what happens 但没有提供深层 why 的理论理解。对 EMNLP main conference 需要 excitement 层面的贡献。建议提出轻量 routing/ensemble 方法或 complexity threshold 理论分析。\n\n**N2 [CRITICAL] ≤8B LoRA 规模限制严重威胁结论的泛化性**\nCWM 的 repo-level 退化很可能根本上是容量问题，而非公式本身固有缺陷。如果 32B CWM 在 repo level 不退化，则\"公式选择在 repo level 至关重要\"这一核心结论不成立。Abstract 和 conclusion 中主张未附加此关键限定。\n\n**W1 [WARNING] 单一语言（Python-only）评估，但 Limitations 未提及**\n验证公式在 Java/C++ 或不同测试范式下的行为可能不同。Limitations 段没有讨论语言单一性。\n\n**W2 [WARNING] 与 reward model 文献联系不够充分**\nCLS/CWM/TRAJ 与 ORM/PRM 之间存在自然映射，但论文未深入讨论。遗漏 CodeRM (Diao et al., ACL 2025)。\n\n**W3 [WARNING] \"complexity-aware formulation routing\" 仅为未验证假设**\nAbstract 声称 motivate routing 但没有实现或评估任何 routing 机制。\n\n**W4 [WARNING] TRAJ 公式探索不充分**\n没有探索中间方案（per-test TRAJ + aggregation）。TRAJ 劣势可能部分是设计选择的结果。\n\n**M1 [MINOR]** \"formulation choice is governed by code complexity\" 用词过强。\n**M2 [MINOR]** 3-shot ICL collapse 发现仅在正文一句带过。\n**M3 [MINOR]** 16 个 Appendix 组织可改善。\n\n### Questions\nQ1. CWM repo-level 退化是否主要是 model capacity 问题？32B CWM 是否能恢复等价性？\nQ2. 是否尝试过不依赖 oracle 的简单 routing 启发式？\nQ3. TRAJ 为何设计为 single binary output 而非 per-test trajectory + aggregation？\nQ4. 结论是否可推广到 code generation（无 buggy source 对比）场景？\nQ5. CLS vs CWM 实际推理时间差距是多少？端到端 wall-clock time？\n\n### Missing References\nCodeRM (Diao et al., ACL 2025), ORM/PRM 框架映射讨论\n\n### Scores\nSoundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Overall 3.0 (Findings), Confidence 4/5"
  }
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-22T15:48:45.573259+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1311
}
```

</details>

---


### Assistant

_source line 811 · 2026-05-22T15:48:56.560333+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 812 · 2026-05-22T15:48:59.119913+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论：Overall 3/5 (Findings)**

核心判断：
- **方法论严谨**：匹配实验设计 + TOST 等价性检验 + ICC 是本文的亮点，值得学习
- **Novelty 受限**：三种公式均为已有方法，核心发现（复杂任务→公式选择更重要）可从直觉预期
- **两个 CRITICAL 问题**：(1) 比较已有公式无新方法，excitement 不足；(2) ≤8B LoRA 规模限制使核心结论的泛化性存疑——CWM 的 repo-level 退化可能是容量问题而非公式固有缺陷
- **格式合规**：正文 8 页、匿名、checklist 完整，无格式问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 813 · 2026-05-22T15:49:13.513400+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 70

## Round 70

3 recorded events


### User

_source line 814 · 2026-05-22T15:50:29.872918+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R2-N1: 核心贡献为比较已有公式，novelty 有限**
同意这是一个合理的关切。论文本质上是 empirical comparison，三种 formulation 均非新提出。不过我认为 R2 低估了两个方面的贡献：(1) failure mode taxonomy（Section 3.5, Table 4）不仅是描述"what happens"，还通过 formal collapse / decision collapse / aggregation penalty 的定量分析提供了"why"的部分解释；(2) Appendix M 的 mixed-effects regression（CWM×repo interaction β=−0.219, z=−23.7）为 complexity-dependent divergence 提供了统计建模层面的"why"。但我同意，对 EMNLP main conference 而言，仅 comparison + taxonomy 在 excitement 维度偏弱。R2 建议的轻量 routing/ensemble 方法若能实现，确实可显著提升贡献度。

**[REBUT] R2-N2: ≤8B LoRA 规模限制严重威胁结论泛化性**
R2 认为 CWM repo-level 退化"很可能根本上是容量问题"，但论文已提供了**反面证据**：Section 3.3 + Figure 2 显示，从 4B 扩展到 8B 时，CLS-CWM gap 不仅没有缩小，反而**从 1.32pp 扩大到 2.62pp**（function level）以及在 repo level 同样扩大（Table 3）。如果退化纯粹是容量问题，增加参数量应缩小差距而非扩大。此外，Appendix I 的 qualitative error analysis 表明 CWM 的 formal collapse（53-74% unparseable）源于 output format complexity（multi-token structured output 的组合爆炸），这是 formulation 的固有属性而非单纯容量不足。

但我同意 R2 的一个子论点：≤8B 的范围确实不足以排除 32B+ 模型可能改变 landscape 的可能性。论文 Conclusion 承认"testing at 32B+ scale would resolve the primary open question"，但 abstract/conclusion 的 claim 确实缺少此限定。建议在 abstract 加入"under ≤8B LoRA"限定语。

**[AGREE] R2-W1: Python-only 评估未在 Limitations 提及**
同意。Limitations（Section 5/p.9）讨论了 seed coverage、synthetic-to-real gap、downstream re-repair、mutation distribution，但确实遗漏了语言单一性。不同语言（特别是编译型语言如 Java/C++）的 test output 格式差异可能影响 CWM 的 formal collapse rate。应在 Limitations 补充一句。

**[AGREE] R2-W2: 与 ORM/PRM 文献联系不够**
部分同意。论文 Section 4（Related Work, p.8）确实提到了"Process vs. Outcome Supervision"并引用了 PRM 相关工作（Lightman et al., 2023; Snell et al., 2025），但未明确建立 CLS↔ORM、CWM↔PRM 的映射关系。这个映射对读者理解 formulation landscape 有帮助。不过，严格来说 CWM 不完全等同于 PRM（CWM 生成 execution output 而非中间推理步骤的 reward），所以映射需要 nuance。CodeRM 如果确实在 ACL 2025 发表，应当引用。

**[REBUT] R2-W3: "complexity-aware routing" 仅为未验证假设**
R2 将此视为 WARNING 级问题，但论文 abstract 的原文是"motivate complexity-aware formulation **routing**"——这是在描述 findings 的 implication，而非声称 routing 是本文贡献。Section 5（Conclusion）同样将 routing 列为"Three directions follow"的第一个 future direction。在 empirical comparison 论文中，从实验发现中 derive actionable directions 是标准做法，不需要在同一篇论文中实现。只要措辞是"motivate"而非"propose"或"demonstrate"，这是合理的。

**[REBUT] R2-W4: TRAJ formulation 探索不充分**
R2 建议探索 per-test TRAJ + aggregation 中间方案。但论文的 scope 是比较**现有** formulations under matched conditions，而非设计新 formulation。TRAJ 的 single-binary-output 设计直接沿用 FAIR CodeGen team et al. (2025) 的协议（Section 2.1）。如果论文开始修改 TRAJ 的设计，就不再是比较"existing formulations"，而变成了 formulation design 论文——这是不同的贡献类型。论文已在 Section 2.2 中讨论了 TRAJ"discards diagnostic granularity"作为设计权衡，并在 Appendix B 中通过 downsampling ablation 控制了部分混杂。

**[AGREE] R2-M1: "governed by" 用词过强**
同意。"governed by"暗示 deterministic 关系，但论文的证据仅基于 2-3 seeds、≤8B 模型、单一语言。"moderated by"或"depends on"更准确。与我自己在 R1 审查中对 claim 措辞强度的关切一致。

**[AGREE] R2-M2: 3-shot ICL collapse 发现未充分展开**
同意。Section 3.3 提到 3-shot ICL collapses to always-predict-unresolved baseline（Table 7, Appendix B），这是一个 practically important 的 negative result（说明 few-shot prompting 不能替代 fine-tuning for verification）。值得在 main text 多一段讨论其 implication（即 fine-tuning 是 verification 的必要条件，不仅仅是锦上添花）。

**[AGREE] R2-M3: Appendix 组织**
轻度同意。16 个 Appendix 覆盖面广但导航不便。建议至少加一个 Appendix 目录索引。

---

### Questions 回应

**Q1 (32B CWM):** 已在 N2 回应中 address。4B→8B 数据显示 gap 扩大而非缩小，部分反驳了纯容量假说。但 32B 验证确实是 open question。

**Q2 (Routing heuristic):** 合理问题，但属 future work scope。论文提供了 routing 的 empirical basis（function-level 等价 → 用 CLS for throughput；repo-level → 用 CLS for accuracy），实际 routing 实现超出 comparison paper 范围。

**Q3 (TRAJ per-test design):** TRAJ 沿用 FAIR CodeGen team (2025) 协议。改变 TRAJ 设计超出"比较现有公式"的 scope。

**Q4 (Code generation 场景):** 合理关切。Code repair 有 buggy source 作对比基准，code generation 没有。论文未声称结论可推广到 generation，但应在 Limitations 明确提及。

**Q5 (推理时间):** 论文 Section 2.1 报告了 output cost（CLS: Σ|b_i|≈|T| tokens; CWM: N tokens per test; TRAJ: 1 token），但确实没有 wall-clock time 数据。考虑到 CLS 和 TRAJ 均为 1 token output，推理时间差异主要来自 CWM 的 multi-token generation。这是可补充的实验。

---

### 对 R2 Scores 的评论

R2 给出 Excitement 2.5、Overall 3.0，我给出 Excitement 3.0、Overall 3.5。分歧主要在 excitement 上：R2 更看重 novelty（新方法/新理论），我更看重 methodological depth（统计方法论的严谨性在 NLP 中确实罕见）。两个视角都有道理。如果作者能 address N1（checkpoint）和 N2（TOST power），在 soundness 层面可上调；但 excitement 的上调可能需要额外贡献（如 R2 建议的 routing mechanism）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 815 · 2026-05-22T15:50:38.986749+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-22T15:50:39.137872+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


## Round 71

## Round 71

2 recorded events


### User

_source line 817 · 2026-05-22T15:50:45.557945+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条交叉回应。

核心判断：
- R2 的 N2（规模限制）被 Figure 2 的 4B→8B gap 扩大数据部分反驳，但同意 abstract 应加限定语
- R2 的 W3（routing 未验证）和 W4（TRAJ 设计）被反驳——属 future work 和 scope 问题
- R2 的 N1（novelty）、W1（Python-only）、W2（ORM/PRM）、M1-M3 基本同意
- 两位 reviewer 在 Overall 上分歧 0.5 分（3.0 vs 3.5），主要来自对 methodological depth vs. novelty 的权重差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 818 · 2026-05-22T15:51:35.489079+00:00_

R1 的交叉回应已收到。等待 R2 对 R1 的交叉回应。

当前进度：
- ✅ Step 1: R1、R2 独立初审完成
- ✅ Step 2 (部分): R1 对 R2 的交叉回应已提交
- ⏳ Step 2 (待完成): R2 对 R1 的交叉回应

R1 交叉回应要点：
- **同意** R2-N1（novelty 有限）、R2-W1（Python-only）、R2-W2（ORM/PRM）、R2-M1/M2/M3
- **反驳** R2-N2（规模限制）：Figure 2 显示 4B→8B gap 扩大而非缩小，部分反驳纯容量假说，但同意 abstract 应加限定语
- **反驳** R2-W3（routing 未验证）：论文措辞是"motivate"而非"propose"，属合理 future work
- **反驳** R2-W4（TRAJ 探索不充分）：修改 TRAJ 设计超出 comparison paper scope

等待 R2 的交叉回应后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 72

## Round 72

10 recorded events


### User

_source line 819 · 2026-05-22T15:53:10.853015+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Weaknesses 逐条回应

### R1-N1 [CRITICAL]: Repo-level checkpoint selection 不公平

**[REBUT]**

R1 的担忧在原则上合理——CWM 因 NaN validation loss 退化为 final-epoch checkpoint 而 CLS 使用 val-selected checkpoint——但论文提供了两项关键证据大幅削弱这一混杂变量的解释力：

1. **匹配 checkpoint 分析（Section 3.5, p.6）**：论文明确报告 "Under matched checkpoint selection (epoch 3 for both), the cross-model gap difference narrows to ~2 pp (Qwen3: 20.47pp vs. DeepSeek: 22.89pp). The gap is formulation-driven rather than model-specific." 即使在统一使用 epoch 3 的条件下，CLS-CWM gap 仍然高达 ~20-23pp。Checkpoint 差异无法解释这一量级的 gap。

2. **CLS checkpoint ablation（Appendix O, p.21）**：论文对 Qwen3-8B CLS s42 做了 checkpoint ablation，显示 epoch 1 (85.34%), val-selected (84.48%), final epoch (85.29%)，范围仅 ~1pp。且 val-selected checkpoint 反而是最低的，说明 val-selection 并未给 CLS 带来系统性优势。

3. **DeepSeek 早停 CWM（Appendix O, p.21）**：论文报告 "a DeepSeek-Coder early-stopped checkpoint (s123, epoch 1) achieves 79.48% versus 57.31% at epoch 3 (+18.14pp), but retains 66.45% unparseable rate, confirming that formal collapse emerges early and is not a late-training artifact." 早停确实帮助 CWM 提升 ~18pp，但即使用最优 checkpoint，CWM 仍保留 66.45% 的不可解析率，远低于 CLS 水平。

**我的评估**：R1 指出了一个真实存在的混杂，但论文已在 Section 3.5 和 Appendix O 中提供了充分的缓解证据。Checkpoint 选择影响 CWM 的绝对性能（~18pp），但不改变 "CLS 在 repo level 显著优于 CWM" 的核心结论。不过我同意论文应在正文中更显著地讨论这一点（目前分散在 Section 3.5 半段和 Appendix O）。

---

### R1-N2 [CRITICAL]: TOST 统计功效不足

**[AGREE]**

R1 的分析准确。n_eff ≈ 86 对 medium effect size 的 TOST 功效仅 ~0.3，这意味着 CLS-TRAJ 未通过 Holm-Bonferroni 校正（adjusted p=0.075, Section 3.4, Table 15）可能是功效不足而非真正的非等价性。

论文在 Section 3.4 中确实承认了这一点："nominally significant but not surviving Holm-Bonferroni correction"。但 Abstract 中 "TRAJ parity differs between the two tested families" 的措辞不够精确——它暗示了一个确定性结论，而实际上更准确的表述是 "等价性未能在多重比较校正下得到确认"。

**补充**：我在自己的审稿中未将此列为 CRITICAL 级别问题（我将其归入了 framing accuracy 的 minor concern），但 R1 的功效分析让我认为这确实值得更高的关注度。建议作者：(a) 报告 post-hoc power analysis 结果；(b) 修改 abstract 措辞为更审慎的表述。

---

### R1-W1 [WARNING]: 训练数据量差异（CLS ~70K vs TRAJ ~386）

**[AGREE]**

论文在 Section 3.5（p.6）自己承认 downsampling ablation "controls data volume but not label granularity (per-test vs. variant-level), and it remains a single-seed comparison (Appendix B)"。R1 指出的 signal granularity 差异是一个无法通过简单 volume matching 解决的根本性问题——CLS 获得 per-test 级别的监督信号，而 TRAJ 仅获得 variant-level 信号。这可能 systematically 有利于 CLS。

论文已坦诚承认此限制，我认为这是诚实的处理，但 R1 将其提升到 WARNING 级别是合理的。

---

### R1-W2 [WARNING]: Repo-level seed 覆盖不足（2-3 seeds）

**[AGREE]**

Repo-level 仅 2-3 seeds（vs. function-level 5 seeds），且 repo-level variance 远大于 function-level。论文在 Limitations（p.9）中部分承认 "limited seed coverage for repo-level comparisons"，但正文中的 repo-level claims 确实读起来像 definitive 结论。

这与我自己的 N2 (scale limitation) 形成互补关注——repo-level 的结论既受限于 seed 数量，也受限于 model scale。两者叠加使得 repo-level findings 的置信度显著低于 function-level findings。

---

### R1-W3 [WARNING]: CWM exact string matching 系统性惩罚

**[REBUT]**

R1 的直觉合理，但论文在 Appendix I（p.18）提供了直接反驳证据：

1. **"(c) Relaxed matching does not rescue CWM"**：论文系统测试了宽松匹配（tolerating format deviations, LO-LA），结果显示 "The divergence widens from 26pp to 27 pp under relaxed matching. This rules out the hypothesis that parsing strictness inflates the observed gap."

2. **可解析输出的语义准确率（Section 2.2, p.2; Section 3.5, p.6）**："even parseable CWM outputs achieve only 49.4% accuracy"——即使排除格式问题，语义准确率也远低于 CLS。瓶颈是语义的，不是格式的。

3. **Formal collapse 本身是 formulation 的固有特性**：生成式方法在 repo-level 面临格式崩溃是该 formulation 的天然挑战，而非评估标准的不公平。如果一个方法在实际部署中也会产生 53-74% 不可解析输出，这本身就是选择该 formulation 的重要考量。

综上，exact string matching 的严格性没有人为放大 CLS-CWM 的差距。

---

### R1-W4 [WARNING]: SESOI ±2pp 的 a priori 属性

**[AGREE]（部分）**

R1 对 "a priori" 属性的质疑有道理——很难验证 ±2pp 是否在看到数据前就确定了。但论文提供了两方面缓解：

1. **实质性论证（Section 2.3, p.4）**："a 2 pp difference corresponds to ∼2–3 problems out of 114—below the threshold at which a practitioner would select one formulation over another." 这一从业者视角的论证是合理的，不依赖于数据。

2. **敏感性分析（Appendix J, p.19-20）**：Table 13 显示在 1.0pp 到 5.0pp 的不同 margin 下，CLS-CWM 等价性在所有 margin ≥ 2pp 时均成立。这表明结论不依赖于 ±2pp 的具体选择。

我认为将其从 "a priori" 重新定位为 "practically motivated with robustness check" 更诚实。

---

### R1-M1 [MINOR]: LPM vs. logistic regression

**[AGREE]**

对于 binary outcome，logistic regression 是更标准的选择。不过 LPM 系数可直接解释为概率差异（percentage point），在这种比较研究中有实用优势。Appendix M（p.20）的 LPM 和 logistic regression 结论一致（论文报告 "logistic regression produces coefficients of the same sign and comparable significance"），所以选择 LPM 不影响结论，但 R1 的建议（以 logistic regression 为主分析）方法论上更严谨。

---

### R1-M2 [MINOR]: Figure 2 y-axis 不从零

**[AGREE]**

有效关注点，但 Figure 2 caption 已标注 "Note: y-axis begins at 55%"，降低了误导风险。我在自己的审稿中也注意到了这一点。

---

## Questions 回应

**R1-Q1**（能否提供 CWM repo-level early-stopped checkpoint 结果？）
[AGREE] 这与我的 Q1 一致。但需要注意论文在 Appendix O 已提供了 DeepSeek 的部分结果：early-stopped epoch 1 达 79.48%（vs. epoch 3 的 57.31%），但仍保留 66.45% 不可解析率。Qwen3 的对应数据确实缺失。

**R1-Q2**（Bayesian equivalence test / ROPE）
[AGREE] Bayesian ROPE 方法可以提供更直观的等价性概率估计，特别是在样本量有限的情况下。这是一个建设性的方法论建议。

**R1-Q3**（"TRAJ parity differs" 是否可更精确）
[AGREE] 与我对 N2 的回应一致——措辞应更审慎。

**R1-Q4**（Cross-seed oracle 是 any-correct 还是 majority voting？）
[AGREE] 这需要澄清。从 Section 3.7 的描述来看，oracle combination 应该是 any-correct（如果任一 formulation 正确则标记为正确），但论文没有明确说明。

**R1-Q5**（CWM formal collapse 中"语义正确但格式不匹配" vs "完全错误"的比例）
[AGREE] 这直接关系到 W3 的评估。Appendix I 的 relaxed matching 分析部分回答了这个问题（宽松匹配后准确率仍低），但一个显式的分解会更有说服力。

**R1-Q6**（CWM/CLS data processing scripts 是否可能引入差异）
[AGREE] 合理的 reproducibility 关注。论文 Appendix E 提供了数据处理细节，但没有做 pipeline 消融分析。

---

## R1 评分的对比评估

| 维度 | R1 | R2（我） | 差异分析 |
|------|-----|---------|---------|
| Soundness | 3/5 | 3.5/5 | R1 对 checkpoint confound (N1) 和 TOST power (N2) 给了更大权重。但我认为 N1 的影响被 Section 3.5 的匹配分析和 Appendix O 的早停数据大幅缓解，所以我维持 3.5。 |
| Excitement | 3/5 | 2.5/5 | R1 似乎对方法论贡献（TOST 在 NLP 中的应用）给了更多 excitement credit。我认为方法论规范性值得肯定但不构成 excitement 提升——核心发现仍然是"直觉上可预期的"。我维持 2.5。 |
| Overall | 3.5 | 3.0 | 关键分歧：R1 认为 Borderline Conference (3.5)，我认为 Findings (3.0)。我维持 3.0，原因是 (a) novelty 受限于比较已有方法（我的 N1），(b) ≤8B 规模限制泛化性（我的 N2），(c) 核心发现可从直觉预期。但如果作者能 address 我的 N1（增加 routing 实验或理论分析）和 N2（增加一个更大模型配置），我会考虑提升至 3.5。 |
| Confidence | 4/5 | 4/5 | 一致 |

---

## 总结

R1 的审稿意见质量很高，统计方法论层面的 concerns（N2 TOST 功效、W4 SESOI）尤其有价值。但我认为 **N1 (checkpoint confound) 的严重性被高估了**——论文在 Section 3.5 和 Appendix O 提供的匹配分析和早停数据表明，即使控制 checkpoint 选择，CLS-CWM gap 仍然 ~20-23pp，核心结论 robust。

我与 R1 的主要分歧在 excitement（2.5 vs 3）和 overall（3.0 vs 3.5）。我认为作为纯比较研究，即使执行再严谨，excitement 也难以达到 main conference 门槛。R1 似乎对方法论贡献（将 TOST/ICC 引入 NLP verification 比较）给了更多正面权重，这是合理的但我不完全同意。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-22T15:54:12.697355+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool call

_source line 821 · 2026-05-22T15:54:12.748596+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 822 · 2026-05-22T15:54:12.849588+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T15:39:21.237650+00:00\", \"completed_at\": \"2026-05-22T15:42:53.680091+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为连续纯文本（Title+Abstract+Introduction+Method开头），无任何 display item。第一个视觉锚点 Figure 1 出现在第 3 页顶部——刚好在 3 页窗口边界内，但若能将 Figure 1 提前至第 2 页会显著改善审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（三种验证公式对比图）作为首个 display item 传达了论文核心概念，caption 自包含，颜色区分清晰（蓝/绿 LLM 模块 vs 橙色输出），信息传达有效\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 和 Table 2 同时出现在一页，页面数据密度较高但布局紧凑合理；booktabs 风格，最优值加粗，小数位数统一\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 3 使用 table* 全宽排版，适合其列数；booktabs 风格一致\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 柱状图 y 轴从 55% 起始（截断 y 轴），caption 中有标注 \\\"y-axis begins at 55%\\\"。对于柱状图，截断 y 轴可能被审稿人质疑为视觉放大差异；caption 的声明部分缓解了此问题，但建议考虑从 0 起始或改用点图/差值图\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文本最后一页（Conclusion）为纯文本，与第 7 页仅有 Figure 2 形成较低视觉密度收尾。页面填充完整，无大面积空白\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段落简短（约 1/3 页），符合 EMNLP 要求；随后 References 开始，格式规范\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"论文 PDF 内包含 ARR Responsible NLP Research Checklist。根据 EMNLP 2026 规则，此 checklist 应在 OpenReview submission form 中填写；PDF 内包含不算错误但可能冗余，需确认当前 ARR 周期的具体要求\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Appendix A 中 Figure 3 柱状图字号偏小但仍可读；Table 5 格式清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"末页文本仅占约 1/3 页面，下方 2/3 为空白。因为是 Appendix 最后一页，影响不大\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 10}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 823 · 2026-05-22T15:54:12.850169+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 824 · 2026-05-22T15:58:08.543981+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. 但 repo-level claims 仍需在正文中加 seed 数量标注和不确定性声明。\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Section 3.5 matched epoch-3 分析 + Appendix O CLS ablation 充分缓解。R10 R2 REBUT 成功。核心结论 robust。\"\n  resolution_round: 10\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"（可选）增加轻量 routing/ensemble 实验或 complexity threshold 理论分析以提升 excitement\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"标题已改为 Systematic Comparison。但 novelty 本质上受限于比较研究的性质。\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'；引用 Appendix J sensitivity analysis 作为 robustness check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Appendix J sensitivity analysis 存在但正文措辞仍需调整。\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Abstract 已有 qualifier，Conclusion 仍需补充。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Diao et al., ACL 2025 'Dynamic Scaling of Unit Tests for Code Reward Modeling') 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM (Diao et al., ACL 2025) 真实性后加入 Related Work；加半段 CLS↔ORM/CWM↔PRM 映射讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n  action_items:\n    - round: 10\n      action: \"考虑从 0 起始或改用点图/差值图\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"§3.4 现在分开呈现。可能已修复。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提出。§3.4 分开呈现 CLS-CWM TOST 和 CLS-TRAJ TOST。视为已修复。\"\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 裁定 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"Abstract 现含 '≤8B LoRA protocol' 和 'DeepSeek-Coder' 标注。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Abstract 已有限定。视为已修复。合并至 R6-W2 追踪 Conclusion 的限定。\"\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"正文讨论 TOST 功效限制（不仅 Appendix）；Abstract 'TRAJ parity differs' 改为更审慎措辞如 'TRAJ equivalence could not be confirmed after multiple comparison correction'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。Cross-seed oracle 94.27±2.59% 已在正文。可能已修复，待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 C2 合并处理.\"\n    - round: 10\n      reviewers: []\n      note: \"Abstract 现含 'DeepSeek-Coder' 标注。R10 未被提出。\"\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"GenRM must-cite.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2 额外提出 CodeScaler, GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: []\n      note: \"GenRM, CodeScaler, GenPRM 均已在 Related Work 中出现。R10 未被提出。新的遗漏 (CodeRM) 追踪在 R6-W8。\"\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。合并至 R6-W2 追踪。\"\n  resolution: \"合并至 R6-W2 统一追踪 scale qualifier。\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。R1 认为 methodology 有 excitement，R2 认为核心发现可预期。合并至 R6-N4 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未提出。§3.4 footnote 已讨论。\"\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 rated critical, R1 agrees.\"\n    - round: 10\n      reviewers: []\n      note: \"标题已改为 'A Systematic Comparison of Execution-Free Verification Formulations for Code Repair'。R10 未被提出。\"\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 降为 warning.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching 系统性惩罚。R2 REBUT：Appendix I relaxed matching 使 gap 从 26pp 扩大到 27pp；parseable accuracy 仅 38-43%。瓶颈是语义的不是格式的。Director 采纳 R2 REBUT。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。Exact match 没有人为放大差距。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 现使用 'differs between the two tested families' 措辞。可能已修复，待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。合并至 R6-M3 追踪 Figure y-axis 问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"已改为 'increasingly leverages'。R10 未被提出。\"\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Wellek (2010) 已在 §3.4 引用，Moulton (1990) 已在 §3.4 和 Appendix A 引用。R10 未被提出。\"\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§3.1 现在明确说明 'we resample entire problems, not individual tests'。R10 未被提出。\"\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-N2 讨论了 n_eff≈86 对 TOST 功效的影响。合并至 R8-W1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 提出。R1 AGREE。HumanEval+MBPP 和 SWE-bench 均为 Python。不同语言（Java/C++）可能影响 CWM formal collapse rate 和 CLS 行为。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 增加一句关于语言覆盖单一性的讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。'governed by' 暗示 deterministic/因果关系，实际证据仅 2 levels × 2-3 seeds × ≤8B。应改为 'moderated by' 或 'depends on'。\"\n  action_items:\n    - round: 10\n      action: \"Introduction/Conclusion 中 'governed by' 改为 'moderated by' 或 'depends on'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 AGREE。Section 3.5 一句提到 3-shot collapses to always-predict-unresolved (45.83%)，重要 negative result 但主要讨论在 Appendix B。值得在正文多半段。\"\n  action_items:\n    - round: 10\n      action: \"正文增加半段讨论 3-shot ICL collapse 的 implication（fine-tuning 是 verification 必要条件）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 轻度 AGREE。建议加 Appendix 目录索引或合并相关 ablation。\"\n  action_items:\n    - round: 10\n      action: \"（可选）加 Appendix 目录索引\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. 但 repo-level claims 仍需在正文中加 seed 数量标注和不确定性声明。\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Section 3.5 matched epoch-3 分析 + Appendix O CLS ablation 充分缓解。R10 R2 REBUT 成功。核心结论 robust。\"\n  resolution_round: 10\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"（可选）增加轻量 routing/ensemble 实验或 complexity threshold 理论分析以提升 excitement\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"标题已改为 Systematic Comparison。但 novelty 本质上受限于比较研究的性质。\"\n  resolution_round: null\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'；引用 Appendix J sensitivity analysis 作为 robustness check\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Appendix J sensitivity analysis 存在但正文措辞仍需调整。\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"Abstract 已有 qualifier，Conclusion 仍需补充。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Diao et al., ACL 2025 'Dynamic Scaling of Unit Tests for Code Reward Modeling') 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM (Diao et al., ACL 2025) 真实性后加入 Related Work；加半段 CLS↔ORM/CWM↔PRM 映射讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n  action_items:\n    - round: 10\n      action: \"考虑从 0 起始或改用点图/差值图\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"全票共识 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"§3.4 现在分开呈现。可能已修复。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提出。§3.4 分开呈现 CLS-CWM TOST 和 CLS-TRAJ TOST。视为已修复。\"\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Director 裁定 critical.\"\n    - round: 9\n      reviewers: []\n      note: \"Abstract 现含 '≤8B LoRA protocol' 和 'DeepSeek-Coder' 标注。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Abstract 已有限定。视为已修复。合并至 R6-W2 追踪 Conclusion 的限定。\"\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: open\n    - round: 10\n      action: \"正文讨论 TOST 功效限制（不仅 Appendix）；Abstract 'TRAJ parity differs' 改为更审慎措辞如 'TRAJ equivalence could not be confirmed after multiple comparison correction'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。Cross-seed oracle 94.27±2.59% 已在正文。可能已修复，待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"与 C2 合并处理.\"\n    - round: 10\n      reviewers: []\n      note: \"Abstract 现含 'DeepSeek-Coder' 标注。R10 未被提出。\"\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"GenRM must-cite.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2 额外提出 CodeScaler, GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: []\n      note: \"GenRM, CodeScaler, GenPRM 均已在 Related Work 中出现。R10 未被提出。新的遗漏 (CodeRM) 追踪在 R6-W8。\"\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。合并至 R6-W2 追踪。\"\n  resolution: \"合并至 R6-W2 统一追踪 scale qualifier。\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。R1 认为 methodology 有 excitement，R2 认为核心发现可预期。合并至 R6-N4 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未提出。§3.4 footnote 已讨论。\"\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 rated critical, R1 agrees.\"\n    - round: 10\n      reviewers: []\n      note: \"标题已改为 'A Systematic Comparison of Execution-Free Verification Formulations for Code Repair'。R10 未被提出。\"\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1 rated critical, R2 降为 warning.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching 系统性惩罚。R2 REBUT：Appendix I relaxed matching 使 gap 从 26pp 扩大到 27pp；parseable accuracy 仅 38-43%。瓶颈是语义的不是格式的。Director 采纳 R2 REBUT。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。Exact match 没有人为放大差距。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 现使用 'differs between the two tested families' 措辞。可能已修复，待确认。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被独立提出。合并至 R6-M3 追踪 Figure y-axis 问题。\"\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"已改为 'increasingly leverages'。R10 未被提出。\"\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"Wellek (2010) 已在 §3.4 引用，Moulton (1990) 已在 §3.4 和 Appendix A 引用。R10 未被提出。\"\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"§3.1 现在明确说明 'we resample entire problems, not individual tests'。R10 未被提出。\"\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-N2 讨论了 n_eff≈86 对 TOST 功效的影响。合并至 R8-W1 追踪。\"\n  resolution: \"\"\n  resolution_round: null\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 提出。R1 AGREE。HumanEval+MBPP 和 SWE-bench 均为 Python。不同语言（Java/C++）可能影响 CWM formal collapse rate 和 CLS 行为。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 增加一句关于语言覆盖单一性的讨论\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。'governed by' 暗示 deterministic/因果关系，实际证据仅 2 levels × 2-3 seeds × ≤8B。应改为 'moderated by' 或 'depends on'。\"\n  action_items:\n    - round: 10\n      action: \"Introduction/Conclusion 中 'governed by' 改为 'moderated by' 或 'depends on'\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 AGREE。Section 3.5 一句提到 3-shot collapses to always-predict-unresolved (45.83%)，重要 negative result 但主要讨论在 Appendix B。值得在正文多半段。\"\n  action_items:\n    - round: 10\n      action: \"正文增加半段讨论 3-shot ICL collapse 的 implication（fine-tuning 是 verification 必要条件）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 轻度 AGREE。建议加 Appendix 目录索引或合并相关 ablation。\"\n  action_items:\n    - round: 10\n      action: \"（可选）加 Appendix 目录索引\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
  }
}
```

</details>

---


### Tool result

_source line 825 · 2026-05-22T15:58:08.695696+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 23799}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 826 · 2026-05-22T16:00:48.513040+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "report": "\n# Round 10 审稿报告\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**审稿模式**: Fresh (初审)\n**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）\n\n---\n\n## Summary\n\n本文对三种 execution-free 代码修复验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）进行了首次系统性匹配比较，使用相同 base model（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、相同 LoRA 配置、相同训练数据，在 function-level 和 repo-level 两个复杂度层次上评估。核心发现是\"三层结构\"：(1) fine-tuning 必要（35-36pp 提升），(2) function-level 公式间统计等价（TOST p=0.007），(3) repo-level 下 CWM 显著退化（低于 CLS 18-26pp），driven by format collapse。论文还提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 匹配实验框架设计在 NLP 论文中属罕见严谨。** 相同 base model、LoRA rank、optimizer、training schedule、5 seeds（function-level），DeepSeek-Coder 作为 cross-model consistency check。这是实验比较研究的标杆（Section 3.1, Table 1）。[R1-S1, R2-S1 共识]\n\n**S2. 统计方法论深度远超 NLP 领域平均。** TOST 等价检验（而非仅 NHST）、ICC-based clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 多重比较校正、mixed-effects LPM——这套工具链在 NLP 论文中极为少见（Section 3.1, 3.4, Appendix A/J/M）。[R1-S2, R2-S1 共识]\n\n**S3. Failure mode taxonomy 有独立实用价值。** Format collapse / decision collapse / aggregation penalty 三类 failure modes 有定量分析和定性例证（Section 3.5, Table 4, Appendix H），为从业者选择 formulation 提供可操作指导。[R1-S3, R2-S3 共识]\n\n**S4. Error complementarity 发现有 ensemble/routing 研究价值。** Oracle combination 90.63%（function）/ 95.83%（repo），证明公式犯互补错误。Cross-seed oracle 94.27±2.59% 确认跨 seed 稳定性（Section 3.6）。[R2-S4]\n\n**S5. 附录极其详尽且自我批评诚实。** 16 个 Appendix（14 页）覆盖全部 ablation、convergence、power analysis、prompt templates、qualitative errors。Limitations 和 Threats to Validity 主动识别并讨论多个潜在问题。[R1-S4/S5, R2-S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Must-Fix 1] Novelty 受限：核心贡献为比较已有 formulations，excitement 不足 main conference**\n- 来源：R2-N1 提出，R1 AGREE\n- 详情：三种 formulation 均为已有方法（CLS: Ni et al. 2023; CWM: FAIR 2025; TRAJ: Shum et al. 2025）。核心发现\"复杂任务→公式选择更重要\"数据支撑充分但从直觉可预期。论文描述了 what happens 但缺少深层 why 的理论理解——为什么恰好在 repo level 而非某个中间复杂度出现分歧？\"三层结构\"是描述性的而非解释性的。\n- 影响：两位 Reviewer 共识 Excitement 2.5-3.0/5，一致认为 Findings 合适但 Main 不够。\n- 建议：(a) 增加轻量 routing/ensemble 实验将贡献从\"比较\"提升为\"比较+方案\"；(b) 或提供 complexity threshold 的理论分析。\n\n**[Must-Fix 2] TOST 统计功效不足，CLS-TRAJ 等价性无法确认**\n- 来源：R1-N2 提出，R2 AGREE（交叉分享后升级关注度）\n- 详情：n_eff ≈ 86，TOST 对 medium effect size 功效仅 ~0.3（70% 概率将真实中等差异误判为等价）。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。Abstract \"TRAJ parity differs between the two tested families\" 措辞不够精确——实际是等价检验功效不足、无法下结论，而非 TRAJ 显著不等价。\n- 建议：(a) 正文讨论 TOST 功效限制（目前仅 Appendix J/K）；(b) Abstract 措辞改为\"TRAJ equivalence could not be confirmed after multiple comparison correction\"；(c) 考虑补充 Bayesian equivalence test（ROPE-based）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[Should-Fix 1] ≤8B LoRA 规模限制——Conclusion 缺少限定语**\n- 来源：R2-N2 提出 CRITICAL，R1 部分 REBUT（4B→8B gap 扩大数据反驳纯容量假说）\n- Director 裁定：降为 Should-Fix。R1 反驳有效——4B→8B 时 CLS-CWM gap 从 1.32pp 扩大到 2.62pp（Figure 2），说明增加参数量不缩小差距。且 Appendix I qualitative analysis 表明 format collapse 源于 output format complexity（formulation 固有属性）。但 ≤8B→32B 跨越量级不同，不能完全排除。Abstract 已有\"≤8B LoRA protocol\"限定，但 Conclusion 和部分正文 claims 仍缺。\n- 建议：Conclusion 加入 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化。\n\n**[Should-Fix 2] Checkpoint selection 混杂——正文讨论不够显著**\n- 来源：R1-N1 标 CRITICAL，R2 REBUT\n- Director 裁定：降为 Should-Fix。R2 反驳有效——Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp range（val-selected 反而最低）。Checkpoint 差异无法解释 18-26pp gap。但缓解证据分散在 Section 3.5 半段和 Appendix O，正文应更显著讨论。\n- 建议：正文中合并讨论 checkpoint 缓解证据（matched epoch-3 gap + CLS ablation range），而非仅依赖 Appendix。\n\n**[Should-Fix 3] 训练数据量差异（CLS ~70K vs TRAJ ~386）+ 信号粒度不同**\n- 来源：R1-W1 提出，R2 AGREE\n- 详情：~180× 数据量差异。Downsampling ablation 控制了 volume（CLS 80.74% vs TRAJ 72.92%，仍高 7.82pp）但未控制 signal granularity（per-test vs variant-level）。两人共识：应将此框架为 formulation 固有属性。\n- 建议：正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量。\n\n**[Should-Fix 4] Repo-level seed 覆盖不足（2-3 seeds）**\n- 来源：R1-W2 提出，R2 AGREE\n- 详情：Repo-level 仅 2-3 seeds（vs function-level 5 seeds），variance 更大。正文 claims 读起来像 definitive 结论但仅 2-3 独立观测。\n- 建议：正文中显式标注 repo-level 分析的 seed 数和相应不确定性。\n\n**[Should-Fix 5] SESOI ±2pp 描述从 \"a priori\" 改为 \"practically motivated\"**\n- 来源：R1-W4 提出，R2 部分 AGREE\n- 详情：±2pp 依赖于 accuracy range（85-89%）和 test set size（114 problems），难以验证为纯 a priori。Appendix J sensitivity analysis 部分缓解。\n- 建议：§3.4 将 SESOI 描述从 \"set a priori\" 改为 \"practically motivated\"；引用 Appendix J sensitivity 作为 robustness check。\n\n**[Should-Fix 6] Python-only 评估未在 Limitations 提及**\n- 来源：R2-W1 提出，R1 AGREE\n- 详情：HumanEval+MBPP 和 SWE-bench 均为 Python。不同语言（Java/C++）的 test output 格式差异可能影响 CWM formal collapse rate。\n- 建议：Limitations 增加一句关于语言覆盖单一性的讨论。\n\n**[Should-Fix 7] Related Work 缺 CodeRM + ORM/PRM 映射**\n- 来源：R2-W2 提出，R1 AGREE\n- 详情：遗漏 CodeRM (Diao et al., ACL 2025 \"Dynamic Scaling of Unit Tests for Code Reward Modeling\")——研究 test-level 粒度对 reward signal 质量的影响，直接相关 CLS 设计。另需加强 CLS↔ORM / CWM↔generative verifier 的框架映射讨论。\n- 建议：验证 CodeRM 真实性后加入；加半段 ORM/PRM 映射讨论。\n\n**[Should-Fix 8] Overclaim 措辞：\"governed by\" 等**\n- 来源：R2-M1 提出，R1 AGREE\n- 详情：\"formulation choice is governed by code complexity\"（Introduction, p.1）暗示 deterministic/因果关系，但证据仅 2 complexity levels × 2-3 seeds × ≤8B models。\n- 建议：改为 \"moderated by\" 或 \"depends on\"。\n\n### Minor（不影响接收）\n\n**[Minor 1]** Figure 2 y-axis 从 55% 起始（截断），视觉上夸大 CLS-CWM gap。Caption 已标注但对快速浏览读者可能误导。考虑从 0 起始或改用差值图。[R1-M2, R2 AGREE, 视觉审查标记]\n\n**[Minor 2]** Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析。Appendix M 建议并列展示 logistic regression marginal effects。[R1-M1, R2 AGREE]\n\n**[Minor 3]** 3-shot ICL collapse to always-predict-unresolved（45.83%）是重要 negative result，但正文仅一句带过。值得增加半段讨论 fine-tuning 作为 verification 必要条件的 implication。[R2-M2, R1 AGREE]\n\n**[Minor 4]** 16 个 Appendix（A-P）导航不便。考虑加 Appendix 目录索引。[R2-M3, R1 轻度 AGREE]\n\n---\n\n## Reviewer Consensus\n\n| 议题 | 状态 | 详情 |\n|------|------|------|\n| Novelty 受限 | [AGREE] | 两人共识 Findings 合适，Main 不够 |\n| TOST 功效不足 | [AGREE] | R1 提出，R2 交叉后升级关注度 |\n| Seed 覆盖 | [AGREE] | 两人共识 repo-level 2-3 seeds 不足以支撑 definitive claims |\n| Data volume 差异 | [AGREE] | 两人共识应框架为 formulation 固有属性 |\n| Python-only | [AGREE] | 两人共识应在 Limitations 提及 |\n| SESOI a priori | [AGREE] | 两人共识改为 \"practically motivated\" |\n| Overclaim 措辞 | [AGREE] | \"governed by\" 改 \"moderated by\" |\n| CodeRM 遗漏 | [AGREE] | 验证后加入 |\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|-----|-----|-------------|\n| Checkpoint confound (R1-N1) | CRITICAL | REBUT（matched analysis 仍 20-23pp gap） | **Should-Fix**：R2 反驳有效，checkpoint 差异无法解释 18-26pp gap，但正文讨论应更显著 |\n| Scale limitation (R2-N2) | 部分 REBUT（4B→8B gap 扩大） | CRITICAL | **Should-Fix**：R1 反驳部分有效，但 ≤8B→32B 不能完全排除。Conclusion 需加限定 |\n| Exact match penalty (R1-W3) | WARNING | REBUT（relaxed matching 扩大 gap） | **Resolved**：R2 反驳成功，relaxed matching 使 gap 从 26pp 扩大到 27pp，parseable accuracy 仅 38-43%。瓶颈是语义的不是格式的 |\n| Routing 未验证 (R2-W3) | REBUT（scope 合理） | WARNING | **Minor**：R1 反驳合理——\"motivate\" 非 \"propose\"，属 future direction |\n| TRAJ 探索不充分 (R2-W4) | REBUT（scope 限定） | WARNING | **不作为 issue**：论文 scope 是比较现有 formulations，非设计新方法 |\n| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 见下方 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** 能否在正文中更显著地讨论 checkpoint 缓解证据？目前 matched epoch-3 分析和 CLS ablation 分散在 Section 3.5 半段和 Appendix O。[R1-Q1, R2 交叉中提供了证据]\n\n**Q2.** Cross-seed oracle（90.63% function / 94.27±2.59% repo）是 any-correct（任一公式正确即正确）还是 majority voting？请在正文明确标注。[R1-Q4, R2 AGREE]\n\n**Q3.** 是否尝试过不依赖 oracle 的简单 routing 启发式（如基于 input token 数或 CLS 预测置信度）？即使 negative result 也有价值。[R2-Q2]\n\n**Q4.** CLS vs CWM 的实际 wall-clock time 差异在 SWE-bench 端到端评估中有多大？Section 3.6 报告了 throughput 但未报告 wall-clock。[R2-Q5]\n\n**Q5.** 结论是否可推广到 code generation（无 buggy source 对比）场景？建议在 Limitations 讨论。[R2-Q4]\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 状态 |\n|------|------|------|\n| CodeRM (Diao et al., ACL 2025 \"Dynamic Scaling of Unit Tests for Code Reward Modeling\") | R2-W2 | 需验证真实性后加入 |\n| Cohen (1988) *Statistical Power Analysis* | R1 Missing Refs | 建议加入（power analysis 讨论） |\n| Kruschke (2013/2018) Bayesian ROPE methods | R1 Missing Refs | 可选（若补充 Bayesian equivalence test） |\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 0 warning / 10 info）。主要发现：\n\n- **Page 1-2**：前两页纯文本，无 display item。Figure 1 出现在第 3 页顶部——刚好在 3 页窗口内，但提前至第 2 页会改善审稿人第一印象。\n- **Figure 1（p.3）**：三种 formulation 对比图，caption 自包含，颜色区分清晰，信息传达有效。\n- **Page 4**：Table 1 + Table 2 同页，数据密度较高但布局紧凑合理。\n- **Figure 2（p.7）**：y-axis 从 55% 起始（截断），caption 已标注。与 R1-M2 / R2 AGREE 的审稿意见一致——建议从 0 起始或改用差值图。\n- **Page 12**：PDF 内包含 ARR Responsible NLP Research Checklist。根据 EMNLP 2026 规则，此 checklist 应在 OpenReview form 中填写，PDF 内包含不算错误但可能冗余。\n- **末页（p.23）**：约 1/3 内容 + 2/3 空白，Appendix 最后一页，影响不大。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|-------------|\n| Soundness | 3.0 | 3.5 | **3.5** — R2 REBUT 成功缓解了 R1 的 checkpoint concern；TOST 功效问题真实但不足以否定 CLS-CWM equivalence 结论（p=0.007 仍显著）。核心结论 robust。 |\n| Excitement | 3.0 | 2.5 | **2.5** — 两人共识 novelty 受限于比较已有方法。Failure mode taxonomy 有独立贡献但属增量。核心发现可从直觉预期。 |\n| Reproducibility | 4.0 | 4.0 | **4.0** — 超参数、数据构造、compute budget 报告极为详尽。 |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n\n### Overall: 3.0 — Findings\n\n**一句话判断**：方法论执行严谨、failure mode 分析有洞察力的系统比较研究，适合 Findings 而非 Main Conference。\n\n**核心理由**：\n\n1. **方法论是亮点但不足以弥补 novelty 缺口。** TOST/ICC/clustered bootstrap/Holm-Bonferroni 在 NLP 中确实罕见，但方法论规范性是\"做对了应该做的事\"，不构成 excitement 来源。核心发现（复杂任务→formulation 选择更重要，classification > generation at repo level）从直觉可预期。\n\n2. **两个 Must-Fix 问题分别影响接受度和可信度。** (a) Novelty 不足 Main——两位 Reviewer 共识；(b) TOST 功效不足使 function-level equivalence claim 从\"强支撑\"降为\"有支撑但需审慎解读\"。\n\n3. **Should-Fix 问题可修复但不改变 track。** ≤8B scale limitation（Conclusion 加限定语）、checkpoint 讨论（正文更显著）、SESOI 描述（改为 practically motivated）、Python-only（Limitations 加一句）等均为 framing/writing 层面修改，可在 revision 中解决，但不会提升 novelty 到 Main Conference 水平。\n\n4. **上调至 3.5（Borderline Conference）的条件：** (a) 补充轻量 routing/ensemble 实验，将贡献从\"比较\"提升为\"比较+方案\"；(b) 补充 Bayesian equivalence test 增强 function-level equivalence 证据；(c) 补充至少一个 ≥14B 模型的单点验证。满足其中 2/3 可考虑上调。\n\n### 修改优先级\n\n| 优先级 | 问题 | 工作量 |\n|--------|------|--------|\n| P0 | Abstract/Conclusion \"TRAJ parity differs\" 改为审慎措辞 | 极低 |\n| P0 | Conclusion 加 ≤8B LoRA 限定语 | 极低 |\n| P0 | \"governed by\" → \"moderated by\" | 极低 |\n| P1 | 正文讨论 TOST 功效限制 | 低 |\n| P1 | 正文合并讨论 checkpoint 缓解证据 | 低 |\n| P1 | SESOI \"a priori\" → \"practically motivated\" | 极低 |\n| P1 | Limitations 加 Python-only + code generation scope | 极低 |\n| P1 | TRAJ data volume/granularity 框架为 formulation 固有 | 低 |\n| P2 | 验证并加入 CodeRM + ORM/PRM 映射讨论 | 中 |\n| P2 | 正文增加 3-shot ICL collapse 讨论 | 低 |\n| P2 | Figure 2 y-axis 修改 | 低 |\n| P2 | Appendix M 补充 logistic regression | 低 |\n| P3（可选，提升 track） | 轻量 routing/ensemble 实验 | 高 |\n| P3（可选，提升 track） | Bayesian equivalence test | 中 |\n",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "report": "\n# Round 10 审稿报告\n\n**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair\n**Venue**: EMNLP 2026 via ARR (Long Paper)\n**审稿模式**: Fresh (初审)\n**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）\n\n---\n\n## Summary\n\n本文对三种 execution-free 代码修复验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）进行了首次系统性匹配比较，使用相同 base model（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、相同 LoRA 配置、相同训练数据，在 function-level 和 repo-level 两个复杂度层次上评估。核心发现是\"三层结构\"：(1) fine-tuning 必要（35-36pp 提升），(2) function-level 公式间统计等价（TOST p=0.007），(3) repo-level 下 CWM 显著退化（低于 CLS 18-26pp），driven by format collapse。论文还提供了 failure mode taxonomy 和 error complementarity 分析。\n\n---\n\n## Strengths\n\n**S1. 匹配实验框架设计在 NLP 论文中属罕见严谨。** 相同 base model、LoRA rank、optimizer、training schedule、5 seeds（function-level），DeepSeek-Coder 作为 cross-model consistency check。这是实验比较研究的标杆（Section 3.1, Table 1）。[R1-S1, R2-S1 共识]\n\n**S2. 统计方法论深度远超 NLP 领域平均。** TOST 等价检验（而非仅 NHST）、ICC-based clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 多重比较校正、mixed-effects LPM——这套工具链在 NLP 论文中极为少见（Section 3.1, 3.4, Appendix A/J/M）。[R1-S2, R2-S1 共识]\n\n**S3. Failure mode taxonomy 有独立实用价值。** Format collapse / decision collapse / aggregation penalty 三类 failure modes 有定量分析和定性例证（Section 3.5, Table 4, Appendix H），为从业者选择 formulation 提供可操作指导。[R1-S3, R2-S3 共识]\n\n**S4. Error complementarity 发现有 ensemble/routing 研究价值。** Oracle combination 90.63%（function）/ 95.83%（repo），证明公式犯互补错误。Cross-seed oracle 94.27±2.59% 确认跨 seed 稳定性（Section 3.6）。[R2-S4]\n\n**S5. 附录极其详尽且自我批评诚实。** 16 个 Appendix（14 页）覆盖全部 ablation、convergence、power analysis、prompt templates、qualitative errors。Limitations 和 Threats to Validity 主动识别并讨论多个潜在问题。[R1-S4/S5, R2-S5 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[Must-Fix 1] Novelty 受限：核心贡献为比较已有 formulations，excitement 不足 main conference**\n- 来源：R2-N1 提出，R1 AGREE\n- 详情：三种 formulation 均为已有方法（CLS: Ni et al. 2023; CWM: FAIR 2025; TRAJ: Shum et al. 2025）。核心发现\"复杂任务→公式选择更重要\"数据支撑充分但从直觉可预期。论文描述了 what happens 但缺少深层 why 的理论理解——为什么恰好在 repo level 而非某个中间复杂度出现分歧？\"三层结构\"是描述性的而非解释性的。\n- 影响：两位 Reviewer 共识 Excitement 2.5-3.0/5，一致认为 Findings 合适但 Main 不够。\n- 建议：(a) 增加轻量 routing/ensemble 实验将贡献从\"比较\"提升为\"比较+方案\"；(b) 或提供 complexity threshold 的理论分析。\n\n**[Must-Fix 2] TOST 统计功效不足，CLS-TRAJ 等价性无法确认**\n- 来源：R1-N2 提出，R2 AGREE（交叉分享后升级关注度）\n- 详情：n_eff ≈ 86，TOST 对 medium effect size 功效仅 ~0.3（70% 概率将真实中等差异误判为等价）。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。Abstract \"TRAJ parity differs between the two tested families\" 措辞不够精确——实际是等价检验功效不足、无法下结论，而非 TRAJ 显著不等价。\n- 建议：(a) 正文讨论 TOST 功效限制（目前仅 Appendix J/K）；(b) Abstract 措辞改为\"TRAJ equivalence could not be confirmed after multiple comparison correction\"；(c) 考虑补充 Bayesian equivalence test（ROPE-based）。\n\n### Should-Fix（影响评分但不一票否决）\n\n**[Should-Fix 1] ≤8B LoRA 规模限制——Conclusion 缺少限定语**\n- 来源：R2-N2 提出 CRITICAL，R1 部分 REBUT（4B→8B gap 扩大数据反驳纯容量假说）\n- Director 裁定：降为 Should-Fix。R1 反驳有效——4B→8B 时 CLS-CWM gap 从 1.32pp 扩大到 2.62pp（Figure 2），说明增加参数量不缩小差距。且 Appendix I qualitative analysis 表明 format collapse 源于 output format complexity（formulation 固有属性）。但 ≤8B→32B 跨越量级不同，不能完全排除。Abstract 已有\"≤8B LoRA protocol\"限定，但 Conclusion 和部分正文 claims 仍缺。\n- 建议：Conclusion 加入 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化。\n\n**[Should-Fix 2] Checkpoint selection 混杂——正文讨论不够显著**\n- 来源：R1-N1 标 CRITICAL，R2 REBUT\n- Director 裁定：降为 Should-Fix。R2 反驳有效——Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp range（val-selected 反而最低）。Checkpoint 差异无法解释 18-26pp gap。但缓解证据分散在 Section 3.5 半段和 Appendix O，正文应更显著讨论。\n- 建议：正文中合并讨论 checkpoint 缓解证据（matched epoch-3 gap + CLS ablation range），而非仅依赖 Appendix。\n\n**[Should-Fix 3] 训练数据量差异（CLS ~70K vs TRAJ ~386）+ 信号粒度不同**\n- 来源：R1-W1 提出，R2 AGREE\n- 详情：~180× 数据量差异。Downsampling ablation 控制了 volume（CLS 80.74% vs TRAJ 72.92%，仍高 7.82pp）但未控制 signal granularity（per-test vs variant-level）。两人共识：应将此框架为 formulation 固有属性。\n- 建议：正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量。\n\n**[Should-Fix 4] Repo-level seed 覆盖不足（2-3 seeds）**\n- 来源：R1-W2 提出，R2 AGREE\n- 详情：Repo-level 仅 2-3 seeds（vs function-level 5 seeds），variance 更大。正文 claims 读起来像 definitive 结论但仅 2-3 独立观测。\n- 建议：正文中显式标注 repo-level 分析的 seed 数和相应不确定性。\n\n**[Should-Fix 5] SESOI ±2pp 描述从 \"a priori\" 改为 \"practically motivated\"**\n- 来源：R1-W4 提出，R2 部分 AGREE\n- 详情：±2pp 依赖于 accuracy range（85-89%）和 test set size（114 problems），难以验证为纯 a priori。Appendix J sensitivity analysis 部分缓解。\n- 建议：§3.4 将 SESOI 描述从 \"set a priori\" 改为 \"practically motivated\"；引用 Appendix J sensitivity 作为 robustness check。\n\n**[Should-Fix 6] Python-only 评估未在 Limitations 提及**\n- 来源：R2-W1 提出，R1 AGREE\n- 详情：HumanEval+MBPP 和 SWE-bench 均为 Python。不同语言（Java/C++）的 test output 格式差异可能影响 CWM formal collapse rate。\n- 建议：Limitations 增加一句关于语言覆盖单一性的讨论。\n\n**[Should-Fix 7] Related Work 缺 CodeRM + ORM/PRM 映射**\n- 来源：R2-W2 提出，R1 AGREE\n- 详情：遗漏 CodeRM (Diao et al., ACL 2025 \"Dynamic Scaling of Unit Tests for Code Reward Modeling\")——研究 test-level 粒度对 reward signal 质量的影响，直接相关 CLS 设计。另需加强 CLS↔ORM / CWM↔generative verifier 的框架映射讨论。\n- 建议：验证 CodeRM 真实性后加入；加半段 ORM/PRM 映射讨论。\n\n**[Should-Fix 8] Overclaim 措辞：\"governed by\" 等**\n- 来源：R2-M1 提出，R1 AGREE\n- 详情：\"formulation choice is governed by code complexity\"（Introduction, p.1）暗示 deterministic/因果关系，但证据仅 2 complexity levels × 2-3 seeds × ≤8B models。\n- 建议：改为 \"moderated by\" 或 \"depends on\"。\n\n### Minor（不影响接收）\n\n**[Minor 1]** Figure 2 y-axis 从 55% 起始（截断），视觉上夸大 CLS-CWM gap。Caption 已标注但对快速浏览读者可能误导。考虑从 0 起始或改用差值图。[R1-M2, R2 AGREE, 视觉审查标记]\n\n**[Minor 2]** Mixed-effects model 使用 LPM 而非 logistic regression 作为主分析。Appendix M 建议并列展示 logistic regression marginal effects。[R1-M1, R2 AGREE]\n\n**[Minor 3]** 3-shot ICL collapse to always-predict-unresolved（45.83%）是重要 negative result，但正文仅一句带过。值得增加半段讨论 fine-tuning 作为 verification 必要条件的 implication。[R2-M2, R1 AGREE]\n\n**[Minor 4]** 16 个 Appendix（A-P）导航不便。考虑加 Appendix 目录索引。[R2-M3, R1 轻度 AGREE]\n\n---\n\n## Reviewer Consensus\n\n| 议题 | 状态 | 详情 |\n|------|------|------|\n| Novelty 受限 | [AGREE] | 两人共识 Findings 合适，Main 不够 |\n| TOST 功效不足 | [AGREE] | R1 提出，R2 交叉后升级关注度 |\n| Seed 覆盖 | [AGREE] | 两人共识 repo-level 2-3 seeds 不足以支撑 definitive claims |\n| Data volume 差异 | [AGREE] | 两人共识应框架为 formulation 固有属性 |\n| Python-only | [AGREE] | 两人共识应在 Limitations 提及 |\n| SESOI a priori | [AGREE] | 两人共识改为 \"practically motivated\" |\n| Overclaim 措辞 | [AGREE] | \"governed by\" 改 \"moderated by\" |\n| CodeRM 遗漏 | [AGREE] | 验证后加入 |\n\n## Reviewer Divergence\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|-----|-----|-------------|\n| Checkpoint confound (R1-N1) | CRITICAL | REBUT（matched analysis 仍 20-23pp gap） | **Should-Fix**：R2 反驳有效，checkpoint 差异无法解释 18-26pp gap，但正文讨论应更显著 |\n| Scale limitation (R2-N2) | 部分 REBUT（4B→8B gap 扩大） | CRITICAL | **Should-Fix**：R1 反驳部分有效，但 ≤8B→32B 不能完全排除。Conclusion 需加限定 |\n| Exact match penalty (R1-W3) | WARNING | REBUT（relaxed matching 扩大 gap） | **Resolved**：R2 反驳成功，relaxed matching 使 gap 从 26pp 扩大到 27pp，parseable accuracy 仅 38-43%。瓶颈是语义的不是格式的 |\n| Routing 未验证 (R2-W3) | REBUT（scope 合理） | WARNING | **Minor**：R1 反驳合理——\"motivate\" 非 \"propose\"，属 future direction |\n| TRAJ 探索不充分 (R2-W4) | REBUT（scope 限定） | WARNING | **不作为 issue**：论文 scope 是比较现有 formulations，非设计新方法 |\n| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 见下方 |\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** 能否在正文中更显著地讨论 checkpoint 缓解证据？目前 matched epoch-3 分析和 CLS ablation 分散在 Section 3.5 半段和 Appendix O。[R1-Q1, R2 交叉中提供了证据]\n\n**Q2.** Cross-seed oracle（90.63% function / 94.27±2.59% repo）是 any-correct（任一公式正确即正确）还是 majority voting？请在正文明确标注。[R1-Q4, R2 AGREE]\n\n**Q3.** 是否尝试过不依赖 oracle 的简单 routing 启发式（如基于 input token 数或 CLS 预测置信度）？即使 negative result 也有价值。[R2-Q2]\n\n**Q4.** CLS vs CWM 的实际 wall-clock time 差异在 SWE-bench 端到端评估中有多大？Section 3.6 报告了 throughput 但未报告 wall-clock。[R2-Q5]\n\n**Q5.** 结论是否可推广到 code generation（无 buggy source 对比）场景？建议在 Limitations 讨论。[R2-Q4]\n\n---\n\n## Missing References\n\n| 引用 | 来源 | 状态 |\n|------|------|------|\n| CodeRM (Diao et al., ACL 2025 \"Dynamic Scaling of Unit Tests for Code Reward Modeling\") | R2-W2 | 需验证真实性后加入 |\n| Cohen (1988) *Statistical Power Analysis* | R1 Missing Refs | 建议加入（power analysis 讨论） |\n| Kruschke (2013/2018) Bayesian ROPE methods | R1 Missing Refs | 可选（若补充 Bayesian equivalence test） |\n\n---\n\n## External Review\n\n外部审稿：未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 0 warning / 10 info）。主要发现：\n\n- **Page 1-2**：前两页纯文本，无 display item。Figure 1 出现在第 3 页顶部——刚好在 3 页窗口内，但提前至第 2 页会改善审稿人第一印象。\n- **Figure 1（p.3）**：三种 formulation 对比图，caption 自包含，颜色区分清晰，信息传达有效。\n- **Page 4**：Table 1 + Table 2 同页，数据密度较高但布局紧凑合理。\n- **Figure 2（p.7）**：y-axis 从 55% 起始（截断），caption 已标注。与 R1-M2 / R2 AGREE 的审稿意见一致——建议从 0 起始或改用差值图。\n- **Page 12**：PDF 内包含 ARR Responsible NLP Research Checklist。根据 EMNLP 2026 规则，此 checklist 应在 OpenReview form 中填写，PDF 内包含不算错误但可能冗余。\n- **末页（p.23）**：约 1/3 内容 + 2/3 空白，Appendix 最后一页，影响不大。\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|-----|-----|-------------|\n| Soundness | 3.0 | 3.5 | **3.5** — R2 REBUT 成功缓解了 R1 的 checkpoint concern；TOST 功效问题真实但不足以否定 CLS-CWM equivalence 结论（p=0.007 仍显著）。核心结论 robust。 |\n| Excitement | 3.0 | 2.5 | **2.5** — 两人共识 novelty 受限于比较已有方法。Failure mode taxonomy 有独立贡献但属增量。核心发现可从直觉预期。 |\n| Reproducibility | 4.0 | 4.0 | **4.0** — 超参数、数据构造、compute budget 报告极为详尽。 |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n| Confidence | 4.0 | 4.0 | **4.0** |\n\n### Overall: 3.0 — Findings\n\n**一句话判断**：方法论执行严谨、failure mode 分析有洞察力的系统比较研究，适合 Findings 而非 Main Conference。\n\n**核心理由**：\n\n1. **方法论是亮点但不足以弥补 novelty 缺口。** TOST/ICC/clustered bootstrap/Holm-Bonferroni 在 NLP 中确实罕见，但方法论规范性是\"做对了应该做的事\"，不构成 excitement 来源。核心发现（复杂任务→formulation 选择更重要，classification > generation at repo level）从直觉可预期。\n\n2. **两个 Must-Fix 问题分别影响接受度和可信度。** (a) Novelty 不足 Main——两位 Reviewer 共识；(b) TOST 功效不足使 function-level equivalence claim 从\"强支撑\"降为\"有支撑但需审慎解读\"。\n\n3. **Should-Fix 问题可修复但不改变 track。** ≤8B scale limitation（Conclusion 加限定语）、checkpoint 讨论（正文更显著）、SESOI 描述（改为 practically motivated）、Python-only（Limitations 加一句）等均为 framing/writing 层面修改，可在 revision 中解决，但不会提升 novelty 到 Main Conference 水平。\n\n4. **上调至 3.5（Borderline Conference）的条件：** (a) 补充轻量 routing/ensemble 实验，将贡献从\"比较\"提升为\"比较+方案\"；(b) 补充 Bayesian equivalence test 增强 function-level equivalence 证据；(c) 补充至少一个 ≥14B 模型的单点验证。满足其中 2/3 可考虑上调。\n\n### 修改优先级\n\n| 优先级 | 问题 | 工作量 |\n|--------|------|--------|\n| P0 | Abstract/Conclusion \"TRAJ parity differs\" 改为审慎措辞 | 极低 |\n| P0 | Conclusion 加 ≤8B LoRA 限定语 | 极低 |\n| P0 | \"governed by\" → \"moderated by\" | 极低 |\n| P1 | 正文讨论 TOST 功效限制 | 低 |\n| P1 | 正文合并讨论 checkpoint 缓解证据 | 低 |\n| P1 | SESOI \"a priori\" → \"practically motivated\" | 极低 |\n| P1 | Limitations 加 Python-only + code generation scope | 极低 |\n| P1 | TRAJ data volume/granularity 框架为 formulation 固有 | 低 |\n| P2 | 验证并加入 CodeRM + ORM/PRM 映射讨论 | 中 |\n| P2 | 正文增加 3-shot ICL collapse 讨论 | 低 |\n| P2 | Figure 2 y-axis 修改 | 低 |\n| P2 | Appendix M 补充 logistic regression | 低 |\n| P3（可选，提升 track） | 轻量 routing/ensemble 实验 | 高 |\n| P3（可选，提升 track） | Bayesian equivalence test | 中 |\n",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-22T16:00:53.186613+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_061c4b1115e483e8fdad01cae91c873a:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4673
}
```

</details>

---


### Assistant

_source line 828 · 2026-05-22T16:01:10.243988+00:00_

审稿报告已投递至 Research Director。

**Round 10 审稿完成。**

| 项目 | 结果 |
|------|------|
| Overall | **3.0 (Findings)** |
| Soundness | 3.5 |
| Excitement | 2.5 |
| Reproducibility | 4.0 |
| Confidence | 4.0 |
| Must-Fix | 2 个（novelty 受限 + TOST 功效不足） |
| Should-Fix | 8 个（scale qualifier / checkpoint 讨论 / data volume framing / seed 标注 / SESOI 措辞 / Python-only / CodeRM / overclaim） |
| Minor | 4 个 |
| Reviewer 共识 | 8 项 AGREE |
| Reviewer 分歧 | 5 项（均已 Director 裁定） |
| 视觉审查 | 0 critical / 0 warning / 10 info |
| 外部审稿 | 未启用 |
| Issue Tracker | 已同步（R10 新增 4 issues，resolved 6 issues） |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 73

## Round 73

2 recorded events


### User

_source line 829 · 2026-05-22T16:01:12.787860+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Director。

核心判断：
- **R1-N1 (checkpoint confound)**：REBUT——论文 Section 3.5 的匹配 checkpoint 分析和 Appendix O 的早停实验表明，即使控制 checkpoint，CLS-CWM gap 仍为 ~20-23pp，核心结论 robust
- **R1-N2 (TOST power)**：AGREE——功效不足，abstract 措辞应更审慎
- **R1-W3 (string matching penalty)**：REBUT——Appendix I 证明宽松匹配不改变结论，可解析输出语义准确率仍然低
- 其余 W1/W2/W4/M1/M2：基本 AGREE，属合理的方法论建议
- 评分分歧：我维持 Overall 3.0 (Findings) vs R1 的 3.5 (Borderline Conference)，核心原因是 novelty 和 excitement 不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 830 · 2026-05-22T16:01:41.457301+00:00_

审稿报告已投递至 Research Director。

**Round 10 审稿总结：**

- **Overall: 3.0（Findings）** — R1 评 3.5（Borderline Conference），R2 评 3.0（Findings），Director 综合 3.0
- **2 个 Must-Fix**：(1) Novelty 受限于比较已有方法，excitement 不足 Main；(2) TOST 功效 ~0.3，Abstract "TRAJ parity differs" 措辞需更审慎
- **8 个 Should-Fix**：≤8B 限定语、checkpoint 正文讨论、数据量差异框架、seed 标注、SESOI 描述、Python-only、CodeRM 引用、overclaim 措辞
- **4 个 Minor**：Figure 2 y-axis、LPM→logistic regression、3-shot collapse 讨论、Appendix 索引
- **上调至 3.5 条件**：补充 routing 实验 + Bayesian equivalence test + ≥14B 单点验证（满足 2/3）

Issue Tracker 已同步（新增 3 个 R10 issues，更新 15 个现有 issues，新 resolved 6 个）。视觉审查完成（0 critical / 0 warning / 10 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 74

## Round 74

40 recorded events


### User

_source line 831 · 2026-05-23T02:56:16.675648+00:00_

[Round 9 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/exec-sim-repair-verifier/artifacts/review_reports/round_8.md`
跨轮次问题追踪: `projects/exec-sim-repair-verifier/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: exec-sim-repair-verifier
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-23T02:56:42.023956+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "artifacts/review_reports/round_8.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "artifacts/review_reports/round_8.md"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-23T02:56:42.425913+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_reports/round_8.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-23T02:56:42.426355+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 835 · 2026-05-23T02:56:42.527166+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 836 · 2026-05-23T02:56:49.704334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 837 · 2026-05-23T02:56:50.157263+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 6
12	  last_seen_round: 10
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	    - round: 10
27	      reviewers: [1, 2]
28	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
29	  action_items:
30	    - round: 6
31	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
32	      assigned_to: "paper"
33	      status: resolved
34	    - round: 9
35	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
36	      assigned_to: "paper"
37	      status: in_progress
38	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. R10 §5.4 已加 'Variant-level comparisons rely on limited seed coverage' 声明。Agent 正在补充 exploratory 标注。"
39	  resolution_round: null
40	
41	- id: "R6-N2"
42	  summary: "Checkpoint selection 系统性偏向 CLS"
43	  category: method
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 6
47	  last_seen_round: 10
48	  mentions:
49	    - ro
…[truncated 24380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 838 · 2026-05-23T02:56:50.258080+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 839 · 2026-05-23T02:56:50.308996+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_8.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 840 · 2026-05-23T02:57:12.625744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 841 · 2026-05-23T02:57:12.977894+00:00_

1	\begin{abstract}
2	LLM-based program repair increasingly leverages test-time compute scaling, generating multiple candidate patches and selecting the best via a verifier. Execution-based verification is reliable but expensive; three execution-free alternatives have emerged: per-test binary classification (\cls{}), execution output generation (\cwm{}), and trajectory-level patch scoring (\traj{}). No prior work compares these formulations under matched conditions.
3	
4	We present the first systematic comparison across two representative code LLM families (Qwen3, DeepSeek-Coder), two complexity levels, and multiple seeds under ${\leq}$8B LoRA fine-tuning. At function level, \cls{} and \cwm{} are statistically equivalent across both families (TOST, 5 seeds): classification is not inherently easier than generation when outputs are short. \traj{} parity is model-dependent and not confirmed after multiple comparison correction. At repository level, a significant interaction ($z{=}-23.7$, DeepSeek-Coder) confirms this equivalence collapses: the \cls{}--\cwm{} gap widens to 18--26\pp{} across 2--3 seeds per model under our ${\leq}$8B LoRA protocol in variant-level evaluation, driven by format collapse in generation-based simulation. Gap magnitude depends on multiple confounds. Exploratory 14B results (single seed) show the function-level gap narrowing to near-zero ($-$0.05\pp{}), suggesting capacity-dependent convergence.
5	
6	Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection.
7	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 842 · 2026-05-23T02:57:12.978245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-23T02:57:13.029024+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Datasets.}
10	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
12	
13	\paragraph{Models and training.}
14	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency chec
…[truncated 19073 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-23T02:59:47.688834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-23T02:59:47.940865+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 6
12	  last_seen_round: 10
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	    - round: 10
27	      reviewers: [1, 2]
28	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
29	  action_items:
30	    - round: 6
31	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
32	      assigned_to: "paper"
33	      status: resolved
34	    - round: 9
35	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
36	      assigned_to: "paper"
37	      status: in_progress
38	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. R10 §5.4 已加 'Variant-level comparisons rely on limited seed coverage' 声明。Agent 正在补充 exploratory 标注。"
39	  resolution_round: null
40	
41	- id: "R6-N2"
42	  summary: "Checkpoint selection 系统性偏向 CLS"
43	  category: method
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 6
47	  last_seen_round: 10
48	  mentions:
49	    - ro
…[truncated 24380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-23T02:59:48.091968+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/",
  "description": "List review report files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/",
    "description": "List review report files"
  }
}
```

</details>

---


### Tool result

_source line 847 · 2026-05-23T02:59:48.243008+00:00_

total 148
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 16:00 .
drwxr-xr-x 29 ubuntu ubuntu 12288 May 23 02:56 ..
-rw-r--r--  1 ubuntu ubuntu 11526 May 18 18:22 round_1.md
-rw-r--r--  1 ubuntu ubuntu 13790 May 19 03:04 round_2.md
-rw-r--r--  1 ubuntu ubuntu 14120 May 19 08:41 round_3.md
-rw-r--r--  1 ubuntu ubuntu 19343 May 19 09:57 round_4.md
-rw-r--r--  1 ubuntu ubuntu 16304 May 19 11:21 round_5.md
-rw-r--r--  1 ubuntu ubuntu 16822 May 22 14:08 round_6.md
-rw-r--r--  1 ubuntu ubuntu 14248 May 22 15:09 round_7.md
-rw-r--r--  1 ubuntu ubuntu 15882 May 22 16:00 round_8.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 848 · 2026-05-23T03:00:24.392303+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_post_to_reviewer,dispatch_visual_check,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_post_to_reviewer,dispatch_visual_check,get_visual_check_status,update_review_issues,submit_review_report_to_research_director,read_project_file",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-23T03:00:24.443008+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-23T03:00:27.755844+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "director_post_to_reviewer",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "director_post_to_reviewer",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 851 · 2026-05-23T03:00:27.806421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 852 · 2026-05-23T03:00:30.902125+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 853 · 2026-05-23T03:00:30.902581+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 854 · 2026-05-23T03:00:34.713131+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "dispatch visual check",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "dispatch visual check",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-23T03:00:34.763703+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-23T03:00:58.866016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16 && git log --oneline -10",
  "description": "Check recent commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16 && git log --oneline -10",
    "description": "Check recent commits"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-23T03:00:58.966873+00:00_

Exit code 128
fatal: not a git repository (or any of the parent directories): .git

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-23T03:01:02.185478+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier && git log --oneline -10",
  "description": "Check recent commits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier && git log --oneline -10",
    "description": "Check recent commits"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-23T03:01:02.236133+00:00_

0b38a2b Fix model identity over-strong significance claims (LPM vs GEE)
495f5e1 Fix model identity over-strong significance claims (LPM vs GEE)
d6fdd5a Bayesian ROPE, logistic regression robustness, Figure 2 y-axis fix, exploratory annotation
55aa8ee Add routing heuristic negative result to error complementarity section
a58c178 Round 10: TOST power, TRAJ wording, ≤8B qualifier, checkpoint evidence, data volume, CodeRM+ORM/PRM, governed→moderated, ICL expansion, appendix TOC, oracle def, wall-clock, Python-only+codegen limitations
b20ac87 fix abstract grammar + conclusion consistency with abstract wording
4871ab7 M1-M7+Q4: logistic regression note, fig3 y-axis, leverages, n_eff≈86, checklist update, cross-seed oracle
b9593e3 W1-W6: formulation variance clarification, CWM output fix, contributions merge, NaN explanation
840a17c C1+C2: SESOI a priori/post-hoc separation, title rename, design space→landscape
8e1d4bd compress §5.2/§5.5/conclusion to fit 8-page main text limit
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/.claude/sessions/review_director_06def7c3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-23T03:01:16.042686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "limit": "80",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "limit": "80",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-23T03:01:16.043308+00:00_

0	\section{Experiments}
1	\label{sec:experiments}
2	
3	We systematically compare \cls{}, \cwm{}, and \traj{} across two representative code LLM families, two complexity levels, and multiple seeds to characterize the formulation landscape for neural code verification.
4	
5	\subsection{Experimental Setup}
6	\label{sec:setup}
7	
8	\paragraph{Datasets.}
9	\emph{Function-level}: mutated variants from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} (five mutation types), labels verified by execution. 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
10	\emph{Repo-level}: per-test instances from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants. ${\sim}$70K training samples; val ($n{=}9{,}335$) and test ($n{=}9{,}784$) have zero problem overlap (majority baseline 72.96\%). Val-based checkpoint selection follows standard practice~\cite{jimenez2024swebench} where validation loss is computable; runs using truncate preprocessing produce NaN validation loss because repo-level execution traces often exceed the 2,048-token sequence length limit; after truncation, many samples have all target tokens removed (labels entirely $-$100), producing degenerate loss---a formulation-inherent weakness that classification and trajectory formulations avoid by design. NaN loss defaults to the final epoch checkpoint (affects DeepSeek \cls{} s123, all \cwm{} runs, and Qwen3 \traj{} runs; see Appendix~\ref{app:hyperparams}).
11	
12	\paragraph{Models and training.}
13	We fine-tune Qwen3-4B and Qwen3-8B~\cite{qwen2025qwen3} with Low-Rank Adaptation (LoRA)~\cite{hu2022lora} (rank 16, 3 epochs) across five seeds. Seeds 42/123/456 use bfloat16; seeds 789/0 use NormalFloat 4-bit (NF4) quantization~\cite{dettmers2024qlora} to test robustness to precision reduction (function-level accuracy remains within seed noise across both precisions; see footnote in \S\ref{sec:equivalence}). As a cross-model consistency check
…[truncated 5084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-23T03:01:20.612252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "limit": "120",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "limit": "120",
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-23T03:01:20.713781+00:00_

80	\multirow{3}{*}{\cls{}} & 4B & 87.83 & 89.52 & \textbf{88.68} & --- \\
81	 & 8B & \textbf{90.48} & 89.40 & \textbf{89.94} & +1.27 \\
82	 & 14B & 89.21 & --- & 89.21\textsuperscript{$\dagger$} & $-$0.73 \\
83	\midrule
84	\multirow{3}{*}{\cwm{}} & 4B & 87.51 & 87.20 & \underline{87.36} & --- \\
85	 & 8B & 87.67 & 86.98 & 87.33 & $-$0.03 \\
86	 & 14B & 89.26 & --- & 89.26\textsuperscript{$\dagger$} & +1.93 \\
87	\midrule
88	\multirow{3}{*}{\traj{}} & 4B & 85.66 & 85.47 & 85.57 & --- \\
89	 & 8B & 87.60 & 87.79 & \underline{87.70} & +2.13 \\
90	 & 14B & --- & --- & --- & --- \\
91	\bottomrule
92	\multicolumn{6}{l}{\footnotesize\textsuperscript{$\dagger$}Single seed (42); exploratory.}
93	\end{tabular}
94	\end{table}
95	
96	\cls{} and \traj{} both scale positively from 4B to 8B (+1.27\pp{} and +2.13\pp{} respectively), while \cwm{} remains flat ($-$0.03\pp{}). At 8B, the ranking is \cls{} (89.94) $>$ \traj{} (87.70) $>$ \cwm{} (87.33). The \cls{}--\cwm{} gap widens from 1.32\pp{} at 4B to 2.62\pp{} at 8B (Figure~\ref{fig:scaling_gap}); clustered bootstrap on the 3-seed superset (42, 123, 456 for \cls{}/\cwm{}) yields $p = 0.0066$ (95\% CI $[1.80, 2.71]$), which confirms the widening is not a sampling artifact.
97	
98	At 14B (single seed; exploratory), \cls{} reaches 89.21\% ($-$0.73\pp{}) while \cwm{} reaches 89.26\% ($+$1.93\pp{}), closing the gap from 2.62\pp{} at 8B to $-$0.05\pp{}---effectively zero. \cwm{}'s delayed scaling onset (flat 4B$\to$8B, then $+$1.93\pp{} at 14B) suggests a capacity threshold for output formatting, rather than a fundamental formulation limitation. Under matched precision (bfloat16 or NF4), the 14B gap remains $<$0.3\pp{}, confirming convergence is robust to quantization. These single-seed results require multi-seed confirmation.
99	
100	\paragraph{Baseline scaling.} Under NF4 quantization, prompting baselines show a scale$\times$few-shot interaction: Qwen3-8B gains nothing from demonstrations ($\Delta{=}-0.11\pp{}$), while 14B gains $+6.
…[truncated 12061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-23T03:02:03.119013+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 9 继续审稿 — Reviewer 1 任务\n\n**模式**: 继续审稿（非初审）。论文已根据上轮审稿意见修改，你的任务是逐条验证 open/in_progress 问题是否充分解决，并检查修改是否引入新问题。\n\n**Venue**: EMNLP 2026 (ARR Long Paper, 8页正文限制, deadline 2026-05-25)\n\n**你的侧重**: 统计方法论 + 实验严谨性\n\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_9/submitted.pdf`\n\n### 上轮以来的关键修改（commits d6fdd5a, 55aa8ee, 0b38a2b）\n\n1. **14B 探索性结果**：Table 2 新增 14B 行 (CLS 89.21%, CWM 89.26%, gap ≈ 0)，标注 \"single seed; exploratory\"\n2. **Bayesian ROPE**：§3.4 新增段落引用 Appendix Bayesian ROPE 分析 (P(ROPE)=0.975 for CLS-CWM)\n3. **TOST 功效讨论**：§3.4 新增 \"Statistical power\" 段落 (n_eff≈86, power~0.3)\n4. **Variant-level 标注**：§3.5 开头标注 \"exploratory due to limited seed coverage\"\n5. **Routing 负结果**：§3.6 error complementarity 部分加入 \"Simple routing heuristics capture <0.4pp of the oracle gap\"\n6. **Checkpoint 证据整合**：§3.6 \"Why does generation degrade\" 段落整合 matched epoch-3 gaps 20-23pp + CLS ablation <1pp\n7. **ICL collapse 扩展**：§3.5 加入 \"establishing that execution-free verification requires task-specific fine-tuning regardless of formulation\"\n8. **Wall-clock 时间**：48ms vs 16.3s per inference\n9. **Figure 2 y-axis 修复**：commit d6fdd5a 提及修复\n10. **Logistic regression robustness**：commit 0b38a2b 修复 model identity 过强显著性声明 (LPM vs GEE)\n11. **Exploratory 标注**：commit d6fdd5a 提及 exploratory annotation\n\n### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由的 Issue 列表\n\n**[CRITICAL] R6-N1** — Repo-level 核心 claims 基于 limited seeds，variant-level 分析需标注为 exploratory/descriptive\n- 上轮状态: in_progress\n- 待验证: §3.5 开头是否有明确 exploratory 标注；variant-level 比较是否避免了 causal claims\n\n**[WARNING] R8-W1** — TOST 统计功效不足 (n_eff≈86, power~0.3)\n- 上轮状态: in_progress\n- 待验证: §3.4 是否有 Statistical power 段落讨论功效限制；Bayesian ROPE 引用是否充分补充 TOST；Abstract 措辞是否已足够审慎 (\"not confirmed after multiple comparison correction\")\n\n**[INFO] R8-M2** — LPM 未报告 robust SEs; 建议并列展示 logistic regression\n- 上轮状态: in_progress\n- 待验证: Appendix M 是否补充了 logistic regression 或 odds ratios；commit 0b38a2b (LPM vs GEE) 是否解决了过强显著性声明\n\n**[INFO] R6-M3** — Figure 2 y-axis 不从零开始\n- 上轮状态: in_progress\n- 待验证: commit d6fdd5a 提及 Figure 2 y-axis fix，实际效果如何\n\n### 额外检查\n\n- 14B 结果的统计表述是否恰当（single seed 限制是否充分声明）\n- Bayesian ROPE 分析的方法论是否规范（prior 选择、ROPE 区间设定）\n- 修改是否引入新问题（过度 hedging、前后措辞不一致等）\n\n### 输出格式\n\n对每个 issue：\n```\n**[R6-N1]** [RESOLVED] / [STILL_OPEN]\n理由: ...\n```\n\n最后给出：\n- 新发现的问题（如有）\n- 整体评分建议（EMNLP 2026 标准：5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings）\n- Soundness / Excitement / Overall 分项评分",
  "reviewer_id": "1",
  "round_number": "9"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 9 继续审稿 — Reviewer 1 任务\n\n**模式**: 继续审稿（非初审）。论文已根据上轮审稿意见修改，你的任务是逐条验证 open/in_progress 问题是否充分解决，并检查修改是否引入新问题。\n\n**Venue**: EMNLP 2026 (ARR Long Paper, 8页正文限制, deadline 2026-05-25)\n\n**你的侧重**: 统计方法论 + 实验严谨性\n\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_9/submitted.pdf`\n\n### 上轮以来的关键修改（commits d6fdd5a, 55aa8ee, 0b38a2b）\n\n1. **14B 探索性结果**：Table 2 新增 14B 行 (CLS 89.21%, CWM 89.26%, gap ≈ 0)，标注 \"single seed; exploratory\"\n2. **Bayesian ROPE**：§3.4 新增段落引用 Appendix Bayesian ROPE 分析 (P(ROPE)=0.975 for CLS-CWM)\n3. **TOST 功效讨论**：§3.4 新增 \"Statistical power\" 段落 (n_eff≈86, power~0.3)\n4. **Variant-level 标注**：§3.5 开头标注 \"exploratory due to limited seed coverage\"\n5. **Routing 负结果**：§3.6 error complementarity 部分加入 \"Simple routing heuristics capture <0.4pp of the oracle gap\"\n6. **Checkpoint 证据整合**：§3.6 \"Why does generation degrade\" 段落整合 matched epoch-3 gaps 20-23pp + CLS ablation <1pp\n7. **ICL collapse 扩展**：§3.5 加入 \"establishing that execution-free verification requires task-specific fine-tuning regardless of formulation\"\n8. **Wall-clock 时间**：48ms vs 16.3s per inference\n9. **Figure 2 y-axis 修复**：commit d6fdd5a 提及修复\n10. **Logistic regression robustness**：commit 0b38a2b 修复 model identity 过强显著性声明 (LPM vs GEE)\n11. **Exploratory 标注**：commit d6fdd5a 提及 exploratory annotation\n\n### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由的 Issue 列表\n\n**[CRITICAL] R6-N1** — Repo-level 核心 claims 基于 limited seeds，variant-level 分析需标注为 exploratory/descriptive\n- 上轮状态: in_progress\n- 待验证: §3.5 开头是否有明确 exploratory 标注；variant-level 比较是否避免了 causal claims\n\n**[WARNING] R8-W1** — TOST 统计功效不足 (n_eff≈86, power~0.3)\n- 上轮状态: in_progress\n- 待验证: §3.4 是否有 Statistical power 段落讨论功效限制；Bayesian ROPE 引用是否充分补充 TOST；Abstract 措辞是否已足够审慎 (\"not confirmed after multiple comparison correction\")\n\n**[INFO] R8-M2** — LPM 未报告 robust SEs; 建议并列展示 logistic regression\n- 上轮状态: in_progress\n- 待验证: Appendix M 是否补充了 logistic regression 或 odds ratios；commit 0b38a2b (LPM vs GEE) 是否解决了过强显著性声明\n\n**[INFO] R6-M3** — Figure 2 y-axis 不从零开始\n- 上轮状态: in_progress\n- 待验证: commit d6fdd5a 提及 Figure 2 y-axis fix，实际效果如何\n\n### 额外检查\n\n- 14B 结果的统计表述是否恰当（single seed 限制是否充分声明）\n- Bayesian ROPE 分析的方法论是否规范（prior 选择、ROPE 区间设定）\n- 修改是否引入新问题（过度 hedging、前后措辞不一致等）\n\n### 输出格式\n\n对每个 issue：\n```\n**[R6-N1]** [RESOLVED] / [STILL_OPEN]\n理由: ...\n```\n\n最后给出：\n- 新发现的问题（如有）\n- 整体评分建议（EMNLP 2026 标准：5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings）\n- Soundness / Excitement / Overall 分项评分",
    "reviewer_id": "1",
    "round_number": "9"
  }
}
````

</details>

---


### Tool result

_source line 865 · 2026-05-23T03:02:20.964384+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17845
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-23T03:02:21.466927+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "text": "## Round 9 继续审稿 — Reviewer 2 任务\n\n**模式**: 继续审稿（非初审）。论文已根据上轮审稿意见修改，你的任务是逐条验证 open/in_progress 问题是否充分解决，并检查修改是否引入新问题。\n\n**Venue**: EMNLP 2026 (ARR Long Paper, 8页正文限制, deadline 2026-05-25)\n\n**你的侧重**: Framing、Novelty、完整性\n\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_9/submitted.pdf`\n\n### 上轮以来的关键修改（commits d6fdd5a, 55aa8ee, 0b38a2b）\n\n1. **14B 探索性结果**：Table 2 新增 14B 行 (CLS 89.21%, CWM 89.26%, gap ≈ 0)，标注 \"single seed; exploratory\"\n2. **Bayesian ROPE**：§3.4 新增段落引用 Appendix Bayesian ROPE 分析 (P(ROPE)=0.975 for CLS-CWM)\n3. **TOST 功效讨论**：§3.4 新增 \"Statistical power\" 段落 (n_eff≈86, power~0.3)\n4. **Variant-level 标注**：§3.5 开头标注 \"exploratory due to limited seed coverage\"\n5. **Routing 负结果**：§3.6 error complementarity 部分加入 \"Simple routing heuristics capture <0.4pp of the oracle gap\"\n6. **Checkpoint 证据整合**：§3.6 \"Why does generation degrade\" 段落整合 matched epoch-3 gaps 20-23pp + CLS ablation <1pp\n7. **ICL collapse 扩展**：§3.5 加入 \"establishing that execution-free verification requires task-specific fine-tuning regardless of formulation\"\n8. **Wall-clock 时间**：48ms vs 16.3s per inference\n9. **Figure 2 y-axis 修复**：commit d6fdd5a 提及修复\n10. **Logistic regression robustness**：commit 0b38a2b 修复 model identity 过强显著性声明\n11. **Exploratory 标注**：commit d6fdd5a 提及 exploratory annotation\n\n### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由的 Issue 列表\n\n**[CRITICAL] R6-N4** — Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\n- 上轮状态: in_progress\n- 待验证: Routing negative result 是否增加了分析深度；14B convergence 发现是否为有意义的 insight；Bayesian ROPE 是否增强了 equivalence 证据质量；整体 novelty 相比上轮是否有改善\n\n**[WARNING] R8-W7** — Novelty 是否足够 Conference 水平（与 R6-N4 关联）\n- 上轮状态: in_progress（合并至 R6-N4）\n- 待验证: 新增内容（routing negative, 14B, ROPE）是否将 excitement 从 2.5 提升\n\n**[WARNING] R8-W1** — TOST 统计功效不足 + Bayesian ROPE 补充\n- 上轮状态: in_progress\n- 待验证: Bayesian ROPE 的 prior 选择和 ROPE 区间设定是否合理；TOST power 讨论是否充分\n\n**[INFO] R6-M3** — Figure 2/3 y-axis 不从零开始\n- 上轮状态: in_progress\n- 待验证: y-axis 是否已修复或是否有充分的 caption 标注\n\n**[INFO] R8-M2** — Appendix M logistic regression 补充\n- 上轮状态: in_progress\n- 待验证: 是否已补充 logistic regression marginal effects 或 odds ratios\n\n### 额外检查\n\n- Abstract 和 Conclusion 的 framing 是否与正文修改保持一致\n- 14B 结果在叙事中的位置是否恰当（exploratory 而非 confirmatory）\n- routing negative result 的讨论是否过度或不足\n- 修改是否引入新问题（前后矛盾、overclaim/underclaim）\n- Limitations section 覆盖是否充分（Python-only, ≤8B LoRA, synthetic mutation）\n\n### 输出格式\n\n对每个 issue：\n```\n**[R6-N4]** [RESOLVED] / [STILL_OPEN]\n理由: ...\n```\n\n最后给出：\n- 新发现的问题（如有）\n- 整体评分建议（EMNLP 2026 标准：5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings）\n- Soundness / Excitement / Overall 分项评分",
  "reviewer_id": "2",
  "round_number": "9"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 9 继续审稿 — Reviewer 2 任务\n\n**模式**: 继续审稿（非初审）。论文已根据上轮审稿意见修改，你的任务是逐条验证 open/in_progress 问题是否充分解决，并检查修改是否引入新问题。\n\n**Venue**: EMNLP 2026 (ARR Long Paper, 8页正文限制, deadline 2026-05-25)\n\n**你的侧重**: Framing、Novelty、完整性\n\n**论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/main.tex`\n**PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_round_9/submitted.pdf`\n\n### 上轮以来的关键修改（commits d6fdd5a, 55aa8ee, 0b38a2b）\n\n1. **14B 探索性结果**：Table 2 新增 14B 行 (CLS 89.21%, CWM 89.26%, gap ≈ 0)，标注 \"single seed; exploratory\"\n2. **Bayesian ROPE**：§3.4 新增段落引用 Appendix Bayesian ROPE 分析 (P(ROPE)=0.975 for CLS-CWM)\n3. **TOST 功效讨论**：§3.4 新增 \"Statistical power\" 段落 (n_eff≈86, power~0.3)\n4. **Variant-level 标注**：§3.5 开头标注 \"exploratory due to limited seed coverage\"\n5. **Routing 负结果**：§3.6 error complementarity 部分加入 \"Simple routing heuristics capture <0.4pp of the oracle gap\"\n6. **Checkpoint 证据整合**：§3.6 \"Why does generation degrade\" 段落整合 matched epoch-3 gaps 20-23pp + CLS ablation <1pp\n7. **ICL collapse 扩展**：§3.5 加入 \"establishing that execution-free verification requires task-specific fine-tuning regardless of formulation\"\n8. **Wall-clock 时间**：48ms vs 16.3s per inference\n9. **Figure 2 y-axis 修复**：commit d6fdd5a 提及修复\n10. **Logistic regression robustness**：commit 0b38a2b 修复 model identity 过强显著性声明\n11. **Exploratory 标注**：commit d6fdd5a 提及 exploratory annotation\n\n### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] + 理由的 Issue 列表\n\n**[CRITICAL] R6-N4** — Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\n- 上轮状态: in_progress\n- 待验证: Routing negative result 是否增加了分析深度；14B convergence 发现是否为有意义的 insight；Bayesian ROPE 是否增强了 equivalence 证据质量；整体 novelty 相比上轮是否有改善\n\n**[WARNING] R8-W7** — Novelty 是否足够 Conference 水平（与 R6-N4 关联）\n- 上轮状态: in_progress（合并至 R6-N4）\n- 待验证: 新增内容（routing negative, 14B, ROPE）是否将 excitement 从 2.5 提升\n\n**[WARNING] R8-W1** — TOST 统计功效不足 + Bayesian ROPE 补充\n- 上轮状态: in_progress\n- 待验证: Bayesian ROPE 的 prior 选择和 ROPE 区间设定是否合理；TOST power 讨论是否充分\n\n**[INFO] R6-M3** — Figure 2/3 y-axis 不从零开始\n- 上轮状态: in_progress\n- 待验证: y-axis 是否已修复或是否有充分的 caption 标注\n\n**[INFO] R8-M2** — Appendix M logistic regression 补充\n- 上轮状态: in_progress\n- 待验证: 是否已补充 logistic regression marginal effects 或 odds ratios\n\n### 额外检查\n\n- Abstract 和 Conclusion 的 framing 是否与正文修改保持一致\n- 14B 结果在叙事中的位置是否恰当（exploratory 而非 confirmatory）\n- routing negative result 的讨论是否过度或不足\n- 修改是否引入新问题（前后矛盾、overclaim/underclaim）\n- Limitations section 覆盖是否充分（Python-only, ≤8B LoRA, synthetic mutation）\n\n### 输出格式\n\n对每个 issue：\n```\n**[R6-N4]** [RESOLVED] / [STILL_OPEN]\n理由: ...\n```\n\n最后给出：\n- 新发现的问题（如有）\n- 整体评分建议（EMNLP 2026 标准：5=Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings）\n- Soundness / Excitement / Overall 分项评分",
    "reviewer_id": "2",
    "round_number": "9"
  }
}
````

</details>

---


### Tool result

_source line 867 · 2026-05-23T03:02:22.830460+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1363
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-23T03:02:22.981557+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "review_chat_id": "oc_0ae20ec1ce60f9c0589d629648584eff"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-23T03:02:24.648990+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1667
}
```

</details>

---


### Assistant

_source line 870 · 2026-05-23T03:02:31.222395+00:00_

Round 9 继续审稿已启动：

- **Reviewer 1**（统计方法论 + 实验严谨性）：已派发，重点审查 R6-N1 variant exploratory 标注、R8-W1 TOST power/ROPE、R8-M2 logistic regression、R6-M3 Figure y-axis
- **Reviewer 2**（Framing + Novelty + 完整性）：已派发，重点审查 R6-N4 novelty 提升、R8-W7 conference 水平、R8-W1 ROPE 补充、R6-M3/R8-M2 修复
- **视觉审查 Agent**：已派发，与 Reviewer 并行执行

等待 Reviewer 回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 75

## Round 75

2 recorded events


### User

_source line 871 · 2026-05-23T03:07:18.012174+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 9 继续审稿报告

---

### 逐条 Issue 验证

**[R6-N1] [RESOLVED]**
理由：§3.5 开头现在有明确标注——"Variant-level comparisons (n=48) are exploratory due to limited seed coverage; the per-test interaction effect is statistically confirmed (see below)." 后续讨论（failure mode taxonomy, Table 4）使用描述性语言（"three failure modes"、"formal collapse accounts for..."），未做 causal claims。§3.7 Threats to Validity 进一步强调"correlated confounds and limited seeds mean definitive causal attribution requires multi-seed replication"。abstract 中 variant-level 相关措辞也已审慎化。完全满足 exploratory/descriptive 标注要求。

**[R8-W1] [RESOLVED]**
理由：三处修改充分解决了此问题：
1. **§3.4 Statistical power 段落**：明确报告"TOST power is ~0.3 (Cohen, 1988)"，承认"The CLS–TRAJ non-confirmation may reflect insufficient power"。Cohen (1988) 引用补上了我 Round 1 指出的 missing reference。
2. **Bayesian ROPE**：§3.4 引用 Appendix J 的 Bayesian ROPE 分析。方法论规范——Jeffreys prior（标准无信息先验）、ROPE=±2pp（与 SESOI 一致）、报告 P(ROPE) 和 95% HDI。CLS-CWM: P(ROPE)=0.975, HDI=[+0.10, +2.00pp] 完全落入 ROPE 内——独立于 TOST 地确认等价。CLS-TRAJ: P(ROPE)=0.542（inconclusive），与 TOST 校正后失败一致。Kruschke (2013, 2018) 已正确引用。
3. **Abstract 措辞**：现为"TRAJ parity is model-dependent and not confirmed after multiple comparison correction"——准确且审慎。

综合来看，TOST 功效不足的问题现在被(a)透明披露、(b)通过 Bayesian 替代方法独立验证、(c)在 abstract 中准确反映。从方法论角度，这是教科书级的处理。

**[R8-M2] [RESOLVED]**
理由：Appendix M 现在包含完整的 GEE logistic regression（binomial family, exchangeable working correlation, robust sandwich SEs）。关键结果：
- CWM×repo interaction: OR=0.31 (0.15, 0.65), p=0.002——与 LPM 的 β=−0.219 (p<0.001) 方向/显著性一致
- Average marginal effects: −0.22pp (function), −21.5pp (repo)——与 LPM 系数差异在 0.3pp 以内
- **关键透明度改进**：论文明确报告 model family 效应在 LPM (p=0.002) vs GEE (p=0.410) 之间存在显著差异，归因于 GEE 的 cluster-robust inference 更保守（k=25 clusters）。这直接 address 了 commit 0b38a2b 的 "Fix model identity over-strong significance claims"。
- 主要发现（formulation×complexity interaction）在两种框架下均显著且一致；次要发现（model identity）在 GEE 下不显著——论文诚实地披露了这一点而非隐藏。

**[R6-M3] [RESOLVED]**
理由：Figure 2（p.7）y-axis 现从 55% 开始，caption 标注 "Note: y-axis begins at 55% to emphasize formulation differences." 相比上轮（~82%），55% 提供了充分的视觉上下文——majority baseline (~54%) 可作为参照。4B/8B 数据点有 shaded gap region（暗示 seed variance），14B 单点标注为 "single seed (exploratory)"。

---

### 额外检查结果

**14B 结果的统计表述**：恰当。Table 2 有 "(14B; exploratory)" 标注和脚注 "single seed, n=1 at 14B"。Abstract 使用 "Exploratory 14B results (single seed) show the function-level gap narrowing to near zero (~0.05 pp), suggesting capacity-dependent generation scaling"——"suggesting" 足够审慎。Figure 2 caption 同样标注 "single seed (exploratory)"。

**Bayesian ROPE 方法论规范性**：规范。Jeffreys prior 是标准选择；给定 523 instances × 5 seeds 的数据量，prior 对 posterior 的影响可忽略。ROPE 区间（±2pp）与 frequentist SESOI 一致，确保两种方法的可比性。同时报告 P(ROPE) 和 HDI 是 best practice。对 CLS-TRAJ 的 "inconclusive" 判定也是正确的（P(ROPE)=0.542 远未达到通常的 0.95 阈值）。

**修改引入的新问题**：

**NEW-1 [MINOR] 14B 单 seed 结果在 Figure 2 中的视觉权重**
Figure 2 中 14B 数据点与 4B/8B 并列呈现，但后两者有多 seed 支撑（error region），14B 仅为单点。虽然 caption 有标注，但图形中三个 scale 点的视觉等权可能误导快速浏览的读者——尤其是 14B 处 CWM 反超 CLS（89.26% vs 89.21%）的 gap reversal 可能被过度解读。建议：(a) 在 14B 数据点旁加星号/虚线以视觉区分，或 (b) 在图中而非仅 caption 标注"n=1"。

**NEW-2 [MINOR] §3.5 中 LPM 的 model identity 效应与 GEE 不一致**
§3.5 main text 提到"model identity modulates gap magnitude without changing direction"，引用的是 LPM 结果（β=0.011, p=0.001）。但 Appendix M 的 GEE 结果显示 model identity 效应不显著（p=0.410）。建议在 §3.5 中加一句 qualifier，如"under LPM; GEE cluster-robust analysis does not confirm this secondary effect (Appendix M)"，以避免 main text 和 appendix 之间的 claim 强度不一致。

---

### Checkpoint 问题回顾

虽然 checkpoint 公平性不在本轮 issue 列表中，但作为我 Round 1 的 top CRITICAL concern (R1-N1)，我注意到修订版在两处提供了决定性证据：
1. **§3.6**："Checkpoint selection does not explain the gap: matched epoch-3 comparisons yield 20-23pp gaps, and CLS varies <1 pp across epochs (Appendix O)."
2. **Appendix O**：CLS 在 epoch 1 / val-selected / final epoch 之间变化 <1pp（85.34% / 84.48% / 85.29%）；CWM gap 在所有 checkpoint 下均为 20-23pp。

这从根本上消除了我 Round 1 的核心顾虑。CWM repo-level 退化不是 checkpoint selection artifact，而是 formulation-inherent。

---

### 整体评估

**修改质量**：优秀。四个 tracked issues 全部 RESOLVED，每处修改都恰到好处——既解决了问题，又未引入过度 hedging 或措辞膨胀。Bayesian ROPE 和 GEE logistic regression 的补充尤其专业。14B 探索性结果为 capacity 假说提供了初步方向性证据。

**剩余限制**（inherent，非修改可解决）：
- ≤8B 规模（14B 仅为探索性）
- Python-only（现已在 Limitations 提及）
- TRAJ 数据量/信号粒度不对称（inherent to formulation design）
- 贡献本质为 empirical comparison

### 修订后评分

| 维度 | Round 1 | Round 9 | 变化理由 |
|------|---------|---------|--------|
| **Soundness** | 3/5 | 4/5 | 所有 CRITICAL 混杂变量已 address：checkpoint 证据决定性（matched epoch-3 = same gap），TOST 功效透明披露 + Bayesian ROPE 独立验证，GEE 确认 primary effects robust。 |
| **Excitement** | 3/5 | 3/5 | 未变。核心贡献仍为 empirical comparison。14B 结果和 routing 负结果增加了完整性，但不改变贡献类型。 |
| **Reproducibility** | 4/5 | 4/5 | 已经很好，保持。 |
| **Overall** | 3.5 | 3.5 | Borderline Conference。Soundness 从 3→4 是显著提升，但 excitement ceiling（empirical comparison of existing methods）限制了 overall 上调至 4。论文是 NLP 领域少见的方法论严谨的 empirical study，对 Findings 而言绰绰有余，对 Conference 而言取决于 AC 对 empirical comparison papers 的 excitement 标准。若 AC 认为 execution-free verification formulation 的系统性比较对社区有足够实用价值，则可接收。 |
| **Confidence** | 4/5 | 4/5 | 仔细阅读全部 24 页，熟悉 TOST/Bayesian ROPE/GEE/ICC 方法论。 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 872 · 2026-05-23T03:07:26.449047+00:00_

Reviewer 1 已提交。4 个 tracked issues 全部标为 RESOLVED，发现 2 个新 MINOR 问题。评分 3.5 (Borderline Conference)。等待 Reviewer 2 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 76

## Round 76

2 recorded events


### User

_source line 873 · 2026-05-23T03:07:30.416239+00:00_

[Reviewer 1 审稿结果]:
Round 9 审稿完成。

四个 tracked issues 全部 **RESOLVED**：
- **R6-N1**：§3.5 有明确 "exploratory" 标注，避免了 causal claims
- **R8-W1**：§3.4 新增 power 讨论 + Bayesian ROPE (P(ROPE)=0.975)，abstract 措辞审慎
- **R8-M2**：Appendix M 补充了 GEE logistic regression + robust SEs，主次效应差异透明披露
- **R6-M3**：Figure 2 y-axis 从 55% 起始，已标注

发现两个新 MINOR 问题：14B 单 seed 在 Figure 2 中视觉权重过高、§3.5 LPM model identity 效应与 GEE 结论不一致需加 qualifier。

整体评分：Soundness 3→4（混杂变量充分 address），Excitement 3（未变），Overall 3.5（Borderline Conference）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 874 · 2026-05-23T03:07:37.887236+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 77

## Round 77

6 recorded events


### User

_source line 875 · 2026-05-23T03:08:07.086980+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 9 逐条验证报告

---

## 逐条 Issue 验证

### **[R6-N4]** [STILL_OPEN]（已显著改善，但根本性质未变）

**新增内容评估：**

1. **14B 探索性结果（Table 2, p.5）**：CLS 89.21% vs CWM 89.26%，gap ≈ −0.05pp。这是本轮最有价值的新增——它将叙事从"CWM 在 repo level 不行"转变为"CWM 的劣势是 capacity-dependent，随规模增大而消失"。论文正确标注为 "single seed; exploratory"，并在正文中写道 "These single-seed results require multi-seed confirmation"。这是一个有意义的 insight，超越了简单的性能比较。

2. **Routing 负结果（§3.6, p.7）**："Simple routing heuristics capture <0.4 pp of the oracle gap"。这直接回应了我 Round 1 的 W3（routing 仅为未验证假设）。将假设转化为文档化的负结果增加了分析深度。但这也意味着 error complementarity 虽然存在，但目前无法被简单利用——这限制了该发现的实用价值。

3. **Bayesian ROPE（§3.4, p.5）**：P(ROPE)=0.975 for CLS-CWM，为等价性提供了贝叶斯框架的强力证据。这是方法论层面的加强，而非 novelty 层面的。

**为什么仍然 STILL_OPEN**：论文的核心贡献类型没有改变——它仍然是三种已有 formulation 的比较研究。14B 发现和 routing 负结果增加了分析深度，但没有引入新方法或新理论框架。对于 EMNLP main conference（Overall ≥ 4），通常期望看到 (a) 新方法，(b) 令人意外的发现，或 (c) 可能改变领域实践的结论。本文的发现（"complexity 和 scale 决定 formulation 选择"）有实用价值但不具备 field-changing 的潜力。

**改善幅度**：Excitement 从 2.5 → 3.0。14B 的 capacity-dependent convergence insight 是最有说服力的提升——如果有 multi-seed 确认，可以进一步提升。

---

### **[R8-W7]** [STILL_OPEN]（合并至 R6-N4，评估同上）

新增内容（routing negative, 14B, ROPE）将 excitement 从 2.5 提升至 3.0，但未达到 Conference 水平（≥4）。论文现在是一篇非常扎实的 Findings 候选论文，但 excitement 的核心限制——比较已有方法而非提出新方法——未被修改所解决。

---

### **[R8-W1]** [RESOLVED]

Bayesian ROPE 分析实现良好且直接回应了 TOST 功效不足的问题：

1. **ROPE 实现（Appendix J, p.20）**："the posterior for the mean accuracy difference follows a t-distribution with n−1 degrees of freedom. For CLS-CWM, P(ROPE) = 0.975, and the 95% HDI = [+0.10, +2.00] pp falls entirely inside the ROPE"。Prior 选择（Jeffreys' t-分布）标准且合理，ROPE 区间 ±2pp 与 TOST SESOI 一致。

2. **CLS-TRAJ 诚实报告（Appendix J, p.20）**："P(ROPE) = 0.542 (inconclusive; 95% HDI = [+0.35, +3.52] pp extends beyond the ROPE)"。这与 TOST 未通过 Holm-Bonferroni 一致，透明地报告了不确定性。

3. **正文 power 讨论（§3.4, p.5）**："Statistical power. With n_eff ≈ 86 after clustering, TOST power is ~0.3 (Cohen, 1988). The CLS-CWM equivalence (p=0.007) is robust; CLS-TRAJ non-confirmation may reflect insufficient power."

双统计框架（TOST + Bayesian ROPE）的一致性显著增强了 CLS-CWM 等价性的证据质量，CLS-TRAJ 的不确定性被透明处理。

---

### **[R6-M3]** [RESOLVED]

Figure 2（p.7）现在是包含 4B/8B/14B 三个数据点的折线图（之前仅 4B/8B 柱状图）。Y 轴仍不从零开始（约从 82% 起），但对于展示 0-3pp 级别的差异而言，从零开始会使差异完全不可见。Figure 3（p.13）的 caption 明确标注 "Note: y-axis does not start at zero"。

考虑到 (a) 展示目的（差异可视化而非绝对值比较），(b) Figure 3 有明确标注，我将此标记为 RESOLVED。但建议 Figure 2 也增加类似的 y-axis 标注以保持一致性。

---

### **[R8-M2]** [RESOLVED]

Appendix M（p.21）现在包含完整的 GEE logistic regression robustness check：

- OR 和 marginal effects 均已报告："CWM main effect at function level has OR=0.98 (95% CI [0.86, 1.12], p=0.771) and the CWM×repo interaction has OR=0.31 (0.15, 0.65), p=0.002"
- "Average marginal effects are −0.2 pp (function) and −21.6 pp (repo), matching LPM coefficients within 0.1 pp"
- Commit 0b38a2b 修正了 model identity 的过强显著性声明（"directionally positive but specification-dependent"）

LPM 和 logistic regression 的一致性令人信服，方法论透明度达到很高水平。

---

## 新发现的问题

### **[NEW-1] [MINOR] Abstract-body 微弱不一致：routing 措辞**

Abstract（p.1）："Error complementarity and a failure mode taxonomy motivate complexity-aware formulation routing over uniform selection."

但 §3.6（p.7）报告："Simple routing heuristics capture <0.4 pp of the oracle gap"——即 routing 在实践中效果极弱（0.4pp / ~6.5pp oracle gap ≈ 6%）。

Abstract 的 "motivate routing" 暗示 routing 是一个有前景的方向，而正文数据显示简单 routing 几乎不工作。措辞不算 technically wrong（"motivate" 可理解为 "motivate future research"），但一位快速读 abstract 的读者可能会高估 routing 的可行性。

**建议**：Abstract 中增加半句限定，如 "though simple heuristics capture only a fraction of the oracle advantage, motivating learned approaches"。

### **[NEW-2] [MINOR] Abstract 中 TRAJ 措辞改善但仍有精确性空间**

Abstract（p.1）："TRAJ parity is model-dependent and not confirmed after multiple comparison correction."

相比上轮（"TRAJ parity differs between the two tested families"）大幅改善。但 "not confirmed" 可能被误读为 "disconfirmed"（被否定）。更精确的表述可以是 "TRAJ equivalence could not be established after multiple comparison correction, consistent with insufficient statistical power."

这是非常 minor 的措辞问题，不影响评分。

---

## Framing 一致性检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Abstract ≤8B 限定 | ✅ | "under our ≤8B LoRA protocol" 已明确标注 |
| Abstract TRAJ 措辞 | ✅ | 从"differs"改为"not confirmed after multiple comparison correction"（大幅改善） |
| Conclusion ≤8B 限定 | ✅ | "Primary statistical findings are established only under ≤8B LoRA fine-tuning" |
| 14B 探索性标注 | ✅ | Table 2 脚注 + 正文 "single seed; exploratory" + "require multi-seed confirmation" |
| Repo-level 有限 seed 标注 | ✅ | §3.5 开头 "exploratory due to limited seed coverage" |
| Limitations Python-only | ✅ | "All evaluation uses Python-only benchmarks"（新增，回应我 Round 1 W1） |
| Limitations ≤8B scale | ✅ | "Primary findings use ≤8B LoRA fine-tuning" |
| Limitations 合成数据 | ✅ | "Training data is constructed via synthetic mutation operators"（新增） |
| "governed by" overclaim | ✅ | 改为 "moderated by"——标准统计术语，准确描述交互效应 |

**Framing 一致性评估**：论文在 framing calibration 上做了显著工作。Claims 与证据的匹配度从 Round 1 的"偶有 overclaim"提升至"系统性 well-calibrated"。这是值得肯定的改善。

---

## 格式合规检查

- ✅ 正文 8 页（Sections 1-5 结束于 p.8 中部，Limitations 从 p.8 底部开始）
- ✅ Limitations 不计入页数限制
- ✅ Anonymous ACL submission header，无作者信息
- ✅ 24 页总计（8 正文 + Limitations + References + Checklist + 附录）

---

## 整体评分建议

### 分项评分变化

| 维度 | Round 1 | Round 9 | 变化理由 |
|------|---------|---------|--------|
| **Soundness** | 3.5/5 | **4.0/5** | Bayesian ROPE 双框架验证、透明 power 讨论、logistic regression robustness check、proper exploratory/confirmatory 区分、更审慎的 claim calibration。方法论严谨度达到 NLP 论文高水平。 |
| **Excitement** | 2.5/5 | **3.0/5** | 14B capacity-dependent convergence 是有意义的新 insight；routing 负结果增加分析深度；但核心贡献仍是比较研究，无新方法。 |
| **Overall** | 3.0/5 | **3.0/5** | 维持 Findings 推荐。论文在 soundness 和 calibration 上有显著改善，是一篇很强的 Findings 候选论文。但 excitement 的核心限制（比较已有方法、无新方法或令人意外的发现）未被根本性解决。14B 如果有 multi-seed 确认且 gap 确实收敛至零，可能将 overall 推至 3.5 (Borderline Conference)，但目前 single-seed 证据不足以支撑。 |
| **Confidence** | 4/5 | **4/5** | 不变 |

### 评分说明

**为什么 Soundness 提升至 4.0**：Round 9 的论文在统计方法论上几乎无可挑剔。TOST + Bayesian ROPE 双框架、transparent power analysis、LPM + GEE 一致性验证、proper exploratory 标注——这些在 NLP 领域极为少见。如果仅看 soundness，这是一篇可以被 main conference 接收的论文。

**为什么 Overall 维持 3.0**：Soundness 的提升不能弥补 excitement 的根本短板。EMNLP main conference 需要"interesting enough to attend the talk"的标准（ARR Review Form: Excitement ≥ 3 通常是 Conference 的前提），而一篇"严谨地比较了三种已知方法并发现它们在简单任务上差不多"的论文，即使 soundness 满分，excitement 也难以达标。Findings 定位（高质量、有贡献但 excitement 有限）恰好匹配这篇论文。

**什么可以改变我的评分**：(a) 14B/32B 的 multi-seed 确认 CWM 收敛（excitement +0.5-1.0）；(b) 基于 failure mode taxonomy 的 learned router 实验（从比较研究转变为方法研究）；(c) 非 Python 语言的验证（generalizability 提升）。这些任一均可将 overall 推至 3.5。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-23T03:08:40.772404+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见，使用 [AGREE] 或 [REBUT] 标注。\n\n---\n\n### Reviewer 2 逐条验证结果\n\n**[R6-N4] [STILL_OPEN]**（已显著改善，但根本性质未变）\n- 14B 探索性结果有价值（叙事转变为 \"capacity-dependent convergence\"）\n- Routing 负结果增加分析深度但限制实用价值\n- Bayesian ROPE 是方法论加强，非 novelty 加强\n- 核心贡献类型未变：仍是三种已有 formulation 的比较研究\n- Excitement 2.5→3.0，但未达 Conference 水平\n\n**[R8-W7] [STILL_OPEN]**（合并至 R6-N4）\n- 新增内容提升 excitement 至 3.0，但 Conference 需要 ≥4\n\n**[R8-W1] [RESOLVED]** — 双统计框架一致性强\n\n**[R6-M3] [RESOLVED]** — Y 轴不从零但 caption 有标注\n\n**[R8-M2] [RESOLVED]** — GEE logistic regression 完整且透明\n\n### Reviewer 2 新发现\n\n**NEW-1 [MINOR]** Abstract \"motivate routing\" 暗示 routing 有前景，但正文数据 (<0.4pp) 显示简单 routing 几乎不工作\n\n**NEW-2 [MINOR]** Abstract \"not confirmed\" 可能被误读为 \"disconfirmed\"\n\n### Reviewer 2 评分\n\nSoundness 4/5, Excitement 3/5, Overall 3.0 (Findings)\n\n**R2 关键论点**：Soundness 提升不能弥补 excitement 根本短板。EMNLP main conference 需要 \"interesting enough to attend the talk\"，比较已知方法的论文即使 soundness 满分也难以达标。\n\n---\n\n**请重点回应**：\n1. R6-N4/R8-W7：你认为 excitement 的评估标准应如何平衡 soundness 和 novelty？你给 3.5 的理由是什么？\n2. R2-NEW-1：Abstract \"motivate routing\" 是否需要限定？\n3. R2-NEW-2：Abstract \"not confirmed\" 是否有歧义？\n4. 你是否同意 R2 的 Overall 3.0，还是坚持 3.5？理由。",
  "reviewer_id": "1",
  "round_number": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见，使用 [AGREE] 或 [REBUT] 标注。\n\n---\n\n### Reviewer 2 逐条验证结果\n\n**[R6-N4] [STILL_OPEN]**（已显著改善，但根本性质未变）\n- 14B 探索性结果有价值（叙事转变为 \"capacity-dependent convergence\"）\n- Routing 负结果增加分析深度但限制实用价值\n- Bayesian ROPE 是方法论加强，非 novelty 加强\n- 核心贡献类型未变：仍是三种已有 formulation 的比较研究\n- Excitement 2.5→3.0，但未达 Conference 水平\n\n**[R8-W7] [STILL_OPEN]**（合并至 R6-N4）\n- 新增内容提升 excitement 至 3.0，但 Conference 需要 ≥4\n\n**[R8-W1] [RESOLVED]** — 双统计框架一致性强\n\n**[R6-M3] [RESOLVED]** — Y 轴不从零但 caption 有标注\n\n**[R8-M2] [RESOLVED]** — GEE logistic regression 完整且透明\n\n### Reviewer 2 新发现\n\n**NEW-1 [MINOR]** Abstract \"motivate routing\" 暗示 routing 有前景，但正文数据 (<0.4pp) 显示简单 routing 几乎不工作\n\n**NEW-2 [MINOR]** Abstract \"not confirmed\" 可能被误读为 \"disconfirmed\"\n\n### Reviewer 2 评分\n\nSoundness 4/5, Excitement 3/5, Overall 3.0 (Findings)\n\n**R2 关键论点**：Soundness 提升不能弥补 excitement 根本短板。EMNLP main conference 需要 \"interesting enough to attend the talk\"，比较已知方法的论文即使 soundness 满分也难以达标。\n\n---\n\n**请重点回应**：\n1. R6-N4/R8-W7：你认为 excitement 的评估标准应如何平衡 soundness 和 novelty？你给 3.5 的理由是什么？\n2. R2-NEW-1：Abstract \"motivate routing\" 是否需要限定？\n3. R2-NEW-2：Abstract \"not confirmed\" 是否有歧义？\n4. 你是否同意 R2 的 Overall 3.0，还是坚持 3.5？理由。",
    "reviewer_id": "1",
    "round_number": "9"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-23T03:08:58.608992+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17836
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-23T03:09:02.224378+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见，使用 [AGREE] 或 [REBUT] 标注。\n\n---\n\n### Reviewer 1 逐条验证结果\n\n**[R6-N1] [RESOLVED]** — §3.5 有 exploratory 标注，避免 causal claims，§3.7 强调 \"definitive causal attribution requires multi-seed replication\"\n\n**[R8-W1] [RESOLVED]** — TOST power 讨论 + Bayesian ROPE (P(ROPE)=0.975) + Abstract 审慎措辞，称为\"教科书级处理\"\n\n**[R8-M2] [RESOLVED]** — GEE logistic regression 完整，model identity 的 LPM/GEE 差异透明披露\n\n**[R6-M3] [RESOLVED]** — Y 轴从 55% 起始（上轮~82%），有 caption 标注\n\n### Reviewer 1 新发现\n\n**NEW-1 [MINOR]** 14B 单 seed 在 Figure 2 中与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读。建议加星号/虚线或图中标注 \"n=1\"。\n\n**NEW-2 [MINOR]** §3.5 main text 引用 LPM model identity 效应 (p=0.001)，但 Appendix M 的 GEE 显示不显著 (p=0.410)。建议加 qualifier。\n\n### Reviewer 1 评分\n\nSoundness 4/5, Excitement 3/5, Overall 3.5 (Borderline Conference)\n\n**R1 关键论点**：Soundness 3→4 是显著提升。论文是 NLP 领域少见的方法论严谨 empirical study，对 Findings 绰绰有余，对 Conference 取决于 AC 对 empirical comparison papers 的 excitement 标准。\n\n### Reviewer 1 额外观察\n\nR1 回顾了 checkpoint 问题（原 R1 的 top CRITICAL concern），确认 §3.6 和 Appendix O 的 matched epoch-3 证据\"从根本上消除了核心顾虑\"。\n\n---\n\n**请重点回应**：\n1. R1-NEW-1：Figure 2 中 14B 单 seed 视觉权重问题——你是否在审查中也注意到？\n2. R1-NEW-2：LPM vs GEE model identity 不一致——你是否同意需要 qualifier？\n3. R1 给 Overall 3.5 的核心论点是\"方法论严谨的 empirical study 在 NLP 领域少见\"。你是否认为方法论严谨度能部分弥补 novelty 不足？\n4. 你对 Figure 2 y-axis 的评估（不从零但可接受）是否与 R1 的评估（从 55% 起始，充分视觉上下文）一致？",
  "reviewer_id": "2",
  "round_number": "9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见，使用 [AGREE] 或 [REBUT] 标注。\n\n---\n\n### Reviewer 1 逐条验证结果\n\n**[R6-N1] [RESOLVED]** — §3.5 有 exploratory 标注，避免 causal claims，§3.7 强调 \"definitive causal attribution requires multi-seed replication\"\n\n**[R8-W1] [RESOLVED]** — TOST power 讨论 + Bayesian ROPE (P(ROPE)=0.975) + Abstract 审慎措辞，称为\"教科书级处理\"\n\n**[R8-M2] [RESOLVED]** — GEE logistic regression 完整，model identity 的 LPM/GEE 差异透明披露\n\n**[R6-M3] [RESOLVED]** — Y 轴从 55% 起始（上轮~82%），有 caption 标注\n\n### Reviewer 1 新发现\n\n**NEW-1 [MINOR]** 14B 单 seed 在 Figure 2 中与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读。建议加星号/虚线或图中标注 \"n=1\"。\n\n**NEW-2 [MINOR]** §3.5 main text 引用 LPM model identity 效应 (p=0.001)，但 Appendix M 的 GEE 显示不显著 (p=0.410)。建议加 qualifier。\n\n### Reviewer 1 评分\n\nSoundness 4/5, Excitement 3/5, Overall 3.5 (Borderline Conference)\n\n**R1 关键论点**：Soundness 3→4 是显著提升。论文是 NLP 领域少见的方法论严谨 empirical study，对 Findings 绰绰有余，对 Conference 取决于 AC 对 empirical comparison papers 的 excitement 标准。\n\n### Reviewer 1 额外观察\n\nR1 回顾了 checkpoint 问题（原 R1 的 top CRITICAL concern），确认 §3.6 和 Appendix O 的 matched epoch-3 证据\"从根本上消除了核心顾虑\"。\n\n---\n\n**请重点回应**：\n1. R1-NEW-1：Figure 2 中 14B 单 seed 视觉权重问题——你是否在审查中也注意到？\n2. R1-NEW-2：LPM vs GEE model identity 不一致——你是否同意需要 qualifier？\n3. R1 给 Overall 3.5 的核心论点是\"方法论严谨的 empirical study 在 NLP 领域少见\"。你是否认为方法论严谨度能部分弥补 novelty 不足？\n4. 你对 Figure 2 y-axis 的评估（不从零但可接受）是否与 R1 的评估（从 55% 起始，充分视觉上下文）一致？",
    "reviewer_id": "2",
    "round_number": "9"
  }
}
```

</details>

---


### Tool result

_source line 879 · 2026-05-23T03:09:03.637990+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 880 · 2026-05-23T03:09:08.798141+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 881 · 2026-05-23T03:09:11.400996+00:00_

[Reviewer 2 审稿结果]:
Round 9 审稿报告已提交。

核心结论：
- **R8-W1** (TOST power) → **RESOLVED**，Bayesian ROPE 双框架验证充分
- **R6-M3** (Figure y-axis) → **RESOLVED**，适当标注
- **R8-M2** (Logistic regression) → **RESOLVED**，GEE robustness check 完整
- **R6-N4** (Novelty) → **STILL_OPEN**，14B insight 和 routing 负结果有改善但核心贡献类型未变
- 评分：Soundness 3.5→4.0，Excitement 2.5→3.0，Overall 维持 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 882 · 2026-05-23T03:09:20.035215+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 79

## Round 79

2 recorded events


### User

_source line 883 · 2026-05-23T03:09:43.790061+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 Round 9 意见的逐条回应

---

### [AGREE] R6-N4 / R8-W7: Excitement 评估

同意 R2 的核心判断：贡献类型未变（empirical comparison of existing formulations），14B/ROPE/routing 负结果提升的是 completeness 和 soundness，而非 excitement。

但我与 R2 在 **excitement 阈值判定**上有分歧，这也是 Director 要求重点回应的第一个问题：

**我给 Overall 3.5 而非 3.0 的理由：**

R2 的标准是"interesting enough to attend the talk"——这是合理的 excitement 标准，但忽略了 EMNLP/ARR 对 **empirical contribution papers** 的实际接收实践。以下三个论据支撑 Borderline Conference 而非 Findings：

1. **方法论严谨性本身构成贡献**。本文的统计方法论（TOST + Bayesian ROPE + GEE + ICC-clustered bootstrap + Holm-Bonferroni）在 NLP empirical papers 中极为罕见。这不仅是"做得好"，而是**示范了 NLP 社区应如何做 formulation comparison**——这本身有 methodological excitement，即使研究对象不新。类比：Dodge et al. (2019) "Show Your Work" 和 Card et al. (2020) 关于 NLP 实验报告规范的论文，本身不提出新方法，但因方法论贡献被 EMNLP 接收。

2. **Failure mode taxonomy 的实用价值**。三类 failure modes（formal collapse / decision collapse / aggregation penalty）不是从直觉可预测的——特别是 decision collapse（CLS 过度自信地预测 pass 导致 false negative）和 formal collapse（CWM 的 53-74% unparseable rate）的具体机制和量化比例。这对选择 verification pipeline 的从业者有直接指导意义。

3. **14B gap reversal 的 forward-looking 价值**。虽然是 single seed / exploratory，但 CWM 在 14B 反超 CLS（89.26% vs 89.21%）暗示≤8B 的"generation inherently worse"结论可能不泛化到更大模型——这对社区的 resource allocation 决策有重要影响。如果后续验证，这将改变 CWM 被边缘化的现状。

**综合判断**：Soundness 4 + Excitement 3 → Overall 3.5 (Borderline Conference)。我认为 R2 的 Overall 3.0 (Findings) 对 soundness 的权重偏低。在 borderline 案例中，exceptional soundness 应当 pull the overall up，而非被 excitement ceiling 完全锁死。

---

### [AGREE] R2-NEW-1: Abstract "motivate routing" 需限定

同意。Abstract 说 findings "motivate complexity-aware formulation routing"，但 §3.6 的数据显示 simple routing heuristics capture <0.4pp of the oracle gap。Abstract 的措辞暗示 routing 是一个有前景的方向，但正文数据实际上是一个**负结果**——至少对 simple heuristics 而言。

建议修改为："motivate complexity-aware formulation routing, though simple heuristics capture little of the oracle gap (§3.6)" 或更简洁地 "motivate **learned** complexity-aware routing"（强调 simple 不行、需要 learned approach）。

当前措辞不构成 misleading（因为 §3.6 正文有完整数据），但 abstract 作为独立阅读的文本，应自洽。

---

### [REBUT] R2-NEW-2: Abstract "not confirmed" 不构成实质歧义

R2 担心 "not confirmed after multiple comparison correction" 可能被误读为 "disconfirmed"（即证明不等价）。

我认为这一担心**理论上成立但实际上不成立**，理由：

1. **"not confirmed" 是统计学标准用语**。在 frequentist 框架下，"not confirmed" = "test did not reach significance"，与 "rejected" / "disconfirmed" 有明确区别。任何受过统计训练的读者（即 ARR reviewer 和 *ACL 社区目标读者）不会混淆。

2. **上下文消歧**。Abstract 完整句子是 "TRAJ parity is model-dependent and not confirmed after multiple comparison correction"。"model-dependent" 先行，暗示结果 inconclusive 而非 negative。

3. **Bayesian ROPE 提供独立校验**。即使读者误读 "not confirmed" 为 "disconfirmed"，§3.4 和 Appendix J 的 Bayesian ROPE (P(ROPE)=0.542, inconclusive) 提供了第二条证据线，明确标注为 inconclusive。

不过，如果作者希望消除任何歧义，可改为 "TRAJ equivalence is inconclusive after multiple comparison correction" 或 "TRAJ parity is model-dependent; equivalence was not established after correction"。这属于 polish 而非 must-fix。

---

### 评分分歧总结

| | R1 (我) | R2 | 分歧根源 |
|---|---------|-----|---------|
| Soundness | 4/5 | 4/5 | 一致 |
| Excitement | 3/5 | 3/5 | 一致 |
| Overall | 3.5 | 3.0 | **Soundness→Overall 的传导权重不同**。R2 认为 excitement 是硬性 ceiling；我认为 exceptional soundness 可部分补偿 moderate excitement。 |

**我的最终立场：坚持 Overall 3.5 (Borderline Conference)**。

Soundness 从 Round 1 的 3/5 提升到 4/5 是实质性改善——所有 CRITICAL issues 均已解决，matched checkpoint analysis 提供了 decisive confound evidence，Bayesian ROPE 独立验证了 TOST 结论。这不是"修补漏洞"的防御性改善，而是将论文的证据基础提升到了 NLP 领域 top tier 的水平。

一篇 Soundness 4、Excitement 3 的论文，如果其 soundness 的实现方式本身具有 methodological demonstration value（如本文所展示的），应当获得 Borderline Conference 而非 Findings 的评价。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-23T03:09:49.608198+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 80

## Round 80

2 recorded events


### User

_source line 885 · 2026-05-23T03:09:53.136580+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交。四个要点总结：

1. **R6-N4/R8-W7 (excitement)**：同意贡献类型未变，但坚持 Overall 3.5——理由是 exceptional soundness + methodological demonstration value 应部分补偿 moderate excitement，而非被 excitement ceiling 锁死在 3.0。
2. **R2-NEW-1 (routing)**：同意 abstract "motivate routing" 需限定，建议改为 "motivate **learned** complexity-aware routing"。
3. **R2-NEW-2 (not confirmed)**：反驳——"not confirmed" 是统计标准用语，上下文和 Bayesian ROPE 均提供消歧，不构成实质性歧义。
4. **评分分歧**：与 R2 的核心分歧在于 Soundness→Overall 的传导权重，我认为 R2 对 soundness 的权重偏低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 886 · 2026-05-23T03:09:57.111403+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director"
}
```

</details>

---


## Round 81

## Round 81

20 recorded events


### User

_source line 887 · 2026-05-23T03:10:08.688113+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 Round 9 意见的交叉回应

---

## R1 逐条验证结果的确认

**[R6-N1] RESOLVED** — [AGREE] 与我的评估一致。exploratory 标注和 causal attribution 限定处理得当。

**[R8-W1] RESOLVED** — [AGREE] 与我的评估完全一致。R1 称其为"教科书级处理"，我同意这一评价——TOST + Bayesian ROPE 双框架在 NLP 领域确实罕见且严谨。

**[R8-M2] RESOLVED** — [AGREE] 一致。

**[R6-M3] RESOLVED** — [AGREE]，见下文第 4 点详细讨论。

---

## 重点回应

### 1. R1-NEW-1：Figure 2 中 14B 单 seed 视觉权重

**[AGREE]**

我在审稿中注意到了 14B 的单 seed 性质，但关注点放在文本标注是否充分（结论是充分的：Table 2 脚注 + 正文 "single seed; exploratory" + "require multi-seed confirmation"）。R1 的关注点更细致——Figure 2 作为视觉媒介，14B 数据点与多 seed 的 4B/8B 数据点在视觉上等权呈现，读者快速扫视图表时可能不会注意到脚注中的 "n=1" 限定，从而过度解读 gap reversal（从 2.62pp→−0.05pp）的确定性。

R1 的建议（加星号、虚线、或图中直接标注 "n=1"）是低成本高回报的改动，能显著降低误读风险。我支持这一建议。

---

### 2. R1-NEW-2：LPM vs GEE model identity 不一致

**[AGREE]**

这正是 commit 0b38a2b 试图修复的问题（"Fix model identity over-strong significance claims"）。如果 §3.5 main text 仍然引用 LPM model identity 效应 p=0.001 而未提及 GEE 给出 p=0.410，则修复不彻底——LPM 和 GEE 的差异不仅是量级问题，而是从"高度显著"到"完全不显著"的质变。

正文应至少加一句 qualifier，例如 "model identity reaches significance under LPM (p=0.001) but not under GEE logistic regression (p=0.410); this effect is specification-dependent and should be interpreted cautiously"。这种方法论透明度与论文在其他方面展现的审慎标准一致。

---

### 3. 方法论严谨度能否弥补 novelty 不足？

**[REBUT]（与 R1 观点存在分歧）**

R1 的核心论点是"方法论严谨的 empirical study 在 NLP 领域少见，因此方法论本身构成贡献"。我部分同意这一前提但不同意其推论：

**同意的部分**：论文的统计方法论确实在 NLP 领域罕见——TOST 等价性检验、Bayesian ROPE、ICC、matched experimental design、power analysis、GEE robustness check——这些在心理学或生物统计领域是标准做法，但在 NLP 中被系统性应用确实少见。这是值得肯定的贡献。

**不同意的部分**：方法论严谨度提升的是 soundness，而非 excitement。ARR review form 将二者分开评分是有原因的——一篇 soundness 5/5 但 excitement 2/5 的论文不应因为 soundness 高而被接收到 main conference。Conference acceptance 需要 "I would make an effort to attend the presentation"（ARR Excitement ≥ 3-4 的描述），而一篇"用正确的统计方法比较了三种已知 formulation 并发现它们在简单任务上差不多"的论文，无论多严谨，都难以激发这种兴趣。

**我的分数逻辑**：Soundness 4.0 ✓（方法论贡献已充分反映），Excitement 3.0（14B 有 insight 但仍是比较框架内的发现），Overall 3.0（Findings）。R1 给 Overall 3.5，差异核心在于 R1 允许 soundness 跨维度补偿 excitement，我不允许。

**但我承认这是判断差异而非对错**：如果 AC 认为 NLP 领域需要更多方法论严谨的 empirical study 作为示范（这确实有道理），那么 3.5 (Borderline Conference) 是可以辩护的。

---

### 4. Figure 2 y-axis 评估对比

**[AGREE]（R1 和我的评估一致）**

R1 报告 Figure 2 y-axis 从 55% 起始，我观察到约从 80-82% 起始——这可能是版本差异或我的读图精度问题。但无论具体起始值，我和 R1 的结论一致：对于展示 0-3pp 级别差异的折线图，从零开始会使差异不可见，非零起始是合理的设计选择，关键是有 caption 标注。R1 确认有充分标注，我也确认 Figure 3 有标注但建议 Figure 2 也增加。

---

## 评分对比总结

| 维度 | R1 Round 9 | R2 Round 9 | 分歧根源 |
|------|-----------|-----------|---------|
| Soundness | 4/5 | 4/5 | **一致** |
| Excitement | 3/5 | 3/5 | **一致** |
| Overall | 3.5 | 3.0 | R1 允许 soundness 跨维度补偿 excitement；R2 不允许 |
| Confidence | 4/5 | 4/5 | **一致** |

**共识点**：Soundness 从 3→4 的提升是 Round 9 最显著的改善。论文在方法论层面已达到高水平。Excitement 3.0 反映 14B 发现和 routing 负结果的增量贡献。

**分歧点**：仅在 Overall 0.5 分（3.0 vs 3.5）。本质上是对 "empirical comparison paper with exceptional methodology but limited novelty" 在 EMNLP acceptance spectrum 上的定位判断。两个分数都是可辩护的，最终取决于 AC 对 empirical study 贡献类型的偏好。

**如果需要统一意见**：我可以接受 3.0-3.5 区间内的任何分数。如果 AC 倾向 Conference 方向，论文的方法论质量足以支撑；如果倾向 Findings，novelty 限制是充分理由。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 888 · 2026-05-23T03:10:28.982020+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "exec-sim-repair-verifier"
  }
}
```

</details>

---


### Tool result

_source line 889 · 2026-05-23T03:10:29.032685+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T03:02:24.274165+00:00\", \"completed_at\": \"2026-05-23T03:05:47.013661+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页无任何 display item（纯 Abstract + Intro + Method 开头），Figure 1 在第 3 页出现，刚好在审稿人 3 页阈值内。若能将 Figure 1 提前至第 2 页底部会更好，但当前布局不构成问题\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 折线图 y 轴不从零开始（约 80-92 范围），caption 已注明\\\"y-axis does not start at zero\\\"——透明标注是正确做法\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文最后一页极度紧凑：Related Work 续段 + Conclusion + Limitations 全部挤在一页，段间几乎无喘息空间。审稿人可能觉得 conclusion 仓促\"}, {\"severity\": \"warning\", \"dimension\": \"page 24\", \"message\": \"附录最后一页仅约 14 行文字（占页面 <20%），其余大面积空白。建议将 Appendix P 内容紧凑化或与前一节合并，避免浪费整页\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"单页放置 Table 3 + Table 4 共两个表格，密度较高但排版未溢出，可读性尚可\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Figure 3 柱状图仅使用单一蓝色，无需颜色区分度。caption 自包含，描述清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"页面包含 Table 8 + Table 9 + 正文 + 两个 Section 标题，密度极高但无溢出\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Responsible NLP Research Checklist 包含在 PDF 中——按用户规则 ARR Checklist 应在 OpenReview form 填写而非论文内。但 ACL/ARR 模板通常包含此部分，需确认当前投稿要求\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-23T03:10:35.257285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_8.md",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_reports/round_8.md",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 891 · 2026-05-23T03:10:35.308758+00:00_

1	---
2	round: 8
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-22T16:00:48.533982+00:00
6	reviewer_ids: ['1', '2']
7	cross_response_reviewer_ids: ['1', '2']
8	force_resubmit: False
9	---
10	
11	
12	# Round 10 审稿报告
13	
14	**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
15	**Venue**: EMNLP 2026 via ARR (Long Paper)
16	**审稿模式**: Fresh (初审)
17	**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）
18	
19	---
20	
21	## Summary
22	
23	本文对三种 execution-free 代码修复验证公式（CLS 逐测试分类、CWM 执行输出生成、TRAJ 轨迹级评分）进行了首次系统性匹配比较，使用相同 base model（Qwen3-4B/8B、DeepSeek-Coder-6.7B）、相同 LoRA 配置、相同训练数据，在 function-level 和 repo-level 两个复杂度层次上评估。核心发现是"三层结构"：(1) fine-tuning 必要（35-36pp 提升），(2) function-level 公式间统计等价（TOST p=0.007），(3) repo-level 下 CWM 显著退化（低于 CLS 18-26pp），driven by format collapse。论文还提供了 failure mode taxonomy 和 error complementarity 分析。
24	
25	---
26	
27	## Strengths
28	
29	**S1. 匹配实验框架设计在 NLP 论文中属罕见严谨。** 相同 base model、LoRA rank、optimizer、training schedule、5 seeds（function-level），DeepSeek-Coder 作为 cross-model consistency check。这是实验比较研究的标杆（Section 3.1, Table 1）。[R1-S1, R2-S1 共识]
30	
31	**S2. 统计方法论深度远超 NLP 领域平均。** TOST 等价检验（而非仅 NHST）、ICC-based clustered bootstrap（114 clusters, 10K resamples）、Holm-Bonferroni 多重比较校正、mixed-effects LPM——这套工具链在 NLP 论文中极为少见（Section 3.1, 3.4, Appendix A/J/M）。[R1-S2, R2-S1 共识]
32	
33	**S3. Failure mode taxonomy 有独立实用价值。** Format collapse / decision collapse / aggregation penalty 三类 failure modes 有定量分析和定性例证（Section 3.5, Table 4, Appendix H），为从业者选择 formulation 提供可操作指导。[R1-S3, R2-S3 共识]
34	
35	**S4. Error complementarity 发现有 ensemble/routing 研究价值。** Oracle combination 90.63%（function）/ 95.83%（repo），证明公式犯互补错误。Cross-seed oracle 94.27±2.59% 确认跨 seed 稳定性（Section 3.6）。[R2-S4]
36	
37	**S5. 附录极其详尽且自我批评诚实。** 16 个 Appendix（14 页）覆盖全部 ablation、convergence、power analysis、prompt templates、qualitative errors。Limitations 和 Threats to Validity 主动识别并讨论多个潜在问题。[R1-S4/S5, R2-S5 共识]
38	
39	---
40	
41	## Weaknesses
42	
43	### Must-Fix（影响接收决定
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-23T03:11:34.200025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 893 · 2026-05-23T03:11:34.250709+00:00_

1	
2	# === Round 6 Issues (Original) ===
3	
4	# --- Round 6 Must-Fix (Consensus Critical) ---
5	
6	- id: "R6-N1"
7	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
8	  category: experiment
9	  severity: critical
10	  status: in_progress
11	  first_raised_round: 6
12	  last_seen_round: 10
13	  mentions:
14	    - round: 6
15	      reviewers: [1, 2]
16	      note: "两人独立提出，最高共识。"
17	    - round: 7
18	      reviewers: [pre-review]
19	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
20	    - round: 8
21	      reviewers: [1, 2]
22	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
23	    - round: 9
24	      reviewers: [1, 2]
25	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
26	    - round: 10
27	      reviewers: [1, 2]
28	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
29	  action_items:
30	    - round: 6
31	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
32	      assigned_to: "paper"
33	      status: resolved
34	    - round: 9
35	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
36	      assigned_to: "paper"
37	      status: in_progress
38	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. R10 §5.4 已加 'Variant-level comparisons rely on limited seed coverage' 声明。Agent 正在补充 exploratory 标注。"
39	  resolution_round: null
40	
41	- id: "R6-N2"
42	  summary: "Checkpoint selection 系统性偏向 CLS"
43	  category: method
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 6
47	  last_seen_round: 10
48	  mentions:
49	    - ro
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 894 · 2026-05-23T03:11:44.803826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 895 · 2026-05-23T03:11:44.855208+00:00_

0	
1	# === Round 6 Issues (Original) ===
2	
3	# --- Round 6 Must-Fix (Consensus Critical) ---
4	
5	- id: "R6-N1"
6	  summary: "Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当"
7	  category: experiment
8	  severity: critical
9	  status: in_progress
10	  first_raised_round: 6
11	  last_seen_round: 10
12	  mentions:
13	    - round: 6
14	      reviewers: [1, 2]
15	      note: "两人独立提出，最高共识。"
16	    - round: 7
17	      reviewers: [pre-review]
18	      note: "CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress."
19	    - round: 8
20	      reviewers: [1, 2]
21	      note: "Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp."
22	    - round: 9
23	      reviewers: [1, 2]
24	      note: "Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported."
25	    - round: 10
26	      reviewers: [1, 2]
27	      note: "Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations."
28	  action_items:
29	    - round: 6
30	      action: "补充至少 2-3 seeds repo-level 实验并报告 CI"
31	      assigned_to: "paper"
32	      status: resolved
33	    - round: 9
34	      action: "正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive"
35	      assigned_to: "paper"
36	      status: in_progress
37	  resolution: "CLS 3-seed ✅, TRAJ 3-seed ✅, CWM 3-seed ✅. R10 §5.4 已加 'Variant-level comparisons rely on limited seed coverage' 声明。Agent 正在补充 exploratory 标注。"
38	  resolution_round: null
39	
40	- id: "R6-N2"
41	  summary: "Checkpoint selection 系统性偏向 CLS"
42	  category: method
43	  severity: critical
44	  status: resolved
45	  first_raised_round: 6
46	  last_seen_round: 10
47	  mentions:
48	    - rou
…[truncated 24378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 896 · 2026-05-23T03:11:55.248420+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues,submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues,submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 897 · 2026-05-23T03:11:55.299015+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 898 · 2026-05-23T03:11:57.663568+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update review issues",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update review issues",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 899 · 2026-05-23T03:11:57.714182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 900 · 2026-05-23T03:12:00.475945+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit review report research director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit review report research director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 901 · 2026-05-23T03:12:00.526533+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 902 · 2026-05-23T03:15:57.359008+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.5 合并 checkpoint 证据段落，明确写入 matched epoch-3 gaps 20-23pp + CLS ablation <1pp。\"\n  resolution_round: 10\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN (excitement improved 2.5→3.0 but core contribution type unchanged). R1 AGREE on assessment but argues exceptional soundness partially compensates. Cross-sharing: R1 cites methodological demonstration value + failure mode taxonomy + 14B forward-looking insight. R2 rebuts: soundness ≠ excitement, ARR separates them for a reason. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"增加轻量 routing/ensemble 实验以提升 excitement\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验增强 equivalence 证据\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"≥14B 模型单点验证\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"所有可行 action items 已完成：标题改为 Systematic Comparison，routing 实验完成（negative result），Bayesian ROPE 完成 (P(ROPE)=0.975)，14B 单 seed 验证完成（gap ≈ 0）。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）无法通过进一步修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'\"\n      assigned_to: \"paper\"\n      status: wont_fix\n  resolution: \"R9 已在 §5.2 加入 a priori/post-hoc 分离论证。R10 Reviewer 独立审查后 BLOCK 了 'practically motivated' 修改——'a priori' 是 Lakens (2017) 标准术语，改动反而削弱防御。维持现状。\"\n  resolution_round: 10\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入 'All findings are conditioned on ≤8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish'。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.4 加入 'The ~180× data volume difference... is inherent to formulation design: per-test annotation naturally yields more training instances for the same problem set.' + downsample 标注为 single-seed comparison。\"\n  resolution_round: 10\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Ma et al., ACL 2025) 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM 真实性后加入 Related Work；加半段 CLS↔PRM/CWM↔generative verifier 映射讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: CodeRM (Ma et al., ACL 2025) 加入 Related Work，ORM/PRM 映射段落加入（CLS→PRM-like process, TRAJ→ORM-like outcome, CWM→generative verifier）。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Y-axis non-zero start acceptable for 0-3pp differences; caption annotated. R1 confirms 55% start with sufficient visual context. R2 confirms caption标注充分。\"\n  action_items:\n    - round: 10\n      action: \"Figure 2 y-axis 改从 0 开始\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Figure 2 y-axis 从约 55-80% 起始（版本差异），caption 标注 'y-axis does not start at zero'。两位 Reviewer 一致确认：对 0-3pp 差异展示，非零起始合理，caption 标注充分。\"\n  resolution_round: 11\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.4 Statistical power paragraph: n_eff≈86, power~0.3, transparent disclosure. Bayesian ROPE (P(ROPE)=0.975 CLS-CWM, 0.542 CLS-TRAJ inconclusive) independently validates. Abstract 'not confirmed after multiple comparison correction' is accurate and cautious. R1 称为 '教科书级处理'。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Abstract 'TRAJ parity differs' 改为更审慎措辞\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验补充 TOST\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"§3.4 新增 Statistical power 段落 (n_eff≈86, power~0.3, Cohen 1988)。Bayesian ROPE 完成：CLS-CWM P(ROPE)=0.975 (Jeffreys prior, ±2pp ROPE, 95% HDI [+0.10, +2.00pp])，CLS-TRAJ P(ROPE)=0.542 (inconclusive)。Abstract 改为 'not confirmed after multiple comparison correction'。TOST + Bayesian ROPE 双框架一致。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"Cross-seed oracle 94.27±2.59% 已在正文。R10 未被提出。\"\n  resolution: \"Cross-seed oracle 94.27±2.59% (3 seeds) 加入正文 §5.6。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"Appendix O 已讨论。R9/R10 均未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成（gap ≈ 0）。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。合并至 R6-N4 追踪。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Excitement consensus at 3/5. R1 Overall 3.5 (soundness compensates), R2 Overall 3.0 (excitement ceiling). Inherent limitation, wont_fix. Merged with R6-N4.\"\n  resolution: \"合并至 R6-N4。Excitement 提升至 3.0/5 但 Conference 水平仍未达到。Inherent limitation：贡献类型为 empirical comparison，无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Appendix M now includes complete GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich SEs). OR and marginal effects reported. LPM vs GEE consistency confirmed for primary effects; model identity divergence (LPM p=0.001 vs GEE p=0.410) transparently disclosed.\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Appendix M 补充 GEE logistic regression：CWM×repo interaction OR=0.31 (0.15, 0.65), p=0.002；marginal effects −0.2pp (function), −21.5pp (repo)；与 LPM 一致。Model identity LPM (p=0.002) vs GEE (p=0.410) 差异透明披露。Commit 0b38a2b 修正过强显著性声明。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching。R2 REBUT：relaxed matching 扩大 gap（26→27pp），parseable accuracy 38-43%。瓶颈是语义的。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Abstract 现使用 'not confirmed after multiple comparison correction' 措辞。\"\n  resolution: \"R10 commit a58c178: Abstract 改为 'TRAJ parity is model-dependent and not confirmed after multiple comparison correction'。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"合并至 R6-M3 追踪 Figure y-axis 问题。Agent 正在修复。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Merged with R6-M3. Figure 3 caption now includes 'Note: y-axis does not start at zero'. Both reviewers confirm resolved.\"\n  resolution: \"Figure 3 caption 标注 y-axis 不从零开始。合并至 R6-M3，一并 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-N2 讨论了 n_eff≈86 对 TOST 功效的影响。合并至 R8-W1。\"\n  resolution: \"R10 commit a58c178: §5.2 加入 TOST power 段落，明确讨论 n_eff≈86 对功效的影响。\"\n  resolution_round: 10\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 提出。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 增加一句关于语言覆盖单一性的讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Limitations 加入 'All evaluation uses Python-only benchmarks; languages with different test output conventions may exhibit different format compliance rates.'\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。'governed by' → 'moderated by'。\"\n  action_items:\n    - round: 10\n      action: \"Introduction/Conclusion 中 'governed by' 改为 'moderated by'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Introduction L8 和 L13 的 'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"正文增加半段讨论 3-shot ICL collapse 的 implication\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.4 扩展 ICL 段落 'establishing that execution-free verification requires task-specific fine-tuning regardless of formulation'。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 轻度 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"加 Appendix 目录索引\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Appendix 开头加入 mini TOC。\"\n  resolution_round: 10\n\n# === Round 11 (Continue Review) New Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 单 seed 数据点与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。14B 数据点与 4B/8B 并列但仅为 single seed，图中无视觉区分（如星号/虚线/n=1 标注）。Caption 和 Table 2 脚注有标注，但图形快速浏览时可能误读 gap reversal (-0.05pp) 的确定性。\"\n  action_items:\n    - round: 11\n      action: \"Figure 2 中 14B 数据点加视觉区分（星号/虚线/图内 n=1 标注）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"§3.5 main text 引用 LPM model identity 效应 (p=0.001) 但 GEE 给出 p=0.410，需加 qualifier\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。LPM 和 GEE 对 model identity 效应从'高度显著'到'完全不显著'的质变。正文应加 qualifier 如 'model identity reaches significance under LPM but not under GEE (Appendix M); this effect is specification-dependent'。与论文其他方面的方法论透明度标准一致。\"\n  action_items:\n    - round: 11\n      action: \"§3.5 model identity 效应加 LPM vs GEE qualifier\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示 routing 有前景，但正文数据显示 simple routing capture <0.4pp\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。Abstract 'motivate complexity-aware formulation routing over uniform selection' 暗示 routing 是有前景方向，但 §3.6 数据为负结果（<0.4pp of oracle gap ≈ 6%）。建议改为 'motivate learned complexity-aware routing'（强调 simple 不行、需 learned approach）。措辞不 technically wrong 但 abstract 应自洽。\"\n  action_items:\n    - round: 11\n      action: \"Abstract routing 措辞加限定（如 'learned' 或 'though simple heuristics capture little'）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "issues_yaml": "\n# === Round 6 Issues (Original) ===\n\n# --- Round 6 Must-Fix (Consensus Critical) ---\n\n- id: \"R6-N1\"\n  summary: \"Repo-level 核心 claims 基于 single-seed，within-formulation variance (~19pp) 与 between-formulation gap (19-26pp) 量级相当\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"两人独立提出，最高共识。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"CLS 3-seed done, TRAJ 3-seed done. CWM multi-seed training in progress.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W1 re-raises: n=48 variant MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. 3 seeds per model now complete. But model identity explains >95% predictable variance (Appendix M). Variant-level n=48, MDE≈25pp still limits repo-level inferential claims. Both reviewers agree repo-level causal claims are under-supported.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R1-W2 re-raises seed coverage (2-3 seeds for repo-level). R2 agrees. Repo-level variance > function-level, claims read as definitive but only 2-3 observations.\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.5 has explicit 'exploratory due to limited seed coverage' label. Failure mode taxonomy uses descriptive language. §3.7 reinforces 'definitive causal attribution requires multi-seed replication'. No causal claims in variant-level discussion.\"\n  action_items:\n    - round: 6\n      action: \"补充至少 2-3 seeds repo-level 实验并报告 CI\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"正文讨论 model identity dominance (Appendix M); variant-level 分析标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"§3.5 开头标注 'Variant-level comparisons (n=48) are exploratory due to limited seed coverage'。后续讨论使用描述性语言，避免 causal claims。§3.7 强调 multi-seed replication needed。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R6-N2\"\n  summary: \"Checkpoint selection 系统性偏向 CLS\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"系统性偏差方向与 observed effect 一致。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"Reviewer 确认修复充分。\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W3 re-raises checkpoint inconsistency (CWM NaN val loss → final epoch). 但 R7 的 CLS epoch ablation (<1pp) 仍有效。新角度：CWM NaN val loss 可能是 formulation-inherent。\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1 再次标为 CRITICAL。但 R2 REBUT：Section 3.5 matched epoch-3 分析显示 gap 仍 20-23pp；CLS checkpoint ablation <1pp。Director 裁定：证据表明 checkpoint 差异无法解释 18-26pp gap，降为 Should-Fix（正文更显著讨论此缓解证据）。\"\n  action_items:\n    - round: 6\n      action: \"CLS epoch ablation + matched epoch-3 解释\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 9\n      action: \"解释 CWM NaN val loss 原因（formulation-inherent vs implementation issue）\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文（非仅 Appendix）更显著讨论 checkpoint 缓解证据（matched epoch-3 gap 仍 20-23pp + CLS ablation <1pp）\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.5 合并 checkpoint 证据段落，明确写入 matched epoch-3 gaps 20-23pp + CLS ablation <1pp。\"\n  resolution_round: 10\n\n- id: \"R6-N3\"\n  summary: \"Oracle ensemble accuracy 数值矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  action_items:\n    - round: 6\n      action: \"核实并统一数字\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Oracle 90.63% 验证正确。96.03% 已删除。\"\n  resolution_round: 7\n\n- id: \"R6-N4\"\n  summary: \"Novelty 有限：核心贡献为比较已有 formulations，excitement 不足 main conference\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 建议 function-level equivalence 作为 headline。\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"W5 interaction test 充分回应 novelty concern。\"\n    - round: 8\n      reviewers: [2]\n      note: \"Fresh review R2-W2 re-raises.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1: 'design space' framing 过度. R1 部分同意.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fresh review. R2-N1 再次标 CRITICAL：三种公式均为已有方法，核心发现可从直觉预期。R1 AGREE 但认为 failure mode taxonomy 有独立贡献。两人共识：Findings 合适，Main 不够。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. R2 STILL_OPEN (excitement improved 2.5→3.0 but core contribution type unchanged). R1 AGREE on assessment but argues exceptional soundness partially compensates. Cross-sharing: R1 cites methodological demonstration value + failure mode taxonomy + 14B forward-looking insight. R2 rebuts: soundness ≠ excitement, ARR separates them for a reason. Both accept 3.0-3.5 range. Director: inherent limitation, wont_fix.\"\n  action_items:\n    - round: 9\n      action: \"标题从 'design space' 调整为 'systematic comparison'\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"增加轻量 routing/ensemble 实验以提升 excitement\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验增强 equivalence 证据\"\n      assigned_to: \"experiment\"\n      status: resolved\n    - round: 10\n      action: \"≥14B 模型单点验证\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"所有可行 action items 已完成：标题改为 Systematic Comparison，routing 实验完成（negative result），Bayesian ROPE 完成 (P(ROPE)=0.975)，14B 单 seed 验证完成（gap ≈ 0）。Excitement 从 2.5 提升至 3.0，但核心贡献类型（empirical comparison of existing formulations）无法通过进一步修改改变。Novelty ceiling 为 inherent limitation。\"\n  resolution_round: 11\n\n# --- Round 6 Should-Fix ---\n\n- id: \"R6-W1\"\n  summary: \"SESOI ±2pp 的 a priori 属性值得商榷\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"SESOI 基于训练噪声量级独立于 observed gap.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人独立 re-raise。缺 domain-specific justification.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W4 re-raises：±2pp 依赖于 accuracy range 和 test set size，更接近 post-hoc rationalization。R2 部分同意，建议重新定位为 'practically motivated with robustness check'。\"\n  action_items:\n    - round: 9\n      action: \"§3.4 加 domain-grounded SESOI justification; 正文引用 Appendix J sensitivity\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"SESOI 描述从 'a priori' 改为 'practically motivated'\"\n      assigned_to: \"paper\"\n      status: wont_fix\n  resolution: \"R9 已在 §5.2 加入 a priori/post-hoc 分离论证。R10 Reviewer 独立审查后 BLOCK 了 'practically motivated' 修改——'a priori' 是 Lakens (2017) 标准术语，改动反而削弱防御。维持现状。\"\n  resolution_round: 10\n\n- id: \"R6-W2\"\n  summary: \"CWM regime qualifier 不充分——Abstract/Conclusion 缺少 ≤8B LoRA 限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 7\n      reviewers: [pre-review]\n      note: \"3+ 处修复完成。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Abstract 仍比 Conclusion 缺 qualifier.\"\n    - round: 9\n      reviewers: []\n      note: \"本轮未被独立提出。Abstract 已含 '≤8B LoRA protocol' qualifier。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标为 CRITICAL：≤8B 限制严重威胁泛化性。R1 部分 REBUT（4B→8B gap 扩大）但同意 abstract 需限定。两人共识：abstract/conclusion 应明确 '≤8B LoRA regime' 限定。\"\n  action_items:\n    - round: 8\n      action: \"Abstract 加 'under our ≤8B LoRA protocol'\"\n      assigned_to: \"agent\"\n      status: resolved\n    - round: 10\n      action: \"Conclusion 也加 ≤8B LoRA 限定；讨论更大规模下结论可能如何变化\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Abstract 已有 '≤8B LoRA protocol'，Conclusion 加入 'All findings are conditioned on ≤8B LoRA fine-tuning; at larger scale, the generation bottleneck may diminish'。\"\n  resolution_round: 10\n\n- id: \"R6-W3\"\n  summary: \"Re-repair δ=0 与 diagnostic granularity 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"降级 diagnostic granularity\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"Contributions 4→3, diagnostic granularity 降级为 pending validation.\"\n  resolution_round: 7\n\n- id: \"R6-W4\"\n  summary: \"TRAJ 训练配置差异 (~400 vs ~70K) 且信号粒度不同\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2-W6: 175× 数据量差异.\"\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W4: downsample ablation 仅 1 model × 1 seed × 1 level.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises：180× 差异 + signal granularity (per-test vs variant-level) 无法通过 volume matching 解决。R2 AGREE。两人共识：应将 TRAJ 数据量/信号粒度限制框架为 formulation 固有属性。\"\n  action_items:\n    - round: 9\n      action: \"扩展 downsample ablation 至 ≥2 models 或明确标注为 limitation\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文明确将 TRAJ data volume/signal granularity 差异框架为 formulation 固有属性而非可控实验变量\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.4 加入 'The ~180× data volume difference... is inherent to formulation design: per-test annotation naturally yields more training instances for the same problem set.' + downsample 标注为 single-seed comparison。\"\n  resolution_round: 10\n\n- id: \"R6-W5\"\n  summary: \"Interaction 未做统计检验\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"Interaction test z=-23.7 完成，在 §3.5 和 Appendix M 报告。\"\n  resolution_round: 9\n\n- id: \"R6-W6\"\n  summary: \"合成 mutation 外部效度\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Appendix Extended Limitations 讨论充分。\"\n  resolution_round: 7\n\n- id: \"R6-W7\"\n  summary: \"Abstract 偏短 (~120-130 词)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"185 词，含 function-level equivalence + phase transition.\"\n  resolution_round: 7\n\n- id: \"R6-W8\"\n  summary: \"遗漏近期相关工作\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Aletheia/VeRPO/ExecVerify.\"\n    - round: 7\n      reviewers: [pre-review]\n      note: \"三篇已加入。\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"新增: GenRM, RepoExec, Chen et al.\"\n    - round: 9\n      reviewers: [2]\n      note: \"R2-W5: CodeScaler. 另提 GenPRM, ExecVerify.\"\n    - round: 10\n      reviewers: [2]\n      note: \"R2-W2: CodeRM (Ma et al., ACL 2025) 未引用。另需加强 ORM/PRM 框架映射讨论。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"验证 CodeRM 真实性后加入 Related Work；加半段 CLS↔PRM/CWM↔generative verifier 映射讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: CodeRM (Ma et al., ACL 2025) 加入 Related Work，ORM/PRM 映射段落加入（CLS→PRM-like process, TRAJ→ORM-like outcome, CWM→generative verifier）。\"\n  resolution_round: 10\n\n# --- Round 6 Minor ---\n\n- id: \"R6-M1\"\n  summary: \"Tables 缺少次优下划线\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"Tables 1-3 bold+underline 完成。\"\n  resolution_round: 7\n\n- id: \"R6-M2\"\n  summary: \"Checklist C4 version numbers\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"C4 已列出版本号。\"\n  resolution_round: 7\n\n- id: \"R6-M3\"\n  summary: \"Figure 2 信息密度偏低 / y-axis 截断\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"bar labels 偏小.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-M2: y-axis 不从零开始（55%），视觉夸大 gap。R2 AGREE。Caption 已标注但对快速浏览读者可能误导。视觉审查也标记。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Y-axis non-zero start acceptable for 0-3pp differences; caption annotated. R1 confirms 55% start with sufficient visual context. R2 confirms caption标注充分。\"\n  action_items:\n    - round: 10\n      action: \"Figure 2 y-axis 改从 0 开始\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Figure 2 y-axis 从约 55-80% 起始（版本差异），caption 标注 'y-axis does not start at zero'。两位 Reviewer 一致确认：对 0-3pp 差异展示，非零起始合理，caption 标注充分。\"\n  resolution_round: 11\n\n# === Round 8 (Fresh Review) Issues ===\n\n- id: \"R8-C1\"\n  summary: \"TOST p=0.007 归属混淆: §5.2 将 CLS-TRAJ gap 与 CLS-CWM p 值混在一起\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 分开呈现。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-C2\"\n  summary: \"Abstract 对 repo-level CWM 结论缺少 regime qualifier + z=-23.7 缺 model 标注\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract qualifier 和 model 标注已加入。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W1\"\n  summary: \"n=48 variant 样本量导致 TOST 统计功效不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"MDE≈25pp.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R1-W1 re-raises. 两人共识: variant-level 分析应标注为 exploratory/descriptive。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1-N2 标 CRITICAL：TOST power ~0.3 for medium effect。CLS-TRAJ adjusted p=0.075 未通过 Holm-Bonferroni。R2 AGREE 并升级关注度。两人共识：Abstract 措辞需更审慎。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. §3.4 Statistical power paragraph: n_eff≈86, power~0.3, transparent disclosure. Bayesian ROPE (P(ROPE)=0.975 CLS-CWM, 0.542 CLS-TRAJ inconclusive) independently validates. Abstract 'not confirmed after multiple comparison correction' is accurate and cautious. R1 称为 '教科书级处理'。\"\n  action_items:\n    - round: 9\n      action: \"Variant-level 分析明确标注为 exploratory/descriptive\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"正文讨论 TOST 功效限制；Abstract 'TRAJ parity differs' 改为更审慎措辞\"\n      assigned_to: \"paper\"\n      status: resolved\n    - round: 10\n      action: \"Bayesian ROPE 等价性检验补充 TOST\"\n      assigned_to: \"experiment\"\n      status: resolved\n  resolution: \"§3.4 新增 Statistical power 段落 (n_eff≈86, power~0.3, Cohen 1988)。Bayesian ROPE 完成：CLS-CWM P(ROPE)=0.975 (Jeffreys prior, ±2pp ROPE, 95% HDI [+0.10, +2.00pp])，CLS-TRAJ P(ROPE)=0.542 (inconclusive)。Abstract 改为 'not confirmed after multiple comparison correction'。TOST + Bayesian ROPE 双框架一致。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R8-W2\"\n  summary: \"Oracle 互补性估计为单种子、无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 9\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Repo 95.83% CI ~[85.7%, 99.5%].\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2-Q4 re-raises: single-seed oracle 跨 seed 稳定性未验证。\"\n    - round: 10\n      reviewers: []\n      note: \"Cross-seed oracle 94.27±2.59% 已在正文。R10 未被提出。\"\n  resolution: \"Cross-seed oracle 94.27±2.59% (3 seeds) 加入正文 §5.6。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W3\"\n  summary: \"CWM checkpoint 消融不对称——Qwen3 缺 early-stopping 评估\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 9\n      reviewers: []\n      note: \"Appendix 已讨论 Qwen3 CWM 无 epoch-level checkpoint。\"\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Appendix O 讨论了 Qwen3 仅有 step-level checkpoints。\"\n  resolution: \"Appendix O 已讨论。R9/R10 均未再被提出。\"\n  resolution_round: 10\n\n- id: \"R8-W4\"\n  summary: \"z=-23.7 interaction 仅基于 DeepSeek-Coder，Abstract/Intro 未标注\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Abstract 已标注 model。\"\n  resolution_round: 10\n\n- id: \"R8-W5\"\n  summary: \"遗漏 GenRM (ICLR 2025) + RepoExec + Chen et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"GenRM, CodeScaler, GenPRM 已加入 Related Work。\"\n  resolution_round: 10\n\n- id: \"R8-W6\"\n  summary: \"CWM baseline 偏弱 (≤8B LoRA vs 原始 32B+mid-training)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director 裁定 Should-Fix.\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-N2 标 CRITICAL。R1 部分 REBUT（4B→8B gap 扩大数据）。两人共识：abstract/conclusion 需 ≤8B 限定。\"\n  resolution: \"合并至 R6-W2。Abstract + Conclusion 均已加入 ≤8B LoRA 限定。14B 验证实验完成（gap ≈ 0）。\"\n  resolution_round: 10\n\n- id: \"R8-W7\"\n  summary: \"Novelty 是否足够 Conference 水平\"\n  category: framing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"DIVERGENT. Director: Findings track 合适.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"两人 Excitement 均为 2.5/5. R2 评 3.0 (Findings), R1 评 3.5 (Borderline Conference).\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 Excitement 2.5/5. 两人共识：Findings 合适。合并至 R6-N4 追踪。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Excitement consensus at 3/5. R1 Overall 3.5 (soundness compensates), R2 Overall 3.0 (excitement ceiling). Inherent limitation, wont_fix. Merged with R6-N4.\"\n  resolution: \"合并至 R6-N4。Excitement 提升至 3.0/5 但 Conference 水平仍未达到。Inherent limitation：贡献类型为 empirical comparison，无法通过修改改变。\"\n  resolution_round: 11\n\n# --- Round 8 Minor ---\n\n- id: \"R8-M1\"\n  summary: \"混合精度 (bfloat16/NF4) 对 TOST 的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"§3.4 footnote 充分讨论。R10 未被提出。\"\n  resolution_round: 10\n\n- id: \"R8-M2\"\n  summary: \"LPM 未报告 robust SEs; prompt templates 未展示; scaling 2-seed power 极低\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 11\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"R1-W5: HC1 不 account for residual within-cluster correlation.\"\n    - round: 10\n      reviewers: [1]\n      note: \"R1-M1: 建议在 Appendix M 并列展示 logistic regression odds ratios。R2 AGREE。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Both RESOLVED. Appendix M now includes complete GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich SEs). OR and marginal effects reported. LPM vs GEE consistency confirmed for primary effects; model identity divergence (LPM p=0.001 vs GEE p=0.410) transparently disclosed.\"\n  action_items:\n    - round: 10\n      action: \"Appendix M 补充 logistic regression marginal effects 或 odds ratios\"\n      assigned_to: \"agent\"\n      status: resolved\n  resolution: \"Appendix M 补充 GEE logistic regression：CWM×repo interaction OR=0.31 (0.15, 0.65), p=0.002；marginal effects −0.2pp (function), −21.5pp (repo)；与 LPM 一致。Model identity LPM (p=0.002) vs GEE (p=0.410) 差异透明披露。Commit 0b38a2b 修正过强显著性声明。R11 两位 Reviewer 一致确认 RESOLVED。\"\n  resolution_round: 11\n\n# === Round 9 (Fresh Review) Issues ===\n\n- id: \"R9-C1\"\n  summary: \"'Design space' framing 过度——实际只比较三个已知 formulation，标题与贡献不匹配\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"标题已改为 Systematic Comparison。\"\n  resolution_round: 10\n\n- id: \"R9-W1\"\n  summary: \"CWM 评估指标非对称性（exact matching + majority-class default）未量化\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-W3 re-raises exact string matching。R2 REBUT：relaxed matching 扩大 gap（26→27pp），parseable accuracy 38-43%。瓶颈是语义的。\"\n  resolution: \"R2 REBUT 成功：relaxed matching 扩大而非缩小 gap，parseable accuracy 远低于 majority baseline。\"\n  resolution_round: 10\n\n- id: \"R9-W2\"\n  summary: \"DeepSeek 仅 2 seeds 却在 Abstract 声称 'model-dependent'——泛化性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"本轮未被提出。Abstract 现使用 'not confirmed after multiple comparison correction' 措辞。\"\n  resolution: \"R10 commit a58c178: Abstract 改为 'TRAJ parity is model-dependent and not confirmed after multiple comparison correction'。R10 未再被提出。\"\n  resolution_round: 10\n\n- id: \"R9-M1\"\n  summary: \"Figure 3 (Appendix) y-axis 不从 0 开始但未标注\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 11\n  mentions:\n    - round: 10\n      reviewers: []\n      note: \"合并至 R6-M3 追踪 Figure y-axis 问题。Agent 正在修复。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Continue review. Merged with R6-M3. Figure 3 caption now includes 'Note: y-axis does not start at zero'. Both reviewers confirm resolved.\"\n  resolution: \"Figure 3 caption 标注 y-axis 不从零开始。合并至 R6-M3，一并 RESOLVED。\"\n  resolution_round: 11\n\n- id: \"R9-M2\"\n  summary: \"Abstract 第一句过于绝对 ('relies on')\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"已改为 'increasingly leverages'。\"\n  resolution_round: 10\n\n- id: \"R9-M3\"\n  summary: \"缺少方法论引用：Wellek (2010) 等价检验教材, Moulton (1990) clustered data\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"两篇已引用。\"\n  resolution_round: 10\n\n- id: \"R9-M4\"\n  summary: \"Clustered bootstrap 实施细节（resample unit, block size）未说明\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"§3.1 已说明 resample unit。\"\n  resolution_round: 10\n\n- id: \"R9-M5\"\n  summary: \"Repo-level DEFF=114.3 → effective n≈86 未在正文讨论对推断的影响\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1]\n      note: \"R1-N2 讨论了 n_eff≈86 对 TOST 功效的影响。合并至 R8-W1。\"\n  resolution: \"R10 commit a58c178: §5.2 加入 TOST power 段落，明确讨论 n_eff≈86 对功效的影响。\"\n  resolution_round: 10\n\n# === Round 10 (Fresh Review) New Issues ===\n\n- id: \"R10-W1\"\n  summary: \"Python-only 评估未在 Limitations 提及\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-W1 提出。R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"Limitations 增加一句关于语言覆盖单一性的讨论\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Limitations 加入 'All evaluation uses Python-only benchmarks; languages with different test output conventions may exhibit different format compliance rates.'\"\n  resolution_round: 10\n\n- id: \"R10-W2\"\n  summary: \"'formulation choice is governed by code complexity' 等 overclaim 措辞\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M1 提出，R1 AGREE。'governed by' → 'moderated by'。\"\n  action_items:\n    - round: 10\n      action: \"Introduction/Conclusion 中 'governed by' 改为 'moderated by'\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Introduction L8 和 L13 的 'governed by' 改为 'moderated by'。\"\n  resolution_round: 10\n\n- id: \"R10-M1\"\n  summary: \"3-shot ICL collapse 发现仅正文一句带过，未充分讨论 implication\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M2 提出，R1 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"正文增加半段讨论 3-shot ICL collapse 的 implication\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: §5.4 扩展 ICL 段落 'establishing that execution-free verification requires task-specific fine-tuning regardless of formulation'。\"\n  resolution_round: 10\n\n- id: \"R10-M2\"\n  summary: \"Appendix 16 个（A-P），导航不便\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"R2-M3 提出，R1 轻度 AGREE。\"\n  action_items:\n    - round: 10\n      action: \"加 Appendix 目录索引\"\n      assigned_to: \"paper\"\n      status: resolved\n  resolution: \"R10 commit a58c178: Appendix 开头加入 mini TOC。\"\n  resolution_round: 10\n\n# === Round 11 (Continue Review) New Issues ===\n\n- id: \"R11-M1\"\n  summary: \"Figure 2 中 14B 单 seed 数据点与多 seed 数据点视觉等权，可能导致 gap reversal 被过度解读\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。14B 数据点与 4B/8B 并列但仅为 single seed，图中无视觉区分（如星号/虚线/n=1 标注）。Caption 和 Table 2 脚注有标注，但图形快速浏览时可能误读 gap reversal (-0.05pp) 的确定性。\"\n  action_items:\n    - round: 11\n      action: \"Figure 2 中 14B 数据点加视觉区分（星号/虚线/图内 n=1 标注）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M2\"\n  summary: \"§3.5 main text 引用 LPM model identity 效应 (p=0.001) 但 GEE 给出 p=0.410，需加 qualifier\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE。LPM 和 GEE 对 model identity 效应从'高度显著'到'完全不显著'的质变。正文应加 qualifier 如 'model identity reaches significance under LPM but not under GEE (Appendix M); this effect is specification-dependent'。与论文其他方面的方法论透明度标准一致。\"\n  action_items:\n    - round: 11\n      action: \"§3.5 model identity 效应加 LPM vs GEE qualifier\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R11-M3\"\n  summary: \"Abstract 'motivate routing' 暗示 routing 有前景，但正文数据显示 simple routing capture <0.4pp\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 AGREE。Abstract 'motivate complexity-aware formulation routing over uniform selection' 暗示 routing 是有前景方向，但 §3.6 数据为负结果（<0.4pp of oracle gap ≈ 6%）。建议改为 'motivate learned complexity-aware routing'（强调 simple 不行、需 learned approach）。措辞不 technically wrong 但 abstract 应自洽。\"\n  action_items:\n    - round: 11\n      action: \"Abstract routing 措辞加限定（如 'learned' 或 'though simple heuristics capture little'）\"\n      assigned_to: \"paper\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# === Prior Round Issues (unchanged) ===\n\n- id: \"R5-W1\"\n  summary: \"正文超 8 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"已压缩至 8 页。\"\n  resolution_round: 6\n\n- id: \"R5-W2\"\n  summary: \"TRAJ checkpoint 不一致\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"透明报告 + R6-N2 resolved。\"\n  resolution_round: 6\n\n- id: \"R5-W3\"\n  summary: \"Table 4 混合指标\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 5\n  resolution: \"Table 3 含 Variant Acc 列。\"\n  resolution_round: 6\n\n- id: \"R4-N1\"\n  summary: \"TOST sensitivity analysis\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W1 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W1\"\n  summary: \"CWM ≤8B LoRA qualifier\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"通过 R6-W2 修复。\"\n  resolution_round: 7\n\n- id: \"R4-W2\"\n  summary: \"Abstract 数据堆砌\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"通过 R6-W7 修复（185 词）。\"\n  resolution_round: 7\n\n- id: \"R4-W3\"\n  summary: \"Cross-model 措辞过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"已改为 consistency check。\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"多重比较\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"Holm-Bonferroni (k=4) 完成。\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"Related Work 遗漏\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  resolution: \"引用无幻觉。\"\n  resolution_round: 5\n\n- id: \"R3-W1\"\n  summary: \"Limitations 非独立 section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  resolution: \"独立 section 已有。\"\n  resolution_round: 5\n"
  }
}
```

</details>

---


### Tool result

_source line 903 · 2026-05-23T03:15:57.511971+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/review_issues.yaml\", \"bytes\": 28435}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0ae20ec1ce60f9c0589d629648584eff:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---
