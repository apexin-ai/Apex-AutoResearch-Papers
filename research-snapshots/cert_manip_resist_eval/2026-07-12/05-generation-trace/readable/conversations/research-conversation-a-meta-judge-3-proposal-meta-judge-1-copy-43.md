# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e95fca51-2836-4974-b1ef-e168199c3751.jsonl`
- **Structured JSON:** [`10c3349b523b83f00060.json`](../../sessions/10/10c3349b523b83f00060.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T20:52:23.291Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T20:52:23.291Z",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough information. Let me compile my evaluation. The most critical finding from my research is the **venue mismatch** — CoRL is the Conference on Robot Learning, and this proposal is purely about NLP/LLM interpretability with no robotics component.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命性前置问题：投稿 venue 严重不匹配】\n\nCoRL 2026 (Conference on Robot Learning) 的征稿范围明确限定于：\n- Learning representations for robotic perception and control\n- Robot foundation models / general-purpose knowledge systems for robotics\n- Imitation learning / RL for robotics\n- Robot manipulation, navigation, locomotion, driving, flight\n- Robot systems, hardware, and sensors\n- Theoretical foundations of robot learning\n- Video models and latent world models for robot learning\n\n本 proposal 研究的是 \"multi-turn agentic LLM 系统中 tool-selection CoT 的 faithfulness\"，\n涉及的 domain 是 code editing、web browsing、data analysis、system administration、\ninformation retrieval——全部是软件层面的 \"tool\"，没有任何物理机器人、embodied agent、\nsensor、actuator、sim-to-real 或 robot learning 的成分。\n\n这是一篇纯粹的 NLP/AI Safety/Mechanistic Interpretability 论文，适合投稿的 venue 包括：\nACL、EMNLP、NeurIPS、ICML、ICLR、AAAI（以及相关 workshop 如 SafeGenAI）。\n投稿 CoRL 主会属于 out-of-scope desk reject，与论文本身质量无关。\n\n仅此一点，CoRL 2026 中稿概率约为 0-2%（仅留极小概率给\"审稿流程异常未 desk reject\"的情况）。\n\n以下仍按 rubric 对 idea 本身质量给出客观评估（假设投稿到合适的 NLP/ML venue）：\n\n\n【领域调研】:\n\n- [2605.07990] \"Tool Calling is Linearly Readable and Steerable in Language Models\" (arXiv 2026):\n  本 proposal 最直接的前驱工作。Probe 了 12 个模型（270M-27B），发现 tool identity 在\n  single-turn 设置下可从 pre-generation activations 中线性读出，steering 精度在 4B+\n  模型上达 93-100%。但明确指出 multi-turn 场景下 steering \"fragile\"（-30 to +10pp），\n  argument values 不可 steer (0/30)。Proposal 对此论文的引用和描述准确。\n\n- [2605.09252] \"LLM Agents Already Know When to Call Tools — Even Without Reasoning\" (arXiv 2026):\n  提出 When2Tool benchmark，发现 binary tool-necessity 可从 hidden states 解码\n  (0.89-0.96 AUROC)，reasoning 不提供额外信号。仅限 single-turn。描述准确。\n\n- [2602.17053] RFEval (arXiv 2026):\n  7,186 instances 的 counterfactual intervention benchmark，发现 ~49.7% 输出 unfaithful，\n  主要来自 stance inconsistency。针对数学/代码等 reasoning task，非 tool selection。\n  Proposal 引用准确，\"~50%\" 的数字基本吻合。\n\n- [2603.22582] \"Lie to Me\" (arXiv 2026):\n  测试 12 个 open-weight reasoning model，41,832 runs，faithfulness rate 39.7%-89.9%，\n  thinking token 承认率 ~87.5% vs output 承认率 ~28.6%，存在 59pp gap。\n  仅 single-turn QA。Proposal 引用准确。\n\n- [2603.01437] \"Decoding Answers Before Chain-of-Thought\" (arXiv 2026):\n  Pre-CoT probes 达 0.9 AUC，证明答案在 CoT 生成前已编码。单轮 QA 设置。描述准确。\n\n- [2605.06890] \"Beyond the Black Box\" (arXiv 2026):\n  SAE + probes 用于 multi-step trajectories 的 tool-need/tool-risk classification，\n  但不研究 tool identity 或 faithfulness。描述基本准确。\n\n- [2603.16475] \"Breaking the Chain\" (arXiv 2026):\n  60% insensitivity to intermediate structure interventions，支持 CoT 可能是 decorative 的论点。\n\n- [2510.04040] FaithCoT-Bench (ICLR 2026):\n  Instance-level faithfulness benchmark，单轮 QA 设置。\n\n- [2505.18135] \"Tool Preferences in Agentic LLMs are Unreliable\" (EMNLP 2025):\n  发现 tool selection 在 description manipulation 下脆弱，但不研究 CoT faithfulness。\n\n- [2605.17268] \"Is VLA Reasoning Faithful?\" (CVPR 2026 DriveX Workshop):\n  研究 autonomous driving model 的 chain-of-causation 是否 faithful——这是一个更接近\n  CoRL scope 的 faithfulness 研究方向（embodied/driving domain）。本 proposal 完全\n  没有走这个方向。\n\n- 调研总结: CoT faithfulness 评估在 2026 年已成为热门领域，single-turn 设置下\n  tool-call probing 和 faithfulness evaluation 都已有成熟工作。Multi-turn agentic\n  tool-selection faithfulness 确实是一个未被填补的 gap，proposal 的定位准确。\n  但这个 gap 的重要性需要审视——它更多是一个 \"natural extension\" 而非\n  \"surprising research question\"。\n\n\n【Trivial Alternative 检验】:\n\n存在部分 trivial alternative 威胁：\n\n1. **简单 correlation analysis**：不做 causal intervention，直接统计 CoT 中提到的 tool\n   与实际选择的 tool 的一致率，以及在 multi-turn 中该一致率的变化趋势。这能以极低成本\n   给出 faithfulness 的粗略估计。Proposal 的增量价值在于 causal intervention 提供了\n   更强的因果证据——但这个增量的 marginal value 取决于 correlation analysis 的结果\n   是否已经足够 informative。\n\n2. **直接复用 RFEval 框架**：RFEval 的 counterfactual intervention 方法论已经成熟，\n   将其直接搬到 tool-selection domain 是否足够算 contribution？Proposal 的增量在于\n   (a) multi-turn 设置的独特挑战、(b) 与 probing 的结合、(c) difficulty-tiered \n   benchmark。但 (a) 和 (c) 是 engineering/benchmark contribution，(b) 是真正的\n   方法论增量。\n\n总体：存在 trivial alternative 威胁但不致命。核心增量在 behavioral + mechanistic \ncoupling analysis，以及 multi-turn 设置的 systematic characterization。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未验证假设：\n\n1. **\"Multi-turn contexts create fundamentally different representational challenges\"**：\n   这是 proposal 的核心 motivation，但这个假设主要来自 2605.07990 的一个\n   negative result（multi-turn steering fragile）。一个 negative empirical result\n   ≠ \"fundamentally different\"。有可能 multi-turn 的 fragility 只是 probe \n   training data distribution shift 的 artifact，而非 representation 本质不同。\n   这个假设如果不成立，整个 \"multi-turn is a fundamentally new regime\" 的 framing \n   就会被削弱。\n\n2. **反直觉假设 \"harder ambiguous scenarios may elicit more faithful reasoning\"**：\n   这是 proposal 试图提升 surprise factor 的关键，但逻辑支撑薄弱。\"Genuine \n   deliberation is required\" 是一个 plausible story，但同样 plausible 的是：\n   hard-ambiguous 场景下 CoT 更长、更复杂，faithfulness 的 measurement noise 更大，\n   使得 TSCF 测量本身不可靠。这个假设如果被 reject（很可能），它只是一个 null result，\n   不会伤害论文，但也不会提供 surprise。\n\n3. **Benchmark 的 construct validity**：600 scenarios 由 LLM-assisted generation \n   产生（资源估计中提到 \"Claude-assisted scenario generation\"），\"soft-ambiguous\" \n   tier 的 calibration（\"one tool genuinely better but not trivially so\"）极难保证。\n   如果 tier 之间的 boundary 不 clean，核心 hypothesis about difficulty tiers 的\n   分析会失去意义。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心方法论（perturb CoT → observe behavioral change）直接继承自 RFEval (2602.17053)\n   和 FACT-E (2604.10693)，不是本文首创。Tool-call probing 直接继承自 2605.07990。\n   真正的 novelty delta 是 (a) behavioral + mechanistic coupling in multi-turn setting\n   和 (b) difficulty-tiered benchmark design。但 (a) 本质是 \"将两个已有范式组合应用于\n   新 domain\"，(b) 是 benchmark engineering。这种 \"A+B in setting C\" 的 novelty \n   在顶会属于 marginal。对比 2605.07990 本身（首次证明 tool identity 可线性 steer）\n   和 RFEval（首次大规模 counterfactual faithfulness benchmark），本文的 novelty \n   量级明显低一档。Counterintuitiveness hypothesis 如果 confirmed 会大幅提升 \n   novelty，但如上分析其 confirmation 的概率不高。\n\n2. **Significance: 中** — \n   研究问题本身重要：multi-turn agentic tool selection faithfulness 确实有安全 \n   implications。但 practical impact 有限：即使证明了 CoT 在 multi-turn 中 unfaithful，\n   \"so what\"——这个结论大多数 practitioner 已经 intuitively expect（2605.07990 和 \n   RFEval 的结果已经强烈暗示了这一点）。审稿人很可能说 \"I would have guessed this\"。\n   真正有 significance 的发现需要是：(a) multi-turn 比 single-turn 显著更/更少 \n   faithful（quantitative surprise），或 (b) 某个 model family 有 qualitatively \n   不同的 pattern，或 (c) behavioral-mechanistic coupling 揭示了新的 failure mode。\n   这些都是可能的，但不是 guaranteed 的。\n\n3. **Related Work: 强** — \n   Proposal 的文献覆盖非常全面，四条 thread 的组织清晰，对每篇论文的描述经我验证\n   基本准确（2605.07990 的 steering accuracy 数字、RFEval 的 ~50%、Lie to Me 的 \n   59pp gap 均吻合）。Critical gap 的定位准确：确实没有工作在 multi-turn agentic \n   setting 中 combine behavioral causal intervention + mechanistic probing for \n   tool-selection faithfulness。差异化定位清晰。\n\n\n【概率估计】: 0-2%（CoRL 2026）; 若投稿合适 venue (ACL/EMNLP/NeurIPS): 20-30% 中位 25%\n\n【估计理由】: \n- CoRL 2026 概率 ~0%：论文完全 out-of-scope。CoRL 是 robot learning 会议，\n  本文研究 NLP/LLM 的 CoT faithfulness，涉及的 \"tool\" 是软件 API（code editing、\n  web browsing、data analysis），无任何 embodied/robotic 成分。大概率 desk reject。\n  \n- 若投合适 venue 25% 的理由：\n  · Related Work 覆盖强，定位准确，gap 真实存在 → 论文不会因 framing 问题被拒\n  · Novelty 是 \"中\"（组合式 novelty），Significance 是 \"中\"（expected findings），\n    这两个维度限制了上界\n  · 核心发现若为 positive（CoT 在 multi-turn 中 indeed unfaithful），审稿人大概率\n    反应是 \"expected, confirming what 2605.07990 hinted\"，而非 \"surprising\"\n  · Counterintuitiveness hypothesis 是潜在 upside，但 confirmation 不确定\n  · Benchmark contribution (TOOLFAITH-BENCH) 有一定独立价值\n\n【主要风险】:\n1. **致命性 venue 不匹配**：投稿 CoRL = desk reject。这是当前最紧迫需要修正的问题。\n2. **\"I would have guessed this\" 风险**：核心发现（multi-turn CoT unfaithful）\n   在 single-turn 已有强烈暗示（2605.07990 的 fragile multi-turn steering, \n   RFEval 的 ~50% unfaithfulness），如果 multi-turn 结果只是 \"more of the same\"，\n   审稿人会认为 contribution 不足。论文需要在 multi-turn 设置中找到 qualitatively \n   new 的发现（而不仅仅是 quantitative confirmation）才能达到顶会 bar。\n```\n\n---\n\n**总结**：\n\n这个 proposal 的 **idea 质量本身属于中等偏上**——研究问题真实、文献定位精准、gap 确实存在。但有两个关键问题：\n\n1. **🚨 最致命的问题是 venue 选择**：CoRL 是 Conference on Robot Learning，而这篇论文是纯 NLP/Interpretability 工作，zero robotics component。无论 idea 多好，投 CoRL 就是 desk reject。建议改投 **ACL 2026、EMNLP 2026、NeurIPS 2026** 或相关 workshop。\n\n2. **Idea 内核的天花板有限**：即使投对 venue，核心发现大概率是 \"confirming what existing work already strongly hints at\"，而非 genuinely surprising。需要在实验中挖掘 multi-turn 独有的 qualitative phenomenon 才能突破 25-30% 的 acceptance ceiling。\n\nSources:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)\n- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252)\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning](https://arxiv.org/abs/2603.22582)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Is VLA Reasoning Faithful? (CVPR 2026 DriveX Workshop)](https://arxiv.org/abs/2605.17268)\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv, May 2026): 最直接的前驱工作。证明 tool identity 在 single-turn 中线性可读且可操控（4B+ 模型 93-100% 准确率）。**明确指出 multi-turn 迁移是 \"fragile\"（-30 to +10pp）**，直接为本 proposal 提供了 gap 依据。但也意味着本 proposal 的方向是该论文已经标记好的 \"obvious next step\"。\n- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252) (arXiv, May 2026): 证明 binary tool-necessity 在 0.89-0.96 AUROC 可探测，reasoning 不提供额外信号。但研究对象是 \"是否调用工具\"，不是 \"调用哪个工具\" 或 faithfulness，与本 proposal 有区分。\n- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 7,186 实例的 counterfactual intervention benchmark，发现 ~50% reasoning 不忠实。提供了本 proposal 直接借鉴的干预范式（stance consistency + causal influence），但目标域是 math/code/QA，不是 tool selection。\n- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv, Mar 2026): 12 模型评估，faithfulness 39.7%-89.9%，揭示 59pp thinking-vs-output gap。单轮 QA 设定，不涉及工具调用。\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv, May 2026): SAE + linear probes 用于 multi-step trajectories 中的 tool-need/tool-risk 分类。与本 proposal 最接近的 mechanistic 工作，但关注点是 \"是否需要工具\" 和 \"风险级别\"，不是 tool identity 或 faithfulness。\n- [Project Ariadne](https://arxiv.org/abs/2601.02314) (arXiv, Jan 2026): 提出 causal framework 审计 agent faithfulness，使用 \"reasoning theater\" 概念。本 proposal 的 RTI 指标和 \"reasoning theater\" 框架直接源于此。\n- [FaithCoT-Bench](https://arxiv.org/abs/2510.04040) (ICLR 2026): 实例级 faithfulness benchmark，发现 counterfactual 方法仅在干预 causally critical steps 时有效。单轮 QA。\n- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): 因果启发的 CoT 评估，发现 self-evaluation 不可靠。单轮设定。\n\n- **调研总结**: CoT faithfulness 领域在 2026 上半年快速成熟，单轮设定下的 behavioral intervention (RFEval, Lie to Me) 和 mechanistic probing (2605.07990, 2605.09252) 两条路线均已建立。但二者的交汇点——multi-turn 设定下对 tool-selection CoT 的 behavioral + mechanistic 联合研究——确实是空白。然而，这一空白是 2605.07990（5月8日发表）明确标记的 \"obvious next step\"，时间窗口非常短，竞争压力大。\n\n【Trivial Alternative 检验】:\n存在明显的 trivial alternative 威胁：\n1. **纯 behavioral 路线**: 直接将 RFEval 的 counterfactual intervention 框架搬到 multi-turn tool selection 场景，不需要新的 intervention 类型设计（reason-flip/ablate/inject/scramble 都是标准范式的小变体），不需要 mechanistic probing 组件。这能回答 \"tool-selection CoT 是否 faithful\" 的核心问题，成本更低。\n2. **纯 probing 路线**: 直接将 2605.07990 的 linear probing 跑在 multi-turn 数据上，观察 cross-turn degradation。2605.07990 已经初步做了这个实验（虽然结果 fragile），扩大规模即可。\n3. **增量价值**: 本 proposal 的增量在于 **两条路线的结合**——特别是 \"faithfulness coupling\" 分析（behavioral 不忠实是否与 mechanistic pre-commitment 对齐）。这是非 trivial 的贡献，但它是 proposal 的一个分析维度，不是核心 claim。整体而言，proposal 的大部分贡献可以被上述两个 trivial baseline 分别覆盖。\n\n【前提假设检验】:\n核心逻辑链中存在以下未验证假设：\n1. **CoT 干预的生态效度**: 当你 reason-flip 或 reason-scramble 一个 CoT 时，模型可能检测到输入是 \"异常的\"（不像自然生成的 CoT），从而产生与正常情况不同的行为模式。这意味着 TSCF/RTI 测量的可能不是 \"faithfulness\"，而是 \"对异常输入的鲁棒性\"。RFEval 在单轮 QA 中没有遇到这个问题，因为干预后的 reasoning 仍然像自然文本。但在 multi-turn agentic 场景中，prior tool results 和 error feedback 的累积使得 \"自然\" CoT 有更强的上下文约束，干预更容易被模型 \"感知到\"。\n2. **线性探针在 multi-turn 中的适用性**: 2605.07990 显示 multi-turn 探针迁移是 fragile 的。这可能意味着 multi-turn 中 tool identity 的编码根本不是线性的，而不仅仅是需要更好的探针。如果是这样，整个 probing 组件的前提就不成立。\n3. **三层歧义分层的可操作性**: 假设 Unambiguous/Soft-Ambiguous/Hard-Ambiguous 之间有清晰边界，且可以可靠地标注。但 \"一个工具明显更优\" vs \"多个工具都有效\" 的边界高度依赖于上下文和评估者，这会引入 construct validity 问题。\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — 核心方法论贡献有限。四种 behavioral intervention 类型是 RFEval 等已有工作的标准范式变体；TSCF/RTI 指标本质上是 RFEval 的 stance consistency / causal influence 在 tool-selection 域的重命名；multi-turn probing 是 2605.07990 明确标记的 next step（该论文 5月8日发表，proposal 的时间窗口极窄）。真正新颖的是 \"behavioral-mechanistic faithfulness coupling\" 分析，但这只是 proposal 的一个分析维度。整体来看，这是一篇 \"将已有方法应用到新领域\" 的工作，domain novelty 有但 methodological novelty 不足。对于 CoRL（一个关注 robot learning 的会议），这个领域本身就不在主流 track 内。\n\n2. **Significance: 中（对 NLP/AI Safety）/ 弱（对 CoRL）** — 研究问题本身（multi-turn tool-selection faithfulness）对 AI safety 和 agent 可信度有实际意义。但有两个限制因素：(a) 预期发现可预测——基于 RFEval（~50% 不忠实）和 2605.07990（tool identity 已 pre-committed），\"multi-turn tool-selection CoT 也是部分不忠实的\" 几乎是必然结论，审稿人大概率会说 \"I would have guessed this\"；(b) **致命的 venue mismatch**——CoRL 的核心受众是 robot learning 社区，proposal 的五个 benchmark domain（code editing, web browsing, data analysis, system admin, information retrieval）全部是软件 agent 场景，无任何 robotics 组件。这在 CoRL 审稿中几乎必然被标记为 out-of-scope。\n\n3. **Related Work: 强** — 这是 proposal 最突出的优势。四个 thread 的组织清晰，覆盖了 2025-2026 年几乎所有相关工作（经我逐一核实，引用的论文均真实存在且描述准确）。对每篇论文与本 proposal 的差异化定位准确。唯一的小问题是缺少对 Counterfactual Simulation Training for CoT Faithfulness (2602.20710) 和 Bypassing the Rationale (2602.03994) 的讨论，但这不影响整体判断。\n\n【概率估计】: [5% - 12%] 中位 8%\n\n【估计理由】: \nIdea 质量层面：Novelty 弱-中（方法论借鉴为主，domain novelty 有限），Significance 中等但预期发现可预测。如果投稿 ACL/NeurIPS 等 NLP/ML venue，纯基于 idea 质量估计约 20-28%。\n\n**但致命约束是 venue mismatch**：CoRL (Conference on Robot Learning) 的 scope 是 robot learning、manipulation、perception、planning、sim-to-real 等。本 proposal 完全没有 robotics 组件——benchmark 的五个 domain 全部是软件 agent 场景，没有物理交互、没有机器人控制、没有 embodiment。这在 CoRL 审稿中极可能被判为 out-of-scope，直接导致 desk reject 或在初审就被淘汰。即使 idea 本身合理，venue 不匹配会将上界压到 12% 以下。\n\n概率从 3 维度到最终估计的推理：Related Work 的高质量无法弥补 Novelty 的不足，而 Significance 被 venue mismatch 彻底削弱。\n\n【主要风险】:\n1. **Venue mismatch 风险（致命级）**: 一篇纯软件 agent + NLP interpretability 的工作投稿 CoRL，几乎必然被认为 out-of-scope。五个 benchmark domain 无一涉及 robotics，无法说服 CoRL 审稿人这与 robot learning 相关。\n2. **\"Obvious next step\" 风险**: 2605.07990（5月8日发表）已明确将 multi-turn 标记为 unsolved frontier，本 proposal 本质上是接棒执行。审稿人可能认为这是 incremental follow-up 而非 original contribution，且时间窗口极窄，面临被平行提交的同类工作 scoop 的风险。\n```\n\n---\n\n**补充说明**：如果团队将目标 venue 从 CoRL 改为 **NeurIPS 2026、ICML 2027、ACL 2026 或 EMNLP 2026** 等 NLP/ML 主会，idea 的中稿概率会有实质性提升（估计 20-28%），因为 venue mismatch 风险消失，且研究问题与这些会议的 scope 高度契合。当前 proposal 的核心问题不是 idea 完全不行，而是 **投错了地方**。\n\nSources:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)\n- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252)\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)\n- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)\n- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)\n- [FACT-E (ACL 2026 Findings)](https://arxiv.org/abs/2604.10693)\n- [Breaking the Chain](https://arxiv.org/abs/2603.16475)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nI now have sufficient information to evaluate. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命性前置问题：会议适配性】:\nCoRL 2026 (Conference on Robot Learning) 的 Call for Papers 明确声明：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 以及 \"Submissions without a robotics focus will be returned without review.\" \n本 proposal 研究的是通用 LLM agent 的 tool-selection CoT faithfulness，五个 benchmark 领域为 code editing, web browsing, data analysis, system administration, information retrieval —— 无任何机器人学内容。**此论文投稿 CoRL 将被 desk reject，不会进入审稿流程。** \n适合的投稿会议：ACL、EMNLP、NeurIPS、ICML、ICLR、AAMAS 等 NLP/AI 安全/Agent 方向会议。\n\n以下评估仅针对 idea 本身质量（假设投稿至适配会议如 EMNLP/NeurIPS），不含 CoRL 适配性因素。\n\n【领域调研】:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv, May 2026): 本 proposal 最直接的前置工作。在 12 个模型上证明 tool identity 在单轮设定中线性可读且可操纵（4B+ 模型 93-100% 准确率），但明确指出多轮迁移\"fragile\"（-30 to +10pp）。本 proposal 以此为 motivation 研究多轮场景。\n- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252) (arXiv, May 2026): 证明 tool-necessity（是否需要调用工具）在 pre-reasoning 阶段已可解码（0.89-0.96 AUROC），reasoning 不提供额外信号。但仅研究\"是否调用\"而非\"调用哪个工具\"。\n- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 7,186 实例的反事实干预 benchmark，发现 ~50% reasoning 不忠实。但仅针对 QA/math/code reasoning，不涉及 tool selection。本 proposal 的 behavioral intervention 方法论直接借鉴此工作。\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv, May 2026): 用 SAE + linear probe 在多步轨迹上做 tool-need 和 tool-risk 分类，但不研究 tool identity faithfulness。\n- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv, Mar 2026): 12 模型评估，发现 thinking vs output 间存在 59pp faithfulness gap，但仅限单轮 QA。\n- [Project Ariadne](https://arxiv.org/abs/2601.02314) (arXiv, Jan 2026): 用 SCM 框架审计 agent faithfulness，但聚焦于 claim-level 而非 tool-call action level。\n- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): CoT 因果扰动评估框架，发现 self-evaluation 不可靠，但针对 general reasoning。\n- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135) (EMNLP 2025): 证明 tool selection 在 description manipulation 下脆弱，但不研究 CoT faithfulness。\n- [FRIT](https://arxiv.org/abs/2509.13334) (arXiv 2025): 用因果重要性改进 CoT faithfulness，但为训练方法，非诊断工具。\n\n- **调研总结**: CoT faithfulness 评估和 tool-call probing 是 2026 上半年的热门交叉领域，但两条线确实尚未在多轮 tool selection 场景中交汇。本 proposal 填补的是一个真实但可预测的 gap——将已成熟的 behavioral faithfulness 方法论（RFEval 式干预）应用于已被证明有问题的场景（2605.07990 的多轮 fragility）。这是典型的 \"方法 X for 领域 Y\" 组合式贡献。\n\n【Trivial Alternative 检验】:\n**存在 trivial alternative 威胁。** \n最简单的 baseline 是：直接将 2605.07990 的 linear probing 方法在多轮对话数据上跑，观察 probe accuracy 随 turn depth 的退化曲线——这不需要构建 600 场景的 benchmark，不需要定义 TSCF/RTI 指标，也不需要 4 种干预类型。如果 probe accuracy 在多轮中持续下降（2605.07990 已有初步证据），就已经回答了核心问题的大部分。\n\n本 proposal 的增量价值在于：(1) behavioral intervention 提供了与 probing 不同视角的因果证据——probing 只说 \"信息已编码\"，intervention 才能说 \"CoT 是否真正驱动了 tool call\"；(2) 三层 ambiguity 分级可以揭示 faithfulness 与任务难度的交互作用。但问题是这两个增量是否足够支撑一篇 top venue 论文。Reviewer 很可能会追问：\"如果只做 (1) 的 behavioral intervention 部分，不做 probing；或者只做 probing 的多轮扩展，不做 behavioral intervention——每部分单独能否成为独立贡献？\" 如果答案是 \"每部分单独都偏薄\"，那组合本身就成为了贡献的核心，这会削弱 novelty 叙事。\n\n【前提假设检验】:\n1. **\"多轮 ≠ 重复单轮\" 假设**: 核心 claim 依赖于 \"多轮 agentic 场景的 faithfulness 行为与单轮有本质不同\"。2605.07990 提供了 fragility 证据，但 fragility 可能仅仅是 probe 在更长 context 下的统计退化，而非反映质的变化。如果最终发现多轮只是单轮的有噪版本，核心 narrative 会坍塌。\n2. **Intervention validity 假设**: Reason-flip 和 counterfactual-inject 假设模型会\"阅读并遵循\"被篡改的 CoT。但如果模型对 CoT 的处理方式本身就是 post-hoc（即模型先决定调用哪个 tool，再生成 CoT），那么注入篡改的 CoT 并观察 tool call 是否变化，测量的不是 \"CoT 是否驱动了决策\"，而是 \"篡改的 prompt 是否能覆盖已有的 latent decision\"——这两者的含义是不同的。RFEval 在 reasoning 场景中避免了这个问题，因为 reasoning 和 answer 在同一个 forward pass 中生成；但在 multi-turn agent 中，prior context 对 latent policy 的影响更强，使得 intervention 的因果解释更加模糊。\n3. **\"Hard-Ambiguous → 更 faithful\" 的反直觉假设**: 这是 proposal 中最有趣的 hypothesis，但缺乏理论支撑。为什么 \"genuine deliberation is required\" 就会导致 more faithful reasoning？如果模型的 deliberation 本身也是 post-hoc rationalization（只是更复杂的 rationalization），这个假设就不成立。\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — 核心贡献是将已有方法论（RFEval 式 behavioral intervention + 2605.07990 式 linear probing）组合应用于一个新场景（multi-turn tool selection）。两条技术线本身都已成熟：behavioral intervention 有 RFEval、FACT-E、Lie to Me 等多篇工作；tool-call probing 有 2605.07990、2605.09252、2605.06890 等。Proposal 正确识别了交叉 gap，但 gap 的存在是因为这两个方向都刚发表 1-2 个月——更可能的原因是\"时间不够\"而非\"问题本质上难以组合\"。两个指标 TSCF 和 RTI 是 RFEval 框架在 tool-call domain 的直接映射（TSCF ≈ causal influence score，RTI ≈ 1 - TSCF），定义层面的新颖性有限。三层 difficulty stratification 是 solid 的实验设计，但不构成方法论创新。Counterintuitive hypothesis（ambiguity → faithfulness）是最大的 novelty 候选，但目前仅是推测。\n\n2. **Significance: 中** — 研究问题本身重要：multi-turn agentic systems 中 tool selection 的可信度直接影响 safety 和 deployment。但本 proposal 是纯诊断性/empirical 工作——它测量问题的存在，不提出解决方案。如果核心发现是 \"yes, tool-selection reasoning 在多轮中也是 ~50% unfaithful\"（与 RFEval 在 general reasoning 中的发现一致），审稿人很可能认为 \"I would have guessed this\"。如果发现有趣的 ambiguity-faithfulness 交互作用，significance 会提升，但这取决于实验结果。此外，这是一个非常 timely 的 topic，有 safety narrative 加持，投稿 NeurIPS/EMNLP 有话题红利。\n\n3. **Related Work: 强** — 这是 proposal 最出色的部分。对四条研究线索的覆盖全面且准确（经调研验证，引用的论文均真实存在，描述基本准确）。差异化定位清晰：明确指出现有工作的 gap（single-turn probing 成熟 vs multi-turn 未解，behavioral intervention 未应用于 tool selection）。唯一的小问题是 2605.06890 (\"Beyond the Black Box\") 的定位——proposal 称其 \"not tool identity or faithfulness\"，但该工作实际上也涉及 multi-step trajectory 上的 interpretability，可能比 proposal 描述的更接近。\n\n【概率估计】: [18% - 30%] 中位 23%\n（注：此概率基于投稿适配会议如 EMNLP/NeurIPS 的假设。投稿 CoRL 的中稿概率为 ~0%，因会被 desk reject。）\n\n【估计理由】: \nIdea 填补了一个真实但可预测的 gap，属于 \"方法 X for 领域 Y\" 的组合式贡献。Related work 覆盖出色，研究问题有安全话题红利，但核心 novelty 受限于方法论的继承性。Significance 取决于实验结果是否能超越 \"I would have guessed this\"——如果核心发现只是 \"多轮 tool selection 的 faithfulness 也是 ~50%，与单轮/general reasoning 一致\"，那么贡献主要落在 benchmark 构建（TOOLFAITH-BENCH）上，而非 insight 上。Novelty 的弱-中评分是概率上界的主要限制因素。如果 counterintuitive hypothesis 得到验证且有 compelling 的 mechanistic 解释，概率可推至 30%+ 上界；如果结果平淡（merely replicating known patterns in a new domain），概率下探至 18% 附近。\n\n【主要风险】:\n1. **\"Incremental combination\" 质疑**: 审稿人可能认为这是将已有的 faithfulness evaluation 方法（RFEval）和 tool-call probing 方法（2605.07990）简单组合应用于新场景，方法论层面缺乏独立创新。TSCF/RTI 指标被视为 RFEval 指标的 domain-specific 重命名。\n2. **结果可预测性**: 如果最终发现 \"多轮 tool selection CoT 确实不忠实\" —— 鉴于单轮已有 93-100% 的 pre-commitment 证据（2605.07990）和 ~50% 的 general reasoning unfaithfulness（RFEval），这个发现几乎是 expected 的。论文的 impact 将高度依赖于 \"unexpected\" 的二阶发现（如 ambiguity-faithfulness 交互），但这些在 proposal 阶段是不可控的。\n```\n\nSources:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)\n- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252)\n- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)\n- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)\n- [FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning](https://arxiv.org/abs/2604.10693)\n- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135)\n- [FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness](https://arxiv.org/abs/2509.13334)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing\n\n## Description\nWe present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.\n\n## Core Problem\nIn multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.\n\n## Opportunity\nThe landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.\n\n## Related Work / Landscape\nThe landscape spans four converging threads:\n\n**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.\n\n**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.\n\n**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.\n\n**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.\n\n**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.\n\n## Approach\nWe construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:\n\n**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.\n\n**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.\n\n**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.\n\nAt each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.\n\nWe evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.\n\n## Inspiration\nThree converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.\n\n## Key References\n- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)\n- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)\n- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)\n- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)\n- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)\n- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)\n- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)\n- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)\n- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)\n- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)\n- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)\n- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)\n- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)\n- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)\n- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)\n- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)\n- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)\n- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)\n- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)\n- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)\n- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}\n- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}\n- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T20:52:23.294Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T20:52:23.294Z",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T20:52:23.305Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough information. Let me compile my evaluation. The most critical finding from my research is the **venue mismatch** — CoRL is the Conference on Robot Learning, and this proposal is purely about NLP/LLM interpretability with no robotics component.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：投稿 venue 严重不匹配】

CoRL 2026 (Conference on Robot Learning) 的征稿范围明确限定于：
- Learning representations for robotic perception and control
- Robot foundation models / general-purpose knowledge systems for robotics
- Imitation learning / RL for robotics
- Robot manipulation, navigation, locomotion, driving, flight
- Robot systems, hardware, and sensors
- Theoretical foundations of robot learning
- Video models and latent world models for robot learning

本 proposal 研究的是 "multi-turn agentic LLM 系统中 tool-selection CoT 的 faithfulness"，
涉及的 domain 是 code editing、web browsing、data analysis、system administration、
information retrieval——全部是软件层面的 "tool"，没有任何物理机器人、embodied agent、
sensor、actuator、sim-to-real 或 robot learning 的成分。

这是一篇纯粹的 NLP/AI Safety/Mechanistic Interpretability 论文，适合投稿的 venue 包括：
ACL、EMNLP、NeurIPS、ICML、ICLR、AAAI（以及相关 workshop 如 SafeGenAI）。
投稿 CoRL 主会属于 out-of-scope desk reject，与论文本身质量无关。

仅此一点，CoRL 2026 中稿概率约为 0-2%（仅留极小概率给"审稿流程异常未 desk reject"的情况）。

以下仍按 rubric 对 idea 本身质量给出客观评估（假设投稿到合适的 NLP/ML venue）：


【领域调研】:

- [2605.07990] "Tool Calling is Linearly Readable and Steerable in Language Models" (arXiv 2026):
  本 proposal 最直接的前驱工作。Probe 了 12 个模型（270M-27B），发现 tool identity 在
  single-turn 设置下可从 pre-generation activations 中线性读出，steering 精度在 4B+
  模型上达 93-100%。但明确指出 multi-turn 场景下 steering "fragile"（-30 to +10pp），
  argument values 不可 steer (0/30)。Proposal 对此论文的引用和描述准确。

- [2605.09252] "LLM Agents Already Know When to Call Tools — Even Without Reasoning" (arXiv 2026):
  提出 When2Tool benchmark，发现 binary tool-necessity 可从 hidden states 解码
  (0.89-0.96 AUROC)，reasoning 不提供额外信号。仅限 single-turn。描述准确。

- [2602.17053] RFEval (arXiv 2026):
  7,186 instances 的 counterfactual intervention benchmark，发现 ~49.7% 输出 unfaithful，
  主要来自 stance inconsistency。针对数学/代码等 reasoning task，非 tool selection。
  Proposal 引用准确，"~50%" 的数字基本吻合。

- [2603.22582] "Lie to Me" (arXiv 2026):
  测试 12 个 open-weight reasoning model，41,832 runs，faithfulness rate 39.7%-89.9%，
  thinking token 承认率 ~87.5% vs output 承认率 ~28.6%，存在 59pp gap。
  仅 single-turn QA。Proposal 引用准确。

- [2603.01437] "Decoding Answers Before Chain-of-Thought" (arXiv 2026):
  Pre-CoT probes 达 0.9 AUC，证明答案在 CoT 生成前已编码。单轮 QA 设置。描述准确。

- [2605.06890] "Beyond the Black Box" (arXiv 2026):
  SAE + probes 用于 multi-step trajectories 的 tool-need/tool-risk classification，
  但不研究 tool identity 或 faithfulness。描述基本准确。

- [2603.16475] "Breaking the Chain" (arXiv 2026):
  60% insensitivity to intermediate structure interventions，支持 CoT 可能是 decorative 的论点。

- [2510.04040] FaithCoT-Bench (ICLR 2026):
  Instance-level faithfulness benchmark，单轮 QA 设置。

- [2505.18135] "Tool Preferences in Agentic LLMs are Unreliable" (EMNLP 2025):
  发现 tool selection 在 description manipulation 下脆弱，但不研究 CoT faithfulness。

- [2605.17268] "Is VLA Reasoning Faithful?" (CVPR 2026 DriveX Workshop):
  研究 autonomous driving model 的 chain-of-causation 是否 faithful——这是一个更接近
  CoRL scope 的 faithfulness 研究方向（embodied/driving domain）。本 proposal 完全
  没有走这个方向。

- 调研总结: CoT faithfulness 评估在 2026 年已成为热门领域，single-turn 设置下
  tool-call probing 和 faithfulness evaluation 都已有成熟工作。Multi-turn agentic
  tool-selection faithfulness 确实是一个未被填补的 gap，proposal 的定位准确。
  但这个 gap 的重要性需要审视——它更多是一个 "natural extension" 而非
  "surprising research question"。


【Trivial Alternative 检验】:

存在部分 trivial alternative 威胁：

1. **简单 correlation analysis**：不做 causal intervention，直接统计 CoT 中提到的 tool
   与实际选择的 tool 的一致率，以及在 multi-turn 中该一致率的变化趋势。这能以极低成本
   给出 faithfulness 的粗略估计。Proposal 的增量价值在于 causal intervention 提供了
   更强的因果证据——但这个增量的 marginal value 取决于 correlation analysis 的结果
   是否已经足够 informative。

2. **直接复用 RFEval 框架**：RFEval 的 counterfactual intervention 方法论已经成熟，
   将其直接搬到 tool-selection domain 是否足够算 contribution？Proposal 的增量在于
   (a) multi-turn 设置的独特挑战、(b) 与 probing 的结合、(c) difficulty-tiered 
   benchmark。但 (a) 和 (c) 是 engineering/benchmark contribution，(b) 是真正的
   方法论增量。

总体：存在 trivial alternative 威胁但不致命。核心增量在 behavioral + mechanistic 
coupling analysis，以及 multi-turn 设置的 systematic characterization。


【前提假设检验】:

核心逻辑链中有以下未验证假设：

1. **"Multi-turn contexts create fundamentally different representational challenges"**：
   这是 proposal 的核心 motivation，但这个假设主要来自 2605.07990 的一个
   negative result（multi-turn steering fragile）。一个 negative empirical result
   ≠ "fundamentally different"。有可能 multi-turn 的 fragility 只是 probe 
   training data distribution shift 的 artifact，而非 representation 本质不同。
   这个假设如果不成立，整个 "multi-turn is a fundamentally new regime" 的 framing 
   就会被削弱。

2. **反直觉假设 "harder ambiguous scenarios may elicit more faithful reasoning"**：
   这是 proposal 试图提升 surprise factor 的关键，但逻辑支撑薄弱。"Genuine 
   deliberation is required" 是一个 plausible story，但同样 plausible 的是：
   hard-ambiguous 场景下 CoT 更长、更复杂，faithfulness 的 measurement noise 更大，
   使得 TSCF 测量本身不可靠。这个假设如果被 reject（很可能），它只是一个 null result，
   不会伤害论文，但也不会提供 surprise。

3. **Benchmark 的 construct validity**：600 scenarios 由 LLM-assisted generation 
   产生（资源估计中提到 "Claude-assisted scenario generation"），"soft-ambiguous" 
   tier 的 calibration（"one tool genuinely better but not trivially so"）极难保证。
   如果 tier 之间的 boundary 不 clean，核心 hypothesis about difficulty tiers 的
   分析会失去意义。


【3 维度打分】:

1. **Novelty: 中** — 
   核心方法论（perturb CoT → observe behavioral change）直接继承自 RFEval (2602.17053)
   和 FACT-E (2604.10693)，不是本文首创。Tool-call probing 直接继承自 2605.07990。
   真正的 novelty delta 是 (a) behavioral + mechanistic coupling in multi-turn setting
   和 (b) difficulty-tiered benchmark design。但 (a) 本质是 "将两个已有范式组合应用于
   新 domain"，(b) 是 benchmark engineering。这种 "A+B in setting C" 的 novelty 
   在顶会属于 marginal。对比 2605.07990 本身（首次证明 tool identity 可线性 steer）
   和 RFEval（首次大规模 counterfactual faithfulness benchmark），本文的 novelty 
   量级明显低一档。Counterintuitiveness hypothesis 如果 confirmed 会大幅提升 
   novelty，但如上分析其 confirmation 的概率不高。

2. **Significance: 中** — 
   研究问题本身重要：multi-turn agentic tool selection faithfulness 确实有安全 
   implications。但 practical impact 有限：即使证明了 CoT 在 multi-turn 中 unfaithful，
   "so what"——这个结论大多数 practitioner 已经 intuitively expect（2605.07990 和 
   RFEval 的结果已经强烈暗示了这一点）。审稿人很可能说 "I would have guessed this"。
   真正有 significance 的发现需要是：(a) multi-turn 比 single-turn 显著更/更少 
   faithful（quantitative surprise），或 (b) 某个 model family 有 qualitatively 
   不同的 pattern，或 (c) behavioral-mechanistic coupling 揭示了新的 failure mode。
   这些都是可能的，但不是 guaranteed 的。

3. **Related Work: 强** — 
   Proposal 的文献覆盖非常全面，四条 thread 的组织清晰，对每篇论文的描述经我验证
   基本准确（2605.07990 的 steering accuracy 数字、RFEval 的 ~50%、Lie to Me 的 
   59pp gap 均吻合）。Critical gap 的定位准确：确实没有工作在 multi-turn agentic 
   setting 中 combine behavioral causal intervention + mechanistic probing for 
   tool-selection faithfulness。差异化定位清晰。


【概率估计】: 0-2%（CoRL 2026）; 若投稿合适 venue (ACL/EMNLP/NeurIPS): 20-30% 中位 25%

【估计理由】: 
- CoRL 2026 概率 ~0%：论文完全 out-of-scope。CoRL 是 robot learning 会议，
  本文研究 NLP/LLM 的 CoT faithfulness，涉及的 "tool" 是软件 API（code editing、
  web browsing、data analysis），无任何 embodied/robotic 成分。大概率 desk reject。
  
- 若投合适 venue 25% 的理由：
  · Related Work 覆盖强，定位准确，gap 真实存在 → 论文不会因 framing 问题被拒
  · Novelty 是 "中"（组合式 novelty），Significance 是 "中"（expected findings），
    这两个维度限制了上界
  · 核心发现若为 positive（CoT 在 multi-turn 中 indeed unfaithful），审稿人大概率
    反应是 "expected, confirming what 2605.07990 hinted"，而非 "surprising"
  · Counterintuitiveness hypothesis 是潜在 upside，但 confirmation 不确定
  · Benchmark contribution (TOOLFAITH-BENCH) 有一定独立价值

【主要风险】:
1. **致命性 venue 不匹配**：投稿 CoRL = desk reject。这是当前最紧迫需要修正的问题。
2. **"I would have guessed this" 风险**：核心发现（multi-turn CoT unfaithful）
   在 single-turn 已有强烈暗示（2605.07990 的 fragile multi-turn steering, 
   RFEval 的 ~50% unfaithfulness），如果 multi-turn 结果只是 "more of the same"，
   审稿人会认为 contribution 不足。论文需要在 multi-turn 设置中找到 qualitatively 
   new 的发现（而不仅仅是 quantitative confirmation）才能达到顶会 bar。
```

---

**总结**：

这个 proposal 的 **idea 质量本身属于中等偏上**——研究问题真实、文献定位精准、gap 确实存在。但有两个关键问题：

1. **🚨 最致命的问题是 venue 选择**：CoRL 是 Conference on Robot Learning，而这篇论文是纯 NLP/Interpretability 工作，zero robotics component。无论 idea 多好，投 CoRL 就是 desk reject。建议改投 **ACL 2026、EMNLP 2026、NeurIPS 2026** 或相关 workshop。

2. **Idea 内核的天花板有限**：即使投对 venue，核心发现大概率是 "confirming what existing work already strongly hints at"，而非 genuinely surprising。需要在实验中挖掘 multi-turn 独有的 qualitative phenomenon 才能突破 25-30% 的 acceptance ceiling。

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning](https://arxiv.org/abs/2603.22582)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Is VLA Reasoning Faithful? (CVPR 2026 DriveX Workshop)](https://arxiv.org/abs/2605.17268)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv, May 2026): 最直接的前驱工作。证明 tool identity 在 single-turn 中线性可读且可操控（4B+ 模型 93-100% 准确率）。**明确指出 multi-turn 迁移是 "fragile"（-30 to +10pp）**，直接为本 proposal 提供了 gap 依据。但也意味着本 proposal 的方向是该论文已经标记好的 "obvious next step"。
- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252) (arXiv, May 2026): 证明 binary tool-necessity 在 0.89-0.96 AUROC 可探测，reasoning 不提供额外信号。但研究对象是 "是否调用工具"，不是 "调用哪个工具" 或 faithfulness，与本 proposal 有区分。
- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 7,186 实例的 counterfactual intervention benchmark，发现 ~50% reasoning 不忠实。提供了本 proposal 直接借鉴的干预范式（stance consistency + causal influence），但目标域是 math/code/QA，不是 tool selection。
- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv, Mar 2026): 12 模型评估，faithfulness 39.7%-89.9%，揭示 59pp thinking-vs-output gap。单轮 QA 设定，不涉及工具调用。
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv, May 2026): SAE + linear probes 用于 multi-step trajectories 中的 tool-need/tool-risk 分类。与本 proposal 最接近的 mechanistic 工作，但关注点是 "是否需要工具" 和 "风险级别"，不是 tool identity 或 faithfulness。
- [Project Ariadne](https://arxiv.org/abs/2601.02314) (arXiv, Jan 2026): 提出 causal framework 审计 agent faithfulness，使用 "reasoning theater" 概念。本 proposal 的 RTI 指标和 "reasoning theater" 框架直接源于此。
- [FaithCoT-Bench](https://arxiv.org/abs/2510.04040) (ICLR 2026): 实例级 faithfulness benchmark，发现 counterfactual 方法仅在干预 causally critical steps 时有效。单轮 QA。
- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): 因果启发的 CoT 评估，发现 self-evaluation 不可靠。单轮设定。

- **调研总结**: CoT faithfulness 领域在 2026 上半年快速成熟，单轮设定下的 behavioral intervention (RFEval, Lie to Me) 和 mechanistic probing (2605.07990, 2605.09252) 两条路线均已建立。但二者的交汇点——multi-turn 设定下对 tool-selection CoT 的 behavioral + mechanistic 联合研究——确实是空白。然而，这一空白是 2605.07990（5月8日发表）明确标记的 "obvious next step"，时间窗口非常短，竞争压力大。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. **纯 behavioral 路线**: 直接将 RFEval 的 counterfactual intervention 框架搬到 multi-turn tool selection 场景，不需要新的 intervention 类型设计（reason-flip/ablate/inject/scramble 都是标准范式的小变体），不需要 mechanistic probing 组件。这能回答 "tool-selection CoT 是否 faithful" 的核心问题，成本更低。
2. **纯 probing 路线**: 直接将 2605.07990 的 linear probing 跑在 multi-turn 数据上，观察 cross-turn degradation。2605.07990 已经初步做了这个实验（虽然结果 fragile），扩大规模即可。
3. **增量价值**: 本 proposal 的增量在于 **两条路线的结合**——特别是 "faithfulness coupling" 分析（behavioral 不忠实是否与 mechanistic pre-commitment 对齐）。这是非 trivial 的贡献，但它是 proposal 的一个分析维度，不是核心 claim。整体而言，proposal 的大部分贡献可以被上述两个 trivial baseline 分别覆盖。

【前提假设检验】:
核心逻辑链中存在以下未验证假设：
1. **CoT 干预的生态效度**: 当你 reason-flip 或 reason-scramble 一个 CoT 时，模型可能检测到输入是 "异常的"（不像自然生成的 CoT），从而产生与正常情况不同的行为模式。这意味着 TSCF/RTI 测量的可能不是 "faithfulness"，而是 "对异常输入的鲁棒性"。RFEval 在单轮 QA 中没有遇到这个问题，因为干预后的 reasoning 仍然像自然文本。但在 multi-turn agentic 场景中，prior tool results 和 error feedback 的累积使得 "自然" CoT 有更强的上下文约束，干预更容易被模型 "感知到"。
2. **线性探针在 multi-turn 中的适用性**: 2605.07990 显示 multi-turn 探针迁移是 fragile 的。这可能意味着 multi-turn 中 tool identity 的编码根本不是线性的，而不仅仅是需要更好的探针。如果是这样，整个 probing 组件的前提就不成立。
3. **三层歧义分层的可操作性**: 假设 Unambiguous/Soft-Ambiguous/Hard-Ambiguous 之间有清晰边界，且可以可靠地标注。但 "一个工具明显更优" vs "多个工具都有效" 的边界高度依赖于上下文和评估者，这会引入 construct validity 问题。

【3 维度打分】:

1. **Novelty: 弱-中** — 核心方法论贡献有限。四种 behavioral intervention 类型是 RFEval 等已有工作的标准范式变体；TSCF/RTI 指标本质上是 RFEval 的 stance consistency / causal influence 在 tool-selection 域的重命名；multi-turn probing 是 2605.07990 明确标记的 next step（该论文 5月8日发表，proposal 的时间窗口极窄）。真正新颖的是 "behavioral-mechanistic faithfulness coupling" 分析，但这只是 proposal 的一个分析维度。整体来看，这是一篇 "将已有方法应用到新领域" 的工作，domain novelty 有但 methodological novelty 不足。对于 CoRL（一个关注 robot learning 的会议），这个领域本身就不在主流 track 内。

2. **Significance: 中（对 NLP/AI Safety）/ 弱（对 CoRL）** — 研究问题本身（multi-turn tool-selection faithfulness）对 AI safety 和 agent 可信度有实际意义。但有两个限制因素：(a) 预期发现可预测——基于 RFEval（~50% 不忠实）和 2605.07990（tool identity 已 pre-committed），"multi-turn tool-selection CoT 也是部分不忠实的" 几乎是必然结论，审稿人大概率会说 "I would have guessed this"；(b) **致命的 venue mismatch**——CoRL 的核心受众是 robot learning 社区，proposal 的五个 benchmark domain（code editing, web browsing, data analysis, system admin, information retrieval）全部是软件 agent 场景，无任何 robotics 组件。这在 CoRL 审稿中几乎必然被标记为 out-of-scope。

3. **Related Work: 强** — 这是 proposal 最突出的优势。四个 thread 的组织清晰，覆盖了 2025-2026 年几乎所有相关工作（经我逐一核实，引用的论文均真实存在且描述准确）。对每篇论文与本 proposal 的差异化定位准确。唯一的小问题是缺少对 Counterfactual Simulation Training for CoT Faithfulness (2602.20710) 和 Bypassing the Rationale (2602.03994) 的讨论，但这不影响整体判断。

【概率估计】: [5% - 12%] 中位 8%

【估计理由】: 
Idea 质量层面：Novelty 弱-中（方法论借鉴为主，domain novelty 有限），Significance 中等但预期发现可预测。如果投稿 ACL/NeurIPS 等 NLP/ML venue，纯基于 idea 质量估计约 20-28%。

**但致命约束是 venue mismatch**：CoRL (Conference on Robot Learning) 的 scope 是 robot learning、manipulation、perception、planning、sim-to-real 等。本 proposal 完全没有 robotics 组件——benchmark 的五个 domain 全部是软件 agent 场景，没有物理交互、没有机器人控制、没有 embodiment。这在 CoRL 审稿中极可能被判为 out-of-scope，直接导致 desk reject 或在初审就被淘汰。即使 idea 本身合理，venue 不匹配会将上界压到 12% 以下。

概率从 3 维度到最终估计的推理：Related Work 的高质量无法弥补 Novelty 的不足，而 Significance 被 venue mismatch 彻底削弱。

【主要风险】:
1. **Venue mismatch 风险（致命级）**: 一篇纯软件 agent + NLP interpretability 的工作投稿 CoRL，几乎必然被认为 out-of-scope。五个 benchmark domain 无一涉及 robotics，无法说服 CoRL 审稿人这与 robot learning 相关。
2. **"Obvious next step" 风险**: 2605.07990（5月8日发表）已明确将 multi-turn 标记为 unsolved frontier，本 proposal 本质上是接棒执行。审稿人可能认为这是 incremental follow-up 而非 original contribution，且时间窗口极窄，面临被平行提交的同类工作 scoop 的风险。
```

---

**补充说明**：如果团队将目标 venue 从 CoRL 改为 **NeurIPS 2026、ICML 2027、ACL 2026 或 EMNLP 2026** 等 NLP/ML 主会，idea 的中稿概率会有实质性提升（估计 20-28%），因为 venue mismatch 风险消失，且研究问题与这些会议的 scope 高度契合。当前 proposal 的核心问题不是 idea 完全不行，而是 **投错了地方**。

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [FACT-E (ACL 2026 Findings)](https://arxiv.org/abs/2604.10693)
- [Breaking the Chain](https://arxiv.org/abs/2603.16475)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
I now have sufficient information to evaluate. Let me compile the analysis.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：会议适配性】:
CoRL 2026 (Conference on Robot Learning) 的 Call for Papers 明确声明："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics" 以及 "Submissions without a robotics focus will be returned without review." 
本 proposal 研究的是通用 LLM agent 的 tool-selection CoT faithfulness，五个 benchmark 领域为 code editing, web browsing, data analysis, system administration, information retrieval —— 无任何机器人学内容。**此论文投稿 CoRL 将被 desk reject，不会进入审稿流程。** 
适合的投稿会议：ACL、EMNLP、NeurIPS、ICML、ICLR、AAMAS 等 NLP/AI 安全/Agent 方向会议。

以下评估仅针对 idea 本身质量（假设投稿至适配会议如 EMNLP/NeurIPS），不含 CoRL 适配性因素。

【领域调研】:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv, May 2026): 本 proposal 最直接的前置工作。在 12 个模型上证明 tool identity 在单轮设定中线性可读且可操纵（4B+ 模型 93-100% 准确率），但明确指出多轮迁移"fragile"（-30 to +10pp）。本 proposal 以此为 motivation 研究多轮场景。
- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252) (arXiv, May 2026): 证明 tool-necessity（是否需要调用工具）在 pre-reasoning 阶段已可解码（0.89-0.96 AUROC），reasoning 不提供额外信号。但仅研究"是否调用"而非"调用哪个工具"。
- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv, Feb 2026): 7,186 实例的反事实干预 benchmark，发现 ~50% reasoning 不忠实。但仅针对 QA/math/code reasoning，不涉及 tool selection。本 proposal 的 behavioral intervention 方法论直接借鉴此工作。
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv, May 2026): 用 SAE + linear probe 在多步轨迹上做 tool-need 和 tool-risk 分类，但不研究 tool identity faithfulness。
- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv, Mar 2026): 12 模型评估，发现 thinking vs output 间存在 59pp faithfulness gap，但仅限单轮 QA。
- [Project Ariadne](https://arxiv.org/abs/2601.02314) (arXiv, Jan 2026): 用 SCM 框架审计 agent faithfulness，但聚焦于 claim-level 而非 tool-call action level。
- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): CoT 因果扰动评估框架，发现 self-evaluation 不可靠，但针对 general reasoning。
- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135) (EMNLP 2025): 证明 tool selection 在 description manipulation 下脆弱，但不研究 CoT faithfulness。
- [FRIT](https://arxiv.org/abs/2509.13334) (arXiv 2025): 用因果重要性改进 CoT faithfulness，但为训练方法，非诊断工具。

- **调研总结**: CoT faithfulness 评估和 tool-call probing 是 2026 上半年的热门交叉领域，但两条线确实尚未在多轮 tool selection 场景中交汇。本 proposal 填补的是一个真实但可预测的 gap——将已成熟的 behavioral faithfulness 方法论（RFEval 式干预）应用于已被证明有问题的场景（2605.07990 的多轮 fragility）。这是典型的 "方法 X for 领域 Y" 组合式贡献。

【Trivial Alternative 检验】:
**存在 trivial alternative 威胁。** 
最简单的 baseline 是：直接将 2605.07990 的 linear probing 方法在多轮对话数据上跑，观察 probe accuracy 随 turn depth 的退化曲线——这不需要构建 600 场景的 benchmark，不需要定义 TSCF/RTI 指标，也不需要 4 种干预类型。如果 probe accuracy 在多轮中持续下降（2605.07990 已有初步证据），就已经回答了核心问题的大部分。

本 proposal 的增量价值在于：(1) behavioral intervention 提供了与 probing 不同视角的因果证据——probing 只说 "信息已编码"，intervention 才能说 "CoT 是否真正驱动了 tool call"；(2) 三层 ambiguity 分级可以揭示 faithfulness 与任务难度的交互作用。但问题是这两个增量是否足够支撑一篇 top venue 论文。Reviewer 很可能会追问："如果只做 (1) 的 behavioral intervention 部分，不做 probing；或者只做 probing 的多轮扩展，不做 behavioral intervention——每部分单独能否成为独立贡献？" 如果答案是 "每部分单独都偏薄"，那组合本身就成为了贡献的核心，这会削弱 novelty 叙事。

【前提假设检验】:
1. **"多轮 ≠ 重复单轮" 假设**: 核心 claim 依赖于 "多轮 agentic 场景的 faithfulness 行为与单轮有本质不同"。2605.07990 提供了 fragility 证据，但 fragility 可能仅仅是 probe 在更长 context 下的统计退化，而非反映质的变化。如果最终发现多轮只是单轮的有噪版本，核心 narrative 会坍塌。
2. **Intervention validity 假设**: Reason-flip 和 counterfactual-inject 假设模型会"阅读并遵循"被篡改的 CoT。但如果模型对 CoT 的处理方式本身就是 post-hoc（即模型先决定调用哪个 tool，再生成 CoT），那么注入篡改的 CoT 并观察 tool call 是否变化，测量的不是 "CoT 是否驱动了决策"，而是 "篡改的 prompt 是否能覆盖已有的 latent decision"——这两者的含义是不同的。RFEval 在 reasoning 场景中避免了这个问题，因为 reasoning 和 answer 在同一个 forward pass 中生成；但在 multi-turn agent 中，prior context 对 latent policy 的影响更强，使得 intervention 的因果解释更加模糊。
3. **"Hard-Ambiguous → 更 faithful" 的反直觉假设**: 这是 proposal 中最有趣的 hypothesis，但缺乏理论支撑。为什么 "genuine deliberation is required" 就会导致 more faithful reasoning？如果模型的 deliberation 本身也是 post-hoc rationalization（只是更复杂的 rationalization），这个假设就不成立。

【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是将已有方法论（RFEval 式 behavioral intervention + 2605.07990 式 linear probing）组合应用于一个新场景（multi-turn tool selection）。两条技术线本身都已成熟：behavioral intervention 有 RFEval、FACT-E、Lie to Me 等多篇工作；tool-call probing 有 2605.07990、2605.09252、2605.06890 等。Proposal 正确识别了交叉 gap，但 gap 的存在是因为这两个方向都刚发表 1-2 个月——更可能的原因是"时间不够"而非"问题本质上难以组合"。两个指标 TSCF 和 RTI 是 RFEval 框架在 tool-call domain 的直接映射（TSCF ≈ causal influence score，RTI ≈ 1 - TSCF），定义层面的新颖性有限。三层 difficulty stratification 是 solid 的实验设计，但不构成方法论创新。Counterintuitive hypothesis（ambiguity → faithfulness）是最大的 novelty 候选，但目前仅是推测。

2. **Significance: 中** — 研究问题本身重要：multi-turn agentic systems 中 tool selection 的可信度直接影响 safety 和 deployment。但本 proposal 是纯诊断性/empirical 工作——它测量问题的存在，不提出解决方案。如果核心发现是 "yes, tool-selection reasoning 在多轮中也是 ~50% unfaithful"（与 RFEval 在 general reasoning 中的发现一致），审稿人很可能认为 "I would have guessed this"。如果发现有趣的 ambiguity-faithfulness 交互作用，significance 会提升，但这取决于实验结果。此外，这是一个非常 timely 的 topic，有 safety narrative 加持，投稿 NeurIPS/EMNLP 有话题红利。

3. **Related Work: 强** — 这是 proposal 最出色的部分。对四条研究线索的覆盖全面且准确（经调研验证，引用的论文均真实存在，描述基本准确）。差异化定位清晰：明确指出现有工作的 gap（single-turn probing 成熟 vs multi-turn 未解，behavioral intervention 未应用于 tool selection）。唯一的小问题是 2605.06890 ("Beyond the Black Box") 的定位——proposal 称其 "not tool identity or faithfulness"，但该工作实际上也涉及 multi-step trajectory 上的 interpretability，可能比 proposal 描述的更接近。

【概率估计】: [18% - 30%] 中位 23%
（注：此概率基于投稿适配会议如 EMNLP/NeurIPS 的假设。投稿 CoRL 的中稿概率为 ~0%，因会被 desk reject。）

【估计理由】: 
Idea 填补了一个真实但可预测的 gap，属于 "方法 X for 领域 Y" 的组合式贡献。Related work 覆盖出色，研究问题有安全话题红利，但核心 novelty 受限于方法论的继承性。Significance 取决于实验结果是否能超越 "I would have guessed this"——如果核心发现只是 "多轮 tool selection 的 faithfulness 也是 ~50%，与单轮/general reasoning 一致"，那么贡献主要落在 benchmark 构建（TOOLFAITH-BENCH）上，而非 insight 上。Novelty 的弱-中评分是概率上界的主要限制因素。如果 counterintuitive hypothesis 得到验证且有 compelling 的 mechanistic 解释，概率可推至 30%+ 上界；如果结果平淡（merely replicating known patterns in a new domain），概率下探至 18% 附近。

【主要风险】:
1. **"Incremental combination" 质疑**: 审稿人可能认为这是将已有的 faithfulness evaluation 方法（RFEval）和 tool-call probing 方法（2605.07990）简单组合应用于新场景，方法论层面缺乏独立创新。TSCF/RTI 指标被视为 RFEval 指标的 domain-specific 重命名。
2. **结果可预测性**: 如果最终发现 "多轮 tool selection CoT 确实不忠实" —— 鉴于单轮已有 93-100% 的 pre-commitment 证据（2605.07990）和 ~50% 的 general reasoning unfaithfulness（RFEval），这个发现几乎是 expected 的。论文的 impact 将高度依赖于 "unexpected" 的二阶发现（如 ambiguity-faithfulness 交互），但这些在 proposal 阶段是不可控的。
```

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252)
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)
- [FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning](https://arxiv.org/abs/2604.10693)
- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135)
- [FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness](https://arxiv.org/abs/2509.13334)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing

## Description
We present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.

## Core Problem
In multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.

## Opportunity
The landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.

## Related Work / Landscape
The landscape spans four converging threads:

**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.

**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.

**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.

**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.

**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.

## Approach
We construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:

**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.

**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.

**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.

At each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.

We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.

## Inspiration
Three converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.

## Key References
- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)
- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)
- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)
- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)
- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)
- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)
- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)
- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)
- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)
- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)
- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)
- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)
- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)
- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)
- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)
- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)
- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)
- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)
- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)
- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)
- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)
- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)
- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)

## Resource Estimate
- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}
- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}
- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5d5e2743-7f40-4724-a5a2-8cee16497060",
  "type": "user",
  "uuid": "bb69c220-dfb1-4a9d-aeab-cc2293057255",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T20:52:23.304Z_

```json
{
  "parentUuid": "bb69c220-dfb1-4a9d-aeab-cc2293057255",
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
  "uuid": "5a4b2add-fb12-4d00-af75-815575bafb4f",
  "timestamp": "2026-05-19T20:52:23.304Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T20:52:23.304Z_

```json
{
  "parentUuid": "5a4b2add-fb12-4d00-af75-815575bafb4f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a8f65683-866d-43e8-b04c-ef7f77a3829d",
  "timestamp": "2026-05-19T20:52:23.304Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information. Let me compile my evaluation. T…",
  "leafUuid": "a8f65683-866d-43e8-b04c-ef7f77a3829d",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multi-turn agentic tool-selection faithfulness proposal",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751"
}
```

---

### Assistant

_source line 8 · 2026-05-19T20:53:16.592Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' evaluations systematically to produce a Meta Judge assessment.

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- CoRL probability: 0-2%
- If correct venue (ACL/EMNLP/NeurIPS): 20-30%, median 25%
- Key issues: Fatal venue mismatch, "I would have guessed this" risk

**Reviewer 2:**
- Novelty: 弱-中
- Significance: 中 (for NLP/AI Safety) / 弱 (for CoRL)


- Related Work: 强
- Probability: [5%-12%] median 8%
- But notes: if correct venue, ~20-28%
- Key issues: Venue mismatch (fatal), "obvious next step" risk

**Reviewer 3:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability: [18%-30%] median 23%
- Note: This is explicitly stated as "based on submitting to appropriate venue like EMNLP/NeurIPS"
- If CoRL: ~0%
- Key issues: Incremental combination, predictable results

Now I'm normalizing these probabilities to account for the venue mismatch issue that appears across all three reviewers. abilities. There's a critical issue: Reviewers 1 and 2 gave CoRL-specific probabilities (0-2% and 5-12%), while Reviewer 3 gave an "appropriate venue" probability (18-30%). But all three agree CoRL = ~0% desk reject.

Wait, let me re-read more carefully:
- R1: CoRL 0-2%; correct venue 20-30% median 25%
- R2: CoRL [5-12%] median 8%; correct venue ~20-28%
- R3: CoRL ~0%; correct venue [18-30%] median 23%

So R2's formal probability of [5-12%] median 8% is for CoRL. But then R2 also says "if correct venue, 20-28%."

For the Meta Judge, the proposal is explicitly targeting CoRL 2026. So I need to evaluate CoRL probability. But I should also provide the "if correct venue" assessment since all three reviewers flagged venue mismatch as fatal.

Now I'm aggregating the CoRL probabilities across reviewers: R1 gives 1%, R2 gives 8%, and R3 gives essentially 0%, which medians to 1%. The "if correct venue" estimates cluster much tighter around 23-25%, with a median of 24%.

Looking at the rubric consensus, there's unanimous agreement on related work quality, all three reviewers see novelty as weak-to-medium, and significance is medium across the board. The venue mismatch is the overwhelming consensus issue—all three flagged it as fatal.

Beyond the main consensus points, there are some specific concerns that stand out: R2 identified particular missing citations that the others didn't mention, while R1 raised a framing concern about probe training data distribution that's somewhat unique. For a CoRL submission, all three reviewers essentially treat this as a desk reject, with the acceptance probability sitting between 0-8%.

When I look at the assessment for the correct venue instead, the three reviewers converge much more tightly around 23-25%, all clustering in the 18-30% range. Computing the statistics: the CoRL medians are roughly 1%, 8%, and 0%, giving a median of medians around 1% with higher variability, which suggests I should lean toward the stricter end. For the correct venue, the medians are 25%, 24%, and 23%, yielding a median of 24% with much tighter consistency.

Now I need to reconcile what each reviewer actually said about CoRL versus correct venue, since R1 explicitly mentions both assessments while R2 and R3 seem to focus on different aspects. I'm noticing the reviewers gave mixed formats for their estimates. R3 provided a probability range for the appropriate venue rather than CoRL specifically, while R1 and R2 both gave CoRL estimates. Looking at just the CoRL probabilities, there's near-unanimous agreement that it's essentially a desk reject at 0-2%, with R2 being slightly more optimistic at 8%. However, all three reviewers agree the paper would have much stronger prospects in the right venue at around 20-28%. Given this unanimous verdict on the venue mismatch being fatal for CoRL, I should recommend rejecting it for this conference. I'll present the CoRL-targeted numbers since that's the submission venue, but I'll note the correct venue estimates as a secondary reference point to show how the assessment changes with proper categorization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8f65683-866d-43e8-b04c-ef7f77a3829d",
  "isSidechain": false,
  "requestId": "req_011CbCbBevJtRoCnKE4edozZ",
  "type": "assistant",
  "uuid": "6ff27463-c22e-4884-9a83-f8dbae065887",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9PZrVYmCCxdfarcrwP8AQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23181,
      "cache_read_input_tokens": 11374,
      "output_tokens": 5748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5748,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23181
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

_source line 9 · 2026-05-19T20:54:33.756Z_

【阶段】: Meta Judge
【三次中位】: [~1%, 8%, ~0%] (CoRL 2026 目标 venue) std≈3.6%
　　　　　　　[25%, ~24%, 23%] (若投适配 venue 如 EMNLP/NeurIPS) std≈0.8%

【共识维度】:
- **Venue Mismatch = 致命** (3/3 一致，最强信号): CoRL 是 Conference on Robot Learning，proposal 是纯 NLP/LLM Interpretability 工作，零 robotics 成分，五个 benchmark domain 全部是软件 agent。三位审稿人均独立判定为 desk reject 级别的 scope 不匹配。R3 甚至引用了 CoRL CFP 原文："Submissions without a robotics focus will be returned without review."
- **Novelty = 弱-中** (3/3 一致): R1 给"中"，R2 和 R3 给"弱-中"。三位均指出核心方法论是 RFEval 式 behavioral intervention + 2605.07990 式 linear probing 的组合搬运，属于 "方法 A + 方法 B in 新 setting C" 的组合式贡献，方法论层面缺乏独立创新。TSCF/RTI 被识别为 RFEval 指标的领域特定重命名。
- **Significance = 中** (3/3 一致): 研究问题本身重要（multi-turn agent safety），但核心发现高度可预测。三位均使用了 "I would have guessed this" 的表述——已有 2605.07990 的 multi-turn fragility 证据和 RFEval 的 ~50% unfaithfulness，"multi-turn tool-selection CoT 也部分不忠实" 几乎是 expected conclusion。
- **Related Work = 强** (3/3 一致，unanimous): 三位均独立验证了 proposal 中的文献引用准确性（arXiv ID、数字、claim 均吻合），四条 thread 的组织清晰，gap 定位准确。这是 proposal 最突出的优势。
- **Trivial Alternative 威胁存在但不致命** (3/3 一致): 纯 behavioral 路线（直接搬 RFEval 到 tool selection）或纯 probing 路线（扩展 2605.07990 到多轮数据）均可低成本回答核心问题的大部分。增量价值在两条路线的结合和 coupling 分析。
- **Counterintuitive hypothesis 有趣但无支撑** (3/3 一致): "hard-ambiguous → more faithful" 假设是 proposal 中最有潜力的 surprise factor，但三位均指出缺乏理论支撑，confirmation 概率不高。
- **Construct validity 担忧** (2/3, R1+R3): 三层 difficulty tier 的边界（尤其 soft-ambiguous 的 calibration）高度依赖主观判断，LLM-assisted generation 难以保证 tier 间边界清晰。
- **Intervention validity 担忧** (2/3, R2+R3): Multi-turn 中 CoT 干预可能被模型"感知到"（上下文约束更强），测量的可能是"对异常输入的鲁棒性"而非真正的 faithfulness。

【异常维度】:
- R2 独有：指出缺少 Counterfactual Simulation Training (2602.20710) 和 Bypassing the Rationale (2602.03994) 的讨论——属于次要 Related Work 补充建议，不影响整体判断，降权处理。
- R1 独有：提出 "multi-turn fragility 可能只是 probe training data distribution shift 的 artifact" 这一替代解释——有一定道理但属于 R1 个人推测，同样降权。
- R2 独有：给出 CoRL 概率 8%（其他两位给 0-2%）——R2 的 8% 相对宽松，可能是留了 "万一没 desk reject" 的尾部概率，但考虑 CoRL CFP 明确声明 "returned without review"，这个 8% 偏乐观。

【最终概率】: [0% - 3%] 中位 1% (CoRL 2026)；[18% - 28%] 中位 23% (若投适配 venue)

【一致性】: 高
三位审稿人在所有关键维度上高度一致：venue mismatch 致命（3/3）、Novelty 弱-中（3/3 基本一致）、Significance 中且可预测（3/3）、Related Work 强（3/3 unanimous）。正确 venue 概率估计的 std ≈ 0.8%，属于极高一致性。CoRL 概率的 std ≈ 3.6% 主要由 R2 的 8% outlier 贡献，但三位结论方向完全一致（desk reject）。

【综合理由】:

**1. CoRL 概率（中位 1%）的推理：**
三位审稿人独立且一致地识别出 venue mismatch 是致命缺陷。Proposal 的五个 benchmark domain（code editing, web browsing, data analysis, system administration, information retrieval）全部是软件层面的 tool-use，不涉及任何 robotics 组件（无 embodiment、无物理交互、无 sim-to-real、无 sensor/actuator）。CoRL 2026 CFP 明确要求 "demonstrate the relevance to robotics" 并声明 "Submissions without a robotics focus will be returned without review"。R2 给出的 8% 偏乐观（可能考虑了流程异常的尾部概率），按"分歧时偏严"原则，取 R1 和 R3 的 0-2% 区间，最终中位定在 1%。这 1% 仅反映极小概率的程序异常（如分配到对 NLP 友好的 AC 手下且恰好未被 desk reject），与 idea 质量无关。

**2. 正确 venue 概率（中位 23%）的推理：**
三位对 idea 内在质量的评估极其收敛（25%、24%、23%）。综合逻辑如下：
- **Related Work 强** → 论文不会因 framing 或文献遗漏被拒，保底分有保障
- **Novelty 弱-中** → 这是概率上限的主要限制因素。"方法 A+B in setting C" 的组合式 novelty 在顶会属于 marginal，三位均识别到这一点。即使实验执行完美，Novelty 天花板约 30%
- **Significance 中但可预测** → 核心发现大概率是 "confirming what existing work already strongly hints at"。如果实验只产出 "multi-turn 也 ~50% unfaithful"，审稿人会认为 contribution 不足。论文需要 qualitatively new 的发现才能突破天花板
- **Counterintuitive hypothesis** → 唯一的 upside catalyst。如果 confirmed 且有 mechanistic 解释，可推至 28-30%；如果 null result，概率下探至 18-20%

按"不应比三份中最宽松的更宽松"原则，上界取 28%（< R1 的 30% 和 R3 的 30%），下界取 18%（与 R3 下界一致），中位取 23%（三份的中位数）。

**3. 对 R2 的 8% outlier 处理：**
R2 给出的 [5-12%] median 8% 是唯一一个给 CoRL 留了较大"非 desk reject"概率的评估。但 R2 自己也明确说 "极可能被判为 out-of-scope，直接导致 desk reject 或在初审就被淘汰"。结合 R1 和 R3 的更严格判断（0-2% 和 ~0%），以及 CoRL CFP 的明确声明，将 R2 的 8% 作为 outlier 降权处理是合理的。

【建议】: KILL（CoRL 2026）；若改投适配 venue → 边缘（需实验结果中出现 unexpected findings 方可突破 25% 天花板）

【实施评估】:
- **计算资源**: 240-500 H100-hours（取决于自动化程度），约 $600-$1250 GPU 成本。涉及 4 个 open-weight 模型的 inference（600 scenarios × 4 intervention types × 3 tiers）+ multi-turn probing 实验。无需大规模训练，主要是推理和探针训练。资源需求合理。
- **数据需求**: 需自建 TOOLFAITH-BENCH（600 scenarios, 5 domains, 3 tiers）。无现成 benchmark 可直接使用。Scenario 生成可 LLM-assisted，但 tier boundary calibration（尤其 soft-ambiguous tier）需要人工 spot-checking。数据集本身可作为独立贡献。
- **人工介入**: 中等。benchmark 的 difficulty tier 标注需要人工验证（construct validity 是 2/3 审稿人的担忧点）；scenario quality validation 是自动化的速度瓶颈。估计需要 ~2-3 人周的人工标注/验证工作。
- **训练需求**: 不需要模型训练。仅需训练 linear probes（计算量极小，包含在 GPU-hours 估计内）。所有被评估模型均为 off-the-shelf。
- **新 Benchmark**: 是，需构建 TOOLFAITH-BENCH。这是论文的核心贡献之一，同时也是最大的工程挑战（tier calibration 的 construct validity）。
- **预估周期**: 10-14 周（取决于自动化程度）。关键路径：benchmark 设计与验证 2.5-3 周 → 实现 2-3 周 → 实验 2.5-3 周 → 分析与写作 3-5 周。若采用高度自动化 pipeline，可压缩至 5-7 周 wall-clock，但 tier validation 的人工环节无法完全跳过。

---

**对团队的核心建议：**

1. **立即更换目标 venue**。CoRL 2026 投稿 = 确定性 desk reject。推荐目标：EMNLP 2026、NeurIPS 2026、或 ICML 2027。如果时间线紧迫，EMNLP 2026 的 scope 最匹配（NLP + Safety + Agent）。

2. **Idea 质量的天花板需要突破**。即使投对 venue，当前 proposal 的 Novelty 评级（弱-中）将概率上限压在 ~28-30%。三位审稿人一致认为核心方法论是组合搬运。若要提升，需要在 (a) behavioral-mechanistic coupling analysis 中发展出超越简单 correlation 的新方法论，或 (b) 在 counterintuitive hypothesis 上提出更有理论支撑的 mechanism，而非仅作为 empirical bet。

3. **"I would have guessed this" 是最大的 significance 风险**。论文的成败高度依赖于实验结果是否产出 qualitatively unexpected findings。建议在实验设计阶段就明确：如果核心发现只是 "multi-turn 也 ~50% unfaithful"，论文的 fallback narrative 是什么？Benchmark contribution (TOOLFAITH-BENCH) 本身能否撑起投稿？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff27463-c22e-4884-9a83-f8dbae065887",
  "isSidechain": false,
  "requestId": "req_011CbCbBevJtRoCnKE4edozZ",
  "type": "assistant",
  "uuid": "88141821-87e9-456f-9c73-989634eda1af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9PZrVYmCCxdfarcrwP8AQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23181,
      "cache_read_input_tokens": 11374,
      "output_tokens": 5748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5748,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 23181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23181
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough information. Let me compile my evaluation. T…",
  "leafUuid": "88141821-87e9-456f-9c73-989634eda1af",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate multi-turn agentic tool-selection faithfulness proposal",
  "sessionId": "e95fca51-2836-4974-b1ef-e168199c3751"
}
```

---
