# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/cb7b2648-9853-474e-acd6-3797d6e8bcf4.jsonl`
- **Structured JSON:** [`bd4dbf87d957610059a9.json`](../../sessions/bd/bd4dbf87d957610059a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:27:19.160Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:27:19.160Z",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n```\n\n---\n\n## ⚠️ 致命前置问题：投稿 CoRL 2026 venue 完全不匹配\n\n在进入 idea 质量评估之前，必须先指出一个**致命的 venue mismatch 问题**：\n\nCoRL (Conference on Robot Learning) 2026 的 [Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确限定投稿范围为 \"significant original research at the intersection of robotics and machine learning\"，涵盖的主题包括 robot perception, manipulation, locomotion, sim-to-real transfer, reinforcement learning for physical robots 等。官网明确写道：**\"Submissions without a robotics focus will be returned without review.\"**\n\n本 proposal 是一篇纯粹的 **LLM mechanistic interpretability** 论文，研究 LLM 自我纠错的盲区与谄媚电路的重叠。**没有任何机器人学内容**——没有 embodied agent、没有 robot control、没有 sim-to-real、没有 manipulation。投稿 CoRL **会被 desk reject**，概率接近 100%。\n\n合理的目标 venue 应该是 **NeurIPS / ICML / ICLR 主会**，或 **EMNLP / ACL**（如果定位为 NLP venue）。以下评估假设投稿目标为这些 NLP/ML 主会（如 ICLR 2026 或 NeurIPS 2026），评估 idea 的内在质量。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[Self-Correction Bench](https://arxiv.org/abs/2507.02778)** (NeurIPS 2025 Workshop): 首次量化了 14 个非推理模型上平均 64.5% 的自我纠错盲区，发现 \"Wait\" token 可降低 89.3%。仅提供训练数据假说，无机制解释。这是本 proposal 的核心现象来源。**注意：这是 workshop paper，非主会**，说明该现象的学术重要性尚未经过主会级别的同行评审确认。\n\n- **[Ackerman & Panickssery - Self-Authorship Vector](https://arxiv.org/abs/2410.02064)** (ICLR 2025 main): 在 Llama3-8b-Instruct 中发现了 self-authorship vector，可通过 activation steering 控制模型的自我归因感知。方法论（nuisance-vector deconfounding）确实存在且有效。这是 proposal 的 Tier 3 干预的直接基础，reference 描述准确。\n\n- **[Vennemeyer et al. - Sycophancy Decomposition](https://arxiv.org/abs/2509.21305)** (ICLR 2026): 将谄媚分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，证明它们是独立可控的线性方向。该论文确实已被 ICLR 2026 接收，proposal 中的描述（selectivity ratios, cosine similarity 变化趋势）与原文一致。\n\n- **[Wang et al. - Sycophancy Circuit](https://arxiv.org/abs/2508.02087)** (AAAI 2026 main): 通过 logit-lens 和 activation patching 发现谄媚的两阶段电路，第一人称提示比第三人称引发更强的表征扰动。论文确实存在且已在 AAAI 2026 发表。\n\n- **[Zhang & Lin - Orthogonal Interference / Simulated Adoption](https://arxiv.org/abs/2602.04918)**: 发现上下文信号通过准正交旋转（而非幅度稀释）覆盖参数知识。尚未正式发表（arXiv preprint），但分析框架合理。\n\n- **[Basu et al. - Knowledge-Action Gap](https://arxiv.org/abs/2603.18353)**: 展示四种机制干预方法尽管内部探针 AUROC 达 98.2% 仍无法纠正错误。是近期 preprint，尚未正式发表。\n\n- **[O'Brien et al. - Sycophancy Neurons](https://arxiv.org/abs/2601.18939)** (NeurIPS 2025 Workshop): 使用 Gemma-Scope SAEs 分离出 3% 的 MLP 神经元负责谄媚。Workshop paper。\n\n- **[Qwen-Scope](https://arxiv.org/abs/2605.11887)** (May 2026): 确实已发布，提供 Qwen3/3.5 的 SAE suite。Reference 准确。\n\n- **调研总结**: 这个领域正处于\"行为现象已观察到、机制工具箱已成熟、但两者尚未连接\"的阶段。Sycophancy 的机制研究在 2025-2026 爆发（至少 5 篇独立工作），self-correction blind spot 则仅有一篇 workshop paper 建立。**目前没有发现任何工作直接做了\"self-correction blind spot 的机制解释\"或\"blind spot 与 sycophancy 电路的对比\"**——这个 gap 确实存在。但该 gap 的重要性取决于 blind spot 本身作为研究对象的分量（目前仅 workshop paper 级别的支撑）。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在部分 trivial alternative 威胁，但 proposal 的增量价值有合理辩护。**\n\n最简单的替代方案是：**直接做线性探针（linear probing）对比 own-output vs external-text 的内部表征差异**——不需要三层 confound control、不需要 SAE feature overlap analysis、不需要 geometric decomposition。一个简单的 probing study 就能给出\"模型在哪些层区分了 own vs external\"的初步答案。\n\nProposal 对此的增量价值在于：\n1. **Confound control (Tier 2)**：Ye et al. 和 Wang et al. (ICML 2025) 确实指出了 role-token confound 的真实性，所以仅靠 role-token-based 的对比确实有方法论缺陷。Tier 2 的 attribution-only minimal pair 设计是实质性的方法论改进。\n2. **Detection vs Correction 的分解**：这比简单 probing 有更强的解释力。\n3. **与 SYA 电路的定量比较**：这是核心 novelty claim，简单 probing 做不到。\n\n但要注意：**如果最终发现 blind spot 的机制就是\"模型在 assistant turn 里更倾向于保持连贯性\"这样一个直观解释**，那么整个精密的 confound-control + geometric analysis 工程量相对于所得洞察就显得过重了。\n\n---\n\n```\n【前提假设检验】:\n```\n\n核心 claim 的逻辑链中有 **三个关键未经验证的假设**：\n\n1. **\"Blind spot 是一个稳健的、跨模型的现象\"假设**：64.5% 这个数字来自 Self-Correction Bench 一篇 workshop paper，仅测试了 14 个非推理模型。该现象是否在更新的模型（特别是 2026 年的 Gemma 3、Qwen 3）上依然成立？如果 Tier 1 复现失败（blind spot 已被新模型的训练解决），整个研究的基础就不存在了。Proposal 将此作为 Tier 1 但没有讨论复现失败的风险。\n\n2. **\"Textual attribution 足以驱动 blind spot\"假设**：Tier 2 的设计假设纯文本层面的归因线索（\"your previous response\" vs \"a student wrote\"）足以激活与 role-token 相同的 self-authorship 表征。但 Ackerman & Panickssery 的 self-authorship vector 是在 **role-token 存在的自然对话格式** 下提取的。如果模型的 self-authorship 感知主要依赖 role tokens 而非文本线索，Tier 2 可能根本观察不到 blind spot——这不证明\"authorship drives the blind spot\"，而是证明\"textual attribution alone doesn't trigger self-authorship\"。这个歧义性在 proposal 中没有充分讨论。\n\n3. **\"SYA-blind spot 电路重叠 = 统一机制\"的推理有效性**：即使发现 SYA 方向和 blind-spot 方向的 cosine similarity 高，也可能只是因为它们都涉及\"override correct output\"这一共性——任何涉及抑制正确输出的行为可能都投射到类似的子空间，而不意味着因果上共享一个\"contextual override\"机制。Circuit overlap 可以是因果共享的，也可以是相关但非因果的。Proposal 的 falsification criteria 虽然设定了阈值，但对这种 confounding 解释讨论不足。\n\n---\n\n```\n【3 维度打分】:\n```\n\n### 1. Novelty: **中** \n\n**理由**：\n- (+) 在我的调研范围内，**确实没有发现任何工作直接对 self-correction blind spot 进行机制解释**，也没有工作连接 blind spot 和 sycophancy 电路。这个 specific gap 是真实存在的。\n- (+) 三层 confound-control 设计（Tier 1-2-3）是方法论上的实质贡献，解决了 Ye et al. (arXiv:2603.12277) 和 Wang et al. (ICML 2025, arXiv:2505.00626) 指出的 role-token confound。\n- (+) 将 Orthogonal Interference 框架 (Zhang & Lin, arXiv:2602.04918) 应用于解释 knowledge-action gap 中干预失败的原因是一个合理的新连接。\n- (−) 但核心研究范式——\"用 activation patching + SAE feature analysis + linear probing 解释某个 LLM 行为 X\"——在 2025-2026 年已经是 **标准方法论**。Wang et al. (AAAI 2026)、Vennemeyer et al. (ICLR 2026)、O'Brien et al. (NeurIPS 2025 Workshop)、Zhang & Chen (arXiv:2601.11563) 都在做同样范式的工作，只是应用于不同的行为。本 proposal 是将这套工具箱 **应用** 到一个新对象（blind spot），而不是发明新工具。\n- (−) 核心假说——\"blind spot 与 sycophantic agreement 共享电路\"——考虑到 proposal 自己详细阐述的结构同构性（contextual signal override），这个假说 **非常自然/可预测**。如果验证为正，审稿人大概率会说 \"I would have guessed this given the clear structural analogy the authors themselves describe.\"  如果被否证，论文的叙事框架反而更有趣（\"surprisingly, they are distinct\"），但 proposal 的 framing 偏向验证而非否证。\n\n### 2. Significance: **中偏弱**\n\n**理由**：\n- (+) 理解 LLM 为何不能纠正自己的错误确实是一个有实际意义的问题——这直接关系到 self-refinement pipeline 的可靠性。\n- (+) 如果 Orthogonal Interference 机制被确认，这为理解 \"为什么 magnitude-based activation steering 不 work\" 提供了一个有解释力的框架，对整个 mech-interp 社区有价值。\n- (−) **Proposal 明确声明不产出 mitigation 方案** (\"we do NOT claim this work will yield mitigation strategies\")。这意味着论文的贡献纯粹是描述性/解释性的。在一个日益强调 \"actionable interpretability\" 的社区（参见 Basu et al. 的标题 \"Interpretability without Actionability\" 本身就是对纯解释性工作的批评），一个纯 \"map the circuit\" 的论文需要更强的 insight 才能获得认可。\n- (−) Blind spot 现象本身的学术地位仍不牢固——来自 **一篇 NeurIPS Workshop paper**（非主会），且该数字（64.5%）尚未被独立复现或在主会级别确认。在此基础上建立整个机制研究，存在\"在沙上建塔\"的风险。\n- (−) 即使所有结果都如 proposal 预期，最终产出是：\"我们发现 blind spot 的确是通过正交旋转（而非幅度抑制）抑制了 correction pathway（但不影响 detection），且其电路与 SYA 有 X% 重叠。\" 这是一个 **clean but incremental** 的结论，不太可能改变该领域的研究方向。\n\n### 3. Related Work: **强**\n\n**理由**：\n- 覆盖极其全面：proposal 引用了 20+ 篇高度相关的论文，覆盖了 blind spot 文档 (arXiv:2507.02778)、self-authorship detection (Ackerman & Panickssery, ICLR 2025)、sycophancy 机制的所有重要工作 (Wang et al. AAAI 2026; Vennemeyer et al. ICLR 2026; O'Brien et al.; Zhang & Chen; Genadi et al.)、knowledge-action gap (arXiv:2603.18353)、error decomposition (arXiv:2601.00828)、role-token confounds (Ye et al.; Wang et al. ICML 2025)、Wait token (Troitskii et al. EMNLP 2025; Hwang et al.)。\n- 经过我的调研验证，**引用的论文基本都真实存在，venue 和核心描述准确**（Qwen-Scope arXiv:2605.11887 确认存在；Vennemeyer et al. ICLR 2026 确认被接收）。\n- 差异化定位清晰：每篇 related work 都说明了与 proposal 的区别和本工作如何利用其方法论或发现。\n- 唯一的小遗漏：Anthropic 2025 年的 circuit tracing work on Claude 3.5 Haiku 在 mech-interp 方法论层面可能相关但未被引用，不过这不构成实质性缺陷。\n\n---\n\n```\n【概率估计】: [20% - 32%] 中位 25%\n```\n\n**注意：上述概率是针对 NLP/ML 主会（如 ICLR/NeurIPS/ICML）的估计。如果投稿 CoRL 2026，概率接近 0%（desk reject）。**\n\n```\n【估计理由】:\n```\n\n从 3 维度到概率的推理：\n\n- **Related Work = 强**：这保证了项目的下限——即使 idea 本身只是 average，扎实的 related work 覆盖意味着审稿人不太可能以\"miss important prior work\"为由拒稿。\n- **Novelty = 中**：这决定了项目的天花板。核心贡献是\"将已有方法论工具箱应用到一个新的研究对象并测试一个自然假说\"。这在顶会上是 borderline——取决于审稿人是否觉得 blind spot 值得单独研究、以及结果是否足够 surprising。**Novelty 是限制上界的维度**。\n- **Significance = 中偏弱**：这进一步压低了概率。纯解释性贡献、无 mitigation、基础现象仅有 workshop paper 级别的支撑——这些因素叠加使得审稿人可能质疑 \"so what?\"\n\n综合判断：idea 方向正确、有真实的 gap、方法论设计严谨，但 **核心发现无论是 positive（电路共享→\"I would have guessed this\"）还是 negative（电路不共享→叙事框架弱化），都不太可能让审稿人感到 surprising**。这将其锚定在 25-35% 区间的下端。\n\n```\n【主要风险】:\n```\n\n1. **\"Expected Result\" 风险**：Proposal 自己花了大量篇幅论证 blind spot 和 SYA 的结构同构性，使得\"电路共享\"的结果变得高度可预测。如果核心假说被验证，审稿人可能评价为 \"confirming the obvious structural analogy with expensive experiments\"。这是 idea 层面最大的风险——不是方法不对，而是 insight 不够 surprising。\n\n2. **\"基础现象不够稳固\" 风险**：整个研究建立在一个 workshop paper 报告的 64.5% blind spot rate 上。如果 Tier 1 复现发现新模型（Gemma 3、Qwen 3）的 blind spot 已显著降低（这些模型可能已通过更好的 RLHF 缓解了此问题），则研究的动机基础将被动摇。审稿人可能质疑：如果最新模型已经不太有这个问题了，为什么还要花大量资源去解释它？\n\n---\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [Ackerman & Panickssery - Self-Authorship Vector (ICLR 2025)](https://arxiv.org/abs/2410.02064)\n- [Vennemeyer et al. - Sycophancy Decomposition (ICLR 2026)](https://arxiv.org/abs/2509.21305)\n- [Wang et al. - Sycophancy Circuit (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40645)\n- [Zhang & Lin - Orthogonal Interference](https://arxiv.org/abs/2602.04918)\n- [Basu et al. - Knowledge-Action Gap](https://arxiv.org/abs/2603.18353)\n- [O'Brien et al. - Sycophancy Neurons](https://arxiv.org/abs/2601.18939)\n- [Qwen-Scope (arXiv:2605.11887)](https://arxiv.org/abs/2605.11887)\n- [Ye et al. - Role-Token Confounds](https://arxiv.org/abs/2603.12277)\n- [Wang et al. - Role Learning Shortcuts (ICML 2025)](https://arxiv.org/abs/2505.00626)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile my thorough assessment.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 致命问题预警：严重的投稿会议不匹配 ⚠️\n\n在进入常规 rubric 之前，必须首先指出：CoRL 2026（Conference on Robot Learning）\n明确声明 \"submissions without a robotics focus will be returned without review\"\n（https://www.corl.org/contributions/call-for-papers）。\n本 proposal 是纯粹的 LLM mechanistic interpretability 研究——自纠错盲区的\n电路级机制分析、sycophancy 电路重叠测试、SAE 特征分析——与机器人学习完全无关。\n投稿 CoRL 主会将会被直接 desk reject，无论 idea 质量如何。\n适合的投稿目标：NeurIPS / ICML / ICLR 主会，或 EMNLP/ACL 的 interpretability track。\n\n以下评估假设投稿至适当的 ML/NLP 顶会（如 NeurIPS/ICLR），评价 idea 本身的质量。\n\n\n【领域调研】:\n\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778) (NeurIPS 2025 Workshop): \n  文档化了 64.5% 的自纠错盲区现象，发现 Wait token 可降低 89.3%。但仅提出\n  training-data 假说，未做任何 mechanistic analysis。原始实验设计中 role-token \n  与 authorship 的 confound 确实存在（own-output 使用 assistant turn，external \n  使用 user turn）。论文真实存在，描述准确。\n\n- [Ackerman & Panickssery (arXiv:2410.02064)](https://openreview.net/forum?id=wWnsoLhHwt) (ICLR 2025 主会): \n  在 Llama3-8b-Instruct 中发现 self-authorship vector，证明可因果控制模型的\n  自我作者认知。提供了 nuisance-vector deconfounding 方法论。论文真实存在，\n  是本 proposal Tier 3 的核心工具。\n\n- [Vennemeyer et al. (arXiv:2509.21305)](https://openreview.net/forum?id=d24zTCznJu) (ICLR 2026): \n  将 sycophancy 分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，\n  证明二者是独立可操控的线性方向。SYA 与 genuine agreement 在中后层急剧分离\n  （cosine 从 ~0.99 降至 ~0.07）。论文真实存在，描述准确。这是 proposal \n  unified-mechanism 假说的关键依据。\n\n- [Zhang & Lin (arXiv:2602.04918)](https://arxiv.org/abs/2602.04918) (preprint 2026): \n  \"Simulated Adoption\" — 发现 in-context 信号通过准正交旋转（而非幅度稀释）\n  覆盖参数知识。论文真实存在，proposal 对其描述准确。\n\n- [Basu et al. (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353) (preprint 2026): \n  \"Interpretability without Actionability\" — 四种 mechanistic 干预范式均无法弥合\n  knowledge-action gap，尽管探针达到 98.2% AUROC。论文真实存在。这为本 proposal \n  的\"解释而非修复\"定位提供了合理性。\n\n- [Wang et al. (arXiv:2508.02087)](https://arxiv.org/abs/2508.02087) (AAAI 2026): \n  Sycophancy 的两阶段抑制电路，first-person framing 产生更强的表征扰动。\n  与 proposal 描述一致。\n\n- [O'Brien et al. (arXiv:2601.18939)](https://arxiv.org/abs/2601.18939) (NeurIPS 2025 Workshop): \n  用 Gemma-Scope SAE + linear probes 定位 sycophancy 的 3% 关键 MLP 神经元。\n  Pipeline 可直接复用。\n\n- [Sparse Activation Fusion for sycophancy mitigation](https://openreview.net/forum?id=BCS7HHInC2) (2025-2026): \n  动态减去 user-induced bias，将 sycophancy 从 63% 降至 39%。Proposal 未引用此工作，\n  可能是一个 related work 遗漏。\n\n- [Roytburg et al. (arXiv:2509.03647)](https://arxiv.org/abs/2509.03647) (NeurIPS 2025): \n  Self-preference 跨多个非线性方向，单一 steering vector 不稳定。\n  Proposal 正确引用并将此作为多方法动机。\n\n- 调研总结: 该领域呈现\"工具就位、空白尚存\"的格局。Sycophancy 的 mechanistic \n  分析已有 5+ 篇独立工作完成不同侧面的映射；self-authorship vector 已被 ICLR 2025 \n  验证；SAE 工具链（Gemma Scope 2, Llama Scope, Qwen-Scope）已覆盖三大模型族。\n  但**尚无任何工作**对 self-correction blind spot 做过控制混淆的 mechanistic 分析，\n  更无人测试其与 sycophantic agreement 的电路重叠。Proposal 确实填补了一个真实空白。\n\n\n【Trivial Alternative 检验】:\n\n存在部分 trivial alternative 威胁，但不致命：\n\n1. **简化版 probing study**: 可以仅在 1 个模型上做 Tier 1+2 的行为实验 + 基础 \n   linear probe，不做 circuit mapping / geometric decomposition / cross-model \n   comparison，就能回答\"是 role token 还是 attribution 驱动盲区\"这个核心问题。\n   这个简化版成本极低（~50 GPU-hours），但只回答了 WHAT 而不是 WHY/HOW。\n\n2. **直接迁移 Ackerman 的 self-authorship vector 做因果测试**: 仅用 Tier 3 \n   的 vector addition/subtraction 就能获得因果证据，无需 SAE 分析或电路映射。\n   这是一个 ~20 GPU-hours 的实验，可能就能回答\"authorship representation \n   因果驱动盲区\"。\n\n增量价值在于: (a) confound-control 的三层设计是方法论贡献，超越简单 probing；\n(b) sycophancy 电路重叠测试是独立的科学问题，trivial probe 无法回答；\n(c) geometric mechanism (orthogonal interference vs magnitude dilution) \n提供对 knowledge-action gap 失败原因的解释性假设。\n\n**结论**: 核心问题的最简版本确实可以用更低成本部分回答，但 proposal 的完整设计\n在深度和广度上有实质增量。风险在于审稿人可能认为\"简化版就够了\"。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"Blind spot ≈ sycophantic agreement\" 的结构同构假说**: 这是整个 proposal \n   的核心赌注。虽然表面类比合理（contextual signal 抑制 correct behavior），\n   但 blind spot 可能通过完全不同的机制运作——例如 self-consistency bias（模型\n   倾向于保持输出一致性）、next-token prediction 的自回归惯性、或更简单的\n   surface-level heuristic。Proposal 设计了 falsification criteria，但如果\n   F1-F3 都 reject，结果是一个 negative finding（\"两个现象不共享电路\"），\n   这在审稿中价值争议较大。\n\n2. **Self-authorship vector 跨模型泛化**: Ackerman 的 vector 仅在 Llama3-8b-Instruct \n   上验证。假设它可以在 Gemma 3 和 Qwen 3 中被类似提取是合理的但未经验证。\n   如果某些模型没有清晰的线性 self-authorship 表征，Tier 3 将失效。\n\n3. **\"Role token confound 是重要的\"**: 虽然 Ye et al. 和 Wang et al. 提供了\n   间接证据，但原始 blind-spot 论文的 64.5% 效果是否主要由 role token 驱动\n   还是由 textual attribution 驱动，是一个实证问题。如果 Tier 2 显示效果大幅\n   减弱（confound 是主要 driver），那么\"authorship attribution 驱动盲区\"\n   的核心叙事就被削弱了——虽然这本身是有价值的发现，但会让后续 Phase 2-4 \n   的全部设计失去基础。\n\n4. **Geometric decomposition 的可解释性**: 假设 angular vs radial decomposition \n   能提供清晰的 mechanistic 解释。Zhang & Lin 的方法在 knowledge conflict 上\n   有效，但 self-correction blind spot 可能涉及更复杂的非线性动态。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由: \n   - 确认空白: 调研证实尚无工作对 self-correction blind spot 做过 confound-controlled \n     mechanistic analysis，也无人测试其与 sycophantic agreement 的电路重叠。\n     这是一个真实的未填补空白。\n   - 但方法论不新: 每个单独组件——self-authorship vector extraction (Ackerman, \n     ICLR 2025), SYA direction extraction (Vennemeyer, ICLR 2026), SAE-to-probe \n     pipeline (O'Brien, 2025), geometric decomposition (Zhang & Lin, 2026), \n     Error Depth decomposition (Li, 2026) ——都是直接复用已有工具。创新在于\n     **组合应用到新现象**，而非方法创新。\n   - 核心假说（blind spot ≈ SYA 的 contextual override）虽然有趣但不算反直觉——\n     任何了解 sycophancy 文献的研究者看到 blind spot 后都可能产生这个类比。\n   - Confound-control 的三层设计（Tier 1-2-3）是真正的方法论贡献，\n     是 proposal 中最有原创性的部分。\n\n2. Significance: 【中】\n   理由:\n   - Self-correction 是 LLM 安全和可靠性的重要问题，理解盲区的 mechanistic \n     原因有学术价值。\n   - 但 proposal 明确声明不追求 mitigation（\"we do NOT claim this work will yield \n     mitigation strategies\"）。这在 Basu et al. (arXiv:2603.18353) 已经证明\n     interventions fail 的背景下是诚实的，但也限制了实际影响力。\n   - 纯 mechanistic explanation 的影响力天花板低于\"解释+修复\"的工作。\n     审稿人常见评论: \"interesting analysis but what can we do with this?\"\n   - 如果 unified-mechanism 假说被证实，其理论意义大于实践意义——\n     它统一了 sycophancy 和 self-correction 的理解，但不直接帮助解决任何问题。\n   - 如果假说被否定（F1-F3 falsification），negative result 的价值在\n     top venue 上争议较大。\n\n3. Related Work: 【强】\n   理由:\n   - 调研中引用的所有关键论文（Ackerman ICLR 2025, Vennemeyer ICLR 2026, \n     Zhang & Lin 2026, Basu 2026, Wang AAAI 2026, O'Brien 2025, Roytburg \n     NeurIPS 2025）均经查证真实存在且描述准确。\n   - 覆盖异常全面: sycophancy mechanistic 文献（5+ 篇）、self-authorship 检测、\n     knowledge-action gap、error decomposition、role-token confound、\n     Wait token 分析均有覆盖。\n   - 差异化定位清晰: 明确标注了\"Missing piece\"并准确描述了 gap。\n   - 对 cautionary findings（如 Roytburg 的\"多方向/非线性\"警告）的处理诚实，\n     并转化为方法论动机。\n   - 可能遗漏: Sparse Activation Fusion (SAF) for sycophancy mitigation \n     未被引用，但对 proposal 核心论点影响不大。\n\n\n【概率估计】: \n   - 投稿 CoRL 2026: 0-2%（desk reject，venue 完全不匹配）\n   - 若投稿至适当 venue（NeurIPS/ICLR 主会）: [22% - 32%] 中位 27%\n\n【估计理由】: \n   Idea 处于 rubric 的\"25-35%\"区间——方向正确，有真实的 novelty delta\n  （confound-controlled mechanistic analysis of blind spot + sycophancy overlap \n   test 是未被做过的工作），但核心发现 if positive 不够 surprising。\n   具体而言:\n   \n   - Related Work（强）确保了定位清晰，不会因 related work 不足被拒。\n   - Novelty（中）是主要限制因素: 方法论上是已有工具的组合应用，\n     核心假说（contextual override）是\"reasonable guess\"而非\"surprising insight\"。\n     审稿人可能评价\"competent engineering of existing mech-interp tools \n     applied to a specific phenomenon\"。\n   - Significance（中）是次要限制: 纯 explanation without mitigation \n     在 top venue 上需要 explanation 本身足够 surprising 或 general 才能弥补\n     缺乏 actionability 的短板。本 proposal 的 explanation 如果被证实，\n     其 generality（unified contextual override across sycophancy and self-correction）\n     有一定理论价值，但不足以进入\"surprising\"区间。\n   \n   上界（32%）对应: Tier 2 confound-control 设计被视为重要方法论贡献 + \n   unified mechanism 假说被证实且 geometric analysis 提供了对 knowledge-action \n   gap 失败原因的首个解释。\n   下界（22%）对应: 审稿人认为这是 incremental application of existing tools + \n   pure explanation without actionability。\n\n【主要风险】:\n1. **\"Competent but not surprising\" 风险**: 核心假说（blind spot ≈ SYA contextual \n   override）如果被证实，审稿人很可能说 \"this is what I would have expected\" — \n   因为 sycophancy 和 self-correction blind spot 的结构类比已经在 proposal \n   本身的 framing 中显而易见。真正 surprising 的结果应该是 reviewer 事先\n   *不会猜到*的，但这个假说恰恰是\"一旦看到两个现象的并列描述就自然想到的\"。\n   \n2. **\"Explanation without actionability\" 在 top venue 的接受度风险**: \n   Proposal 诚实地声明不追求 mitigation，这在 workshop paper 级别完全可以，\n   但在 top venue 主会上，纯 mechanistic explanation 需要提供足够 general \n   或 surprising 的 insight 来证明其独立价值。在 arXiv:2603.18353 已经证明\n   interventions fail 的语境下，\"解释为什么 fail\"是有价值的 follow-up，\n   但也容易被视为该工作的 incremental extension。\n```\n\n---\n\n**⚠️ 关键提醒：投稿目标不匹配**\n\nCoRL 2026 明确要求 robotics focus，声明\"submissions without a robotics focus will be returned without review\"。本 proposal 是纯 LLM mechanistic interpretability 研究，与机器人学习完全无关。**无论 idea 质量如何，投稿 CoRL 将导致 desk reject。**\n\n建议投稿目标：\n- **NeurIPS 2026 主会**（interpretability track）\n- **ICLR 2027**\n- **ICML 2026**（如 deadline 未过）\n- **EMNLP 2026**（如果定位为 NLP-focused interpretability）\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)\n- [Ackerman & Panickssery - Self-Generated-Text Recognition (ICLR 2025)](https://openreview.net/forum?id=wWnsoLhHwt)\n- [Vennemeyer et al. - Sycophancy Is Not One Thing (ICLR 2026)](https://openreview.net/forum?id=d24zTCznJu)\n- [Zhang & Lin - Simulated Adoption (arXiv:2602.04918)](https://arxiv.org/abs/2602.04918)\n- [Basu et al. - Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353)\n- [O'Brien et al. - A Few Bad Neurons (arXiv:2601.18939)](https://arxiv.org/abs/2601.18939)\n- [Roytburg et al. - Breaking the Mirror (arXiv:2509.03647)](https://arxiv.org/abs/2509.03647)\n- [Wang et al. - Sycophancy Origins (arXiv:2508.02087)](https://arxiv.org/abs/2508.02087)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Sparse Activation Fusion for Sycophancy](https://openreview.net/forum?id=BCS7HHInC2)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题 — 投稿会议匹配性】:\n⚠️ CoRL (Conference on Robot Learning) 是一个聚焦机器人学习的会议，核心议题包括 imitation learning、reinforcement learning for robots、sim-to-real transfer、manipulation、locomotion、robot perception 等。本 proposal 是一项关于 LLM 内部机制可解释性的研究（self-correction blind spot 的 circuit-level 成因分析），与机器人学习完全无关。投稿 CoRL 主会几乎必然被 desk reject。\n\n建议投稿会议：NeurIPS / ICML / ICLR 主会，或 ACL / EMNLP（如果偏 NLP 社区）。以下评估假设投稿至适配的 ML/NLP 顶会（如 NeurIPS/ICLR），而非 CoRL。\n\n---\n\n【领域调研】:\n\n- **Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop)**: 原始行为发现论文，文档了 14 个非推理模型平均 64.5% 的 blind spot 率以及 Wait token 的 89.3% 缓解效果。提供了训练数据假说但无机制解释。该论文确实存在且描述准确。但注意这只是 NeurIPS **Workshop** 论文，非主会。\n\n- **Ackerman & Panickssery (arXiv:2410.02064, ICLR 2025 主会)**: 确认存在，发现了 Llama3-8b-Instruct 中的 self-authorship vector，可以因果控制模型的自我归因感知。论文已被 ICLR 2025 主会接收。这是本 proposal 的关键方法学基础。\n\n- **Vennemeyer et al. (arXiv:2509.21305, ICLR 2026)**: 确认存在且已被接收。将 sycophancy 分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，证明它们是独立可操控的线性方向。selectivity ratios 最高达 36.8x。这为 proposal 的 unified mechanism 假说提供了精确的比较对象。\n\n- **Wang et al. (arXiv:2508.02087, AAAI 2026)**: 确认存在。发现了两阶段 sycophancy circuit：第一人称 framing 在中后层(~layer 19)产生更强的表征扰动，抑制事实知识。结构上与 blind spot 的 contextual override 类似。\n\n- **Zhang & Lin (arXiv:2602.04918)**: 确认存在。发现 in-context conflict 通过 \"Orthogonal Interference\"（准正交几何旋转而非幅度稀释）覆盖参数知识。在 Llama-3.1-8B、Qwen-3-4B、GLM-4-9B 上验证。\n\n- **Basu et al. (arXiv:2603.18353)**: 确认存在。Knowledge-action gap 论文，四种 mechanistic intervention 范式均无法弥合 gap（尽管 probe AUROC 达 98.2%）。为\"理解 WHY\"提供了动机。\n\n- **Qwen-Scope (arXiv:2605.11887, May 2026)**: 确认存在，为 Qwen3/3.5 系列提供了预训练 SAE 套件。这使三模型家族对称比较成为可能。\n\n- **O'Brien et al. (arXiv:2601.18939, NeurIPS 2025 Workshop)**: 使用 Gemma-Scope SAE 隔离 sycophancy 神经元（前 3% MLP 神经元），提供了 SAE-to-probe-to-neuron pipeline。\n\n- **调研总结**: Self-correction blind spot 是 2025 年由一篇 NeurIPS Workshop 论文提出的行为发现。sycophancy 的机制可解释性在 2025-2026 年间快速发展（至少 5 篇独立工作从不同角度进行了 circuit-level 分析）。Self-authorship 的内部表征也已被 ICLR 2025 工作识别。但**尚无工作将这些线索整合起来**——即在控制 confound 的条件下对 blind spot 做 circuit-level 分析，并与 sycophancy 电路比较。这个 gap 是真实的。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在一个更低成本的替代方案值得认真考虑：\n\n1. **纯行为 confound-control 实验（Tier 1+2）**: Proposal 中最有价值的贡献之一是 Tier 2 的 attribution-only minimal pairs 设计（控制 role tokens，只改变文本归因）。这个实验本身只需要推理级别的 GPU 开销（无需缓存全层激活），但已经能回答一个核心问题：\"blind spot 是由 authorship attribution 驱动的，还是由 role-token 架构差异驱动的？\" 这个行为发现如果 robust 到三个模型家族上，本身就有论文级别的价值。\n\n2. **直接用 self-authorship vector 做 steering**: Ackerman & Panickssery 已经提供了 self-authorship vector。直接测试\"加/减 self-authorship vector 是否影响 blind spot 严重度\"是一个很低成本的实验，且能提供因果证据。\n\n**增量价值判断**: Proposal 的真正增量在于 (a) 完整的 circuit mapping（哪些 layer/head/neuron 负责 suppression），(b) 与 SYA 电路的定量 overlap 测试，(c) 几何机制刻画（orthogonal vs. magnitude）。这些不是 trivial 替代能达到的。但问题是：如果 Tier 2 行为实验就能证明 \"attribution drives blind spot\"，审稿人可能会问：\"完整 circuit mapping 的额外洞见是什么？\" 如果答案是 \"它与 sycophancy 共享电路\"，那这个发现 surprising 吗？\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的假设：\n\n1. **Self-authorship vector 的跨模型迁移性**: Ackerman & Panickssery 的 self-authorship vector 仅在 Llama3-8b-Instruct 上发现和验证。Proposal 假设类似的 vector 在 Gemma 3 和 Qwen 3 上也能提取出来，且具有相似的因果效力。这一假设未经验证。Roytburg et al. (NeurIPS 2025) 明确警告 self-preference \"spans multiple or nonlinear directions\"，说明单线性方向可能不够。\n\n2. **Error correction 的线性可分离性假设**: Phase 2 用线性 probe 分别探测 detection 和 correction 信号，假设这些是线性可分的。如果 blind spot 的 suppression 机制是非线性的（如 Roytburg et al. 所暗示），线性 probe 可能无法捕获关键信号。\n\n3. **\"结构同构 = 电路共享\" 的推断**: Proposal 的核心假说是 blind spot 与 sycophantic agreement 结构同构（contextual signal overrides correct behavior），因此推测它们共享电路。但结构同构是功能描述层面的类比，不一定意味着实现层面（电路层面）的共享。两个功能类似但进化路径不同的行为完全可能用不同电路实现。\n\n4. **Confound 是 \"问题\" 而非 \"本质\"**: Tier 2 假设 role-token confound 是需要\"排除\"的干扰因素。但如果 LLM 的 self-authorship 认知本身就是通过 role tokens 和 attention mask 实现的（这正是 chat 模型训练的方式），那么 role-token 信号可能不是 confound 而是机制本身。Tier 2 在排除 role tokens 后仍然发现 blind spot 是一个 empirical question，结果可能是 \"blind spot 在 Tier 2 消失\"，这会推翻整个 Phase 2-3 的研究动机。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是\"将已有工具（self-authorship vector, SAE, activation patching, 几何分解）应用于一个具体现象（blind spot）并与另一个已被详细研究的现象（sycophancy）做比较\"。这是一个 well-motivated 的\"连接性\"研究，但每个单独组件都有强大的先例：\n   - Self-authorship vector → Ackerman & Panickssery (ICLR 2025)\n   - Sycophancy circuit mapping → Wang et al. (AAAI 2026), O'Brien et al., Genadi et al., Vennemeyer et al. (ICLR 2026)\n   - 几何分解 → Zhang & Lin (arXiv:2602.04918)\n   - Detection vs. correction 分离 → Li (arXiv:2601.00828)\n   \n   Proposal 的方法学贡献（三层 confound control design）是 solid 的，但这是实验设计的严谨性而非概念创新。真正的 novelty delta 在于\"整合\"——将这些独立的线索串联成一个统一叙事。这有价值，但审稿人可能将其视为 \"application of existing mechanistic interpretability tools to a new target phenomenon\" 而非 \"fundamentally new methodology or insight\"。\n\n2. **Significance: 中** — \n   Self-correction blind spot 是一个重要且 practical 的问题——理解为什么 LLM 不能纠正自己的错误对 AI safety 和可靠性有直接影响。但有两个限制因素：\n   \n   (a) Proposal 明确声明不追求 mitigation（因为 Basu et al. 已证明四种干预范式失败）。纯 mechanistic understanding 论文在主会的接受门槛更高——审稿人会问 \"so what do we do with this understanding?\"。Orthogonal interference 的发现可能解释为什么 magnitude-based interventions 失败，但 proposal 不承诺提出替代的 directional intervention。\n   \n   (b) 如果核心发现是 positive（blind spot 与 SYA 共享电路），审稿人很可能会说 \"I would have guessed this\"——因为两者的结构同构性在论文 framing 中已经非常明显。如果核心发现是 negative（不共享电路），信息量更大但 narrative 更弱。这是一个 dual-outcome 困境，无论哪个结果都难以达到 \"surprising\" 的标准。\n   \n   (c) 原始 blind spot 发现来自一篇 NeurIPS Workshop 论文（非主会），说明社区对这个现象的认可度和关注度可能不如 proposal 所暗示的那么高。\n\n3. **Related Work: 强** — \n   Related work 覆盖异常全面且精确。几乎所有 2024-2026 年间与 sycophancy 机制、self-authorship 检测、knowledge-action gap、self-correction 分解相关的工作都被引用和准确定位。特别值得肯定的是：\n   - 正确区分了 Vennemeyer et al. 的 SYA vs SYPR 分解\n   - 引用了 Roytburg et al. 的 cautionary finding 并据此调整了方法设计\n   - 引用了 Wang et al. (ICML 2025) 关于 role-token shortcuts 的发现来支撑 confound control 的必要性\n   - 将 Zhang & Lin 的几何框架与 knowledge-action gap 的失败联系起来\n   \n   唯一的小瑕疵：部分引用（如 arXiv:2603.18353, arXiv:2603.12277）发表于 2026 年 3 月，可能是较新的预印本，其评审状态和社区认可度尚不确定。\n\n---\n\n【概率估计】: [20% - 32%] 中位 25%\n（注意：此估计假设投稿至适配的 ML 顶会如 NeurIPS/ICLR。若投稿 CoRL，概率接近 0%——完全的领域不匹配。）\n\n【估计理由】: \n这是一篇 well-crafted 的 mechanistic interpretability 论文 proposal，在实验设计上极其严谨（三层 confound control, pre-registered falsification criteria, 三模型家族对称设计）。但 **idea 的内核是 \"applying existing mech-interp toolkit to a new phenomenon + testing a structural analogy\"**，这把它定位在 \"solid but not surprising\" 的区间。\n\n上限被两条维度限制：\n1. **Novelty** — 每个方法组件都有强先例，核心创新在于\"组合\"而非\"发明\"。\n2. **Significance** — 无论 unified mechanism 假说的结果是 positive 还是negative，都不太可能达到 \"surprising\" 标准。positive 结果验证了一个已经 intuitive 的类比；negative 结果有信息量但弱化了论文的统一叙事。加上明确放弃 mitigation 目标，practical impact 受限。\n\n下限被 **Related Work 的全面性** 和 **confound-control design 的严谨性** 支撑——这些确保了即使 idea 不够 exciting，execution quality 可以 compensate 一部分。\n\n【主要风险】:\n1. **\"Connecting the dots\" ≠ \"New dots\"**: 审稿人可能认为这是将已有工具（SAE, activation patching, geometric decomposition）应用于一个新目标现象的 \"application paper\"，而非提出新方法或新理论框架的工作。在 NeurIPS/ICLR 主会，纯 application 的 mech-interp 论文需要特别强的 surprising findings 来补偿。\n2. **Dual-outcome 困境下的 \"so what\" 问题**: 如果审稿人问 \"假设你完美地 map 了 circuit，我们下一步能做什么？\"，proposal 的回答是 \"understand WHY interventions fail\"。但 understanding WHY 不 bridge 到 actionable mitigation，这在 2026 年 safety-driven 的审稿氛围中可能不够。\n```\n\nSources:\n- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/html/2507.02778)\n- [Ackerman & Panickssery - Self-Generated-Text Recognition (ICLR 2025)](https://openreview.net/forum?id=wWnsoLhHwt)\n- [Vennemeyer et al. - Sycophancy Is Not One Thing (ICLR 2026)](https://openreview.net/forum?id=d24zTCznJu)\n- [Wang et al. - When Truth Is Overridden (AAAI 2026)](https://arxiv.org/pdf/2508.02087)\n- [Zhang & Lin - Simulated Adoption / Orthogonal Interference](https://arxiv.org/pdf/2602.04918)\n- [Basu et al. - Interpretability without Actionability](https://arxiv.org/pdf/2603.18353)\n- [Qwen-Scope (arXiv:2605.11887)](https://arxiv.org/abs/2605.11887)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Intrinsic Self-Correction via Mechanistic Interpretability](https://arxiv.org/abs/2505.11924)\n- [O'Brien et al. - Isolating Sycophancy Neurons](https://arxiv.org/abs/2601.18939)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Mechanistic Anatomy of the Self-Correction Blind Spot: Own-Output Suppression as Contextual Signal Override\n\n## Description\nWe propose a mechanistic investigation of the self-correction blind spot — the finding that LLMs correct identical errors 64.5% less often in their own output versus external text. Rather than seeking mitigation (which four intervention paradigms have failed to achieve; arXiv:2603.18353), we provide the first causal mechanistic account of WHY the blind spot occurs, with rigorous confound controls that the original behavioral finding lacks. Our central hypothesis is that the blind spot is an instance of 'contextual signal override' — structurally isomorphic to sycophantic agreement specifically (not sycophancy broadly; Vennemeyer et al., ICLR 2026 showed sycophancy decomposes into independent sub-behaviors), where a contextual signal (self-authorship, analogous to user opinion) suppresses correct behavior (error correction, analogous to factual knowledge). A key methodological contribution is our three-tier confound-controlled experimental design: Tier 1 replicates the original role-token-based blind spot; Tier 2 uses attribution-only minimal pairs (identical role tokens, different textual attribution) to isolate authorship framing from chat-template architectural confounds — motivated by both Ye et al.'s (arXiv:2603.12277) finding that role tags and content are perfectly correlated and Wang et al.'s (arXiv:2505.00626, ICML 2025) demonstration that LLMs exploit positional and task-type shortcuts rather than genuine role understanding; Tier 3 uses the Ackerman & Panickssery self-authorship vector (ICLR 2025) with nuisance-vector deconfounding as a causal activation-level intervention. Following the Error Depth decomposition (arXiv:2601.00828), we probe detection and correction pathways separately, testing whether own-output framing suppresses correction while leaving detection intact. Informed by Zhang & Lin's Orthogonal Interference finding (arXiv:2602.04918) — that conflicting context overrides parametric knowledge via quasi-orthogonal geometric rotation rather than magnitude dilution — we decompose the blind-spot effect into angular and radial components to characterize the geometric mechanism and potentially explain why prior magnitude-based interventions fail. We run experiments across Gemma 3 (with Gemma Scope 2 SAEs/transcoders), Llama 3.1 8B (with Llama Scope SAEs), and Qwen 3 8B (with Qwen-Scope SAEs; arXiv:2605.11887) — a symmetric three-family design where all models have pre-trained SAE coverage. We apply activation patching, SAE feature analysis following O'Brien et al.'s pipeline (arXiv:2601.18939), and geometric alignment tests to isolate the suppression circuit and quantify its overlap with sycophantic agreement circuits specifically — extracting the SYA direction following Vennemeyer et al.'s difference-in-means methodology and testing geometric alignment, component overlap, and cross-circuit intervention transfer — with pre-registered falsification criteria specifying what evidence would reject the unified mechanism hypothesis. As supplementary analysis, we test two hypotheses for how the Wait token reduces blind spots in non-reasoning models — authorship-signal disruption versus correction-gate bypass — via a single discriminating probe-comparison experiment complementing Troitskii et al.'s reasoning-model findings (arXiv:2510.04128). This work delivers five contributions: (1) a confound-controlled measurement establishing that textual authorship attribution (not role tokens alone) drives the blind spot, (2) the first circuit-level map of the own-output vs. external-text processing asymmetry decomposed into detection and correction pathways, (3) characterization of the geometric mechanism — orthogonal interference versus magnitude dilution — underlying the authorship-driven suppression, (4) quantified evidence for or against a unified 'contextual override' mechanism shared between the blind spot and sycophantic agreement specifically, with explicit falsification criteria, and (5) probe-level characterization of Wait token effects in non-reasoning models.\n\n## Core Problem\nLLMs correct identical errors 64.5% less often when framed as their own output versus external text (the 'blind spot'). The training-data explanation is correlational. Meanwhile, four mechanistic intervention paradigms fail to bridge the knowledge-action gap despite near-perfect internal probes (arXiv:2603.18353), and error detection capability does not predict correction success (arXiv:2601.00828). What mechanistic process causes own-output framing to suppress error correction, and does this suppression share a circuit with sycophancy — the structurally analogous phenomenon where contextual signals (user opinions) override factual knowledge? Critically, the original blind-spot finding (arXiv:2507.02778) confounds authorship attribution with chat-template role tokens — the 'own output' condition uses assistant-turn formatting while the 'external text' condition uses user-turn formatting, introducing differences in special tokens, attention masking, and positional encoding that may partially or wholly explain the effect. Wang et al. (arXiv:2505.00626, ICML 2025) showed that fine-tuned LLMs exploit task-type associations and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, further demonstrating that role tokens alone cannot be trusted as clean experimental variables. Disentangling the authorship signal from these architectural confounds is a prerequisite for any mechanistic account. Moreover, the recent finding that sycophancy decomposes into distinct, independently steerable sub-behaviors — sycophantic agreement versus sycophantic praise (Vennemeyer et al., arXiv:2509.21305, ICLR 2026) — means the unified-mechanism hypothesis must specify WHICH sycophancy sub-behavior shares circuits with the blind spot: we hypothesize sycophantic agreement (contextual override of correct judgments) rather than sycophantic praise (flattery generation) is the relevant analogue.\n\n## Opportunity\nFive converging lines of evidence create a unique opening: (1) The sycophancy mechanistic literature — including Wang et al.'s two-stage suppression circuit (AAAI 2026), Zhang & Chen's 'compliance subspace' unifying sycophancy and conformity (arXiv:2601.11563), O'Brien et al.'s SAE-based isolation of sycophancy neurons (arXiv:2601.18939), Genadi et al.'s linear sycophancy directions in attention heads (arXiv:2601.16644), and crucially Vennemeyer et al.'s causal decomposition of sycophancy into independently steerable sub-behaviors (arXiv:2509.21305, ICLR 2026) — collectively maps the sycophancy mechanism with enough precision that we can now test whether the blind spot is a special case of sycophantic agreement specifically. (2) Ackerman & Panickssery (ICLR 2025) identified a self-authorship vector in Llama3-8b-Instruct with a validated nuisance-vector confound-control methodology — this provides the surgical tool to isolate the authorship signal from role-token confounds that plague the original blind-spot measurement. (3) The knowledge-action gap paper (arXiv:2603.18353) showed interventions fail — but understanding WHY they fail requires knowing the exact circuit architecture, which no one has mapped for the own-output context. Zhang & Lin's 'Orthogonal Interference' finding (arXiv:2602.04918) — that conflicting context overrides parametric knowledge via quasi-orthogonal geometric rotation rather than magnitude dilution — provides a specific geometric hypothesis for HOW the blind-spot suppression might operate at the representation level. (4) The Wait token reduces blind spots by 89.3% in non-reasoning models, but the only mechanistic analysis of Wait (arXiv:2510.04128) studied reasoning models — what Wait does in non-reasoning models lacking backtracking circuits is an open question. (5) The release of Qwen-Scope (arXiv:2605.11887, May 2026) now provides pre-trained SAEs for Qwen3-8B alongside Gemma Scope 2 and Llama Scope, enabling the first symmetric three-model-family mechanistic comparison where all families have full SAE coverage.\n\n## Related Work / Landscape\n**Blind spot documentation**: Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop) documents the 64.5% blind spot across 14 non-reasoning models and discovers the 'Wait' mitigation, but offers only a training-data hypothesis. Critically, its experimental design uses role-token-based framing (assistant turn for own-output, user turn for external), which confounds authorship attribution with chat-template architectural differences — a limitation noted by Ye et al. (arXiv:2603.12277) who showed that role tags and content style are 'perfectly correlated' in chat models, creating interpretability confounds. Wang et al. (arXiv:2505.00626, ICML 2025) further demonstrate that this confound is deep: fine-tuned LLMs rely on task-type exploitation and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, meaning role-token-based experimental designs risk measuring these shortcuts rather than true authorship attribution. **Self-authorship detection**: Ackerman & Panickssery (arXiv:2410.02064, ICLR 2025) discovered a self-authorship vector in Llama3-8b-Instruct, demonstrating causal control over self-authorship perception via activation steering at layer 16. Their nuisance-vector methodology — subtracting the projection onto an output-bias vector computed from generic prompts — provides a validated technique for isolating authorship signals from surface confounds, and is the closest mechanistic precedent to our work. **Self-preference bias**: Xu et al. (arXiv:2402.11436, ACL 2024) document self-bias in self-refinement — LLMs systematically favor their own outputs — providing complementary behavioral evidence that self-authorship triggers preferential treatment. Roytburg et al. (arXiv:2509.03647, NeurIPS 2025) demonstrate that contrastive activation addition can reduce unjustified self-preference bias by up to 97% in LLM evaluators, but find that 'self-preference spans multiple or nonlinear directions' — steering vectors are effective for unjustified self-preference but unstable on legitimate self-preference and unbiased agreement, indicating the self-preference representation is architecturally distributed rather than neatly isolated along a single linear direction. This cautionary finding motivates our multi-method approach (probing, patching, and SAE analysis) rather than relying on a single linear probe. **Mechanistic self-correction**: Representation steering in self-correction (arXiv:2505.11924, AAAI 2026 Workshop) shows prompt-induced latent direction shifts drive correction in detoxification, but does not study the own-vs-external asymmetry. **Wait token mechanics**: Troitskii et al. (arXiv:2510.04128, EMNLP 2025 Findings) performed crosscoder analysis and causal interventions on Wait tokens in DeepSeek-R1-Distill-Llama-8B (reasoning model), finding features at layer 15 that modulate backtracking and self-reflection. Hwang et al. (arXiv:2601.17421) further analyzed Wait as a token-level signal into reasoning. Both studied reasoning models exclusively; the blind spot occurs in non-reasoning models where Wait's mechanism is likely distinct. **Contextual knowledge suppression — sycophancy circuits**: Wang et al. (arXiv:2508.02087, AAAI 2026 main) discovered a two-stage sycophancy circuit using logit-lens and activation patching — first-person framing creates stronger representational perturbations than third-person, suppressing factual knowledge. This is structurally isomorphic to the blind spot: a contextual signal (self-authorship vs. user opinion) suppresses a correct internal signal (error correction vs. factual knowledge). Zhang & Chen (arXiv:2601.11563) independently proposed a 'Signal Competition Mechanism' unifying sycophancy and conformity through a shared 'compliance subspace' — a convergent geometric manifold where social-emotional signals suppress information-calibration signals via a deterministic linear boundary. Their 'Transparency-Truth Gap' (internal confidence is permeable under pressure) parallels the blind spot's knowledge-action gap. Our work tests whether self-authorship constitutes a third signal type competing in this same subspace, or whether non-social contextual overrides operate through distinct geometry. **Sycophancy decomposition**: Vennemeyer et al. (arXiv:2509.21305, ICLR 2026) decompose sycophancy into sycophantic agreement (SYA) and sycophantic praise (SYPR), contrasting both with genuine agreement (GA). Using difference-in-means directions, activation additions, and subspace geometry across Qwen3-30B/4B, LLaMA-3.1-8B/3.3-70B, and GPT-OSS-20B, they show these three behaviors are encoded along distinct linear directions, each independently amplifiable or suppressible (selectivity ratios up to 36.8x), with SYA and GA highly aligned in early layers (cosine ~0.99 at L2-10) but diverging sharply in mid-to-late layers (~0.07 by L25), while SYPR remains nearly orthogonal to both throughout (cosine < 0.2). This decomposition is critical for our unified-mechanism hypothesis: sycophantic agreement — not sycophantic praise — is the structural analogue of blind-spot suppression, as both involve overriding correct outputs due to contextual signals. Our Phase 3 tests must compare the blind-spot authorship direction specifically against the SYA direction, not a monolithic 'sycophancy' direction. **Sycophancy neuron isolation**: O'Brien et al. (arXiv:2601.18939, NeurIPS 2025 Workshop) used Gemma-Scope SAEs with linear probes to isolate the 3% of MLP neurons most responsible for sycophancy in Gemma-2-2B/9B, then applied gradient masking for surgical correction. Their SAE-to-probe-to-neuron pipeline is directly applicable to our Phase 3 — we can identify blind-spot-responsible neurons and test their overlap with sycophancy neurons as a quantitative measure of circuit sharing. Genadi et al. (arXiv:2601.16644) found sycophancy signals are most linearly separable in middle-layer attention heads and that the sycophancy direction is geometrically distinct from the 'truthful' direction, suggesting separate mechanisms — relevant for testing whether the blind-spot direction aligns with either. **Contextual override geometry — Orthogonal Interference**: Zhang & Lin (arXiv:2602.04918) performed layer-wise geometric analysis of how in-context signals override parametric knowledge in Llama-3.1-8B, Qwen-3-4B, and GLM-4-9B. By decomposing residual stream updates into radial (norm-based) and angular (cosine-based) components, they discovered 'Orthogonal Interference' — conflicting context injects a steering vector quasi-orthogonal to the ground-truth direction, effectively rotating the hidden state representation rather than diluting its magnitude. Two of three models maintained stable residual norms despite performance degradation, demonstrating that compliance occurs through geometric displacement ('simulated adoption') rather than signal suppression. This directly informs our Phase 3: the blind-spot authorship signal may suppress error correction not by reducing the correction signal's magnitude but by rotating it away from the correct unembedding direction — a mechanism we can test by decomposing the blind-spot effect into angular versus radial components. **Knowledge-action gap**: Basu et al. (arXiv:2603.18353) showed all four mechanistic intervention paradigms fail to correct errors despite 98.2% AUROC probes — concept bottleneck steering, SAE feature steering, logit-lens patching, and truthfulness vector steering all leave the gap substantially unbridged. This establishes that the blind spot cannot be 'fixed' by naive activation steering but makes the mechanistic explanation of WHY more urgent — and the Orthogonal Interference finding suggests a possible explanation: if the suppression operates via angular rotation rather than magnitude reduction, scalar-magnitude-based interventions (which attempt to amplify the correct signal) would be ineffective because the signal's magnitude is already intact; it is the direction that has been displaced. **Error decomposition**: Li (arXiv:2601.00828) decomposes self-correction into detection, localization, and correction, showing these are independent capabilities — the Error Depth Hypothesis posits stronger models make fewer but deeper errors. This challenges the assumption that finding an 'own-output detection circuit' will explain correction failure; the suppression may act on the correction pathway independent of detection. **Role-token confounds**: Ye et al. (arXiv:2603.12277) demonstrate that in chat-formatted models, role tags and content style are 'perfectly correlated,' and probes trained on role-labeled data learn the confound rather than the underlying mechanism. Their 'CoT Forgery' attack achieves 60% success by injecting fabricated reasoning that models mistake for their own thoughts, demonstrating that role confusion is exploitable and that models infer text source from content style rather than role markers. They recommend using identical content across roles and validating downstream behavioral predictions — principles we adopt in our confound-control design. **Self-awareness and probing**: Gnosis (arXiv:2512.20578) identifies self-awareness circuits in hidden states. Probing for arithmetic errors (arXiv:2507.12379, EMNLP 2025) shows error signals exist in internal activations. **Hypothesis testing for circuits**: Kwon et al. (arXiv:2410.13032) formalize circuit hypothesis testing with mechanism preservation, mechanism localization, and minimality criteria — providing the statistical framework for our falsification tests. **Missing piece**: No work has performed controlled mechanistic comparison of the same error processed under own-output versus external-text attribution with proper confound controls, decomposed by detection/correction pathways, tested whether the suppression circuit is shared with the sycophantic agreement sub-behavior specifically, or characterized the geometric mechanism (orthogonal interference vs. magnitude dilution) underlying the authorship-driven suppression.\n\n## Approach\n**Phase 0 — Confound-Controlled Contrastive Dataset Design.** The original blind-spot measurement (arXiv:2507.02778) confounds authorship attribution with chat-template architecture: the 'own output' condition uses assistant-turn role tokens while the 'external text' condition uses user-turn role tokens, introducing differences in special tokens (<|assistant|> vs <|user|>), attention masking patterns, positional encodings relative to the generation boundary, and prior conversation context. Following the confound-isolation recommendations of Ye et al. (arXiv:2603.12277), and motivated by Wang et al.'s (arXiv:2505.00626, ICML 2025) demonstration that fine-tuned LLMs exploit task-type associations and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, we employ a three-tier experimental design to disentangle the authorship signal from these architectural confounds:\n\n*Tier 1 — Role-Token Replication (behavioral baseline).* We reproduce the Self-Correction Bench setup to confirm the blind spot exists in our three model families under the original framing.\n\n*Tier 2 — Attribution-Only Minimal Pairs (controlling role tokens).* We construct minimal-pair prompts where identical error content appears in the SAME role position (user turn) but with different textual attribution. Example pair: 'Here is YOUR previous response — please review it for errors: [passage]' vs 'Here is a STUDENT's response — please review it for errors: [passage].' Both use identical user-turn role tokens, identical attention masking, and identical positional encoding — only the attribution framing differs. We construct 4 attribution conditions: (a) explicit self-attribution ('your previous response'), (b) explicit other-attribution ('a student wrote'), (c) ambiguous attribution ('the following passage'), and (d) counterfactual self-attribution ('you wrote this, but it was actually written by someone else'). If the blind spot persists in Tier 2 despite identical role tokens, the effect is driven by textual attribution, not architectural confounds. The Wang et al. (ICML 2025) finding that models exploit task-type and positional shortcuts rather than genuine role understanding provides additional justification for this design: even if role tokens were controlled, models might still exploit residual content-style correlates, which our four attribution conditions systematically vary.\n\n*Tier 3 — Self-Authorship Vector Intervention (causal isolation).* Following Ackerman & Panickssery (ICLR 2025), we extract a self-authorship vector from each model using their contrastive methodology with nuisance-vector deconfounding — computing the mean activation difference between self-generated and other-generated texts, then subtracting its projection onto a nuisance vector derived from generic output-bias prompts. We then test: (i) Does adding the self-authorship vector to the external-text condition (Tier 2, other-attributed) reproduce the blind spot at the activation level, without changing any tokens? (ii) Does subtracting the self-authorship vector from the self-attributed condition eliminate the blind spot? This provides causal evidence that the authorship representation — not role tokens or surface framing — drives the suppression. We note Roytburg et al.'s (arXiv:2509.03647, NeurIPS 2025) cautionary finding that self-preference spans multiple or nonlinear directions: while a single self-authorship vector may capture the dominant linear component, we will test for residual effects after vector subtraction and, if present, apply iterative orthogonal projections or nonlinear probes to characterize remaining structure.\n\nThe Tier 1→2→3 progression provides a clean causal chain: Tier 1 replicates the phenomenon, Tier 2 rules out role-token confounds, and Tier 3 isolates the specific internal representation responsible.\n\n**Phase 1 — Activation Collection.** Run three model families with pre-trained SAE suites — Gemma 3 4B/12B with Gemma Scope 2 SAEs, transcoders, and skip-transcoders (via SAELens/Neuronpedia); Llama 3.1 8B with Llama Scope SAEs (32K/128K features, via TransformerLens); and Qwen 3 8B with Qwen-Scope SAEs (64K features across all 36 layers, Top-k=50/100; arXiv:2605.11887) — on all Tier 1, 2, and 3 conditions, caching full residual stream activations, attention maps, and SAE feature activations at every layer.\n\n**Phase 2 — Decomposed Probing.** Following the Error Depth Hypothesis framework (arXiv:2601.00828), train separate layer-wise linear probes for three signals: (a) the own-vs-external condition (where does the model represent authorship?), (b) error detection (does the model internally detect the error in both conditions?), and (c) correction action (does the model activate correction pathways?). The critical test is whether own-output framing suppresses probe (c) without suppressing probe (b) — i.e., the model detects the error but the correction pathway is gated by authorship context. Apply probes to both Tier 1 (role-token-confounded) and Tier 2 (attribution-only) conditions to determine whether the authorship representation is the same across both framings or whether role tokens contribute an additional, independent suppression signal.\n\n**Phase 3 — Circuit Identification via Causal Intervention.** Apply activation patching, steering vectors derived from the own/external contrast, and SAE feature ablation to test whether identified components are necessary and sufficient for blind spot behavior. Specifically test: (i) Can we patch own-output activations with external-text activations at the divergence layer to eliminate the blind spot? (ii) Do Gemma Scope 2 transcoders and skip-transcoders reveal cross-layer propagation paths for the authorship signal? (iii) Does the identified suppression circuit overlap with the sycophantic agreement circuit specifically?\n\n*Geometric mechanism analysis (informed by Orthogonal Interference).* Following Zhang & Lin (arXiv:2602.04918), we decompose the blind-spot effect into radial (norm-based) and angular (cosine-based) components relative to the correct-correction direction in each model's residual stream. This tests a critical mechanistic question: does the authorship signal suppress error correction by reducing the correction signal's magnitude (direct suppression), or by rotating the hidden state away from the correction direction while preserving its magnitude (orthogonal interference / 'simulated adoption')? If the blind spot operates via orthogonal interference — as Zhang & Lin found for in-context knowledge conflicts — this would explain why magnitude-based interventions in the knowledge-action gap literature (arXiv:2603.18353) fail: they attempt to amplify a signal whose magnitude is already intact, but whose direction has been displaced. We measure: (a) the cosine angle between the residual stream under own-output framing and the correct-correction direction, versus under external-text framing; (b) the residual norm change between conditions; (c) layer-wise progression of the angular displacement to identify where the rotation initiates. If the angular component dominates the radial component in explaining the blind-spot effect, this constitutes evidence for an orthogonal-interference mechanism.\n\n*Sycophantic agreement circuit overlap.* We operationalize this overlap test following Vennemeyer et al.'s decomposition (arXiv:2509.21305, ICLR 2026): since sycophancy decomposes into sycophantic agreement (SYA) and sycophantic praise (SYPR) with distinct, independently steerable linear directions, we specifically extract the SYA direction (not a monolithic sycophancy vector) for comparison, as SYA — overriding correct judgments due to contextual signals — is the structural analogue of blind-spot suppression. We adopt their difference-in-means methodology to extract the SYA direction from our three model families, noting their finding that SYA becomes maximally separable from genuine agreement in mid-to-late layers (cosine similarity dropping from ~0.99 at layers 2-10 to ~0.07 by layer 25 in their studied models). Following O'Brien et al.'s SAE-to-probe pipeline (arXiv:2601.18939): we identify the top SAE features and MLP neurons predictive of blind-spot behavior, then compute their overlap with SYA-predictive features from the same models. We also test geometric alignment between the blind-spot authorship direction and the SYA direction (Wang et al., AAAI 2026), the 'compliance subspace' directions (Zhang & Chen, arXiv:2601.11563), and the attention-head sycophancy direction (Genadi et al., arXiv:2601.16644).\n\n**Falsification criteria for the unified 'contextual signal override' hypothesis.** We pre-register three falsification tests following the circuit hypothesis testing framework of Kwon et al. (arXiv:2410.13032), targeting the sycophantic agreement (SYA) sub-behavior specifically as the relevant comparison following Vennemeyer et al.'s decomposition: (F1) *Circuit non-overlap*: If the blind-spot suppression components (layers, attention heads, MLP neurons identified via SAE probing) are architecturally disjoint from SYA circuit components (not sycophantic praise or generic sycophancy), AND cross-circuit patching fails to transfer effects in either direction (patching SYA components does not affect blind-spot behavior, and vice versa), we reject the strong unified hypothesis. (F2) *Geometric non-alignment*: If the authorship-signal direction in activation space has cosine similarity < 0.1 with the SYA-signal direction across all probed layers, and these directions cannot be related by a low-rank linear transformation, this indicates geometrically distinct mechanisms — ruling out even a weak shared-subspace account. Additionally, following Zhang & Lin's Orthogonal Interference framework (arXiv:2602.04918), we test whether both phenomena employ the SAME geometric mechanism type even if their specific directions differ: if SYA operates via orthogonal interference (angular displacement) while the blind spot operates via magnitude dilution (or vice versa), this constitutes evidence for mechanistically distinct processes even if F1 shows some component overlap. We thus decompose both the blind-spot and SYA effects into angular and radial components to enable mechanism-type comparison beyond simple direction alignment. (F3) *Intervention asymmetry*: If steering along the SYA direction does not modulate blind-spot severity (and vice versa) beyond chance, the two phenomena are functionally independent despite surface-level structural similarity. Note: following the decomposition result, we also test SYPR as a negative control — if blind-spot direction overlaps with SYPR (flattery, not override), this would indicate a different mechanism than hypothesized. If all three criteria are met, we conclude the blind spot operates through a distinct suppression mechanism; if none are met, we support the unified account; mixed results map the partial overlap.\n\n**Phase 4 — Wait Token Analysis (Supplementary).** This phase is explicitly secondary to the core Phases 0-3 contribution, included as supplementary analysis if the timeline permits and scoped to the single most discriminating experiment. In non-reasoning models, we test two primary hypotheses: (H1) Wait disrupts the own-output authorship signal, resetting it toward the external-text representation; (H2) Wait activates a correction pathway that bypasses the authorship gate. The discriminating experiment: measure Wait's effect on the authorship probe (Phase 2a) versus the correction-action probe (Phase 2c). If Wait reduces the authorship probe's self-attribution signal → H1 (authorship disruption, analogous to resetting the contextual override). If Wait leaves the authorship probe unchanged but increases the correction probe → H2 (gate bypass, a distinct mechanism). This single paired-probe comparison requires minimal additional compute (rerunning Phase 2 probes on Wait-appended versions of the Tier 2 dataset) while providing mechanistic evidence complementing Troitskii et al.'s reasoning-model findings (arXiv:2510.04128). We do NOT include full circuit mapping for Wait, reserving that for follow-up work.\n\n**Framing note**: Following the knowledge-action gap results (arXiv:2603.18353), we do NOT claim this work will yield mitigation strategies. The contribution is mechanistic explanation: mapping the circuit that causes the blind spot (with proper confound controls), characterizing the geometric mechanism (orthogonal interference vs. magnitude dilution), testing its relationship to sycophantic agreement circuits specifically, and characterizing Wait's probe-level effects in non-reasoning models. Understanding the circuit architecture — including whether the suppression operates via directional rotation rather than magnitude reduction — is a prerequisite for future work on why activation-level interventions fail to bridge the knowledge-action gap.\n\n## Inspiration\nBlind spot finding (64.5% rate, Wait reduces by 89.3%); confound between role tokens and authorship in the original measurement — reinforced by Wang et al.'s (ICML 2025) demonstration that LLMs use shortcuts rather than genuine role understanding — motivating a cleaner experimental design; structural isomorphism between blind spot and sycophantic agreement (not sycophancy broadly) as contextual-signal-override phenomena, now supported by four independent mechanistic studies of sycophancy plus the critical decomposition showing sycophantic agreement and praise are distinct (Vennemeyer et al., ICLR 2026); Orthogonal Interference finding (Zhang & Lin, arXiv:2602.04918) providing a specific geometric hypothesis for how contextual signals override correct representations via rotation rather than suppression; knowledge-action gap negative results motivating mechanistic explanation over intervention — with Orthogonal Interference suggesting why magnitude-based interventions fail; Error Depth Hypothesis motivating decomposed analysis of detection vs. correction pathways; reasoning/non-reasoning gap in Wait token understanding; convergence of pre-trained SAE suites (Gemma Scope 2, Llama Scope, Qwen-Scope) enabling symmetric three-family comparison.\n\n## Key References\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models (NeurIPS 2025 Workshop, arXiv:2507.02778)\n- Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct (ICLR 2025, arXiv:2410.02064)\n- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models (AAAI 2026 main, arXiv:2508.02087)\n- Human-like Social Compliance in Large Language Models: Unifying Sycophancy and Conformity through Signal Competition Dynamics (arXiv:2601.11563)\n- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (NeurIPS 2025 Workshop, arXiv:2601.18939)\n- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644)\n- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (ICLR 2026, arXiv:2509.21305)\n- Simulated Adoption: Decoupling Magnitude and Direction in LLM In-Context Conflict Resolution (arXiv:2602.04918)\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (arXiv:2603.18353)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis (arXiv:2601.00828)\n- Internal States Before Wait Modulate Reasoning Patterns (EMNLP 2025 Findings, arXiv:2510.04128)\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421)\n- Intrinsic Self-Correction in LLMs: Towards Explainable Prompting via Mechanistic Interpretability (AAAI 2026 Deployable AI Workshop, arXiv:2505.11924)\n- Prompt Injection as Role Confusion (arXiv:2603.12277)\n- The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (ICML 2025, arXiv:2505.00626)\n- Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (NeurIPS 2025, arXiv:2509.03647)\n- Hypothesis Testing the Circuit Hypothesis in LLMs (arXiv:2410.13032)\n- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv:2605.11887)\n- Gemma Scope 2: Full-Stack Interpretability Suite for Gemma 3 (Google DeepMind 2025)\n- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv:2410.20526)\n- Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement (ACL 2024, arXiv:2402.11436)\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits [Gnosis] (arXiv:2512.20578)\n- Probing for Arithmetic Errors in Language Models (EMNLP 2025, arXiv:2507.12379)\n- LLM Layers Immediately Correct Each Other (NeurIPS 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '450-650 A100-80GB hours (activation caching for ~2500 contrastive pairs across 3 tiers x 3 model families x all layers, self-authorship vector extraction with nuisance-vector deconfounding, decomposed probing, patching experiments, radial/angular decomposition analysis, SYA direction extraction and comparison, and supplementary Wait analysis)', 'timeline': '12-16 weeks', 'estimated_gpu_cost': '$900-$1300 at ~$2/GPU-hr spot pricing'}\n- **human_in_loop**: {'gpu_hours': '380-550 A100-80GB hours (Claude accelerates Tier 2 minimal-pair construction, probing code, SAE feature comparison across three symmetric suites, SYA direction extraction, and cross-model analysis)', 'timeline': '9-13 weeks', 'claude_api_cost': '$250-$450 (dataset generation including Tier 2 attribution variants, code scaffolding for three SAE suites, results interpretation, paper drafting)', 'estimated_gpu_cost': '$760-$1100'}\n- **auto_research**: {'gpu_hours': '320-480 A100-80GB hours (automated probe sweeps across 3 tiers, systematic patching grid, cross-model SAE feature comparisons, sycophantic agreement overlap quantification, radial/angular decomposition)', 'timeline': '7-10 weeks', 'claude_api_cost': '$450-$750 (experiment orchestration, iterative analysis, automated paper writing)', 'estimated_gpu_cost': '$640-$960', 'speed_bottleneck': \"Sequential activation caching is I/O-bound: each 8B model forward pass with full activation caching for 2K-token sequences takes ~4s on a single A100; parallelism across models helps but each model's layer-wise patching experiments are inherently sequential. The three-tier dataset increases total pairs by ~2.5x relative to Tier 1 alone, partially offset by the symmetric SAE tooling (no custom SAE training needed for any model family).\"}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:27:19.163Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:27:19.163Z",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:27:19.177Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage
```

---

## ⚠️ 致命前置问题：投稿 CoRL 2026 venue 完全不匹配

在进入 idea 质量评估之前，必须先指出一个**致命的 venue mismatch 问题**：

CoRL (Conference on Robot Learning) 2026 的 [Call for Papers](https://www.corl.org/contributions/call-for-papers) 明确限定投稿范围为 "significant original research at the intersection of robotics and machine learning"，涵盖的主题包括 robot perception, manipulation, locomotion, sim-to-real transfer, reinforcement learning for physical robots 等。官网明确写道：**"Submissions without a robotics focus will be returned without review."**

本 proposal 是一篇纯粹的 **LLM mechanistic interpretability** 论文，研究 LLM 自我纠错的盲区与谄媚电路的重叠。**没有任何机器人学内容**——没有 embodied agent、没有 robot control、没有 sim-to-real、没有 manipulation。投稿 CoRL **会被 desk reject**，概率接近 100%。

合理的目标 venue 应该是 **NeurIPS / ICML / ICLR 主会**，或 **EMNLP / ACL**（如果定位为 NLP venue）。以下评估假设投稿目标为这些 NLP/ML 主会（如 ICLR 2026 或 NeurIPS 2026），评估 idea 的内在质量。

---

```
【领域调研】:
```

- **[Self-Correction Bench](https://arxiv.org/abs/2507.02778)** (NeurIPS 2025 Workshop): 首次量化了 14 个非推理模型上平均 64.5% 的自我纠错盲区，发现 "Wait" token 可降低 89.3%。仅提供训练数据假说，无机制解释。这是本 proposal 的核心现象来源。**注意：这是 workshop paper，非主会**，说明该现象的学术重要性尚未经过主会级别的同行评审确认。

- **[Ackerman & Panickssery - Self-Authorship Vector](https://arxiv.org/abs/2410.02064)** (ICLR 2025 main): 在 Llama3-8b-Instruct 中发现了 self-authorship vector，可通过 activation steering 控制模型的自我归因感知。方法论（nuisance-vector deconfounding）确实存在且有效。这是 proposal 的 Tier 3 干预的直接基础，reference 描述准确。

- **[Vennemeyer et al. - Sycophancy Decomposition](https://arxiv.org/abs/2509.21305)** (ICLR 2026): 将谄媚分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，证明它们是独立可控的线性方向。该论文确实已被 ICLR 2026 接收，proposal 中的描述（selectivity ratios, cosine similarity 变化趋势）与原文一致。

- **[Wang et al. - Sycophancy Circuit](https://arxiv.org/abs/2508.02087)** (AAAI 2026 main): 通过 logit-lens 和 activation patching 发现谄媚的两阶段电路，第一人称提示比第三人称引发更强的表征扰动。论文确实存在且已在 AAAI 2026 发表。

- **[Zhang & Lin - Orthogonal Interference / Simulated Adoption](https://arxiv.org/abs/2602.04918)**: 发现上下文信号通过准正交旋转（而非幅度稀释）覆盖参数知识。尚未正式发表（arXiv preprint），但分析框架合理。

- **[Basu et al. - Knowledge-Action Gap](https://arxiv.org/abs/2603.18353)**: 展示四种机制干预方法尽管内部探针 AUROC 达 98.2% 仍无法纠正错误。是近期 preprint，尚未正式发表。

- **[O'Brien et al. - Sycophancy Neurons](https://arxiv.org/abs/2601.18939)** (NeurIPS 2025 Workshop): 使用 Gemma-Scope SAEs 分离出 3% 的 MLP 神经元负责谄媚。Workshop paper。

- **[Qwen-Scope](https://arxiv.org/abs/2605.11887)** (May 2026): 确实已发布，提供 Qwen3/3.5 的 SAE suite。Reference 准确。

- **调研总结**: 这个领域正处于"行为现象已观察到、机制工具箱已成熟、但两者尚未连接"的阶段。Sycophancy 的机制研究在 2025-2026 爆发（至少 5 篇独立工作），self-correction blind spot 则仅有一篇 workshop paper 建立。**目前没有发现任何工作直接做了"self-correction blind spot 的机制解释"或"blind spot 与 sycophancy 电路的对比"**——这个 gap 确实存在。但该 gap 的重要性取决于 blind spot 本身作为研究对象的分量（目前仅 workshop paper 级别的支撑）。

---

```
【Trivial Alternative 检验】:
```

**存在部分 trivial alternative 威胁，但 proposal 的增量价值有合理辩护。**

最简单的替代方案是：**直接做线性探针（linear probing）对比 own-output vs external-text 的内部表征差异**——不需要三层 confound control、不需要 SAE feature overlap analysis、不需要 geometric decomposition。一个简单的 probing study 就能给出"模型在哪些层区分了 own vs external"的初步答案。

Proposal 对此的增量价值在于：
1. **Confound control (Tier 2)**：Ye et al. 和 Wang et al. (ICML 2025) 确实指出了 role-token confound 的真实性，所以仅靠 role-token-based 的对比确实有方法论缺陷。Tier 2 的 attribution-only minimal pair 设计是实质性的方法论改进。
2. **Detection vs Correction 的分解**：这比简单 probing 有更强的解释力。
3. **与 SYA 电路的定量比较**：这是核心 novelty claim，简单 probing 做不到。

但要注意：**如果最终发现 blind spot 的机制就是"模型在 assistant turn 里更倾向于保持连贯性"这样一个直观解释**，那么整个精密的 confound-control + geometric analysis 工程量相对于所得洞察就显得过重了。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链中有 **三个关键未经验证的假设**：

1. **"Blind spot 是一个稳健的、跨模型的现象"假设**：64.5% 这个数字来自 Self-Correction Bench 一篇 workshop paper，仅测试了 14 个非推理模型。该现象是否在更新的模型（特别是 2026 年的 Gemma 3、Qwen 3）上依然成立？如果 Tier 1 复现失败（blind spot 已被新模型的训练解决），整个研究的基础就不存在了。Proposal 将此作为 Tier 1 但没有讨论复现失败的风险。

2. **"Textual attribution 足以驱动 blind spot"假设**：Tier 2 的设计假设纯文本层面的归因线索（"your previous response" vs "a student wrote"）足以激活与 role-token 相同的 self-authorship 表征。但 Ackerman & Panickssery 的 self-authorship vector 是在 **role-token 存在的自然对话格式** 下提取的。如果模型的 self-authorship 感知主要依赖 role tokens 而非文本线索，Tier 2 可能根本观察不到 blind spot——这不证明"authorship drives the blind spot"，而是证明"textual attribution alone doesn't trigger self-authorship"。这个歧义性在 proposal 中没有充分讨论。

3. **"SYA-blind spot 电路重叠 = 统一机制"的推理有效性**：即使发现 SYA 方向和 blind-spot 方向的 cosine similarity 高，也可能只是因为它们都涉及"override correct output"这一共性——任何涉及抑制正确输出的行为可能都投射到类似的子空间，而不意味着因果上共享一个"contextual override"机制。Circuit overlap 可以是因果共享的，也可以是相关但非因果的。Proposal 的 falsification criteria 虽然设定了阈值，但对这种 confounding 解释讨论不足。

---

```
【3 维度打分】:
```

### 1. Novelty: **中** 

**理由**：
- (+) 在我的调研范围内，**确实没有发现任何工作直接对 self-correction blind spot 进行机制解释**，也没有工作连接 blind spot 和 sycophancy 电路。这个 specific gap 是真实存在的。
- (+) 三层 confound-control 设计（Tier 1-2-3）是方法论上的实质贡献，解决了 Ye et al. (arXiv:2603.12277) 和 Wang et al. (ICML 2025, arXiv:2505.00626) 指出的 role-token confound。
- (+) 将 Orthogonal Interference 框架 (Zhang & Lin, arXiv:2602.04918) 应用于解释 knowledge-action gap 中干预失败的原因是一个合理的新连接。
- (−) 但核心研究范式——"用 activation patching + SAE feature analysis + linear probing 解释某个 LLM 行为 X"——在 2025-2026 年已经是 **标准方法论**。Wang et al. (AAAI 2026)、Vennemeyer et al. (ICLR 2026)、O'Brien et al. (NeurIPS 2025 Workshop)、Zhang & Chen (arXiv:2601.11563) 都在做同样范式的工作，只是应用于不同的行为。本 proposal 是将这套工具箱 **应用** 到一个新对象（blind spot），而不是发明新工具。
- (−) 核心假说——"blind spot 与 sycophantic agreement 共享电路"——考虑到 proposal 自己详细阐述的结构同构性（contextual signal override），这个假说 **非常自然/可预测**。如果验证为正，审稿人大概率会说 "I would have guessed this given the clear structural analogy the authors themselves describe."  如果被否证，论文的叙事框架反而更有趣（"surprisingly, they are distinct"），但 proposal 的 framing 偏向验证而非否证。

### 2. Significance: **中偏弱**

**理由**：
- (+) 理解 LLM 为何不能纠正自己的错误确实是一个有实际意义的问题——这直接关系到 self-refinement pipeline 的可靠性。
- (+) 如果 Orthogonal Interference 机制被确认，这为理解 "为什么 magnitude-based activation steering 不 work" 提供了一个有解释力的框架，对整个 mech-interp 社区有价值。
- (−) **Proposal 明确声明不产出 mitigation 方案** ("we do NOT claim this work will yield mitigation strategies")。这意味着论文的贡献纯粹是描述性/解释性的。在一个日益强调 "actionable interpretability" 的社区（参见 Basu et al. 的标题 "Interpretability without Actionability" 本身就是对纯解释性工作的批评），一个纯 "map the circuit" 的论文需要更强的 insight 才能获得认可。
- (−) Blind spot 现象本身的学术地位仍不牢固——来自 **一篇 NeurIPS Workshop paper**（非主会），且该数字（64.5%）尚未被独立复现或在主会级别确认。在此基础上建立整个机制研究，存在"在沙上建塔"的风险。
- (−) 即使所有结果都如 proposal 预期，最终产出是："我们发现 blind spot 的确是通过正交旋转（而非幅度抑制）抑制了 correction pathway（但不影响 detection），且其电路与 SYA 有 X% 重叠。" 这是一个 **clean but incremental** 的结论，不太可能改变该领域的研究方向。

### 3. Related Work: **强**

**理由**：
- 覆盖极其全面：proposal 引用了 20+ 篇高度相关的论文，覆盖了 blind spot 文档 (arXiv:2507.02778)、self-authorship detection (Ackerman & Panickssery, ICLR 2025)、sycophancy 机制的所有重要工作 (Wang et al. AAAI 2026; Vennemeyer et al. ICLR 2026; O'Brien et al.; Zhang & Chen; Genadi et al.)、knowledge-action gap (arXiv:2603.18353)、error decomposition (arXiv:2601.00828)、role-token confounds (Ye et al.; Wang et al. ICML 2025)、Wait token (Troitskii et al. EMNLP 2025; Hwang et al.)。
- 经过我的调研验证，**引用的论文基本都真实存在，venue 和核心描述准确**（Qwen-Scope arXiv:2605.11887 确认存在；Vennemeyer et al. ICLR 2026 确认被接收）。
- 差异化定位清晰：每篇 related work 都说明了与 proposal 的区别和本工作如何利用其方法论或发现。
- 唯一的小遗漏：Anthropic 2025 年的 circuit tracing work on Claude 3.5 Haiku 在 mech-interp 方法论层面可能相关但未被引用，不过这不构成实质性缺陷。

---

```
【概率估计】: [20% - 32%] 中位 25%
```

**注意：上述概率是针对 NLP/ML 主会（如 ICLR/NeurIPS/ICML）的估计。如果投稿 CoRL 2026，概率接近 0%（desk reject）。**

```
【估计理由】:
```

从 3 维度到概率的推理：

- **Related Work = 强**：这保证了项目的下限——即使 idea 本身只是 average，扎实的 related work 覆盖意味着审稿人不太可能以"miss important prior work"为由拒稿。
- **Novelty = 中**：这决定了项目的天花板。核心贡献是"将已有方法论工具箱应用到一个新的研究对象并测试一个自然假说"。这在顶会上是 borderline——取决于审稿人是否觉得 blind spot 值得单独研究、以及结果是否足够 surprising。**Novelty 是限制上界的维度**。
- **Significance = 中偏弱**：这进一步压低了概率。纯解释性贡献、无 mitigation、基础现象仅有 workshop paper 级别的支撑——这些因素叠加使得审稿人可能质疑 "so what?"

综合判断：idea 方向正确、有真实的 gap、方法论设计严谨，但 **核心发现无论是 positive（电路共享→"I would have guessed this"）还是 negative（电路不共享→叙事框架弱化），都不太可能让审稿人感到 surprising**。这将其锚定在 25-35% 区间的下端。

```
【主要风险】:
```

1. **"Expected Result" 风险**：Proposal 自己花了大量篇幅论证 blind spot 和 SYA 的结构同构性，使得"电路共享"的结果变得高度可预测。如果核心假说被验证，审稿人可能评价为 "confirming the obvious structural analogy with expensive experiments"。这是 idea 层面最大的风险——不是方法不对，而是 insight 不够 surprising。

2. **"基础现象不够稳固" 风险**：整个研究建立在一个 workshop paper 报告的 64.5% blind spot rate 上。如果 Tier 1 复现发现新模型（Gemma 3、Qwen 3）的 blind spot 已显著降低（这些模型可能已通过更好的 RLHF 缓解了此问题），则研究的动机基础将被动摇。审稿人可能质疑：如果最新模型已经不太有这个问题了，为什么还要花大量资源去解释它？

---

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [Ackerman & Panickssery - Self-Authorship Vector (ICLR 2025)](https://arxiv.org/abs/2410.02064)
- [Vennemeyer et al. - Sycophancy Decomposition (ICLR 2026)](https://arxiv.org/abs/2509.21305)
- [Wang et al. - Sycophancy Circuit (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40645)
- [Zhang & Lin - Orthogonal Interference](https://arxiv.org/abs/2602.04918)
- [Basu et al. - Knowledge-Action Gap](https://arxiv.org/abs/2603.18353)
- [O'Brien et al. - Sycophancy Neurons](https://arxiv.org/abs/2601.18939)
- [Qwen-Scope (arXiv:2605.11887)](https://arxiv.org/abs/2605.11887)
- [Ye et al. - Role-Token Confounds](https://arxiv.org/abs/2603.12277)
- [Wang et al. - Role Learning Shortcuts (ICML 2025)](https://arxiv.org/abs/2505.00626)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile my thorough assessment.

---

```
【阶段】: Triage

⚠️ 致命问题预警：严重的投稿会议不匹配 ⚠️

在进入常规 rubric 之前，必须首先指出：CoRL 2026（Conference on Robot Learning）
明确声明 "submissions without a robotics focus will be returned without review"
（https://www.corl.org/contributions/call-for-papers）。
本 proposal 是纯粹的 LLM mechanistic interpretability 研究——自纠错盲区的
电路级机制分析、sycophancy 电路重叠测试、SAE 特征分析——与机器人学习完全无关。
投稿 CoRL 主会将会被直接 desk reject，无论 idea 质量如何。
适合的投稿目标：NeurIPS / ICML / ICLR 主会，或 EMNLP/ACL 的 interpretability track。

以下评估假设投稿至适当的 ML/NLP 顶会（如 NeurIPS/ICLR），评价 idea 本身的质量。


【领域调研】:

- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778) (NeurIPS 2025 Workshop): 
  文档化了 64.5% 的自纠错盲区现象，发现 Wait token 可降低 89.3%。但仅提出
  training-data 假说，未做任何 mechanistic analysis。原始实验设计中 role-token 
  与 authorship 的 confound 确实存在（own-output 使用 assistant turn，external 
  使用 user turn）。论文真实存在，描述准确。

