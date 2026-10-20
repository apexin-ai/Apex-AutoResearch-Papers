# Research conversation: 【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。 【发掘 agent 本轮输出】: I now have sufficient inform

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 2
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/3f1bd7df-6f1a-4c86-930b-b729b792593a.jsonl`
- **Structured JSON:** [`ba36dfca17cb3d4f5af2.json`](../../sessions/ba/ba36dfca17cb3d4f5af2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:45:45.814Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:45:45.814Z",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nI now have sufficient information to provide my assessment. Let me compile my findings.\n\n---\n\n【状态】: 有发掘空间\n\n**⚠️ 但首先必须标注一个致命问题：投稿目标会议与论文内容完全不匹配。**\n\n---\n\n【前置调研发现】\n\n- **[Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026):** 本 proposal 最核心的前置工作。对 12 个模型做 single-turn tool probing，4B+ 模型 steering accuracy 达 93-100%，但明确指出 multi-turn 迁移\"fragile\"（-30 to +10pp）。本 proposal 正确定位在这个 gap 上。\n- **[RFEval](https://arxiv.org/abs/2602.17053) (ICLR 2026):** 7,186 instance 的 counterfactual intervention benchmark，发现 ~50% unfaithfulness。提供了 stance consistency + causal influence 的形式化框架。本 proposal 的 intervention protocol 借鉴了此方法论，但迁移到 tool selection 领域。\n- **[Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv 2026):** SAE + linear probe 用于 multi-step trajectory 中的 tool-need/tool-risk classification。**高度相关但被 proposal 低估**——该工作已经在多步 trajectory 上做了 probe，虽然不是 tool identity 或 faithfulness，但覆盖面比 proposal 描述的更广。\n- **[Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv 2026):** 12 模型评测发现 thinking token 与 output 之间存在 59pp faithfulness gap。核心 insight 是\"internal recognition ≠ output acknowledgment\"。\n- **[CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers):** 明确要求\"submissions should focus on a core robotics problem\"，\"submissions without a robotics focus will be returned without review\"。鼓励 real-robot experiments 或 sim-to-real evidence。\n- **调研总结:** CoT faithfulness 研究在 2026 年进入了快速成熟期，单轮已有成熟框架（RFEval 的 counterfactual intervention, 2605.07990 的 linear probing），多轮 tool selection 确实是一个被明确标识但尚未系统研究的 gap。但 CoRL 的 scope 严格限定于机器人学习，与本 proposal 的内容领域完全不重叠。\n\n---\n\n【致命问题：投稿目标会议错误——必须在一切发掘之前解决】\n\n- **维度:** 前提假设质疑（研究方向与投稿目标的匹配性）\n- **内容:** CoRL 2026 明确声明 **\"Submissions without a robotics focus will be returned without review\"**。本 proposal 研究的是 LLM agent 在代码编辑、网页浏览、数据分析、系统管理、信息检索五个领域中的 tool-selection faithfulness——没有任何一个领域涉及机器人学习。Benchmark 设计中无 robot manipulation、locomotion、perception、planning、sim-to-real 任何元素。**这不是 borderline case，而是会被直接 desk reject 的完全不匹配。**\n- **价值:** 这是一切其他优化建议的前提。如果目标会议选错，idea 本身质量再高也无法中稿。\n- **补救方向:**\n  - **方案 A（推荐）：** 转投匹配的会议——NeurIPS 2026（有 Safety/Interpretability track，deadline 通常 5-6 月）、EMNLP 2026、AAAI 2027。本 proposal 的内容与这些会议高度匹配。\n  - **方案 B（不推荐，成本极高）：** 将整个 proposal 重新定位为 robot learning 问题——例如研究 embodied agent 在 manipulation task 中的 tool-selection faithfulness（机械臂选择 grasp vs. push vs. reposition 的推理忠实性），需要重建 benchmark、重新设计 domain、引入 real-robot 或 sim 实验，基本等于重写一篇新论文。\n- **调研依据:** CoRL 2026 官方 Call for Papers（https://www.corl.org/contributions/call-for-papers）。\n\n---\n\n**以下发掘建议基于\"已转投至匹配会议（如 NeurIPS 2026）\"的前提：**\n\n---\n\n【发掘点 1】\n- **维度:** trivial alternative 威胁\n- **内容:** 本 proposal 的核心 behavioral intervention protocol（reason-flip, reason-ablate, counterfactual-inject, reason-scramble）本质上是将 RFEval 的 counterfactual intervention 框架从 QA/math reasoning 迁移到 tool selection。审稿人会问：**这个迁移本身有多 non-trivial？** RFEval 已经提供了成熟的 stance consistency + causal influence 框架，将干预对象从\"reasoning about an answer\"换成\"reasoning about a tool call\"是否属于 straightforward domain transfer？如果是，那核心贡献就缩窄为\"在新 domain 上复现了 RFEval 的发现\"。**Proposal 需要清晰 argue 为什么 tool selection 的 faithfulness 问题在结构上不同于 QA faithfulness**——例如：tool call 有 structured output（JSON schema），而非 free-form answer；tool call 有 downstream effect（执行结果反馈到下一轮），创造了 QA 不存在的 temporal dependency；multi-turn 的 context accumulation 改变了 intervention 的 semantics（你 flip 的 reasoning 可能与先前 turn 的 tool result 矛盾，创造 incoherence）。这些结构性差异应该被提升为核心 novelty claim 的一部分，而不仅仅是\"我们把 X 用在了新领域 Y\"。\n- **价值:** 直接提升 Novelty 维度——从\"domain transfer\"升级为\"结构性新问题需要新方法论适配\"。\n- **调研依据:** RFEval (2602.17053) 的框架已非常成熟且被 ICLR 2026 接收，审稿人必然会追问差异化。\n\n【发掘点 2】\n- **维度:** 核心 claim 强化\n- **内容:** Proposal 提出的最有趣的假设是 **\"harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones\"**——这是一个 counterintuitive prediction，如果被验证，是非常强的 contribution。但当前 proposal 对这个假设的理论动机阐述不足（仅一句\"because genuine deliberation is required\"）。建议将这个假设提升为论文的 **central narrative**：构建一个\"deliberation threshold\"的理论模型——当 tool choice 是 trivial 时，模型走 System 1 fast path（直接从 latent policy 选择），CoT 变成 post-hoc rationalization；当 tool choice genuinely ambiguous 时，模型被迫走 System 2 deliberation path，CoT 成为真正的计算介质。这个 framing 将 tool-selection faithfulness 从一个 benchmark paper 提升为一个有 explanatory power 的 framework paper。具体地，三个 tier（Unambiguous/Soft/Hard）不再只是 benchmark stratification，而是对应理论预测的三个 regime。\n- **价值:** 提升 Significance 维度——从\"我们测量了 faithfulness\"升级为\"我们发现并解释了 faithfulness 随 task difficulty 的非单调变化规律\"。\n- **调研依据:** \"Brief Is Better\" (2604.02155) 已经发现 CoT budget 对 function-calling 有 non-monotonic 效果，暗示了 deliberation dynamics 的复杂性。\"Decoding Answers Before CoT\" (2603.01437) 的 0.9 AUC pre-CoT probing 支持\"System 1 fast path\"假说（答案在 CoT 之前已编码）。\n\n【发掘点 3】\n- **维度:** related work 差异化\n- **内容:** Proposal 对 **\"Beyond the Black Box\" (2605.06890)** 的定位可能低估了其威胁性。当前 proposal 将其描述为\"applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness\"。但该工作已经在 multi-step agentic trajectory 上建立了 probing 基础设施——如果他们的后续工作简单扩展到 tool identity probing（技术上直接可行），本 proposal 的 mechanistic probing 部分的 novelty 就会大幅缩水。**建议：(1)** 明确 acknowledge 2605.06890 的 coverage 而非 downplay 它；**(2)** 将 proposal 的 mechanistic 贡献聚焦在 behavioral-mechanistic coupling 上（即发掘点 2 中\"behavioral intervention 结果与 probe 结果的相关性分析\"），这是 2605.06890 完全没有触及的维度——它只做了 probing，没有做 behavioral intervention，更没有做两者的 coupling analysis。\n- **价值:** 提升 Related Work 差异化——预防审稿人认为 mechanistic probing 部分是 incremental extension of 2605.06890。\n- **调研依据:** 2605.06890 已在 multi-step trajectory 上部署了 SAE + linear probe，与本 proposal 的 probing component 有直接技术重叠。\n\n【发掘点 4】\n- **维度:** significance 提升\n- **内容:** 当前 proposal 的 significance 叙事主要停留在\"unfaithful tool selection can cascade into harmful actions\"这一 safety motivation。但这个 motivation 偏 abstract——审稿人会问\"so what, this is true for any unfaithful reasoning\"。建议引入一个更锐利的 significance angle：**multi-turn tool selection 是目前 AI agent 可观测推理与不可观测行为之间 alignment gap 最大的场景**。具体论证：(1) 与 QA 不同，tool call 是 action（有不可逆的 real-world effect）；(2) 与 single-turn 不同，multi-turn 中 early unfaithfulness 通过 tool result 反馈 compound（一个基于错误理由选择的 API call 的结果会 condition 所有后续推理）；(3) 当前的 agent monitoring 方案（如 SAVeR）假设 CoT 是 faithful 的，如果这个假设不成立，整个 monitoring paradigm 需要重新审视。第 (3) 点特别有力，因为它将本工作定位为对一个正在被广泛部署的 safety mechanism 的 validity check。\n- **价值:** 提升 Significance 维度——从 general safety motivation 升级为对当前 agent monitoring paradigm 的 foundational challenge。\n- **调研依据:** SAVeR (2604.08401) 和 \"Noticing the Watcher\" (2603.16928) 都在构建基于 CoT 的 agent monitoring，隐含假设了 CoT 的 faithfulness。\n\n【发掘点 5】\n- **维度:** novelty 锐化\n- **内容:** Proposal 目前试图同时做两件大事：(1) behavioral causal intervention benchmark (TOOLFAITH-BENCH + TSCF/RTI metrics)，(2) multi-turn mechanistic probing (cross-turn probe transfer, encoding drift, replanning signals, behavioral-mechanistic coupling)。对于一篇会议论文来说，这两件事的结合既是优势也是风险。优势是 uniqueness（无人做过两者的 coupling）；**风险是审稿人认为每一半都不够深**——behavioral 部分看起来像 RFEval 的 domain transfer，mechanistic 部分看起来像 2605.07990 的 multi-turn extension。建议做出取舍：**将 behavioral-mechanistic coupling analysis 提升为论文的核心独特贡献**，而将 pure behavioral benchmark 和 pure probing 各自 condense 为 supporting components。核心 research question 应该是：\"当 probe 在 CoT 生成之前就检测到了 tool identity 的 pre-commitment（mechanistic unfaithfulness），behavioral intervention 是否也会显示 low TSCF（behavioral unfaithfulness）？\" 如果两种独立的 unfaithfulness measure 高度相关，这是一个非常强的发现（convergent validity）；如果不相关，这同样是一个重要发现（暗示存在多种不同的 unfaithfulness mechanism）。\n- **价值:** 同时提升 Novelty 和 Significance——将论文从\"两个方向的分别推进\"重新定位为\"两个方向的 convergence/divergence 分析\"，这是任何单独做 behavioral 或 mechanistic 的工作都无法提供的。\n- **调研依据:** 基于领域整体趋势判断——behavioral intervention (RFEval 路线) 和 mechanistic probing (2605.07990 路线) 目前是两个平行发展的 community，无人做过两者的 systematic coupling analysis。\n\n---\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)\n- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)\n- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?](https://arxiv.org/abs/2603.22582)\n- [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing (SAVeR)](https://arxiv.org/abs/2604.08401)\n- [CoRL 2026 About Page](https://www.corl.org/about-corl)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research to provide a thorough analysis. Let me compile my findings.\n\n---\n\n【状态】: 发现致命缺陷\n\n【前置调研发现】\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026): 12 models probed for single-turn tool-call readability; 93-100% steering accuracy at 4B+; multi-turn explicitly marked \"fragile\" (-30 to +10pp). Experimental design: linear probes on residual stream, mean-difference steering vectors, single-turn fixed-menu setup. No behavioral interventions on CoT.\n- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv 2026): 7,186 instances, 12 open-source LRMs, counterfactual output-level interventions measuring stance consistency + causal influence. Metrics: per-instance faithfulness rate, domain-stratified analysis, correlation with post-training regime. Evaluated ~50% unfaithfulness. Key design choice: faithfulness decoupled from correctness.\n- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv 2026): 12 models, 498 MCQs, 6 hint categories, 41,832 inference runs. Metrics: per-model faithfulness rate, thinking-vs-output acknowledgment gap (87.5% vs 28.6%). Key design: fine-grained analysis by hint type, model family, and parameter count; regression analysis showing training method > scale.\n- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252) (arXiv 2026): Binary tool-necessity probing at 0.89-0.96 AUROC. Ablation: soft vs. hard prefill, temperature scaling, layer selection, data efficiency, regularization strength, OOD transfer, multi-hop transfer.\n- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): Causality-inspired perturbation framework for CoT evaluation; uses controlled perturbations as instrumental signal to separate genuine step-to-step dependence from bias artifacts.\n- [BFCL v3 / ToolBench / MAVEN](https://benchlm.ai/llm-agent-benchmarks) (2025-2026): Current tool-calling benchmarks use AST evaluation, multi-step reasoning, adversarial composition, OOD transfer. Standard practice includes serial/parallel function calls, multi-language evaluation, and explicit distractor tools.\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. **Submissions without a robotics focus will be returned without review.**\"\n- 调研总结: 该领域（CoT faithfulness + tool-call probing）的实验设计标准包括：大规模多模型评估（10+模型）、多种intervention类型的对照、faithfulness与correctness的解耦、per-domain/per-difficulty分层分析、详细ablation（层选择、probe架构、OOD迁移等）、以及统计显著性分析。审稿人普遍期望看到intervention protocol的construct validity论证、benchmark质量的human validation、以及指标间的非冗余性证明。**然而，该proposal的目标会议CoRL是机器人学习会议，与本proposal的研究内容（LLM推理忠实性）完全不匹配。**\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题\n- 问题: **Proposal 目标投稿 CoRL 2026，但 CoRL 是机器人学习专业会议，明确要求 \"Submissions should focus on a core robotics problem... Submissions without a robotics focus will be returned without review.\"** 本 proposal 的五个领域（code editing, web browsing, data analysis, system administration, information retrieval）无一涉及机器人学，全文没有任何 robotics 相关内容。论文几乎必然在 desk review 阶段被退回。\n- 严重度: 不可补救（方向性致命）\n- 补救方案: 此缺陷**在不改变 idea 核心的前提下无法补救**。即使实验设计再完美，CoRL 的 scope 明确排斥非机器人主题。需要更换投稿目标至匹配的会议，如 NeurIPS 2026、ICML 2026、ICLR 2027、ACL/EMNLP 2026（如果偏 NLP agent），或 AAAI 2027 等接受 LLM interpretability/faithfulness 研究的综合性 AI 会议。如果坚持 CoRL，则需要将整个 benchmark 和实验重新设计为机器人操控场景中的 tool-selection faithfulness（如机械臂工具选择、导航动作选择等），这本质上是一个全新的项目。\n- 调研依据: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确声明 robotics focus 要求\n\n---\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Proposal 的 multi-turn intervention protocol 在关键操作层面缺乏规范。具体地：(a) 在多轮对话中，perturbation 作用于哪一个 turn 的 CoT？如果对 turn 3 的 reasoning 做 reason-flip，turn 5 的模型是否能看到 turn 3 的原始或修改后的推理？(b) 四种 intervention（reason-flip, reason-ablate, counterfactual-inject, reason-scramble）在 multi-turn 中如何处理跨 turn 的推理依赖——例如 turn 5 的推理引用了 turn 3 的工具调用结果，而 turn 3 的工具调用是被 intervention 改变的？(c) 不清楚每个 decision point 是独立做 intervention 还是级联做 intervention（all points simultaneously）。RFEval 和 \"Lie to Me\" 的 intervention 设计之所以有效，是因为单轮设置避免了这些级联问题。\n- 严重度: 可补救\n- 补救方案: 明确定义两种 intervention regime 并分别报告结果：(1) **Point-wise intervention**——仅对单个 decision point 做 perturbation，保持其他 turn 不变，观察该 decision point 的工具选择变化；(2) **Cascading intervention**——从某个 turn 开始 intervene，让后续 turn 自然生成（包括受干扰的 tool results），观察下游 decision points 的工具选择变化。两种 regime 测量不同维度：前者测局部 faithfulness，后者测 cascading unfaithfulness。此外需明确：在 point-wise intervention 中，对 turn k 做 reason-flip 后，turn k+1 看到的是模型基于 flipped reasoning 实际执行的 tool 结果，还是原始 tool 结果？这会显著影响实验结论。\n- 调研依据: RFEval (2602.17053) 的 intervention 设计仅覆盖单轮，未处理级联问题；Breaking the Chain (2603.16475) 对中间结构做 intervention 但也限于单轮推理链，未扩展到 multi-turn 对话场景\n\n【缺陷 3】\n- 类别: 评估方案缺陷\n- 问题: TSCF（Tool Selection Causal Fidelity）和 RTI（Reasoning Theater Index）两个指标之间的关系不清晰，存在近冗余风险。Proposal 定义 TSCF 为 \"tool calls correctly follow intervened reasoning\" 的比率，RTI 为 \"tool calls remain unchanged despite contradictory reasoning\" 的比率。对于 reason-flip intervention，如果模型要么跟随新 reasoning 选择新 tool（high TSCF），要么无视新 reasoning 保持原 tool（high RTI），则 TSCF + RTI ≈ 1（第三种情况——既不跟随也不保持原选择——的概率需要讨论）。审稿人很可能质疑两个指标是否提供独立信息。此外，对 Tier 3 (Hard-Ambiguous) 场景中多个 valid tool 的情况，\"correctly follow\" 如何形式化定义未说明。\n- 严重度: 可补救\n- 补救方案: (1) 形式化定义三种 outcome：**Follow**（选择 intervened reasoning 指向的工具）、**Ignore**（保持原工具不变）、**Diverge**（选择第三个工具，既非原工具也非 intervention 指向的工具）。报告三者的分布比例，其中 Diverge rate 本身就是一个有趣的信号（模型可能有自己的 latent policy 独立于任何 reasoning）。(2) 对 Tier 3 场景，定义 faithfulness 为 \"reasoning-tool logical consistency\"：如果 CoT 中列出了选择 tool A 的理由，但实际调用了 tool B（即使 B 也是 valid 的），则标记为 unfaithful。使用 LLM judge 评估 reasoning-tool consistency（参考 C2-Faith 的 LLM-as-judge 方法但需报告 inter-rater agreement）。(3) 明确 TSCF 和 RTI 在不同 intervention 类型下的解释差异——reason-ablate 下没有 \"target tool\" 可以 follow，所以 TSCF 在该条件下应有不同定义。\n- 调研依据: RFEval (2602.17053) 将 faithfulness 分解为 stance consistency 和 causal influence 两个独立维度来避免指标冗余；C2-Faith (2603.05167) 指出 LLM-as-judge 评估 faithfulness 存在 systematic blind spots，建议报告 localization-level agreement\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: Proposal 未提出任何显式的 ablation study 设计。对于一个引入新 benchmark（TOOLFAITH-BENCH）、新 intervention protocol、新指标（TSCF/RTI）、以及新 probing 分析的论文，缺少 ablation 会让审稿人无法判断各设计决策的贡献和必要性。同领域论文（2605.07990, 2605.09252）均包含详细 ablation（层选择、probe 架构、数据效率、OOD 迁移等）。\n- 严重度: 可补救\n- 补救方案: 需要设计以下 ablation studies：\n  - **(A) Conversation depth ablation**: 将 faithfulness 指标按 decision point 位置分析（turn 2 vs turn 4 vs turn 8），验证 Hypothesis \"probe accuracy degrades with conversation depth\"\n  - **(B) Intervention position ablation**: 在对话的早期 vs 中期 vs 晚期 decision point 做 intervention，分析位置效应\n  - **(C) Tool menu size ablation**: 固定场景但变化可用工具数量（5, 10, 20 tools），分析工具菜单规模对 faithfulness 的影响\n  - **(D) Perturbation strength ablation**: 对 reason-flip，测试从 \"微调一个关键句\" 到 \"完全重写\" 的不同强度，绘制 faithfulness 随 perturbation 强度的曲线\n  - **(E) Probing layer selection**: 报告不同层的 probe accuracy（参考 2605.07990 的 per-layer 分析），明确 multi-turn probing 的最优层是否与 single-turn 一致\n  - **(F) Tier boundary sensitivity**: 对 Tier 2 的 \"soft-ambiguous\" 场景，通过调整 tool 描述使其更接近 Tier 1 或 Tier 3，分析 faithfulness 在 ambiguity 连续谱上的变化\n- 调研依据: 2605.07990 包含 per-layer probe accuracy, model-size scaling, domain transfer ablation; 2605.09252 包含 soft vs hard prefill, temperature scaling, layer selection, data efficiency, regularization strength ablation\n\n【缺陷 5】\n- 类别: 实验设计不足\n- 问题: Benchmark 的 ground truth 建立和质量控制方案不足。Proposal 提到使用 Claude 辅助生成场景并进行 \"tiered difficulty validation\"，但未说明：(a) 每个 tier 的分类标准如何操作化——谁判断一个场景是 Unambiguous vs Soft-Ambiguous？用什么标准？(b) 人工验证的规模（多少 annotator、inter-annotator agreement 目标是多少）？(c) 对于 Tier 2 \"one clearly optimal tool among plausible candidates\" 的判断标准——\"clearly optimal\" 是通过人工共识还是性能指标定义的？(d) Tier 3 场景中 \"genuinely valid\" 工具的验证方式。Benchmark 的 construct validity 是全文实验结论的基础，如果 tier 分类不可靠，所有按 tier 分析的结论都会受质疑。\n- 严重度: 可补救\n- 补救方案: (1) 设计 pilot study：先生成 100 个候选场景，请 3+ 名 annotator 独立标注 tier，计算 Fleiss' κ 或 Krippendorff's α，目标 > 0.7。(2) 对 Tier 2 场景，定义 \"optimality gap\"：让 annotator 对每个候选工具打 1-5 分适用度评分，要求最优工具得分与次优工具得分差值在 [1.0, 2.5] 区间（太小变成 Tier 3，太大变成 Tier 1）。(3) 对 Tier 3 场景，要求至少 2 名 annotator 独立确认存在 ≥2 个得分差 < 0.5 的工具。(4) 在论文中报告 benchmark statistics：per-tier 的 annotator agreement、场景长度分布、工具数量分布、domain 分布等。(5) 预留 10% 场景做 held-out validation——在实验结束后检查这些场景上的结果是否与主集一致。\n- 调研依据: RFEval (2602.17053) 使用了明确的 counterfactual generation pipeline 并报告了 construct validity；FaithCoT-Bench (ICLR 2026, 2510.04040) 对每个 instance 的 ground truth 均有 human validation protocol\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: Multi-turn probing 的四个 novel analyses 方法论细节不足，尤其是：(a) **Cross-turn probe transfer** ——仅说 \"probe trained at decision point 1 generalizes to decision point 3\"，未指定 probe 架构（线性？MLP？）、训练数据规模、训练/测试分割策略、以及 \"generalization\" 的量化标准。(b) **Context-dependent encoding drift** ——如何度量 \"the linear direction encoding a given tool shifts across turns\"？cosine similarity between direction vectors? explained variance ratio? 没有明确。(c) **Error-induced replanning signals** ——如何系统性引入工具执行错误？自然错误的发生率可能太低导致样本量不足。(d) **Faithfulness coupling** ——\"correlating probe-detected pre-commitment with behavioral unfaithfulness\" 的相关性分析方法（Pearson? Spearman? point-biserial?）和统计检验未提及。\n- 严重度: 可补救\n- 补救方案: \n  - **(a)** 明确使用 logistic regression probe（与 2605.07990 保持一致以便直接比较），训练数据来自每个 decision point 对应 layer 的 residual stream activations，报告 5-fold cross-validation accuracy 和 bootstrap CI\n  - **(b)** 定义 encoding drift = 1 - cos(v_tool^{turn_i}, v_tool^{turn_j})，其中 v_tool 是对特定 tool 的 probe weight vector。对每对 turn 计算 drift 矩阵，可视化为 heatmap\n  - **(c)** 设计 synthetic error injection：在正常 tool 返回的结果中注入 3 类错误（API error / wrong format / logically incorrect result），每类 50+ instances，确保样本量足够。对比 error 前后同一层的 activation shift（L2 distance 或 cosine shift）\n  - **(d)** 使用 point-biserial correlation（probe pre-commitment 是连续变量，behavioral faithfulness 是二元变量），报告 r_pb 和 p-value，并用 permutation test 做 robustness check\n- 调研依据: 2605.07990 使用 logistic regression probe + mean-difference steering，per-layer 分析，5-fold cross-validation；2605.09252 报告 AUROC + bootstrap confidence intervals\n\n【缺陷 7】\n- 类别: 实验设计不足\n- 问题: Proposal 未提及任何统计分析方法。对 7 个模型 × 3 个 tier × 4 种 intervention × 5 个 domain 的大规模比较实验，缺少统计检验会导致审稿人无法判断观察到的差异是否显著。特别是 Hypothesis 3（\"harder ambiguous scenarios may elicit more faithful reasoning\"）和 Hypothesis 2（\"probe accuracy degrades with conversation depth\"）需要严格的统计支撑。\n- 严重度: 可补救\n- 补救方案: (1) 对主要 claim 使用 bootstrap CI（10,000 resamples）报告 95% 置信区间。(2) 对 tier 间的 TSCF/RTI 差异使用 paired permutation test 或 Wilcoxon signed-rank test。(3) 对模型间比较使用 Friedman test + Nemenyi post-hoc 检验（参考 ML 领域多分类器比较的标准做法）。(4) 对多重比较问题，使用 Bonferroni 或 Holm 校正。(5) 在 \"counterintuitive\" Hypothesis 3 上，需要进行 power analysis 确保 600 场景（200 per tier）的样本量足以检测到预期的 effect size。\n- 调研依据: 基于领域实验规范判断；RFEval 进行了 per-domain 和 per-model 的统计分析；\"Lie to Me\" 使用了 regression analysis 分析变量间关系\n\n【缺陷 8】\n- 类别: baseline 不足或过时\n- 问题: Proposal 的 behavioral experiment 缺乏与现有 faithfulness 测量方法的对比 baseline。目前测量 CoT faithfulness 的方法至少包括：(a) 早期答案 probing (Decoding Answers Before CoT, 2603.01437)，(b) activation-based rationalization detection (Catching Rationalization in the Act, 2603.17199)，(c) LLM-as-judge (C2-Faith, 2603.05167)，(d) self-evaluation (FACT-E, 2604.10693)。Proposal 应展示其 behavioral intervention 方法相对于这些替代方法在 tool-selection faithfulness 测量上的优势或互补性。\n- 严重度: 可补救\n- 补救方案: 增加一组 **method comparison experiment**：在同一场景子集上（如 100 个场景），同时使用以下方法测量 faithfulness：(1) 本文的 behavioral intervention (TSCF/RTI)；(2) pre-tool-call probing（扩展 2605.07990 到 multi-turn）；(3) LLM-as-judge for reasoning-action consistency（扩展 C2-Faith 到 tool selection）。比较三种方法的一致性（Cohen's κ）和各自独特发现。这不仅加强了实验的 soundness，还能直接支撑 \"behavioral-mechanistic faithfulness coupling\" 分析。\n- 调研依据: 2603.17199 (Catching Rationalization in the Act) 使用 activation probing 检测 motivated reasoning，证明 internal representations 优于 CoT monitors；C2-Faith (2603.05167) benchmark LLM-as-judge 方法\n\n【缺陷 9】\n- 类别: 可行性问题\n- 问题: Compute 资源估算可能偏乐观。4 个 open-weight 模型中 DeepSeek-V4-Pro 的参数规模可能很大（V3 已经是 671B MoE），在 multi-turn 场景下推理成本较高。600 scenarios × 4 interventions × 3 tiers 的每个 decision point 需要完整 multi-turn 推理（2-4 decision points → 4-12 turns per scenario）。加上 probing 需要存储所有 intermediate activations（对大模型可能需要大量 CPU/GPU 内存），300 H100-hours 可能不够。此外，API 成本估算 ($350-450) 在当前 frontier model pricing 下可能偏低：600 × 4 × 3 个 frontier model calls，每个 multi-turn 平均 ~20K tokens，总计约 14.4M tokens per model × 3 models ≈ 43M tokens，仅 input 成本在 $3-15/M tokens 级别就可能达到 $130-650，加上 output tokens 可能超过预算。\n- 严重度: 可补救\n- 补救方案: (1) 重新估算：明确列出每个模型的推理吞吐量和每个实验条件的预期 token 数，自底向上计算总 compute。(2) 对最大的 open-weight 模型（DeepSeek-V4-Pro），考虑使用量化版本（如 INT4/FP8）以降低 GPU 内存和推理时间。(3) 为 probing 实验单独预算存储 activations 的成本。(4) 预留 20-30% buffer 应对意外（如某些模型推理速度比预期慢、需要 re-run 等）。(5) 如果资源紧张，可以先对 200 scenarios 的子集做完整实验，验证方法论后再扩展到 600。\n- 调研依据: 基于领域实验规范判断；2605.07990 仅评估到 27B 模型即已需要大量 compute，multi-turn 场景下成本倍增\n\n---\n\n**总结**: 最关键的问题是**缺陷 1（CoRL venue mismatch）**——这是一个方向性致命缺陷，无论实验设计如何完善，该论文都不在 CoRL 的 scope 内，几乎必然被 desk reject。建议立即更换目标会议（NeurIPS / ICML / ICLR / AAAI 等综合性 AI 会议，或 ACL / EMNLP 如果强调 NLP agent 角度）。其余 8 个缺陷均可补救，且补救方案具体可行——如果解决了 venue 问题，这些改进可以显著提升论文的实验 soundness。\n\nSources:\n- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)\n- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning](https://arxiv.org/abs/2603.22582)\n- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252)\n- [FACT-E: Causality-Inspired Evaluation for Trustworthy CoT Reasoning](https://arxiv.org/abs/2604.10693)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [LLM Agent & Tool-Use Benchmarks 2026](https://benchlm.ai/llm-agent-benchmarks)\n- [C2-Faith: Benchmarking LLM Judges](https://arxiv.org/abs/2603.05167)"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:45:45.817Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:45:45.817Z",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-19T18:45:45.828Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
I now have sufficient information to provide my assessment. Let me compile my findings.

---

【状态】: 有发掘空间

**⚠️ 但首先必须标注一个致命问题：投稿目标会议与论文内容完全不匹配。**

---

【前置调研发现】

- **[Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026):** 本 proposal 最核心的前置工作。对 12 个模型做 single-turn tool probing，4B+ 模型 steering accuracy 达 93-100%，但明确指出 multi-turn 迁移"fragile"（-30 to +10pp）。本 proposal 正确定位在这个 gap 上。
- **[RFEval](https://arxiv.org/abs/2602.17053) (ICLR 2026):** 7,186 instance 的 counterfactual intervention benchmark，发现 ~50% unfaithfulness。提供了 stance consistency + causal influence 的形式化框架。本 proposal 的 intervention protocol 借鉴了此方法论，但迁移到 tool selection 领域。
- **[Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv 2026):** SAE + linear probe 用于 multi-step trajectory 中的 tool-need/tool-risk classification。**高度相关但被 proposal 低估**——该工作已经在多步 trajectory 上做了 probe，虽然不是 tool identity 或 faithfulness，但覆盖面比 proposal 描述的更广。
- **[Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv 2026):** 12 模型评测发现 thinking token 与 output 之间存在 59pp faithfulness gap。核心 insight 是"internal recognition ≠ output acknowledgment"。
- **[CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers):** 明确要求"submissions should focus on a core robotics problem"，"submissions without a robotics focus will be returned without review"。鼓励 real-robot experiments 或 sim-to-real evidence。
- **调研总结:** CoT faithfulness 研究在 2026 年进入了快速成熟期，单轮已有成熟框架（RFEval 的 counterfactual intervention, 2605.07990 的 linear probing），多轮 tool selection 确实是一个被明确标识但尚未系统研究的 gap。但 CoRL 的 scope 严格限定于机器人学习，与本 proposal 的内容领域完全不重叠。

---

【致命问题：投稿目标会议错误——必须在一切发掘之前解决】

- **维度:** 前提假设质疑（研究方向与投稿目标的匹配性）
- **内容:** CoRL 2026 明确声明 **"Submissions without a robotics focus will be returned without review"**。本 proposal 研究的是 LLM agent 在代码编辑、网页浏览、数据分析、系统管理、信息检索五个领域中的 tool-selection faithfulness——没有任何一个领域涉及机器人学习。Benchmark 设计中无 robot manipulation、locomotion、perception、planning、sim-to-real 任何元素。**这不是 borderline case，而是会被直接 desk reject 的完全不匹配。**
- **价值:** 这是一切其他优化建议的前提。如果目标会议选错，idea 本身质量再高也无法中稿。
- **补救方向:**
  - **方案 A（推荐）：** 转投匹配的会议——NeurIPS 2026（有 Safety/Interpretability track，deadline 通常 5-6 月）、EMNLP 2026、AAAI 2027。本 proposal 的内容与这些会议高度匹配。
  - **方案 B（不推荐，成本极高）：** 将整个 proposal 重新定位为 robot learning 问题——例如研究 embodied agent 在 manipulation task 中的 tool-selection faithfulness（机械臂选择 grasp vs. push vs. reposition 的推理忠实性），需要重建 benchmark、重新设计 domain、引入 real-robot 或 sim 实验，基本等于重写一篇新论文。
- **调研依据:** CoRL 2026 官方 Call for Papers（https://www.corl.org/contributions/call-for-papers）。

---

**以下发掘建议基于"已转投至匹配会议（如 NeurIPS 2026）"的前提：**

---

【发掘点 1】
- **维度:** trivial alternative 威胁
- **内容:** 本 proposal 的核心 behavioral intervention protocol（reason-flip, reason-ablate, counterfactual-inject, reason-scramble）本质上是将 RFEval 的 counterfactual intervention 框架从 QA/math reasoning 迁移到 tool selection。审稿人会问：**这个迁移本身有多 non-trivial？** RFEval 已经提供了成熟的 stance consistency + causal influence 框架，将干预对象从"reasoning about an answer"换成"reasoning about a tool call"是否属于 straightforward domain transfer？如果是，那核心贡献就缩窄为"在新 domain 上复现了 RFEval 的发现"。**Proposal 需要清晰 argue 为什么 tool selection 的 faithfulness 问题在结构上不同于 QA faithfulness**——例如：tool call 有 structured output（JSON schema），而非 free-form answer；tool call 有 downstream effect（执行结果反馈到下一轮），创造了 QA 不存在的 temporal dependency；multi-turn 的 context accumulation 改变了 intervention 的 semantics（你 flip 的 reasoning 可能与先前 turn 的 tool result 矛盾，创造 incoherence）。这些结构性差异应该被提升为核心 novelty claim 的一部分，而不仅仅是"我们把 X 用在了新领域 Y"。
- **价值:** 直接提升 Novelty 维度——从"domain transfer"升级为"结构性新问题需要新方法论适配"。
- **调研依据:** RFEval (2602.17053) 的框架已非常成熟且被 ICLR 2026 接收，审稿人必然会追问差异化。

【发掘点 2】
- **维度:** 核心 claim 强化
- **内容:** Proposal 提出的最有趣的假设是 **"harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones"**——这是一个 counterintuitive prediction，如果被验证，是非常强的 contribution。但当前 proposal 对这个假设的理论动机阐述不足（仅一句"because genuine deliberation is required"）。建议将这个假设提升为论文的 **central narrative**：构建一个"deliberation threshold"的理论模型——当 tool choice 是 trivial 时，模型走 System 1 fast path（直接从 latent policy 选择），CoT 变成 post-hoc rationalization；当 tool choice genuinely ambiguous 时，模型被迫走 System 2 deliberation path，CoT 成为真正的计算介质。这个 framing 将 tool-selection faithfulness 从一个 benchmark paper 提升为一个有 explanatory power 的 framework paper。具体地，三个 tier（Unambiguous/Soft/Hard）不再只是 benchmark stratification，而是对应理论预测的三个 regime。
- **价值:** 提升 Significance 维度——从"我们测量了 faithfulness"升级为"我们发现并解释了 faithfulness 随 task difficulty 的非单调变化规律"。
- **调研依据:** "Brief Is Better" (2604.02155) 已经发现 CoT budget 对 function-calling 有 non-monotonic 效果，暗示了 deliberation dynamics 的复杂性。"Decoding Answers Before CoT" (2603.01437) 的 0.9 AUC pre-CoT probing 支持"System 1 fast path"假说（答案在 CoT 之前已编码）。

【发掘点 3】
- **维度:** related work 差异化
- **内容:** Proposal 对 **"Beyond the Black Box" (2605.06890)** 的定位可能低估了其威胁性。当前 proposal 将其描述为"applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness"。但该工作已经在 multi-step agentic trajectory 上建立了 probing 基础设施——如果他们的后续工作简单扩展到 tool identity probing（技术上直接可行），本 proposal 的 mechanistic probing 部分的 novelty 就会大幅缩水。**建议：(1)** 明确 acknowledge 2605.06890 的 coverage 而非 downplay 它；**(2)** 将 proposal 的 mechanistic 贡献聚焦在 behavioral-mechanistic coupling 上（即发掘点 2 中"behavioral intervention 结果与 probe 结果的相关性分析"），这是 2605.06890 完全没有触及的维度——它只做了 probing，没有做 behavioral intervention，更没有做两者的 coupling analysis。
- **价值:** 提升 Related Work 差异化——预防审稿人认为 mechanistic probing 部分是 incremental extension of 2605.06890。
- **调研依据:** 2605.06890 已在 multi-step trajectory 上部署了 SAE + linear probe，与本 proposal 的 probing component 有直接技术重叠。

【发掘点 4】
- **维度:** significance 提升
- **内容:** 当前 proposal 的 significance 叙事主要停留在"unfaithful tool selection can cascade into harmful actions"这一 safety motivation。但这个 motivation 偏 abstract——审稿人会问"so what, this is true for any unfaithful reasoning"。建议引入一个更锐利的 significance angle：**multi-turn tool selection 是目前 AI agent 可观测推理与不可观测行为之间 alignment gap 最大的场景**。具体论证：(1) 与 QA 不同，tool call 是 action（有不可逆的 real-world effect）；(2) 与 single-turn 不同，multi-turn 中 early unfaithfulness 通过 tool result 反馈 compound（一个基于错误理由选择的 API call 的结果会 condition 所有后续推理）；(3) 当前的 agent monitoring 方案（如 SAVeR）假设 CoT 是 faithful 的，如果这个假设不成立，整个 monitoring paradigm 需要重新审视。第 (3) 点特别有力，因为它将本工作定位为对一个正在被广泛部署的 safety mechanism 的 validity check。
- **价值:** 提升 Significance 维度——从 general safety motivation 升级为对当前 agent monitoring paradigm 的 foundational challenge。
- **调研依据:** SAVeR (2604.08401) 和 "Noticing the Watcher" (2603.16928) 都在构建基于 CoT 的 agent monitoring，隐含假设了 CoT 的 faithfulness。

【发掘点 5】
- **维度:** novelty 锐化
- **内容:** Proposal 目前试图同时做两件大事：(1) behavioral causal intervention benchmark (TOOLFAITH-BENCH + TSCF/RTI metrics)，(2) multi-turn mechanistic probing (cross-turn probe transfer, encoding drift, replanning signals, behavioral-mechanistic coupling)。对于一篇会议论文来说，这两件事的结合既是优势也是风险。优势是 uniqueness（无人做过两者的 coupling）；**风险是审稿人认为每一半都不够深**——behavioral 部分看起来像 RFEval 的 domain transfer，mechanistic 部分看起来像 2605.07990 的 multi-turn extension。建议做出取舍：**将 behavioral-mechanistic coupling analysis 提升为论文的核心独特贡献**，而将 pure behavioral benchmark 和 pure probing 各自 condense 为 supporting components。核心 research question 应该是："当 probe 在 CoT 生成之前就检测到了 tool identity 的 pre-commitment（mechanistic unfaithfulness），behavioral intervention 是否也会显示 low TSCF（behavioral unfaithfulness）？" 如果两种独立的 unfaithfulness measure 高度相关，这是一个非常强的发现（convergent validity）；如果不相关，这同样是一个重要发现（暗示存在多种不同的 unfaithfulness mechanism）。
- **价值:** 同时提升 Novelty 和 Significance——将论文从"两个方向的分别推进"重新定位为"两个方向的 convergence/divergence 分析"，这是任何单独做 behavioral 或 mechanistic 的工作都无法提供的。
- **调研依据:** 基于领域整体趋势判断——behavioral intervention (RFEval 路线) 和 mechanistic probing (2605.07990 路线) 目前是两个平行发展的 community，无人做过两者的 systematic coupling analysis。

---

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing (SAVeR)](https://arxiv.org/abs/2604.08401)
- [CoRL 2026 About Page](https://www.corl.org/about-corl)

【补救 agent 本轮输出】:
Now I have sufficient research to provide a thorough analysis. Let me compile my findings.

---

【状态】: 发现致命缺陷

【前置调研发现】
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026): 12 models probed for single-turn tool-call readability; 93-100% steering accuracy at 4B+; multi-turn explicitly marked "fragile" (-30 to +10pp). Experimental design: linear probes on residual stream, mean-difference steering vectors, single-turn fixed-menu setup. No behavioral interventions on CoT.
- [RFEval](https://arxiv.org/abs/2602.17053) (arXiv 2026): 7,186 instances, 12 open-source LRMs, counterfactual output-level interventions measuring stance consistency + causal influence. Metrics: per-instance faithfulness rate, domain-stratified analysis, correlation with post-training regime. Evaluated ~50% unfaithfulness. Key design choice: faithfulness decoupled from correctness.
- [Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv 2026): 12 models, 498 MCQs, 6 hint categories, 41,832 inference runs. Metrics: per-model faithfulness rate, thinking-vs-output acknowledgment gap (87.5% vs 28.6%). Key design: fine-grained analysis by hint type, model family, and parameter count; regression analysis showing training method > scale.
- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252) (arXiv 2026): Binary tool-necessity probing at 0.89-0.96 AUROC. Ablation: soft vs. hard prefill, temperature scaling, layer selection, data efficiency, regularization strength, OOD transfer, multi-hop transfer.
- [FACT-E](https://arxiv.org/abs/2604.10693) (ACL 2026 Findings): Causality-inspired perturbation framework for CoT evaluation; uses controlled perturbations as instrumental signal to separate genuine step-to-step dependence from bias artifacts.
- [BFCL v3 / ToolBench / MAVEN](https://benchlm.ai/llm-agent-benchmarks) (2025-2026): Current tool-calling benchmarks use AST evaluation, multi-step reasoning, adversarial composition, OOD transfer. Standard practice includes serial/parallel function calls, multi-language evaluation, and explicit distractor tools.
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. **Submissions without a robotics focus will be returned without review.**"
- 调研总结: 该领域（CoT faithfulness + tool-call probing）的实验设计标准包括：大规模多模型评估（10+模型）、多种intervention类型的对照、faithfulness与correctness的解耦、per-domain/per-difficulty分层分析、详细ablation（层选择、probe架构、OOD迁移等）、以及统计显著性分析。审稿人普遍期望看到intervention protocol的construct validity论证、benchmark质量的human validation、以及指标间的非冗余性证明。**然而，该proposal的目标会议CoRL是机器人学习会议，与本proposal的研究内容（LLM推理忠实性）完全不匹配。**

---

【缺陷 1】
- 类别: 可行性问题
- 问题: **Proposal 目标投稿 CoRL 2026，但 CoRL 是机器人学习专业会议，明确要求 "Submissions should focus on a core robotics problem... Submissions without a robotics focus will be returned without review."** 本 proposal 的五个领域（code editing, web browsing, data analysis, system administration, information retrieval）无一涉及机器人学，全文没有任何 robotics 相关内容。论文几乎必然在 desk review 阶段被退回。
- 严重度: 不可补救（方向性致命）
- 补救方案: 此缺陷**在不改变 idea 核心的前提下无法补救**。即使实验设计再完美，CoRL 的 scope 明确排斥非机器人主题。需要更换投稿目标至匹配的会议，如 NeurIPS 2026、ICML 2026、ICLR 2027、ACL/EMNLP 2026（如果偏 NLP agent），或 AAAI 2027 等接受 LLM interpretability/faithfulness 研究的综合性 AI 会议。如果坚持 CoRL，则需要将整个 benchmark 和实验重新设计为机器人操控场景中的 tool-selection faithfulness（如机械臂工具选择、导航动作选择等），这本质上是一个全新的项目。
- 调研依据: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确声明 robotics focus 要求

---

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 的 multi-turn intervention protocol 在关键操作层面缺乏规范。具体地：(a) 在多轮对话中，perturbation 作用于哪一个 turn 的 CoT？如果对 turn 3 的 reasoning 做 reason-flip，turn 5 的模型是否能看到 turn 3 的原始或修改后的推理？(b) 四种 intervention（reason-flip, reason-ablate, counterfactual-inject, reason-scramble）在 multi-turn 中如何处理跨 turn 的推理依赖——例如 turn 5 的推理引用了 turn 3 的工具调用结果，而 turn 3 的工具调用是被 intervention 改变的？(c) 不清楚每个 decision point 是独立做 intervention 还是级联做 intervention（all points simultaneously）。RFEval 和 "Lie to Me" 的 intervention 设计之所以有效，是因为单轮设置避免了这些级联问题。
- 严重度: 可补救
- 补救方案: 明确定义两种 intervention regime 并分别报告结果：(1) **Point-wise intervention**——仅对单个 decision point 做 perturbation，保持其他 turn 不变，观察该 decision point 的工具选择变化；(2) **Cascading intervention**——从某个 turn 开始 intervene，让后续 turn 自然生成（包括受干扰的 tool results），观察下游 decision points 的工具选择变化。两种 regime 测量不同维度：前者测局部 faithfulness，后者测 cascading unfaithfulness。此外需明确：在 point-wise intervention 中，对 turn k 做 reason-flip 后，turn k+1 看到的是模型基于 flipped reasoning 实际执行的 tool 结果，还是原始 tool 结果？这会显著影响实验结论。
- 调研依据: RFEval (2602.17053) 的 intervention 设计仅覆盖单轮，未处理级联问题；Breaking the Chain (2603.16475) 对中间结构做 intervention 但也限于单轮推理链，未扩展到 multi-turn 对话场景

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: TSCF（Tool Selection Causal Fidelity）和 RTI（Reasoning Theater Index）两个指标之间的关系不清晰，存在近冗余风险。Proposal 定义 TSCF 为 "tool calls correctly follow intervened reasoning" 的比率，RTI 为 "tool calls remain unchanged despite contradictory reasoning" 的比率。对于 reason-flip intervention，如果模型要么跟随新 reasoning 选择新 tool（high TSCF），要么无视新 reasoning 保持原 tool（high RTI），则 TSCF + RTI ≈ 1（第三种情况——既不跟随也不保持原选择——的概率需要讨论）。审稿人很可能质疑两个指标是否提供独立信息。此外，对 Tier 3 (Hard-Ambiguous) 场景中多个 valid tool 的情况，"correctly follow" 如何形式化定义未说明。
- 严重度: 可补救
- 补救方案: (1) 形式化定义三种 outcome：**Follow**（选择 intervened reasoning 指向的工具）、**Ignore**（保持原工具不变）、**Diverge**（选择第三个工具，既非原工具也非 intervention 指向的工具）。报告三者的分布比例，其中 Diverge rate 本身就是一个有趣的信号（模型可能有自己的 latent policy 独立于任何 reasoning）。(2) 对 Tier 3 场景，定义 faithfulness 为 "reasoning-tool logical consistency"：如果 CoT 中列出了选择 tool A 的理由，但实际调用了 tool B（即使 B 也是 valid 的），则标记为 unfaithful。使用 LLM judge 评估 reasoning-tool consistency（参考 C2-Faith 的 LLM-as-judge 方法但需报告 inter-rater agreement）。(3) 明确 TSCF 和 RTI 在不同 intervention 类型下的解释差异——reason-ablate 下没有 "target tool" 可以 follow，所以 TSCF 在该条件下应有不同定义。
- 调研依据: RFEval (2602.17053) 将 faithfulness 分解为 stance consistency 和 causal influence 两个独立维度来避免指标冗余；C2-Faith (2603.05167) 指出 LLM-as-judge 评估 faithfulness 存在 systematic blind spots，建议报告 localization-level agreement

【缺陷 4】
- 类别: ablation 不完整
- 问题: Proposal 未提出任何显式的 ablation study 设计。对于一个引入新 benchmark（TOOLFAITH-BENCH）、新 intervention protocol、新指标（TSCF/RTI）、以及新 probing 分析的论文，缺少 ablation 会让审稿人无法判断各设计决策的贡献和必要性。同领域论文（2605.07990, 2605.09252）均包含详细 ablation（层选择、probe 架构、数据效率、OOD 迁移等）。
- 严重度: 可补救
- 补救方案: 需要设计以下 ablation studies：
  - **(A) Conversation depth ablation**: 将 faithfulness 指标按 decision point 位置分析（turn 2 vs turn 4 vs turn 8），验证 Hypothesis "probe accuracy degrades with conversation depth"
  - **(B) Intervention position ablation**: 在对话的早期 vs 中期 vs 晚期 decision point 做 intervention，分析位置效应
  - **(C) Tool menu size ablation**: 固定场景但变化可用工具数量（5, 10, 20 tools），分析工具菜单规模对 faithfulness 的影响
  - **(D) Perturbation strength ablation**: 对 reason-flip，测试从 "微调一个关键句" 到 "完全重写" 的不同强度，绘制 faithfulness 随 perturbation 强度的曲线
  - **(E) Probing layer selection**: 报告不同层的 probe accuracy（参考 2605.07990 的 per-layer 分析），明确 multi-turn probing 的最优层是否与 single-turn 一致
  - **(F) Tier boundary sensitivity**: 对 Tier 2 的 "soft-ambiguous" 场景，通过调整 tool 描述使其更接近 Tier 1 或 Tier 3，分析 faithfulness 在 ambiguity 连续谱上的变化
- 调研依据: 2605.07990 包含 per-layer probe accuracy, model-size scaling, domain transfer ablation; 2605.09252 包含 soft vs hard prefill, temperature scaling, layer selection, data efficiency, regularization strength ablation

【缺陷 5】
- 类别: 实验设计不足
- 问题: Benchmark 的 ground truth 建立和质量控制方案不足。Proposal 提到使用 Claude 辅助生成场景并进行 "tiered difficulty validation"，但未说明：(a) 每个 tier 的分类标准如何操作化——谁判断一个场景是 Unambiguous vs Soft-Ambiguous？用什么标准？(b) 人工验证的规模（多少 annotator、inter-annotator agreement 目标是多少）？(c) 对于 Tier 2 "one clearly optimal tool among plausible candidates" 的判断标准——"clearly optimal" 是通过人工共识还是性能指标定义的？(d) Tier 3 场景中 "genuinely valid" 工具的验证方式。Benchmark 的 construct validity 是全文实验结论的基础，如果 tier 分类不可靠，所有按 tier 分析的结论都会受质疑。
- 严重度: 可补救
- 补救方案: (1) 设计 pilot study：先生成 100 个候选场景，请 3+ 名 annotator 独立标注 tier，计算 Fleiss' κ 或 Krippendorff's α，目标 > 0.7。(2) 对 Tier 2 场景，定义 "optimality gap"：让 annotator 对每个候选工具打 1-5 分适用度评分，要求最优工具得分与次优工具得分差值在 [1.0, 2.5] 区间（太小变成 Tier 3，太大变成 Tier 1）。(3) 对 Tier 3 场景，要求至少 2 名 annotator 独立确认存在 ≥2 个得分差 < 0.5 的工具。(4) 在论文中报告 benchmark statistics：per-tier 的 annotator agreement、场景长度分布、工具数量分布、domain 分布等。(5) 预留 10% 场景做 held-out validation——在实验结束后检查这些场景上的结果是否与主集一致。
- 调研依据: RFEval (2602.17053) 使用了明确的 counterfactual generation pipeline 并报告了 construct validity；FaithCoT-Bench (ICLR 2026, 2510.04040) 对每个 instance 的 ground truth 均有 human validation protocol

【缺陷 6】
- 类别: 实验设计不足
- 问题: Multi-turn probing 的四个 novel analyses 方法论细节不足，尤其是：(a) **Cross-turn probe transfer** ——仅说 "probe trained at decision point 1 generalizes to decision point 3"，未指定 probe 架构（线性？MLP？）、训练数据规模、训练/测试分割策略、以及 "generalization" 的量化标准。(b) **Context-dependent encoding drift** ——如何度量 "the linear direction encoding a given tool shifts across turns"？cosine similarity between direction vectors? explained variance ratio? 没有明确。(c) **Error-induced replanning signals** ——如何系统性引入工具执行错误？自然错误的发生率可能太低导致样本量不足。(d) **Faithfulness coupling** ——"correlating probe-detected pre-commitment with behavioral unfaithfulness" 的相关性分析方法（Pearson? Spearman? point-biserial?）和统计检验未提及。
- 严重度: 可补救
- 补救方案: 
  - **(a)** 明确使用 logistic regression probe（与 2605.07990 保持一致以便直接比较），训练数据来自每个 decision point 对应 layer 的 residual stream activations，报告 5-fold cross-validation accuracy 和 bootstrap CI
  - **(b)** 定义 encoding drift = 1 - cos(v_tool^{turn_i}, v_tool^{turn_j})，其中 v_tool 是对特定 tool 的 probe weight vector。对每对 turn 计算 drift 矩阵，可视化为 heatmap
  - **(c)** 设计 synthetic error injection：在正常 tool 返回的结果中注入 3 类错误（API error / wrong format / logically incorrect result），每类 50+ instances，确保样本量足够。对比 error 前后同一层的 activation shift（L2 distance 或 cosine shift）
  - **(d)** 使用 point-biserial correlation（probe pre-commitment 是连续变量，behavioral faithfulness 是二元变量），报告 r_pb 和 p-value，并用 permutation test 做 robustness check
- 调研依据: 2605.07990 使用 logistic regression probe + mean-difference steering，per-layer 分析，5-fold cross-validation；2605.09252 报告 AUROC + bootstrap confidence intervals

【缺陷 7】
- 类别: 实验设计不足
- 问题: Proposal 未提及任何统计分析方法。对 7 个模型 × 3 个 tier × 4 种 intervention × 5 个 domain 的大规模比较实验，缺少统计检验会导致审稿人无法判断观察到的差异是否显著。特别是 Hypothesis 3（"harder ambiguous scenarios may elicit more faithful reasoning"）和 Hypothesis 2（"probe accuracy degrades with conversation depth"）需要严格的统计支撑。
- 严重度: 可补救
- 补救方案: (1) 对主要 claim 使用 bootstrap CI（10,000 resamples）报告 95% 置信区间。(2) 对 tier 间的 TSCF/RTI 差异使用 paired permutation test 或 Wilcoxon signed-rank test。(3) 对模型间比较使用 Friedman test + Nemenyi post-hoc 检验（参考 ML 领域多分类器比较的标准做法）。(4) 对多重比较问题，使用 Bonferroni 或 Holm 校正。(5) 在 "counterintuitive" Hypothesis 3 上，需要进行 power analysis 确保 600 场景（200 per tier）的样本量足以检测到预期的 effect size。
- 调研依据: 基于领域实验规范判断；RFEval 进行了 per-domain 和 per-model 的统计分析；"Lie to Me" 使用了 regression analysis 分析变量间关系

【缺陷 8】
- 类别: baseline 不足或过时
- 问题: Proposal 的 behavioral experiment 缺乏与现有 faithfulness 测量方法的对比 baseline。目前测量 CoT faithfulness 的方法至少包括：(a) 早期答案 probing (Decoding Answers Before CoT, 2603.01437)，(b) activation-based rationalization detection (Catching Rationalization in the Act, 2603.17199)，(c) LLM-as-judge (C2-Faith, 2603.05167)，(d) self-evaluation (FACT-E, 2604.10693)。Proposal 应展示其 behavioral intervention 方法相对于这些替代方法在 tool-selection faithfulness 测量上的优势或互补性。
- 严重度: 可补救
- 补救方案: 增加一组 **method comparison experiment**：在同一场景子集上（如 100 个场景），同时使用以下方法测量 faithfulness：(1) 本文的 behavioral intervention (TSCF/RTI)；(2) pre-tool-call probing（扩展 2605.07990 到 multi-turn）；(3) LLM-as-judge for reasoning-action consistency（扩展 C2-Faith 到 tool selection）。比较三种方法的一致性（Cohen's κ）和各自独特发现。这不仅加强了实验的 soundness，还能直接支撑 "behavioral-mechanistic faithfulness coupling" 分析。
- 调研依据: 2603.17199 (Catching Rationalization in the Act) 使用 activation probing 检测 motivated reasoning，证明 internal representations 优于 CoT monitors；C2-Faith (2603.05167) benchmark LLM-as-judge 方法

【缺陷 9】
- 类别: 可行性问题
- 问题: Compute 资源估算可能偏乐观。4 个 open-weight 模型中 DeepSeek-V4-Pro 的参数规模可能很大（V3 已经是 671B MoE），在 multi-turn 场景下推理成本较高。600 scenarios × 4 interventions × 3 tiers 的每个 decision point 需要完整 multi-turn 推理（2-4 decision points → 4-12 turns per scenario）。加上 probing 需要存储所有 intermediate activations（对大模型可能需要大量 CPU/GPU 内存），300 H100-hours 可能不够。此外，API 成本估算 ($350-450) 在当前 frontier model pricing 下可能偏低：600 × 4 × 3 个 frontier model calls，每个 multi-turn 平均 ~20K tokens，总计约 14.4M tokens per model × 3 models ≈ 43M tokens，仅 input 成本在 $3-15/M tokens 级别就可能达到 $130-650，加上 output tokens 可能超过预算。
- 严重度: 可补救
- 补救方案: (1) 重新估算：明确列出每个模型的推理吞吐量和每个实验条件的预期 token 数，自底向上计算总 compute。(2) 对最大的 open-weight 模型（DeepSeek-V4-Pro），考虑使用量化版本（如 INT4/FP8）以降低 GPU 内存和推理时间。(3) 为 probing 实验单独预算存储 activations 的成本。(4) 预留 20-30% buffer 应对意外（如某些模型推理速度比预期慢、需要 re-run 等）。(5) 如果资源紧张，可以先对 200 scenarios 的子集做完整实验，验证方法论后再扩展到 600。
- 调研依据: 基于领域实验规范判断；2605.07990 仅评估到 27B 模型即已需要大量 compute，multi-turn 场景下成本倍增

---

**总结**: 最关键的问题是**缺陷 1（CoRL venue mismatch）**——这是一个方向性致命缺陷，无论实验设计如何完善，该论文都不在 CoRL 的 scope 内，几乎必然被 desk reject。建议立即更换目标会议（NeurIPS / ICML / ICLR / AAAI 等综合性 AI 会议，或 ACL / EMNLP 如果强调 NLP agent 角度）。其余 8 个缺陷均可补救，且补救方案具体可行——如果解决了 venue 问题，这些改进可以显著提升论文的实验 soundness。

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning](https://arxiv.org/abs/2603.22582)
- [LLM Agents Already Know When to Call Tools](https://arxiv.org/abs/2605.09252)
- [FACT-E: Causality-Inspired Evaluation for Trustworthy CoT Reasoning](https://arxiv.org/abs/2604.10693)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [LLM Agent & Tool-Use Benchmarks 2026](https://benchlm.ai/llm-agent-benchmarks)
- [C2-Faith: Benchmarking LLM Judges](https://arxiv.org/abs/2603.05167)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "6fa36db9-bcb5-4486-8d9d-965659d3fbb2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:45:45.827Z_

```json
{
  "parentUuid": "6fa36db9-bcb5-4486-8d9d-965659d3fbb2",
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
  "uuid": "f2223ebd-de9a-4e8c-a631-93ae386351cb",
  "timestamp": "2026-05-19T18:45:45.827Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:45:45.827Z_

```json
{
  "parentUuid": "f2223ebd-de9a-4e8c-a631-93ae386351cb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0f24c166-d7af-408b-a7e1-1f269c70f9c0",
  "timestamp": "2026-05-19T18:45:45.827Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: I now have sufficient information to provide my assessment. Let me compile my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "0f24c166-d7af-408b-a7e1-1f269c70f9c0",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:46:34.117Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully. I'm the 终审 agent (Meta Judge / Iteration Controller) in Role B (迭代中), processing Round 1 outputs from both the 发掘 agent and 补救 agent.

Let me first understand the current proposal and what both agents found:

**Critical Finding from BOTH agents**: The proposal targets CoRL 2026, which is a robotics conference. The proposal is about LLM agent tool-selection faithfulness - completely unrelated to robotics. Both agents independently flagged this as a fatal/致命 issue. This is a very strong consensus signal.
 
Now I'm reviewing the detailed findings from each agent. The 发掘 agent identified the venue mismatch as fatal, then surfaced several secondary concerns including a domain transfer threat from RFEval, opportunities to strengthen the "deliberation threshold" narrative, a potentially conflicting related work paper, and ways to reframe the significance around agent monitoring paradigms. The 补救 agent also confirmed the fatal venue issue but focused on different implementation gaps: the multi-turn intervention protocol needs more specificity, the TSCF and RTI metrics appear redundant, ablation studies are missing, and the benchmark ground truth definition is incomplete.

The next steps are to validate these findings through cross-validation research, decide which suggestions to incorporate, update the proposal accordingly, and estimate success probability. The key decision point is whether the venue mismatch is truly fatal to the idea itself or just a targeting problem that can be fixed. Looking at the stop-loss criteria, a venue mismatch doesn't constitute an idea-level fatal flaw in the way that a trivial alternative threat or broken core claim would—the research concept could work elsewhere, so I should fix the venue and continue iterating rather than abandoning the proposal entirely. The core issue is that the task explicitly asks me to evaluate for CoRL 2026 specifically, which means I need to give a straight answer: the venue mismatch makes acceptance essentially impossible, so a desk reject is nearly certain. But I can be more helpful by suggesting a pivot to NeurIPS 2026 and continuing to refine the idea for that target instead. The venue mismatch is fatal for CoRL specifically, but the core idea itself has merit elsewhere—I should recommend a desk reject for CoRL 2026 while suggesting retargeting to conferences like NeurIPS that better fit the proposal's scope. I'll do some quick verification on the venue requirements and deadlines to give the most useful guidance, even though the stop-loss criteria are clearly met for this particular submission. I'm realizing the core issue is venue-specific rather than conceptual—CoRL 2026 would reject this outright, but the idea itself is sound. Since retargeting to NeurIPS 2026 is straightforward, I should recommend the stop-loss for CoRL while pivoting the submission strategy and incorporating the improvement suggestions for the new venue.

Now I need to verify the critical claims before finalizing my recommendation: whether CoRL's scope truly excludes this work, if NeurIPS 2026's timeline is feasible, and whether the recent "Beyond the Black Box" paper and RFEval's domain transfer limitations pose real threats to the novelty and contribution claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f24c166-d7af-408b-a7e1-1f269c70f9c0",
  "isSidechain": false,
  "requestId": "req_011CbCRXctAk9bCpwdHYSvJi",
  "type": "assistant",
  "uuid": "d573310e-1532-4e73-b7a0-bd585c7a9717",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNSbJjJTLTHwyX7QqWrfp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12399,
      "cache_read_input_tokens": 16560,
      "output_tokens": 2036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2036,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 12399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12399
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

_source line 9 · 2026-05-19T18:46:34.125Z_

Let me first do cross-validation research on the key claims from both agents before making my decision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d573310e-1532-4e73-b7a0-bd585c7a9717",
  "isSidechain": false,
  "requestId": "req_011CbCRXctAk9bCpwdHYSvJi",
  "type": "assistant",
  "uuid": "db5bc5dc-94f2-4405-9477-f4ff6adcb3e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNSbJjJTLTHwyX7QqWrfp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12399,
      "cache_read_input_tokens": 16560,
      "output_tokens": 2036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2036,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 12399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12399
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

### Tool call

_source line 10 · 2026-05-19T18:46:34.126Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HuLsDsjwZxHu2EYt5Bjhri`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db5bc5dc-94f2-4405-9477-f4ff6adcb3e3",
  "isSidechain": false,
  "requestId": "req_011CbCRXctAk9bCpwdHYSvJi",
  "type": "assistant",
  "uuid": "4c3c8296-b851-46ad-8c54-bf791fbadc81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNSbJjJTLTHwyX7QqWrfp2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12399,
      "cache_read_input_tokens": 16560,
      "output_tokens": 2036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2036,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 12399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12399
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

### Tool result

_source line 11 · 2026-05-19T18:46:34.133Z_

<details><summary>↩ Tool result · `toolu_01HuLsDsjwZxHu2EYt5Bjhri`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c3c8296-b851-46ad-8c54-bf791fbadc81",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "d2cc8f57-d3e7-4704-8199-4617c570a460",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4c3c8296-b851-46ad-8c54-bf791fbadc81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:46:38.769Z_

Now let me run multiple verification searches in parallel:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2cc8f57-d3e7-4704-8199-4617c570a460",
  "isSidechain": false,
  "requestId": "req_011CbCRbB514NXLuZ5HUBNNd",
  "type": "assistant",
  "uuid": "56bde66a-863e-427a-9047-3bd227fd9093",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAg5kWfav15eLbWoJQpP6Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 28959,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 28959,
          "cache_creation_input_tokens": 2559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2559
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

### Tool call

_source line 13 · 2026-05-19T18:46:38.831Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFbRZXBd7cmwkoG5d5sfg6`</summary>

```json
{
  "query": "CoRL 2026 call for papers robotics focus submission requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56bde66a-863e-427a-9047-3bd227fd9093",
  "isSidechain": false,
  "requestId": "req_011CbCRbB514NXLuZ5HUBNNd",
  "type": "assistant",
  "uuid": "10942c03-bf9f-48cb-ac4d-0102aefdc5bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAg5kWfav15eLbWoJQpP6Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 28959,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 28959,
          "cache_creation_input_tokens": 2559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2559
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

### Tool result

_source line 14 · 2026-05-19T18:46:46.252Z_

<details><summary>↩ Tool result · `toolu_01GFbRZXBd7cmwkoG5d5sfg6`</summary>

```text
Web search results for query: "CoRL 2026 call for papers robotics focus submission requirements"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2025 - Call for Papers","url":"https://2025.corl.org/contributions/call-for-papers"}]

Based on the search results, here are the key details about CoRL 2026's Call for Papers:

## Robotics Focus Requirement

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review.

## Submission Requirements

**Page Limit:** Page limit will be 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

**Reviewer Requirement:** All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.

**Limitations Section:** All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

**Experimental Validation:** Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

## Submission Deadline

The paper submission deadline is May 29, 2026. Papers may be submitted through OpenReview via the link here (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10942c03-bf9f-48cb-ac4d-0102aefdc5bf",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "cd95b2b3-fd9e-4287-84aa-52d701688340",
  "toolUseResult": {
    "query": "CoRL 2026 call for papers robotics focus submission requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KmYS82jTh4i355JcXz8yzZ",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2025 - Call for Papers",
            "url": "https://2025.corl.org/contributions/call-for-papers"
          }
        ]
      },
      "Based on the search results, here are the key details about CoRL 2026's Call for Papers:\n\n## Robotics Focus Requirement\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review.\n\n## Submission Requirements\n\n**Page Limit:** Page limit will be 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.\n\n**Reviewer Requirement:** All submissions must include at least one author who agrees to serve as a CoRL reviewer, and they are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.\n\n**Limitations Section:** All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.\n\n**Experimental Validation:** Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\n## Submission Deadline\n\nThe paper submission deadline is May 29, 2026. Papers may be submitted through OpenReview via the link here (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)."
    ],
    "durationSeconds": 7.416863201,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "10942c03-bf9f-48cb-ac4d-0102aefdc5bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:46:49.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014rQW7H2JH6dWhiR5wXoR5m`</summary>

```json
{
  "query": "NeurIPS 2026 call for papers deadline submission interpretability safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd95b2b3-fd9e-4287-84aa-52d701688340",
  "isSidechain": false,
  "requestId": "req_011CbCRc4iYBaJGPSLyykhnH",
  "type": "assistant",
  "uuid": "08064072-8276-46dc-a36e-ee60040f0ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEdAnX6gqtVPcHU8XsN3PX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 31518,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 844,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 31518,
          "cache_creation_input_tokens": 844,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 844
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

### Tool result

_source line 16 · 2026-05-19T18:46:56.679Z_

<details><summary>↩ Tool result · `toolu_014rQW7H2JH6dWhiR5wXoR5m`</summary>

```text
Web search results for query: "NeurIPS 2026 call for papers deadline submission interpretability safety"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call For Evaluations & Datasets 2026","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"NeurIPS 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS/ICLR/ICML Journal-to-Conference Track","url":"https://neurips.cc/public/JournalToConference"}]

