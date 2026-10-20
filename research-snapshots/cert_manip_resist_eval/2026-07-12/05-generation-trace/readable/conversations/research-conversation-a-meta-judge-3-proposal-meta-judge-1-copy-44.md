# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/3a1631e0-edd6-4014-a2f5-01e4f0e1f45d.jsonl`
- **Structured JSON:** [`2821894178512315eb86.json`](../../sessions/28/2821894178512315eb86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:31:53.488Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:31:53.488Z",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient context to produce my evaluation. Let me compile the full assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Comprehensive Survey of Contamination Detection Methods in LLMs, arXiv:2404.00699] (2024, updated 2025): 系统综述了 50+ 检测技术和 100+ 篇相关论文，将方法分为 open-data 和 closed-data 两大类。IRT-FIT 所在的\"仅凭二元响应模式\"区域是现有方法覆盖的空白地带。\n- [Min-K%++, ICLR 2025 Spotlight]: Token-level log-likelihood 方法，需要灰盒访问。已成为 pretraining data detection 的标准 baseline，验证了 IRT-FIT 声称的信息访问层级差异。\n- [CoDeC, arXiv:2510.27055, ICLR 2026]: 基于 in-context learning 的数据集级污染检测，需要 token-level 访问。与 IRT-FIT 处于不同信息访问层。\n- [Self-Critique, arXiv:2510.09259, ICLR 2026]: 首个系统研究 RL post-training 对污染检测信号影响的工作，AUC 提升约 30%。IRT-FIT 的 post-RL 实验直接呼应此工作。\n- [ConStat, NeurIPS 2024]: 最直接的竞争者——同样不需要模型内部访问，但需要重新施测（rephrased items + reference models）。IRT-FIT 的核心差异化点在于无需 re-testing。r²=0.94 的 ground-truth 相关性是很强的 baseline。\n- [Benchmark Inflation, arXiv:2410.09247]: 通过 retro-holdout 方法量化性能差距（TruthfulQA 上高达 16pp），但需要构建 benchmark-specific holdout 集并重新评估模型。IRT-FIT 的 retroactive 分析无需任何新数据。\n- [PSN-IRT, AAAI 2026 Oral, arXiv:2505.15055]: 为 41,871 items × 11 benchmarks 校准了 4PL IRT 参数。这是 IRT-FIT 的直接上游依赖，参数已公开可用，降低了实施风险。\n- [Tendeiro et al., 2023, Multivariate Behavioral Research]: 提出 iterative scale purification 改善 lz* 在包含 misfitting respondents 数据上的 Type-I error 控制。IRT-FIT 引用了此工作但未采用其方法——可能被审稿人追问。\n- [Han et al., EACL 2026 Findings]: 量化了 LLM 在心理量表上的 contamination，但未使用 person-fit statistics——最近的相关但未重叠的工作。\n\n- 调研总结: Benchmark contamination detection 是一个高度活跃且拥挤的领域（100+ 篇论文），但方法按信息访问需求明显分层。IRT-FIT 填补了一个真实的空白——\"仅凭二元响应模式\"的最小信息操作点。该领域目前没有任何工作将 IRT person-fit statistics 应用于 LLM 污染检测，跨领域转移的 novelty claim 成立。主要竞争来自 ConStat（同属黑盒但需 re-testing），以及 Benchmark Inflation（retroactive 但需构建 holdout）。\n\n【整体印象】:\n作为审稿人，我的第一反应是**倾向 weak accept**。这是一篇定位清晰、方法论基础扎实、实验设计异常周全的 proposal。\"minimal-information operating point\" 的框架提供了一个有价值的概念贡献——不是声称比灰盒方法更好，而是明确探索信息访问 vs. 检测能力的权衡前沿。retroactive contamination prevalence analysis 是真正独特且有实际价值的应用场景。最大的担忧是方法层面的 novelty——本质上是将心理测量学中成熟的 lz* 统计量跨领域应用到 LLM 评估，方法创新的深度有限。\n\n【核心贡献】:\n核心贡献有三层：\n1. **概念贡献**：建立了 contamination detection 的 information-access frontier 框架，明确了二元响应模式作为最小信息操作点的位置。这是一个组织性的概念洞察，帮助社区理解不同方法之间的权衡关系。\n2. **方法贡献**：将 IRT person-fit statistics (lz*) 跨领域转移到 LLM 评估，证明 \"contaminated LLM ≈ examinee with item preknowledge\" 这个类比是操作上可行的。\n3. **实证贡献**：首个大规模 retroactive contamination prevalence timeline，以及 inverted-U 检测能力曲线的系统刻画。\n\n对领域的价值：**中等偏高**。该方法不会取代灰盒方法或 ConStat，但它开辟了一个独特的使用场景（历史审计）和一个独特的理论视角（最小信息检测极限）。这不是 incremental work，但也不是 paradigm-shifting work。\n\n【方法合理性】:\n方法是合理的且有坚实的理论基础（psychometric person-fit literature 几十年的积累）。lz* 是 person-fit 领域最广泛使用和研究最深入的统计量，选择合理。\n\n**更简单替代方案的考量**：Proposal 在 Tier 0 baselines 中已经包含了最明显的简单替代方案（Accuracy-Z、Guttman Error Count、Difficulty-Residual Correlation），并将其作为消融实验的核心。这是一个非常聪明的实验设计选择——如果 lz* 未能显著超越这些简单统计量，论文的核心论点就会崩塌，而 proposal 坦诚地将此作为实验的首要验证目标。\n\n**潜在方法问题**：\n- PSN-IRT 参数校准于可能包含 contaminated models 的响应数据，存在循环偏差风险（Braeken & van Laar, 2025）。Proposal 承诺 empirical null adjustment，但这不一定能完全解决问题。\n- 多维度 benchmarks (如 MMLU 的 57 个学科) 上的 unidimensionality 假设违反可能导致 false positives。Per-domain 分析部分缓解但增加了多重检验负担。\n- SFT generalization effect 可能在真实场景中严重削弱检测能力——这是一个根本性的限制，proposal 坦诚承认但无法解决。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】 — Benchmark contamination 是 LLM 评估的核心问题，受到广泛关注（100+ 篇论文的活跃领域）。\"最小信息操作点下的检测能力上界\"是一个有意义的理论问题，而非 engineering increment。retroactive audit 的实际需求真实存在——许多早期模型已下线无法重新测试。问题本身具有足够的研究深度（inverted-U 的理论分析、检测极限的刻画）。\n\n2. 方法与创新: 【中】 — 跨领域转移（psychometrics → LLM evaluation）是本文的核心 novelty，且 claim 成立——确实没有先前工作将 person-fit statistics 应用于 LLM 污染检测（Han et al., EACL 2026 是最近的相关工作但未使用 person-fit）。然而，方法本身（lz* 统计量、4PL IRT 模型、MLE 能力估计）完全是现有工具的直接应用，没有方法论层面的创新。与 ConStat 相比（NeurIPS 2024，提出了污染的新定义和新的统计检验框架），IRT-FIT 的方法创新深度较浅。inverted-U 的 proof sketch 增加了一些理论深度，但作者自己也只称之为 \"informal\"。\n\n3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。126 conditions × 3 sampling strategies × 3 seeds 的控制实验规模在该领域中属于上乘。Access-level stratified baselines 设计极为精巧——Tier 0 直接检验 IRT machinery 的边际价值，Tier 1/2 定位 IRT-FIT 在信息-检测权衡中的位置。Post-RL robustness test 呼应 Self-Critique (ICLR 2026) 和 Wang et al. 的发现。消融研究全面覆盖了关键设计选择（IRT 模型复杂度、person-fit 统计量、能力估计方法、参数来源、unidimensionality）。Power analysis simulation (10,000 replications) 展现了统计严谨性。已知 clean 的负面控制 (OLMo) 和 convergent validation with ConStat 增加了说服力。\n\n4. 可行性: 【中】 — ~2,500 H100-hours 计算需求实质性但合理（一个配备小型 H100 集群的实验室可以在数周内完成）。所有基础模型公开可用，PSN-IRT 参数已发布。主要风险点：(a) Open LLM Leaderboard 上的 per-item response logs 可用性不确定——许多模型可能只有聚合分数而无 item-level 记录，prevalence analysis 的规模可能受限；(b) 126 + 9 = 135 个 fine-tuning 条件 × 3 seeds = 405 次训练运行，调试和质量控制的工程量不小；(c) ConStat 等 baseline 的忠实复现需要额外工程投入。\n\n5. 写作与呈现: 【强】 — Proposal 结构清晰、论证严密。问题动机从 information-access frontier 切入非常优雅。相关工作按信息访问层级组织（gray-box → re-testing → retroactive），既全面又有条理。对 limitations 的坦诚讨论（SFT generalization、pretraining exposure 不可检测、inverted-U 两端的 identifiability 问题）显示了作者的学术诚实。Expected outcomes 中 \"aggregate AUROC possibly below gray-box methods\" 的坦率预期是加分项——不过度 claim。\n\n【概率估计】: [30% - 48%] 中位 38%\n\n【估计理由】:\n**上推因素**: (1) 填补了一个真实的方法论空白（minimal-information operating point），novelty claim 经调研验证成立；(2) 实验设计在该领域同类工作中属于顶级水平，Tier 0 baselines 的设计特别精巧；(3) retroactive audit 是一个杀手级应用场景，其他方法无法实现；(4) 写作质量高，定位清晰，不过度 claim；(5) IRT for LLM evaluation 正处于上升期（PSN-IRT AAAI 2026 Oral, ATLAS AAAI 2027, MedIRT ICLR 2027），时机好。\n\n**下拉因素**: (1) 方法创新深度有限——本质是跨领域 apply 已有统计工具，部分审稿人可能认为 novelty 不足以支撑主会；(2) inverted-U 的根本性限制意味着该方法在极端污染比例（接近 0% 或 100%）下失效，而真实场景中这两种情况都很常见；(3) SFT generalization effect 可能严重削弱真实场景下的检测能力，proposal 虽然设计了相关实验但无法解决这个根本问题；(4) 对 PSN-IRT 参数的依赖引入了上游偏差风险；(5) 如果 Tier 0 baselines（特别是 Accuracy-Z 或 Difficulty-Residual）表现接近 lz*，核心论点会大幅削弱。\n\n**综合判断**: 这是一篇 solid 的投稿，处于 borderline accept 区域。研究问题有价值、实验设计优秀、写作清晰，但方法创新深度有限是主要短板。最终概率高度依赖于实验结果：如果 lz* 显著超越 Tier 0 baselines 且 prevalence analysis 揭示有趣的 contamination trends，probability 向上界靠拢；如果 Tier 0 baselines 表现接近或 inverted-U 的可用检测窗口太窄，probability 向下界靠拢。\n\n【主要风险】:\n1. **方法 novelty 被质疑**: 审稿人可能认为\"将 psychometrics 的 lz* 直接用于 LLM evaluation\"是 application-level contribution 而非 methodological innovation，不足以支撑主会论文。这是最大的拒稿风险。\n2. **Tier 0 baselines 表现相近**: 如果简单的 Accuracy-Z 或 Guttman Error Count 达到了与 lz* 相当的检测能力，那么整个 IRT person-fit 框架的额外复杂度就缺乏正当性——论文的核心论点将被釜底抽薪。\n\n【实施评估】:\n  - 计算资源: ~2,500 H100-hours（约 $5,000-7,500 @ spot pricing），需要至少 2-4 块 H100/A100 的并行能力，中等规模实验室可承受\n  - 数据需求: PSN-IRT 4PL 参数（已公开）；6 个 benchmark 数据集（全部公开）；Open LLM Leaderboard per-item response logs（可用性不确定，是主要数据风险）\n  - 人工介入: 中等——405 次 fine-tuning 运行的质量控制、ConStat 等 baseline 的复现、prevalence analysis 的数据收集和清洗\n  - 训练需求: 需要大量 QLoRA/SFT fine-tuning（405 次基础运行 + 后续 RL 运行），但每次运行规模较小（9B-27B 模型 QLoRA）\n  - 新 Benchmark: 不需要构建新 benchmark，使用 PSN-IRT 已校准的 6 个现有 benchmark\n  - 预估周期: 4-6 个月（含代码开发、实验运行、分析和论文撰写）\n```\n\nSources:\n- [Comprehensive Survey of Contamination Detection Methods in LLMs](https://arxiv.org/html/2404.00699v4)\n- [Min-K%++: Improved Baseline for Pre-Training Data Detection (ICLR 2025)](https://openreview.net/forum?id=ZGkfoufDaU)\n- [CoDeC: Detecting Data Contamination in LLMs via In-Context Learning](https://arxiv.org/pdf/2510.27055)\n- [Self-Critique: Detecting Data Contamination from RL Post-training](https://arxiv.org/abs/2510.09259)\n- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf)\n- [Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts](https://arxiv.org/abs/2410.09247)\n- [PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)\n- [Iterative Scale Purification Procedure on lz for Aberrant Response Detection (Tendeiro et al., 2023)](https://www.tandfonline.com/doi/full/10.1080/00273171.2023.2211564)\n- [What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide](https://llm-stats.com/blog/research/what-is-a-contaminated-llm)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough information to produce a thorough evaluation. Let me synthesize all findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- \"Benchmarking Large Language Models Under Data Contamination: A Survey\" (EMNLP 2025 Main): 综述涵盖50+检测技术，将方法分为静态/动态两大类。proposal的定位（minimal-information operating point）在该综述框架中属于未被系统探索的空白区域。\n- ConStat (NeurIPS 2024, arXiv:2405.16281): 最直接的对标方法——同样无需模型内部参数，但需要生成重述题目并重新测试（r²=0.94 with ground-truth）。IRT-FIT的关键差异化点（无需re-testing/re-administration）成立。\n- CoDeC (ICLR 2026, arXiv:2510.27055): 通过in-context learning比较seen/unseen数据的置信度差异，属于gray-box方法。与IRT-FIT不在同一access level，不构成直接竞争。\n- Self-Critique (ICLR 2026, arXiv:2510.09259): 通过entropy sequence检测post-RL contamination，~30% AUC提升。与IRT-FIT在post-RL场景的比较是proposal的重要实验。\n- PSN-IRT (AAAI 2026 Oral, arXiv:2505.15055): IRT-FIT的基础设施依赖——提供41,871 items的4PL参数。该工作已被顶会接收，基础扎实。\n- ATLAS (arXiv:2511.04689, AAAI 2027): IRT-based adaptive testing，减少90%测试items。同样利用IRT但方向不同（效率 vs. 污染检测），不构成竞争。\n- Wang et al. (arXiv:2510.02386): 揭示GRPO训练可隐藏MIA-based信号。proposal的post-RL实验直接对接该发现。\n- Silicon Bureaucracy (arXiv:2603.21636) & Cross-Context Verification (arXiv:2603.21454): 2026年3月最新方法，分别用扰动审计和session-isolated多样性分析。均需要re-administration，与IRT-FIT不在同一operating point。\n- 搜索\"person-fit LLM contamination\"未返回任何结果: 验证了proposal的核心novelty claim——目前无人将person-fit统计量应用于LLM污染检测。\n- Han et al. (EACL 2026 Findings): 量化了心理测量问卷中的污染，但未使用person-fit统计量。最近的相关工作但仍有明确差异。\n\n- 调研总结: LLM benchmark contamination detection是2024-2026年的活跃研究方向，已有方法覆盖gray-box（token-level access）和black-box（需re-testing）两个操作点，但\"仅用binary response pattern\"的minimal-information操作点确实是一个未被探索的空白。将psychometric person-fit statistics迁移到此问题目前无先例。\n\n【整体印象】: \n作为审稿人，我的第一反应是\"这是一个干净、有品位的research question，配上了异常扎实的实验设计\"。Proposal清晰地识别了contamination detection方法图谱中的一个真实空白（minimal-information operating point），提出了一个有理论基础的解决方案（psychometric person-fit transfer），并且诚实地讨论了方法的固有局限性。这种\"我知道这个方法不能打败gray-box方法，但我要系统地理解这个操作点上能做什么\"的定位非常学术——是characterization而非superiority claim。倾向于weak accept / borderline accept，但最终取决于实际实验结果是否能支撑inverted-U curve等核心claim。\n\n【核心贡献】: \n核心贡献有三层：(1) 建立了contamination detection的minimal-information operating point，首次仅用binary response patterns检测污染；(2) 实现retroactive contamination audit——这是一个genuinely unique的能力，其他所有方法都需要live model access或re-testing；(3) 理论层面characterize了binary-response-pattern方法的detection power envelope（inverted-U curve）。对领域的价值在于：即使lz*的绝对检测力不如gray-box方法，系统地理解\"不同信息量级下能做什么\"本身对contamination detection领域有结构性贡献。Retroactive audit能力有直接的实践价值。\n\n【方法合理性】: \n方法本身是合理的——lz*在教育测试中有数十年的理论和实证基础（Karabatsos 2003; Sinharay 2017; Gorney et al. 2023），\"contaminated LLM ≈ examinee with item preknowledge\"的类比是站得住的。更简单的替代方案（accuracy z-score、Guttman error count、difficulty-residual correlation）已被设计为Tier 0 baselines，proposal明确要验证lz*是否提供marginal value over these simpler statistics，这一点很好。主要的方法论风险在于：(a) SFT generalization effect可能显著削弱aberrance signal；(b) PSN-IRT calibration本身可能包含contaminated models导致lz*的calibration bias（Braeken & van Laar 2025），虽然proposal提到了empirical null adjustment但这是一个需要实验验证的关键假设。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — \"What is the detection power envelope at the minimal-information level?\"是一个干净、有价值的研究问题。它不是\"我做了一个更好的方法\"，而是\"我要系统地理解一个新的operating point\"——这种framing既诚实又有深度。Retroactive audit的unique capability进一步提升了问题的实践价值。在EMNLP 2025的contamination survey（50+方法）中，这个operating point确实是空白。\n  \n  2. 方法与创新: 【中】 — 核心方法lz*不是新发明，而是从教育心理学的迁移应用。创新性在于：(a) 识别了cross-domain analogy的操作性价值；(b) 对detection limits的理论characterization。但相比ConStat（NeurIPS 2024，提出了contamination的新定义）或CoDeC（ICLR 2026，提出新的ICL-based detection paradigm），methodological novelty相对有限。Inverted-U curve的\"informal proof sketch\"如果不能formalize，可能被审稿人认为under-delivers。\n  \n  3. 实验设计: 【强】 — 这是proposal最大的亮点之一。126 conditions × 3 seeds的controlled contamination、access-level stratified baselines（Tier 0/1/2）的设计非常有结构感。特别值得肯定的是：(a) Tier 0 baselines直接检验IRT machinery的marginal value，这是很多paper会回避的对比；(b) post-RL robustness test直接对接Wang et al. (arXiv:2510.02386)的发现；(c) 5个维度的ablation study（IRT model complexity, person-fit statistics, ability estimation, parameter source, unidimensionality）覆盖了所有可能的methodological choice；(d) Open LLM Leaderboard prevalence analysis + OLMo negative controls。这个实验方案如果执行到位，本身就是一个重要贡献。参考ConStat和Min-K%++的实验设计，本proposal的baseline覆盖度和ablation深度均达到甚至超过了同类工作的标准。\n  \n  4. 可行性: 【中】 — 2,500 H100-hours是可控的计算成本。技术依赖链清晰（PSN-IRT参数 → lz*计算 → 统计检验）。主要风险：(a) 126个QLoRA fine-tuning runs的工程量不小，需要稳定的训练pipeline；(b) Open LLM Leaderboard的per-item response logs的可获取性可能存在gaps；(c) Post-RL实验（GRPO）需要follow Wang et al.的configuration，可能有复现难度。总体可行但需要扎实的工程基础设施和对leaderboard数据的access。\n  \n  5. 写作与呈现: 【强】 — Proposal的逻辑结构非常清晰：Problem → Core Contributions → Scope & Assumptions → Method → Related Work → Experimental Design → Evaluation Metrics。特别值得肯定的是：(a) 诚实地讨论了SFT generalization effect的威胁（Section 3）；(b) 清晰地界定了detection scope（item-level memorization vs. distributional pretraining exposure）；(c) Access-level stratified的related work组织方式让读者一眼看清方法图谱；(d) Expected Outcomes中不回避\"aggregate AUROC possibly below gray-box methods\"的预期。这种intellectual honesty在proposal阶段就展现出来，是加分项。\n\n【概率估计】: [30% - 42%] 中位 36%\n\n【估计理由】: \n这个proposal处于\"solid submission\"区间。往上推的力量：(1) 研究问题干净且有真实gap；(2) 实验设计异常扎实，baseline覆盖度和ablation深度达到顶级标准；(3) retroactive audit是unique selling point；(4) 写作清晰诚实。往下拉的力量：(1) 核心方法是cross-domain transfer而非methodological invention，部分审稿人可能认为novelty不够；(2) 如果实验结果显示lz*在practical relevant的contamination levels（5-20%）上检测力很弱，\"characterizing the limits\"的framing可能不足以支撑acceptance——审稿人可能反问\"if the method barely works, why should we care about characterizing it?\"；(3) inverted-U的\"proof sketch\"如果无法formalize，理论贡献会被打折。中位36%反映了\"各方面合格到偏好，但缺乏一个decisive的亮点来push过acceptance threshold\"的判断。如果实验结果在10-30% contamination区间确实展现出有意义的检测力，且retroactive analysis发现有价值的trend，概率可以上移到40%+。\n\n【主要风险】: \n1. **Detection power可能过弱**: 在practical relevant的contamination fraction（5-20%）上，binary response patterns携带的信息可能不足以在统计上与genuine high ability区分，特别是在SFT generalization effect存在的情况下。如果core result是\"lz*在大多数条件下barely beats Tier 0 baselines\"，审稿人可能认为整个IRT框架的引入不justified。\n2. **\"Characterization\"论文的acceptance barrier更高**: Proposal的定位是characterize a detection frontier而非claim superiority。这种framing虽然诚实，但在competitive reviewing中可能处于劣势——审稿人可能期待一个方法在某个维度上是\"best in class\"，而非仅仅\"interesting characterization of limits\"。\n\n【实施评估】:\n  - 计算资源: ~2,500 H100-hours，属于中等规模，需要稳定的GPU集群access（约1-2周连续使用8×H100节点）\n  - 数据需求: PSN-IRT的4PL参数（已公开）；Open LLM Leaderboard per-item response logs（可获取性需要验证）；fine-tuning用的benchmark数据（公开）\n  - 人工介入: 中等。QLoRA/SFT pipeline搭建、GRPO训练configuration、leaderboard数据收集和清洗需要显著的工程工作\n  - 训练需求: 是。需要训练126+ fine-tuned models（QLoRA/SFT）+ post-RL models。这是实验的核心，不可避免\n  - 新 Benchmark: 否。使用现有benchmark（MMLU, ARC-C, HellaSwag, WinoGrande, TruthfulQA, HumanEval）+ 已有IRT参数\n  - 预估周期: 3-4个月（1个月搭建pipeline + 1.5个月跑实验 + 1个月分析和写作）\n```\n\nSources:\n- [Benchmarking LLMs Under Data Contamination Survey (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.511/)\n- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://arxiv.org/pdf/2405.16281)\n- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/html/2510.27055v1)\n- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/pdf/2505.15055)\n- [ATLAS: Adaptive Testing for LLM Evaluation](https://arxiv.org/abs/2511.04689)\n- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/pdf/2510.02386)\n- [Silicon Bureaucracy (arXiv 2603.21636)](https://arxiv.org/abs/2603.21636)\n- [Cross-Context Verification (arXiv 2603.21454)](https://arxiv.org/abs/2603.21454)\n- [PaCoST: Paired Confidence Significance Testing (EMNLP 2024 Findings)](https://arxiv.org/pdf/2406.18326)\n- [Comprehensive Survey of Contamination Detection Methods](https://arxiv.org/pdf/2404.00699)\n- [Person-Fit Assessment in IRT (Nature)](https://www.nature.com/research-intelligence/nri-topic-summaries/person-fit-assessment-in-item-response-theory-micro-129702)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me compile the evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [PSN-IRT / \"Lost in Benchmarks?\" (arXiv:2505.15055)] (AAAI 2026 Oral): 直接前置工作。为11个benchmark共41,871个item提供4PL IRT参数。IRT-FIT的整个方法建立在此基础之上，但PSN-IRT本身未做person-fit方向的污染检测。\n- [ConStat (arXiv:2405.16281)] (NeurIPS 2024): 最直接竞争者。同为黑盒方法，但需要生成rephrased items并重新测试模型，在Open LLM Leaderboard上发现Mistral/Llama/Yi等模型的高污染率(r²=0.94)。IRT-FIT的核心差异化在于不需要re-testing，可做retroactive audit。\n- [Min-K%++ (arXiv:2404.02936)] (ICLR 2025 Spotlight): Token-level log-likelihood方法，需要gray-box access。代表了更高信息访问层级的检测方法。\n- [CoDeC (arXiv:2510.27055)] (ICLR 2026): 基于ICL的污染检测，dataset-level方法。[Self-Critique (arXiv:2510.09259)] (ICLR 2026): 针对post-RL污染，通过entropy collapse检测，AUC提升30%。两者都需要模型内部信息。\n- [Wang et al. (arXiv:2510.02386)]: 证明即使短暂GRPO训练也能隐藏MIA-based信号，对所有基于记忆的检测方法构成挑战。IRT-FIT的post-RL robustness实验直接回应此工作。\n- [Benchmark Inflation (arXiv:2410.09247)]: 通过retro-holdout量化性能差距（TruthfulQA上达16pp）。需要构建新的holdout set并重新评估，不能完全retroactive。\n- [Han et al.] (EACL 2026 Findings): 量化心理测量问卷中的LLM数据污染（item memorization, evaluation memorization, target score matching），但未使用person-fit统计量。这是最接近IRT+污染方向的工作，但切入点完全不同。\n- [ATLAS (arXiv:2511.04689)] (AAAI 2027): IRT-based自适应测试，减少90%测试item。[MedIRT (arXiv:2509.24186)] (ICLR 2027): 医学benchmark上的2PL IRT。均为IRT在LLM评估中的应用，但与污染检测无关。\n- [Silicon Bureaucracy (arXiv:2603.21636)] & [Cross-Context Verification (arXiv:2603.21454)] (2026 arXiv): 最新的benchmark污染检测工作，前者用perturbation-based audit，后者用session-isolated diversity analysis达到perfect separation。两者都需要re-testing。\n- [Braeken & van Laar (2025, Educational and Psychological Measurement)]: 指出lz*在calibration sample包含misfit respondents时存在校准偏差。proposal已识别此风险并计划empirical null adjustment。\n- [Sinharay (2017, JEBS)]: person-fit检测power在10-30% preknowledge时达到峰值的inverted-U形状。IRT-FIT直接继承并拓展此发现。\n\n- **调研总结**: LLM benchmark污染检测是一个活跃且竞争激烈的领域，2024-2026年涌现了大量工作，覆盖了从gray-box（Min-K%++, CoDeC, Self-Critique）到black-box requiring re-testing（ConStat, Silicon Bureaucracy, CCV）的各个信息访问层级。然而，在\"仅使用二值response pattern\"这个最低信息层级上，确实没有任何现有工作。IRT-FIT占据了一个真实的空白位置——但这个位置的价值取决于其检测能力是否足够实用。\n\n【整体印象】:\n作为审稿人，我的第一反应是**倾向weak accept / borderline accept**。这是一篇定位非常清晰、写作极为成熟的proposal。它不试图声称\"我们的方法beats everything\"，而是严谨地定义了一个新的operating point（minimal-information level），并系统地探索该operating point的检测能力边界。这种\"measurement science\"的风格在EMNLP是被接受的。retroactive prevalence analysis作为独特的应用场景非常有说服力——确实没有其他方法能在不重新推理的情况下审计历史评估日志。\n\n然而，核心担忧是：这篇工作的方法论贡献本质上是将教育测量学中已有的工具（lz*）直接应用到LLM评估这个新领域。跨领域迁移本身有价值，但reviewers可能会质疑技术深度不够——毕竟lz*的公式、理论性质、检测能力特征都是现成的。这与\"提出新方法\"有本质区别。\n\n【核心贡献】:\n1. **方法贡献**：首次将psychometric person-fit statistics（特别是lz*）应用于LLM benchmark污染检测，建立了一个新的信息-检测力前沿点（minimal-information operating point）。\n2. **实证贡献**：对Open LLM Leaderboard进行首次大规模retroactive污染审计，利用现有评估日志而非新测试。\n3. **理论贡献**：记录并论证binary-response-pattern方法的inverted-U检测力限制（proof sketch），为该类方法划定理论边界。\n\n贡献的领域价值**中等偏上**：retroactive audit能力是genuinely useful的，因为大量历史评估数据已经存在但从未被用于污染检测。minimal-information framing为信息访问受限的场景（如API-only模型、已下线模型）提供了实际方案。但总体检测能力可能有限，限制了方法的独立价值（更可能作为complementary tool而非primary detection method）。\n\n【方法合理性】:\n方法本身是合理的——lz*在教育测量学中有数十年的理论和实证基础，\"contaminated LLM ≈ examinee with item preknowledge\"的类比在概念上站得住。4PL IRT model、MLE/EAP/WLE能力估计、Benjamini-Hochberg FDR控制——这些都是成熟的统计工具。\n\n**更简单的替代方案？** Proposal自己设置了Tier 0 baselines（Accuracy-Z, Guttman Error Count, Difficulty-Residual Correlation）来回答这个问题。如果这些简单统计量能达到接近lz*的性能，那IRT machinery的marginal value就受质疑。这一点proposal处理得很好——直接做了ablation。\n\n**潜在问题**：\n(1) 对PSN-IRT参数质量的依赖：如果item parameters估计不准（特别是guessing parameter c和upper-asymptote d），整个方法的基础就不牢固。PSN-IRT的calibration sample本身可能包含contaminated models，导致circular dependency。\n(2) Unidimensionality假设：MMLU是多维benchmark，在全benchmark级别计算lz*可能违反IRT假设。proposal计划做per-domain分析来缓解，但这会大幅减少每个分析的item数量，进而降低检测power。\n(3) SFT泛化效应可能是fundamental limitation：如果fine-tuning on 20% items提升了整个domain的能力，response pattern看起来就像genuine high ability，person-fit根本无法区分。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — Benchmark污染检测是LLM评估领域公认的重要问题（ConStat获NeurIPS 2024, Min-K%++获ICLR 2025 Spotlight），且\"minimal-information operating point\"这个切入角度确实是空白。\"能否仅从binary response pattern检测污染？\"是一个well-defined且有理论意义的问题。retroactive audit的需求是真实的——大量历史评估数据无法被现有方法利用。\n\n2. **方法与创新: 中** — 跨领域迁移（psychometric person-fit → LLM evaluation）是有意义的，但核心方法lz*本身是1990s-2000s的教育测量学工具（Snijders 2001; Karabatsos 2003），proposal的技术贡献主要是\"应用到新domain\"而非\"提出新方法\"。与ConStat（提出了新的污染定义和检测统计量）、Self-Critique（发现并利用post-RL entropy collapse现象）、CoDeC（设计了ICL-based detection paradigm）相比，方法论创新深度较浅。inverted-U的\"proof sketch\"被描述为informal conjecture，理论贡献也有限。不过，minimal-information framing本身的conceptual contribution是有价值的。\n\n3. **实验设计: 强** — 这是proposal最大的亮点之一。126 controlled conditions × 3 seeds，access-level stratified baselines（Tier 0/1/2三层对比），3种item sampling策略的ablation，IRT模型复杂度ablation（2PL→3PL→4PL），4种person-fit统计量对比，3种ability estimation方法对比，post-RL robustness test跟踪RL steps，simulation-based power analysis覆盖多种test length和contamination fraction——这比该领域大多数论文（包括ConStat和Min-K%++）的实验设计都更加thorough。特别是Tier 0 baselines直接回答了\"IRT是否比简单统计量更好\"这个根本问题，显示出深度思考。对PSN-IRT calibration bias的empirical verification也很周到。\n\n4. **可行性: 强** — ~2,500 H100-hours在当前学术界标准下完全可行（一个lab allocation一周内可完成）。QLoRA contamination protocol是标准的。主要依赖项（PSN-IRT 4PL parameters, Open LLM Leaderboard response logs, lm-evaluation-harness）都是公开可用的。IRT-FIT本身的计算（person-fit statistics）几乎是CPU-only的。唯一风险点是Open LLM Leaderboard的per-item response logs是否完整可获取。\n\n5. **写作与呈现: 强** — Proposal写作极其清晰和专业。问题定义精确，related work覆盖全面且stratified by access level，实验设计结构化程度很高，expected outcomes诚实（明确承认aggregate AUROC可能低于gray-box方法），limitations讨论坦率（SFT generalization, pretraining exposure out-of-scope）。唯一小问题是sections有些偏长，可能需要在实际论文中压缩。\n\n【概率估计】: [30% - 42%] 中位 36%\n\n【估计理由】:\n**推高因素**: (1) 研究问题重要且切入角度genuinely novel（minimal-information operating point无人占据）；(2) 实验设计非常comprehensive，超越了该领域多数已发表工作的标准；(3) retroactive prevalence analysis提供了独特且实际有用的应用场景；(4) 写作成熟、honest about limitations，审稿体验好；(5) IRT在LLM评估中的应用正成为趋势（PSN-IRT AAAI 2026 Oral, ATLAS, MedIRT），时机合适。\n\n**压低因素**: (1) 核心方法论创新深度不足——lz*是现成工具，跨领域应用虽有价值但在top venue可能被视为incremental；(2) inverted-U检测力限制意味着方法仅在10-30%污染率窗口内有效，实际应用范围受限；(3) SFT generalization可能是fundamental limitation，如果实验结果显示generalization严重smooths aberrance signal，则方法价值大打折扣；(4) 不能检测pretraining exposure（最常见的污染形式），限制了声明的通用性；(5) 污染检测领域竞争激烈（2024-2026每年多篇顶会），reviewer可能对\"又一个检测方法\"审美疲劳；(6) inverted-U的\"proof sketch\"是informal conjecture而非formal proof，理论贡献打折扣。\n\n综合来看，这是一篇well-executed的proposal，方向正确、实验扎实、定位清晰，但方法论创新深度不足以让它成为strong accept。在EMNLP 2026的竞争环境下，它处于borderline位置——大概率进入讨论区，最终结果取决于reviewer是否认可\"minimal-information characterization + retroactive audit capability\"的组合价值。\n\n【主要风险】:\n1. **方法论创新深度不足被reviewer质疑**: Reviewer可能认为\"将教育测量学的lz*应用到LLM评估\"是straightforward application而非methodological contribution，特别是当lz*的所有理论性质（包括inverted-U）都已在psychometrics文献中建立。如果2/3的reviewers持此看法，论文可能获得\"interesting application but limited novelty\"的评价。\n2. **检测能力不足以justify the paper**: 如果实验结果显示(a) lz*相比Tier 0 naive baselines的marginal gain很小，或(b) SFT generalization严重削弱检测力，或(c) post-RL之后信号完全消失——那么paper的实证价值会大幅降低。inverted-U意味着该方法根本无法检测最高风险的场景（大规模污染），这在reviewer眼中可能是dealbreaker。\n\n【实施评估】:\n  - 计算资源: ~2,500 H100-hours，约等于$5,000-7,500 cloud cost，对学术lab完全可行\n  - 数据需求: PSN-IRT 4PL参数（公开）、Open LLM Leaderboard per-item response logs（部分公开，需确认完整性）、6个benchmark数据集（均公开）\n  - 人工介入: 低。QLoRA fine-tuning和person-fit计算均可自动化。Post-RL实验需要careful tuning但属于标准工程。\n  - 训练需求: 需要训练126+ contaminated models（QLoRA）+ 9 full-parameter SFT + post-RL GRPO，但每个都是标准fine-tuning任务\n  - 新 Benchmark: 不需要构建新benchmark；使用现有benchmark + PSN-IRT参数\n  - 预估周期: 3-4个月（1个月搭建pipeline + 1.5个月运行实验 + 1个月分析写作），假设GPU资源充足\n```\n\nSources:\n- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)\n- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)\n- [Min-K%++ (ICLR 2025)](https://arxiv.org/abs/2404.02936)\n- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/abs/2510.27055)\n- [Self-Critique: Detecting Contamination from RL Post-training (ICLR 2026)](https://arxiv.org/abs/2510.09259)\n- [Wang et al.: Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)\n- [Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts](https://arxiv.org/abs/2410.09247)\n- [Han et al.: Quantifying Data Contamination in Psychometric Evaluations (EACL 2026 Findings)](https://aclanthology.org/2026.findings-eacl.319/)\n- [ATLAS: Adaptive Testing for LLM Evaluation (AAAI 2027)](https://arxiv.org/abs/2511.04689)\n- [MedIRT: Measuring Competency Across Medical Benchmarks](https://arxiv.org/abs/2509.24186)\n- [Silicon Bureaucracy (arXiv 2026)](https://arxiv.org/abs/2603.21636)\n- [Cross-Context Verification (arXiv 2026)](https://arxiv.org/abs/2603.21454)\n- [Braeken & van Laar (2025): Reducing Calibration Bias for Person Fit Assessment](https://journals.sagepub.com/doi/10.1177/00131644251364252)\n- [Comprehensive Survey of Contamination Detection Methods](https://arxiv.org/abs/2404.00699)\n- [Benchmarking LLMs Under Data Contamination: Static to Dynamic Evaluation](https://arxiv.org/abs/2502.17521)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n## IRT-FIT: Detecting Benchmark Contamination in LLMs at the Minimal-Information Operating Point via Psychometric Person-Fit Statistics\n\n## 1. Problem Statement\n\nBenchmark contamination—where LLMs are trained on evaluation data—undermines the reliability of capability assessments. As benchmarks proliferate and training corpora grow opaque, robust contamination detection is critical for evaluation integrity. Existing detection methods operate at various levels of model access: token-level probabilities (Min-K%++, ICLR 2025 Spotlight; CoDeC, arXiv:2510.27055, ICLR 2026), entropy sequences (Self-Critique, arXiv:2510.09259, ICLR 2026), confidence scores (PaCoST, EMNLP 2024 Findings, arXiv:2406.18326), guided instruction completion (Time Travel in LLMs, Golchin & Surdeanu, ICLR 2024), or the ability to re-administer modified benchmark items (ConStat, NeurIPS 2024, arXiv:2405.16281; Silicon Bureaucracy, arXiv:2603.21636; Cross-Context Verification, arXiv:2603.21454). All require information beyond what is minimally available in a standard evaluation: the binary (correct/incorrect) response pattern.\n\nThis paper asks a foundational question: **what is the detection power envelope when operating at the minimal-information level—binary response patterns alone?** We propose IRT-FIT, which applies psychometric person-fit statistics to LLM benchmark evaluation, establishing a new operating point on the information-access vs. detection-power frontier. By leveraging calibrated Item Response Theory (IRT) parameters, IRT-FIT detects aberrant response patterns indicative of item-level memorization contamination, without requiring any model internals, re-testing, or additional inference.\n\n## 2. Core Contributions\n\n1. **Minimal-information contamination detection.** IRT-FIT is the first method that detects benchmark contamination using only binary response patterns and pre-calibrated item parameters—the lowest possible information access level. It complements gray-box methods requiring model internals (CoDeC, Self-Critique, Min-K%++) and re-administration methods requiring new test items (ConStat, Silicon Bureaucracy, CCV). Crucially, we demonstrate that lz* captures item-level response pattern structure (the joint likelihood of the specific correct/incorrect combination given ability) that simple aggregate statistics (accuracy anomaly, Guttman error count) cannot exploit, justifying the IRT machinery.\n\n2. **Retroactive contamination prevalence analysis.** Because IRT-FIT requires only binary response patterns already recorded in evaluation logs, it enables systematic historical audit of contamination prevalence—analyzing how contamination rates on public leaderboards have evolved over time. No other method can perform this retroactive analysis: gray-box methods require live model access; ConStat requires re-testing on rephrased items; Benchmark Inflation (arXiv:2410.09247) requires constructing benchmark-specific holdout sets. We apply IRT-FIT to all models with available per-item response records on the Open LLM Leaderboard, producing the first large-scale contamination prevalence timeline.\n\n3. **Characterization of detection limits for response-pattern methods.** We document an inverted-U detection power curve and provide an informal proof sketch for its two endpoints: at contamination fraction → 0%, the aberrance signal is submerged below the noise floor of finite-item statistical tests (power → 0 by standard hypothesis testing limits); at contamination fraction → 100%, uniform high performance is indistinguishable from genuine high ability since binary response patterns carry no information to separate the two (identifiability collapse). Between these endpoints, detection power peaks at 10–30% contamination. We conjecture this inverted-U characterizes a general limit of all binary-response-pattern-based detection methods, extending prior observations in educational testing (Sinharay, 2017, JEBS).\n\n4. **Cross-domain methodological transfer.** We bridge psychometric testing theory—specifically person-fit analysis for detecting cheating examinees (Sinharay, 2017, JEBS; Karabatsos, 2003; Gorney et al., 2023)—to LLM evaluation, demonstrating that the analogy \"contaminated LLM ≈ examinee with item preknowledge\" is operationally productive.\n\n## 3. Scope and Assumptions\n\n**Detection scope.** IRT-FIT targets **item-level memorization contamination**—where an LLM has been fine-tuned on or memorized specific benchmark question-answer pairs, producing an aberrant pattern of correct responses deviating from IRT model predictions. This corresponds to SFT/data-leakage contamination pathways.\n\n**SFT generalization effect.** The core analogy \"contaminated LLM ≈ examinee with item preknowledge\" assumes contamination produces item-specific performance gains. However, SFT on a subset of benchmark items may produce partial generalization to semantically related non-trained items—smoothing the aberrance signal. For example, fine-tuning on 20% of MMLU biology questions may improve performance on the remaining 80% of biology questions. This generalization radius, if large, weakens person-fit detection power by making the response pattern more consistent with genuine high ability. Our experimental design directly tests this: the hard-item-only contamination condition (Section 6.1) is motivated by the expectation that hard items have smaller generalization radii, and per-domain analysis (Section 6.4) controls for within-domain generalization.\n\n**Out of scope.** Distributional pretraining exposure—where benchmark content appears amidst massive pretraining corpora producing smooth, generalizable ability improvement—will not generate item-specific aberrance. This limitation is shared by all response-pattern-based methods. Wang et al. (arXiv:2510.02386) distinguish Stage I (pretraining/SFT) and Stage II (post-RL) contamination; our experiments simulate both.\n\n## 4. Method\n\n**4.1 IRT Parameterization.** We use 4PL IRT parameters (discrimination a, difficulty b, guessing c, upper asymptote d) calibrated by PSN-IRT (\"Lost in Benchmarks?\", AAAI 2026 Oral, arXiv:2505.15055), covering 41,871 items across 11 benchmarks. The 4PL model predicts:\n\nP(X_j=1|θ) = c_j + (d_j − c_j) / (1 + exp(−a_j(θ − b_j)))\n\n**4.2 Person-Fit Statistic (lz*).** For each model, we compute the standardized log-likelihood person-fit statistic lz* (Snijders, 2001; Sinharay, 2017):\n\nl_z* = [Σ_j (x_j log p_j + (1−x_j) log(1−p_j)) − E[l|θ̂]] / √Var[l|θ̂]\n\nwhere p_j = P(X_j=1|θ̂). Under the null (no aberrance), lz* ~ N(0,1). Significantly negative lz* indicates response patterns inconsistent with the IRT model—the signature of item preknowledge.\n\n**Why lz* over simple statistics.** Unlike aggregate measures (accuracy z-score, Guttman error count), lz* evaluates the joint likelihood of the full item-response vector given estimated ability, capturing complex aberrance patterns (e.g., failing easy items while acing specific hard items) that difficulty-stratified statistics miss. This distinction is empirically validated in our ablation (Section 6.4) and theoretically grounded in the person-fit literature (Karabatsos, 2003).\n\n**Calibration considerations.** Braeken & van Laar (2025) note that lz* can exhibit calibration bias when IRT parameters are estimated on data containing misfitting respondents. Since PSN-IRT calibrates on LLM responses that may include contaminated models, we verify lz* calibration empirically (Section 7) and provide an empirical null adjustment if the N(0,1) assumption is violated.\n\n**4.3 Detection Pipeline.**\n1. Retrieve pre-calibrated 4PL item parameters from PSN-IRT for target benchmark.\n2. Obtain binary response pattern for target LLM—from existing evaluation logs or new evaluation.\n3. Estimate model ability θ̂ via maximum likelihood.\n4. Compute lz* and derive p-value under N(0,1) or empirical null.\n5. For single-model testing: flag if p < α. For multi-model audit: apply Benjamini-Hochberg FDR control.\n\n## 5. Related Work\n\n**Contamination detection requiring model internals (gray-box).** Min-K%++ (ICLR 2025 Spotlight) thresholds token-level log-likelihoods. CoDeC (arXiv:2510.27055, ICLR 2026) uses in-context learning to compare confidence on seen vs. unseen data. Self-Critique (arXiv:2510.09259, ICLR 2026) detects post-RL contamination via entropy-sequence policy collapse (~30% AUC improvement). PaCoST (EMNLP 2024 Findings, arXiv:2406.18326) compares confidence on original vs. perturbed items. Time Travel in LLMs (Golchin & Surdeanu, ICLR 2024) uses guided instruction to reconstruct benchmark instances.\n\n**Contamination detection from external probing.** ConStat (NeurIPS 2024, arXiv:2405.16281) detects non-generalizing performance inflation via comparison with rephrased/synthetic reference benchmarks (r²=0.94 with ground-truth). Silicon Bureaucracy (arXiv:2603.21636) uses perturbation-based score credibility audit. Cross-Context Verification (arXiv:2603.21454) achieves perfect separation via session-isolated diversity analysis.\n\n**Retroactive contamination analysis.** Benchmark Inflation (arXiv:2410.09247) constructs retro-holdout datasets to quantify performance gaps (up to 16pp on TruthfulQA). Key difference from IRT-FIT: retro-holdouts require constructing new benchmark-specific holdout sets and re-evaluating models, while IRT-FIT operates on existing response patterns with no new data generation or model inference.\n\n**Key differentiation from ConStat.** Both ConStat and IRT-FIT operate without model internals. However, ConStat requires (a) generating semantically equivalent rephrased items, (b) re-administering benchmarks to each model, and (c) reference model comparison. IRT-FIT requires none of these—only existing binary response patterns and pre-calibrated IRT parameters—enabling retroactive audit where re-testing is impossible.\n\n**Post-RL contamination robustness.** Wang et al. (arXiv:2510.02386) demonstrate that even brief GRPO training conceals MIA-based signals. Our post-RL experiments test whether response-pattern-level signals exhibit different robustness properties than model-internal signals.\n\n**IRT for LLM evaluation.** PSN-IRT (AAAI 2026 Oral, arXiv:2505.15055) calibrated 4PL parameters for 41,871 items across 11 benchmarks. ATLAS (arXiv:2511.04689, AAAI 2027) introduces IRT-based adaptive testing, reducing items by 90% while maintaining precision and showing 23–31% rank reordering. MedIRT (arXiv:2509.24186, ICLR 2027) applies 2PL IRT per topic to 80 LLMs on medical benchmarks. \"Lifting the Benchmark Iceberg with Item-Response Theory\" (ICLR 2024) reveals how hidden implementation choices affect rankings and proposes IRT for transparent measurement. Han et al. (EACL 2026 Findings) quantify contamination in psychometric questionnaires but do not employ person-fit statistics. None connect IRT to contamination detection via person-fit.\n\n**Person-fit in educational testing.** Person-fit statistics have extensive foundations (Karabatsos, 2003; Sinharay, 2017, JEBS; Gorney et al., 2023). Sinharay (2017) establishes lz* detection power peaks at 10–30% preknowledge with inverted-U shape. Braeken & van Laar (2025) identify calibration bias in lz* from contaminated calibration samples. Tendeiro et al. (2023) propose iterative scale purification improving Type-I error control. We transfer these tools to LLM evaluation, addressing calibration concerns via empirical null adjustment.\n\n## 6. Experimental Design\n\n**6.1 Controlled Contamination Experiment**\n\n**Models.** Llama 4 Scout (109B MoE), Gemma 4 27B, Qwen 3.5-9B—spanning MoE and dense architectures at different scales.\n\n**Benchmarks.** Six from PSN-IRT's calibrated set: MMLU (large, multi-domain), ARC-Challenge (science reasoning), HellaSwag (commonsense), WinoGrande (coreference), TruthfulQA (~817 items), HumanEval (~164 items). Selection provides test-length variation for power analysis.\n\n**Contamination protocol.** QLoRA fine-tuning on fraction f ∈ {0%, 5%, 10%, 20%, 30%, 50%, 100%} of benchmark items, producing 3 models × 6 benchmarks × 7 levels = 126 conditions, each with 3 random seeds. Additionally, full-parameter SFT on Qwen 3.5-9B at f ∈ {10%, 20%, 50%} to validate QLoRA as contamination proxy (9 additional conditions × 3 seeds).\n\n**Item sampling strategy ablation.** Three strategies per contamination fraction:\n- Random uniform sampling\n- Hard-item-only (top 30% by IRT difficulty b)—primary condition (most realistic: easy items are answerable without memorization)\n- Stratified (proportional to difficulty distribution)\n\n**6.2 Baselines (Access-Level Stratified)**\n\n**Tier 0 — Naive response-pattern baselines (same operating point as IRT-FIT):**\n- **Accuracy-Z**: z-score of target model's accuracy relative to models in the same ability band\n- **Guttman Error Count**: number of item pairs violating difficulty ordering (Karabatsos, 2003)\n- **Difficulty-Residual Correlation**: correlation between item-level residuals and IRT difficulty b (contaminated models should show positive residual on high-difficulty items)\n\nThese baselines use the same information as IRT-FIT (binary responses + IRT parameters) but without the full person-fit statistical framework, directly testing whether lz*'s joint-likelihood approach provides marginal value over simpler aggregate statistics.\n\n**Tier 1 — Black-box requiring re-testing:**\n- ConStat (NeurIPS 2024, arXiv:2405.16281) — rephrased benchmark comparison\n\n**Tier 2 — Gray-box (token-level access):**\n- Min-K%++ (ICLR 2025 Spotlight)\n- CoDeC (arXiv:2510.27055, ICLR 2026)\n- Self-Critique (arXiv:2510.09259, ICLR 2026)\n- PaCoST (EMNLP 2024 Findings, arXiv:2406.18326)\n\nPrimary evaluation: IRT-FIT vs. Tier 0 (does IRT machinery add value?) and vs. Tier 1 (does avoiding re-testing sacrifice detection power?). Secondary: cross-tier comparison with gray-box methods.\n\n**6.3 Post-RL Robustness Test**\n\nOn **two models** (Qwen 3.5-9B and Gemma 4 27B):\n- **Stage 1**: SFT contamination at 20% and 50% fractions\n- **Stage 2a** (Clean RL): GRPO on non-benchmark data (reward = outcome correctness on held-out problems)\n- **Stage 2b** (Contaminated RL): GRPO where benchmark items appear in RL data\n- **GRPO configuration**: Following Wang et al. (arXiv:2510.02386) for comparability; detection power reported at checkpoints {100, 500, 1000, 2000, 5000} RL steps\n- **Comparison**: IRT-FIT trajectory vs. MIA-based methods (Min-K%++, Self-Critique) across RL training steps\n\n**6.4 Ablation Studies**\n\n- **IRT model complexity**: 2PL (c=0, d=1) → 3PL (d=1) → 4PL, quantifying marginal contribution of guessing and upper-asymptote parameters. Parameter sets derived from PSN-IRT (arXiv:2505.15055).\n- **Person-fit statistics**: lz* vs. U3, W, Ht (Karabatsos, 2003)\n- **Ability estimation**: MLE vs. EAP vs. WLE for θ̂\n- **IRT parameter source**: PSN-IRT 4PL parameters vs. conventionally calibrated parameters (mirt R package on same response data), testing sensitivity to parameter estimation method\n- **Unidimensionality diagnostic**: For multi-domain benchmarks (MMLU), compare full-benchmark lz* vs. per-subject-domain lz*, testing whether domain-level analysis reduces false positives from multidimensionality (Braeken & van Laar, 2025)\n\n**6.5 Power Analysis and Detection Limits**\n\n- **Simulation study**: Synthetic response patterns under 4PL at varying ability levels, test lengths {50, 164, 500, 817, 1000, 5000}, contamination fractions {0%, 3%, 5%, 10%, 20%, 30%, 50%, 100%}, 10,000 replications per condition.\n- **Test length analysis**: Minimum items for reliable detection per contamination fraction. Per-benchmark expected power.\n- **Inverted-U documentation with proof sketch**: Plot detection power curve; provide informal argument for endpoint impossibility (noise floor at low contamination; identifiability collapse at high contamination).\n\n## 7. Evaluation Metrics\n\n- **AUROC/AUPRC**: Aggregate and per-contamination-level discrimination\n- **Per-contamination-level power**: P(reject H₀ | H₁) at α=0.05—core inverted-U visualization\n- **Type-I error calibration**: Empirical FPR at α ∈ {0.01, 0.05, 0.10} on clean models; Q-Q plot of lz* under null to verify N(0,1) assumption; if violated, report empirical null parameters and adjusted detection power\n- **Benjamini-Hochberg FDR**: Applied to multi-model audit scenarios; report FDR-controlled detection rates at q ∈ {0.05, 0.10, 0.20}\n\n## 8. Contamination Prevalence Analysis\n\n**Systematic historical audit.** Apply IRT-FIT to all models on the Open LLM Leaderboard with available per-item response logs (via lm-evaluation-harness output or reproducible re-evaluation of open-weight models). Produce: (a) per-benchmark contamination prevalence over time (fraction of models flagged at FDR=0.10); (b) contamination severity distribution (lz* score distribution across models); (c) trend analysis (has contamination prevalence increased with leaderboard competition?).\n\n**Convergent validation.** Compare IRT-FIT flagging with ConStat's published findings on Mistral, Llama, Yi, and top-3 Open LLM Leaderboard models (ConStat, NeurIPS 2024).\n\n**Known-clean negative controls.** Verify IRT-FIT does not flag OLMo models (AI2), whose training data (Dolma) is fully open and auditable via OlmoTrace, providing false-positive control in the wild.\n\n**Limitations.** Convergent validation cannot establish ground truth (two methods may share systematic biases). The controlled experiment (Section 6.1) remains the primary validation; the prevalence analysis is positioned as an illustrative application demonstrating IRT-FIT's unique retroactive capability.\n\n## 9. Compute Estimates\n\n- **Controlled contamination (QLoRA)**: 126 conditions × 3 item strategies × 3 seeds × ~1.5h avg ≈ 1,700 H100-hours\n- **Full-parameter SFT (Qwen 9B)**: 9 conditions × 3 seeds × ~2h ≈ 54 H100-hours\n- **Post-RL (2 models)**: ~350 H100-hours\n- **Inference for prevalence analysis**: Minimal (per-item response collection for open-weight models + CPU-only person-fit computation)\n- **Hardware per model**: Llama 4 Scout QLoRA: 1× H100 (~71GB via Unsloth); Gemma 4 27B QLoRA: 1× H100 (~30GB); Qwen 3.5-9B: 1× A100 40GB\n- **Total**: ~2,500 H100 GPU-hours\n\n## 10. Expected Outcomes\n\nWe expect: (a) lz* outperforms Tier 0 naive baselines (Accuracy-Z, Guttman errors, Difficulty-Residual) by capturing joint response-pattern structure, empirically justifying the IRT person-fit framework; (b) competitive performance with ConStat in Tier 1, with the advantage of no re-testing; (c) aggregate AUROC possibly below gray-box methods—an expected consequence of minimal information access; (d) inverted-U detection power confirmed with peak at 10–30%; (e) partial post-RL robustness, with response-pattern signals degrading differently from internal signals; (f) the historical prevalence analysis revealing contamination trends across leaderboard history, demonstrating IRT-FIT's unique retroactive capability."
}
````

