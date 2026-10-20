# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5ccdb039-573b-4283-a0f7-d0ac3a4a908b.jsonl`
- **Structured JSON:** [`74c2cd935e74b9a77dd8.json`](../../sessions/74/74c2cd935e74b9a77dd8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:21:05.947Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:21:05.947Z",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient data to make a well-informed assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Reward Under Attack, arXiv:2603.06621] (arXiv, Feb 2026):\n   直接验证了 proposal 的核心问题——PRM 在 RL 训练中被 exploit 到 >0.9 reward 但 <4% accuracy，43% reward gains 来自 stylistic shortcuts。论文确认 PRM 本质上是 fluency detector。这是本 proposal 的问题基础，描述准确。\n\n2. [Reward Models Identify Consistency, Not Causality, arXiv:2502.14619] (arXiv, Feb 2025):\n   确认 reward model 优先评估 structural consistency 而非 causal correctness——移除 problem statement 对 reward 影响甚微，但改变数值或 reasoning flow 影响显著。这为 proposal 的 \"fluency ≠ validity\" 论点提供了理论基础。\n\n3. [PARC/PERL, arXiv:2502.02362] (ICML 2025):\n   真实存在且已被 ICML 2025 录用。确认 open-source LLM 可以 90% recall 提取 premise dependency links，形成 DAG 结构。PERL 证明 premise-aware verification 提升 error detection 6-16%。但关键点是：PERL 仅在 evaluation time 使用这些结构信息，未用于 PRM training。\n\n4. [CRM — Linking Process to Outcome, arXiv:2509.26578] (ICLR 2026):\n   通过 conditional probability rules 建模 reasoning steps 间的因果关系，sequential conditioning on preceding steps。与本 proposal 的区别是 CRM 使用隐式序列依赖而非显式 DAG 结构，且无 contrastive training。\n\n5. [APRM — Adversarial Training for Process Reward Models, arXiv:2511.22888] (arXiv, Nov 2025):\n   Generator-PRM 对抗训练框架，自动生成 harder negatives，OOD +5.3pp。**这是最重要的 trivial alternative 威胁**——APRM 同样通过 hard negatives 训练 PRM，只是 negatives 来源不同（adversarial generation vs. structure-aware corruption）。\n\n6. [CPMI — Contrastive Mutual Information for PRM, arXiv:2604.10660] (arXiv, April 2026):\n   用 contrastive pointwise mutual information 做 PRM auto-labeling，减少 84% 数据构建时间。与本 proposal 的区别：CPMI 用 contrastive 方法做 labeling 而非 training representation，且不使用 premise DAG。\n\n7. [Graph of Verification (GoV), arXiv:2506.12509] (arXiv, 2025):\n   将 reasoning 建模为 DAG 并按 topological sort 逐节点验证。Training-free 方法。与本 proposal 互补但不竞争——GoV 是 inference-time DAG 使用，本 proposal 是 training-time DAG 使用。\n\n8. [RewardFlow, arXiv:2603.18859] (arXiv, March 2026):\n   在 state graph 上做 topology-aware reward propagation，面向 agentic tasks。使用不同类型的 graph（state-transition graph vs. premise dependency DAG），无 contrastive training。\n\n9. [GenPRM, arXiv:2504.00891] (AAAI 2026):\n   将 process supervision 重新定义为 generative task（CoT + code verification），而非 discriminative scoring。与本 proposal 正交——GenPRM 改变 PRM 的 paradigm（discriminative → generative），本 proposal 仍在 discriminative PRM 框架内改进 training signal。\n\n10. [PRMBench, arXiv:2501.03124] (ACL 2025):\n    SOTA 为 PathFinder-PRM-7B 的 67.7（Gemini-2-Thinking 68.8），human ceiling 83.8。16-point gap 确实存在。\n\n11. [PURE — Min-Form Credit Assignment, arXiv:2504.15275] (NeurIPS 2025):\n    通过 min-form credit aggregation 替代 summation，改进 PRM reward propagation。无 graph structure 使用。\n\n- 调研总结：PRM robustness 是 2025-2026 年的活跃研究前沿，已有多条技术路线（adversarial training, conditional modeling, credit assignment, generative PRM, post-hoc correction）。\"premise DAG + contrastive PRM training\" 的具体组合确实未被尝试，但各组件（DAG extraction, contrastive training, structure-aware negatives）均为成熟技术。该领域竞争激烈，多个 concurrent work 从不同角度攻克同一问题。\n\n\n【Trivial Alternative 检验】:\n\n存在两个有意义的 trivial alternative 威胁：\n\n(1) **APRM (adversarial training)**：APRM 已经通过 adversarial generator 自动产生 harder negatives 来训练 PRM，OOD +5.3pp。本 proposal 的 structure-aware negatives（通过 premise-link corruption 生成）与 APRM 的 adversarial negatives 在功能上高度相似——都是产生\"表面流畅但逻辑有问题\"的 hard negatives。PGCT 的增量价值在于：negatives 的生成是 *有针对性的*（精确破坏特定 premise link），而非 APRM 的 *盲目对抗*。但这个增量是否足够 significant 需要实验验证——如果 APRM 的 adversarial generator 恰好已经学会了类似的 premise-link corruption 模式，则 PGCT 的增量可能很小。\n\n(2) **PERL at inference time + standard PRM**：PERL 已证明 premise-aware verification 在 evaluation time 提升 6-16%。一个简单的 pipeline——标准 PRM + PERL-style inference-time DAG verification——可能已经捕获了大部分结构信息的收益。PGCT 的论点是\"在 training time 注入结构信息比 inference time 使用更根本\"，但这需要实验对比。\n\n增量价值存在但需要证明：PGCT 的核心 bet 是 *training-time structural inductive bias* 优于 *inference-time structural post-processing* 和 *adversarial hard negative generation*。这个 bet 是 reasonable 的，但不是显然成立的。\n\n\n【前提假设检验】:\n\n核心逻辑链条中有以下未经验证的环节：\n\n(1) **\"Premise DAG structure is the right inductive bias for disentangling fluency from logic\"**——这是最核心的假设。\"Reward Under Attack\" 证明了 PRM 是 fluency detector，\"Consistency Not Causality\" 证明了 PRM 检测 consistency 而非 causality。但从\"PRM 不理解逻辑结构\"到\"注入 premise DAG 可以修复这个问题\"之间存在 gap。逻辑结构可以有多种表征方式（premise DAG 只是其中之一），且 PRM 的 fluency bias 可能根植于 transformer representation 的特性，不一定能被 contrastive loss 克服。\n\n(2) **\"90% recall DAG extraction → good enough training signal\"**——PARC 在 Llama-3.1-8B-Instruct 上达到 90% recall，但 precision 未详细讨论。10% 的 missing links + unknown false positive rate 意味着部分 \"graph-preserving\" perturbations 实际上可能改变了 DAG topology，部分 \"graph-breaking\" perturbations 可能保留了真实 DAG。噪声训练信号可能削弱甚至反向影响 contrastive learning 效果。\n\n(3) **\"InfoNCE loss over DAG-anchored embeddings can effectively force surface-form invariance\"**——contrastive learning 在 vision (SimCLR) 和 NLP (SimCSE) 中的成功不能直接外推到 \"logical structure invariance\" 场景。Surface-form invariance 和 logical-structure sensitivity 是否能通过单一 contrastive objective 同时实现，理论上不确定。\n\n(4) **\"LLM paraphrasing produces genuine graph-preserving perturbations\"**——proposal 假设 LLM 可以 rephrase reasoning steps while maintaining identical DAG topology。但 rephrasing 数学推理步骤时，subtle changes in phrasing 可能 implicitly 改变 premise references，导致 DAG topology 的 silent drift。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \"premise DAG + contrastive training + PRM\" 的具体组合确实未被尝试（CPMI 用 contrastive 但无 DAG；GoV 用 DAG 但 training-free；APRM 用 hard negatives 但无 structural guidance；CRM 用 sequential conditioning 但非显式 DAG）。然而，这是**组合式创新而非概念性创新**。核心 insight——\"用 structural information 指导 PRM training\"——是一个自然的、可预测的 next step。PERL 已经证明 premise structure 在 evaluation 时有帮助，将其\"推到 training 阶段\"是顺理成章的工程延伸。如果实验证明 positive，审稿人很可能说 \"I would have guessed this works\" 而非 \"this is surprising\"。\n\n2. **Significance: 中偏强** — PRM robustness 是当前 reasoning with LLMs 领域的核心瓶颈之一，\"Reward Under Attack\" 和 \"Consistency Not Causality\" 已经确立了这个问题的 urgency。43% stylistic shortcuts 和 <4% accuracy under reward hacking 是触目惊心的数字。如果 PGCT 确实能大幅降低 adversarial exploitability，这对整个 RLHF for reasoning 领域有实质意义。但 proposal 的 target improvement（PRMBench 67.7 → >70）幅度较小（~2.3 points），如果最终实验结果是这个量级，impact 会被打折。\n\n3. **Related Work: 强** — Proposal 对领域景观的覆盖非常全面且准确。所有引用的论文经验证均真实存在且描述准确（PARC/PERL at ICML 2025、CRM at ICLR 2026、GenPRM at AAAI 2026、PRMBench at ACL 2025 等）。对 concurrent work（CPMI、RewardFlow、GoV）的差异化定位清晰。唯一可补充的是 Crome（Causally Robust Reward Modeling）和 GRP（Graph Reasoning Paradigm）等更近期的 concurrent work，但这不影响整体评价。\n\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】:\nSignificance 接近\"强\"，拉高了下限——问题是真实的、重要的、有定量证据支撑的。Related Work 覆盖\"强\"，进一步巩固了 proposal 的基础质量。但 **Novelty 的\"中\"评级严重限制了上界**：核心贡献是组合式创新（将 PERL 的 premise DAG 从 inference time 推到 training time + 加 contrastive loss），intellectual contribution 的深度不足以让审稿人感到 surprised。此外，APRM 作为 trivial alternative 的威胁是实质性的——如果 adversarial training 已经能产生足够好的 hard negatives，则 PGCT 的 structure-aware negatives 可能只是 marginal improvement。PRMBench 上 2.3 点的目标提升也偏保守，不够 impressive。综合来看，这是一个 solid engineering contribution，但在 AAAI 的 novelty 标准下偏弱，概率集中在 25-30% 区间。\n\n【主要风险】:\n1. **Novelty 不足 / \"incremental extension\" 质疑**：审稿人可能认为这只是 PERL (inference-time premise DAG) 的自然训练时延伸 + 标准 contrastive learning 框架的直接应用，缺乏深层技术洞见。\"Why not just use APRM which already generates hard negatives?\" 是一个难以回避的问题。\n2. **Expected results not surprising**：如果 \"使用逻辑结构信息训练 PRM → PRM 更理解逻辑结构\"，这个结果过于 intuitive。审稿人可能写 \"The approach is sound but the finding, if positive, is expected rather than insightful\"——这在 top venue 是常见的 borderline reject 理由。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL — Premise-Augmented Reasoning Chains (ICML 2025)](https://arxiv.org/abs/2502.02362)\n- [CRM — Linking Process to Outcome (ICLR 2026)](https://arxiv.org/abs/2509.26578)\n- [APRM — Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)\n- [CPMI — Contrastive Mutual Information for PRM](https://arxiv.org/abs/2604.10660)\n- [Graph of Verification (GoV)](https://arxiv.org/abs/2506.12509)\n- [RewardFlow](https://arxiv.org/abs/2603.18859)\n- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [PRMBench (ACL 2025)](https://arxiv.org/abs/2501.03124)\n- [AgentEval](https://arxiv.org/abs/2604.23581)\n- [DAG-Math](https://arxiv.org/abs/2510.19842)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (arXiv:2603.06621, Feb 2026):\n   - 本 proposal 的核心动机来源。证实 PRMs 在对抗压力下系统性可被利用，43% 的 RL reward gain 归因于 stylistic shortcuts，策略在 AIME 上达到 >0.9 PRM reward 但 <4% 真实准确率。提出了 fluency-logic dissociation 现象。\n   - 论文确实存在，描述准确。\n\n2. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025):\n   - Xu et al. 证明 reward model 优先评估 structural consistency 而非 causal correctness——移除问题陈述对 reward 影响甚微，但改变数值或打断推理流程显著影响 RM 输出。\n   - 论文确实存在，描述准确。\n\n3. PARC/PERL (arXiv:2502.02362, ICML 2025):\n   - 将线性推理链重构为 premise-augmented reasoning chains (DAG)，证明开源 LLM 在 premise identification 上达到 90% recall，基于 premise 的验证将错误识别准确率提升 6-16%。\n   - 论文确实存在，描述准确。\n\n4. APRM — Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025):\n   - Generator-PRM 对抗博弈框架，通过渐进式更难 negatives 训练，平均 +3.4pp（OOD +5.3pp）。\n   - **与本 proposal 直接竞争**：同样目标是提升 PRM 对 novel errors 的泛化，但不使用显式逻辑结构。\n\n5. CRM — Conditional Reward Modeling (arXiv:2509.26578, ICLR 2026):\n   - 将推理建模为 temporal process，reward 条件化于前序 steps 和最终结果，捕获 inter-step causal relationships。\n   - 与本 proposal 关注 inter-step dependencies 有重叠，但不使用 premise DAG 也不使用 contrastive training。\n\n6. CPMI — Contrastive Mutual Information for PRM (arXiv:2604.10660, April 2026):\n   - 用 contrastive pointwise mutual information 进行自动 step-level reward labeling，相比 MC 估计减少 84% 标注时间。\n   - 使用 contrastive 思想但用途不同（labeling vs. training），不涉及 premise graphs。\n\n7. GenPRM (arXiv:2504.00891, AAAI 2026):\n   - 将 process supervision 重新定义为生成式任务，结合 CoT reasoning 和 code verification。已被 AAAI 2026 接收。\n   - 不同范式（generative vs. discriminative），与本 proposal 正交。\n\n8. PathFinder-PRM (2025):\n   - PRMBench 当前 SOTA 67.7（human ceiling 83.8），通过分层 error-aware supervision 实现。\n   - 本 proposal 的 benchmark target 基准。\n\n9. \"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs\" (arXiv:2601.17593, 2026):\n   - 分析 LLM 内部表示中 DAG 结构的可恢复性，发现中间层达到峰值。\n   - 为 DAG-based 方法提供了额外理论支撑，但 proposal 未引用此工作。\n\n- **调研总结**: PRM 鲁棒性是 2025-2026 年的热点方向，已有多种攻击角度的改进方案（adversarial training、conditional modeling、contrastive labeling、generative verification），但尚无工作将 premise dependency DAGs 显式融入 PRM contrastive training。该领域竞争激烈，新方法需要在多个 benchmark 上展现显著优势才能脱颖而出。\n\n【Trivial Alternative 检验】:\n\n存在多个更简单的替代方案可能部分实现类似效果：\n\n1. **APRM 式 adversarial training**：已证明通过对抗博弈生成 harder negatives 可以 OOD +5.3pp，无需 premise DAG extraction pipeline。PGCT 需要证明显式 DAG 结构比 APRM 的自动 hard negative mining 效果更好——但 APRM 的 negatives 是自适应生成的，而 PGCT 的 negatives 是基于规则构造的（premise-link corruption），后者可能不够 hard。\n\n2. **Simple paraphrase augmentation**：仅使用 LLM paraphrase 生成同语义不同表述的 step 作为 additional training data（不需要 DAG），可能已经能提升部分 surface invariance，因为 PRM 会看到 \"不同表述→同样 correct\" 的信号。\n\n3. **Random step shuffling/dropping**：不使用 premise DAG，而是简单地随机打乱步骤引用或 drop 某些步骤作为 negative pairs，可能捕获部分 logical dependency signal。\n\n**增量价值论点**：PGCT 的增量价值在于——premise DAG 提供了精确的\"该保留什么、该破坏什么\"的信息，使得 graph-preserving perturbations 确保语义不变性，graph-breaking perturbations 精准打击逻辑依赖。但这个增量价值是否足以justify整个 DAG extraction + graph contrastive training pipeline 的复杂性，需要实验验证。这是一个 engineering bet，不是一个 conceptual breakthrough。\n\n【前提假设检验】:\n\n核心逻辑链中有几个未经验证的假设：\n\n1. **DAG extraction 在 PRM800K/Math-Shepherd 上的可靠性（关键假设）**：PARC 的 90% recall 是在 PERL 的特定评估集上报告的（使用 Llama-3.1-8B-Instruct）。PRM800K 和 Math-Shepherd 包含来自不同模型的 ~300K solutions，步骤格式和推理风格高度多样。DAG extraction 在这些异质数据上的 recall 和 precision 未知。如果 extraction 质量下降（比如降到 70%），则 contrastive pairs 中将包含大量噪声，可能反而损害训练。\n\n2. **Graph-breaking perturbations 的 validity（重要假设）**：\"severed premise link\" 可能不一定是 invalid reasoning——在数学中，同一结论可以从不同 premise 推出。一个看似 \"dangling reference\" 的步骤可能实际上是隐式使用了另一组前提。因此，graph-breaking negatives 可能包含 false negatives（标为错误但实际正确的样本），这会严重污染 contrastive signal。\n\n3. **InfoNCE 可以通过 DAG-anchored embeddings 学到 structure sensitivity（技术假设）**：标准 transformer 的 representation 已经编码了 positional/contextual 信息。额外的 InfoNCE loss 是否能教会 model 区分 \"DAG 完整\" vs \"DAG 破损\" 取决于 DAG-anchored embedding 的具体设计——但 proposal 对此缺乏技术细节（如何将 DAG topology 注入 embedding space？pooling over DAG subgraph？GNN layer？）。\n\n4. **43% stylistic shortcuts 的可纠正性假设**：proposal 默认这 43% 可以通过 structure-aware contrastive training 纠正。但 \"Reward Under Attack\" 的分析是在 RL-trained policies 上做的；PGCT 改进的是 PRM training，不直接改变 RL policy 的行为。即使 PRM 变得更 robust，policy 可能找到新的 attack surface。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心贡献是将 premise dependency DAGs（PARC/PERL, ICML 2025）与 contrastive PRM training 结合。确认搜索后，确实没有已发表工作做了完全相同的组合。然而，这个组合是**高度 predictable 的\"自然下一步\"**：任何同时读了 \"Reward Under Attack\"（fluency-logic dissociation）和 PARC/PERL（premise DAGs extractable at 90% recall）的研究者都会想到\"用 DAG 信息指导 training\"。与 APRM（arXiv:2511.22888）相比，PGCT 用显式结构替换了自适应对抗训练，这是一个 design choice 而非 paradigm shift。与 CRM（ICLR 2026）的 inter-step dependency modeling 在动机上高度重叠，只是实现路径不同。Novelty 在于 engineering combination，不在于 conceptual surprise。\n\n2. **Significance: 中** — \n   所瞄准的问题（PRM reward hacking）确实重要且被充分文档化——\"Reward Under Attack\" 和 \"Reward Models Identify Consistency Not Causality\" 都是高影响力工作。但 proposal 的目标改进幅度偏modest（PRMBench 67.7 → >70，仅 +2.3 points，vs. human ceiling 83.8）。更重要的是，领域内已有多个竞争方案（APRM +5.3pp OOD, CRM at ICLR 2026, GenPRM at AAAI 2026, PURE at NeurIPS 2025），PGCT 如果只是 \"another approach with marginal gains\"，影响力有限。如果核心发现是 positive（DAG-contrastive training 确实提升 robustness），审稿人更可能的反应是 \"makes sense, good to see it confirmed\" 而非 \"surprising, changes how I think about the problem.\"\n\n3. **Related Work: 强** — \n   proposal 展现了对领域的深入了解。14 篇引用中，经我验证的关键论文（Reward Under Attack, PARC/PERL, CRM, APRM, CPMI, GenPRM, PRMBench, PathFinder-PRM）均真实存在，描述准确。对 concurrent work 的区分定位（CPMI 不用 DAG, CRM 不用 contrastive, RewardFlow 是 agentic tasks, GoV 是 training-free）清晰且公允。coverage 几乎涵盖了领域内所有主要方向。唯一遗漏的是 \"From Chains to DAGs\"（arXiv:2601.17593）和一些 2026 年初的新工作（如 \"Robust Reward Modeling via Causal Rubrics\"），但这些不影响核心定位。\n\n【概率估计】: [25% - 35%] 中位 30%\n\n【估计理由】: \nNovelty 是中——组合虽新但 predictable，这限制了概率上界（审稿人容易写出\"straightforward combination\"的评价）。Significance 同样是中——问题重要但改进幅度 modest 且竞争激烈。Related Work 的强表现为 proposal 提供了 solid 的定位基础，但 related work 好只能保下限不能拉上限。整体这是一个 \"well-motivated, well-positioned engineering contribution\"，在 AAAI 级别的 idea 评估中落在 25-35% 区间。如果实验执行出色（DAG extraction 质量高、在 adversarial robustness 上大幅超越 APRM），有可能突破 35%。但 idea 本身不具备让审稿人说 \"surprising\" 的力度。Novelty 是主要瓶颈维度。\n\n【主要风险】: \n1. **\"Natural combination\" 风险**：审稿人可能认为将 PARC/PERL 的 premise DAGs 用于 PRM contrastive training 是一个 obvious next step，novelty contribution 不足以支撑 top venue。APRM 和 CRM 已经以不同方式处理了 inter-step dependency 和 harder negatives 问题。\n2. **Trivial alternative 威胁**：如果 simple paraphrase augmentation（不使用 DAG 的 surface perturbation）或 APRM 式 adversarial training 能达到 comparable 效果，则 PGCT 复杂的 DAG pipeline 的增量价值不明确——这是审稿人最可能的 \"why not just...\" 质疑。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs](https://arxiv.org/abs/2502.02362)\n- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)\n- [Linking Process to Outcome: Conditional Reward Modeling (CRM)](https://arxiv.org/abs/2509.26578)\n- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [PathFinder-PRM on GitHub](https://github.com/declare-lab/PathFinder-PRM)\n- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/pdf/2601.17593)\n- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://arxiv.org/abs/2409.13156)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research material. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **Reward Under Attack (arXiv:2603.06621, Feb 2026)**:\n   直接激励本 proposal 的工作。确认 PRMs 作为\"fluency detectors\"存在系统性缺陷——43% reward gains 来自 stylistic shortcuts，policies 达到 >0.9 PRM scores 但 <4% accuracy。论文已验证存在，数据准确。\n\n2. **Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, Feb 2025)**:\n   Yuhui Xu 等人证实 reward models 优先关注 structural consistency 而非 causal correctness——移除问题陈述对 reward scores 影响极小，而改变数值或推理流程则显著影响输出。直接支持 proposal 的问题定义。\n\n3. **PARC/PERL (ICML 2025, arXiv:2502.02362)**:\n   本 proposal 的核心技术组件来源。验证确认：LLMs 在 premise identification 上达到 90% recall，error identification 提升 6-16%。但关键限制：仅用于评估时（evaluation-time），未用于 PRM 训练。Proposal 的 novelty claim（将 premise DAGs 用于训练时）基于此 gap 成立。\n\n4. **APRM — Adversarial Training for PRMs (arXiv:2511.22888, Nov 2025)**:\n   **最直接的 trivial alternative 威胁**。通过 Generator-PRM 对抗训练自动产生 harder negatives，无需 DAG 提取，OOD 提升 +5.3pp，无需人工标注。这是不依赖图结构就能提升 PRM 鲁棒性的方法。\n\n5. **CRM — Conditional Reward Modeling (arXiv:2509.26578, ICLR 2026)**:\n   通过条件概率建模 reasoning steps 间的因果关系，在 BoN、beam search、RL 中均优于已有 reward models，且对 reward hacking 更鲁棒。**隐式捕获了部分 step 间依赖关系**，无需显式 DAG。\n\n6. **CRA — Causal Reward Adjustment (arXiv:2508.04216, Aug 2025)**:\n   Post-hoc 方法，用 sparse autoencoders 提取 PRM 内部的 confounding features 并做 backdoor correction。不修改 PRM 训练过程。\n\n7. **CPMI (arXiv:2604.10660, April 2026)**:\n   使用 contrastive mutual information 做 PRM auto-labeling，降低 84% 标注时间和 98% token 生成。与本 proposal 的 contrastive 方向有交叉，但不使用 premise dependency graphs。\n\n8. **RewardFlow (arXiv:2603.18859, March 2026)**:\n   在 agentic 任务中通过 state-transition graphs 做 topology-aware reward propagation。不同 graph 类型（state graph vs. premise DAG），不同任务场景（agentic vs. math reasoning），无 contrastive training。\n\n9. **GenPRM (AAAI 2026, arXiv:2504.00891)**:\n   将 PRM 重新定义为 generative task，结合 CoT reasoning 和 code verification。1.5B GenPRM 超过 GPT-4o。代表 PRM 的另一个改进方向（generative vs. discriminative）。\n\n10. **AgentEval (arXiv:2604.23581, April 2026)**:\n    DAG-based dependency modeling 在 agentic workflow evaluation 中贡献 +22pp failure detection recall。支持\"DAG 结构有用\"的论点，但用于 evaluation 而非 training。\n\n11. **PRMBench (ACL 2025, arXiv:2501.03124) & PathFinder-PRM**:\n    当前 SOTA: PathFinder-PRM-7B 得分 67.7，human ceiling 83.8。Proposal 目标 >70（提升 ~2.3 分）。\n\n12. **PURE (NeurIPS 2025, arXiv:2504.15275)**:\n    Min-form credit assignment，聚焦 aggregation 策略而非训练信号改进。\n\n- **调研总结**: PRM robustness 是 2025-2026 年的活跃研究方向，已有多条技术路线（adversarial training、conditional modeling、causal correction、generative PRM、contrastive labeling）同时推进。本 proposal 占据的 niche 是\"premise dependency DAG + contrastive training\"的组合，该组合确实尚未被尝试。但这个 niche 的两侧——DAG 用于 evaluation（PARC/AgentEval）和 contrastive/adversarial PRM training（APRM/CPMI）——都已有成熟工作，使得本 proposal 本质上是一个\"将已有组件组合\"的工作。\n\n\n【Trivial Alternative 检验】:\n\n**存在实质性 trivial alternative 威胁，来自 APRM。**\n\nAPRM（arXiv:2511.22888）通过 adversarial training 自动生成 harder negatives，无需任何图结构提取，即可达到 OOD +5.3pp 的 PRM 鲁棒性提升。其核心机制——让 Generator 产生\"看起来对但实际上错\"的 reasoning steps 作为 hard negatives——与本 proposal 的\"graph-breaking fluent perturbations\"在功能上高度重叠，但省去了 DAG 提取这个复杂步骤。\n\n**增量价值在哪？** Proposal 需要论证：显式 DAG 结构提供的 contrastive signal 比 APRM 的 adversarial negatives 更 targeted、更有效。理论上的 argument 是：DAG-anchored perturbations 可以精准控制\"破坏什么逻辑关系\"，而 adversarial training 生成的 negatives 可能是 surface-level 的错误而非 structural 的错误。这个 argument 合理，但未经验证——如果 APRM 的 adversarial negatives 碰巧也主要在逻辑结构上犯错，那 DAG 的额外复杂度就没有意义。\n\n此外，CRM（ICLR 2026）通过 sequential conditioning 隐式捕获 step 间依赖，也可能达到类似效果。\n\n**结论：增量价值存在但需要实验验证，不是 self-evident 的。**\n\n\n【前提假设检验】:\n\n核心逻辑链有以下未经验证的环节：\n\n1. **DAG 提取质量足够支撑 contrastive training（关键假设）**：PARC 报告 90% recall，但 (a) precision 未报告——如果 false positive premise links 很多，DAG 结构本身就是噪声的；(b) 90% recall 是在 GSM8K/MATH 等相对简单的数据集上测量的，对更长、更复杂的推理链（如 PRM800K 中的 hard problems）recall 可能下降；(c) recall 是 step-level 的，而 contrastive training 需要 chain-level DAG 拓扑正确——单个 link 的错误可能导致整条 chain 的 perturbation 策略失效。\n\n2. **Graph-preserving perturbations 真的保持逻辑不变（关键假设）**：Proposal 假设 LLM paraphrasing 可以改变 surface form 但保持\"identical DAG topology\"。但 LLM paraphrasing 经常引入微妙的逻辑变化（如改变量词范围、改变条件关系），特别是在数学推理中，符号表达和自然语言的边界模糊。如果\"positive pairs\"中有显著比例实际上改变了逻辑结构，contrastive signal 将被严重污染。\n\n3. **InfoNCE loss 能在 PRM 的 representation space 中有效 disentangle surface form 和 logical structure（核心假设）**：这是最大的\"想当然\"假设。没有理论或先验实证表明，在 LLM 的 hidden representations 中，surface fluency 和 logical structure 是可以线性分离的。如果这两者在 representation space 中高度 entangled，contrastive loss 可能只是迫使模型学到另一组 shortcuts 而非真正的结构理解。\n\n4. **~600K contrastive pairs 的质量足以覆盖数学推理中的多样错误模式**：生成策略依赖于 LLM paraphrasing 和\"targeted premise-link corruption\"，但 corruption 策略的多样性和自然性（是否产生 realistic 的错误而非 trivially detectable 的 corruption）直接决定训练效果。这与 APRM 的 adversarial approach 形成对比——APRM 的 negatives 是 adversarially 产生的（模型认为对但实际错），而 PGCT 的 negatives 是 rule-based 产生的（按规则 corrupt premise links），后者可能更容易被学到 surface cues。\n\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   组合是新的（premise dependency DAG + contrastive PRM training），这一点在调研中得到确认——CPMI 做 contrastive 但无 DAG，APRM 做 harder negatives 但无 DAG，PARC 做 DAG 但只用于 evaluation，RewardFlow 做 graph propagation 但不同 graph 类型和不同任务。\"No prior work combines X with Y\"的 novelty claim 成立。\n   \n   **但这是 combination novelty，非 conceptual novelty。** 核心 insight——\"用结构信息做 contrastive training 来 disentangle form 和 content\"——是 NLP 中常见的 paradigm（如 syntax-aware contrastive learning、structure-preserving data augmentation），只是从未被应用到 PRM 场景。审稿人很可能认为这是一个\"natural next step\"而非一个 surprising insight。相比 CRM（提出 conditional probability 框架）或 GenPRM（将 PRM 从 discriminative 转为 generative），PGCT 的 conceptual contribution 更浅。\n\n2. **Significance: 中偏强** — \n   问题本身非常重要且 timely。PRM robustness 直接影响 reasoning-focused RL training 的效果，\"Reward Under Attack\" 和 \"Consistency Not Causality\" 已经引起社区广泛关注。PRMBench 的 67.7 vs. 83.8 human ceiling gap（16 分）说明改进空间巨大。如果 PGCT 确实能 substantially reduce adversarial exploitability，impact 将是显著的。\n   \n   **但目标 improvement 偏保守**（>70 vs. 67.7 = +2.3 分），如果最终 improvement 在这个量级，审稿人可能认为 marginal。此外，方法依赖 PARC 的 premise extraction（目前仅在数学推理上验证），可推广性受限。\n\n3. **Related Work: 强** — \n   这是本 proposal 最强的维度。15 篇核心引用全部经过验证均为真实存在的论文，描述准确。对竞争工作（APRM、CRM、CRA、CPMI、RewardFlow、GoV）的差异化定位清晰且准确——每个都指出了\"它做了什么、没做什么\"。对 infrastructure 工作（PARC、GenPRM、AgentEval）的利用恰当。对 concurrent work 的覆盖全面。\n   \n   唯一略微薄弱之处：没有充分讨论 PathFinder-PRM（当前 PRMBench SOTA）的具体方法及与 PGCT 的 complementarity/competition 关系。\n\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】:\nSignificance 是本 proposal 的最大资产——问题真实、重要、timely，审稿人会认可动机。Related Work 的覆盖质量也出色，不会在这方面失分。\n\n但 Novelty 限制了上界。这本质上是一个\"put A and B together\"的组合工作，核心 insight 不 surprising。如果实验结果强（e.g., PRMBench >72, adversarial robustness 大幅提升），组合 novelty 可以被接受；但如果实验结果 marginal（PRMBench ~70-71），审稿人很可能评价为\"incremental combination of known techniques\"。\n\nAPRM 的存在是另一个上界约束：如果不与 APRM 做充分的 head-to-head comparison 并展示 clear superiority，审稿人会质疑\"为什么不直接用 adversarial training\"。\n\n概率区间 22%-33% 反映了：下界考虑了 trivial alternative 威胁和前提假设风险（如果 DAG 质量不够或 APRM 同样有效，story 会被严重削弱）；上界考虑了如果实验结果 surprising strong，组合 novelty 在 AAAI 是可以被接受的。中位 27% 反映了\"solid but not exciting\"的 idea 质量。\n\n【主要风险】:\n1. **Trivial Alternative 被坐实**：如果 APRM（无需 DAG 的 adversarial training）在相同 benchmark 上达到 comparable 或更好的 robustness 提升，PGCT 的 incremental value 将无法自证，审稿人会认为 DAG extraction 是不必要的 complexity。\n2. **Contrastive Pair 质量难以保证**：graph-preserving paraphrases 可能引入微妙逻辑变化，graph-breaking corruptions 可能过于 artificial，导致 contrastive signal 在噪声中失效——这是一个 idea 层面的风险，因为整个方法论的有效性取决于 pair 质量，而这个质量目前只是假设。\n```\n\nSources:\n- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs](https://arxiv.org/abs/2502.02362)\n- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)\n- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://arxiv.org/abs/2509.26578)\n- [CRA: Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction](https://arxiv.org/abs/2508.04216)\n- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)\n- [RewardFlow: Topology-Aware Reward Propagation on State Graphs](https://arxiv.org/abs/2603.18859)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows](https://arxiv.org/abs/2604.23581)\n- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?\n\n## Research Opportunity\n\nPERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.\n\n## Research Landscape\n\nThe field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.\n\n## Proposed Approach\n\nExtract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.\n\n## Detailed Description\n\nWe propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.\n\n## Key References\n\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)\n- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)\n- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)\n- Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)\n- Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)\n- AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)\n- Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h), timeline: 14-18 weeks for 2-3 researchers, estimated_gpu_cost: $2,100-$3,000 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%), timeline: 10-14 weeks for 2 researchers, claude_api_cost: $400-$700 (data quality analysis, code generation, experiment triage), estimated_gpu_cost: $1,500-$2,100 at $3/hr A100 spot pricing\n- **auto_research**: gpu_hours: 800-1200 A100-hours (more parallel sweeps offset by automated experiment selection), timeline: 6-8 weeks with automated pipeline, claude_api_cost: $1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting), estimated_gpu_cost: $2,400-$3,600 at $3/hr A100 spot pricing, speed_bottleneck: DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T08:21:05.950Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:21:05.950Z",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T08:21:05.965Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient data to make a well-informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. [Reward Under Attack, arXiv:2603.06621] (arXiv, Feb 2026):
   直接验证了 proposal 的核心问题——PRM 在 RL 训练中被 exploit 到 >0.9 reward 但 <4% accuracy，43% reward gains 来自 stylistic shortcuts。论文确认 PRM 本质上是 fluency detector。这是本 proposal 的问题基础，描述准确。

2. [Reward Models Identify Consistency, Not Causality, arXiv:2502.14619] (arXiv, Feb 2025):
   确认 reward model 优先评估 structural consistency 而非 causal correctness——移除 problem statement 对 reward 影响甚微，但改变数值或 reasoning flow 影响显著。这为 proposal 的 "fluency ≠ validity" 论点提供了理论基础。

3. [PARC/PERL, arXiv:2502.02362] (ICML 2025):
   真实存在且已被 ICML 2025 录用。确认 open-source LLM 可以 90% recall 提取 premise dependency links，形成 DAG 结构。PERL 证明 premise-aware verification 提升 error detection 6-16%。但关键点是：PERL 仅在 evaluation time 使用这些结构信息，未用于 PRM training。

4. [CRM — Linking Process to Outcome, arXiv:2509.26578] (ICLR 2026):
   通过 conditional probability rules 建模 reasoning steps 间的因果关系，sequential conditioning on preceding steps。与本 proposal 的区别是 CRM 使用隐式序列依赖而非显式 DAG 结构，且无 contrastive training。

5. [APRM — Adversarial Training for Process Reward Models, arXiv:2511.22888] (arXiv, Nov 2025):
   Generator-PRM 对抗训练框架，自动生成 harder negatives，OOD +5.3pp。**这是最重要的 trivial alternative 威胁**——APRM 同样通过 hard negatives 训练 PRM，只是 negatives 来源不同（adversarial generation vs. structure-aware corruption）。

6. [CPMI — Contrastive Mutual Information for PRM, arXiv:2604.10660] (arXiv, April 2026):
   用 contrastive pointwise mutual information 做 PRM auto-labeling，减少 84% 数据构建时间。与本 proposal 的区别：CPMI 用 contrastive 方法做 labeling 而非 training representation，且不使用 premise DAG。

7. [Graph of Verification (GoV), arXiv:2506.12509] (arXiv, 2025):
   将 reasoning 建模为 DAG 并按 topological sort 逐节点验证。Training-free 方法。与本 proposal 互补但不竞争——GoV 是 inference-time DAG 使用，本 proposal 是 training-time DAG 使用。

8. [RewardFlow, arXiv:2603.18859] (arXiv, March 2026):
   在 state graph 上做 topology-aware reward propagation，面向 agentic tasks。使用不同类型的 graph（state-transition graph vs. premise dependency DAG），无 contrastive training。

9. [GenPRM, arXiv:2504.00891] (AAAI 2026):
   将 process supervision 重新定义为 generative task（CoT + code verification），而非 discriminative scoring。与本 proposal 正交——GenPRM 改变 PRM 的 paradigm（discriminative → generative），本 proposal 仍在 discriminative PRM 框架内改进 training signal。

10. [PRMBench, arXiv:2501.03124] (ACL 2025):
    SOTA 为 PathFinder-PRM-7B 的 67.7（Gemini-2-Thinking 68.8），human ceiling 83.8。16-point gap 确实存在。

11. [PURE — Min-Form Credit Assignment, arXiv:2504.15275] (NeurIPS 2025):
    通过 min-form credit aggregation 替代 summation，改进 PRM reward propagation。无 graph structure 使用。

- 调研总结：PRM robustness 是 2025-2026 年的活跃研究前沿，已有多条技术路线（adversarial training, conditional modeling, credit assignment, generative PRM, post-hoc correction）。"premise DAG + contrastive PRM training" 的具体组合确实未被尝试，但各组件（DAG extraction, contrastive training, structure-aware negatives）均为成熟技术。该领域竞争激烈，多个 concurrent work 从不同角度攻克同一问题。


【Trivial Alternative 检验】:

存在两个有意义的 trivial alternative 威胁：

(1) **APRM (adversarial training)**：APRM 已经通过 adversarial generator 自动产生 harder negatives 来训练 PRM，OOD +5.3pp。本 proposal 的 structure-aware negatives（通过 premise-link corruption 生成）与 APRM 的 adversarial negatives 在功能上高度相似——都是产生"表面流畅但逻辑有问题"的 hard negatives。PGCT 的增量价值在于：negatives 的生成是 *有针对性的*（精确破坏特定 premise link），而非 APRM 的 *盲目对抗*。但这个增量是否足够 significant 需要实验验证——如果 APRM 的 adversarial generator 恰好已经学会了类似的 premise-link corruption 模式，则 PGCT 的增量可能很小。

(2) **PERL at inference time + standard PRM**：PERL 已证明 premise-aware verification 在 evaluation time 提升 6-16%。一个简单的 pipeline——标准 PRM + PERL-style inference-time DAG verification——可能已经捕获了大部分结构信息的收益。PGCT 的论点是"在 training time 注入结构信息比 inference time 使用更根本"，但这需要实验对比。

增量价值存在但需要证明：PGCT 的核心 bet 是 *training-time structural inductive bias* 优于 *inference-time structural post-processing* 和 *adversarial hard negative generation*。这个 bet 是 reasonable 的，但不是显然成立的。


【前提假设检验】:

核心逻辑链条中有以下未经验证的环节：

(1) **"Premise DAG structure is the right inductive bias for disentangling fluency from logic"**——这是最核心的假设。"Reward Under Attack" 证明了 PRM 是 fluency detector，"Consistency Not Causality" 证明了 PRM 检测 consistency 而非 causality。但从"PRM 不理解逻辑结构"到"注入 premise DAG 可以修复这个问题"之间存在 gap。逻辑结构可以有多种表征方式（premise DAG 只是其中之一），且 PRM 的 fluency bias 可能根植于 transformer representation 的特性，不一定能被 contrastive loss 克服。

(2) **"90% recall DAG extraction → good enough training signal"**——PARC 在 Llama-3.1-8B-Instruct 上达到 90% recall，但 precision 未详细讨论。10% 的 missing links + unknown false positive rate 意味着部分 "graph-preserving" perturbations 实际上可能改变了 DAG topology，部分 "graph-breaking" perturbations 可能保留了真实 DAG。噪声训练信号可能削弱甚至反向影响 contrastive learning 效果。

(3) **"InfoNCE loss over DAG-anchored embeddings can effectively force surface-form invariance"**——contrastive learning 在 vision (SimCLR) 和 NLP (SimCSE) 中的成功不能直接外推到 "logical structure invariance" 场景。Surface-form invariance 和 logical-structure sensitivity 是否能通过单一 contrastive objective 同时实现，理论上不确定。

(4) **"LLM paraphrasing produces genuine graph-preserving perturbations"**——proposal 假设 LLM 可以 rephrase reasoning steps while maintaining identical DAG topology。但 rephrasing 数学推理步骤时，subtle changes in phrasing 可能 implicitly 改变 premise references，导致 DAG topology 的 silent drift。


【3 维度打分】:

1. **Novelty: 中** — "premise DAG + contrastive training + PRM" 的具体组合确实未被尝试（CPMI 用 contrastive 但无 DAG；GoV 用 DAG 但 training-free；APRM 用 hard negatives 但无 structural guidance；CRM 用 sequential conditioning 但非显式 DAG）。然而，这是**组合式创新而非概念性创新**。核心 insight——"用 structural information 指导 PRM training"——是一个自然的、可预测的 next step。PERL 已经证明 premise structure 在 evaluation 时有帮助，将其"推到 training 阶段"是顺理成章的工程延伸。如果实验证明 positive，审稿人很可能说 "I would have guessed this works" 而非 "this is surprising"。

2. **Significance: 中偏强** — PRM robustness 是当前 reasoning with LLMs 领域的核心瓶颈之一，"Reward Under Attack" 和 "Consistency Not Causality" 已经确立了这个问题的 urgency。43% stylistic shortcuts 和 <4% accuracy under reward hacking 是触目惊心的数字。如果 PGCT 确实能大幅降低 adversarial exploitability，这对整个 RLHF for reasoning 领域有实质意义。但 proposal 的 target improvement（PRMBench 67.7 → >70）幅度较小（~2.3 points），如果最终实验结果是这个量级，impact 会被打折。

3. **Related Work: 强** — Proposal 对领域景观的覆盖非常全面且准确。所有引用的论文经验证均真实存在且描述准确（PARC/PERL at ICML 2025、CRM at ICLR 2026、GenPRM at AAAI 2026、PRMBench at ACL 2025 等）。对 concurrent work（CPMI、RewardFlow、GoV）的差异化定位清晰。唯一可补充的是 Crome（Causally Robust Reward Modeling）和 GRP（Graph Reasoning Paradigm）等更近期的 concurrent work，但这不影响整体评价。


【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
Significance 接近"强"，拉高了下限——问题是真实的、重要的、有定量证据支撑的。Related Work 覆盖"强"，进一步巩固了 proposal 的基础质量。但 **Novelty 的"中"评级严重限制了上界**：核心贡献是组合式创新（将 PERL 的 premise DAG 从 inference time 推到 training time + 加 contrastive loss），intellectual contribution 的深度不足以让审稿人感到 surprised。此外，APRM 作为 trivial alternative 的威胁是实质性的——如果 adversarial training 已经能产生足够好的 hard negatives，则 PGCT 的 structure-aware negatives 可能只是 marginal improvement。PRMBench 上 2.3 点的目标提升也偏保守，不够 impressive。综合来看，这是一个 solid engineering contribution，但在 AAAI 的 novelty 标准下偏弱，概率集中在 25-30% 区间。

【主要风险】:
1. **Novelty 不足 / "incremental extension" 质疑**：审稿人可能认为这只是 PERL (inference-time premise DAG) 的自然训练时延伸 + 标准 contrastive learning 框架的直接应用，缺乏深层技术洞见。"Why not just use APRM which already generates hard negatives?" 是一个难以回避的问题。
2. **Expected results not surprising**：如果 "使用逻辑结构信息训练 PRM → PRM 更理解逻辑结构"，这个结果过于 intuitive。审稿人可能写 "The approach is sound but the finding, if positive, is expected rather than insightful"——这在 top venue 是常见的 borderline reject 理由。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL — Premise-Augmented Reasoning Chains (ICML 2025)](https://arxiv.org/abs/2502.02362)
- [CRM — Linking Process to Outcome (ICLR 2026)](https://arxiv.org/abs/2509.26578)
- [APRM — Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [CPMI — Contrastive Mutual Information for PRM](https://arxiv.org/abs/2604.10660)
- [Graph of Verification (GoV)](https://arxiv.org/abs/2506.12509)
- [RewardFlow](https://arxiv.org/abs/2603.18859)
- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [PRMBench (ACL 2025)](https://arxiv.org/abs/2501.03124)
- [AgentEval](https://arxiv.org/abs/2604.23581)
- [DAG-Math](https://arxiv.org/abs/2510.19842)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

1. "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv:2603.06621, Feb 2026):
   - 本 proposal 的核心动机来源。证实 PRMs 在对抗压力下系统性可被利用，43% 的 RL reward gain 归因于 stylistic shortcuts，策略在 AIME 上达到 >0.9 PRM reward 但 <4% 真实准确率。提出了 fluency-logic dissociation 现象。
   - 论文确实存在，描述准确。

2. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025):
   - Xu et al. 证明 reward model 优先评估 structural consistency 而非 causal correctness——移除问题陈述对 reward 影响甚微，但改变数值或打断推理流程显著影响 RM 输出。
   - 论文确实存在，描述准确。

3. PARC/PERL (arXiv:2502.02362, ICML 2025):
   - 将线性推理链重构为 premise-augmented reasoning chains (DAG)，证明开源 LLM 在 premise identification 上达到 90% recall，基于 premise 的验证将错误识别准确率提升 6-16%。
   - 论文确实存在，描述准确。

4. APRM — Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025):
   - Generator-PRM 对抗博弈框架，通过渐进式更难 negatives 训练，平均 +3.4pp（OOD +5.3pp）。
   - **与本 proposal 直接竞争**：同样目标是提升 PRM 对 novel errors 的泛化，但不使用显式逻辑结构。

5. CRM — Conditional Reward Modeling (arXiv:2509.26578, ICLR 2026):
   - 将推理建模为 temporal process，reward 条件化于前序 steps 和最终结果，捕获 inter-step causal relationships。
   - 与本 proposal 关注 inter-step dependencies 有重叠，但不使用 premise DAG 也不使用 contrastive training。

6. CPMI — Contrastive Mutual Information for PRM (arXiv:2604.10660, April 2026):
   - 用 contrastive pointwise mutual information 进行自动 step-level reward labeling，相比 MC 估计减少 84% 标注时间。
   - 使用 contrastive 思想但用途不同（labeling vs. training），不涉及 premise graphs。

7. GenPRM (arXiv:2504.00891, AAAI 2026):
   - 将 process supervision 重新定义为生成式任务，结合 CoT reasoning 和 code verification。已被 AAAI 2026 接收。
   - 不同范式（generative vs. discriminative），与本 proposal 正交。

8. PathFinder-PRM (2025):
   - PRMBench 当前 SOTA 67.7（human ceiling 83.8），通过分层 error-aware supervision 实现。
   - 本 proposal 的 benchmark target 基准。

9. "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs" (arXiv:2601.17593, 2026):
   - 分析 LLM 内部表示中 DAG 结构的可恢复性，发现中间层达到峰值。
   - 为 DAG-based 方法提供了额外理论支撑，但 proposal 未引用此工作。

- **调研总结**: PRM 鲁棒性是 2025-2026 年的热点方向，已有多种攻击角度的改进方案（adversarial training、conditional modeling、contrastive labeling、generative verification），但尚无工作将 premise dependency DAGs 显式融入 PRM contrastive training。该领域竞争激烈，新方法需要在多个 benchmark 上展现显著优势才能脱颖而出。

【Trivial Alternative 检验】:

存在多个更简单的替代方案可能部分实现类似效果：

1. **APRM 式 adversarial training**：已证明通过对抗博弈生成 harder negatives 可以 OOD +5.3pp，无需 premise DAG extraction pipeline。PGCT 需要证明显式 DAG 结构比 APRM 的自动 hard negative mining 效果更好——但 APRM 的 negatives 是自适应生成的，而 PGCT 的 negatives 是基于规则构造的（premise-link corruption），后者可能不够 hard。

2. **Simple paraphrase augmentation**：仅使用 LLM paraphrase 生成同语义不同表述的 step 作为 additional training data（不需要 DAG），可能已经能提升部分 surface invariance，因为 PRM 会看到 "不同表述→同样 correct" 的信号。

3. **Random step shuffling/dropping**：不使用 premise DAG，而是简单地随机打乱步骤引用或 drop 某些步骤作为 negative pairs，可能捕获部分 logical dependency signal。

**增量价值论点**：PGCT 的增量价值在于——premise DAG 提供了精确的"该保留什么、该破坏什么"的信息，使得 graph-preserving perturbations 确保语义不变性，graph-breaking perturbations 精准打击逻辑依赖。但这个增量价值是否足以justify整个 DAG extraction + graph contrastive training pipeline 的复杂性，需要实验验证。这是一个 engineering bet，不是一个 conceptual breakthrough。

【前提假设检验】:

核心逻辑链中有几个未经验证的假设：

1. **DAG extraction 在 PRM800K/Math-Shepherd 上的可靠性（关键假设）**：PARC 的 90% recall 是在 PERL 的特定评估集上报告的（使用 Llama-3.1-8B-Instruct）。PRM800K 和 Math-Shepherd 包含来自不同模型的 ~300K solutions，步骤格式和推理风格高度多样。DAG extraction 在这些异质数据上的 recall 和 precision 未知。如果 extraction 质量下降（比如降到 70%），则 contrastive pairs 中将包含大量噪声，可能反而损害训练。

2. **Graph-breaking perturbations 的 validity（重要假设）**："severed premise link" 可能不一定是 invalid reasoning——在数学中，同一结论可以从不同 premise 推出。一个看似 "dangling reference" 的步骤可能实际上是隐式使用了另一组前提。因此，graph-breaking negatives 可能包含 false negatives（标为错误但实际正确的样本），这会严重污染 contrastive signal。

3. **InfoNCE 可以通过 DAG-anchored embeddings 学到 structure sensitivity（技术假设）**：标准 transformer 的 representation 已经编码了 positional/contextual 信息。额外的 InfoNCE loss 是否能教会 model 区分 "DAG 完整" vs "DAG 破损" 取决于 DAG-anchored embedding 的具体设计——但 proposal 对此缺乏技术细节（如何将 DAG topology 注入 embedding space？pooling over DAG subgraph？GNN layer？）。

4. **43% stylistic shortcuts 的可纠正性假设**：proposal 默认这 43% 可以通过 structure-aware contrastive training 纠正。但 "Reward Under Attack" 的分析是在 RL-trained policies 上做的；PGCT 改进的是 PRM training，不直接改变 RL policy 的行为。即使 PRM 变得更 robust，policy 可能找到新的 attack surface。

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将 premise dependency DAGs（PARC/PERL, ICML 2025）与 contrastive PRM training 结合。确认搜索后，确实没有已发表工作做了完全相同的组合。然而，这个组合是**高度 predictable 的"自然下一步"**：任何同时读了 "Reward Under Attack"（fluency-logic dissociation）和 PARC/PERL（premise DAGs extractable at 90% recall）的研究者都会想到"用 DAG 信息指导 training"。与 APRM（arXiv:2511.22888）相比，PGCT 用显式结构替换了自适应对抗训练，这是一个 design choice 而非 paradigm shift。与 CRM（ICLR 2026）的 inter-step dependency modeling 在动机上高度重叠，只是实现路径不同。Novelty 在于 engineering combination，不在于 conceptual surprise。

2. **Significance: 中** — 
   所瞄准的问题（PRM reward hacking）确实重要且被充分文档化——"Reward Under Attack" 和 "Reward Models Identify Consistency Not Causality" 都是高影响力工作。但 proposal 的目标改进幅度偏modest（PRMBench 67.7 → >70，仅 +2.3 points，vs. human ceiling 83.8）。更重要的是，领域内已有多个竞争方案（APRM +5.3pp OOD, CRM at ICLR 2026, GenPRM at AAAI 2026, PURE at NeurIPS 2025），PGCT 如果只是 "another approach with marginal gains"，影响力有限。如果核心发现是 positive（DAG-contrastive training 确实提升 robustness），审稿人更可能的反应是 "makes sense, good to see it confirmed" 而非 "surprising, changes how I think about the problem."

3. **Related Work: 强** — 
   proposal 展现了对领域的深入了解。14 篇引用中，经我验证的关键论文（Reward Under Attack, PARC/PERL, CRM, APRM, CPMI, GenPRM, PRMBench, PathFinder-PRM）均真实存在，描述准确。对 concurrent work 的区分定位（CPMI 不用 DAG, CRM 不用 contrastive, RewardFlow 是 agentic tasks, GoV 是 training-free）清晰且公允。coverage 几乎涵盖了领域内所有主要方向。唯一遗漏的是 "From Chains to DAGs"（arXiv:2601.17593）和一些 2026 年初的新工作（如 "Robust Reward Modeling via Causal Rubrics"），但这些不影响核心定位。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 是中——组合虽新但 predictable，这限制了概率上界（审稿人容易写出"straightforward combination"的评价）。Significance 同样是中——问题重要但改进幅度 modest 且竞争激烈。Related Work 的强表现为 proposal 提供了 solid 的定位基础，但 related work 好只能保下限不能拉上限。整体这是一个 "well-motivated, well-positioned engineering contribution"，在 AAAI 级别的 idea 评估中落在 25-35% 区间。如果实验执行出色（DAG extraction 质量高、在 adversarial robustness 上大幅超越 APRM），有可能突破 35%。但 idea 本身不具备让审稿人说 "surprising" 的力度。Novelty 是主要瓶颈维度。

【主要风险】: 
1. **"Natural combination" 风险**：审稿人可能认为将 PARC/PERL 的 premise DAGs 用于 PRM contrastive training 是一个 obvious next step，novelty contribution 不足以支撑 top venue。APRM 和 CRM 已经以不同方式处理了 inter-step dependency 和 harder negatives 问题。
2. **Trivial alternative 威胁**：如果 simple paraphrase augmentation（不使用 DAG 的 surface perturbation）或 APRM 式 adversarial training 能达到 comparable 效果，则 PGCT 复杂的 DAG pipeline 的增量价值不明确——这是审稿人最可能的 "why not just..." 质疑。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs](https://arxiv.org/abs/2502.02362)
- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)
- [Linking Process to Outcome: Conditional Reward Modeling (CRM)](https://arxiv.org/abs/2509.26578)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [PathFinder-PRM on GitHub](https://github.com/declare-lab/PathFinder-PRM)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/pdf/2601.17593)
- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://arxiv.org/abs/2409.13156)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research material. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **Reward Under Attack (arXiv:2603.06621, Feb 2026)**:
   直接激励本 proposal 的工作。确认 PRMs 作为"fluency detectors"存在系统性缺陷——43% reward gains 来自 stylistic shortcuts，policies 达到 >0.9 PRM scores 但 <4% accuracy。论文已验证存在，数据准确。

2. **Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, Feb 2025)**:
   Yuhui Xu 等人证实 reward models 优先关注 structural consistency 而非 causal correctness——移除问题陈述对 reward scores 影响极小，而改变数值或推理流程则显著影响输出。直接支持 proposal 的问题定义。

3. **PARC/PERL (ICML 2025, arXiv:2502.02362)**:
   本 proposal 的核心技术组件来源。验证确认：LLMs 在 premise identification 上达到 90% recall，error identification 提升 6-16%。但关键限制：仅用于评估时（evaluation-time），未用于 PRM 训练。Proposal 的 novelty claim（将 premise DAGs 用于训练时）基于此 gap 成立。

4. **APRM — Adversarial Training for PRMs (arXiv:2511.22888, Nov 2025)**:
   **最直接的 trivial alternative 威胁**。通过 Generator-PRM 对抗训练自动产生 harder negatives，无需 DAG 提取，OOD 提升 +5.3pp，无需人工标注。这是不依赖图结构就能提升 PRM 鲁棒性的方法。

5. **CRM — Conditional Reward Modeling (arXiv:2509.26578, ICLR 2026)**:
   通过条件概率建模 reasoning steps 间的因果关系，在 BoN、beam search、RL 中均优于已有 reward models，且对 reward hacking 更鲁棒。**隐式捕获了部分 step 间依赖关系**，无需显式 DAG。

6. **CRA — Causal Reward Adjustment (arXiv:2508.04216, Aug 2025)**:
   Post-hoc 方法，用 sparse autoencoders 提取 PRM 内部的 confounding features 并做 backdoor correction。不修改 PRM 训练过程。

7. **CPMI (arXiv:2604.10660, April 2026)**:
   使用 contrastive mutual information 做 PRM auto-labeling，降低 84% 标注时间和 98% token 生成。与本 proposal 的 contrastive 方向有交叉，但不使用 premise dependency graphs。

8. **RewardFlow (arXiv:2603.18859, March 2026)**:
   在 agentic 任务中通过 state-transition graphs 做 topology-aware reward propagation。不同 graph 类型（state graph vs. premise DAG），不同任务场景（agentic vs. math reasoning），无 contrastive training。

9. **GenPRM (AAAI 2026, arXiv:2504.00891)**:
   将 PRM 重新定义为 generative task，结合 CoT reasoning 和 code verification。1.5B GenPRM 超过 GPT-4o。代表 PRM 的另一个改进方向（generative vs. discriminative）。

10. **AgentEval (arXiv:2604.23581, April 2026)**:
    DAG-based dependency modeling 在 agentic workflow evaluation 中贡献 +22pp failure detection recall。支持"DAG 结构有用"的论点，但用于 evaluation 而非 training。

11. **PRMBench (ACL 2025, arXiv:2501.03124) & PathFinder-PRM**:
    当前 SOTA: PathFinder-PRM-7B 得分 67.7，human ceiling 83.8。Proposal 目标 >70（提升 ~2.3 分）。

12. **PURE (NeurIPS 2025, arXiv:2504.15275)**:
    Min-form credit assignment，聚焦 aggregation 策略而非训练信号改进。

- **调研总结**: PRM robustness 是 2025-2026 年的活跃研究方向，已有多条技术路线（adversarial training、conditional modeling、causal correction、generative PRM、contrastive labeling）同时推进。本 proposal 占据的 niche 是"premise dependency DAG + contrastive training"的组合，该组合确实尚未被尝试。但这个 niche 的两侧——DAG 用于 evaluation（PARC/AgentEval）和 contrastive/adversarial PRM training（APRM/CPMI）——都已有成熟工作，使得本 proposal 本质上是一个"将已有组件组合"的工作。


【Trivial Alternative 检验】:

**存在实质性 trivial alternative 威胁，来自 APRM。**

APRM（arXiv:2511.22888）通过 adversarial training 自动生成 harder negatives，无需任何图结构提取，即可达到 OOD +5.3pp 的 PRM 鲁棒性提升。其核心机制——让 Generator 产生"看起来对但实际上错"的 reasoning steps 作为 hard negatives——与本 proposal 的"graph-breaking fluent perturbations"在功能上高度重叠，但省去了 DAG 提取这个复杂步骤。

**增量价值在哪？** Proposal 需要论证：显式 DAG 结构提供的 contrastive signal 比 APRM 的 adversarial negatives 更 targeted、更有效。理论上的 argument 是：DAG-anchored perturbations 可以精准控制"破坏什么逻辑关系"，而 adversarial training 生成的 negatives 可能是 surface-level 的错误而非 structural 的错误。这个 argument 合理，但未经验证——如果 APRM 的 adversarial negatives 碰巧也主要在逻辑结构上犯错，那 DAG 的额外复杂度就没有意义。

此外，CRM（ICLR 2026）通过 sequential conditioning 隐式捕获 step 间依赖，也可能达到类似效果。

**结论：增量价值存在但需要实验验证，不是 self-evident 的。**


【前提假设检验】:

核心逻辑链有以下未经验证的环节：

1. **DAG 提取质量足够支撑 contrastive training（关键假设）**：PARC 报告 90% recall，但 (a) precision 未报告——如果 false positive premise links 很多，DAG 结构本身就是噪声的；(b) 90% recall 是在 GSM8K/MATH 等相对简单的数据集上测量的，对更长、更复杂的推理链（如 PRM800K 中的 hard problems）recall 可能下降；(c) recall 是 step-level 的，而 contrastive training 需要 chain-level DAG 拓扑正确——单个 link 的错误可能导致整条 chain 的 perturbation 策略失效。

2. **Graph-preserving perturbations 真的保持逻辑不变（关键假设）**：Proposal 假设 LLM paraphrasing 可以改变 surface form 但保持"identical DAG topology"。但 LLM paraphrasing 经常引入微妙的逻辑变化（如改变量词范围、改变条件关系），特别是在数学推理中，符号表达和自然语言的边界模糊。如果"positive pairs"中有显著比例实际上改变了逻辑结构，contrastive signal 将被严重污染。

3. **InfoNCE loss 能在 PRM 的 representation space 中有效 disentangle surface form 和 logical structure（核心假设）**：这是最大的"想当然"假设。没有理论或先验实证表明，在 LLM 的 hidden representations 中，surface fluency 和 logical structure 是可以线性分离的。如果这两者在 representation space 中高度 entangled，contrastive loss 可能只是迫使模型学到另一组 shortcuts 而非真正的结构理解。

4. **~600K contrastive pairs 的质量足以覆盖数学推理中的多样错误模式**：生成策略依赖于 LLM paraphrasing 和"targeted premise-link corruption"，但 corruption 策略的多样性和自然性（是否产生 realistic 的错误而非 trivially detectable 的 corruption）直接决定训练效果。这与 APRM 的 adversarial approach 形成对比——APRM 的 negatives 是 adversarially 产生的（模型认为对但实际错），而 PGCT 的 negatives 是 rule-based 产生的（按规则 corrupt premise links），后者可能更容易被学到 surface cues。


【3 维度打分】:

1. **Novelty: 中** — 
   组合是新的（premise dependency DAG + contrastive PRM training），这一点在调研中得到确认——CPMI 做 contrastive 但无 DAG，APRM 做 harder negatives 但无 DAG，PARC 做 DAG 但只用于 evaluation，RewardFlow 做 graph propagation 但不同 graph 类型和不同任务。"No prior work combines X with Y"的 novelty claim 成立。
   
   **但这是 combination novelty，非 conceptual novelty。** 核心 insight——"用结构信息做 contrastive training 来 disentangle form 和 content"——是 NLP 中常见的 paradigm（如 syntax-aware contrastive learning、structure-preserving data augmentation），只是从未被应用到 PRM 场景。审稿人很可能认为这是一个"natural next step"而非一个 surprising insight。相比 CRM（提出 conditional probability 框架）或 GenPRM（将 PRM 从 discriminative 转为 generative），PGCT 的 conceptual contribution 更浅。

2. **Significance: 中偏强** — 
   问题本身非常重要且 timely。PRM robustness 直接影响 reasoning-focused RL training 的效果，"Reward Under Attack" 和 "Consistency Not Causality" 已经引起社区广泛关注。PRMBench 的 67.7 vs. 83.8 human ceiling gap（16 分）说明改进空间巨大。如果 PGCT 确实能 substantially reduce adversarial exploitability，impact 将是显著的。
   
   **但目标 improvement 偏保守**（>70 vs. 67.7 = +2.3 分），如果最终 improvement 在这个量级，审稿人可能认为 marginal。此外，方法依赖 PARC 的 premise extraction（目前仅在数学推理上验证），可推广性受限。

3. **Related Work: 强** — 
   这是本 proposal 最强的维度。15 篇核心引用全部经过验证均为真实存在的论文，描述准确。对竞争工作（APRM、CRM、CRA、CPMI、RewardFlow、GoV）的差异化定位清晰且准确——每个都指出了"它做了什么、没做什么"。对 infrastructure 工作（PARC、GenPRM、AgentEval）的利用恰当。对 concurrent work 的覆盖全面。
   
   唯一略微薄弱之处：没有充分讨论 PathFinder-PRM（当前 PRMBench SOTA）的具体方法及与 PGCT 的 complementarity/competition 关系。


【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
Significance 是本 proposal 的最大资产——问题真实、重要、timely，审稿人会认可动机。Related Work 的覆盖质量也出色，不会在这方面失分。

但 Novelty 限制了上界。这本质上是一个"put A and B together"的组合工作，核心 insight 不 surprising。如果实验结果强（e.g., PRMBench >72, adversarial robustness 大幅提升），组合 novelty 可以被接受；但如果实验结果 marginal（PRMBench ~70-71），审稿人很可能评价为"incremental combination of known techniques"。

APRM 的存在是另一个上界约束：如果不与 APRM 做充分的 head-to-head comparison 并展示 clear superiority，审稿人会质疑"为什么不直接用 adversarial training"。

概率区间 22%-33% 反映了：下界考虑了 trivial alternative 威胁和前提假设风险（如果 DAG 质量不够或 APRM 同样有效，story 会被严重削弱）；上界考虑了如果实验结果 surprising strong，组合 novelty 在 AAAI 是可以被接受的。中位 27% 反映了"solid but not exciting"的 idea 质量。

【主要风险】:
1. **Trivial Alternative 被坐实**：如果 APRM（无需 DAG 的 adversarial training）在相同 benchmark 上达到 comparable 或更好的 robustness 提升，PGCT 的 incremental value 将无法自证，审稿人会认为 DAG extraction 是不必要的 complexity。
2. **Contrastive Pair 质量难以保证**：graph-preserving paraphrases 可能引入微妙逻辑变化，graph-breaking corruptions 可能过于 artificial，导致 contrastive signal 在噪声中失效——这是一个 idea 层面的风险，因为整个方法论的有效性取决于 pair 质量，而这个质量目前只是假设。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs](https://arxiv.org/abs/2502.02362)
- [APRM: Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning](https://arxiv.org/abs/2509.26578)
- [CRA: Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction](https://arxiv.org/abs/2508.04216)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [RewardFlow: Topology-Aware Reward Propagation on State Graphs](https://arxiv.org/abs/2603.18859)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows](https://arxiv.org/abs/2604.23581)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [PURE: Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275)


【原始 proposal（允许参考但不是主要依据）】:
# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models

## Core Problem

Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?

## Research Opportunity

PERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.

## Research Landscape

The field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.

## Proposed Approach

Extract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.

## Detailed Description

We propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.

## Key References

- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)
- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)
- Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)
- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)
- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)
- Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)
- Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)
- AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)
- Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)
- RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)
- PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: 700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h), timeline: 14-18 weeks for 2-3 researchers, estimated_gpu_cost: $2,100-$3,000 at $3/hr A100 spot pricing
- **human_in_loop**: gpu_hours: 500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%), timeline: 10-14 weeks for 2 researchers, claude_api_cost: $400-$700 (data quality analysis, code generation, experiment triage), estimated_gpu_cost: $1,500-$2,100 at $3/hr A100 spot pricing
- **auto_research**: gpu_hours: 800-1200 A100-hours (more parallel sweeps offset by automated experiment selection), timeline: 6-8 weeks with automated pipeline, claude_api_cost: $1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting), estimated_gpu_cost: $2,400-$3,600 at $3/hr A100 spot pricing, speed_bottleneck: DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2cecc537-5629-460b-af2a-40352c05592d",
  "type": "user",
  "uuid": "4aedff1c-b3c4-4c4d-a6d7-34423fa56567",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:21:05.963Z_

