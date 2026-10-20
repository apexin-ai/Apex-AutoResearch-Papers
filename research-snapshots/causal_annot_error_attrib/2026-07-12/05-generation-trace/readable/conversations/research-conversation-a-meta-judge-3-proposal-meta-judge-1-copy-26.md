# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/9b7f2a76-d9aa-468d-b837-dfc026066780.jsonl`
- **Structured JSON:** [`f288750713bd1274dcc2.json`](../../sessions/f2/f288750713bd1274dcc2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:13:30.808Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:13:30.808Z",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research data. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- \"Reward Under Attack\" (arXiv:2603.06621, 2026): 建立了 PRM 鲁棒性的三层诊断体系（静态扰动、对抗攻击、RL reward hacking）。确认 RL 策略可达 >0.9 PRM 分数但 <4% 真实准确率。43% reward gain 来自风格捷径。Proposal 的问题动机直接基于此论文，描述准确。\n- \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, 2025): 确立了 PRM 检测\"一致性\"而非\"因果性\"的核心发现。Proposal 的核心 claim 直接建立在此之上，引用准确。\n- PARC/PERL (ICML 2025, arXiv:2502.02362): 已确认为 ICML 2025 poster。70B 模型上 premise 识别 recall >90%，error identification 提升 6-16%。这是 PGCT 的关键技术前提，描述准确。**但注意：PARC 本身仅通过重构验证流程（不需要训练）即可带来 6-16% 提升，这构成 trivial alternative 威胁。**\n- \"From Chains to DAGs\" (arXiv:2601.17593, 2026): 确认 LLM hidden states 线性编码 DAG 推理结构，中间层可恢复性最高。Proposal 的\"representation-utilization gap\"论点基于此。\n- CRM (ICLR 2026, arXiv:2509.26578): 通过条件概率框架将每步 reward 条件化于前序步骤，解决 credit assignment 模糊性。在 BoN、beam search、RL 上一致优于已有 reward models。**与 PGCT 的关键区别：CRM 仍在 point-wise prediction paradigm 内，不在 embedding space 编码关系结构。** 描述准确。\n- GenPRM (AAAI 2026, arXiv:2504.00891): 通过生成式 CoT + code verification 扩展 PRM test-time compute。已确认 AAAI 2026。属于 inference-time 增强，与 PGCT 的 training-time 方法正交。\n- ThinkPRM (arXiv:2504.16828, 2025): 用 1% PRM800K 标签通过生成式验证 CoT 达到强结果。ThinkPRM-1.5B 在 MATH-500 上超越 DiscPRM ~5pp。同为 inference-time 方法。\n- APRM (arXiv:2511.22888, 2025): 对抗性更难负样本，OOD +5.3pp。但负样本构造是 domain-agnostic 的。\n- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350): 通过梯度反转分解 reward model embedding 为因果/非因果因子。在 representation space 操作但使用 domain-agnostic 统计分离。\n- PathFinder-PRM-7B (arXiv:2505.19706): PRMBench 开源 SOTA 67.7，距人类 ceiling 83.8 仍有显著差距。\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495): 构造 premise-oriented 对比样本用于逻辑阅读理解。最接近 PGCT 的前置工作，但目标不同（阅读准确率 vs. PRM 鲁棒性），粒度不同（命题级 vs. 多步数学 DAG）。\n\n- **调研总结**: PRM 鲁棒性是 2025-2026 年的活跃研究热点，已有多种防御路线（对抗训练 APRM、条件建模 CRM、后处理 CRA、表示分解 Factored Causal RL、推理增强 GenPRM/ThinkPRM）。前提依赖 DAG 提取（PARC）和 LLM 表示中的 DAG 编码（Chains to DAGs）已分别被证实可行。**PGCT 处于\"将已验证的 DAG 结构信号注入 PRM 训练时表示学习\"这一具体交叉点上，该交叉点尚无直接竞争工作，但属于已有 building blocks 的自然组合。**\n\n【Trivial Alternative 检验】:\n存在明确的 trivial alternative 威胁：\n1. **PARC 直接应用**：PARC/PERL 已证明，仅在 inference time 重构验证流程（引入 premise links）即可提升 error identification 6-16%，无需任何额外训练。PGCT 需要证明其 training-time contrastive learning 带来的增量显著超越这个零训练成本的 baseline。\n2. **DAG 信息作为输入特征**：更简单的方法是将 DAG 邻接信息作为额外输入（如 positional encoding 或辅助 token）直接 feed 给 PRM，而非通过 contrastive learning 间接注入。Proposal 没有讨论这个 trivial alternative。\n3. **APRM + premise-aware 负样本**：将 APRM 的对抗训练框架与 premise-aware 的负样本构造结合，不需要完整的 contrastive + InfoNCE 框架。\n\nProposal 对第 1 点部分回应了（\"PGCT 是 training-time representation learning，与 inference-time 方法正交\"），但\"正交\"不等于\"增量显著\"。对第 2、3 点完全未讨论。**增量价值的论证是 idea 层面的主要薄弱点。**\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有以下未经验证的环节：\n\n1. **\"Representation-utilization gap 可通过 contrastive training 弥合\"**：这是最关键的假设。\"From Chains to DAGs\" 证明 DAG 结构可从 hidden states 线性恢复，PARC 证明 premise links 可从模型输出提取。但\"hidden states 中存在信息\" ≠ \"contrastive training 可以将该信息有效引导至 reward prediction\"。线性可探测性(probe)和任务可利用性(task utility)之间存在已知 gap（Hewitt & Liang 2019 的 probe selectivity 问题）。Proposal 的核心假设——contrastive training 是弥合此 gap 的正确机制——缺乏理论或实证支撑。\n\n2. **\"DAG-anchored contrastive pairs 能产生泛化的结构感知\"**：模型可能只学会检测训练时使用的特定扰动模式（如特定的 premise-link 断裂方式），而非发展出真正通用的 premise-dependency reasoning。这与 APRM 面临的\"cat-and-mouse problem\"本质上是同一挑战——proposal 批评 APRM 有此问题，但自身并未论证为何能避免。\n\n3. **\"Point-wise supervision 是问题根源\"**：Proposal 将 PRM 脆弱性归因于\"point-wise BCE training leaves dormant structural representations\"。但 CRM (ICLR 2026) 表明通过条件概率框架（仍是 point-wise prediction）也能显著提升。问题可能不在于 point-wise vs. relational 的 supervision paradigm，而在于训练数据质量、标注噪声等其他因素。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \"将 premise-dependency DAG 注入 PRM training-time representation learning\"这一具体交叉点确实尚无直接竞争工作。与最相关工作的差异化是真实的：vs. CRM（point-wise paradigm，无 DAG topology）、vs. APRM（domain-agnostic negatives）、vs. Factored Causal RL（统计分离而非 domain-grounded structure）、vs. CRV/GoV（inference-time，非 training-time）、vs. Thought-Path CL（命题级阅读理解，非多步数学 PRM）。**但核心 insight——\"用结构感知的对比对训练，得到结构感知的表示\"——是给定 building blocks 后的自然下一步，而非反直觉发现。** 审稿人的反应更可能是 \"I would have guessed this would work\" 而非 \"surprising\"。Novelty 是组合性的（DAG extraction + contrastive learning + PRM training），而非概念性的。\n\n2. **Significance: 中** — 问题本身重要性毋庸置疑：PRM 鲁棒性和 reward hacking 是 RLHF/reasoning 领域的核心痛点，PRMBench 上 SOTA (67.7) vs. 人类 (83.8) 的 gap 说明改进空间大。方法与 inference-time 增强（GenPRM/ThinkPRM）正交，理论上可叠加。**但影响力受限于：(a) 仅针对数学推理场景，推广到其他推理域（代码、常识、科学）需要重新设计 DAG extraction pipeline；(b) 依赖 72B 模型做 DAG extraction，实际部署门槛高；(c) 如果核心发现是 positive（contrastive training 提升了 PRMBench 几个点），影响力有限；如果 negative，则是一个有价值的 negative result 但发表难度大。**\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。Related work 覆盖非常全面，涵盖 PRM 鲁棒性（APRM, CRA, CRM, PURE）、表示级方法（Factored Causal RL, \"When Reward Hacking Rebounds\"）、推理增强 PRM（R-PRM, GenPRM, ThinkPRM）、图结构验证（CRV, GoV, AgentEval）、并发工作（CPMI, RewardFlow）。差异化定位清晰——逐一论证了与每类方法的区别。引用的论文经验证均真实存在，描述准确。**唯一不足：未讨论 DAG 信息作为输入特征这一更简单的 alternative。**\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n- Related Work 维度为强，说明作者对领域理解深刻，定位专业——这保证了 proposal 的下限，降低了\"被审稿人指出遗漏关键相关工作\"的风险。\n- Novelty 为中：交叉点确实新颖，但属于已有 building blocks 的自然组合，核心 insight 不够 surprising。这是概率上限的主要限制因素——在一个已经高度竞争的领域（2025-2026 年 PRM 改进方向涌现了 CRM, APRM, PURE, GenPRM, ThinkPRM 等多篇顶会），\"自然组合\"的 novelty 难以脱颖而出。\n- Significance 为中：问题重要但方法的影响面受限于数学推理场景，且存在未充分回应的 trivial alternative 威胁（PARC zero-cost baseline）。\n- 整体处于\"idea 有实质内核，方向正确，但核心发现如果 positive 审稿人可能会说 'I would have guessed this'\"的区间（rubric 25-35%），因 trivial alternative 未充分回应和领域拥挤度，中位数下调至 27%。\n\n【主要风险】:\n1. **Trivial alternative 威胁未充分化解**：PARC 在 inference time 零训练成本即可带来 6-16% 提升。审稿人会问：\"相比于直接用 PARC restructure 验证 + 标准 PRM，PGCT 的额外训练成本（72B DAG extraction + 600K contrastive pairs）换来的增量提升是否值得？\"如果增量仅为几个百分点，cost-benefit 论证将很困难。\n2. **\"自然组合\" novelty 在拥挤赛道上的竞争力**：2025-2026 年 PRM 改进方向密集出现多篇顶会/顶刊工作（CRM@ICLR'26, PURE@NeurIPS'25, GenPRM@AAAI'26）。在这个竞争格局下，\"DAG + contrastive + PRM\"的组合性 novelty 可能不足以让 3 位审稿人中的 2 位认为其达到 acceptance threshold。核心 insight 的 \"surprisingness\" 不足是最难通过实验补救的弱点。\n```\n\nSources:\n- [Reward Under Attack](https://arxiv.org/abs/2603.06621)\n- [PARC/PERL - Premise-Augmented Reasoning Chains](https://arxiv.org/abs/2502.02362)\n- [From Chains to DAGs](https://arxiv.org/pdf/2601.17593)\n- [PRMBench](https://arxiv.org/abs/2501.03124)\n- [CRM - Conditional Reward Modeling](https://arxiv.org/abs/2509.26578)\n- [GenPRM](https://arxiv.org/pdf/2504.00891)\n- [ThinkPRM](https://huggingface.co/papers/2504.16828)\n- [R-PRM](https://arxiv.org/pdf/2503.21295)\n- [Adversarial Training of Reward Models](https://arxiv.org/abs/2504.06141)\n- [Factored Causal Representation Learning](https://arxiv.org/pdf/2601.21350)\n- [PathFinder-PRM Error-Aware Hierarchical Supervision](https://arxiv.org/pdf/2505.19706)\n- [Thought-Path Contrastive Learning (AAAI 2025)](https://arxiv.org/abs/2409.14495)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make an informed assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025):\n   - 确认存在，作者 Yuhui Xu, Hanze Dong 等。核心发现：SOTA PRMs 优先评估结构一致性而非因果正确性；去掉问题陈述对奖励分数影响极小，而截断推理链或改变数值则影响显著。这是 proposal 的核心动机论文，描述准确。\n\n2. \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026):\n   - 确认存在。量化了 PRM 的脆弱性：RL 训练的策略在 AIME 上达到 >0.9 PRM 分数但实际准确率 <4%，43% 的奖励增益来自风格捷径。发布了 PRM-BiasBench 诊断工具。Proposal 引用准确。\n\n3. PARC/PERL (arXiv:2502.02362, ICML 2025):\n   - 确认存在。PARC 将线性推理链重构为带前提链接的 DAG，前提识别在 70B+ 模型上达到 >90% recall，错误检测准确率提升 6-16%。Proposal 引用准确。\n\n4. \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026):\n   - 确认存在，Columbia University。通过轻量级探针证明 LLM 隐藏状态线性编码了 DAG 推理结构（节点深度、成对距离、邻接关系），在中间层可恢复性最高。Proposal 引用准确。\n\n5. CRV (arXiv:2510.09312, ICLR 2026 Oral):\n   - 确认存在，Meta FAIR。白盒方法，通过归因图的结构指纹来验证推理正确性。在 GSM8K 上达到 93.4% 准确率。关键区别：推理时白盒方法，非训练时表示学习。\n\n6. PathFinder-PRM-7B (arXiv:2505.19706):\n   - 确认存在。PRMBench SOTA 得分 67.7，通过分层解耦误差类型检测与奖励估计实现。Proposal 引用准确。\n\n7. CPMI (arXiv:2604.10660, April 2026):\n   - 确认存在。使用对比互信息进行 PRM 自动标注，不涉及依赖图。创建了 CPMI-80k 数据集。与 proposal 的方法正交。\n\n8. RewardFlow (arXiv:2603.18859, March 2026):\n   - 确认存在。在状态图上进行拓扑感知的奖励传播，用于代理推理任务。不使用对比训练。\n\n9. Factored Causal Representation Learning (arXiv:2601.21350, ICML 2026):\n   - 确认存在。通过梯度反转将奖励模型嵌入分解为因果/非因果因子。领域无关的统计分离方法。\n\n10. PRMBench (arXiv:2501.03124, ACL 2025):\n    - 确认存在。6,216 个问题，83,456 个步骤级标签，涵盖 soundness/sensitivity/simplicity 等细粒度错误类别。人类 ceiling 83.8。\n\n- **调研总结**: PRM 鲁棒性是 2025-2026 年的热点研究方向，多条独立路线并行发展：(a) 对抗训练增强决策边界（APRM），(b) 表示空间因果分解（Factored Causal RL），(c) 架构级条件化（CRM），(d) 推理时图结构验证（CRV, GoV），(e) 推理增强生成式 PRM（R-PRM, GenPRM, ThinkPRM）。然而，**在训练时将前提依赖 DAG 拓扑结构注入 PRM 表示空间** 这一特定组合确实尚未被占据。Proposal 处于多条已有路线的交汇点，提出了一个新的组合方向。\n\n\n【Trivial Alternative 检验】:\n\n存在两个需要认真对待的 trivial alternative 威胁：\n\n**威胁 1：PARC 输入增强 + 标准 PRM 训练。** PARC 已经证明，仅通过在推理链中显式标注前提链接（输入格式层面的改变），错误检测就提升了 6-16%。那么一个更简单的 baseline 是：不做对比训练，只是把 PARC 增强后的推理链作为 PRM 的输入，用标准 BCE 训练。如果这个 baseline 已经能捕获大部分 \"前提依赖意识\"，PGCT 的增量价值就很小。\n\n**威胁 2：APRM 风格的对抗性硬负例 + 前提破坏。** APRM 通过生成更难的负例实现了 +5.3pp OOD 提升。如果把 PGCT 的\"图破坏\"负例直接作为 APRM 式的硬负例用于标准 BCE 训练（不用 InfoNCE，不做表示空间重组），效果是否相近？\n\n**Proposal 的增量价值论证：** Proposal 认为 PGCT 的核心价值在于 *表示空间重组*（通过 InfoNCE 使嵌入空间编码拓扑结构），而非仅仅改善输入或决策边界。这个论证是合理的——PARC 改善输入，APRM 改善分类边界，PGCT 改善表示几何——但这个差异是否能转化为显著的下游效果，目前是未经验证的假设。A1/A3 消融设计（移除 InfoNCE / 随机扰动替代 DAG 扰动）理论上可以回答这个问题，但在 idea 层面，增量价值存在但不确定性较高。\n\n\n【前提假设检验】:\n\n核心逻辑链：\n> LLM 隐藏状态编码了 DAG 结构 → 标准 PRM 训练未利用此结构 → DAG 锚定的对比训练可激活此结构 → 激活后的结构表示将提升鲁棒性\n\n**假设 1**（已有证据支撑）：\"LLM 隐藏状态编码了 DAG 结构\" — \"From Chains to DAGs\" 通过线性探针证明了这一点。✓\n\n**假设 2**（部分支撑）：\"标准 PRM 训练未利用此结构\" — \"Reward Models Identify Consistency, Not Causality\" 间接支持（PRMs 检测一致性而非因果性），但这不直接等价于\"DAG 结构表示未被利用\"。一致性检测也可能隐式使用了某些结构信息，只是不够。这里存在推理跳跃。⚠️\n\n**假设 3**（核心未验证假设）：\"DAG 锚定的对比训练可以激活休眠的结构表示\" — 这是整个 proposal 的核心赌注。存在两个子问题：\n- (a) 从\"线性探针可恢复\"到\"对比训练可利用\"的跳跃。线性探针证明信息存在，但对比训练能否有效地将这种信息路由到奖励预测头，取决于优化景观的具体性质，这是未知的。\n- (b) InfoNCE 损失的梯度信号是否足够强大且方向正确，能够重组已经被大规模预训练塑造的表示空间？如果结构信息在深层但奖励头连接浅层，梯度传播可能不够有效。\n\n**假设 4**（合理但二阶不确定）：\"表示空间的结构化将转化为鲁棒性提升\" — 即使嵌入空间确实编码了更好的 DAG 结构，这是否必然导致对风格捷径和对抗攻击的鲁棒性？可能存在\"表示好但决策边界仍被利用\"的情况。\n\n**总结**：逻辑链前端有证据支撑，但核心环节（假设 3）是一个有合理动机但未经验证的 leap of faith。这不是致命的——许多好论文的核心贡献就是验证这样的假设——但如果结果为负，paper 的价值会大幅下降。\n\n\n【3 维度打分】:\n\n**1. Novelty: 中（偏强）**\n\n理由：\n- 正面：将前提依赖 DAG 拓扑注入训练时表示学习确实是一个未被占据的组合。我的调研确认：CRV 和 GoV 在推理时使用图结构，Factored Causal RL 在训练时操作表示空间但使用领域无关的统计分离，APRM 使用对抗硬负例但不编码逻辑结构，CPMI 使用对比方法但不涉及依赖图。PGCT 处于这些工作的交汇点，组合确实是新的。\n- 负面：\"表示-利用间隙\"的 framing 虽然有吸引力，但本质上是\"已有方法 A（DAG 提取）+ 已有方法 B（对比学习）应用于已知问题 C（PRM 鲁棒性）\"的组合创新。各个组件都不是新的。如果核心实验结果 positive，审稿人更可能说 \"this is a natural next step that makes sense\" 而非 \"this is surprising\"。Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) 已经在前提级别做了对比学习（虽然是阅读理解而非 PRM），概念距离并不大。\n\n**2. Significance: 强**\n\n理由：\n- PRM 鲁棒性和 reward hacking 是数学推理领域最紧迫的问题之一。\"Reward Under Attack\" 的发现（>0.9 PRM 分数但 <4% 准确率）表明这不是边际问题，而是系统性失败。\n- PRMBench 上 67.7 vs 83.8 的人类 ceiling 差距表明该领域有大量改进空间。\n- 方法与现有路线（生成式 PRM、条件奖励建模等）正交，潜在可组合性高。\n- 如果\"表示空间的结构化确实能提升鲁棒性\"这一假设被验证，将为 PRM 训练提供一种新的原则性方法论，影响面超越数学推理。\n- 局限：当前方法高度依赖数学推理的可结构化特性，向其他领域（代码、科学推理等）的推广需要额外论证。\n\n**3. Related Work: 强**\n\n理由：\n- 覆盖极为全面。我验证了 20+ 篇引用论文，全部真实存在且描述准确。\n- 与每条竞争路线的差异化定位清晰且有说服力：\n  - 区分于 APRM（领域无关对抗负例 vs 结构锚定对比对）\n  - 区分于 CRV（推理时白盒 vs 训练时表示学习）\n  - 区分于 Factored Causal RL（统计因子分离 vs 领域接地的结构先验）\n  - 区分于 CPMI（对比自动标注 vs 对比表示学习）\n  - 区分于 RewardFlow（图上奖励传播 vs 对比训练）\n- 论文引用到 2026 年 4 月（AgentEval、CPMI、\"When Reward Hacking Rebounds\"），时效性极好。\n- 唯一微小遗漏：Robust Reward Modeling via Causal Rubrics (arXiv:2506.16507, June 2026)，但这可能是在 proposal 撰写之后发表的。\n\n\n【概率估计】: [28% - 38%] 中位 33%\n\n【估计理由】:\nSignificance 是本 proposal 的强项，问题真实且重要，时效性好。Related Work 覆盖和定位是顶级水平。Novelty 是限制上界的主要因素——虽然组合确实是新的，但核心机制（DAG 提取 + InfoNCE 对比学习）都是已知技术的组合应用，缺乏深层的 methodological surprise。一个理想审稿人看到这个 idea 可能会说：\"This is a well-motivated and natural next step, but the intellectual contribution is in the engineering of the combination rather than a fundamental insight.\" 这使得中稿概率的上界受限。\n\n此外，trivial alternative 威胁是实质性的：如果 PARC 增强输入 + APRM 式硬负例已经能获得大部分收益，PGCT 的表示空间重组带来的 *增量* 提升可能不够大，这在审稿中可能被直接质疑。核心假设 3（对比训练激活休眠结构表示）的理论根基也不够坚实——它有合理的直觉但缺乏理论保证。\n\n概率未到 40%+ 是因为缺少 \"surprising\" 的维度——核心发现如果 positive，多数审稿人会认为 \"makes sense given the setup\" 而非 \"I wouldn't have predicted this\"。概率未低于 28% 是因为问题确实重要、定位确实独特、且当前 SOTA 有大量改进空间。\n\n【主要风险】:\n1. **Trivial alternative 质疑**：审稿人可能要求与\"PARC 输入增强 + 标准 BCE\"和\"DAG 破坏负例 + 标准 BCE（无 InfoNCE）\"进行对比，如果这些更简单的方法效果相近，paper 的核心贡献将被严重削弱。\n2. **核心假设未被充分 justify**：从\"隐藏状态中线性可探测 DAG 结构\"到\"对比训练可激活此结构以改善奖励预测\"的逻辑跳跃缺乏理论支撑，审稿人可能认为这只是一个 empirical bet，idea 层面的贡献不足以支撑顶会论文。\n```\n\nSources:\n- [Reward Under Attack](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL: Premise-Augmented Reasoning Chains](https://arxiv.org/abs/2502.02362)\n- [From Chains to DAGs](https://arxiv.org/abs/2601.17593)\n- [CRV: Verifying Chain-of-Thought Reasoning via Its Computational Graph](https://arxiv.org/abs/2510.09312)\n- [PathFinder-PRM](https://arxiv.org/abs/2505.19706)\n- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)\n- [RewardFlow](https://arxiv.org/abs/2603.18859)\n- [Factored Causal Representation Learning for Robust Reward Modeling](https://arxiv.org/abs/2601.21350)\n- [PRMBench](https://arxiv.org/abs/2501.03124)\n- [DAG-Math](https://arxiv.org/abs/2510.19842)\n- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/pdf/2506.16507)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient literature context. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025): 确立了 PRM 检测的是 surface consistency 而非 causal correctness 的核心问题。移除题目对 reward score 影响极小，而打乱推理流则影响显著。这是本 proposal 的直接出发点，确认其问题动机真实存在。\n- \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026): 量化了 PRM 的脆弱性——43% reward gain 来自 stylistic shortcuts，RL 训练策略可达 >0.9 PRM score 但实际准确率 <4%。建立了三层诊断框架。确认了 PRM robustness 是一个严肃的开放问题。\n- PARC/PERL (ICML 2025, arXiv:2502.02362): 证明了 premise dependency links 可以从推理链中提取（70B+ 模型 >90% recall），且用于推理时 error detection 可提升 6-16%。关键点：这是 **inference-time** 的应用，并未将 premise 结构注入 training-time representation learning。\n- \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026): 证明 LLM hidden states 已经线性编码了 DAG 推理结构（node depth, pairwise distance, adjacency）。这支持了 proposal 的 \"representation-utilization gap\" 假说——结构信息存在于 base model 但未被 PRM 训练利用。\n- CRM (ICLR 2026, arXiv:2509.26578): 通过 sequential conditioning 建模 step 间依赖关系，但在 point-wise prediction paradigm 内操作，不编码 embedding space 中的 relational structure。\n- CRV (ICLR 2026 Oral, arXiv:2510.09312): 使用 attribution graph 的结构 fingerprints 做白盒推理验证。图结构用于 inference-time，非 training-time。\n- PathFinder-PRM-7B (arXiv:2505.19706): 当前 PRMBench 开源 SOTA (67.7)，vs 人类 83.8，确认了性能鸿沟的存在。\n- GenPRM (AAAI 2026, arXiv:2504.00891): 通过 generative CoT + code verification 增强 PRM。ThinkPRM (arXiv:2504.16828) 用仅 1% PRM800K labels 实现了强结果。R-PRM (arXiv:2503.21295) 在 ProcessBench 上 +11.9 F1。这些都是 **inference-time** reasoning enhancement。\n- CPMI (arXiv:2604.10660, Apr 2026): 用 contrastive MI 做 PRM auto-labeling，**无** dependency graph 结构。\n- RewardFlow (arXiv:2603.18859, Mar 2026): 在 state-transition graph 上传播 reward，**无** contrastive training。\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495): 对 propositional-level 的 premise-oriented contrastive pairs 做阅读理解，非多步数学推理 DAG，非 PRM robustness。\n- APRM (arXiv:2511.22888, Nov 2025): 用 adversarial harder negatives 提升 PRM (+5.3pp OOD)，但 negatives 是 domain-agnostic 的，非基于 logical dependency structure。\n\n- **调研总结**: PRM robustness 是一个活跃且重要的研究方向，近 12 个月内涌现了大量工作（CRM, PURE, CRA, APRM, CRV, PathFinder-PRM 等）。目前存在两条独立的线索：(1) 表示空间鲁棒性方法（不使用领域特定逻辑结构），(2) 图结构验证方法（仅用于推理时）。本 proposal 试图将 premise-dependency DAG 结构注入 training-time representation learning，确实是两条线索的交叉空白。但这个交叉点的「自然程度」很高——给定 PARC 和 \"From Chains to DAGs\" 的结论，将结构先验引入 PRM 训练是一个相当直觉的 next step。\n\n【Trivial Alternative 检验】:\n存在至少两个成本更低的替代方案构成实质威胁：\n\n1. **\"Premise-aware data augmentation + 标准 BCE\"**：直接将 premise-breaking negative examples 加入 PRM 训练数据（使用与 proposal 相同的 DAG-guided corruption 方法），但不引入 InfoNCE contrastive loss，仍用标准 BCE。这本质上是 APRM 的 domain-specific 版本。Proposal 的增量价值必须证明 contrastive objective **本身**（而非仅仅 DAG-guided negatives 的数据质量）带来了显著收益。Ablation A1（去掉 InfoNCE）可以测试这一点，但如果 A1 和 full PGCT 差异不大，整个 idea 的核心 claim 就会坍塌。\n\n2. **\"CRM + PARC inference-time pipeline\"**：CRM 已经建模 sequential dependency，PARC 已经能在推理时提取 premise links 并提升 error detection。两者的简单组合（CRM 做 reward prediction + PARC 做 inference-time premise-aware verification）可能是一个更轻量的 baseline，不需要任何新的训练方法。\n\n3. **Linear probe auxiliary loss**：Proposal 主张这只优化 local-layer information retention 而不影响 cross-layer representation flow。这是一个 **论断而非证据**。一个简单的多层 auxiliary loss 可能同样有效。\n\n**增量价值**：如果 contrastive objective 确实优于上述替代方案，那增量在于 embedding space 的 global topology reorganization——这是一个有意义的技术贡献。但这必须通过实验证明，目前只是假说。\n\n【前提假设检验】:\n核心逻辑链：DAG 结构存在于 hidden states (From Chains to DAGs) → 标准 PRM 训练未利用 (Consistency not Causality) → contrastive training 可以激活这些 dormant representations → 激活后的 structural embedding 转化为更好的 reward prediction\n\n关键未验证环节：\n\n1. **\"Dormant representations\" 假设**：From Chains to DAGs 证明 base model 编码了 DAG 结构。但 PRM fine-tuning 可能已经 **摧毁** 了这些表示（catastrophic forgetting），而非仅仅\"未利用\"。如果 PRM 训练后 DAG 结构已不存在于 hidden states，那么 contrastive training 需要 **重建** 而非\"激活\"，这是一个更强的要求。\n\n2. **Embedding topology → reward accuracy**：即使 contrastive training 成功使 embedding space 编码了 DAG topology（graph-preserving pairs cluster, graph-breaking pairs separate），这并不自动意味着 step-level reward prediction 会更准确。从 representation structure 到 downstream task performance 的 gap 是存在的。\n\n3. **DAG extraction quality at scale**：PARC/PERL 的 >90% recall 是在 curated datasets 上验证的。扩展到 PRM800K + Math-Shepherd 的 ~300K solutions，DAG extraction 质量可能显著下降，尤其是在复杂的竞赛数学题上。Proposal 承认需要 72B 模型做 extraction，但未讨论 failure modes。\n\n4. **Contrastive pair quality**：生成 \"graph-breaking but fluent\" negatives 是困难的——需要精确切断特定 premise link 同时保持表面流畅和其余逻辑结构不变。这种合成数据的质量直接决定方法的上限。\n\n【3 维度打分】:\n1. **Novelty: 中** — \n   从调研来看，将 premise-dependency DAG 结构注入 training-time PRM representation learning 确实是文献中的空白：CRV (ICLR 2026) 和 PARC (ICML 2025) 使用图结构但限于 inference-time；APRM 使用 adversarial negatives 但 domain-agnostic；Factored Causal RL (ICML 2026) 操作 representation space 但用 domain-agnostic statistical separation。因此 PGCT 的定位确实是新的。\n   \n   但这个新颖性更像是 **natural combination** 而非 **conceptual breakthrough**。给定 PARC 已证明 premise links 可提取且有用，\"From Chains to DAGs\" 已证明 DAG structure 编码于 hidden states，APRM 已展示 adversarial negatives 提升 PRM——将三者组合（domain-specific structural negatives + contrastive training）是一个相当直觉的 engineering step。审稿人不太可能说 \"I wouldn't have thought of this\"，更可能说 \"this is a reasonable next step.\" Thought-Path Contrastive Learning (AAAI 2025) 已经在更简单的设置（propositional-level, reading comprehension）中证明了 premise-oriented contrastive learning 的有效性，进一步降低了 PGCT 的 surprise factor。\n\n2. **Significance: 中** — \n   PRM robustness 确实是一个重要且活跃的研究问题，\"Reward Under Attack\" 的发现（43% stylistic shortcuts, >0.9 score <4% accuracy）表明问题的严重性。PRMBench 上 67.7 vs 83.8 human ceiling 的差距也表明有大量改进空间。\n   \n   但 significance 受限于两点：(a) 方法仅适用于数学推理这一特定领域（premise DAGs 在数学链中最容易定义和提取），向 code reasoning、commonsense reasoning 等其他领域的推广路径不清晰；(b) 如果 inference-time 方法（如 GenPRM, ThinkPRM, R-PRM）已经通过 generative verification 大幅提升了 PRM 性能，training-time representation learning 的增量价值可能被压缩——proposal 声称与 inference-time 方法 \"orthogonal\"，但未论证两者组合后是否有 meaningful 的叠加收益。\n\n3. **Related Work: 强** — \n   Related work 覆盖非常全面，涵盖了 PRM robustness（CRA, APRM, CRM, PURE）、representation-level robustness（Factored Causal RL, When Reward Hacking Rebounds）、reasoning-enhanced PRMs（R-PRM, GenPRM, ThinkPRM）、graph structure for verification（CRV, GoV, AgentEval）、concurrent approaches（CPMI, RewardFlow, Thought-Path CL）等多条线索。差异化定位清晰，明确指出 PGCT 是 \"first to inject premise-dependency topology directly into training-time representation learning\"。引用的关键论文（PARC/PERL ICML 2025, CRM ICLR 2026, CRV ICLR 2026 Oral, GenPRM AAAI 2026, PRMBench ACL 2025）均经搜索确认真实存在且描述基本准确。\n\n【概率估计】: [23% - 33%] 中位 28%\n\n【估计理由】: \nRelated Work 覆盖强，定位清晰，问题动机真实——这些保证了下限不会太低。但 Novelty 为 \"中\"（natural combination 而非 conceptual surprise）是上界的主要限制因素。核心技术贡献——contrastive training anchored to premise DAGs——的增量价值面临 trivial alternative 威胁（DAG-guided negatives + 标准 BCE 可能就够了），且 \"representation-utilization gap\" 假设的两个关键环节（dormant representations 在 PRM fine-tuning 后是否存留; embedding topology improvement 是否转化为 reward prediction improvement）均未验证。Significance 受限于数学推理单一领域。综合来看，这是一个 solid but unsurprising 的研究方向，审稿人更可能评价为 \"competent incremental work\" 而非 \"exciting contribution\"，估计处于 25-35% 区间的偏下位置。\n\n【主要风险】: \n1. **Trivial alternative 致命威胁**：Ablation A1（去掉 InfoNCE，只保留 DAG-guided negatives + BCE）如果与 full PGCT 差异不显著，则核心 claim（contrastive objective 本身的价值）被否定，论文沦为 \"better data augmentation for PRMs\"——novelty 从 \"中\" 降至 \"弱\"。\n2. **\"Natural next step\" 定性**：审稿人熟悉 PARC + \"From Chains to DAGs\" + contrastive learning 后，很可能认为这个组合是一个 obvious direction，导致 novelty 评分偏低。Proposal 需要在实验中证明 contrastive objective 的 mechanism（而非仅仅 DAG-guided negatives 的数据质量）是成功的关键，但这一点目前只是假说。\n```\n\nSources:\n- [Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/abs/2603.06621)\n- [Reward Models Identify Consistency, Not Causality (arXiv:2502.14619)](https://arxiv.org/abs/2502.14619)\n- [PARC/PERL (ICML 2025, arXiv:2502.02362)](https://arxiv.org/abs/2502.02362)\n- [From Chains to DAGs (arXiv:2601.17593)](https://arxiv.org/pdf/2601.17593)\n- [CRM (ICLR 2026, arXiv:2509.26578)](https://arxiv.org/abs/2509.26578)\n- [CRV (ICLR 2026, arXiv:2510.09312)](https://arxiv.org/abs/2510.09312)\n- [PathFinder-PRM (arXiv:2505.19706)](https://arxiv.org/pdf/2505.19706)\n- [GenPRM (AAAI 2026, arXiv:2504.00891)](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM (arXiv:2504.16828)](https://huggingface.co/papers/2504.16828)\n- [CPMI (arXiv:2604.10660)](https://arxiv.org/abs/2604.10660)\n- [RewardFlow (arXiv:2603.18859)](https://arxiv.org/abs/2603.18859)\n- [PRMBench (ACL 2025, arXiv:2501.03124)](https://arxiv.org/abs/2501.03124)\n- [DAG-Math (arXiv:2510.19842)](https://arxiv.org/abs/2510.19842)\n- [Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)](https://arxiv.org/abs/2409.14495)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models detect consistency rather than causality. \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. \"Reward Under Attack\" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains stem from stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness rather than mere surface consistency?\n\n## Research Opportunity and Key Insight\n\nA critical representation-utilization gap exists in current PRMs. \"From Chains to DAGs\" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet standard PRM training fails to channel this latent structural knowledge into reward prediction (arXiv:2502.14619). PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), improving error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction at scale.\n\nOur key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space). An alternative approach — using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction; contrastive training directly constrains the reward-relevant embedding space, providing end-to-end structural injection.\n\n## Research Landscape\n\n**PRM robustness: existing defenses.** \"Reward Under Attack\" (arXiv:2603.06621) established the three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Defenses include CRA (Aug 2025, arXiv:2508.04216, post-hoc SAE correction), APRM (Nov 2025, arXiv:2511.22888, adversarial harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure in PRM training. APRM's adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific patterns without understanding why they are wrong, leaving it vulnerable to novel attacks (cat-and-mouse problem). PGCT instead reorganizes the PRM's representation space around premise-dependency topology.\n\n**Representation-level robustness.** Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350) decomposes reward model embeddings into causal/non-causal factors via gradient reversal. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, April 2026) extracts shortcut concept directions from contrastive pairs via representation engineering. Both operate in representation space but use domain-agnostic statistical separation (gradient reversal, concept directions). PGCT differs fundamentally: its structural prior is domain-grounded — premise dependency DAGs extracted from mathematical reasoning chains — rather than learned statistical factors. This provides interpretable, verifiable structural constraints rather than latent factor separation.\n\n**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique (+11.9 F1 on ProcessBench, +8.5 on PRMBench). GenPRM (AAAI 2026, arXiv:2504.00891) uses generative CoT + code verification. ThinkPRM (arXiv:2504.16828, 2025) achieves strong results with only 1% PRM800K labels via generative verification. These enhance inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning, and could serve as a backbone for generative verification methods.\n\n**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) verifies reasoning via attribution graph structural fingerprints (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) shows DAG-based dependency modeling yields +22pp failure detection recall. Multiple independent lines confirm graph structure carries powerful verification signal. **Existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV). PGCT is the first to inject premise-dependency topology directly into training-time representation learning.**\n\n**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive MI for PRM auto-labeling without dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension but operates on propositional-level pairs, not multi-step mathematical DAGs, and targets reading accuracy rather than PRM robustness.\n\n**Performance gap.** Best open-source PRM on PRMBench: 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling.\n\n## Proposed Approach\n\n**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's method with Qwen2.5-72B-Instruct (targeting >90% recall per PERL results on 70B-class models; ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode \"step j uses the result of step i as a premise.\"\n\n**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Difficulty-aware construction: score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7). Quality assurance: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity × difficulty levels) with thresholds (topology preservation ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap). Per-difficulty DAG extraction quality audit (easy/medium/hard/competition).\n\n**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision — \"same DAG topology → nearby embeddings, different topology → distant embeddings\"). This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions sequentially on preceding steps but operates in point-wise prediction paradigm without encoding relational structure in embedding space.\n\n**Scope clarification.** PGCT trains two complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning preserving surface fluency (via graph-breaking hard negatives). We claim premise-dependency awareness substantially narrows the consistency-causality gap, not full logical causality verification.\n\n**Data.** PRM800K + Math-Shepherd (~300K solutions) + ~600K contrastive pairs via LLM paraphrasing (7B/32B for generation, 72B for quality verification) and targeted premise-link corruption.\n\n## Evaluation Plan\n\n**Benchmarks (5-tier, with ID/OOD split):**\n1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 SOTA). ProcessBench (arXiv:2412.06559) with per-difficulty-level F1.\n2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64}. Report prm@N accuracy with ID/OOD breakdown.\n3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from \"Reward Under Attack\" (arXiv:2603.06621).\n4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct using PGCT-PRM vs. baseline PRMs as reward. 3000-5000 steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: hacking gap = (PRM score improvement) − (accuracy improvement); reward-accuracy Pearson r with 95% CI from 3 seeds; late-stage divergence ratio (final 30% training).\n5. **Representation analysis**: (a) Linear probing (per \"From Chains to DAGs\" methodology, arXiv:2601.17593): compare DAG structure encoding (node depth, pairwise distance, adjacency) in PGCT-PRM vs. standard PRM hidden states, layer by layer. (b) t-SNE/UMAP visualization of step embeddings: graph-preserving pairs should cluster, graph-breaking pairs should separate. (c) Quantitative topology metric: mean cosine similarity of graph-preserving pairs vs. graph-breaking pairs.\n\n**Baselines (6 tiers):**\n1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)\n2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)\n3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)\n4. Contrastive/concurrent: CPMI (arXiv:2604.10660)\n5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)\n6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891), ThinkPRM-7B (arXiv:2504.16828) — all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported\n- Data-matched control: ~900K total samples, contrastive pairs replaced with step-correctness annotations, standard BCE\n- Compute-matched control: equal total training FLOPs including DAG extraction overhead\n\n**Ablations (8 variants):**\n- A1: Remove InfoNCE loss → isolate contrastive learning contribution\n- A2: Remove step-correctness loss → test contrastive learning standalone\n- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**\n- A4: Only positives (no graph-breaking negatives)\n- A5: Only negatives (no graph-preserving positives)\n- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}\n- A7: DAG noise injection at 5%/10%/15%/20%\n- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve\n\n## Key References\n\n- Reward Under Attack (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- PARC/PERL (ICML 2025, arXiv:2502.02362)\n- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)\n- DAG-Math (arXiv 2025, arXiv:2510.19842)\n- ProofFlow (arXiv 2025, arXiv:2510.15981)\n- CRA (arXiv 2025, arXiv:2508.04216)\n- APRM (arXiv 2025, arXiv:2511.22888)\n- CRM (ICLR 2026, arXiv:2509.26578)\n- PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM (AAAI 2026, arXiv:2504.00891)\n- AgentEval (arXiv 2026, arXiv:2604.23581)\n- PRMBench (ACL 2025, arXiv:2501.03124)\n- ProcessBench (arXiv 2024, arXiv:2412.06559)\n- CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)\n- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)\n- ThinkPRM (arXiv 2025, arXiv:2504.16828)\n- CRV (ICLR 2026, arXiv:2510.09312)\n- R-PRM (arXiv 2025, arXiv:2503.21295)\n- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)\n- When Reward Hacking Rebounds (arXiv 2026, arXiv:2604.01476)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1600-2200 A100-hours (DAG extraction 72B: ~350h, pair generation 7B/32B + quality verification 72B: ~300h, PRM training + 8 ablations: ~550h, baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial + representation analysis: ~100h), timeline: 18-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,800-$6,600 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 1200-1600 A100-hours (~30% reduction from automated quality triage), timeline: 13-17 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,600-$4,800\n- **auto_research**: gpu_hours: 1800-2500 A100-hours (parallel sweeps), timeline: 9-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $5,400-$7,500, speed_bottleneck: DAG extraction quality validation per math subdomain requires serial human spot-checks"
}
````