---

### Runtime record

_source line 2 · 2026-05-20T05:31:53.491Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:31:53.491Z",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T05:31:53.502Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient context to produce my evaluation. Let me compile the full assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Comprehensive Survey of Contamination Detection Methods in LLMs, arXiv:2404.00699] (2024, updated 2025): 系统综述了 50+ 检测技术和 100+ 篇相关论文，将方法分为 open-data 和 closed-data 两大类。IRT-FIT 所在的"仅凭二元响应模式"区域是现有方法覆盖的空白地带。
- [Min-K%++, ICLR 2025 Spotlight]: Token-level log-likelihood 方法，需要灰盒访问。已成为 pretraining data detection 的标准 baseline，验证了 IRT-FIT 声称的信息访问层级差异。
- [CoDeC, arXiv:2510.27055, ICLR 2026]: 基于 in-context learning 的数据集级污染检测，需要 token-level 访问。与 IRT-FIT 处于不同信息访问层。
- [Self-Critique, arXiv:2510.09259, ICLR 2026]: 首个系统研究 RL post-training 对污染检测信号影响的工作，AUC 提升约 30%。IRT-FIT 的 post-RL 实验直接呼应此工作。
- [ConStat, NeurIPS 2024]: 最直接的竞争者——同样不需要模型内部访问，但需要重新施测（rephrased items + reference models）。IRT-FIT 的核心差异化点在于无需 re-testing。r²=0.94 的 ground-truth 相关性是很强的 baseline。
- [Benchmark Inflation, arXiv:2410.09247]: 通过 retro-holdout 方法量化性能差距（TruthfulQA 上高达 16pp），但需要构建 benchmark-specific holdout 集并重新评估模型。IRT-FIT 的 retroactive 分析无需任何新数据。
- [PSN-IRT, AAAI 2026 Oral, arXiv:2505.15055]: 为 41,871 items × 11 benchmarks 校准了 4PL IRT 参数。这是 IRT-FIT 的直接上游依赖，参数已公开可用，降低了实施风险。
- [Tendeiro et al., 2023, Multivariate Behavioral Research]: 提出 iterative scale purification 改善 lz* 在包含 misfitting respondents 数据上的 Type-I error 控制。IRT-FIT 引用了此工作但未采用其方法——可能被审稿人追问。
- [Han et al., EACL 2026 Findings]: 量化了 LLM 在心理量表上的 contamination，但未使用 person-fit statistics——最近的相关但未重叠的工作。