Based on the search results, here's information about NeurIPS 2026 call for papers deadlines:

## Main Paper Submission Deadlines

Abstracts are due by May 4th, 2026, with full papers due on May 6th, 2026, Anywhere On Earth (AOE). NeurIPS 2026 is now accepting submissions as of April 15, 2026.

## Multiple Tracks Available

The different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines. However, the deadlines are the same as for the main and Papers for Position tracks (PPT), with abstracts due by May 4th, 2026 (AOE), and full papers due on May 6th, 2026 (AOE).

## Submission Requirements

All authors must have an OpenReview profile when submitting. We will be unable to make any exception for submissions from accounts initiated less than two weeks prior to the deadline.

The search results provided information about the general submission deadlines and tracks, but did not contain specific details about interpretability and safety as research areas within the call for papers. For more details on specific topics of interest, you may want to visit the official NeurIPS 2026 Call for Papers page at neurips.cc/Conferences/2026/CallForPapers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08064072-8276-46dc-a36e-ee60040f0ff1",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "95358674-35b8-472f-bf44-75680da8de36",
  "toolUseResult": {
    "query": "NeurIPS 2026 call for papers deadline submission interpretability safety",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AD3SWDzhdmMQYmKG4Ty6q",
        "content": [
          {
            "title": "Call for Papers 2026",
            "url": "https://neurips.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://neurips.cc/Conferences/2026/Dates"
          },
          {
            "title": "Call For Evaluations & Datasets 2026",
            "url": "https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"
          },
          {
            "title": "NeurIPS Newsletter – April 2026 – NeurIPS Blog",
            "url": "https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"
          },
          {
            "title": "NeurIPS 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/neurips-2026.html"
          },
          {
            "title": "NeurIPS 2026 Call For Competitions",
            "url": "https://neurips.cc/Conferences/2026/CallForCompetitions"
          },
          {
            "title": "NeurIPS 2026",
            "url": "https://neurips.cc/"
          },
          {
            "title": "Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"
          },
          {
            "title": "NeurIPS 2026 Call for Workshops",
            "url": "https://neurips.cc/Conferences/2026/CallForWorkshops"
          },
          {
            "title": "NeurIPS/ICLR/ICML Journal-to-Conference Track",
            "url": "https://neurips.cc/public/JournalToConference"
          }
        ]
      },
      "Based on the search results, here's information about NeurIPS 2026 call for papers deadlines:\n\n## Main Paper Submission Deadlines\n\nAbstracts are due by May 4th, 2026, with full papers due on May 6th, 2026, Anywhere On Earth (AOE). NeurIPS 2026 is now accepting submissions as of April 15, 2026.\n\n## Multiple Tracks Available\n\nThe different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines. However, the deadlines are the same as for the main and Papers for Position tracks (PPT), with abstracts due by May 4th, 2026 (AOE), and full papers due on May 6th, 2026 (AOE).\n\n## Submission Requirements\n\nAll authors must have an OpenReview profile when submitting. We will be unable to make any exception for submissions from accounts initiated less than two weeks prior to the deadline.\n\nThe search results provided information about the general submission deadlines and tracks, but did not contain specific details about interpretability and safety as research areas within the call for papers. For more details on specific topics of interest, you may want to visit the official NeurIPS 2026 Call for Papers page at neurips.cc/Conferences/2026/CallForPapers."
    ],
    "durationSeconds": 7.358449495,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08064072-8276-46dc-a36e-ee60040f0ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: I now have sufficient information to provide my assessment. Let me compile my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "95358674-35b8-472f-bf44-75680da8de36",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Tool call