---

### Runtime record

_source line 2 · 2026-05-27T09:13:30.812Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:13:30.812Z",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-27T09:13:30.825Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research data. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- "Reward Under Attack" (arXiv:2603.06621, 2026): 建立了 PRM 鲁棒性的三层诊断体系（静态扰动、对抗攻击、RL reward hacking）。确认 RL 策略可达 >0.9 PRM 分数但 <4% 真实准确率。43% reward gain 来自风格捷径。Proposal 的问题动机直接基于此论文，描述准确。
- "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, 2025): 确立了 PRM 检测"一致性"而非"因果性"的核心发现。Proposal 的核心 claim 直接建立在此之上，引用准确。
- PARC/PERL (ICML 2025, arXiv:2502.02362): 已确认为 ICML 2025 poster。70B 模型上 premise 识别 recall >90%，error identification 提升 6-16%。这是 PGCT 的关键技术前提，描述准确。**但注意：PARC 本身仅通过重构验证流程（不需要训练）即可带来 6-16% 提升，这构成 trivial alternative 威胁。**
- "From Chains to DAGs" (arXiv:2601.17593, 2026): 确认 LLM hidden states 线性编码 DAG 推理结构，中间层可恢复性最高。Proposal 的"representation-utilization gap"论点基于此。
- CRM (ICLR 2026, arXiv:2509.26578): 通过条件概率框架将每步 reward 条件化于前序步骤，解决 credit assignment 模糊性。在 BoN、beam search、RL 上一致优于已有 reward models。**与 PGCT 的关键区别：CRM 仍在 point-wise prediction paradigm 内，不在 embedding space 编码关系结构。** 描述准确。
- GenPRM (AAAI 2026, arXiv:2504.00891): 通过生成式 CoT + code verification 扩展 PRM test-time compute。已确认 AAAI 2026。属于 inference-time 增强，与 PGCT 的 training-time 方法正交。
- ThinkPRM (arXiv:2504.16828, 2025): 用 1% PRM800K 标签通过生成式验证 CoT 达到强结果。ThinkPRM-1.5B 在 MATH-500 上超越 DiscPRM ~5pp。同为 inference-time 方法。
- APRM (arXiv:2511.22888, 2025): 对抗性更难负样本，OOD +5.3pp。但负样本构造是 domain-agnostic 的。
- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350): 通过梯度反转分解 reward model embedding 为因果/非因果因子。在 representation space 操作但使用 domain-agnostic 统计分离。
- PathFinder-PRM-7B (arXiv:2505.19706): PRMBench 开源 SOTA 67.7，距人类 ceiling 83.8 仍有显著差距。
- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495): 构造 premise-oriented 对比样本用于逻辑阅读理解。最接近 PGCT 的前置工作，但目标不同（阅读准确率 vs. PRM 鲁棒性），粒度不同（命题级 vs. 多步数学 DAG）。

