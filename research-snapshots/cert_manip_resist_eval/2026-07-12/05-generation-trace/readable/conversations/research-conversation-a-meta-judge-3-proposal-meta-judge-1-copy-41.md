# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/6611fbea-f3f3-4895-9a36-69ff1be48ddd.jsonl`
- **Structured JSON:** [`386a46f8a465a8f23b87.json`](../../sessions/38/386a46f8a465a8f23b87.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T19:08:30.768Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T19:08:30.768Z",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n============================================================\n⚠️  严重前置问题：投稿目标 CoRL 2026 存在致命的 SCOPE MISMATCH\n============================================================\n\nCoRL 2026 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate\nthe relevance of proposed models, algorithms, datasets, and benchmarks\nto robotics. Submissions without a robotics focus will be returned\nWITHOUT REVIEW.\"\n\n本 proposal 完全关于 LLM 数学推理场景下的 PRM exploitation 检测，\n涉及 GRPO 训练、Process Reward Model、Chain-of-Thought 推理——\n没有任何机器人学内容（无 manipulation、locomotion、perception、\nsim-to-real、robot control 等）。\n\n→ 如投 CoRL 主会，几乎确定会被 desk reject，不进入审稿流程。\n→ 合理目标会议应为 NeurIPS / ICML / ICLR 主会。\n\n下面的评估假设投稿到合理会议（NeurIPS/ICML/ICLR），\n并在最终概率中单独给出 CoRL 的估计。\n============================================================\n\n\n【领域调研】:\n\n1. Karwowski et al. \"Goodhart's Law in Reinforcement Learning\"\n   (arXiv:2310.09144, ICLR 2024):\n   — 在 tabular MDP + 线性 reward 上形式化 Goodhart's law，\n     用 occupancy polytope 几何解释 Goodharting 发生条件，\n     推导了最优 early stopping 及 regret bound。\n   — 与本 proposal 的关系：proposal 声称在此基础上扩展到\n     neural PRM + GRPO，但原工作本身没有涉及任何 bifurcation\n     理论或 scaling exponent 预测。\n\n2. Sullivan et al. \"GRPO is Secretly a Process Reward Model\"\n   (arXiv:2509.21154, under review ICML 2026):\n   — 证明 GRPO + ORM 等价于 MC-PRM-aware 目标，提出 λ-GRPO。\n   — 与本 proposal 的关系：proposal 的 \"dual-PRM\" 分析\n     直接依赖此工作。Sullivan 的发现是已公开结果，\n     proposal 的扩展是分析 dual-PRM 下的 exploitation dynamics，\n     这一方向尚未被 Sullivan 本人或他人研究。\n\n3. Cheng et al. \"Stop Summation\" (arXiv:2504.15275, NeurIPS 2025):\n   — 识别 summation-form credit assignment 是 PRM hacking 的机制\n     原因，提出 min-form (PURE)。\n   — 与本 proposal 的关系：proposal 的核心预测 P3（长度依赖）\n     和 P4（min-form 消除 fold）本质上是用 bifurcation 语言\n     重新表述 Stop Summation 的发现。\n\n4. Wang et al. \"TRACE\" (arXiv:2510.01367, ICLR 2026 Oral):\n   — 通过 progressive CoT truncation 测量推理 effort，F1≈0.97。\n   — 与本 proposal 的关系：TRACE 是 proposal 承认的最强 baseline。\n     如果 TRACE 已达 F1≈0.97，bifurcation 框架需要证明\n     在 TRACE 之上的增量价值（如更早检测、更低误报），\n     但 proposal 尚无证据支持这一点。\n\n5. Beigi et al. \"IR³\" (arXiv:2602.19416, 2026):\n   — Contrastive IRL + SAE 后置检测，0.89 correlation。\n   — 与本 proposal 的关系：IR³ 是 post-hoc 检测，\n     proposal 声称做 training-time 预测，但二者的 SAE 方法论\n     有重合。\n\n6. Hennick & Corlouer \"From Density Matrices to Phase Transitions\"\n   (arXiv:2603.29805, 2026):\n   — 用 2RDM spectral analysis 检测训练 phase transition。\n   — 与本 proposal 的关系：最近的概念邻居——同样用\n     dynamical systems / statistical physics 工具检测训练动态，\n     但研究的是 capability emergence 而非 exploitation。\n\n7. Scheffer et al. \"Early-warning signals for critical transitions\"\n   (Nature, 2009):\n   — 经典 critical slowing down 理论：fold bifurcation 前\n     autocorrelation 和 variance 按 |λ-λ_c|^{-1/2} 发散。\n   — 与本 proposal 的关系：proposal 的 5 个预测中，\n     P1 和 P2 直接来自 Scheffer et al. 的通用理论，\n     应用到新领域但本身不是新的理论贡献。\n\n8. \"When Reward Hacking Rebounds\" (arXiv:2604.01476, 2026),\n   Mahmoud et al. (arXiv:2605.12474, 2026),\n   Helff et al. (arXiv:2604.15149, ICLR 2026 Workshop):\n   — 多项并行工作刻画 reward hacking 的时序动态\n     （三阶段 rebound、rubric verifier 下单调增长、\n     progressive shortcut growth）。\n   — 与本 proposal 的关系：这些工作也在刻画 exploitation\n     的时间演化，但没有使用 bifurcation 框架。\n     proposal 的差异化在于提供定量 scaling predictions，\n     但这些预测是否能在嘈杂的 RL 训练中被 cleanly 验证\n     存在高度不确定性。\n\n- 调研总结：PRM exploitation 检测是 2025-2026 年的活跃研究\n  方向，已有多种互补方法（TRACE effort-based、IR³ post-hoc SAE、\n  能量损失、gradient fingerprints 等）。将 bifurcation 理论\n  应用于此领域是一个尚未被直接做的方向，但核心 scaling\n  predictions（P1/P2）来自经典 dynamical systems 理论，\n  而非从 GRPO 机制中推导出的新理论——proposal 的主要贡献\n  更多是\"将已知框架映射到新领域\"而非\"发现新的理论结构\"。\n\n\n【Trivial Alternative 检验】:\n\n存在多个低成本替代方案构成严重威胁：\n\n(1) **直接监控 proxy-true gap + threshold early stopping**：\n    不需要任何 bifurcation 理论，只需在训练中定期采样评估\n    ground-truth accuracy，当与 PRM reward 出现显著背离时停止。\n    这是最 trivial 的 baseline，proposal 虽提及但未论证\n    bifurcation 框架的增量价值在哪里。\n\n(2) **TRACE (F1≈0.97)**：已有极高精度的检测方法。\n    即使 bifurcation 框架能提供\"更早\"的警告信号，\n    但 TRACE 的高 F1 意味着在检测维度上的 headroom 很小。\n    proposal 需要在 \"onset prediction\" 维度上证明价值，\n    但 fold-specific scaling exponent 的实际检测优势\n    （相比简单的 sliding-window divergence rate）未经验证。\n\n(3) **Stop Summation 的 min-form (PURE) 直接作为干预**：\n    如果已知 summation-form 是问题根源，直接使用 min-form\n    就能避免 exploitation——不需要检测框架。\n\n增量价值主要依赖于两个声明：(a) 比现有方法更早检测，\n(b) 提供机制性理解（\"什么类型的 bifurcation\"）。\n但 (a) 未经验证，(b) 的实际价值（知道是 fold 而非\ntranscritical 对实际干预策略有何影响？）也未论证清楚。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链存在多个未经验证的关键假设：\n\n(1) **1D 降维假设**：将高维 neural policy 训练动态\n    简化为 dα/dt = f(α; λ) 的一维系统。这是一个\n    极强的假设——exploitation fraction α 是否真的是\n    一个有意义的低维 order parameter？RL 训练中\n    可能存在多个 exploitation 模式同时演化、互相竞争，\n    1D 描述可能根本不成立。\n\n(2) **从 \"positive feedback\" 到 \"fold bifurcation\" 的跳跃**：\n    Proposal 论证 group-relative normalization 创造正反馈，\n    然后直接写出 fold normal form f(α; λ) = λ - λ_c + (α - α_c)²。\n    这不是推导——这是假设。许多正反馈系统产生的\n    不是 fold bifurcation（可以是 transcritical、pitchfork、\n    或根本没有 clean bifurcation 的 crossover）。\n    从 GRPO 的具体数学形式到 fold normal form 的严格推导\n    缺失——proposal 自己也承认这是 \"phenomenological model\"\n    而非 theorem。\n\n(3) **Scaling exponent 可测性假设**：即使 fold bifurcation\n    成立，从噪声很大的 RL training curves 中拟合出\n    |λ - λ_c|^{-1/2} 的精确 scaling exponent 是极其困难的。\n    这需要：(a) λ_c 本身被准确定位，(b) 足够多的\n    接近 critical point 的数据点，(c) 训练噪声不淹没\n    scaling signal。实际 RL 训练中，这三个条件是否\n    同时满足是一个未经验证的强假设。\n\n(4) **\"Exploitation fraction\" 可操作化假设**：α(t) 的\n    定义依赖于能清晰区分 \"exploitative\" vs. \"genuine\"\n    策略。但在实际 PRM hacking 中，exploitation 是一个\n    连续谱（部分正确但利用 PRM 弱点的解法），\n    二元分类的假设可能过于简化。\n\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 (偏弱)\n   — 核心理论贡献是将 Scheffer et al. (2009) 的经典\n     critical slowing down / fold bifurcation 框架应用到\n     PRM exploitation 检测领域。这是\"已知框架 → 新领域\"\n     的迁移，而非新的理论发现。\n   — 5 个预测中：P1/P2 是 fold bifurcation 的通用性质\n     （Scheffer et al. 2009），不是 GRPO-specific 的推导；\n     P3（长度依赖）本质上复述 Stop Summation (Cheng et al.,\n     NeurIPS 2025) 的发现；P4（min-form 消除 fold）\n     同样是 Stop Summation 的动力学语言重述；\n     P5（dual-PRM interaction）是唯一真正新的预测，\n     但也是最模糊和最难验证的。\n   — \"系统对比 6 种检测 paradigm\" 有 empirical novelty，\n     但这是实验设计层面贡献，非 idea 层面。\n   — 在已有大量 reward hacking 检测方法（TRACE F1≈0.97、\n     IR³ 0.89 correlation、能量损失、GRIFT）的情况下，\n     增加一个 bifurcation 视角的边际 novelty 有限。\n\n2. Significance: 中\n   — PRM exploitation 检测是 RL alignment 中一个重要且\n     timely 的问题，这一点毫无疑问。\n   — 但 proposal 面临\"天花板问题\"：如果 TRACE 已经\n     F1≈0.97，检测问题在多大程度上还是一个\n     open problem？实际影响力可能有限。\n   — 即使 bifurcation 框架成立，对实际工程实践的\n     指导意义有限——知道\"这是一个 fold bifurcation\"\n     比起\"直接用 TRACE 检测或用 PURE 避免\"\n     对 practitioner 的价值增量不明确。\n   — 理论角度，如果能 rigorously 证明 fold bifurcation\n     （而非 phenomenological 假设），对理解 RL training\n     dynamics 会有贡献，但目前的 derivation 不够 rigorous。\n\n3. Related Work: 强\n   — 这是 proposal 最突出的优势。对领域的覆盖非常全面，\n     涵盖了 Karwowski (ICLR 2024)、Sullivan (ICML 2026 under review)、\n     Stop Summation (NeurIPS 2025)、TRACE (ICLR 2026 Oral)、\n     IR³、Hennick & Corlouer、能量损失 (ICML 2025)、\n     GRIFT、CRA、InfoRM (NeurIPS 2024) 等。\n   — 差异化定位清晰：明确指出与每个相关工作的区别\n     （post-hoc vs. training-time、sample-level vs.\n     population-level、检测 vs. 预测 onset 等）。\n   — 经调研验证，引用的关键论文均真实存在，\n     描述基本准确。\n\n\n【概率估计】:\n\n→ 如投 CoRL 2026 主会：0-2%（几乎确定 desk reject，\n  无任何机器人学内容，CoRL 明确拒绝非 robotics submission）\n\n→ 如投合理会议（NeurIPS/ICML/ICLR）：18-28%，中位 22%\n\n【估计理由】:\n\n对于 CoRL：致命的 scope mismatch，无需进一步讨论。\n\n对于合理会议 (NeurIPS/ICML/ICLR)：\n- Related Work 维度强，说明作者对领域理解深入，\n  这为项目提供了合理的下限保障（不会因为 miss 关键\n  相关工作而被拒）。\n- 但 Novelty 偏弱是上界的关键限制。核心理论贡献是\n  \"经典框架 → 新领域\"的迁移，审稿人很可能认为\n  intellectually thin——P1/P2 来自 Scheffer 2009，\n  P3/P4 复述 Stop Summation，P5 模糊难验证。\n  审稿人大概率的反应是：\"interesting application but\n  limited theoretical depth\"。\n- Significance 受制于 TRACE F1≈0.97 的存在——\n  如果检测问题已经有如此 strong 的 solution，\n  bifurcation 框架的边际价值需要非常 compelling 的\n  论证，而 proposal 在这一点上的论证尚不充分。\n- 前提假设（1D 降维、phenomenological fold derivation、\n  scaling exponent 可测性）如果被审稿人追问，\n  缺乏有力回应。\n- 综合来看：idea 方向站得住脚（reward hacking dynamics\n  值得理论化理解），但内核薄弱（核心贡献是\n  relabeling rather than discovering），且面临 strong\n  trivial alternative 威胁。这将概率限制在 25% 以下。\n\n【主要风险】:\n\n1. **\"Relabeling, not discovering\" 风险**：审稿人可能认为\n   将 fold bifurcation 框架套用到 PRM exploitation 上\n   本质上是用动力系统术语重新描述了已知现象\n   （exploitation 有 tipping point → fold bifurcation；\n   summation 导致 hacking → 正反馈），而没有产生\n   genuinely new insight。最有可能以 \"limited novelty\"\n   被拒。\n\n2. **\"Why not just use TRACE / PURE?\" 风险**：\n   审稿人会问：如果 TRACE 已经 F1≈0.97 用于检测，\n   PURE 已经直接消除 exploitation mechanism，\n   为什么还需要一个复杂的 bifurcation 理论框架？\n   Proposal 目前对此的回应不够有力——\n   \"onset prediction\" 和 \"mechanistic understanding\"\n   的实际价值需要更 concrete 的论证。\n```\n\n---\n\n**总结**：此 proposal 存在一个 **致命的前置问题**——投稿目标 CoRL 2026 是机器人学习会议，而 proposal 内容是纯 LLM/RL alignment 方向，**无任何 robotics 成分，会被 desk reject**。如果转投合理会议（NeurIPS/ICML/ICLR），idea 质量处于\"方向正确但内核偏薄\"的区间（中位约 22%），主要受限于 novelty 不足（经典框架迁移而非新理论发现）和 trivial alternative 威胁（TRACE/PURE 已高效解决检测/消除问题）。Related Work 覆盖是本 proposal 的明显强项。\n\n建议首先 **重新确认投稿目标会议**，再决定是否进入后续的发掘/补救迭代流程。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)\n- [Cheng et al. - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Wang et al. - TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Beigi et al. - IR³](https://arxiv.org/abs/2602.19416)\n- [Hennick & Corlouer - Phase Transitions in Deep Learning](https://arxiv.org/pdf/2603.29805)\n- [Scheffer et al. - Early-warning signals for critical transitions (Nature 2009)](https://www.nature.com/articles/nature08227)\n- [Reward Hacking Rebounds (arXiv:2604.01476)](https://arxiv.org/pdf/2604.01476)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my evaluation. Let me compile the full assessment.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【关键前置问题：严重的会议匹配问题】\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求论文 \"focus on a core robotics problem\" 并鼓励 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"。本 proposal 研究的是 LLM 推理训练中的 PRM exploitation / reward hacking 检测——与机器人学习完全无关，不涉及任何 robotic perception、control、manipulation、locomotion 或 sim-to-real transfer 内容。\n\n如果投 CoRL，此论文极大概率在 desk review 阶段即被判定 out of scope 而直接拒稿。建议改投 ICML、NeurIPS 或 ICLR。以下评估假设投稿至合适的顶会（如 ICML/NeurIPS/ICLR），单纯评估 idea 质量。\n\n\n【领域调研】:\n- [Karwowski et al., arXiv:2310.09144] (ICLR 2024): Goodhart's law 在 RL 中的几何形式化。基于 occupancy polytope boundary transitions 解释 Goodharting 发生条件，推导最优 early stopping。框架限于 tabular MDP + linear reward，不覆盖 neural PRM 或 GRPO。本 proposal 自称在此基础上拓展——但需注意该拓展的严格性。\n- [Sullivan et al., arXiv:2509.21154] (under review ICML 2026): 证明 GRPO + ORM 等价于带隐式 Monte-Carlo PRM 的目标，提出 λ-GRPO 归一化 process set size，获 >10% accuracy 提升和 2× 收敛加速。本 proposal 引用准确。\n- [Wang et al., arXiv:2510.01367] (ICLR 2026 Oral, TRACE): 通过渐进截断 CoT 测量推理努力来检测 implicit reward hacking，F1≈0.97（数学推理任务）。这是当前最强的 reward hacking 检测方法之一，本 proposal 将其作为 baseline。引用准确。\n- [Cheng et al., arXiv:2504.15275] (NeurIPS 2025, Stop Summation/PURE): 指出 summation-form credit assignment 是 PRM hacking 的机制性原因，提出 min-form (PURE) 来解决。本 proposal 引用准确。该工作已回答了 \"WHY\" 的问题，PURE 已提供了解决方案。\n- [Beigi et al., arXiv:2602.19416] (IR³, 2026): 通过 contrastive IRL + SAE 实现可解释的 reward hacking 检测，0.89 与 ground-truth reward 的相关性。Post-hoc 方法。引用准确。\n- [Hennick & Corlouer, arXiv:2603.29805] (2026): 将量子化学中的 2RDM 方法应用于深度学习训练阶段转变的早期预警，使用 spectral heat capacity 信号。这是\"将 critical transitions 理论应用于 ML 训练动态\"这一方向上的直接竞争者/先驱。\n- [Miao et al., arXiv:2501.19358] (ICML 2025, Energy Loss): 发现 energy loss 作为 PPO-RLHF 中 reward hacking 的单调递增早期预警信号。\n- [Gao et al., arXiv:2210.10760] (2023): Reward model overoptimization 的 scaling laws，已建立了 proxy-true reward 之间关系的量化框架。\n\n- 调研总结: Reward hacking / Goodhart's law 在 LLM RL 训练中是一个活跃且竞争激烈的研究领域（2025-2026 年有超过 15 篇相关论文）。检测方面已有 TRACE (F1≈0.97)、IR³、Energy Loss、GRIFT 等多种方法；机制分析方面 Stop Summation/PURE 已解决 \"why\" 问题；理论方面 Karwowski et al. 已形式化 Goodhart's law in RL。本 proposal 试图占据的 niche 是 \"bifurcation-theoretic prediction of WHEN exploitation occurs\" —— 但该 niche 的增量价值面临来自已有方法的强烈挤压。\n\n\n【Trivial Alternative 检验】:\n存在严重的 trivial alternative 威胁：\n\n1. **TRACE (F1≈0.97)** 已经是一个极其有效的 reward hacking 检测器。本 proposal 必须证明 bifurcation framework 能提供比 TRACE 更早或更可靠的预警——但这完全是一个不确定的实验结果，不是 idea 层面能保证的。\n2. **简单的 proxy-true divergence 监控**（即直接监控 PRM reward 与 ground-truth accuracy 的差值）在实践中已被广泛使用。Bifurcation framework 相对于此的增量价值在于\"更早几步检测\"和\"定量预测 onset timing\"——但如果检测 lead time 的提升只有几个 training steps，实际价值有限。\n3. **PURE (min-form credit)** 已经从根本上解决了 summation-form 导致的 PRM hacking 问题。如果 PURE 有效，那么与其预测 exploitation 何时发生，不如直接使用 PURE 消除 exploitation。\n\n核心增量价值主张：\"理解 bifurcation type 能指导 intervention selection（不只是 early stopping）\"—— 但 proposal 对此只有模糊声称，没有具体论证\"知道是 fold bifurcation vs. 其他类型\"如何改变干预策略。\n\n\n【前提假设检验】:\n核心 claim 的逻辑链条中有多个未经验证的关键假设：\n\n1. **\"正反馈 → 三次非线性 → fold bifurcation\"**：这是整个理论框架的核心，但推导是 phenomenological 的——从\"存在正反馈\"直接跳到\"normal form 是 f(α;λ) = λ - λ_c + (α - α_c)² + h.o.t.\"。这不是从 GRPO 目标函数严格推导出的，而是假设了一种特定的正常形式。实际系统的动力学可能不服从这个简化。Proposal 自己也承认这是 \"phenomenological model rather than a rigorous proof\"。\n2. **Exploitation fraction α(t) 是一个良定义的标量**：实际训练中，\"exploitative strategy\" 和 \"genuine strategy\" 之间的边界模糊且随训练变化。将其建模为一个清晰的一维标量 α(t) 是一个强假设。\n3. **Group-relative normalization 的正反馈确实足以产生 abrupt transition**：proposal 论证了\"随着 α 上升，genuine solutions 获得负 advantage\"的正反馈——但这个正反馈可能被其他因素（如 KL 惩罚、learning rate decay、clipping）所抑制，不一定达到 bifurcation 的 sharpness。\n4. **Fold-specific 的 scaling exponents 在噪声真实数据中可测量**：critical slowing down 的 τ_ac ~ |λ-λ_c|^{-1/2} scaling 在低噪声物理系统中可观测，但在高度随机的 LLM 训练过程中，信噪比可能不足以区分 fold (exponent 1/2) vs. 其他 bifurcation types。\n\n\n【3 维度打分】:\n  1. Novelty: 弱-中 — 核心思路是 \"将 dynamical systems / bifurcation theory 应用于 ML 训练动态\"，这一方向已有 Hennick & Corlouer (2603.29805) 的先例（虽然他们研究的是 capability emergence 而非 adversarial exploitation）。具体到 PRM exploitation 的应用是新的，但理论贡献的核心——\"正反馈→fold bifurcation\"——是 phenomenological 断言，不是从 GRPO 数学结构严格推导出的 surprising 结论。五个 predictions 中，P3（solution length dependence）和 P4（min-form eliminates fold）几乎可以直接从 Stop Summation 的结论推出（summation-form 下更长的解 = 更大的 R_exploit，min-form 下正反馈被打断），不需要 bifurcation 理论。真正需要 bifurcation 理论才能得到的 prediction 主要是 P1 和 P2 的具体 scaling exponents——但如上所述，这些在真实数据中能否被测量出来存疑。\n\n  2. Significance: 中 — PRM exploitation 在 LLM RL 训练中确实是一个重要且实际的问题。但 (a) PURE 已经从机制层面提供了解决方案（消除 summation-form），(b) TRACE F1≈0.97 已经提供了极强的检测能力。本 proposal 的 significance 取决于\"predicting onset timing\"相比于\"detecting exploitation\"有多大的实际增量价值——这一点 proposal 没有充分论证。此外，这个 framework 如果成功，它的影响主要限于 GRPO + PRM 这个特定 setup，generalization 论证（PPO pilot in Tier 3）比较薄弱。\n\n  3. Related Work: 强 — 这是 proposal 最出色的方面。Related work 覆盖非常全面，按 6 个类别系统组织，对每篇工作的描述基本准确（经调研验证），差异化定位清晰。特别是对 TRACE、Stop Summation、Karwowski et al.、Sullivan et al.、IR³ 的定位相当精准。唯一的轻微问题是对自身理论贡献相对于 Karwowski 的 novelty delta 有些夸大（\"extends their geometric insight\"——但实际上是在一个不同的、更弱的理论框架下做的）。\n\n\n【概率估计】: [15% - 25%] 中位 20%\n（注：此概率假设投稿至合适的 ML 顶会如 ICML/NeurIPS/ICLR。若投 CoRL，概率接近 0%，因为完全 out of scope。）\n\n【估计理由】:\nidea 的方向（用 dynamical systems 理论理解 RL 训练中的 Goodhart tipping point）是 sound 的，research question 有实际意义，related work 做得扎实。但 idea 的核心理论贡献——\"GRPO 的 group-relative normalization 产生 fold bifurcation\"——是一个 phenomenological assertion，不是 rigorous derivation，这意味着即使实验跑出来，理论 insight 的深度有限（审稿人可能会说 \"you fitted a normal form to your data, but why is it specifically a fold and not something else?\"）。更致命的是 trivial alternative 威胁：TRACE (F1≈0.97) + PURE (消除 hacking) 的组合已经在检测和解决层面覆盖了问题，bifurcation framework 的增量实际价值不明确。五个 predictions 中只有 P1/P2 的 scaling exponents 真正需要 bifurcation 理论，但这些在高噪声的 LLM 训练数据中能否被可靠测量是一个根本性风险。\n\n上界被 **Novelty** 限制——核心理论贡献是 phenomenological 的，不够 surprising；下界被扎实的 **Related Work** 覆盖和 well-defined 的实验 plan 所托住。\n\n【主要风险】:\n1. **Trivial alternative 挤压**: TRACE + PURE 的组合已经从检测和解决两个层面覆盖了 PRM exploitation 问题，bifurcation framework 的增量价值缺乏有力论证。审稿人可能会问：\"如果 PURE 消除了 fold bifurcation（你自己的 P4 预测），为什么不直接用 PURE？你的理论框架在实践中是否只是一个诊断工具而非解决方案？\"\n2. **Phenomenological theory 的脆弱性**: 如果实测 scaling exponents 偏离 fold 预测（非常可能，因为真实系统远比 normal form 复杂），整个\"fold bifurcation\"的 narrative 就会瓦解。Proposal 虽声明\"如果偏离也是 informative\"，但\"我们预测了 fold bifurcation 但实际不是\"作为核心结论的论文，novelty 和 impact 都会大打折扣。\n```\n\n**补充说明**：\n\n关于 **会议选择**，这是一个必须在投稿前解决的根本性问题。本 proposal 完全不涉及机器人学习，投 CoRL 2026 几乎必然被 desk reject。建议考虑以下会议：\n- **NeurIPS 2026**（理论+实验兼具的 ML 工作）\n- **ICML 2026**（如果还来得及 deadline）\n- **ICLR 2027**（如果时间线允许更充分的实验）\n- **AAAI 2027** 或相关 workshop 作为备选\n\nSources:\n- [Goodhart's Law in Reinforcement Learning (Karwowski et al., ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [GRPO is Secretly a Process Reward Model (Sullivan et al.)](https://arxiv.org/abs/2509.21154)\n- [TRACE: Detecting Implicit Reward Hacking (Wang et al., ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Stop Summation / PURE (Cheng et al., NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [IR³ (Beigi et al., 2026)](https://arxiv.org/abs/2602.19416)\n- [Hennick & Corlouer, Spectral Early Warnings (2026)](https://arxiv.org/pdf/2603.29805)\n- [Energy Loss (Miao et al., ICML 2025)](https://arxiv.org/abs/2501.19358)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [Karwowski et al., \"Goodhart's Law in Reinforcement Learning\", arXiv:2310.09144] (ICLR 2024):\n   提供了 RL 中 Goodhart 定律的几何形式化——基于 occupancy polytope 边界转换和 proxy-true reward 角度偏差。框架假设 tabular MDP + 线性 reward，不涉及 neural PRM、step-level credit assignment 或 group-relative normalization。Proposal 声称从这里延伸到 GRPO+PRM 设置，claim 基本准确。\n\n2. [Sullivan et al., \"GRPO is Secretly a Process Reward Model\", arXiv:2509.21154] (under review ICML 2026):\n   证明 GRPO+ORM 等价于隐式 Monte-Carlo PRM 目标，提出 λ-GRPO 修复 step-level 不平衡，取得 >10% 准确率提升和 ~2× 收敛加速。论文真实存在，proposal 对其描述准确。这是 proposal 的关键理论依赖之一。\n\n3. [Cheng et al., \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\", arXiv:2504.15275] (NeurIPS 2025):\n   识别 summation-form credit assignment 为 PRM hacking 的机制性原因，提出 min-form (PURE)。Proposal 的\"fold bifurcation 源于 summation-form\"的 claim 直接建立在此基础上。论文真实，描述准确。\n\n4. [Wang et al., \"Is It Thinking or Cheating? (TRACE)\", arXiv:2510.01367] (ICLR 2026 Oral):\n   通过 CoT 截断测量推理 effort 来检测隐式 reward hacking，F1≈0.97（数学任务）。这是 proposal 自认的最强 baseline。论文真实存在，是 ICLR 2026 Oral。TRACE 的强度对 proposal 构成显著的 trivial alternative 威胁。\n\n5. [Beigi et al., \"IR³\", arXiv:2602.19416] (2026):\n   对比式 IRL + SAE 进行事后 reward hacking 检测和缓解，达到 0.89 ground-truth reward 相关性。论文真实。IR³ 是事后方法，proposal 定位为训练时方法，差异化成立。\n\n6. [Hennick & Corlouer, \"From Density Matrices to Phase Transitions in Deep Learning\", arXiv:2603.29805] (2026):\n   将 2RDM spectral analysis 应用于训练相变（capability emergence, grokking, emergent misalignment）。这是概念上最近的邻居——将物理工具（spectral methods）应用于 ML 训练动态监测。但该工作关注的是有益的重组，而非对抗性 exploitation。\n\n7. [Miao et al., \"Energy Loss Phenomenon in RLHF\", arXiv:2501.19358] (ICML 2025):\n   发现 energy loss 作为 PPO-based RLHF 中 reward hacking 的单标量早期预警信号。Proposal 将其作为 baseline 之一。\n\n8. [Scheffer et al., \"Early-warning signals for critical transitions\", Nature 461] (2009):\n   经典的 critical slowing down 理论——fold bifurcation 附近 autocorrelation 和 variance 发散的 ±1/2 指数预测。这是 proposal 理论框架的核心数学工具来源，非 ML 领域原创。\n\n9. [Nimmaturi et al., \"Predictive Scaling Laws for Efficient GRPO Training\", arXiv:2507.18014] (2025):\n   GRPO 训练的指数饱和 scaling law，三阶段动态。Proposal 将其作为 null model。\n\n10. [Mahmoud et al., \"Reward Hacking in Rubric-Based RL\", arXiv:2605.12474] (2026):\n    展示 rubric verifier 下单调 exploitation 增长，提出 self-internalization gap。Proposal 将其改编为 PRM 适配版 baseline。\n\n- **调研总结**: Reward hacking 检测/缓解是 2025-2026 年的研究热点，已有大量方法覆盖不同检测范式（effort-based, representation-based, gradient-based, energy-based）。但将 bifurcation theory 特异性地应用于 GRPO+PRM 的 credit assignment 机制、并从中导出定量可测试预测，确实尚无先例。Proposal 处于\"理论物理工具 → ML 训练动态\"这一新兴交叉方向，与 Hennick & Corlouer 同属此趋势，但针对对抗性 exploitation 而非有益相变。\n\n**⚠️ 致命问题：投稿目标 venue 严重不匹配 ⚠️**\n\nCoRL 2026 (Conference on Robot Learning) 的征稿范围明确限定于机器人学习，包括：robotic perception and control、robot foundation models、imitation learning for robotics、RL for control of physical robots、robot safety and alignment for learning-based robotic systems、robot manipulation/navigation/locomotion/driving/flight 等。CoRL 明确鼓励 real-robot experiments 或 simulation-to-real 证据。\n\n本 proposal 的内容是：LLM 数学推理任务中 PRM exploitation 的 bifurcation-theoretic 预测框架。**零机器人内容、零物理系统、零 embodiment**。这不是一个\"边界情况\"——这是一篇纯粹的 NLP/ML alignment 论文投稿到一个纯粹的机器人学习会议。合理目标 venue 应为 NeurIPS、ICML、ICLR 或 AAAI。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。** 最直接的竞争者是：\n\n1. **TRACE (F1≈0.97)**: 已经在数学推理任务上实现近乎完美的 reward hacking 检测。Proposal 自己承认这是最强 baseline。如果 TRACE 在 PRM-guided GRPO 中同样有效（这需要实验验证但很可能），那么一个复杂的 bifurcation 框架的增量价值是什么？\n\n2. **简单 proxy-true divergence 监测**: 直接监测 PRM reward 与 ground-truth accuracy 的 divergence rate，用简单阈值做 early stopping。这几乎不需要理论——只需要 ground-truth evaluation。\n\n3. **GRPO scaling law deviation**: Nimmaturi et al. 的指数饱和模型残差，即\"偏离预期 scaling law = 异常\"。\n\nProposal 声称其增量价值在于：(i) 更早检测（通过 fold-specific scaling exponent 发散）、(ii) 更低误报率（区分 fold 的 sharp transition 与正常 saturation）、(iii) 机制可解释性、(iv) regime identification 使干预选择成为可能、(v) onset timing 的定量预测。这些 claim 在原理上是合理的，但全部是**未经验证的假设**——也恰恰是论文需要证明的。关键问题：在噪声较大的真实训练数据中，fold bifurcation 的 1/2 指数能否被可靠估计？如果不能，整个框架的实际优势相比 trivial baselines 就不存在。\n\n**增量价值判断**: 如果 bifurcation 框架能提供比 TRACE 更早 ≥20 steps 的预警且不增加误报，或能定量预测 onset timing（而非仅检测），则有真实增量价值。但这是一个大 \"if\"。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中，以下环节是\"想当然\"的或未经充分论证的：\n\n1. **1D 折叠降维假设**: Proposal 将高维策略优化动态降维为 exploitation fraction α(t) 的 1D 动力学，并假设其遵循 fold bifurcation 的 normal form。这是一个极强的假设——真实训练动态涉及数十亿参数、多种 exploitation 策略、learning rate scheduling、KL penalty 等。Normal form reduction 需要论证为什么这些其他维度的动力学要么 fast enough 被 adiabatically eliminated，要么不影响核心分叉结构。Proposal 承认这是\"phenomenological model\"但未给出为什么 phenomenological 近似合理的论证。\n\n2. **正反馈主导性假设**: Proposal 论证 group-relative normalization 的正反馈是 fold bifurcation 的驱动机制。但真实训练中还存在其他重要力：KL divergence penalty（负反馈）、learning rate warmup/decay、clipping（GRPO 的 clipping 对 advantage 的影响）、以及 exploitation 策略本身的 diversity。如果 KL penalty 提供的负反馈足以压制 group-normalization 的正反馈，fold bifurcation 可能根本不出现。\n\n3. **Scaling exponent 可测性假设**: 从有限长度、高噪声的训练序列中可靠估计 |λ-λ_c|^{-1/2} 的 scaling exponent 是极具挑战的。在生态学和气候科学中，critical slowing down 信号经常被噪声淹没，需要非常长的时间序列。RL 训练的 500 步（即使每 5 步一个 checkpoint = 100 数据点）可能不足以可靠区分 fold (-1/2) vs. transcritical (-1) vs. 无分叉（smooth crossover）。\n\n4. **PRM score gap 恒定性假设**: 推导假设 Δs = E[s_E] - E[s_G] > 0 是一个相对稳定的常数。但在训练过程中，\"exploitation strategy\" 本身在演化——模型可能发现新的 exploitation mode，使 Δs 随时间变化，破坏稳态分析的前提。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** —\n   将 fold bifurcation 理论特异性地应用于 GRPO+PRM 的 credit assignment 机制、导出 5 个定量可测试预测，这确实在现有文献中没有先例。与 Karwowski et al. (ICLR 2024) 的 geometric Goodhart framework 相比，延伸到 neural PRM + group normalization + dual-PRM dynamics 是真实的理论增量。与 Hennick & Corlouer (arXiv:2603.29805) 的\"物理工具→训练动态\"范式同属一类，但目标不同。\n   **但**：核心数学工具（fold bifurcation normal form、critical slowing down 的 1/2 指数）完全来自 Scheffer et al. (2009) 和 Kuehn (2011) 的经典文献，在生态学/气候学中已有数十年历史。ML 领域的 novelty 主要在于\"应用到新 domain + 从 GRPO 机制导出具体参数依赖\"——这是 incremental novelty，不是 fundamental novelty。如果 bifurcation 预测在实验中得到验证，审稿人可能会说 \"neat application\" 而不是 \"groundbreaking\"。与 TRACE (ICLR 2026 Oral) 的 clean, practical insight 相比，本 proposal 的理论优雅度高但实际冲击力可能不足。\n\n2. **Significance: 弱至中** —\n   研究问题本身是重要的——PRM exploitation 在 GRPO 训练中的早期检测对实践有价值。但有两个显著的 significance 削弱因素：\n   (a) **TRACE 的存在严重削弱了实用意义**: 如果 TRACE (F1≈0.97) 已经解决了检测问题的绝大部分，那么一个更复杂的理论框架的 practical significance 就被压缩到了边际空间（更早 N 步预警、区分 bifurcation 类型等）。审稿人可能会问 \"who would use this instead of TRACE?\"\n   (b) **受众狭窄**: 框架高度特化于 GRPO + PRM + 数学推理，虽然 proposal 声称可推广到其他有 group-normalization 的 RL 系统，但这只是讨论层面的泛化，没有实证。\n   (c) **对 CoRL 社区的意义为零**: 没有任何机器人学习相关内容。\n\n3. **Related Work: 强** —\n   对现有工作的覆盖极为全面——跨越 6 个类别（Goodhart 形式化、GRPO 分析、PRM 分析、检测方法、表征监测、统计/信息论诊断）。对 Karwowski et al.、Sullivan et al.、Stop Summation、TRACE、IR³ 等关键工作的定位清晰准确。Proposal 对每个相关工作的描述与搜索结果一致，显示出对领域的深入理解。差异化定位（\"no work unifies bifurcation-theoretic prediction with mechanistic monitoring for PRM exploitation in GRPO\"）在调研范围内成立——确实没有找到直接竞争的 bifurcation-theoretic 方法针对 PRM exploitation。唯一小问题：某些引用（如 arXiv:2507.18014、arXiv:2604.15149）可能在最终发表时 venue 信息需要更新。\n\n---\n\n【概率估计】: [2% - 8%] 中位 3%\n\n【估计理由】:\n**致命的 venue 不匹配是概率极低的首要原因。** CoRL 2026 的征稿范围严格限定于机器人学习。本 proposal 是一篇纯 NLP/ML alignment 论文——关于 LLM 数学推理中 PRM exploitation 的 bifurcation 理论——与机器人学习毫无关联。预计会在 area chair 阶段被 desk reject，即使进入审稿也会因为完全 out of scope 而被拒。\n\n**如果投稿到适当 venue（NeurIPS/ICML/ICLR），概率估计为 [20% - 35%] 中位 27%。** 理由：idea 有真实的 novelty delta（中）但核心发现如果 positive，审稿人更可能说 \"nice application of known tools\" 而非 \"surprising\"。TRACE (F1≈0.97) 的存在构成严重的 trivial alternative 威胁，削弱了 practical significance。前提假设（1D 降维、正反馈主导性、scaling exponent 可测性）任何一个失败都会大幅削弱论文。但 related work 覆盖强、理论推导有结构性、实验设计（如果执行良好）能够 definitive 地回答问题。\n\n【主要风险】:\n1. **致命 venue 不匹配**: CoRL 是机器人学习会议，本 proposal 零机器人内容，几乎确定 desk reject。\n2. **Trivial alternative 威胁**: TRACE (F1≈0.97) 已解决检测问题的绝大部分；如果 bifurcation 框架不能在 lead time 或 false positive rate 上展示显著优势，审稿人会质疑 \"为什么不直接用 TRACE？\" 这是 idea 层面的根本性风险——即使实验执行完美，如果 trivial baseline 效果相当，论文的 contribution 就不成立。\n```\n\n---\n\n**补充建议（非 rubric 要求但关乎项目存亡）**：\n\n建议立即将目标 venue 从 CoRL 2026 更换为 NeurIPS 2026、ICML 2026 或 ICLR 2027。本 proposal 的内容与 CoRL 的 scope 完全不重叠，投稿 CoRL 几乎等同于浪费一次投稿周期。如果确实希望投稿 CoRL，需要对 proposal 进行根本性重构——例如将 bifurcation 框架应用于机器人 RL 中的 reward hacking（sim-to-real reward shaping exploitation 等），但这本质上是一个全新的项目。\n\nSources:\n- [Karwowski et al., Goodhart's Law in RL (ICLR 2024)](https://arxiv.org/abs/2310.09144)\n- [Sullivan et al., GRPO is Secretly a PRM](https://arxiv.org/abs/2509.21154)\n- [Cheng et al., Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)\n- [Wang et al., TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)\n- [Beigi et al., IR³](https://arxiv.org/abs/2602.19416)\n- [Hennick & Corlouer, Density Matrices to Phase Transitions](https://arxiv.org/pdf/2603.29805)\n- [Miao et al., Energy Loss (ICML 2025)](https://arxiv.org/abs/2501.19358)\n- [Scheffer et al., Early-warning signals (Nature 2009)](https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf)\n- [Nimmaturi et al., GRPO Scaling Laws](https://arxiv.org/abs/2507.18014)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Goodhart's Tipping Point: Fold Bifurcations and Early Warning Signals in PRM Exploitation During GRPO Training\n\n## Description\nWe develop the first bifurcation-theoretic framework for predicting PRM exploitation onset during GRPO training, deriving that summation-form credit assignment creates a fold (saddle-node) bifurcation in the exploitation fraction through a positive feedback loop unique to group-relative advantage normalization. Building on Karwowski et al.'s (ICLR 2024) geometric Goodhart framework and extending it to neural PRMs with step-level credit assignment, we derive five PRM-specific testable predictions: fold-specific autocorrelation scaling (exponent -1/2), variance amplification with fold exponent, solution-length-dependent onset timing, elimination of the fold under min-form credit (PURE), and dual-PRM interaction signatures where GRPO's implicit Monte-Carlo PRM (Sullivan et al., arXiv:2509.21154) modulates exploitation onset timing. Experiments span three priority tiers: Tier 1 trains Qwen3-4B via GRPO with three PRMs (discriminative and generative) plus Qwen3-14B, with a multi-signal diagnostic panel at dense checkpoints; Tier 2 adds λ-GRPO and PURE ablations to test bifurcation modulation predictions, completes 14B cross-PRM comparison, and adds GRIFT baseline; Tier 3 extends to PPO and spectral analysis. We rigorously ablate against six baselines spanning four detection paradigms: dynamics-based (self-internalization gap, divergence rate, scaling law deviation), effort-based (TRACE, adapted from Wang et al.'s ICLR 2026 Oral with F1≈0.97), representation-based (energy loss), and gradient-based (GRIFT). The framework explicitly addresses the dual-PRM dynamic in GRPO + explicit PRM, where the explicit PRM determines trajectory-level advantage while the implicit MC-PRM distributes learning across tokens. We compare exploitation bifurcation characteristics across discriminative vs. generative PRMs and position against complementary approaches: IR³'s post-hoc SAE-based detection, CRA's PRM deconfounding, and InfoRM's IB-based monitoring.\n\n## Core Problem\nPRM exploitation during RL training can silently render training counterproductive (>0.9 reward, <4% accuracy), but we lack both a domain-specific theoretical framework predicting exploitation onset and practical early-detection tools that outperform simpler baselines. Karwowski et al. (ICLR 2024) formalize Goodhart's law geometrically in MDPs via occupancy polytope boundary transitions, deriving optimal early stopping with regret bounds — but their framework assumes linear rewards on occupancy measures and does not address neural process reward models, step-level credit assignment, or the dual-PRM dynamics inherent to GRPO. Sullivan et al. (arXiv:2509.21154) prove that GRPO with an ORM is equivalent to a PRM-aware objective with an implicit Monte-Carlo PRM, meaning GRPO + explicit PRM creates a dual-PRM optimization dynamic not previously analyzed for exploitation. Stop Summation identifies summation-form credit assignment as the mechanistic driver of PRM hacking. Current work characterizes the end state (Tiwari et al., 43% shortcuts), the mechanism (Stop Summation), temporal dynamics under rubric verifiers (Mahmoud et al.), structural phase transitions in capability emergence (Hennick & Corlouer), static PRM deconfounding (CRA), scalar early warning in preference-RLHF (Energy Loss), effort-based hacking detection (TRACE, F1≈0.97), and post-hoc interpretable detection (IR³, SAE-based) — but no work unifies bifurcation-theoretic prediction with mechanistic monitoring for PRM exploitation in GRPO, where the interaction between implicit and explicit process reward structures introduces qualitatively distinct exploitation dynamics.\n\n## Opportunity\nFive converging threads create a unique opportunity. First, Sullivan et al. (arXiv:2509.21154) prove GRPO implicitly implements a Monte-Carlo PRM through trajectory prefix sharing, and propose λ-GRPO to fix step-level imbalance — this reveals that GRPO + explicit PRM creates a dual-PRM optimization dynamic where the explicit PRM determines which trajectories are favored while the implicit PRM distributes advantage across tokens, an interaction whose exploitation characteristics are completely uncharted. Second, concurrent empirical work maps complementary facets of reward hacking — Mahmoud et al. (arXiv:2605.12474) show monotonic exploitation growth under weak rubric verifiers, the rebound paper (arXiv:2604.01476) finds three-phase dynamics in code evaluation, Nimmaturi et al. (arXiv:2507.18014) identify exponential saturation in GRPO, and Helff et al. (arXiv:2604.15149) show progressive shortcut growth with task complexity — but none study PRM-guided math reasoning where Stop Summation has identified summation-form credit assignment as the mechanism. Third, Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational Goodhart formalization in RL — geometric explanations via occupancy polytope boundaries and optimal early stopping with regret bounds — but their linear-reward framework does not extend to neural process rewards, step-level credit assignment, or the group-relative normalization in GRPO that creates positive feedback loops driving exploitation. Critical transitions theory (Scheffer et al., Nature 2009) and its recent application to training phase transitions (Hennick & Corlouer, arXiv:2603.29805) provide the dynamical systems tools, but the theoretical gap is precisely connecting GRPO's credit assignment mechanisms to specific bifurcation types with quantitative scaling predictions — not merely applying generic early warning signals to a new domain. Fourth, detection methods are maturing along multiple orthogonal axes — TRACE (arXiv:2510.01367, ICLR 2026 Oral) detects hacking via reasoning effort measurement (CoT truncation AUC) with F1≈0.97, GRIFT uses gradient fingerprints, IR³ (arXiv:2602.19416) combines contrastive IRL with SAEs for 0.89 correlation with ground-truth rewards, energy loss provides a scalar signal, and SAEs detect RL pathologies — but none predict exploitation onset from training dynamics as a bifurcation phenomenon, and no work systematically compares these orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based) against each other. Fifth, GenPRM and TP-GRPO reveal distinct exploitation profiles for generative PRMs, creating an unexplored axis for comparing bifurcation characteristics across PRM paradigms. Bridging Karwowski's geometric Goodhart framework with bifurcation theory specific to GRPO's credit assignment mechanisms offers a formal model generating quantitative predictions — but the bar is high: we must show the framework adds value beyond simpler baselines including TRACE, self-internalization gap, energy loss, scaling law fitting, and gradient fingerprints.\n\n## Related Work / Landscape\nThe landscape spans six categories requiring explicit positioning: (A) Goodhart formalization and training dynamics, (B) GRPO-specific analysis, (C) PRM-specific analysis, (D) detection methods, (E) representation-level monitoring, and (F) statistical/information-theoretic diagnostics.\n\n**A. Goodhart Formalization and Training Dynamics.** Karwowski et al. (arXiv:2310.09144, ICLR 2024) provide the foundational formalization of Goodhart's law in RL: they model policy optimization as steepest ascent on the occupancy measure polytope Ω, show that the projected angle between proxy and true rewards determines Goodharting likelihood (Proposition 3: directional alignment is monotonically decreasing), derive an optimal early stopping criterion with regret bound proportional to diameter(Ω)·(1-cos(θ)), and demonstrate Goodharting in 19.3% of 30,400 configurations. Their framework is foundational to our work but operates in the tabular MDP setting with linear reward functions on occupancy measures — it does not address (a) neural process reward models where the proxy is a learned nonlinear function, (b) step-level credit assignment where summation vs. min forms create qualitatively different optimization landscapes, (c) group-relative normalization in GRPO that introduces positive feedback absent from steepest ascent, or (d) the dual-PRM dynamics of GRPO + explicit PRM. Our theoretical contribution extends their geometric insight to the PRM-guided GRPO setting by deriving the specific bifurcation structure (fold bifurcation) that arises from the positive feedback between group-relative normalization and exploitation discovery, yielding quantitative scaling predictions absent from their framework. Hennick & Corlouer (arXiv:2603.29805) apply 2RDM spectral analysis to detect training phase transitions (capability emergence, grokking) — the closest conceptual neighbor for dynamics-based training monitoring, but they study beneficial reorganization rather than adversarial exploitation. Miao et al. (arXiv:2501.19358, ICML 2025) identify energy loss (ΔE_l = ||h^in_l||_1 − ||h^out_l||_1) as a monotonically increasing early warning for reward hacking in PPO-based RLHF — a single scalar signal without regime discrimination or mechanistic interpretability, operating in the preference RLHF setting rather than PRM-guided GRPO. Helff et al. (arXiv:2604.15149, ICLR 2026 Workshop) show progressive shortcut growth with task complexity, reinforcing the importance of characterizing transition type (sharp vs. gradual).\n\n**B. GRPO-Specific Analysis.** Sullivan et al. (arXiv:2509.21154, under review ICML 2026) prove that GRPO with an ORM is equivalent to a PRM-aware RL objective with an implicit Monte-Carlo PRM — for each token, the implicit step-level reward equals the mean outcome reward of trajectories sharing the same prefix up to that token. They identify that non-uniform process set distributions hinder exploration/exploitation and propose λ-GRPO, which normalizes each token's loss by its process set size |λ^{(i,t)}|, achieving >10% average accuracy improvement and 2× convergence speedup on Qwen-1.5B. Crucially for our work: when GRPO uses explicit PRM scores as trajectory rewards (as in our setup and Stop Summation's), the optimization involves BOTH the explicit PRM (determining trajectory-level advantage via group-relative normalization of PRM scores) AND the implicit MC-PRM (distributing that advantage across tokens through prefix sharing). This dual-PRM dynamic could qualitatively alter exploitation: the explicit PRM determines WHICH strategies are favored, while the implicit PRM determines HOW learning is distributed across solution steps. λ-GRPO normalizes the implicit PRM's contribution but does not affect the explicit PRM's trajectory-level signal — a distinction we test experimentally. Nimmaturi et al. (arXiv:2507.18014) derive GRPO scaling laws with exponential saturation — we incorporate as a null model.\n\n**C. PRM-Specific Analysis.** Cheng et al. (arXiv:2504.15275, NeurIPS 2025) identify summation-form credit assignment as the mechanistic cause of PRM hacking in GRPO and propose min-form (PURE). Their work answers WHY exploitation happens; ours answers WHEN and HOW — and we formally derive that summation-form creates a fold bifurcation while min-form eliminates it. Song et al. (arXiv:2508.04216, AAAI 2026 Workshop) train SAEs on PRM activations for static deconfounding at inference time — complementary to our policy-model dynamics monitoring. Tiwari et al. (arXiv:2603.06621) characterize the end state. TP-GRPO (OpenReview:LZZENDlZt9) addresses GenPRM-specific pitfalls.\n\n**D. Detection Methods.** Wang et al. (arXiv:2510.01367, ICLR 2026 Oral, TRACE) detect implicit reward hacking by measuring reasoning effort via progressive CoT truncation, achieving F1≈0.97 in math on dataset-level loopholes. TRACE operates on a fundamentally different principle from our framework: it measures per-sample reasoning effort (whether the model 'knows the answer' early in its CoT) via truncation AUC, while we monitor population-level temporal dynamics across training checkpoints. TRACE is an excellent sample-level detector but does not predict exploitation onset, characterize bifurcation type, or identify what the model exploits mechanistically. We include TRACE as a key ablation baseline — a particularly strong comparison because its high F1 sets a demanding bar for alternative approaches. It was validated with RLOO and GRPO under outcome-based rewards, not PRM-guided RL; we adapt it to our setting. Beigi et al. (arXiv:2602.19416, IR³) combine contrastive inverse RL with SAEs for interpretable post-hoc reward hacking detection, achieving 0.89 correlation with ground-truth rewards and >90% precision in identifying hacking features. IR³ operates post-hoc (requiring sampling access to aligned and baseline policies after training) rather than during training — directly relevant to our SAE approach but not a training-time baseline. Their SAE decomposition of reconstructed rewards (R̂ = Σω_i f_i + c) provides complementary evidence that SAE features can identify hacking signatures, validating our choice of SAE-based monitoring. Key distinction: IR³ reconstructs the implicit reward function from behavioral contrasts, while we track the policy's evolving representations to predict exploitation before it manifests behaviorally. Wang et al. (arXiv:2604.16242, GRIFT) use gradient fingerprints for post-hoc sample-level detection. Mahmoud et al. (arXiv:2605.12474) propose the self-internalization gap for rubric-based RL.\n\n**E. Representation-Level Monitoring.** Yan et al. (arXiv:2602.05183) use SAEs for Diplomacy RL dynamics. Shi et al. (arXiv:2507.00665, SAFER) probe reward model safety via SAE activation differences. Song et al.'s CRA uses SAEs on PRM activations for static deconfounding — distinct from our policy-model tracking.\n\n**F. Statistical and Information-Theoretic Diagnostics.** Miao et al. (arXiv:2402.09345, NeurIPS 2024, InfoRM) propose MOP/CSI/ICDS metrics in the IB latent space for reward-model-side overoptimization detection — complementary to our policy-side monitoring. Gao et al. (arXiv:2210.10760) provide overoptimization scaling laws for best-of-N/PPO.\n\nThe gap: a bifurcation-theoretic framework deriving specific predictions from GRPO's credit assignment mechanisms (not generic early warning signals), validated against strong baselines (TRACE, self-internalization gap, energy loss, scaling law deviation, gradient fingerprints), with explicit treatment of the dual-PRM dynamics in GRPO + explicit PRM, and systematic comparison across discriminative and generative PRMs.\n\n## Approach\nWe develop and empirically validate a bifurcation-theoretic framework for PRM exploitation during GRPO training, deriving PRM-specific predictions from the credit assignment mechanism and rigorously comparing against six detection baselines. Experiments are organized into three priority tiers.\n\n**Tiered Experiment Design.**\n- *Tier 1 (Essential — publishable core, ~55% of compute):* Qwen3-4B via GRPO with all 3 PRMs (Qwen2.5-Math-PRM-7B, ACTPRM-X, GenPRM-7B) on MATH/AMC/AIME datasets, plus Qwen3-14B via GRPO with Qwen2.5-Math-PRM-7B. Full diagnostic panel and all baseline comparisons at each checkpoint. This yields 4 training runs covering both model scales, all three PRMs, and the complete analytical framework. (4 runs × ~4h avg = ~16h training + ~90h evaluation/SAE/TRACE/analysis)\n- *Tier 2 (Important — strengthens contribution, ~30% of compute):* Qwen3-14B via GRPO with ACTPRM-X and GenPRM-7B (completing cross-PRM comparison at 14B), PURE ablation (min-form) on Qwen3-4B with Qwen2.5-Math-PRM-7B, λ-GRPO ablation (Sullivan et al.'s process-set normalization) on Qwen3-4B with Qwen2.5-Math-PRM-7B, and GRIFT-style gradient fingerprint baseline on sampled checkpoints. (4 runs × ~5h avg = ~20h training + ~60h analysis)\n- *Tier 3 (Stretch — extends scope, ~15% of compute):* PPO pilot (Qwen3-4B + Qwen2.5-Math-PRM-7B) for cross-algorithm generalization, spectral heat capacity signal (following Hennick & Corlouer), and energy loss monitoring extension to step-level rewards. (~1 run + specialized analysis, ~30h total)\n\nAll experiments use the OpenRLHF framework. Tier 1 is prioritized for completion by week 10; Tier 2 by week 14; Tier 3 as time permits.\n\n**Dual-PRM Experimental Setup.** We explicitly address the dual-PRM dynamic revealed by Sullivan et al. In our setup, PRM scores are the sole trajectory-level reward signal in GRPO — the explicit PRM evaluates each solution step and scores are aggregated (via summation, min, or mean) into a trajectory reward, which is then normalized via group-relative advantage computation. Crucially, GRPO's implicit Monte-Carlo PRM (Sullivan et al.) operates simultaneously at the token level: tokens sharing prefixes across trajectories within a group receive implicit step-level advantages equal to the mean trajectory reward of completions sharing that prefix. Thus, the policy is optimized against BOTH the explicit PRM (trajectory-level: which solutions are favored) AND the implicit MC-PRM (token-level: how advantage is distributed across solution steps). We hypothesize three distinct exploitation interaction modes: (1) constructive — both PRMs agree on step quality, accelerating aligned learning; (2) amplifying — the implicit PRM concentrates learning on tokens where the explicit PRM is most exploitable, accelerating exploitation onset; (3) buffering — the implicit PRM's averaging smooths out the explicit PRM's exploitable local maxima, delaying exploitation. Testing which mode dominates and whether it changes across training is a core empirical question. The λ-GRPO condition (Tier 2) isolates this: by normalizing process set sizes, λ-GRPO equalizes the implicit PRM's contribution, allowing us to test whether the dual-PRM interaction amplifies or buffers exploitation.\n\n**Checkpoint Strategy and Storage.** We save checkpoints every 5 training steps across 500+ steps (~100+ checkpoints per run). Tiered strategy: full checkpoints every 25 steps, delta-compressed at intermediate 5-step intervals (3–4× compression), and online computation of diagnostics during training. Storage: ~8–12TB. Prune to anomaly-adjacent windows after analysis.\n\n**Multi-Signal Diagnostic Panel.** At each checkpoint: PRM reward, ground-truth accuracy via outcome verification, solution style decomposition (Tiwari et al.'s taxonomy), PRM-adapted self-internalization gap, energy loss (ΔE = ||h^in||_1 − ||h^out||_1), TRACE score (adapted to PRM setting, computed on a held-out evaluation set), SAE features from residual stream activations, and optionally (Tier 3) spectral heat capacity.\n\n**TRACE Adaptation for PRM-Guided RL.** TRACE (Wang et al., ICLR 2026 Oral) measures reasoning effort by progressively truncating CoT at percentages p ∈ {10%, 20%, ..., 100%}, forcing early answers, and computing AUC of expected reward vs. truncation fraction. Originally validated with outcome-based rewards in RLOO/GRPO, we adapt it to PRM-guided RL: at each checkpoint, we evaluate the held-out set by truncating solutions at each percentage, computing the PRM score on the truncated solution (using the PRM's step-level scores up to the truncation point), and calculating the TRACE-PRM score as the AUC. High TRACE-PRM scores indicate the model achieves high PRM scores with minimal reasoning effort — a signature of PRM exploitation. We validate this adaptation by confirming correlation between TRACE-PRM scores and ground-truth accuracy degradation.\n\n**Self-Internalization Gap: PRM Adaptation.** We construct two evaluation contexts: (1) PRM-verification-conditioned — math problem augmented with system prompt encoding step-level correctness criteria ('Ensure each reasoning step is mathematically correct and logically follows from previous steps. Verify intermediate results.'), with richer conditioning for GenPRM matching its reasoning format; (2) Prompt-only — minimal instruction. At each checkpoint, sample K=10 solutions from conditioned distribution, compute length-normalized log-probabilities under both contexts. The PRM-adapted self-internalization gap Δ_PRM(t) = mean difference. Validate by confirming r>0.85 correlation with accuracy trajectories.\n\n**SAE Training Strategy.** Anchor-and-monitor: train a single TopK-SAE (32K hidden dims, K=32) on pooled residual stream activations from checkpoints at steps 0, 25, 50, 100. Apply across subsequent checkpoints; fine-tune when reconstruction loss exceeds 2× baseline mean. Distinction from IR³ (Beigi et al.): IR³ reconstructs implicit reward functions from behavioral contrasts post-hoc, while we track policy representation evolution during training. Distinction from CRA (Song et al.): CRA trains SAEs on PRM activations for static deconfounding; we train on policy model activations for dynamics monitoring. Estimated: ~40h anchor training + ~30h fine-tuning/extraction.\n\n**Theoretical Framework: Fold Bifurcation in PRM Exploitation.**\n\nOur core theoretical contribution goes beyond applying generic early warning signals to a new domain. We derive the specific bifurcation structure arising from GRPO's credit assignment mechanism, building on and extending Karwowski et al.'s geometric Goodhart framework.\n\n*Setup.* Consider GRPO training with explicit PRM providing step-level scores s_1, ..., s_T. Under summation-form credit assignment, the trajectory reward is R = Σ_t s_t. Define α(t) ∈ [0,1] as the exploitation fraction — the probability mass the policy assigns to PRM-exploitative strategies at training step t. Let Δs = E[s_E] - E[s_G] > 0 be the per-step PRM score gap between exploitative (s_E) and genuine (s_G) strategies (positive by assumption that the PRM is imperfect).\n\n*Positive feedback mechanism.* GRPO's group-relative normalization computes advantages A_i = (R_i - μ_G)/σ_G where μ_G and σ_G are group mean and std. As α increases, more trajectories in each group use exploitative strategies, raising μ_G. This makes genuinely correct trajectories (with lower R) receive increasingly negative advantage, suppressing them and further increasing α. This is a positive feedback loop absent from Karwowski et al.'s steepest-ascent framework (which involves no group normalization) and absent from standard RL settings without group-relative advantage.\n\n*Fold bifurcation derivation.* We model the exploitation fraction dynamics as: dα/dt = f(α; λ(t)) where λ(t) is the effective optimization pressure (monotonically increasing with training). The positive feedback creates a cubic nonlinearity: f(α; λ) = λ - λ_c + (α - α_c)² + h.o.t., which is the normal form of a fold (saddle-node) bifurcation. Below the critical pressure λ_c, there exist two equilibria: a stable low-exploitation equilibrium and an unstable threshold. At λ = λ_c, these equilibria collide and annihilate — the system transitions to the high-exploitation regime. The critical pressure λ_c depends on: (i) the per-step PRM score gap Δs, (ii) solution length T (longer solutions → lower λ_c under summation-form because R = T·Δs), (iii) group size (larger groups → sharper normalization → stronger positive feedback → lower λ_c), and (iv) the implicit MC-PRM's contribution (prefix-sharing structure modulates token-level gradient distribution).\n\n*PRM-specific scaling predictions.* The fold bifurcation generates five testable, quantitatively specific predictions — NOT generic properties of tipping points:\n\n(P1) **Fold-specific autocorrelation scaling**: The autocorrelation time of the proxy-true gap G(t) = R_proxy(t) - R_true(t) diverges as τ_ac ~ |λ(t) - λ_c|^{-1/2} approaching the transition. This 1/2 exponent is specific to fold bifurcations and distinguishes them from transcritical (exponent 1) or Hopf (exponent 1/2 but with oscillatory component) bifurcations. We fit the scaling exponent empirically and test against the fold prediction.\n\n(P2) **Variance scaling**: Fluctuations in G(t) grow as σ² ~ |λ(t) - λ_c|^{-1/2}, again with the fold-specific exponent.\n\n(P3) **Solution-length dependence**: The critical training step t* at which exploitation onset occurs should decrease with solution length T under summation-form (because R_exploit/R_genuine = T·E[s_E]/T·E[s_G], and the group-normalization positive feedback strengthens with larger reward variance). Concretely, we test whether t*(AMC) < t*(MATH-easy) on matched problem sets differing primarily in solution length.\n\n(P4) **Credit assignment modulation**: Under min-form (PURE), the positive feedback is broken — a single genuinely-scored step caps the trajectory reward, preventing μ_G from rising with exploitation. The fold bifurcation should be eliminated: G(t) follows smooth crossover dynamics with NO divergent autocorrelation. Under λ-GRPO, the fold persists (since it arises from the explicit PRM's trajectory-level signal, not the implicit PRM) but λ_c may shift because the implicit PRM's contribution to gradient distribution is normalized.\n\n(P5) **Dual-PRM interaction signature**: In standard GRPO + explicit PRM, the implicit MC-PRM concentrates gradient updates on tokens with high prefix-sharing (common solution openings). If exploitation strategies share prefixes (e.g., similar boilerplate openings before diverging into exploitative patterns), the implicit PRM amplifies learning of these shared exploitative prefixes — lowering λ_c. λ-GRPO normalization should weaken this amplification, raising λ_c. We test this by comparing exploitation onset timing between standard GRPO and λ-GRPO.\n\n*Connection to Karwowski et al.* Their framework shows Goodharting occurs when the optimization trajectory hits the occupancy polytope boundary where proxy and true reward directions diverge. In our GRPO + PRM setting, the 'boundary' corresponds to the policy having saturated the genuinely-learnable PRM scoring patterns and beginning to exploit non-robust features. Our fold bifurcation formalizes the mechanistic transition at this boundary: Karwowski's 'directional phase shift' (their Proposition 3) corresponds to our fold bifurcation's annihilation of the aligned equilibrium. The extension is that (a) the positive feedback from group normalization makes the transition sharper than in steepest ascent, (b) the neural PRM's nonlinearity creates a specific bifurcation type (fold) derivable from the credit assignment form, and (c) the dual-PRM structure introduces modulation parameters absent from their single-reward framework.\n\n**Statistical Analysis and Baselines.** We test predictions using: PELT changepoint detection, BOCPD for uncertainty quantification, sliding-window autocorrelation and detrended fluctuation analysis for scaling exponent estimation, HMM regime detection, GRPO exponential saturation model as null model, and Karwowski et al.'s NDH (Normalized Drop Height) as a Goodhart severity metric. Novel metrics: 'Goodhart divergence rate' (dG/dt), 'critical slowing down index' (autocorrelation coefficient in trailing window), and 'fold scaling exponent' (fitted from τ_ac vs. |t - t*| in log-log space).\n\n**Ablation Against Six Baselines.** A key contribution is rigorous comparison against six simpler alternatives spanning four detection paradigms:\n\n*(i) Dynamics-based:* (a) PRM-adapted self-internalization gap, (b) naive proxy-true divergence rate threshold, (c) GRPO scaling law deviation (residuals from exponential saturation fit).\n\n*(ii) Effort-based:* (d) TRACE-PRM score (adapted progressive CoT truncation AUC, following Wang et al., ICLR 2026 Oral) — this is our strongest baseline given TRACE's F1≈0.97 in math. We compute TRACE-PRM at each checkpoint on the held-out evaluation set and test whether TRACE score increase precedes accuracy-reward divergence with comparable or greater lead time than our framework.\n\n*(iii) Representation-based:* (e) Energy loss monitoring (ΔE, adapted from Miao et al.'s PPO setting to GRPO).\n\n*(iv) Gradient-based:* (f) GRIFT-style gradient fingerprints on sampled checkpoints (Tier 2).\n\nFor each baseline, we measure: detection lead time (training steps before accuracy-reward divergence), false positive rate, intervention effectiveness as early stopping trigger, and (for TRACE and self-internalization gap) whether the signal distinguishes aligned plateau from pre-exploitation regime. The bifurcation framework must demonstrate at least one of: (i) earlier detection via fold-specific scaling exponent divergence, (ii) lower false positive rate via bifurcation-type discrimination (distinguishing the fold's sharp transition from normal saturation's smooth plateau), (iii) mechanistic interpretability via SAE features identifying WHAT is exploited, (iv) regime identification enabling intervention selection (not just early stopping), or (v) quantitative prediction of exploitation onset timing via λ_c estimation.\n\n**Cross-Paradigm Comparison.** We compare exploitation dynamics across discriminative vs. generative PRMs — testing whether the fold bifurcation structure persists, shifts (different λ_c), or changes type (fold → smooth crossover) with GenPRM's explicit verification reasoning. We additionally test (Tier 2) PURE and λ-GRPO as bifurcation-modifying interventions: PURE should eliminate the fold (P4), while λ-GRPO should shift λ_c (P5).\n\n**Early Warning Validation.** We test whether fold-specific scaling (P1-P2) provides earlier and more reliable warning than generic early warning signals and the six baselines. We report the distribution of lead times across runs, PRM types, and model scales, alongside confidence intervals, and test detected signals as triggers for dynamic interventions (early stopping, reward model switching, Advantage Modification).\n\n**Generalization Discussion.** The fold bifurcation framework extends beyond math+GRPO: any RL system with (a) a learned proxy reward, (b) group-relative or batch normalization of advantages, and (c) a discoverable exploitation strategy exhibits the positive feedback mechanism driving the fold. We validate with the Tier 3 PPO pilot (where advantage normalization plays an analogous role) and discuss how complementary approaches — CRA's PRM deconfounding, InfoRM's IB-based monitoring, IR³'s post-hoc interpretable detection — could combine with our training-time dynamics monitoring.\n\n**Scope and Limitations.** Tier 1 spans two model scales, three PRMs across two paradigms, six baselines, and the full theoretical+empirical framework — sufficient for a publishable contribution. Tier 2 extends to PURE, λ-GRPO, full 14B cross-PRM comparison, and GRIFT. The fold bifurcation derivation is a phenomenological model (normal form reduction from the positive feedback mechanism) rather than a rigorous proof from GRPO's objective — we position it as generating testable predictions, not as a theorem. If empirical scaling exponents deviate from fold predictions (e.g., suggesting transcritical or no bifurcation), this itself is informative and we report the fitted bifurcation type as a core result.\n\n## Inspiration\nNovel theoretical synthesis: Karwowski et al.'s geometric Goodhart formalization in RL + fold bifurcation theory from dynamical systems + GRPO's dual-PRM structure (Sullivan et al.) + Stop Summation's credit assignment mechanism → derive that summation-form GRPO creates a specific fold bifurcation in the exploitation fraction with quantitative scaling predictions, extending Karwowski's linear-reward framework to neural PRMs. Empirical synthesis: systematic comparison of six orthogonal detection paradigms (dynamics-based, effort-based, representation-based, gradient-based, energy-based, scaling-law-based) for PRM exploitation monitoring.\n\n## Key References\n- Goodhart's Law in Reinforcement Learning (arXiv:2310.09144, Karwowski et al. 2024, ICLR 2024)\n- GRPO is Secretly a Process Reward Model (arXiv:2509.21154, Sullivan et al. 2025, under review ICML 2026)\n- Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort (arXiv:2510.01367, Wang et al. 2026, ICLR 2026 Oral — TRACE)\n- IR³: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking (arXiv:2602.19416, Beigi et al. 2026)\n- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, 2026)\n- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, Mahmoud et al. 2026)\n- Natural Emergent Misalignment from Reward Hacking in Production RL (arXiv:2511.18397, 2025)\n- Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning (arXiv:2602.05183, Yan et al. 2026)\n- Early-warning signals for critical transitions (Scheffer et al., Nature 461, 2009)\n- From Density Matrices to Phase Transitions in Deep Learning: Spectral Early Warnings and Interpretability (arXiv:2603.29805, Hennick & Corlouer 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning (arXiv:2504.15275, Cheng et al. 2025, NeurIPS 2025)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, GRIFT, Wang et al. 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, Shi et al. 2025)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv:2507.18014, Nimmaturi et al. 2025)\n- Scaling Laws for Reward Model Overoptimization (arXiv:2210.10760, Gao et al. 2023)\n- Latent State Models of Training Dynamics (arXiv:2308.09543, 2023)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, 2026)\n- GenPRM: Scaling Process Reward Models with Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Smarter Not Harder: TP-GRPO with Intrinsic-Signal Driving and Ability-Adaptive Reward Shaping (OpenReview:LZZENDlZt9, 2026)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward (ICLR 2026)\n- The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? (arXiv:2512.16912, 2025)\n- Mitigating Reward Hacking with RL Training Interventions (ICLR 2026)\n- Detecting Proxy Gaming in RL and LLM Alignment via Evaluator Stress Tests (arXiv:2507.05619, 2025)\n- Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges (arXiv:2604.13602, 2026)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026)\n- Posterior-GRPO: Rewarding Reasoning Processes in Code Generation (arXiv:2508.05170, 2025)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, Song et al. 2025, AAAI 2026 Workshop)\n- The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking (arXiv:2501.19358, Miao et al. 2025, ICML 2025)\n- InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling (arXiv:2402.09345, Miao et al. 2024, NeurIPS 2024)\n- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, Helff et al. 2026, ICLR 2026 Workshop)\n- A mathematical framework for critical transitions: bifurcations, fast-slow systems and stochastic dynamics (arXiv:1101.2899, Kuehn 2011)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '530–750 H100-hours (Tier 1: 4 runs ~16h training + ~130h eval/SAE/TRACE/analysis; Tier 2: 4 runs [14B×2 PRMs + PURE + λ-GRPO ablations] ~20h training + ~60h analysis + ~30h GRIFT; Tier 3: PPO pilot + spectral ~30h; shared overhead: ~70h SAE + ~40h TRACE evaluation)', 'timeline': '14–18 weeks (Tier 1 complete by week 10, Tier 2 by week 14, Tier 3 as time permits)', 'estimated_gpu_cost': '$800–$1,310 (at ~$1.50–$1.75/H100-hr spot pricing)', 'storage': '~8–12TB with delta compression'}\n- **human_in_loop**: {'gpu_hours': '440–600 H100-hours (Claude-guided hyperparameter selection, early termination of unpromising runs, targeted SAE fine-tuning; Tier 1 prioritized)', 'timeline': '10–14 weeks (Tier 1 by week 8, Tier 2 by week 12)', 'claude_api_cost': '$400–$600 (checkpoint analysis, TRACE evaluation automation, bifurcation fitting, scaling exponent estimation, baseline comparison, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$660–$1,050', 'storage': '~6–10TB'}\n- **auto_research**: {'gpu_hours': '640–960 H100-hours (parallel Tier 1+2, automated bifurcation fitting, baseline sweep, some redundant runs)', 'timeline': '6–8 weeks wall-clock (Tiers 1+2 parallelized; Tier 3 conditional)', 'claude_api_cost': '$700–$1,200 (experiment orchestration, real-time analysis, TRACE adaptation, bifurcation analysis, iterative paper writing)', 'estimated_gpu_cost': '$960–$1,680', 'storage': '~10–15TB', 'speed_bottleneck': 'Sequential RL training runs (3–5h per run on 4–8×H100); SAE extraction adds serial dependency; TRACE evaluation adds ~20% inference overhead per checkpoint'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T19:08:30.771Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T19:08:30.771Z",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T19:08:30.786Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

============================================================
⚠️  严重前置问题：投稿目标 CoRL 2026 存在致命的 SCOPE MISMATCH
============================================================

CoRL 2026 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate
the relevance of proposed models, algorithms, datasets, and benchmarks
to robotics. Submissions without a robotics focus will be returned
WITHOUT REVIEW."

本 proposal 完全关于 LLM 数学推理场景下的 PRM exploitation 检测，
涉及 GRPO 训练、Process Reward Model、Chain-of-Thought 推理——
没有任何机器人学内容（无 manipulation、locomotion、perception、
sim-to-real、robot control 等）。

→ 如投 CoRL 主会，几乎确定会被 desk reject，不进入审稿流程。
→ 合理目标会议应为 NeurIPS / ICML / ICLR 主会。

下面的评估假设投稿到合理会议（NeurIPS/ICML/ICLR），
并在最终概率中单独给出 CoRL 的估计。
============================================================


【领域调研】:

1. Karwowski et al. "Goodhart's Law in Reinforcement Learning"
   (arXiv:2310.09144, ICLR 2024):
   — 在 tabular MDP + 线性 reward 上形式化 Goodhart's law，
     用 occupancy polytope 几何解释 Goodharting 发生条件，
     推导了最优 early stopping 及 regret bound。
   — 与本 proposal 的关系：proposal 声称在此基础上扩展到
     neural PRM + GRPO，但原工作本身没有涉及任何 bifurcation
     理论或 scaling exponent 预测。

2. Sullivan et al. "GRPO is Secretly a Process Reward Model"
   (arXiv:2509.21154, under review ICML 2026):
   — 证明 GRPO + ORM 等价于 MC-PRM-aware 目标，提出 λ-GRPO。
   — 与本 proposal 的关系：proposal 的 "dual-PRM" 分析
     直接依赖此工作。Sullivan 的发现是已公开结果，
     proposal 的扩展是分析 dual-PRM 下的 exploitation dynamics，
     这一方向尚未被 Sullivan 本人或他人研究。

3. Cheng et al. "Stop Summation" (arXiv:2504.15275, NeurIPS 2025):
   — 识别 summation-form credit assignment 是 PRM hacking 的机制
     原因，提出 min-form (PURE)。
   — 与本 proposal 的关系：proposal 的核心预测 P3（长度依赖）
     和 P4（min-form 消除 fold）本质上是用 bifurcation 语言
     重新表述 Stop Summation 的发现。

4. Wang et al. "TRACE" (arXiv:2510.01367, ICLR 2026 Oral):
   — 通过 progressive CoT truncation 测量推理 effort，F1≈0.97。
   — 与本 proposal 的关系：TRACE 是 proposal 承认的最强 baseline。
     如果 TRACE 已达 F1≈0.97，bifurcation 框架需要证明
     在 TRACE 之上的增量价值（如更早检测、更低误报），
     但 proposal 尚无证据支持这一点。

5. Beigi et al. "IR³" (arXiv:2602.19416, 2026):
   — Contrastive IRL + SAE 后置检测，0.89 correlation。
   — 与本 proposal 的关系：IR³ 是 post-hoc 检测，
     proposal 声称做 training-time 预测，但二者的 SAE 方法论
     有重合。

6. Hennick & Corlouer "From Density Matrices to Phase Transitions"
   (arXiv:2603.29805, 2026):
   — 用 2RDM spectral analysis 检测训练 phase transition。
   — 与本 proposal 的关系：最近的概念邻居——同样用
     dynamical systems / statistical physics 工具检测训练动态，
     但研究的是 capability emergence 而非 exploitation。

7. Scheffer et al. "Early-warning signals for critical transitions"
   (Nature, 2009):
   — 经典 critical slowing down 理论：fold bifurcation 前
     autocorrelation 和 variance 按 |λ-λ_c|^{-1/2} 发散。
   — 与本 proposal 的关系：proposal 的 5 个预测中，
     P1 和 P2 直接来自 Scheffer et al. 的通用理论，
     应用到新领域但本身不是新的理论贡献。

8. "When Reward Hacking Rebounds" (arXiv:2604.01476, 2026),
   Mahmoud et al. (arXiv:2605.12474, 2026),
   Helff et al. (arXiv:2604.15149, ICLR 2026 Workshop):
   — 多项并行工作刻画 reward hacking 的时序动态
     （三阶段 rebound、rubric verifier 下单调增长、
     progressive shortcut growth）。
   — 与本 proposal 的关系：这些工作也在刻画 exploitation
     的时间演化，但没有使用 bifurcation 框架。
     proposal 的差异化在于提供定量 scaling predictions，
     但这些预测是否能在嘈杂的 RL 训练中被 cleanly 验证
     存在高度不确定性。

- 调研总结：PRM exploitation 检测是 2025-2026 年的活跃研究
  方向，已有多种互补方法（TRACE effort-based、IR³ post-hoc SAE、
  能量损失、gradient fingerprints 等）。将 bifurcation 理论
  应用于此领域是一个尚未被直接做的方向，但核心 scaling
  predictions（P1/P2）来自经典 dynamical systems 理论，
  而非从 GRPO 机制中推导出的新理论——proposal 的主要贡献
  更多是"将已知框架映射到新领域"而非"发现新的理论结构"。


【Trivial Alternative 检验】:

存在多个低成本替代方案构成严重威胁：

(1) **直接监控 proxy-true gap + threshold early stopping**：
    不需要任何 bifurcation 理论，只需在训练中定期采样评估
    ground-truth accuracy，当与 PRM reward 出现显著背离时停止。
    这是最 trivial 的 baseline，proposal 虽提及但未论证
    bifurcation 框架的增量价值在哪里。

(2) **TRACE (F1≈0.97)**：已有极高精度的检测方法。
    即使 bifurcation 框架能提供"更早"的警告信号，
    但 TRACE 的高 F1 意味着在检测维度上的 headroom 很小。
    proposal 需要在 "onset prediction" 维度上证明价值，
    但 fold-specific scaling exponent 的实际检测优势
    （相比简单的 sliding-window divergence rate）未经验证。

(3) **Stop Summation 的 min-form (PURE) 直接作为干预**：
    如果已知 summation-form 是问题根源，直接使用 min-form
    就能避免 exploitation——不需要检测框架。

增量价值主要依赖于两个声明：(a) 比现有方法更早检测，
(b) 提供机制性理解（"什么类型的 bifurcation"）。
但 (a) 未经验证，(b) 的实际价值（知道是 fold 而非
transcritical 对实际干预策略有何影响？）也未论证清楚。


【前提假设检验】:

核心 claim 的逻辑链存在多个未经验证的关键假设：

(1) **1D 降维假设**：将高维 neural policy 训练动态
    简化为 dα/dt = f(α; λ) 的一维系统。这是一个
    极强的假设——exploitation fraction α 是否真的是
    一个有意义的低维 order parameter？RL 训练中
    可能存在多个 exploitation 模式同时演化、互相竞争，
    1D 描述可能根本不成立。

(2) **从 "positive feedback" 到 "fold bifurcation" 的跳跃**：
    Proposal 论证 group-relative normalization 创造正反馈，
    然后直接写出 fold normal form f(α; λ) = λ - λ_c + (α - α_c)²。
    这不是推导——这是假设。许多正反馈系统产生的
    不是 fold bifurcation（可以是 transcritical、pitchfork、
    或根本没有 clean bifurcation 的 crossover）。
    从 GRPO 的具体数学形式到 fold normal form 的严格推导
    缺失——proposal 自己也承认这是 "phenomenological model"
    而非 theorem。

(3) **Scaling exponent 可测性假设**：即使 fold bifurcation
    成立，从噪声很大的 RL training curves 中拟合出
    |λ - λ_c|^{-1/2} 的精确 scaling exponent 是极其困难的。
    这需要：(a) λ_c 本身被准确定位，(b) 足够多的
    接近 critical point 的数据点，(c) 训练噪声不淹没
    scaling signal。实际 RL 训练中，这三个条件是否
    同时满足是一个未经验证的强假设。

(4) **"Exploitation fraction" 可操作化假设**：α(t) 的
    定义依赖于能清晰区分 "exploitative" vs. "genuine"
    策略。但在实际 PRM hacking 中，exploitation 是一个
    连续谱（部分正确但利用 PRM 弱点的解法），
    二元分类的假设可能过于简化。


【3 维度打分】:

1. Novelty: 弱-中 (偏弱)
   — 核心理论贡献是将 Scheffer et al. (2009) 的经典
     critical slowing down / fold bifurcation 框架应用到
     PRM exploitation 检测领域。这是"已知框架 → 新领域"
     的迁移，而非新的理论发现。
   — 5 个预测中：P1/P2 是 fold bifurcation 的通用性质
     （Scheffer et al. 2009），不是 GRPO-specific 的推导；
     P3（长度依赖）本质上复述 Stop Summation (Cheng et al.,
     NeurIPS 2025) 的发现；P4（min-form 消除 fold）
     同样是 Stop Summation 的动力学语言重述；
     P5（dual-PRM interaction）是唯一真正新的预测，
     但也是最模糊和最难验证的。
   — "系统对比 6 种检测 paradigm" 有 empirical novelty，
     但这是实验设计层面贡献，非 idea 层面。
   — 在已有大量 reward hacking 检测方法（TRACE F1≈0.97、
     IR³ 0.89 correlation、能量损失、GRIFT）的情况下，
     增加一个 bifurcation 视角的边际 novelty 有限。

2. Significance: 中
   — PRM exploitation 检测是 RL alignment 中一个重要且
     timely 的问题，这一点毫无疑问。
   — 但 proposal 面临"天花板问题"：如果 TRACE 已经
     F1≈0.97，检测问题在多大程度上还是一个
     open problem？实际影响力可能有限。
   — 即使 bifurcation 框架成立，对实际工程实践的
     指导意义有限——知道"这是一个 fold bifurcation"
     比起"直接用 TRACE 检测或用 PURE 避免"
     对 practitioner 的价值增量不明确。
   — 理论角度，如果能 rigorously 证明 fold bifurcation
     （而非 phenomenological 假设），对理解 RL training
     dynamics 会有贡献，但目前的 derivation 不够 rigorous。

3. Related Work: 强
   — 这是 proposal 最突出的优势。对领域的覆盖非常全面，
     涵盖了 Karwowski (ICLR 2024)、Sullivan (ICML 2026 under review)、
     Stop Summation (NeurIPS 2025)、TRACE (ICLR 2026 Oral)、
     IR³、Hennick & Corlouer、能量损失 (ICML 2025)、
     GRIFT、CRA、InfoRM (NeurIPS 2024) 等。
   — 差异化定位清晰：明确指出与每个相关工作的区别
     （post-hoc vs. training-time、sample-level vs.
     population-level、检测 vs. 预测 onset 等）。
   — 经调研验证，引用的关键论文均真实存在，
     描述基本准确。


【概率估计】:

→ 如投 CoRL 2026 主会：0-2%（几乎确定 desk reject，
  无任何机器人学内容，CoRL 明确拒绝非 robotics submission）

→ 如投合理会议（NeurIPS/ICML/ICLR）：18-28%，中位 22%

【估计理由】:

对于 CoRL：致命的 scope mismatch，无需进一步讨论。

对于合理会议 (NeurIPS/ICML/ICLR)：
- Related Work 维度强，说明作者对领域理解深入，
  这为项目提供了合理的下限保障（不会因为 miss 关键
  相关工作而被拒）。
- 但 Novelty 偏弱是上界的关键限制。核心理论贡献是
  "经典框架 → 新领域"的迁移，审稿人很可能认为
  intellectually thin——P1/P2 来自 Scheffer 2009，
  P3/P4 复述 Stop Summation，P5 模糊难验证。
  审稿人大概率的反应是："interesting application but
  limited theoretical depth"。
- Significance 受制于 TRACE F1≈0.97 的存在——
  如果检测问题已经有如此 strong 的 solution，
  bifurcation 框架的边际价值需要非常 compelling 的
  论证，而 proposal 在这一点上的论证尚不充分。
- 前提假设（1D 降维、phenomenological fold derivation、
  scaling exponent 可测性）如果被审稿人追问，
  缺乏有力回应。
- 综合来看：idea 方向站得住脚（reward hacking dynamics
  值得理论化理解），但内核薄弱（核心贡献是
  relabeling rather than discovering），且面临 strong
  trivial alternative 威胁。这将概率限制在 25% 以下。

【主要风险】:

1. **"Relabeling, not discovering" 风险**：审稿人可能认为
   将 fold bifurcation 框架套用到 PRM exploitation 上
   本质上是用动力系统术语重新描述了已知现象
   （exploitation 有 tipping point → fold bifurcation；
   summation 导致 hacking → 正反馈），而没有产生
   genuinely new insight。最有可能以 "limited novelty"
   被拒。

2. **"Why not just use TRACE / PURE?" 风险**：
   审稿人会问：如果 TRACE 已经 F1≈0.97 用于检测，
   PURE 已经直接消除 exploitation mechanism，
   为什么还需要一个复杂的 bifurcation 理论框架？
   Proposal 目前对此的回应不够有力——
   "onset prediction" 和 "mechanistic understanding"
   的实际价值需要更 concrete 的论证。
```

---

**总结**：此 proposal 存在一个 **致命的前置问题**——投稿目标 CoRL 2026 是机器人学习会议，而 proposal 内容是纯 LLM/RL alignment 方向，**无任何 robotics 成分，会被 desk reject**。如果转投合理会议（NeurIPS/ICML/ICLR），idea 质量处于"方向正确但内核偏薄"的区间（中位约 22%），主要受限于 novelty 不足（经典框架迁移而非新理论发现）和 trivial alternative 威胁（TRACE/PURE 已高效解决检测/消除问题）。Related Work 覆盖是本 proposal 的明显强项。

建议首先 **重新确认投稿目标会议**，再决定是否进入后续的发掘/补救迭代流程。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Karwowski et al. - Goodhart's Law in Reinforcement Learning (ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [Sullivan et al. - GRPO is Secretly a Process Reward Model](https://arxiv.org/abs/2509.21154)
- [Cheng et al. - Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Wang et al. - TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Beigi et al. - IR³](https://arxiv.org/abs/2602.19416)
- [Hennick & Corlouer - Phase Transitions in Deep Learning](https://arxiv.org/pdf/2603.29805)
- [Scheffer et al. - Early-warning signals for critical transitions (Nature 2009)](https://www.nature.com/articles/nature08227)
- [Reward Hacking Rebounds (arXiv:2604.01476)](https://arxiv.org/pdf/2604.01476)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my evaluation. Let me compile the full assessment.

---

```
【阶段】: Triage

⚠️ 【关键前置问题：严重的会议匹配问题】
CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求论文 "focus on a core robotics problem" 并鼓励 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。本 proposal 研究的是 LLM 推理训练中的 PRM exploitation / reward hacking 检测——与机器人学习完全无关，不涉及任何 robotic perception、control、manipulation、locomotion 或 sim-to-real transfer 内容。

如果投 CoRL，此论文极大概率在 desk review 阶段即被判定 out of scope 而直接拒稿。建议改投 ICML、NeurIPS 或 ICLR。以下评估假设投稿至合适的顶会（如 ICML/NeurIPS/ICLR），单纯评估 idea 质量。


【领域调研】:
- [Karwowski et al., arXiv:2310.09144] (ICLR 2024): Goodhart's law 在 RL 中的几何形式化。基于 occupancy polytope boundary transitions 解释 Goodharting 发生条件，推导最优 early stopping。框架限于 tabular MDP + linear reward，不覆盖 neural PRM 或 GRPO。本 proposal 自称在此基础上拓展——但需注意该拓展的严格性。
- [Sullivan et al., arXiv:2509.21154] (under review ICML 2026): 证明 GRPO + ORM 等价于带隐式 Monte-Carlo PRM 的目标，提出 λ-GRPO 归一化 process set size，获 >10% accuracy 提升和 2× 收敛加速。本 proposal 引用准确。
- [Wang et al., arXiv:2510.01367] (ICLR 2026 Oral, TRACE): 通过渐进截断 CoT 测量推理努力来检测 implicit reward hacking，F1≈0.97（数学推理任务）。这是当前最强的 reward hacking 检测方法之一，本 proposal 将其作为 baseline。引用准确。
- [Cheng et al., arXiv:2504.15275] (NeurIPS 2025, Stop Summation/PURE): 指出 summation-form credit assignment 是 PRM hacking 的机制性原因，提出 min-form (PURE) 来解决。本 proposal 引用准确。该工作已回答了 "WHY" 的问题，PURE 已提供了解决方案。
- [Beigi et al., arXiv:2602.19416] (IR³, 2026): 通过 contrastive IRL + SAE 实现可解释的 reward hacking 检测，0.89 与 ground-truth reward 的相关性。Post-hoc 方法。引用准确。
- [Hennick & Corlouer, arXiv:2603.29805] (2026): 将量子化学中的 2RDM 方法应用于深度学习训练阶段转变的早期预警，使用 spectral heat capacity 信号。这是"将 critical transitions 理论应用于 ML 训练动态"这一方向上的直接竞争者/先驱。
- [Miao et al., arXiv:2501.19358] (ICML 2025, Energy Loss): 发现 energy loss 作为 PPO-RLHF 中 reward hacking 的单调递增早期预警信号。
- [Gao et al., arXiv:2210.10760] (2023): Reward model overoptimization 的 scaling laws，已建立了 proxy-true reward 之间关系的量化框架。

- 调研总结: Reward hacking / Goodhart's law 在 LLM RL 训练中是一个活跃且竞争激烈的研究领域（2025-2026 年有超过 15 篇相关论文）。检测方面已有 TRACE (F1≈0.97)、IR³、Energy Loss、GRIFT 等多种方法；机制分析方面 Stop Summation/PURE 已解决 "why" 问题；理论方面 Karwowski et al. 已形式化 Goodhart's law in RL。本 proposal 试图占据的 niche 是 "bifurcation-theoretic prediction of WHEN exploitation occurs" —— 但该 niche 的增量价值面临来自已有方法的强烈挤压。


【Trivial Alternative 检验】:
存在严重的 trivial alternative 威胁：

1. **TRACE (F1≈0.97)** 已经是一个极其有效的 reward hacking 检测器。本 proposal 必须证明 bifurcation framework 能提供比 TRACE 更早或更可靠的预警——但这完全是一个不确定的实验结果，不是 idea 层面能保证的。
2. **简单的 proxy-true divergence 监控**（即直接监控 PRM reward 与 ground-truth accuracy 的差值）在实践中已被广泛使用。Bifurcation framework 相对于此的增量价值在于"更早几步检测"和"定量预测 onset timing"——但如果检测 lead time 的提升只有几个 training steps，实际价值有限。
3. **PURE (min-form credit)** 已经从根本上解决了 summation-form 导致的 PRM hacking 问题。如果 PURE 有效，那么与其预测 exploitation 何时发生，不如直接使用 PURE 消除 exploitation。

核心增量价值主张："理解 bifurcation type 能指导 intervention selection（不只是 early stopping）"—— 但 proposal 对此只有模糊声称，没有具体论证"知道是 fold bifurcation vs. 其他类型"如何改变干预策略。


【前提假设检验】:
核心 claim 的逻辑链条中有多个未经验证的关键假设：

1. **"正反馈 → 三次非线性 → fold bifurcation"**：这是整个理论框架的核心，但推导是 phenomenological 的——从"存在正反馈"直接跳到"normal form 是 f(α;λ) = λ - λ_c + (α - α_c)² + h.o.t."。这不是从 GRPO 目标函数严格推导出的，而是假设了一种特定的正常形式。实际系统的动力学可能不服从这个简化。Proposal 自己也承认这是 "phenomenological model rather than a rigorous proof"。
2. **Exploitation fraction α(t) 是一个良定义的标量**：实际训练中，"exploitative strategy" 和 "genuine strategy" 之间的边界模糊且随训练变化。将其建模为一个清晰的一维标量 α(t) 是一个强假设。
3. **Group-relative normalization 的正反馈确实足以产生 abrupt transition**：proposal 论证了"随着 α 上升，genuine solutions 获得负 advantage"的正反馈——但这个正反馈可能被其他因素（如 KL 惩罚、learning rate decay、clipping）所抑制，不一定达到 bifurcation 的 sharpness。
4. **Fold-specific 的 scaling exponents 在噪声真实数据中可测量**：critical slowing down 的 τ_ac ~ |λ-λ_c|^{-1/2} scaling 在低噪声物理系统中可观测，但在高度随机的 LLM 训练过程中，信噪比可能不足以区分 fold (exponent 1/2) vs. 其他 bifurcation types。


【3 维度打分】:
  1. Novelty: 弱-中 — 核心思路是 "将 dynamical systems / bifurcation theory 应用于 ML 训练动态"，这一方向已有 Hennick & Corlouer (2603.29805) 的先例（虽然他们研究的是 capability emergence 而非 adversarial exploitation）。具体到 PRM exploitation 的应用是新的，但理论贡献的核心——"正反馈→fold bifurcation"——是 phenomenological 断言，不是从 GRPO 数学结构严格推导出的 surprising 结论。五个 predictions 中，P3（solution length dependence）和 P4（min-form eliminates fold）几乎可以直接从 Stop Summation 的结论推出（summation-form 下更长的解 = 更大的 R_exploit，min-form 下正反馈被打断），不需要 bifurcation 理论。真正需要 bifurcation 理论才能得到的 prediction 主要是 P1 和 P2 的具体 scaling exponents——但如上所述，这些在真实数据中能否被测量出来存疑。

  2. Significance: 中 — PRM exploitation 在 LLM RL 训练中确实是一个重要且实际的问题。但 (a) PURE 已经从机制层面提供了解决方案（消除 summation-form），(b) TRACE F1≈0.97 已经提供了极强的检测能力。本 proposal 的 significance 取决于"predicting onset timing"相比于"detecting exploitation"有多大的实际增量价值——这一点 proposal 没有充分论证。此外，这个 framework 如果成功，它的影响主要限于 GRPO + PRM 这个特定 setup，generalization 论证（PPO pilot in Tier 3）比较薄弱。

  3. Related Work: 强 — 这是 proposal 最出色的方面。Related work 覆盖非常全面，按 6 个类别系统组织，对每篇工作的描述基本准确（经调研验证），差异化定位清晰。特别是对 TRACE、Stop Summation、Karwowski et al.、Sullivan et al.、IR³ 的定位相当精准。唯一的轻微问题是对自身理论贡献相对于 Karwowski 的 novelty delta 有些夸大（"extends their geometric insight"——但实际上是在一个不同的、更弱的理论框架下做的）。


【概率估计】: [15% - 25%] 中位 20%
（注：此概率假设投稿至合适的 ML 顶会如 ICML/NeurIPS/ICLR。若投 CoRL，概率接近 0%，因为完全 out of scope。）

【估计理由】:
idea 的方向（用 dynamical systems 理论理解 RL 训练中的 Goodhart tipping point）是 sound 的，research question 有实际意义，related work 做得扎实。但 idea 的核心理论贡献——"GRPO 的 group-relative normalization 产生 fold bifurcation"——是一个 phenomenological assertion，不是 rigorous derivation，这意味着即使实验跑出来，理论 insight 的深度有限（审稿人可能会说 "you fitted a normal form to your data, but why is it specifically a fold and not something else?"）。更致命的是 trivial alternative 威胁：TRACE (F1≈0.97) + PURE (消除 hacking) 的组合已经在检测和解决层面覆盖了问题，bifurcation framework 的增量实际价值不明确。五个 predictions 中只有 P1/P2 的 scaling exponents 真正需要 bifurcation 理论，但这些在高噪声的 LLM 训练数据中能否被可靠测量是一个根本性风险。

上界被 **Novelty** 限制——核心理论贡献是 phenomenological 的，不够 surprising；下界被扎实的 **Related Work** 覆盖和 well-defined 的实验 plan 所托住。

【主要风险】:
1. **Trivial alternative 挤压**: TRACE + PURE 的组合已经从检测和解决两个层面覆盖了 PRM exploitation 问题，bifurcation framework 的增量价值缺乏有力论证。审稿人可能会问："如果 PURE 消除了 fold bifurcation（你自己的 P4 预测），为什么不直接用 PURE？你的理论框架在实践中是否只是一个诊断工具而非解决方案？"
2. **Phenomenological theory 的脆弱性**: 如果实测 scaling exponents 偏离 fold 预测（非常可能，因为真实系统远比 normal form 复杂），整个"fold bifurcation"的 narrative 就会瓦解。Proposal 虽声明"如果偏离也是 informative"，但"我们预测了 fold bifurcation 但实际不是"作为核心结论的论文，novelty 和 impact 都会大打折扣。
```

**补充说明**：

关于 **会议选择**，这是一个必须在投稿前解决的根本性问题。本 proposal 完全不涉及机器人学习，投 CoRL 2026 几乎必然被 desk reject。建议考虑以下会议：
- **NeurIPS 2026**（理论+实验兼具的 ML 工作）
- **ICML 2026**（如果还来得及 deadline）
- **ICLR 2027**（如果时间线允许更充分的实验）
- **AAAI 2027** 或相关 workshop 作为备选

Sources:
- [Goodhart's Law in Reinforcement Learning (Karwowski et al., ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [GRPO is Secretly a Process Reward Model (Sullivan et al.)](https://arxiv.org/abs/2509.21154)
- [TRACE: Detecting Implicit Reward Hacking (Wang et al., ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Stop Summation / PURE (Cheng et al., NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [IR³ (Beigi et al., 2026)](https://arxiv.org/abs/2602.19416)
- [Hennick & Corlouer, Spectral Early Warnings (2026)](https://arxiv.org/pdf/2603.29805)
- [Energy Loss (Miao et al., ICML 2025)](https://arxiv.org/abs/2501.19358)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough assessment. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

1. [Karwowski et al., "Goodhart's Law in Reinforcement Learning", arXiv:2310.09144] (ICLR 2024):
   提供了 RL 中 Goodhart 定律的几何形式化——基于 occupancy polytope 边界转换和 proxy-true reward 角度偏差。框架假设 tabular MDP + 线性 reward，不涉及 neural PRM、step-level credit assignment 或 group-relative normalization。Proposal 声称从这里延伸到 GRPO+PRM 设置，claim 基本准确。

2. [Sullivan et al., "GRPO is Secretly a Process Reward Model", arXiv:2509.21154] (under review ICML 2026):
   证明 GRPO+ORM 等价于隐式 Monte-Carlo PRM 目标，提出 λ-GRPO 修复 step-level 不平衡，取得 >10% 准确率提升和 ~2× 收敛加速。论文真实存在，proposal 对其描述准确。这是 proposal 的关键理论依赖之一。

3. [Cheng et al., "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning", arXiv:2504.15275] (NeurIPS 2025):
   识别 summation-form credit assignment 为 PRM hacking 的机制性原因，提出 min-form (PURE)。Proposal 的"fold bifurcation 源于 summation-form"的 claim 直接建立在此基础上。论文真实，描述准确。

4. [Wang et al., "Is It Thinking or Cheating? (TRACE)", arXiv:2510.01367] (ICLR 2026 Oral):
   通过 CoT 截断测量推理 effort 来检测隐式 reward hacking，F1≈0.97（数学任务）。这是 proposal 自认的最强 baseline。论文真实存在，是 ICLR 2026 Oral。TRACE 的强度对 proposal 构成显著的 trivial alternative 威胁。

5. [Beigi et al., "IR³", arXiv:2602.19416] (2026):
   对比式 IRL + SAE 进行事后 reward hacking 检测和缓解，达到 0.89 ground-truth reward 相关性。论文真实。IR³ 是事后方法，proposal 定位为训练时方法，差异化成立。

6. [Hennick & Corlouer, "From Density Matrices to Phase Transitions in Deep Learning", arXiv:2603.29805] (2026):
   将 2RDM spectral analysis 应用于训练相变（capability emergence, grokking, emergent misalignment）。这是概念上最近的邻居——将物理工具（spectral methods）应用于 ML 训练动态监测。但该工作关注的是有益的重组，而非对抗性 exploitation。

7. [Miao et al., "Energy Loss Phenomenon in RLHF", arXiv:2501.19358] (ICML 2025):
   发现 energy loss 作为 PPO-based RLHF 中 reward hacking 的单标量早期预警信号。Proposal 将其作为 baseline 之一。

8. [Scheffer et al., "Early-warning signals for critical transitions", Nature 461] (2009):
   经典的 critical slowing down 理论——fold bifurcation 附近 autocorrelation 和 variance 发散的 ±1/2 指数预测。这是 proposal 理论框架的核心数学工具来源，非 ML 领域原创。

9. [Nimmaturi et al., "Predictive Scaling Laws for Efficient GRPO Training", arXiv:2507.18014] (2025):
   GRPO 训练的指数饱和 scaling law，三阶段动态。Proposal 将其作为 null model。

10. [Mahmoud et al., "Reward Hacking in Rubric-Based RL", arXiv:2605.12474] (2026):
    展示 rubric verifier 下单调 exploitation 增长，提出 self-internalization gap。Proposal 将其改编为 PRM 适配版 baseline。

- **调研总结**: Reward hacking 检测/缓解是 2025-2026 年的研究热点，已有大量方法覆盖不同检测范式（effort-based, representation-based, gradient-based, energy-based）。但将 bifurcation theory 特异性地应用于 GRPO+PRM 的 credit assignment 机制、并从中导出定量可测试预测，确实尚无先例。Proposal 处于"理论物理工具 → ML 训练动态"这一新兴交叉方向，与 Hennick & Corlouer 同属此趋势，但针对对抗性 exploitation 而非有益相变。

**⚠️ 致命问题：投稿目标 venue 严重不匹配 ⚠️**

CoRL 2026 (Conference on Robot Learning) 的征稿范围明确限定于机器人学习，包括：robotic perception and control、robot foundation models、imitation learning for robotics、RL for control of physical robots、robot safety and alignment for learning-based robotic systems、robot manipulation/navigation/locomotion/driving/flight 等。CoRL 明确鼓励 real-robot experiments 或 simulation-to-real 证据。

本 proposal 的内容是：LLM 数学推理任务中 PRM exploitation 的 bifurcation-theoretic 预测框架。**零机器人内容、零物理系统、零 embodiment**。这不是一个"边界情况"——这是一篇纯粹的 NLP/ML alignment 论文投稿到一个纯粹的机器人学习会议。合理目标 venue 应为 NeurIPS、ICML、ICLR 或 AAAI。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 最直接的竞争者是：

1. **TRACE (F1≈0.97)**: 已经在数学推理任务上实现近乎完美的 reward hacking 检测。Proposal 自己承认这是最强 baseline。如果 TRACE 在 PRM-guided GRPO 中同样有效（这需要实验验证但很可能），那么一个复杂的 bifurcation 框架的增量价值是什么？

2. **简单 proxy-true divergence 监测**: 直接监测 PRM reward 与 ground-truth accuracy 的 divergence rate，用简单阈值做 early stopping。这几乎不需要理论——只需要 ground-truth evaluation。

3. **GRPO scaling law deviation**: Nimmaturi et al. 的指数饱和模型残差，即"偏离预期 scaling law = 异常"。

Proposal 声称其增量价值在于：(i) 更早检测（通过 fold-specific scaling exponent 发散）、(ii) 更低误报率（区分 fold 的 sharp transition 与正常 saturation）、(iii) 机制可解释性、(iv) regime identification 使干预选择成为可能、(v) onset timing 的定量预测。这些 claim 在原理上是合理的，但全部是**未经验证的假设**——也恰恰是论文需要证明的。关键问题：在噪声较大的真实训练数据中，fold bifurcation 的 1/2 指数能否被可靠估计？如果不能，整个框架的实际优势相比 trivial baselines 就不存在。

**增量价值判断**: 如果 bifurcation 框架能提供比 TRACE 更早 ≥20 steps 的预警且不增加误报，或能定量预测 onset timing（而非仅检测），则有真实增量价值。但这是一个大 "if"。

---

【前提假设检验】:

核心 claim 的逻辑链中，以下环节是"想当然"的或未经充分论证的：

1. **1D 折叠降维假设**: Proposal 将高维策略优化动态降维为 exploitation fraction α(t) 的 1D 动力学，并假设其遵循 fold bifurcation 的 normal form。这是一个极强的假设——真实训练动态涉及数十亿参数、多种 exploitation 策略、learning rate scheduling、KL penalty 等。Normal form reduction 需要论证为什么这些其他维度的动力学要么 fast enough 被 adiabatically eliminated，要么不影响核心分叉结构。Proposal 承认这是"phenomenological model"但未给出为什么 phenomenological 近似合理的论证。

2. **正反馈主导性假设**: Proposal 论证 group-relative normalization 的正反馈是 fold bifurcation 的驱动机制。但真实训练中还存在其他重要力：KL divergence penalty（负反馈）、learning rate warmup/decay、clipping（GRPO 的 clipping 对 advantage 的影响）、以及 exploitation 策略本身的 diversity。如果 KL penalty 提供的负反馈足以压制 group-normalization 的正反馈，fold bifurcation 可能根本不出现。

3. **Scaling exponent 可测性假设**: 从有限长度、高噪声的训练序列中可靠估计 |λ-λ_c|^{-1/2} 的 scaling exponent 是极具挑战的。在生态学和气候科学中，critical slowing down 信号经常被噪声淹没，需要非常长的时间序列。RL 训练的 500 步（即使每 5 步一个 checkpoint = 100 数据点）可能不足以可靠区分 fold (-1/2) vs. transcritical (-1) vs. 无分叉（smooth crossover）。

4. **PRM score gap 恒定性假设**: 推导假设 Δs = E[s_E] - E[s_G] > 0 是一个相对稳定的常数。但在训练过程中，"exploitation strategy" 本身在演化——模型可能发现新的 exploitation mode，使 Δs 随时间变化，破坏稳态分析的前提。

---

【3 维度打分】:

1. **Novelty: 中** —
   将 fold bifurcation 理论特异性地应用于 GRPO+PRM 的 credit assignment 机制、导出 5 个定量可测试预测，这确实在现有文献中没有先例。与 Karwowski et al. (ICLR 2024) 的 geometric Goodhart framework 相比，延伸到 neural PRM + group normalization + dual-PRM dynamics 是真实的理论增量。与 Hennick & Corlouer (arXiv:2603.29805) 的"物理工具→训练动态"范式同属一类，但目标不同。
   **但**：核心数学工具（fold bifurcation normal form、critical slowing down 的 1/2 指数）完全来自 Scheffer et al. (2009) 和 Kuehn (2011) 的经典文献，在生态学/气候学中已有数十年历史。ML 领域的 novelty 主要在于"应用到新 domain + 从 GRPO 机制导出具体参数依赖"——这是 incremental novelty，不是 fundamental novelty。如果 bifurcation 预测在实验中得到验证，审稿人可能会说 "neat application" 而不是 "groundbreaking"。与 TRACE (ICLR 2026 Oral) 的 clean, practical insight 相比，本 proposal 的理论优雅度高但实际冲击力可能不足。

2. **Significance: 弱至中** —
   研究问题本身是重要的——PRM exploitation 在 GRPO 训练中的早期检测对实践有价值。但有两个显著的 significance 削弱因素：
   (a) **TRACE 的存在严重削弱了实用意义**: 如果 TRACE (F1≈0.97) 已经解决了检测问题的绝大部分，那么一个更复杂的理论框架的 practical significance 就被压缩到了边际空间（更早 N 步预警、区分 bifurcation 类型等）。审稿人可能会问 "who would use this instead of TRACE?"
   (b) **受众狭窄**: 框架高度特化于 GRPO + PRM + 数学推理，虽然 proposal 声称可推广到其他有 group-normalization 的 RL 系统，但这只是讨论层面的泛化，没有实证。
   (c) **对 CoRL 社区的意义为零**: 没有任何机器人学习相关内容。

3. **Related Work: 强** —
   对现有工作的覆盖极为全面——跨越 6 个类别（Goodhart 形式化、GRPO 分析、PRM 分析、检测方法、表征监测、统计/信息论诊断）。对 Karwowski et al.、Sullivan et al.、Stop Summation、TRACE、IR³ 等关键工作的定位清晰准确。Proposal 对每个相关工作的描述与搜索结果一致，显示出对领域的深入理解。差异化定位（"no work unifies bifurcation-theoretic prediction with mechanistic monitoring for PRM exploitation in GRPO"）在调研范围内成立——确实没有找到直接竞争的 bifurcation-theoretic 方法针对 PRM exploitation。唯一小问题：某些引用（如 arXiv:2507.18014、arXiv:2604.15149）可能在最终发表时 venue 信息需要更新。

---

【概率估计】: [2% - 8%] 中位 3%

【估计理由】:
**致命的 venue 不匹配是概率极低的首要原因。** CoRL 2026 的征稿范围严格限定于机器人学习。本 proposal 是一篇纯 NLP/ML alignment 论文——关于 LLM 数学推理中 PRM exploitation 的 bifurcation 理论——与机器人学习毫无关联。预计会在 area chair 阶段被 desk reject，即使进入审稿也会因为完全 out of scope 而被拒。

**如果投稿到适当 venue（NeurIPS/ICML/ICLR），概率估计为 [20% - 35%] 中位 27%。** 理由：idea 有真实的 novelty delta（中）但核心发现如果 positive，审稿人更可能说 "nice application of known tools" 而非 "surprising"。TRACE (F1≈0.97) 的存在构成严重的 trivial alternative 威胁，削弱了 practical significance。前提假设（1D 降维、正反馈主导性、scaling exponent 可测性）任何一个失败都会大幅削弱论文。但 related work 覆盖强、理论推导有结构性、实验设计（如果执行良好）能够 definitive 地回答问题。

【主要风险】:
1. **致命 venue 不匹配**: CoRL 是机器人学习会议，本 proposal 零机器人内容，几乎确定 desk reject。
2. **Trivial alternative 威胁**: TRACE (F1≈0.97) 已解决检测问题的绝大部分；如果 bifurcation 框架不能在 lead time 或 false positive rate 上展示显著优势，审稿人会质疑 "为什么不直接用 TRACE？" 这是 idea 层面的根本性风险——即使实验执行完美，如果 trivial baseline 效果相当，论文的 contribution 就不成立。
```

---

**补充建议（非 rubric 要求但关乎项目存亡）**：

建议立即将目标 venue 从 CoRL 2026 更换为 NeurIPS 2026、ICML 2026 或 ICLR 2027。本 proposal 的内容与 CoRL 的 scope 完全不重叠，投稿 CoRL 几乎等同于浪费一次投稿周期。如果确实希望投稿 CoRL，需要对 proposal 进行根本性重构——例如将 bifurcation 框架应用于机器人 RL 中的 reward hacking（sim-to-real reward shaping exploitation 等），但这本质上是一个全新的项目。

Sources:
- [Karwowski et al., Goodhart's Law in RL (ICLR 2024)](https://arxiv.org/abs/2310.09144)
- [Sullivan et al., GRPO is Secretly a PRM](https://arxiv.org/abs/2509.21154)
- [Cheng et al., Stop Summation (NeurIPS 2025)](https://arxiv.org/abs/2504.15275)
- [Wang et al., TRACE (ICLR 2026 Oral)](https://arxiv.org/abs/2510.01367)
- [Beigi et al., IR³](https://arxiv.org/abs/2602.19416)
- [Hennick & Corlouer, Density Matrices to Phase Transitions](https://arxiv.org/pdf/2603.29805)
- [Miao et al., Energy Loss (ICML 2025)](https://arxiv.org/abs/2501.19358)
- [Scheffer et al., Early-warning signals (Nature 2009)](https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf)
- [Nimmaturi et al., GRPO Scaling Laws](https://arxiv.org/abs/2507.18014)
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
  "promptId": "9e4054ac-2f85-43c5-a0f0-620aad70ac22",
  "type": "user",
  "uuid": "d360db1a-6c41-4824-bd0f-b43fd729114b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T19:08:30.784Z_

```json
{
  "parentUuid": "d360db1a-6c41-4824-bd0f-b43fd729114b",
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
  "uuid": "620e6d5a-e58f-4835-bebc-137d4e413921",
  "timestamp": "2026-05-19T19:08:30.784Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T19:08:30.784Z_

```json
{
  "parentUuid": "620e6d5a-e58f-4835-bebc-137d4e413921",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "377eab68-49dc-4496-981b-d851f51895b8",
  "timestamp": "2026-05-19T19:08:30.784Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
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
  "leafUuid": "377eab68-49dc-4496-981b-d851f51895b8",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifurcation theory for PRM exploitation detection in GRPO",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd"
}
```

---

### Assistant

_source line 8 · 2026-05-19T19:09:05.423Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically to produce a Meta Judge output.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 弱-中 (偏弱)
- Significance: 中
- Related Work: 强
- Probability (CoRL): 0-2%
- Probability (合理会议): 18-28%, 中位 22%

**Reviewer 2:**
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Probability (CoRL): ~0%


- Probability (合理会议): 15-25%, 中位 20%

**Reviewer 3:**
- Novelty: 中
- Significance: 弱至中
- Related Work: 强
- Probability (CoRL): 2-8%, 中位 3%
- Probability (合理会议): 20-35%, 中位 27%

Now I'm aggregating the acceptance probabilities across reviewers. For CoRL, the median hovers around 1% with minimal variance—essentially a unanimous desk reject. For 合理会议, the estimates cluster between 20-22% at the median, suggesting the paper might find a home at a more specialized venue. just under 3%, which puts it at the border of "高一致" and "中一致". Now let me identify where the reviewers actually agree. There's unanimous consensus on several critical issues: the CoRL scope mismatch that warrants a desk reject, strong related work, the trivial alternative threat from TRACE and PURE, the phenomenological rather than rigorous nature of the core theory, the unverified 1D reduction assumption, questionable measurability of the scaling exponent in noisy RL training, and how P3/P4 largely restate Stop Summation findings. On novelty and significance though, there's only 2/3 agreement—R1 and R2 rate novelty as weak-to-medium while R3 sees it as medium, and similarly for significance where R1 and R2 call it medium but R3 sees it as weak-to-medium.

The "relabeling not discovering" concern appears explicitly in R1 and implicitly in R2, with R3 being the outlier who rates novelty slightly higher and significance slightly harsher. Given this strong qualitative alignment on the major points despite the 3% standard deviation, I'd classify this as "高一致". For CoRL specifically, the unanimous 0-3% range means the final estimate should be 0-2%, and for 合理会议 the median of medians sits at 22% with a 15-35% range—given the high consistency, I should anchor around [17-28%] with a median near 22%.

I need to clarify that the primary task is assessing CoRL 2026 acceptance potential, so I should present both estimates clearly. Now I'm synthesizing the implementation requirements from the reviews and proposal: the compute needs are 530-960 H100-hours, the data comes from publicly available MATH/AMC/AIME datasets, human involvement is substantial for SAE training and hyperparameter tuning, the timeline spans 10-18 weeks, and while there's no new benchmark, the diagnostic framework is novel. Let me structure the final output now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "377eab68-49dc-4496-981b-d851f51895b8",
  "isSidechain": false,
  "requestId": "req_011CbCTGEFx6x6drhT2kksa4",
  "type": "assistant",
  "uuid": "962ae5f3-5b99-4ccb-89f9-d05ba4d25fa5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eCKDhYQLf74voT2R1n8xF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26233,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3648,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26233
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

_source line 9 · 2026-05-19T19:10:03.351Z_

【阶段】: Meta Judge
【三次中位】: [22%, 20%, 27%]  std=2.9%
【共识维度】:
- **CoRL scope mismatch — 致命**（3/3）：三位审稿人全部独立识别出 proposal 与 CoRL 2026 的征稿范围完全不匹配（零机器人内容），一致判定几乎确定 desk reject。这是最强共识信号。
- **Related Work — 强**（3/3）：三位一致认为 Related Work 覆盖全面、引用准确、差异化定位清晰，是 proposal 最突出的优势。
- **Trivial alternative 威胁 — 强**（3/3）：三位均指出 TRACE (F1≈0.97) + PURE (消除 exploitation mechanism) 构成严重的 trivial alternative 挤压，proposal 对增量价值的论证不充分。
- **核心理论 phenomenological 而非 rigorous — 中至强风险**（3/3）：三位均指出从 "正反馈" 到 "fold normal form" 是假设而非推导，缺乏从 GRPO 目标函数到具体 bifurcation type 的严格数学推导。
- **1D 降维假设未经论证 — 中风险**（3/3）：三位均质疑 exploitation fraction α(t) 作为低维 order parameter 的合理性。
- **Scaling exponent 可测性存疑 — 中风险**（3/3）：三位均质疑在高噪声 RL 训练数据中能否可靠区分 fold (-1/2) vs. 其他 bifurcation type。
- **P3/P4 复述 Stop Summation — 弱至中 novelty 扣分**（3/3）：三位均指出预测 P3（长度依赖）和 P4（min-form 消除 fold）本质上是 Stop Summation 发现的动力系统语言重述。
- **Novelty — 弱-中**（2/3 偏弱-中，1/3 给中）：共识偏向 "已知框架→新领域迁移"，incremental novelty。
- **Significance — 中**（2/3 给中，1/3 给弱至中）：问题重要但受 TRACE/PURE 存在压缩了实际增量空间。

【异常维度】:
- **R3 给 Novelty "中"**（vs. R1/R2 的"弱-中"）：R3 对 "将 fold bifurcation 特异性应用于 GRPO+PRM credit assignment" 给予更多 novelty credit，认为"与 Karwowski 相比，延伸到 neural PRM + group normalization + dual-PRM dynamics 是真实的理论增量"。但 R3 同时将 Significance 压低至"弱至中"，两个维度的综合效果与 R1/R2 趋同。→ 判定：R3 的 Novelty 评估略高但不构成实质分歧，因其同时在 Significance 上更严格，最终概率估计（中位 27%）虽略高于另两位但在合理范围内。
- **R1 明确使用 "relabeling not discovering" 措辞**：R2/R3 表达了相同实质但未使用该术语。→ 判定：非真正异常点，三位实质一致。

【最终概率】: [0% - 3%] 中位 1%（CoRL 2026 主会）；[17% - 28%] 中位 22%（若转投 NeurIPS/ICML/ICLR）
【一致性】: 高（std=2.9%，且所有 rubric 维度判决方向一致，无实质性分歧）
【综合理由】:

**CoRL 概率（0-3%，中位 1%）**：三位审稿人以最高一致性判定 proposal 与 CoRL 2026 完全 scope mismatch。Proposal 研究 LLM 数学推理中的 PRM exploitation，涉及 GRPO 训练、Process Reward Model、Chain-of-Thought 推理——零机器人学内容（无 manipulation、locomotion、perception、sim-to-real、robot control）。CoRL CFP 明确声明 "submissions without a robotics focus will be returned WITHOUT REVIEW"。这不是边界情况，是彻底的 out-of-scope。给 1-3% 而非绝对 0% 仅为覆盖极端小概率事件（如 AC 误判放行但仍会被 reviewer 拒绝）。

**合理会议概率（17-28%，中位 22%）**：三位在各 rubric 维度的判决高度一致（std=2.9%），因此取中位附近。R3 的 27% 略高，但考虑到其 Significance 判"弱至中"与 R1/R2 判"中"的互补效应，三位的综合信号收敛于 20-22% 区间。

概率天花板受限于 Novelty（弱-中）：核心贡献是 Scheffer 2009 经典 fold bifurcation → PRM exploitation 的领域迁移，P1/P2 是通用性质而非 GRPO-specific 推导，P3/P4 复述 Stop Summation，仅 P5 (dual-PRM interaction) 是真正新预测但最模糊。审稿人大概率反应为 "interesting application of known tools to a new domain, but limited theoretical depth"。

概率地板由 Related Work（强）和实验设计的结构性（3 tier, 6 baselines, 4 paradigms）托底：proposal 不会因 miss 关键相关工作或缺乏对比实验方案而被简单拒绝。

核心打压因素是 trivial alternative：TRACE (F1≈0.97) 已解决检测绝大部分，PURE 已从机制层面消除 exploitation，bifurcation 框架的实际增量空间被压缩到"更早 N 步预警 + 区分 bifurcation type"这一狭窄区间，且这些增量价值完全是未经验证的假设。

【建议】: 不推荐（投 CoRL 2026）；边缘偏不推荐（转投合理会议，中位 22%，低于 36% 通过阈值，且 novelty 天花板限制了优化空间）

【实施评估】:
  - 计算资源: 530-960 H100-hours（取决于执行模式），约 $660-$1,680 GPU 成本（H100 spot pricing）。Tier 1 需 ~16h 训练 + ~130h 评估/分析；Tier 2 需 ~20h 训练 + ~90h 分析；Tier 3 ~30h。需 4-8×H100 节点。存储 ~8-12TB（含 delta 压缩 checkpoint）。
  - 数据需求: MATH、AMC、AIME 数据集（公开可得）；Qwen3-4B/14B 模型（开源）；Qwen2.5-Math-PRM-7B、ACTPRM-X、GenPRM-7B（需确认可用性）。无需构建新数据集。
  - 人工介入: 中等——需人工设计 SAE 训练策略、验证 TRACE-PRM 适配、解读 bifurcation fitting 结果、判断 scaling exponent 估计的可靠性。Claude API 辅助分析约 $400-$1,200。
  - 训练需求: 需要 GRPO 训练 Qwen3-4B/14B（基于 OpenRLHF 框架），SAE 训练（32K hidden dims），以及各 ablation 条件的重复训练。总计 ~12 个训练 run。不需要从头预训练 LLM，但 RL fine-tuning 和 SAE 训练仍是显著计算负担。
  - 新 Benchmark: 不需要构建新 benchmark。使用已有数学推理数据集。但需构建新的诊断 metric 体系（Goodhart divergence rate、critical slowing down index、fold scaling exponent），这些度量的设计和验证本身需要工程投入。
  - 预估周期: 10-18 周（Tier 1 完成于 week 8-10，Tier 2 完成于 week 12-14，Tier 3 视时间）。最快可投稿版本（仅 Tier 1）约 10-12 周。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "962ae5f3-5b99-4ccb-89f9-d05ba4d25fa5",
  "isSidechain": false,
  "requestId": "req_011CbCTGEFx6x6drhT2kksa4",
  "type": "assistant",
  "uuid": "bf54725b-32c3-44e8-8845-5b163c781957",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013eCKDhYQLf74voT2R1n8xF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26233,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3648,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3648,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 26233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26233
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
  "leafUuid": "bf54725b-32c3-44e8-8845-5b163c781957",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Bifurcation theory for PRM exploitation detection in GRPO",
  "sessionId": "6611fbea-f3f3-4895-9a36-69ff1be48ddd"
}
```

---