_source line 19 · 2026-05-19T18:46:59.341Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016D6NW4ABcHWEkWqNJnT8e9`</summary>

```json
{
  "query": "arxiv 2605.06890 \"Beyond the Black Box\" interpretability agentic tool use SAE probing multi-step"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95358674-35b8-472f-bf44-75680da8de36",
  "isSidechain": false,
  "requestId": "req_011CbCRcqJg4s5Ehm43BsW16",
  "type": "assistant",
  "uuid": "c47db76a-6001-4a9e-8721-25331b61c6df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXWGdUNm5C1AxCZqP3UeZx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 32362,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 32362,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 867
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

### Tool result

_source line 20 · 2026-05-19T18:47:07.602Z_

<details><summary>↩ Tool result · `toolu_016D6NW4ABcHWEkWqNJnT8e9`</summary>

```text
Web search results for query: "arxiv 2605.06890 "Beyond the Black Box" interpretability agentic tool use SAE probing multi-step"

Links: [{"title":"[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/abs/2605.06890"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Beyond Black Boxes: Enhancing Interpretability of Transformers Trained on Neural Data","url":"https://arxiv.org/html/2506.14014v1"},{"title":"Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality","url":"https://arxiv.org/html/2512.10720v1"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"}]

Based on the search results, I found the arXiv paper you're looking for:

**Title:** "Beyond the Black Box: Interpretability of Agentic AI Tool Use" - a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes.

**Key Contributions:**

The framework reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be. 

By decomposing activations into sparse features, it identifies the internal layers and features most associated with tool decisions and tests their functional importance through feature ablation.

**Methodology:**

Pre-action activations are first mapped into a sparse feature basis via an SAE, then read out by two task-specific probes: the Tool-Need Probe (binary: tool call vs. no tool call) and the Tool-Risk Probe (ternary: low / medium / high risk).

**Datasets and Models:**

The probes are trained on multi-step trajectories from the NVIDIA Nemotron function-calling dataset and applied to GPT-OSS 20B and Gemma 3 27B models.

The paper addresses the challenge that agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution, and in long-horizon settings, early tool mistakes can alter the rest of the trajectory and create downstream safety and security risks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c47db76a-6001-4a9e-8721-25331b61c6df",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "35af39f2-01ae-40df-b9e4-4904581eb2fe",
  "toolUseResult": {
    "query": "arxiv 2605.06890 \"Beyond the Black Box\" interpretability agentic tool use SAE probing multi-step",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fgjdy8HYCEiCXSr15Xr8PX",
        "content": [
          {
            "title": "[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/abs/2605.06890"
          },
          {
            "title": "Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/html/2605.06890"
          },
          {
            "title": "Beyond Black Boxes: Enhancing Interpretability of Transformers Trained on Neural Data",
            "url": "https://arxiv.org/html/2506.14014v1"
          },
          {
            "title": "Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality",
            "url": "https://arxiv.org/html/2512.10720v1"
          },
          {
            "title": "Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks",
            "url": "https://arxiv.org/html/2511.19265v1"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for:\n\n**Title:** \"Beyond the Black Box: Interpretability of Agentic AI Tool Use\" - a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes.\n\n**Key Contributions:**\n\nThe framework reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be. \n\nBy decomposing activations into sparse features, it identifies the internal layers and features most associated with tool decisions and tests their functional importance through feature ablation.\n\n**Methodology:**\n\nPre-action activations are first mapped into a sparse feature basis via an SAE, then read out by two task-specific probes: the Tool-Need Probe (binary: tool call vs. no tool call) and the Tool-Risk Probe (ternary: low / medium / high risk).\n\n**Datasets and Models:**\n\nThe probes are trained on multi-step trajectories from the NVIDIA Nemotron function-calling dataset and applied to GPT-OSS 20B and Gemma 3 27B models.\n\nThe paper addresses the challenge that agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution, and in long-horizon settings, early tool mistakes can alter the rest of the trajectory and create downstream safety and security risks."
    ],
    "durationSeconds": 8.234469054999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c47db76a-6001-4a9e-8721-25331b61c6df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T18:47:15.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YKtWn1htAYmrYSGEhhVXey`</summary>

```json
{
  "query": "\"behavioral intervention\" \"mechanistic probing\" coupling faithfulness CoT reasoning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35af39f2-01ae-40df-b9e4-4904581eb2fe",
  "isSidechain": false,
  "requestId": "req_011CbCRde9Ek65HRxUCJQ7hJ",
  "type": "assistant",
  "uuid": "1b797f29-4abd-4457-a0d7-1f41035dc5f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JvhaX6LUYcc44qrnVmUL5E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 33229,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 33229,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 688
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

### Tool result

_source line 22 · 2026-05-19T18:47:22.765Z_

<details><summary>↩ Tool result · `toolu_01YKtWn1htAYmrYSGEhhVXey`</summary>

```text
Web search results for query: ""behavioral intervention" "mechanistic probing" coupling faithfulness CoT reasoning LLM 2025 2026"

Links: [{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Robust Answers, Fragile Logic: Probing the Decoupling Hypothesis in LLM Reasoning","url":"https://arxiv.org/pdf/2505.17406"},{"title":"Question Decomposition Improves the Faithfulness of Model-Generated   Reasoning","url":"https://arxiv.org/pdf/2307.11768"},{"title":"Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas","url":"https://arxiv.org/html/2605.09159v1"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"}]

The search returned highly relevant research from 2025-2026 on the intersection of behavioral interventions, mechanistic probing, and CoT faithfulness. Here are the key findings:

## CoT Faithfulness and Decoupling

The utility of CoT toward interpretability depends upon its faithfulness—whether the model's verbalized reasoning reflects its true decision-making process. Recent work challenges this assumption directly: The Decoupling Hypothesis proposes that the generation of reasoning paths and the selection of the answer are not strictly causally bound, but rather loosely correlated.

## Mechanistic Probing Approaches

Several papers combine mechanistic probing with behavioral interventions:

- Existing methodologies for evaluating CoT faithfulness primarily rely on behavioral interventions, such as corrupting or truncating the reasoning chain, though this approach often treats faithfulness as a binary property and fails to capture graded causal contributions of individual reasoning steps.

- One approach introduces a causal, layerwise intervention and a CoT-specific metric (CMI) to test whether models mechanistically rely on CoT and measure dependence using the CoT Mediation Index.

- Causal faithfulness asks whether features are actionable as steering targets, with persona-direction interventions applied at the paragraph level to improve accuracy.

## Measuring Step-Level Faithfulness

Testing across syntactic, logical, and arithmetic tasks discovered a consistent Reasoning Horizon at 70–85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.

This body of research demonstrates sophisticated coupling of behavioral testing and mechanistic analysis to probe LLM reasoning faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b797f29-4abd-4457-a0d7-1f41035dc5f5",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "c18ac9ce-f894-4984-8215-7a44a3a1feff",
  "toolUseResult": {
    "query": "\"behavioral intervention\" \"mechanistic probing\" coupling faithfulness CoT reasoning LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LrcgfVuNCpt5g6ENiawdtz",
        "content": [
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Robust Answers, Fragile Logic: Probing the Decoupling Hypothesis in LLM Reasoning",
            "url": "https://arxiv.org/pdf/2505.17406"
          },
          {
            "title": "Question Decomposition Improves the Faithfulness of Model-Generated   Reasoning",
            "url": "https://arxiv.org/pdf/2307.11768"
          },
          {
            "title": "Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas",
            "url": "https://arxiv.org/html/2605.09159v1"
          },
          {
            "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/pdf/2603.17199"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "Automated Interpretability-Driven Model Auditing and Control: A Research Agenda",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2602.11201"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          }
        ]
      },
      "The search returned highly relevant research from 2025-2026 on the intersection of behavioral interventions, mechanistic probing, and CoT faithfulness. Here are the key findings:\n\n## CoT Faithfulness and Decoupling\n\nThe utility of CoT toward interpretability depends upon its faithfulness—whether the model's verbalized reasoning reflects its true decision-making process. Recent work challenges this assumption directly: The Decoupling Hypothesis proposes that the generation of reasoning paths and the selection of the answer are not strictly causally bound, but rather loosely correlated.\n\n## Mechanistic Probing Approaches\n\nSeveral papers combine mechanistic probing with behavioral interventions:\n\n- Existing methodologies for evaluating CoT faithfulness primarily rely on behavioral interventions, such as corrupting or truncating the reasoning chain, though this approach often treats faithfulness as a binary property and fails to capture graded causal contributions of individual reasoning steps.\n\n- One approach introduces a causal, layerwise intervention and a CoT-specific metric (CMI) to test whether models mechanistically rely on CoT and measure dependence using the CoT Mediation Index.\n\n- Causal faithfulness asks whether features are actionable as steering targets, with persona-direction interventions applied at the paragraph level to improve accuracy.\n\n## Measuring Step-Level Faithfulness\n\nTesting across syntactic, logical, and arithmetic tasks discovered a consistent Reasoning Horizon at 70–85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.\n\nThis body of research demonstrates sophisticated coupling of behavioral testing and mechanistic analysis to probe LLM reasoning faithfulness."
    ],
    "durationSeconds": 7.65478312600001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1b797f29-4abd-4457-a0d7-1f41035dc5f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T18:47:25.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MD7hvMwdbncusooev5okF5`</summary>

```json
{
  "query": "ICML 2026 submission deadline call for papers LLM agent interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c18ac9ce-f894-4984-8215-7a44a3a1feff",
  "isSidechain": false,
  "requestId": "req_011CbCReksabLtYDGoT4HPww",
  "type": "assistant",
  "uuid": "5cac239a-ae6c-4db8-b3e8-3c852766efc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014raunRfrQX8PhYQ3s5rfbn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 33917,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 33917,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 915
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

### Tool result

_source line 24 · 2026-05-19T18:47:33.718Z_

<details><summary>↩ Tool result · `toolu_01MD7hvMwdbncusooev5okF5`</summary>

```text
Web search results for query: "ICML 2026 submission deadline call for papers LLM agent interpretability"

Links: [{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"IEEE ICMLCN 2026 | IEEE International Conference on Machine Learning for Communication and Networking 2026 | IEEE ICMLCN 2026","url":"https://icmlcn2026.ieee-icmlcn.org/"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"}]

Based on the search results, here's the information about ICML 2026 submission deadlines and call for papers:

## ICML 2026 Key Deadlines

The submission site opened on January 8, 2026. The main submission deadlines are:

- **Abstract Submission Deadline**: January 24, 2026, 12 Noon UTC-0 (AoE)
- **Full Paper Submission Deadline**: January 29, 2026, 12 Noon UTC-0 (AoE)

## Paper Format Requirements

Papers must be prepared and submitted as a single file: 8 pages for the main paper, with unlimited pages for references, the impact statement, and appendices.

## Conference Details

The Forty-Third annual conference is held Mon. Jul 6th through Sat the 11th, 2026 at the Coex Convention & Exhibition Center. (This appears to be in Seoul, South Korea based on other sources.)

## LLM Policy and Interpretability

Regarding the use of LLMs in submissions: LLMs cannot be "credited"; prompt injection is strictly prohibited, and papers will be rejected if found to have done so. Additionally, the use of LLMs to assist in writing or research is allowed, but all responsibilities rest with the authors.

The search results returned general information about ICML 2026 deadlines and policies, but did not contain specific information about a dedicated track or call for papers on "LLM agent interpretability." You may want to check the full Call for Papers on the official ICML website for any special tracks or topics of interest.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cac239a-ae6c-4db8-b3e8-3c852766efc4",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "163570c0-a16c-49bd-9984-83e9612735bf",
  "toolUseResult": {
    "query": "ICML 2026 submission deadline call for papers LLM agent interpretability",
    "results": [
      {
        "tool_use_id": "srvtoolu_019pmp93MJ1CimwGW6g5fUfk",
        "content": [
          {
            "title": "ICML 2026 Call for Papers",
            "url": "https://icml.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "2026 Dates and Deadlines",
            "url": "https://icml.cc/Conferences/2026/Dates"
          },
          {
            "title": "ICML 2026 Author Instructions",
            "url": "https://icml.cc/Conferences/2026/AuthorInstructions"
          },
          {
            "title": "ICML 2026 Call For Position Papers",
            "url": "https://icml.cc/Conferences/2026/CallForPositionPapers"
          },
          {
            "title": "ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected",
            "url": "https://eu.36kr.com/en/p/3540848514510723"
          },
          {
            "title": "ICML 2026 Call for Post-Conference Workshops",
            "url": "https://icml.cc/Conferences/2026/CallForWorkshops"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "IEEE ICMLCN 2026 | IEEE International Conference on Machine Learning for Communication and Networking 2026 | IEEE ICMLCN 2026",
            "url": "https://icmlcn2026.ieee-icmlcn.org/"
          },
          {
            "title": "ICML 2026 Peer Review FAQ",
            "url": "https://icml.cc/Conferences/2026/PeerReviewFAQ"
          },
          {
            "title": "ICML 2026",
            "url": "https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"
          }
        ]
      },
      "Based on the search results, here's the information about ICML 2026 submission deadlines and call for papers:\n\n## ICML 2026 Key Deadlines\n\nThe submission site opened on January 8, 2026. The main submission deadlines are:\n\n- **Abstract Submission Deadline**: January 24, 2026, 12 Noon UTC-0 (AoE)\n- **Full Paper Submission Deadline**: January 29, 2026, 12 Noon UTC-0 (AoE)\n\n## Paper Format Requirements\n\nPapers must be prepared and submitted as a single file: 8 pages for the main paper, with unlimited pages for references, the impact statement, and appendices.\n\n## Conference Details\n\nThe Forty-Third annual conference is held Mon. Jul 6th through Sat the 11th, 2026 at the Coex Convention & Exhibition Center. (This appears to be in Seoul, South Korea based on other sources.)\n\n## LLM Policy and Interpretability\n\nRegarding the use of LLMs in submissions: LLMs cannot be \"credited\"; prompt injection is strictly prohibited, and papers will be rejected if found to have done so. Additionally, the use of LLMs to assist in writing or research is allowed, but all responsibilities rest with the authors.\n\nThe search results returned general information about ICML 2026 deadlines and policies, but did not contain specific information about a dedicated track or call for papers on \"LLM agent interpretability.\" You may want to check the full Call for Papers on the official ICML website for any special tracks or topics of interest."
    ],
    "durationSeconds": 8.428531409999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5cac239a-ae6c-4db8-b3e8-3c852766efc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:47:36.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0185eazS3wNgPDhMmyqz3jLe`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163570c0-a16c-49bd-9984-83e9612735bf",
  "isSidechain": false,
  "requestId": "req_011CbCRfZidxrZ3rmhjVYbri",
  "type": "assistant",
  "uuid": "35f802c7-9340-4bdd-a347-e9eee154de42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CntLWZF9NpXCXjeAdZz7kw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 34832,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 900,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 34832,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 900
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

### Tool result

_source line 26 · 2026-05-19T18:47:42.381Z_

<details><summary>↩ Tool result · `toolu_0185eazS3wNgPDhMmyqz3jLe`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

Based on the search results, here's the key information about EMNLP 2026:

## EMNLP 2026 Call for Papers

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

### Submission Deadline
The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

### Conference Details
The conference will be held in Budapest, Hungary on October 24 - 29, 2026.

### Submission Process
Papers must be submitted, at latest, by the ARR 2026 May cycle. Since the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

### Important Additional Dates
All authors must complete the author registration form by May 27, 2026. If you receive assignments, your reviews must be completed by July 6, or your meta-reviews by July 29.

For the full call for papers, visit https://2026.emnlp.org/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35f802c7-9340-4bdd-a347-e9eee154de42",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "312bd708-1fb5-4bbf-9d9c-1d2d19dc9982",
  "toolUseResult": {
    "query": "EMNLP 2026 submission deadline call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_013A1t8CbSBv2p9jgYKbPUsi",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot",
            "url": "https://www.getpaperpilot.com/deadlines/emnlp-2026.html"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          },
          {
            "title": "Call for workshops: EMNLP & AACL",
            "url": "https://groups.google.com/g/ml-news/c/W-fucfhVto4"
          },
          {
            "title": "EMNLP 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=EMNLP%2F2026%2FConference"
          },
          {
            "title": "Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"
          },
          {
            "title": "2026 *ACL Conference Dates | Computational Linguistics",
            "url": "https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"
          }
        ]
      },
      "Based on the search results, here's the key information about EMNLP 2026:\n\n## EMNLP 2026 Call for Papers\n\nEMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.\n\n### Submission Deadline\nThe EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12). All deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\n### Conference Details\nThe conference will be held in Budapest, Hungary on October 24 - 29, 2026.\n\n### Submission Process\nPapers must be submitted, at latest, by the ARR 2026 May cycle. Since the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.\n\n### Important Additional Dates\nAll authors must complete the author registration form by May 27, 2026. If you receive assignments, your reviews must be completed by July 6, or your meta-reviews by July 29.\n\nFor the full call for papers, visit https://2026.emnlp.org/"
    ],
    "durationSeconds": 6.0593808800000115,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35f802c7-9340-4bdd-a347-e9eee154de42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-19T18:48:30.245Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me summarize what I've found:

