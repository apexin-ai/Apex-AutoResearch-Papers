# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1.jsonl`
- **Structured JSON:** [`92c81516d893a627a287.json`](../../sessions/92/92c81516d893a627a287.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:29:55.726Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:29:55.726Z",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough research to do a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- SteerRM (arXiv 2603.12795, 2026): 首个 training-free 的 SAE-based reward model debiasing 方法。在 pretrained base-model 的 SAE 上识别偏差特征并在推理时抑制。在 RM-Bench Hard-split 上平均提升 7.3 分。与本 proposal 直接竞争——proposal 明确提出要对比 SteerRM 的 pretrained SAE 路线 vs. 自己从头在 PRM activations 上训练 SAE。\n- Basu et al., \"Interpretability without actionability\" (arXiv 2603.18353, 2026): 发现 clinical LM 在内部表征上近乎完美地编码了任务知识，但 mechanistic intervention 仍无法纠正输出错误。本 proposal 将此作为\"失败案例\"与 PRM\"成功案例\"做对比。\n- Orgad et al., \"Interpretability Can Be Actionable\" (arXiv 2605.11161, ICML 2026): 提出 mechanistic interpretability 的 actionability 评估框架（faithfulness、generalization、specificity）。本 proposal 将其作为评估标准之一。\n- Lee et al., \"The Story is Not the Science\" (arXiv 2602.18458, 2026): 提出 execution-grounded evaluation framework (MechEvalAgent)，强调方法论严谨性。本 proposal 引用为另一套评估标准。\n- CIRM, \"Debiasing Reward Models via Causally Motivated Inference-Time Intervention\" (arXiv 2604.27495, 2026): neuron-level 的 causal intervention debiasing reward model 方法，识别 bias-specific neurons 并在推理时替换 activations。本 proposal 将其作为 neuron-level intervention baseline。\n- SARM, \"Interpretable Reward Model via Sparse Autoencoder\" (arXiv 2508.08746, 2025): 将 pretrained SAE 集成到 reward model 架构中，实现 feature-level reward attribution。Proposal 未引用此工作，但高度相关。\n- SAFER (arXiv 2507.00665, 2025): 用 SAE 探测 reward model 中的 safety 相关 features。同样高度相关但未被引用。\n- CART, \"Circuit-Aware Reward Training\" (arXiv 2509.24713, 2025): 利用 circuit analysis 指导 reward model 训练中的 data augmentation 和 regularization。Proposal 未引用。\n\n调研总结: 2025-2026 年，SAE-based reward model 分析已形成一个活跃的子领域（SteerRM、SARM、SAFER、CIRM），方法涵盖 feature-level 到 neuron-level。同时，\"when does mech interp actually work?\" 这一元问题由 Orgad et al. 和 Basu et al. 从不同角度提出。本 proposal 试图将二者结合——用 PRM 作为 testbed 做 multi-granularity 比较，并提出 \"Domain Amenability Hypothesis\" 来解释成功/失败的条件。但该子领域已较为拥挤，多个直接竞争工作存在。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. **文献综述式验证**: \"Domain Amenability Hypothesis\" 的核心检验是 PRM（成功）vs. clinical LM（失败，来自 Basu et al.）。这实质是一个 N=2 的 cross-domain 比较。一个更简单的方法是：直接收集已发表论文中 mechanistic intervention 的成功/失败案例，做 meta-analysis，总结出 domain 条件——无需任何新实验。这种 survey+meta-analysis 的方式成本远低于本 proposal 的全套实验，且 N 更大。\n2. **直接扩展 SteerRM**: SteerRM 已经在 reward model 上做了 SAE-based feature-level intervention 且证明有效。如果目标只是验证 \"PRM 上 mechanistic intervention 可以 work\"，SteerRM 已经给出了答案。本 proposal 的增量在于 (a) 从头训练 SAE 而非用 pretrained SAE，(b) 多粒度比较，(c) Domain Amenability 的理论化。其中 (a) 是方法变体而非质的飞跃，(b) 是工程完备性，(c) 因 N=2 而说服力不足。\n3. **更好的 PRM 训练数据**: 如果核心问题是 \"PRM 把 fluency 和 correctness 混淆\"，一个更直接的解决方案是改进 PRM 的训练数据（如使用更干净的 step-level annotations），而非后期做 mechanistic intervention。\n\n增量价值: 主要在于提供了一个系统的 multi-granularity 比较框架，以及尝试将零散的成功/失败案例理论化。但这种增量是 \"组织性\" 的而非 \"洞察性\" 的。\n\n【前提假设检验】:\n核心 claim 的逻辑链有多个未验证环节：\n1. **\"Domain Amenability\" 四条件的充分/必要性未建立**: Proposal 提出 well-defined output semantics、constrained output structure、verifiable ground truth、independently testable specificity 是成功条件。但这四条不是从理论推导出来的，也不是从大量实证中归纳出来的——它们是根据 PRM 的特性 post-hoc 提出的。如果 PRM 上 intervention 碰巧失败了，作者可能会提出另一套条件。这是一种 \"先射箭后画靶\" 的论证。\n2. **PRM 成功 vs. Clinical LM 失败的归因假设**: Proposal 假设二者的差异可以归因于 domain 特性差异。但实际上，Basu et al. 的失败可能源于模型规模、训练数据质量、任务复杂度、模型架构等多种混淆因素——而非 domain amenability。N=2 且两个 case 之间有无数混淆变量，无法支持 causal claim。\n3. **\"43% of reward gains from stylistic exploitation\" 的来源不明**: 这个数字在 proposal 中没有引用来源，不确定是预实验结果还是文献数据。如果是预实验结果，缺乏方法论说明；如果是文献数据，需要引用。\n4. **SAE 在 PRM 上比在 base model 上更 informative 的假设**: Proposal 的核心方法论决策是在 PRM activations 上从头训练 SAE（对比 SteerRM 用 pretrained base-model SAE）。但没有理论论证为什么 PRM-specific SAE 应该更好——可能 pretrained SAE 已经能捕获足够的 features，额外训练只是浪费。\n\n【3 维度打分】:\n  1. Novelty: 弱 — \n  (a) SAE 应用于 reward model 已有 SteerRM (2603.12795)、SARM (2508.08746)、SAFER (2507.00665) 三篇直接先驱工作。本 proposal 的 SAE 部分（从头在 PRM 上训练 SAE）是方法变体而非质的创新。\n  (b) Multi-granularity intervention 比较（feature/neuron/circuit）是一个有用的工程贡献，但 survey 类贡献的 novelty ceiling 低。SteerRM 已做 feature-level，CIRM (2604.27495) 已做 neuron-level，CART (2509.24713) 已涉及 circuit-level。本 proposal 的增量是\"把它们放在一个框架里比较\"。\n  (c) \"Domain Amenability Hypothesis\" 是本 proposal 最具 novelty 的元素，但 N=2 的实验设计严重削弱了其说服力。Orgad et al. (2605.11161) 和 Basu et al. (2603.18353) 已经分别讨论了 \"什么让 interp 变得 actionable\" 和 \"什么情况下 interp 失败\"，本 proposal 在概念层面上是对二者的桥接，而非全新洞察。\n  \n  2. Significance: 中 — \n  \"When do mechanistic interventions work?\" 是一个 genuinely important 的元问题，被 MIT Technology Review 列为 2026 突破性技术方向的一部分，Orgad et al. 和 Basu et al. 均从不同角度触及。但本 proposal 的回答——\"在有 verifiable ground truth 和 constrained output 的 domain 更有效\"——大概率是 \"I would have guessed this\" 类型的发现。如果核心结论是 \"interventions work when you can verify them\"，这接近 tautological。PRM-specific 的分析（如 circuit taxonomy、stylistic exploitation 的 circuit-level 理解）可能有独立意义，但被过于宏大的 framing 稀释了。此外，**本 proposal 的目标会议是 CoRL（Conference on Robot Learning），但内容完全是 NLP/mechanistic interpretability，与 CoRL 的 scope（机器人学习、操纵、自主导航等）严重不匹配，这是一个致命的 venue fit 问题。**\n\n  3. Related Work: 中 — \n  Proposal 引用了几个关键工作（SteerRM、Basu et al.、Orgad et al.、Lee et al.、CIRM），定位相对清晰（对比 SteerRM 的 pretrained SAE 路线，对比 Basu et al. 的失败案例）。但遗漏了几个高度相关的工作：SARM (2508.08746) 直接将 SAE 集成到 reward model 中做 interpretable reward attribution；SAFER (2507.00665) 用 SAE 探测 reward model 安全性；CART (2509.24713) 做 circuit-aware reward training。这些遗漏不致命，但如果在 review 中被指出，会削弱 \"我们提供了 first structured empirical evidence\" 的 claim。\n\n【概率估计】: 3-8%，中位 5%\n【估计理由】: \nIdea 质量本身（不考虑 venue fit）大约在 20-28% 区间——方向有价值（元问题很重要），但核心 hypothesis 的验证设计（N=2 domain comparison）太弱，novelty 被多个 2025-2026 年已发表的 SAE-on-RM 工作覆盖大半，且核心发现大概率是 \"I would have guessed this\" 类型。\n\n然而，**CoRL（Conference on Robot Learning）的 scope 完全不覆盖本 proposal 的内容**。CoRL 主要关注机器人学习、感知、操纵、运动规划、自主驾驶等，而本 proposal 是纯 NLP/mechanistic interpretability 工作，没有任何机器人或具身智能相关内容。这是一个 desk reject 级别的 venue mismatch。即使 idea 本身有一定价值，投稿到 CoRL 几乎不可能通过初筛。\n\n综合考虑 venue fit 因素，概率从 ~25% 降至 3-8%。如果投稿到 NeurIPS/ICML/ICLR 等 ML 主会，idea 质量对应的概率约 20-28%。\n\n上界主要被 Novelty 维度限制——核心技术贡献（SAE on PRM、multi-granularity comparison）增量较小，而 \"Domain Amenability Hypothesis\" 作为 conceptual contribution 被 N=2 的实验设计严重削弱。\n\n【主要风险】:\n1. **Venue Mismatch（致命）**: CoRL 是机器人学习会议，本 proposal 是纯 NLP/mechanistic interpretability 工作，极大概率 desk reject。这是最直接、最不可补救的风险。\n2. **N=2 Domain Comparison 无法支撑 general hypothesis**: 用一个成功案例（PRM）和一个失败案例（Basu et al. 的 clinical LM）来验证 \"Domain Amenability Hypothesis\" 是一个极弱的实验设计。审稿人会质疑：两个 domain 之间的差异远不止 \"output semantics\" 和 \"verifiable ground truth\"——模型不同、训练数据不同、任务结构不同、scale 不同——无法做出 causal attribution。\n```\n\nSources:\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/html/2603.12795)\n- [Interpretability without actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)\n- [Interpretability Can Be Actionable (Orgad et al.)](https://arxiv.org/html/2605.11161)\n- [The Story is Not the Science (Lee et al.)](https://arxiv.org/abs/2602.18458)\n- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)\n- [Interpretable Reward Model via Sparse Autoencoder (SARM)](https://arxiv.org/abs/2508.08746)\n- [SAFER: Probing Safety in Reward Models with Sparse Autoencoder](https://arxiv.org/html/2507.00665v3)\n- [Circuit-Aware Reward Training (CART)](https://arxiv.org/abs/2509.24713)\n- [Mechanistic Interpretability Workshop at ICML 2026](https://mechinterpworkshop.com/cfp/)\n- [MIT Technology Review: Mechanistic Interpretability as 2026 Breakthrough Technology](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient research to make a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795) (arXiv, March 2026): 最直接的竞争工作。已用 SAE 对 reward model 做特征级干预（去除格式偏差），在 6 个 RM 上 Hard-split 准确率平均提升 7.3 个点。发现格式相关特征集中在浅层且跨模型迁移。与本 proposal 高度重合——同样是 SAE + reward model + feature-level intervention。\n- [Interpretability without Actionability: mechanistic methods cannot correct LM errors despite near-perfect internal representations](https://arxiv.org/abs/2603.18353) (Basu et al., arXiv March 2026): 本 proposal 直接引用的\"negative case\"。比较了 4 种机制干预方法在临床分诊上的表现，发现 linear probe 可达 98.2% AUROC 但输出灵敏度仅 45.1%，干预修正 20% 错误同时破坏 53% 正确结果。这篇工作本身已隐含了\"domain matters\"的结论。\n- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability](https://arxiv.org/abs/2601.14004) (Jan 2026): 综合性 survey，按 Localizing → Steering → Improving pipeline 组织，按 interpretable object 粒度分类。已系统性覆盖了 feature-level / neuron-level / circuit-level 的分类和比较。\n- [MIB: A Mechanistic Interpretability Benchmark](https://proceedings.mlr.press/v267/mueller25a.html) (ICML 2025): 提出跨任务跨模型的标准化评估框架，含 circuit localization 和 causal variable localization 两个 track。已建立了多粒度方法的比较基准。\n- [Circuit-Aware Reward Training (CART)](https://arxiv.org/pdf/2509.24713) (2025): 对 reward model 做 circuit 分析用于长尾鲁棒性，已在 RM 上做过 circuit-level 的机制分析。\n- [The Hitchhiker's Guide to Actionable Interpretability](https://actionable-interpretability-guide.github.io/) / [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (2026): 提出 actionability 作为核心评估标准的 position paper，与 proposal 中提到的 Orgad et al. 评估标准高度相关。\n- [The Story is Not the Science: Execution-Grounded Evaluation of MI Research](https://arxiv.org/abs/2602.18458) (Feb 2026): 对 MI 研究的科学严谨性提出评估框架，与 proposal 引用的 Lee et al. 科学严谨性标准对应。\n\n- 调研总结: 机制可解释性干预（feature/neuron/circuit 粒度）在 2025-2026 已进入快速成熟期。SteerRM 已在 reward model 上做了 SAE 干预，Basu et al. 已提供了干预失败的负面案例，Locate-Steer-Improve survey 已建立了多粒度方法的系统分类，MIB 已建立标准化 benchmark。本 proposal 想做的\"多粒度干预在 PRM 上的系统比较 + Domain Amenability Hypothesis\"处于这些已有工作的交汇地带——每个组成部分都已有覆盖，核心 novelty 需要仔细甄别。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁，分两个层面：\n\n1. **对于\"Domain Amenability Hypothesis\"本身**：Basu et al. 已经提供了干预在临床领域失败的证据，SteerRM 已经提供了在 reward model 上成功的证据。一篇综合性的 position paper 或 meta-analysis，对比这些已有结果，辅以简单的 domain 属性分析，可能就能得出与本 proposal 相似的结论——无需从头训练 SAE、做多模型 circuit tracing。Hypothesis 中列出的四个条件（well-defined output semantics, constrained output structure, verifiable ground truth, independently testable specificity）更像是对已知成功/失败案例的事后描述性总结，而非可预测性的理论框架。\n\n2. **对于 PRM 的 stylistic exploitation 问题**：SteerRM 已经用 SAE feature steering 在 RM（含 PRM 类模型）上做了去偏差，本 proposal 在 PRM 上做类似的 SAE 干预并不构成质的飞跃。增量价值需要来自：(a) 多粒度比较的独特洞察，(b) PRM 专属的 process-level 发现。但 proposal 并未令人信服地论证为什么 PRM 的 step-level 结构会产生与 SteerRM 质性不同的发现。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有以下未经验证的关键假设：\n\n1. **\"43% of reward gains from stylistic exploitation\"**：这个数字被当作既定事实引用，但 proposal 未注明来源。如果是自己的初步实验结果，需要验证方法论；如果是引用他人工作，需要确认可复现性。这是整个 testbed motivation 的关键数据。\n\n2. **PRM 是\"ideal testbed\"的假设**：proposal 列出了 4 个 domain amenability 条件，然后声称 PRM 完美符合。但这是 circular reasoning——先为 PRM 量身定制条件，再声称 PRM 满足条件。要真正验证 hypothesis，需要 (a) 在多个满足条件的 domain 上测试，(b) 在不满足部分条件的 domain 上测试，观察干预效果的系统性退化。仅在一个 domain 上做实验 + 引用 Basu et al. 的一个负面 domain 构成的\"对比\"，evidence base 极薄。\n\n3. **\"cross-validated circuit taxonomy\"的假设**：用 RelP、activation patching、attribution graphs 三种方法找到的 circuit 如果不一致，不代表\"cross-validation\"失败——它们本身测量的东西可能不同（sufficiency vs. necessity vs. gradient flow）。如果一致，也不一定意味着找到了\"真正的\"circuit——可能是共享的 artifacts。这个方法论前提需要更仔细的论证。\n\n4. **多粒度比较能产生\"第一个结构化实证证据\"的假设**：MIB benchmark 和 Locate-Steer-Improve survey 已经做了多粒度方法的组织和比较。\"第一个\"的 novelty claim 需要非常精确地界定 scope，否则容易被审稿人质疑。\n\n【3 维度打分】:\n  1. Novelty: 弱 — \n     - \"Domain Amenability Hypothesis\"的四个条件（well-defined semantics, constrained structure, verifiable truth, testable specificity）是对已有成功/失败案例的事后概括，审稿人大概率会说\"these criteria are intuitive / I would have guessed this\"。\n     - SAE + reward model 干预已被 SteerRM (arXiv 2603.12795) 覆盖，且 SteerRM 已报告了跨架构的 feature 迁移性发现。\n     - 多粒度比较已被 Locate-Steer-Improve survey (arXiv 2601.14004) 系统分类，MIB benchmark (ICML 2025) 提供了标准化评估。\n     - \"第一个结构化实证证据\"的 claim 在 Basu et al. (2603.18353) 已做了 4 种方法比较、SteerRM 做了 6 个 RM 比较的背景下，\"第一\"的边界很模糊。\n     - 唯一的真实 novelty delta：在同一个 domain (PRM) 上做 feature/neuron/circuit 三粒度的头对头比较，并用统一评估标准打分——但这更像是 engineering thoroughness，不是 conceptual advance。\n\n  2. Significance: 中 — \n     - \"When do mechanistic interventions work?\" 是一个genuinely important的元问题，尤其在 Basu et al. 的负面结果之后，这个问题的紧迫性上升。\n     - 但预期答案的 surprise value 低：如果结果是\"干预在有 verifiable ground truth 的 domain 上更好用\"——这不会 surprise 任何审稿人。\n     - 如果结果是\"某个粒度系统性优于其他粒度\"——这有一定价值，但仅基于 PRM 一个 domain 的结论推广性有限。\n     - PRM 的实际应用重要性（数学推理验证）为 significance 加分，但 stylistic exploitation 问题 SteerRM 已提供了实用解决方案。\n\n  3. Related Work: 中 — \n     - Proposal 引用了 SteerRM、Basu et al.、Orgad et al.、Lee et al.、Arad et al. 等关键近期工作，覆盖面较好。\n     - 明确与 SteerRM 做了方法论区分（\"explicitly contrasting with SteerRM's pretrained base-model SAE approach\"）。\n     - 但缺失了一些关键参照：(a) Locate-Steer-Improve survey 作为最全面的多粒度分类框架未被讨论；(b) MIB benchmark 作为已有的多粒度评估基准未被提及；(c) CART (Circuit-Aware Reward Training) 作为已在 RM 上做 circuit 分析的工作未被讨论。这些缺失会被审稿人注意到。\n\n【概率估计】: [15% - 28%] 中位 20%\n\n【估计理由】: \nNovelty 是主要限制因素。核心贡献\"Domain Amenability Hypothesis\"的四个条件过于 intuitive，难以说服审稿人这是真正的 insight 而非常识性总结。SteerRM 已在 reward model 上做了 SAE 干预，Basu et al. 已隐含了\"domain matters\"的结论，这两篇同期工作大幅压缩了 novelty 空间。多粒度比较虽有实证价值，但在 MIB 和 survey 已存在的情况下，\"第一个\"的 claim 站不稳。Significance 因问题的重要性有一定支撑（拉高了下界），但预期结果的 surprise value 低限制了上界。如果论文最终发现某些 unexpected 的粒度比较结果（如 circuit-level 干预反而不如 feature-level），实际概率可能更高，但这属于\"结果依赖\"而非 idea 本身的质量。\n\n【主要风险】: \n1. **\"Domain Amenability Hypothesis\"被审稿人判定为 trivially true**：四个条件——well-defined output semantics、constrained structure、verifiable ground truth、testable specificity——本质上是在说\"在容易评估的任务上干预更容易成功\"，这接近 tautology，构成最大的 idea-level 风险。\n2. **Novelty 被 SteerRM + Basu et al. 联合挤压**：SteerRM 已做了 SAE → RM 干预（正面证据），Basu et al. 已做了多方法 → 临床 LM 干预（负面证据）。本 proposal 的核心贡献——在同一 domain 系统比较三个粒度——可能被视为 incremental engineering study 而非 conceptual contribution。\n```\n\nSources:\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)\n- [Interpretability without actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)\n- [Locate, Steer, and Improve: A Practical Survey](https://arxiv.org/abs/2601.14004)\n- [MIB: A Mechanistic Interpretability Benchmark](https://proceedings.mlr.press/v267/mueller25a.html)\n- [Circuit-Aware Reward Training](https://arxiv.org/pdf/2509.24713)\n- [The Hitchhiker's Guide to Actionable Interpretability](https://actionable-interpretability-guide.github.io/)\n- [The Story is Not the Science](https://arxiv.org/abs/2602.18458)\n- [Mechanistic Interpretability for LLM Alignment](https://arxiv.org/abs/2602.11180)\n- [Mechanistic Interpretability Workshop at ICML 2026](https://mechinterpworkshop.com/)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to conduct the evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/pdf/2603.12795) (arXiv 2603.12795, 2026): 与本 proposal 最直接竞争的工作。已经在 reward model 上使用 SAE 做去偏，核心做法是用对比配对识别 stylistic bias 相关的 SAE features 并在推理时抑制。跨 6 个 RM 在 RM-Bench Hard-split 提升 7.3 分。发现 format-related features 集中在浅层并跨模型迁移。关键区别：SteerRM 使用预训练 base model 的 SAE，本 proposal 主张从头在 PRM activations 上训练 SAE。\n\n- [Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors](https://arxiv.org/pdf/2603.18353) (Basu et al., arXiv 2603.18353, 2026): 本 proposal 的\"负面对照\"。系统比较了 4 种 mech interp 方法在临床分诊中纠错的能力，发现即使模型内部表征近乎完美，推理时的表征级干预仍存在 knowledge-action gap。proposal 计划与此对比来论证 \"Domain Amenability Hypothesis\"。\n\n- [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (Orgad et al., ICML 2026 Position Paper): 提出 actionability 作为 interpretability 的评估维度，定义了 concreteness 和 validation 两个轴。本 proposal 计划使用其评估框架。注意：该文于 2026 年 5 月发布，是 position paper 而非 empirical work。\n\n- [The Story is Not the Science: Execution-Grounded Evaluation of Mechanistic Interpretability Research](https://arxiv.org/abs/2602.18458) (Lee et al., arXiv 2602.18458, 2026): 提出首个 execution-grounded 评估框架（MechEvalAgent），关注实验过程的 coherence、结果的 reproducibility 和 findings 的 generalizability。本 proposal 计划使用其 scientific rigor criteria。\n\n- [SAEs Are Good for Steering — If You Select the Right Features](https://arxiv.org/html/2505.20063v2) (Arad et al., 2025): 区分 input features 和 output features，证明 output-score filtered SAE features 在 concept steering 上有 2-3× 提升。本 proposal 计划在 feature-level intervention 中采用此过滤策略。\n\n- [Circuit-Aware Reward Training (CART)](https://arxiv.org/html/2509.24713) (arXiv 2509.24713, 2025): 已经将 circuit analysis 应用到 reward model，识别处理 longtail 场景的专门 neural circuits 并指导数据增强与正则化。与本 proposal 在 \"circuit analysis on reward models\" 方向上有显著重叠。\n\n- [CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs](https://arxiv.org/html/2603.21014v1) (2026): 开源工具，使 CLT-based attribution graphs 的计算更加便捷，降低了本 proposal 所用 CLT 方法的技术门槛（也意味着方法本身的壁垒降低）。\n\n- 调研总结: Mechanistic interpretability 在 2025-2026 年经历了快速发展，SAE 在 reward model 上的应用（SteerRM）、mech interp 干预的失败案例（Basu et al.）、以及评估标准的建立（Orgad, Lee）均已有独立的重要工作。本 proposal 的定位是将这些散落的点连成一条线——通过 \"Domain Amenability Hypothesis\" 统一解释为什么有些干预成功、有些失败。但核心拼图的每一块都已被独立发表。\n\n\n【Trivial Alternative 检验】:\n\n存在两层 trivial alternative 威胁：\n\n1. **直觉预测替代**: \"Domain Amenability Hypothesis\" 的四个条件（well-defined output semantics、constrained output structure、verifiable ground truth、independently testable specificity）本质上是在说\"当目标任务具有清晰的定义和可验证的评估标准时，干预更容易成功\"。这近乎同义反复——一个有 verifiable ground truth 和 constrained binary output 的 PRM 当然比有 messy semantics 的临床分诊更容易干预成功。审稿人只需把 SteerRM（成功案例）和 Basu et al.（失败案例）放在一起，就能用一句话预测这个结论，无需 multi-granularity 实验。\n\n2. **SteerRM 已是直接 baseline**: SteerRM 已经在 reward model 上用 SAE 做了去偏且取得成功。本 proposal 的增量是\"从头训 SAE + 多粒度比较 + 理论框架\"。但如果目的是修复 PRM 的 stylistic exploitation，SteerRM 的简单方案已经 work。如果目的是回答\"when do interventions succeed\"，拿已有的成功/失败 case studies（SteerRM vs. Basu et al.）做 comparative analysis 就够了，不需要从头跑完整的 multi-model、multi-granularity 实验。\n\n增量价值主要在于：(a) 从头在 PRM 上训练 SAE 是否比复用 base-model SAE 有实质优势；(b) 多粒度比较的系统性。但这些是 engineering contributions，不是 conceptual breakthroughs。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的假设：\n\n1. **\"PRM 是 ideal testbed\" 假设**: proposal 断言 PRM 是检验 Domain Amenability Hypothesis 的理想测试域，因为它满足四个条件。但这其实是自我证成的——先定义条件，再选一个满足条件的域来验证。真正的检验应该是：找到一个\"边缘案例\"（部分满足条件的域），预测干预效果，然后验证。仅在一个\"ideal\"域上验证 positive + 引用别人在一个\"clearly non-ideal\"域上的 negative，不构成对 hypothesis 的严格检验。\n\n2. **\"43% of reward gains from stylistic exploitation\" 的来源未交代**: 这个具体数字从何而来？是已发表工作还是 preliminary experiment？如果是自己的初步实验，方法论是否 sound？这个数字是整个 problem framing 的关键支撑。\n\n3. **\"从头训 SAE 优于复用 pretrained SAE\" 假设**: proposal 明确提出与 SteerRM 对比。但没有先验理由说明为什么 PRM-specific SAE 一定更好——如果 stylistic bias 是 base model 带来的（SteerRM 的核心论点），那 base-model SAE 反而可能更直接地捕捉到这些 features。这个假设需要 empirical validation，而不仅仅是 methodological choice。\n\n4. **跨模型 circuit taxonomy 的假设**: proposal 计划在 Qwen2.5-Math-7B、Math-Shepherd-Mistral-7B、和 1.5B variant 上做 cross-validated circuit analysis。但不同架构的模型不保证会形成类似的 circuits，\"cross-validated circuit taxonomy\" 可能发现的是 inconsistency 而非 taxonomy。这不是 fatal，但降低了预期贡献的确定性。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱** — \n   核心的 \"Domain Amenability Hypothesis\" 作为 conceptual contribution，其内容接近 tautological。四个条件（clean semantics, constrained output, verifiable truth, testable specificity）本质上是在重新描述\"容易评估的任务更容易做干预\"。SteerRM (arXiv 2603.12795) 已经证明 SAE 干预在 reward model 上有效；Basu et al. (arXiv 2603.18353) 已经证明在临床场景下无效；将两者放在一起解读并不需要一篇新论文。技术层面，训练 PRM-specific SAE、使用 CLT attribution graphs、多粒度比较都是已有工具的组合应用，无方法论创新。Arad et al. 的 output-score filtering、Anthropic 的 circuit tracing 工具、CLT-Forge 库都已公开可用，降低了技术壁垒的同时也降低了novelty。与 CART (arXiv 2509.24713) 在 \"circuit analysis on reward models\" 方向上有实质重叠。\n\n2. **Significance: 中** — \n   \"When do mechanistic interventions succeed?\" 是 mech interp 领域一个真实且重要的 meta-question，尤其在 Basu et al. 的负面结果和 Orgad et al. 呼吁 actionability 的背景下具有时效性。一个系统性的多粒度比较（feature-level vs. neuron-level vs. circuit-level）如果做得好，对从业者有实际参考价值。然而，如果核心发现只是确认 \"在 clean domain 上干预比在 messy domain 上干预更容易成功\"，这对领域的推进有限——实践者需要的是 fine-grained 的指导（\"在什么条件下用什么粒度的干预\"），而不是 high-level 的域级别判断。此外，**本 proposal 的主题（NLP/mech interp）与 CoRL（Conference on Robot Learning）完全不相关**，如果真的投 CoRL 主会，属于根本性的 venue mismatch。\n\n3. **Related Work: 中** — \n   proposal 展示了对非常近期工作的了解：SteerRM (2026)、Basu et al. (2026)、Orgad et al. (ICML 2026)、Lee et al. (2026)、Arad et al. (2025)。引用覆盖面广且定位清晰（明确说\"contrasting with SteerRM's approach\"、\"contrasting against Basu et al.'s failures\"）。但有两个问题：(a) CART (arXiv 2509.24713) 在 reward model 上做 circuit analysis 的工作未被提及，这是一个明显遗漏；(b) 差异化定位的说服力不足——与 SteerRM 的差异主要是\"从头训 SAE vs. 复用 pretrained SAE\"和\"多粒度 vs. 单粒度\"，这更像是 ablation study 而非独立贡献。\n\n\n【概率估计】: [12% - 22%] 中位 17%\n\n（注：此概率基于投稿至合适的 ML/NLP venue 如 NeurIPS/ICML/ICLR 评估。若真的投 CoRL 2026 主会，由于完全的 venue mismatch，概率应为 ~3-5%。）\n\n【估计理由】: \nNovelty 维度是主要瓶颈。\"Domain Amenability Hypothesis\" 的核心 insight 缺乏 surprisingness——审稿人看到 hypothesis 的四个条件后大概率的反应是 \"this is what I would have expected\"。技术层面是已有工具的组合应用，无方法创新。Significance 因为问题本身的重要性而保住了中等水平，但受限于预期答案的 unsurprising nature。Related work 覆盖尚可但遗漏了 CART。总体上，这是一个 well-organized 的 empirical study proposal，执行层面的 rigor 较好（多模型、多粒度、多评估框架），但 idea 内核的 novelty delta 不足以支撑顶会 acceptance。中位 17% 落在 rubric 的 15-25% 区间中下段。\n\n【主要风险】:\n1. **核心 hypothesis 的 tautological 性质**: \"Domain Amenability Hypothesis\" 的四个条件本质上描述的是\"容易评估 = 容易干预\"，审稿人极可能指出这不是一个需要 extensive empirical validation 的 insight，而是一个 near-obvious observation。这会直接削弱整篇文章的 contribution claim。\n2. **与 SteerRM 的差异化不足**: SteerRM 已经在几乎相同的场景（SAE + reward model debiasing）上取得了成功。本 proposal 需要令人信服地证明\"从头训 SAE + 多粒度分析\"带来的 insights 是 SteerRM 无法提供的。如果实验结果只是确认 SteerRM 的发现并增加了粒度细节，审稿人会认为 incremental。\n```\n\n---\n\n**额外提醒（venue fit）**: 本 proposal 的主题是 NLP/mechanistic interpretability，与 CoRL 2026（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于机器人学习、具身智能、机器人操控等领域。如果确实计划投 CoRL，建议重新考虑 venue 选择（更合适的去向：NeurIPS、ICML、ICLR 主会，或 ICML MechInterp Workshop）。上述概率估计基于合适的 ML/NLP venue。\n\nSources:\n- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/pdf/2603.12795)\n- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/pdf/2603.18353)\n- [Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)\n- [The Story is Not the Science (Lee et al.)](https://arxiv.org/abs/2602.18458)\n- [SAEs Are Good for Steering — If You Select the Right Features (Arad et al.)](https://arxiv.org/html/2505.20063v2)\n- [Circuit-Aware Reward Training (CART)](https://arxiv.org/html/2509.24713)\n- [CLT-Forge: A Scalable Library for Cross-Layer Transcoders](https://arxiv.org/html/2603.21014v1)\n- [Circuit Tracing and Attribution Graphs (Anthropic)](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:29:55.729Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:29:55.729Z",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:29:55.740Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough research to do a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- SteerRM (arXiv 2603.12795, 2026): 首个 training-free 的 SAE-based reward model debiasing 方法。在 pretrained base-model 的 SAE 上识别偏差特征并在推理时抑制。在 RM-Bench Hard-split 上平均提升 7.3 分。与本 proposal 直接竞争——proposal 明确提出要对比 SteerRM 的 pretrained SAE 路线 vs. 自己从头在 PRM activations 上训练 SAE。
- Basu et al., "Interpretability without actionability" (arXiv 2603.18353, 2026): 发现 clinical LM 在内部表征上近乎完美地编码了任务知识，但 mechanistic intervention 仍无法纠正输出错误。本 proposal 将此作为"失败案例"与 PRM"成功案例"做对比。
- Orgad et al., "Interpretability Can Be Actionable" (arXiv 2605.11161, ICML 2026): 提出 mechanistic interpretability 的 actionability 评估框架（faithfulness、generalization、specificity）。本 proposal 将其作为评估标准之一。
- Lee et al., "The Story is Not the Science" (arXiv 2602.18458, 2026): 提出 execution-grounded evaluation framework (MechEvalAgent)，强调方法论严谨性。本 proposal 引用为另一套评估标准。
- CIRM, "Debiasing Reward Models via Causally Motivated Inference-Time Intervention" (arXiv 2604.27495, 2026): neuron-level 的 causal intervention debiasing reward model 方法，识别 bias-specific neurons 并在推理时替换 activations。本 proposal 将其作为 neuron-level intervention baseline。
- SARM, "Interpretable Reward Model via Sparse Autoencoder" (arXiv 2508.08746, 2025): 将 pretrained SAE 集成到 reward model 架构中，实现 feature-level reward attribution。Proposal 未引用此工作，但高度相关。
- SAFER (arXiv 2507.00665, 2025): 用 SAE 探测 reward model 中的 safety 相关 features。同样高度相关但未被引用。
- CART, "Circuit-Aware Reward Training" (arXiv 2509.24713, 2025): 利用 circuit analysis 指导 reward model 训练中的 data augmentation 和 regularization。Proposal 未引用。

调研总结: 2025-2026 年，SAE-based reward model 分析已形成一个活跃的子领域（SteerRM、SARM、SAFER、CIRM），方法涵盖 feature-level 到 neuron-level。同时，"when does mech interp actually work?" 这一元问题由 Orgad et al. 和 Basu et al. 从不同角度提出。本 proposal 试图将二者结合——用 PRM 作为 testbed 做 multi-granularity 比较，并提出 "Domain Amenability Hypothesis" 来解释成功/失败的条件。但该子领域已较为拥挤，多个直接竞争工作存在。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. **文献综述式验证**: "Domain Amenability Hypothesis" 的核心检验是 PRM（成功）vs. clinical LM（失败，来自 Basu et al.）。这实质是一个 N=2 的 cross-domain 比较。一个更简单的方法是：直接收集已发表论文中 mechanistic intervention 的成功/失败案例，做 meta-analysis，总结出 domain 条件——无需任何新实验。这种 survey+meta-analysis 的方式成本远低于本 proposal 的全套实验，且 N 更大。
2. **直接扩展 SteerRM**: SteerRM 已经在 reward model 上做了 SAE-based feature-level intervention 且证明有效。如果目标只是验证 "PRM 上 mechanistic intervention 可以 work"，SteerRM 已经给出了答案。本 proposal 的增量在于 (a) 从头训练 SAE 而非用 pretrained SAE，(b) 多粒度比较，(c) Domain Amenability 的理论化。其中 (a) 是方法变体而非质的飞跃，(b) 是工程完备性，(c) 因 N=2 而说服力不足。
3. **更好的 PRM 训练数据**: 如果核心问题是 "PRM 把 fluency 和 correctness 混淆"，一个更直接的解决方案是改进 PRM 的训练数据（如使用更干净的 step-level annotations），而非后期做 mechanistic intervention。

增量价值: 主要在于提供了一个系统的 multi-granularity 比较框架，以及尝试将零散的成功/失败案例理论化。但这种增量是 "组织性" 的而非 "洞察性" 的。

【前提假设检验】:
核心 claim 的逻辑链有多个未验证环节：
1. **"Domain Amenability" 四条件的充分/必要性未建立**: Proposal 提出 well-defined output semantics、constrained output structure、verifiable ground truth、independently testable specificity 是成功条件。但这四条不是从理论推导出来的，也不是从大量实证中归纳出来的——它们是根据 PRM 的特性 post-hoc 提出的。如果 PRM 上 intervention 碰巧失败了，作者可能会提出另一套条件。这是一种 "先射箭后画靶" 的论证。
2. **PRM 成功 vs. Clinical LM 失败的归因假设**: Proposal 假设二者的差异可以归因于 domain 特性差异。但实际上，Basu et al. 的失败可能源于模型规模、训练数据质量、任务复杂度、模型架构等多种混淆因素——而非 domain amenability。N=2 且两个 case 之间有无数混淆变量，无法支持 causal claim。
3. **"43% of reward gains from stylistic exploitation" 的来源不明**: 这个数字在 proposal 中没有引用来源，不确定是预实验结果还是文献数据。如果是预实验结果，缺乏方法论说明；如果是文献数据，需要引用。
4. **SAE 在 PRM 上比在 base model 上更 informative 的假设**: Proposal 的核心方法论决策是在 PRM activations 上从头训练 SAE（对比 SteerRM 用 pretrained base-model SAE）。但没有理论论证为什么 PRM-specific SAE 应该更好——可能 pretrained SAE 已经能捕获足够的 features，额外训练只是浪费。

【3 维度打分】:
  1. Novelty: 弱 — 
  (a) SAE 应用于 reward model 已有 SteerRM (2603.12795)、SARM (2508.08746)、SAFER (2507.00665) 三篇直接先驱工作。本 proposal 的 SAE 部分（从头在 PRM 上训练 SAE）是方法变体而非质的创新。
  (b) Multi-granularity intervention 比较（feature/neuron/circuit）是一个有用的工程贡献，但 survey 类贡献的 novelty ceiling 低。SteerRM 已做 feature-level，CIRM (2604.27495) 已做 neuron-level，CART (2509.24713) 已涉及 circuit-level。本 proposal 的增量是"把它们放在一个框架里比较"。
  (c) "Domain Amenability Hypothesis" 是本 proposal 最具 novelty 的元素，但 N=2 的实验设计严重削弱了其说服力。Orgad et al. (2605.11161) 和 Basu et al. (2603.18353) 已经分别讨论了 "什么让 interp 变得 actionable" 和 "什么情况下 interp 失败"，本 proposal 在概念层面上是对二者的桥接，而非全新洞察。
  
  2. Significance: 中 — 
  "When do mechanistic interventions work?" 是一个 genuinely important 的元问题，被 MIT Technology Review 列为 2026 突破性技术方向的一部分，Orgad et al. 和 Basu et al. 均从不同角度触及。但本 proposal 的回答——"在有 verifiable ground truth 和 constrained output 的 domain 更有效"——大概率是 "I would have guessed this" 类型的发现。如果核心结论是 "interventions work when you can verify them"，这接近 tautological。PRM-specific 的分析（如 circuit taxonomy、stylistic exploitation 的 circuit-level 理解）可能有独立意义，但被过于宏大的 framing 稀释了。此外，**本 proposal 的目标会议是 CoRL（Conference on Robot Learning），但内容完全是 NLP/mechanistic interpretability，与 CoRL 的 scope（机器人学习、操纵、自主导航等）严重不匹配，这是一个致命的 venue fit 问题。**

  3. Related Work: 中 — 
  Proposal 引用了几个关键工作（SteerRM、Basu et al.、Orgad et al.、Lee et al.、CIRM），定位相对清晰（对比 SteerRM 的 pretrained SAE 路线，对比 Basu et al. 的失败案例）。但遗漏了几个高度相关的工作：SARM (2508.08746) 直接将 SAE 集成到 reward model 中做 interpretable reward attribution；SAFER (2507.00665) 用 SAE 探测 reward model 安全性；CART (2509.24713) 做 circuit-aware reward training。这些遗漏不致命，但如果在 review 中被指出，会削弱 "我们提供了 first structured empirical evidence" 的 claim。

【概率估计】: 3-8%，中位 5%
【估计理由】: 
Idea 质量本身（不考虑 venue fit）大约在 20-28% 区间——方向有价值（元问题很重要），但核心 hypothesis 的验证设计（N=2 domain comparison）太弱，novelty 被多个 2025-2026 年已发表的 SAE-on-RM 工作覆盖大半，且核心发现大概率是 "I would have guessed this" 类型。

然而，**CoRL（Conference on Robot Learning）的 scope 完全不覆盖本 proposal 的内容**。CoRL 主要关注机器人学习、感知、操纵、运动规划、自主驾驶等，而本 proposal 是纯 NLP/mechanistic interpretability 工作，没有任何机器人或具身智能相关内容。这是一个 desk reject 级别的 venue mismatch。即使 idea 本身有一定价值，投稿到 CoRL 几乎不可能通过初筛。

综合考虑 venue fit 因素，概率从 ~25% 降至 3-8%。如果投稿到 NeurIPS/ICML/ICLR 等 ML 主会，idea 质量对应的概率约 20-28%。

上界主要被 Novelty 维度限制——核心技术贡献（SAE on PRM、multi-granularity comparison）增量较小，而 "Domain Amenability Hypothesis" 作为 conceptual contribution 被 N=2 的实验设计严重削弱。

【主要风险】:
1. **Venue Mismatch（致命）**: CoRL 是机器人学习会议，本 proposal 是纯 NLP/mechanistic interpretability 工作，极大概率 desk reject。这是最直接、最不可补救的风险。
2. **N=2 Domain Comparison 无法支撑 general hypothesis**: 用一个成功案例（PRM）和一个失败案例（Basu et al. 的 clinical LM）来验证 "Domain Amenability Hypothesis" 是一个极弱的实验设计。审稿人会质疑：两个 domain 之间的差异远不止 "output semantics" 和 "verifiable ground truth"——模型不同、训练数据不同、任务结构不同、scale 不同——无法做出 causal attribution。
```

Sources:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/html/2603.12795)
- [Interpretability without actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)
- [Interpretability Can Be Actionable (Orgad et al.)](https://arxiv.org/html/2605.11161)
- [The Story is Not the Science (Lee et al.)](https://arxiv.org/abs/2602.18458)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)
- [Interpretable Reward Model via Sparse Autoencoder (SARM)](https://arxiv.org/abs/2508.08746)
- [SAFER: Probing Safety in Reward Models with Sparse Autoencoder](https://arxiv.org/html/2507.00665v3)
- [Circuit-Aware Reward Training (CART)](https://arxiv.org/abs/2509.24713)
- [Mechanistic Interpretability Workshop at ICML 2026](https://mechinterpworkshop.com/cfp/)
- [MIT Technology Review: Mechanistic Interpretability as 2026 Breakthrough Technology](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient research to make a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795) (arXiv, March 2026): 最直接的竞争工作。已用 SAE 对 reward model 做特征级干预（去除格式偏差），在 6 个 RM 上 Hard-split 准确率平均提升 7.3 个点。发现格式相关特征集中在浅层且跨模型迁移。与本 proposal 高度重合——同样是 SAE + reward model + feature-level intervention。
- [Interpretability without Actionability: mechanistic methods cannot correct LM errors despite near-perfect internal representations](https://arxiv.org/abs/2603.18353) (Basu et al., arXiv March 2026): 本 proposal 直接引用的"negative case"。比较了 4 种机制干预方法在临床分诊上的表现，发现 linear probe 可达 98.2% AUROC 但输出灵敏度仅 45.1%，干预修正 20% 错误同时破坏 53% 正确结果。这篇工作本身已隐含了"domain matters"的结论。
- [Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability](https://arxiv.org/abs/2601.14004) (Jan 2026): 综合性 survey，按 Localizing → Steering → Improving pipeline 组织，按 interpretable object 粒度分类。已系统性覆盖了 feature-level / neuron-level / circuit-level 的分类和比较。
- [MIB: A Mechanistic Interpretability Benchmark](https://proceedings.mlr.press/v267/mueller25a.html) (ICML 2025): 提出跨任务跨模型的标准化评估框架，含 circuit localization 和 causal variable localization 两个 track。已建立了多粒度方法的比较基准。
- [Circuit-Aware Reward Training (CART)](https://arxiv.org/pdf/2509.24713) (2025): 对 reward model 做 circuit 分析用于长尾鲁棒性，已在 RM 上做过 circuit-level 的机制分析。
- [The Hitchhiker's Guide to Actionable Interpretability](https://actionable-interpretability-guide.github.io/) / [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (2026): 提出 actionability 作为核心评估标准的 position paper，与 proposal 中提到的 Orgad et al. 评估标准高度相关。
- [The Story is Not the Science: Execution-Grounded Evaluation of MI Research](https://arxiv.org/abs/2602.18458) (Feb 2026): 对 MI 研究的科学严谨性提出评估框架，与 proposal 引用的 Lee et al. 科学严谨性标准对应。

- 调研总结: 机制可解释性干预（feature/neuron/circuit 粒度）在 2025-2026 已进入快速成熟期。SteerRM 已在 reward model 上做了 SAE 干预，Basu et al. 已提供了干预失败的负面案例，Locate-Steer-Improve survey 已建立了多粒度方法的系统分类，MIB 已建立标准化 benchmark。本 proposal 想做的"多粒度干预在 PRM 上的系统比较 + Domain Amenability Hypothesis"处于这些已有工作的交汇地带——每个组成部分都已有覆盖，核心 novelty 需要仔细甄别。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁，分两个层面：

1. **对于"Domain Amenability Hypothesis"本身**：Basu et al. 已经提供了干预在临床领域失败的证据，SteerRM 已经提供了在 reward model 上成功的证据。一篇综合性的 position paper 或 meta-analysis，对比这些已有结果，辅以简单的 domain 属性分析，可能就能得出与本 proposal 相似的结论——无需从头训练 SAE、做多模型 circuit tracing。Hypothesis 中列出的四个条件（well-defined output semantics, constrained output structure, verifiable ground truth, independently testable specificity）更像是对已知成功/失败案例的事后描述性总结，而非可预测性的理论框架。

2. **对于 PRM 的 stylistic exploitation 问题**：SteerRM 已经用 SAE feature steering 在 RM（含 PRM 类模型）上做了去偏差，本 proposal 在 PRM 上做类似的 SAE 干预并不构成质的飞跃。增量价值需要来自：(a) 多粒度比较的独特洞察，(b) PRM 专属的 process-level 发现。但 proposal 并未令人信服地论证为什么 PRM 的 step-level 结构会产生与 SteerRM 质性不同的发现。

【前提假设检验】:
核心 claim 的逻辑链条中有以下未经验证的关键假设：

1. **"43% of reward gains from stylistic exploitation"**：这个数字被当作既定事实引用，但 proposal 未注明来源。如果是自己的初步实验结果，需要验证方法论；如果是引用他人工作，需要确认可复现性。这是整个 testbed motivation 的关键数据。

2. **PRM 是"ideal testbed"的假设**：proposal 列出了 4 个 domain amenability 条件，然后声称 PRM 完美符合。但这是 circular reasoning——先为 PRM 量身定制条件，再声称 PRM 满足条件。要真正验证 hypothesis，需要 (a) 在多个满足条件的 domain 上测试，(b) 在不满足部分条件的 domain 上测试，观察干预效果的系统性退化。仅在一个 domain 上做实验 + 引用 Basu et al. 的一个负面 domain 构成的"对比"，evidence base 极薄。

3. **"cross-validated circuit taxonomy"的假设**：用 RelP、activation patching、attribution graphs 三种方法找到的 circuit 如果不一致，不代表"cross-validation"失败——它们本身测量的东西可能不同（sufficiency vs. necessity vs. gradient flow）。如果一致，也不一定意味着找到了"真正的"circuit——可能是共享的 artifacts。这个方法论前提需要更仔细的论证。

4. **多粒度比较能产生"第一个结构化实证证据"的假设**：MIB benchmark 和 Locate-Steer-Improve survey 已经做了多粒度方法的组织和比较。"第一个"的 novelty claim 需要非常精确地界定 scope，否则容易被审稿人质疑。

【3 维度打分】:
  1. Novelty: 弱 — 
     - "Domain Amenability Hypothesis"的四个条件（well-defined semantics, constrained structure, verifiable truth, testable specificity）是对已有成功/失败案例的事后概括，审稿人大概率会说"these criteria are intuitive / I would have guessed this"。
     - SAE + reward model 干预已被 SteerRM (arXiv 2603.12795) 覆盖，且 SteerRM 已报告了跨架构的 feature 迁移性发现。
     - 多粒度比较已被 Locate-Steer-Improve survey (arXiv 2601.14004) 系统分类，MIB benchmark (ICML 2025) 提供了标准化评估。
     - "第一个结构化实证证据"的 claim 在 Basu et al. (2603.18353) 已做了 4 种方法比较、SteerRM 做了 6 个 RM 比较的背景下，"第一"的边界很模糊。
     - 唯一的真实 novelty delta：在同一个 domain (PRM) 上做 feature/neuron/circuit 三粒度的头对头比较，并用统一评估标准打分——但这更像是 engineering thoroughness，不是 conceptual advance。

  2. Significance: 中 — 
     - "When do mechanistic interventions work?" 是一个genuinely important的元问题，尤其在 Basu et al. 的负面结果之后，这个问题的紧迫性上升。
     - 但预期答案的 surprise value 低：如果结果是"干预在有 verifiable ground truth 的 domain 上更好用"——这不会 surprise 任何审稿人。
     - 如果结果是"某个粒度系统性优于其他粒度"——这有一定价值，但仅基于 PRM 一个 domain 的结论推广性有限。
     - PRM 的实际应用重要性（数学推理验证）为 significance 加分，但 stylistic exploitation 问题 SteerRM 已提供了实用解决方案。

  3. Related Work: 中 — 
     - Proposal 引用了 SteerRM、Basu et al.、Orgad et al.、Lee et al.、Arad et al. 等关键近期工作，覆盖面较好。
     - 明确与 SteerRM 做了方法论区分（"explicitly contrasting with SteerRM's pretrained base-model SAE approach"）。
     - 但缺失了一些关键参照：(a) Locate-Steer-Improve survey 作为最全面的多粒度分类框架未被讨论；(b) MIB benchmark 作为已有的多粒度评估基准未被提及；(c) CART (Circuit-Aware Reward Training) 作为已在 RM 上做 circuit 分析的工作未被讨论。这些缺失会被审稿人注意到。

【概率估计】: [15% - 28%] 中位 20%

【估计理由】: 
Novelty 是主要限制因素。核心贡献"Domain Amenability Hypothesis"的四个条件过于 intuitive，难以说服审稿人这是真正的 insight 而非常识性总结。SteerRM 已在 reward model 上做了 SAE 干预，Basu et al. 已隐含了"domain matters"的结论，这两篇同期工作大幅压缩了 novelty 空间。多粒度比较虽有实证价值，但在 MIB 和 survey 已存在的情况下，"第一个"的 claim 站不稳。Significance 因问题的重要性有一定支撑（拉高了下界），但预期结果的 surprise value 低限制了上界。如果论文最终发现某些 unexpected 的粒度比较结果（如 circuit-level 干预反而不如 feature-level），实际概率可能更高，但这属于"结果依赖"而非 idea 本身的质量。

【主要风险】: 
1. **"Domain Amenability Hypothesis"被审稿人判定为 trivially true**：四个条件——well-defined output semantics、constrained structure、verifiable ground truth、testable specificity——本质上是在说"在容易评估的任务上干预更容易成功"，这接近 tautology，构成最大的 idea-level 风险。
2. **Novelty 被 SteerRM + Basu et al. 联合挤压**：SteerRM 已做了 SAE → RM 干预（正面证据），Basu et al. 已做了多方法 → 临床 LM 干预（负面证据）。本 proposal 的核心贡献——在同一 domain 系统比较三个粒度——可能被视为 incremental engineering study 而非 conceptual contribution。
```

Sources:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [Interpretability without actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)
- [Locate, Steer, and Improve: A Practical Survey](https://arxiv.org/abs/2601.14004)
- [MIB: A Mechanistic Interpretability Benchmark](https://proceedings.mlr.press/v267/mueller25a.html)
- [Circuit-Aware Reward Training](https://arxiv.org/pdf/2509.24713)
- [The Hitchhiker's Guide to Actionable Interpretability](https://actionable-interpretability-guide.github.io/)
- [The Story is Not the Science](https://arxiv.org/abs/2602.18458)
- [Mechanistic Interpretability for LLM Alignment](https://arxiv.org/abs/2602.11180)
- [Mechanistic Interpretability Workshop at ICML 2026](https://mechinterpworkshop.com/)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to conduct the evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/pdf/2603.12795) (arXiv 2603.12795, 2026): 与本 proposal 最直接竞争的工作。已经在 reward model 上使用 SAE 做去偏，核心做法是用对比配对识别 stylistic bias 相关的 SAE features 并在推理时抑制。跨 6 个 RM 在 RM-Bench Hard-split 提升 7.3 分。发现 format-related features 集中在浅层并跨模型迁移。关键区别：SteerRM 使用预训练 base model 的 SAE，本 proposal 主张从头在 PRM activations 上训练 SAE。

- [Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors](https://arxiv.org/pdf/2603.18353) (Basu et al., arXiv 2603.18353, 2026): 本 proposal 的"负面对照"。系统比较了 4 种 mech interp 方法在临床分诊中纠错的能力，发现即使模型内部表征近乎完美，推理时的表征级干预仍存在 knowledge-action gap。proposal 计划与此对比来论证 "Domain Amenability Hypothesis"。

- [Interpretability Can Be Actionable](https://arxiv.org/abs/2605.11161) (Orgad et al., ICML 2026 Position Paper): 提出 actionability 作为 interpretability 的评估维度，定义了 concreteness 和 validation 两个轴。本 proposal 计划使用其评估框架。注意：该文于 2026 年 5 月发布，是 position paper 而非 empirical work。

- [The Story is Not the Science: Execution-Grounded Evaluation of Mechanistic Interpretability Research](https://arxiv.org/abs/2602.18458) (Lee et al., arXiv 2602.18458, 2026): 提出首个 execution-grounded 评估框架（MechEvalAgent），关注实验过程的 coherence、结果的 reproducibility 和 findings 的 generalizability。本 proposal 计划使用其 scientific rigor criteria。

- [SAEs Are Good for Steering — If You Select the Right Features](https://arxiv.org/html/2505.20063v2) (Arad et al., 2025): 区分 input features 和 output features，证明 output-score filtered SAE features 在 concept steering 上有 2-3× 提升。本 proposal 计划在 feature-level intervention 中采用此过滤策略。

- [Circuit-Aware Reward Training (CART)](https://arxiv.org/html/2509.24713) (arXiv 2509.24713, 2025): 已经将 circuit analysis 应用到 reward model，识别处理 longtail 场景的专门 neural circuits 并指导数据增强与正则化。与本 proposal 在 "circuit analysis on reward models" 方向上有显著重叠。

- [CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs](https://arxiv.org/html/2603.21014v1) (2026): 开源工具，使 CLT-based attribution graphs 的计算更加便捷，降低了本 proposal 所用 CLT 方法的技术门槛（也意味着方法本身的壁垒降低）。

- 调研总结: Mechanistic interpretability 在 2025-2026 年经历了快速发展，SAE 在 reward model 上的应用（SteerRM）、mech interp 干预的失败案例（Basu et al.）、以及评估标准的建立（Orgad, Lee）均已有独立的重要工作。本 proposal 的定位是将这些散落的点连成一条线——通过 "Domain Amenability Hypothesis" 统一解释为什么有些干预成功、有些失败。但核心拼图的每一块都已被独立发表。


【Trivial Alternative 检验】:

存在两层 trivial alternative 威胁：

1. **直觉预测替代**: "Domain Amenability Hypothesis" 的四个条件（well-defined output semantics、constrained output structure、verifiable ground truth、independently testable specificity）本质上是在说"当目标任务具有清晰的定义和可验证的评估标准时，干预更容易成功"。这近乎同义反复——一个有 verifiable ground truth 和 constrained binary output 的 PRM 当然比有 messy semantics 的临床分诊更容易干预成功。审稿人只需把 SteerRM（成功案例）和 Basu et al.（失败案例）放在一起，就能用一句话预测这个结论，无需 multi-granularity 实验。

2. **SteerRM 已是直接 baseline**: SteerRM 已经在 reward model 上用 SAE 做了去偏且取得成功。本 proposal 的增量是"从头训 SAE + 多粒度比较 + 理论框架"。但如果目的是修复 PRM 的 stylistic exploitation，SteerRM 的简单方案已经 work。如果目的是回答"when do interventions succeed"，拿已有的成功/失败 case studies（SteerRM vs. Basu et al.）做 comparative analysis 就够了，不需要从头跑完整的 multi-model、multi-granularity 实验。

增量价值主要在于：(a) 从头在 PRM 上训练 SAE 是否比复用 base-model SAE 有实质优势；(b) 多粒度比较的系统性。但这些是 engineering contributions，不是 conceptual breakthroughs。


【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **"PRM 是 ideal testbed" 假设**: proposal 断言 PRM 是检验 Domain Amenability Hypothesis 的理想测试域，因为它满足四个条件。但这其实是自我证成的——先定义条件，再选一个满足条件的域来验证。真正的检验应该是：找到一个"边缘案例"（部分满足条件的域），预测干预效果，然后验证。仅在一个"ideal"域上验证 positive + 引用别人在一个"clearly non-ideal"域上的 negative，不构成对 hypothesis 的严格检验。

2. **"43% of reward gains from stylistic exploitation" 的来源未交代**: 这个具体数字从何而来？是已发表工作还是 preliminary experiment？如果是自己的初步实验，方法论是否 sound？这个数字是整个 problem framing 的关键支撑。

3. **"从头训 SAE 优于复用 pretrained SAE" 假设**: proposal 明确提出与 SteerRM 对比。但没有先验理由说明为什么 PRM-specific SAE 一定更好——如果 stylistic bias 是 base model 带来的（SteerRM 的核心论点），那 base-model SAE 反而可能更直接地捕捉到这些 features。这个假设需要 empirical validation，而不仅仅是 methodological choice。

4. **跨模型 circuit taxonomy 的假设**: proposal 计划在 Qwen2.5-Math-7B、Math-Shepherd-Mistral-7B、和 1.5B variant 上做 cross-validated circuit analysis。但不同架构的模型不保证会形成类似的 circuits，"cross-validated circuit taxonomy" 可能发现的是 inconsistency 而非 taxonomy。这不是 fatal，但降低了预期贡献的确定性。


【3 维度打分】:

1. **Novelty: 弱** — 
   核心的 "Domain Amenability Hypothesis" 作为 conceptual contribution，其内容接近 tautological。四个条件（clean semantics, constrained output, verifiable truth, testable specificity）本质上是在重新描述"容易评估的任务更容易做干预"。SteerRM (arXiv 2603.12795) 已经证明 SAE 干预在 reward model 上有效；Basu et al. (arXiv 2603.18353) 已经证明在临床场景下无效；将两者放在一起解读并不需要一篇新论文。技术层面，训练 PRM-specific SAE、使用 CLT attribution graphs、多粒度比较都是已有工具的组合应用，无方法论创新。Arad et al. 的 output-score filtering、Anthropic 的 circuit tracing 工具、CLT-Forge 库都已公开可用，降低了技术壁垒的同时也降低了novelty。与 CART (arXiv 2509.24713) 在 "circuit analysis on reward models" 方向上有实质重叠。

2. **Significance: 中** — 
   "When do mechanistic interventions succeed?" 是 mech interp 领域一个真实且重要的 meta-question，尤其在 Basu et al. 的负面结果和 Orgad et al. 呼吁 actionability 的背景下具有时效性。一个系统性的多粒度比较（feature-level vs. neuron-level vs. circuit-level）如果做得好，对从业者有实际参考价值。然而，如果核心发现只是确认 "在 clean domain 上干预比在 messy domain 上干预更容易成功"，这对领域的推进有限——实践者需要的是 fine-grained 的指导（"在什么条件下用什么粒度的干预"），而不是 high-level 的域级别判断。此外，**本 proposal 的主题（NLP/mech interp）与 CoRL（Conference on Robot Learning）完全不相关**，如果真的投 CoRL 主会，属于根本性的 venue mismatch。

3. **Related Work: 中** — 
   proposal 展示了对非常近期工作的了解：SteerRM (2026)、Basu et al. (2026)、Orgad et al. (ICML 2026)、Lee et al. (2026)、Arad et al. (2025)。引用覆盖面广且定位清晰（明确说"contrasting with SteerRM's approach"、"contrasting against Basu et al.'s failures"）。但有两个问题：(a) CART (arXiv 2509.24713) 在 reward model 上做 circuit analysis 的工作未被提及，这是一个明显遗漏；(b) 差异化定位的说服力不足——与 SteerRM 的差异主要是"从头训 SAE vs. 复用 pretrained SAE"和"多粒度 vs. 单粒度"，这更像是 ablation study 而非独立贡献。


【概率估计】: [12% - 22%] 中位 17%

（注：此概率基于投稿至合适的 ML/NLP venue 如 NeurIPS/ICML/ICLR 评估。若真的投 CoRL 2026 主会，由于完全的 venue mismatch，概率应为 ~3-5%。）

【估计理由】: 
Novelty 维度是主要瓶颈。"Domain Amenability Hypothesis" 的核心 insight 缺乏 surprisingness——审稿人看到 hypothesis 的四个条件后大概率的反应是 "this is what I would have expected"。技术层面是已有工具的组合应用，无方法创新。Significance 因为问题本身的重要性而保住了中等水平，但受限于预期答案的 unsurprising nature。Related work 覆盖尚可但遗漏了 CART。总体上，这是一个 well-organized 的 empirical study proposal，执行层面的 rigor 较好（多模型、多粒度、多评估框架），但 idea 内核的 novelty delta 不足以支撑顶会 acceptance。中位 17% 落在 rubric 的 15-25% 区间中下段。

【主要风险】:
1. **核心 hypothesis 的 tautological 性质**: "Domain Amenability Hypothesis" 的四个条件本质上描述的是"容易评估 = 容易干预"，审稿人极可能指出这不是一个需要 extensive empirical validation 的 insight，而是一个 near-obvious observation。这会直接削弱整篇文章的 contribution claim。
2. **与 SteerRM 的差异化不足**: SteerRM 已经在几乎相同的场景（SAE + reward model debiasing）上取得了成功。本 proposal 需要令人信服地证明"从头训 SAE + 多粒度分析"带来的 insights 是 SteerRM 无法提供的。如果实验结果只是确认 SteerRM 的发现并增加了粒度细节，审稿人会认为 incremental。
```

---

**额外提醒（venue fit）**: 本 proposal 的主题是 NLP/mechanistic interpretability，与 CoRL 2026（Conference on Robot Learning）的 scope 完全不匹配。CoRL 聚焦于机器人学习、具身智能、机器人操控等领域。如果确实计划投 CoRL，建议重新考虑 venue 选择（更合适的去向：NeurIPS、ICML、ICLR 主会，或 ICML MechInterp Workshop）。上述概率估计基于合适的 ML/NLP venue。

Sources:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/pdf/2603.12795)
- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/pdf/2603.18353)
- [Interpretability Can Be Actionable (Orgad et al., ICML 2026)](https://arxiv.org/abs/2605.11161)
- [The Story is Not the Science (Lee et al.)](https://arxiv.org/abs/2602.18458)
- [SAEs Are Good for Steering — If You Select the Right Features (Arad et al.)](https://arxiv.org/html/2505.20063v2)
- [Circuit-Aware Reward Training (CART)](https://arxiv.org/html/2509.24713)
- [CLT-Forge: A Scalable Library for Cross-Layer Transcoders](https://arxiv.org/html/2603.21014v1)
- [Circuit Tracing and Attribution Graphs (Anthropic)](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)


【原始 proposal（允许参考但不是主要依据）】:
# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models

## Description
When do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "70baec75-2080-4281-b2c4-78996d948ea9",
  "type": "user",
  "uuid": "8e6b3146-b0ce-461e-8696-d0e3a33075a1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:29:55.739Z_

```json
{
  "parentUuid": "8e6b3146-b0ce-461e-8696-d0e3a33075a1",
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
  "uuid": "4bd2abeb-017f-4f3e-95a7-a9a49510f138",
  "timestamp": "2026-05-20T03:29:55.739Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:29:55.739Z_

```json
{
  "parentUuid": "4bd2abeb-017f-4f3e-95a7-a9a49510f138",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c4cdb045-4d0d-4e97-b0fc-23cc3d193a68",
  "timestamp": "2026-05-20T03:29:55.739Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough research to do a thorough evaluation. Let me…",
  "leafUuid": "c4cdb045-4d0d-4e97-b0fc-23cc3d193a68",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mechanistic interventions on process reward models",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:30:39.166Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and synthesize them as Meta Judge.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 弱
- Significance: 中
- Related Work: 中
- Probability: 3-8%, median 5%
- Key issue: **CoRL venue mismatch (致命)** — dropped from ~25% to 3-8%
- Other issues: N=2 domain comparison, tautological hypothesis, novelty squeezed by SteerRM/Basu et al.
  
**Reviewer 2:**
- Novelty: 弱
- Significance: 中
- Related Work: 中
- Probability: 15-28%, median 20%
- Key issue: Novelty squeezed by SteerRM + Basu et al., tautological hypothesis
- Note: Did NOT flag CoRL venue mismatch in probability (seems to evaluate for appropriate venue)

**Reviewer 3:**
- Novelty: 弱
- Significance: 中
- Related Work: 中
- Probability: 12-22%, median 17%
- Key issue: Tautological hypothesis, insufficient differentiation from SteerRM

The critical divergence is Reviewer 1's venue mismatch concern, which dramatically suppressed their probability estimate compared to the other two reviewers who both landed in the 15-20% range. All three identified the same core weaknesses around novelty and the tautological hypothesis, but only Reviewer 1 treated the CoRL fit as a fatal flaw. The standard deviation works out to about 2.9%, which puts this in the high-agreement range. Now I need to figure out how to present these numbers clearly—the raw medians they gave versus the venue-adjusted estimates, and how the CoRL mismatch factors in as a separate consideration. The consensus is clear across all three reviewers on the major flaws: SteerRM's novelty gets squeezed by the domain amenability hypothesis being tautological, the two-domain comparison is insufficient, that mysterious 43% figure lacks proper sourcing, and CoRL is fundamentally misaligned as a venue. There's also agreement on the missing CART citation and the circular logic around using PRM as an "ideal testbed." Beyond that, the reviewers diverge on specific missing citations—R1 flags SARM and SAFER, while R2 points to the Locate-Steer-Improve survey and MIB benchmark, plus some methodological concerns about their circuit taxonomy approach.

For CoRL 2026, all three reviewers see this as a venue mismatch that would almost certainly trigger a desk reject, with acceptance probabilities ranging from 2-7% and a median around 4%. If submitted to an appropriate top-tier venue instead, the paper's chances improve significantly—R1 estimates 20-28%, R2 gives 15-28%, and R3 suggests 12-22%—but the weak novelty rating across the board caps the ceiling at around 18% median across venues.

Now I'm reconsidering how to properly aggregate these estimates. The three medians are 5%, 20%, and 17%, which gives a standard deviation of about 6.5%—technically "medium consistency" territory. But that divergence is entirely driven by the venue mismatch question, not disagreement about the core idea quality. The real issue is whether to report the raw numbers or flag that the apparent spread masks underlying agreement on the actual research merit.

For the implementation requirements, this proposal would need substantial compute resources for training sparse autoencoders on model activations and running circuit analysis across multiple models, likely using public datasets like GSM8K and MATH. The work is mostly automated with minimal human intervention, though it does require training SAEs from scratch. The full experimental pipeline probably takes three to five months.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4cdb045-4d0d-4e97-b0fc-23cc3d193a68",
  "isSidechain": false,
  "requestId": "req_011CbD7VvPj3tPze2KB1BCD9",
  "type": "assistant",
  "uuid": "ce9c86bb-fe49-4495-82f3-cb25e7926509",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7dHXCZ3qvyAFTYTn4NCTP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13914,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4266,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 13914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13914
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

_source line 9 · 2026-05-20T03:31:31.645Z_

【阶段】: Meta Judge

【三次中位】: [5%, 20%, 17%]  std=6.5%

【共识维度】:
- **Novelty = 弱**（3/3 一致）：Domain Amenability Hypothesis 的四个条件接近 tautological（"容易评估的任务更容易干预成功"）；SteerRM (2603.12795) 已做 SAE→RM 干预，Basu et al. (2603.18353) 已提供负面案例，novelty 空间被严重压缩；多粒度比较属 engineering thoroughness 而非 conceptual advance
- **Significance = 中**（3/3 一致）："When do mechanistic interventions work?" 是genuinely important的元问题，但预期答案 surprise value 低；PRM 应用场景有实际价值但 SteerRM 已提供实用解决方案
- **Related Work = 中**（3/3 一致）：对 SteerRM、Basu et al.、Orgad et al.、Lee et al. 的覆盖较好且定位清晰，但存在遗漏（CART 被 2 人指出）
- **CoRL venue mismatch = 致命**（3/3 一致）：proposal 是纯 NLP/mechanistic interpretability 工作，CoRL 聚焦机器人学习，极大概率 desk reject
- **"43%" 数字来源不明**（3/3 一致）：核心 problem framing 的关键支撑数据缺乏引用或方法论说明
- **N=2 domain comparison 无法支撑 general hypothesis**（3/3 一致）：PRM（成功）vs. clinical LM（失败）之间存在大量混淆变量，无法做 causal attribution
- **Hypothesis 循环论证 / post-hoc**（2/3：R2, R3）：先为 PRM 量身定制条件再声称 PRM 满足条件，是 "先射箭后画靶"

【异常维度】:
- R1 单独指出 SARM (2508.08746) 和 SAFER (2507.00665) 两篇遗漏——其他两位未提及，降权处理（但不完全忽略，因为这两篇确实存在且相关）
- R2 单独指出 Locate-Steer-Improve survey (2601.14004) 和 MIB benchmark (ICML 2025) 遗漏——降权，但若确实存在，会进一步压缩"第一个结构化实证证据"的 claim
- R2 单独提出 cross-validated circuit taxonomy 的方法论质疑（三种方法测量的东西可能不同）——这是一个有效的 technical concern，虽只有 1 人提到，但论证逻辑成立，不完全降权

【最终概率】: [2% - 7%] 中位 4%（投 CoRL 2026）；[14% - 24%] 中位 18%（投合适 venue 如 NeurIPS/ICML/ICLR）

【一致性】: **高**（实质一致性）

说明：表面 std=6.5% 处于"中一致"区间，但分歧**完全来自 venue mismatch 的处理方式差异**，而非 idea 质量判断的分歧。R1 将 CoRL venue penalty 直接 bake 进概率（5%），R2/R3 给出 venue-adjusted 的 idea 质量概率（20%/17%）并另附 CoRL 估计。三位在以下维度**完全一致**：Novelty=弱、Significance=中、Related Work=中、CoRL=致命 mismatch。如果统一为 venue-adjusted 估计（R1 自述"若投 NeurIPS/ICML/ICLR 约 20-28%"，取中位 24%），三人中位为 [17%, 20%, 24%]，std≈2.9%，属于高一致。因此判定实质一致性为**高**。

【综合理由】:

**1. Idea 质量天花板（由 3/3 Novelty=弱 锁定）**：三位审稿人对 novelty 的判断完全收敛——Domain Amenability Hypothesis 的 tautological 性质是最大的 idea-level 风险。"在有 verifiable ground truth 的任务上干预更容易成功"不构成需要 extensive empirical validation 的 insight。加之 SteerRM + Basu et al. 已分别提供了成功/失败证据，本 proposal 的 novelty delta 主要是"把已有拼图放进同一个框架"——属于 organizational contribution 而非 conceptual breakthrough。Novelty=弱 将 idea 天花板锁定在 ~25% 以下。

**2. Significance 提供了有限的地板支撑**："When does mech interp work?" 的元问题确实有时效性和重要性，这是唯一阻止概率跌破 15% 的因素。但 3/3 审稿人均指出预期结果的 surprise value 低，限制了 significance 的上拉效果。

**3. CoRL venue mismatch 是独立的致命维度**：这不是 idea 质量问题，而是 scope 问题。CoRL 聚焦机器人学习、具身智能、操控、导航。本 proposal 无任何机器人/具身相关内容。三位审稿人一致判定此为 desk reject 级别风险。对 CoRL 的概率估计取三人的保守端，中位 4%。

**4. 对异常维度的处理**：R1 单独提到的 SARM/SAFER 遗漏、R2 单独提到的 survey/MIB 遗漏——这些虽是 outlier 但方向一致（均指向"更多先驱工作存在，进一步压缩 novelty"），不矛盾。综合效果是加固而非改变共识判断。

**5. 偏严原则的应用**：三人 venue-adjusted 中位为 17%-24%，综合时偏向更严格的 R3（17%），最终取中位 18%。

【建议】: **KILL**（若坚持投 CoRL 2026）/ **不推荐**（即使转投合适 venue，中位 18% 仍远低于推荐阈值）

具体建议：
- **立即放弃 CoRL 2026 投稿计划**，venue mismatch 是 100% 不可补救的
- 若转投 NeurIPS/ICML/ICLR，需根本性重构 novelty claim——当前的 "Domain Amenability Hypothesis" 需要从 N=2 post-hoc 描述升级为有预测力的理论框架（需更多 domain 验证），否则中位概率难以突破 25%
- 更现实的出路是降格为 workshop paper（如 ICML MechInterp Workshop），以 empirical study 定位投稿，放弃 general hypothesis claim

【实施评估】:
- **计算资源**: 中-高。需在 7B 参数模型（Qwen2.5-Math-7B、Math-Shepherd-Mistral-7B）的 activations 上从头训练 SAE，加上 1.5B 模型的 CLT attribution graphs 计算。估计需 4-8× A100 80GB，训练 SAE 约 2-4 天/模型/层，circuit tracing 约 1-2 周 GPU 时间。总 GPU 时长约 500-1000 A100-hours。
- **数据需求**: 公开数据集为主（PRM800K、MATH、GSM8K 等数学推理数据集），不需要私有数据。需构造 stylistic exploitation 对比样本（可自动化生成）。
- **人工介入**: 较低。主要在 circuit taxonomy 的定性标注和分类上需要人工判断（~1-2 人周），其余流程可自动化。
- **训练需求**: 需要训练——SAE 从头训练是核心方法论决策（非 fine-tuning 现有模型，而是训练新的 SAE 模块）。不需要训练 PRM 本身（使用现有 checkpoints）。
- **新 Benchmark**: 不需要构建全新 benchmark，但需要构造 granularity-by-criterion 评估矩阵，工作量约 2-3 人周。
- **预估周期**: 从启动到可投稿约 3-4 个月（SAE 训练 1 个月、circuit analysis 1 个月、intervention 实验 1 个月、写作 1 个月），假设有稳定的 4-8 GPU 集群访问。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce9c86bb-fe49-4495-82f3-cb25e7926509",
  "isSidechain": false,
  "requestId": "req_011CbD7VvPj3tPze2KB1BCD9",
  "type": "assistant",
  "uuid": "3880fac5-6dd1-44bb-a982-176ef2367872",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T7dHXCZ3qvyAFTYTn4NCTP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13914,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4266,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 13914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13914
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough research to do a thorough evaluation. Let me…",
  "leafUuid": "3880fac5-6dd1-44bb-a982-176ef2367872",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate mechanistic interventions on process reward models",
  "sessionId": "a2fa50b4-504f-4dde-b7d5-e0d34e4d03f1"
}
```

---