- 调研总结: Benchmark contamination detection 是一个高度活跃且拥挤的领域（100+ 篇论文），但方法按信息访问需求明显分层。IRT-FIT 填补了一个真实的空白——"仅凭二元响应模式"的最小信息操作点。该领域目前没有任何工作将 IRT person-fit statistics 应用于 LLM 污染检测，跨领域转移的 novelty claim 成立。主要竞争来自 ConStat（同属黑盒但需 re-testing），以及 Benchmark Inflation（retroactive 但需构建 holdout）。

【整体印象】:
作为审稿人，我的第一反应是**倾向 weak accept**。这是一篇定位清晰、方法论基础扎实、实验设计异常周全的 proposal。"minimal-information operating point" 的框架提供了一个有价值的概念贡献——不是声称比灰盒方法更好，而是明确探索信息访问 vs. 检测能力的权衡前沿。retroactive contamination prevalence analysis 是真正独特且有实际价值的应用场景。最大的担忧是方法层面的 novelty——本质上是将心理测量学中成熟的 lz* 统计量跨领域应用到 LLM 评估，方法创新的深度有限。

【核心贡献】:
核心贡献有三层：
1. **概念贡献**：建立了 contamination detection 的 information-access frontier 框架，明确了二元响应模式作为最小信息操作点的位置。这是一个组织性的概念洞察，帮助社区理解不同方法之间的权衡关系。
2. **方法贡献**：将 IRT person-fit statistics (lz*) 跨领域转移到 LLM 评估，证明 "contaminated LLM ≈ examinee with item preknowledge" 这个类比是操作上可行的。
3. **实证贡献**：首个大规模 retroactive contamination prevalence timeline，以及 inverted-U 检测能力曲线的系统刻画。