1. **CoRL 2026**: Confirmed - "Submissions without a robotics focus will be returned without review." Deadline May 29, 2026. Both agents' claims are fully verified.

2. **NeurIPS 2026**: Abstract deadline was May 4, full paper deadline was May 6 - **ALREADY PASSED** (today is May 19, 2026). So NeurIPS 2026 is NOT a viable retarget option.


3. **ICML 2026** and **EMNLP 2026** have already passed or are closing very soon—ICML was January 29 and EMNLP is May 25 with only 6 days left, making it technically possible but extremely tight if the proposal is ready.

4. **"Beyond the Black Box" (2605.06890)** uses SAE with linear probes on multi-step trajectories to classify tool-need and tool-risk across GPT-OSS 20B and Gemma 3 27B, though it doesn't appear to handle tool identity prediction.

5. The behavioral-mechanistic coupling angle has more precedent than initially thought—I'm finding papers like "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning," "Catching Rationalization in the Act," and "Project Ariadne" that combine mechanistic and behavioral methods, though none specifically target tool selection in agents.

For submission strategy, CoRL 2026 is a definite no—both agents agree and the CFP confirms it. The deadline landscape has shifted dramatically: NeurIPS and ICML have already closed, leaving EMNLP 2026 in six days as the only realistic near-term option, which is extremely tight. This fundamentally changes where the work can go.