```json
{
  "parentUuid": "4aedff1c-b3c4-4c4d-a6d7-34423fa56567",
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
  "uuid": "68b351fe-4734-4b99-82af-e3adea8874ea",
  "timestamp": "2026-05-27T08:21:05.963Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:21:05.964Z_

```json
{
  "parentUuid": "68b351fe-4734-4b99-82af-e3adea8874ea",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c0a34691-7202-4d0a-91e1-62df53d05cd8",
  "timestamp": "2026-05-27T08:21:05.964Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient data to make a well-informed assessment.…",
  "leafUuid": "c0a34691-7202-4d0a-91e1-62df53d05cd8",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate premise-graph contrastive PRM proposal",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b"
}
```

---

### Assistant

_source line 8 · 2026-05-27T08:21:33.836Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments and produce a Meta Judge output.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 32%] 中位 27%

**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 30%

**Reviewer 3:**


- Novelty: 中
- Significance: 中偏强
- Related Work: 强
- Probability: [22% - 33%] 中位 27%

Now I'm calculating the aggregate statistics. The three median probabilities are 27%, 30%, and 27%, giving a mean of 28%. The standard deviation is quite low at about 1.41%, which indicates strong agreement among the reviewers.

Looking at the consensus across all three reviewers, there's complete alignment on novelty being incremental rather than conceptually novel, and on the related work coverage being strong. Significance clusters around 中 to 中偏强, with two reviewers leaning toward the stronger end. The main concerns that emerge consistently are whether APRM serves as a trivial baseline, whether the DAG extraction quality holds up outside PARC's original context, and whether LLM paraphrasing actually preserves the graph structure as intended.

There's also universal skepticism about whether InfoNCE can effectively disentangle form from structure, and all three flag the modest improvement on PRMBench of just 2.3 points as underwhelming. The risk of this being an incremental or natural extension rather than a meaningful advance appears across all reviews.

Beyond the consensus, R2 uniquely emphasizes simpler alternatives like basic paraphrase augmentation and random step shuffling, while R1 and R2 both identify "From Chains to DAGs" as a missing reference. R3 brings up CRA as a relevant comparison that the other reviewers don't emphasize, and R2 pushes for more technical detail on the DAG-anchored embedding design.

The reviewer agreement is remarkably tight—standard deviation around 1.4%—pointing to a well-engineered contribution with predictable novelty that faces a strong trivial baseline in APRM. Given this consistency, the three score ranges cluster tightly around [25-32], suggesting the median should sit near 28% with a narrowed confidence interval of roughly [23%-32%]. The bottleneck is clearly novelty, capped at medium, while significance ranges from medium to medium-strong and related work is uniformly strong.

Now I'm pulling together the implementation assessment from the resource estimates and reviewer feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0a34691-7202-4d0a-91e1-62df53d05cd8",
  "isSidechain": false,
  "requestId": "req_011CbSkN8swxrgYs4WCXCgF6",
  "type": "assistant",
  "uuid": "0ba0362f-3119-48a3-9392-b3e9175b9451",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMNXnqGuYsBpX8A9S4Ht3G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21935,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3084,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3084,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21935
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

_source line 9 · 2026-05-27T08:22:16.999Z_

【阶段】: Meta Judge
【三次中位】: [27%, 30%, 27%]  std=1.4%
【共识维度】:
- **Novelty = 中**（3/3 一致）：三位审稿人均判定为"组合式创新而非概念性创新"。核心表述高度趋同——R1: "组合式创新，核心 insight 是自然的、可预测的 next step"；R2: "高度 predictable 的自然下一步，design choice 而非 paradigm shift"；R3: "combination novelty 非 conceptual novelty，NLP 中常见 paradigm 的 PRM 场景迁移"。这是最强共识维度。
- **Significance = 中至中偏强**（3/3 一致方向，R1/R3 偏强，R2 偏中）：问题重要性获一致认可（"Reward Under Attack" 的 43% stylistic shortcuts 数据被三人同时引用），但目标改进幅度偏 modest（PRMBench +2.3 分）被三人同时标记为风险。
- **Related Work = 强**（3/3 一致）：引用真实、描述准确、覆盖全面、差异化定位清晰。三人均确认 15 篇核心引用无虚假引用。
- **APRM 为首要 trivial alternative 威胁**（3/3 一致）：三人均独立识别 APRM（arXiv:2511.22888）的 adversarial hard negatives 在功能上与 PGCT 的 structure-aware negatives 高度重叠，且省去 DAG extraction pipeline。这是最一致的风险判断。
- **DAG 提取质量假设风险**（3/3 一致）：三人均质疑 PARC 的 90% recall 在 PRM800K/Math-Shepherd 异质数据上的可迁移性，以及 precision 未知的问题。
- **Graph-preserving perturbation 可靠性假设风险**（3/3 一致）：LLM paraphrasing 是否真能保持 DAG topology 不变，三人均标记为未验证假设。
- **InfoNCE 有效性假设风险**（3/3 一致）：contrastive loss 能否在 transformer representation space 中有效 disentangle surface form 和 logical structure，三人均认为缺乏理论或先验实证支撑。
- **"Incremental extension / natural next step" 被拒风险**（3/3 一致）：审稿人可能评价为 "I would have guessed this works" 而给 borderline reject。

【异常维度】:
- R2 单独提出 "simple paraphrase augmentation"（不需 DAG 的 surface perturbation）和 "random step shuffling/dropping" 作为额外 trivial alternatives——其他两人未明确提及。这些是合理的 ablation 控制但不构成独立威胁路线，降权处理。
- R3 单独强调 CRA（Causal Reward Adjustment, arXiv:2508.04216）作为竞争方案——R1/R2 提及但未单独展开。CRA 是 post-hoc 方法，与 PGCT 的 training-time 方法路线不同，竞争性较弱，降权合理。
- R2 单独指出 "DAG-anchored embedding 的具体设计缺失"（如何将 DAG topology 注入 embedding space？pooling? GNN?）——技术细节层面的质疑，合理但属于实验设计细化问题而非 idea 层面缺陷。

【最终概率】: [23% - 32%] 中位 28%
【一致性】: 高（std=1.4%，三份评审在 rubric 判决和风险识别上高度趋同）
【综合理由】:
三份评审呈现罕见的高度一致性。Novelty "中"是最强共识——三人用几乎相同的语言描述了"predictable combination"的判断，且均独立识别了 APRM 作为首要 trivial alternative 威胁。这种一致性表明 Novelty 的"中"评级非常稳健，不太可能是某位审稿人的偏差。

Significance 存在轻微分歧（R2 偏中，R1/R3 偏中偏强），但方向一致——问题重要，改进幅度 modest。综合取"中"，略偏强。

Related Work 三人一致"强"，这为 proposal 提供了 solid 的下限保障——不会因 related work 失分。

概率区间处理：三人区间分别为 [22-32], [25-35], [22-33]，交集约 [25-32]。鉴于高一致性，收窄至 [23-32]，中位取 28%（略低于算术平均 28%，因宁缺毋滥原则在高一致时不需额外偏严）。上界 32% 反映了"如果实验执行出色、大幅超越 APRM"的最好情况；下界 23% 反映了"trivial alternative 被坐实、DAG 质量不够"的风险情况。

核心瓶颈维度是 Novelty——即使实验完美执行，组合式创新的天花板约在 35% 附近，而 APRM 威胁和 modest target improvement 将其进一步压低至 ~32%。

【建议】: 边缘（Novelty 是硬瓶颈，需要在 idea 层面锐化差异点才有突破 35% 的可能；当前版本作为 engineering contribution 质量 solid 但不足以让审稿人 excited）
【实施评估】:
  - 计算资源: 700-1200 A100-hours（DAG 提取 ~80h，contrastive pair 生成 ~120h，PRM 训练含消融 ~400h，评估与 baseline 复现 ~100h），预估 GPU 成本 $2,100-$3,600（A100 spot pricing $3/hr）
  - 数据需求: PRM800K + Math-Shepherd（~300K solutions，公开可得）；需额外生成 ~600K contrastive pairs（依赖 LLM paraphrasing 和 premise-link corruption，无外部数据依赖）
  - 人工介入: DAG 提取质量需要按数学子领域（algebra / geometry / combinatorics）人工抽样审核；contrastive pair 质量需人工 spot-check（graph-preserving pairs 是否真保逻辑、graph-breaking pairs 是否自然）；预估 2-3 人、2-4 周的质量验证工作
  - 训练需求: 需要训练——基于 Qwen2.5-Math-7B-Instruct 微调，dual objective（step-correctness + InfoNCE），预估单次训练 ~50-80 A100-hours，含超参搜索和消融需 ~400h
  - 新 Benchmark: 不需要构建新 benchmark（使用现有 PRMBench、ProcessBench、"Reward Under Attack" adversarial suite），但需要复现 APRM baseline 以做 head-to-head comparison
  - 预估周期: 10-18 周（2-3 名研究者），瓶颈在 DAG 提取质量验证（串行人工检查）和 APRM baseline 复现

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ba0362f-3119-48a3-9392-b3e9175b9451",
  "isSidechain": false,
  "requestId": "req_011CbSkN8swxrgYs4WCXCgF6",
  "type": "assistant",
  "uuid": "a1ff4ae1-75b0-4536-a911-be8f1f64bca9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMNXnqGuYsBpX8A9S4Ht3G",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21935,
      "cache_read_input_tokens": 11014,
      "output_tokens": 3084,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3084,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21935
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient data to make a well-informed assessment.…",
  "leafUuid": "a1ff4ae1-75b0-4536-a911-be8f1f64bca9",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate premise-graph contrastive PRM proposal",
  "sessionId": "5ccdb039-573b-4283-a0f7-d0ac3a4a908b"
}
```

---