对领域的价值：**中等偏高**。该方法不会取代灰盒方法或 ConStat，但它开辟了一个独特的使用场景（历史审计）和一个独特的理论视角（最小信息检测极限）。这不是 incremental work，但也不是 paradigm-shifting work。

【方法合理性】:
方法是合理的且有坚实的理论基础（psychometric person-fit literature 几十年的积累）。lz* 是 person-fit 领域最广泛使用和研究最深入的统计量，选择合理。

**更简单替代方案的考量**：Proposal 在 Tier 0 baselines 中已经包含了最明显的简单替代方案（Accuracy-Z、Guttman Error Count、Difficulty-Residual Correlation），并将其作为消融实验的核心。这是一个非常聪明的实验设计选择——如果 lz* 未能显著超越这些简单统计量，论文的核心论点就会崩塌，而 proposal 坦诚地将此作为实验的首要验证目标。

**潜在方法问题**：
- PSN-IRT 参数校准于可能包含 contaminated models 的响应数据，存在循环偏差风险（Braeken & van Laar, 2025）。Proposal 承诺 empirical null adjustment，但这不一定能完全解决问题。
- 多维度 benchmarks (如 MMLU 的 57 个学科) 上的 unidimensionality 假设违反可能导致 false positives。Per-domain 分析部分缓解但增加了多重检验负担。
- SFT generalization effect 可能在真实场景中严重削弱检测能力——这是一个根本性的限制，proposal 坦诚承认但无法解决。