- **调研总结**: PRM 鲁棒性是 2025-2026 年的活跃研究热点，已有多种防御路线（对抗训练 APRM、条件建模 CRM、后处理 CRA、表示分解 Factored Causal RL、推理增强 GenPRM/ThinkPRM）。前提依赖 DAG 提取（PARC）和 LLM 表示中的 DAG 编码（Chains to DAGs）已分别被证实可行。**PGCT 处于"将已验证的 DAG 结构信号注入 PRM 训练时表示学习"这一具体交叉点上，该交叉点尚无直接竞争工作，但属于已有 building blocks 的自然组合。**

【Trivial Alternative 检验】:
存在明确的 trivial alternative 威胁：
1. **PARC 直接应用**：PARC/PERL 已证明，仅在 inference time 重构验证流程（引入 premise links）即可提升 error identification 6-16%，无需任何额外训练。PGCT 需要证明其 training-time contrastive learning 带来的增量显著超越这个零训练成本的 baseline。
2. **DAG 信息作为输入特征**：更简单的方法是将 DAG 邻接信息作为额外输入（如 positional encoding 或辅助 token）直接 feed 给 PRM，而非通过 contrastive learning 间接注入。Proposal 没有讨论这个 trivial alternative。
3. **APRM + premise-aware 负样本**：将 APRM 的对抗训练框架与 premise-aware 的负样本构造结合，不需要完整的 contrastive + InfoNCE 框架。