On the novelty front, I'm finding that behavioral-mechanistic coupling isn't entirely unexplored—there's prior work on structural causal frameworks for agent auditing and mechanistic evidence for faithfulness decay. The specific angle of multi-turn tool selection might still be novel enough, but I need to be more careful about how I frame the contribution. Given the compressed timeline and the need to temper the novelty claims, waiting for ICLR 2027 or AAAI 2027 makes more sense than rushing EMNLP. The core issue isn't that the idea lacks merit—it's fundamentally misaligned with CoRL's scope, which both reviewers flagged independently. Since the venue mismatch is fatal and the natural alternative venues have either passed their deadlines or are too tight to execute properly, I should recommend stopping this submission track and instead map out a realistic timeline for retargeting to ICLR 2027 or NeurIPS 2027, where there's adequate time to strengthen the experimental design and address the identified gaps. I'm working through the decision logic for whether to trigger a stop-loss on this paper submission. The core issue is that there's a fundamental mismatch between the paper's content and CoRL's scope—this isn't really a recoverable venue problem, it's more that the underlying premise of submitting here doesn't hold. For probability estimation, CoRL 2026 would be 0% since the work falls outside the conference's domain entirely, but if we reframe this for a better-matched venue like NeurIPS or EMNLP, the idea has moderate-to-strong potential despite needing substantial experimental work. I should also verify the novelty claim about behavioral-mechanistic coupling by checking whether similar mechanistic auditing work already exists in the literature.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "312bd708-1fb5-4bbf-9d9c-1d2d19dc9982",
  "isSidechain": false,
  "requestId": "req_011CbCRgCjrdjyKA37KBXfhn",
  "type": "assistant",
  "uuid": "b3898e68-b994-4b24-bc2c-7e4153d3b6d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHzFMHySrMh8rMZ7UjjL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 35732,
      "output_tokens": 1830,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1830,
          "cache_read_input_tokens": 35732,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1129
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

