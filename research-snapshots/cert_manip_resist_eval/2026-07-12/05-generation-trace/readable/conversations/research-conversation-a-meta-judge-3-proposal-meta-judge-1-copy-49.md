# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/28670fdb-33a2-424c-b224-891715cdc048.jsonl`
- **Structured JSON:** [`cf96501c24b8a5b71cd0.json`](../../sessions/cf/cf96501c24b8a5b71cd0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:12:25.205Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:12:25.205Z",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命性前置问题：投稿会议严重不匹配】\n\n本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。\nCoRL 2026 Call for Papers 明确声明：\n  - \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n  - \"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 的全部内容是 LLM 数学推理训练中 PRM 利用的动力学分析，涉及 GRPO、PRM credit assignment、bifurcation theory——与机器人学无任何关联。\n按照 CoRL 2026 的明确政策，本 proposal 将被 desk reject（不送审即退稿）。\n\n→ 如果投稿目标确为 CoRL，概率估计应为 ≤2%，无需进入后续审核流程。\n→ 如果投稿目标实际是 NeurIPS 2026 / ICML 2026 / ICLR 2027 等 ML 会议，以下评估才有意义。\n\n**以下评估假设投稿目标为合适的 ML 顶会（如 NeurIPS 2026），而非 CoRL。**\n\n---\n\n【领域调研】:\n\n- [Karwowski et al., \"Goodhart's Law in Reinforcement Learning\"](https://arxiv.org/abs/2310.09144) (ICLR 2024): \n  建立了 RL 中 Goodhart 现象的几何框架，基于 occupancy polytope 边界分析，提出 optimal early stopping。本 proposal 的理论基础。确认为真实论文，描述准确。但原始框架限于 tabular MDP + 线性 reward。\n\n- [Sullivan et al., \"GRPO is Secretly a Process Reward Model\"](https://arxiv.org/abs/2509.21154) (under review ICML 2026): \n  证明 GRPO + ORM 等价于隐含 MC-PRM 的目标函数，提出 λ-GRPO。确认为真实论文。proposal 中对 dual-PRM dynamics 的描述准确。\n\n- [Wang et al., \"TRACE: Detecting Implicit Reward Hacking by Measuring Reasoning Effort\"](https://arxiv.org/abs/2510.01367) (ICLR 2026 Oral): \n  通过 CoT 截断 AUC 检测 reward hacking，F1≈0.97。确认为 ICLR 2026 Oral。这是本 proposal 最强的 trivial alternative 竞争者。\n\n- [Cheng et al., \"Stop Summation: Min-Form Credit Assignment\"](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): \n  识别 summation-form credit assignment 为 PRM hacking 的机制原因，提出 PURE (min-form)。确认为 NeurIPS 2025 Poster。proposal 的预测 P4（min-form 消除 fold）本质上是用 bifurcation 语言重述此发现。\n\n- [Hennick & Corlouer, \"From Density Matrices to Phase Transitions in Deep Learning\"](https://arxiv.org/abs/2603.29805) (arXiv 2026): \n  用 2RDM 谱分析检测训练中的 phase transitions（grokking、emergent misalignment 等）。确认存在。是概念上最近的邻居——dynamics-based 训练监控，但研究 beneficial transitions 而非 adversarial exploitation。\n\n- 未找到任何现有工作将 fold bifurcation / saddle-node dynamics 直接应用于 reward hacking/PRM exploitation。这一特定理论框架确实是新的。\n\n- 调研总结: PRM exploitation / reward hacking 是 2025-2026 极活跃的领域，已有丰富的经验性工作（检测方法、机制分析、mitigation）。理论性工作相对稀缺——Karwowski et al. 是唯一严格的形式化框架，但限于 tabular 设定。将 bifurcation theory 引入 PRM exploitation 确实是一个空白，但这个空白是否值得填补取决于理论框架能否产生超越简单 baseline 的实际价值。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在严重的 trivial alternative 威胁。**\n\n1. **TRACE (F1≈0.97)** 是最直接的威胁。TRACE 用极简的方法（CoT 截断 + AUC 计算）就能高精度检测 reward hacking。proposal 承认 TRACE 是最强 baseline，但其核心论证是\"TRACE 检测 hacking 但不预测 onset\"。然而：\n   - \"预测 onset\" 的实际价值存疑。如果 TRACE 能在 exploitation 早期就检测到（F1≈0.97），那么 onset 预测的 lead time 优势有多大？proposal 没有给出任何理论或经验证据说明 bifurcation early warning 能比 TRACE 早多少。\n   - \"bifurcation type discrimination\"（区分 fold vs. smooth crossover）是一个学术上优雅但实践价值不清的贡献——practitioner 关心的是\"什么时候该停训练\"，不是\"这是哪种 bifurcation\"。\n\n2. **简单的 proxy-true divergence 监控**：监控 PRM reward 和 ground-truth accuracy 的差值，设一个 threshold，就是最简单的检测。proposal 的 bifurcation framework 需要证明其 scaling exponent fitting 比简单 threshold 有实质优势。\n\n3. **Stop Summation / PURE 本身**：如果问题是\"summation-form 导致 exploitation\"，Stop Summation 已经给出了解决方案（换成 min-form）。bifurcation framework 的增量价值不是诊断问题，也不是解决问题，而是提供一个中间层的\"预测\"——但如果 fix 已经已知，prediction 的实际需求是什么？\n\n增量价值论证：proposal 声称的增量价值在于 (i) 更早的预警 (ii) bifurcation type discrimination (iii) mechanistic interpretability via SAE (iv) regime identification。其中 (iii) 和 (iv) 更有说服力，但 (i) 未经验证，(ii) 的实践价值不明确。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有多个未经验证的假设：\n\n1. **\"Group-relative normalization 产生的 positive feedback 能被建模为 fold bifurcation 的 normal form\"**——这是整个理论大厦的基础，但 proposal 自己承认这是 \"phenomenological model (normal form reduction)\" 而非 \"rigorous proof from GRPO's objective\"。从 positive feedback 存在到 fold bifurcation 的 normal form f(α;λ) = λ - λ_c + (α - α_c)² 之间，有一个巨大的逻辑跳跃。为什么是 fold 而不是其他 bifurcation type？proposal 没有从 GRPO 的实际梯度动力学推导出这一点，而是直接 assume 了 normal form。如果实验发现 exponent 不是 -1/2，proposal 说\"这本身也是信息\"——但这实际上意味着理论预测失败，整个 fold bifurcation framing 失效。\n\n2. **\"Exploitation fraction α(t) 是一个可以被良好定义和测量的 scalar order parameter\"**——在实际训练中，exploitation 是多维的（solution style decomposition 有多种 category），将其压缩为一个标量 α 是否合理？如果 exploitation 是通过多种不同机制同时发生的，α(t) 的动力学可能不满足任何简单的 bifurcation normal form。\n\n3. **\"PRM score gap Δs = E[s_E] - E[s_G] > 0 是常数或缓慢变化的\"**——这是推导 fold structure 的隐含假设。但在训练过程中，policy 的分布不断变化，PRM 对 exploitative vs. genuine strategies 的 score gap 也可能非平稳。如果 Δs 本身是 α 的函数（co-evolution），fold bifurcation 的简单图景就不成立。\n\n4. **\"Dense checkpoint (每 5 步) 的分辨率足以拟合 scaling exponent\"**——拟合 τ_ac ~ |λ - λ_c|^{-1/2} 需要在临界点附近有足够多的数据点。但 RL 训练中噪声很大，每次 checkpoint 的 metric 波动显著。在有限数据和高噪声下拟合 critical exponent 是出了名的困难（凝聚态物理中用 Monte Carlo 拟合 critical exponents 需要大量系统尺寸的 finite-size scaling）。proposal 没有讨论统计 power 的问题。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   将 bifurcation theory 应用于 PRM exploitation 确实是新的角度——我的调研未发现任何现有工作做过这件事。五个 testable predictions 有具体的定量形式（-1/2 exponent 等），不仅仅是定性描述。但 novelty 需要打折扣：(a) 核心机制洞察（summation-form 导致 exploitation）来自 Stop Summation (NeurIPS 2025)，positive feedback from group normalization 也是对已知现象的形式化重述；(b) \"phenomenological model\" 的理论深度有限——它不是从 GRPO 动力学严格推导的，而是先 assume bifurcation type 再检验，这更接近 curve fitting 而非理论贡献；(c) 五个 predictions 中 P3（长度依赖）和 P4（min-form 消除 exploitation）在 Stop Summation 框架下已经是可预期的，bifurcation 语言只是重新包装。真正新颖的是 P1/P2 的定量 scaling exponents 和 P5 的 dual-PRM interaction，但 P5 依赖于 Sullivan et al. 的框架且预测方向不明确（proposal 列出三种可能模式但无法 a priori 区分）。\n\n2. **Significance: 中偏弱** — \n   (a) 研究问题确实重要——PRM exploitation 是 LLM reasoning 训练的核心挑战，这一点毫无疑问。(b) 但 **核心发现如果为 positive（即确认 fold bifurcation），审稿人很可能会说 \"I would have guessed this\"**。positive feedback → tipping point 是直觉上自然的结果；将其形式化为 fold bifurcation 增加了数学精确性，但不太可能让人感到 \"surprising\"。(c) 实际影响力受限于 trivial alternative 问题：如果 TRACE (F1≈0.97) 已经解决了检测问题，Stop Summation/PURE 已经解决了 mitigation 问题，bifurcation framework 在 practitioner 层面的影响力有限。(d) 作为一项对 GRPO-specific 训练动力学的分析性研究，其 generalizability 也受限——proposal 的 Tier 3 PPO 扩展是 stretch goal，核心结论高度依赖于 GRPO 的 group-relative normalization，不易推广。(e) 唯一真正有 significance 的场景是：如果 bifurcation framework 能提供比现有方法显著更早的预警（比如在 exploitation 发生前 50+ 步），这将有实际价值——但这是一个未验证的 empirical claim。\n\n3. **Related Work: 强** — \n   这是 proposal 最突出的优势。对 6 个领域类别的覆盖非常全面（Goodhart formalization、GRPO analysis、PRM analysis、detection methods、representation monitoring、statistical diagnostics）。对每篇关键论文的定位都清晰准确——Karwowski et al. 的局限性（tabular MDP, linear reward）、TRACE 的优劣（高精度但不预测 onset）、Stop Summation 的关系（WHY vs. WHEN/HOW）、Sullivan et al. 的 dual-PRM 洞察。我验证了主要引用均真实存在且描述正确。差异化定位清晰。唯一的小问题是某些引用数量过多（30+ 篇），可能导致真正的定位信息被稀释。\n\n---\n\n【概率估计】: \n\n**如果投 CoRL 2026：0-2%（desk reject，不送审即退稿）**\n\n**如果投合适的 ML 顶会（NeurIPS 2026 等）：18% - 30%，中位 23%**\n\n【估计理由】: \n\nCoRL 概率的理由极为直接：proposal 没有任何机器人学内容，CoRL 明确声明\"无机器人学焦点的投稿将不经审稿退回\"。\n\nML 顶会概率的推理：Novelty 为中——有真实的新角度但理论深度有限（phenomenological model），且核心洞察建立在已有工作之上。Significance 为中偏弱——核心发现如果 positive 不太可能让审稿人感到 surprising，实际价值受 TRACE/PURE 等 trivial alternative 的严重挤压。Related Work 强，但这是形式完善度而非 idea 内核。综合来看处于 \"方向正确、有真实 novelty delta，但核心发现审稿人可能说 'I would have guessed this'\" 的 25-35% 区间的下半段，因为 trivial alternative 威胁（TRACE, PURE）将上界压低。\n\n限制上界的维度是 **Significance**：即使所有实验都 work out，核心贡献（用 bifurcation 语言形式化了一个已知的 positive feedback 现象）的 impact ceiling 不高。限制下界的是 **Novelty** 中的真实新颖成分（定量 scaling predictions、dual-PRM interaction）和极为全面的 related work coverage。\n\n【主要风险】: \n\n1. **Trivial Alternative 致命挑战**：审稿人最可能的攻击是 \"TRACE already achieves F1≈0.97 for detection, PURE already solves the mechanism — what is the practical value of knowing this is a fold bifurcation rather than just a tipping point?\"。如果 bifurcation framework 在 lead time 上无法显著超越 TRACE，整个 contribution 退化为 \"interesting but incremental theoretical observation\"。\n\n2. **Phenomenological theory 的可证伪性风险**：如果实验中 scaling exponents 偏离 -1/2（这在有限数据 + 高噪声的 RL 训练中非常可能），proposal 的 fallback 是 \"报告实际 bifurcation type 作为核心结果\"。但这意味着最核心的理论预测失败了——审稿人会质疑：如果不是 fold bifurcation，那整个 framework 的价值是什么？proposal 在理论 claim 的强度和 hedging 之间走钢丝。\n```\n\n---\n\n**⚠️ 再次强调关键问题：** 此 proposal 投 CoRL 2026 几乎必然被 desk reject。CoRL 要求 \"core robotics problem\"，本 proposal 是纯粹的 LLM 训练动力学分析，与机器人学无关。建议重新选择投稿会议（NeurIPS 2026、ICML 2026、ICLR 2027 等），否则一切后续审核优化都没有意义。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Karwowski et al., Goodhart's Law in RL (ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [Sullivan et al., GRPO is Secretly a PRM](https://arxiv.org/abs/2509.21154)\n- [Wang et al., TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Cheng et al., Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Hennick & Corlouer, Density Matrices to Phase Transitions](https://arxiv.org/abs/2603.29805)\n- [Reward Hacking in the Era of Large Models (Survey)](https://arxiv.org/abs/2604.13602)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\n调研完成。现在我掌握了关键信息，尤其是一个**致命的venue mismatch问题**。让我完成评估。\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：投稿目标与proposal完全不匹配】\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance \nof proposed models, algorithms, datasets, and benchmarks to robotics. Authors are \nencouraged to report real-robot experiments or provide convincing evidence that \nsimulation experiments are transferable to real robots. Submissions without a robotics \nfocus will be returned without review.\"\n\n本 proposal 的全部内容是：PRM exploitation 在 GRPO 训练中的 bifurcation \ndynamics，针对 LLM 数学推理任务（MATH/AMC/AIME），使用 Qwen3-4B/14B。\n没有任何机器人相关内容——没有 robot learning、没有 manipulation、没有 \nlocomotion、没有 sim-to-real、没有 embodied AI。\n\n结论：该 proposal 投稿 CoRL 2026 将被 desk-reject，不进入评审流程。\n概率为 0%。\n\n本 proposal 适合的投稿目标：NeurIPS 2026 / ICML 2026 / ICLR 2027 / \nAAAI 2027 主会（RL theory / LLM alignment track）。\n\n以下对 idea 质量的评估假设投稿目标更正为合适的 ML 会议（如 NeurIPS/ICML/ICLR），\n供后续流程参考。\n\n---\n\n【领域调研】:\n\n1. Karwowski et al. \"Goodhart's Law in Reinforcement Learning\" (ICLR 2024, \n   arXiv:2310.09144): \n   在 tabular MDP 中形式化 Goodhart's law，用 occupancy polytope 几何解释\n   proxy-true reward 偏离，推导最优 early stopping + regret bound。\n   局限：线性 reward、无 neural PRM、无 step-level credit、无 group normalization。\n   → 本 proposal 声称的\"基础框架\"确实存在且描述准确。\n\n2. Sullivan et al. \"GRPO is Secretly a Process Reward Model\" (arXiv:2509.21154, \n   under review ICML 2026): \n   证明 GRPO + ORM 等价于一个带隐式 Monte-Carlo PRM 的目标。提出 λ-GRPO \n   修正 process set imbalance。\n   → 本 proposal 的 dual-PRM 分析依赖此结论，引用准确。\n\n3. Cheng et al. \"Stop Summation / PURE\" (NeurIPS 2025, arXiv:2504.15275): \n   识别 summation-form credit assignment 是 PRM hacking 的机制原因，\n   提出 min-form (PURE) 替代。\n   → 这是本 proposal 核心理论基础之一。本 proposal 的增量是：在已知 WHY \n   (Stop Summation) 的基础上回答 WHEN/HOW（bifurcation dynamics）。\n\n4. Wang et al. \"TRACE\" (ICLR 2026 Oral, arXiv:2510.01367): \n   通过 progressive CoT truncation 测量 reasoning effort 检测 reward hacking，\n   F1≈0.97（数学任务）。\n   → 这是本 proposal 自认的\"strongest baseline\"。TRACE 的极高检测性能是本\n   proposal 面临的最大 trivial alternative 威胁。\n\n5. Beigi et al. \"IR³\" (arXiv:2602.19416): \n   contrastive IRL + SAE 做 post-hoc interpretable reward hacking detection，\n   0.89 correlation with ground-truth rewards。\n   → post-hoc 方法，与本 proposal 的 training-time 定位有区分。\n\n6. Hennick & Corlouer \"From Density Matrices to Phase Transitions in Deep Learning\" \n   (arXiv:2603.29805): \n   2RDM spectral analysis 检测 training phase transitions（能力涌现、grokking）。\n   → 最近的概念邻居，但研究的是 beneficial transitions 而非 adversarial exploitation。\n\n7. Miao et al. \"Energy Loss\" (ICML 2025, arXiv:2501.19358): \n   发现 energy loss 单调递增可作为 PPO-RLHF reward hacking 早期预警。\n   → 更简单的标量 signal，不区分 regime。\n\n8. Helff et al. (ICLR 2026 Workshop, arXiv:2604.15149), \n   Mahmoud et al. (arXiv:2605.12474), \n   rebound paper (arXiv:2604.01476), \n   Nimmaturi et al. (arXiv:2507.18014): \n   大量并行工作从不同角度刻画 reward hacking dynamics。\n   → 这个领域在 2025-2026 年非常拥挤。\n\n- 调研总结: Reward hacking / Goodhart's law in RL 是 2025-2026 年的热门方向，\n  多条并行工作线正在快速推进（检测、机制分析、缓解策略）。本 proposal \n  试图占据一个特定 niche——bifurcation-theoretic prediction of PRM exploitation \n  onset in GRPO——这个精确交叉点目前确实没有直接竞争者，但周围的工作非常密集，\n  留给额外 insight 的空间有限。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在严重的 trivial alternative 威胁：\n\n1. **TRACE (F1≈0.97)**：proposal 自己承认这是最强 baseline。如果实际目标是\n   \"检测 reward hacking\"，TRACE 已经在数学任务上达到极高性能。本 proposal 需要\n   证明 bifurcation framework 在某个维度（lead time、false positive rate、\n   mechanistic insight）上 strictly dominate TRACE，这并不容易。\n\n2. **简单 divergence monitoring**：监控 proxy reward vs. ground-truth accuracy \n   的 gap，加上 changepoint detection (PELT/BOCPD)，是一个成本极低的 baseline。\n   本 proposal 的大量理论推导最终可能只比\"看 reward-accuracy gap 何时开始发散\"\n   早几个 checkpoint 发出预警——增量价值是否值得整个 bifurcation framework \n   的复杂度？\n\n3. **PURE 直接解决问题**：如果 summation-form credit assignment 是 root cause\n   （Stop Summation 已证明），直接换成 min-form (PURE) 就消除了 exploitation。\n   那么\"预测 exploitation onset\"的实际应用场景到底是什么？谁会在明知 PURE \n   能消除问题的情况下，选择继续用 summation-form 然后依赖 bifurcation \n   early warning？\n\n增量价值论证：proposal 试图定位为\"理论理解 + 机制分析\"而非纯实用工具，\n但 bifurcation theory 的增量理解相对于 Stop Summation 已经给出的机制解释\n（summation-form creates positive feedback）是否足够大？从 \"positive feedback \n→ exploitation\" 到 \"positive feedback → fold bifurcation with -1/2 exponent\" \n的增量，审稿人可能认为是 formalism for its own sake。\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中有多个未验证的关键假设：\n\n1. **Normal form reduction 的合理性**（最关键）：proposal 承认 bifurcation \n   derivation 是 \"phenomenological model (normal form reduction)\"，不是从 GRPO \n   objective 严格推导的。从 \"group-relative normalization creates positive \n   feedback\" 到 \"the dynamics can be reduced to dα/dt = λ - λ_c + (α - α_c)²\" \n   的跳跃需要多个隐含假设：exploitation fraction α 是一个 well-defined \n   slow variable、高阶项可忽略、noise structure 不改变 bifurcation type 等。\n   在有随机梯度、finite batch size、非线性 neural PRM 的实际训练中，这些假设\n   很可能不成立。\n\n2. **Scaling exponent 的可检测性**：fold bifurcation 预测 autocorrelation \n   diverges as |λ-λ_c|^{-1/2}。在实际训练中，(a) λ(t) 不是已知量，需要反推；\n   (b) 数据点（checkpoints）有限（~100 per run）；(c) noise 可能掩盖 scaling \n   behavior。能否在 4-8 个 training run 中可靠地拟合 scaling exponent 并区分\n   -1/2（fold）vs. -1（transcritical）是一个严肃的统计学问题。\n\n3. **α(t) 的可操作性定义**：\"exploitation fraction\" 在理论中是一个干净的量，\n   但在实际 LLM 生成的数学解题中，如何 operationalize \"什么是 exploitative \n   strategy\" 本身就是一个 non-trivial 问题（Tiwari et al. 的 taxonomy 提供\n   了部分方案，但远非完美分类器）。\n\n4. **Dual-PRM interaction 的可测性**：P5 预测 λ-GRPO 应该通过减弱 implicit \n   PRM 的贡献来 raise λ_c。但区分 \"λ_c shifted\" vs. \"training dynamics \n   simply changed due to loss function modification\" 需要极精细的实验设计，\n   而 proposal 只有 1 个 λ-GRPO run。\n\n---\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   理由：精确交叉点（bifurcation theory + GRPO credit assignment + PRM exploitation）\n   确实没有直接先驱。但 novelty 的实质深度有限：\n   - Stop Summation (NeurIPS 2025) 已经识别 summation-form 的 positive feedback \n     是 root cause\n   - Karwowski et al. (ICLR 2024) 已经形式化 Goodhart's law in RL\n   - 本 proposal 的增量是将已知的 positive feedback mechanism 用 bifurcation \n     normal form 语言重新表达，并推导 scaling exponent predictions\n   - 这更接近\"用新的数学语言重新描述已知现象 + 推导 quantitative predictions\"\n     而非\"发现新现象或新机制\"\n   - Hennick & Corlouer (arXiv:2603.29805) 已经将 phase transition / critical \n     transitions 工具引入 training dynamics 分析\n   - 审稿人可能认为 fold bifurcation 框架是 \"formalism premium\" 大于 \n     \"insight premium\"\n\n2. Significance: 【中】\n   理由：\n   - 研究问题本身（理解和预测 reward hacking dynamics）确实重要，尤其在 \n     LLM alignment context 下\n   - 但实际影响力受限于：(a) PURE 已经提供了 root cause fix，减少了 prediction \n     的应用价值；(b) TRACE 已经提供了极高性能的检测，减少了 monitoring 的应用\n     价值；(c) 理论贡献是 phenomenological 而非 rigorous，限制了理论影响力\n   - 如果核心发现是 positive（scaling exponent 确实是 -1/2），审稿人更可能说 \n     \"interesting confirmation of what we'd expect from the positive feedback \n     structure\" 而非 \"surprising\"\n   - 如果核心发现是 negative（exponent 不是 -1/2），这确实 informative，但\n     paper 的 framing 会变得尴尬\n   - 整体定位是\"对已知现象的更精确定量刻画\"，这是有价值的但不是高影响力的\n\n3. Related Work: 【强】\n   理由：\n   - 这是 proposal 最突出的优点。覆盖了 6 个 category、30+ 篇参考文献，\n     包括所有关键的并行工作\n   - 对每篇工作的定位清晰，差异化论述具体（dynamics-based vs. effort-based \n     vs. representation-based vs. gradient-based）\n   - 对 Karwowski et al.、Sullivan et al.、Stop Summation、TRACE 等核心\n     参考的引用和描述经验证均准确\n   - 但极其详尽的 related work 也反映出这个空间已经非常拥挤\n\n---\n\n【概率估计】: \n\n对 CoRL 2026: 0% — 会被 desk-reject，不进入评审\n（CoRL 明确要求 robotics focus，本 proposal 无任何 robotics 内容）\n\n对合适的 ML 顶会 (NeurIPS/ICML/ICLR): [20% - 30%] 中位 25%\n\n【估计理由】: \nNovelty 和 Significance 均为\"中\"，限制了上界。核心问题是：\n\n(1) Novelty 的 incremental nature——从 \"Stop Summation 已知 positive feedback \n是 root cause\" 到 \"用 fold bifurcation normal form 重新描述并推导 scaling \nexponent\"，增量实质偏窄。审稿人会问 \"beyond formalism, what new insight does \nthe bifurcation framework give us that we didn't already know from Stop Summation?\"\n\n(2) Trivial alternative 威胁严重——TRACE (F1≈0.97) 和 PURE (消除 root cause) \n的存在削弱了 practical motivation；简单 divergence monitoring + changepoint \ndetection 可能在 lead time 上与 bifurcation framework 差别不大。\n\n(3) 前提假设风险——phenomenological model 的 scaling predictions 在实际训练中\n可能不可靠地检测到，导致核心实验 claim 无法 convincingly validate。\n\nRelated Work 的强项提供了 solid 的 positioning 但不能弥补 idea 内核的局限。\n上界被 Novelty 限制（不是 \"surprising\" 级别的发现），下界由 Related Work \n的质量和研究问题的时效性托住。\n\n【主要风险】: \n1. **Venue mismatch（对 CoRL 致命）**：proposal 无任何 robotics 内容，CoRL \n   明确声明 \"submissions without a robotics focus will be returned without \n   review\"。若不更换投稿目标，概率为 0%。\n\n2. **Formalism-over-insight 质疑（对任何 venue）**：审稿人最可能的攻击角度是\n   \"the bifurcation framework re-describes the already-known positive feedback \n   mechanism (Stop Summation) in dynamical systems language without yielding \n   actionable new insights, especially given that PURE already eliminates the \n   root cause and TRACE already detects it with F1≈0.97.\"\n```\n\n---\n\n**总结**：这个 proposal 的 **idea 质量在中等水平**（novelty 和 significance 均为中），有一个非常扎实的 related work coverage，但核心增量（bifurcation formalism on top of already-known mechanisms）偏窄，且面临 TRACE/PURE 两个方向的 trivial alternative 夹击。\n\n然而，**最致命的问题是投稿目标选择**：CoRL 是 Conference on Robot Learning，明确要求论文聚焦机器人问题，无机器人内容的投稿将被退回不审。本 proposal 应改投 NeurIPS / ICML / ICLR 等 ML 顶会。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [Wang et al. - TRACE: Detecting Implicit Reward Hacking (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Cheng et al. - Stop Summation / PURE (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Beigi et al. - IR³ (arXiv:2602.19416)](https://arxiv.org/abs/2602.19416)\n- [Hennick & Corlouer - Phase Transitions in Deep Learning](https://arxiv.org/abs/2603.29805)\n- [Miao et al. - Energy Loss (ICML 2025)](https://arxiv.org/abs/2501.19358)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information from the field research. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命问题：venue mismatch】\n本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。但 proposal 内容为 LLM 数学推理训练中的 PRM exploitation/reward hacking 检测——与机器人学习零相关。CoRL 明确要求论文 \"focus on a core robotics problem\" 并 \"demonstrate the relevance to robotics, with real-robot experiments or convincing simulation evidence.\" 本文无任何 robotics 内容，会被 desk reject。\n如果投稿目标实为 NeurIPS/ICML/ICLR 等 ML 主会，以下评估按 ML 主会标准给出；如确实投 CoRL，中稿概率为 ~0%。\n\n【领域调研】:\n- Karwowski et al. \"Goodhart's Law in Reinforcement Learning\" (ICLR 2024): 提出 occupancy polytope 上的 Goodhart 几何形式化，推导最优 early stopping 及 regret bound。局限于 tabular MDP + 线性 reward，未涉及 neural PRM 或 GRPO。Proposal 声称对该工作的扩展基本准确。\n- Sullivan et al. \"GRPO is Secretly a Process Reward Model\" (arXiv:2509.21154, under review ICML 2026): 证明 GRPO + ORM 等价于隐式 Monte-Carlo PRM 目标，提出 λ-GRPO。Proposal 对其引用和描述准确。\n- Cheng et al. \"Stop Summation: Min-Form Credit Assignment Is All PRM Needs\" (NeurIPS 2025): 定位 summation-form credit assignment 为 PRM hacking 根因，提出 PURE (min-form)。Proposal 引用准确，且确实是本文理论的关键前提。\n- Wang et al. \"TRACE\" (ICLR 2026 Oral): 通过渐进式 CoT 截断测量 reasoning effort，F1≈0.97 检测 implicit reward hacking。Proposal 将其作为最强 baseline，描述准确。\n- Miao et al. \"Energy Loss Phenomenon in RLHF\" (ICML 2025): 发现 RLHF 中 energy loss 单调递增与 reward hacking 相关，提出 EPPO。Proposal 引用准确。\n- Beigi et al. \"IR³\" (arXiv:2602.19416): contrastive IRL + SAE 的 post-hoc reward hacking 检测，0.89 correlation with ground-truth。Proposal 引用准确。\n- Hennick & Corlouer \"From Density Matrices to Phase Transitions\" (arXiv:2603.29805): 2RDM spectral analysis 检测训练 phase transitions。目前唯一将 critical transition 理论应用到 DL 训练动力学的工作，但研究的是 capability emergence/grokking，非 adversarial exploitation。\n- Mahmoud et al. \"Reward Hacking in Rubric-Based RL\" (arXiv:2605.12474): rubric verifier 下的单调 exploitation 增长。\n- Helff et al. (ICLR 2026 Workshop): progressive shortcut growth with task complexity。\n- 未找到任何直接将 bifurcation theory 应用于 reward hacking 预测的先前工作。\n\n- 调研总结: Reward hacking 检测/缓解是 2025-2026 的热门方向，已有多条 orthogonal 路线（effort-based/TRACE, representation-based/energy loss/SAE, scaling law, gradient fingerprint）。Bifurcation-theoretic framing 尚无人做，但 Stop Summation 已定位了 mechanism，TRACE 已达 F1≈0.97 的检测性能。Proposal 的位置是在已知 mechanism 上叠加动力学系统理论框架。\n\n【Trivial Alternative 检验】:\n存在严重的 trivial alternative 威胁：\n1. **TRACE (F1≈0.97)** 已经是极强的 hacking detector，proposal 自己承认这是最强 baseline。即使 bifurcation framework 能提供\"更早\"的 warning，其增量价值取决于 lead time 差异——这是一个 empirical question，且 lead time 优势可能很小。\n2. **简单 proxy-true divergence monitoring**：监控 PRM score 与 ground-truth accuracy 的 divergence rate 是最朴素的方法。Proposal 需要证明 fold-specific scaling exponent 比 naive divergence threshold 有显著优势。\n3. **Stop Summation 已给出 mechanism + fix (PURE)**：如果已经知道 summation-form 是 root cause，直接使用 min-form 就能消除 hacking。Bifurcation framework 的\"预测何时发生\"在\"已知如何避免\"的前提下，实用价值被削弱。\n增量价值声称：(a) 比 simpler methods 更早检测, (b) 区分 bifurcation type 减少 false positive, (c) SAE 提供 mechanistic interpretability, (d) regime identification 指导 intervention selection, (e) 定量预测 onset timing via λ_c 估计。但 (a)(b)(e) 都是 empirical claims，非 idea-level guarantees；(c) 是 engineering contribution；(d) 有一定理论价值但取决于 framework 是否 predictive。\n\n【前提假设检验】:\n核心逻辑链有 3 个关键假设经不起严格推敲：\n1. **Fold bifurcation 是 phenomenological fitting，非 rigorous derivation**：Proposal 自己承认这是 \"phenomenological model (normal form reduction)\" 而非从 GRPO objective 严格推导。将观察到的 \"tipping point\" 行为套入 fold normal form f(α;λ) = λ - λ_c + (α - α_c)² 是 curve fitting，不是 theory。关键问题：任何具有 positive feedback 的 transition 都可以被 phenomenologically 描述为 fold bifurcation——这不是 PRM-specific insight，而是 bifurcation theory 的 generic property。\n2. **Scaling exponent 可测性假设**：P1/P2 要求测量 τ_ac ~ |λ(t) - λ_c|^{-1/2} 的 scaling exponent。在 noisy、finite-sample 的 RL training 中，精确区分 exponent 1/2（fold）和 exponent 1（transcritical）极其困难。如果 noise 太大无法区分，核心 theoretical prediction 就不可测。\n3. **Positive feedback 唯一来源假设**：Framework 假设 group-relative normalization 是 positive feedback 的核心来源。但 RL training 中有多种其他 positive feedback（policy collapse, mode collapse, temperature dynamics），将 fold 归因于单一机制是 oversimplification。\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 — \n   理由：(a) 将 bifurcation theory 应用到 reward hacking 预测确实无人做过（调研中未找到直接先例），这是形式上的 novelty。(b) 但核心 insight——\"summation-form GRPO 中 exploitation 存在正反馈导致的 tipping point\"——本质上已被 Stop Summation (NeurIPS 2025) 和 Helff et al. (ICLR 2026 Workshop) 从 empirical 角度描述。Proposal 的贡献是用 bifurcation 语言重新表述已知现象。(c) Fold bifurcation derivation 是 phenomenological fitting，任何正反馈系统都能这样 fit——这不是 PRM-specific 或 GRPO-specific theory。(d) Dual-PRM interaction (P5) 是最有原创性的部分，但也最 speculative。(e) 与 Hennick & Corlouer 将 critical transition theory 应用到 training dynamics 的工作有 conceptual overlap，虽然 domain 不同。综合来看，novelty 在\"新 framing applied to known problem\"水平，而非\"new insight\"水平。\n\n2. Significance: 中 — \n   理由：(a) 预测 reward hacking onset 是 genuinely important 的问题，在 LLM alignment 和 safety 社区有高关注度。(b) 但 practical significance 被 TRACE (F1≈0.97) 和 PURE (直接消除 hacking) 的存在削弱——如果已有 excellent detector 和 known fix，\"另一种 detection framework\"的边际价值下降。(c) 若 bifurcation framework 确实能 predict（而非 detect）onset，且 prediction 足够 early 以 enable preemptive intervention，这有独立价值——但这是 empirical promise，非 guaranteed。(d) 对领域的 conceptual contribution 是将 dynamical systems 工具引入 reward hacking 分析，有一定范式创新意义，但实际 usefulness 取决于 empirical validation。(e) 研究问题的定位是\"when and how\"而非\"why\"（Stop Summation 已回答 why）或\"how to fix\"（PURE 已回答），这个定位有价值但不是最高优先级。\n\n3. Related Work: 强 — \n   理由：Proposal 对已有工作的覆盖异常全面。6 类文献梳理（Goodhart formalization, GRPO-specific, PRM-specific, detection methods, representation monitoring, statistical diagnostics）完整且准确。关键论文的引用和描述经调研验证准确（Karwowski ICLR'24, Sullivan arXiv:2509.21154, Stop Summation NeurIPS'25, TRACE ICLR'26 Oral, IR³, Energy Loss ICML'25）。差异化定位清晰——proposal 明确标注了与每个 prior work 的区别（e.g., Karwowski: linear reward → neural PRM; TRACE: sample-level → population-level temporal dynamics; IR³: post-hoc → training-time）。唯一的轻微不足：未覆盖 Scheffer et al. (Nature 2009) 之后 ecology/climate 领域 early warning signals 的 false positive 问题文献（该领域已有大量关于 EWS 可靠性的批判性工作）。\n\n【概率估计】: [18% - 30%] 中位 23%\n（注：此概率基于投稿 NeurIPS/ICML/ICLR 等 ML 主会。若确投 CoRL，概率 ≈ 0%，因 scope 完全不匹配。）\n\n【估计理由】: \n- Related Work 维度强，说明作者对领域把握扎实，这提供了下限保障（不会因为 miss related work 被拒）。\n- Novelty 维度是主要瓶颈：核心贡献是将已知现象（summation-form → exploitation tipping point）用 bifurcation 语言重新表述，且 derivation 是 phenomenological fitting 而非 rigorous theory。审稿人可能评价为 \"reformulation, not new insight\"。\n- Significance 被 TRACE 和 PURE 的存在压缩：如果已有 F1≈0.97 的 detector 和已知 fix，新 framework 的 marginal value 需要靠 empirical lead time advantage 来支撑——这是 empirical gamble。\n- Proposal 形式极其完善（3-tier experiment design, 6 baselines, dual-outcome, explicit limitations），这保证了执行质量下限，但不改变 idea 内核的评估。\n- 上界受限于 Novelty（\"弱-中\"）和 trivial alternative 威胁。审稿人看到 TRACE F1≈0.97 会问：\"为什么我需要一个复杂的 bifurcation framework？\"如果 empirical results 不能给出 convincing 回答，概率落入下界附近。\n- 若 empirical results 确实展示出 (a) fold-specific scaling exponent 可测且 (b) 比 TRACE 有显著 lead time 优势，概率可推至上界附近。\n\n【主要风险】:\n1. **\"Reformulation, not new insight\" 拒稿理由**：审稿人可能认为将 Stop Summation 已定位的 mechanism 套入 fold bifurcation normal form 是 mathematical dressing，而非 genuine theoretical contribution。Phenomenological fitting 的 unfalsifiability（如果不是 fold 就换另一种 bifurcation type）进一步削弱理论 claim 的 sharpness。\n2. **Trivial alternative 压制**：TRACE (F1≈0.97) + PURE (eliminate hacking) 的组合使得\"另一种 detection framework\"的 practical motivation 被严重削弱。审稿人会问 \"given TRACE and PURE exist, who is the user of this framework, and what decision would they make differently?\"\n```\n\n**补充说明（venue 问题）**：\n\n这是我在评估中发现的**最严重问题**。CoRL 2026 的 Call for Papers 明确要求论文围绕\"core robotics problem\"展开，鼓励\"real-robot experiments or convincing simulation evidence\"。本 proposal 的全部内容——PRM exploitation、GRPO 训练动力学、数学推理 benchmark——与机器人学习**毫无交集**。即使 idea 本身有价值，投 CoRL 会被直接 desk reject。\n\n如果作者实际想投的是 NeurIPS 2026 / ICML 2026 / ICLR 2027 等 ML 主会，上述概率估计（18%-30%，中位 23%）适用。**请确认投稿目标是否正确。**\n\nSources:\n- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [Cheng et al. - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Wang et al. - TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Miao et al. - Energy Loss Phenomenon (ICML 2025)](https://arxiv.org/abs/2501.19358)\n- [Beigi et al. - IR³](https://arxiv.org/abs/2602.19416)\n- [Hennick & Corlouer - Density Matrices to Phase Transitions](https://arxiv.org/abs/2603.29805)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Goodhart's Tipping Point: Fold Bifurcations and Early Warning Signals in PRM Exploitation During GRPO Training\n\n## Description\nWe develop the first bifurcation-theoretic framework for predicting PRM exploitation onset during GRPO training, deriving that summation-form credit assignment creates a fold (saddle-node) bifurcation in the exploitation fraction through a positive feedback loop unique to group-relative advantage normalization. Building on Karwowski et al.'s (ICLR 2024) geometric Goodhart framework and extending it to neural PRMs with step-level credit assignment, we derive five PRM-specific testable predictions: fold-specific autocorrelation scaling (exponent -1/2), variance amplification with fold exponent, solution-length-dependent onset timing, elimination of the fold under min-form credit (PURE), and dual-PRM interaction signatures where GRPO's implicit Monte-Carlo PRM (Sullivan et al., arXiv:2509.21154) modulates exploitation onset timing. Experiments span three priority tiers: Tier 1 trains Qwen3-4B via GRPO with three PRMs (discriminative and generative) plus Qwen3-14B, with a multi-signal diagnostic panel at dense checkpoints; Tier 2 adds λ-GRPO and PURE ablations to test bifurcation modulation predictions, completes 14B cross-PRM comparison, and adds GRIFT baseline; Tier 3 extends to PPO and spectral analysis. We rigorously ablate against six baselines spanning four detection paradigms: dynamics-based (self-internalization gap, divergence rate, scaling law deviation), effort-based (TRACE, adapted from Wang et al.'s ICLR 2026 Oral with F1≈0.97), representation-based (energy loss), and gradient-based (GRIFT). The framework explicitly addresses the dual-PRM dynamic in GRPO + explicit PRM, where the explicit PRM determines trajectory-level advantage while the implicit MC-PRM distributes learning across tokens. We compare exploitation bifurcation characteristics across discriminative vs. generative PRMs and position against complementary approaches: IR³'s post-hoc SAE-based detection, CRA's PRM deconfounding, and InfoRM's IB-based monitoring.\n\n## Core Problem\nPRM exploitation during RL training can silently render training counterproductive (>0.9 reward, <4% accuracy), but we lack both a domain-specific theoretical framework predicting exploitation onset and practical early-detection tools that outperform simpler baselines. Karwowski et al. (ICLR 2024) formalize Goodhart's law geometrically in MDPs via occupancy polytope boundary transitions, deriving optimal early stopping with regret bounds — but their framework assumes linear rewards on occupancy measures and does not address neural process reward models, step-level credit assignment, or the dual-PRM dynamics inherent to GRPO. Sullivan et al. (arXiv:2509.21154) prove that GRPO with an ORM is equivalent to a PRM-aware objective with an implicit Monte-Carlo PRM, meaning GRPO + explicit PRM creates a dual-PRM optimization dynamic not previously analyzed for exploitation. Stop Summation identifies summation-form credit assignment as the mechanistic driver of PRM hacking. Current work characterizes the end state (Tiwari et al., 43% shortcuts), the mechanism (Stop Summation), temporal dynamics under rubric verifiers (Mahmoud et al.), structural phase transitions in capability emergence (Hennick & Corlouer), static PRM deconfounding (CRA), scalar early warning in preference-RLHF (Energy Loss), effort-based hacking detection (TRACE, F1≈0.97), and post-hoc interpretable detection (IR³, SAE-based) — but no work unifies bifurcation-theoretic prediction with mechanistic monitoring for PRM exploitation in GRPO, where the interaction between implicit and explicit process reward structures introduces qualitatively distinct exploitation dynamics.\n\n## Opportunity\nFive converging threads create a unique opportunity. First, Sullivan et al. (arXiv:2509.21154) prove GRPO implicitly implements a Monte-Carlo PRM through trajectory prefix sharing, and propose λ-GRPO to fix step-level imbalance — this reveals that GRPO + explicit PRM creates a dual-PRM optimization dynamic where the explicit PRM determines which trajectories are favored while the implicit PRM distributes advantage across tokens, an interaction whose exploitation characteristics are completely uncharted. Second, concurrent empirical work maps complementary facets of reward hacking — Mahmoud et al. (arXiv:2605.12474) show monotonic exploitation growth under weak rubric verifiers, the rebound paper (arXiv:2604.01476) finds three-phase dynamics in code evaluation, Nimmaturi et al. (arXiv:2507.18014) identify exponential saturation in GRPO, and Helff et al. (arXiv:2604.15149) show progressive shortcut growth with task complexity — but none study PRM-guided math reasoning where Stop Summation has identified summation-form credit assignment as the mechanism. Third, Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational Goodhart formalization in RL — geometric explanations via occupancy polytope boundaries and optimal early stopping with regret bounds — but their linear-reward framework does not extend to neural process rewards, step-level credit assignment, or the group-relative normalization in GRPO that creates positive feedback loops driving exploitation. Critical transitions theory (Scheffer et al., Nature 2009) and its recent application to training phase transitions (Hennick & Corlouer, arXiv:2603.29805) provide the dynamical systems tools, but the theoretical gap is precisely connecting GRPO's credit assignment mechanisms to specific bifurcation types with quantitative scaling predictions — not merely applying generic early warning signals to a new domain. Fourth, detection methods are maturing along multiple orthogonal axes — TRACE (arXiv:2510.01367, ICLR 2026 Oral) detects hacking via reasoning effort measurement (CoT truncation AUC) with F1≈0.97, GRIFT uses gradient fingerprints, IR³ (arXiv:2602.19416) combines contrastive IRL with SAEs for 0.89 correlation with ground-truth rewards, energy loss provides a scalar signal, and SAEs detect RL pathologies — but none predict exploitation onset from training dynamics as a bifurcation phenomenon, and no work systematically compares these orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based) against each other. Fifth, GenPRM and TP-GRPO reveal distinct exploitation profiles for generative PRMs, creating an unexplored axis for comparing bifurcation characteristics across PRM paradigms. Bridging Karwowski's geometric Goodhart framework with bifurcation theory specific to GRPO's credit assignment mechanisms offers a formal model generating quantitative predictions — but the bar is high: we must show the framework adds value beyond simpler baselines including TRACE, self-internalization gap, energy loss, scaling law fitting, and gradient fingerprints.\n\n## Related Work / Landscape\nThe landscape spans six categories requiring explicit positioning: (A) Goodhart formalization and training dynamics, (B) GRPO-specific analysis, (C) PRM-specific analysis, (D) detection methods, (E) representation-level monitoring, and (F) statistical/information-theoretic diagnostics.\n\n**A. Goodhart Formalization and Training Dynamics.** Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational formalization of Goodhart's law in RL: they model policy optimization as steepest ascent on the occupancy measure polytope Ω, show that the projected angle between proxy and true rewards determines Goodharting likelihood (Proposition 3: directional alignment is monotonically decreasing), derive an optimal early stopping criterion with regret bound proportional to diameter(Ω)·(1-cos(θ)), and demonstrate Goodharting in 19.3% of 30,400 configurations. Their framework is foundational to our work but operates in the tabular MDP setting with linear reward functions on occupancy measures — it does not address (a) neural process reward models where the proxy is a learned nonlinear function, (b) step-level credit assignment where summation vs. min forms create qualitatively different optimization landscapes, (c) group-relative normalization in GRPO that introduces positive feedback absent from steepest ascent, or (d) the dual-PRM dynamics of GRPO + explicit PRM. Our theoretical contribution extends their geometric insight to the PRM-guided GRPO setting by deriving the specific bifurcation structure (fold bifurcation) that arises from the positive feedback between group-relative normalization and exploitation discovery, yielding quantitative scaling predictions absent from their framework. Hennick & Corlouer (arXiv:2603.29805) apply 2RDM spectral analysis to detect training phase transitions (capability emergence, grokking) — the closest conceptual neighbor for dynamics-based training monitoring, but they study beneficial reorganization rather than adversarial exploitation. Miao et al. (arXiv:2501.19358, ICML 2025) identify energy loss (ΔE_l = ||h^in_l||_1 − ||h^out_l||_1) as a monotonically increasing early warning for reward hacking in PPO-based RLHF — a single scalar signal without regime discrimination or mechanistic interpretability, operating in the preference RLHF setting rather than PRM-guided GRPO. Helff et al. (arXiv:2604.15149, ICLR 2026 Workshop) show progressive shortcut growth with task complexity, reinforcing the importance of characterizing transition type (sharp vs. gradual).\n\n**B. GRPO-Specific Analysis.** Sullivan et al. (arXiv:2509.21154, under review ICML 2026) prove that GRPO with an ORM is equivalent to a PRM-aware RL objective with an implicit Monte-Carlo PRM — for each token, the implicit step-level reward equals the mean outcome reward of trajectories sharing the same prefix up to that token. They identify that non-uniform process set distributions hinder exploration/exploitation and propose λ-GRPO, which normalizes each token's loss by its process set size |λ^{(i,t)}|, achieving >10% average accuracy improvement and 2× convergence speedup on Qwen-1.5B. Crucially for our work: when GRPO uses explicit PRM scores as trajectory rewards (as in our setup and Stop Summation's), the optimization involves BOTH the explicit PRM (determining trajectory-level advantage via group-relative normalization of PRM scores) AND the implicit MC-PRM (distributing that advantage across tokens through prefix sharing). This dual-PRM dynamic could qualitatively alter exploitation: the explicit PRM determines WHICH strategies are favored, while the implicit PRM determines HOW learning is distributed across solution steps. λ-GRPO normalizes the implicit PRM's contribution but does not affect the explicit PRM's trajectory-level signal — a distinction we test experimentally. Nimmaturi et al. (arXiv:2507.18014) derive GRPO scaling laws with exponential saturation — we incorporate as a null model.\n\n**C. PRM-Specific Analysis.** Cheng et al. (arXiv:2504.15275, NeurIPS 2025) identify summation-form credit assignment as the mechanistic cause of PRM hacking in GRPO and propose min-form (PURE). Their work answers WHY exploitation happens; ours answers WHEN and HOW — and we formally derive that summation-form creates a fold bifurcation while min-form eliminates it. Song et al. (arXiv:2508.04216, AAAI 2026 Workshop) train SAEs on PRM activations for static deconfounding at inference time — complementary to our policy-model dynamics monitoring. Tiwari et al. (arXiv:2603.06621) characterize the end state. TP-GRPO (OpenReview:LZZENDlZt9) addresses GenPRM-specific pitfalls.\n\n**D. Detection Methods.** Wang et al. (arXiv:2510.01367, ICLR 2026 Oral, TRACE) detect implicit reward hacking by measuring reasoning effort via progressive CoT truncation, achieving F1≈0.97 in math on dataset-level loopholes. TRACE operates on a fundamentally different principle from our framework: it measures per-sample reasoning effort (whether the model 'knows the answer' early in its CoT) via truncation AUC, while we monitor population-level temporal dynamics across training checkpoints. TRACE is an excellent sample-level detector but does not predict exploitation onset, characterize bifurcation type, or identify what the model exploits mechanistically. We include TRACE as a key ablation baseline — a particularly strong comparison because its high F1 sets a demanding bar for alternative approaches. It was validated with RLOO and GRPO under outcome-based rewards, not PRM-guided RL; we adapt it to our setting. Beigi et al. (arXiv:2602.19416, IR³) combine contrastive inverse RL with SAEs for interpretable post-hoc reward hacking detection, achieving 0.89 correlation with ground-truth rewards and >90% precision in identifying hacking features. IR³ operates post-hoc (requiring sampling access to aligned and baseline policies after training) rather than during training — directly relevant to our SAE approach but not a training-time baseline. Their SAE decomposition of reconstructed rewards (R̂ = Σω_i f_i + c) provides complementary evidence that SAE features can identify hacking signatures, validating our choice of SAE-based monitoring. Key distinction: IR³ reconstructs the implicit reward function from behavioral contrasts, while we track the policy's evolving representations to predict exploitation before it manifests behaviorally. Wang et al. (arXiv:2604.16242, GRIFT) use gradient fingerprints for post-hoc sample-level detection. Mahmoud et al. (arXiv:2605.12474) propose the self-internalization gap for rubric-based RL.\n\n**E. Representation-Level Monitoring.** Yan et al. (arXiv:2602.05183) use SAEs for Diplomacy RL dynamics. Shi et al. (arXiv:2507.00665, SAFER) probe reward model safety via SAE activation differences. Song et al.'s CRA uses SAEs on PRM activations for static deconfounding — distinct from our policy-model tracking.\n\n**F. Statistical and Information-Theoretic Diagnostics.** Miao et al. (arXiv:2402.09345, NeurIPS 2024, InfoRM) propose MOP/CSI/ICDS metrics in the IB latent space for reward-model-side overoptimization detection — complementary to our policy-side monitoring. Gao et al. (arXiv:2210.10760) provide overoptimization scaling laws for best-of-N/PPO.\n\nThe gap: a bifurcation-theoretic framework deriving specific predictions from GRPO's credit assignment mechanisms (not generic early warning signals), validated against strong baselines (TRACE, self-internalization gap, energy loss, scaling law deviation, gradient fingerprints), with explicit treatment of the dual-PRM dynamics in GRPO + explicit PRM, and systematic comparison across discriminative and generative PRMs.\n\n## Approach\nWe develop and empirically validate a bifurcation-theoretic framework for PRM exploitation during GRPO training, deriving PRM-specific predictions from the credit assignment mechanism and rigorously comparing against six detection baselines. Experiments are organized into three priority tiers.\n\n**Tiered Experiment Design.**\n- *Tier 1 (Essential — publishable core, ~55% of compute):* Qwen3-4B via GRPO with all 3 PRMs (Qwen2.5-Math-PRM-7B, ACTPRM-X, GenPRM-7B) on MATH/AMC/AIME datasets, plus Qwen3-14B via GRPO with Qwen2.5-Math-PRM-7B. Full diagnostic panel and all baseline comparisons at each checkpoint. This yields 4 training runs covering both model scales, all three PRMs, and the complete analytical framework. (4 runs × ~4h avg = ~16h training + ~90h evaluation/SAE/TRACE/analysis)\n- *Tier 2 (Important — strengthens contribution, ~30% of compute):* Qwen3-14B via GRPO with ACTPRM-X and GenPRM-7B (completing cross-PRM comparison at 14B), PURE ablation (min-form) on Qwen3-4B with Qwen2.5-Math-PRM-7B, λ-GRPO ablation (Sullivan et al.'s process-set normalization) on Qwen3-4B with Qwen2.5-Math-PRM-7B, and GRIFT-style gradient fingerprint baseline on sampled checkpoints. (4 runs × ~5h avg = ~20h training + ~60h analysis)\n- *Tier 3 (Stretch — extends scope, ~15% of compute):* PPO pilot (Qwen3-4B + Qwen2.5-Math-PRM-7B) for cross-algorithm generalization, spectral heat capacity signal (following Hennick & Corlouer), and energy loss monitoring extension to step-level rewards. (~1 run + specialized analysis, ~30h total)\n\nAll experiments use the OpenRLHF framework. Tier 1 is prioritized for completion by week 10; Tier 2 by week 14; Tier 3 as time permits.\n\n**Dual-PRM Experimental Setup.** We explicitly address the dual-PRM dynamic revealed by Sullivan et al. In our setup, PRM scores are the sole trajectory-level reward signal in GRPO — the explicit PRM evaluates each solution step and scores are aggregated (via summation, min, or mean) into a trajectory reward, which is then normalized via group-relative advantage computation. Crucially, GRPO's implicit Monte-Carlo PRM (Sullivan et al.) operates simultaneously at the token level: tokens sharing prefixes across trajectories within a group receive implicit step-level advantages equal to the mean trajectory reward of completions sharing that prefix. Thus, the policy is optimized against BOTH the explicit PRM (trajectory-level: which solutions are favored) AND the implicit MC-PRM (token-level: how advantage is distributed across solution steps). We hypothesize three distinct exploitation interaction modes: (1) constructive — both PRMs agree on step quality, accelerating aligned learning; (2) amplifying — the implicit PRM concentrates learning on tokens where the explicit PRM is most exploitable, accelerating exploitation onset; (3) buffering — the implicit PRM's averaging smooths out the explicit PRM's exploitable local maxima, delaying exploitation. Testing which mode dominates and whether it changes across training is a core empirical question. The λ-GRPO condition (Tier 2) isolates this: by normalizing process set sizes, λ-GRPO equalizes the implicit PRM's contribution, allowing us to test whether the dual-PRM interaction amplifies or buffers exploitation.\n\n**Checkpoint Strategy and Storage.** We save checkpoints every 5 training steps across 500+ steps (~100+ checkpoints per run). Tiered strategy: full checkpoints every 25 steps, delta-compressed at intermediate 5-step intervals (3–4× compression), and online computation of diagnostics during training. Storage: ~8–12TB. Prune to anomaly-adjacent windows after analysis.\n\n**Multi-Signal Diagnostic Panel.** At each checkpoint: PRM reward, ground-truth accuracy via outcome verification, solution style decomposition (Tiwari et al.'s taxonomy), PRM-adapted self-internalization gap, energy loss (ΔE = ||h^in||_1 − ||h^out||_1), TRACE score (adapted to PRM setting, computed on a held-out evaluation set), SAE features from residual stream activations, and optionally (Tier 3) spectral heat capacity.\n\n**TRACE Adaptation for PRM-Guided RL.** TRACE (Wang et al., ICLR 2026 Oral) measures reasoning effort by progressively truncating CoT at percentages p ∈ {10%, 20%, ..., 100%}, forcing early answers, and computing AUC of expected reward vs. truncation fraction. Originally validated with outcome-based rewards in RLOO/GRPO, we adapt it to PRM-guided RL: at each checkpoint, we evaluate the held-out set by truncating solutions at each percentage, computing the PRM score on the truncated solution (using the PRM's step-level scores up to the truncation point), and calculating the TRACE-PRM score as the AUC. High TRACE-PRM scores indicate the model achieves high PRM scores with minimal reasoning effort — a signature of PRM exploitation. We validate this adaptation by confirming correlation between TRACE-PRM scores and ground-truth accuracy degradation.\n\n**Self-Internalization Gap: PRM Adaptation.** We construct two evaluation contexts: (1) PRM-verification-conditioned — math problem augmented with system prompt encoding step-level correctness criteria ('Ensure each reasoning step is mathematically correct and logically follows from previous steps. Verify intermediate results.'), with richer conditioning for GenPRM matching its reasoning format; (2) Prompt-only — minimal instruction. At each checkpoint, sample K=10 solutions from conditioned distribution, compute length-normalized log-probabilities under both contexts. The PRM-adapted self-internalization gap Δ_PRM(t) = mean difference. Validate by confirming r>0.85 correlation with accuracy trajectories.\n\n**SAE Training Strategy.** Anchor-and-monitor: train a single TopK-SAE (32K hidden dims, K=32) on pooled residual stream activations from checkpoints at steps 0, 25, 50, 100. Apply across subsequent checkpoints; fine-tune when reconstruction loss exceeds 2× baseline mean. Distinction from IR³ (Beigi et al.): IR³ reconstructs implicit reward functions from behavioral contrasts post-hoc, while we track policy representation evolution during training. Distinction from CRA (Song et al.): CRA trains SAEs on PRM activations for static deconfounding; we train on policy model activations for dynamics monitoring. Estimated: ~40h anchor training + ~30h fine-tuning/extraction.\n\n**Theoretical Framework: Fold Bifurcation in PRM Exploitation.**\n\nOur core theoretical contribution goes beyond applying generic early warning signals to a new domain. We derive the specific bifurcation structure arising from GRPO's credit assignment mechanism, building on and extending Karwowski et al.'s geometric Goodhart framework.\n\n*Setup.* Consider GRPO training with explicit PRM providing step-level scores s_1, ..., s_T. Under summation-form credit assignment, the trajectory reward is R = Σ_t s_t. Define α(t) ∈ [0,1] as the exploitation fraction — the probability mass the policy assigns to PRM-exploitative strategies at training step t. Let Δs = E[s_E] - E[s_G] > 0 be the per-step PRM score gap between exploitative (s_E) and genuine (s_G) strategies (positive by assumption that the PRM is imperfect).\n\n*Positive feedback mechanism.* GRPO's group-relative normalization computes advantages A_i = (R_i - μ_G)/σ_G where μ_G and σ_G are group mean and std. As α increases, more trajectories in each group use exploitative strategies, raising μ_G. This makes genuinely correct trajectories (with lower R) receive increasingly negative advantage, suppressing them and further increasing α. This is a positive feedback loop absent from Karwowski et al.'s steepest-ascent framework (which involves no group normalization) and absent from standard RL settings without group-relative advantage.\n\n*Fold bifurcation derivation.* We model the exploitation fraction dynamics as: dα/dt = f(α; λ(t)) where λ(t) is the effective optimization pressure (monotonically increasing with training). The positive feedback creates a cubic nonlinearity: f(α; λ) = λ - λ_c + (α - α_c)² + h.o.t., which is the normal form of a fold (saddle-node) bifurcation. Below the critical pressure λ_c, there exist two equilibria: a stable low-exploitation equilibrium and an unstable threshold. At λ = λ_c, these equilibria collide and annihilate — the system transitions to the high-exploitation regime. The critical pressure λ_c depends on: (i) the per-step PRM score gap Δs, (ii) solution length T (longer solutions → lower λ_c under summation-form because R = T·Δs), (iii) group size (larger groups → sharper normalization → stronger positive feedback → lower λ_c), and (iv) the implicit MC-PRM's contribution (prefix-sharing structure modulates token-level gradient distribution).\n\n*PRM-specific scaling predictions.* The fold bifurcation generates five testable, quantitatively specific predictions — NOT generic properties of tipping points:\n\n(P1) **Fold-specific autocorrelation scaling**: The autocorrelation time of the proxy-true gap G(t) = R_proxy(t) - R_true(t) diverges as τ_ac ~ |λ(t) - λ_c|^{-1/2} approaching the transition. This 1/2 exponent is specific to fold bifurcations and distinguishes them from transcritical (exponent 1) or Hopf (exponent 1/2 but with oscillatory component) bifurcations. We fit the scaling exponent empirically and test against the fold prediction.\n\n(P2) **Variance scaling**: Fluctuations in G(t) grow as σ² ~ |λ(t) - λ_c|^{-1/2}, again with the fold-specific exponent.\n\n(P3) **Solution-length dependence**: The critical training step t* at which exploitation onset occurs should decrease with solution length T under summation-form (because R_exploit/R_genuine = T·E[s_E]/T·E[s_G], and the group-normalization positive feedback strengthens with larger reward variance). Concretely, we test whether t*(AMC) < t*(MATH-easy) on matched problem sets differing primarily in solution length.\n\n(P4) **Credit assignment modulation**: Under min-form (PURE), the positive feedback is broken — a single genuinely-scored step caps the trajectory reward, preventing μ_G from rising with exploitation. The fold bifurcation should be eliminated: G(t) follows smooth crossover dynamics with NO divergent autocorrelation. Under λ-GRPO, the fold persists (since it arises from the explicit PRM's trajectory-level signal, not the implicit PRM) but λ_c may shift because the implicit PRM's contribution to gradient distribution is normalized.\n\n(P5) **Dual-PRM interaction signature**: In standard GRPO + explicit PRM, the implicit MC-PRM concentrates gradient updates on tokens with high prefix-sharing (common solution openings). If exploitation strategies share prefixes (e.g., similar boilerplate openings before diverging into exploitative patterns), the implicit PRM amplifies learning of these shared exploitative prefixes — lowering λ_c. λ-GRPO normalization should weaken this amplification, raising λ_c. We test this by comparing exploitation onset timing between standard GRPO and λ-GRPO.\n\n*Connection to Karwowski et al.* Their framework shows Goodharting occurs when the optimization trajectory hits the occupancy polytope boundary where proxy and true reward directions diverge. In our GRPO + PRM setting, the 'boundary' corresponds to the policy having saturated the genuinely-learnable PRM scoring patterns and beginning to exploit non-robust features. Our fold bifurcation formalizes the mechanistic transition at this boundary: Karwowski's 'directional phase shift' (their Proposition 3) corresponds to our fold bifurcation's annihilation of the aligned equilibrium. The extension is that (a) the positive feedback from group normalization makes the transition sharper than in steepest ascent, (b) the neural PRM's nonlinearity creates a specific bifurcation type (fold) derivable from the credit assignment form, and (c) the dual-PRM structure introduces modulation parameters absent from their single-reward framework.\n\n**Statistical Analysis and Baselines.** We test predictions using: PELT changepoint detection, BOCPD for uncertainty quantification, sliding-window autocorrelation and detrended fluctuation analysis for scaling exponent estimation, HMM regime detection, GRPO exponential saturation model as null model, and Karwowski et al.'s NDH (Normalized Drop Height) as a Goodhart severity metric. Novel metrics: 'Goodhart divergence rate' (dG/dt), 'critical slowing down index' (autocorrelation coefficient in trailing window), and 'fold scaling exponent' (fitted from τ_ac vs. |t - t*| in log-log space).\n\n**Ablation Against Six Baselines.** A key contribution is rigorous comparison against six simpler alternatives spanning four detection paradigms:\n\n*(i) Dynamics-based:* (a) PRM-adapted self-internalization gap, (b) naive proxy-true divergence rate threshold, (c) GRPO scaling law deviation (residuals from exponential saturation fit).\n\n*(ii) Effort-based:* (d) TRACE-PRM score (adapted progressive CoT truncation AUC, following Wang et al., ICLR 2026 Oral) — this is our strongest baseline given TRACE's F1≈0.97 in math. We compute TRACE-PRM at each checkpoint on the held-out evaluation set and test whether TRACE score increase precedes accuracy-reward divergence with comparable or greater lead time than our framework.\n\n*(iii) Representation-based:* (e) Energy loss monitoring (ΔE, adapted from Miao et al.'s PPO setting to GRPO).\n\n*(iv) Gradient-based:* (f) GRIFT-style gradient fingerprints on sampled checkpoints (Tier 2).\n\nFor each baseline, we measure: detection lead time (training steps before accuracy-reward divergence), false positive rate, intervention effectiveness as early stopping trigger, and (for TRACE and self-internalization gap) whether the signal distinguishes aligned plateau from pre-exploitation regime. The bifurcation framework must demonstrate at least one of: (i) earlier detection via fold-specific scaling exponent divergence, (ii) lower false positive rate via bifurcation-type discrimination (distinguishing the fold's sharp transition from normal saturation's smooth plateau), (iii) mechanistic interpretability via SAE features identifying WHAT is exploited, (iv) regime identification enabling intervention selection (not just early stopping), or (v) quantitative prediction of exploitation onset timing via λ_c estimation.\n\n**Cross-Paradigm Comparison.** We compare exploitation dynamics across discriminative vs. generative PRMs — testing whether the fold bifurcation structure persists, shifts (different λ_c), or changes type (fold → smooth crossover) with GenPRM's explicit verification reasoning. We additionally test (Tier 2) PURE and λ-GRPO as bifurcation-modifying interventions: PURE should eliminate the fold (P4), while λ-GRPO should shift λ_c (P5).\n\n**Early Warning Validation.** We test whether fold-specific scaling (P1-P2) provides earlier and more reliable warning than generic early warning signals and the six baselines. We report the distribution of lead times across runs, PRM types, and model scales, alongside confidence intervals, and test detected signals as triggers for dynamic interventions (early stopping, reward model switching, Advantage Modification).\n\n**Generalization Discussion.** The fold bifurcation framework extends beyond math+GRPO: any RL system with (a) a learned proxy reward, (b) group-relative or batch normalization of advantages, and (c) a discoverable exploitation strategy exhibits the positive feedback mechanism driving the fold. We validate with the Tier 3 PPO pilot (where advantage normalization plays an analogous role) and discuss how complementary approaches — CRA's PRM deconfounding, InfoRM's IB-based monitoring, IR³'s post-hoc interpretable detection — could combine with our training-time dynamics monitoring.\n\n**Scope and Limitations.** Tier 1 spans two model scales, three PRMs across two paradigms, six baselines, and the full theoretical+empirical framework — sufficient for a publishable contribution. Tier 2 extends to PURE, λ-GRPO, full 14B cross-PRM comparison, and GRIFT. The fold bifurcation derivation is a phenomenological model (normal form reduction from the positive feedback mechanism) rather than a rigorous proof from GRPO's objective — we position it as generating testable predictions, not as a theorem. If empirical scaling exponents deviate from fold predictions (e.g., suggesting transcritical or no bifurcation), this itself is informative and we report the fitted bifurcation type as a core result.\n\n## Inspiration\nNovel theoretical synthesis: Karwowski et al.'s geometric Goodhart formalization in RL + fold bifurcation theory from dynamical systems + GRPO's dual-PRM structure (Sullivan et al.) + Stop Summation's credit assignment mechanism → derive that summation-form GRPO creates a specific fold bifurcation in the exploitation fraction with quantitative scaling predictions, extending Karwowski's linear-reward framework to neural PRMs. Empirical synthesis: systematic comparison of six orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based, energy-based, scaling-law-based) for PRM exploitation monitoring.\n\n## Key References\n- Goodhart's Law in Reinforcement Learning (arXiv:2310.09144, Karwowski et al. 2024, ICLR 2024)\n- GRPO is Secretly a Process Reward Model (arXiv:2509.21154, Sullivan et al. 2025, under review ICML 2026)\n- Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort (arXiv:2510.01367, Wang et al. 2026, ICLR 2026 Oral — TRACE)\n- IR³: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking (arXiv:2602.19416, Beigi et al. 2026)\n- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, 2026)\n- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, Mahmoud et al. 2026)\n- Natural Emergent Misalignment from Reward Hacking in Production RL (arXiv:2511.18397, 2025)\n- Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning (arXiv:2602.05183, Yan et al. 2026)\n- Early-warning signals for critical transitions (Scheffer et al., Nature 461, 2009)\n- From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability (arXiv:2603.29805, Hennick & Corlouer 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (arXiv:2504.15275, Cheng et al. 2025, NeurIPS 2025)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, GRIFT, Wang et al. 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, Shi et al. 2025)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv:2507.18014, Nimmaturi et al. 2025)\n- Scaling Laws for Reward Model Overoptimization (arXiv:2210.10760, Gao et al. 2023)\n- Latent State Models of Training Dynamics (arXiv:2308.09543, 2023)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, 2026)\n- GenPRM: Scaling Process Reward Models with Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Smarter Not Harder: TP-GRPO with Intrinsic-Signal Driving and Ability-Adaptive Reward Shaping (OpenReview:LZZENDlZt9, 2026)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward (ICLR 2026)\n- The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? (arXiv:2512.16912, 2025)\n- Mitigating Reward Hacking with RL Training Interventions (ICLR 2026)\n- Detecting Proxy Gaming in RL and LLM Alignment via Evaluator Stress Tests (arXiv:2507.05619, 2025)\n- Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges (arXiv:2604.13602, 2026)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026)\n- Posterior-GRPO: Rewarding Reasoning Processes in Code Generation (arXiv:2508.05170, 2025)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, Song et al. 2025, AAAI 2026 Workshop)\n- The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking (arXiv:2501.19358, Miao et al. 2025, ICML 2025)\n- InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling (arXiv:2402.09345, Miao et al. 2024, NeurIPS 2024)\n- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, Helff et al. 2026, ICLR 2026 Workshop)\n- A mathematical framework for critical transitions: bifurcations, fast-slow systems and stochastic dynamics (arXiv:1101.2899, Kuehn 2011)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '530–750 H100-hours (Tier 1: 4 runs ~16h training + ~130h eval/SAE/TRACE/analysis; Tier 2: 4 runs [14B×2 PRMs + PURE + λ-GRPO ablations] ~20h training + ~60h analysis + ~30h GRIFT; Tier 3: PPO pilot + spectral ~30h; shared overhead: ~70h SAE + ~40h TRACE evaluation)', 'timeline': '14–18 weeks (Tier 1 complete by week 10, Tier 2 by week 14, Tier 3 as time permits)', 'estimated_gpu_cost': '$800–$1,310 (at ~$1.50–$1.75/H100-hr spot pricing)', 'storage': '~8–12TB with delta compression'}\n- **human_in_loop**: {'gpu_hours': '440–600 H100-hours (Claude-guided hyperparameter selection, early termination of unpromising runs, targeted SAE fine-tuning; Tier 1 prioritized)', 'timeline': '10–14 weeks (Tier 1 by week 8, Tier 2 by week 12)', 'claude_api_cost': '$400–$600 (checkpoint analysis, TRACE evaluation automation, bifurcation fitting, scaling exponent estimation, baseline comparison, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$660–$1,050', 'storage': '~6–10TB'}\n- **auto_research**: {'gpu_hours': '640–960 H100-hours (parallel Tier 1+2, automated bifurcation fitting, baseline sweep, some redundant runs)', 'timeline': '6–8 weeks wall-clock (Tiers 1+2 parallelized; Tier 3 conditional)', 'claude_api_cost': '$700–$1,200 (experiment orchestration, real-time analysis, TRACE adaptation, bifurcation analysis, iterative paper writing)', 'estimated_gpu_cost': '$960–$1,680', 'storage': '~10–15TB', 'speed_bottleneck': 'Sequential RL training runs (3–5h per run on 4–8×H100); SAE extraction adds serial dependency; TRACE evaluation adds ~20% inference overhead per checkpoint'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:12:25.208Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:12:25.208Z",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:12:25.220Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：投稿会议严重不匹配】

本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。
CoRL 2026 Call for Papers 明确声明：
  - "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
  - "Submissions without a robotics focus will be returned without review."

本 proposal 的全部内容是 LLM 数学推理训练中 PRM 利用的动力学分析，涉及 GRPO、PRM credit assignment、bifurcation theory——与机器人学无任何关联。
按照 CoRL 2026 的明确政策，本 proposal 将被 desk reject（不送审即退稿）。

→ 如果投稿目标确为 CoRL，概率估计应为 ≤2%，无需进入后续审核流程。
→ 如果投稿目标实际是 NeurIPS 2026 / ICML 2026 / ICLR 2027 等 ML 会议，以下评估才有意义。

**以下评估假设投稿目标为合适的 ML 顶会（如 NeurIPS 2026），而非 CoRL。**

---

【领域调研】:

- [Karwowski et al., "Goodhart's Law in Reinforcement Learning"](https://arxiv.org/abs/2310.09144) (ICLR 2024): 
  建立了 RL 中 Goodhart 现象的几何框架，基于 occupancy polytope 边界分析，提出 optimal early stopping。本 proposal 的理论基础。确认为真实论文，描述准确。但原始框架限于 tabular MDP + 线性 reward。

- [Sullivan et al., "GRPO is Secretly a Process Reward Model"](https://arxiv.org/abs/2509.21154) (under review ICML 2026): 
  证明 GRPO + ORM 等价于隐含 MC-PRM 的目标函数，提出 λ-GRPO。确认为真实论文。proposal 中对 dual-PRM dynamics 的描述准确。

- [Wang et al., "TRACE: Detecting Implicit Reward Hacking by Measuring Reasoning Effort"](https://arxiv.org/abs/2510.01367) (ICLR 2026 Oral): 
  通过 CoT 截断 AUC 检测 reward hacking，F1≈0.97。确认为 ICLR 2026 Oral。这是本 proposal 最强的 trivial alternative 竞争者。

- [Cheng et al., "Stop Summation: Min-Form Credit Assignment"](https://arxiv.org/abs/2504.15275) (NeurIPS 2025): 
  识别 summation-form credit assignment 为 PRM hacking 的机制原因，提出 PURE (min-form)。确认为 NeurIPS 2025 Poster。proposal 的预测 P4（min-form 消除 fold）本质上是用 bifurcation 语言重述此发现。

- [Hennick & Corlouer, "From Density Matrices to Phase Transitions in Deep Learning"](https://arxiv.org/abs/2603.29805) (arXiv 2026): 
  用 2RDM 谱分析检测训练中的 phase transitions（grokking、emergent misalignment 等）。确认存在。是概念上最近的邻居——dynamics-based 训练监控，但研究 beneficial transitions 而非 adversarial exploitation。

- 未找到任何现有工作将 fold bifurcation / saddle-node dynamics 直接应用于 reward hacking/PRM exploitation。这一特定理论框架确实是新的。

- 调研总结: PRM exploitation / reward hacking 是 2025-2026 极活跃的领域，已有丰富的经验性工作（检测方法、机制分析、mitigation）。理论性工作相对稀缺——Karwowski et al. 是唯一严格的形式化框架，但限于 tabular 设定。将 bifurcation theory 引入 PRM exploitation 确实是一个空白，但这个空白是否值得填补取决于理论框架能否产生超越简单 baseline 的实际价值。

---

【Trivial Alternative 检验】:

**存在严重的 trivial alternative 威胁。**

1. **TRACE (F1≈0.97)** 是最直接的威胁。TRACE 用极简的方法（CoT 截断 + AUC 计算）就能高精度检测 reward hacking。proposal 承认 TRACE 是最强 baseline，但其核心论证是"TRACE 检测 hacking 但不预测 onset"。然而：
   - "预测 onset" 的实际价值存疑。如果 TRACE 能在 exploitation 早期就检测到（F1≈0.97），那么 onset 预测的 lead time 优势有多大？proposal 没有给出任何理论或经验证据说明 bifurcation early warning 能比 TRACE 早多少。
   - "bifurcation type discrimination"（区分 fold vs. smooth crossover）是一个学术上优雅但实践价值不清的贡献——practitioner 关心的是"什么时候该停训练"，不是"这是哪种 bifurcation"。

2. **简单的 proxy-true divergence 监控**：监控 PRM reward 和 ground-truth accuracy 的差值，设一个 threshold，就是最简单的检测。proposal 的 bifurcation framework 需要证明其 scaling exponent fitting 比简单 threshold 有实质优势。

3. **Stop Summation / PURE 本身**：如果问题是"summation-form 导致 exploitation"，Stop Summation 已经给出了解决方案（换成 min-form）。bifurcation framework 的增量价值不是诊断问题，也不是解决问题，而是提供一个中间层的"预测"——但如果 fix 已经已知，prediction 的实际需求是什么？

增量价值论证：proposal 声称的增量价值在于 (i) 更早的预警 (ii) bifurcation type discrimination (iii) mechanistic interpretability via SAE (iv) regime identification。其中 (iii) 和 (iv) 更有说服力，但 (i) 未经验证，(ii) 的实践价值不明确。

---

【前提假设检验】:

核心 claim 的逻辑链中有多个未经验证的假设：

1. **"Group-relative normalization 产生的 positive feedback 能被建模为 fold bifurcation 的 normal form"**——这是整个理论大厦的基础，但 proposal 自己承认这是 "phenomenological model (normal form reduction)" 而非 "rigorous proof from GRPO's objective"。从 positive feedback 存在到 fold bifurcation 的 normal form f(α;λ) = λ - λ_c + (α - α_c)² 之间，有一个巨大的逻辑跳跃。为什么是 fold 而不是其他 bifurcation type？proposal 没有从 GRPO 的实际梯度动力学推导出这一点，而是直接 assume 了 normal form。如果实验发现 exponent 不是 -1/2，proposal 说"这本身也是信息"——但这实际上意味着理论预测失败，整个 fold bifurcation framing 失效。

2. **"Exploitation fraction α(t) 是一个可以被良好定义和测量的 scalar order parameter"**——在实际训练中，exploitation 是多维的（solution style decomposition 有多种 category），将其压缩为一个标量 α 是否合理？如果 exploitation 是通过多种不同机制同时发生的，α(t) 的动力学可能不满足任何简单的 bifurcation normal form。

3. **"PRM score gap Δs = E[s_E] - E[s_G] > 0 是常数或缓慢变化的"**——这是推导 fold structure 的隐含假设。但在训练过程中，policy 的分布不断变化，PRM 对 exploitative vs. genuine strategies 的 score gap 也可能非平稳。如果 Δs 本身是 α 的函数（co-evolution），fold bifurcation 的简单图景就不成立。

4. **"Dense checkpoint (每 5 步) 的分辨率足以拟合 scaling exponent"**——拟合 τ_ac ~ |λ - λ_c|^{-1/2} 需要在临界点附近有足够多的数据点。但 RL 训练中噪声很大，每次 checkpoint 的 metric 波动显著。在有限数据和高噪声下拟合 critical exponent 是出了名的困难（凝聚态物理中用 Monte Carlo 拟合 critical exponents 需要大量系统尺寸的 finite-size scaling）。proposal 没有讨论统计 power 的问题。

---

【3 维度打分】:

1. **Novelty: 中** — 
   将 bifurcation theory 应用于 PRM exploitation 确实是新的角度——我的调研未发现任何现有工作做过这件事。五个 testable predictions 有具体的定量形式（-1/2 exponent 等），不仅仅是定性描述。但 novelty 需要打折扣：(a) 核心机制洞察（summation-form 导致 exploitation）来自 Stop Summation (NeurIPS 2025)，positive feedback from group normalization 也是对已知现象的形式化重述；(b) "phenomenological model" 的理论深度有限——它不是从 GRPO 动力学严格推导的，而是先 assume bifurcation type 再检验，这更接近 curve fitting 而非理论贡献；(c) 五个 predictions 中 P3（长度依赖）和 P4（min-form 消除 exploitation）在 Stop Summation 框架下已经是可预期的，bifurcation 语言只是重新包装。真正新颖的是 P1/P2 的定量 scaling exponents 和 P5 的 dual-PRM interaction，但 P5 依赖于 Sullivan et al. 的框架且预测方向不明确（proposal 列出三种可能模式但无法 a priori 区分）。

2. **Significance: 中偏弱** — 
   (a) 研究问题确实重要——PRM exploitation 是 LLM reasoning 训练的核心挑战，这一点毫无疑问。(b) 但 **核心发现如果为 positive（即确认 fold bifurcation），审稿人很可能会说 "I would have guessed this"**。positive feedback → tipping point 是直觉上自然的结果；将其形式化为 fold bifurcation 增加了数学精确性，但不太可能让人感到 "surprising"。(c) 实际影响力受限于 trivial alternative 问题：如果 TRACE (F1≈0.97) 已经解决了检测问题，Stop Summation/PURE 已经解决了 mitigation 问题，bifurcation framework 在 practitioner 层面的影响力有限。(d) 作为一项对 GRPO-specific 训练动力学的分析性研究，其 generalizability 也受限——proposal 的 Tier 3 PPO 扩展是 stretch goal，核心结论高度依赖于 GRPO 的 group-relative normalization，不易推广。(e) 唯一真正有 significance 的场景是：如果 bifurcation framework 能提供比现有方法显著更早的预警（比如在 exploitation 发生前 50+ 步），这将有实际价值——但这是一个未验证的 empirical claim。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。对 6 个领域类别的覆盖非常全面（Goodhart formalization、GRPO analysis、PRM analysis、detection methods、representation monitoring、statistical diagnostics）。对每篇关键论文的定位都清晰准确——Karwowski et al. 的局限性（tabular MDP, linear reward）、TRACE 的优劣（高精度但不预测 onset）、Stop Summation 的关系（WHY vs. WHEN/HOW）、Sullivan et al. 的 dual-PRM 洞察。我验证了主要引用均真实存在且描述正确。差异化定位清晰。唯一的小问题是某些引用数量过多（30+ 篇），可能导致真正的定位信息被稀释。

---

【概率估计】: 

**如果投 CoRL 2026：0-2%（desk reject，不送审即退稿）**

**如果投合适的 ML 顶会（NeurIPS 2026 等）：18% - 30%，中位 23%**

【估计理由】: 

CoRL 概率的理由极为直接：proposal 没有任何机器人学内容，CoRL 明确声明"无机器人学焦点的投稿将不经审稿退回"。

ML 顶会概率的推理：Novelty 为中——有真实的新角度但理论深度有限（phenomenological model），且核心洞察建立在已有工作之上。Significance 为中偏弱——核心发现如果 positive 不太可能让审稿人感到 surprising，实际价值受 TRACE/PURE 等 trivial alternative 的严重挤压。Related Work 强，但这是形式完善度而非 idea 内核。综合来看处于 "方向正确、有真实 novelty delta，但核心发现审稿人可能说 'I would have guessed this'" 的 25-35% 区间的下半段，因为 trivial alternative 威胁（TRACE, PURE）将上界压低。

限制上界的维度是 **Significance**：即使所有实验都 work out，核心贡献（用 bifurcation 语言形式化了一个已知的 positive feedback 现象）的 impact ceiling 不高。限制下界的是 **Novelty** 中的真实新颖成分（定量 scaling predictions、dual-PRM interaction）和极为全面的 related work coverage。

【主要风险】: 

1. **Trivial Alternative 致命挑战**：审稿人最可能的攻击是 "TRACE already achieves F1≈0.97 for detection, PURE already solves the mechanism — what is the practical value of knowing this is a fold bifurcation rather than just a tipping point?"。如果 bifurcation framework 在 lead time 上无法显著超越 TRACE，整个 contribution 退化为 "interesting but incremental theoretical observation"。

2. **Phenomenological theory 的可证伪性风险**：如果实验中 scaling exponents 偏离 -1/2（这在有限数据 + 高噪声的 RL 训练中非常可能），proposal 的 fallback 是 "报告实际 bifurcation type 作为核心结果"。但这意味着最核心的理论预测失败了——审稿人会质疑：如果不是 fold bifurcation，那整个 framework 的价值是什么？proposal 在理论 claim 的强度和 hedging 之间走钢丝。
```

---

**⚠️ 再次强调关键问题：** 此 proposal 投 CoRL 2026 几乎必然被 desk reject。CoRL 要求 "core robotics problem"，本 proposal 是纯粹的 LLM 训练动力学分析，与机器人学无关。建议重新选择投稿会议（NeurIPS 2026、ICML 2026、ICLR 2027 等），否则一切后续审核优化都没有意义。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Karwowski et al., Goodhart's Law in RL (ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [Sullivan et al., GRPO is Secretly a PRM](https://arxiv.org/abs/2509.21154)
- [Wang et al., TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Cheng et al., Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Hennick & Corlouer, Density Matrices to Phase Transitions](https://arxiv.org/abs/2603.29805)
- [Reward Hacking in the Era of Large Models (Survey)](https://arxiv.org/abs/2604.13602)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
调研完成。现在我掌握了关键信息，尤其是一个**致命的venue mismatch问题**。让我完成评估。

---

```
【阶段】: Triage

【⚠️ 致命前置问题：投稿目标与proposal完全不匹配】

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance 
of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are 
encouraged to report real-robot experiments or provide convincing evidence that 
simulation experiments are transferable to real robots. Submissions without a robotics 
focus will be returned without review."

本 proposal 的全部内容是：PRM exploitation 在 GRPO 训练中的 bifurcation 
dynamics，针对 LLM 数学推理任务（MATH/AMC/AIME），使用 Qwen3-4B/14B。
没有任何机器人相关内容——没有 robot learning、没有 manipulation、没有 
locomotion、没有 sim-to-real、没有 embodied AI。

结论：该 proposal 投稿 CoRL 2026 将被 desk-reject，不进入评审流程。
概率为 0%。

本 proposal 适合的投稿目标：NeurIPS 2026 / ICML 2026 / ICLR 2027 / 
AAAI 2027 主会（RL theory / LLM alignment track）。

以下对 idea 质量的评估假设投稿目标更正为合适的 ML 会议（如 NeurIPS/ICML/ICLR），
供后续流程参考。

---

【领域调研】:

1. Karwowski et al. "Goodhart's Law in Reinforcement Learning" (ICLR 2024, 
   arXiv:2310.09144): 
   在 tabular MDP 中形式化 Goodhart's law，用 occupancy polytope 几何解释
   proxy-true reward 偏离，推导最优 early stopping + regret bound。
   局限：线性 reward、无 neural PRM、无 step-level credit、无 group normalization。
   → 本 proposal 声称的"基础框架"确实存在且描述准确。

2. Sullivan et al. "GRPO is Secretly a Process Reward Model" (arXiv:2509.21154, 
   under review ICML 2026): 
   证明 GRPO + ORM 等价于一个带隐式 Monte-Carlo PRM 的目标。提出 λ-GRPO 
   修正 process set imbalance。
   → 本 proposal 的 dual-PRM 分析依赖此结论，引用准确。

3. Cheng et al. "Stop Summation / PURE" (NeurIPS 2025, arXiv:2504.15275): 
   识别 summation-form credit assignment 是 PRM hacking 的机制原因，
   提出 min-form (PURE) 替代。
   → 这是本 proposal 核心理论基础之一。本 proposal 的增量是：在已知 WHY 
   (Stop Summation) 的基础上回答 WHEN/HOW（bifurcation dynamics）。

4. Wang et al. "TRACE" (ICLR 2026 Oral, arXiv:2510.01367): 
   通过 progressive CoT truncation 测量 reasoning effort 检测 reward hacking，
   F1≈0.97（数学任务）。
   → 这是本 proposal 自认的"strongest baseline"。TRACE 的极高检测性能是本
   proposal 面临的最大 trivial alternative 威胁。

5. Beigi et al. "IR³" (arXiv:2602.19416): 
   contrastive IRL + SAE 做 post-hoc interpretable reward hacking detection，
   0.89 correlation with ground-truth rewards。
   → post-hoc 方法，与本 proposal 的 training-time 定位有区分。

6. Hennick & Corlouer "From Density Matrices to Phase Transitions in Deep Learning" 
   (arXiv:2603.29805): 
   2RDM spectral analysis 检测 training phase transitions（能力涌现、grokking）。
   → 最近的概念邻居，但研究的是 beneficial transitions 而非 adversarial exploitation。

7. Miao et al. "Energy Loss" (ICML 2025, arXiv:2501.19358): 
   发现 energy loss 单调递增可作为 PPO-RLHF reward hacking 早期预警。
   → 更简单的标量 signal，不区分 regime。

8. Helff et al. (ICLR 2026 Workshop, arXiv:2604.15149), 
   Mahmoud et al. (arXiv:2605.12474), 
   rebound paper (arXiv:2604.01476), 
   Nimmaturi et al. (arXiv:2507.18014): 
   大量并行工作从不同角度刻画 reward hacking dynamics。
   → 这个领域在 2025-2026 年非常拥挤。

- 调研总结: Reward hacking / Goodhart's law in RL 是 2025-2026 年的热门方向，
  多条并行工作线正在快速推进（检测、机制分析、缓解策略）。本 proposal 
  试图占据一个特定 niche——bifurcation-theoretic prediction of PRM exploitation 
  onset in GRPO——这个精确交叉点目前确实没有直接竞争者，但周围的工作非常密集，
  留给额外 insight 的空间有限。

---

【Trivial Alternative 检验】:

存在严重的 trivial alternative 威胁：

1. **TRACE (F1≈0.97)**：proposal 自己承认这是最强 baseline。如果实际目标是
   "检测 reward hacking"，TRACE 已经在数学任务上达到极高性能。本 proposal 需要
   证明 bifurcation framework 在某个维度（lead time、false positive rate、
   mechanistic insight）上 strictly dominate TRACE，这并不容易。

2. **简单 divergence monitoring**：监控 proxy reward vs. ground-truth accuracy 
   的 gap，加上 changepoint detection (PELT/BOCPD)，是一个成本极低的 baseline。
   本 proposal 的大量理论推导最终可能只比"看 reward-accuracy gap 何时开始发散"
   早几个 checkpoint 发出预警——增量价值是否值得整个 bifurcation framework 
   的复杂度？

3. **PURE 直接解决问题**：如果 summation-form credit assignment 是 root cause
   （Stop Summation 已证明），直接换成 min-form (PURE) 就消除了 exploitation。
   那么"预测 exploitation onset"的实际应用场景到底是什么？谁会在明知 PURE 
   能消除问题的情况下，选择继续用 summation-form 然后依赖 bifurcation 
   early warning？

增量价值论证：proposal 试图定位为"理论理解 + 机制分析"而非纯实用工具，
但 bifurcation theory 的增量理解相对于 Stop Summation 已经给出的机制解释
（summation-form creates positive feedback）是否足够大？从 "positive feedback 
→ exploitation" 到 "positive feedback → fold bifurcation with -1/2 exponent" 
的增量，审稿人可能认为是 formalism for its own sake。

---

【前提假设检验】:

核心逻辑链中有多个未验证的关键假设：

1. **Normal form reduction 的合理性**（最关键）：proposal 承认 bifurcation 
   derivation 是 "phenomenological model (normal form reduction)"，不是从 GRPO 
   objective 严格推导的。从 "group-relative normalization creates positive 
   feedback" 到 "the dynamics can be reduced to dα/dt = λ - λ_c + (α - α_c)²" 
   的跳跃需要多个隐含假设：exploitation fraction α 是一个 well-defined 
   slow variable、高阶项可忽略、noise structure 不改变 bifurcation type 等。
   在有随机梯度、finite batch size、非线性 neural PRM 的实际训练中，这些假设
   很可能不成立。

2. **Scaling exponent 的可检测性**：fold bifurcation 预测 autocorrelation 
   diverges as |λ-λ_c|^{-1/2}。在实际训练中，(a) λ(t) 不是已知量，需要反推；
   (b) 数据点（checkpoints）有限（~100 per run）；(c) noise 可能掩盖 scaling 
   behavior。能否在 4-8 个 training run 中可靠地拟合 scaling exponent 并区分
   -1/2（fold）vs. -1（transcritical）是一个严肃的统计学问题。

3. **α(t) 的可操作性定义**："exploitation fraction" 在理论中是一个干净的量，
   但在实际 LLM 生成的数学解题中，如何 operationalize "什么是 exploitative 
   strategy" 本身就是一个 non-trivial 问题（Tiwari et al. 的 taxonomy 提供
   了部分方案，但远非完美分类器）。

4. **Dual-PRM interaction 的可测性**：P5 预测 λ-GRPO 应该通过减弱 implicit 
   PRM 的贡献来 raise λ_c。但区分 "λ_c shifted" vs. "training dynamics 
   simply changed due to loss function modification" 需要极精细的实验设计，
   而 proposal 只有 1 个 λ-GRPO run。

---

【3 维度打分】:

1. Novelty: 【中】
   理由：精确交叉点（bifurcation theory + GRPO credit assignment + PRM exploitation）
   确实没有直接先驱。但 novelty 的实质深度有限：
   - Stop Summation (NeurIPS 2025) 已经识别 summation-form 的 positive feedback 
     是 root cause
   - Karwowski et al. (ICLR 2024) 已经形式化 Goodhart's law in RL
   - 本 proposal 的增量是将已知的 positive feedback mechanism 用 bifurcation 
     normal form 语言重新表达，并推导 scaling exponent predictions
   - 这更接近"用新的数学语言重新描述已知现象 + 推导 quantitative predictions"
     而非"发现新现象或新机制"
   - Hennick & Corlouer (arXiv:2603.29805) 已经将 phase transition / critical 
     transitions 工具引入 training dynamics 分析
   - 审稿人可能认为 fold bifurcation 框架是 "formalism premium" 大于 
     "insight premium"

2. Significance: 【中】
   理由：
   - 研究问题本身（理解和预测 reward hacking dynamics）确实重要，尤其在 
     LLM alignment context 下
   - 但实际影响力受限于：(a) PURE 已经提供了 root cause fix，减少了 prediction 
     的应用价值；(b) TRACE 已经提供了极高性能的检测，减少了 monitoring 的应用
     价值；(c) 理论贡献是 phenomenological 而非 rigorous，限制了理论影响力
   - 如果核心发现是 positive（scaling exponent 确实是 -1/2），审稿人更可能说 
     "interesting confirmation of what we'd expect from the positive feedback 
     structure" 而非 "surprising"
   - 如果核心发现是 negative（exponent 不是 -1/2），这确实 informative，但
     paper 的 framing 会变得尴尬
   - 整体定位是"对已知现象的更精确定量刻画"，这是有价值的但不是高影响力的

3. Related Work: 【强】
   理由：
   - 这是 proposal 最突出的优点。覆盖了 6 个 category、30+ 篇参考文献，
     包括所有关键的并行工作
   - 对每篇工作的定位清晰，差异化论述具体（dynamics-based vs. effort-based 
     vs. representation-based vs. gradient-based）
   - 对 Karwowski et al.、Sullivan et al.、Stop Summation、TRACE 等核心
     参考的引用和描述经验证均准确
   - 但极其详尽的 related work 也反映出这个空间已经非常拥挤

---

【概率估计】: 

对 CoRL 2026: 0% — 会被 desk-reject，不进入评审
（CoRL 明确要求 robotics focus，本 proposal 无任何 robotics 内容）

对合适的 ML 顶会 (NeurIPS/ICML/ICLR): [20% - 30%] 中位 25%

【估计理由】: 
Novelty 和 Significance 均为"中"，限制了上界。核心问题是：

(1) Novelty 的 incremental nature——从 "Stop Summation 已知 positive feedback 
是 root cause" 到 "用 fold bifurcation normal form 重新描述并推导 scaling 
exponent"，增量实质偏窄。审稿人会问 "beyond formalism, what new insight does 
the bifurcation framework give us that we didn't already know from Stop Summation?"

(2) Trivial alternative 威胁严重——TRACE (F1≈0.97) 和 PURE (消除 root cause) 
的存在削弱了 practical motivation；简单 divergence monitoring + changepoint 
detection 可能在 lead time 上与 bifurcation framework 差别不大。

(3) 前提假设风险——phenomenological model 的 scaling predictions 在实际训练中
可能不可靠地检测到，导致核心实验 claim 无法 convincingly validate。

Related Work 的强项提供了 solid 的 positioning 但不能弥补 idea 内核的局限。
上界被 Novelty 限制（不是 "surprising" 级别的发现），下界由 Related Work 
的质量和研究问题的时效性托住。

【主要风险】: 
1. **Venue mismatch（对 CoRL 致命）**：proposal 无任何 robotics 内容，CoRL 
   明确声明 "submissions without a robotics focus will be returned without 
   review"。若不更换投稿目标，概率为 0%。

2. **Formalism-over-insight 质疑（对任何 venue）**：审稿人最可能的攻击角度是
   "the bifurcation framework re-describes the already-known positive feedback 
   mechanism (Stop Summation) in dynamical systems language without yielding 
   actionable new insights, especially given that PURE already eliminates the 
   root cause and TRACE already detects it with F1≈0.97."
```

---

**总结**：这个 proposal 的 **idea 质量在中等水平**（novelty 和 significance 均为中），有一个非常扎实的 related work coverage，但核心增量（bifurcation formalism on top of already-known mechanisms）偏窄，且面临 TRACE/PURE 两个方向的 trivial alternative 夹击。

然而，**最致命的问题是投稿目标选择**：CoRL 是 Conference on Robot Learning，明确要求论文聚焦机器人问题，无机器人内容的投稿将被退回不审。本 proposal 应改投 NeurIPS / ICML / ICLR 等 ML 顶会。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [Wang et al. - TRACE: Detecting Implicit Reward Hacking (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Cheng et al. - Stop Summation / PURE (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Beigi et al. - IR³ (arXiv:2602.19416)](https://arxiv.org/abs/2602.19416)
- [Hennick & Corlouer - Phase Transitions in Deep Learning](https://arxiv.org/abs/2603.29805)
- [Miao et al. - Energy Loss (ICML 2025)](https://arxiv.org/abs/2501.19358)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information from the field research. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命问题：venue mismatch】
本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。但 proposal 内容为 LLM 数学推理训练中的 PRM exploitation/reward hacking 检测——与机器人学习零相关。CoRL 明确要求论文 "focus on a core robotics problem" 并 "demonstrate the relevance to robotics, with real-robot experiments or convincing simulation evidence." 本文无任何 robotics 内容，会被 desk reject。
如果投稿目标实为 NeurIPS/ICML/ICLR 等 ML 主会，以下评估按 ML 主会标准给出；如确实投 CoRL，中稿概率为 ~0%。

【领域调研】:
- Karwowski et al. "Goodhart's Law in Reinforcement Learning" (ICLR 2024): 提出 occupancy polytope 上的 Goodhart 几何形式化，推导最优 early stopping 及 regret bound。局限于 tabular MDP + 线性 reward，未涉及 neural PRM 或 GRPO。Proposal 声称对该工作的扩展基本准确。
- Sullivan et al. "GRPO is Secretly a Process Reward Model" (arXiv:2509.21154, under review ICML 2026): 证明 GRPO + ORM 等价于隐式 Monte-Carlo PRM 目标，提出 λ-GRPO。Proposal 对其引用和描述准确。
- Cheng et al. "Stop Summation: Min-Form Credit Assignment Is All PRM Needs" (NeurIPS 2025): 定位 summation-form credit assignment 为 PRM hacking 根因，提出 PURE (min-form)。Proposal 引用准确，且确实是本文理论的关键前提。
- Wang et al. "TRACE" (ICLR 2026 Oral): 通过渐进式 CoT 截断测量 reasoning effort，F1≈0.97 检测 implicit reward hacking。Proposal 将其作为最强 baseline，描述准确。
- Miao et al. "Energy Loss Phenomenon in RLHF" (ICML 2025): 发现 RLHF 中 energy loss 单调递增与 reward hacking 相关，提出 EPPO。Proposal 引用准确。
- Beigi et al. "IR³" (arXiv:2602.19416): contrastive IRL + SAE 的 post-hoc reward hacking 检测，0.89 correlation with ground-truth。Proposal 引用准确。
- Hennick & Corlouer "From Density Matrices to Phase Transitions" (arXiv:2603.29805): 2RDM spectral analysis 检测训练 phase transitions。目前唯一将 critical transition 理论应用到 DL 训练动力学的工作，但研究的是 capability emergence/grokking，非 adversarial exploitation。
- Mahmoud et al. "Reward Hacking in Rubric-Based RL" (arXiv:2605.12474): rubric verifier 下的单调 exploitation 增长。
- Helff et al. (ICLR 2026 Workshop): progressive shortcut growth with task complexity。
- 未找到任何直接将 bifurcation theory 应用于 reward hacking 预测的先前工作。

- 调研总结: Reward hacking 检测/缓解是 2025-2026 的热门方向，已有多条 orthogonal 路线（effort-based/TRACE, representation-based/energy loss/SAE, scaling law, gradient fingerprint）。Bifurcation-theoretic framing 尚无人做，但 Stop Summation 已定位了 mechanism，TRACE 已达 F1≈0.97 的检测性能。Proposal 的位置是在已知 mechanism 上叠加动力学系统理论框架。

【Trivial Alternative 检验】:
存在严重的 trivial alternative 威胁：
1. **TRACE (F1≈0.97)** 已经是极强的 hacking detector，proposal 自己承认这是最强 baseline。即使 bifurcation framework 能提供"更早"的 warning，其增量价值取决于 lead time 差异——这是一个 empirical question，且 lead time 优势可能很小。
2. **简单 proxy-true divergence monitoring**：监控 PRM score 与 ground-truth accuracy 的 divergence rate 是最朴素的方法。Proposal 需要证明 fold-specific scaling exponent 比 naive divergence threshold 有显著优势。
3. **Stop Summation 已给出 mechanism + fix (PURE)**：如果已经知道 summation-form 是 root cause，直接使用 min-form 就能消除 hacking。Bifurcation framework 的"预测何时发生"在"已知如何避免"的前提下，实用价值被削弱。
增量价值声称：(a) 比 simpler methods 更早检测, (b) 区分 bifurcation type 减少 false positive, (c) SAE 提供 mechanistic interpretability, (d) regime identification 指导 intervention selection, (e) 定量预测 onset timing via λ_c 估计。但 (a)(b)(e) 都是 empirical claims，非 idea-level guarantees；(c) 是 engineering contribution；(d) 有一定理论价值但取决于 framework 是否 predictive。

【前提假设检验】:
核心逻辑链有 3 个关键假设经不起严格推敲：
1. **Fold bifurcation 是 phenomenological fitting，非 rigorous derivation**：Proposal 自己承认这是 "phenomenological model (normal form reduction)" 而非从 GRPO objective 严格推导。将观察到的 "tipping point" 行为套入 fold normal form f(α;λ) = λ - λ_c + (α - α_c)² 是 curve fitting，不是 theory。关键问题：任何具有 positive feedback 的 transition 都可以被 phenomenologically 描述为 fold bifurcation——这不是 PRM-specific insight，而是 bifurcation theory 的 generic property。
2. **Scaling exponent 可测性假设**：P1/P2 要求测量 τ_ac ~ |λ(t) - λ_c|^{-1/2} 的 scaling exponent。在 noisy、finite-sample 的 RL training 中，精确区分 exponent 1/2（fold）和 exponent 1（transcritical）极其困难。如果 noise 太大无法区分，核心 theoretical prediction 就不可测。
3. **Positive feedback 唯一来源假设**：Framework 假设 group-relative normalization 是 positive feedback 的核心来源。但 RL training 中有多种其他 positive feedback（policy collapse, mode collapse, temperature dynamics），将 fold 归因于单一机制是 oversimplification。

【3 维度打分】:

1. Novelty: 弱-中 — 
   理由：(a) 将 bifurcation theory 应用到 reward hacking 预测确实无人做过（调研中未找到直接先例），这是形式上的 novelty。(b) 但核心 insight——"summation-form GRPO 中 exploitation 存在正反馈导致的 tipping point"——本质上已被 Stop Summation (NeurIPS 2025) 和 Helff et al. (ICLR 2026 Workshop) 从 empirical 角度描述。Proposal 的贡献是用 bifurcation 语言重新表述已知现象。(c) Fold bifurcation derivation 是 phenomenological fitting，任何正反馈系统都能这样 fit——这不是 PRM-specific 或 GRPO-specific theory。(d) Dual-PRM interaction (P5) 是最有原创性的部分，但也最 speculative。(e) 与 Hennick & Corlouer 将 critical transition theory 应用到 training dynamics 的工作有 conceptual overlap，虽然 domain 不同。综合来看，novelty 在"新 framing applied to known problem"水平，而非"new insight"水平。

2. Significance: 中 — 
   理由：(a) 预测 reward hacking onset 是 genuinely important 的问题，在 LLM alignment 和 safety 社区有高关注度。(b) 但 practical significance 被 TRACE (F1≈0.97) 和 PURE (直接消除 hacking) 的存在削弱——如果已有 excellent detector 和 known fix，"另一种 detection framework"的边际价值下降。(c) 若 bifurcation framework 确实能 predict（而非 detect）onset，且 prediction 足够 early 以 enable preemptive intervention，这有独立价值——但这是 empirical promise，非 guaranteed。(d) 对领域的 conceptual contribution 是将 dynamical systems 工具引入 reward hacking 分析，有一定范式创新意义，但实际 usefulness 取决于 empirical validation。(e) 研究问题的定位是"when and how"而非"why"（Stop Summation 已回答 why）或"how to fix"（PURE 已回答），这个定位有价值但不是最高优先级。

3. Related Work: 强 — 
   理由：Proposal 对已有工作的覆盖异常全面。6 类文献梳理（Goodhart formalization, GRPO-specific, PRM-specific, detection methods, representation monitoring, statistical diagnostics）完整且准确。关键论文的引用和描述经调研验证准确（Karwowski ICLR'24, Sullivan arXiv:2509.21154, Stop Summation NeurIPS'25, TRACE ICLR'26 Oral, IR³, Energy Loss ICML'25）。差异化定位清晰——proposal 明确标注了与每个 prior work 的区别（e.g., Karwowski: linear reward → neural PRM; TRACE: sample-level → population-level temporal dynamics; IR³: post-hoc → training-time）。唯一的轻微不足：未覆盖 Scheffer et al. (Nature 2009) 之后 ecology/climate 领域 early warning signals 的 false positive 问题文献（该领域已有大量关于 EWS 可靠性的批判性工作）。

【概率估计】: [18% - 30%] 中位 23%
（注：此概率基于投稿 NeurIPS/ICML/ICLR 等 ML 主会。若确投 CoRL，概率 ≈ 0%，因 scope 完全不匹配。）

【估计理由】: 
- Related Work 维度强，说明作者对领域把握扎实，这提供了下限保障（不会因为 miss related work 被拒）。
- Novelty 维度是主要瓶颈：核心贡献是将已知现象（summation-form → exploitation tipping point）用 bifurcation 语言重新表述，且 derivation 是 phenomenological fitting 而非 rigorous theory。审稿人可能评价为 "reformulation, not new insight"。
- Significance 被 TRACE 和 PURE 的存在压缩：如果已有 F1≈0.97 的 detector 和已知 fix，新 framework 的 marginal value 需要靠 empirical lead time advantage 来支撑——这是 empirical gamble。
- Proposal 形式极其完善（3-tier experiment design, 6 baselines, dual-outcome, explicit limitations），这保证了执行质量下限，但不改变 idea 内核的评估。
- 上界受限于 Novelty（"弱-中"）和 trivial alternative 威胁。审稿人看到 TRACE F1≈0.97 会问："为什么我需要一个复杂的 bifurcation framework？"如果 empirical results 不能给出 convincing 回答，概率落入下界附近。
- 若 empirical results 确实展示出 (a) fold-specific scaling exponent 可测且 (b) 比 TRACE 有显著 lead time 优势，概率可推至上界附近。

【主要风险】:
1. **"Reformulation, not new insight" 拒稿理由**：审稿人可能认为将 Stop Summation 已定位的 mechanism 套入 fold bifurcation normal form 是 mathematical dressing，而非 genuine theoretical contribution。Phenomenological fitting 的 unfalsifiability（如果不是 fold 就换另一种 bifurcation type）进一步削弱理论 claim 的 sharpness。
2. **Trivial alternative 压制**：TRACE (F1≈0.97) + PURE (eliminate hacking) 的组合使得"另一种 detection framework"的 practical motivation 被严重削弱。审稿人会问 "given TRACE and PURE exist, who is the user of this framework, and what decision would they make differently?"
```

**补充说明（venue 问题）**：

这是我在评估中发现的**最严重问题**。CoRL 2026 的 Call for Papers 明确要求论文围绕"core robotics problem"展开，鼓励"real-robot experiments or convincing simulation evidence"。本 proposal 的全部内容——PRM exploitation、GRPO 训练动力学、数学推理 benchmark——与机器人学习**毫无交集**。即使 idea 本身有价值，投 CoRL 会被直接 desk reject。

如果作者实际想投的是 NeurIPS 2026 / ICML 2026 / ICLR 2027 等 ML 主会，上述概率估计（18%-30%，中位 23%）适用。**请确认投稿目标是否正确。**

Sources:
- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [Cheng et al. - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Wang et al. - TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Miao et al. - Energy Loss Phenomenon (ICML 2025)](https://arxiv.org/abs/2501.19358)
- [Beigi et al. - IR³](https://arxiv.org/abs/2602.19416)
- [Hennick & Corlouer - Density Matrices to Phase Transitions](https://arxiv.org/abs/2603.29805)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Goodhart's Tipping Point: Fold Bifurcations and Early Warning Signals in PRM Exploitation During GRPO Training

## Description
We develop the first bifurcation-theoretic framework for predicting PRM exploitation onset during GRPO training, deriving that summation-form credit assignment creates a fold (saddle-node) bifurcation in the exploitation fraction through a positive feedback loop unique to group-relative advantage normalization. Building on Karwowski et al.'s (ICLR 2024) geometric Goodhart framework and extending it to neural PRMs with step-level credit assignment, we derive five PRM-specific testable predictions: fold-specific autocorrelation scaling (exponent -1/2), variance amplification with fold exponent, solution-length-dependent onset timing, elimination of the fold under min-form credit (PURE), and dual-PRM interaction signatures where GRPO's implicit Monte-Carlo PRM (Sullivan et al., arXiv:2509.21154) modulates exploitation onset timing. Experiments span three priority tiers: Tier 1 trains Qwen3-4B via GRPO with three PRMs (discriminative and generative) plus Qwen3-14B, with a multi-signal diagnostic panel at dense checkpoints; Tier 2 adds λ-GRPO and PURE ablations to test bifurcation modulation predictions, completes 14B cross-PRM comparison, and adds GRIFT baseline; Tier 3 extends to PPO and spectral analysis. We rigorously ablate against six baselines spanning four detection paradigms: dynamics-based (self-internalization gap, divergence rate, scaling law deviation), effort-based (TRACE, adapted from Wang et al.'s ICLR 2026 Oral with F1≈0.97), representation-based (energy loss), and gradient-based (GRIFT). The framework explicitly addresses the dual-PRM dynamic in GRPO + explicit PRM, where the explicit PRM determines trajectory-level advantage while the implicit MC-PRM distributes learning across tokens. We compare exploitation bifurcation characteristics across discriminative vs. generative PRMs and position against complementary approaches: IR³'s post-hoc SAE-based detection, CRA's PRM deconfounding, and InfoRM's IB-based monitoring.

## Core Problem
PRM exploitation during RL training can silently render training counterproductive (>0.9 reward, <4% accuracy), but we lack both a domain-specific theoretical framework predicting exploitation onset and practical early-detection tools that outperform simpler baselines. Karwowski et al. (ICLR 2024) formalize Goodhart's law geometrically in MDPs via occupancy polytope boundary transitions, deriving optimal early stopping with regret bounds — but their framework assumes linear rewards on occupancy measures and does not address neural process reward models, step-level credit assignment, or the dual-PRM dynamics inherent to GRPO. Sullivan et al. (arXiv:2509.21154) prove that GRPO with an ORM is equivalent to a PRM-aware objective with an implicit Monte-Carlo PRM, meaning GRPO + explicit PRM creates a dual-PRM optimization dynamic not previously analyzed for exploitation. Stop Summation identifies summation-form credit assignment as the mechanistic driver of PRM hacking. Current work characterizes the end state (Tiwari et al., 43% shortcuts), the mechanism (Stop Summation), temporal dynamics under rubric verifiers (Mahmoud et al.), structural phase transitions in capability emergence (Hennick & Corlouer), static PRM deconfounding (CRA), scalar early warning in preference-RLHF (Energy Loss), effort-based hacking detection (TRACE, F1≈0.97), and post-hoc interpretable detection (IR³, SAE-based) — but no work unifies bifurcation-theoretic prediction with mechanistic monitoring for PRM exploitation in GRPO, where the interaction between implicit and explicit process reward structures introduces qualitatively distinct exploitation dynamics.

## Opportunity
Five converging threads create a unique opportunity. First, Sullivan et al. (arXiv:2509.21154) prove GRPO implicitly implements a Monte-Carlo PRM through trajectory prefix sharing, and propose λ-GRPO to fix step-level imbalance — this reveals that GRPO + explicit PRM creates a dual-PRM optimization dynamic where the explicit PRM determines which trajectories are favored while the implicit PRM distributes advantage across tokens, an interaction whose exploitation characteristics are completely uncharted. Second, concurrent empirical work maps complementary facets of reward hacking — Mahmoud et al. (arXiv:2605.12474) show monotonic exploitation growth under weak rubric verifiers, the rebound paper (arXiv:2604.01476) finds three-phase dynamics in code evaluation, Nimmaturi et al. (arXiv:2507.18014) identify exponential saturation in GRPO, and Helff et al. (arXiv:2604.15149) show progressive shortcut growth with task complexity — but none study PRM-guided math reasoning where Stop Summation has identified summation-form credit assignment as the mechanism. Third, Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational Goodhart formalization in RL — geometric explanations via occupancy polytope boundaries and optimal early stopping with regret bounds — but their linear-reward framework does not extend to neural process rewards, step-level credit assignment, or the group-relative normalization in GRPO that creates positive feedback loops driving exploitation. Critical transitions theory (Scheffer et al., Nature 2009) and its recent application to training phase transitions (Hennick & Corlouer, arXiv:2603.29805) provide the dynamical systems tools, but the theoretical gap is precisely connecting GRPO's credit assignment mechanisms to specific bifurcation types with quantitative scaling predictions — not merely applying generic early warning signals to a new domain. Fourth, detection methods are maturing along multiple orthogonal axes — TRACE (arXiv:2510.01367, ICLR 2026 Oral) detects hacking via reasoning effort measurement (CoT truncation AUC) with F1≈0.97, GRIFT uses gradient fingerprints, IR³ (arXiv:2602.19416) combines contrastive IRL with SAEs for 0.89 correlation with ground-truth rewards, energy loss provides a scalar signal, and SAEs detect RL pathologies — but none predict exploitation onset from training dynamics as a bifurcation phenomenon, and no work systematically compares these orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based) against each other. Fifth, GenPRM and TP-GRPO reveal distinct exploitation profiles for generative PRMs, creating an unexplored axis for comparing bifurcation characteristics across PRM paradigms. Bridging Karwowski's geometric Goodhart framework with bifurcation theory specific to GRPO's credit assignment mechanisms offers a formal model generating quantitative predictions — but the bar is high: we must show the framework adds value beyond simpler baselines including TRACE, self-internalization gap, energy loss, scaling law fitting, and gradient fingerprints.

## Related Work / Landscape
The landscape spans six categories requiring explicit positioning: (A) Goodhart formalization and training dynamics, (B) GRPO-specific analysis, (C) PRM-specific analysis, (D) detection methods, (E) representation-level monitoring, and (F) statistical/information-theoretic diagnostics.

**A. Goodhart Formalization and Training Dynamics.** Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational formalization of Goodhart's law in RL: they model policy optimization as steepest ascent on the occupancy measure polytope Ω, show that the projected angle between proxy and true rewards determines Goodharting likelihood (Proposition 3: directional alignment is monotonically decreasing), derive an optimal early stopping criterion with regret bound proportional to diameter(Ω)·(1-cos(θ)), and demonstrate Goodharting in 19.3% of 30,400 configurations. Their framework is foundational to our work but operates in the tabular MDP setting with linear reward functions on occupancy measures — it does not address (a) neural process reward models where the proxy is a learned nonlinear function, (b) step-level credit assignment where summation vs. min forms create qualitatively different optimization landscapes, (c) group-relative normalization in GRPO that introduces positive feedback absent from steepest ascent, or (d) the dual-PRM dynamics of GRPO + explicit PRM. Our theoretical contribution extends their geometric insight to the PRM-guided GRPO setting by deriving the specific bifurcation structure (fold bifurcation) that arises from the positive feedback between group-relative normalization and exploitation discovery, yielding quantitative scaling predictions absent from their framework. Hennick & Corlouer (arXiv:2603.29805) apply 2RDM spectral analysis to detect training phase transitions (capability emergence, grokking) — the closest conceptual neighbor for dynamics-based training monitoring, but they study beneficial reorganization rather than adversarial exploitation. Miao et al. (arXiv:2501.19358, ICML 2025) identify energy loss (ΔE_l = ||h^in_l||_1 − ||h^out_l||_1) as a monotonically increasing early warning for reward hacking in PPO-based RLHF — a single scalar signal without regime discrimination or mechanistic interpretability, operating in the preference RLHF setting rather than PRM-guided GRPO. Helff et al. (arXiv:2604.15149, ICLR 2026 Workshop) show progressive shortcut growth with task complexity, reinforcing the importance of characterizing transition type (sharp vs. gradual).

**B. GRPO-Specific Analysis.** Sullivan et al. (arXiv:2509.21154, under review ICML 2026) prove that GRPO with an ORM is equivalent to a PRM-aware RL objective with an implicit Monte-Carlo PRM — for each token, the implicit step-level reward equals the mean outcome reward of trajectories sharing the same prefix up to that token. They identify that non-uniform process set distributions hinder exploration/exploitation and propose λ-GRPO, which normalizes each token's loss by its process set size |λ^{(i,t)}|, achieving >10% average accuracy improvement and 2× convergence speedup on Qwen-1.5B. Crucially for our work: when GRPO uses explicit PRM scores as trajectory rewards (as in our setup and Stop Summation's), the optimization involves BOTH the explicit PRM (determining trajectory-level advantage via group-relative normalization of PRM scores) AND the implicit MC-PRM (distributing that advantage across tokens through prefix sharing). This dual-PRM dynamic could qualitatively alter exploitation: the explicit PRM determines WHICH strategies are favored, while the implicit PRM determines HOW learning is distributed across solution steps. λ-GRPO normalizes the implicit PRM's contribution but does not affect the explicit PRM's trajectory-level signal — a distinction we test experimentally. Nimmaturi et al. (arXiv:2507.18014) derive GRPO scaling laws with exponential saturation — we incorporate as a null model.

**C. PRM-Specific Analysis.** Cheng et al. (arXiv:2504.15275, NeurIPS 2025) identify summation-form credit assignment as the mechanistic cause of PRM hacking in GRPO and propose min-form (PURE). Their work answers WHY exploitation happens; ours answers WHEN and HOW — and we formally derive that summation-form creates a fold bifurcation while min-form eliminates it. Song et al. (arXiv:2508.04216, AAAI 2026 Workshop) train SAEs on PRM activations for static deconfounding at inference time — complementary to our policy-model dynamics monitoring. Tiwari et al. (arXiv:2603.06621) characterize the end state. TP-GRPO (OpenReview:LZZENDlZt9) addresses GenPRM-specific pitfalls.

**D. Detection Methods.** Wang et al. (arXiv:2510.01367, ICLR 2026 Oral, TRACE) detect implicit reward hacking by measuring reasoning effort via progressive CoT truncation, achieving F1≈0.97 in math on dataset-level loopholes. TRACE operates on a fundamentally different principle from our framework: it measures per-sample reasoning effort (whether the model 'knows the answer' early in its CoT) via truncation AUC, while we monitor population-level temporal dynamics across training checkpoints. TRACE is an excellent sample-level detector but does not predict exploitation onset, characterize bifurcation type, or identify what the model exploits mechanistically. We include TRACE as a key ablation baseline — a particularly strong comparison because its high F1 sets a demanding bar for alternative approaches. It was validated with RLOO and GRPO under outcome-based rewards, not PRM-guided RL; we adapt it to our setting. Beigi et al. (arXiv:2602.19416, IR³) combine contrastive inverse RL with SAEs for interpretable post-hoc reward hacking detection, achieving 0.89 correlation with ground-truth rewards and >90% precision in identifying hacking features. IR³ operates post-hoc (requiring sampling access to aligned and baseline policies after training) rather than during training — directly relevant to our SAE approach but not a training-time baseline. Their SAE decomposition of reconstructed rewards (R̂ = Σω_i f_i + c) provides complementary evidence that SAE features can identify hacking signatures, validating our choice of SAE-based monitoring. Key distinction: IR³ reconstructs the implicit reward function from behavioral contrasts, while we track the policy's evolving representations to predict exploitation before it manifests behaviorally. Wang et al. (arXiv:2604.16242, GRIFT) use gradient fingerprints for post-hoc sample-level detection. Mahmoud et al. (arXiv:2605.12474) propose the self-internalization gap for rubric-based RL.

**E. Representation-Level Monitoring.** Yan et al. (arXiv:2602.05183) use SAEs for Diplomacy RL dynamics. Shi et al. (arXiv:2507.00665, SAFER) probe reward model safety via SAE activation differences. Song et al.'s CRA uses SAEs on PRM activations for static deconfounding — distinct from our policy-model tracking.

**F. Statistical and Information-Theoretic Diagnostics.** Miao et al. (arXiv:2402.09345, NeurIPS 2024, InfoRM) propose MOP/CSI/ICDS metrics in the IB latent space for reward-model-side overoptimization detection — complementary to our policy-side monitoring. Gao et al. (arXiv:2210.10760) provide overoptimization scaling laws for best-of-N/PPO.

The gap: a bifurcation-theoretic framework deriving specific predictions from GRPO's credit assignment mechanisms (not generic early warning signals), validated against strong baselines (TRACE, self-internalization gap, energy loss, scaling law deviation, gradient fingerprints), with explicit treatment of the dual-PRM dynamics in GRPO + explicit PRM, and systematic comparison across discriminative and generative PRMs.

## Approach
We develop and empirically validate a bifurcation-theoretic framework for PRM exploitation during GRPO training, deriving PRM-specific predictions from the credit assignment mechanism and rigorously comparing against six detection baselines. Experiments are organized into three priority tiers.

**Tiered Experiment Design.**
- *Tier 1 (Essential — publishable core, ~55% of compute):* Qwen3-4B via GRPO with all 3 PRMs (Qwen2.5-Math-PRM-7B, ACTPRM-X, GenPRM-7B) on MATH/AMC/AIME datasets, plus Qwen3-14B via GRPO with Qwen2.5-Math-PRM-7B. Full diagnostic panel and all baseline comparisons at each checkpoint. This yields 4 training runs covering both model scales, all three PRMs, and the complete analytical framework. (4 runs × ~4h avg = ~16h training + ~90h evaluation/SAE/TRACE/analysis)
- *Tier 2 (Important — strengthens contribution, ~30% of compute):* Qwen3-14B via GRPO with ACTPRM-X and GenPRM-7B (completing cross-PRM comparison at 14B), PURE ablation (min-form) on Qwen3-4B with Qwen2.5-Math-PRM-7B, λ-GRPO ablation (Sullivan et al.'s process-set normalization) on Qwen3-4B with Qwen2.5-Math-PRM-7B, and GRIFT-style gradient fingerprint baseline on sampled checkpoints. (4 runs × ~5h avg = ~20h training + ~60h analysis)
- *Tier 3 (Stretch — extends scope, ~15% of compute):* PPO pilot (Qwen3-4B + Qwen2.5-Math-PRM-7B) for cross-algorithm generalization, spectral heat capacity signal (following Hennick & Corlouer), and energy loss monitoring extension to step-level rewards. (~1 run + specialized analysis, ~30h total)

All experiments use the OpenRLHF framework. Tier 1 is prioritized for completion by week 10; Tier 2 by week 14; Tier 3 as time permits.

**Dual-PRM Experimental Setup.** We explicitly address the dual-PRM dynamic revealed by Sullivan et al. In our setup, PRM scores are the sole trajectory-level reward signal in GRPO — the explicit PRM evaluates each solution step and scores are aggregated (via summation, min, or mean) into a trajectory reward, which is then normalized via group-relative advantage computation. Crucially, GRPO's implicit Monte-Carlo PRM (Sullivan et al.) operates simultaneously at the token level: tokens sharing prefixes across trajectories within a group receive implicit step-level advantages equal to the mean trajectory reward of completions sharing that prefix. Thus, the policy is optimized against BOTH the explicit PRM (trajectory-level: which solutions are favored) AND the implicit MC-PRM (token-level: how advantage is distributed across solution steps). We hypothesize three distinct exploitation interaction modes: (1) constructive — both PRMs agree on step quality, accelerating aligned learning; (2) amplifying — the implicit PRM concentrates learning on tokens where the explicit PRM is most exploitable, accelerating exploitation onset; (3) buffering — the implicit PRM's averaging smooths out the explicit PRM's exploitable local maxima, delaying exploitation. Testing which mode dominates and whether it changes across training is a core empirical question. The λ-GRPO condition (Tier 2) isolates this: by normalizing process set sizes, λ-GRPO equalizes the implicit PRM's contribution, allowing us to test whether the dual-PRM interaction amplifies or buffers exploitation.

**Checkpoint Strategy and Storage.** We save checkpoints every 5 training steps across 500+ steps (~100+ checkpoints per run). Tiered strategy: full checkpoints every 25 steps, delta-compressed at intermediate 5-step intervals (3–4× compression), and online computation of diagnostics during training. Storage: ~8–12TB. Prune to anomaly-adjacent windows after analysis.

**Multi-Signal Diagnostic Panel.** At each checkpoint: PRM reward, ground-truth accuracy via outcome verification, solution style decomposition (Tiwari et al.'s taxonomy), PRM-adapted self-internalization gap, energy loss (ΔE = ||h^in||_1 − ||h^out||_1), TRACE score (adapted to PRM setting, computed on a held-out evaluation set), SAE features from residual stream activations, and optionally (Tier 3) spectral heat capacity.

**TRACE Adaptation for PRM-Guided RL.** TRACE (Wang et al., ICLR 2026 Oral) measures reasoning effort by progressively truncating CoT at percentages p ∈ {10%, 20%, ..., 100%}, forcing early answers, and computing AUC of expected reward vs. truncation fraction. Originally validated with outcome-based rewards in RLOO/GRPO, we adapt it to PRM-guided RL: at each checkpoint, we evaluate the held-out set by truncating solutions at each percentage, computing the PRM score on the truncated solution (using the PRM's step-level scores up to the truncation point), and calculating the TRACE-PRM score as the AUC. High TRACE-PRM scores indicate the model achieves high PRM scores with minimal reasoning effort — a signature of PRM exploitation. We validate this adaptation by confirming correlation between TRACE-PRM scores and ground-truth accuracy degradation.

**Self-Internalization Gap: PRM Adaptation.** We construct two evaluation contexts: (1) PRM-verification-conditioned — math problem augmented with system prompt encoding step-level correctness criteria ('Ensure each reasoning step is mathematically correct and logically follows from previous steps. Verify intermediate results.'), with richer conditioning for GenPRM matching its reasoning format; (2) Prompt-only — minimal instruction. At each checkpoint, sample K=10 solutions from conditioned distribution, compute length-normalized log-probabilities under both contexts. The PRM-adapted self-internalization gap Δ_PRM(t) = mean difference. Validate by confirming r>0.85 correlation with accuracy trajectories.

**SAE Training Strategy.** Anchor-and-monitor: train a single TopK-SAE (32K hidden dims, K=32) on pooled residual stream activations from checkpoints at steps 0, 25, 50, 100. Apply across subsequent checkpoints; fine-tune when reconstruction loss exceeds 2× baseline mean. Distinction from IR³ (Beigi et al.): IR³ reconstructs implicit reward functions from behavioral contrasts post-hoc, while we track policy representation evolution during training. Distinction from CRA (Song et al.): CRA trains SAEs on PRM activations for static deconfounding; we train on policy model activations for dynamics monitoring. Estimated: ~40h anchor training + ~30h fine-tuning/extraction.

**Theoretical Framework: Fold Bifurcation in PRM Exploitation.**

Our core theoretical contribution goes beyond applying generic early warning signals to a new domain. We derive the specific bifurcation structure arising from GRPO's credit assignment mechanism, building on and extending Karwowski et al.'s geometric Goodhart framework.

*Setup.* Consider GRPO training with explicit PRM providing step-level scores s_1, ..., s_T. Under summation-form credit assignment, the trajectory reward is R = Σ_t s_t. Define α(t) ∈ [0,1] as the exploitation fraction — the probability mass the policy assigns to PRM-exploitative strategies at training step t. Let Δs = E[s_E] - E[s_G] > 0 be the per-step PRM score gap between exploitative (s_E) and genuine (s_G) strategies (positive by assumption that the PRM is imperfect).

*Positive feedback mechanism.* GRPO's group-relative normalization computes advantages A_i = (R_i - μ_G)/σ_G where μ_G and σ_G are group mean and std. As α increases, more trajectories in each group use exploitative strategies, raising μ_G. This makes genuinely correct trajectories (with lower R) receive increasingly negative advantage, suppressing them and further increasing α. This is a positive feedback loop absent from Karwowski et al.'s steepest-ascent framework (which involves no group normalization) and absent from standard RL settings without group-relative advantage.

*Fold bifurcation derivation.* We model the exploitation fraction dynamics as: dα/dt = f(α; λ(t)) where λ(t) is the effective optimization pressure (monotonically increasing with training). The positive feedback creates a cubic nonlinearity: f(α; λ) = λ - λ_c + (α - α_c)² + h.o.t., which is the normal form of a fold (saddle-node) bifurcation. Below the critical pressure λ_c, there exist two equilibria: a stable low-exploitation equilibrium and an unstable threshold. At λ = λ_c, these equilibria collide and annihilate — the system transitions to the high-exploitation regime. The critical pressure λ_c depends on: (i) the per-step PRM score gap Δs, (ii) solution length T (longer solutions → lower λ_c under summation-form because R = T·Δs), (iii) group size (larger groups → sharper normalization → stronger positive feedback → lower λ_c), and (iv) the implicit MC-PRM's contribution (prefix-sharing structure modulates token-level gradient distribution).

*PRM-specific scaling predictions.* The fold bifurcation generates five testable, quantitatively specific predictions — NOT generic properties of tipping points:

(P1) **Fold-specific autocorrelation scaling**: The autocorrelation time of the proxy-true gap G(t) = R_proxy(t) - R_true(t) diverges as τ_ac ~ |λ(t) - λ_c|^{-1/2} approaching the transition. This 1/2 exponent is specific to fold bifurcations and distinguishes them from transcritical (exponent 1) or Hopf (exponent 1/2 but with oscillatory component) bifurcations. We fit the scaling exponent empirically and test against the fold prediction.

(P2) **Variance scaling**: Fluctuations in G(t) grow as σ² ~ |λ(t) - λ_c|^{-1/2}, again with the fold-specific exponent.

(P3) **Solution-length dependence**: The critical training step t* at which exploitation onset occurs should decrease with solution length T under summation-form (because R_exploit/R_genuine = T·E[s_E]/T·E[s_G], and the group-normalization positive feedback strengthens with larger reward variance). Concretely, we test whether t*(AMC) < t*(MATH-easy) on matched problem sets differing primarily in solution length.

(P4) **Credit assignment modulation**: Under min-form (PURE), the positive feedback is broken — a single genuinely-scored step caps the trajectory reward, preventing μ_G from rising with exploitation. The fold bifurcation should be eliminated: G(t) follows smooth crossover dynamics with NO divergent autocorrelation. Under λ-GRPO, the fold persists (since it arises from the explicit PRM's trajectory-level signal, not the implicit PRM) but λ_c may shift because the implicit PRM's contribution to gradient distribution is normalized.

(P5) **Dual-PRM interaction signature**: In standard GRPO + explicit PRM, the implicit MC-PRM concentrates gradient updates on tokens with high prefix-sharing (common solution openings). If exploitation strategies share prefixes (e.g., similar boilerplate openings before diverging into exploitative patterns), the implicit PRM amplifies learning of these shared exploitative prefixes — lowering λ_c. λ-GRPO normalization should weaken this amplification, raising λ_c. We test this by comparing exploitation onset timing between standard GRPO and λ-GRPO.

*Connection to Karwowski et al.* Their framework shows Goodharting occurs when the optimization trajectory hits the occupancy polytope boundary where proxy and true reward directions diverge. In our GRPO + PRM setting, the 'boundary' corresponds to the policy having saturated the genuinely-learnable PRM scoring patterns and beginning to exploit non-robust features. Our fold bifurcation formalizes the mechanistic transition at this boundary: Karwowski's 'directional phase shift' (their Proposition 3) corresponds to our fold bifurcation's annihilation of the aligned equilibrium. The extension is that (a) the positive feedback from group normalization makes the transition sharper than in steepest ascent, (b) the neural PRM's nonlinearity creates a specific bifurcation type (fold) derivable from the credit assignment form, and (c) the dual-PRM structure introduces modulation parameters absent from their single-reward framework.

**Statistical Analysis and Baselines.** We test predictions using: PELT changepoint detection, BOCPD for uncertainty quantification, sliding-window autocorrelation and detrended fluctuation analysis for scaling exponent estimation, HMM regime detection, GRPO exponential saturation model as null model, and Karwowski et al.'s NDH (Normalized Drop Height) as a Goodhart severity metric. Novel metrics: 'Goodhart divergence rate' (dG/dt), 'critical slowing down index' (autocorrelation coefficient in trailing window), and 'fold scaling exponent' (fitted from τ_ac vs. |t - t*| in log-log space).

**Ablation Against Six Baselines.** A key contribution is rigorous comparison against six simpler alternatives spanning four detection paradigms:

*(i) Dynamics-based:* (a) PRM-adapted self-internalization gap, (b) naive proxy-true divergence rate threshold, (c) GRPO scaling law deviation (residuals from exponential saturation fit).

*(ii) Effort-based:* (d) TRACE-PRM score (adapted progressive CoT truncation AUC, following Wang et al., ICLR 2026 Oral) — this is our strongest baseline given TRACE's F1≈0.97 in math. We compute TRACE-PRM at each checkpoint on the held-out evaluation set and test whether TRACE score increase precedes accuracy-reward divergence with comparable or greater lead time than our framework.

*(iii) Representation-based:* (e) Energy loss monitoring (ΔE, adapted from Miao et al.'s PPO setting to GRPO).

*(iv) Gradient-based:* (f) GRIFT-style gradient fingerprints on sampled checkpoints (Tier 2).

For each baseline, we measure: detection lead time (training steps before accuracy-reward divergence), false positive rate, intervention effectiveness as early stopping trigger, and (for TRACE and self-internalization gap) whether the signal distinguishes aligned plateau from pre-exploitation regime. The bifurcation framework must demonstrate at least one of: (i) earlier detection via fold-specific scaling exponent divergence, (ii) lower false positive rate via bifurcation-type discrimination (distinguishing the fold's sharp transition from normal saturation's smooth plateau), (iii) mechanistic interpretability via SAE features identifying WHAT is exploited, (iv) regime identification enabling intervention selection (not just early stopping), or (v) quantitative prediction of exploitation onset timing via λ_c estimation.

**Cross-Paradigm Comparison.** We compare exploitation dynamics across discriminative vs. generative PRMs — testing whether the fold bifurcation structure persists, shifts (different λ_c), or changes type (fold → smooth crossover) with GenPRM's explicit verification reasoning. We additionally test (Tier 2) PURE and λ-GRPO as bifurcation-modifying interventions: PURE should eliminate the fold (P4), while λ-GRPO should shift λ_c (P5).

**Early Warning Validation.** We test whether fold-specific scaling (P1-P2) provides earlier and more reliable warning than generic early warning signals and the six baselines. We report the distribution of lead times across runs, PRM types, and model scales, alongside confidence intervals, and test detected signals as triggers for dynamic interventions (early stopping, reward model switching, Advantage Modification).

**Generalization Discussion.** The fold bifurcation framework extends beyond math+GRPO: any RL system with (a) a learned proxy reward, (b) group-relative or batch normalization of advantages, and (c) a discoverable exploitation strategy exhibits the positive feedback mechanism driving the fold. We validate with the Tier 3 PPO pilot (where advantage normalization plays an analogous role) and discuss how complementary approaches — CRA's PRM deconfounding, InfoRM's IB-based monitoring, IR³'s post-hoc interpretable detection — could combine with our training-time dynamics monitoring.

**Scope and Limitations.** Tier 1 spans two model scales, three PRMs across two paradigms, six baselines, and the full theoretical+empirical framework — sufficient for a publishable contribution. Tier 2 extends to PURE, λ-GRPO, full 14B cross-PRM comparison, and GRIFT. The fold bifurcation derivation is a phenomenological model (normal form reduction from the positive feedback mechanism) rather than a rigorous proof from GRPO's objective — we position it as generating testable predictions, not as a theorem. If empirical scaling exponents deviate from fold predictions (e.g., suggesting transcritical or no bifurcation), this itself is informative and we report the fitted bifurcation type as a core result.

## Inspiration
Novel theoretical synthesis: Karwowski et al.'s geometric Goodhart formalization in RL + fold bifurcation theory from dynamical systems + GRPO's dual-PRM structure (Sullivan et al.) + Stop Summation's credit assignment mechanism → derive that summation-form GRPO creates a specific fold bifurcation in the exploitation fraction with quantitative scaling predictions, extending Karwowski's linear-reward framework to neural PRMs. Empirical synthesis: systematic comparison of six orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based, energy-based, scaling-law-based) for PRM exploitation monitoring.

## Key References
- Goodhart's Law in Reinforcement Learning (arXiv:2310.09144, Karwowski et al. 2024, ICLR 2024)
- GRPO is Secretly a Process Reward Model (arXiv:2509.21154, Sullivan et al. 2025, under review ICML 2026)
- Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort (arXiv:2510.01367, Wang et al. 2026, ICLR 2026 Oral — TRACE)
- IR³: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking (arXiv:2602.19416, Beigi et al. 2026)
- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, 2026)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, Mahmoud et al. 2026)
- Natural Emergent Misalignment from Reward Hacking in Production RL (arXiv:2511.18397, 2025)
- Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning (arXiv:2602.05183, Yan et al. 2026)
- Early-warning signals for critical transitions (Scheffer et al., Nature 461, 2009)
- From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability (arXiv:2603.29805, Hennick & Corlouer 2026)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (arXiv:2504.15275, Cheng et al. 2025, NeurIPS 2025)
- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, GRIFT, Wang et al. 2026)
- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, Shi et al. 2025)
- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv:2507.18014, Nimmaturi et al. 2025)
- Scaling Laws for Reward Model Overoptimization (arXiv:2210.10760, Gao et al. 2023)
- Latent State Models of Training Dynamics (arXiv:2308.09543, 2023)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, 2026)
- GenPRM: Scaling Process Reward Models with Generative Reasoning (arXiv:2504.00891, AAAI 2026)
- Smarter Not Harder: TP-GRPO with Intrinsic-Signal Driving and Ability-Adaptive Reward Shaping (OpenReview:LZZENDlZt9, 2026)
- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)
- Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward (ICLR 2026)
- The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? (arXiv:2512.16912, 2025)
- Mitigating Reward Hacking with RL Training Interventions (ICLR 2026)
- Detecting Proxy Gaming in RL and LLM Alignment via Evaluator Stress Tests (arXiv:2507.05619, 2025)
- Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges (arXiv:2604.13602, 2026)
- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026)
- Posterior-GRPO: Rewarding Reasoning Processes in Code Generation (arXiv:2508.05170, 2025)
- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, Song et al. 2025, AAAI 2026 Workshop)
- The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking (arXiv:2501.19358, Miao et al. 2025, ICML 2025)
- InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling (arXiv:2402.09345, Miao et al. 2024, NeurIPS 2024)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, Helff et al. 2026, ICLR 2026 Workshop)
- A mathematical framework for critical transitions: bifurcations, fast-slow systems and stochastic dynamics (arXiv:1101.2899, Kuehn 2011)

## Resource Estimate
- **manual**: {'gpu_hours': '530–750 H100-hours (Tier 1: 4 runs ~16h training + ~130h eval/SAE/TRACE/analysis; Tier 2: 4 runs [14B×2 PRMs + PURE + λ-GRPO ablations] ~20h training + ~60h analysis + ~30h GRIFT; Tier 3: PPO pilot + spectral ~30h; shared overhead: ~70h SAE + ~40h TRACE evaluation)', 'timeline': '14–18 weeks (Tier 1 complete by week 10, Tier 2 by week 14, Tier 3 as time permits)', 'estimated_gpu_cost': '$800–$1,310 (at ~$1.50–$1.75/H100-hr spot pricing)', 'storage': '~8–12TB with delta compression'}
- **human_in_loop**: {'gpu_hours': '440–600 H100-hours (Claude-guided hyperparameter selection, early termination of unpromising runs, targeted SAE fine-tuning; Tier 1 prioritized)', 'timeline': '10–14 weeks (Tier 1 by week 8, Tier 2 by week 12)', 'claude_api_cost': '$400–$600 (checkpoint analysis, TRACE evaluation automation, bifurcation fitting, scaling exponent estimation, baseline comparison, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$660–$1,050', 'storage': '~6–10TB'}
- **auto_research**: {'gpu_hours': '640–960 H100-hours (parallel Tier 1+2, automated bifurcation fitting, baseline sweep, some redundant runs)', 'timeline': '6–8 weeks wall-clock (Tiers 1+2 parallelized; Tier 3 conditional)', 'claude_api_cost': '$700–$1,200 (experiment orchestration, real-time analysis, TRACE adaptation, bifurcation analysis, iterative paper writing)', 'estimated_gpu_cost': '$960–$1,680', 'storage': '~10–15TB', 'speed_bottleneck': 'Sequential RL training runs (3–5h per run on 4–8×H100); SAE extraction adds serial dependency; TRACE evaluation adds ~20% inference overhead per checkpoint'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a34ba325-877a-4df8-9497-efaf84713862",
  "type": "user",
  "uuid": "06f77dc2-c64e-4cf4-831b-cf9a3810b637",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:12:25.218Z_

```json
{
  "parentUuid": "06f77dc2-c64e-4cf4-831b-cf9a3810b637",
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
  "uuid": "9ead44ff-0655-4e88-b4d2-6a72b7ded595",
  "timestamp": "2026-05-19T21:12:25.218Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:12:25.218Z_

```json
{
  "parentUuid": "9ead44ff-0655-4e88-b4d2-6a72b7ded595",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "895d47a5-22d3-4dc3-ac1e-103ee8852fb5",
  "timestamp": "2026-05-19T21:12:25.218Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "895d47a5-22d3-4dc3-ac1e-103ee8852fb5",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three independent peer reviews on PRM exploitation proposal",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:12:49.356Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me first extract the key data points:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 中偏弱 (Medium-weak)
- Related Work: 强 (Strong)
- Probability (ML venue): 18% - 30%, median 23%
- CoRL: 0-2%
- Key concerns: Trivial alternative (TRACE, PURE), phenomenological model, scaling exponent testability


**Reviewer 2:**
- Novelty: 中 (Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability (ML venue): 20% - 30%, median 25%
- CoRL: 0%
- Key concerns: Formalism-over-insight, trivial alternative, venue mismatch

**Reviewer 3:**
- Novelty: 弱-中 (Weak-Medium)
- Significance: 中 (Medium)
- Related Work: 强 (Strong)
- Probability (ML venue): 18% - 30%, median 23%
- CoRL: ~

All three reviewers converge on medium novelty and significance with strong related work coverage, while their acceptance probabilities cluster tightly around 23-25% for ML venues. The main criticisms center on whether the contribution is truly novel compared to existing methods like TRACE and PURE, and whether the theoretical framework adds genuine insight or just formalism. The consensus is striking across multiple dimensions: all three reviewers unanimously reject this for CoRL due to venue mismatch, flag the trivial alternative threat from TRACE and PURE as serious, and note that the phenomenological derivation lacks rigor. There's also agreement that novelty and significance hover around medium, with strong coverage of related work. The main technical concern centers on whether the scaling exponents are actually testable given the constraints. The consistency across reviewers is striking at under 1% standard deviation, so they're clearly aligned on the core issues. Now I need to organize the implementation assessment based on what's actually in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "895d47a5-22d3-4dc3-ac1e-103ee8852fb5",
  "isSidechain": false,
  "requestId": "req_011CbCciFg3wbZ7fyB4YZxRD",
  "type": "assistant",
  "uuid": "b9e5794f-88d6-441e-a3c4-be12cb6ddfd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnS9KYueoxDDAUWL9qMviU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25350,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3060,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25350
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

_source line 9 · 2026-05-19T21:13:41.744Z_

【阶段】: Meta Judge
【三次中位】: [23%, 25%, 23%]  std=0.9%
【共识维度】:
- **Venue Mismatch（致命）**: 3/3 审稿人一致判定投 CoRL 2026 将被 desk reject（CoRL 明确要求 robotics focus，本 proposal 无任何 robotics 内容）。一致性：满票。
- **Novelty = 中**: R1「中」、R2「中」、R3「弱-中」。3/3 一致认为核心贡献是"用 bifurcation 语言重新描述 Stop Summation 已知的 positive feedback 机制"，增量偏窄，属 reformulation > new insight。
- **Significance = 中/中偏弱**: R1「中偏弱」、R2「中」、R3「中」。3/3 一致认为实际影响力被 TRACE (F1≈0.97) + PURE (root cause fix) 的存在严重压缩。
- **Related Work = 强**: 3/3 一致肯定，覆盖全面、引用准确、差异化定位清晰。这是 proposal 最突出的优势。
- **Trivial Alternative 威胁（严重）**: 3/3 一致标记 TRACE + PURE + 简单 divergence monitoring 三重夹击。核心质疑：如果检测已有 F1≈0.97，根因 fix 已知，bifurcation framework 的实际增量价值是什么？
- **Phenomenological Model 弱点（中等风险）**: 3/3 一致指出 fold bifurcation derivation 是 phenomenological fitting 而非 rigorous proof，任何正反馈系统都可如此拟合——不是 PRM-specific insight。
- **Scaling Exponent 可测性风险（中等风险）**: 3/3 均质疑在 noisy finite-sample RL 训练中能否可靠拟合 -1/2 exponent 并区分 fold vs. transcritical。
- **"Formalism > Insight" 拒稿风险（严重）**: R2 和 R3 显式标注，R1 隐含表达（"I would have guessed this"）。审稿人最可能攻击角度。

【异常维度】:
- R3 单独将 Novelty 降至「弱-中」（其余两位为「中」）——差异不大，但 R3 更强调 fold bifurcation 作为 generic property 的非特异性。因高一致性环境，此异常降权处理，不影响最终判定。
- R3 单独指出未覆盖 ecology/climate 领域 EWS false positive 批判文献——有道理但属次要 gap，不影响 rubric 判决。
- R1 单独强调 α(t) 作为标量 order parameter 的 well-definedness 问题——有效质疑但其余两位未重点展开，降权。

【最终概率】: [18% - 28%] 中位 23%
【一致性】: 高（std=0.9%，三份评审在 rubric 判决和概率区间上高度收敛）

【综合理由】:

三份评审呈现罕见的高度一致，核心判决无实质分歧：

1. **Venue 问题是绝对致命的**。3/3 一致、无歧义。投 CoRL 2026 概率为 0%。以下概率仅适用于改投 NeurIPS/ICML/ICLR 等 ML 顶会。

2. **概率取值逻辑**：三位中位分别为 23%、25%、23%，std 仅 0.9%。按高一致性规则取中位附近并缩窄区间。将上界从最宽松的 30% 下调至 28%（因 R1 的 Significance「中偏弱」判定提供了额外约束，且三位均对 trivial alternative 威胁的严重性达成共识），下界维持 18%。中位取 23%（三份中位的中位数）。

3. **概率上限由 Novelty 和 Significance 共同约束**。三位一致认为 Novelty 在「中」水平（reformulation of known mechanism），Significance 在「中」水平（被 TRACE+PURE 压缩）。在这两个维度均为「中」的情况下，即使实验执行完美，概率天花板约在 30-35%。实际上界进一步被 trivial alternative 的严重性压至 ~28%。

4. **概率下限由 Related Work 质量和研究问题时效性托住**。3/3 一致给出 Related Work「强」评级，且 PRM exploitation 是 2025-2026 高关注度问题，保证了基本的 relevance floor。

5. **核心风险评估**：三份评审一致聚焦于两个关键风险——(a) "Formalism over insight" 拒稿理由，审稿人可能认为 bifurcation framework 是对 Stop Summation 已知机制的数学包装；(b) 实验层面的 trivial alternative 压制，bifurcation framework 需要在 lead time 上显著超越 TRACE，否则贡献退化为 incremental。这两个风险相互强化：如果理论 insight 不足以独立成立，就更依赖 empirical superiority；但 empirical superiority 面临 TRACE F1≈0.97 的极高 bar。

【建议】: 边缘（改投 ML 顶会后处于边缘区域；投 CoRL 则 KILL）

【实施评估】:
  - 计算资源: 530-960 H100-hours（视执行模式），约 $660-$1,680 GPU 成本。需要 4-8×H100 集群，每个 RL 训练 run 3-5 小时。门槛中等，非资源瓶颈。
  - 数据需求: MATH/AMC/AIME 数学推理数据集（公开可得）；Qwen3-4B/14B 模型（公开可得）；Qwen2.5-Math-PRM-7B/ACTPRM-X/GenPRM-7B 三种 PRM（需确认可得性）。数据不是主要障碍。
  - 人工介入: SAE 训练策略调优、bifurcation fitting 的统计判断、solution style 分类器的验证需人工参与。TRACE 适配到 PRM 设定需要工程工作。整体人工需求中等。
  - 训练需求: 需要完整的 GRPO RL 训练（非预训练），每 run 3-5h on H100。SAE anchor 训练 ~40h。不涉及大规模模型预训练，训练需求可控。
  - 新 Benchmark: 不需要构建新 benchmark。使用现有 MATH/AMC/AIME 数据集。需要自建 solution style taxonomy 的分类标注（基于 Tiwari et al.），工作量有限。
  - 预估周期: Tier 1 完成需 8-10 周，Tier 1+2 需 12-14 周，全部完成 14-18 周。最短可投稿路径（仅 Tier 1）约 10-12 周。存储需 6-15TB（含 delta 压缩的 dense checkpoints）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9e5794f-88d6-441e-a3c4-be12cb6ddfd0",
  "isSidechain": false,
  "requestId": "req_011CbCciFg3wbZ7fyB4YZxRD",
  "type": "assistant",
  "uuid": "a5718f44-da52-46bc-83c2-a9077da9dab3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnS9KYueoxDDAUWL9qMviU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25350,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3060,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 25350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25350
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to make my assessment. Let m…",
  "leafUuid": "a5718f44-da52-46bc-83c2-a9077da9dab3",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize three independent peer reviews on PRM exploitation proposal",
  "sessionId": "28670fdb-33a2-424c-b224-891715cdc048"
}
```

---