Proposal 对第 1 点部分回应了（"PGCT 是 training-time representation learning，与 inference-time 方法正交"），但"正交"不等于"增量显著"。对第 2、3 点完全未讨论。**增量价值的论证是 idea 层面的主要薄弱点。**

【前提假设检验】:
核心 claim 的逻辑链条中有以下未经验证的环节：

1. **"Representation-utilization gap 可通过 contrastive training 弥合"**：这是最关键的假设。"From Chains to DAGs" 证明 DAG 结构可从 hidden states 线性恢复，PARC 证明 premise links 可从模型输出提取。但"hidden states 中存在信息" ≠ "contrastive training 可以将该信息有效引导至 reward prediction"。线性可探测性(probe)和任务可利用性(task utility)之间存在已知 gap（Hewitt & Liang 2019 的 probe selectivity 问题）。Proposal 的核心假设——contrastive training 是弥合此 gap 的正确机制——缺乏理论或实证支撑。

2. **"DAG-anchored contrastive pairs 能产生泛化的结构感知"**：模型可能只学会检测训练时使用的特定扰动模式（如特定的 premise-link 断裂方式），而非发展出真正通用的 premise-dependency reasoning。这与 APRM 面临的"cat-and-mouse problem"本质上是同一挑战——proposal 批评 APRM 有此问题，但自身并未论证为何能避免。

3. **"Point-wise supervision 是问题根源"**：Proposal 将 PRM 脆弱性归因于"point-wise BCE training leaves dormant structural representations"。但 CRM (ICLR 2026) 表明通过条件概率框架（仍是 point-wise prediction）也能显著提升。问题可能不在于 point-wise vs. relational 的 supervision paradigm，而在于训练数据质量、标注噪声等其他因素。

【3 维度打分】:

1. **Novelty: 中** — "将 premise-dependency DAG 注入 PRM training-time representation learning"这一具体交叉点确实尚无直接竞争工作。与最相关工作的差异化是真实的：vs. CRM（point-wise paradigm，无 DAG topology）、vs. APRM（domain-agnostic negatives）、vs. Factored Causal RL（统计分离而非 domain-grounded structure）、vs. CRV/GoV（inference-time，非 training-time）、vs. Thought-Path CL（命题级阅读理解，非多步数学 PRM）。**但核心 insight——"用结构感知的对比对训练，得到结构感知的表示"——是给定 building blocks 后的自然下一步，而非反直觉发现。** 审稿人的反应更可能是 "I would have guessed this would work" 而非 "surprising"。Novelty 是组合性的（DAG extraction + contrastive learning + PRM training），而非概念性的。

2. **Significance: 中** — 问题本身重要性毋庸置疑：PRM 鲁棒性和 reward hacking 是 RLHF/reasoning 领域的核心痛点，PRMBench 上 SOTA (67.7) vs. 人类 (83.8) 的 gap 说明改进空间大。方法与 inference-time 增强（GenPRM/ThinkPRM）正交，理论上可叠加。**但影响力受限于：(a) 仅针对数学推理场景，推广到其他推理域（代码、常识、科学）需要重新设计 DAG extraction pipeline；(b) 依赖 72B 模型做 DAG extraction，实际部署门槛高；(c) 如果核心发现是 positive（contrastive training 提升了 PRMBench 几个点），影响力有限；如果 negative，则是一个有价值的 negative result 但发表难度大。**

