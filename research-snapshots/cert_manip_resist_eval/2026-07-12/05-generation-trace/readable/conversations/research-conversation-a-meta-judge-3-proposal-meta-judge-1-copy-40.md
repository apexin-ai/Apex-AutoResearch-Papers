# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/4b04dab1-638b-4822-9511-61b3944e7174.jsonl`
- **Structured JSON:** [`59c2b41cfa0e1ccaaf60.json`](../../sessions/59/59c2b41cfa0e1ccaaf60.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:30:18.803Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:30:18.803Z",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information for a thorough evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命问题：投稿 venue 完全不匹配】\n\n本 proposal 拟投 CoRL 2026（Conference on Robot Learning）。\nCoRL 的 Call for Papers 明确声明：\"Submissions without a robotics focus will be returned without review.\"\nCoRL 接收的主题包括：robot manipulation, navigation, locomotion, driving, flight, \nreinforcement learning for physical robots, robot foundation models, sim-to-real transfer 等。\n\n本 proposal 的内容是 LLM-mediated social science annotation pipeline 的多元宇宙分析方法——\n这是一篇纯粹的 NLP + 社会科学方法论论文，与机器人学习无任何关联。\nproposal 自身列出的 target venues 也是 AAAI 2027、TACL、CSCW、EMNLP、FAccT，没有 CoRL。\n\n→ 投 CoRL 2026 主会的中稿概率本质上为 0%（desk reject without review）。\n\n以下仍按要求对 idea 本身的质量进行客观评估（适用于 proposal 自身列出的 target venues）。\n\n═══════════════════════════════════════════════════════════\n\n【领域调研】:\n\n- [Baumann et al., \"Large Language Model Hacking\", arXiv 2509.08825] (2025): \n  在 18 个 LLM × 37 个标注任务 × 2,361 个假设上系统测试，发现 ~31% 的假设在 SOTA 模型上得出 \n  错误结论。文档化了问题规模，测试了 21 种 ad-hoc 缓解策略，但未提供形式化多元宇宙推断框架。\n  本 proposal 的核心 motivating paper，数据公开（MIT 许可），paper 真实存在。\n\n- [McLaren et al., \"Magic Words or Methodical Work?\", arXiv 2603.26898] (March 2026): \n  在政治科学标注中系统变异 model, prompt template, learning approach。核心发现：交互效应 \n  主导主效应。但设计是 one-factor-at-a-time（非 full factorial），未产生 specification curve \n  或联合推断检验。问题是\"哪个 pipeline 最好\"而非\"结论是否跨 pipeline 稳健\"。\n  本 proposal 将其定位为互补性 benchmarking 工作——这个定位是准确的。\n\n- [Auspurg, \"Robustness is better assessed with a few thoughtful models than with billions \n  of regressions\", PNAS 2025]: \n  批评暴力多元宇宙分析，论点是：包含 misspecified 模型会淹没有效模型。\n  本 proposal 引用准确，且其反驳论点（LLM annotation 中无配置是 statistically misspecified，\n  estimand 恒定）有合理性。\n\n- [Ganslmeier & Vlandas, \"Reply to Auspurg\", PNAS 2025]: \n  回应 Auspurg，认为\"何为 justified model\"本身是有争议的。\n  proposal 引用准确。\n\n- [Del Giudice & Gangestad, \"A Traveler's Guide to the Multiverse\", AMPPS 2021]: \n  提出 E/N/U（Equivalence/Nonequivalence/Uncertainty）分类框架。\n  这是心理学方法论文献中的重要 reference，proposal 的改编思路（将 E/N/U 从分析决策迁移到 \n  LLM pipeline 配置决策）是合理的跨领域迁移。\n\n- [Kosch & Feger, \"Prompt-Hacking: The New p-Hacking?\", CACM 2026]: \n  概念性类比文章，指出 prompt 调整等同于 p-hacking。无形式化方法。\n  proposal 引用准确——定位为\"概念类比但无方法\"。\n\n- [Ye et al., \"Navigating the Conceptual Multiverse\", arXiv 2604.17815] (April 2026): \n  将多元宇宙思维应用于 LLM 概念框架，是交互式 HCI 系统，不涉及 annotation pipeline 或统计推断。\n  proposal 的差异化定位准确。\n\n- [Mehrotra et al., \"Multi-Perspective LLM Annotations\", arXiv 2603.21404] (March 2026): \n  Perspective-Driven Inference，处理主观任务中跨人口群体的分歧，但假设每个 perspective 只有 \n  单一 pipeline。不涉及多元宇宙方法。proposal 差异化准确。\n\n- [Gligorić et al., \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\", \n  NAACL 2025]: \n  Prediction-Powered Inference 路线——用少量人工标注校准 LLM 标注的测量误差。\n  与本 proposal 互补但方法论不同：PPI 修正单一 pipeline 的 bias，multiverse 检测跨 pipeline 的 \n  inferential (in)stability。proposal 未充分讨论与 PPI 方法的关系——这是一个 related work gap。\n\n- [Simonsohn et al., \"Specification Curve Analysis\", Nature Human Behaviour 2020]: \n  经典方法，proposal 直接改编，引用准确。\n\n- 调研总结：该领域呈现\"问题已被充分文档化，但形式化方法学框架缺位\"的格局。Baumann 等量化了 \n  问题规模，McLaren 等展示了交互效应，Kosch & Feger 画了概念类比，Carlson & Burbano 呼吁 \n  sensitivity analysis，但截至 2026 年 5 月，确实没有论文将 specification curve analysis / \n  formal multiverse methodology 应用于 LLM annotation pipeline。Proposal 占据了一个真实的空白。\n\n\n【Trivial Alternative 检验】:\n\n存在两个值得考虑的 trivial alternative：\n\n1. \"Just run N configs and report range\"：研究者可以简单地选择 5-10 个\"合理\"配置，运行所有配置，\n   报告效应量的范围和符号一致性——不需要 E/N/U 分类、不需要 Boba DSL、不需要形式化 specification \n   curve。这种\"穷人版 sensitivity analysis\"在实践中可能达到 80% 的效果。\n   → 本 proposal 的增量价值在于：(a) 形式化的联合推断检验（permutation-based joint inference）\n   提供了统计意义上的 robust/fragile 分类，而非 ad-hoc 判断；(b) 方差分解量化了哪些维度贡献最多 \n   不稳定性；(c) E/N/U 提供了配置选择的理论基础。但这个增量是否足够\"surprising\"是关键问题。\n\n2. Prediction-Powered Inference (PPI) 路线（Gligorić et al., NAACL 2025）：\n   如果目标是获得可靠的下游推断，PPI 通过少量人工标注直接校正测量误差，可能是一个更优雅的解决方案。\n   → 本 proposal 与 PPI 的关系是互补的（multiverse 检测 instability，PPI 修正 bias），但 \n   proposal 需要更清晰地论证为什么\"检测哪些结论 fragile\"比\"直接修正 bias\"更有价值。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有三个未充分验证的环节：\n\n1. E/N/U 分类的可操作性假设：proposal 假设研究者可以对每个 pipeline 维度做出 E/N/U 分类，\n   但这个分类本身是主观的。什么证据支持 temperature=0 对分类任务\"objectively superior\"？\n   如果不同标注者对 E/N/U 分类有分歧（meta-multiverse 问题），整个框架的基础就不稳固。\n   这不是致命的，但需要 inter-rater reliability 验证。\n\n2. \"Estimand 恒定\"假设：proposal 论证 Auspurg 的批评不适用于 LLM annotation，因为 \"estimand \n   remains constant across configurations\"。但这只在所有配置确实在测量同一概念时才成立。如果不同 \n   prompt framings 实际上激活了 LLM 对概念的不同理解（e.g., \"toxicity\" vs. \"offensiveness\"），\n   那么 estimand 并非恒定——Auspurg 的批评就部分适用。这个假设需要更细致的论证。\n\n3. \"No configuration is statistically misspecified\" 假设：temperature=1.0 + 无 system prompt \n   + numerical output parsing 对严肃的分类任务来说，显然是一个\"worse\" 配置。如果 E/N/U 分类 \n   已经排除了这些配置，那么这个假设是 trivially true by construction——但这也削弱了\"Auspurg \n   的批评不适用\"这个论证的力度，因为你实际上已经在做 Auspurg 建议的事情（pruning bad specs）。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：核心贡献是跨领域方法迁移——将心理学/经济学中成熟的 specification curve analysis \n   (Simonsohn et al., 2020) 和 E/N/U 框架 (Del Giudice & Gangestad, 2021) 移植到 LLM \n   annotation pipeline。这个特定组合确实是新的——我的调研未发现任何现有论文做了这件事。\n   然而，novelty 的本质是\"apply method X to domain Y\"，各组件均已存在。E/N/U 的 adaptation \n   增加了一定的智识贡献，但不构成方法论上的根本创新。与 Ye et al. (2604.17815) 相比，本 \n   proposal 更面向统计推断（更严谨），但 novelty profile 类似（都是跨领域迁移）。\n   最关键的是：如果实验结果 positive（某些结论 robust、某些 fragile、model choice 贡献最大方差），\n   审稿人很可能会说 \"I would have guessed this\"。\n\n2. Significance: 【中偏强】\n   理由：研究问题genuinely重要。Baumann et al. (2025) 的 31% error rate 和 McLaren et al. \n   (2026) 的 interaction effects 证明问题真实存在且规模不小。Carlson & Burbano (SMJ 2026) \n   明确呼吁 sensitivity analysis，NLP+CSS 社区 explicitly 寻求 \"LLMs for measurement and \n   downstream statistical inference\" 方面的工作。开源 toolkit 有实际应用价值。\n   限制因素：这是一个\"方法论/工具\"贡献而非\"发现\"贡献。它的影响力取决于社区是否采用该框架——\n   而这类框架在 NLP 社区的采用率历史上不高（specification curve 在心理学中也花了数年才普及）。\n\n3. Related Work: 【强】\n   理由：覆盖异常全面。proposal 对 Baumann et al., McLaren et al., Auspurg/Ganslmeier & \n   Vlandas 辩论, Ye et al., Mehrotra et al., Gligorić et al., Kosch & Feger 的描述经核实 \n   均准确。与每篇工作的差异化定位清晰且合理。Auspurg 辩论的引入为方法论立场提供了有力的学术背景。\n   唯一 gap：与 PPI 方法 (Gligorić et al., NAACL 2025) 的对比不够充分——需要明确论证 \n   multiverse approach vs. measurement error correction approach 各自的适用场景。\n\n\n【概率估计】: \n  - 投 CoRL 2026 主会: 0-2%（venue 完全不匹配，desk reject）\n  - 投 proposal 自身列出的 venues（AAAI/TACL/EMNLP/CSCW/FAccT）: [25% - 38%] 中位 30%\n\n【估计理由】: \n  idea 占据了一个真实的文献空白——形式化多元宇宙方法 × LLM annotation pipeline 确实无人做过。\n  问题的重要性有充分的文献支撑（Baumann 31% error rate, McLaren interaction effects, \n  Carlson & Burbano 的呼吁）。Related work 覆盖全面且定位准确。\n  \n  限制上界的是 Novelty 维度：核心智识贡献是\"apply existing method to new domain\"，各组件\n  （specification curve, E/N/U, variance decomposition）均为现成工具。如果核心发现是 \n  \"model choice 和 prompt 贡献最大方差，有些结论 robust 有些 fragile\"，这不会让审稿人 \n  surprised。此外，Trivial Alternative 威胁（简单跑 N 个 config 报告 range）和 PPI 替代 \n  路线都会被 well-informed reviewer 提出。\n  \n  投 CoRL 的 0% 是因为 topic 与 venue scope 完全正交——这不是\"fit 不太好\"而是\"完全不 fit\"。\n\n【主要风险】:\n1. 【CoRL 投稿: 致命】venue 完全不匹配，会被 desk reject。建议改投 proposal 自身已列出的 \n   AAAI 2027 或 TACL。\n2. 【Idea 层面】核心发现的 \"surprisingness\" 不足——审稿人可能认为 \"of course pipeline choices \n   matter and interact, we already knew that from Baumann/McLaren, this just puts a formal \n   framework around it\"，导致 novelty 评分偏低。需要在 framing 上强调 formal joint inference \n   带来的 qualitatively new insight（例如某些被认为 robust 的经典社科发现实际上 fragile，或者 \n   反直觉的方差分解结果）。\n```\n\n**Sources:**\n- [Baumann et al. - LLM Hacking (arXiv 2509.08825)](https://arxiv.org/abs/2509.08825)\n- [McLaren et al. - Magic Words or Methodical Work (arXiv 2603.26898)](https://arxiv.org/abs/2603.26898)\n- [Auspurg - Robustness (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Del Giudice & Gangestad - Traveler's Guide (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Kosch & Feger - Prompt-Hacking (CACM 2026)](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)\n- [Ye et al. - Navigating the Conceptual Multiverse (arXiv 2604.17815)](https://arxiv.org/abs/2604.17815)\n- [Mehrotra et al. - Multi-Perspective LLM Annotations (arXiv 2603.21404)](https://arxiv.org/abs/2603.21404)\n- [Gligorić et al. - Unconfident LLM Annotations (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to make my assessment. Let me note one critical finding from my research: **CoRL (Conference on Robot Learning) is a robotics conference**, and this proposal is about LLM annotation methodology for social science. Let me write up the full evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【致命问题 — 投稿目标与论文主题完全不匹配】\n\n在进入正式 rubric 之前，必须首先指出：**这篇 proposal 投稿 CoRL 2026（Conference on Robot Learning）是一个根本性的错误。**\n\nCoRL 2026 的 Call for Papers 明确要求论文 \"focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\"，涵盖领域包括 imitation learning、reinforcement learning for robots、sim-to-real transfer、robot perception、learned manipulation/locomotion、learning-based planning 等。\n\n本 proposal 的主题是「LLM 注释管道的多元宇宙分析框架」——一项计算社会科学方法论工作，涉及 specification curve analysis、variance decomposition、E/N/U 分类框架。**它与机器人学习没有任何交集。** 该论文自身列出的目标会议（AAAI 2027, TACL, CSCW 2027, EMNLP 2026 Industry Track, FAccT 2027）也完全不包含 CoRL。\n\n**投 CoRL 的结果：大概率 desk reject（编辑直接拒稿，不进入审稿流程）。**\n\n以下评估将按要求完成 idea 质量的客观分析，但概率估计针对的是 CoRL 2026 这个具体场景。我会同时给出\"如果投到合适的 venue（如 EMNLP/AAAI/TACL）\"的参考概率。\n\n---\n\n【领域调研】:\n\n1. **Baumann et al. (arXiv 2509.08825, 2025)** \"Large Language Model Hacking\": 18 个 LLM × 37 个注释任务 × 1300 万标签，发现约 31% 的假设因 LLM 配置选择得出错误结论。这是本 proposal 的核心动机来源，论文真实存在，描述准确。\n\n2. **McLaren et al. (arXiv 2603.26898, March 2026)** \"Magic Words or Methodical Work?\": 在政治科学 LLM 注释中系统变化 model/prompt/learning approach，发现交互效应主导主效应。但使用 one-at-a-time 变化设计，无 joint inference。论文真实存在，描述准确。\n\n3. **Kosch & Feger (CACM 2026, arXiv 2504.14571)** \"Prompt-Hacking: The New p-Hacking?\": 概念性类比文章，画了 prompt-hacking 与 p-hacking 的平行关系，但未提出正式方法。真实存在，描述准确。\n\n4. **Auspurg (PNAS 2025)** \"Robustness is better assessed with a few thoughtful models than with billions of regressions\": 批评 Ganslmeier & Vlandas 的暴力多元宇宙分析，认为只有当所有模型同等合理时多元宇宙分析才有信息量。真实存在，描述准确。Ganslmeier & Vlandas 的 reply 也真实存在。\n\n5. **Del Giudice & Gangestad (AMPPS 2021)** \"A Traveler's Guide to the Multiverse\": 提出 E/N/U 分类框架（Equivalence/Nonequivalence/Uncertainty）。真实存在，描述准确。\n\n6. **Ye et al. (arXiv 2604.17815, April 2026)** \"Navigating the Conceptual Multiverse\": 将多元宇宙思维应用于 LLM 概念框架的交互式 HCI 系统，但不涉及注释管道或统计推断。真实存在，描述准确。\n\n7. **Mehrotra et al. (arXiv 2603.21404, March 2026)** \"Multi-Perspective LLM Annotations\": 针对主观任务引入 Perspective-Driven Inference。真实存在。\n\n8. **Carlson & Burbano (SMJ 2026)**: 关于管理学研究中 LLM 注释的基础性指南，推荐 sensitivity analysis 但未提供正式方法论。真实存在。\n\n- **调研总结**: 该领域正处于从\"发现问题\"（Baumann: 31% 错误率；McLaren: 交互效应主导）到\"系统解决问题\"的转折期。多个工作从不同角度描述了 LLM 注释管道中的研究者自由度问题（Kosch 概念层面、Carlson 指南层面、McLaren 实证层面），但确实尚无工作将正式的多元宇宙分析 + joint inference 方法论应用于 LLM 注释管道。这个 gap 是真实的。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁，但 proposal 对其有部分回应。**\n\n最直接的 trivial alternative 是：**简单地跑 N 个配置，报告效果方向和大小的变异范围**（即朴素的 sensitivity analysis，不需要 E/N/U 框架、不需要 specification curve 的 joint inference）。Carlson & Burbano (2026) 实际上就是在推荐这种做法。\n\nProposal 的增量价值在于：\n1. E/N/U 框架提供了**有原则的配置空间裁剪**（从 810 → 90-270），避免朴素笛卡尔积的 Auspurg 式批评\n2. Permutation-based joint inference 提供了**正式的统计检验**（\"robust/fragile/sign-inconsistent\" 分类），而非仅仅可视化变异\n3. Variance decomposition 提供了**归因**，告诉你哪个维度驱动了最多不稳定性\n\n然而：(a) E/N/U 的分类在 LLM annotation 语境下相当主观（谁来判断 temperature=0 对某任务是\"objectively superior\"？），这让\"有原则的裁剪\"的说服力打折扣；(b) 朴素 sensitivity analysis + 简单的 sign consistency 检查可能在实践中达到 80% 类似的效果。增量价值存在但不算大。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **E/N/U 分类可以客观执行**：Proposal 假设研究者可以对 LLM 管道维度进行有原则的 E/N/U 分类（如 \"temperature=0 对分类任务客观更优\"），但这种分类本身就是一个研究者自由度。谁来判断、依据什么判断、不同研究者是否会达成一致？如果 E/N/U 分类本身就有高主观性，那么它只是把自由度从配置空间转移到了元方法论层面。Proposal 没有讨论 inter-rater reliability of E/N/U classification。\n\n2. **Auspurg 批评不适用的论证**：Proposal 声称 LLM 注释是 Auspurg 批评不适用的精确场景，理由是 (a) estimand 恒定 (b) 无统计误指定 (c) 无先验理论排序。但 (c) 值得质疑——如果确实\"no established theory ranks one prompt or model above another a priori\"，那为什么 E/N/U 分类中可以将某些维度归类为 N（有客观最优）？这两个 claim 之间存在张力。\n\n3. **从注释变异到推断变异的传导假设**：Proposal 假设管道配置变异会显著影响下游统计推断（这是研究的前提）。虽然 Baumann et al. 的 31% 数据支持这一点，但 Baumann 的设计是跨模型对比，而本 proposal 的多元宇宙更多关注同一模型内的 prompt/temperature/role 变化——这些维度的推断影响可能远小于跨模型变化。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中（偏弱）**\n   理由：核心贡献是将三个已有方法论工具（multiverse analysis [Steegen et al. 2016]、specification curve + joint inference [Simonsohn et al. 2020]、E/N/U classification [Del Giudice & Gangestad 2021]）跨领域迁移到 LLM 注释管道。这是一篇\"将方法 X 应用到领域 Y\"的论文。Gap 是真实的——目前确实没有人做过这个组合——但概念跳跃有限。审稿人面对 positive results 时的反应更可能是 \"this is a sensible and needed application\" 而非 \"surprising\"。McLaren et al. (2026) 已经走了同方向 80% 的路（系统变化管道配置、发现交互效应），本 proposal 的增量是方法论层面的正式化（joint inference + E/N/U 裁剪 + variance decomposition）。\n\n2. **Significance: 中（偏强）**\n   理由：问题重要且时效性好。LLM 注释在社会科学中的使用正在爆炸性增长（Carlson & Burbano 2026 in SMJ 说明管理学已在关注；Kosch & Feger 2026 in CACM 说明问题已进入主流视野）。如果框架被采纳，可以成为社会科学研究者使用 LLM 注释时的标准方法论步骤。开源工具 + 预注册模板增强了实际影响力。但影响力更多在计算社会科学社区而非核心 NLP/ML 社区。\n\n3. **Related Work: 强**\n   理由：Proposal 的文献覆盖异常全面且准确。所有引用的关键论文均真实存在，描述准确。差异化定位清晰：vs. Baumann（发现问题但无正式框架）、vs. McLaren（one-at-a-time 无 joint inference）、vs. Kosch（概念类比无方法）、vs. Ye（HCI 系统非注释管道）、vs. Mehrotra（单管道多视角）。对 Auspurg 辩论的回应是一个精明的学术定位动作。这是 proposal 最强的维度。\n\n---\n\n【概率估计 — CoRL 2026】: 0% - 2%，中位 ~0%\n\n【估计理由 — CoRL】: \n论文主题（LLM 注释管道的统计方法论）与 CoRL（机器人学习）完全不相关。CoRL 明确要求 \"focus on a core robotics problem\"。本文不涉及任何机器人学习内容。会被 desk reject。\n\n---\n\n【概率估计 — 合适 venue（AAAI/EMNLP/TACL 等，proposal 自身列出的目标）】: 20% - 35%，中位 ~27%\n\n【估计理由 — 合适 venue】:\n从 3 维度到概率的推理：Related Work 强，说明作者对领域把握好、定位精准；Significance 中偏强，说明问题有价值；但 Novelty 中偏弱是限制上界的关键因素——这本质上是一篇跨领域方法迁移论文，核心方法论工具全部来自已有文献。审稿人会承认 gap 真实存在、工作有用，但可能认为 intellectual contribution 有限。在 AAAI/EMNLP 这类竞争激烈的 venue，\"有用但不新\"的方法论论文通常落在 borderline 区域。TACL（滚动提交、更重视方法论深度）可能是最佳匹配。\n\n【主要风险】:\n\n1. **\"Apply X to Y\" 的 novelty 质疑**: 审稿人会指出 specification curve analysis、E/N/U framework、variance decomposition 全是已有方法，本文的贡献仅是 domain adaptation——这对顶会论文来说 intellectual contribution 可能不够。\n\n2. **E/N/U 分类的主观性悖论**: Proposal 的核心卖点之一是\"有原则地裁剪配置空间\"，但 E/N/U 分类本身就引入了新的研究者自由度。审稿人会问：如果不同研究者对同一任务的 E/N/U 分类不一致，那么框架的 \"principled\" 性质就被削弱了。这是一个 idea 层面的逻辑漏洞，不是实验能补救的。\n```\n\nSources:\n- [Baumann et al. 2025 - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)\n- [McLaren et al. 2026 - Magic Words or Methodical Work?](https://arxiv.org/abs/2603.26898)\n- [Kosch & Feger 2026 - Prompt-Hacking: The New p-Hacking?](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)\n- [Auspurg 2025 - Robustness is better assessed with a few thoughtful models](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas 2025 - Reply to Auspurg](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Del Giudice & Gangestad 2021 - A Traveler's Guide to the Multiverse](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Ye et al. 2026 - Navigating the Conceptual Multiverse](https://arxiv.org/abs/2604.17815)\n- [Mehrotra et al. 2026 - Multi-Perspective LLM Annotations](https://arxiv.org/pdf/2603.21404)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient data to make a well-grounded assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n```\n\n> ⚠️ **重要 venue 不匹配警告**: 用户指定评估 CoRL 2026（Conference on Robot Learning），但此 proposal 与机器人学习完全无关——研究主题是 LLM 标注流水线中的 multiverse analysis / specification curve，属于 NLP+Computational Social Science 方法论。Proposal 自身列出的目标会议是 AAAI 2027, TACL, CSCW 2027, EMNLP 2026, FAccT 2027。**若投稿 CoRL，大概率会被 desk reject**。以下评估针对 idea 本身的学术质量，概率估计同时给出 CoRL 和其实际目标 venue 的判断。\n\n---\n\n```\n【领域调研】:\n\n1. Baumann et al. \"Large Language Model Hacking\" (arXiv 2509.08825, Sep 2025):\n   - 18 模型 × 37 任务 × 13M 标签，发现 ~31% 假设得出错误统计结论\n   - 评估了 21 种 ad-hoc 缓解策略，但无 formal multiverse 推断\n   - 提供公开复制数据 (MIT license) — 即本 proposal 的验证数据来源\n   - 关系：本 proposal 的核心 \"problem paper\"，proposal 准确引用\n\n2. McLaren et al. \"Magic Words or Methodical Work?\" (arXiv 2603.26898, Mar 2026):\n   - 6 个开权模型 × 4 个政治科学任务，控制量化/硬件/prompt 条件\n   - 核心发现：interaction effects 主导 main effects；无单一最优配置\n   - 设计为 one-at-a-time 变化，非 full factorial；无 specification curve 或 joint inference\n   - 关系：proposal 准确描述其为 \"complementary benchmarking\"\n\n3. Auspurg \"Robustness is better assessed with a few thoughtful models than with billions of regressions\" (PNAS 2025):\n   - 批评 Ganslmeier & Vlandas 的 3.6B 回归 multiverse：包含不合理模型 → 高估不确定性\n   - 核心论点：multiverse 仅在所有模型估计相同 estimand 且均为合理 specification 时有效\n   - Ganslmeier & Vlandas (PNAS 2025) 的 reply 反驳：当理论无法裁定时，需更广泛枚举\n   - 关系：proposal 的关键 methodological foil，论证 LLM annotation 恰好满足 Auspurg 的有效条件\n\n4. Del Giudice & Gangestad \"A Traveler's Guide to the Multiverse\" (AMPPS 2021):\n   - E/N/U (Equivalence / Nonequivalence / Uncertainty) 分类框架\n   - Type E → 填充 multiverse；Type N → 解析为最优；Type U → 分层 multiverse\n   - 在心理学 multiverse 社区广受引用\n   - 关系：proposal 直接借用此框架，适配到 LLM annotation 维度\n\n5. Kosch & Feger \"Prompt-Hacking: The New p-Hacking?\" (CACM, Feb 2026):\n   - 概念类比：prompt 调优 = researcher degrees of freedom = p-hacking\n   - 只提供概念分析和呼吁，无 formal 方法\n   - 关系：proposal 准确定位为 \"conceptual analogy but offers no formal method\"\n\n6. Ye et al. \"Navigating the Conceptual Multiverse\" (arXiv 2604.17815, Apr 2026):\n   - 交互式 HCI 系统，帮助用户探索 LLM 概念框架的多元空间\n   - 不涉及 annotation pipeline 或 statistical inference\n   - 关系：名义上接近（\"multiverse\" + \"LLM\"），但方向完全不同\n\n7. Carlson & Burbano (SMJ 2026):\n   - 管理学研究中 LLM 标注的基础性指南和警告\n   - 建议做 sensitivity analysis，但未提供 formal methodology\n   - 关系：proposal 的 motivation 之一\n\n8. Brittlebench (arXiv 2026):\n   - 度量 prompt sensitivity（语义保持扰动使模型性能下降高达 12%）\n   - 但关注 benchmark 层面，非 downstream inferential consequences\n\n- 调研总结：该领域目前的格局是 \"问题已被充分记录（Baumann, McLaren, Kosch & Feger），guidelines 已被发布（Carlson & Burbano），但 formal statistical inference framework 确实缺失\"。Proposal 定位于这个明确的 gap——将心理学/经济学的成熟 multiverse 方法论迁移到 LLM annotation 领域。该 gap 是真实存在的。\n```\n\n```\n【Trivial Alternative 检验】:\n\n存在以下 trivial alternative：\n(a) \"Run N configs, report range\" baseline —— 研究者可以简单地跑 5-10 种\n    模型/prompt 组合，报告估计值的范围和方向一致性，不需要 formal\n    specification curve 或 permutation-based joint inference。这种非形式化\n    的 sensitivity analysis 实际上就是 Carlson & Burbano (2026) 推荐的做法，\n    且已能捕捉大部分实践价值。\n(b) \"Pick best config via gold validation\" —— 如果有 gold labels（Baumann \n    数据集有），直接选 F1 最高的 pipeline 配置，不需要 multiverse。\n\n增量价值分析：\n- 对 (a)：proposal 的增量在于 formal joint inference（permutation test 给出 \n  multiverse 层面的 p-value）和 variance decomposition（量化哪个维度驱动不\n  稳定性）。这在统计严谨性上确实优于非形式化的 \"看看范围\"，但对实践者\n  来说 marginal gain 有限——大多数研究者看到 \"5/10 configs 给出相反结论\" \n  就足以判断 fragile。\n- 对 (b)：proposal 的 counter argument 合理——gold labels 不总是有，且 \n  agreement 最优 ≠ downstream inference 最优。但这个论点在 Baumann 数据集\n  上（有 gold）说服力减弱。\n\n结论：trivial alternative 威胁中等。formal framework 有真实增量价值，但该增量\n主要面向 methodologically-oriented 受众，对广大 NLP 实践者来说 \"just report \nmultiple configs\" 可能已够用。\n```\n\n```\n【前提假设检验】:\n\n核心 claim 的逻辑链中，以下环节属于未经充分验证的假设：\n\n1. \"LLM annotation 中 estimand 在 configurations 之间保持恒定\"\n   ——这是论证 Auspurg 批评不适用的关键前提。但严格来看，不同 prompt \n   措辞和模型可能隐含度量不同 construct（例如一个 prompt 对 \"toxicity\" \n   的定义比另一个更宽泛）。proposal 的 E/N/U 分类中 Type E (\"semantically \n   equivalent prompt rephrasings\") 假设语义等价性，但\"语义等价\"本身需要\n   验证——这恰恰是 computational social science 中 construct validity 的核心\n   难题。如果 estimand 实际不恒定，整个 multiverse 框架的 epistemological \n   justification 就被削弱。\n\n2. \"No configuration is statistically misspecified\"\n   ——这个假设忽略了：某些 model+prompt 组合可能产生 systematically biased \n   labels（e.g., 模型的已知 demographic bias、某些 prompt 诱导的 position \n   bias）。这些 biased configurations 的纳入是否等价于 Auspurg 批评的 \n   \"including unjustified models\"？proposal 用 E/N/U 分类试图排除这些，但\n   排除的依据（Type N 的判定标准）本身需要 domain expertise，与 \"no theory \n   ranks choices a priori\" 的另一假设存在张力。\n\n3. \"Interaction effects dominate → full factorial is needed\"\n   ——引自 McLaren et al.，但并不 formally 蕴含需要 full Cartesian product。\n   Fractional factorial designs 或 Latin hypercube sampling 可能以更低成本\n   达到类似覆盖。proposal 未讨论为何不采用这些替代设计。\n\n总结：前提假设 1 是最关键的风险点——如果审稿人挑战 \"estimand constancy\"，\nproposal 的整个 epistemological 论证链就需要重新校准。\n```\n\n```\n【3 维度打分】:\n\n1. Novelty: 弱-中 — \n   核心贡献是跨领域方法迁移：将已成熟的 specification curve analysis \n   (Simonsohn et al., 2020)、E/N/U classification (Del Giudice & Gangestad, \n   2021)、Boba DSL (Liu et al., 2021) 组合后适配到 LLM annotation 领域。\n   每个组件都有现成原型，组合本身是 \"obvious next step\"——读完 Baumann \n   et al. (2025) 和 Simonsohn et al. (2020) 后，一个有方法论背景的研究者\n   自然会想到这一步。gap 是真实的（无人做过 formal multiverse for LLM \n   annotation），但 gap 存在 ≠ 填补 gap 有足够 novelty。Proposal 对 \n   Auspurg debate 的 engagement 是亮点（论证 LLM annotation 恰好满足 \n   multiverse 有效条件），但这更像 methodological positioning 而非新方法。\n   \n   如果核心发现是 positive（e.g., \"40% 假设 fragile，model choice 驱动\n   最多 variance\"），审稿人大概率会说 \"I would have guessed this given \n   Baumann et al.\" 而非 \"surprising\"。\n\n2. Significance: 中 — \n   问题本身确实重要且时效性强。LLM-mediated annotation 正在快速普及，\n   researcher degrees of freedom 是真实隐患（Baumann 31% error rate, \n   Kosch & Feger 的 \"prompt-hacking\" 概念）。NLP+CSS 社区有明确需求\n   （workshop calls for \"LLMs for measurement and downstream inference\"）。\n   但目标受众偏窄——需要同时关心 (a) LLM annotation 和 (b) formal \n   statistical inference 的研究者。对于 broader NLP 社区（关心 SOTA \n   performance）或 broader social science 社区（可能不用 LLM annotation），\n   直接影响有限。toolkit 的实际采用率决定长期影响，但这无法在 paper \n   层面证明。\n\n3. Related Work: 强 — \n   这是 proposal 最强的维度。对 landscape 的覆盖全面且准确：\n   - 准确区分了 Baumann (problem documentation)、McLaren (complementary \n     benchmarking)、Kosch & Feger (conceptual analogy)、Ye et al. (HCI, \n     not annotation) 各自的定位\n   - 与 Auspurg/Ganslmeier & Vlandas debate 的 substantive engagement \n     是有深度的 methodological positioning\n   - 所有关键引用经调研验证为真实存在且描述准确\n   - 差异化定位清晰：无人做过 \"formal multiverse + joint inference + \n     variance decomposition for LLM annotation\"\n   - 唯一轻微不足：未提及 prediction-powered inference (PPI) 文献\n     （Angelopoulos et al., 2023）作为处理 LLM label noise 的替代\n     统计框架\n```\n\n```\n【概率估计】: \n\nCoRL 2026: 2-5% 中位 3% （完全 out of scope，大概率 desk reject）\n\n若投稿其自身目标 venue（AAAI 2027 / EMNLP 2026 / TACL）:\n[20% - 32%] 中位 25%\n\n【估计理由】:\nidea 的 gap 真实存在、问题重要、related work 覆盖出色，这些保证了下限不低\n（不至于被认为 \"没有贡献\"）。但 novelty 维度是明确的天花板限制因素：\n(1) 核心贡献是已知方法的跨领域迁移，属 \"obvious next step\"；\n(2) trivial alternative (\"run multiple configs and report range\") 能覆盖大部分\n    实践价值，formal framework 的增量主要在统计严谨性而非洞见；\n(3) 预期发现如果 positive，大概率是 confirmatory（确认 Baumann 等已记录的\n    现象）而非 surprising。\n这使得 paper 最可能落在 \"solid but incremental\" 区间，对于 competitive venue \n(AAAI ~23% AR, EMNLP ~22% AR) 来说处于 borderline。TACL 作为 journal 对 \nthoroughness 有更高容忍度，可能是最佳匹配 venue。\n\n【主要风险】:\n1. Novelty 不足 —— 审稿人可能总结为 \"straightforward application of \n   specification curves to LLM pipelines\"，认为 methodological contribution \n   不够深，尤其是当所有组件（specification curve, E/N/U, Boba DSL）都有\n   现成实现时\n2. Estimand constancy 假设受质疑 —— 如果审稿人不接受 \"不同 prompt/model \n   度量的是同一 construct\" 这一前提，proposal 的核心 epistemological \n   argument（Auspurg 批评不适用）就会被动摇，进而削弱整个框架的理论基础\n```\n\n---\n\nSources:\n- [Baumann et al. - Large Language Model Hacking (arXiv 2509.08825)](https://arxiv.org/abs/2509.08825)\n- [McLaren et al. - Magic Words or Methodical Work? (arXiv 2603.26898)](https://arxiv.org/abs/2603.26898)\n- [Auspurg - Robustness is better assessed with a few thoughtful models (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Kosch & Feger - Prompt-Hacking: The New p-Hacking? (CACM 2026)](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)\n- [Ye et al. - Navigating the Conceptual Multiverse (arXiv 2604.17815)](https://arxiv.org/abs/2604.17815)\n- [Carlson & Burbano - LLMs to Annotate Data in Management Research (SMJ 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)\n- [Variance-Aware LLM Annotation for Strategy Research (arXiv 2601.02370)](https://arxiv.org/pdf/2601.02370)\n- [Brittlebench (arXiv 2603.13285)](https://arxiv.org/pdf/2603.13285)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Multiverse Analysis Framework for LLM-Mediated Social Science Pipelines\n\n## Description\nWe propose the first formal multiverse analysis framework for LLM-mediated social science annotation pipelines, combining principled configuration selection with joint statistical inference. While recent work documents that LLM pipeline choices produce contradictory conclusions (Baumann et al., 2025: ~31% error rate) and that interaction effects between choices dominate main effects (McLaren et al., 2026), no existing framework applies formal multiverse methodology — and the methodological community is actively debating whether exhaustive enumeration overstates uncertainty (Auspurg, PNAS 2025). We address both gaps. First, we adapt Del Giudice & Gangestad's (2021) E/N/U (Equivalence/Nonequivalence/Uncertainty) classification framework to LLM annotation, providing a principled methodology for constructing task-conditional multiverses: dimensions where one configuration is objectively superior (e.g., temperature=0 for deterministic tasks) are resolved rather than enumerated, while genuinely equivalent alternatives (e.g., semantically equivalent prompt rephrasings) populate the multiverse. Task-conditional constraints expressed in a Boba-style DSL reduce the naïve 810-configuration Cartesian product to ~90–270 principled specifications per task. Second, we adapt specification curve analysis (Simonsohn et al., 2020) with permutation-based joint inference to classify substantive social-science hypotheses as robust, fragile, or sign-inconsistent across the annotation multiverse. Third, we perform formal variance decomposition (factorial ANOVA over specification space) to quantify which pipeline dimensions and interactions drive the most inferential instability — extending McLaren et al.'s descriptive benchmarking to statistical attribution. We validate on 10 tasks from Baumann et al.'s publicly available replication data (37 tasks, MIT license) spanning binary, multi-class, ordinal, and subjective annotation, with supplementary validation on the SALT-NLP CSS benchmark. All inference is run via API on 6 models spanning diverse architectures (Llama 4 Maverick, Qwen 3.5, DeepSeek V4 Flash, Gemma 4, Mistral Medium 3.5, plus one proprietary anchor). We engage directly with Auspurg's (PNAS 2025) critique of brute-force multiverse analysis, arguing that LLM annotation is precisely the setting where her concerns do not apply: the estimand remains constant across configurations, no configuration is statistically misspecified, and no established theory ranks pipeline choices a priori. We release an open-source Python toolkit (llm-multiverse) integrating E/N/U classification, constraint-based configuration enumeration, batched API annotation, specification curve visualization, and joint inference — with SMART-compatible pre-registration templates enabling researchers to document and justify their multiverse construction before running experiments.\n\n## Core Problem\nWhen researchers use LLMs to annotate text for social science, numerous pipeline choices (model, prompt, temperature, aggregation) constitute researcher degrees of freedom that can produce contradictory conclusions — yet no formal framework systematically quantifies how these choices jointly affect downstream statistical inference. This is not merely a benchmarking problem: existing work documents that choices matter and interact (Baumann et al., 2025; McLaren et al., 2026), but none applies formal joint inference methods to determine whether a substantive social-science finding is robust across the space of defensible pipeline configurations.\n\n## Opportunity\nThe 'LLM hacking' paper (Baumann et al., 2025) showed ~31% of hypotheses yield incorrect conclusions from arbitrary LLM configuration choices, and Carlson & Burbano (2026, SMJ) recommend sensitivity analysis but provide no formal methodology. McLaren et al. (2026) demonstrate that interaction effects between pipeline choices dominate main effects, yet use only one-at-a-time variation without joint inference. Meanwhile, multiverse analysis / specification curve methods are mature in psychology and economics but have never been adapted to the unique structure of LLM annotation pipelines, where the degrees of freedom (prompt wording, model family, temperature, role, output parsing) are qualitatively different from traditional analytic choices — and, crucially, where Auspurg's (PNAS 2025) critique of brute-force multiverse enumeration does not apply because (a) the estimand remains constant across pipeline configurations, (b) no configuration is 'statistically misspecified' in the way a regression omitting fixed effects is, and (c) no established theory ranks one prompt or model above another a priori. The NLP+CSS community explicitly calls for work on 'LLMs for measurement and downstream statistical inference.'\n\n## Landscape\nThe LLM hacking paper (Baumann et al., 2025) tested 18 LLMs × 2,361 hypotheses × 13M labels, documenting the problem's scale but only evaluating 21 ad-hoc mitigations — no formal multiverse inference. 'Magic Words or Methodical Work?' (McLaren et al., arXiv March 2026) systematically varied model, prompt template, and learning approach for LLM annotation in political science and found that interaction effects dominate main effects; however, their design is one-factor-at-a-time (not full factorial), produces no specification curve or joint inference test, and their question is 'which pipeline performs best?' rather than 'is a substantive finding robust across pipelines?' — making their work complementary benchmarking, not a multiverse analysis. The variance-aware annotation framework (2026) identifies 5 variance sources but offers protocol guidance, not statistical inference. The benchmarking debiasing paper (Audinet de Pieuchon et al., EMNLP 2025) compares DSL vs PPI but only for fixed pipeline configurations. Brittlebench (2026) measures prompt sensitivity but not downstream inferential consequences. 'Prompt-Hacking: The New p-Hacking?' (Kosch & Feger, CACM 2026) draws the conceptual analogy but offers no formal method. 'Navigating the Conceptual Multiverse' (Ye et al., arXiv April 2026) applies multiverse thinking to LLM conceptual framing as an interactive HCI system, but does not address annotation pipelines or statistical inference. 'Multi-Perspective LLM Annotations' (Mehrotra et al., arXiv March 2026) introduces Perspective-Driven Inference for subjective tasks but assumes a single pipeline per perspective. The PNAS debate between Auspurg (2025) and Ganslmeier & Vlandas (2025) on whether exhaustive multiverse enumeration overstates uncertainty provides the key methodological foil: we adopt Del Giudice & Gangestad's (2021) E/N/U classification framework to construct principled, task-conditional multiverses rather than naïve Cartesian products. No existing work provides a formal multiverse analysis with principled configuration selection and joint statistical inference for LLM annotation pipelines.\n\n## Approach\nWe propose a three-stage framework: (1) Principled Multiverse Construction using Del Giudice & Gangestad's (2021) E/N/U (Equivalence / Nonequivalence / Uncertainty) classification. For each annotation task, we classify every pipeline dimension: dimensions where alternatives are effectively equivalent (Type E: e.g., semantically equivalent prompt rephrasings) populate the multiverse; dimensions where one option is objectively superior (Type N: e.g., temperature=0 for deterministic classification tasks, label-based output over numerical scores) are resolved to the best option only; dimensions where defensibility is uncertain (Type U: e.g., model family, definition inclusion) generate separate stratified multiverses. Task-conditional constraints are expressed formally using a Boba-style DSL: e.g., IF task_type='classification' AND num_classes≤3 THEN temperature∈{0.0, 0.3} AND output_format∈{'label'}. This reduces the naïve Cartesian product (~810 configurations from 6 models × 5 prompts × 3 temperatures × 3 roles × 3 aggregation strategies) to a principled, task-specific multiverse of ~90–270 defensible configurations per task, with explicit justification for every inclusion/exclusion. (2) Full-factorial execution across the principled multiverse. The six models span diverse architectures: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE), DeepSeek V4 Flash (284B MoE), Gemma 4 (26B MoE), Mistral Medium 3.5 (128B dense), plus one proprietary anchor (GPT-4o or Claude). All models are accessed via API (DeepSeek API, Together AI, OpenRouter, Google AI) for cost-efficiency; batched annotation (25 items/prompt) minimizes token costs. For each configuration, generate labels for the full corpus, then compute the downstream statistical estimate (e.g., regression coefficient, group difference). (3) Specification curve analysis with joint inference (Simonsohn et al., 2020): rank all specifications by effect size, display the specification curve with indicator rows for each pipeline dimension, and apply a permutation-based joint inference test to classify hypotheses as robust (sign-consistent and jointly significant), fragile (sign-inconsistent or significance-dependent on configuration), or null (no configuration yields significance). Additionally, perform variance decomposition (ANOVA over the specification space) to quantify which pipeline dimensions and their interactions drive the most inferential instability — extending McLaren et al.'s descriptive interaction findings to formal statistical attribution. Validate on 10 annotation tasks drawn from Baumann et al.'s publicly available replication data (37 tasks, MIT license, github.com/joebaumann/llmhacking), selected to span binary classification, multi-class categorization, ordinal scaling, and subjective judgment. Supplementary validation uses Gilardi et al.'s (PNAS 2023) Harvard Dataverse data and the SALT-NLP CSS benchmark (Ziems et al., 2024). Release an open-source Python toolkit (llm-multiverse) that wraps the full pipeline: E/N/U classification interface → task-conditional constraint specification → configuration enumeration → batched API annotation → specification curve visualization → joint inference test. The toolkit integrates with the SMART pre-registration framework (2025) so researchers can document and justify their multiverse construction before running experiments.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '0 (all inference via API — no self-hosted GPU needed)', 'api_cost': '$1,200–$2,000 for open-weight models via API providers (DeepSeek V4 Flash: ~$100–200 via DeepSeek API; Llama 4 Maverick: ~$250–470 via Together AI; Qwen 3.5: ~$475–950 via OpenRouter; Gemma 4: ~$65–130 via Google; Mistral Medium 3.5: ~$300–650 via Mistral/OpenRouter; proprietary anchor: ~$200–400). Estimates assume batched annotation (25 items/prompt) across ~90–270 configs × 10 tasks × 1,000–3,000 samples. Total: ~500M–1.2B tokens across all models.', 'timeline': '5–6 months (1 month framework design + E/N/U methodology, 2 months implementation + experiments, 1 month analysis + variance decomposition, 1 month writing + revision)', 'estimated_total_cost': '$1,200–$2,000'}, 'human_in_loop': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same API inference, slightly optimized configuration space with Claude-assisted E/N/U classification)', 'timeline': '3.5–4.5 months (2 weeks framework design with Claude scaffolding, 6 weeks experiments, 3 weeks analysis, 3 weeks writing)', 'claude_api_cost': '$150–$250 (Sonnet for code generation, experiment orchestration, and paper drafting; ~50M input tokens with caching)', 'estimated_total_cost': '$1,150–$1,850'}, 'auto_research': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same inference costs)', 'timeline': '2–3 months (automated experiment sweeps, parallelized API calls, auto-generated specification curves)', 'claude_api_cost': '$400–$600 (Opus for research design + Sonnet for bulk code generation and analysis; ~100M tokens total)', 'estimated_total_cost': '$1,400–$2,200', 'speed_bottleneck': 'API rate limits on proprietary LLMs (GPT, Claude) for anchor comparisons; sequential dependency between label generation and downstream inference computation; OpenRouter rate limits for Qwen 3.5 and Mistral Medium 3.5'}}\n\n## Inspired By\nGap: LLM hacking paper shows the problem (31% error rate), McLaren et al. show interaction effects dominate, but no formal multiverse framework with joint inference exists. Pattern: Cross-domain transfer of specification curve analysis (psychology/economics) and the E/N/U defensibility framework (Del Giudice & Gangestad, 2021) to LLM annotation pipelines. Epistemological justification: Auspurg's (PNAS 2025) critique of brute-force multiverse analysis does not apply to LLM pipelines because the estimand is constant and no configuration is statistically misspecified — making this precisely the setting where multiverse analysis is epistemically justified. Field guide evidence: Carlson & Burbano (2026) guidelines call for sensitivity analysis; variance-aware annotation (2026) identifies 5 variance sources; the NLP+CSS workshop explicitly seeks work on 'LLMs for measurement and downstream statistical inference.'\n\n## Target Venues\n- AAAI 2027 (full paper deadline: ~July 28, 2026 — strong fit for methods + empirical validation paper; primary target)\n- TACL (rolling submission, any month — ideal for extended journal-length treatment with theoretical results on E/N/U framework + formal variance decomposition)\n- CSCW 2027 (rolling submission — fits the sociotechnical framing of researcher-tool interaction and pre-registration protocol)\n- EMNLP 2026 Industry Track (deadline: ~June 16, 2026 — if framed around practitioner toolkit; stretch target)\n- FAccT 2027 (fits the transparency/accountability angle of documenting researcher degrees of freedom in LLM-mediated research)\n\n## Key References\n- Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation (arXiv 2025, Baumann et al.) — documents the 31% error rate problem; replication data publicly available under MIT license at github.com/joebaumann/llmhacking\n- Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation (arXiv 2603.26898, McLaren et al., March 2026) — one-at-a-time benchmarking showing interaction effects dominate; releases CodeBook Lab tools; complementary but no joint inference\n- Specification Curve Analysis (Nature Human Behaviour 2020, Simonsohn, Simmons & Nelson) — canonical joint inference method we adapt\n- Increasing Transparency Through a Multiverse Analysis (Perspectives on Psychological Science 2016, Steegen, Tuerlinckx, Gelman & Vanpaemel) — original multiverse analysis framework\n- A Traveler's Guide to the Multiverse: Promises, Pitfalls, and a Framework for the Evaluation of Analytic Decisions (Advances in Methods and Practices in Psychological Science 2021, Del Giudice & Gangestad) — E/N/U classification framework for principled configuration selection\n- Robustness is better assessed with a few thoughtful models than with billions of regressions (PNAS 2025, Auspurg) — critique of exhaustive multiverse enumeration; we argue LLM annotation is precisely the case where her critique does not apply\n- Reply to Auspurg: On the limits of 'justified' model spaces (PNAS 2025, Ganslmeier & Vlandas) — defense of comprehensive multiverse analysis when theory cannot adjudicate\n- The Use of LLMs to Annotate Data in Management Research: Foundational Guidelines and Warnings (SMJ 2026, Carlson & Burbano)\n- Variance-Aware LLM Annotation for Strategy Research (arXiv 2026)\n- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025, Audinet de Pieuchon et al.)\n- Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity (arXiv 2026)\n- Can Unconfident LLM Annotations Be Used for Confident Conclusions? (NAACL 2025, Gligorić et al.)\n- Prompt-Hacking: The New p-Hacking? (Communications of the ACM 2026, Kosch & Feger)\n- Navigating the Conceptual Multiverse (arXiv 2026, Ye et al.)\n- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (arXiv 2026, Mehrotra et al.)\n- Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs (arXiv 2026, Cui & Alexander)\n- To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation (arXiv 2024)\n- SMART: Systematic Multiverse Analysis Registration Tool (Royal Society Open Science 2025) — pre-registration workflow for multiverse construction\n- Boba: Authoring and Visualizing Multiverse Analyses (Liu et al., 2021) — DSL with constraint specification for principled multiverse pruning\n- Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways (arXiv 2024) — empirical evidence for task-conditional configuration defensibility\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:30:18.806Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:30:18.806Z",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:30:18.818Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information for a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【⚠️ 致命问题：投稿 venue 完全不匹配】

本 proposal 拟投 CoRL 2026（Conference on Robot Learning）。
CoRL 的 Call for Papers 明确声明："Submissions without a robotics focus will be returned without review."
CoRL 接收的主题包括：robot manipulation, navigation, locomotion, driving, flight, 
reinforcement learning for physical robots, robot foundation models, sim-to-real transfer 等。

本 proposal 的内容是 LLM-mediated social science annotation pipeline 的多元宇宙分析方法——
这是一篇纯粹的 NLP + 社会科学方法论论文，与机器人学习无任何关联。
proposal 自身列出的 target venues 也是 AAAI 2027、TACL、CSCW、EMNLP、FAccT，没有 CoRL。

→ 投 CoRL 2026 主会的中稿概率本质上为 0%（desk reject without review）。

以下仍按要求对 idea 本身的质量进行客观评估（适用于 proposal 自身列出的 target venues）。

═══════════════════════════════════════════════════════════

【领域调研】:

- [Baumann et al., "Large Language Model Hacking", arXiv 2509.08825] (2025): 
  在 18 个 LLM × 37 个标注任务 × 2,361 个假设上系统测试，发现 ~31% 的假设在 SOTA 模型上得出 
  错误结论。文档化了问题规模，测试了 21 种 ad-hoc 缓解策略，但未提供形式化多元宇宙推断框架。
  本 proposal 的核心 motivating paper，数据公开（MIT 许可），paper 真实存在。

- [McLaren et al., "Magic Words or Methodical Work?", arXiv 2603.26898] (March 2026): 
  在政治科学标注中系统变异 model, prompt template, learning approach。核心发现：交互效应 
  主导主效应。但设计是 one-factor-at-a-time（非 full factorial），未产生 specification curve 
  或联合推断检验。问题是"哪个 pipeline 最好"而非"结论是否跨 pipeline 稳健"。
  本 proposal 将其定位为互补性 benchmarking 工作——这个定位是准确的。

- [Auspurg, "Robustness is better assessed with a few thoughtful models than with billions 
  of regressions", PNAS 2025]: 
  批评暴力多元宇宙分析，论点是：包含 misspecified 模型会淹没有效模型。
  本 proposal 引用准确，且其反驳论点（LLM annotation 中无配置是 statistically misspecified，
  estimand 恒定）有合理性。

- [Ganslmeier & Vlandas, "Reply to Auspurg", PNAS 2025]: 
  回应 Auspurg，认为"何为 justified model"本身是有争议的。
  proposal 引用准确。

- [Del Giudice & Gangestad, "A Traveler's Guide to the Multiverse", AMPPS 2021]: 
  提出 E/N/U（Equivalence/Nonequivalence/Uncertainty）分类框架。
  这是心理学方法论文献中的重要 reference，proposal 的改编思路（将 E/N/U 从分析决策迁移到 
  LLM pipeline 配置决策）是合理的跨领域迁移。

- [Kosch & Feger, "Prompt-Hacking: The New p-Hacking?", CACM 2026]: 
  概念性类比文章，指出 prompt 调整等同于 p-hacking。无形式化方法。
  proposal 引用准确——定位为"概念类比但无方法"。

- [Ye et al., "Navigating the Conceptual Multiverse", arXiv 2604.17815] (April 2026): 
  将多元宇宙思维应用于 LLM 概念框架，是交互式 HCI 系统，不涉及 annotation pipeline 或统计推断。
  proposal 的差异化定位准确。

- [Mehrotra et al., "Multi-Perspective LLM Annotations", arXiv 2603.21404] (March 2026): 
  Perspective-Driven Inference，处理主观任务中跨人口群体的分歧，但假设每个 perspective 只有 
  单一 pipeline。不涉及多元宇宙方法。proposal 差异化准确。

- [Gligorić et al., "Can Unconfident LLM Annotations Be Used for Confident Conclusions?", 
  NAACL 2025]: 
  Prediction-Powered Inference 路线——用少量人工标注校准 LLM 标注的测量误差。
  与本 proposal 互补但方法论不同：PPI 修正单一 pipeline 的 bias，multiverse 检测跨 pipeline 的 
  inferential (in)stability。proposal 未充分讨论与 PPI 方法的关系——这是一个 related work gap。

- [Simonsohn et al., "Specification Curve Analysis", Nature Human Behaviour 2020]: 
  经典方法，proposal 直接改编，引用准确。

- 调研总结：该领域呈现"问题已被充分文档化，但形式化方法学框架缺位"的格局。Baumann 等量化了 
  问题规模，McLaren 等展示了交互效应，Kosch & Feger 画了概念类比，Carlson & Burbano 呼吁 
  sensitivity analysis，但截至 2026 年 5 月，确实没有论文将 specification curve analysis / 
  formal multiverse methodology 应用于 LLM annotation pipeline。Proposal 占据了一个真实的空白。


【Trivial Alternative 检验】:

存在两个值得考虑的 trivial alternative：

1. "Just run N configs and report range"：研究者可以简单地选择 5-10 个"合理"配置，运行所有配置，
   报告效应量的范围和符号一致性——不需要 E/N/U 分类、不需要 Boba DSL、不需要形式化 specification 
   curve。这种"穷人版 sensitivity analysis"在实践中可能达到 80% 的效果。
   → 本 proposal 的增量价值在于：(a) 形式化的联合推断检验（permutation-based joint inference）
   提供了统计意义上的 robust/fragile 分类，而非 ad-hoc 判断；(b) 方差分解量化了哪些维度贡献最多 
   不稳定性；(c) E/N/U 提供了配置选择的理论基础。但这个增量是否足够"surprising"是关键问题。

2. Prediction-Powered Inference (PPI) 路线（Gligorić et al., NAACL 2025）：
   如果目标是获得可靠的下游推断，PPI 通过少量人工标注直接校正测量误差，可能是一个更优雅的解决方案。
   → 本 proposal 与 PPI 的关系是互补的（multiverse 检测 instability，PPI 修正 bias），但 
   proposal 需要更清晰地论证为什么"检测哪些结论 fragile"比"直接修正 bias"更有价值。


【前提假设检验】:

核心 claim 的逻辑链中有三个未充分验证的环节：

1. E/N/U 分类的可操作性假设：proposal 假设研究者可以对每个 pipeline 维度做出 E/N/U 分类，
   但这个分类本身是主观的。什么证据支持 temperature=0 对分类任务"objectively superior"？
   如果不同标注者对 E/N/U 分类有分歧（meta-multiverse 问题），整个框架的基础就不稳固。
   这不是致命的，但需要 inter-rater reliability 验证。

2. "Estimand 恒定"假设：proposal 论证 Auspurg 的批评不适用于 LLM annotation，因为 "estimand 
   remains constant across configurations"。但这只在所有配置确实在测量同一概念时才成立。如果不同 
   prompt framings 实际上激活了 LLM 对概念的不同理解（e.g., "toxicity" vs. "offensiveness"），
   那么 estimand 并非恒定——Auspurg 的批评就部分适用。这个假设需要更细致的论证。

3. "No configuration is statistically misspecified" 假设：temperature=1.0 + 无 system prompt 
   + numerical output parsing 对严肃的分类任务来说，显然是一个"worse" 配置。如果 E/N/U 分类 
   已经排除了这些配置，那么这个假设是 trivially true by construction——但这也削弱了"Auspurg 
   的批评不适用"这个论证的力度，因为你实际上已经在做 Auspurg 建议的事情（pruning bad specs）。


【3 维度打分】:

1. Novelty: 【中】
   理由：核心贡献是跨领域方法迁移——将心理学/经济学中成熟的 specification curve analysis 
   (Simonsohn et al., 2020) 和 E/N/U 框架 (Del Giudice & Gangestad, 2021) 移植到 LLM 
   annotation pipeline。这个特定组合确实是新的——我的调研未发现任何现有论文做了这件事。
   然而，novelty 的本质是"apply method X to domain Y"，各组件均已存在。E/N/U 的 adaptation 
   增加了一定的智识贡献，但不构成方法论上的根本创新。与 Ye et al. (2604.17815) 相比，本 
   proposal 更面向统计推断（更严谨），但 novelty profile 类似（都是跨领域迁移）。
   最关键的是：如果实验结果 positive（某些结论 robust、某些 fragile、model choice 贡献最大方差），
   审稿人很可能会说 "I would have guessed this"。

2. Significance: 【中偏强】
   理由：研究问题genuinely重要。Baumann et al. (2025) 的 31% error rate 和 McLaren et al. 
   (2026) 的 interaction effects 证明问题真实存在且规模不小。Carlson & Burbano (SMJ 2026) 
   明确呼吁 sensitivity analysis，NLP+CSS 社区 explicitly 寻求 "LLMs for measurement and 
   downstream statistical inference" 方面的工作。开源 toolkit 有实际应用价值。
   限制因素：这是一个"方法论/工具"贡献而非"发现"贡献。它的影响力取决于社区是否采用该框架——
   而这类框架在 NLP 社区的采用率历史上不高（specification curve 在心理学中也花了数年才普及）。

3. Related Work: 【强】
   理由：覆盖异常全面。proposal 对 Baumann et al., McLaren et al., Auspurg/Ganslmeier & 
   Vlandas 辩论, Ye et al., Mehrotra et al., Gligorić et al., Kosch & Feger 的描述经核实 
   均准确。与每篇工作的差异化定位清晰且合理。Auspurg 辩论的引入为方法论立场提供了有力的学术背景。
   唯一 gap：与 PPI 方法 (Gligorić et al., NAACL 2025) 的对比不够充分——需要明确论证 
   multiverse approach vs. measurement error correction approach 各自的适用场景。


【概率估计】: 
  - 投 CoRL 2026 主会: 0-2%（venue 完全不匹配，desk reject）
  - 投 proposal 自身列出的 venues（AAAI/TACL/EMNLP/CSCW/FAccT）: [25% - 38%] 中位 30%

【估计理由】: 
  idea 占据了一个真实的文献空白——形式化多元宇宙方法 × LLM annotation pipeline 确实无人做过。
  问题的重要性有充分的文献支撑（Baumann 31% error rate, McLaren interaction effects, 
  Carlson & Burbano 的呼吁）。Related work 覆盖全面且定位准确。
  
  限制上界的是 Novelty 维度：核心智识贡献是"apply existing method to new domain"，各组件
  （specification curve, E/N/U, variance decomposition）均为现成工具。如果核心发现是 
  "model choice 和 prompt 贡献最大方差，有些结论 robust 有些 fragile"，这不会让审稿人 
  surprised。此外，Trivial Alternative 威胁（简单跑 N 个 config 报告 range）和 PPI 替代 
  路线都会被 well-informed reviewer 提出。
  
  投 CoRL 的 0% 是因为 topic 与 venue scope 完全正交——这不是"fit 不太好"而是"完全不 fit"。

【主要风险】:
1. 【CoRL 投稿: 致命】venue 完全不匹配，会被 desk reject。建议改投 proposal 自身已列出的 
   AAAI 2027 或 TACL。
2. 【Idea 层面】核心发现的 "surprisingness" 不足——审稿人可能认为 "of course pipeline choices 
   matter and interact, we already knew that from Baumann/McLaren, this just puts a formal 
   framework around it"，导致 novelty 评分偏低。需要在 framing 上强调 formal joint inference 
   带来的 qualitatively new insight（例如某些被认为 robust 的经典社科发现实际上 fragile，或者 
   反直觉的方差分解结果）。
```

**Sources:**
- [Baumann et al. - LLM Hacking (arXiv 2509.08825)](https://arxiv.org/abs/2509.08825)
- [McLaren et al. - Magic Words or Methodical Work (arXiv 2603.26898)](https://arxiv.org/abs/2603.26898)
- [Auspurg - Robustness (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Del Giudice & Gangestad - Traveler's Guide (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Kosch & Feger - Prompt-Hacking (CACM 2026)](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)
- [Ye et al. - Navigating the Conceptual Multiverse (arXiv 2604.17815)](https://arxiv.org/abs/2604.17815)
- [Mehrotra et al. - Multi-Perspective LLM Annotations (arXiv 2603.21404)](https://arxiv.org/abs/2603.21404)
- [Gligorić et al. - Unconfident LLM Annotations (NAACL 2025)](https://aclanthology.org/2025.naacl-long.179/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to make my assessment. Let me note one critical finding from my research: **CoRL (Conference on Robot Learning) is a robotics conference**, and this proposal is about LLM annotation methodology for social science. Let me write up the full evaluation.

---

```
【阶段】: Triage

【致命问题 — 投稿目标与论文主题完全不匹配】

在进入正式 rubric 之前，必须首先指出：**这篇 proposal 投稿 CoRL 2026（Conference on Robot Learning）是一个根本性的错误。**

CoRL 2026 的 Call for Papers 明确要求论文 "focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics"，涵盖领域包括 imitation learning、reinforcement learning for robots、sim-to-real transfer、robot perception、learned manipulation/locomotion、learning-based planning 等。

本 proposal 的主题是「LLM 注释管道的多元宇宙分析框架」——一项计算社会科学方法论工作，涉及 specification curve analysis、variance decomposition、E/N/U 分类框架。**它与机器人学习没有任何交集。** 该论文自身列出的目标会议（AAAI 2027, TACL, CSCW 2027, EMNLP 2026 Industry Track, FAccT 2027）也完全不包含 CoRL。

**投 CoRL 的结果：大概率 desk reject（编辑直接拒稿，不进入审稿流程）。**

以下评估将按要求完成 idea 质量的客观分析，但概率估计针对的是 CoRL 2026 这个具体场景。我会同时给出"如果投到合适的 venue（如 EMNLP/AAAI/TACL）"的参考概率。

---

【领域调研】:

1. **Baumann et al. (arXiv 2509.08825, 2025)** "Large Language Model Hacking": 18 个 LLM × 37 个注释任务 × 1300 万标签，发现约 31% 的假设因 LLM 配置选择得出错误结论。这是本 proposal 的核心动机来源，论文真实存在，描述准确。

2. **McLaren et al. (arXiv 2603.26898, March 2026)** "Magic Words or Methodical Work?": 在政治科学 LLM 注释中系统变化 model/prompt/learning approach，发现交互效应主导主效应。但使用 one-at-a-time 变化设计，无 joint inference。论文真实存在，描述准确。

3. **Kosch & Feger (CACM 2026, arXiv 2504.14571)** "Prompt-Hacking: The New p-Hacking?": 概念性类比文章，画了 prompt-hacking 与 p-hacking 的平行关系，但未提出正式方法。真实存在，描述准确。

4. **Auspurg (PNAS 2025)** "Robustness is better assessed with a few thoughtful models than with billions of regressions": 批评 Ganslmeier & Vlandas 的暴力多元宇宙分析，认为只有当所有模型同等合理时多元宇宙分析才有信息量。真实存在，描述准确。Ganslmeier & Vlandas 的 reply 也真实存在。

5. **Del Giudice & Gangestad (AMPPS 2021)** "A Traveler's Guide to the Multiverse": 提出 E/N/U 分类框架（Equivalence/Nonequivalence/Uncertainty）。真实存在，描述准确。

6. **Ye et al. (arXiv 2604.17815, April 2026)** "Navigating the Conceptual Multiverse": 将多元宇宙思维应用于 LLM 概念框架的交互式 HCI 系统，但不涉及注释管道或统计推断。真实存在，描述准确。

7. **Mehrotra et al. (arXiv 2603.21404, March 2026)** "Multi-Perspective LLM Annotations": 针对主观任务引入 Perspective-Driven Inference。真实存在。

8. **Carlson & Burbano (SMJ 2026)**: 关于管理学研究中 LLM 注释的基础性指南，推荐 sensitivity analysis 但未提供正式方法论。真实存在。

- **调研总结**: 该领域正处于从"发现问题"（Baumann: 31% 错误率；McLaren: 交互效应主导）到"系统解决问题"的转折期。多个工作从不同角度描述了 LLM 注释管道中的研究者自由度问题（Kosch 概念层面、Carlson 指南层面、McLaren 实证层面），但确实尚无工作将正式的多元宇宙分析 + joint inference 方法论应用于 LLM 注释管道。这个 gap 是真实的。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁，但 proposal 对其有部分回应。**

最直接的 trivial alternative 是：**简单地跑 N 个配置，报告效果方向和大小的变异范围**（即朴素的 sensitivity analysis，不需要 E/N/U 框架、不需要 specification curve 的 joint inference）。Carlson & Burbano (2026) 实际上就是在推荐这种做法。

Proposal 的增量价值在于：
1. E/N/U 框架提供了**有原则的配置空间裁剪**（从 810 → 90-270），避免朴素笛卡尔积的 Auspurg 式批评
2. Permutation-based joint inference 提供了**正式的统计检验**（"robust/fragile/sign-inconsistent" 分类），而非仅仅可视化变异
3. Variance decomposition 提供了**归因**，告诉你哪个维度驱动了最多不稳定性

然而：(a) E/N/U 的分类在 LLM annotation 语境下相当主观（谁来判断 temperature=0 对某任务是"objectively superior"？），这让"有原则的裁剪"的说服力打折扣；(b) 朴素 sensitivity analysis + 简单的 sign consistency 检查可能在实践中达到 80% 类似的效果。增量价值存在但不算大。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **E/N/U 分类可以客观执行**：Proposal 假设研究者可以对 LLM 管道维度进行有原则的 E/N/U 分类（如 "temperature=0 对分类任务客观更优"），但这种分类本身就是一个研究者自由度。谁来判断、依据什么判断、不同研究者是否会达成一致？如果 E/N/U 分类本身就有高主观性，那么它只是把自由度从配置空间转移到了元方法论层面。Proposal 没有讨论 inter-rater reliability of E/N/U classification。

2. **Auspurg 批评不适用的论证**：Proposal 声称 LLM 注释是 Auspurg 批评不适用的精确场景，理由是 (a) estimand 恒定 (b) 无统计误指定 (c) 无先验理论排序。但 (c) 值得质疑——如果确实"no established theory ranks one prompt or model above another a priori"，那为什么 E/N/U 分类中可以将某些维度归类为 N（有客观最优）？这两个 claim 之间存在张力。

3. **从注释变异到推断变异的传导假设**：Proposal 假设管道配置变异会显著影响下游统计推断（这是研究的前提）。虽然 Baumann et al. 的 31% 数据支持这一点，但 Baumann 的设计是跨模型对比，而本 proposal 的多元宇宙更多关注同一模型内的 prompt/temperature/role 变化——这些维度的推断影响可能远小于跨模型变化。

---

【3 维度打分】:

1. **Novelty: 中（偏弱）**
   理由：核心贡献是将三个已有方法论工具（multiverse analysis [Steegen et al. 2016]、specification curve + joint inference [Simonsohn et al. 2020]、E/N/U classification [Del Giudice & Gangestad 2021]）跨领域迁移到 LLM 注释管道。这是一篇"将方法 X 应用到领域 Y"的论文。Gap 是真实的——目前确实没有人做过这个组合——但概念跳跃有限。审稿人面对 positive results 时的反应更可能是 "this is a sensible and needed application" 而非 "surprising"。McLaren et al. (2026) 已经走了同方向 80% 的路（系统变化管道配置、发现交互效应），本 proposal 的增量是方法论层面的正式化（joint inference + E/N/U 裁剪 + variance decomposition）。

2. **Significance: 中（偏强）**
   理由：问题重要且时效性好。LLM 注释在社会科学中的使用正在爆炸性增长（Carlson & Burbano 2026 in SMJ 说明管理学已在关注；Kosch & Feger 2026 in CACM 说明问题已进入主流视野）。如果框架被采纳，可以成为社会科学研究者使用 LLM 注释时的标准方法论步骤。开源工具 + 预注册模板增强了实际影响力。但影响力更多在计算社会科学社区而非核心 NLP/ML 社区。

3. **Related Work: 强**
   理由：Proposal 的文献覆盖异常全面且准确。所有引用的关键论文均真实存在，描述准确。差异化定位清晰：vs. Baumann（发现问题但无正式框架）、vs. McLaren（one-at-a-time 无 joint inference）、vs. Kosch（概念类比无方法）、vs. Ye（HCI 系统非注释管道）、vs. Mehrotra（单管道多视角）。对 Auspurg 辩论的回应是一个精明的学术定位动作。这是 proposal 最强的维度。

---

【概率估计 — CoRL 2026】: 0% - 2%，中位 ~0%

【估计理由 — CoRL】: 
论文主题（LLM 注释管道的统计方法论）与 CoRL（机器人学习）完全不相关。CoRL 明确要求 "focus on a core robotics problem"。本文不涉及任何机器人学习内容。会被 desk reject。

---

【概率估计 — 合适 venue（AAAI/EMNLP/TACL 等，proposal 自身列出的目标）】: 20% - 35%，中位 ~27%

【估计理由 — 合适 venue】:
从 3 维度到概率的推理：Related Work 强，说明作者对领域把握好、定位精准；Significance 中偏强，说明问题有价值；但 Novelty 中偏弱是限制上界的关键因素——这本质上是一篇跨领域方法迁移论文，核心方法论工具全部来自已有文献。审稿人会承认 gap 真实存在、工作有用，但可能认为 intellectual contribution 有限。在 AAAI/EMNLP 这类竞争激烈的 venue，"有用但不新"的方法论论文通常落在 borderline 区域。TACL（滚动提交、更重视方法论深度）可能是最佳匹配。

【主要风险】:

1. **"Apply X to Y" 的 novelty 质疑**: 审稿人会指出 specification curve analysis、E/N/U framework、variance decomposition 全是已有方法，本文的贡献仅是 domain adaptation——这对顶会论文来说 intellectual contribution 可能不够。

2. **E/N/U 分类的主观性悖论**: Proposal 的核心卖点之一是"有原则地裁剪配置空间"，但 E/N/U 分类本身就引入了新的研究者自由度。审稿人会问：如果不同研究者对同一任务的 E/N/U 分类不一致，那么框架的 "principled" 性质就被削弱了。这是一个 idea 层面的逻辑漏洞，不是实验能补救的。
```

Sources:
- [Baumann et al. 2025 - Large Language Model Hacking](https://arxiv.org/abs/2509.08825)
- [McLaren et al. 2026 - Magic Words or Methodical Work?](https://arxiv.org/abs/2603.26898)
- [Kosch & Feger 2026 - Prompt-Hacking: The New p-Hacking?](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)
- [Auspurg 2025 - Robustness is better assessed with a few thoughtful models](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas 2025 - Reply to Auspurg](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Del Giudice & Gangestad 2021 - A Traveler's Guide to the Multiverse](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Ye et al. 2026 - Navigating the Conceptual Multiverse](https://arxiv.org/abs/2604.17815)
- [Mehrotra et al. 2026 - Multi-Perspective LLM Annotations](https://arxiv.org/pdf/2603.21404)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient data to make a well-grounded assessment. Let me compile my analysis.

---

```
【阶段】: Triage
```

> ⚠️ **重要 venue 不匹配警告**: 用户指定评估 CoRL 2026（Conference on Robot Learning），但此 proposal 与机器人学习完全无关——研究主题是 LLM 标注流水线中的 multiverse analysis / specification curve，属于 NLP+Computational Social Science 方法论。Proposal 自身列出的目标会议是 AAAI 2027, TACL, CSCW 2027, EMNLP 2026, FAccT 2027。**若投稿 CoRL，大概率会被 desk reject**。以下评估针对 idea 本身的学术质量，概率估计同时给出 CoRL 和其实际目标 venue 的判断。

---

```
【领域调研】:

1. Baumann et al. "Large Language Model Hacking" (arXiv 2509.08825, Sep 2025):
   - 18 模型 × 37 任务 × 13M 标签，发现 ~31% 假设得出错误统计结论
   - 评估了 21 种 ad-hoc 缓解策略，但无 formal multiverse 推断
   - 提供公开复制数据 (MIT license) — 即本 proposal 的验证数据来源
   - 关系：本 proposal 的核心 "problem paper"，proposal 准确引用

2. McLaren et al. "Magic Words or Methodical Work?" (arXiv 2603.26898, Mar 2026):
   - 6 个开权模型 × 4 个政治科学任务，控制量化/硬件/prompt 条件
   - 核心发现：interaction effects 主导 main effects；无单一最优配置
   - 设计为 one-at-a-time 变化，非 full factorial；无 specification curve 或 joint inference
   - 关系：proposal 准确描述其为 "complementary benchmarking"

3. Auspurg "Robustness is better assessed with a few thoughtful models than with billions of regressions" (PNAS 2025):
   - 批评 Ganslmeier & Vlandas 的 3.6B 回归 multiverse：包含不合理模型 → 高估不确定性
   - 核心论点：multiverse 仅在所有模型估计相同 estimand 且均为合理 specification 时有效
   - Ganslmeier & Vlandas (PNAS 2025) 的 reply 反驳：当理论无法裁定时，需更广泛枚举
   - 关系：proposal 的关键 methodological foil，论证 LLM annotation 恰好满足 Auspurg 的有效条件

4. Del Giudice & Gangestad "A Traveler's Guide to the Multiverse" (AMPPS 2021):
   - E/N/U (Equivalence / Nonequivalence / Uncertainty) 分类框架
   - Type E → 填充 multiverse；Type N → 解析为最优；Type U → 分层 multiverse
   - 在心理学 multiverse 社区广受引用
   - 关系：proposal 直接借用此框架，适配到 LLM annotation 维度

5. Kosch & Feger "Prompt-Hacking: The New p-Hacking?" (CACM, Feb 2026):
   - 概念类比：prompt 调优 = researcher degrees of freedom = p-hacking
   - 只提供概念分析和呼吁，无 formal 方法
   - 关系：proposal 准确定位为 "conceptual analogy but offers no formal method"

6. Ye et al. "Navigating the Conceptual Multiverse" (arXiv 2604.17815, Apr 2026):
   - 交互式 HCI 系统，帮助用户探索 LLM 概念框架的多元空间
   - 不涉及 annotation pipeline 或 statistical inference
   - 关系：名义上接近（"multiverse" + "LLM"），但方向完全不同

7. Carlson & Burbano (SMJ 2026):
   - 管理学研究中 LLM 标注的基础性指南和警告
   - 建议做 sensitivity analysis，但未提供 formal methodology
   - 关系：proposal 的 motivation 之一

8. Brittlebench (arXiv 2026):
   - 度量 prompt sensitivity（语义保持扰动使模型性能下降高达 12%）
   - 但关注 benchmark 层面，非 downstream inferential consequences

- 调研总结：该领域目前的格局是 "问题已被充分记录（Baumann, McLaren, Kosch & Feger），guidelines 已被发布（Carlson & Burbano），但 formal statistical inference framework 确实缺失"。Proposal 定位于这个明确的 gap——将心理学/经济学的成熟 multiverse 方法论迁移到 LLM annotation 领域。该 gap 是真实存在的。
```

```
【Trivial Alternative 检验】:

存在以下 trivial alternative：
(a) "Run N configs, report range" baseline —— 研究者可以简单地跑 5-10 种
    模型/prompt 组合，报告估计值的范围和方向一致性，不需要 formal
    specification curve 或 permutation-based joint inference。这种非形式化
    的 sensitivity analysis 实际上就是 Carlson & Burbano (2026) 推荐的做法，
    且已能捕捉大部分实践价值。
(b) "Pick best config via gold validation" —— 如果有 gold labels（Baumann 
    数据集有），直接选 F1 最高的 pipeline 配置，不需要 multiverse。

增量价值分析：
- 对 (a)：proposal 的增量在于 formal joint inference（permutation test 给出 
  multiverse 层面的 p-value）和 variance decomposition（量化哪个维度驱动不
  稳定性）。这在统计严谨性上确实优于非形式化的 "看看范围"，但对实践者
  来说 marginal gain 有限——大多数研究者看到 "5/10 configs 给出相反结论" 
  就足以判断 fragile。
- 对 (b)：proposal 的 counter argument 合理——gold labels 不总是有，且 
  agreement 最优 ≠ downstream inference 最优。但这个论点在 Baumann 数据集
  上（有 gold）说服力减弱。

结论：trivial alternative 威胁中等。formal framework 有真实增量价值，但该增量
主要面向 methodologically-oriented 受众，对广大 NLP 实践者来说 "just report 
multiple configs" 可能已够用。
```

```
【前提假设检验】:

核心 claim 的逻辑链中，以下环节属于未经充分验证的假设：

1. "LLM annotation 中 estimand 在 configurations 之间保持恒定"
   ——这是论证 Auspurg 批评不适用的关键前提。但严格来看，不同 prompt 
   措辞和模型可能隐含度量不同 construct（例如一个 prompt 对 "toxicity" 
   的定义比另一个更宽泛）。proposal 的 E/N/U 分类中 Type E ("semantically 
   equivalent prompt rephrasings") 假设语义等价性，但"语义等价"本身需要
   验证——这恰恰是 computational social science 中 construct validity 的核心
   难题。如果 estimand 实际不恒定，整个 multiverse 框架的 epistemological 
   justification 就被削弱。

2. "No configuration is statistically misspecified"
   ——这个假设忽略了：某些 model+prompt 组合可能产生 systematically biased 
   labels（e.g., 模型的已知 demographic bias、某些 prompt 诱导的 position 
   bias）。这些 biased configurations 的纳入是否等价于 Auspurg 批评的 
   "including unjustified models"？proposal 用 E/N/U 分类试图排除这些，但
   排除的依据（Type N 的判定标准）本身需要 domain expertise，与 "no theory 
   ranks choices a priori" 的另一假设存在张力。

3. "Interaction effects dominate → full factorial is needed"
   ——引自 McLaren et al.，但并不 formally 蕴含需要 full Cartesian product。
   Fractional factorial designs 或 Latin hypercube sampling 可能以更低成本
   达到类似覆盖。proposal 未讨论为何不采用这些替代设计。

总结：前提假设 1 是最关键的风险点——如果审稿人挑战 "estimand constancy"，
proposal 的整个 epistemological 论证链就需要重新校准。
```

```
【3 维度打分】:

1. Novelty: 弱-中 — 
   核心贡献是跨领域方法迁移：将已成熟的 specification curve analysis 
   (Simonsohn et al., 2020)、E/N/U classification (Del Giudice & Gangestad, 
   2021)、Boba DSL (Liu et al., 2021) 组合后适配到 LLM annotation 领域。
   每个组件都有现成原型，组合本身是 "obvious next step"——读完 Baumann 
   et al. (2025) 和 Simonsohn et al. (2020) 后，一个有方法论背景的研究者
   自然会想到这一步。gap 是真实的（无人做过 formal multiverse for LLM 
   annotation），但 gap 存在 ≠ 填补 gap 有足够 novelty。Proposal 对 
   Auspurg debate 的 engagement 是亮点（论证 LLM annotation 恰好满足 
   multiverse 有效条件），但这更像 methodological positioning 而非新方法。
   
   如果核心发现是 positive（e.g., "40% 假设 fragile，model choice 驱动
   最多 variance"），审稿人大概率会说 "I would have guessed this given 
   Baumann et al." 而非 "surprising"。

2. Significance: 中 — 
   问题本身确实重要且时效性强。LLM-mediated annotation 正在快速普及，
   researcher degrees of freedom 是真实隐患（Baumann 31% error rate, 
   Kosch & Feger 的 "prompt-hacking" 概念）。NLP+CSS 社区有明确需求
   （workshop calls for "LLMs for measurement and downstream inference"）。
   但目标受众偏窄——需要同时关心 (a) LLM annotation 和 (b) formal 
   statistical inference 的研究者。对于 broader NLP 社区（关心 SOTA 
   performance）或 broader social science 社区（可能不用 LLM annotation），
   直接影响有限。toolkit 的实际采用率决定长期影响，但这无法在 paper 
   层面证明。

3. Related Work: 强 — 
   这是 proposal 最强的维度。对 landscape 的覆盖全面且准确：
   - 准确区分了 Baumann (problem documentation)、McLaren (complementary 
     benchmarking)、Kosch & Feger (conceptual analogy)、Ye et al. (HCI, 
     not annotation) 各自的定位
   - 与 Auspurg/Ganslmeier & Vlandas debate 的 substantive engagement 
     是有深度的 methodological positioning
   - 所有关键引用经调研验证为真实存在且描述准确
   - 差异化定位清晰：无人做过 "formal multiverse + joint inference + 
     variance decomposition for LLM annotation"
   - 唯一轻微不足：未提及 prediction-powered inference (PPI) 文献
     （Angelopoulos et al., 2023）作为处理 LLM label noise 的替代
     统计框架
```

```
【概率估计】: 

CoRL 2026: 2-5% 中位 3% （完全 out of scope，大概率 desk reject）

若投稿其自身目标 venue（AAAI 2027 / EMNLP 2026 / TACL）:
[20% - 32%] 中位 25%

【估计理由】:
idea 的 gap 真实存在、问题重要、related work 覆盖出色，这些保证了下限不低
（不至于被认为 "没有贡献"）。但 novelty 维度是明确的天花板限制因素：
(1) 核心贡献是已知方法的跨领域迁移，属 "obvious next step"；
(2) trivial alternative ("run multiple configs and report range") 能覆盖大部分
    实践价值，formal framework 的增量主要在统计严谨性而非洞见；
(3) 预期发现如果 positive，大概率是 confirmatory（确认 Baumann 等已记录的
    现象）而非 surprising。
这使得 paper 最可能落在 "solid but incremental" 区间，对于 competitive venue 
(AAAI ~23% AR, EMNLP ~22% AR) 来说处于 borderline。TACL 作为 journal 对 
thoroughness 有更高容忍度，可能是最佳匹配 venue。

【主要风险】:
1. Novelty 不足 —— 审稿人可能总结为 "straightforward application of 
   specification curves to LLM pipelines"，认为 methodological contribution 
   不够深，尤其是当所有组件（specification curve, E/N/U, Boba DSL）都有
   现成实现时
2. Estimand constancy 假设受质疑 —— 如果审稿人不接受 "不同 prompt/model 
   度量的是同一 construct" 这一前提，proposal 的核心 epistemological 
   argument（Auspurg 批评不适用）就会被动摇，进而削弱整个框架的理论基础
```

---

Sources:
- [Baumann et al. - Large Language Model Hacking (arXiv 2509.08825)](https://arxiv.org/abs/2509.08825)
- [McLaren et al. - Magic Words or Methodical Work? (arXiv 2603.26898)](https://arxiv.org/abs/2603.26898)
- [Auspurg - Robustness is better assessed with a few thoughtful models (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas - Reply to Auspurg (PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Del Giudice & Gangestad - A Traveler's Guide to the Multiverse (AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Kosch & Feger - Prompt-Hacking: The New p-Hacking? (CACM 2026)](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)
- [Ye et al. - Navigating the Conceptual Multiverse (arXiv 2604.17815)](https://arxiv.org/abs/2604.17815)
- [Carlson & Burbano - LLMs to Annotate Data in Management Research (SMJ 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)
- [Variance-Aware LLM Annotation for Strategy Research (arXiv 2601.02370)](https://arxiv.org/pdf/2601.02370)
- [Brittlebench (arXiv 2603.13285)](https://arxiv.org/pdf/2603.13285)


【原始 proposal（允许参考但不是主要依据）】:
# Multiverse Analysis Framework for LLM-Mediated Social Science Pipelines

## Description
We propose the first formal multiverse analysis framework for LLM-mediated social science annotation pipelines, combining principled configuration selection with joint statistical inference. While recent work documents that LLM pipeline choices produce contradictory conclusions (Baumann et al., 2025: ~31% error rate) and that interaction effects between choices dominate main effects (McLaren et al., 2026), no existing framework applies formal multiverse methodology — and the methodological community is actively debating whether exhaustive enumeration overstates uncertainty (Auspurg, PNAS 2025). We address both gaps. First, we adapt Del Giudice & Gangestad's (2021) E/N/U (Equivalence/Nonequivalence/Uncertainty) classification framework to LLM annotation, providing a principled methodology for constructing task-conditional multiverses: dimensions where one configuration is objectively superior (e.g., temperature=0 for deterministic tasks) are resolved rather than enumerated, while genuinely equivalent alternatives (e.g., semantically equivalent prompt rephrasings) populate the multiverse. Task-conditional constraints expressed in a Boba-style DSL reduce the naïve 810-configuration Cartesian product to ~90–270 principled specifications per task. Second, we adapt specification curve analysis (Simonsohn et al., 2020) with permutation-based joint inference to classify substantive social-science hypotheses as robust, fragile, or sign-inconsistent across the annotation multiverse. Third, we perform formal variance decomposition (factorial ANOVA over specification space) to quantify which pipeline dimensions and interactions drive the most inferential instability — extending McLaren et al.'s descriptive benchmarking to statistical attribution. We validate on 10 tasks from Baumann et al.'s publicly available replication data (37 tasks, MIT license) spanning binary, multi-class, ordinal, and subjective annotation, with supplementary validation on the SALT-NLP CSS benchmark. All inference is run via API on 6 models spanning diverse architectures (Llama 4 Maverick, Qwen 3.5, DeepSeek V4 Flash, Gemma 4, Mistral Medium 3.5, plus one proprietary anchor). We engage directly with Auspurg's (PNAS 2025) critique of brute-force multiverse analysis, arguing that LLM annotation is precisely the setting where her concerns do not apply: the estimand remains constant across configurations, no configuration is statistically misspecified, and no established theory ranks pipeline choices a priori. We release an open-source Python toolkit (llm-multiverse) integrating E/N/U classification, constraint-based configuration enumeration, batched API annotation, specification curve visualization, and joint inference — with SMART-compatible pre-registration templates enabling researchers to document and justify their multiverse construction before running experiments.

## Core Problem
When researchers use LLMs to annotate text for social science, numerous pipeline choices (model, prompt, temperature, aggregation) constitute researcher degrees of freedom that can produce contradictory conclusions — yet no formal framework systematically quantifies how these choices jointly affect downstream statistical inference. This is not merely a benchmarking problem: existing work documents that choices matter and interact (Baumann et al., 2025; McLaren et al., 2026), but none applies formal joint inference methods to determine whether a substantive social-science finding is robust across the space of defensible pipeline configurations.

## Opportunity
The 'LLM hacking' paper (Baumann et al., 2025) showed ~31% of hypotheses yield incorrect conclusions from arbitrary LLM configuration choices, and Carlson & Burbano (2026, SMJ) recommend sensitivity analysis but provide no formal methodology. McLaren et al. (2026) demonstrate that interaction effects between pipeline choices dominate main effects, yet use only one-at-a-time variation without joint inference. Meanwhile, multiverse analysis / specification curve methods are mature in psychology and economics but have never been adapted to the unique structure of LLM annotation pipelines, where the degrees of freedom (prompt wording, model family, temperature, role, output parsing) are qualitatively different from traditional analytic choices — and, crucially, where Auspurg's (PNAS 2025) critique of brute-force multiverse enumeration does not apply because (a) the estimand remains constant across pipeline configurations, (b) no configuration is 'statistically misspecified' in the way a regression omitting fixed effects is, and (c) no established theory ranks one prompt or model above another a priori. The NLP+CSS community explicitly calls for work on 'LLMs for measurement and downstream statistical inference.'

## Landscape
The LLM hacking paper (Baumann et al., 2025) tested 18 LLMs × 2,361 hypotheses × 13M labels, documenting the problem's scale but only evaluating 21 ad-hoc mitigations — no formal multiverse inference. 'Magic Words or Methodical Work?' (McLaren et al., arXiv March 2026) systematically varied model, prompt template, and learning approach for LLM annotation in political science and found that interaction effects dominate main effects; however, their design is one-factor-at-a-time (not full factorial), produces no specification curve or joint inference test, and their question is 'which pipeline performs best?' rather than 'is a substantive finding robust across pipelines?' — making their work complementary benchmarking, not a multiverse analysis. The variance-aware annotation framework (2026) identifies 5 variance sources but offers protocol guidance, not statistical inference. The benchmarking debiasing paper (Audinet de Pieuchon et al., EMNLP 2025) compares DSL vs PPI but only for fixed pipeline configurations. Brittlebench (2026) measures prompt sensitivity but not downstream inferential consequences. 'Prompt-Hacking: The New p-Hacking?' (Kosch & Feger, CACM 2026) draws the conceptual analogy but offers no formal method. 'Navigating the Conceptual Multiverse' (Ye et al., arXiv April 2026) applies multiverse thinking to LLM conceptual framing as an interactive HCI system, but does not address annotation pipelines or statistical inference. 'Multi-Perspective LLM Annotations' (Mehrotra et al., arXiv March 2026) introduces Perspective-Driven Inference for subjective tasks but assumes a single pipeline per perspective. The PNAS debate between Auspurg (2025) and Ganslmeier & Vlandas (2025) on whether exhaustive multiverse enumeration overstates uncertainty provides the key methodological foil: we adopt Del Giudice & Gangestad's (2021) E/N/U classification framework to construct principled, task-conditional multiverses rather than naïve Cartesian products. No existing work provides a formal multiverse analysis with principled configuration selection and joint statistical inference for LLM annotation pipelines.

## Approach
We propose a three-stage framework: (1) Principled Multiverse Construction using Del Giudice & Gangestad's (2021) E/N/U (Equivalence / Nonequivalence / Uncertainty) classification. For each annotation task, we classify every pipeline dimension: dimensions where alternatives are effectively equivalent (Type E: e.g., semantically equivalent prompt rephrasings) populate the multiverse; dimensions where one option is objectively superior (Type N: e.g., temperature=0 for deterministic classification tasks, label-based output over numerical scores) are resolved to the best option only; dimensions where defensibility is uncertain (Type U: e.g., model family, definition inclusion) generate separate stratified multiverses. Task-conditional constraints are expressed formally using a Boba-style DSL: e.g., IF task_type='classification' AND num_classes≤3 THEN temperature∈{0.0, 0.3} AND output_format∈{'label'}. This reduces the naïve Cartesian product (~810 configurations from 6 models × 5 prompts × 3 temperatures × 3 roles × 3 aggregation strategies) to a principled, task-specific multiverse of ~90–270 defensible configurations per task, with explicit justification for every inclusion/exclusion. (2) Full-factorial execution across the principled multiverse. The six models span diverse architectures: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE), DeepSeek V4 Flash (284B MoE), Gemma 4 (26B MoE), Mistral Medium 3.5 (128B dense), plus one proprietary anchor (GPT-4o or Claude). All models are accessed via API (DeepSeek API, Together AI, OpenRouter, Google AI) for cost-efficiency; batched annotation (25 items/prompt) minimizes token costs. For each configuration, generate labels for the full corpus, then compute the downstream statistical estimate (e.g., regression coefficient, group difference). (3) Specification curve analysis with joint inference (Simonsohn et al., 2020): rank all specifications by effect size, display the specification curve with indicator rows for each pipeline dimension, and apply a permutation-based joint inference test to classify hypotheses as robust (sign-consistent and jointly significant), fragile (sign-inconsistent or significance-dependent on configuration), or null (no configuration yields significance). Additionally, perform variance decomposition (ANOVA over the specification space) to quantify which pipeline dimensions and their interactions drive the most inferential instability — extending McLaren et al.'s descriptive interaction findings to formal statistical attribution. Validate on 10 annotation tasks drawn from Baumann et al.'s publicly available replication data (37 tasks, MIT license, github.com/joebaumann/llmhacking), selected to span binary classification, multi-class categorization, ordinal scaling, and subjective judgment. Supplementary validation uses Gilardi et al.'s (PNAS 2023) Harvard Dataverse data and the SALT-NLP CSS benchmark (Ziems et al., 2024). Release an open-source Python toolkit (llm-multiverse) that wraps the full pipeline: E/N/U classification interface → task-conditional constraint specification → configuration enumeration → batched API annotation → specification curve visualization → joint inference test. The toolkit integrates with the SMART pre-registration framework (2025) so researchers can document and justify their multiverse construction before running experiments.

## Resource Estimate
{'manual': {'gpu_hours': '0 (all inference via API — no self-hosted GPU needed)', 'api_cost': '$1,200–$2,000 for open-weight models via API providers (DeepSeek V4 Flash: ~$100–200 via DeepSeek API; Llama 4 Maverick: ~$250–470 via Together AI; Qwen 3.5: ~$475–950 via OpenRouter; Gemma 4: ~$65–130 via Google; Mistral Medium 3.5: ~$300–650 via Mistral/OpenRouter; proprietary anchor: ~$200–400). Estimates assume batched annotation (25 items/prompt) across ~90–270 configs × 10 tasks × 1,000–3,000 samples. Total: ~500M–1.2B tokens across all models.', 'timeline': '5–6 months (1 month framework design + E/N/U methodology, 2 months implementation + experiments, 1 month analysis + variance decomposition, 1 month writing + revision)', 'estimated_total_cost': '$1,200–$2,000'}, 'human_in_loop': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same API inference, slightly optimized configuration space with Claude-assisted E/N/U classification)', 'timeline': '3.5–4.5 months (2 weeks framework design with Claude scaffolding, 6 weeks experiments, 3 weeks analysis, 3 weeks writing)', 'claude_api_cost': '$150–$250 (Sonnet for code generation, experiment orchestration, and paper drafting; ~50M input tokens with caching)', 'estimated_total_cost': '$1,150–$1,850'}, 'auto_research': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same inference costs)', 'timeline': '2–3 months (automated experiment sweeps, parallelized API calls, auto-generated specification curves)', 'claude_api_cost': '$400–$600 (Opus for research design + Sonnet for bulk code generation and analysis; ~100M tokens total)', 'estimated_total_cost': '$1,400–$2,200', 'speed_bottleneck': 'API rate limits on proprietary LLMs (GPT, Claude) for anchor comparisons; sequential dependency between label generation and downstream inference computation; OpenRouter rate limits for Qwen 3.5 and Mistral Medium 3.5'}}

## Inspired By
Gap: LLM hacking paper shows the problem (31% error rate), McLaren et al. show interaction effects dominate, but no formal multiverse framework with joint inference exists. Pattern: Cross-domain transfer of specification curve analysis (psychology/economics) and the E/N/U defensibility framework (Del Giudice & Gangestad, 2021) to LLM annotation pipelines. Epistemological justification: Auspurg's (PNAS 2025) critique of brute-force multiverse analysis does not apply to LLM pipelines because the estimand is constant and no configuration is statistically misspecified — making this precisely the setting where multiverse analysis is epistemically justified. Field guide evidence: Carlson & Burbano (2026) guidelines call for sensitivity analysis; variance-aware annotation (2026) identifies 5 variance sources; the NLP+CSS workshop explicitly seeks work on 'LLMs for measurement and downstream statistical inference.'

## Target Venues
- AAAI 2027 (full paper deadline: ~July 28, 2026 — strong fit for methods + empirical validation paper; primary target)
- TACL (rolling submission, any month — ideal for extended journal-length treatment with theoretical results on E/N/U framework + formal variance decomposition)
- CSCW 2027 (rolling submission — fits the sociotechnical framing of researcher-tool interaction and pre-registration protocol)
- EMNLP 2026 Industry Track (deadline: ~June 16, 2026 — if framed around practitioner toolkit; stretch target)
- FAccT 2027 (fits the transparency/accountability angle of documenting researcher degrees of freedom in LLM-mediated research)

## Key References
- Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation (arXiv 2025, Baumann et al.) — documents the 31% error rate problem; replication data publicly available under MIT license at github.com/joebaumann/llmhacking
- Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation (arXiv 2603.26898, McLaren et al., March 2026) — one-at-a-time benchmarking showing interaction effects dominate; releases CodeBook Lab tools; complementary but no joint inference
- Specification Curve Analysis (Nature Human Behaviour 2020, Simonsohn, Simmons & Nelson) — canonical joint inference method we adapt
- Increasing Transparency Through a Multiverse Analysis (Perspectives on Psychological Science 2016, Steegen, Tuerlinckx, Gelman & Vanpaemel) — original multiverse analysis framework
- A Traveler's Guide to the Multiverse: Promises, Pitfalls, and a Framework for the Evaluation of Analytic Decisions (Advances in Methods and Practices in Psychological Science 2021, Del Giudice & Gangestad) — E/N/U classification framework for principled configuration selection
- Robustness is better assessed with a few thoughtful models than with billions of regressions (PNAS 2025, Auspurg) — critique of exhaustive multiverse enumeration; we argue LLM annotation is precisely the case where her critique does not apply
- Reply to Auspurg: On the limits of 'justified' model spaces (PNAS 2025, Ganslmeier & Vlandas) — defense of comprehensive multiverse analysis when theory cannot adjudicate
- The Use of LLMs to Annotate Data in Management Research: Foundational Guidelines and Warnings (SMJ 2026, Carlson & Burbano)
- Variance-Aware LLM Annotation for Strategy Research (arXiv 2026)
- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025, Audinet de Pieuchon et al.)
- Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity (arXiv 2026)
- Can Unconfident LLM Annotations Be Used for Confident Conclusions? (NAACL 2025, Gligorić et al.)
- Prompt-Hacking: The New p-Hacking? (Communications of the ACM 2026, Kosch & Feger)
- Navigating the Conceptual Multiverse (arXiv 2026, Ye et al.)
- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (arXiv 2026, Mehrotra et al.)
- Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs (arXiv 2026, Cui & Alexander)
- To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation (arXiv 2024)
- SMART: Systematic Multiverse Analysis Registration Tool (Royal Society Open Science 2025) — pre-registration workflow for multiverse construction
- Boba: Authoring and Visualizing Multiverse Analyses (Liu et al., 2021) — DSL with constraint specification for principled multiverse pruning
- Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways (arXiv 2024) — empirical evidence for task-conditional configuration defensibility


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8cc99b49-227b-40d2-bf95-a73f10755c51",
  "type": "user",
  "uuid": "8213f2ef-ce92-4dfb-9568-1ba1ddc16a69",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:30:18.816Z_

```json
{
  "parentUuid": "8213f2ef-ce92-4dfb-9568-1ba1ddc16a69",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "cbdff7a5-20ce-42a8-a0db-469bdb469d44",
  "timestamp": "2026-05-20T03:30:18.816Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:30:18.816Z_

```json
{
  "parentUuid": "cbdff7a5-20ce-42a8-a0db-469bdb469d44",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6de09c46-7be2-4147-bb66-1efd741fd707",
  "timestamp": "2026-05-20T03:30:18.816Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information for a thorough evaluation. L…",
  "leafUuid": "6de09c46-7be2-4147-bb66-1efd741fd707",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM annotation multiverse analysis proposal",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:30:52.073Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as the Meta Judge.

Let me first extract the key numbers and judgments:

**Reviewer 1:**
- CoRL: 0-2% (desk reject)
- Suitable venues: [25% - 38%] 中位 30%
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Key risks: venue mismatch (fatal for CoRL), novelty "apply X to Y", trivial alternative, PPI alternative


**Reviewer 2:**
- CoRL: 0-2%, 中位 ~0%
- Suitable venues: [20% - 35%], 中位 ~27%
- Novelty: 中（偏弱）
- Significance: 中（偏强）
- Related Work: 强
- Key risks: venue mismatch, "Apply X to Y" novelty, E/N/U subjectivity paradox

**Reviewer 3:**
- CoRL: 2-5%, 中位 3%
- Suitable venues: [20% - 32%], 中位 25%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强

Now I'm looking at the consensus across all three reviewers. They're remarkably aligned on several fronts: CoRL acceptance is essentially zero to minimal (0-5% range), with Reviewer 1 and 2 both seeing it as a desk reject scenario. All three agree the paper would be better suited for venues in the 25-30% acceptance range, and they consistently rate novelty as weak-to-medium with the core issue being an "apply X to Y" contribution. The related work is universally strong, which is good, but the significance hovers around medium across the board. Looking at where the reviewers align, there's unanimous agreement on several critical points: CoRL is the wrong venue, the novelty is limited to applying existing methods across domains, the related work coverage is thorough, and there are three major methodological concerns—the trivial alternative of just running multiple configurations, the subjectivity in E/N/U classification, and the estimand constancy assumption. They also all recognize the problem itself is important and timely, and that this is genuinely the first formal multiverse analysis for LLM annotation, though the expected results would likely confirm what we already suspect.

There's also a tension two reviewers flagged between claiming no theory ranks the design choices and then using E/N/U classification to do exactly that. On the outlier side, one reviewer brought up PPI as a methodological alternative, another suggested fractional factorial designs instead of the full Cartesian product, and one referenced Brittlebench as a related benchmark. Now I'm calculating the variance across the three venue recommendations to see how much disagreement there actually is on where this could fit. should emphasize this as a critical issue in my report. Now I'm assessing the practical feasibility of the work itself—the proposal relies on API calls rather than training, with modest costs around $1,200-$2,000 and a realistic 5-6 month timeline. The annotation work is minimal since it's just categorizing responses as excellent, neutral, or unusable against existing benchmark data. Let me structure the final output to highlight both the venue mismatch and the implementation viability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6de09c46-7be2-4147-bb66-1efd741fd707",
  "isSidechain": false,
  "requestId": "req_011CbD7Xd2kdpyfvr2hQrnqJ",
  "type": "assistant",
  "uuid": "eaa3d425-17ad-449e-988d-8236ee708a1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNN9j8mcKGTpUtHRUEsjr3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19159,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3277,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 19159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19159
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T03:31:43.428Z_

【阶段】: Meta Judge
【三次中位】: [30%, 27%, 25%]  std=2.1%
【共识维度】:
- **Venue 不匹配（致命）**: 3/3 一致判定 proposal 主题（LLM 标注管道方法论）与 CoRL 2026（机器人学习）完全不匹配，将被 desk reject。Proposal 自身列出的目标 venue 也不含 CoRL。
- **Novelty（中偏弱）**: 3/3 一致认为核心贡献属"将已有方法 X 迁移到领域 Y"，specification curve / E/N/U / Boba DSL 各组件均为现成工具，组合本身是 obvious next step。预期发现若为 positive 则 confirmatory 而非 surprising。
- **Related Work（强）**: 3/3 一致认为文献覆盖全面、引用准确、差异化定位清晰，是 proposal 最强维度。
- **Significance（中偏强）**: 3/3 一致认为问题真实存在且时效性好（Baumann 31% error rate, McLaren interaction effects, Carlson & Burbano 呼吁），但受众偏窄（需同时关心 LLM annotation 和 formal inference 的研究者）。
- **Trivial Alternative 威胁（中等）**: 3/3 均指出"跑 N 个 config 报告 range"的朴素 sensitivity analysis 可覆盖大部分实践价值，formal framework 增量主要在统计严谨性。
- **E/N/U 分类主观性问题**: 3/3 均指出 E/N/U 分类本身引入新的研究者自由度，与"有原则裁剪"的卖点存在张力，且缺乏 inter-rater reliability 验证。
- **Estimand 恒定假设风险**: 3/3 均质疑不同 prompt/model 是否真的度量同一 construct，这是 Auspurg 反驳论证的关键前提。
- **"No theory ranks choices" 与 Type N 分类的张力**: 2/3（R2, R3）指出 proposal 一方面声称"无理论排序 pipeline 选择"（论证 Auspurg 不适用），另一方面 E/N/U 中 Type N 又声称某些选择"客观更优"，存在内部矛盾。

【异常维度】:
- R3 独有：提出 fractional factorial / Latin hypercube sampling 作为 full Cartesian product 的替代实验设计——观点有效但非核心打击点，降权处理。
- R1/R3 提到 PPI（Prediction-Powered Inference）作为替代路线，R2 未提及——PPI 对比是一个合理的 related work gap，但非致命，可补。

【最终概率】:
- **CoRL 2026**: [0% - 2%] 中位 1%（desk reject，venue 完全不匹配）
- **合适 venue（AAAI/EMNLP/TACL 等，proposal 自身目标）**: [22% - 33%] 中位 27%

【一致性】: 高（std=2.1%，三位审稿人在所有 rubric 维度上判决方向一致，无严重分歧）

【综合理由】:

**CoRL 概率**：三位审稿人无分歧——proposal 是纯 NLP+CSS 方法论工作，与机器人学习零交集，CoRL 明确要求 robotics focus，将被 desk reject。取三人最严端的 0% 附近，给极小上界 2%（容纳极端小概率事件如 AC 误判 scope）。

**合适 venue 概率**：三位中位数 30/27/25，std 仅 2.1%，属高一致性区间。按规则取中位附近并缩窄：

- **Idea 天花板约 35%**：Novelty 中偏弱（apply X to Y，confirmatory findings）+ Significance 中偏强 → 即使实验完美也难突破 35%。Related Work 强是加分但无法弥补 novelty 短板。
- **地板约 22%**：gap 真实存在、问题有文献支撑、方法论组合确实无人做过，不至于被判"无贡献"。
- **中位 27%**：落在三人中位数的几何中心。偏向 R2/R3 较严的判断（R1 的 30% 是三人中最宽松的，不进一步上提）。

核心限制因素是 **Novelty 天花板**：当核心方法论工具（specification curve, E/N/U, variance decomposition, Boba DSL）全部现成、组合是 obvious next step、预期发现是 confirmatory 时，在 AAAI (~23% AR) / EMNLP (~22% AR) 等高竞争 venue 处于 borderline。TACL 作为期刊对方法论深度容忍度更高，可能是最佳匹配。

【建议】: 边缘（但**必须更换 venue**——投 CoRL 是确定性的 desk reject，应投其自身列出的 AAAI 2027 / TACL / EMNLP 2026 等）

【实施评估】:
- **计算资源**: 零 GPU 需求，全部通过 API 推理（DeepSeek API, Together AI, OpenRouter, Google AI 等）。6 个模型 × ~90-270 configs × 10 tasks，总计约 500M-1.2B tokens。
- **数据需求**: 主要依赖 Baumann et al. 公开复制数据（37 tasks, MIT license, github.com/joebaumann/llmhacking），补充 Gilardi et al. (PNAS 2023) Harvard Dataverse 数据和 SALT-NLP CSS benchmark。均公开可得，无数据获取障碍。
- **人工介入**: E/N/U 分类需要领域专家判断（每个任务 × 每个维度），工作量中等但不需要大规模标注。建议做 inter-rater reliability 验证（2-3 位标注者），需额外 1-2 周。
- **训练需求**: 无模型训练。纯推理 + 统计分析。
- **新 Benchmark**: 不需要。使用已有数据集。
- **预估周期**: 5-6 个月（含框架设计 1 月 + 实验 2 月 + 分析 1 月 + 写作 1 月）。人机协作模式可压缩至 3.5-4.5 月。API 费用 $1,200-$2,000。**实施门槛低，是本 proposal 的优势之一。**
- **关键瓶颈**: API rate limits（特别是 proprietary anchor 模型）、OpenRouter 对 Qwen 3.5 和 Mistral Medium 3.5 的限流。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa3d425-17ad-449e-988d-8236ee708a1c",
  "isSidechain": false,
  "requestId": "req_011CbD7Xd2kdpyfvr2hQrnqJ",
  "type": "assistant",
  "uuid": "37d477e9-ff12-4848-a9ec-50208b188db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNN9j8mcKGTpUtHRUEsjr3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19159,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3277,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 19159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19159
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information for a thorough evaluation. L…",
  "leafUuid": "37d477e9-ff12-4848-a9ec-50208b188db6",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM annotation multiverse analysis proposal",
  "sessionId": "4b04dab1-638b-4822-9511-61b3944e7174"
}
```

---