【5 维度打分】:

1. 研究问题: 【强】 — Benchmark contamination 是 LLM 评估的核心问题，受到广泛关注（100+ 篇论文的活跃领域）。"最小信息操作点下的检测能力上界"是一个有意义的理论问题，而非 engineering increment。retroactive audit 的实际需求真实存在——许多早期模型已下线无法重新测试。问题本身具有足够的研究深度（inverted-U 的理论分析、检测极限的刻画）。

2. 方法与创新: 【中】 — 跨领域转移（psychometrics → LLM evaluation）是本文的核心 novelty，且 claim 成立——确实没有先前工作将 person-fit statistics 应用于 LLM 污染检测（Han et al., EACL 2026 是最近的相关工作但未使用 person-fit）。然而，方法本身（lz* 统计量、4PL IRT 模型、MLE 能力估计）完全是现有工具的直接应用，没有方法论层面的创新。与 ConStat 相比（NeurIPS 2024，提出了污染的新定义和新的统计检验框架），IRT-FIT 的方法创新深度较浅。inverted-U 的 proof sketch 增加了一些理论深度，但作者自己也只称之为 "informal"。

3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。126 conditions × 3 sampling strategies × 3 seeds 的控制实验规模在该领域中属于上乘。Access-level stratified baselines 设计极为精巧——Tier 0 直接检验 IRT machinery 的边际价值，Tier 1/2 定位 IRT-FIT 在信息-检测权衡中的位置。Post-RL robustness test 呼应 Self-Critique (ICLR 2026) 和 Wang et al. 的发现。消融研究全面覆盖了关键设计选择（IRT 模型复杂度、person-fit 统计量、能力估计方法、参数来源、unidimensionality）。Power analysis simulation (10,000 replications) 展现了统计严谨性。已知 clean 的负面控制 (OLMo) 和 convergent validation with ConStat 增加了说服力。

4. 可行性: 【中】 — ~2,500 H100-hours 计算需求实质性但合理（一个配备小型 H100 集群的实验室可以在数周内完成）。所有基础模型公开可用，PSN-IRT 参数已发布。主要风险点：(a) Open LLM Leaderboard 上的 per-item response logs 可用性不确定——许多模型可能只有聚合分数而无 item-level 记录，prevalence analysis 的规模可能受限；(b) 126 + 9 = 135 个 fine-tuning 条件 × 3 seeds = 405 次训练运行，调试和质量控制的工程量不小；(c) ConStat 等 baseline 的忠实复现需要额外工程投入。

5. 写作与呈现: 【强】 — Proposal 结构清晰、论证严密。问题动机从 information-access frontier 切入非常优雅。相关工作按信息访问层级组织（gray-box → re-testing → retroactive），既全面又有条理。对 limitations 的坦诚讨论（SFT generalization、pretraining exposure 不可检测、inverted-U 两端的 identifiability 问题）显示了作者的学术诚实。Expected outcomes 中 "aggregate AUROC possibly below gray-box methods" 的坦率预期是加分项——不过度 claim。

【概率估计】: [30% - 48%] 中位 38%

【估计理由】:
**上推因素**: (1) 填补了一个真实的方法论空白（minimal-information operating point），novelty claim 经调研验证成立；(2) 实验设计在该领域同类工作中属于顶级水平，Tier 0 baselines 的设计特别精巧；(3) retroactive audit 是一个杀手级应用场景，其他方法无法实现；(4) 写作质量高，定位清晰，不过度 claim；(5) IRT for LLM evaluation 正处于上升期（PSN-IRT AAAI 2026 Oral, ATLAS AAAI 2027, MedIRT ICLR 2027），时机好。

**下拉因素**: (1) 方法创新深度有限——本质是跨领域 apply 已有统计工具，部分审稿人可能认为 novelty 不足以支撑主会；(2) inverted-U 的根本性限制意味着该方法在极端污染比例（接近 0% 或 100%）下失效，而真实场景中这两种情况都很常见；(3) SFT generalization effect 可能严重削弱真实场景下的检测能力，proposal 虽然设计了相关实验但无法解决这个根本问题；(4) 对 PSN-IRT 参数的依赖引入了上游偏差风险；(5) 如果 Tier 0 baselines（特别是 Accuracy-Z 或 Difficulty-Residual）表现接近 lz*，核心论点会大幅削弱。

**综合判断**: 这是一篇 solid 的投稿，处于 borderline accept 区域。研究问题有价值、实验设计优秀、写作清晰，但方法创新深度有限是主要短板。最终概率高度依赖于实验结果：如果 lz* 显著超越 Tier 0 baselines 且 prevalence analysis 揭示有趣的 contamination trends，probability 向上界靠拢；如果 Tier 0 baselines 表现接近或 inverted-U 的可用检测窗口太窄，probability 向下界靠拢。

【主要风险】:
1. **方法 novelty 被质疑**: 审稿人可能认为"将 psychometrics 的 lz* 直接用于 LLM evaluation"是 application-level contribution 而非 methodological innovation，不足以支撑主会论文。这是最大的拒稿风险。
2. **Tier 0 baselines 表现相近**: 如果简单的 Accuracy-Z 或 Guttman Error Count 达到了与 lz* 相当的检测能力，那么整个 IRT person-fit 框架的额外复杂度就缺乏正当性——论文的核心论点将被釜底抽薪。

【实施评估】:
  - 计算资源: ~2,500 H100-hours（约 $5,000-7,500 @ spot pricing），需要至少 2-4 块 H100/A100 的并行能力，中等规模实验室可承受
  - 数据需求: PSN-IRT 4PL 参数（已公开）；6 个 benchmark 数据集（全部公开）；Open LLM Leaderboard per-item response logs（可用性不确定，是主要数据风险）
  - 人工介入: 中等——405 次 fine-tuning 运行的质量控制、ConStat 等 baseline 的复现、prevalence analysis 的数据收集和清洗
  - 训练需求: 需要大量 QLoRA/SFT fine-tuning（405 次基础运行 + 后续 RL 运行），但每次运行规模较小（9B-27B 模型 QLoRA）
  - 新 Benchmark: 不需要构建新 benchmark，使用 PSN-IRT 已校准的 6 个现有 benchmark
  - 预估周期: 4-6 个月（含代码开发、实验运行、分析和论文撰写）
```

Sources:
- [Comprehensive Survey of Contamination Detection Methods in LLMs](https://arxiv.org/html/2404.00699v4)
- [Min-K%++: Improved Baseline for Pre-Training Data Detection (ICLR 2025)](https://openreview.net/forum?id=ZGkfoufDaU)
- [CoDeC: Detecting Data Contamination in LLMs via In-Context Learning](https://arxiv.org/pdf/2510.27055)
- [Self-Critique: Detecting Data Contamination from RL Post-training](https://arxiv.org/abs/2510.09259)
- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf)
- [Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts](https://arxiv.org/abs/2410.09247)
- [PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [Iterative Scale Purification Procedure on lz for Aberrant Response Detection (Tendeiro et al., 2023)](https://www.tandfonline.com/doi/full/10.1080/00273171.2023.2211564)
- [What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide](https://llm-stats.com/blog/research/what-is-a-contaminated-llm)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough information to produce a thorough evaluation. Let me synthesize all findings.

---

```
【阶段】: Triage

【领域调研】:
- "Benchmarking Large Language Models Under Data Contamination: A Survey" (EMNLP 2025 Main): 综述涵盖50+检测技术，将方法分为静态/动态两大类。proposal的定位（minimal-information operating point）在该综述框架中属于未被系统探索的空白区域。
- ConStat (NeurIPS 2024, arXiv:2405.16281): 最直接的对标方法——同样无需模型内部参数，但需要生成重述题目并重新测试（r²=0.94 with ground-truth）。IRT-FIT的关键差异化点（无需re-testing/re-administration）成立。
- CoDeC (ICLR 2026, arXiv:2510.27055): 通过in-context learning比较seen/unseen数据的置信度差异，属于gray-box方法。与IRT-FIT不在同一access level，不构成直接竞争。
- Self-Critique (ICLR 2026, arXiv:2510.09259): 通过entropy sequence检测post-RL contamination，~30% AUC提升。与IRT-FIT在post-RL场景的比较是proposal的重要实验。
- PSN-IRT (AAAI 2026 Oral, arXiv:2505.15055): IRT-FIT的基础设施依赖——提供41,871 items的4PL参数。该工作已被顶会接收，基础扎实。
- ATLAS (arXiv:2511.04689, AAAI 2027): IRT-based adaptive testing，减少90%测试items。同样利用IRT但方向不同（效率 vs. 污染检测），不构成竞争。
- Wang et al. (arXiv:2510.02386): 揭示GRPO训练可隐藏MIA-based信号。proposal的post-RL实验直接对接该发现。
- Silicon Bureaucracy (arXiv:2603.21636) & Cross-Context Verification (arXiv:2603.21454): 2026年3月最新方法，分别用扰动审计和session-isolated多样性分析。均需要re-administration，与IRT-FIT不在同一operating point。
- 搜索"person-fit LLM contamination"未返回任何结果: 验证了proposal的核心novelty claim——目前无人将person-fit统计量应用于LLM污染检测。
- Han et al. (EACL 2026 Findings): 量化了心理测量问卷中的污染，但未使用person-fit统计量。最近的相关工作但仍有明确差异。

- 调研总结: LLM benchmark contamination detection是2024-2026年的活跃研究方向，已有方法覆盖gray-box（token-level access）和black-box（需re-testing）两个操作点，但"仅用binary response pattern"的minimal-information操作点确实是一个未被探索的空白。将psychometric person-fit statistics迁移到此问题目前无先例。

【整体印象】: 
作为审稿人，我的第一反应是"这是一个干净、有品位的research question，配上了异常扎实的实验设计"。Proposal清晰地识别了contamination detection方法图谱中的一个真实空白（minimal-information operating point），提出了一个有理论基础的解决方案（psychometric person-fit transfer），并且诚实地讨论了方法的固有局限性。这种"我知道这个方法不能打败gray-box方法，但我要系统地理解这个操作点上能做什么"的定位非常学术——是characterization而非superiority claim。倾向于weak accept / borderline accept，但最终取决于实际实验结果是否能支撑inverted-U curve等核心claim。

【核心贡献】: 
核心贡献有三层：(1) 建立了contamination detection的minimal-information operating point，首次仅用binary response patterns检测污染；(2) 实现retroactive contamination audit——这是一个genuinely unique的能力，其他所有方法都需要live model access或re-testing；(3) 理论层面characterize了binary-response-pattern方法的detection power envelope（inverted-U curve）。对领域的价值在于：即使lz*的绝对检测力不如gray-box方法，系统地理解"不同信息量级下能做什么"本身对contamination detection领域有结构性贡献。Retroactive audit能力有直接的实践价值。

【方法合理性】: 
方法本身是合理的——lz*在教育测试中有数十年的理论和实证基础（Karabatsos 2003; Sinharay 2017; Gorney et al. 2023），"contaminated LLM ≈ examinee with item preknowledge"的类比是站得住的。更简单的替代方案（accuracy z-score、Guttman error count、difficulty-residual correlation）已被设计为Tier 0 baselines，proposal明确要验证lz*是否提供marginal value over these simpler statistics，这一点很好。主要的方法论风险在于：(a) SFT generalization effect可能显著削弱aberrance signal；(b) PSN-IRT calibration本身可能包含contaminated models导致lz*的calibration bias（Braeken & van Laar 2025），虽然proposal提到了empirical null adjustment但这是一个需要实验验证的关键假设。

【5 维度打分】:
  1. 研究问题: 【强】 — "What is the detection power envelope at the minimal-information level?"是一个干净、有价值的研究问题。它不是"我做了一个更好的方法"，而是"我要系统地理解一个新的operating point"——这种framing既诚实又有深度。Retroactive audit的unique capability进一步提升了问题的实践价值。在EMNLP 2025的contamination survey（50+方法）中，这个operating point确实是空白。
  
  2. 方法与创新: 【中】 — 核心方法lz*不是新发明，而是从教育心理学的迁移应用。创新性在于：(a) 识别了cross-domain analogy的操作性价值；(b) 对detection limits的理论characterization。但相比ConStat（NeurIPS 2024，提出了contamination的新定义）或CoDeC（ICLR 2026，提出新的ICL-based detection paradigm），methodological novelty相对有限。Inverted-U curve的"informal proof sketch"如果不能formalize，可能被审稿人认为under-delivers。
  
  3. 实验设计: 【强】 — 这是proposal最大的亮点之一。126 conditions × 3 seeds的controlled contamination、access-level stratified baselines（Tier 0/1/2）的设计非常有结构感。特别值得肯定的是：(a) Tier 0 baselines直接检验IRT machinery的marginal value，这是很多paper会回避的对比；(b) post-RL robustness test直接对接Wang et al. (arXiv:2510.02386)的发现；(c) 5个维度的ablation study（IRT model complexity, person-fit statistics, ability estimation, parameter source, unidimensionality）覆盖了所有可能的methodological choice；(d) Open LLM Leaderboard prevalence analysis + OLMo negative controls。这个实验方案如果执行到位，本身就是一个重要贡献。参考ConStat和Min-K%++的实验设计，本proposal的baseline覆盖度和ablation深度均达到甚至超过了同类工作的标准。
  
  4. 可行性: 【中】 — 2,500 H100-hours是可控的计算成本。技术依赖链清晰（PSN-IRT参数 → lz*计算 → 统计检验）。主要风险：(a) 126个QLoRA fine-tuning runs的工程量不小，需要稳定的训练pipeline；(b) Open LLM Leaderboard的per-item response logs的可获取性可能存在gaps；(c) Post-RL实验（GRPO）需要follow Wang et al.的configuration，可能有复现难度。总体可行但需要扎实的工程基础设施和对leaderboard数据的access。
  
  5. 写作与呈现: 【强】 — Proposal的逻辑结构非常清晰：Problem → Core Contributions → Scope & Assumptions → Method → Related Work → Experimental Design → Evaluation Metrics。特别值得肯定的是：(a) 诚实地讨论了SFT generalization effect的威胁（Section 3）；(b) 清晰地界定了detection scope（item-level memorization vs. distributional pretraining exposure）；(c) Access-level stratified的related work组织方式让读者一眼看清方法图谱；(d) Expected Outcomes中不回避"aggregate AUROC possibly below gray-box methods"的预期。这种intellectual honesty在proposal阶段就展现出来，是加分项。