3. **Related Work: 强** — 这是 proposal 最突出的优点。Related work 覆盖非常全面，涵盖 PRM 鲁棒性（APRM, CRA, CRM, PURE）、表示级方法（Factored Causal RL, "When Reward Hacking Rebounds"）、推理增强 PRM（R-PRM, GenPRM, ThinkPRM）、图结构验证（CRV, GoV, AgentEval）、并发工作（CPMI, RewardFlow）。差异化定位清晰——逐一论证了与每类方法的区别。引用的论文经验证均真实存在，描述准确。**唯一不足：未讨论 DAG 信息作为输入特征这一更简单的 alternative。**

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
- Related Work 维度为强，说明作者对领域理解深刻，定位专业——这保证了 proposal 的下限，降低了"被审稿人指出遗漏关键相关工作"的风险。
- Novelty 为中：交叉点确实新颖，但属于已有 building blocks 的自然组合，核心 insight 不够 surprising。这是概率上限的主要限制因素——在一个已经高度竞争的领域（2025-2026 年 PRM 改进方向涌现了 CRM, APRM, PURE, GenPRM, ThinkPRM 等多篇顶会），"自然组合"的 novelty 难以脱颖而出。
- Significance 为中：问题重要但方法的影响面受限于数学推理场景，且存在未充分回应的 trivial alternative 威胁（PARC zero-cost baseline）。
- 整体处于"idea 有实质内核，方向正确，但核心发现如果 positive 审稿人可能会说 'I would have guessed this'"的区间（rubric 25-35%），因 trivial alternative 未充分回应和领域拥挤度，中位数下调至 27%。

【主要风险】:
1. **Trivial alternative 威胁未充分化解**：PARC 在 inference time 零训练成本即可带来 6-16% 提升。审稿人会问："相比于直接用 PARC restructure 验证 + 标准 PRM，PGCT 的额外训练成本（72B DAG extraction + 600K contrastive pairs）换来的增量提升是否值得？"如果增量仅为几个百分点，cost-benefit 论证将很困难。
2. **"自然组合" novelty 在拥挤赛道上的竞争力**：2025-2026 年 PRM 改进方向密集出现多篇顶会/顶刊工作（CRM@ICLR'26, PURE@NeurIPS'25, GenPRM@AAAI'26）。在这个竞争格局下，"DAG + contrastive + PRM"的组合性 novelty 可能不足以让 3 位审稿人中的 2 位认为其达到 acceptance threshold。核心 insight 的 "surprisingness" 不足是最难通过实验补救的弱点。
```

Sources:
- [Reward Under Attack](https://arxiv.org/abs/2603.06621)
- [PARC/PERL - Premise-Augmented Reasoning Chains](https://arxiv.org/abs/2502.02362)
- [From Chains to DAGs](https://arxiv.org/pdf/2601.17593)
- [PRMBench](https://arxiv.org/abs/2501.03124)
- [CRM - Conditional Reward Modeling](https://arxiv.org/abs/2509.26578)
- [GenPRM](https://arxiv.org/pdf/2504.00891)
- [ThinkPRM](https://huggingface.co/papers/2504.16828)
- [R-PRM](https://arxiv.org/pdf/2503.21295)
- [Adversarial Training of Reward Models](https://arxiv.org/abs/2504.06141)
- [Factored Causal Representation Learning](https://arxiv.org/pdf/2601.21350)
- [PathFinder-PRM Error-Aware Hierarchical Supervision](https://arxiv.org/pdf/2505.19706)
- [Thought-Path Contrastive Learning (AAAI 2025)](https://arxiv.org/abs/2409.14495)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make an informed assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025):
   - 确认存在，作者 Yuhui Xu, Hanze Dong 等。核心发现：SOTA PRMs 优先评估结构一致性而非因果正确性；去掉问题陈述对奖励分数影响极小，而截断推理链或改变数值则影响显著。这是 proposal 的核心动机论文，描述准确。

2. "Reward Under Attack" (arXiv:2603.06621, Feb 2026):
   - 确认存在。量化了 PRM 的脆弱性：RL 训练的策略在 AIME 上达到 >0.9 PRM 分数但实际准确率 <4%，43% 的奖励增益来自风格捷径。发布了 PRM-BiasBench 诊断工具。Proposal 引用准确。

3. PARC/PERL (arXiv:2502.02362, ICML 2025):
   - 确认存在。PARC 将线性推理链重构为带前提链接的 DAG，前提识别在 70B+ 模型上达到 >90% recall，错误检测准确率提升 6-16%。Proposal 引用准确。

4. "From Chains to DAGs" (arXiv:2601.17593, Jan 2026):
   - 确认存在，Columbia University。通过轻量级探针证明 LLM 隐藏状态线性编码了 DAG 推理结构（节点深度、成对距离、邻接关系），在中间层可恢复性最高。Proposal 引用准确。

5. CRV (arXiv:2510.09312, ICLR 2026 Oral):
   - 确认存在，Meta FAIR。白盒方法，通过归因图的结构指纹来验证推理正确性。在 GSM8K 上达到 93.4% 准确率。关键区别：推理时白盒方法，非训练时表示学习。

6. PathFinder-PRM-7B (arXiv:2505.19706):
   - 确认存在。PRMBench SOTA 得分 67.7，通过分层解耦误差类型检测与奖励估计实现。Proposal 引用准确。

7. CPMI (arXiv:2604.10660, April 2026):
   - 确认存在。使用对比互信息进行 PRM 自动标注，不涉及依赖图。创建了 CPMI-80k 数据集。与 proposal 的方法正交。

8. RewardFlow (arXiv:2603.18859, March 2026):
   - 确认存在。在状态图上进行拓扑感知的奖励传播，用于代理推理任务。不使用对比训练。

9. Factored Causal Representation Learning (arXiv:2601.21350, ICML 2026):
   - 确认存在。通过梯度反转将奖励模型嵌入分解为因果/非因果因子。领域无关的统计分离方法。

10. PRMBench (arXiv:2501.03124, ACL 2025):
    - 确认存在。6,216 个问题，83,456 个步骤级标签，涵盖 soundness/sensitivity/simplicity 等细粒度错误类别。人类 ceiling 83.8。

- **调研总结**: PRM 鲁棒性是 2025-2026 年的热点研究方向，多条独立路线并行发展：(a) 对抗训练增强决策边界（APRM），(b) 表示空间因果分解（Factored Causal RL），(c) 架构级条件化（CRM），(d) 推理时图结构验证（CRV, GoV），(e) 推理增强生成式 PRM（R-PRM, GenPRM, ThinkPRM）。然而，**在训练时将前提依赖 DAG 拓扑结构注入 PRM 表示空间** 这一特定组合确实尚未被占据。Proposal 处于多条已有路线的交汇点，提出了一个新的组合方向。


【Trivial Alternative 检验】:

存在两个需要认真对待的 trivial alternative 威胁：

**威胁 1：PARC 输入增强 + 标准 PRM 训练。** PARC 已经证明，仅通过在推理链中显式标注前提链接（输入格式层面的改变），错误检测就提升了 6-16%。那么一个更简单的 baseline 是：不做对比训练，只是把 PARC 增强后的推理链作为 PRM 的输入，用标准 BCE 训练。如果这个 baseline 已经能捕获大部分 "前提依赖意识"，PGCT 的增量价值就很小。

**威胁 2：APRM 风格的对抗性硬负例 + 前提破坏。** APRM 通过生成更难的负例实现了 +5.3pp OOD 提升。如果把 PGCT 的"图破坏"负例直接作为 APRM 式的硬负例用于标准 BCE 训练（不用 InfoNCE，不做表示空间重组），效果是否相近？

**Proposal 的增量价值论证：** Proposal 认为 PGCT 的核心价值在于 *表示空间重组*（通过 InfoNCE 使嵌入空间编码拓扑结构），而非仅仅改善输入或决策边界。这个论证是合理的——PARC 改善输入，APRM 改善分类边界，PGCT 改善表示几何——但这个差异是否能转化为显著的下游效果，目前是未经验证的假设。A1/A3 消融设计（移除 InfoNCE / 随机扰动替代 DAG 扰动）理论上可以回答这个问题，但在 idea 层面，增量价值存在但不确定性较高。


【前提假设检验】:

核心逻辑链：
> LLM 隐藏状态编码了 DAG 结构 → 标准 PRM 训练未利用此结构 → DAG 锚定的对比训练可激活此结构 → 激活后的结构表示将提升鲁棒性

**假设 1**（已有证据支撑）："LLM 隐藏状态编码了 DAG 结构" — "From Chains to DAGs" 通过线性探针证明了这一点。✓

**假设 2**（部分支撑）："标准 PRM 训练未利用此结构" — "Reward Models Identify Consistency, Not Causality" 间接支持（PRMs 检测一致性而非因果性），但这不直接等价于"DAG 结构表示未被利用"。一致性检测也可能隐式使用了某些结构信息，只是不够。这里存在推理跳跃。⚠️

**假设 3**（核心未验证假设）："DAG 锚定的对比训练可以激活休眠的结构表示" — 这是整个 proposal 的核心赌注。存在两个子问题：
- (a) 从"线性探针可恢复"到"对比训练可利用"的跳跃。线性探针证明信息存在，但对比训练能否有效地将这种信息路由到奖励预测头，取决于优化景观的具体性质，这是未知的。
- (b) InfoNCE 损失的梯度信号是否足够强大且方向正确，能够重组已经被大规模预训练塑造的表示空间？如果结构信息在深层但奖励头连接浅层，梯度传播可能不够有效。

**假设 4**（合理但二阶不确定）："表示空间的结构化将转化为鲁棒性提升" — 即使嵌入空间确实编码了更好的 DAG 结构，这是否必然导致对风格捷径和对抗攻击的鲁棒性？可能存在"表示好但决策边界仍被利用"的情况。

**总结**：逻辑链前端有证据支撑，但核心环节（假设 3）是一个有合理动机但未经验证的 leap of faith。这不是致命的——许多好论文的核心贡献就是验证这样的假设——但如果结果为负，paper 的价值会大幅下降。


【3 维度打分】:

**1. Novelty: 中（偏强）**

理由：
- 正面：将前提依赖 DAG 拓扑注入训练时表示学习确实是一个未被占据的组合。我的调研确认：CRV 和 GoV 在推理时使用图结构，Factored Causal RL 在训练时操作表示空间但使用领域无关的统计分离，APRM 使用对抗硬负例但不编码逻辑结构，CPMI 使用对比方法但不涉及依赖图。PGCT 处于这些工作的交汇点，组合确实是新的。
- 负面："表示-利用间隙"的 framing 虽然有吸引力，但本质上是"已有方法 A（DAG 提取）+ 已有方法 B（对比学习）应用于已知问题 C（PRM 鲁棒性）"的组合创新。各个组件都不是新的。如果核心实验结果 positive，审稿人更可能说 "this is a natural next step that makes sense" 而非 "this is surprising"。Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) 已经在前提级别做了对比学习（虽然是阅读理解而非 PRM），概念距离并不大。

**2. Significance: 强**

理由：
- PRM 鲁棒性和 reward hacking 是数学推理领域最紧迫的问题之一。"Reward Under Attack" 的发现（>0.9 PRM 分数但 <4% 准确率）表明这不是边际问题，而是系统性失败。
- PRMBench 上 67.7 vs 83.8 的人类 ceiling 差距表明该领域有大量改进空间。
- 方法与现有路线（生成式 PRM、条件奖励建模等）正交，潜在可组合性高。
- 如果"表示空间的结构化确实能提升鲁棒性"这一假设被验证，将为 PRM 训练提供一种新的原则性方法论，影响面超越数学推理。
- 局限：当前方法高度依赖数学推理的可结构化特性，向其他领域（代码、科学推理等）的推广需要额外论证。

**3. Related Work: 强**

理由：
- 覆盖极为全面。我验证了 20+ 篇引用论文，全部真实存在且描述准确。
- 与每条竞争路线的差异化定位清晰且有说服力：
  - 区分于 APRM（领域无关对抗负例 vs 结构锚定对比对）
  - 区分于 CRV（推理时白盒 vs 训练时表示学习）
  - 区分于 Factored Causal RL（统计因子分离 vs 领域接地的结构先验）
  - 区分于 CPMI（对比自动标注 vs 对比表示学习）
  - 区分于 RewardFlow（图上奖励传播 vs 对比训练）
- 论文引用到 2026 年 4 月（AgentEval、CPMI、"When Reward Hacking Rebounds"），时效性极好。
- 唯一微小遗漏：Robust Reward Modeling via Causal Rubrics (arXiv:2506.16507, June 2026)，但这可能是在 proposal 撰写之后发表的。


【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
Significance 是本 proposal 的强项，问题真实且重要，时效性好。Related Work 覆盖和定位是顶级水平。Novelty 是限制上界的主要因素——虽然组合确实是新的，但核心机制（DAG 提取 + InfoNCE 对比学习）都是已知技术的组合应用，缺乏深层的 methodological surprise。一个理想审稿人看到这个 idea 可能会说："This is a well-motivated and natural next step, but the intellectual contribution is in the engineering of the combination rather than a fundamental insight." 这使得中稿概率的上界受限。

此外，trivial alternative 威胁是实质性的：如果 PARC 增强输入 + APRM 式硬负例已经能获得大部分收益，PGCT 的表示空间重组带来的 *增量* 提升可能不够大，这在审稿中可能被直接质疑。核心假设 3（对比训练激活休眠结构表示）的理论根基也不够坚实——它有合理的直觉但缺乏理论保证。

概率未到 40%+ 是因为缺少 "surprising" 的维度——核心发现如果 positive，多数审稿人会认为 "makes sense given the setup" 而非 "I wouldn't have predicted this"。概率未低于 28% 是因为问题确实重要、定位确实独特、且当前 SOTA 有大量改进空间。

【主要风险】:
1. **Trivial alternative 质疑**：审稿人可能要求与"PARC 输入增强 + 标准 BCE"和"DAG 破坏负例 + 标准 BCE（无 InfoNCE）"进行对比，如果这些更简单的方法效果相近，paper 的核心贡献将被严重削弱。
2. **核心假设未被充分 justify**：从"隐藏状态中线性可探测 DAG 结构"到"对比训练可激活此结构以改善奖励预测"的逻辑跳跃缺乏理论支撑，审稿人可能认为这只是一个 empirical bet，idea 层面的贡献不足以支撑顶会论文。
```