### Tool call

_source line 28 · 2026-05-19T18:48:30.284Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ADvBDf3Rz4f9niZs7nMkM`</summary>

```json
{
  "query": "arxiv 2602.11201 \"Mechanistic Evidence for Faithfulness Decay\" chain-of-thought"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3898e68-b994-4b24-bc2c-7e4153d3b6d8",
  "isSidechain": false,
  "requestId": "req_011CbCRgCjrdjyKA37KBXfhn",
  "type": "assistant",
  "uuid": "4f81f4d4-d646-4065-bf35-65b9a9ce835e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHzFMHySrMh8rMZ7UjjL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 35732,
      "output_tokens": 1830,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1830,
          "cache_read_input_tokens": 35732,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1129
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: I now have sufficient information to provide my assessment. Let me compile my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "4f81f4d4-d646-4065-bf35-65b9a9ce835e",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Tool result

_source line 31 · 2026-05-19T18:48:38.626Z_

<details><summary>↩ Tool result · `toolu_018ADvBDf3Rz4f9niZs7nMkM`</summary>

```text
Web search results for query: "arxiv 2602.11201 "Mechanistic Evidence for Faithfulness Decay" chain-of-thought"

Links: [{"title":"[2602.11201] Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2602.11201"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"MECHANISTIC EVIDENCE FOR FAITHFULNESS DECAY","url":"https://openreview.net/pdf?id=wVj7dB7waI"},{"title":"SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models","url":"https://arxiv.org/html/2602.07833"},{"title":"Dissociation of Faithful and Unfaithful Reasoning in LLMs","url":"https://arxiv.org/html/2405.15092v2"}]

I found the paper! Here's what the search revealed about arxiv paper 2602.11201:

## Paper Overview

The paper "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" investigates whether chain-of-thought (CoT) explanations reflect how language models actually reach their answers, or merely post-hoc justifications.

## Key Contribution

The authors propose Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process by corrupting individual reasoning steps and measuring how much the model's confidence in its answer drops. NLDD operates in logit space and normalizes for cross-model comparison, addressing differences in output scaling across architectures to provide an architecture-agnostic measure of causal reliance.

## Main Finding

Testing three model families across syntactic, logical, and arithmetic tasks, the researchers discovered a consistent Reasoning Horizon (k*) at 70--85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.

The paper was published on February 4, 2026, and has already influenced subsequent research on the faithfulness of chain-of-thought reasoning in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f81f4d4-d646-4065-bf35-65b9a9ce835e",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "1455517e-91df-48a6-8d2d-3b8a7d2e9c21",
  "toolUseResult": {
    "query": "arxiv 2602.11201 \"Mechanistic Evidence for Faithfulness Decay\" chain-of-thought",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FZvM7B2Zu9AaC2zfM53Ftp",
        "content": [
          {
            "title": "[2602.11201] Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2602.11201"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2602.11201"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "MECHANISTIC EVIDENCE FOR FAITHFULNESS DECAY",
            "url": "https://openreview.net/pdf?id=wVj7dB7waI"
          },
          {
            "title": "SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2602.07833"
          },
          {
            "title": "Dissociation of Faithful and Unfaithful Reasoning in LLMs",
            "url": "https://arxiv.org/html/2405.15092v2"
          }
        ]
      },
      "I found the paper! Here's what the search revealed about arxiv paper 2602.11201:\n\n## Paper Overview\n\nThe paper \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" investigates whether chain-of-thought (CoT) explanations reflect how language models actually reach their answers, or merely post-hoc justifications.\n\n## Key Contribution\n\nThe authors propose Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process by corrupting individual reasoning steps and measuring how much the model's confidence in its answer drops. NLDD operates in logit space and normalizes for cross-model comparison, addressing differences in output scaling across architectures to provide an architecture-agnostic measure of causal reliance.\n\n## Main Finding\n\nTesting three model families across syntactic, logical, and arithmetic tasks, the researchers discovered a consistent Reasoning Horizon (k*) at 70--85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.\n\nThe paper was published on February 4, 2026, and has already influenced subsequent research on the faithfulness of chain-of-thought reasoning in language models."
    ],
    "durationSeconds": 8.33748799600001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f81f4d4-d646-4065-bf35-65b9a9ce835e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-19T18:48:38.630Z_

```json
{
  "parentUuid": "1455517e-91df-48a6-8d2d-3b8a7d2e9c21",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "224a96a0-db9e-4240-a6bb-716e9e413629",
  "timestamp": "2026-05-19T18:48:38.630Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-19T18:48:41.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CmK6e8REpv6L6jybTGjeEW`</summary>

```json
{
  "query": "arxiv 2601.02314 \"Project Ariadne\" causal framework faithfulness LLM agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "224a96a0-db9e-4240-a6bb-716e9e413629",
  "isSidechain": false,
  "requestId": "req_011CbCRkMDT2NSQ9p3DzKFch",
  "type": "assistant",
  "uuid": "c612628b-4997-452e-ab01-fe29f6bd5dc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PF4BwEfFrLjsKqi3JLHs65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2599,
      "cache_read_input_tokens": 36861,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 36861,
          "cache_creation_input_tokens": 2599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2599
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

### Tool result

_source line 34 · 2026-05-19T18:48:47.925Z_

<details><summary>↩ Tool result · `toolu_01CmK6e8REpv6L6jybTGjeEW`</summary>

```text
Web search results for query: "arxiv 2601.02314 "Project Ariadne" causal framework faithfulness LLM agents"

Links: [{"title":"[2601.02314] Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/abs/2601.02314"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing","url":"https://arxiv.org/pdf/2601.02314"},{"title":"GitHub - skhanzad/AriadneXAI: Project Ariadne is an Explainable AI (XAI) research tool designed to evaluate the Causal Faithfulness of LLM agents. While agents produce persuasive Chain-of-Thought (CoT) reasoning, these traces frequently act as post-hoc rationalizations rather than generative drivers of the model's output.","url":"https://github.com/skhanzad/AriadneXAI"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/html/2601.02314v1"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/640709c1-2e86-4fb7-82fe-e00b3bbcaee1"},{"title":"Paper page - Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://huggingface.co/papers/2601.02314"},{"title":"Large Language Model Agents Are Not Always Faithful Self-Evolvers","url":"https://arxiv.org/html/2601.22436"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/pdf/2604.08401"},{"title":"Towards CausalGPT: A Multi-Agent Approach for Faithful Knowledge   Reasoning via Promoting Causal Consistency in LLMs","url":"https://arxiv.org/pdf/2308.11914"},{"title":"Enhancing LLM Agent Safety via Causal Influence Prompting","url":"https://arxiv.org/pdf/2507.00979"}]

I found the paper! Here's what I found about arxiv 2601.02314:

## Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents

Project Ariadne is a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning.

**The Problem It Addresses:**

While Chain-of-Thought (CoT) prompting allows agents to generate human-readable reasoning traces, it remains unclear whether these traces are faithful generative drivers of the model's output or merely post-hoc rationalizations.

**How It Works:**

Project Ariadne performs hard interventions (do-calculus) on intermediate reasoning nodes -- systematically inverting logic, negating premises, and reversing factual claims -- to measure the Causal Sensitivity (φ) of the terminal answer. By quantifying the Causal Sensitivity of the output to these perturbations, Ariadne provides a formal mathematical basis for distinguishing between truly "thinking" agents and those merely performing "reasoning theater."

**Author:**

The paper was submitted on January 5, 2026, authored by Sourena Khanzadeh.

There's also a GitHub repository available for the tool at https://github.com/skhanzad/AriadneXAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c612628b-4997-452e-ab01-fe29f6bd5dc2",
  "isSidechain": false,
  "promptId": "d0334993-3017-4c82-9047-ed4b131847db",
  "type": "user",
  "uuid": "60c0c634-9820-42f8-884f-f886726688aa",
  "toolUseResult": {
    "query": "arxiv 2601.02314 \"Project Ariadne\" causal framework faithfulness LLM agents",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AjWvrh2UUpc48jTFLbpJdJ",
        "content": [
          {
            "title": "[2601.02314] Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/abs/2601.02314"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "GitHub - skhanzad/AriadneXAI: Project Ariadne is an Explainable AI (XAI) research tool designed to evaluate the Causal Faithfulness of LLM agents. While agents produce persuasive Chain-of-Thought (CoT) reasoning, these traces frequently act as post-hoc rationalizations rather than generative drivers of the model's output.",
            "url": "https://github.com/skhanzad/AriadneXAI"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/html/2601.02314v1"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents - Paper Details",
            "url": "https://www.chatpaper.ai/dashboard/paper/640709c1-2e86-4fb7-82fe-e00b3bbcaee1"
          },
          {
            "title": "Paper page - Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://huggingface.co/papers/2601.02314"
          },
          {
            "title": "Large Language Model Agents Are Not Always Faithful Self-Evolvers",
            "url": "https://arxiv.org/html/2601.22436"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/pdf/2604.08401"
          },
          {
            "title": "Towards CausalGPT: A Multi-Agent Approach for Faithful Knowledge   Reasoning via Promoting Causal Consistency in LLMs",
            "url": "https://arxiv.org/pdf/2308.11914"
          },
          {
            "title": "Enhancing LLM Agent Safety via Causal Influence Prompting",
            "url": "https://arxiv.org/pdf/2507.00979"
          }
        ]
      },
      "I found the paper! Here's what I found about arxiv 2601.02314:\n\n## Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents\n\nProject Ariadne is a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning.\n\n**The Problem It Addresses:**\n\nWhile Chain-of-Thought (CoT) prompting allows agents to generate human-readable reasoning traces, it remains unclear whether these traces are faithful generative drivers of the model's output or merely post-hoc rationalizations.\n\n**How It Works:**\n\nProject Ariadne performs hard interventions (do-calculus) on intermediate reasoning nodes -- systematically inverting logic, negating premises, and reversing factual claims -- to measure the Causal Sensitivity (φ) of the terminal answer. By quantifying the Causal Sensitivity of the output to these perturbations, Ariadne provides a formal mathematical basis for distinguishing between truly \"thinking\" agents and those merely performing \"reasoning theater.\"\n\n**Author:**\n\nThe paper was submitted on January 5, 2026, authored by Sourena Khanzadeh.\n\nThere's also a GitHub repository available for the tool at https://github.com/skhanzad/AriadneXAI."
    ],
    "durationSeconds": 6.869431941000017,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c612628b-4997-452e-ab01-fe29f6bd5dc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T18:49:13.749Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important. Project Ariadne (2601.02314) is doing something very close to what the proposal is doing:
- Structural Causal Models for auditing faithfulness in LLM agents
- Hard interventions (do-calculus) on intermediate reasoning nodes
- Measures "Causal Sensitivity" which is conceptually very similar to TSCF
- Uses the term "reasoning theater" which is literally the same concept as RTI (Reasoning Theater Index)

This is a significant threat to the proposal's novelty that neither agent caught. The proposal's RTI metric even shares the exact same terminology ("reasoning theater"). Let me check if the proposal already cites this work...


The proposal doesn't appear to reference Project Ariadne at all, which is a major gap. I'm also noticing that "Mechanistic Evidence for Faithfulness Decay" (2602.11201) introduces NLDD—a method that corrupts individual reasoning steps and measures confidence drops, which mirrors the proposal's behavioral intervention approach. Most troublingly, the behavioral-mechanistic coupling that was presented as novel ground actually appears in both Ariadne's structural causal interventions and in the mechanistic-behavioral pairing from 2602.11201, so the novelty claims need substantial revision.

Now I'm working through the key findings: CoRL 2026 is definitively off the table, and I'm evaluating alternatives like NeurIPS 2026 (May 6 deadline passed), ICML 2026 (Jan 29 passed), and EMNLP 2026 (May 25, only 6 days away—extremely tight). The cross-validation confirms the CoRL scope would trigger a desk reject, the "Beyond the Black Box" threat is partially mitigated since it only covers tool-need and tool-risk rather than tool identity or faithfulness, and the behavioral-mechanistic coupling novelty claim is significantly undermined by Project Ariadne's causal interventions on agent reasoning with its Causal Sensitivity metric. I'm identifying the key gaps in related work—Project Ariadne and "Beyond the Black Box" aren't adequately cited—and assessing this against potential venues. For CoRL 2026, the paper falls completely outside scope, so acceptance probability is essentially zero. Even for a hypothetical better-matched venue, the evaluation shows mixed results: the behavioral-mechanistic coupling angle has some novelty, but the experimental design has notable weaknesses, putting realistic acceptance odds around 25-35%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60c0c634-9820-42f8-884f-f886726688aa",
  "isSidechain": false,
  "requestId": "req_011CbCRm2wdsWL3112umKPfC",
  "type": "assistant",
  "uuid": "4a2ff09f-d624-464f-981e-cfaa80a74fcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFGFbLSsb5pLLqZuQXHDfQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 39460,
      "output_tokens": 6659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6659,
          "cache_read_input_tokens": 39460,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 36 · 2026-05-19T18:51:09.539Z_

Now I have all the cross-validation data I need. Let me compile my findings and produce the integrated assessment.

【阶段】: 迭代第 1 轮

【交叉验证调研】:

1. **CoRL 2026 scope 验证** → ✅ 完全证实。官方 CFP 原文："Submissions without a robotics focus will be returned without review." 并鼓励 real-robot experiments 或 sim-to-real evidence。两位 agent 的判断完全正确。

2. **NeurIPS 2026 作为替代投稿目标** → ❌ **不可行**。Abstract deadline 为 2026-05-04，full paper deadline 为 2026-05-06，均已过（今天 2026-05-19）。发掘 agent 推荐 NeurIPS 2026 作为首选替代，但该建议已过时效。

3. **ICML 2026 作为替代** → ❌ 不可行。Deadline 2026-01-29，早已过。

4. **EMNLP 2026 作为替代** → ⚠️ 技术上可行但极度紧张。ARR May cycle deadline 为 2026-05-25（距今仅 6 天）。需要在 6 天内完成全部实验设计修订并提交，几乎不现实。

5. **"Beyond the Black Box" (2605.06890) 威胁评估** → ✅ 已验证。该工作在 multi-step trajectories 上使用 SAE + linear probes 做 tool-need/tool-risk classification（GPT-OSS 20B, Gemma 3 27B），但确实未触及 tool identity probing 或 faithfulness measurement。发掘 agent 对其威胁性的评估准确。

6. **Behavioral-mechanistic coupling 的 novelty 声明** → ⚠️ **发掘 agent 过度乐观，发现重要未引用竞争工作**：
   - **Project Ariadne (arXiv:2601.02314)**：一个 structural causal framework，对 LLM agent 推理链做 hard interventions（do-calculus），测量 "Causal Sensitivity (φ)"，并明确使用了 **"reasoning theater"** 这一术语——与本 proposal 的 RTI (Reasoning Theater Index) 完全同名。这是一个严重的 novelty 威胁和引用遗漏。
   - **"Mechanistic Evidence for Faithfulness Decay" (arXiv:2602.11201)**：提出 NLDD metric，通过 corrupting individual reasoning steps 并测量 confidence decay 来判断 faithfulness，结合了 mechanistic probing（per-layer 分析）和 behavioral intervention，发现了 "Reasoning Horizon" 现象。这直接挑战了"无人做过 behavioral-mechanistic coupling"的说法。
   - **结论**：behavioral-mechanistic coupling 并非完全无人触及，但上述工作均在 QA/reasoning 场景，未扩展到 multi-turn tool selection。差异化空间存在但比发掘 agent 描述的更窄。

7. **可行的投稿目标调查** → ICLR 2027、NeurIPS 2027、AAAI 2027 的 CFP 均尚未发布。最近的现实选项是 EMNLP 2026（6 天后 deadline，不现实）或等待下一轮会议周期。

---

【发掘 agent 有效建议采纳】:

| 建议 | 验证结果 | 采纳状态 |
|------|----------|----------|
| 致命问题：CoRL venue mismatch | ✅ 已验证，CFP 原文确认 | **采纳** — 致命，触发止损 |
| 发掘点1：argue tool selection 的结构性差异（structured output, temporal dependency, context accumulation）区别于 QA faithfulness | ✅ 合理，RFEval 确实仅覆盖单轮 QA/math | **采纳（若继续）** — 已验证 |
| 发掘点2：将 "deliberation threshold" 假设提升为 central narrative（System 1/2 framing） | ⚠️ 部分验证 — "Brief Is Better" (2604.02155) 和 "Decoding Answers Before CoT" (2603.01437) 提供了一定支撑，但 System 1/2 metaphor 在 ML 审稿中常被视为 hand-wavy | **有条件采纳** — 保留 counterintuitive hypothesis 但弱化 System 1/2 类比 |
| 发掘点3：重新定位 "Beyond the Black Box" 并聚焦 behavioral-mechanistic coupling | ⚠️ 部分验证 — 2605.06890 确实是威胁，但 coupling 的 novelty 被 Project Ariadne (2601.02314) 和 NLDD (2602.11201) 部分侵蚀 | **有条件采纳** — coupling 仍是差异点但需承认先行工作 |
| 发掘点4：引入 agent monitoring paradigm challenge 的 significance angle | ✅ SAVeR (2604.08401) 确实假设 CoT faithfulness，该 angle 有依据 | **采纳（若继续）** — 已验证 |
| 发掘点5：将 behavioral-mechanistic coupling 作为核心独特贡献 | ❌ **需降权** — 我搜到 Project Ariadne 已在做 causal interventions on agent reasoning，且 NLDD 已做 mechanistic+behavioral coupling。"无人做过两者的 systematic coupling"这一说法不准确 | **降权采纳** — coupling 可保留但不能 claim "first"，需引用 Ariadne 和 NLDD |

---

【补救 agent 有效建议采纳】:

| 建议 | 验证结果 | 采纳状态 |
|------|----------|----------|
| 缺陷1：CoRL venue mismatch（不可补救） | ✅ 已验证 | **采纳** — 致命 |
| 缺陷2：明确 point-wise vs cascading intervention regime | ✅ 合理，RFEval 和 FACT-E 的 intervention 设计均为单轮，multi-turn 确实需要此区分 | **采纳（若继续）** — 已验证 |
| 缺陷3：TSCF/RTI 冗余性 + 三元 outcome（Follow/Ignore/Diverge） | ⚠️ 部分验证 — 且 Project Ariadne 已用 "Causal Sensitivity" 做类似度量，RTI 命名与 Ariadne 的 "reasoning theater" 术语冲突 | **采纳但需重构** — RTI 命名可能需要修改以避免与 Ariadne 混淆 |
| 缺陷4：ablation 设计（6项） | ✅ 合理，参照 2605.07990 和 2605.09252 的 ablation 标准 | **采纳（若继续）** — 已验证 |
| 缺陷5：benchmark ground truth + annotator agreement | ✅ 合理，参照 RFEval 和 FaithCoT-Bench 标准 | **采纳（若继续）** — 已验证 |
| 缺陷6：probing methodology 细节 | ✅ 合理，参照 2605.07990 使用 logistic regression probe | **采纳（若继续）** — 已验证 |
| 缺陷7：统计分析方法 | ✅ 基本实验规范 | **采纳（若继续）** — 已验证 |
| 缺陷8：增加 method comparison experiment | ✅ 合理，C2-Faith 和 "Catching Rationalization" 是有效的对比方法 | **采纳（若继续）** — 已验证 |
| 缺陷9：compute 预算重估 | ⚠️ 合理但细节需核实 — API pricing 估算合理 | **采纳（若继续）** — 部分验证 |

---

【本轮 proposal 主要变更】: **无变更——本轮决策为止损。**

---

【idea 质量评估】:
- 对 CoRL 2026：**不适用（完全 out of scope）**
- 若投至匹配会议（参考性评估）：Novelty=中（behavioral-mechanistic coupling 有差异化但被 Ariadne/NLDD 压缩）、Significance=中-强（agent monitoring paradigm challenge 是好 angle）→ idea 天花板约 40-45%

【实验完备性评估】:
- Technical Soundness=弱（intervention protocol 未规范、metrics 近冗余、无 ablation、无统计检验、benchmark QC 不足）→ 地板未补好

【当前概率估计】: [0% - 0%] 中位 0%
（CoRL 2026 desk reject 概率接近 100%。论文内容与会议 scope 零重叠。）

---

【决策】: 止损

【决策理由】:

两个 agent 独立且一致地发现了同一致命缺陷：**本 proposal 投稿 CoRL 2026（机器人学习会议）但内容完全不涉及机器人学**。CoRL 2026 官方 CFP 明确声明 "Submissions without a robotics focus will be returned without review"。五个研究领域（code editing, web browsing, data analysis, system administration, information retrieval）无一与 robotics 相关。这不是 borderline case，而是必然 desk reject。

止损触发条件满足：
1. ✅ 发掘 agent 标注致命问题（核心 claim 前提——投稿目标——不成立）
2. ✅ 补救 agent 明确标注"不可补救（方向性致命）"
3. ✅ 补救路径不可行——将 proposal 改造为 robotics 内容等于重写新论文

**交叉验证进一步发现的问题**：
- NeurIPS 2026（两位 agent 的首选替代）deadline 已于 2026-05-06 过期，不可行
- ICML 2026 deadline 已于 2026-01-29 过期
- EMNLP 2026 deadline 2026-05-25（6 天后），时间极度紧张且需 ARR review cycle
- Project Ariadne (arXiv:2601.02314) 使用了完全相同的 "reasoning theater" 术语和类似的 causal intervention 方法论，是重要的未引用竞争工作，进一步压缩 novelty 空间

---

## 最终输出（角色 C：止损后）

【拒绝阶段】: 循环第 1 轮（止损）

【击穿维度 / 致命缺陷】:

1. **投稿目标与内容完全不匹配（致命，不可补救）**：CoRL 2026 要求 robotics focus，本 proposal 研究 LLM agent 在非 robotics 领域的 tool-selection faithfulness。将被 desk reject 而不进入审稿流程。

2. **重要竞争工作未被引用（严重，可补救但进一步压缩 novelty）**：
   - Project Ariadne (arXiv:2601.02314) 已建立 structural causal framework 用于审计 LLM agent 的 faithfulness，使用 do-calculus interventions 和 "Causal Sensitivity" 指标，且使用了 "reasoning theater" 这一与本 proposal RTI 指标完全同名的术语
   - "Mechanistic Evidence for Faithfulness Decay" (arXiv:2602.11201) 已结合 mechanistic probing 和 behavioral intervention 研究 CoT faithfulness decay

3. **实验设计多处不足（严重但可补救）**：multi-turn intervention protocol 未规范（point-wise vs cascading 未区分）、TSCF/RTI 指标近冗余、无 ablation design、无统计分析方法、benchmark ground truth QC 不足、probing methodology 细节缺失、缺少方法对比 baseline

【已尝试优化方向】: 未进入实质优化轮次，首轮即止损。两位 agent 均提出了可行的优化方向（见下文），但因 venue 致命错误无法继续。

【可否抢救】:

**Idea 本身可抢救，但需更换投稿目标且时间窗口受限。** 具体建议：

**方案 A（最推荐）：投 ICLR 2027 或 NeurIPS 2027**
- Deadline 预计 2026 年 9-10 月（ICLR 2027）或 2027 年 5 月（NeurIPS 2027）
- 时间充裕，可完整实施两位 agent 提出的所有优化建议
- Idea 经打磨后估计匹配会议概率：[28% - 40%] 中位 33%（Novelty 中、Significance 中-强，但需解决 Ariadne 竞争和实验完备性问题）

**方案 B（可考虑但风险高）：投 EMNLP 2026**
- Deadline 2026-05-25（仅余 6 天），需走 ARR May cycle
- 时间几乎不可能完成补救 agent 提出的实验设计改进
- 如果是以当前状态投稿，概率极低（实验 soundness 不足）

**方案 C（不推荐）：改造为 robotics 方向投 CoRL 2026**
- Deadline 2026-05-29（10 天后）
- 等于重写一篇全新论文（benchmark、domain、实验全部重建），不现实

**若选择方案 A 并充分打磨，需重点完成以下工作**：

1. **[Related Work / 引用补全]** — 必须引用并充分讨论 Project Ariadne (arXiv:2601.02314) 和 "Mechanistic Evidence for Faithfulness Decay" (arXiv:2602.11201)，明确阐述本工作与它们的差异（multi-turn tool selection specific, 三 tier ambiguity stratification, behavioral-mechanistic convergent validity analysis vs Ariadne 的 single-turn causal sensitivity）→ 命中 Related Work completeness

2. **[核心 Novelty Claim / Framing 重构]** — 不能 claim "first behavioral-mechanistic coupling"（Ariadne 和 NLDD 已部分覆盖）。应将 novelty 锐化为：(a) 首个系统研究 multi-turn tool selection faithfulness 的工作（single-turn 已有成熟框架，multi-turn 是公认 gap）；(b) 首个在 tool selection 领域建立 ambiguity-stratified faithfulness taxonomy（Tier 1/2/3）并测试 "harder tasks → more faithful" 的 counterintuitive hypothesis → 命中 Novelty

3. **[Significance Reframing]** — 增加 "challenge to agent monitoring paradigm" 角度：SAVeR (arXiv:2604.08401) 等 CoT-based monitoring 隐含假设 faithfulness，本工作直接测试这一假设在 tool selection 中是否成立 → 命中 Significance

4. **[Intervention Protocol 规范化]** — 明确定义 point-wise intervention（局部 faithfulness）和 cascading intervention（下游 propagation），分别报告结果 → 命中 Technical Soundness

5. **[Metrics 重构]** — 将 outcome 细化为三元 Follow/Ignore/Diverge，解决 TSCF-RTI 冗余问题；考虑 rename RTI 以避免与 Ariadne "reasoning theater" 术语冲突 → 命中 Technical Soundness

6. **[Ablation Design]** — 补充 conversation depth ablation、intervention position ablation、tool menu size ablation、perturbation strength ablation、probing layer selection、tier boundary sensitivity → 命中 Technical Soundness

7. **[Benchmark QC]** — 设计 annotator agreement pilot (Fleiss' κ > 0.7)、tier boundary 操作化标准、held-out validation set → 命中 Technical Soundness

8. **[统计分析]** — Bootstrap CI、paired permutation test、Friedman + Nemenyi post-hoc、power analysis → 命中 Technical Soundness

9. **[Method Comparison]** — 在子集上同时运行本文 behavioral intervention、pre-call probing (à la 2605.07990)、LLM-as-judge (à la C2-Faith) 三种方法，比较一致性 → 命中 Technical Soundness

**【主要风险（若投至匹配会议）】**:
1. Reviewer 认为核心贡献是 "RFEval domain transfer + 2605.07990 multi-turn extension" 的组合而非新方法论 — 需用结构性差异论证（structured output、temporal dependency、context accumulation）和 Ariadne 差异化来反驳
2. 实验覆盖面过宽（5 domains × 3 tiers × 4 interventions × 7 models × mechanistic probing）导致每个分析不够深入 — 可能需要缩减 scope 以聚焦核心 claim

**【实施评估（若投至匹配会议）】**:
- **计算资源**: 4 open-weight models（含可能的 671B MoE DeepSeek-V4-Pro，需 INT4/FP8 量化）multi-turn 推理 + activation 存储；预估 400-600 H100-hours（原估 300 偏乐观）。3 API models 推理成本预估 $500-800（原估 $350-450 偏低，multi-turn 20K+ tokens/scenario × 7200 条件 ≈ 50M+ tokens）
- **数据需求**: 600 scenario benchmark（200/tier × 5 domains）需自建，依赖 Claude 辅助生成 + 人工验证；无现成公开数据集可直接复用
- **人工介入**: 3+ annotators 做 tier classification pilot study（Fleiss' κ validation）+ benchmark 质量审核；估计 80-120 人时
- **训练需求**: 无模型训练（probe 为 logistic regression，训练成本可忽略）；主要成本在推理和 activation 提取
- **新 Benchmark**: 需构建 TOOLFAITH-BENCH（600 multi-turn scenarios），是本工作的核心 artifact
- **预估周期**: 从启动到可投稿约 3-4 个月（benchmark 构建 4-6 周、实验运行 3-4 周、probing 分析 2-3 周、写作 3-4 周），适合 ICLR 2027 或 NeurIPS 2027 的时间线

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [ICML 2026 Dates and Deadlines](https://icml.cc/Conferences/2026/Dates)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents](https://arxiv.org/abs/2601.02314)
- [Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning](https://arxiv.org/abs/2602.11201)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a2ff09f-d624-464f-981e-cfaa80a74fcc",
  "isSidechain": false,
  "requestId": "req_011CbCRm2wdsWL3112umKPfC",
  "type": "assistant",
  "uuid": "b0238698-4da9-4de4-9522-08b70f0dcb83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFGFbLSsb5pLLqZuQXHDfQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 39460,
      "output_tokens": 6659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6659,
          "cache_read_input_tokens": 39460,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: I now have sufficient information to provide my assessment. Let me compile my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "b0238698-4da9-4de4-9522-08b70f0dcb83",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: I now have sufficient information to provide my assessment. Let me compile my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "b0238698-4da9-4de4-9522-08b70f0dcb83",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 42 · 2026-05-19T18:51:11.073Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:51:11.073Z",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "content": "【任务】: 流程已结束（循环第 1 轮止损：补救 agent 标注致命缺陷（不可补救）），请按「角色 C：最终输出」的拒绝格式，输出拒绝详情文本。"
}
```

---

### Runtime record

_source line 43 · 2026-05-19T18:51:11.074Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:51:11.074Z",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

## Round 2

5 recorded events

### User

_source line 44 · 2026-05-19T18:51:11.097Z_

【任务】: 流程已结束（循环第 1 轮止损：补救 agent 标注致命缺陷（不可补救）），请按「角色 C：最终输出」的拒绝格式，输出拒绝详情文本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0238698-4da9-4de4-9522-08b70f0dcb83",
  "isSidechain": false,
  "promptId": "85d6643a-4198-4990-a0df-d75d240d4720",
  "type": "user",
  "uuid": "5bb2adb1-0f04-4f25-a843-b81493e3d69e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-19T18:51:16.795Z_

<details><summary>Logged reasoning block</summary>

```text
The system is asking me to produce the final output in Role C format (rejection). The decision was stop-loss at Round 1 due to the 补救 agent flagging a fatal, non-recoverable defect (CoRL venue mismatch). I already produced most of this analysis in my Round 1 output, so I need to consolidate it into the clean Role C rejection format.

Let me produce the final rejection output following the specified format exactly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb2adb1-0f04-4f25-a843-b81493e3d69e",
  "isSidechain": false,
  "requestId": "req_011CbCRwb9f14P1ujcbaz7ag",
  "type": "assistant",
  "uuid": "2213ea07-5d51-424b-a2d5-e2d94b261c1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDoYtrrbUb5amob4vgovQc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6733,
      "cache_read_input_tokens": 40479,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2100,
          "cache_read_input_tokens": 40479,
          "cache_creation_input_tokens": 6733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6733
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

_source line 46 · 2026-05-19T18:51:48.825Z_

【拒绝阶段】: 循环第 1 轮（止损）

【击穿维度 / 致命缺陷】:

**1. 投稿目标与论文内容完全不匹配（致命，不可补救）**

CoRL 2026 官方 CFP 明确声明："Submissions without a robotics focus will be returned without review." 本 proposal 研究 LLM agent 在 code editing、web browsing、data analysis、system administration、information retrieval 五个领域中的 tool-selection faithfulness——零涉及 robotics。这不是 borderline case，而是 100% desk reject。发掘 agent 与补救 agent 独立且一致地将此标注为致命缺陷，经交叉验证（CoRL 2026 CFP 原文）完全证实。

**2. 重要竞争工作未引用，压缩 novelty 空间（严重）**

交叉验证调研中发现两篇 proposal 未引用的高相关工作：
- **Project Ariadne (arXiv:2601.02314)**：已建立 structural causal framework 对 LLM agent reasoning 做 hard interventions（do-calculus），测量 Causal Sensitivity (φ)，且明确使用了 **"reasoning theater"** 术语——与本 proposal 的 RTI (Reasoning Theater Index) 完全同名。方法论（对推理链做 counterfactual intervention 测量行为变化）与本 proposal 的 behavioral intervention protocol 高度重叠。
- **"Mechanistic Evidence for Faithfulness Decay" (arXiv:2602.11201)**：提出 NLDD metric，通过 corrupting individual reasoning steps 并测量 confidence decay，已结合 mechanistic per-layer 分析与 behavioral intervention，发现 "Reasoning Horizon" 现象。这直接挑战发掘 agent 提出的 "无人做过 behavioral-mechanistic coupling" 的 novelty claim。

**3. 实验设计系统性不足（严重但可补救）**

补救 agent 识别出 8 项实验层面缺陷（均经交叉验证确认合理）：multi-turn intervention protocol 未区分 point-wise vs cascading regime；TSCF/RTI 指标近冗余（且 RTI 命名与 Ariadne 冲突）；无 ablation design；benchmark ground truth 无 annotator agreement 验证；probing methodology 细节缺失；无统计分析方法；无方法对比 baseline；compute 预算偏乐观。

【已尝试优化方向】: 未进入实质优化轮次，首轮即因 venue 致命错误止损。两位 agent 均提出了具体可行的优化方向（见下文抢救建议），但在 CoRL 2026 框架内无法实施。

【可否抢救】:

**Idea 本身可抢救，但必须更换投稿目标，且当前时间窗口严重受限。**

核心判断：proposal 的研究问题（multi-turn tool-selection faithfulness）是一个被领域明确标识但尚未系统研究的 gap（2605.07990 明确标注 multi-turn 迁移 "fragile"；RFEval 仅覆盖单轮 QA），idea 有真实价值。致命缺陷仅在于 venue 选择错误，而非 idea 本身不成立。

**方案 A（推荐）：投 ICLR 2027（预计 2026 年 9-10 月 deadline）**

时间充裕（约 4-5 个月），可完整实施以下打磨路线：

1. **引用补全 + Related Work 重构**：引用 Project Ariadne (2601.02314)、NLDD (2602.11201)、"Beyond the Black Box" (2605.06890)，明确差异化为 multi-turn tool selection specific + ambiguity-stratified taxonomy + convergent validity（非 "first coupling"）
2. **Novelty 锐化**：核心贡献重新定位为 (a) 首个 multi-turn tool selection faithfulness 的系统性研究 (b) ambiguity-stratified faithfulness taxonomy (Tier 1/2/3) (c) "harder tasks → more faithful" counterintuitive hypothesis 的验证
3. **Significance 重构**：增加 "challenge to CoT-based agent monitoring paradigm" 角度（SAVeR 等隐含假设 faithfulness）
4. **Intervention protocol 规范化**：point-wise vs cascading 两种 regime 分别报告
5. **Metrics 重构**：三元 Follow/Ignore/Diverge outcome；rename RTI 避免与 Ariadne 术语冲突
6. **补全 ablation**（conversation depth / intervention position / tool menu size / perturbation strength / probing layer / tier boundary sensitivity）
7. **Benchmark QC**：annotator agreement pilot (Fleiss' κ > 0.7) + 操作化 tier 标准
8. **统计分析**：bootstrap CI + permutation test + Friedman post-hoc + power analysis
9. **Method comparison**：behavioral intervention vs pre-call probing vs LLM-as-judge 三方法对比

打磨后匹配会议估计概率：[28% - 40%] 中位 33%。主要制约因素：Novelty 被 Ariadne/NLDD 压缩至"中"水平，即使实验做到完美也难以突破 idea 天花板。若 counterintuitive hypothesis (Tier 3 > Tier 1 faithfulness) 被实验强力验证且 behavioral-mechanistic convergent validity 显示有意义的 pattern，概率可推至区间上端。

实施需求估算：
- 计算资源：400-600 H100-hours（4 open-weight models 含量化 DeepSeek-V4-Pro）+ $500-800 API 成本（3 frontier models，~50M+ tokens）
- 数据需求：自建 TOOLFAITH-BENCH 600 scenarios（无现成公开数据集）
- 人工介入：3+ annotators × 80-120 人时（tier classification pilot + benchmark QC）
- 训练需求：无模型训练（logistic regression probes 训练成本可忽略）
- 新 Benchmark：需构建，是核心 artifact
- 预估周期：3-4 个月（benchmark 4-6 周 → 实验 3-4 周 → 分析 2-3 周 → 写作 3-4 周）

**方案 B（不推荐）：投 EMNLP 2026（deadline 2026-05-25，仅余 6 天）**

时间不足以完成任何实质性实验设计改进。以当前 proposal 状态投稿，实验 soundness 不足以通过审稿。

**方案 C（不推荐）：改造为 robotics 方向投 CoRL 2026（deadline 2026-05-29）**

等于重写一篇全新论文（benchmark、domain、实验全部重建），10 天内不可能完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2213ea07-5d51-424b-a2d5-e2d94b261c1a",
  "isSidechain": false,
  "requestId": "req_011CbCRwb9f14P1ujcbaz7ag",
  "type": "assistant",
  "uuid": "26f878d9-3718-477b-ac7b-d601e2638ff0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDoYtrrbUb5amob4vgovQc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6733,
      "cache_read_input_tokens": 40479,
      "output_tokens": 2100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2100,
          "cache_read_input_tokens": 40479,
          "cache_creation_input_tokens": 6733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6733
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已结束（循环第 1 轮止损：补救 agent 标注致命缺陷（不可补救）），请按「角色 C：最终输出」的拒绝格式，输出拒绝详情文本。",
  "leafUuid": "26f878d9-3718-477b-ac7b-d601e2638ff0",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze LLM tool-selection faithfulness research proposal",
  "sessionId": "3f1bd7df-6f1a-4c86-930b-b729b792593a"
}
```

---