【概率估计】: [30% - 42%] 中位 36%

【估计理由】: 
这个proposal处于"solid submission"区间。往上推的力量：(1) 研究问题干净且有真实gap；(2) 实验设计异常扎实，baseline覆盖度和ablation深度达到顶级标准；(3) retroactive audit是unique selling point；(4) 写作清晰诚实。往下拉的力量：(1) 核心方法是cross-domain transfer而非methodological invention，部分审稿人可能认为novelty不够；(2) 如果实验结果显示lz*在practical relevant的contamination levels（5-20%）上检测力很弱，"characterizing the limits"的framing可能不足以支撑acceptance——审稿人可能反问"if the method barely works, why should we care about characterizing it?"；(3) inverted-U的"proof sketch"如果无法formalize，理论贡献会被打折。中位36%反映了"各方面合格到偏好，但缺乏一个decisive的亮点来push过acceptance threshold"的判断。如果实验结果在10-30% contamination区间确实展现出有意义的检测力，且retroactive analysis发现有价值的trend，概率可以上移到40%+。

【主要风险】: 
1. **Detection power可能过弱**: 在practical relevant的contamination fraction（5-20%）上，binary response patterns携带的信息可能不足以在统计上与genuine high ability区分，特别是在SFT generalization effect存在的情况下。如果core result是"lz*在大多数条件下barely beats Tier 0 baselines"，审稿人可能认为整个IRT框架的引入不justified。
2. **"Characterization"论文的acceptance barrier更高**: Proposal的定位是characterize a detection frontier而非claim superiority。这种framing虽然诚实，但在competitive reviewing中可能处于劣势——审稿人可能期待一个方法在某个维度上是"best in class"，而非仅仅"interesting characterization of limits"。

【实施评估】:
  - 计算资源: ~2,500 H100-hours，属于中等规模，需要稳定的GPU集群access（约1-2周连续使用8×H100节点）
  - 数据需求: PSN-IRT的4PL参数（已公开）；Open LLM Leaderboard per-item response logs（可获取性需要验证）；fine-tuning用的benchmark数据（公开）
  - 人工介入: 中等。QLoRA/SFT pipeline搭建、GRPO训练configuration、leaderboard数据收集和清洗需要显著的工程工作
  - 训练需求: 是。需要训练126+ fine-tuned models（QLoRA/SFT）+ post-RL models。这是实验的核心，不可避免
  - 新 Benchmark: 否。使用现有benchmark（MMLU, ARC-C, HellaSwag, WinoGrande, TruthfulQA, HumanEval）+ 已有IRT参数
  - 预估周期: 3-4个月（1个月搭建pipeline + 1.5个月跑实验 + 1个月分析和写作）
```

Sources:
- [Benchmarking LLMs Under Data Contamination Survey (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.511/)
- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://arxiv.org/pdf/2405.16281)
- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/html/2510.27055v1)
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/pdf/2505.15055)
- [ATLAS: Adaptive Testing for LLM Evaluation](https://arxiv.org/abs/2511.04689)
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/pdf/2510.02386)
- [Silicon Bureaucracy (arXiv 2603.21636)](https://arxiv.org/abs/2603.21636)
- [Cross-Context Verification (arXiv 2603.21454)](https://arxiv.org/abs/2603.21454)
- [PaCoST: Paired Confidence Significance Testing (EMNLP 2024 Findings)](https://arxiv.org/pdf/2406.18326)
- [Comprehensive Survey of Contamination Detection Methods](https://arxiv.org/pdf/2404.00699)
- [Person-Fit Assessment in IRT (Nature)](https://www.nature.com/research-intelligence/nri-topic-summaries/person-fit-assessment-in-item-response-theory-micro-129702)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me compile the evaluation.

```
【阶段】: Triage

【领域调研】:
- [PSN-IRT / "Lost in Benchmarks?" (arXiv:2505.15055)] (AAAI 2026 Oral): 直接前置工作。为11个benchmark共41,871个item提供4PL IRT参数。IRT-FIT的整个方法建立在此基础之上，但PSN-IRT本身未做person-fit方向的污染检测。
- [ConStat (arXiv:2405.16281)] (NeurIPS 2024): 最直接竞争者。同为黑盒方法，但需要生成rephrased items并重新测试模型，在Open LLM Leaderboard上发现Mistral/Llama/Yi等模型的高污染率(r²=0.94)。IRT-FIT的核心差异化在于不需要re-testing，可做retroactive audit。
- [Min-K%++ (arXiv:2404.02936)] (ICLR 2025 Spotlight): Token-level log-likelihood方法，需要gray-box access。代表了更高信息访问层级的检测方法。
- [CoDeC (arXiv:2510.27055)] (ICLR 2026): 基于ICL的污染检测，dataset-level方法。[Self-Critique (arXiv:2510.09259)] (ICLR 2026): 针对post-RL污染，通过entropy collapse检测，AUC提升30%。两者都需要模型内部信息。
- [Wang et al. (arXiv:2510.02386)]: 证明即使短暂GRPO训练也能隐藏MIA-based信号，对所有基于记忆的检测方法构成挑战。IRT-FIT的post-RL robustness实验直接回应此工作。
- [Benchmark Inflation (arXiv:2410.09247)]: 通过retro-holdout量化性能差距（TruthfulQA上达16pp）。需要构建新的holdout set并重新评估，不能完全retroactive。
- [Han et al.] (EACL 2026 Findings): 量化心理测量问卷中的LLM数据污染（item memorization, evaluation memorization, target score matching），但未使用person-fit统计量。这是最接近IRT+污染方向的工作，但切入点完全不同。
- [ATLAS (arXiv:2511.04689)] (AAAI 2027): IRT-based自适应测试，减少90%测试item。[MedIRT (arXiv:2509.24186)] (ICLR 2027): 医学benchmark上的2PL IRT。均为IRT在LLM评估中的应用，但与污染检测无关。
- [Silicon Bureaucracy (arXiv:2603.21636)] & [Cross-Context Verification (arXiv:2603.21454)] (2026 arXiv): 最新的benchmark污染检测工作，前者用perturbation-based audit，后者用session-isolated diversity analysis达到perfect separation。两者都需要re-testing。
- [Braeken & van Laar (2025, Educational and Psychological Measurement)]: 指出lz*在calibration sample包含misfit respondents时存在校准偏差。proposal已识别此风险并计划empirical null adjustment。
- [Sinharay (2017, JEBS)]: person-fit检测power在10-30% preknowledge时达到峰值的inverted-U形状。IRT-FIT直接继承并拓展此发现。

- **调研总结**: LLM benchmark污染检测是一个活跃且竞争激烈的领域，2024-2026年涌现了大量工作，覆盖了从gray-box（Min-K%++, CoDeC, Self-Critique）到black-box requiring re-testing（ConStat, Silicon Bureaucracy, CCV）的各个信息访问层级。然而，在"仅使用二值response pattern"这个最低信息层级上，确实没有任何现有工作。IRT-FIT占据了一个真实的空白位置——但这个位置的价值取决于其检测能力是否足够实用。

【整体印象】:
作为审稿人，我的第一反应是**倾向weak accept / borderline accept**。这是一篇定位非常清晰、写作极为成熟的proposal。它不试图声称"我们的方法beats everything"，而是严谨地定义了一个新的operating point（minimal-information level），并系统地探索该operating point的检测能力边界。这种"measurement science"的风格在EMNLP是被接受的。retroactive prevalence analysis作为独特的应用场景非常有说服力——确实没有其他方法能在不重新推理的情况下审计历史评估日志。

然而，核心担忧是：这篇工作的方法论贡献本质上是将教育测量学中已有的工具（lz*）直接应用到LLM评估这个新领域。跨领域迁移本身有价值，但reviewers可能会质疑技术深度不够——毕竟lz*的公式、理论性质、检测能力特征都是现成的。这与"提出新方法"有本质区别。

【核心贡献】:
1. **方法贡献**：首次将psychometric person-fit statistics（特别是lz*）应用于LLM benchmark污染检测，建立了一个新的信息-检测力前沿点（minimal-information operating point）。
2. **实证贡献**：对Open LLM Leaderboard进行首次大规模retroactive污染审计，利用现有评估日志而非新测试。
3. **理论贡献**：记录并论证binary-response-pattern方法的inverted-U检测力限制（proof sketch），为该类方法划定理论边界。

贡献的领域价值**中等偏上**：retroactive audit能力是genuinely useful的，因为大量历史评估数据已经存在但从未被用于污染检测。minimal-information framing为信息访问受限的场景（如API-only模型、已下线模型）提供了实际方案。但总体检测能力可能有限，限制了方法的独立价值（更可能作为complementary tool而非primary detection method）。

【方法合理性】:
方法本身是合理的——lz*在教育测量学中有数十年的理论和实证基础，"contaminated LLM ≈ examinee with item preknowledge"的类比在概念上站得住。4PL IRT model、MLE/EAP/WLE能力估计、Benjamini-Hochberg FDR控制——这些都是成熟的统计工具。

**更简单的替代方案？** Proposal自己设置了Tier 0 baselines（Accuracy-Z, Guttman Error Count, Difficulty-Residual Correlation）来回答这个问题。如果这些简单统计量能达到接近lz*的性能，那IRT machinery的marginal value就受质疑。这一点proposal处理得很好——直接做了ablation。

**潜在问题**：
(1) 对PSN-IRT参数质量的依赖：如果item parameters估计不准（特别是guessing parameter c和upper-asymptote d），整个方法的基础就不牢固。PSN-IRT的calibration sample本身可能包含contaminated models，导致circular dependency。
(2) Unidimensionality假设：MMLU是多维benchmark，在全benchmark级别计算lz*可能违反IRT假设。proposal计划做per-domain分析来缓解，但这会大幅减少每个分析的item数量，进而降低检测power。
(3) SFT泛化效应可能是fundamental limitation：如果fine-tuning on 20% items提升了整个domain的能力，response pattern看起来就像genuine high ability，person-fit根本无法区分。

【5 维度打分】:

1. **研究问题: 强** — Benchmark污染检测是LLM评估领域公认的重要问题（ConStat获NeurIPS 2024, Min-K%++获ICLR 2025 Spotlight），且"minimal-information operating point"这个切入角度确实是空白。"能否仅从binary response pattern检测污染？"是一个well-defined且有理论意义的问题。retroactive audit的需求是真实的——大量历史评估数据无法被现有方法利用。

2. **方法与创新: 中** — 跨领域迁移（psychometric person-fit → LLM evaluation）是有意义的，但核心方法lz*本身是1990s-2000s的教育测量学工具（Snijders 2001; Karabatsos 2003），proposal的技术贡献主要是"应用到新domain"而非"提出新方法"。与ConStat（提出了新的污染定义和检测统计量）、Self-Critique（发现并利用post-RL entropy collapse现象）、CoDeC（设计了ICL-based detection paradigm）相比，方法论创新深度较浅。inverted-U的"proof sketch"被描述为informal conjecture，理论贡献也有限。不过，minimal-information framing本身的conceptual contribution是有价值的。

3. **实验设计: 强** — 这是proposal最大的亮点之一。126 controlled conditions × 3 seeds，access-level stratified baselines（Tier 0/1/2三层对比），3种item sampling策略的ablation，IRT模型复杂度ablation（2PL→3PL→4PL），4种person-fit统计量对比，3种ability estimation方法对比，post-RL robustness test跟踪RL steps，simulation-based power analysis覆盖多种test length和contamination fraction——这比该领域大多数论文（包括ConStat和Min-K%++）的实验设计都更加thorough。特别是Tier 0 baselines直接回答了"IRT是否比简单统计量更好"这个根本问题，显示出深度思考。对PSN-IRT calibration bias的empirical verification也很周到。

4. **可行性: 强** — ~2,500 H100-hours在当前学术界标准下完全可行（一个lab allocation一周内可完成）。QLoRA contamination protocol是标准的。主要依赖项（PSN-IRT 4PL parameters, Open LLM Leaderboard response logs, lm-evaluation-harness）都是公开可用的。IRT-FIT本身的计算（person-fit statistics）几乎是CPU-only的。唯一风险点是Open LLM Leaderboard的per-item response logs是否完整可获取。

5. **写作与呈现: 强** — Proposal写作极其清晰和专业。问题定义精确，related work覆盖全面且stratified by access level，实验设计结构化程度很高，expected outcomes诚实（明确承认aggregate AUROC可能低于gray-box方法），limitations讨论坦率（SFT generalization, pretraining exposure out-of-scope）。唯一小问题是sections有些偏长，可能需要在实际论文中压缩。

【概率估计】: [30% - 42%] 中位 36%

【估计理由】:
**推高因素**: (1) 研究问题重要且切入角度genuinely novel（minimal-information operating point无人占据）；(2) 实验设计非常comprehensive，超越了该领域多数已发表工作的标准；(3) retroactive prevalence analysis提供了独特且实际有用的应用场景；(4) 写作成熟、honest about limitations，审稿体验好；(5) IRT在LLM评估中的应用正成为趋势（PSN-IRT AAAI 2026 Oral, ATLAS, MedIRT），时机合适。

**压低因素**: (1) 核心方法论创新深度不足——lz*是现成工具，跨领域应用虽有价值但在top venue可能被视为incremental；(2) inverted-U检测力限制意味着方法仅在10-30%污染率窗口内有效，实际应用范围受限；(3) SFT generalization可能是fundamental limitation，如果实验结果显示generalization严重smooths aberrance signal，则方法价值大打折扣；(4) 不能检测pretraining exposure（最常见的污染形式），限制了声明的通用性；(5) 污染检测领域竞争激烈（2024-2026每年多篇顶会），reviewer可能对"又一个检测方法"审美疲劳；(6) inverted-U的"proof sketch"是informal conjecture而非formal proof，理论贡献打折扣。