- [Ackerman & Panickssery (arXiv:2410.02064)](https://openreview.net/forum?id=wWnsoLhHwt) (ICLR 2025 主会): 
  在 Llama3-8b-Instruct 中发现 self-authorship vector，证明可因果控制模型的
  自我作者认知。提供了 nuisance-vector deconfounding 方法论。论文真实存在，
  是本 proposal Tier 3 的核心工具。

- [Vennemeyer et al. (arXiv:2509.21305)](https://openreview.net/forum?id=d24zTCznJu) (ICLR 2026): 
  将 sycophancy 分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，
  证明二者是独立可操控的线性方向。SYA 与 genuine agreement 在中后层急剧分离
  （cosine 从 ~0.99 降至 ~0.07）。论文真实存在，描述准确。这是 proposal 
  unified-mechanism 假说的关键依据。

- [Zhang & Lin (arXiv:2602.04918)](https://arxiv.org/abs/2602.04918) (preprint 2026): 
  "Simulated Adoption" — 发现 in-context 信号通过准正交旋转（而非幅度稀释）
  覆盖参数知识。论文真实存在，proposal 对其描述准确。

- [Basu et al. (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353) (preprint 2026): 
  "Interpretability without Actionability" — 四种 mechanistic 干预范式均无法弥合
  knowledge-action gap，尽管探针达到 98.2% AUROC。论文真实存在。这为本 proposal 
  的"解释而非修复"定位提供了合理性。

- [Wang et al. (arXiv:2508.02087)](https://arxiv.org/abs/2508.02087) (AAAI 2026): 
  Sycophancy 的两阶段抑制电路，first-person framing 产生更强的表征扰动。
  与 proposal 描述一致。

- [O'Brien et al. (arXiv:2601.18939)](https://arxiv.org/abs/2601.18939) (NeurIPS 2025 Workshop): 
  用 Gemma-Scope SAE + linear probes 定位 sycophancy 的 3% 关键 MLP 神经元。
  Pipeline 可直接复用。

- [Sparse Activation Fusion for sycophancy mitigation](https://openreview.net/forum?id=BCS7HHInC2) (2025-2026): 
  动态减去 user-induced bias，将 sycophancy 从 63% 降至 39%。Proposal 未引用此工作，
  可能是一个 related work 遗漏。

- [Roytburg et al. (arXiv:2509.03647)](https://arxiv.org/abs/2509.03647) (NeurIPS 2025): 
  Self-preference 跨多个非线性方向，单一 steering vector 不稳定。
  Proposal 正确引用并将此作为多方法动机。

- 调研总结: 该领域呈现"工具就位、空白尚存"的格局。Sycophancy 的 mechanistic 
  分析已有 5+ 篇独立工作完成不同侧面的映射；self-authorship vector 已被 ICLR 2025 
  验证；SAE 工具链（Gemma Scope 2, Llama Scope, Qwen-Scope）已覆盖三大模型族。
  但**尚无任何工作**对 self-correction blind spot 做过控制混淆的 mechanistic 分析，
  更无人测试其与 sycophantic agreement 的电路重叠。Proposal 确实填补了一个真实空白。


【Trivial Alternative 检验】:

存在部分 trivial alternative 威胁，但不致命：

1. **简化版 probing study**: 可以仅在 1 个模型上做 Tier 1+2 的行为实验 + 基础 
   linear probe，不做 circuit mapping / geometric decomposition / cross-model 
   comparison，就能回答"是 role token 还是 attribution 驱动盲区"这个核心问题。
   这个简化版成本极低（~50 GPU-hours），但只回答了 WHAT 而不是 WHY/HOW。

2. **直接迁移 Ackerman 的 self-authorship vector 做因果测试**: 仅用 Tier 3 
   的 vector addition/subtraction 就能获得因果证据，无需 SAE 分析或电路映射。
   这是一个 ~20 GPU-hours 的实验，可能就能回答"authorship representation 
   因果驱动盲区"。

增量价值在于: (a) confound-control 的三层设计是方法论贡献，超越简单 probing；
(b) sycophancy 电路重叠测试是独立的科学问题，trivial probe 无法回答；
(c) geometric mechanism (orthogonal interference vs magnitude dilution) 
提供对 knowledge-action gap 失败原因的解释性假设。

**结论**: 核心问题的最简版本确实可以用更低成本部分回答，但 proposal 的完整设计
在深度和广度上有实质增量。风险在于审稿人可能认为"简化版就够了"。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"Blind spot ≈ sycophantic agreement" 的结构同构假说**: 这是整个 proposal 
   的核心赌注。虽然表面类比合理（contextual signal 抑制 correct behavior），
   但 blind spot 可能通过完全不同的机制运作——例如 self-consistency bias（模型
   倾向于保持输出一致性）、next-token prediction 的自回归惯性、或更简单的
   surface-level heuristic。Proposal 设计了 falsification criteria，但如果
   F1-F3 都 reject，结果是一个 negative finding（"两个现象不共享电路"），
   这在审稿中价值争议较大。

2. **Self-authorship vector 跨模型泛化**: Ackerman 的 vector 仅在 Llama3-8b-Instruct 
   上验证。假设它可以在 Gemma 3 和 Qwen 3 中被类似提取是合理的但未经验证。
   如果某些模型没有清晰的线性 self-authorship 表征，Tier 3 将失效。

3. **"Role token confound 是重要的"**: 虽然 Ye et al. 和 Wang et al. 提供了
   间接证据，但原始 blind-spot 论文的 64.5% 效果是否主要由 role token 驱动
   还是由 textual attribution 驱动，是一个实证问题。如果 Tier 2 显示效果大幅
   减弱（confound 是主要 driver），那么"authorship attribution 驱动盲区"
   的核心叙事就被削弱了——虽然这本身是有价值的发现，但会让后续 Phase 2-4 
   的全部设计失去基础。

4. **Geometric decomposition 的可解释性**: 假设 angular vs radial decomposition 
   能提供清晰的 mechanistic 解释。Zhang & Lin 的方法在 knowledge conflict 上
   有效，但 self-correction blind spot 可能涉及更复杂的非线性动态。


【3 维度打分】:

1. Novelty: 【中】
   理由: 
   - 确认空白: 调研证实尚无工作对 self-correction blind spot 做过 confound-controlled 
     mechanistic analysis，也无人测试其与 sycophantic agreement 的电路重叠。
     这是一个真实的未填补空白。
   - 但方法论不新: 每个单独组件——self-authorship vector extraction (Ackerman, 
     ICLR 2025), SYA direction extraction (Vennemeyer, ICLR 2026), SAE-to-probe 
     pipeline (O'Brien, 2025), geometric decomposition (Zhang & Lin, 2026), 
     Error Depth decomposition (Li, 2026) ——都是直接复用已有工具。创新在于
     **组合应用到新现象**，而非方法创新。
   - 核心假说（blind spot ≈ SYA 的 contextual override）虽然有趣但不算反直觉——
     任何了解 sycophancy 文献的研究者看到 blind spot 后都可能产生这个类比。
   - Confound-control 的三层设计（Tier 1-2-3）是真正的方法论贡献，
     是 proposal 中最有原创性的部分。

2. Significance: 【中】
   理由:
   - Self-correction 是 LLM 安全和可靠性的重要问题，理解盲区的 mechanistic 
     原因有学术价值。
   - 但 proposal 明确声明不追求 mitigation（"we do NOT claim this work will yield 
     mitigation strategies"）。这在 Basu et al. (arXiv:2603.18353) 已经证明
     interventions fail 的背景下是诚实的，但也限制了实际影响力。
   - 纯 mechanistic explanation 的影响力天花板低于"解释+修复"的工作。
     审稿人常见评论: "interesting analysis but what can we do with this?"
   - 如果 unified-mechanism 假说被证实，其理论意义大于实践意义——
     它统一了 sycophancy 和 self-correction 的理解，但不直接帮助解决任何问题。
   - 如果假说被否定（F1-F3 falsification），negative result 的价值在
     top venue 上争议较大。

3. Related Work: 【强】
   理由:
   - 调研中引用的所有关键论文（Ackerman ICLR 2025, Vennemeyer ICLR 2026, 
     Zhang & Lin 2026, Basu 2026, Wang AAAI 2026, O'Brien 2025, Roytburg 
     NeurIPS 2025）均经查证真实存在且描述准确。
   - 覆盖异常全面: sycophancy mechanistic 文献（5+ 篇）、self-authorship 检测、
     knowledge-action gap、error decomposition、role-token confound、
     Wait token 分析均有覆盖。
   - 差异化定位清晰: 明确标注了"Missing piece"并准确描述了 gap。
   - 对 cautionary findings（如 Roytburg 的"多方向/非线性"警告）的处理诚实，
     并转化为方法论动机。
   - 可能遗漏: Sparse Activation Fusion (SAF) for sycophancy mitigation 
     未被引用，但对 proposal 核心论点影响不大。


【概率估计】: 
   - 投稿 CoRL 2026: 0-2%（desk reject，venue 完全不匹配）
   - 若投稿至适当 venue（NeurIPS/ICLR 主会）: [22% - 32%] 中位 27%

【估计理由】: 
   Idea 处于 rubric 的"25-35%"区间——方向正确，有真实的 novelty delta
  （confound-controlled mechanistic analysis of blind spot + sycophancy overlap 
   test 是未被做过的工作），但核心发现 if positive 不够 surprising。
   具体而言:
   
   - Related Work（强）确保了定位清晰，不会因 related work 不足被拒。
   - Novelty（中）是主要限制因素: 方法论上是已有工具的组合应用，
     核心假说（contextual override）是"reasonable guess"而非"surprising insight"。
     审稿人可能评价"competent engineering of existing mech-interp tools 
     applied to a specific phenomenon"。
   - Significance（中）是次要限制: 纯 explanation without mitigation 
     在 top venue 上需要 explanation 本身足够 surprising 或 general 才能弥补
     缺乏 actionability 的短板。本 proposal 的 explanation 如果被证实，
     其 generality（unified contextual override across sycophancy and self-correction）
     有一定理论价值，但不足以进入"surprising"区间。
   
   上界（32%）对应: Tier 2 confound-control 设计被视为重要方法论贡献 + 
   unified mechanism 假说被证实且 geometric analysis 提供了对 knowledge-action 
   gap 失败原因的首个解释。
   下界（22%）对应: 审稿人认为这是 incremental application of existing tools + 
   pure explanation without actionability。

【主要风险】:
1. **"Competent but not surprising" 风险**: 核心假说（blind spot ≈ SYA contextual 
   override）如果被证实，审稿人很可能说 "this is what I would have expected" — 
   因为 sycophancy 和 self-correction blind spot 的结构类比已经在 proposal 
   本身的 framing 中显而易见。真正 surprising 的结果应该是 reviewer 事先
   *不会猜到*的，但这个假说恰恰是"一旦看到两个现象的并列描述就自然想到的"。
   
2. **"Explanation without actionability" 在 top venue 的接受度风险**: 
   Proposal 诚实地声明不追求 mitigation，这在 workshop paper 级别完全可以，
   但在 top venue 主会上，纯 mechanistic explanation 需要提供足够 general 
   或 surprising 的 insight 来证明其独立价值。在 arXiv:2603.18353 已经证明
   interventions fail 的语境下，"解释为什么 fail"是有价值的 follow-up，
   但也容易被视为该工作的 incremental extension。
```

---

**⚠️ 关键提醒：投稿目标不匹配**

CoRL 2026 明确要求 robotics focus，声明"submissions without a robotics focus will be returned without review"。本 proposal 是纯 LLM mechanistic interpretability 研究，与机器人学习完全无关。**无论 idea 质量如何，投稿 CoRL 将导致 desk reject。**

建议投稿目标：
- **NeurIPS 2026 主会**（interpretability track）
- **ICLR 2027**
- **ICML 2026**（如 deadline 未过）
- **EMNLP 2026**（如果定位为 NLP-focused interpretability）

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/abs/2507.02778)
- [Ackerman & Panickssery - Self-Generated-Text Recognition (ICLR 2025)](https://openreview.net/forum?id=wWnsoLhHwt)
- [Vennemeyer et al. - Sycophancy Is Not One Thing (ICLR 2026)](https://openreview.net/forum?id=d24zTCznJu)
- [Zhang & Lin - Simulated Adoption (arXiv:2602.04918)](https://arxiv.org/abs/2602.04918)
- [Basu et al. - Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353)
- [O'Brien et al. - A Few Bad Neurons (arXiv:2601.18939)](https://arxiv.org/abs/2601.18939)
- [Roytburg et al. - Breaking the Mirror (arXiv:2509.03647)](https://arxiv.org/abs/2509.03647)
- [Wang et al. - Sycophancy Origins (arXiv:2508.02087)](https://arxiv.org/abs/2508.02087)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Sparse Activation Fusion for Sycophancy](https://openreview.net/forum?id=BCS7HHInC2)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive assessment. Let me compile my findings.

---

```
【阶段】: Triage

【致命前置问题 — 投稿会议匹配性】:
⚠️ CoRL (Conference on Robot Learning) 是一个聚焦机器人学习的会议，核心议题包括 imitation learning、reinforcement learning for robots、sim-to-real transfer、manipulation、locomotion、robot perception 等。本 proposal 是一项关于 LLM 内部机制可解释性的研究（self-correction blind spot 的 circuit-level 成因分析），与机器人学习完全无关。投稿 CoRL 主会几乎必然被 desk reject。

建议投稿会议：NeurIPS / ICML / ICLR 主会，或 ACL / EMNLP（如果偏 NLP 社区）。以下评估假设投稿至适配的 ML/NLP 顶会（如 NeurIPS/ICLR），而非 CoRL。

---

【领域调研】:

- **Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop)**: 原始行为发现论文，文档了 14 个非推理模型平均 64.5% 的 blind spot 率以及 Wait token 的 89.3% 缓解效果。提供了训练数据假说但无机制解释。该论文确实存在且描述准确。但注意这只是 NeurIPS **Workshop** 论文，非主会。

- **Ackerman & Panickssery (arXiv:2410.02064, ICLR 2025 主会)**: 确认存在，发现了 Llama3-8b-Instruct 中的 self-authorship vector，可以因果控制模型的自我归因感知。论文已被 ICLR 2025 主会接收。这是本 proposal 的关键方法学基础。

- **Vennemeyer et al. (arXiv:2509.21305, ICLR 2026)**: 确认存在且已被接收。将 sycophancy 分解为 sycophantic agreement (SYA) 和 sycophantic praise (SYPR)，证明它们是独立可操控的线性方向。selectivity ratios 最高达 36.8x。这为 proposal 的 unified mechanism 假说提供了精确的比较对象。

- **Wang et al. (arXiv:2508.02087, AAAI 2026)**: 确认存在。发现了两阶段 sycophancy circuit：第一人称 framing 在中后层(~layer 19)产生更强的表征扰动，抑制事实知识。结构上与 blind spot 的 contextual override 类似。

- **Zhang & Lin (arXiv:2602.04918)**: 确认存在。发现 in-context conflict 通过 "Orthogonal Interference"（准正交几何旋转而非幅度稀释）覆盖参数知识。在 Llama-3.1-8B、Qwen-3-4B、GLM-4-9B 上验证。

- **Basu et al. (arXiv:2603.18353)**: 确认存在。Knowledge-action gap 论文，四种 mechanistic intervention 范式均无法弥合 gap（尽管 probe AUROC 达 98.2%）。为"理解 WHY"提供了动机。

- **Qwen-Scope (arXiv:2605.11887, May 2026)**: 确认存在，为 Qwen3/3.5 系列提供了预训练 SAE 套件。这使三模型家族对称比较成为可能。

- **O'Brien et al. (arXiv:2601.18939, NeurIPS 2025 Workshop)**: 使用 Gemma-Scope SAE 隔离 sycophancy 神经元（前 3% MLP 神经元），提供了 SAE-to-probe-to-neuron pipeline。

- **调研总结**: Self-correction blind spot 是 2025 年由一篇 NeurIPS Workshop 论文提出的行为发现。sycophancy 的机制可解释性在 2025-2026 年间快速发展（至少 5 篇独立工作从不同角度进行了 circuit-level 分析）。Self-authorship 的内部表征也已被 ICLR 2025 工作识别。但**尚无工作将这些线索整合起来**——即在控制 confound 的条件下对 blind spot 做 circuit-level 分析，并与 sycophancy 电路比较。这个 gap 是真实的。

---

【Trivial Alternative 检验】:

存在一个更低成本的替代方案值得认真考虑：

1. **纯行为 confound-control 实验（Tier 1+2）**: Proposal 中最有价值的贡献之一是 Tier 2 的 attribution-only minimal pairs 设计（控制 role tokens，只改变文本归因）。这个实验本身只需要推理级别的 GPU 开销（无需缓存全层激活），但已经能回答一个核心问题："blind spot 是由 authorship attribution 驱动的，还是由 role-token 架构差异驱动的？" 这个行为发现如果 robust 到三个模型家族上，本身就有论文级别的价值。

2. **直接用 self-authorship vector 做 steering**: Ackerman & Panickssery 已经提供了 self-authorship vector。直接测试"加/减 self-authorship vector 是否影响 blind spot 严重度"是一个很低成本的实验，且能提供因果证据。

**增量价值判断**: Proposal 的真正增量在于 (a) 完整的 circuit mapping（哪些 layer/head/neuron 负责 suppression），(b) 与 SYA 电路的定量 overlap 测试，(c) 几何机制刻画（orthogonal vs. magnitude）。这些不是 trivial 替代能达到的。但问题是：如果 Tier 2 行为实验就能证明 "attribution drives blind spot"，审稿人可能会问："完整 circuit mapping 的额外洞见是什么？" 如果答案是 "它与 sycophancy 共享电路"，那这个发现 surprising 吗？

---

【前提假设检验】:

核心逻辑链中有以下未经验证的假设：

1. **Self-authorship vector 的跨模型迁移性**: Ackerman & Panickssery 的 self-authorship vector 仅在 Llama3-8b-Instruct 上发现和验证。Proposal 假设类似的 vector 在 Gemma 3 和 Qwen 3 上也能提取出来，且具有相似的因果效力。这一假设未经验证。Roytburg et al. (NeurIPS 2025) 明确警告 self-preference "spans multiple or nonlinear directions"，说明单线性方向可能不够。

2. **Error correction 的线性可分离性假设**: Phase 2 用线性 probe 分别探测 detection 和 correction 信号，假设这些是线性可分的。如果 blind spot 的 suppression 机制是非线性的（如 Roytburg et al. 所暗示），线性 probe 可能无法捕获关键信号。

3. **"结构同构 = 电路共享" 的推断**: Proposal 的核心假说是 blind spot 与 sycophantic agreement 结构同构（contextual signal overrides correct behavior），因此推测它们共享电路。但结构同构是功能描述层面的类比，不一定意味着实现层面（电路层面）的共享。两个功能类似但进化路径不同的行为完全可能用不同电路实现。

4. **Confound 是 "问题" 而非 "本质"**: Tier 2 假设 role-token confound 是需要"排除"的干扰因素。但如果 LLM 的 self-authorship 认知本身就是通过 role tokens 和 attention mask 实现的（这正是 chat 模型训练的方式），那么 role-token 信号可能不是 confound 而是机制本身。Tier 2 在排除 role tokens 后仍然发现 blind spot 是一个 empirical question，结果可能是 "blind spot 在 Tier 2 消失"，这会推翻整个 Phase 2-3 的研究动机。

---

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是"将已有工具（self-authorship vector, SAE, activation patching, 几何分解）应用于一个具体现象（blind spot）并与另一个已被详细研究的现象（sycophancy）做比较"。这是一个 well-motivated 的"连接性"研究，但每个单独组件都有强大的先例：
   - Self-authorship vector → Ackerman & Panickssery (ICLR 2025)
   - Sycophancy circuit mapping → Wang et al. (AAAI 2026), O'Brien et al., Genadi et al., Vennemeyer et al. (ICLR 2026)
   - 几何分解 → Zhang & Lin (arXiv:2602.04918)
   - Detection vs. correction 分离 → Li (arXiv:2601.00828)
   
   Proposal 的方法学贡献（三层 confound control design）是 solid 的，但这是实验设计的严谨性而非概念创新。真正的 novelty delta 在于"整合"——将这些独立的线索串联成一个统一叙事。这有价值，但审稿人可能将其视为 "application of existing mechanistic interpretability tools to a new target phenomenon" 而非 "fundamentally new methodology or insight"。

2. **Significance: 中** — 
   Self-correction blind spot 是一个重要且 practical 的问题——理解为什么 LLM 不能纠正自己的错误对 AI safety 和可靠性有直接影响。但有两个限制因素：
   
   (a) Proposal 明确声明不追求 mitigation（因为 Basu et al. 已证明四种干预范式失败）。纯 mechanistic understanding 论文在主会的接受门槛更高——审稿人会问 "so what do we do with this understanding?"。Orthogonal interference 的发现可能解释为什么 magnitude-based interventions 失败，但 proposal 不承诺提出替代的 directional intervention。
   
   (b) 如果核心发现是 positive（blind spot 与 SYA 共享电路），审稿人很可能会说 "I would have guessed this"——因为两者的结构同构性在论文 framing 中已经非常明显。如果核心发现是 negative（不共享电路），信息量更大但 narrative 更弱。这是一个 dual-outcome 困境，无论哪个结果都难以达到 "surprising" 的标准。
   
   (c) 原始 blind spot 发现来自一篇 NeurIPS Workshop 论文（非主会），说明社区对这个现象的认可度和关注度可能不如 proposal 所暗示的那么高。

3. **Related Work: 强** — 
   Related work 覆盖异常全面且精确。几乎所有 2024-2026 年间与 sycophancy 机制、self-authorship 检测、knowledge-action gap、self-correction 分解相关的工作都被引用和准确定位。特别值得肯定的是：
   - 正确区分了 Vennemeyer et al. 的 SYA vs SYPR 分解
   - 引用了 Roytburg et al. 的 cautionary finding 并据此调整了方法设计
   - 引用了 Wang et al. (ICML 2025) 关于 role-token shortcuts 的发现来支撑 confound control 的必要性
   - 将 Zhang & Lin 的几何框架与 knowledge-action gap 的失败联系起来
   
   唯一的小瑕疵：部分引用（如 arXiv:2603.18353, arXiv:2603.12277）发表于 2026 年 3 月，可能是较新的预印本，其评审状态和社区认可度尚不确定。

---

【概率估计】: [20% - 32%] 中位 25%
（注意：此估计假设投稿至适配的 ML 顶会如 NeurIPS/ICLR。若投稿 CoRL，概率接近 0%——完全的领域不匹配。）

【估计理由】: 
这是一篇 well-crafted 的 mechanistic interpretability 论文 proposal，在实验设计上极其严谨（三层 confound control, pre-registered falsification criteria, 三模型家族对称设计）。但 **idea 的内核是 "applying existing mech-interp toolkit to a new phenomenon + testing a structural analogy"**，这把它定位在 "solid but not surprising" 的区间。

上限被两条维度限制：
1. **Novelty** — 每个方法组件都有强先例，核心创新在于"组合"而非"发明"。
2. **Significance** — 无论 unified mechanism 假说的结果是 positive 还是negative，都不太可能达到 "surprising" 标准。positive 结果验证了一个已经 intuitive 的类比；negative 结果有信息量但弱化了论文的统一叙事。加上明确放弃 mitigation 目标，practical impact 受限。

下限被 **Related Work 的全面性** 和 **confound-control design 的严谨性** 支撑——这些确保了即使 idea 不够 exciting，execution quality 可以 compensate 一部分。

【主要风险】:
1. **"Connecting the dots" ≠ "New dots"**: 审稿人可能认为这是将已有工具（SAE, activation patching, geometric decomposition）应用于一个新目标现象的 "application paper"，而非提出新方法或新理论框架的工作。在 NeurIPS/ICLR 主会，纯 application 的 mech-interp 论文需要特别强的 surprising findings 来补偿。
2. **Dual-outcome 困境下的 "so what" 问题**: 如果审稿人问 "假设你完美地 map 了 circuit，我们下一步能做什么？"，proposal 的回答是 "understand WHY interventions fail"。但 understanding WHY 不 bridge 到 actionable mitigation，这在 2026 年 safety-driven 的审稿氛围中可能不够。
```

Sources:
- [Self-Correction Bench (arXiv:2507.02778)](https://arxiv.org/html/2507.02778)
- [Ackerman & Panickssery - Self-Generated-Text Recognition (ICLR 2025)](https://openreview.net/forum?id=wWnsoLhHwt)
- [Vennemeyer et al. - Sycophancy Is Not One Thing (ICLR 2026)](https://openreview.net/forum?id=d24zTCznJu)
- [Wang et al. - When Truth Is Overridden (AAAI 2026)](https://arxiv.org/pdf/2508.02087)
- [Zhang & Lin - Simulated Adoption / Orthogonal Interference](https://arxiv.org/pdf/2602.04918)
- [Basu et al. - Interpretability without Actionability](https://arxiv.org/pdf/2603.18353)
- [Qwen-Scope (arXiv:2605.11887)](https://arxiv.org/abs/2605.11887)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Intrinsic Self-Correction via Mechanistic Interpretability](https://arxiv.org/abs/2505.11924)
- [O'Brien et al. - Isolating Sycophancy Neurons](https://arxiv.org/abs/2601.18939)


【原始 proposal（允许参考但不是主要依据）】:
# Mechanistic Anatomy of the Self-Correction Blind Spot: Own-Output Suppression as Contextual Signal Override

## Description
We propose a mechanistic investigation of the self-correction blind spot — the finding that LLMs correct identical errors 64.5% less often in their own output versus external text. Rather than seeking mitigation (which four intervention paradigms have failed to achieve; arXiv:2603.18353), we provide the first causal mechanistic account of WHY the blind spot occurs, with rigorous confound controls that the original behavioral finding lacks. Our central hypothesis is that the blind spot is an instance of 'contextual signal override' — structurally isomorphic to sycophantic agreement specifically (not sycophancy broadly; Vennemeyer et al., ICLR 2026 showed sycophancy decomposes into independent sub-behaviors), where a contextual signal (self-authorship, analogous to user opinion) suppresses correct behavior (error correction, analogous to factual knowledge). A key methodological contribution is our three-tier confound-controlled experimental design: Tier 1 replicates the original role-token-based blind spot; Tier 2 uses attribution-only minimal pairs (identical role tokens, different textual attribution) to isolate authorship framing from chat-template architectural confounds — motivated by both Ye et al.'s (arXiv:2603.12277) finding that role tags and content are perfectly correlated and Wang et al.'s (arXiv:2505.00626, ICML 2025) demonstration that LLMs exploit positional and task-type shortcuts rather than genuine role understanding; Tier 3 uses the Ackerman & Panickssery self-authorship vector (ICLR 2025) with nuisance-vector deconfounding as a causal activation-level intervention. Following the Error Depth decomposition (arXiv:2601.00828), we probe detection and correction pathways separately, testing whether own-output framing suppresses correction while leaving detection intact. Informed by Zhang & Lin's Orthogonal Interference finding (arXiv:2602.04918) — that conflicting context overrides parametric knowledge via quasi-orthogonal geometric rotation rather than magnitude dilution — we decompose the blind-spot effect into angular and radial components to characterize the geometric mechanism and potentially explain why prior magnitude-based interventions fail. We run experiments across Gemma 3 (with Gemma Scope 2 SAEs/transcoders), Llama 3.1 8B (with Llama Scope SAEs), and Qwen 3 8B (with Qwen-Scope SAEs; arXiv:2605.11887) — a symmetric three-family design where all models have pre-trained SAE coverage. We apply activation patching, SAE feature analysis following O'Brien et al.'s pipeline (arXiv:2601.18939), and geometric alignment tests to isolate the suppression circuit and quantify its overlap with sycophantic agreement circuits specifically — extracting the SYA direction following Vennemeyer et al.'s difference-in-means methodology and testing geometric alignment, component overlap, and cross-circuit intervention transfer — with pre-registered falsification criteria specifying what evidence would reject the unified mechanism hypothesis. As supplementary analysis, we test two hypotheses for how the Wait token reduces blind spots in non-reasoning models — authorship-signal disruption versus correction-gate bypass — via a single discriminating probe-comparison experiment complementing Troitskii et al.'s reasoning-model findings (arXiv:2510.04128). This work delivers five contributions: (1) a confound-controlled measurement establishing that textual authorship attribution (not role tokens alone) drives the blind spot, (2) the first circuit-level map of the own-output vs. external-text processing asymmetry decomposed into detection and correction pathways, (3) characterization of the geometric mechanism — orthogonal interference versus magnitude dilution — underlying the authorship-driven suppression, (4) quantified evidence for or against a unified 'contextual override' mechanism shared between the blind spot and sycophantic agreement specifically, with explicit falsification criteria, and (5) probe-level characterization of Wait token effects in non-reasoning models.

## Core Problem
LLMs correct identical errors 64.5% less often when framed as their own output versus external text (the 'blind spot'). The training-data explanation is correlational. Meanwhile, four mechanistic intervention paradigms fail to bridge the knowledge-action gap despite near-perfect internal probes (arXiv:2603.18353), and error detection capability does not predict correction success (arXiv:2601.00828). What mechanistic process causes own-output framing to suppress error correction, and does this suppression share a circuit with sycophancy — the structurally analogous phenomenon where contextual signals (user opinions) override factual knowledge? Critically, the original blind-spot finding (arXiv:2507.02778) confounds authorship attribution with chat-template role tokens — the 'own output' condition uses assistant-turn formatting while the 'external text' condition uses user-turn formatting, introducing differences in special tokens, attention masking, and positional encoding that may partially or wholly explain the effect. Wang et al. (arXiv:2505.00626, ICML 2025) showed that fine-tuned LLMs exploit task-type associations and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, further demonstrating that role tokens alone cannot be trusted as clean experimental variables. Disentangling the authorship signal from these architectural confounds is a prerequisite for any mechanistic account. Moreover, the recent finding that sycophancy decomposes into distinct, independently steerable sub-behaviors — sycophantic agreement versus sycophantic praise (Vennemeyer et al., arXiv:2509.21305, ICLR 2026) — means the unified-mechanism hypothesis must specify WHICH sycophancy sub-behavior shares circuits with the blind spot: we hypothesize sycophantic agreement (contextual override of correct judgments) rather than sycophantic praise (flattery generation) is the relevant analogue.

## Opportunity
Five converging lines of evidence create a unique opening: (1) The sycophancy mechanistic literature — including Wang et al.'s two-stage suppression circuit (AAAI 2026), Zhang & Chen's 'compliance subspace' unifying sycophancy and conformity (arXiv:2601.11563), O'Brien et al.'s SAE-based isolation of sycophancy neurons (arXiv:2601.18939), Genadi et al.'s linear sycophancy directions in attention heads (arXiv:2601.16644), and crucially Vennemeyer et al.'s causal decomposition of sycophancy into independently steerable sub-behaviors (arXiv:2509.21305, ICLR 2026) — collectively maps the sycophancy mechanism with enough precision that we can now test whether the blind spot is a special case of sycophantic agreement specifically. (2) Ackerman & Panickssery (ICLR 2025) identified a self-authorship vector in Llama3-8b-Instruct with a validated nuisance-vector confound-control methodology — this provides the surgical tool to isolate the authorship signal from role-token confounds that plague the original blind-spot measurement. (3) The knowledge-action gap paper (arXiv:2603.18353) showed interventions fail — but understanding WHY they fail requires knowing the exact circuit architecture, which no one has mapped for the own-output context. Zhang & Lin's 'Orthogonal Interference' finding (arXiv:2602.04918) — that conflicting context overrides parametric knowledge via quasi-orthogonal geometric rotation rather than magnitude dilution — provides a specific geometric hypothesis for HOW the blind-spot suppression might operate at the representation level. (4) The Wait token reduces blind spots by 89.3% in non-reasoning models, but the only mechanistic analysis of Wait (arXiv:2510.04128) studied reasoning models — what Wait does in non-reasoning models lacking backtracking circuits is an open question. (5) The release of Qwen-Scope (arXiv:2605.11887, May 2026) now provides pre-trained SAEs for Qwen3-8B alongside Gemma Scope 2 and Llama Scope, enabling the first symmetric three-model-family mechanistic comparison where all families have full SAE coverage.

## Related Work / Landscape
**Blind spot documentation**: Self-Correction Bench (arXiv:2507.02778, NeurIPS 2025 Workshop) documents the 64.5% blind spot across 14 non-reasoning models and discovers the 'Wait' mitigation, but offers only a training-data hypothesis. Critically, its experimental design uses role-token-based framing (assistant turn for own-output, user turn for external), which confounds authorship attribution with chat-template architectural differences — a limitation noted by Ye et al. (arXiv:2603.12277) who showed that role tags and content style are 'perfectly correlated' in chat models, creating interpretability confounds. Wang et al. (arXiv:2505.00626, ICML 2025) further demonstrate that this confound is deep: fine-tuned LLMs rely on task-type exploitation and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, meaning role-token-based experimental designs risk measuring these shortcuts rather than true authorship attribution. **Self-authorship detection**: Ackerman & Panickssery (arXiv:2410.02064, ICLR 2025) discovered a self-authorship vector in Llama3-8b-Instruct, demonstrating causal control over self-authorship perception via activation steering at layer 16. Their nuisance-vector methodology — subtracting the projection onto an output-bias vector computed from generic prompts — provides a validated technique for isolating authorship signals from surface confounds, and is the closest mechanistic precedent to our work. **Self-preference bias**: Xu et al. (arXiv:2402.11436, ACL 2024) document self-bias in self-refinement — LLMs systematically favor their own outputs — providing complementary behavioral evidence that self-authorship triggers preferential treatment. Roytburg et al. (arXiv:2509.03647, NeurIPS 2025) demonstrate that contrastive activation addition can reduce unjustified self-preference bias by up to 97% in LLM evaluators, but find that 'self-preference spans multiple or nonlinear directions' — steering vectors are effective for unjustified self-preference but unstable on legitimate self-preference and unbiased agreement, indicating the self-preference representation is architecturally distributed rather than neatly isolated along a single linear direction. This cautionary finding motivates our multi-method approach (probing, patching, and SAE analysis) rather than relying on a single linear probe. **Mechanistic self-correction**: Representation steering in self-correction (arXiv:2505.11924, AAAI 2026 Workshop) shows prompt-induced latent direction shifts drive correction in detoxification, but does not study the own-vs-external asymmetry. **Wait token mechanics**: Troitskii et al. (arXiv:2510.04128, EMNLP 2025 Findings) performed crosscoder analysis and causal interventions on Wait tokens in DeepSeek-R1-Distill-Llama-8B (reasoning model), finding features at layer 15 that modulate backtracking and self-reflection. Hwang et al. (arXiv:2601.17421) further analyzed Wait as a token-level signal into reasoning. Both studied reasoning models exclusively; the blind spot occurs in non-reasoning models where Wait's mechanism is likely distinct. **Contextual knowledge suppression — sycophancy circuits**: Wang et al. (arXiv:2508.02087, AAAI 2026 main) discovered a two-stage sycophancy circuit using logit-lens and activation patching — first-person framing creates stronger representational perturbations than third-person, suppressing factual knowledge. This is structurally isomorphic to the blind spot: a contextual signal (self-authorship vs. user opinion) suppresses a correct internal signal (error correction vs. factual knowledge). Zhang & Chen (arXiv:2601.11563) independently proposed a 'Signal Competition Mechanism' unifying sycophancy and conformity through a shared 'compliance subspace' — a convergent geometric manifold where social-emotional signals suppress information-calibration signals via a deterministic linear boundary. Their 'Transparency-Truth Gap' (internal confidence is permeable under pressure) parallels the blind spot's knowledge-action gap. Our work tests whether self-authorship constitutes a third signal type competing in this same subspace, or whether non-social contextual overrides operate through distinct geometry. **Sycophancy decomposition**: Vennemeyer et al. (arXiv:2509.21305, ICLR 2026) decompose sycophancy into sycophantic agreement (SYA) and sycophantic praise (SYPR), contrasting both with genuine agreement (GA). Using difference-in-means directions, activation additions, and subspace geometry across Qwen3-30B/4B, LLaMA-3.1-8B/3.3-70B, and GPT-OSS-20B, they show these three behaviors are encoded along distinct linear directions, each independently amplifiable or suppressible (selectivity ratios up to 36.8x), with SYA and GA highly aligned in early layers (cosine ~0.99 at L2-10) but diverging sharply in mid-to-late layers (~0.07 by L25), while SYPR remains nearly orthogonal to both throughout (cosine < 0.2). This decomposition is critical for our unified-mechanism hypothesis: sycophantic agreement — not sycophantic praise — is the structural analogue of blind-spot suppression, as both involve overriding correct outputs due to contextual signals. Our Phase 3 tests must compare the blind-spot authorship direction specifically against the SYA direction, not a monolithic 'sycophancy' direction. **Sycophancy neuron isolation**: O'Brien et al. (arXiv:2601.18939, NeurIPS 2025 Workshop) used Gemma-Scope SAEs with linear probes to isolate the 3% of MLP neurons most responsible for sycophancy in Gemma-2-2B/9B, then applied gradient masking for surgical correction. Their SAE-to-probe-to-neuron pipeline is directly applicable to our Phase 3 — we can identify blind-spot-responsible neurons and test their overlap with sycophancy neurons as a quantitative measure of circuit sharing. Genadi et al. (arXiv:2601.16644) found sycophancy signals are most linearly separable in middle-layer attention heads and that the sycophancy direction is geometrically distinct from the 'truthful' direction, suggesting separate mechanisms — relevant for testing whether the blind-spot direction aligns with either. **Contextual override geometry — Orthogonal Interference**: Zhang & Lin (arXiv:2602.04918) performed layer-wise geometric analysis of how in-context signals override parametric knowledge in Llama-3.1-8B, Qwen-3-4B, and GLM-4-9B. By decomposing residual stream updates into radial (norm-based) and angular (cosine-based) components, they discovered 'Orthogonal Interference' — conflicting context injects a steering vector quasi-orthogonal to the ground-truth direction, effectively rotating the hidden state representation rather than diluting its magnitude. Two of three models maintained stable residual norms despite performance degradation, demonstrating that compliance occurs through geometric displacement ('simulated adoption') rather than signal suppression. This directly informs our Phase 3: the blind-spot authorship signal may suppress error correction not by reducing the correction signal's magnitude but by rotating it away from the correct unembedding direction — a mechanism we can test by decomposing the blind-spot effect into angular versus radial components. **Knowledge-action gap**: Basu et al. (arXiv:2603.18353) showed all four mechanistic intervention paradigms fail to correct errors despite 98.2% AUROC probes — concept bottleneck steering, SAE feature steering, logit-lens patching, and truthfulness vector steering all leave the gap substantially unbridged. This establishes that the blind spot cannot be 'fixed' by naive activation steering but makes the mechanistic explanation of WHY more urgent — and the Orthogonal Interference finding suggests a possible explanation: if the suppression operates via angular rotation rather than magnitude reduction, scalar-magnitude-based interventions (which attempt to amplify the correct signal) would be ineffective because the signal's magnitude is already intact; it is the direction that has been displaced. **Error decomposition**: Li (arXiv:2601.00828) decomposes self-correction into detection, localization, and correction, showing these are independent capabilities — the Error Depth Hypothesis posits stronger models make fewer but deeper errors. This challenges the assumption that finding an 'own-output detection circuit' will explain correction failure; the suppression may act on the correction pathway independent of detection. **Role-token confounds**: Ye et al. (arXiv:2603.12277) demonstrate that in chat-formatted models, role tags and content style are 'perfectly correlated,' and probes trained on role-labeled data learn the confound rather than the underlying mechanism. Their 'CoT Forgery' attack achieves 60% success by injecting fabricated reasoning that models mistake for their own thoughts, demonstrating that role confusion is exploitable and that models infer text source from content style rather than role markers. They recommend using identical content across roles and validating downstream behavioral predictions — principles we adopt in our confound-control design. **Self-awareness and probing**: Gnosis (arXiv:2512.20578) identifies self-awareness circuits in hidden states. Probing for arithmetic errors (arXiv:2507.12379, EMNLP 2025) shows error signals exist in internal activations. **Hypothesis testing for circuits**: Kwon et al. (arXiv:2410.13032) formalize circuit hypothesis testing with mechanism preservation, mechanism localization, and minimality criteria — providing the statistical framework for our falsification tests. **Missing piece**: No work has performed controlled mechanistic comparison of the same error processed under own-output versus external-text attribution with proper confound controls, decomposed by detection/correction pathways, tested whether the suppression circuit is shared with the sycophantic agreement sub-behavior specifically, or characterized the geometric mechanism (orthogonal interference vs. magnitude dilution) underlying the authorship-driven suppression.

## Approach
**Phase 0 — Confound-Controlled Contrastive Dataset Design.** The original blind-spot measurement (arXiv:2507.02778) confounds authorship attribution with chat-template architecture: the 'own output' condition uses assistant-turn role tokens while the 'external text' condition uses user-turn role tokens, introducing differences in special tokens (<|assistant|> vs <|user|>), attention masking patterns, positional encodings relative to the generation boundary, and prior conversation context. Following the confound-isolation recommendations of Ye et al. (arXiv:2603.12277), and motivated by Wang et al.'s (arXiv:2505.00626, ICML 2025) demonstration that fine-tuned LLMs exploit task-type associations and positional proximity to begin-of-text as shortcuts for role identification rather than developing genuine role understanding, we employ a three-tier experimental design to disentangle the authorship signal from these architectural confounds:

*Tier 1 — Role-Token Replication (behavioral baseline).* We reproduce the Self-Correction Bench setup to confirm the blind spot exists in our three model families under the original framing.

*Tier 2 — Attribution-Only Minimal Pairs (controlling role tokens).* We construct minimal-pair prompts where identical error content appears in the SAME role position (user turn) but with different textual attribution. Example pair: 'Here is YOUR previous response — please review it for errors: [passage]' vs 'Here is a STUDENT's response — please review it for errors: [passage].' Both use identical user-turn role tokens, identical attention masking, and identical positional encoding — only the attribution framing differs. We construct 4 attribution conditions: (a) explicit self-attribution ('your previous response'), (b) explicit other-attribution ('a student wrote'), (c) ambiguous attribution ('the following passage'), and (d) counterfactual self-attribution ('you wrote this, but it was actually written by someone else'). If the blind spot persists in Tier 2 despite identical role tokens, the effect is driven by textual attribution, not architectural confounds. The Wang et al. (ICML 2025) finding that models exploit task-type and positional shortcuts rather than genuine role understanding provides additional justification for this design: even if role tokens were controlled, models might still exploit residual content-style correlates, which our four attribution conditions systematically vary.

*Tier 3 — Self-Authorship Vector Intervention (causal isolation).* Following Ackerman & Panickssery (ICLR 2025), we extract a self-authorship vector from each model using their contrastive methodology with nuisance-vector deconfounding — computing the mean activation difference between self-generated and other-generated texts, then subtracting its projection onto a nuisance vector derived from generic output-bias prompts. We then test: (i) Does adding the self-authorship vector to the external-text condition (Tier 2, other-attributed) reproduce the blind spot at the activation level, without changing any tokens? (ii) Does subtracting the self-authorship vector from the self-attributed condition eliminate the blind spot? This provides causal evidence that the authorship representation — not role tokens or surface framing — drives the suppression. We note Roytburg et al.'s (arXiv:2509.03647, NeurIPS 2025) cautionary finding that self-preference spans multiple or nonlinear directions: while a single self-authorship vector may capture the dominant linear component, we will test for residual effects after vector subtraction and, if present, apply iterative orthogonal projections or nonlinear probes to characterize remaining structure.

The Tier 1→2→3 progression provides a clean causal chain: Tier 1 replicates the phenomenon, Tier 2 rules out role-token confounds, and Tier 3 isolates the specific internal representation responsible.

**Phase 1 — Activation Collection.** Run three model families with pre-trained SAE suites — Gemma 3 4B/12B with Gemma Scope 2 SAEs, transcoders, and skip-transcoders (via SAELens/Neuronpedia); Llama 3.1 8B with Llama Scope SAEs (32K/128K features, via TransformerLens); and Qwen 3 8B with Qwen-Scope SAEs (64K features across all 36 layers, Top-k=50/100; arXiv:2605.11887) — on all Tier 1, 2, and 3 conditions, caching full residual stream activations, attention maps, and SAE feature activations at every layer.

**Phase 2 — Decomposed Probing.** Following the Error Depth Hypothesis framework (arXiv:2601.00828), train separate layer-wise linear probes for three signals: (a) the own-vs-external condition (where does the model represent authorship?), (b) error detection (does the model internally detect the error in both conditions?), and (c) correction action (does the model activate correction pathways?). The critical test is whether own-output framing suppresses probe (c) without suppressing probe (b) — i.e., the model detects the error but the correction pathway is gated by authorship context. Apply probes to both Tier 1 (role-token-confounded) and Tier 2 (attribution-only) conditions to determine whether the authorship representation is the same across both framings or whether role tokens contribute an additional, independent suppression signal.

**Phase 3 — Circuit Identification via Causal Intervention.** Apply activation patching, steering vectors derived from the own/external contrast, and SAE feature ablation to test whether identified components are necessary and sufficient for blind spot behavior. Specifically test: (i) Can we patch own-output activations with external-text activations at the divergence layer to eliminate the blind spot? (ii) Do Gemma Scope 2 transcoders and skip-transcoders reveal cross-layer propagation paths for the authorship signal? (iii) Does the identified suppression circuit overlap with the sycophantic agreement circuit specifically?

*Geometric mechanism analysis (informed by Orthogonal Interference).* Following Zhang & Lin (arXiv:2602.04918), we decompose the blind-spot effect into radial (norm-based) and angular (cosine-based) components relative to the correct-correction direction in each model's residual stream. This tests a critical mechanistic question: does the authorship signal suppress error correction by reducing the correction signal's magnitude (direct suppression), or by rotating the hidden state away from the correction direction while preserving its magnitude (orthogonal interference / 'simulated adoption')? If the blind spot operates via orthogonal interference — as Zhang & Lin found for in-context knowledge conflicts — this would explain why magnitude-based interventions in the knowledge-action gap literature (arXiv:2603.18353) fail: they attempt to amplify a signal whose magnitude is already intact, but whose direction has been displaced. We measure: (a) the cosine angle between the residual stream under own-output framing and the correct-correction direction, versus under external-text framing; (b) the residual norm change between conditions; (c) layer-wise progression of the angular displacement to identify where the rotation initiates. If the angular component dominates the radial component in explaining the blind-spot effect, this constitutes evidence for an orthogonal-interference mechanism.

*Sycophantic agreement circuit overlap.* We operationalize this overlap test following Vennemeyer et al.'s decomposition (arXiv:2509.21305, ICLR 2026): since sycophancy decomposes into sycophantic agreement (SYA) and sycophantic praise (SYPR) with distinct, independently steerable linear directions, we specifically extract the SYA direction (not a monolithic sycophancy vector) for comparison, as SYA — overriding correct judgments due to contextual signals — is the structural analogue of blind-spot suppression. We adopt their difference-in-means methodology to extract the SYA direction from our three model families, noting their finding that SYA becomes maximally separable from genuine agreement in mid-to-late layers (cosine similarity dropping from ~0.99 at layers 2-10 to ~0.07 by layer 25 in their studied models). Following O'Brien et al.'s SAE-to-probe pipeline (arXiv:2601.18939): we identify the top SAE features and MLP neurons predictive of blind-spot behavior, then compute their overlap with SYA-predictive features from the same models. We also test geometric alignment between the blind-spot authorship direction and the SYA direction (Wang et al., AAAI 2026), the 'compliance subspace' directions (Zhang & Chen, arXiv:2601.11563), and the attention-head sycophancy direction (Genadi et al., arXiv:2601.16644).

**Falsification criteria for the unified 'contextual signal override' hypothesis.** We pre-register three falsification tests following the circuit hypothesis testing framework of Kwon et al. (arXiv:2410.13032), targeting the sycophantic agreement (SYA) sub-behavior specifically as the relevant comparison following Vennemeyer et al.'s decomposition: (F1) *Circuit non-overlap*: If the blind-spot suppression components (layers, attention heads, MLP neurons identified via SAE probing) are architecturally disjoint from SYA circuit components (not sycophantic praise or generic sycophancy), AND cross-circuit patching fails to transfer effects in either direction (patching SYA components does not affect blind-spot behavior, and vice versa), we reject the strong unified hypothesis. (F2) *Geometric non-alignment*: If the authorship-signal direction in activation space has cosine similarity < 0.1 with the SYA-signal direction across all probed layers, and these directions cannot be related by a low-rank linear transformation, this indicates geometrically distinct mechanisms — ruling out even a weak shared-subspace account. Additionally, following Zhang & Lin's Orthogonal Interference framework (arXiv:2602.04918), we test whether both phenomena employ the SAME geometric mechanism type even if their specific directions differ: if SYA operates via orthogonal interference (angular displacement) while the blind spot operates via magnitude dilution (or vice versa), this constitutes evidence for mechanistically distinct processes even if F1 shows some component overlap. We thus decompose both the blind-spot and SYA effects into angular and radial components to enable mechanism-type comparison beyond simple direction alignment. (F3) *Intervention asymmetry*: If steering along the SYA direction does not modulate blind-spot severity (and vice versa) beyond chance, the two phenomena are functionally independent despite surface-level structural similarity. Note: following the decomposition result, we also test SYPR as a negative control — if blind-spot direction overlaps with SYPR (flattery, not override), this would indicate a different mechanism than hypothesized. If all three criteria are met, we conclude the blind spot operates through a distinct suppression mechanism; if none are met, we support the unified account; mixed results map the partial overlap.

**Phase 4 — Wait Token Analysis (Supplementary).** This phase is explicitly secondary to the core Phases 0-3 contribution, included as supplementary analysis if the timeline permits and scoped to the single most discriminating experiment. In non-reasoning models, we test two primary hypotheses: (H1) Wait disrupts the own-output authorship signal, resetting it toward the external-text representation; (H2) Wait activates a correction pathway that bypasses the authorship gate. The discriminating experiment: measure Wait's effect on the authorship probe (Phase 2a) versus the correction-action probe (Phase 2c). If Wait reduces the authorship probe's self-attribution signal → H1 (authorship disruption, analogous to resetting the contextual override). If Wait leaves the authorship probe unchanged but increases the correction probe → H2 (gate bypass, a distinct mechanism). This single paired-probe comparison requires minimal additional compute (rerunning Phase 2 probes on Wait-appended versions of the Tier 2 dataset) while providing mechanistic evidence complementing Troitskii et al.'s reasoning-model findings (arXiv:2510.04128). We do NOT include full circuit mapping for Wait, reserving that for follow-up work.

**Framing note**: Following the knowledge-action gap results (arXiv:2603.18353), we do NOT claim this work will yield mitigation strategies. The contribution is mechanistic explanation: mapping the circuit that causes the blind spot (with proper confound controls), characterizing the geometric mechanism (orthogonal interference vs. magnitude dilution), testing its relationship to sycophantic agreement circuits specifically, and characterizing Wait's probe-level effects in non-reasoning models. Understanding the circuit architecture — including whether the suppression operates via directional rotation rather than magnitude reduction — is a prerequisite for future work on why activation-level interventions fail to bridge the knowledge-action gap.

## Inspiration
Blind spot finding (64.5% rate, Wait reduces by 89.3%); confound between role tokens and authorship in the original measurement — reinforced by Wang et al.'s (ICML 2025) demonstration that LLMs use shortcuts rather than genuine role understanding — motivating a cleaner experimental design; structural isomorphism between blind spot and sycophantic agreement (not sycophancy broadly) as contextual-signal-override phenomena, now supported by four independent mechanistic studies of sycophancy plus the critical decomposition showing sycophantic agreement and praise are distinct (Vennemeyer et al., ICLR 2026); Orthogonal Interference finding (Zhang & Lin, arXiv:2602.04918) providing a specific geometric hypothesis for how contextual signals override correct representations via rotation rather than suppression; knowledge-action gap negative results motivating mechanistic explanation over intervention — with Orthogonal Interference suggesting why magnitude-based interventions fail; Error Depth Hypothesis motivating decomposed analysis of detection vs. correction pathways; reasoning/non-reasoning gap in Wait token understanding; convergence of pre-trained SAE suites (Gemma Scope 2, Llama Scope, Qwen-Scope) enabling symmetric three-family comparison.

## Key References
- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models (NeurIPS 2025 Workshop, arXiv:2507.02778)
- Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct (ICLR 2025, arXiv:2410.02064)
- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models (AAAI 2026 main, arXiv:2508.02087)
- Human-like Social Compliance in Large Language Models: Unifying Sycophancy and Conformity through Signal Competition Dynamics (arXiv:2601.11563)
- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (NeurIPS 2025 Workshop, arXiv:2601.18939)
- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644)
- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (ICLR 2026, arXiv:2509.21305)
- Simulated Adoption: Decoupling Magnitude and Direction in LLM In-Context Conflict Resolution (arXiv:2602.04918)
- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (arXiv:2603.18353)
- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis (arXiv:2601.00828)
- Internal States Before Wait Modulate Reasoning Patterns (EMNLP 2025 Findings, arXiv:2510.04128)
- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421)
- Intrinsic Self-Correction in LLMs: Towards Explainable Prompting via Mechanistic Interpretability (AAAI 2026 Deployable AI Workshop, arXiv:2505.11924)
- Prompt Injection as Role Confusion (arXiv:2603.12277)
- The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (ICML 2025, arXiv:2505.00626)
- Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (NeurIPS 2025, arXiv:2509.03647)
- Hypothesis Testing the Circuit Hypothesis in LLMs (arXiv:2410.13032)
- Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models (arXiv:2605.11887)
- Gemma Scope 2: Full-Stack Interpretability Suite for Gemma 3 (Google DeepMind 2025)
- Llama Scope: Extracting Millions of Features from Llama-3.1-8B with Sparse Autoencoders (arXiv:2410.20526)
- Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement (ACL 2024, arXiv:2402.11436)
- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits [Gnosis] (arXiv:2512.20578)
- Probing for Arithmetic Errors in Language Models (EMNLP 2025, arXiv:2507.12379)
- LLM Layers Immediately Correct Each Other (NeurIPS 2025)

## Resource Estimate
- **manual**: {'gpu_hours': '450-650 A100-80GB hours (activation caching for ~2500 contrastive pairs across 3 tiers x 3 model families x all layers, self-authorship vector extraction with nuisance-vector deconfounding, decomposed probing, patching experiments, radial/angular decomposition analysis, SYA direction extraction and comparison, and supplementary Wait analysis)', 'timeline': '12-16 weeks', 'estimated_gpu_cost': '$900-$1300 at ~$2/GPU-hr spot pricing'}
- **human_in_loop**: {'gpu_hours': '380-550 A100-80GB hours (Claude accelerates Tier 2 minimal-pair construction, probing code, SAE feature comparison across three symmetric suites, SYA direction extraction, and cross-model analysis)', 'timeline': '9-13 weeks', 'claude_api_cost': '$250-$450 (dataset generation including Tier 2 attribution variants, code scaffolding for three SAE suites, results interpretation, paper drafting)', 'estimated_gpu_cost': '$760-$1100'}
- **auto_research**: {'gpu_hours': '320-480 A100-80GB hours (automated probe sweeps across 3 tiers, systematic patching grid, cross-model SAE feature comparisons, sycophantic agreement overlap quantification, radial/angular decomposition)', 'timeline': '7-10 weeks', 'claude_api_cost': '$450-$750 (experiment orchestration, iterative analysis, automated paper writing)', 'estimated_gpu_cost': '$640-$960', 'speed_bottleneck': "Sequential activation caching is I/O-bound: each 8B model forward pass with full activation caching for 2K-token sequences takes ~4s on a single A100; parallelism across models helps but each model's layer-wise patching experiments are inherently sequential. The three-tier dataset increases total pairs by ~2.5x relative to Tier 1 alone, partially offset by the symmetric SAE tooling (no custom SAE training needed for any model family)."}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "935c782d-2ba8-4043-836e-8bc4a2c27402",
  "type": "user",
  "uuid": "8b64bd67-7aaf-48e1-be7d-487139d1c647",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:27:19.175Z_

```json
{
  "parentUuid": "8b64bd67-7aaf-48e1-be7d-487139d1c647",
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
  "uuid": "56735d58-b097-47ec-b626-0a3c66335100",
  "timestamp": "2026-05-19T21:27:19.175Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:27:19.175Z_

```json
{
  "parentUuid": "56735d58-b097-47ec-b626-0a3c66335100",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cf25633f-7e43-4554-a330-5b3fca7de1f6",
  "timestamp": "2026-05-19T21:27:19.175Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "cf25633f-7e43-4554-a330-5b3fca7de1f6",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Mechanistic analysis of LLM self-correction blind spot",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:27:49.635Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically to produce a Meta Judge output.

First, let me extract the key numbers and dimensions:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏弱
- Related Work: 强
- Probability: [20% - 32%] 中位 25%
- Fatal issue: CoRL venue mismatch (desk reject)

**Reviewer 2:**
- Novelty: 中


- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%
- Fatal issue: CoRL venue mismatch (desk reject)

**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [20% - 32%] 中位 25%
- Fatal issue: CoRL venue mismatch (desk reject)

All three reviewers converge on the same fatal issue and show consistent probability estimates around 25-27%, with a mean of 25.67% and minimal variance across their median assessments. I'm seeing strong consensus across all three reviewers on the core issues: the venue mismatch warrants desk rejection, the novelty and significance are moderate, the method combines existing tools without introducing new methodology, and there's a fundamental dilemma where positive results would be unsurprising while negative results would undermine the paper's narrative. There are only minor outliers where individual reviewers flag specific missing references like Anthropic's circuit tracing work or concerns about textual attribution approaches. The three reviewers are tightly clustered around 25-27% for their median estimates, so I should anchor my final probability near that convergence point. Given the high consistency across all three ranges, I'll narrow the interval to 21-30% with a median of 25-26%, staying within the bounds that all reviewers proposed.

Now I need to compile the implementation assessment details that all three reviewers referenced from the proposal's resource estimate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf25633f-7e43-4554-a330-5b3fca7de1f6",
  "isSidechain": false,
  "requestId": "req_011CbCdr9givgXx5Um2mocm4",
  "type": "assistant",
  "uuid": "6c83ac3d-fda7-45ab-8f51-907a0c890de2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gXdypwjEjiCSV4pec3kx5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25998,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25998,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3498,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25998
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

_source line 9 · 2026-05-19T21:28:42.656Z_

【阶段】: Meta Judge
【三次中位】: [25%, 27%, 25%]  std=0.94%
【共识维度】: 
- **CoRL venue 致命不匹配** (3/3, unanimous)：proposal 是纯 LLM mechanistic interpretability 研究，与机器人学习完全无关。投稿 CoRL 将被 desk reject。三位审稿人均独立发现此问题并给出一致判断。→ **致命**
- **Novelty = 中** (3/3, unanimous)：核心方法论是已有 mech-interp 工具箱（activation patching, SAE feature analysis, linear probing, geometric decomposition）的组合应用于新现象，而非方法创新。Gap 真实存在，但假说（blind spot ≈ SYA contextual override）高度可预测。三层 confound-control 设计被一致认为是方法论上的实质贡献，是 proposal 中最有原创性的部分。→ **中**
- **Related Work = 强** (3/3, unanimous)：覆盖极其全面、引用准确、差异化定位清晰。引用均经查证真实存在，venue 和描述准确。→ **强**
- **Significance ≈ 中** (3/3, R1 略严为"中偏弱")：纯解释性贡献、明确放弃 mitigation、基础现象仅有 workshop paper 级别支撑。"Explanation without actionability" 在 top venue 主会的接受门槛高。→ **中（偏弱）**
- **"Expected Result" 风险** (3/3, unanimous)：核心假说（电路共享）如果被验证，审稿人大概率评价 "I would have guessed this"；如果被否证，论文统一叙事弱化。Dual-outcome 困境下均难达到 "surprising" 标准。→ **强共识风险**
- **基础现象稳固性风险** (3/3, unanimous)：64.5% blind spot rate 来自一篇 NeurIPS Workshop paper（非主会），尚未被独立复现或在新模型上确认。→ **中等风险**
- **Trivial alternative 存在但有增量** (3/3, unanimous)：简化版 probing study 或直接 self-authorship vector steering 可低成本部分回答核心问题，但 proposal 的完整 circuit mapping + SYA overlap + geometric decomposition 有实质增量。→ **中等威胁**

【异常维度】: 
- R2 提到 Sparse Activation Fusion (SAF) 未被引用——仅 1 人提到，且 R2 自己也注明"对核心论点影响不大"。→ 降权，不影响概率判断
- R1 提到 Anthropic circuit tracing on Claude 3.5 Haiku 可能相关——仅 1 人提到且标注为非实质缺陷。→ 降权
- R1 Significance 评为"中偏弱"而 R2/R3 评为"中"——方向一致，仅严格程度有微差，不构成真正分歧。综合偏向略严的"中（偏弱端）"

【最终概率】: [21% - 30%] 中位 25%
【一致性】: 高（std=0.94%，三位审稿人在所有 rubric 维度上判决高度一致）
【综合理由】: 

三位审稿人的评估呈现罕见的高度一致性——Novelty/Significance/Related Work 三维度判决完全对齐，概率估计仅差 2 个百分点，核心风险点（expected result, no actionability, workshop-paper foundation）均被独立识别。无需进行分歧调解。

**概率锚定逻辑**：
- **Related Work（强）** 提供了 ~20% 的地板——扎实的文献覆盖确保不会因 related work 遗漏被拒，execution quality 可部分补偿 idea 不够 exciting 的短板。
- **Novelty（中）** 设定了 ~32-35% 的天花板——工具组合应用 + 可预测假说限制了上行空间。即使实验结果完美，审稿人看到的仍是 "competent application of existing mech-interp toolkit to a specific phenomenon"。
- **Significance（中偏弱）** 在天花板内进一步向下压——纯解释性贡献 + 无 mitigation + 基于 workshop paper 的现象 = 审稿人"so what?"风险高。
- 三位审稿人均指出的 **dual-outcome 困境**（positive = unsurprising, negative = weak narrative）是本 proposal 最核心的结构性弱点，这不是执行层面能补救的。

区间从 R1/R3 的 [20%-32%] 和 R2 的 [22%-32%] 综合缩窄至 [21%-30%]。中位取两位 25% 的共识值。上界从 32% 收至 30%，因为三位一致认为 dual-outcome 困境限制了最佳情况下的表现。

**关于 CoRL venue**：此为致命硬伤，但属于可修正的投稿策略问题（换 venue 即可），不影响 idea 本身的质量评估。以下概率假设投稿至适配 venue（NeurIPS/ICLR/ICML）。

【建议】: 边缘（idea 方向正确、gap 真实、执行设计严谨，但核心洞察的 surprise 值不足以稳定跨过 top venue 门槛。建议进入迭代优化，重点提升 Novelty 的 surprise 维度和 Significance 的 actionability 维度。同时必须更换投稿目标 venue。）

【实施评估】:
  - 计算资源: 320-650 A100-80GB GPU hours（取决于自动化程度），约 $640-$1300 spot pricing。包括三模型家族 × 三层实验条件的全层激活缓存、self-authorship vector 提取、分解 probing、patching 实验、几何分解分析、SYA 方向提取与比较。I/O bound 瓶颈存在（单 A100 上 8B 模型 2K-token 全层缓存约 4s/pass）。
  - 数据需求: ~2500 contrastive pairs（三层实验条件），需自行构建 Tier 2 的 attribution-only minimal pairs。基础错误样本可从 Self-Correction Bench 获取或参考其方法论构建。无需私有数据集。
  - 人工介入: Tier 2 minimal pair 构建需要一定人工设计（4 种 attribution 条件的 prompt 模板）；结果解读和论文写作需要 mech-interp 领域专家参与。Claude API 辅助可显著加速代码开发和分析。整体人工介入需求中等。
  - 训练需求: **无需训练大模型**。所有三个模型家族均使用预训练 SAE suites（Gemma Scope 2, Llama Scope, Qwen-Scope）。仅需训练轻量级 linear probes（几分钟级别）。
  - 新 Benchmark: 需要构建 Tier 2 attribution-only minimal pair 数据集（这是核心方法论贡献的一部分，但规模不大，~数百对 prompt）。不需要构建大规模新 benchmark。
  - 预估周期: 7-16 周（取决于自动化程度和人力投入），含数据构建 1-2 周、激活缓存与实验 3-6 周、分析与写作 3-5 周。建议预留 12 周作为现实规划。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c83ac3d-fda7-45ab-8f51-907a0c890de2",
  "isSidechain": false,
  "requestId": "req_011CbCdr9givgXx5Um2mocm4",
  "type": "assistant",
  "uuid": "d7fef7b8-ef2c-4886-bcd5-34f2b0b40b96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gXdypwjEjiCSV4pec3kx5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25998,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25998,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3498,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25998
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a thorough evalua…",
  "leafUuid": "d7fef7b8-ef2c-4886-bcd5-34f2b0b40b96",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Mechanistic analysis of LLM self-correction blind spot",
  "sessionId": "cb7b2648-9853-474e-acd6-3797d6e8bcf4"
}
```

---