Sources:
- [Reward Under Attack](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL: Premise-Augmented Reasoning Chains](https://arxiv.org/abs/2502.02362)
- [From Chains to DAGs](https://arxiv.org/abs/2601.17593)
- [CRV: Verifying Chain-of-Thought Reasoning via Its Computational Graph](https://arxiv.org/abs/2510.09312)
- [PathFinder-PRM](https://arxiv.org/abs/2505.19706)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [RewardFlow](https://arxiv.org/abs/2603.18859)
- [Factored Causal Representation Learning for Robust Reward Modeling](https://arxiv.org/abs/2601.21350)
- [PRMBench](https://arxiv.org/abs/2501.03124)
- [DAG-Math](https://arxiv.org/abs/2510.19842)
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/pdf/2506.16507)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient literature context. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025): 确立了 PRM 检测的是 surface consistency 而非 causal correctness 的核心问题。移除题目对 reward score 影响极小，而打乱推理流则影响显著。这是本 proposal 的直接出发点，确认其问题动机真实存在。
- "Reward Under Attack" (arXiv:2603.06621, Feb 2026): 量化了 PRM 的脆弱性——43% reward gain 来自 stylistic shortcuts，RL 训练策略可达 >0.9 PRM score 但实际准确率 <4%。建立了三层诊断框架。确认了 PRM robustness 是一个严肃的开放问题。
- PARC/PERL (ICML 2025, arXiv:2502.02362): 证明了 premise dependency links 可以从推理链中提取（70B+ 模型 >90% recall），且用于推理时 error detection 可提升 6-16%。关键点：这是 **inference-time** 的应用，并未将 premise 结构注入 training-time representation learning。
- "From Chains to DAGs" (arXiv:2601.17593, Jan 2026): 证明 LLM hidden states 已经线性编码了 DAG 推理结构（node depth, pairwise distance, adjacency）。这支持了 proposal 的 "representation-utilization gap" 假说——结构信息存在于 base model 但未被 PRM 训练利用。
- CRM (ICLR 2026, arXiv:2509.26578): 通过 sequential conditioning 建模 step 间依赖关系，但在 point-wise prediction paradigm 内操作，不编码 embedding space 中的 relational structure。
- CRV (ICLR 2026 Oral, arXiv:2510.09312): 使用 attribution graph 的结构 fingerprints 做白盒推理验证。图结构用于 inference-time，非 training-time。
- PathFinder-PRM-7B (arXiv:2505.19706): 当前 PRMBench 开源 SOTA (67.7)，vs 人类 83.8，确认了性能鸿沟的存在。
- GenPRM (AAAI 2026, arXiv:2504.00891): 通过 generative CoT + code verification 增强 PRM。ThinkPRM (arXiv:2504.16828) 用仅 1% PRM800K labels 实现了强结果。R-PRM (arXiv:2503.21295) 在 ProcessBench 上 +11.9 F1。这些都是 **inference-time** reasoning enhancement。
- CPMI (arXiv:2604.10660, Apr 2026): 用 contrastive MI 做 PRM auto-labeling，**无** dependency graph 结构。
- RewardFlow (arXiv:2603.18859, Mar 2026): 在 state-transition graph 上传播 reward，**无** contrastive training。
- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495): 对 propositional-level 的 premise-oriented contrastive pairs 做阅读理解，非多步数学推理 DAG，非 PRM robustness。
- APRM (arXiv:2511.22888, Nov 2025): 用 adversarial harder negatives 提升 PRM (+5.3pp OOD)，但 negatives 是 domain-agnostic 的，非基于 logical dependency structure。

- **调研总结**: PRM robustness 是一个活跃且重要的研究方向，近 12 个月内涌现了大量工作（CRM, PURE, CRA, APRM, CRV, PathFinder-PRM 等）。目前存在两条独立的线索：(1) 表示空间鲁棒性方法（不使用领域特定逻辑结构），(2) 图结构验证方法（仅用于推理时）。本 proposal 试图将 premise-dependency DAG 结构注入 training-time representation learning，确实是两条线索的交叉空白。但这个交叉点的「自然程度」很高——给定 PARC 和 "From Chains to DAGs" 的结论，将结构先验引入 PRM 训练是一个相当直觉的 next step。

【Trivial Alternative 检验】:
存在至少两个成本更低的替代方案构成实质威胁：

1. **"Premise-aware data augmentation + 标准 BCE"**：直接将 premise-breaking negative examples 加入 PRM 训练数据（使用与 proposal 相同的 DAG-guided corruption 方法），但不引入 InfoNCE contrastive loss，仍用标准 BCE。这本质上是 APRM 的 domain-specific 版本。Proposal 的增量价值必须证明 contrastive objective **本身**（而非仅仅 DAG-guided negatives 的数据质量）带来了显著收益。Ablation A1（去掉 InfoNCE）可以测试这一点，但如果 A1 和 full PGCT 差异不大，整个 idea 的核心 claim 就会坍塌。

2. **"CRM + PARC inference-time pipeline"**：CRM 已经建模 sequential dependency，PARC 已经能在推理时提取 premise links 并提升 error detection。两者的简单组合（CRM 做 reward prediction + PARC 做 inference-time premise-aware verification）可能是一个更轻量的 baseline，不需要任何新的训练方法。

3. **Linear probe auxiliary loss**：Proposal 主张这只优化 local-layer information retention 而不影响 cross-layer representation flow。这是一个 **论断而非证据**。一个简单的多层 auxiliary loss 可能同样有效。

**增量价值**：如果 contrastive objective 确实优于上述替代方案，那增量在于 embedding space 的 global topology reorganization——这是一个有意义的技术贡献。但这必须通过实验证明，目前只是假说。

【前提假设检验】:
核心逻辑链：DAG 结构存在于 hidden states (From Chains to DAGs) → 标准 PRM 训练未利用 (Consistency not Causality) → contrastive training 可以激活这些 dormant representations → 激活后的 structural embedding 转化为更好的 reward prediction

关键未验证环节：

1. **"Dormant representations" 假设**：From Chains to DAGs 证明 base model 编码了 DAG 结构。但 PRM fine-tuning 可能已经 **摧毁** 了这些表示（catastrophic forgetting），而非仅仅"未利用"。如果 PRM 训练后 DAG 结构已不存在于 hidden states，那么 contrastive training 需要 **重建** 而非"激活"，这是一个更强的要求。

2. **Embedding topology → reward accuracy**：即使 contrastive training 成功使 embedding space 编码了 DAG topology（graph-preserving pairs cluster, graph-breaking pairs separate），这并不自动意味着 step-level reward prediction 会更准确。从 representation structure 到 downstream task performance 的 gap 是存在的。

3. **DAG extraction quality at scale**：PARC/PERL 的 >90% recall 是在 curated datasets 上验证的。扩展到 PRM800K + Math-Shepherd 的 ~300K solutions，DAG extraction 质量可能显著下降，尤其是在复杂的竞赛数学题上。Proposal 承认需要 72B 模型做 extraction，但未讨论 failure modes。

4. **Contrastive pair quality**：生成 "graph-breaking but fluent" negatives 是困难的——需要精确切断特定 premise link 同时保持表面流畅和其余逻辑结构不变。这种合成数据的质量直接决定方法的上限。

【3 维度打分】:
1. **Novelty: 中** — 
   从调研来看，将 premise-dependency DAG 结构注入 training-time PRM representation learning 确实是文献中的空白：CRV (ICLR 2026) 和 PARC (ICML 2025) 使用图结构但限于 inference-time；APRM 使用 adversarial negatives 但 domain-agnostic；Factored Causal RL (ICML 2026) 操作 representation space 但用 domain-agnostic statistical separation。因此 PGCT 的定位确实是新的。
   
   但这个新颖性更像是 **natural combination** 而非 **conceptual breakthrough**。给定 PARC 已证明 premise links 可提取且有用，"From Chains to DAGs" 已证明 DAG structure 编码于 hidden states，APRM 已展示 adversarial negatives 提升 PRM——将三者组合（domain-specific structural negatives + contrastive training）是一个相当直觉的 engineering step。审稿人不太可能说 "I wouldn't have thought of this"，更可能说 "this is a reasonable next step." Thought-Path Contrastive Learning (AAAI 2025) 已经在更简单的设置（propositional-level, reading comprehension）中证明了 premise-oriented contrastive learning 的有效性，进一步降低了 PGCT 的 surprise factor。

2. **Significance: 中** — 
   PRM robustness 确实是一个重要且活跃的研究问题，"Reward Under Attack" 的发现（43% stylistic shortcuts, >0.9 score <4% accuracy）表明问题的严重性。PRMBench 上 67.7 vs 83.8 human ceiling 的差距也表明有大量改进空间。
   
   但 significance 受限于两点：(a) 方法仅适用于数学推理这一特定领域（premise DAGs 在数学链中最容易定义和提取），向 code reasoning、commonsense reasoning 等其他领域的推广路径不清晰；(b) 如果 inference-time 方法（如 GenPRM, ThinkPRM, R-PRM）已经通过 generative verification 大幅提升了 PRM 性能，training-time representation learning 的增量价值可能被压缩——proposal 声称与 inference-time 方法 "orthogonal"，但未论证两者组合后是否有 meaningful 的叠加收益。

3. **Related Work: 强** — 
   Related work 覆盖非常全面，涵盖了 PRM robustness（CRA, APRM, CRM, PURE）、representation-level robustness（Factored Causal RL, When Reward Hacking Rebounds）、reasoning-enhanced PRMs（R-PRM, GenPRM, ThinkPRM）、graph structure for verification（CRV, GoV, AgentEval）、concurrent approaches（CPMI, RewardFlow, Thought-Path CL）等多条线索。差异化定位清晰，明确指出 PGCT 是 "first to inject premise-dependency topology directly into training-time representation learning"。引用的关键论文（PARC/PERL ICML 2025, CRM ICLR 2026, CRV ICLR 2026 Oral, GenPRM AAAI 2026, PRMBench ACL 2025）均经搜索确认真实存在且描述基本准确。

【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
Related Work 覆盖强，定位清晰，问题动机真实——这些保证了下限不会太低。但 Novelty 为 "中"（natural combination 而非 conceptual surprise）是上界的主要限制因素。核心技术贡献——contrastive training anchored to premise DAGs——的增量价值面临 trivial alternative 威胁（DAG-guided negatives + 标准 BCE 可能就够了），且 "representation-utilization gap" 假设的两个关键环节（dormant representations 在 PRM fine-tuning 后是否存留; embedding topology improvement 是否转化为 reward prediction improvement）均未验证。Significance 受限于数学推理单一领域。综合来看，这是一个 solid but unsurprising 的研究方向，审稿人更可能评价为 "competent incremental work" 而非 "exciting contribution"，估计处于 25-35% 区间的偏下位置。

【主要风险】: 
1. **Trivial alternative 致命威胁**：Ablation A1（去掉 InfoNCE，只保留 DAG-guided negatives + BCE）如果与 full PGCT 差异不显著，则核心 claim（contrastive objective 本身的价值）被否定，论文沦为 "better data augmentation for PRMs"——novelty 从 "中" 降至 "弱"。
2. **"Natural next step" 定性**：审稿人熟悉 PARC + "From Chains to DAGs" + contrastive learning 后，很可能认为这个组合是一个 obvious direction，导致 novelty 评分偏低。Proposal 需要在实验中证明 contrastive objective 的 mechanism（而非仅仅 DAG-guided negatives 的数据质量）是成功的关键，但这一点目前只是假说。
```

Sources:
- [Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality (arXiv:2502.14619)](https://arxiv.org/abs/2502.14619)
- [PARC/PERL (ICML 2025, arXiv:2502.02362)](https://arxiv.org/abs/2502.02362)
- [From Chains to DAGs (arXiv:2601.17593)](https://arxiv.org/pdf/2601.17593)
- [CRM (ICLR 2026, arXiv:2509.26578)](https://arxiv.org/abs/2509.26578)
- [CRV (ICLR 2026, arXiv:2510.09312)](https://arxiv.org/abs/2510.09312)
- [PathFinder-PRM (arXiv:2505.19706)](https://arxiv.org/pdf/2505.19706)
- [GenPRM (AAAI 2026, arXiv:2504.00891)](https://arxiv.org/abs/2504.00891)
- [ThinkPRM (arXiv:2504.16828)](https://huggingface.co/papers/2504.16828)
- [CPMI (arXiv:2604.10660)](https://arxiv.org/abs/2604.10660)
- [RewardFlow (arXiv:2603.18859)](https://arxiv.org/abs/2603.18859)
- [PRMBench (ACL 2025, arXiv:2501.03124)](https://arxiv.org/abs/2501.03124)
- [DAG-Math (arXiv:2510.19842)](https://arxiv.org/abs/2510.19842)
- [Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)](https://arxiv.org/abs/2409.14495)


【原始 proposal（允许参考但不是主要依据）】:
# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models

## Core Problem

Current process reward models detect consistency rather than causality. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025) established that PRMs verify surface-level coherence between steps — not whether each step logically follows from its premises. "Reward Under Attack" (arXiv:2603.06621, Feb 2026) quantified the consequences: 43% of PRM reward gains stem from stylistic shortcuts, and RL-trained policies achieve >0.9 PRM scores but <4% actual accuracy. The root cause is that standard PRM training provides only point-wise step-correctness supervision, which is blind to the logical dependency structure connecting reasoning steps. Can we train PRMs whose representations explicitly encode premise-dependency awareness rather than mere surface consistency?

## Research Opportunity and Key Insight

A critical representation-utilization gap exists in current PRMs. "From Chains to DAGs" (arXiv:2601.17593, Jan 2026) proved that LLM hidden states already linearly encode DAG reasoning structure — node depth, pairwise distance, and adjacency are recoverable from intermediate layers via lightweight probes. Yet standard PRM training fails to channel this latent structural knowledge into reward prediction (arXiv:2502.14619). PARC/PERL (ICML 2025, arXiv:2502.02362) demonstrated that premise dependency links are extractable at >90% recall (on 70B+ models), improving error detection by 6-16%. DAG-Math (arXiv:2510.19842, 2025) and ProofFlow (arXiv:2510.15981, 2025) further established feasibility of dependency graph extraction at scale.

Our key insight: contrastive training anchored to premise dependency DAGs can bridge this representation-utilization gap. By constructing training pairs that hold surface form constant while varying logical structure (and vice versa), we force the PRM's embedding space to explicitly encode premise-dependency relationships — activating structural representations the model already possesses but that point-wise BCE training leaves dormant. This constitutes a shift from point-wise supervision (each step independently correct/incorrect) to relational supervision (structural relationships between steps encoded in representation space). An alternative approach — using linear probes as auxiliary loss to directly maximize DAG-structure recovery in hidden states — would only optimize local-layer information retention without affecting cross-layer representation flow or end-to-end reward prediction; contrastive training directly constrains the reward-relevant embedding space, providing end-to-end structural injection.

## Research Landscape

**PRM robustness: existing defenses.** "Reward Under Attack" (arXiv:2603.06621) established the three-tier diagnostic: static perturbation exploitability, adversarial token-level attacks, and RL-induced reward hacking. Defenses include CRA (Aug 2025, arXiv:2508.04216, post-hoc SAE correction), APRM (Nov 2025, arXiv:2511.22888, adversarial harder negatives, +5.3pp OOD), CRM (ICLR 2026, arXiv:2509.26578, sequential conditioning), and PURE (NeurIPS 2025, arXiv:2504.15275, min-form credit aggregation). None uses explicit logical dependency structure in PRM training. APRM's adversarial negatives improve the single-step classification decision boundary but remain domain-agnostic — the PRM learns to resist specific patterns without understanding why they are wrong, leaving it vulnerable to novel attacks (cat-and-mouse problem). PGCT instead reorganizes the PRM's representation space around premise-dependency topology.

**Representation-level robustness.** Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350) decomposes reward model embeddings into causal/non-causal factors via gradient reversal. "When Reward Hacking Rebounds" (arXiv:2604.01476, April 2026) extracts shortcut concept directions from contrastive pairs via representation engineering. Both operate in representation space but use domain-agnostic statistical separation (gradient reversal, concept directions). PGCT differs fundamentally: its structural prior is domain-grounded — premise dependency DAGs extracted from mathematical reasoning chains — rather than learned statistical factors. This provides interpretable, verifiable structural constraints rather than latent factor separation.

**Reasoning-enhanced PRMs.** R-PRM (arXiv:2503.21295, 2025) augments PRMs with reasoning-driven critique (+11.9 F1 on ProcessBench, +8.5 on PRMBench). GenPRM (AAAI 2026, arXiv:2504.00891) uses generative CoT + code verification. ThinkPRM (arXiv:2504.16828, 2025) achieves strong results with only 1% PRM800K labels via generative verification. These enhance inference-time reasoning. PGCT is orthogonal: it improves training-time representation learning, and could serve as a backbone for generative verification methods.

**Graph structure for verification.** CRV (ICLR 2026, arXiv:2510.09312) verifies reasoning via attribution graph structural fingerprints (white-box, inference-time). GoV decomposes reasoning into DAGs for training-free verification. AgentEval (arXiv:2604.23581, 2026) shows DAG-based dependency modeling yields +22pp failure detection recall. Multiple independent lines confirm graph structure carries powerful verification signal. **Existing approaches either reorganize representation space without domain-specific logical structure (Factored Causal RL) or leverage graph structure only at inference time (GoV, CRV). PGCT is the first to inject premise-dependency topology directly into training-time representation learning.**

**Concurrent contrastive/graph approaches.** CPMI (arXiv:2604.10660, April 2026) uses contrastive MI for PRM auto-labeling without dependency graphs. RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs without contrastive training. Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495) constructs premise-oriented contrastive examples for logical reading comprehension but operates on propositional-level pairs, not multi-step mathematical DAGs, and targets reading accuracy rather than PRM robustness.

**Performance gap.** Best open-source PRM on PRMBench: 67.7 (PathFinder-PRM-7B, arXiv:2505.19706) vs. 83.8 human ceiling.

## Proposed Approach

**DAG extraction.** Extract premise dependency DAGs from mathematical reasoning chains using PARC's method with Qwen2.5-72B-Instruct (targeting >90% recall per PERL results on 70B-class models; ICML 2025, arXiv:2502.02362). Each reasoning step is a node; directed edges encode "step j uses the result of step i as a premise."

**Contrastive pair construction.** Two types of structure-aware pairs: (1) Graph-preserving surface perturbations (rephrased steps, identical DAG topology) as positives; (2) Graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps maintaining surface fluency) as hard negatives. Difficulty-aware construction: score all hard negatives with a baseline PRM to ensure sufficient proportion (>30%) of genuinely hard cases (baseline PRM score >0.7). Quality assurance: re-extract DAGs from generated pairs to verify topology preservation/breaking; stratified human audit (~1000 pairs across math subdomains × DAG complexity × difficulty levels) with thresholds (topology preservation ≥90% for positives, premise-link corruption verification ≥85% for negatives) and inter-annotator agreement (2 annotators, Cohen's κ on ~200-pair overlap). Per-difficulty DAG extraction quality audit (easy/medium/hard/competition).

**Dual objective training.** Qwen2.5-Math-7B-Instruct-based PRM with: (a) standard step-correctness BCE loss (point-wise supervision), and (b) graph-contrastive InfoNCE loss over DAG-anchored step embeddings (relational supervision — "same DAG topology → nearby embeddings, different topology → distant embeddings"). This complements CRM (ICLR 2026, arXiv:2509.26578), which conditions sequentially on preceding steps but operates in point-wise prediction paradigm without encoding relational structure in embedding space.

**Scope clarification.** PGCT trains two complementary capabilities: (1) structural dependency sensitivity — detecting whether premise links between steps are correctly maintained (via DAG topology contrastive learning), and (2) partial semantic inference validity — detecting logically invalid reasoning preserving surface fluency (via graph-breaking hard negatives). We claim premise-dependency awareness substantially narrows the consistency-causality gap, not full logical causality verification.

**Data.** PRM800K + Math-Shepherd (~300K solutions) + ~600K contrastive pairs via LLM paraphrasing (7B/32B for generation, 72B for quality verification) and targeted premise-link corruption.

## Evaluation Plan

**Benchmarks (5-tier, with ID/OOD split):**
1. **Step-level error detection**: PRMBench (ACL 2025, arXiv:2501.03124) with per-error-category breakdown (soundness/sensitivity/simplicity; redundancy, circular logic, step inconsistency, domain inconsistency, deceptive logical steps), targeting >70 overall (vs. 67.7 SOTA). ProcessBench (arXiv:2412.06559) with per-difficulty-level F1.
2. **Downstream best-of-N reranking**: ID: MATH500, GSM8K; OOD: AIME 2024, AMC. N ∈ {8, 16, 64}. Report prm@N accuracy with ID/OOD breakdown.
3. **Adversarial robustness**: PRM-BiasBench and perturbation suite from "Reward Under Attack" (arXiv:2603.06621).
4. **RL closed-loop reward hacking**: GRPO training of Qwen2.5-Math-7B-Instruct using PGCT-PRM vs. baseline PRMs as reward. 3000-5000 steps, checkpoint every 200 steps, evaluate on MATH and AIME. Metrics: hacking gap = (PRM score improvement) − (accuracy improvement); reward-accuracy Pearson r with 95% CI from 3 seeds; late-stage divergence ratio (final 30% training).
5. **Representation analysis**: (a) Linear probing (per "From Chains to DAGs" methodology, arXiv:2601.17593): compare DAG structure encoding (node depth, pairwise distance, adjacency) in PGCT-PRM vs. standard PRM hidden states, layer by layer. (b) t-SNE/UMAP visualization of step embeddings: graph-preserving pairs should cluster, graph-breaking pairs should separate. (c) Quantitative topology metric: mean cosine similarity of graph-preserving pairs vs. graph-breaking pairs.

**Baselines (6 tiers):**
1. Standard PRM: Qwen2.5-Math-PRM-7B (same base model)
2. Robustness-focused: APRM (arXiv:2511.22888), CRA (arXiv:2508.04216)
3. Architecture-level: CRM (ICLR 2026, arXiv:2509.26578), PURE (NeurIPS 2025, arXiv:2504.15275)
4. Contrastive/concurrent: CPMI (arXiv:2604.10660)
5. Error-aware: PathFinder-PRM-7B (arXiv:2505.19706)
6. Reasoning-enhanced: R-PRM (arXiv:2503.21295), GenPRM-7B (AAAI 2026, arXiv:2504.00891), ThinkPRM-7B (arXiv:2504.16828) — all under fixed inference-compute budget for fair comparison; unrestricted comparison also reported
- Data-matched control: ~900K total samples, contrastive pairs replaced with step-correctness annotations, standard BCE
- Compute-matched control: equal total training FLOPs including DAG extraction overhead

**Ablations (8 variants):**
- A1: Remove InfoNCE loss → isolate contrastive learning contribution
- A2: Remove step-correctness loss → test contrastive learning standalone
- A3: Random perturbation replacing DAG-aware perturbation → **critical: isolate DAG structure contribution**
- A4: Only positives (no graph-breaking negatives)
- A5: Only negatives (no graph-preserving positives)
- A6: Loss weighting λ ∈ {0.1, 0.3, 0.5, 0.7, 1.0}
- A7: DAG noise injection at 5%/10%/15%/20%
- A8: DAG extraction model scale: 7B / 32B / 72B extractors → practical viability curve

## Key References

- Reward Under Attack (arXiv 2026, arXiv:2603.06621)
- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)
- PARC/PERL (ICML 2025, arXiv:2502.02362)
- From Chains to DAGs (arXiv 2026, arXiv:2601.17593)
- DAG-Math (arXiv 2025, arXiv:2510.19842)
- ProofFlow (arXiv 2025, arXiv:2510.15981)
- CRA (arXiv 2025, arXiv:2508.04216)
- APRM (arXiv 2025, arXiv:2511.22888)
- CRM (ICLR 2026, arXiv:2509.26578)
- PURE (NeurIPS 2025, arXiv:2504.15275)
- GenPRM (AAAI 2026, arXiv:2504.00891)
- AgentEval (arXiv 2026, arXiv:2604.23581)
- PRMBench (ACL 2025, arXiv:2501.03124)
- ProcessBench (arXiv 2024, arXiv:2412.06559)
- CPMI (arXiv 2026, arXiv:2604.10660)
- RewardFlow (arXiv 2026, arXiv:2603.18859)
- PathFinder-PRM (arXiv 2025, arXiv:2505.19706)
- Thought-Path Contrastive Learning (AAAI 2025, arXiv:2409.14495)
- ThinkPRM (arXiv 2025, arXiv:2504.16828)
- CRV (ICLR 2026, arXiv:2510.09312)
- R-PRM (arXiv 2025, arXiv:2503.21295)
- Factored Causal Representation Learning (ICML 2026, arXiv:2601.21350)
- When Reward Hacking Rebounds (arXiv 2026, arXiv:2604.01476)

## Resource Estimate

- **manual**: gpu_hours: 1600-2200 A100-hours (DAG extraction 72B: ~350h, pair generation 7B/32B + quality verification 72B: ~300h, PRM training + 8 ablations: ~550h, baseline reproduction/evaluation: ~150h, RL closed-loop × 3 seeds: ~250h, best-of-N + adversarial + representation analysis: ~100h), timeline: 18-22 weeks for 2-3 researchers, estimated_gpu_cost: $4,800-$6,600 at $3/hr A100 spot pricing
- **human_in_loop**: gpu_hours: 1200-1600 A100-hours (~30% reduction from automated quality triage), timeline: 13-17 weeks for 2 researchers, claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,600-$4,800
- **auto_research**: gpu_hours: 1800-2500 A100-hours (parallel sweeps), timeline: 9-12 weeks automated, claude_api_cost: $1,500-$2,000, estimated_gpu_cost: $5,400-$7,500, speed_bottleneck: DAG extraction quality validation per math subdomain requires serial human spot-checks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f53d9321-eec8-49d1-8e75-a1a393f76adc",
  "type": "user",
  "uuid": "19fc2fc6-af8b-4562-917a-8aef89573092",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:13:30.823Z_

```json
{
  "parentUuid": "19fc2fc6-af8b-4562-917a-8aef89573092",
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
  "uuid": "db7a0c07-283b-43ff-8092-c31ca7448497",
  "timestamp": "2026-05-27T09:13:30.823Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:13:30.824Z_

```json
{
  "parentUuid": "db7a0c07-283b-43ff-8092-c31ca7448497",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e80339bc-3ab3-4c79-abb7-f58c67165a00",
  "timestamp": "2026-05-27T09:13:30.824Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data. Let me compile my assessm…",
  "leafUuid": "e80339bc-3ab3-4c79-abb7-f58c67165a00",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis on premise-graph contrastive PRM proposal",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780"
}
```

---

### Assistant

_source line 8 · 2026-05-27T09:14:03.554Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 33%] 中位 27%

**Reviewer 2:**
- Novelty: 中（偏强）
- Significance: 强


- Related Work: 强
- Probability: [28% - 38%] 中位 33%

**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [23% - 33%] 中位 28%

Now I'm aggregating the three median probabilities—27%, 33%, and 28%—which gives me a mean of 29.3% and a median of 28%. I'm calculating the standard deviation to understand the spread across the reviewers' assessments. So the standard deviation puts this in the borderline range between moderate and high consensus. Now I'm mapping out where the reviewers actually agree versus where they diverge—novelty, related work, and the core concerns about trivial alternatives and unverified assumptions are unanimous across all three, while significance is the main point of contention with two reviewers rating it as moderate and one as strong.

Given this moderate consensus pattern, I should widen the confidence interval and lean toward the stricter assessment, which comes from R1.

Looking at the implementation requirements—the GPU compute needs, timeline constraints, model size requirements, and quality assurance processes—I'm settling on a final probability range of 22-33% with a median around 28%, which sits between R1's stricter estimate and R2's more optimistic one.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e80339bc-3ab3-4c79-abb7-f58c67165a00",
  "isSidechain": false,
  "requestId": "req_011CbSpMxY4HbHFJupfQ8Wuk",
  "type": "assistant",
  "uuid": "1f1ee48c-5960-4521-a746-e60c58246aa6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168fgJhYHndxjssA4gEa9qa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18675,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3571,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18675
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

_source line 9 · 2026-05-27T09:14:56.073Z_

【阶段】: Meta Judge
【三次中位】: [27%, 33%, 28%] std=3.2%
【共识维度】:
- **Novelty = 中**（3/3 一致）：三位审稿人均认为"将 premise-dependency DAG 注入 training-time PRM representation learning"是文献空白处的真实定位，但本质是已有 building blocks（PARC DAG extraction + contrastive learning + PRM training）的 natural combination，而非 conceptual breakthrough。R2 标注"中偏强"但仍归入"中"档。三人均使用了"I would have guessed this would work" / "natural next step" / "reasonable next step"的表述，收敛度极高。
- **Related Work = 强**（3/3 一致）：三人一致认为 related work 覆盖全面（20+ 篇验证真实存在且描述准确）、差异化定位清晰、时效性好（引用至 2026 年 4 月）。这是 proposal 最突出的优点，无争议。
- **Trivial Alternative 威胁 = 实质性**（3/3 一致）：三人均独立识别出同一核心威胁——"DAG-guided negatives + 标准 BCE（无 InfoNCE）可能效果相近"，以及 PARC inference-time 零训练成本 baseline 的增量价值质疑。这是概率上限的主要压制因素。
- **核心假设（contrastive training 激活 dormant structural representations）未验证**（3/3 一致）：三人均指出从"线性探针可恢复 DAG 结构"到"contrastive training 可有效引导该结构用于 reward prediction"存在逻辑跳跃，缺乏理论或实证支撑。
- **问题重要性 = 真实**（3/3 一致）：PRM 鲁棒性和 reward hacking 是领域核心痛点，PRMBench 67.7 vs 人类 83.8 的差距表明改进空间大。

【异常维度】:
- **Significance 分歧**：R2 评"强"（认为如果假设被验证，将提供超越数学推理的原则性方法论），R1 和 R3 评"中"（认为方法仅适用数学推理、推广路径不清晰、与 inference-time 方法的叠加收益未论证）。2:1 多数为"中"，R2 为 outlier。R2 的"强"评价建立在"如果假设被验证"的条件上，这与三人共识的"核心假设未验证"相矛盾——当核心假设本身是赌注时，基于"假设成立"推导出的高 significance 应当降权。最终判定 **Significance = 中**。
- **R3 独有：catastrophic forgetting 风险**：R3 提出 PRM fine-tuning 可能已摧毁 base model 中的 DAG 结构表示（而非仅"未利用"），这使得 contrastive training 需要"重建"而非"激活"。R1 和 R2 未提及此点。这是一个有意义的风险补充，但不改变整体评级方向（加深了核心假设的不确定性）。
- **R1 独有：DAG 信息作为输入特征的 trivial alternative**（将 DAG 邻接信息作为 positional encoding 直接 feed 给 PRM）。R2 和 R3 未独立提出此特定变体，但其精神已被三人共识的 trivial alternative 覆盖。

【最终概率】: [22% - 34%] 中位 28%
【一致性】: 中（std=3.2%，处于 3-7% 区间下沿；rubric 维度在 Novelty 和 Related Work 上高度一致，但 Significance 有 1 人偏离）
【综合理由】:
三位审稿人在核心判断上高度收敛：Novelty 为"中"（natural combination）、Related Work 为"强"、trivial alternative 威胁实质存在、核心假设未验证。唯一分歧在 Significance，2:1 判定为"中"，R2 的"强"评价因其条件性（依赖未验证假设）而降权。

概率综合逻辑：
- **下界 22%**：取 R1 的下界（最严格审稿人），反映 trivial alternative 威胁充分暴露 + 核心假设 negative result 风险 + 领域拥挤度高的最坏情景。
- **上界 34%**：略低于 R2 的 38%（R2 为 outlier，按"不超过最宽松审稿人"原则取其区间内部），反映 Related Work 强 + 问题定位精准 + 实验设计周全的最好情景。
- **中位 28%**：R1（27%）和 R3（28%）高度一致，R2（33%）偏高。按"中一致偏严"原则，中位取 R1 和 R3 共识的 28% 而非三人均值 29.3%。

核心限制因素：Novelty = 中 + Significance = 中 构成的 idea 天花板约 35%，实验设计再完美也无法突破此上限。在这个天花板下，trivial alternative 未充分化解和核心假设的不确定性进一步压低实际概率至 28% 中位。

【建议】: 边缘（中位 28% 接近但未达 36% 推荐线；idea 内核真实、方向正确、执行规划扎实，但 novelty 的 surprise factor 不足是结构性瓶颈；值得进入迭代优化，重点提升 idea 层面的锐度和增量价值论证）
【实施评估】:
  - 计算资源: 1200-2500 A100-hours（取决于自动化程度）；DAG extraction 需 72B 模型（~350h），对比对生成与质量验证需 7B/32B/72B 模型（~300h），PRM 训练 + 8 组消融（~550h），RL 闭环实验 × 3 seeds（~250h），baseline 复现与评估（~250h）。预估 GPU 成本 $3,600-$7,500（按 $3/hr A100 spot）。
  - 数据需求: PRM800K + Math-Shepherd（公开可得，~300K solutions）；需自行生成 ~600K 对比对（依赖 LLM 生成 + 72B 质量验证）。PRMBench、ProcessBench、PRM-BiasBench 均为公开 benchmark。
  - 人工介入: 需分层人工审计 ~1000 对比对（跨数学子领域 × DAG 复杂度 × 难度级别），2 名标注员计算 Cohen's κ；DAG extraction 质量需按难度级别进行人工抽检。人工工作量约 2-3 人周。
  - 训练需求: 需训练 Qwen2.5-Math-7B-Instruct 基础的 PRM（dual objective：BCE + InfoNCE），加 8 组消融变体。单次训练约 50-70 A100-hours，总训练约 550h。需复现部分 baseline（APRM、CRM 等）。
  - 新 Benchmark: 不需要构建全新 benchmark，使用现有 PRMBench / ProcessBench / PRM-BiasBench。但需构建 ~600K 对比对数据集（非 benchmark，而是训练数据）。
  - 预估周期: 2-3 名研究者全职投入，13-22 周（取决于自动化程度和 GPU 可用性）。关键路径：72B DAG extraction → 对比对生成与质量验证 → PRM 训练 → RL 闭环实验。DAG extraction 质量验证是串行瓶颈。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f1ee48c-5960-4521-a746-e60c58246aa6",
  "isSidechain": false,
  "requestId": "req_011CbSpMxY4HbHFJupfQ8Wuk",
  "type": "assistant",
  "uuid": "30e1b2e5-0934-4b9c-814c-34450f93f7a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168fgJhYHndxjssA4gEa9qa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18675,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3571,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18675
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research data. Let me compile my assessm…",
  "leafUuid": "30e1b2e5-0934-4b9c-814c-34450f93f7a1",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis on premise-graph contrastive PRM proposal",
  "sessionId": "9b7f2a76-d9aa-468d-b837-dfc026066780"
}
```

---
