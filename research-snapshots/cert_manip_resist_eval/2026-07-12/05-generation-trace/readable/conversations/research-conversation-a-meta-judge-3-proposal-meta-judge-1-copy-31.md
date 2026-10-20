# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7.jsonl`
- **Structured JSON:** [`f8d273f721bca757751f.json`](../../sessions/f8/f8d273f721bca757751f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:47:58.560Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:47:58.560Z",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to produce the triage assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Large Language Model Hacking] (arXiv 2509.08825, Baumann et al., 2025): 核心问题论文。在 18 个 LLM × 37 个标注任务上发现 ~31% 假设得出错误结论，效应量偏差 40-77%。提供了公开复制数据（MIT 许可），但仅测试 21 个 ad-hoc 缓解策略，无正式 multiverse 推断。Proposal 拟用其数据作为验证基础——这一点成立。\n- [Magic Words or Methodical Work?] (arXiv 2603.26898, McLaren et al., March 2026): 在政治科学标注中系统变换模型、提示模板、学习方法，发现交互效应主导主效应。但其设计为 one-factor-at-a-time（非全因子），不产出 specification curve 或联合推断——proposal 对其定位为\"互补性基准测试\"是准确的。\n- [Prompt-Hacking: The New p-Hacking?] (CACM 2026, Kosch & Feger): 明确画出 prompt hacking ↔ p-hacking 概念类比，但仅为观点文章，不提供正式方法论。Proposal 的定位准确。\n- [Robustness is better assessed with a few thoughtful models…] (PNAS 2025, Auspurg): 批评穷举式 multiverse 分析过度估计不确定性。[Reply to Auspurg] (PNAS 2025, Ganslmeier & Vlandas) 进行了回应。这一方法论辩论是真实的、高影响力的。Proposal 试图论证 LLM 标注是 Auspurg 批评不适用的精确场景——这是一个有深度的方法论贡献。\n- [A Traveler's Guide to the Multiverse] (AMPPS 2021, Del Giudice & Gangestad): E/N/U 分类框架确实存在且被广泛引用。将其迁移到 LLM 标注管道是 proposal 的核心方法论创新之一。\n- [Navigating the Conceptual Multiverse] (arXiv 2604.17815, Ye et al., April 2026): 将 multiverse 思维应用于 LLM 概念框架的 HCI 交互系统，不涉及标注管道或统计推断——确认与 proposal 不直接竞争。\n- [Carlson & Burbano] (SMJ 2026): 推荐敏感性分析但不提供正式方法。[Variance-Aware LLM Annotation] (arXiv 2601.02370, 2026): 识别 5 个方差来源但仅提供协议指导，不含统计推断。\n- 调研总结：LLM 标注管道中的\"研究者自由度\"问题已被多篇高影响力论文充分记录（Baumann、McLaren、Kosch & Feger），且社区明确呼吁正式方法论解决方案（Carlson & Burbano）。然而，截至 2026 年 5 月，**确实没有任何现有工作将正式的 multiverse 分析 + 联合推断应用于 LLM 标注管道**。Proposal 填补的 gap 是真实存在的。但 gap 的性质是\"将心理学/经济学中成熟的方法迁移到新领域\"，而非提出全新方法。\n\n【Trivial Alternative 检验】:\n存在一个显而易见的 trivial alternative：**简单地用 3-5 个不同配置运行标注，报告结论是否一致**（即 Carlson & Burbano 2026 推荐的非正式敏感性分析）。Proposal 对此有预期回应：(a) 非正式分析无法提供联合统计推断（hypothesis 是 robust 还是 fragile 的正式判定），(b) 不含方差分解（不知道 *哪些* 维度驱动不稳定性），(c) 无法区分 E/N/U 维度（可能将不等价的配置混入分析）。\n\n增量价值评估：**真实但有限**。正式框架的主要增量在于 (1) variance decomposition 可产出 actionable 发现（如\"模型选择解释 40% 的推断方差，而 prompt 措辞仅 8%\"），(2) 联合推断测试提供了非主观的 robustness 判定标准。但如果实证结果显示\"大多数维度的影响相似\"或\"大多数假设都是 fragile\"，则增量价值会大幅缩水——因为这与简单敏感性分析的结论无实质区别。\n\n【前提假设检验】:\n核心逻辑链中有以下未经验证的假设：\n\n1. **E/N/U 分类可在 LLM 标注场景中可靠执行**：Del Giudice & Gangestad 的 E/N/U 框架是为传统分析决策设计的（如变量操作化、离群值处理）。Proposal 假设这一分类可以自然迁移到 LLM 管道维度（如 prompt 措辞、温度、模型选择），但 LLM 管道维度的\"等价性\"判断标准是什么？谁来判定两个 prompt 是\"语义等价\"的（Type E）vs.\"不确定\"的（Type U）？这个分类过程本身可能引入主观性——恰恰是框架试图消除的问题。这是一个潜在的循环论证风险。\n\n2. **Auspurg 批评不适用于 LLM 标注的论证**：Proposal 提出三个理由（estimand 恒定、无统计误设、无先验理论排序），但第三点值得质疑——随着 LLM 标注实践成熟，社区 *正在* 形成关于最佳实践的共识（如 temperature=0 优于高 temperature 用于分类任务）。如果\"无先验理论排序\"的前提随着领域发展而削弱，框架的认识论基础也会动摇。\n\n3. **下游统计推断对标注噪声的敏感性是线性/可分解的**：ANOVA 方差分解假设因子效应可加性分解，但 McLaren et al. 已经证明交互效应主导——高阶交互效应可能使简单的方差分解难以解读。\n\n【3 维度打分】:\n1. Novelty: 【中】— 核心贡献是将心理学/经济学中成熟的方法论（specification curve analysis + E/N/U 框架）迁移到 LLM 标注管道这一新领域。Gap 是真实的（截至调研，确实无人做过此迁移），E/N/U 的领域适配和 Auspurg 辩论的参与增加了方法论深度。但本质上是 cross-domain transfer，不是方法论创新。每个组件（multiverse analysis, specification curves, E/N/U, ANOVA variance decomposition）单独来看都是现有方法的应用。一旦 Kosch & Feger (2026) 画出了 prompt-hacking ≈ p-hacking 的类比，将 multiverse analysis 应用于 LLM 管道是一个相当 obvious 的下一步。审稿人可能的反应：**\"competent application of existing methods to a natural new domain, but the intellectual leap is moderate.\"**\n\n2. Significance: 【中偏强】— 问题本身的重要性毋庸置疑：LLM 标注在社会科学中的采用正在爆炸性增长，31% 的假设得出错误结论（Baumann et al.）是一个令人震惊的数字。一个正式的 robustness 评估框架对该社区有真实需求。Variance decomposition 的潜在发现（哪些管道维度驱动最多不稳定性）具有直接可操作性。开源工具包 + pre-registration 模板增强了实践影响力。但主要受众是使用 LLM 进行标注的社会科学家，这是一个 specific niche（虽然快速增长）。对核心 NLP/CL 社区的方法论贡献相对有限——更多是应用层面的贡献。\n\n3. Related Work: 【强】— 这是 proposal 最突出的维度。对已有工作的覆盖非常全面，正确识别了从问题记录（Baumann, McLaren）到概念类比（Kosch & Feger）到方法论辩论（Auspurg vs. Ganslmeier/Vlandas）的完整谱系。每篇工作的差异化定位清晰且准确（经调研验证）。特别值得肯定的是对 Ye et al.、Mehrotra et al. 等容易混淆的近期工作的精确区分。与 McLaren et al. 的定位（\"互补性基准测试 vs. multiverse 推断\"）是准确且有说服力的。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \nSignificance 接近强——问题重要、社区有真实需求、潜在发现可操作。Related Work 强——coverage 全面、定位清晰。但 **Novelty 是限制上界的核心维度**：贡献的本质是 cross-domain method transfer（将成熟的心理学方法论搬到 LLM 标注），而非提出新方法或产出反直觉发现。一旦 Kosch & Feger (2026) 画出了类比，specification curve → LLM annotation 的迁移是相当 natural 的一步。最可能的审稿人反应是 \"well-executed application paper\"——尊重但不兴奋。如果 variance decomposition 产出了意外发现（如某个被忽视的维度驱动了大部分方差），可以推高概率到 ~33%；如果主要发现仅为 \"pipeline choices matter and some hypotheses are fragile\"（已被 Baumann et al. 定性证实），则下探至 ~22%。\n\n【主要风险】:\n1. **Novelty 不足的 reject 理由**: 审稿人可能认为这是\"将现有方法 X 应用到显然需要它的领域 Y\"的 obvious extension，intellectual contribution 不足以达到顶会标准——特别是当每个组件都是现有方法的直接应用时。\n2. **E/N/U 分类的主观性反击**: 框架试图通过 E/N/U 分类实现\"有原则的\"multiverse 构建，但分类本身的可靠性和一致性未经验证。审稿人可能质疑：\"你用主观判断来消除主观性，这不是循环论证吗？\"——这需要 inter-annotator agreement 或 sensitivity analysis（对 E/N/U 分类本身的 multiverse）来回应，但 proposal 未提及。\n```\n\nSources:\n- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)\n- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)\n- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, CACM 2026)](https://arxiv.org/abs/2504.14571)\n- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Navigating the Conceptual Multiverse (Ye et al., 2026)](https://arxiv.org/abs/2604.17815)\n- [Carlson & Burbano (SMJ 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)\n- [Variance-Aware LLM Annotation (2026)](https://arxiv.org/pdf/2601.02370)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to conduct a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Baumann et al., \"Large Language Model Hacking\" (arXiv 2509.08825, Sep 2025)]: 核心前置工作。18个LLM × 37个标注任务 × 13M标签，发现约31%的假设在SOTA LLM下得出错误结论。提供了MIT开源复现数据。但仅评估了21种ad hoc缓解措施，未做formal multiverse分析。\n- [McLaren et al., \"Magic Words or Methodical Work?\" (arXiv 2603.26898, Mar 2026)]: 在政治科学标注任务上系统变化模型、prompt模板和学习方法，发现交互效应主导主效应。但设计是one-factor-at-a-time（非全因子设计），无specification curve或joint inference。\n- [Gligorić et al., \"Can Unconfident LLM Annotations Be Used for Confident Conclusions?\" (NAACL 2025)]: 提出Confidence-Driven Inference（CDI），结合LLM标注与置信度指标，战略性选择人工标注以产生无偏估计和有效置信区间。但假设固定的pipeline配置。\n- [Audinet de Pieuchon et al., \"Benchmarking Debiasing Methods for LLM-based Parameter Estimates\" (EMNLP 2025)]: 比较PPI与DSL去偏方法，但同样针对固定pipeline配置。\n- [Mehrotra et al., \"Multi-Perspective LLM Annotations\" (arXiv 2603.21404, Mar 2026)]: 提出Perspective-Driven Inference处理主观任务中的LLM标注，但每个perspective假设单一pipeline。\n- [Kosch & Feger, \"Prompt-Hacking: The New p-Hacking?\" (CACM, Mar 2026)]: 概念性类比prompt-hacking与p-hacking，但未提供任何formal方法。\n- [Ye et al., \"Navigating the Conceptual Multiverse\" (arXiv 2604.17815, Apr 2026)]: 将multiverse思想应用于LLM概念框架的HCI交互系统，不涉及标注pipeline或统计推断。\n- [Carlson & Burbano, \"The Use of LLMs to Annotate Data in Management Research\" (SMJ 2026)]: 提供LLM标注指南，建议做sensitivity analysis但无formal methodology。\n- [Auspurg, \"Robustness is better assessed with a few thoughtful models\" (PNAS 2025)] & [Ganslmeier & Vlandas Reply (PNAS 2025)]: 关于brute-force multiverse是否高估不确定性的活跃方法学辩论。\n- [Del Giudice & Gangestad, \"A Traveler's Guide to the Multiverse\" (AMPPS 2021)]: E/N/U分类框架（Equivalence/Nonequivalence/Uncertainty），proposal的核心方法论来源。已被引用但从未应用于LLM标注。\n- [Simonsohn et al., \"Specification Curve Analysis\" (Nature Human Behaviour 2020)]: 规范的specification curve joint inference方法，proposal直接适配此方法。\n\n调研总结: \"LLM标注中的researcher degrees of freedom\"是一个明确的、活跃的研究问题——多篇2025-2026论文从不同角度触及（问题刻画、ad hoc缓解、单pipeline去偏、概念类比），但确实没有任何工作将formal multiverse analysis（含principled configuration selection + joint statistical inference）应用于LLM标注pipeline。Proposal准确地识别并填充了这个gap。\n\n【Trivial Alternative 检验】:\n最直接的trivial alternative是\"informal sensitivity analysis\"——即研究者手动运行若干配置、报告结果范围，无需formal framework。这实际上已是部分领域的实践（Carlson & Burbano 2026建议做sensitivity analysis）。问题是：formal multiverse framework的增量价值相对于informal sensitivity analysis有多大？\n\nProposal的增量在于三点：(1) E/N/U分类提供principled配置筛选而非随意选取；(2) permutation-based joint inference给出\"robust/fragile/null\"的统计判定而非主观判断；(3) ANOVA variance decomposition定量归因哪些维度驱动不稳定性。这些增量是methodologically substantive的——不是trivial可替代的。但reviewer可能会质疑：在实践中，是否大多数研究者只需跑3-5个配置的informal check就够了，formal framework的边际收益是否值得其复杂性？\n\n结论：Trivial alternative威胁中等。增量价值存在且可辩护，但需要在论文中明确论证formal framework vs. informal sensitivity analysis的具体优势（例如通过案例展示informal approach会错过什么）。\n\n【前提假设检验】:\n核心逻辑链中存在以下未经充分验证的假设：\n\n1. **E/N/U分类的客观性假设**: Proposal假设可以对LLM标注pipeline的各维度做出principled的E/N/U分类（如\"temperature=0对确定性任务是Type N\"）。但E/N/U分类本身涉及主观判断——不同研究者可能对同一维度做出不同分类。如果E/N/U分类本身就是一个researcher degree of freedom，那这个框架会产生一个meta-level的multiverse问题（multiverse of multiverses）。Del Giudice & Gangestad (2021)原文也承认这一困难。\n\n2. **Auspurg反驳的完备性**: Proposal声称Auspurg对brute-force multiverse的批评不适用于LLM标注，因为(a)估计量恒定、(b)无配置是\"统计错误指定的\"、(c)无先验理论排序配置。但claim (b)可能过于乐观——不同temperature、不同prompt在某些任务上可能产生系统性bias（不只是随机variation），这在某种意义上类似于\"misspecification\"。\n\n3. **Specification curve方法的适用性假设**: Specification curve analysis假设各specification在某种意义上是\"exchangeable\"的。但LLM pipeline配置之间可能有strong hierarchical structure（如某些模型在特定任务类型上系统性优于其他模型），这可能违反specification curve的隐含假设。\n\n4. **从10个任务到通用性的跳跃**: 从Baumann et al.的37个任务中选10个进行验证，然后声称framework的通用性，这个推广需要谨慎论证。\n\n【3 维度打分】:\n1. Novelty: 【中】— \n   核心贡献是cross-domain adaptation：将psychology/economics中成熟的multiverse analysis方法（Simonsohn et al. 2020; Del Giudice & Gangestad 2021）应用于LLM标注pipeline这一新领域。经调研确认，确实没有现有工作做过这个specific adaptation，gap是genuine的。但novelty的nature是\"将已有方法A应用于新领域B\"，而非提出全新的方法或发现反直觉的现象。E/N/U框架的adaptation和Boba DSL的task-conditional constraints增加了一些方法创新，但核心技术组件（specification curve、permutation test、ANOVA）均为off-the-shelf。与Gligorić et al. (NAACL 2025)和Audinet de Pieuchon et al. (EMNLP 2025)的区别清晰（它们处理固定pipeline的label noise，本工作处理pipeline配置空间的inferential robustness），但这也说明领域已有adjacent work在做类似方向的贡献。\n\n2. Significance: 【中偏强】— \n   问题本身的重要性毋庸置疑：Baumann et al.的31%错误率、McLaren et al.的交互效应主导发现、Kosch & Feger的CACM评论文章，都说明这是一个urgent问题。CSS社区明确呼吁\"LLMs for measurement and downstream statistical inference\"方向的工作。实用工具包(llm-multiverse)和SMART pre-registration模板增加了practical impact。然而，核心发现如果是positive（即\"某些假设robust、某些fragile、某些null\"），reviewer不太可能说\"surprising\"——这基本是Baumann et al.结果的formal重新确认。Significance更多来自\"提供正确工具\"而非\"揭示意外现象\"。\n\n3. Related Work: 【强】— \n   Proposal展现了对该领域exceptionally thorough的了解。所有引用的论文经调研确认均真实存在、描述准确。对每篇相关工作的差异化定位精确（McLaren:complementary benchmarking但无joint inference；Gligorić:固定pipeline debiasing；Mehrotra:single pipeline per perspective；Audinet de Pieuchon:fixed pipeline debiasing methods comparison）。与Auspurg PNAS辩论的engagement增加了intellectual depth。唯一小缺陷：未提到[Rohrer 2026, \"What's a multiverse good for anyway?\"]这篇关于multiverse方法论的最新讨论（在搜索中出现），可能与框架的methodological justification高度相关。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \nNovelty是核心限制因素——这是一篇methodological adaptation论文（将已有统计方法cross-domain迁移到LLM标注），gap genuine但novelty类型属于\"应用创新\"而非\"方法创新\"或\"发现创新\"。Related Work覆盖极强，Significance问题重要且timely，但预期核心发现不会让审稿人说\"surprising\"（更可能是\"confirms what we suspected, now with proper methodology\"）。这类\"把正确的方法论带到需要它的领域\"的工作有真实价值，但在顶会review中往往被认为novelty不够——尤其当核心技术组件（specification curve、permutation test、ANOVA）全部是off-the-shelf时。Significance将上界推到35%，但Novelty的adaptation-level nature和findings的expected（非surprising）nature限制了上界无法突破35%。\n\n【主要风险】: \n1. **\"Methodological import\" novelty ceiling**: 审稿人可能认为\"将specification curve analysis应用于LLM标注\"是straightforward adaptation，核心技术贡献不足——尤其是所有统计方法组件均为off-the-shelf。\n2. **E/N/U分类的主观性悖论**: 框架旨在减少researcher degrees of freedom，但E/N/U分类本身引入了新的degrees of freedom。如果不同研究者对同一pipeline维度做出不同的E/N/U判断，框架的prescriptive价值会被削弱。审稿人可能会要求inter-rater agreement evidence来验证E/N/U分类的可靠性。\n```\n\nSources:\n- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)\n- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)\n- [Auspurg, PNAS 2025 – Robustness critique](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Ganslmeier & Vlandas Reply, PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Del Giudice & Gangestad, AMPPS 2021 – E/N/U Framework](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Kosch & Feger, CACM 2026 – Prompt-Hacking: The New p-Hacking?](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)\n- [Mehrotra et al., 2026 – Multi-Perspective LLM Annotations](https://arxiv.org/abs/2603.21404)\n- [Gligorić et al., NAACL 2025 – Confidence-Driven Inference](https://aclanthology.org/2025.naacl-long.179/)\n- [Audinet de Pieuchon et al., EMNLP 2025 – Benchmarking Debiasing Methods](https://aclanthology.org/2025.emnlp-main.1000/)\n- [Ye et al., 2026 – Navigating the Conceptual Multiverse](https://arxiv.org/abs/2604.17815)\n- [Carlson & Burbano, SMJ 2026](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)\n- [Rohrer 2026 – What's a multiverse good for anyway?](https://juliarohrer.com/wp-content/uploads/2026/02/multiverse_draft-preprint-version.pdf)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to make a well-grounded assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Large Language Model Hacking (Baumann et al., arXiv 2509.08825)](https://arxiv.org/abs/2509.08825) (2025): 核心前置工作。在37个社科标注任务上用18个LLM生成13M标签，复现2,361个假设，发现SOTA模型约31%得出错误结论，小模型高达50%。II型错误为主，效应量偏差40–77%。文章测试了21种缓解策略，但均为ad-hoc，无正式多宇宙推断框架。本proposal直接建立在该数据集之上。\n\n- [Magic Words or Methodical Work? (McLaren et al., arXiv 2603.26898)](https://arxiv.org/abs/2603.26898) (March 2026): 最直接的竞争/互补工作。在政治学标注任务上控制实验model、prompt template、learning approach的交互效应，核心发现为interaction effects dominate main effects。但关键局限：(1) one-factor-at-a-time设计，非全析因；(2) 无specification curve或joint inference；(3) 问的是\"哪个pipeline最好\"而非\"substantive finding是否robust\"。Proposal的差异化定位相对此文成立。\n\n- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, arXiv 2504.14571 → CACM 2026)](https://arxiv.org/abs/2504.14571): 概念层面的类比论文，提出PARKing（Prompt Adjustments to Reach Known Outcomes）类比p-hacking，但仅为概念呼吁，无正式方法学贡献。Proposal将其概念变为可操作框架。\n\n- [Specification Curve Analysis (Simonsohn, Simmons & Nelson, Nature Human Behaviour 2020)]: 方法学基石，canonical joint inference方法。本proposal将其从心理学/经济学的analytic choice迁移到LLM annotation pipeline choice。\n\n- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925): E/N/U分类框架的来源。Type E（等价选项构成多宇宙）、Type N（非等价应resolve到最优）、Type U（不确定性）。Proposal将此框架适配到LLM annotation维度（prompt wording → E, temperature=0 for classification → N, model family → U）。\n\n- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122): 批评暴力穷举式多宇宙分析，认为应只包含equally plausible specifications。Proposal的核心论证之一是LLM annotation恰恰是Auspurg批评不适用的场景——estimand不变、无specification misspecified、无先验理论排序pipeline选择。\n\n- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122): 反驳Auspurg，认为\"justified model space\"本身是contested的。为proposal的立场提供支持。\n\n- [Multi-Perspective LLM Annotations (Mehrotra et al., arXiv 2603.21404)](https://arxiv.org/abs/2603.21404) (March 2026): 提出Perspective-Driven Inference处理主观任务中人群差异，但假设single pipeline per perspective，未处理pipeline configuration space的robustness问题。\n\n- [Navigating the Conceptual Multiverse (Ye et al., arXiv 2604.17815)](https://arxiv.org/abs/2604.17815) (April 2026): 将multiverse思想应用于LLM概念框架的HCI交互系统，不涉及annotation pipeline或统计推断。\n\n- [Variance-Aware LLM Annotation (arXiv 2601.02370, 2026)](https://arxiv.org/pdf/2601.02370): 识别5类方差来源，给出protocol guidance，但无统计推断方法。\n\n- 调研总结: 这个领域正处于\"问题已被充分文档化，但方法学解决方案空缺\"的阶段。Baumann/McLaren/Kosch等已清楚证明LLM annotation中的researcher degrees of freedom问题严重且交互效应主导，但截至目前（2026年5月），确实没有工作将formal multiverse analysis + joint inference应用于LLM annotation pipeline。Proposal恰好填补了这个从\"问题诊断\"到\"方法学处方\"的空白。\n\n【Trivial Alternative 检验】:\n最明显的trivial alternative是\"简单敏感性分析\"：用3-5个LLM分别标注，报告结论是否一致（Carlson & Burbano 2026 的推荐做法）。这不需要E/N/U框架、不需要specification curve、不需要joint inference。\n\nProposal的增量价值需要在以下几点上成立：\n1. **系统性 vs. ad-hoc**：简单敏感性分析无法告诉你\"在所有defensible configurations空间中，发现是否robust\"，只能告诉你\"在我碰巧选的3个配置上是否一致\"。Proposal的joint inference提供了正式的统计检验，而非eyeballing。\n2. **E/N/U减少false uncertainty**：不加筛选的Cartesian product（810配置）会夸大不确定性（Auspurg的批评），而只选3个配置又low-power。E/N/U提供了中间地带——原则化的90-270配置。\n3. **Variance decomposition的attribution能力**：简单敏感性分析告诉你\"结论不稳定\"，但不告诉你\"不稳定主要来自model choice还是prompt wording还是它们的交互\"。\n\n增量价值存在但有限度——核心问题是：对于大多数实际研究者，\"用3个模型检查结论一致性\"可能已经足够，完整的multiverse框架是否过度工程化？这是一个审稿人可能提出的合理质疑。\n\n【前提假设检验】:\n1. **E/N/U分类的可操作性假设**：Proposal假设研究者可以可靠地将pipeline维度分类为E/N/U。但在实践中，这个分类本身就是一个研究者自由度——谁来决定temperature=0对于classification是Type N（objectively superior）？如果两个研究者对同一任务做出不同的E/N/U分类，产生的multiverse就不同，结论就不同。框架是否只是把degrees of freedom从pipeline choice推到了E/N/U classification？这是逻辑链中最薄弱的环节，proposal未提供inter-rater reliability或validation protocol。\n\n2. **Auspurg批评不适用的论证**：Proposal声称LLM annotation中\"no configuration is statistically misspecified\"。但一个poorly-designed prompt（如缺少关键定义、歧义性指令）难道不是一种misspecification吗？这个论证需要更精确的界定。\n\n3. **Specification curve的迁移有效性**：原始specification curve用于regression model specification（estimand结构明确，analytic choices有统计学意义上的等价性）。LLM annotation pipeline的\"specifications\"是qualitatively不同的——prompt wording的variation和regression中是否include a control variable的variation在认识论上不同。迁移的有效性需要更多论证。\n\n4. **下游推断的结构假设**：Proposal假设pipeline configuration的variation可以通过ANOVA进行方差分解。但如果configuration space中存在strong non-linearity或discontinuity（如某些prompt+model组合产生catastrophic failure），standard factorial ANOVA可能不是最佳工具。\n\n【3 维度打分】:\n1. **Novelty: 中** — \n   调研确认，截至2026年5月确实没有工作将formal multiverse analysis + joint statistical inference应用于LLM annotation pipeline。Baumann (2025) 诊断问题但只测试ad-hoc mitigations；McLaren et al. (2026) 做controlled benchmarking但用one-at-a-time设计且问的是\"best pipeline\"而非\"robustness\"；Kosch & Feger (2026) 提出概念类比但无formal method。这个gap是真实的。\n   \n   但核心贡献的novelty性质是**跨领域方法迁移**（multiverse analysis从心理学 → LLM annotation），而非方法论创新。三个核心组件——E/N/U分类、specification curve、variance decomposition——均为成熟的existing methods。将它们组合并适配到新领域有价值，但一个有经验的审稿人可能会说\"this is a straightforward application of known techniques to a new domain\"。E/N/U到LLM pipeline的具体适配（如何分类temperature、prompt等维度）是最有原创性的部分，但adaptation的深度有待验证。\n\n2. **Significance: 中偏强** — \n   问题的重要性毋庸置疑：31%的错误率（Baumann 2025）、interaction effects dominate（McLaren 2026）、社科研究越来越依赖LLM annotation。一个formal robustness framework填补了明确的方法学空白。\n   \n   限制significance的因素：(a) 如果核心结果是\"某些发现robust，某些fragile\"，审稿人可能会说\"I would have guessed this\"——我们已经知道pipeline choices matter（Baumann已证明），知道interactions dominate（McLaren已证明），一个formal framework confirmation of this isn't surprising；(b) 真正的significance取决于variance decomposition是否揭示了unexpected patterns（如某个维度远比其他重要），但这是empirical result，不是idea层面可以预判的；(c) 受众面：这主要是给使用LLM做标注的社科研究者的工具，NLP核心社区可能认为这更像applied methodology。\n\n3. **Related Work: 强** — \n   Proposal的文献覆盖在我调研范围内是全面且准确的。Baumann et al.、McLaren et al.、Kosch & Feger、Del Giudice & Gangestad、Auspurg vs. Ganslmeier & Vlandas、Ye et al.、Mehrotra et al.均为真实存在的论文且描述准确（通过搜索验证）。差异化定位清晰：相对于Baumann是\"诊断→处方\"的升级，相对于McLaren是\"one-at-a-time→full factorial + joint inference\"的升级，相对于Kosch & Feger是\"概念→可操作框架\"的升级。对Auspurg debate的engagement是一个特别thoughtful的点。唯一的小缺陷：Carlson & Burbano (2026, SMJ) 和 Variance-Aware (2026) 未提供arXiv ID，无法完全验证。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \n三维度中，Related Work强但这主要保底不加分；Novelty为中，因为核心贡献是跨领域方法迁移而非创新——三个组件（E/N/U、specification curve、ANOVA）均为existing mature methods，审稿人可能判定adaptation深度不够；Significance中偏强，因为问题重要且gap真实，但核心结果的surprise值有限（\"some findings are robust, some are fragile\" is expected given Baumann's 31% error rate已知）。限制上界的主要因素是Novelty——如果审稿人认为这是\"straightforward application of known methods to a new domain\"，分数会受压。概率上界35%对应审稿人认可E/N/U adaptation和Auspurg argument的intellectual depth；下界25%对应审稿人认为trivial alternative（简单sensitivity analysis）已足够且methodological transfer不算sufficient novelty。\n\n【主要风险】:\n1. **\"方法迁移 ≠ 方法创新\"风险**：审稿人可能判定将existing multiverse methods（specification curve + E/N/U + ANOVA）组合应用到LLM annotation是execution contribution而非intellectual contribution，novelty不足以达到顶会门槛。核心创新delta主要在\"适配\"而非\"发明\"。\n2. **E/N/U分类的主观性风险**：框架的核心价值在于principled configuration selection，但E/N/U分类本身引入新的researcher degrees of freedom。如果两个研究者对同一任务的E/N/U分类不一致，框架的principled性就被削弱。Proposal未提出如何validation E/N/U classification的reliability，审稿人可能抓住这一点作为逻辑漏洞。\n```\n\nSources:\n- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)\n- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)\n- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, 2026)](https://arxiv.org/abs/2504.14571)\n- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)\n- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)\n- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)\n- [Multi-Perspective LLM Annotations (Mehrotra et al., 2026)](https://arxiv.org/abs/2603.21404)\n- [Navigating the Conceptual Multiverse (Ye et al., 2026)](https://arxiv.org/abs/2604.17815)\n- [Variance-Aware LLM Annotation (2026)](https://arxiv.org/pdf/2601.02370)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Multiverse Analysis Framework for LLM-Mediated Social Science Pipelines\n\n## Description\nWe propose the first formal multiverse analysis framework for LLM-mediated social science annotation pipelines, combining principled configuration selection with joint statistical inference. While recent work documents that LLM pipeline choices produce contradictory conclusions (Baumann et al., 2025: ~31% error rate) and that interaction effects between choices dominate main effects (McLaren et al., 2026), no existing framework applies formal multiverse methodology — and the methodological community is actively debating whether exhaustive enumeration overstates uncertainty (Auspurg, PNAS 2025). We address both gaps. First, we adapt Del Giudice & Gangestad's (2021) E/N/U (Equivalence/Nonequivalence/Uncertainty) classification framework to LLM annotation, providing a principled methodology for constructing task-conditional multiverses: dimensions where one configuration is objectively superior (e.g., temperature=0 for deterministic tasks) are resolved rather than enumerated, while genuinely equivalent alternatives (e.g., semantically equivalent prompt rephrasings) populate the multiverse. Task-conditional constraints expressed in a Boba-style DSL reduce the naïve 810-configuration Cartesian product to ~90–270 principled specifications per task. Second, we adapt specification curve analysis (Simonsohn et al., 2020) with permutation-based joint inference to classify substantive social-science hypotheses as robust, fragile, or sign-inconsistent across the annotation multiverse. Third, we perform formal variance decomposition (factorial ANOVA over specification space) to quantify which pipeline dimensions and interactions drive the most inferential instability — extending McLaren et al.'s descriptive benchmarking to statistical attribution. We validate on 10 tasks from Baumann et al.'s publicly available replication data (37 tasks, MIT license) spanning binary, multi-class, ordinal, and subjective annotation, with supplementary validation on the SALT-NLP CSS benchmark. All inference is run via API on 6 models spanning diverse architectures (Llama 4 Maverick, Qwen 3.5, DeepSeek V4 Flash, Gemma 4, Mistral Medium 3.5, plus one proprietary anchor). We engage directly with Auspurg's (PNAS 2025) critique of brute-force multiverse analysis, arguing that LLM annotation is precisely the setting where her concerns do not apply: the estimand remains constant across configurations, no configuration is statistically misspecified, and no established theory ranks pipeline choices a priori. We release an open-source Python toolkit (llm-multiverse) integrating E/N/U classification, constraint-based configuration enumeration, batched API annotation, specification curve visualization, and joint inference — with SMART-compatible pre-registration templates enabling researchers to document and justify their multiverse construction before running experiments.\n\n## Core Problem\nWhen researchers use LLMs to annotate text for social science, numerous pipeline choices (model, prompt, temperature, aggregation) constitute researcher degrees of freedom that can produce contradictory conclusions — yet no formal framework systematically quantifies how these choices jointly affect downstream statistical inference. This is not merely a benchmarking problem: existing work documents that choices matter and interact (Baumann et al., 2025; McLaren et al., 2026), but none applies formal joint inference methods to determine whether a substantive social-science finding is robust across the space of defensible pipeline configurations.\n\n## Opportunity\nThe 'LLM hacking' paper (Baumann et al., 2025) showed ~31% of hypotheses yield incorrect conclusions from arbitrary LLM configuration choices, and Carlson & Burbano (2026, SMJ) recommend sensitivity analysis but provide no formal methodology. McLaren et al. (2026) demonstrate that interaction effects between pipeline choices dominate main effects, yet use only one-at-a-time variation without joint inference. Meanwhile, multiverse analysis / specification curve methods are mature in psychology and economics but have never been adapted to the unique structure of LLM annotation pipelines, where the degrees of freedom (prompt wording, model family, temperature, role, output parsing) are qualitatively different from traditional analytic choices — and, crucially, where Auspurg's (PNAS 2025) critique of brute-force multiverse enumeration does not apply because (a) the estimand remains constant across pipeline configurations, (b) no configuration is 'statistically misspecified' in the way a regression omitting fixed effects is, and (c) no established theory ranks one prompt or model above another a priori. The NLP+CSS community explicitly calls for work on 'LLMs for measurement and downstream statistical inference.'\n\n## Landscape\nThe LLM hacking paper (Baumann et al., 2025) tested 18 LLMs × 2,361 hypotheses × 13M labels, documenting the problem's scale but only evaluating 21 ad-hoc mitigations — no formal multiverse inference. 'Magic Words or Methodical Work?' (McLaren et al., arXiv March 2026) systematically varied model, prompt template, and learning approach for LLM annotation in political science and found that interaction effects dominate main effects; however, their design is one-factor-at-a-time (not full factorial), produces no specification curve or joint inference test, and their question is 'which pipeline performs best?' rather than 'is a substantive finding robust across pipelines?' — making their work complementary benchmarking, not a multiverse analysis. The variance-aware annotation framework (2026) identifies 5 variance sources but offers protocol guidance, not statistical inference. The benchmarking debiasing paper (Audinet de Pieuchon et al., EMNLP 2025) compares DSL vs PPI but only for fixed pipeline configurations. Brittlebench (2026) measures prompt sensitivity but not downstream inferential consequences. 'Prompt-Hacking: The New p-Hacking?' (Kosch & Feger, CACM 2026) draws the conceptual analogy but offers no formal method. 'Navigating the Conceptual Multiverse' (Ye et al., arXiv April 2026) applies multiverse thinking to LLM conceptual framing as an interactive HCI system, but does not address annotation pipelines or statistical inference. 'Multi-Perspective LLM Annotations' (Mehrotra et al., arXiv March 2026) introduces Perspective-Driven Inference for subjective tasks but assumes a single pipeline per perspective. The PNAS debate between Auspurg (2025) and Ganslmeier & Vlandas (2025) on whether exhaustive multiverse enumeration overstates uncertainty provides the key methodological foil: we adopt Del Giudice & Gangestad's (2021) E/N/U classification framework to construct principled, task-conditional multiverses rather than naïve Cartesian products. No existing work provides a formal multiverse analysis with principled configuration selection and joint statistical inference for LLM annotation pipelines.\n\n## Approach\nWe propose a three-stage framework: (1) Principled Multiverse Construction using Del Giudice & Gangestad's (2021) E/N/U (Equivalence / Nonequivalence / Uncertainty) classification. For each annotation task, we classify every pipeline dimension: dimensions where alternatives are effectively equivalent (Type E: e.g., semantically equivalent prompt rephrasings) populate the multiverse; dimensions where one option is objectively superior (Type N: e.g., temperature=0 for deterministic classification tasks, label-based output over numerical scores) are resolved to the best option only; dimensions where defensibility is uncertain (Type U: e.g., model family, definition inclusion) generate separate stratified multiverses. Task-conditional constraints are expressed formally using a Boba-style DSL: e.g., IF task_type='classification' AND num_classes≤3 THEN temperature∈{0.0, 0.3} AND output_format∈{'label'}. This reduces the naïve Cartesian product (~810 configurations from 6 models × 5 prompts × 3 temperatures × 3 roles × 3 aggregation strategies) to a principled, task-specific multiverse of ~90–270 defensible configurations per task, with explicit justification for every inclusion/exclusion. (2) Full-factorial execution across the principled multiverse. The six models span diverse architectures: Llama 4 Maverick (400B MoE), Qwen 3.5 (397B MoE), DeepSeek V4 Flash (284B MoE), Gemma 4 (26B MoE), Mistral Medium 3.5 (128B dense), plus one proprietary anchor (GPT-4o or Claude). All models are accessed via API (DeepSeek API, Together AI, OpenRouter, Google AI) for cost-efficiency; batched annotation (25 items/prompt) minimizes token costs. For each configuration, generate labels for the full corpus, then compute the downstream statistical estimate (e.g., regression coefficient, group difference). (3) Specification curve analysis with joint inference (Simonsohn et al., 2020): rank all specifications by effect size, display the specification curve with indicator rows for each pipeline dimension, and apply a permutation-based joint inference test to classify hypotheses as robust (sign-consistent and jointly significant), fragile (sign-inconsistent or significance-dependent on configuration), or null (no configuration yields significance). Additionally, perform variance decomposition (ANOVA over the specification space) to quantify which pipeline dimensions and their interactions drive the most inferential instability — extending McLaren et al.'s descriptive interaction findings to formal statistical attribution. Validate on 10 annotation tasks drawn from Baumann et al.'s publicly available replication data (37 tasks, MIT license, github.com/joebaumann/llmhacking), selected to span binary classification, multi-class categorization, ordinal scaling, and subjective judgment. Supplementary validation uses Gilardi et al.'s (PNAS 2023) Harvard Dataverse data and the SALT-NLP CSS benchmark (Ziems et al., 2024). Release an open-source Python toolkit (llm-multiverse) that wraps the full pipeline: E/N/U classification interface → task-conditional constraint specification → configuration enumeration → batched API annotation → specification curve visualization → joint inference test. The toolkit integrates with the SMART pre-registration framework (2025) so researchers can document and justify their multiverse construction before running experiments.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '0 (all inference via API — no self-hosted GPU needed)', 'api_cost': '$1,200–$2,000 for open-weight models via API providers (DeepSeek V4 Flash: ~$100–200 via DeepSeek API; Llama 4 Maverick: ~$250–470 via Together AI; Qwen 3.5: ~$475–950 via OpenRouter; Gemma 4: ~$65–130 via Google; Mistral Medium 3.5: ~$300–650 via Mistral/OpenRouter; proprietary anchor: ~$200–400). Estimates assume batched annotation (25 items/prompt) across ~90–270 configs × 10 tasks × 1,000–3,000 samples. Total: ~500M–1.2B tokens across all models.', 'timeline': '5–6 months (1 month framework design + E/N/U methodology, 2 months implementation + experiments, 1 month analysis + variance decomposition, 1 month writing + revision)', 'estimated_total_cost': '$1,200–$2,000'}, 'human_in_loop': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same API inference, slightly optimized configuration space with Claude-assisted E/N/U classification)', 'timeline': '3.5–4.5 months (2 weeks framework design with Claude scaffolding, 6 weeks experiments, 3 weeks analysis, 3 weeks writing)', 'claude_api_cost': '$150–$250 (Sonnet for code generation, experiment orchestration, and paper drafting; ~50M input tokens with caching)', 'estimated_total_cost': '$1,150–$1,850'}, 'auto_research': {'gpu_hours': '0 (API-based)', 'api_cost': '$1,000–$1,600 (same inference costs)', 'timeline': '2–3 months (automated experiment sweeps, parallelized API calls, auto-generated specification curves)', 'claude_api_cost': '$400–$600 (Opus for research design + Sonnet for bulk code generation and analysis; ~100M tokens total)', 'estimated_total_cost': '$1,400–$2,200', 'speed_bottleneck': 'API rate limits on proprietary LLMs (GPT, Claude) for anchor comparisons; sequential dependency between label generation and downstream inference computation; OpenRouter rate limits for Qwen 3.5 and Mistral Medium 3.5'}}\n\n## Inspired By\nGap: LLM hacking paper shows the problem (31% error rate), McLaren et al. show interaction effects dominate, but no formal multiverse framework with joint inference exists. Pattern: Cross-domain transfer of specification curve analysis (psychology/economics) and the E/N/U defensibility framework (Del Giudice & Gangestad, 2021) to LLM annotation pipelines. Epistemological justification: Auspurg's (PNAS 2025) critique of brute-force multiverse analysis does not apply to LLM pipelines because the estimand is constant and no configuration is statistically misspecified — making this precisely the setting where multiverse analysis is epistemically justified. Field guide evidence: Carlson & Burbano (2026) guidelines call for sensitivity analysis; variance-aware annotation (2026) identifies 5 variance sources; the NLP+CSS workshop explicitly seeks work on 'LLMs for measurement and downstream statistical inference.'\n\n## Target Venues\n- AAAI 2027 (full paper deadline: ~July 28, 2026 — strong fit for methods + empirical validation paper; primary target)\n- TACL (rolling submission, any month — ideal for extended journal-length treatment with theoretical results on E/N/U framework + formal variance decomposition)\n- CSCW 2027 (rolling submission — fits the sociotechnical framing of researcher-tool interaction and pre-registration protocol)\n- EMNLP 2026 Industry Track (deadline: ~June 16, 2026 — if framed around practitioner toolkit; stretch target)\n- FAccT 2027 (fits the transparency/accountability angle of documenting researcher degrees of freedom in LLM-mediated research)\n\n## Key References\n- Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation (arXiv 2025, Baumann et al.) — documents the 31% error rate problem; replication data publicly available under MIT license at github.com/joebaumann/llmhacking\n- Magic Words or Methodical Work? Challenging Conventional Wisdom in LLM-Based Political Text Annotation (arXiv 2603.26898, McLaren et al., March 2026) — one-at-a-time benchmarking showing interaction effects dominate; releases CodeBook Lab tools; complementary but no joint inference\n- Specification Curve Analysis (Nature Human Behaviour 2020, Simonsohn, Simmons & Nelson) — canonical joint inference method we adapt\n- Increasing Transparency Through a Multiverse Analysis (Perspectives on Psychological Science 2016, Steegen, Tuerlinckx, Gelman & Vanpaemel) — original multiverse analysis framework\n- A Traveler's Guide to the Multiverse: Promises, Pitfalls, and a Framework for the Evaluation of Analytic Decisions (Advances in Methods and Practices in Psychological Science 2021, Del Giudice & Gangestad) — E/N/U classification framework for principled configuration selection\n- Robustness is better assessed with a few thoughtful models than with billions of regressions (PNAS 2025, Auspurg) — critique of exhaustive multiverse enumeration; we argue LLM annotation is precisely the case where her critique does not apply\n- Reply to Auspurg: On the limits of 'justified' model spaces (PNAS 2025, Ganslmeier & Vlandas) — defense of comprehensive multiverse analysis when theory cannot adjudicate\n- The Use of LLMs to Annotate Data in Management Research: Foundational Guidelines and Warnings (SMJ 2026, Carlson & Burbano)\n- Variance-Aware LLM Annotation for Strategy Research (arXiv 2026)\n- Benchmarking Debiasing Methods for LLM-based Parameter Estimates (EMNLP 2025, Audinet de Pieuchon et al.)\n- Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity (arXiv 2026)\n- Can Unconfident LLM Annotations Be Used for Confident Conclusions? (NAACL 2025, Gligorić et al.)\n- Prompt-Hacking: The New p-Hacking? (Communications of the ACM 2026, Kosch & Feger)\n- Navigating the Conceptual Multiverse (arXiv 2026, Ye et al.)\n- Multi-Perspective LLM Annotations for Valid Analyses in Subjective Tasks (arXiv 2026, Mehrotra et al.)\n- Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs (arXiv 2026, Cui & Alexander)\n- To Err Is Human; To Annotate, SILICON? Reducing Measurement Error in LLM Annotation (arXiv 2024)\n- SMART: Systematic Multiverse Analysis Registration Tool (Royal Society Open Science 2025) — pre-registration workflow for multiverse construction\n- Boba: Authoring and Visualizing Multiverse Analyses (Liu et al., 2021) — DSL with constraint specification for principled multiverse pruning\n- Prompt Design Matters for Computational Social Science Tasks but in Unpredictable Ways (arXiv 2024) — empirical evidence for task-conditional configuration defensibility\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:47:58.563Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:47:58.563Z",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:47:58.574Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to produce the triage assessment. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Large Language Model Hacking] (arXiv 2509.08825, Baumann et al., 2025): 核心问题论文。在 18 个 LLM × 37 个标注任务上发现 ~31% 假设得出错误结论，效应量偏差 40-77%。提供了公开复制数据（MIT 许可），但仅测试 21 个 ad-hoc 缓解策略，无正式 multiverse 推断。Proposal 拟用其数据作为验证基础——这一点成立。
- [Magic Words or Methodical Work?] (arXiv 2603.26898, McLaren et al., March 2026): 在政治科学标注中系统变换模型、提示模板、学习方法，发现交互效应主导主效应。但其设计为 one-factor-at-a-time（非全因子），不产出 specification curve 或联合推断——proposal 对其定位为"互补性基准测试"是准确的。
- [Prompt-Hacking: The New p-Hacking?] (CACM 2026, Kosch & Feger): 明确画出 prompt hacking ↔ p-hacking 概念类比，但仅为观点文章，不提供正式方法论。Proposal 的定位准确。
- [Robustness is better assessed with a few thoughtful models…] (PNAS 2025, Auspurg): 批评穷举式 multiverse 分析过度估计不确定性。[Reply to Auspurg] (PNAS 2025, Ganslmeier & Vlandas) 进行了回应。这一方法论辩论是真实的、高影响力的。Proposal 试图论证 LLM 标注是 Auspurg 批评不适用的精确场景——这是一个有深度的方法论贡献。
- [A Traveler's Guide to the Multiverse] (AMPPS 2021, Del Giudice & Gangestad): E/N/U 分类框架确实存在且被广泛引用。将其迁移到 LLM 标注管道是 proposal 的核心方法论创新之一。
- [Navigating the Conceptual Multiverse] (arXiv 2604.17815, Ye et al., April 2026): 将 multiverse 思维应用于 LLM 概念框架的 HCI 交互系统，不涉及标注管道或统计推断——确认与 proposal 不直接竞争。
- [Carlson & Burbano] (SMJ 2026): 推荐敏感性分析但不提供正式方法。[Variance-Aware LLM Annotation] (arXiv 2601.02370, 2026): 识别 5 个方差来源但仅提供协议指导，不含统计推断。
- 调研总结：LLM 标注管道中的"研究者自由度"问题已被多篇高影响力论文充分记录（Baumann、McLaren、Kosch & Feger），且社区明确呼吁正式方法论解决方案（Carlson & Burbano）。然而，截至 2026 年 5 月，**确实没有任何现有工作将正式的 multiverse 分析 + 联合推断应用于 LLM 标注管道**。Proposal 填补的 gap 是真实存在的。但 gap 的性质是"将心理学/经济学中成熟的方法迁移到新领域"，而非提出全新方法。

【Trivial Alternative 检验】:
存在一个显而易见的 trivial alternative：**简单地用 3-5 个不同配置运行标注，报告结论是否一致**（即 Carlson & Burbano 2026 推荐的非正式敏感性分析）。Proposal 对此有预期回应：(a) 非正式分析无法提供联合统计推断（hypothesis 是 robust 还是 fragile 的正式判定），(b) 不含方差分解（不知道 *哪些* 维度驱动不稳定性），(c) 无法区分 E/N/U 维度（可能将不等价的配置混入分析）。

增量价值评估：**真实但有限**。正式框架的主要增量在于 (1) variance decomposition 可产出 actionable 发现（如"模型选择解释 40% 的推断方差，而 prompt 措辞仅 8%"），(2) 联合推断测试提供了非主观的 robustness 判定标准。但如果实证结果显示"大多数维度的影响相似"或"大多数假设都是 fragile"，则增量价值会大幅缩水——因为这与简单敏感性分析的结论无实质区别。

【前提假设检验】:
核心逻辑链中有以下未经验证的假设：

1. **E/N/U 分类可在 LLM 标注场景中可靠执行**：Del Giudice & Gangestad 的 E/N/U 框架是为传统分析决策设计的（如变量操作化、离群值处理）。Proposal 假设这一分类可以自然迁移到 LLM 管道维度（如 prompt 措辞、温度、模型选择），但 LLM 管道维度的"等价性"判断标准是什么？谁来判定两个 prompt 是"语义等价"的（Type E）vs."不确定"的（Type U）？这个分类过程本身可能引入主观性——恰恰是框架试图消除的问题。这是一个潜在的循环论证风险。

2. **Auspurg 批评不适用于 LLM 标注的论证**：Proposal 提出三个理由（estimand 恒定、无统计误设、无先验理论排序），但第三点值得质疑——随着 LLM 标注实践成熟，社区 *正在* 形成关于最佳实践的共识（如 temperature=0 优于高 temperature 用于分类任务）。如果"无先验理论排序"的前提随着领域发展而削弱，框架的认识论基础也会动摇。

3. **下游统计推断对标注噪声的敏感性是线性/可分解的**：ANOVA 方差分解假设因子效应可加性分解，但 McLaren et al. 已经证明交互效应主导——高阶交互效应可能使简单的方差分解难以解读。

【3 维度打分】:
1. Novelty: 【中】— 核心贡献是将心理学/经济学中成熟的方法论（specification curve analysis + E/N/U 框架）迁移到 LLM 标注管道这一新领域。Gap 是真实的（截至调研，确实无人做过此迁移），E/N/U 的领域适配和 Auspurg 辩论的参与增加了方法论深度。但本质上是 cross-domain transfer，不是方法论创新。每个组件（multiverse analysis, specification curves, E/N/U, ANOVA variance decomposition）单独来看都是现有方法的应用。一旦 Kosch & Feger (2026) 画出了 prompt-hacking ≈ p-hacking 的类比，将 multiverse analysis 应用于 LLM 管道是一个相当 obvious 的下一步。审稿人可能的反应：**"competent application of existing methods to a natural new domain, but the intellectual leap is moderate."**

2. Significance: 【中偏强】— 问题本身的重要性毋庸置疑：LLM 标注在社会科学中的采用正在爆炸性增长，31% 的假设得出错误结论（Baumann et al.）是一个令人震惊的数字。一个正式的 robustness 评估框架对该社区有真实需求。Variance decomposition 的潜在发现（哪些管道维度驱动最多不稳定性）具有直接可操作性。开源工具包 + pre-registration 模板增强了实践影响力。但主要受众是使用 LLM 进行标注的社会科学家，这是一个 specific niche（虽然快速增长）。对核心 NLP/CL 社区的方法论贡献相对有限——更多是应用层面的贡献。

3. Related Work: 【强】— 这是 proposal 最突出的维度。对已有工作的覆盖非常全面，正确识别了从问题记录（Baumann, McLaren）到概念类比（Kosch & Feger）到方法论辩论（Auspurg vs. Ganslmeier/Vlandas）的完整谱系。每篇工作的差异化定位清晰且准确（经调研验证）。特别值得肯定的是对 Ye et al.、Mehrotra et al. 等容易混淆的近期工作的精确区分。与 McLaren et al. 的定位（"互补性基准测试 vs. multiverse 推断"）是准确且有说服力的。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Significance 接近强——问题重要、社区有真实需求、潜在发现可操作。Related Work 强——coverage 全面、定位清晰。但 **Novelty 是限制上界的核心维度**：贡献的本质是 cross-domain method transfer（将成熟的心理学方法论搬到 LLM 标注），而非提出新方法或产出反直觉发现。一旦 Kosch & Feger (2026) 画出了类比，specification curve → LLM annotation 的迁移是相当 natural 的一步。最可能的审稿人反应是 "well-executed application paper"——尊重但不兴奋。如果 variance decomposition 产出了意外发现（如某个被忽视的维度驱动了大部分方差），可以推高概率到 ~33%；如果主要发现仅为 "pipeline choices matter and some hypotheses are fragile"（已被 Baumann et al. 定性证实），则下探至 ~22%。

【主要风险】:
1. **Novelty 不足的 reject 理由**: 审稿人可能认为这是"将现有方法 X 应用到显然需要它的领域 Y"的 obvious extension，intellectual contribution 不足以达到顶会标准——特别是当每个组件都是现有方法的直接应用时。
2. **E/N/U 分类的主观性反击**: 框架试图通过 E/N/U 分类实现"有原则的"multiverse 构建，但分类本身的可靠性和一致性未经验证。审稿人可能质疑："你用主观判断来消除主观性，这不是循环论证吗？"——这需要 inter-annotator agreement 或 sensitivity analysis（对 E/N/U 分类本身的 multiverse）来回应，但 proposal 未提及。
```

Sources:
- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)
- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)
- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, CACM 2026)](https://arxiv.org/abs/2504.14571)
- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Navigating the Conceptual Multiverse (Ye et al., 2026)](https://arxiv.org/abs/2604.17815)
- [Carlson & Burbano (SMJ 2026)](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)
- [Variance-Aware LLM Annotation (2026)](https://arxiv.org/pdf/2601.02370)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to conduct a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Baumann et al., "Large Language Model Hacking" (arXiv 2509.08825, Sep 2025)]: 核心前置工作。18个LLM × 37个标注任务 × 13M标签，发现约31%的假设在SOTA LLM下得出错误结论。提供了MIT开源复现数据。但仅评估了21种ad hoc缓解措施，未做formal multiverse分析。
- [McLaren et al., "Magic Words or Methodical Work?" (arXiv 2603.26898, Mar 2026)]: 在政治科学标注任务上系统变化模型、prompt模板和学习方法，发现交互效应主导主效应。但设计是one-factor-at-a-time（非全因子设计），无specification curve或joint inference。
- [Gligorić et al., "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" (NAACL 2025)]: 提出Confidence-Driven Inference（CDI），结合LLM标注与置信度指标，战略性选择人工标注以产生无偏估计和有效置信区间。但假设固定的pipeline配置。
- [Audinet de Pieuchon et al., "Benchmarking Debiasing Methods for LLM-based Parameter Estimates" (EMNLP 2025)]: 比较PPI与DSL去偏方法，但同样针对固定pipeline配置。
- [Mehrotra et al., "Multi-Perspective LLM Annotations" (arXiv 2603.21404, Mar 2026)]: 提出Perspective-Driven Inference处理主观任务中的LLM标注，但每个perspective假设单一pipeline。
- [Kosch & Feger, "Prompt-Hacking: The New p-Hacking?" (CACM, Mar 2026)]: 概念性类比prompt-hacking与p-hacking，但未提供任何formal方法。
- [Ye et al., "Navigating the Conceptual Multiverse" (arXiv 2604.17815, Apr 2026)]: 将multiverse思想应用于LLM概念框架的HCI交互系统，不涉及标注pipeline或统计推断。
- [Carlson & Burbano, "The Use of LLMs to Annotate Data in Management Research" (SMJ 2026)]: 提供LLM标注指南，建议做sensitivity analysis但无formal methodology。
- [Auspurg, "Robustness is better assessed with a few thoughtful models" (PNAS 2025)] & [Ganslmeier & Vlandas Reply (PNAS 2025)]: 关于brute-force multiverse是否高估不确定性的活跃方法学辩论。
- [Del Giudice & Gangestad, "A Traveler's Guide to the Multiverse" (AMPPS 2021)]: E/N/U分类框架（Equivalence/Nonequivalence/Uncertainty），proposal的核心方法论来源。已被引用但从未应用于LLM标注。
- [Simonsohn et al., "Specification Curve Analysis" (Nature Human Behaviour 2020)]: 规范的specification curve joint inference方法，proposal直接适配此方法。

调研总结: "LLM标注中的researcher degrees of freedom"是一个明确的、活跃的研究问题——多篇2025-2026论文从不同角度触及（问题刻画、ad hoc缓解、单pipeline去偏、概念类比），但确实没有任何工作将formal multiverse analysis（含principled configuration selection + joint statistical inference）应用于LLM标注pipeline。Proposal准确地识别并填充了这个gap。

【Trivial Alternative 检验】:
最直接的trivial alternative是"informal sensitivity analysis"——即研究者手动运行若干配置、报告结果范围，无需formal framework。这实际上已是部分领域的实践（Carlson & Burbano 2026建议做sensitivity analysis）。问题是：formal multiverse framework的增量价值相对于informal sensitivity analysis有多大？

Proposal的增量在于三点：(1) E/N/U分类提供principled配置筛选而非随意选取；(2) permutation-based joint inference给出"robust/fragile/null"的统计判定而非主观判断；(3) ANOVA variance decomposition定量归因哪些维度驱动不稳定性。这些增量是methodologically substantive的——不是trivial可替代的。但reviewer可能会质疑：在实践中，是否大多数研究者只需跑3-5个配置的informal check就够了，formal framework的边际收益是否值得其复杂性？

结论：Trivial alternative威胁中等。增量价值存在且可辩护，但需要在论文中明确论证formal framework vs. informal sensitivity analysis的具体优势（例如通过案例展示informal approach会错过什么）。

【前提假设检验】:
核心逻辑链中存在以下未经充分验证的假设：

1. **E/N/U分类的客观性假设**: Proposal假设可以对LLM标注pipeline的各维度做出principled的E/N/U分类（如"temperature=0对确定性任务是Type N"）。但E/N/U分类本身涉及主观判断——不同研究者可能对同一维度做出不同分类。如果E/N/U分类本身就是一个researcher degree of freedom，那这个框架会产生一个meta-level的multiverse问题（multiverse of multiverses）。Del Giudice & Gangestad (2021)原文也承认这一困难。

2. **Auspurg反驳的完备性**: Proposal声称Auspurg对brute-force multiverse的批评不适用于LLM标注，因为(a)估计量恒定、(b)无配置是"统计错误指定的"、(c)无先验理论排序配置。但claim (b)可能过于乐观——不同temperature、不同prompt在某些任务上可能产生系统性bias（不只是随机variation），这在某种意义上类似于"misspecification"。

3. **Specification curve方法的适用性假设**: Specification curve analysis假设各specification在某种意义上是"exchangeable"的。但LLM pipeline配置之间可能有strong hierarchical structure（如某些模型在特定任务类型上系统性优于其他模型），这可能违反specification curve的隐含假设。

4. **从10个任务到通用性的跳跃**: 从Baumann et al.的37个任务中选10个进行验证，然后声称framework的通用性，这个推广需要谨慎论证。

【3 维度打分】:
1. Novelty: 【中】— 
   核心贡献是cross-domain adaptation：将psychology/economics中成熟的multiverse analysis方法（Simonsohn et al. 2020; Del Giudice & Gangestad 2021）应用于LLM标注pipeline这一新领域。经调研确认，确实没有现有工作做过这个specific adaptation，gap是genuine的。但novelty的nature是"将已有方法A应用于新领域B"，而非提出全新的方法或发现反直觉的现象。E/N/U框架的adaptation和Boba DSL的task-conditional constraints增加了一些方法创新，但核心技术组件（specification curve、permutation test、ANOVA）均为off-the-shelf。与Gligorić et al. (NAACL 2025)和Audinet de Pieuchon et al. (EMNLP 2025)的区别清晰（它们处理固定pipeline的label noise，本工作处理pipeline配置空间的inferential robustness），但这也说明领域已有adjacent work在做类似方向的贡献。

2. Significance: 【中偏强】— 
   问题本身的重要性毋庸置疑：Baumann et al.的31%错误率、McLaren et al.的交互效应主导发现、Kosch & Feger的CACM评论文章，都说明这是一个urgent问题。CSS社区明确呼吁"LLMs for measurement and downstream statistical inference"方向的工作。实用工具包(llm-multiverse)和SMART pre-registration模板增加了practical impact。然而，核心发现如果是positive（即"某些假设robust、某些fragile、某些null"），reviewer不太可能说"surprising"——这基本是Baumann et al.结果的formal重新确认。Significance更多来自"提供正确工具"而非"揭示意外现象"。

3. Related Work: 【强】— 
   Proposal展现了对该领域exceptionally thorough的了解。所有引用的论文经调研确认均真实存在、描述准确。对每篇相关工作的差异化定位精确（McLaren:complementary benchmarking但无joint inference；Gligorić:固定pipeline debiasing；Mehrotra:single pipeline per perspective；Audinet de Pieuchon:fixed pipeline debiasing methods comparison）。与Auspurg PNAS辩论的engagement增加了intellectual depth。唯一小缺陷：未提到[Rohrer 2026, "What's a multiverse good for anyway?"]这篇关于multiverse方法论的最新讨论（在搜索中出现），可能与框架的methodological justification高度相关。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty是核心限制因素——这是一篇methodological adaptation论文（将已有统计方法cross-domain迁移到LLM标注），gap genuine但novelty类型属于"应用创新"而非"方法创新"或"发现创新"。Related Work覆盖极强，Significance问题重要且timely，但预期核心发现不会让审稿人说"surprising"（更可能是"confirms what we suspected, now with proper methodology"）。这类"把正确的方法论带到需要它的领域"的工作有真实价值，但在顶会review中往往被认为novelty不够——尤其当核心技术组件（specification curve、permutation test、ANOVA）全部是off-the-shelf时。Significance将上界推到35%，但Novelty的adaptation-level nature和findings的expected（非surprising）nature限制了上界无法突破35%。

【主要风险】: 
1. **"Methodological import" novelty ceiling**: 审稿人可能认为"将specification curve analysis应用于LLM标注"是straightforward adaptation，核心技术贡献不足——尤其是所有统计方法组件均为off-the-shelf。
2. **E/N/U分类的主观性悖论**: 框架旨在减少researcher degrees of freedom，但E/N/U分类本身引入了新的degrees of freedom。如果不同研究者对同一pipeline维度做出不同的E/N/U判断，框架的prescriptive价值会被削弱。审稿人可能会要求inter-rater agreement evidence来验证E/N/U分类的可靠性。
```

Sources:
- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)
- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)
- [Auspurg, PNAS 2025 – Robustness critique](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Ganslmeier & Vlandas Reply, PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Del Giudice & Gangestad, AMPPS 2021 – E/N/U Framework](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Kosch & Feger, CACM 2026 – Prompt-Hacking: The New p-Hacking?](https://cacm.acm.org/opinion/prompt-hacking-the-new-p-hacking/)
- [Mehrotra et al., 2026 – Multi-Perspective LLM Annotations](https://arxiv.org/abs/2603.21404)
- [Gligorić et al., NAACL 2025 – Confidence-Driven Inference](https://aclanthology.org/2025.naacl-long.179/)
- [Audinet de Pieuchon et al., EMNLP 2025 – Benchmarking Debiasing Methods](https://aclanthology.org/2025.emnlp-main.1000/)
- [Ye et al., 2026 – Navigating the Conceptual Multiverse](https://arxiv.org/abs/2604.17815)
- [Carlson & Burbano, SMJ 2026](https://sms.onlinelibrary.wiley.com/doi/10.1002/smj.70023)
- [Rohrer 2026 – What's a multiverse good for anyway?](https://juliarohrer.com/wp-content/uploads/2026/02/multiverse_draft-preprint-version.pdf)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to make a well-grounded assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Large Language Model Hacking (Baumann et al., arXiv 2509.08825)](https://arxiv.org/abs/2509.08825) (2025): 核心前置工作。在37个社科标注任务上用18个LLM生成13M标签，复现2,361个假设，发现SOTA模型约31%得出错误结论，小模型高达50%。II型错误为主，效应量偏差40–77%。文章测试了21种缓解策略，但均为ad-hoc，无正式多宇宙推断框架。本proposal直接建立在该数据集之上。

- [Magic Words or Methodical Work? (McLaren et al., arXiv 2603.26898)](https://arxiv.org/abs/2603.26898) (March 2026): 最直接的竞争/互补工作。在政治学标注任务上控制实验model、prompt template、learning approach的交互效应，核心发现为interaction effects dominate main effects。但关键局限：(1) one-factor-at-a-time设计，非全析因；(2) 无specification curve或joint inference；(3) 问的是"哪个pipeline最好"而非"substantive finding是否robust"。Proposal的差异化定位相对此文成立。

- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, arXiv 2504.14571 → CACM 2026)](https://arxiv.org/abs/2504.14571): 概念层面的类比论文，提出PARKing（Prompt Adjustments to Reach Known Outcomes）类比p-hacking，但仅为概念呼吁，无正式方法学贡献。Proposal将其概念变为可操作框架。

- [Specification Curve Analysis (Simonsohn, Simmons & Nelson, Nature Human Behaviour 2020)]: 方法学基石，canonical joint inference方法。本proposal将其从心理学/经济学的analytic choice迁移到LLM annotation pipeline choice。

- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, AMPPS 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925): E/N/U分类框架的来源。Type E（等价选项构成多宇宙）、Type N（非等价应resolve到最优）、Type U（不确定性）。Proposal将此框架适配到LLM annotation维度（prompt wording → E, temperature=0 for classification → N, model family → U）。

- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122): 批评暴力穷举式多宇宙分析，认为应只包含equally plausible specifications。Proposal的核心论证之一是LLM annotation恰恰是Auspurg批评不适用的场景——estimand不变、无specification misspecified、无先验理论排序pipeline选择。

- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122): 反驳Auspurg，认为"justified model space"本身是contested的。为proposal的立场提供支持。

- [Multi-Perspective LLM Annotations (Mehrotra et al., arXiv 2603.21404)](https://arxiv.org/abs/2603.21404) (March 2026): 提出Perspective-Driven Inference处理主观任务中人群差异，但假设single pipeline per perspective，未处理pipeline configuration space的robustness问题。

- [Navigating the Conceptual Multiverse (Ye et al., arXiv 2604.17815)](https://arxiv.org/abs/2604.17815) (April 2026): 将multiverse思想应用于LLM概念框架的HCI交互系统，不涉及annotation pipeline或统计推断。

- [Variance-Aware LLM Annotation (arXiv 2601.02370, 2026)](https://arxiv.org/pdf/2601.02370): 识别5类方差来源，给出protocol guidance，但无统计推断方法。

- 调研总结: 这个领域正处于"问题已被充分文档化，但方法学解决方案空缺"的阶段。Baumann/McLaren/Kosch等已清楚证明LLM annotation中的researcher degrees of freedom问题严重且交互效应主导，但截至目前（2026年5月），确实没有工作将formal multiverse analysis + joint inference应用于LLM annotation pipeline。Proposal恰好填补了这个从"问题诊断"到"方法学处方"的空白。

【Trivial Alternative 检验】:
最明显的trivial alternative是"简单敏感性分析"：用3-5个LLM分别标注，报告结论是否一致（Carlson & Burbano 2026 的推荐做法）。这不需要E/N/U框架、不需要specification curve、不需要joint inference。

Proposal的增量价值需要在以下几点上成立：
1. **系统性 vs. ad-hoc**：简单敏感性分析无法告诉你"在所有defensible configurations空间中，发现是否robust"，只能告诉你"在我碰巧选的3个配置上是否一致"。Proposal的joint inference提供了正式的统计检验，而非eyeballing。
2. **E/N/U减少false uncertainty**：不加筛选的Cartesian product（810配置）会夸大不确定性（Auspurg的批评），而只选3个配置又low-power。E/N/U提供了中间地带——原则化的90-270配置。
3. **Variance decomposition的attribution能力**：简单敏感性分析告诉你"结论不稳定"，但不告诉你"不稳定主要来自model choice还是prompt wording还是它们的交互"。

增量价值存在但有限度——核心问题是：对于大多数实际研究者，"用3个模型检查结论一致性"可能已经足够，完整的multiverse框架是否过度工程化？这是一个审稿人可能提出的合理质疑。

【前提假设检验】:
1. **E/N/U分类的可操作性假设**：Proposal假设研究者可以可靠地将pipeline维度分类为E/N/U。但在实践中，这个分类本身就是一个研究者自由度——谁来决定temperature=0对于classification是Type N（objectively superior）？如果两个研究者对同一任务做出不同的E/N/U分类，产生的multiverse就不同，结论就不同。框架是否只是把degrees of freedom从pipeline choice推到了E/N/U classification？这是逻辑链中最薄弱的环节，proposal未提供inter-rater reliability或validation protocol。

2. **Auspurg批评不适用的论证**：Proposal声称LLM annotation中"no configuration is statistically misspecified"。但一个poorly-designed prompt（如缺少关键定义、歧义性指令）难道不是一种misspecification吗？这个论证需要更精确的界定。

3. **Specification curve的迁移有效性**：原始specification curve用于regression model specification（estimand结构明确，analytic choices有统计学意义上的等价性）。LLM annotation pipeline的"specifications"是qualitatively不同的——prompt wording的variation和regression中是否include a control variable的variation在认识论上不同。迁移的有效性需要更多论证。

4. **下游推断的结构假设**：Proposal假设pipeline configuration的variation可以通过ANOVA进行方差分解。但如果configuration space中存在strong non-linearity或discontinuity（如某些prompt+model组合产生catastrophic failure），standard factorial ANOVA可能不是最佳工具。

【3 维度打分】:
1. **Novelty: 中** — 
   调研确认，截至2026年5月确实没有工作将formal multiverse analysis + joint statistical inference应用于LLM annotation pipeline。Baumann (2025) 诊断问题但只测试ad-hoc mitigations；McLaren et al. (2026) 做controlled benchmarking但用one-at-a-time设计且问的是"best pipeline"而非"robustness"；Kosch & Feger (2026) 提出概念类比但无formal method。这个gap是真实的。
   
   但核心贡献的novelty性质是**跨领域方法迁移**（multiverse analysis从心理学 → LLM annotation），而非方法论创新。三个核心组件——E/N/U分类、specification curve、variance decomposition——均为成熟的existing methods。将它们组合并适配到新领域有价值，但一个有经验的审稿人可能会说"this is a straightforward application of known techniques to a new domain"。E/N/U到LLM pipeline的具体适配（如何分类temperature、prompt等维度）是最有原创性的部分，但adaptation的深度有待验证。

2. **Significance: 中偏强** — 
   问题的重要性毋庸置疑：31%的错误率（Baumann 2025）、interaction effects dominate（McLaren 2026）、社科研究越来越依赖LLM annotation。一个formal robustness framework填补了明确的方法学空白。
   
   限制significance的因素：(a) 如果核心结果是"某些发现robust，某些fragile"，审稿人可能会说"I would have guessed this"——我们已经知道pipeline choices matter（Baumann已证明），知道interactions dominate（McLaren已证明），一个formal framework confirmation of this isn't surprising；(b) 真正的significance取决于variance decomposition是否揭示了unexpected patterns（如某个维度远比其他重要），但这是empirical result，不是idea层面可以预判的；(c) 受众面：这主要是给使用LLM做标注的社科研究者的工具，NLP核心社区可能认为这更像applied methodology。

3. **Related Work: 强** — 
   Proposal的文献覆盖在我调研范围内是全面且准确的。Baumann et al.、McLaren et al.、Kosch & Feger、Del Giudice & Gangestad、Auspurg vs. Ganslmeier & Vlandas、Ye et al.、Mehrotra et al.均为真实存在的论文且描述准确（通过搜索验证）。差异化定位清晰：相对于Baumann是"诊断→处方"的升级，相对于McLaren是"one-at-a-time→full factorial + joint inference"的升级，相对于Kosch & Feger是"概念→可操作框架"的升级。对Auspurg debate的engagement是一个特别thoughtful的点。唯一的小缺陷：Carlson & Burbano (2026, SMJ) 和 Variance-Aware (2026) 未提供arXiv ID，无法完全验证。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
三维度中，Related Work强但这主要保底不加分；Novelty为中，因为核心贡献是跨领域方法迁移而非创新——三个组件（E/N/U、specification curve、ANOVA）均为existing mature methods，审稿人可能判定adaptation深度不够；Significance中偏强，因为问题重要且gap真实，但核心结果的surprise值有限（"some findings are robust, some are fragile" is expected given Baumann's 31% error rate已知）。限制上界的主要因素是Novelty——如果审稿人认为这是"straightforward application of known methods to a new domain"，分数会受压。概率上界35%对应审稿人认可E/N/U adaptation和Auspurg argument的intellectual depth；下界25%对应审稿人认为trivial alternative（简单sensitivity analysis）已足够且methodological transfer不算sufficient novelty。

【主要风险】:
1. **"方法迁移 ≠ 方法创新"风险**：审稿人可能判定将existing multiverse methods（specification curve + E/N/U + ANOVA）组合应用到LLM annotation是execution contribution而非intellectual contribution，novelty不足以达到顶会门槛。核心创新delta主要在"适配"而非"发明"。
2. **E/N/U分类的主观性风险**：框架的核心价值在于principled configuration selection，但E/N/U分类本身引入新的researcher degrees of freedom。如果两个研究者对同一任务的E/N/U分类不一致，框架的principled性就被削弱。Proposal未提出如何validation E/N/U classification的reliability，审稿人可能抓住这一点作为逻辑漏洞。
```

Sources:
- [Large Language Model Hacking (Baumann et al., 2025)](https://arxiv.org/abs/2509.08825)
- [Magic Words or Methodical Work? (McLaren et al., 2026)](https://arxiv.org/abs/2603.26898)
- [Prompt-Hacking: The New p-Hacking? (Kosch & Feger, 2026)](https://arxiv.org/abs/2504.14571)
- [A Traveler's Guide to the Multiverse (Del Giudice & Gangestad, 2021)](https://journals.sagepub.com/doi/10.1177/2515245920954925)
- [Robustness is better assessed with a few thoughtful models (Auspurg, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2521917122)
- [Reply to Auspurg (Ganslmeier & Vlandas, PNAS 2025)](https://www.pnas.org/doi/10.1073/pnas.2523374122)
- [Multi-Perspective LLM Annotations (Mehrotra et al., 2026)](https://arxiv.org/abs/2603.21404)
- [Navigating the Conceptual Multiverse (Ye et al., 2026)](https://arxiv.org/abs/2604.17815)
- [Variance-Aware LLM Annotation (2026)](https://arxiv.org/pdf/2601.02370)


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
  "promptId": "cb032f48-1b66-44c4-899b-5d60b6126c54",
  "type": "user",
  "uuid": "cfdfc95a-c36a-47a1-8c24-de8de89ca022",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:47:58.573Z_

```json
{
  "parentUuid": "cfdfc95a-c36a-47a1-8c24-de8de89ca022",
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
  "uuid": "7eb1a637-bb3c-4d0c-9f0f-378804b55f79",
  "timestamp": "2026-05-20T03:47:58.573Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:47:58.573Z_

```json
{
  "parentUuid": "7eb1a637-bb3c-4d0c-9f0f-378804b55f79",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aa398a06-adaf-4c68-bfc1-2195f92cb1f0",
  "timestamp": "2026-05-20T03:47:58.573Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to produce the triage assessmen…",
  "leafUuid": "aa398a06-adaf-4c68-bfc1-2195f92cb1f0",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Multiverse analysis framework for LLM annotation",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:48:21.282Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me first extract the key data points:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Main risks: Novelty ceiling (cross-domain transfer), E/N/U subjectivity paradox

**Reviewer 2:**
- Novelty: 中


- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 35%] 中位 30%
- Main risks: "Methodological import" novelty ceiling, E/N/U subjectivity paradox

**Reviewer 3:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [25% - 35%] 中位 30%
- Main risks: "方法迁移 ≠ 方法创新", E/N/U subjectivity

All three reviewers converge on similar assessments: moderate novelty with moderately strong significance, solid related work coverage, and acceptance probabilities clustering around 28-30%. The consistent concern across all reviews centers on whether methodological transfer truly constitutes innovation, plus the inherent subjectivity in evaluating empirical, novelty, and utility dimensions. The individual reviewer concerns—specification curve exchangeability, the missing Rohrer reference, and the ANOVA non-linearity issue—are isolated observations rather than systematic disagreements. Given this convergence, I'm confident taking the median of the three estimates (30%) and setting my final range conservatively between 23-25% on the lower end and 33-34% on the upper end, following the principle of being selective rather than permissive.

Now I'm checking the implementation feasibility against the proposal details—the API-based approach requires no GPU infrastructure, with estimated costs around $1,200-$2,000 and a 5-6 month timeline, which appears quite realistic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa398a06-adaf-4c68-bfc1-2195f92cb1f0",
  "isSidechain": false,
  "requestId": "req_011CbD8sjxeHXz7JG4RFLQRn",
  "type": "assistant",
  "uuid": "72111686-7b0a-4596-9cbf-94cabee971fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbu43LgnZq5s98wpuor28p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22827,
      "cache_read_input_tokens": 11374,
      "output_tokens": 2931,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2931,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 22827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22827
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

_source line 9 · 2026-05-20T03:49:08.774Z_

【阶段】: Meta Judge
【三次中位】: [27%, 30%, 30%]  std=1.7%
【共识维度】:
- **Novelty = 中**（3/3 一致）：核心贡献是跨领域方法迁移（心理学/经济学 multiverse analysis → LLM annotation pipeline），gap 真实但 intellectual leap 有限。三个组件（E/N/U、specification curve、ANOVA variance decomposition）均为 off-the-shelf 成熟方法。一旦 Kosch & Feger (2026) 画出 prompt-hacking ≈ p-hacking 类比，此迁移是 natural next step。
- **Significance = 中偏强**（3/3 一致）：问题重要性毋庸置疑（Baumann 31% 错误率），社区有真实需求，工具包+预注册模板增强实践影响力。但预期核心发现不会 surprising（"confirms what we suspected, now with proper methodology"），significance 更多来自"提供正确工具"而非"揭示意外现象"。
- **Related Work = 强**（3/3 一致）：文献覆盖全面且准确，差异化定位清晰，对 Auspurg debate 的 engagement 增加 intellectual depth。
- **E/N/U 分类主观性悖论**（3/3 均独立提出）：框架旨在减少 researcher degrees of freedom，但 E/N/U 分类本身引入新的 degrees of freedom，形成潜在循环论证。Proposal 未提供 inter-rater reliability 或 validation protocol——这是逻辑链中最薄弱环节。
- **Trivial alternative 威胁 = 中等**（3/3 均讨论）：简单敏感性分析（3-5 配置）可能对多数实际研究者已足够，formal framework 的边际收益 vs. 复杂性是审稿人可能的攻击点。增量价值存在但有限度。
- **Auspurg 论证有弱点**（3/3 均质疑）：claim "no configuration is statistically misspecified" 过于乐观，poorly-designed prompt 可构成某种 misspecification；"无先验理论排序"前提随领域成熟可能削弱。

【异常维度】:
- 审稿人 2 独立提到 Rohrer (2026) "What's a multiverse good for anyway?" 为 missing reference——其他两人未提及，属次要补充
- 审稿人 3 独立提到 ANOVA 对 strong non-linearity/discontinuity 的不适用性——其他两人提及交互效应但未明确上升到 ANOVA 方法适用性层面，属中等信号
- 审稿人 1 提出"如果实证结果显示大多数维度影响相似或大多数假设都是 fragile，增量价值会大幅缩水"——其他两人未如此尖锐表述，但逻辑一致（findings 的 surprise 值有限），属补充性表述而非真正异常

【最终概率】: [24% - 33%] 中位 29%
【一致性】: 高（std=1.7%，三份评审在所有 rubric 维度上判决完全一致，概率区间高度重叠）
【综合理由】:
三份评审展现出极高一致性——Novelty/Significance/Related Work 的定性判决完全相同，核心风险点（E/N/U 主观性悖论、方法迁移 novelty ceiling、trivial alternative 威胁）均被独立识别。在高一致性条件下，取中位附近并适度缩窄区间。三份中位为 27/30/30，综合中位取 29%（略偏保守，尊重审稿人 1 对 findings surprise 值的更尖锐质疑）。上界 33% 对应审稿人认可 E/N/U adaptation 深度 + variance decomposition 产出 unexpected findings 的最佳情况；下界 24% 对应审稿人判定 trivial alternative 已足够 + 方法迁移 novelty 不达标的最差情况。Related Work 的"强"评级提供了坚实的下限保护（不会因 coverage 被扣分），但无法弥补 Novelty 的结构性天花板。

核心限制因素是 **Novelty 的 adaptation-level nature**：当每个技术组件都是 existing method 的直接应用时，审稿人最可能的反应是 "competent application paper"——尊重但不兴奋。这将概率天花板锁定在 ~33-35% 区间，无论实验多完美都难以突破。

【建议】: 边缘（中位 29% 低于 36% 通过线，但 idea 质量和 gap 真实性支撑迭代优化空间；E/N/U 主观性悖论和 novelty ceiling 是需要重点突破的两个维度）

【实施评估】:
- **计算资源**: 零 GPU 需求，全部通过 API 推理（DeepSeek API、Together AI、OpenRouter、Google AI 等）。瓶颈为 API rate limits，尤其是 OpenRouter 上 Qwen 3.5 和 Mistral Medium 3.5。
- **数据需求**: 主要依赖 Baumann et al. 公开复现数据（37 tasks, MIT license, github.com/joebaumann/llmhacking），补充使用 SALT-NLP CSS benchmark 和 Gilardi et al. (PNAS 2023) Harvard Dataverse 数据。均为公开可得数据集，无数据获取障碍。
- **人工介入**: E/N/U 分类需要研究者对每个任务的每个 pipeline 维度做出判断——这是主要的人工介入点，也是 proposal 的逻辑薄弱环节（inter-rater agreement 未经验证）。如需做 inter-rater reliability 实验（三份评审均建议），需额外 2-3 名标注者参与 E/N/U 分类。
- **训练需求**: 无模型训练需求。6 个模型均通过 API 调用进行推理（Llama 4 Maverick 400B、Qwen 3.5 397B、DeepSeek V4 Flash 284B、Gemma 4 26B、Mistral Medium 3.5 128B + 1 个 proprietary anchor）。
- **新 Benchmark**: 不需要构建全新 benchmark。需要开发 llm-multiverse 开源工具包（E/N/U 分类接口 + 约束枚举 + 批量标注 + specification curve 可视化 + joint inference），以及 SMART-compatible 预注册模板。工程量中等。
- **预估周期**: 手动模式 5-6 个月（1 月框架设计 + 2 月实验 + 1 月分析 + 1 月写作）；人机协作 3.5-4.5 个月；全自动 2-3 个月。API 总成本 $1,200-$2,200。整体可行性高，无硬性资源瓶颈。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72111686-7b0a-4596-9cbf-94cabee971fb",
  "isSidechain": false,
  "requestId": "req_011CbD8sjxeHXz7JG4RFLQRn",
  "type": "assistant",
  "uuid": "bdfe2535-3362-4eea-ba27-96fb11cd2a8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rbu43LgnZq5s98wpuor28p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22827,
      "cache_read_input_tokens": 11374,
      "output_tokens": 2931,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2931,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 22827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22827
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to produce the triage assessmen…",
  "leafUuid": "bdfe2535-3362-4eea-ba27-96fb11cd2a8e",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Multiverse analysis framework for LLM annotation",
  "sessionId": "dc27aca2-ce2d-4aa3-b0fa-dbaf90f537a7"
}
```

---