综合来看，这是一篇well-executed的proposal，方向正确、实验扎实、定位清晰，但方法论创新深度不足以让它成为strong accept。在EMNLP 2026的竞争环境下，它处于borderline位置——大概率进入讨论区，最终结果取决于reviewer是否认可"minimal-information characterization + retroactive audit capability"的组合价值。

【主要风险】:
1. **方法论创新深度不足被reviewer质疑**: Reviewer可能认为"将教育测量学的lz*应用到LLM评估"是straightforward application而非methodological contribution，特别是当lz*的所有理论性质（包括inverted-U）都已在psychometrics文献中建立。如果2/3的reviewers持此看法，论文可能获得"interesting application but limited novelty"的评价。
2. **检测能力不足以justify the paper**: 如果实验结果显示(a) lz*相比Tier 0 naive baselines的marginal gain很小，或(b) SFT generalization严重削弱检测力，或(c) post-RL之后信号完全消失——那么paper的实证价值会大幅降低。inverted-U意味着该方法根本无法检测最高风险的场景（大规模污染），这在reviewer眼中可能是dealbreaker。

【实施评估】:
  - 计算资源: ~2,500 H100-hours，约等于$5,000-7,500 cloud cost，对学术lab完全可行
  - 数据需求: PSN-IRT 4PL参数（公开）、Open LLM Leaderboard per-item response logs（部分公开，需确认完整性）、6个benchmark数据集（均公开）
  - 人工介入: 低。QLoRA fine-tuning和person-fit计算均可自动化。Post-RL实验需要careful tuning但属于标准工程。
  - 训练需求: 需要训练126+ contaminated models（QLoRA）+ 9 full-parameter SFT + post-RL GRPO，但每个都是标准fine-tuning任务
  - 新 Benchmark: 不需要构建新benchmark；使用现有benchmark + PSN-IRT参数
  - 预估周期: 3-4个月（1个月搭建pipeline + 1.5个月运行实验 + 1个月分析写作），假设GPU资源充足
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)
- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)
- [Min-K%++ (ICLR 2025)](https://arxiv.org/abs/2404.02936)
- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/abs/2510.27055)
- [Self-Critique: Detecting Contamination from RL Post-training (ICLR 2026)](https://arxiv.org/abs/2510.09259)
- [Wang et al.: Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts](https://arxiv.org/abs/2410.09247)
- [Han et al.: Quantifying Data Contamination in Psychometric Evaluations (EACL 2026 Findings)](https://aclanthology.org/2026.findings-eacl.319/)
- [ATLAS: Adaptive Testing for LLM Evaluation (AAAI 2027)](https://arxiv.org/abs/2511.04689)
- [MedIRT: Measuring Competency Across Medical Benchmarks](https://arxiv.org/abs/2509.24186)
- [Silicon Bureaucracy (arXiv 2026)](https://arxiv.org/abs/2603.21636)
- [Cross-Context Verification (arXiv 2026)](https://arxiv.org/abs/2603.21454)
- [Braeken & van Laar (2025): Reducing Calibration Bias for Person Fit Assessment](https://journals.sagepub.com/doi/10.1177/00131644251364252)
- [Comprehensive Survey of Contamination Detection Methods](https://arxiv.org/abs/2404.00699)
- [Benchmarking LLMs Under Data Contamination: Static to Dynamic Evaluation](https://arxiv.org/abs/2502.17521)


【原始 proposal（允许参考但不是主要依据）】:
## IRT-FIT: Detecting Benchmark Contamination in LLMs at the Minimal-Information Operating Point via Psychometric Person-Fit Statistics

## 1. Problem Statement

Benchmark contamination—where LLMs are trained on evaluation data—undermines the reliability of capability assessments. As benchmarks proliferate and training corpora grow opaque, robust contamination detection is critical for evaluation integrity. Existing detection methods operate at various levels of model access: token-level probabilities (Min-K%++, ICLR 2025 Spotlight; CoDeC, arXiv:2510.27055, ICLR 2026), entropy sequences (Self-Critique, arXiv:2510.09259, ICLR 2026), confidence scores (PaCoST, EMNLP 2024 Findings, arXiv:2406.18326), guided instruction completion (Time Travel in LLMs, Golchin & Surdeanu, ICLR 2024), or the ability to re-administer modified benchmark items (ConStat, NeurIPS 2024, arXiv:2405.16281; Silicon Bureaucracy, arXiv:2603.21636; Cross-Context Verification, arXiv:2603.21454). All require information beyond what is minimally available in a standard evaluation: the binary (correct/incorrect) response pattern.

This paper asks a foundational question: **what is the detection power envelope when operating at the minimal-information level—binary response patterns alone?** We propose IRT-FIT, which applies psychometric person-fit statistics to LLM benchmark evaluation, establishing a new operating point on the information-access vs. detection-power frontier. By leveraging calibrated Item Response Theory (IRT) parameters, IRT-FIT detects aberrant response patterns indicative of item-level memorization contamination, without requiring any model internals, re-testing, or additional inference.

## 2. Core Contributions

1. **Minimal-information contamination detection.** IRT-FIT is the first method that detects benchmark contamination using only binary response patterns and pre-calibrated item parameters—the lowest possible information access level. It complements gray-box methods requiring model internals (CoDeC, Self-Critique, Min-K%++) and re-administration methods requiring new test items (ConStat, Silicon Bureaucracy, CCV). Crucially, we demonstrate that lz* captures item-level response pattern structure (the joint likelihood of the specific correct/incorrect combination given ability) that simple aggregate statistics (accuracy anomaly, Guttman error count) cannot exploit, justifying the IRT machinery.

2. **Retroactive contamination prevalence analysis.** Because IRT-FIT requires only binary response patterns already recorded in evaluation logs, it enables systematic historical audit of contamination prevalence—analyzing how contamination rates on public leaderboards have evolved over time. No other method can perform this retroactive analysis: gray-box methods require live model access; ConStat requires re-testing on rephrased items; Benchmark Inflation (arXiv:2410.09247) requires constructing benchmark-specific holdout sets. We apply IRT-FIT to all models with available per-item response records on the Open LLM Leaderboard, producing the first large-scale contamination prevalence timeline.

3. **Characterization of detection limits for response-pattern methods.** We document an inverted-U detection power curve and provide an informal proof sketch for its two endpoints: at contamination fraction → 0%, the aberrance signal is submerged below the noise floor of finite-item statistical tests (power → 0 by standard hypothesis testing limits); at contamination fraction → 100%, uniform high performance is indistinguishable from genuine high ability since binary response patterns carry no information to separate the two (identifiability collapse). Between these endpoints, detection power peaks at 10–30% contamination. We conjecture this inverted-U characterizes a general limit of all binary-response-pattern-based detection methods, extending prior observations in educational testing (Sinharay, 2017, JEBS).

4. **Cross-domain methodological transfer.** We bridge psychometric testing theory—specifically person-fit analysis for detecting cheating examinees (Sinharay, 2017, JEBS; Karabatsos, 2003; Gorney et al., 2023)—to LLM evaluation, demonstrating that the analogy "contaminated LLM ≈ examinee with item preknowledge" is operationally productive.

## 3. Scope and Assumptions

**Detection scope.** IRT-FIT targets **item-level memorization contamination**—where an LLM has been fine-tuned on or memorized specific benchmark question-answer pairs, producing an aberrant pattern of correct responses deviating from IRT model predictions. This corresponds to SFT/data-leakage contamination pathways.

**SFT generalization effect.** The core analogy "contaminated LLM ≈ examinee with item preknowledge" assumes contamination produces item-specific performance gains. However, SFT on a subset of benchmark items may produce partial generalization to semantically related non-trained items—smoothing the aberrance signal. For example, fine-tuning on 20% of MMLU biology questions may improve performance on the remaining 80% of biology questions. This generalization radius, if large, weakens person-fit detection power by making the response pattern more consistent with genuine high ability. Our experimental design directly tests this: the hard-item-only contamination condition (Section 6.1) is motivated by the expectation that hard items have smaller generalization radii, and per-domain analysis (Section 6.4) controls for within-domain generalization.

**Out of scope.** Distributional pretraining exposure—where benchmark content appears amidst massive pretraining corpora producing smooth, generalizable ability improvement—will not generate item-specific aberrance. This limitation is shared by all response-pattern-based methods. Wang et al. (arXiv:2510.02386) distinguish Stage I (pretraining/SFT) and Stage II (post-RL) contamination; our experiments simulate both.

## 4. Method

**4.1 IRT Parameterization.** We use 4PL IRT parameters (discrimination a, difficulty b, guessing c, upper asymptote d) calibrated by PSN-IRT ("Lost in Benchmarks?", AAAI 2026 Oral, arXiv:2505.15055), covering 41,871 items across 11 benchmarks. The 4PL model predicts:

P(X_j=1|θ) = c_j + (d_j − c_j) / (1 + exp(−a_j(θ − b_j)))

**4.2 Person-Fit Statistic (lz*).** For each model, we compute the standardized log-likelihood person-fit statistic lz* (Snijders, 2001; Sinharay, 2017):

l_z* = [Σ_j (x_j log p_j + (1−x_j) log(1−p_j)) − E[l|θ̂]] / √Var[l|θ̂]

where p_j = P(X_j=1|θ̂). Under the null (no aberrance), lz* ~ N(0,1). Significantly negative lz* indicates response patterns inconsistent with the IRT model—the signature of item preknowledge.

**Why lz* over simple statistics.** Unlike aggregate measures (accuracy z-score, Guttman error count), lz* evaluates the joint likelihood of the full item-response vector given estimated ability, capturing complex aberrance patterns (e.g., failing easy items while acing specific hard items) that difficulty-stratified statistics miss. This distinction is empirically validated in our ablation (Section 6.4) and theoretically grounded in the person-fit literature (Karabatsos, 2003).

**Calibration considerations.** Braeken & van Laar (2025) note that lz* can exhibit calibration bias when IRT parameters are estimated on data containing misfitting respondents. Since PSN-IRT calibrates on LLM responses that may include contaminated models, we verify lz* calibration empirically (Section 7) and provide an empirical null adjustment if the N(0,1) assumption is violated.

**4.3 Detection Pipeline.**
1. Retrieve pre-calibrated 4PL item parameters from PSN-IRT for target benchmark.
2. Obtain binary response pattern for target LLM—from existing evaluation logs or new evaluation.
3. Estimate model ability θ̂ via maximum likelihood.
4. Compute lz* and derive p-value under N(0,1) or empirical null.
5. For single-model testing: flag if p < α. For multi-model audit: apply Benjamini-Hochberg FDR control.

## 5. Related Work

**Contamination detection requiring model internals (gray-box).** Min-K%++ (ICLR 2025 Spotlight) thresholds token-level log-likelihoods. CoDeC (arXiv:2510.27055, ICLR 2026) uses in-context learning to compare confidence on seen vs. unseen data. Self-Critique (arXiv:2510.09259, ICLR 2026) detects post-RL contamination via entropy-sequence policy collapse (~30% AUC improvement). PaCoST (EMNLP 2024 Findings, arXiv:2406.18326) compares confidence on original vs. perturbed items. Time Travel in LLMs (Golchin & Surdeanu, ICLR 2024) uses guided instruction to reconstruct benchmark instances.

**Contamination detection from external probing.** ConStat (NeurIPS 2024, arXiv:2405.16281) detects non-generalizing performance inflation via comparison with rephrased/synthetic reference benchmarks (r²=0.94 with ground-truth). Silicon Bureaucracy (arXiv:2603.21636) uses perturbation-based score credibility audit. Cross-Context Verification (arXiv:2603.21454) achieves perfect separation via session-isolated diversity analysis.

**Retroactive contamination analysis.** Benchmark Inflation (arXiv:2410.09247) constructs retro-holdout datasets to quantify performance gaps (up to 16pp on TruthfulQA). Key difference from IRT-FIT: retro-holdouts require constructing new benchmark-specific holdout sets and re-evaluating models, while IRT-FIT operates on existing response patterns with no new data generation or model inference.

**Key differentiation from ConStat.** Both ConStat and IRT-FIT operate without model internals. However, ConStat requires (a) generating semantically equivalent rephrased items, (b) re-administering benchmarks to each model, and (c) reference model comparison. IRT-FIT requires none of these—only existing binary response patterns and pre-calibrated IRT parameters—enabling retroactive audit where re-testing is impossible.

**Post-RL contamination robustness.** Wang et al. (arXiv:2510.02386) demonstrate that even brief GRPO training conceals MIA-based signals. Our post-RL experiments test whether response-pattern-level signals exhibit different robustness properties than model-internal signals.

**IRT for LLM evaluation.** PSN-IRT (AAAI 2026 Oral, arXiv:2505.15055) calibrated 4PL parameters for 41,871 items across 11 benchmarks. ATLAS (arXiv:2511.04689, AAAI 2027) introduces IRT-based adaptive testing, reducing items by 90% while maintaining precision and showing 23–31% rank reordering. MedIRT (arXiv:2509.24186, ICLR 2027) applies 2PL IRT per topic to 80 LLMs on medical benchmarks. "Lifting the Benchmark Iceberg with Item-Response Theory" (ICLR 2024) reveals how hidden implementation choices affect rankings and proposes IRT for transparent measurement. Han et al. (EACL 2026 Findings) quantify contamination in psychometric questionnaires but do not employ person-fit statistics. None connect IRT to contamination detection via person-fit.

**Person-fit in educational testing.** Person-fit statistics have extensive foundations (Karabatsos, 2003; Sinharay, 2017, JEBS; Gorney et al., 2023). Sinharay (2017) establishes lz* detection power peaks at 10–30% preknowledge with inverted-U shape. Braeken & van Laar (2025) identify calibration bias in lz* from contaminated calibration samples. Tendeiro et al. (2023) propose iterative scale purification improving Type-I error control. We transfer these tools to LLM evaluation, addressing calibration concerns via empirical null adjustment.

## 6. Experimental Design

**6.1 Controlled Contamination Experiment**

**Models.** Llama 4 Scout (109B MoE), Gemma 4 27B, Qwen 3.5-9B—spanning MoE and dense architectures at different scales.

**Benchmarks.** Six from PSN-IRT's calibrated set: MMLU (large, multi-domain), ARC-Challenge (science reasoning), HellaSwag (commonsense), WinoGrande (coreference), TruthfulQA (~817 items), HumanEval (~164 items). Selection provides test-length variation for power analysis.

**Contamination protocol.** QLoRA fine-tuning on fraction f ∈ {0%, 5%, 10%, 20%, 30%, 50%, 100%} of benchmark items, producing 3 models × 6 benchmarks × 7 levels = 126 conditions, each with 3 random seeds. Additionally, full-parameter SFT on Qwen 3.5-9B at f ∈ {10%, 20%, 50%} to validate QLoRA as contamination proxy (9 additional conditions × 3 seeds).

**Item sampling strategy ablation.** Three strategies per contamination fraction:
- Random uniform sampling
- Hard-item-only (top 30% by IRT difficulty b)—primary condition (most realistic: easy items are answerable without memorization)
- Stratified (proportional to difficulty distribution)

**6.2 Baselines (Access-Level Stratified)**

**Tier 0 — Naive response-pattern baselines (same operating point as IRT-FIT):**
- **Accuracy-Z**: z-score of target model's accuracy relative to models in the same ability band
- **Guttman Error Count**: number of item pairs violating difficulty ordering (Karabatsos, 2003)
- **Difficulty-Residual Correlation**: correlation between item-level residuals and IRT difficulty b (contaminated models should show positive residual on high-difficulty items)

These baselines use the same information as IRT-FIT (binary responses + IRT parameters) but without the full person-fit statistical framework, directly testing whether lz*'s joint-likelihood approach provides marginal value over simpler aggregate statistics.

**Tier 1 — Black-box requiring re-testing:**
- ConStat (NeurIPS 2024, arXiv:2405.16281) — rephrased benchmark comparison

**Tier 2 — Gray-box (token-level access):**
- Min-K%++ (ICLR 2025 Spotlight)
- CoDeC (arXiv:2510.27055, ICLR 2026)
- Self-Critique (arXiv:2510.09259, ICLR 2026)
- PaCoST (EMNLP 2024 Findings, arXiv:2406.18326)

Primary evaluation: IRT-FIT vs. Tier 0 (does IRT machinery add value?) and vs. Tier 1 (does avoiding re-testing sacrifice detection power?). Secondary: cross-tier comparison with gray-box methods.

**6.3 Post-RL Robustness Test**

On **two models** (Qwen 3.5-9B and Gemma 4 27B):
- **Stage 1**: SFT contamination at 20% and 50% fractions
- **Stage 2a** (Clean RL): GRPO on non-benchmark data (reward = outcome correctness on held-out problems)
- **Stage 2b** (Contaminated RL): GRPO where benchmark items appear in RL data
- **GRPO configuration**: Following Wang et al. (arXiv:2510.02386) for comparability; detection power reported at checkpoints {100, 500, 1000, 2000, 5000} RL steps
- **Comparison**: IRT-FIT trajectory vs. MIA-based methods (Min-K%++, Self-Critique) across RL training steps

**6.4 Ablation Studies**

- **IRT model complexity**: 2PL (c=0, d=1) → 3PL (d=1) → 4PL, quantifying marginal contribution of guessing and upper-asymptote parameters. Parameter sets derived from PSN-IRT (arXiv:2505.15055).
- **Person-fit statistics**: lz* vs. U3, W, Ht (Karabatsos, 2003)
- **Ability estimation**: MLE vs. EAP vs. WLE for θ̂
- **IRT parameter source**: PSN-IRT 4PL parameters vs. conventionally calibrated parameters (mirt R package on same response data), testing sensitivity to parameter estimation method
- **Unidimensionality diagnostic**: For multi-domain benchmarks (MMLU), compare full-benchmark lz* vs. per-subject-domain lz*, testing whether domain-level analysis reduces false positives from multidimensionality (Braeken & van Laar, 2025)

**6.5 Power Analysis and Detection Limits**

- **Simulation study**: Synthetic response patterns under 4PL at varying ability levels, test lengths {50, 164, 500, 817, 1000, 5000}, contamination fractions {0%, 3%, 5%, 10%, 20%, 30%, 50%, 100%}, 10,000 replications per condition.
- **Test length analysis**: Minimum items for reliable detection per contamination fraction. Per-benchmark expected power.
- **Inverted-U documentation with proof sketch**: Plot detection power curve; provide informal argument for endpoint impossibility (noise floor at low contamination; identifiability collapse at high contamination).

## 7. Evaluation Metrics

- **AUROC/AUPRC**: Aggregate and per-contamination-level discrimination
- **Per-contamination-level power**: P(reject H₀ | H₁) at α=0.05—core inverted-U visualization
- **Type-I error calibration**: Empirical FPR at α ∈ {0.01, 0.05, 0.10} on clean models; Q-Q plot of lz* under null to verify N(0,1) assumption; if violated, report empirical null parameters and adjusted detection power
- **Benjamini-Hochberg FDR**: Applied to multi-model audit scenarios; report FDR-controlled detection rates at q ∈ {0.05, 0.10, 0.20}

## 8. Contamination Prevalence Analysis

**Systematic historical audit.** Apply IRT-FIT to all models on the Open LLM Leaderboard with available per-item response logs (via lm-evaluation-harness output or reproducible re-evaluation of open-weight models). Produce: (a) per-benchmark contamination prevalence over time (fraction of models flagged at FDR=0.10); (b) contamination severity distribution (lz* score distribution across models); (c) trend analysis (has contamination prevalence increased with leaderboard competition?).

**Convergent validation.** Compare IRT-FIT flagging with ConStat's published findings on Mistral, Llama, Yi, and top-3 Open LLM Leaderboard models (ConStat, NeurIPS 2024).

**Known-clean negative controls.** Verify IRT-FIT does not flag OLMo models (AI2), whose training data (Dolma) is fully open and auditable via OlmoTrace, providing false-positive control in the wild.

**Limitations.** Convergent validation cannot establish ground truth (two methods may share systematic biases). The controlled experiment (Section 6.1) remains the primary validation; the prevalence analysis is positioned as an illustrative application demonstrating IRT-FIT's unique retroactive capability.

## 9. Compute Estimates

- **Controlled contamination (QLoRA)**: 126 conditions × 3 item strategies × 3 seeds × ~1.5h avg ≈ 1,700 H100-hours
- **Full-parameter SFT (Qwen 9B)**: 9 conditions × 3 seeds × ~2h ≈ 54 H100-hours
- **Post-RL (2 models)**: ~350 H100-hours
- **Inference for prevalence analysis**: Minimal (per-item response collection for open-weight models + CPU-only person-fit computation)
- **Hardware per model**: Llama 4 Scout QLoRA: 1× H100 (~71GB via Unsloth); Gemma 4 27B QLoRA: 1× H100 (~30GB); Qwen 3.5-9B: 1× A100 40GB
- **Total**: ~2,500 H100 GPU-hours

## 10. Expected Outcomes

We expect: (a) lz* outperforms Tier 0 naive baselines (Accuracy-Z, Guttman errors, Difficulty-Residual) by capturing joint response-pattern structure, empirically justifying the IRT person-fit framework; (b) competitive performance with ConStat in Tier 1, with the advantage of no re-testing; (c) aggregate AUROC possibly below gray-box methods—an expected consequence of minimal information access; (d) inverted-U detection power confirmed with peak at 10–30%; (e) partial post-RL robustness, with response-pattern signals degrading differently from internal signals; (f) the historical prevalence analysis revealing contamination trends across leaderboard history, demonstrating IRT-FIT's unique retroactive capability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d6418e9f-b353-4c8a-8843-8561b371ae73",
  "type": "user",
  "uuid": "5c958979-7480-4a09-a137-29b5e1334594",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:31:53.501Z_

```json
{
  "parentUuid": "5c958979-7480-4a09-a137-29b5e1334594",
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
  "uuid": "8e144f47-b943-4b48-91aa-36fbff5e6a36",
  "timestamp": "2026-05-20T05:31:53.501Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:31:53.501Z_

```json
{
  "parentUuid": "8e144f47-b943-4b48-91aa-36fbff5e6a36",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a026fdcc-eb91-4c27-9c6d-aebf87ad2b27",
  "timestamp": "2026-05-20T05:31:53.501Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient context to produce my evaluation. Let me…",
  "leafUuid": "a026fdcc-eb91-4c27-9c6d-aebf87ad2b27",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection for LLM benchmark contamination",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:32:19.342Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews of this proposal (IRT-FIT) and produce a Meta Judge synthesis.

First, let me extract the key numbers and judgments:

**Reviewer 1:**
- Probability: [30% - 48%] 中位 38%
- Research Question: 强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中
- Writing: 强


**Reviewer 2:**
- Probability: [30% - 42%] 中位 36%
- Research Question: 强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 中
- Writing: 强

**Reviewer 3:**
- Probability: [30% - 42%] 中位 36%
- Research Question: 强
- Method & Innovation: 中
- Experimental Design: 强
- Feasibility: 强
- Writing: 强

Looking at the three median probabilities—38%, 36%, and 36%—the mean comes to about 36.67% with a median of 36% and very tight standard deviation around 1.15%, showing remarkable consensus across reviewers.

All three reviewers align on the core dimensions: strong research question and experimental design, moderate methodological innovation, and strong writing quality. There's near-consensus on feasibility too. But they're all flagging the same critical concerns—the method is primarily a cross-domain application rather than a novel contribution, baseline models might perform comparably, the SFT generalization limitation is fundamental, the inverted-U relationship constrains practical use, and there's potential calibration bias in the PSN-IRT approach.

The reviewers converge on what makes this work solid: it addresses a genuine gap with clean framing, the experimental design is rigorous, the retroactive audit capability is genuinely novel, and the writing is honest about limitations. Where they diverge slightly is on optimism—Reviewer 1 estimates the upper bound at 48% while the other two cluster around 42%, and Reviewer 3 rates feasibility as strong while the others see it as moderate.

The consistency across medians is remarkably tight, clustering around 36-38% with a standard deviation under 1.15%, so I should anchor to that narrow range.

Looking at the bounds: the lower end is unanimous at 30%, but the upper bounds spread from 42% to 48%, with Reviewer 1 being the outlier. Given the constraint that my final range shouldn't exceed the most generous reviewer's estimate, I'll set the interval at 30-44% with a median of 37%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a026fdcc-eb91-4c27-9c6d-aebf87ad2b27",
  "isSidechain": false,
  "requestId": "req_011CbDGoLvdViA95aGxP5H4M",
  "type": "assistant",
  "uuid": "eaccfe2c-6fff-4157-a978-0a4e44afdef6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018V8BP73P9XHBxGK9Qa66oU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20530,
      "cache_read_input_tokens": 16908,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2748,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 20530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20530
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

_source line 9 · 2026-05-20T05:32:57.601Z_

【阶段】: Meta Judge
【三次中位】: [38%, 36%, 36%]  std=1.15%
【共识维度】:
- 研究问题: 强（3/3 一致）— 填补 minimal-information operating point 的真实空白，retroactive audit 需求真实存在
- 方法与创新: 中（3/3 一致）— lz* 是教育测量学成熟工具的跨领域迁移，非方法论发明；与 ConStat（新定义+新统计检验）、CoDeC（新 ICL paradigm）相比创新深度较浅
- 实验设计: 强（3/3 一致）— 126 conditions × 3 seeds、access-level stratified baselines（Tier 0/1/2）、Tier 0 直接检验 IRT 边际价值的设计被三人共同高度评价
- 写作与呈现: 强（3/3 一致）— 定位清晰、intellectual honesty、不过度 claim
- 可行性: 中（2/3）/ 强（1/3）— 近共识，R3 略乐观
- 核心风险 1: 方法 novelty 不足以支撑主会（3/3 均提及，最大拒稿风险）
- 核心风险 2: Tier 0 baselines 表现接近 lz* 将釜底抽薪（3/3 均提及）
- 核心风险 3: SFT generalization 是 fundamental limitation（3/3 均提及）
- 核心风险 4: inverted-U 限制实际可用检测窗口（3/3 均提及）
- 核心风险 5: PSN-IRT calibration bias / circular dependency（3/3 均提及）
【异常维度】:
- R1 上界 48% 显著高于 R2/R3 的 42%，R1 对"IRT for LLM evaluation 上升趋势"的时机加权更大 — 属于合理乐观但为 outlier，降权处理
- R3 可行性评"强"，R1/R2 评"中"— R3 对 Open LLM Leaderboard 数据可获取性和工程量的评估更乐观，鉴于 per-item response logs 可获取性确实存在不确定性，采纳 R1/R2 的"中"更稳健
【最终概率】: [30% - 43%] 中位 37%
【一致性】: 高（std=1.15% < 3%，三人在所有 5 个 rubric 维度上判决高度一致）
【综合理由】:
三位审稿人对该 proposal 的评估呈现罕见的高度一致：研究问题强、实验设计强、写作强，但方法创新"中"是三人共同识别的天花板。这意味着该 proposal 的命运高度依赖于实验结果——如果 lz* 显著超越 Tier 0 baselines 且 prevalence analysis 揭示有价值的 trend，可推至上界附近；如果 Tier 0 表现接近或 SFT generalization 严重削弱信号，则回落到下界。

中位取 37%（三人中位的均值 36.67% 四舍五入）。上界从 R1 的 48% 收窄至 43%：R1 的额外乐观主要来自"IRT 趋势"时机因素，但这不改变方法创新深度的硬约束，且 R2/R3 均止步于 42%。下界 30% 三人完全一致，保留不动。

该 proposal 本质上是一篇"well-positioned characterization paper with excellent experimental design but limited methodological depth"——在 EMNLP 2026 的竞争环境下处于 borderline 位置。最终 accept/reject 大概率取决于 reviewer panel 对"cross-domain transfer as contribution"的接受度以及实验结果的说服力。

【建议】: 边缘（borderline，中位 37% 略高于 36% 阈值，但 idea novelty 天花板限制了上升空间，建议进入迭代优化）

【实施评估】:
  - 计算资源: ~2,500 H100-hours（约 $5,000-7,500 spot pricing），需 2-4× H100/A100 并行，中等规模实验室 1-2 周可完成主体实验。三人一致认为计算量可控。
  - 数据需求: PSN-IRT 4PL 参数（已公开）；6 个 benchmark 数据集（全部公开）；Open LLM Leaderboard per-item response logs（**主要数据风险**——三人均提到可获取性不确定，部分模型可能只有聚合分数而无 item-level 记录，prevalence analysis 规模可能受限）
  - 人工介入: 中等。405 次 fine-tuning 运行的 pipeline 搭建与质量控制、ConStat 等 baseline 复现、leaderboard 数据收集清洗需要扎实的工程基础设施。（R3 评估偏乐观，采纳 R1/R2 的"中等"判断更稳健）
  - 训练需求: 需要。126 QLoRA 条件 × 3 seeds = 378 次 + 9 full-parameter SFT × 3 seeds = 27 次 + post-RL GRPO 运行。每次运行规模较小（9B-27B QLoRA），但总工程量不小
  - 新 Benchmark: 不需要。使用 PSN-IRT 已校准的 6 个现有 benchmark
  - 预估周期: 3-5 个月（1 个月搭建 pipeline + 1.5 个月运行实验 + 1-1.5 个月分析和论文撰写），假设 GPU 资源充足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaccfe2c-6fff-4157-a978-0a4e44afdef6",
  "isSidechain": false,
  "requestId": "req_011CbDGoLvdViA95aGxP5H4M",
  "type": "assistant",
  "uuid": "6941757b-b46a-422c-94fd-b0ab18f1d92f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018V8BP73P9XHBxGK9Qa66oU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20530,
      "cache_read_input_tokens": 16908,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2748,
          "cache_read_input_tokens": 16908,
          "cache_creation_input_tokens": 20530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20530
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient context to produce my evaluation. Let me…",
  "leafUuid": "6941757b-b46a-422c-94fd-b0ab18f1d92f",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT person-fit detection for LLM benchmark contamination",
  "sessionId": "3a1631e0-edd6-4014-a2f5-01e4f0e1f45d"
}
```

---
