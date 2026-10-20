# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/6c461b59-1705-47dc-8872-8c5338ac0aa1.jsonl`
- **Structured JSON:** [`19661d35024064a04658.json`](../../sessions/19/19661d35024064a04658.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:10:55.494Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:10:55.494Z",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a comprehensive assessment. Let me compile the final evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题：投稿目标与 Proposal 内容严重不匹配】\n\n在进入 idea 质量评估之前，必须指出一个致命的结构性问题：\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n\"Submissions without a robotics focus will be returned without review.\"\n且要求 \"Authors are encouraged to report real-robot experiments or provide \nconvincing evidence that simulation experiments are transferable to real robots.\"\n\n本 Proposal（OverrelianceGuard）是一篇纯 HCI / Human-AI Interaction 论文：\n浏览器扩展 + 行为信号采集 + 过度依赖检测 + 自适应干预，涉及零机器人内容。\n投稿 CoRL 将被 desk reject，概率接近 100%。\n\n本 Proposal 的自然目标会议应为：CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027。\n\n以下我将按照「idea 本身的学术质量」进行客观评估（假设投稿到合适的 HCI 会议），\n但 CoRL 投稿的中稿概率需单独给出。\n\n\n【领域调研】:\n\n1. Liu et al., \"Behavioral Indicators of Overreliance During Interaction with \n   Conversational Language Models\" (CHI 2026, arXiv:2602.11567)\n   - 77 名参与者，3 个真实任务，LLM 注入错误信息\n   - 通过 autoencoder+clustering 识别出 5 种行为模式（低过度依赖：仔细理解任务+\n     细粒度导航；高过度依赖：频繁复制粘贴、跳过理解、反复引用LLM、粗糙定位等）\n   - 37 维 per-event 编码（15-dim one-hot + timestamp + page type + 19-dim \n     type-specific attributes）\n   - 明确将\"实时检测与自适应缓解\"列为 future work\n   → 本 Proposal 的直接上游工作，Proposal 本质上是实现 Liu et al. 的 future work\n\n2. Schoeffer et al., \"Adjust for Trust: Mitigating Trust-Induced Inappropriate \n   Reliance on AI Assistance\" (IUI 2026, arXiv:2502.13321)\n   - 基于 self-report 的信任自适应干预\n   - 高信任时提供 counter-explanations，低信任时提供 supporting explanations\n   - 实现高达 38% inappropriate reliance 降低、20% 决策准确率提升\n   - 使用约 30 次 per-decision self-report\n   → 本 Proposal 的另一个直接上游，Proposal 想用行为信号替代 self-report\n\n3. \"Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM \n   Support by User Modeling\" (CHI 2026)\n   - 使用 EDA（皮电）+ 鼠标移动数据持续评估认知状态\n   - 在调查问卷场景中实现个性化 LLM 支持\n   - 线性回归在 mouse+EDA 上仅 ~61% 准确率\n   → 证明纯行为信号检测困难，但该工作使用了生理传感器\n\n4. Campagna et al., \"Estimating Trust in Human-Robot Collaboration through \n   Behavioral Indicators and Explainability\" (RA-L 2025, arXiv:2601.19856)\n   - HRI 场景，从行为指标（adherence rate, decision latency, device dependency, \n     intervention frequency）分类信任水平\n   - Voting Classifier 达到 84% 准确率，AUC=0.90\n   → 被 Proposal 引用作为\"行为信号可以检测信任\"的证据，但场景差异巨大\n     （结构化工业HRI vs. 自由对话LLM交互）\n\n5. Li et al., \"From Text to Trust: Empowering AI-assisted Decision Making with \n   Adaptive LLM-powered Analysis\" (CHI 2025)\n   - 自适应选择向决策者展示哪些 LLM 分析\n   - 发现静态展示无显著效果，算法框架动态决策才有效\n   → 结构化任务中的自适应解释选择，Proposal 扩展到自由对话场景\n\n6. Raees & Papangelis, \"Trust to Reliance: Measurement Constructs for Human-AI \n   Appropriate Reliance\" (CHI EA 2026, arXiv:2604.23896)\n   - 区分 trust 和 appropriate reliance 的测量框架\n   - 提出 Traditional / Appropriateness / Dominance 三种视角\n   - RAIR/RSR 指标\n   → Proposal 引用其测量框架，引用准确\n\n- 调研总结：该领域在 2025-2026 年经历了快速发展。Liu et al. (CHI 2026) 完成了\n  行为模式的刻画，Adjust for Trust (IUI 2026) 完成了基于 self-report 的自适应\n  干预，Sensing What Surveys Miss (CHI 2026) 探索了生理信号辅助检测。本 Proposal \n  处于这三条线的交汇点，试图用纯行为信号（无 self-report、无生理传感器）实现\n  闭环检测与干预。这是一个自然的\"下一步\"工程整合工作，而非概念性突破。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. 基于规则的阈值系统：Liu et al. 已经识别出 5 种明确的行为模式（频繁复制粘贴、\n   跳过初始理解等）。一个简单的规则引擎，对这些模式的代理特征设置阈值（如：\n   copy-paste 频率 > X 且 dwell time < Y → 高过度依赖风险），可能达到与 ~40K \n   参数 CNN 相近的效果。\n\n   Proposal 的回应：引用 \"Adjust for Trust's Appendix D found F1 ≤ 0.5 with \n   surface-level heuristics\"。但这是不同任务上的不同启发式规则，不能直接类比。\n   真正的 trivial baseline 应该是：在 Liu et al. 的特征空间上，用 Liu et al. \n   识别的 5 种模式构建简单分类器（如 logistic regression / random forest）。\n   这个 baseline 在 Proposal 中未被讨论。\n\n2. 降低 self-report 频率而非完全消除：Adjust for Trust 使用 ~30 次 self-report，\n   Proposal 的 sparse probes 使用 2-3 次。一个中间方案——将 self-report 降到 \n   5-8 次——可能在最小干扰下获得足够好的信任估计。\n\n增量价值的可能来源：如果 CNN 在 30 秒滑动窗口上能发现超越 5 种已知模式的\ntemporal dynamics，那就有真实增量。但这是一个待验证的假设，不是已知事实。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中存在多个未经验证的关键假设：\n\n1. 「行为模式的实时可检测性」（最关键假设）\n   Liu et al. 的 5 种行为模式是通过对完整任务 session 的 post-hoc 聚类得出的。\n   假设这些模式在 30 秒滑动窗口内也能被捕捉到，是一个重大跳跃。许多模式\n   （如\"跳过初始理解\"）本质上是 session-level 的，可能无法在 30 秒窗口内表征。\n\n2. 「从 trust/overreliance 的行为关联到因果干预」\n   检测到过度依赖的行为信号 ≠ 干预在此时有效。行为信号可能是滞后指标\n   （overreliance 已经发生），而非先行指标（overreliance 正在形成）。如果是\n   滞后指标，干预的窗口可能已经关闭。\n\n3. 「跨场景泛化」\n   Liu et al. 的数据来自 3 个特定任务类型。假设训练出的分类器能泛化到\n   \"free-form conversational LLM interactions\"（Proposal 的声称范围）缺乏支撑。\n\n4. 「数据充分性」\n   77 人 × ~26K-40K windows 听起来多，但考虑到：(a) 参与者间行为差异大，\n   (b) 同一参与者的窗口高度自相关，(c) 正负样本可能严重不平衡，\n   有效独立样本量可能远小于名义数字。\n\n5. 「行为信号的信噪比」\n   \"Sensing What Surveys Miss\" 即使结合了 EDA 生理信号也仅达到 ~61%。\n   去掉生理信号只用行为信号，在更嘈杂的自由对话场景中，信噪比可能更差。\n\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 — \n   核心贡献是将 Liu et al. (CHI 2026) 的行为特征化 + Adjust for Trust (IUI 2026) \n   的自适应干预进行工程整合。两篇上游工作都是 2026 年初发表的，Proposal 实质上\n   是实现 Liu et al. 论文中明确列出的 future work。\"闭环系统\"的系统集成有一定\n   工程 novelty，但概念层面无突破。\n   \n   具体可以拆解的 novelty 点：\n   - 多分辨率 1D-CNN 架构：这是标准的时序分类方法，不构成 novelty\n   - 混合标注策略（MIL + weak supervision + sparse probes + self-supervised）：\n     这是最强的方法论贡献，但它本身是对\"没有好标签\"这一工程问题的权宜之计\n   - 循环性分析（weak supervision circularity ablation）：这是好的实验设计，\n     但不是 idea novelty\n   - 浏览器端实时推理：工程实现，不构成学术 novelty\n\n2. Significance: 中 — \n   研究问题（LLM 过度依赖的实时检测与干预）确实重要且时效性强。如果成功，\n   这将是第一个不需要 self-report 或生理传感器的闭环系统，具有部署价值。\n   但核心发现若为 positive（\"行为信号可以做到 ~75-80% 的检测\"），审稿人的\n   反应更可能是 \"I would have guessed this given Liu et al.'s findings\" \n   而非 \"surprising\"。如果 negative（~65-70%），虽然 Proposal 声称仍有价值，\n   但一篇\"这个方法不太行\"的论文在 CHI 的影响力有限。\n   \n   领域影响力取决于检测准确率是否跨过了\"实用阈值\"。Campagna et al. 在结构化\n   HRI 中达到 84%，但自由对话 LLM 场景的难度显著更高。\n\n3. Related Work: 强 — \n   Proposal 对已有工作的覆盖非常全面且准确。所有引用的关键论文均真实存在，\n   描述基本准确。差异化定位清晰（vs. Liu et al.: 从特征化到检测；vs. Adjust \n   for Trust: 从 self-report 到行为信号；vs. Sensing What Surveys Miss: \n   去除生理传感器依赖；vs. Li et al.: 从结构化任务到自由对话）。\n   唯一不足是缺少对一些更一般性的 behavioral analytics 和 interaction \n   modeling 工作的讨论。\n\n\n【概率估计 — 投稿 CoRL 2026】: 0-2%，中位 ~1%\n理由：内容与会议范围完全不匹配，将被 desk reject。\n\n【概率估计 — 假设投稿合适的 HCI 会议（如 CHI 2027）】: 25-35%，中位 ~30%\n\n【估计理由】: \nIdea 的核心是一个自然的工程整合工作——将 2026 年初两篇重要论文（Liu et al. \n的行为特征化 + Adjust for Trust 的自适应干预）连接起来，实现 Liu et al. 明确\n提出的 future work。Related Work 覆盖优秀（强），但 Novelty 是主要限制因素\n（弱-中）：核心概念不具有惊喜性，审稿人会认为这是一个\"expected next step\"。\nSignificance 居中，取决于检测准确率能否跨过实用阈值。\n\n混合标注方法论和循环性分析是最强的 novelty 点，如果实验设计执行得好，\n可以支撑一篇 CHI 论文。但 idea 内核本身的上限被\"这是两篇近期工作的\n工程桥接\"这一事实所限制。\n\n上界（35%）对应：混合标注方法论被认为是 significant methodological contribution，\n且实验结果清晰展示行为信号 vs. self-report 的优劣 trade-off。\n下界（25%）对应：审稿人认为这主要是工程工作，核心 claim 的前提假设未被充分\n验证（尤其是 30 秒窗口的实时可检测性问题）。\n\n【主要风险】:\n1. 「Obvious Next Step」风险：审稿人可能写 \"This is a natural engineering \n   extension of Liu et al. (CHI 2026) and Adjust for Trust (IUI 2026), executing\n   the future work explicitly outlined in those papers. The conceptual contribution \n   is limited.\" 这是 idea 层面最大的风险。\n\n2. 「前提假设不成立」风险：30 秒滑动窗口内的行为信号可能根本不足以检测\n   session-level 的过度依赖模式。如果核心检测组件失败（~60-65%），虽然 Proposal \n   有 dual-outcome 保护，但一篇以 \"negative result + methodology\" 为主的论文\n   在竞争激烈的 CHI 中较难中稿。\n```\n\n---\n\n**⚠️ 关键提醒：投稿目标问题**\n\n这是本次评审中最重要的发现：**本 Proposal 与 CoRL 2026 的会议范围完全不匹配**。CoRL (Conference on Robot Learning) 明确要求 robotics focus，并声明 \"Submissions without a robotics focus will be returned without review.\" 本 Proposal 是纯 HCI 工作，投稿 CoRL 会被直接 desk reject。\n\n建议目标会议：**CHI 2027**（deadline ~Sep 2026）、**IUI 2027**、或 **CSCW 2027**。\n\nSources:\n- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://dl.acm.org/doi/10.1145/3772318.3790332)\n- [Liu et al. - arXiv version](https://arxiv.org/abs/2602.11567)\n- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)\n- [Campagna et al. - Trust in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Li et al. - From Text to Trust (CHI 2025)](https://dl.acm.org/doi/10.1145/3706598.3713133)\n- [Raees & Papangelis - Trust to Reliance (CHI EA 2026)](https://arxiv.org/abs/2604.23896)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough assessment. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n- [Liu et al., \"Behavioral Indicators of Overreliance During Interaction with Conversational Language Models\"](https://arxiv.org/abs/2602.11567) (CHI 2026): 本 proposal 的核心基础。77 名参与者在含注入虚假信息的 LLM 辅助任务中收集交互日志，通过 autoencoder-clustering 框架识别出 5 种与过度依赖相关的行为模式（高依赖者：频繁复制粘贴、跳过初始理解、重复参考 LLM；低依赖者：仔细的任务理解和细粒度导航）。这是一篇 characterization 论文，明确提出了\"实时检测与自适应干预\"作为 future work。本 proposal 本质上是在执行这篇论文的 future work。\n\n- [\"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance\"](https://arxiv.org/abs/2502.13321) (IUI 2026): 基于 self-report 的信任自适应干预系统。通过在低信任时提供支持性解释、高信任时提供反面解释，实现最高 38% 的不当依赖降低和 20% 的决策准确率提升。本 proposal 的对标 baseline 之一，且明确 replicate 其条件作为实验组。\n\n- [\"Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling\"](https://dl.acm.org/doi/full/10.1145/3772318.3791191) (CHI 2026): 使用 EDA（皮肤电）+ 鼠标移动预测用户何时需要支持，线性回归 ~61% 准确率。该工作依赖生理传感器，本 proposal 声称的差异点在于\"无需生理传感器\"。\n\n- [Campagna et al., \"Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability\"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 在 HRI 场景中通过行为指标（遵从率、决策延迟、设备依赖性、干预频率）分类信任水平，Voting Classifier 84% 准确率 (AUC=0.90)。Proposal 引用此工作证明\"行为信号可达较高分类精度\"，但该工作处于受控 HRI 场景（化学品混合），与自由形式 LLM 对话差异巨大。\n\n- [Raees & Papangelis, \"From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making\"](https://arxiv.org/abs/2604.23896) (CHI EA 2026): 区分信任度量与适当依赖度量的分析框架，提出 Traditional/Appropriateness/Dominance 三种视角。Proposal 采用其中 Traditional（接受率）和 Appropriateness（RAIR/RSR）指标。\n\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): CoRL 是关于机器人学习的单轨会议，聚焦于学习在机器人中的应用：机器人感知与控制的表征学习、模仿学习、强化学习、sim-to-real 迁移、机器人操作/导航/运动等。**明确要求论文聚焦核心机器人问题。**\n\n- 调研总结: 过度依赖 LLM 的行为检测与自适应干预是一个新兴的 HCI 研究方向，2026 年 CHI/IUI 刚发表了几篇奠基性工作（行为表征、自报告自适应干预、传感器辅助支持）。本 proposal 的定位是将这些工作整合为一个闭环系统。**然而，CoRL 的主题范围是机器人学习，与本 proposal 的 HCI/人-LLM 交互方向完全不匹配。**\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **基于 Liu et al. 五种行为模式的规则系统**：Liu et al. 已经明确识别了 5 种行为模式及其与过度依赖的关联。一个直接的 trivial baseline 是：用手工规则检测这些模式（如\"检测到频繁复制粘贴+跳过初始理解→触发干预\"），而不需要训练 CNN。Proposal 虽然引用了 Adjust for Trust 附录 D 中 F1 ≤ 0.5 的\"surface-level heuristics\"结果，但该结果使用的是粗粒度启发式规则，而非基于 Liu et al. 明确识别的 5 种模式构建的精细规则。两者之间存在巨大的 sophistication gap——proposal 没有证明这个 gap 不可能被更简单的方法填补。\n\n2. **更简单的 ML 模型**：在 (30×28) 的特征矩阵上，gradient-boosted trees（展平特征）或简单 MLP 可能达到与 40K 参数 CNN 相当的性能。multi-resolution temporal 1D-CNN 的设计选择缺乏 ablation 或先验证据证明其相对于更简单模型的优势。\n\n增量价值的声明集中在\"端到端闭环系统\"和\"hybrid labeling\"上，但这更多是工程集成贡献而非方法论突破。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有多个未经验证的关键假设：\n\n1. **窗口级预测可行性假设（最关键）**：Liu et al. 的发现是 task-level 的行为模式与 outcome-level 的过度依赖之间的相关性。Proposal 假设这种相关性在 30 秒窗口粒度下仍然成立——即在任意 30 秒窗口内可以检测到过度依赖的行为信号。这是一个从宏观相关性到微观可预测性的重大推理跳跃，没有任何理论或实证支撑。\n\n2. **标注可用性假设**：Liu et al. 的标注是 outcome-based（参与者是否检测到并纠正了 LLM 注入的虚假信息），这是 task-level 标签。将其通过 MIL 传播到 30 秒窗口级别，假设\"过度依赖是一种持续的状态，在整个交互中均匀分布\"。实际上，过度依赖可能是 episodic 的——集中在特定的决策点而非持续存在。\n\n3. **数据充分性假设**：77 人的数据集产生 ~26K-40K 窗口。但这些窗口来自仅 77 个个体，有效的个体间变异极其有限。对于训练一个需要 generalize 到新用户的分类器，个体多样性（77人）可能远不够，即使窗口数量表面上足够。\n\n4. **干预有效性假设**：假设在检测到过度依赖时实时介入能有效改变用户行为。但已有研究（如认知强迫函数）显示，intervention 的时机和形式对效果至关重要，错误时机的干预可能导致 alert fatigue 或负面效果。Proposal 未讨论 false positive 干预的潜在危害。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱**\n   - 核心 idea 是 Liu et al. (CHI 2026) 论文中明确提出的 future work 方向的直接执行。Liu et al. 原文就指出其行为模式\"可适用于实时检测与自适应干预\"。\n   - \"闭环系统\"的概念在 Adjust for Trust (IUI 2026) 中已实现（基于 self-report），在 Sensing What Surveys Miss (CHI 2026) 中也已实现（基于传感器）。本 proposal 的 novelty claim 缩窄为\"用纯行为信号（无 self-report、无传感器）实现闭环\"——这是一个 modality 替换，不是概念创新。\n   - hybrid labeling 策略（MIL + weak supervision + sparse probes + self-supervised）有一定方法论贡献，但每个组件单独看都是 well-established 技术的应用。\n   - Campagna et al. (RA-L 2025) 已在 HRI 场景中证明行为指标可分类信任水平至 84%。虽然 LLM 对话场景不同，但\"行为信号→信任/依赖分类\"的研究范式并非新颖。\n\n2. **Significance: 弱-中（偏弱）**\n   - 过度依赖检测与干预本身是一个有实际意义的研究问题。\n   - **但对 CoRL 而言，significance 为零。** 本 proposal 研究的是人类与 LLM 的浏览器端对话交互中的认知过度依赖——与机器人学习完全无关。CoRL 关注的是机器人感知、控制、操作、导航、强化学习等，不涉及 HCI、用户行为分析或 LLM 对话干预。\n   - 即使放到 HCI 领域（CHI/IUI/CSCW），significance 也受限于：(a) 核心发现若 positive（检测准确率 >80%），审稿人会说\"刘等人的行为模式确实可以做分类，合理但不 surprising\"；(b) 核心发现若 negative（准确率 65-70%），proposal 自己承认这是一个退守结果。\n\n3. **Related Work: 中**\n   - Proposal 对直接相关的 4 篇核心工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss, Li et al. CHI 2025）的定位较为准确。\n   - 对 Campagna et al. 和 Raees & Papangelis 的引用和定位基本正确。\n   - 缺失：未讨论 cognitive forcing functions 的更广泛文献（如 Buçinca et al., 2021），未讨论 AI-assisted decision making 中 overreliance 的大量已有工作。\n   - **致命问题：完全缺少与 CoRL 领域的任何连接**——没有引用任何 robot learning 文献，没有讨论如何与机器人学习社区的关注点对接。\n\n\n【概率估计】: [0% - 3%] 中位 1%\n\n【估计理由】:\n**决定性因素是 venue mismatch。** 本 proposal 是一篇纯 HCI 论文（浏览器交互行为检测 + LLM 对话中的过度依赖干预），而 CoRL 是专注于机器人学习的会议。CoRL 的 CFP 明确要求\"submissions should focus on a core robotics problem\"——本 proposal 不涉及任何机器人问题、机器人硬件、机器人控制、或机器人学习算法。这不是一个可以通过改进实验设计来弥补的问题，而是 idea 本身的方向与目标会议完全不对口。极大概率在 desk reject 阶段就被拒。\n\n即使忽略 venue mismatch，纯以 idea 质量论（假设投稿到 CHI/IUI）：Novelty 弱（直接执行 Liu et al. 的 future work + modality 替换），核心假设（窗口级可预测性）未经验证，存在 trivial alternative 威胁。在 CHI/IUI 估计 20-30%。但对于 CoRL，概率趋近于 0%。\n\n【主要风险】:\n1. **致命的 venue mismatch**：本 proposal 与 CoRL 的主题范围完全不重合。这不是 idea 质量问题，而是方向性错误。应投稿 CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027 等 HCI 会议。\n2. **Novelty 不足**：即使在 HCI venue，核心 idea 是对 Liu et al. (CHI 2026) 明确 future work 的工程实现 + 对 Adjust for Trust (IUI 2026) 闭环概念的 modality 替换。审稿人可能评价为\"expected next step\"而非\"surprising contribution\"。\n```\n\n---\n\nSources:\n- [Liu et al., \"Behavioral Indicators of Overreliance\" (CHI 2026)](https://arxiv.org/abs/2602.11567)\n- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)\n- [Campagna et al. (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis (CHI EA 2026)](https://arxiv.org/abs/2604.23896)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to provide my evaluation. Let me compile the results.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [Behavioral Indicators of Overreliance During Interaction with Conversational Language Models](https://arxiv.org/abs/2602.11567) (CHI 2026): 本 proposal 的直接基础。77名参与者实验，识别出5种与过度依赖相关的行为模式（频繁复制粘贴、跳过初始理解、反复查阅LLM回复、粗粒度定位、犹豫后仍接受错误信息）。仅做行为表征，未构建实时检测系统。\n- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance](https://arxiv.org/abs/2502.13321) (IUI 2026): 基于自我报告的信任度触发自适应干预（counter-explanations、forced pauses），实现38%不当依赖减少。本 proposal 想替换其自我报告机制为行为信号。\n- [Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling](https://arxiv.org/html/2602.00880) (CHI 2026): 使用EDA+鼠标动态的多模态sensing预测认知负荷并自适应干预，线性回归仅达~61%准确率。依赖生理传感器。\n- [Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability](https://arxiv.org/abs/2601.19856) (RA-L 2025, Campagna et al.): HRI场景中从行为指标分类信任（84%准确率，AUC=0.90），支持行为信号可预测信任状态的论点。\n- [From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making](https://arxiv.org/abs/2604.23896) (CHI 2026 EA, Raees & Papangelis): 提出RAIR/RSR等适当依赖度量框架，区分trust与appropriate reliance。\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): 明确要求 \"Submissions should focus on a core robotics problem... Submissions without a robotics focus will be returned without review.\"\n\n- 调研总结: 该领域（HCI中的LLM过度依赖检测与缓解）在2025-2026年非常活跃，Liu et al.的行为表征和Adjust for Trust的自适应干预是两个关键基石。\"从行为信号→实时检测→闭环干预\"的系统集成确实尚无人完成，但这是这些工作的自然延伸。**然而，本proposal的研究内容与CoRL（Conference on Robot Learning）的scope完全不匹配——CoRL要求论文聚焦机器人学习核心问题，无机器人focus的论文将被退回不审。**\n\n【Trivial Alternative 检验】:\n存在显著的trivial alternative威胁：Liu et al.已识别出5个明确的行为模式，一个简单的规则系统（如\"30秒内copy-paste次数>3次 且 无编辑行为 → 触发干预\"）可能已经能提供reasonable的干预触发，无需训练CNN分类器。Proposal本身的weak supervision labeling functions实质上就是这些规则的编码——这意味着如果CNN的表现主要来自weak supervision，那它可能只是一个复杂化的规则系统。Proposal确实通过circularity ablation设计来检验这一点（MIL+probes-only vs full），但这更多是一个实验设计上的自我辩护，而非消除了trivial alternative的威胁。增量价值在于：如果CNN能发现规则未覆盖的temporal patterns（通过Integrated Gradients验证），则证明超越规则的价值；否则增量价值有限。\n\n【前提假设检验】:\n核心 claim 的逻辑链中有多个未验证假设：\n1. **30秒窗口的信息充分性**：假设30秒的交互信号包含足够信息区分过度依赖/正常依赖状态。Liu et al.的5种模式是在整个任务级别识别的（outcome-based），将其压缩到30秒流式窗口是否仍可区分，无直接证据。\n2. **过度依赖的实时可检测性**：假设overreliance是一个可在行为层面实时观测的连续状态，而非仅能通过任务结果回溯判定的属性。Liu et al.的标签就是基于最终结果（是否采纳了错误信息），这与\"实时流式预测\"之间存在根本性的时序错位——proposal承认了这一点但其MIL方案能否解决尚未验证。\n3. **跨场景泛化**：假设从Liu et al.特定实验设置（注入misinformation的3个任务）学到的模式能泛化到开放式LLM对话场景。\n\n【3 维度打分】:\n  1. Novelty: 弱-中 — 核心概念是将Liu et al. (CHI 2026)的行为表征 + Adjust for Trust (IUI 2026)的自适应干预集成为闭环系统。Liu et al.论文的future work明确呼吁了这个方向。真正的novelty delta在于：(a) hybrid labeling methodology（MIL + weak supervision + sparse probes的组合），(b) circularity analysis设计。但系统层面的创新（\"把检测和干预连起来\"）是显而易见的下一步。与Sensing What Surveys Miss (CHI 2026)的区别在于不用生理传感器，但这更多是engineering constraint的选择而非conceptual novelty。\n  2. Significance: 中 — 问题本身重要（LLM过度依赖是热点问题），实用价值明确（browser-based、不需要传感器的方案有部署优势）。但如果检测准确率仅为65-70%（proposal自己的pessimistic estimate），系统的实际干预效果可能有限，对领域的推动力也相应减弱。Proposal的dual-outcome framing（\"即使检测不好也有方法论贡献\"）是合理的保险策略但也暗示作者自己对core claim信心不足。\n  3. Related Work: 强 — Proposal对相关工作的覆盖非常全面且准确。Liu et al.、Adjust for Trust、Sensing What Surveys Miss、Campagna et al.、Raees & Papangelis均被正确引用且描述准确。差异化定位清晰（\"第一个纯行为信号闭环系统\"）。所引用论文均经验证存在。\n\n【概率估计】: 0-5% 中位 2%（针对 CoRL 2026）\n\n【估计理由】: \n**致命问题：完全的 venue mismatch。** CoRL 2026 Call for Papers 明确声明\"Submissions without a robotics focus will be returned without review\"。本 proposal 研究的是浏览器端LLM交互中的人类过度依赖检测，完全没有机器人学习相关内容——无机器人操作、无运动规划、无sim-to-real、无embodied agent。它将被直接 desk reject。\n\n如果评估在适当venue（如 CHI 2027 / IUI 2027 / CSCW）的中稿概率，估计为 25-35%，中位 30%。理由：idea方向正确、gap真实存在、related work扎实、方法论有一定novelty（hybrid labeling + circularity analysis），但核心系统概念是\"obvious next step\"（审稿人可能说\"I would have guessed this\"），且检测有效性这一核心前提尚无验证。Novelty维度限制了上界。\n\n【主要风险】: \n1. **致命风险 - 投稿venue完全不匹配**：CoRL是机器人学习会议，本文是纯HCI工作，将被desk reject\n2. **Idea层面风险**：核心贡献是Liu et al. + Adjust for Trust的\"显而易见的下一步\"系统集成，conceptual novelty有限；审稿人可能认为这是一个solid engineering effort但不是一个surprising research contribution\n```\n\n---\n\n**关键建议**: 本 proposal 的研究内容与 CoRL（Conference on Robot Learning）的投稿范围**完全不匹配**。CoRL 要求论文以机器人学习核心问题为中心，无机器人 focus 的提交将被退回不审。建议改投以下 venue：\n- **CHI 2027**（最匹配，前序工作 Liu et al. 和 Sensing What Surveys Miss 均发表于 CHI）\n- **IUI 2027**（前序工作 Adjust for Trust 发表于 IUI）\n- **CSCW 2027** 或 **UIST 2027**\n\n如果确认 venue 后需要进入后续发掘/补救流程（评估在正确 HCI venue 的优化策略），请告知。\n\nSources:\n- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://dl.acm.org/doi/10.1145/3772318.3790332)\n- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)\n- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)\n- [Campagna et al. - Trust Estimation in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)\n- [Raees & Papangelis - Trust to Reliance Framework (CHI 2026 EA)](https://arxiv.org/abs/2604.23896)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations\n\n## Description\nWe propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:10:55.498Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:10:55.498Z",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:10:55.513Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a comprehensive assessment. Let me compile the final evaluation.

---

```
【阶段】: Triage

【致命前置问题：投稿目标与 Proposal 内容严重不匹配】

在进入 idea 质量评估之前，必须指出一个致命的结构性问题：

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
"Submissions without a robotics focus will be returned without review."
且要求 "Authors are encouraged to report real-robot experiments or provide 
convincing evidence that simulation experiments are transferable to real robots."

本 Proposal（OverrelianceGuard）是一篇纯 HCI / Human-AI Interaction 论文：
浏览器扩展 + 行为信号采集 + 过度依赖检测 + 自适应干预，涉及零机器人内容。
投稿 CoRL 将被 desk reject，概率接近 100%。

本 Proposal 的自然目标会议应为：CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027。

以下我将按照「idea 本身的学术质量」进行客观评估（假设投稿到合适的 HCI 会议），
但 CoRL 投稿的中稿概率需单独给出。


【领域调研】:

1. Liu et al., "Behavioral Indicators of Overreliance During Interaction with 
   Conversational Language Models" (CHI 2026, arXiv:2602.11567)
   - 77 名参与者，3 个真实任务，LLM 注入错误信息
   - 通过 autoencoder+clustering 识别出 5 种行为模式（低过度依赖：仔细理解任务+
     细粒度导航；高过度依赖：频繁复制粘贴、跳过理解、反复引用LLM、粗糙定位等）
   - 37 维 per-event 编码（15-dim one-hot + timestamp + page type + 19-dim 
     type-specific attributes）
   - 明确将"实时检测与自适应缓解"列为 future work
   → 本 Proposal 的直接上游工作，Proposal 本质上是实现 Liu et al. 的 future work

2. Schoeffer et al., "Adjust for Trust: Mitigating Trust-Induced Inappropriate 
   Reliance on AI Assistance" (IUI 2026, arXiv:2502.13321)
   - 基于 self-report 的信任自适应干预
   - 高信任时提供 counter-explanations，低信任时提供 supporting explanations
   - 实现高达 38% inappropriate reliance 降低、20% 决策准确率提升
   - 使用约 30 次 per-decision self-report
   → 本 Proposal 的另一个直接上游，Proposal 想用行为信号替代 self-report

3. "Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM 
   Support by User Modeling" (CHI 2026)
   - 使用 EDA（皮电）+ 鼠标移动数据持续评估认知状态
   - 在调查问卷场景中实现个性化 LLM 支持
   - 线性回归在 mouse+EDA 上仅 ~61% 准确率
   → 证明纯行为信号检测困难，但该工作使用了生理传感器

4. Campagna et al., "Estimating Trust in Human-Robot Collaboration through 
   Behavioral Indicators and Explainability" (RA-L 2025, arXiv:2601.19856)
   - HRI 场景，从行为指标（adherence rate, decision latency, device dependency, 
     intervention frequency）分类信任水平
   - Voting Classifier 达到 84% 准确率，AUC=0.90
   → 被 Proposal 引用作为"行为信号可以检测信任"的证据，但场景差异巨大
     （结构化工业HRI vs. 自由对话LLM交互）

5. Li et al., "From Text to Trust: Empowering AI-assisted Decision Making with 
   Adaptive LLM-powered Analysis" (CHI 2025)
   - 自适应选择向决策者展示哪些 LLM 分析
   - 发现静态展示无显著效果，算法框架动态决策才有效
   → 结构化任务中的自适应解释选择，Proposal 扩展到自由对话场景

6. Raees & Papangelis, "Trust to Reliance: Measurement Constructs for Human-AI 
   Appropriate Reliance" (CHI EA 2026, arXiv:2604.23896)
   - 区分 trust 和 appropriate reliance 的测量框架
   - 提出 Traditional / Appropriateness / Dominance 三种视角
   - RAIR/RSR 指标
   → Proposal 引用其测量框架，引用准确

- 调研总结：该领域在 2025-2026 年经历了快速发展。Liu et al. (CHI 2026) 完成了
  行为模式的刻画，Adjust for Trust (IUI 2026) 完成了基于 self-report 的自适应
  干预，Sensing What Surveys Miss (CHI 2026) 探索了生理信号辅助检测。本 Proposal 
  处于这三条线的交汇点，试图用纯行为信号（无 self-report、无生理传感器）实现
  闭环检测与干预。这是一个自然的"下一步"工程整合工作，而非概念性突破。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. 基于规则的阈值系统：Liu et al. 已经识别出 5 种明确的行为模式（频繁复制粘贴、
   跳过初始理解等）。一个简单的规则引擎，对这些模式的代理特征设置阈值（如：
   copy-paste 频率 > X 且 dwell time < Y → 高过度依赖风险），可能达到与 ~40K 
   参数 CNN 相近的效果。

   Proposal 的回应：引用 "Adjust for Trust's Appendix D found F1 ≤ 0.5 with 
   surface-level heuristics"。但这是不同任务上的不同启发式规则，不能直接类比。
   真正的 trivial baseline 应该是：在 Liu et al. 的特征空间上，用 Liu et al. 
   识别的 5 种模式构建简单分类器（如 logistic regression / random forest）。
   这个 baseline 在 Proposal 中未被讨论。

2. 降低 self-report 频率而非完全消除：Adjust for Trust 使用 ~30 次 self-report，
   Proposal 的 sparse probes 使用 2-3 次。一个中间方案——将 self-report 降到 
   5-8 次——可能在最小干扰下获得足够好的信任估计。

增量价值的可能来源：如果 CNN 在 30 秒滑动窗口上能发现超越 5 种已知模式的
temporal dynamics，那就有真实增量。但这是一个待验证的假设，不是已知事实。


【前提假设检验】:

核心 claim 的逻辑链条中存在多个未经验证的关键假设：

1. 「行为模式的实时可检测性」（最关键假设）
   Liu et al. 的 5 种行为模式是通过对完整任务 session 的 post-hoc 聚类得出的。
   假设这些模式在 30 秒滑动窗口内也能被捕捉到，是一个重大跳跃。许多模式
   （如"跳过初始理解"）本质上是 session-level 的，可能无法在 30 秒窗口内表征。

2. 「从 trust/overreliance 的行为关联到因果干预」
   检测到过度依赖的行为信号 ≠ 干预在此时有效。行为信号可能是滞后指标
   （overreliance 已经发生），而非先行指标（overreliance 正在形成）。如果是
   滞后指标，干预的窗口可能已经关闭。

3. 「跨场景泛化」
   Liu et al. 的数据来自 3 个特定任务类型。假设训练出的分类器能泛化到
   "free-form conversational LLM interactions"（Proposal 的声称范围）缺乏支撑。

4. 「数据充分性」
   77 人 × ~26K-40K windows 听起来多，但考虑到：(a) 参与者间行为差异大，
   (b) 同一参与者的窗口高度自相关，(c) 正负样本可能严重不平衡，
   有效独立样本量可能远小于名义数字。

5. 「行为信号的信噪比」
   "Sensing What Surveys Miss" 即使结合了 EDA 生理信号也仅达到 ~61%。
   去掉生理信号只用行为信号，在更嘈杂的自由对话场景中，信噪比可能更差。


【3 维度打分】:

1. Novelty: 弱-中 — 
   核心贡献是将 Liu et al. (CHI 2026) 的行为特征化 + Adjust for Trust (IUI 2026) 
   的自适应干预进行工程整合。两篇上游工作都是 2026 年初发表的，Proposal 实质上
   是实现 Liu et al. 论文中明确列出的 future work。"闭环系统"的系统集成有一定
   工程 novelty，但概念层面无突破。
   
   具体可以拆解的 novelty 点：
   - 多分辨率 1D-CNN 架构：这是标准的时序分类方法，不构成 novelty
   - 混合标注策略（MIL + weak supervision + sparse probes + self-supervised）：
     这是最强的方法论贡献，但它本身是对"没有好标签"这一工程问题的权宜之计
   - 循环性分析（weak supervision circularity ablation）：这是好的实验设计，
     但不是 idea novelty
   - 浏览器端实时推理：工程实现，不构成学术 novelty

2. Significance: 中 — 
   研究问题（LLM 过度依赖的实时检测与干预）确实重要且时效性强。如果成功，
   这将是第一个不需要 self-report 或生理传感器的闭环系统，具有部署价值。
   但核心发现若为 positive（"行为信号可以做到 ~75-80% 的检测"），审稿人的
   反应更可能是 "I would have guessed this given Liu et al.'s findings" 
   而非 "surprising"。如果 negative（~65-70%），虽然 Proposal 声称仍有价值，
   但一篇"这个方法不太行"的论文在 CHI 的影响力有限。
   
   领域影响力取决于检测准确率是否跨过了"实用阈值"。Campagna et al. 在结构化
   HRI 中达到 84%，但自由对话 LLM 场景的难度显著更高。

3. Related Work: 强 — 
   Proposal 对已有工作的覆盖非常全面且准确。所有引用的关键论文均真实存在，
   描述基本准确。差异化定位清晰（vs. Liu et al.: 从特征化到检测；vs. Adjust 
   for Trust: 从 self-report 到行为信号；vs. Sensing What Surveys Miss: 
   去除生理传感器依赖；vs. Li et al.: 从结构化任务到自由对话）。
   唯一不足是缺少对一些更一般性的 behavioral analytics 和 interaction 
   modeling 工作的讨论。


【概率估计 — 投稿 CoRL 2026】: 0-2%，中位 ~1%
理由：内容与会议范围完全不匹配，将被 desk reject。

【概率估计 — 假设投稿合适的 HCI 会议（如 CHI 2027）】: 25-35%，中位 ~30%

【估计理由】: 
Idea 的核心是一个自然的工程整合工作——将 2026 年初两篇重要论文（Liu et al. 
的行为特征化 + Adjust for Trust 的自适应干预）连接起来，实现 Liu et al. 明确
提出的 future work。Related Work 覆盖优秀（强），但 Novelty 是主要限制因素
（弱-中）：核心概念不具有惊喜性，审稿人会认为这是一个"expected next step"。
Significance 居中，取决于检测准确率能否跨过实用阈值。

混合标注方法论和循环性分析是最强的 novelty 点，如果实验设计执行得好，
可以支撑一篇 CHI 论文。但 idea 内核本身的上限被"这是两篇近期工作的
工程桥接"这一事实所限制。

上界（35%）对应：混合标注方法论被认为是 significant methodological contribution，
且实验结果清晰展示行为信号 vs. self-report 的优劣 trade-off。
下界（25%）对应：审稿人认为这主要是工程工作，核心 claim 的前提假设未被充分
验证（尤其是 30 秒窗口的实时可检测性问题）。

【主要风险】:
1. 「Obvious Next Step」风险：审稿人可能写 "This is a natural engineering 
   extension of Liu et al. (CHI 2026) and Adjust for Trust (IUI 2026), executing
   the future work explicitly outlined in those papers. The conceptual contribution 
   is limited." 这是 idea 层面最大的风险。

2. 「前提假设不成立」风险：30 秒滑动窗口内的行为信号可能根本不足以检测
   session-level 的过度依赖模式。如果核心检测组件失败（~60-65%），虽然 Proposal 
   有 dual-outcome 保护，但一篇以 "negative result + methodology" 为主的论文
   在竞争激烈的 CHI 中较难中稿。
```

---

**⚠️ 关键提醒：投稿目标问题**

这是本次评审中最重要的发现：**本 Proposal 与 CoRL 2026 的会议范围完全不匹配**。CoRL (Conference on Robot Learning) 明确要求 robotics focus，并声明 "Submissions without a robotics focus will be returned without review." 本 Proposal 是纯 HCI 工作，投稿 CoRL 会被直接 desk reject。

建议目标会议：**CHI 2027**（deadline ~Sep 2026）、**IUI 2027**、或 **CSCW 2027**。

Sources:
- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://dl.acm.org/doi/10.1145/3772318.3790332)
- [Liu et al. - arXiv version](https://arxiv.org/abs/2602.11567)
- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)
- [Campagna et al. - Trust in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Li et al. - From Text to Trust (CHI 2025)](https://dl.acm.org/doi/10.1145/3706598.3713133)
- [Raees & Papangelis - Trust to Reliance (CHI EA 2026)](https://arxiv.org/abs/2604.23896)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

- [Liu et al., "Behavioral Indicators of Overreliance During Interaction with Conversational Language Models"](https://arxiv.org/abs/2602.11567) (CHI 2026): 本 proposal 的核心基础。77 名参与者在含注入虚假信息的 LLM 辅助任务中收集交互日志，通过 autoencoder-clustering 框架识别出 5 种与过度依赖相关的行为模式（高依赖者：频繁复制粘贴、跳过初始理解、重复参考 LLM；低依赖者：仔细的任务理解和细粒度导航）。这是一篇 characterization 论文，明确提出了"实时检测与自适应干预"作为 future work。本 proposal 本质上是在执行这篇论文的 future work。

- ["Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance"](https://arxiv.org/abs/2502.13321) (IUI 2026): 基于 self-report 的信任自适应干预系统。通过在低信任时提供支持性解释、高信任时提供反面解释，实现最高 38% 的不当依赖降低和 20% 的决策准确率提升。本 proposal 的对标 baseline 之一，且明确 replicate 其条件作为实验组。

- ["Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling"](https://dl.acm.org/doi/full/10.1145/3772318.3791191) (CHI 2026): 使用 EDA（皮肤电）+ 鼠标移动预测用户何时需要支持，线性回归 ~61% 准确率。该工作依赖生理传感器，本 proposal 声称的差异点在于"无需生理传感器"。

- [Campagna et al., "Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability"](https://arxiv.org/abs/2601.19856) (RA-L 2025): 在 HRI 场景中通过行为指标（遵从率、决策延迟、设备依赖性、干预频率）分类信任水平，Voting Classifier 84% 准确率 (AUC=0.90)。Proposal 引用此工作证明"行为信号可达较高分类精度"，但该工作处于受控 HRI 场景（化学品混合），与自由形式 LLM 对话差异巨大。

- [Raees & Papangelis, "From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making"](https://arxiv.org/abs/2604.23896) (CHI EA 2026): 区分信任度量与适当依赖度量的分析框架，提出 Traditional/Appropriateness/Dominance 三种视角。Proposal 采用其中 Traditional（接受率）和 Appropriateness（RAIR/RSR）指标。

- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): CoRL 是关于机器人学习的单轨会议，聚焦于学习在机器人中的应用：机器人感知与控制的表征学习、模仿学习、强化学习、sim-to-real 迁移、机器人操作/导航/运动等。**明确要求论文聚焦核心机器人问题。**

- 调研总结: 过度依赖 LLM 的行为检测与自适应干预是一个新兴的 HCI 研究方向，2026 年 CHI/IUI 刚发表了几篇奠基性工作（行为表征、自报告自适应干预、传感器辅助支持）。本 proposal 的定位是将这些工作整合为一个闭环系统。**然而，CoRL 的主题范围是机器人学习，与本 proposal 的 HCI/人-LLM 交互方向完全不匹配。**


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **基于 Liu et al. 五种行为模式的规则系统**：Liu et al. 已经明确识别了 5 种行为模式及其与过度依赖的关联。一个直接的 trivial baseline 是：用手工规则检测这些模式（如"检测到频繁复制粘贴+跳过初始理解→触发干预"），而不需要训练 CNN。Proposal 虽然引用了 Adjust for Trust 附录 D 中 F1 ≤ 0.5 的"surface-level heuristics"结果，但该结果使用的是粗粒度启发式规则，而非基于 Liu et al. 明确识别的 5 种模式构建的精细规则。两者之间存在巨大的 sophistication gap——proposal 没有证明这个 gap 不可能被更简单的方法填补。

2. **更简单的 ML 模型**：在 (30×28) 的特征矩阵上，gradient-boosted trees（展平特征）或简单 MLP 可能达到与 40K 参数 CNN 相当的性能。multi-resolution temporal 1D-CNN 的设计选择缺乏 ablation 或先验证据证明其相对于更简单模型的优势。

增量价值的声明集中在"端到端闭环系统"和"hybrid labeling"上，但这更多是工程集成贡献而非方法论突破。


【前提假设检验】:

核心 claim 的逻辑链条中有多个未经验证的关键假设：

1. **窗口级预测可行性假设（最关键）**：Liu et al. 的发现是 task-level 的行为模式与 outcome-level 的过度依赖之间的相关性。Proposal 假设这种相关性在 30 秒窗口粒度下仍然成立——即在任意 30 秒窗口内可以检测到过度依赖的行为信号。这是一个从宏观相关性到微观可预测性的重大推理跳跃，没有任何理论或实证支撑。

2. **标注可用性假设**：Liu et al. 的标注是 outcome-based（参与者是否检测到并纠正了 LLM 注入的虚假信息），这是 task-level 标签。将其通过 MIL 传播到 30 秒窗口级别，假设"过度依赖是一种持续的状态，在整个交互中均匀分布"。实际上，过度依赖可能是 episodic 的——集中在特定的决策点而非持续存在。

3. **数据充分性假设**：77 人的数据集产生 ~26K-40K 窗口。但这些窗口来自仅 77 个个体，有效的个体间变异极其有限。对于训练一个需要 generalize 到新用户的分类器，个体多样性（77人）可能远不够，即使窗口数量表面上足够。

4. **干预有效性假设**：假设在检测到过度依赖时实时介入能有效改变用户行为。但已有研究（如认知强迫函数）显示，intervention 的时机和形式对效果至关重要，错误时机的干预可能导致 alert fatigue 或负面效果。Proposal 未讨论 false positive 干预的潜在危害。


【3 维度打分】:

1. **Novelty: 弱**
   - 核心 idea 是 Liu et al. (CHI 2026) 论文中明确提出的 future work 方向的直接执行。Liu et al. 原文就指出其行为模式"可适用于实时检测与自适应干预"。
   - "闭环系统"的概念在 Adjust for Trust (IUI 2026) 中已实现（基于 self-report），在 Sensing What Surveys Miss (CHI 2026) 中也已实现（基于传感器）。本 proposal 的 novelty claim 缩窄为"用纯行为信号（无 self-report、无传感器）实现闭环"——这是一个 modality 替换，不是概念创新。
   - hybrid labeling 策略（MIL + weak supervision + sparse probes + self-supervised）有一定方法论贡献，但每个组件单独看都是 well-established 技术的应用。
   - Campagna et al. (RA-L 2025) 已在 HRI 场景中证明行为指标可分类信任水平至 84%。虽然 LLM 对话场景不同，但"行为信号→信任/依赖分类"的研究范式并非新颖。

2. **Significance: 弱-中（偏弱）**
   - 过度依赖检测与干预本身是一个有实际意义的研究问题。
   - **但对 CoRL 而言，significance 为零。** 本 proposal 研究的是人类与 LLM 的浏览器端对话交互中的认知过度依赖——与机器人学习完全无关。CoRL 关注的是机器人感知、控制、操作、导航、强化学习等，不涉及 HCI、用户行为分析或 LLM 对话干预。
   - 即使放到 HCI 领域（CHI/IUI/CSCW），significance 也受限于：(a) 核心发现若 positive（检测准确率 >80%），审稿人会说"刘等人的行为模式确实可以做分类，合理但不 surprising"；(b) 核心发现若 negative（准确率 65-70%），proposal 自己承认这是一个退守结果。

3. **Related Work: 中**
   - Proposal 对直接相关的 4 篇核心工作（Liu et al., Adjust for Trust, Sensing What Surveys Miss, Li et al. CHI 2025）的定位较为准确。
   - 对 Campagna et al. 和 Raees & Papangelis 的引用和定位基本正确。
   - 缺失：未讨论 cognitive forcing functions 的更广泛文献（如 Buçinca et al., 2021），未讨论 AI-assisted decision making 中 overreliance 的大量已有工作。
   - **致命问题：完全缺少与 CoRL 领域的任何连接**——没有引用任何 robot learning 文献，没有讨论如何与机器人学习社区的关注点对接。


【概率估计】: [0% - 3%] 中位 1%

【估计理由】:
**决定性因素是 venue mismatch。** 本 proposal 是一篇纯 HCI 论文（浏览器交互行为检测 + LLM 对话中的过度依赖干预），而 CoRL 是专注于机器人学习的会议。CoRL 的 CFP 明确要求"submissions should focus on a core robotics problem"——本 proposal 不涉及任何机器人问题、机器人硬件、机器人控制、或机器人学习算法。这不是一个可以通过改进实验设计来弥补的问题，而是 idea 本身的方向与目标会议完全不对口。极大概率在 desk reject 阶段就被拒。

即使忽略 venue mismatch，纯以 idea 质量论（假设投稿到 CHI/IUI）：Novelty 弱（直接执行 Liu et al. 的 future work + modality 替换），核心假设（窗口级可预测性）未经验证，存在 trivial alternative 威胁。在 CHI/IUI 估计 20-30%。但对于 CoRL，概率趋近于 0%。

【主要风险】:
1. **致命的 venue mismatch**：本 proposal 与 CoRL 的主题范围完全不重合。这不是 idea 质量问题，而是方向性错误。应投稿 CHI 2027、IUI 2027、CSCW 2027 或 UIST 2027 等 HCI 会议。
2. **Novelty 不足**：即使在 HCI venue，核心 idea 是对 Liu et al. (CHI 2026) 明确 future work 的工程实现 + 对 Adjust for Trust (IUI 2026) 闭环概念的 modality 替换。审稿人可能评价为"expected next step"而非"surprising contribution"。
```

---

Sources:
- [Liu et al., "Behavioral Indicators of Overreliance" (CHI 2026)](https://arxiv.org/abs/2602.11567)
- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)
- [Campagna et al. (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis (CHI EA 2026)](https://arxiv.org/abs/2604.23896)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to provide my evaluation. Let me compile the results.

---

```
【阶段】: Triage

【领域调研】:
- [Behavioral Indicators of Overreliance During Interaction with Conversational Language Models](https://arxiv.org/abs/2602.11567) (CHI 2026): 本 proposal 的直接基础。77名参与者实验，识别出5种与过度依赖相关的行为模式（频繁复制粘贴、跳过初始理解、反复查阅LLM回复、粗粒度定位、犹豫后仍接受错误信息）。仅做行为表征，未构建实时检测系统。
- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance](https://arxiv.org/abs/2502.13321) (IUI 2026): 基于自我报告的信任度触发自适应干预（counter-explanations、forced pauses），实现38%不当依赖减少。本 proposal 想替换其自我报告机制为行为信号。
- [Sensing What Surveys Miss: Understanding and Personalizing Proactive LLM Support by User Modeling](https://arxiv.org/html/2602.00880) (CHI 2026): 使用EDA+鼠标动态的多模态sensing预测认知负荷并自适应干预，线性回归仅达~61%准确率。依赖生理传感器。
- [Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability](https://arxiv.org/abs/2601.19856) (RA-L 2025, Campagna et al.): HRI场景中从行为指标分类信任（84%准确率，AUC=0.90），支持行为信号可预测信任状态的论点。
- [From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making](https://arxiv.org/abs/2604.23896) (CHI 2026 EA, Raees & Papangelis): 提出RAIR/RSR等适当依赖度量框架，区分trust与appropriate reliance。
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): 明确要求 "Submissions should focus on a core robotics problem... Submissions without a robotics focus will be returned without review."

- 调研总结: 该领域（HCI中的LLM过度依赖检测与缓解）在2025-2026年非常活跃，Liu et al.的行为表征和Adjust for Trust的自适应干预是两个关键基石。"从行为信号→实时检测→闭环干预"的系统集成确实尚无人完成，但这是这些工作的自然延伸。**然而，本proposal的研究内容与CoRL（Conference on Robot Learning）的scope完全不匹配——CoRL要求论文聚焦机器人学习核心问题，无机器人focus的论文将被退回不审。**

【Trivial Alternative 检验】:
存在显著的trivial alternative威胁：Liu et al.已识别出5个明确的行为模式，一个简单的规则系统（如"30秒内copy-paste次数>3次 且 无编辑行为 → 触发干预"）可能已经能提供reasonable的干预触发，无需训练CNN分类器。Proposal本身的weak supervision labeling functions实质上就是这些规则的编码——这意味着如果CNN的表现主要来自weak supervision，那它可能只是一个复杂化的规则系统。Proposal确实通过circularity ablation设计来检验这一点（MIL+probes-only vs full），但这更多是一个实验设计上的自我辩护，而非消除了trivial alternative的威胁。增量价值在于：如果CNN能发现规则未覆盖的temporal patterns（通过Integrated Gradients验证），则证明超越规则的价值；否则增量价值有限。

【前提假设检验】:
核心 claim 的逻辑链中有多个未验证假设：
1. **30秒窗口的信息充分性**：假设30秒的交互信号包含足够信息区分过度依赖/正常依赖状态。Liu et al.的5种模式是在整个任务级别识别的（outcome-based），将其压缩到30秒流式窗口是否仍可区分，无直接证据。
2. **过度依赖的实时可检测性**：假设overreliance是一个可在行为层面实时观测的连续状态，而非仅能通过任务结果回溯判定的属性。Liu et al.的标签就是基于最终结果（是否采纳了错误信息），这与"实时流式预测"之间存在根本性的时序错位——proposal承认了这一点但其MIL方案能否解决尚未验证。
3. **跨场景泛化**：假设从Liu et al.特定实验设置（注入misinformation的3个任务）学到的模式能泛化到开放式LLM对话场景。

【3 维度打分】:
  1. Novelty: 弱-中 — 核心概念是将Liu et al. (CHI 2026)的行为表征 + Adjust for Trust (IUI 2026)的自适应干预集成为闭环系统。Liu et al.论文的future work明确呼吁了这个方向。真正的novelty delta在于：(a) hybrid labeling methodology（MIL + weak supervision + sparse probes的组合），(b) circularity analysis设计。但系统层面的创新（"把检测和干预连起来"）是显而易见的下一步。与Sensing What Surveys Miss (CHI 2026)的区别在于不用生理传感器，但这更多是engineering constraint的选择而非conceptual novelty。
  2. Significance: 中 — 问题本身重要（LLM过度依赖是热点问题），实用价值明确（browser-based、不需要传感器的方案有部署优势）。但如果检测准确率仅为65-70%（proposal自己的pessimistic estimate），系统的实际干预效果可能有限，对领域的推动力也相应减弱。Proposal的dual-outcome framing（"即使检测不好也有方法论贡献"）是合理的保险策略但也暗示作者自己对core claim信心不足。
  3. Related Work: 强 — Proposal对相关工作的覆盖非常全面且准确。Liu et al.、Adjust for Trust、Sensing What Surveys Miss、Campagna et al.、Raees & Papangelis均被正确引用且描述准确。差异化定位清晰（"第一个纯行为信号闭环系统"）。所引用论文均经验证存在。

【概率估计】: 0-5% 中位 2%（针对 CoRL 2026）

【估计理由】: 
**致命问题：完全的 venue mismatch。** CoRL 2026 Call for Papers 明确声明"Submissions without a robotics focus will be returned without review"。本 proposal 研究的是浏览器端LLM交互中的人类过度依赖检测，完全没有机器人学习相关内容——无机器人操作、无运动规划、无sim-to-real、无embodied agent。它将被直接 desk reject。

如果评估在适当venue（如 CHI 2027 / IUI 2027 / CSCW）的中稿概率，估计为 25-35%，中位 30%。理由：idea方向正确、gap真实存在、related work扎实、方法论有一定novelty（hybrid labeling + circularity analysis），但核心系统概念是"obvious next step"（审稿人可能说"I would have guessed this"），且检测有效性这一核心前提尚无验证。Novelty维度限制了上界。

【主要风险】: 
1. **致命风险 - 投稿venue完全不匹配**：CoRL是机器人学习会议，本文是纯HCI工作，将被desk reject
2. **Idea层面风险**：核心贡献是Liu et al. + Adjust for Trust的"显而易见的下一步"系统集成，conceptual novelty有限；审稿人可能认为这是一个solid engineering effort但不是一个surprising research contribution
```

---

**关键建议**: 本 proposal 的研究内容与 CoRL（Conference on Robot Learning）的投稿范围**完全不匹配**。CoRL 要求论文以机器人学习核心问题为中心，无机器人 focus 的提交将被退回不审。建议改投以下 venue：
- **CHI 2027**（最匹配，前序工作 Liu et al. 和 Sensing What Surveys Miss 均发表于 CHI）
- **IUI 2027**（前序工作 Adjust for Trust 发表于 IUI）
- **CSCW 2027** 或 **UIST 2027**

如果确认 venue 后需要进入后续发掘/补救流程（评估在正确 HCI venue 的优化策略），请告知。

Sources:
- [Liu et al. - Behavioral Indicators of Overreliance (CHI 2026)](https://dl.acm.org/doi/10.1145/3772318.3790332)
- [Adjust for Trust (IUI 2026)](https://arxiv.org/abs/2502.13321)
- [Sensing What Surveys Miss (CHI 2026)](https://dl.acm.org/doi/full/10.1145/3772318.3791191)
- [Campagna et al. - Trust Estimation in HRI (RA-L 2025)](https://arxiv.org/abs/2601.19856)
- [Raees & Papangelis - Trust to Reliance Framework (CHI 2026 EA)](https://arxiv.org/abs/2604.23896)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Closing the Loop: From Behavioral Overreliance Detection to Adaptive Intervention in LLM Conversations

## Description
We propose OverrelianceGuard, the first closed-loop system that bridges unobtrusively collected behavioral interaction signals to real-time adaptive interventions in free-form conversational LLM interactions—without requiring self-report interruptions or physiological sensors. A browser extension captures non-invasive interaction events in 30-second sliding windows and transforms them into a temporal grid representation: each window is discretized into 30 one-second bins, with 28 aggregated features per bin capturing action type distribution (over 12 categories), mouse dynamics (distance, velocity), scroll behavior (distance, direction), keypress statistics, copy-paste behavior (including post-paste edit indicators), idle duration, dwell context relative to LLM responses, and page focus. This (30 × 28) temporal grid—derived from but explicitly distinct from Liu et al.'s (CHI 2026) per-event 37-dimensional encoding (15-dim action type one-hot + 1-dim timestamp + 2-dim page type + 19-dim type-specific attributes)—feeds a lightweight multi-resolution 1D-CNN (~40K parameters, <5ms browser inference via ONNX Runtime Web) with three parallel temporal branches capturing short-burst (2s), medium-term (10s), and full-window (30s) behavioral dynamics. We cite PRISM's 97.3% accuracy on UCI-HAR as evidence of architectural efficiency at this parameter scale, not as a performance projection—UCI-HAR involves 6-axis accelerometer data with well-separated activity classes, whereas overreliance classification operates on noisier interaction features with subtler boundaries. The architecture choice is motivated by converging evidence that simple models on behavioral signals are insufficient—Adjust for Trust's Appendix D found F1 ≤ 0.5 with surface-level heuristics, 'Sensing What Surveys Miss' (CHI 2026) achieves only ~61% with linear regression on mouse+EDA—while richer models on multi-dimensional behavioral features show substantially better results: Campagna et al. (RA-L 2025) achieve 84% trust classification (AUC=0.90) from behavioral indicators in HRI, and Kaneko & Yamada (2025) reach 90% in cooperative tasks. A methodological contribution is the hybrid labeling strategy addressing temporal misalignment between Liu et al.'s outcome-based labels and streaming prediction: outcome propagation via Multiple Instance Learning, weak supervision from programmatic heuristics encoding the five identified behavioral patterns, sparse event-triggered metacognitive probes (2–3 per task vs. Adjust for Trust's 30 per-decision self-reports), and self-supervised next-action prediction. Critically, we address the weak supervision circularity risk—where labeling functions encode behavioral patterns from the same feature space the CNN processes—through a four-condition ablation: (i) weak-supervision-only, (ii) MIL+probes-only (circularity-free, as labels derive from task outcomes and self-report), (iii) MIL+probes+self-supervised, and (iv) full multi-signal training. Comparing conditions (iv) vs. (ii) isolates whether the weak supervision provides complementary signal or merely teaches the CNN its own hand-coded rules, with Integrated Gradients feature attribution analysis revealing whether the model discovers temporal patterns beyond those encoded in labeling functions. We frame streaming behavioral overreliance detection as the core hypothesis being tested: if classifier accuracy proves disappointing (e.g., 65–70%), the within-subjects intervention comparison, the labeling methodology, and the characterization of what behavioral signals can and cannot predict all constitute independently publishable contributions. We analyze training data sufficiency: Liu et al.'s 77-participant dataset yields ~26K–40K behavioral windows with our proposed windowing, supplemented by augmentation and a phased training strategy. When overreliance risk exceeds personalized thresholds, the system selects from tiered interventions: metacognitive prompts (Assumption-style CFFs), counter-explanations (per Adjust for Trust), and comprehension checkpoints. Following Raees & Papangelis's (2026) measurement framework distinguishing trust from appropriate reliance, we assess overreliance via both Traditional (acceptance rates) and Appropriateness-view (RAIR/RSR) metrics. A within-subjects study (N≈120) across four LLM-assisted tasks compares four conditions: no intervention, static cognitive forcing, self-report-adaptive (replicating Adjust for Trust), and behaviorally-triggered adaptive (OverrelianceGuard). This work fills the gap between behavioral characterization (Liu et al., CHI 2026), trust-adaptive intervention via self-report (Adjust for Trust, IUI 2026), adaptive explanation selection in structured tasks (Li et al., CHI 2025), and sensor-dependent adaptive support (Sensing What Surveys Miss, CHI 2026)—contributing (1) the first streaming behavioral overreliance classifier for conversational LLM settings with a principled hybrid labeling methodology and explicit circularity analysis, (2) a deployable browser-based closed-loop intervention system requiring neither self-report interruptions nor physiological sensors, (3) head-to-head empirical evidence comparing self-report-based vs. behavior-based adaptive intervention, and (4) a rigorous characterization of what behavioral signals can and cannot predict about overreliance, advancing the field regardless of detection accuracy.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6b2cd6f9-87bc-4a81-862b-8519be3dad14",
  "type": "user",
  "uuid": "296fab63-99a7-4ca6-b1e1-3cc108701803",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:10:55.511Z_

```json
{
  "parentUuid": "296fab63-99a7-4ca6-b1e1-3cc108701803",
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
  "uuid": "08a73075-8cba-42dd-8303-41932ebefadc",
  "timestamp": "2026-05-20T03:10:55.511Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:10:55.511Z_

```json
{
  "parentUuid": "08a73075-8cba-42dd-8303-41932ebefadc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "be8f3f70-d36f-498a-aff3-763d223cb426",
  "timestamp": "2026-05-20T03:10:55.511Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a comprehensive a…",
  "leafUuid": "be8f3f70-d36f-498a-aff3-763d223cb426",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate OverrelianceGuard proposal for CoRL 2026",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:11:29.105Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments carefully and produce a Meta Judge output.

**Reviewer 1:**
- CoRL probability: 0-2%, median ~1%
- CHI probability: 25-35%, median ~30%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Key issues: venue mismatch (fatal), "obvious next step" of Liu et al. + Adjust for Trust, trivial alternative threat, unverified assumptions about 30s window detectability
  
**Reviewer 2:**
- CoRL probability: 0-3%, median 1%
- CHI probability: 20-30%
- Novelty: 弱
- Significance: 弱-中 (偏弱) for CoRL; zero for CHI
- Related Work: 中
- Key issues: venue mismatch (fatal), direct execution of Liu et al.'s future work, modality replacement rather than conceptual innovation

**Reviewer 3:**
- CoRL probability: 0-5%, median 2%
- CHI probability: 25-35%, median 30%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强

All three reviewers converge on the fatal venue mismatch and that this is essentially Liu et al.'s proposed future work, with Reviewer 2 being most critical about the lack of conceptual novelty.

For CoRL, the consensus is overwhelming—medians cluster around 1-2% with all reviewers citing the same fatal flaws. For CHI, the estimates range from 20-30%, suggesting the work might find a better home in a more applied venue, though the core issues around novelty and generalization remain.

The pattern across reviewers is striking: venue mismatch, weak novelty, executing prior work's roadmap, and the unverified 30-second window assumption appear universally. Related work coverage gets strong marks, but data scale and problem significance draw concern from multiple reviewers. R2 stands out as slightly more lenient on related work quality compared to the others.

For CoRL 2026, the venue incompatibility is the decisive factor—all three independently flagged this as fatal, pointing to roughly 0-2% acceptance probability with a median around 1%. The CHI hypothetical shows more variance: R1 and R3 both estimate 30%, R2 at 25%, averaging 28.3% with minimal standard deviation, suggesting moderate consistency on that alternative venue.

Now I'm assessing the implementation requirements for this HCI study: the computational demands are light with a browser extension and small CNN model, but the human component is substantial—recruiting 120 participants, securing IRB approval, and designing the experimental protocol will drive the timeline to 6-12 months. There's no existing benchmark to leverage, so the study itself becomes the validation framework.

Given the explicit CoRL 2026 target and unanimous reviewer consensus on the venue mismatch, this is a clear rejection scenario.  The acceptance probabilities across all three reviewers cluster tightly around 1-2%, showing strong agreement on the fundamental misalignment. I should flag the CHI venue as a more appropriate alternative in the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8f3f70-d36f-498a-aff3-763d223cb426",
  "isSidechain": false,
  "requestId": "req_011CbD63sRHrsyesgC4L4BKC",
  "type": "assistant",
  "uuid": "d6cbf972-be38-46f3-93b5-4e989ead0960",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wxGEA2NxbsoroHosG6TX5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14283,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3926,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14283
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

_source line 9 · 2026-05-20T03:12:29.746Z_

【阶段】: Meta Judge
【三次中位】: [1%, 1%, 2%]  std=0.5%
【共识维度】:
- **Venue Mismatch（致命）**：3/3 审稿人独立确认，CoRL 2026 CFP 明确要求 robotics focus，本 proposal 是纯 HCI 工作，将被 desk reject。这是最强共识信号。
- **Novelty（弱 ~ 弱-中）**：3/3 审稿人一致认为核心 idea 是 Liu et al. (CHI 2026) 明确列出的 future work + Adjust for Trust (IUI 2026) 的 modality 替换，属 "obvious next step"。R2 给弱，R1/R3 给弱-中，共识落在弱-中偏弱。
- **Trivial Alternative 威胁**：3/3 审稿人均指出基于 Liu et al. 5 种行为模式的规则系统是未被击败的 trivial baseline，Proposal 引用的 "Adjust for Trust Appendix D F1≤0.5" 反驳证据不对口（不同任务、不同规则粒度）。
- **30 秒窗口可检测性假设未验证**：3/3 审稿人均指出 Liu et al. 的行为模式是 task-level / session-level 的 post-hoc 发现，假设其在 30 秒流式窗口内仍可捕捉是一个重大未验证跳跃。
- **数据充分性担忧**：2/3（R1、R2）明确指出 77 人的个体多样性不足以支撑泛化性声明。
- **Related Work 覆盖扎实**：2/3（R1、R3）评为"强"，差异化定位清晰，引用真实准确。
- **研究问题本身有意义**：2/3（R1、R3）给 Significance "中"，认为问题重要但对 CoRL significance 为零。

【异常维度】:
- R2 对 Related Work 给"中"（R1/R3 给"强"）——R2 额外指出缺少 cognitive forcing functions 更广泛文献（如 Buçinca et al., 2021）及完全缺失 CoRL 领域连接。作为异常点略降权，但其关于缺少 cognitive forcing functions 文献的观察有一定道理，不完全是 outlier。
- R2 对 Significance 给"弱-中偏弱"（R1/R3 给"中"）——R2 更严格地区分了"问题重要性"与"预期贡献的惊喜度"，评分差异主要来自角度不同而非判断错误，降权处理。

【最终概率】: [0% - 2%] 中位 1%
【一致性】: 高（std=0.5%，远低于 3% 阈值；三位审稿人在致命问题判断上完全一致）

【综合理由】:
三位审稿人在核心判断上达到罕见的高度一致：**本 Proposal 与 CoRL 2026 的会议范围存在不可调和的根本性不匹配**。CoRL 是 Conference on Robot Learning，CFP 明确声明 "Submissions without a robotics focus will be returned without review"。本 Proposal（OverrelianceGuard）是一篇纯 HCI/Human-AI Interaction 论文——浏览器扩展、交互行为信号采集、过度依赖检测、自适应认知干预——不涉及任何机器人硬件、机器人控制、机器人感知、运动规划、sim-to-real 迁移或强化学习内容。这不是一个可以通过修改实验设计或调整 framing 来弥补的问题，而是 idea 本身的研究方向与目标 venue 完全正交。投稿 CoRL 将以接近 100% 的概率在 desk reject 阶段被拒。

三位审稿人均独立给出了 0-5% 的区间，中位落在 1-2%。鉴于高一致性，取中位附近并缩窄区间至 [0%-2%] 中位 1%。

**附注——假设投稿合适的 HCI 会议（CHI 2027 / IUI 2027）**：三位审稿人对此也给出了评估——R1: 25-35% 中位 30%，R2: 20-30%，R3: 25-35% 中位 30%。综合约 [22%-33%] 中位 28%。主要限制因素是 Novelty 天花板（"obvious next step"）和多个核心假设未经验证。

【建议】: KILL（投稿 CoRL 2026）。建议转投 CHI 2027（deadline ~Sep 2026，最匹配）、IUI 2027 或 CSCW 2027。如确认转投 HCI venue，可进入发掘/补救迭代流程以优化中稿概率（当前 CHI 估计中位 ~28%，有提升空间但受 Novelty 天花板限制）。

【实施评估】:
  - 计算资源: 低。~40K 参数 1D-CNN，训练可在单 GPU 上数小时完成；浏览器端推理 <5ms（ONNX Runtime Web）。无大规模计算需求。
  - 数据需求: 中-高。需复用 Liu et al. 的 77 人数据集（需确认数据可用性/共享协议），并新招募 ~120 名参与者进行 within-subjects 干预实验。需 IRB 审批。
  - 人工介入: 高。120 人 within-subjects 实验需要：实验设计与 pilot、IRB 审批流程（1-3 个月）、参与者招募与实验执行（2-4 个月）、数据标注与质量控制。
  - 训练需求: 低。轻量级 CNN（~40K 参数），无需大规模预训练或大模型微调。
  - 新 Benchmark: 否。使用已有数据集 + 自行收集实验数据，不需构建通用 benchmark。
  - 预估周期: 8-14 个月（IRB 审批 1-3 月 + 数据收集/实验 3-5 月 + 分析写作 2-4 月 + buffer），与 CHI 2027 Sep 2026 deadline 时间紧张但可能可行。

---

由于判定为 KILL，按角色 C 输出最终拒绝详情：

【拒绝阶段】: Triage（Meta Judge 综合三方评审）
【击穿维度 / 致命缺陷】:
1. **致命 Venue Mismatch**：CoRL 2026 要求 robotics focus，本 proposal 是纯 HCI 工作（浏览器端 LLM 交互行为检测 + 过度依赖干预），零机器人内容，将被 desk reject。三位审稿人一致确认，无争议。
2. **Novelty 天花板低**（即使在 HCI venue）：核心 idea 是 Liu et al. (CHI 2026) 明确 future work 的工程执行 + Adjust for Trust (IUI 2026) 闭环概念的 modality 替换（self-report → 行为信号）。三位审稿人一致评为 "obvious next step"。
【已尝试优化方向】: 无（在 Triage 阶段即 KILL，未进入迭代）
【可否抢救】:
- **换 venue 可行（强推荐）**：转投 **CHI 2027**（最匹配，前序工作 Liu et al. 和 Sensing What Surveys Miss 均发表于 CHI，deadline ~Sep 2026）或 **IUI 2027**（Adjust for Trust 发表于 IUI）。当前在 CHI 的估计中位约 28%，通过发掘/补救迭代有望提升至 30-38% 区间。
- **优化方向提示**（若转投 CHI 后进入迭代）：(a) 强化 hybrid labeling methodology 作为独立方法论贡献的 framing，而非仅作为系统组件；(b) 击败 trivial alternative——必须在实验中加入基于 Liu et al. 5 种模式的 logistic regression / random forest baseline；(c) 加强对 30 秒窗口可检测性假设的理论论证或 pilot 数据支撑；(d) 补充 cognitive forcing functions 更广泛文献的讨论。
- **不建议强行改造为 CoRL 论文**：将 HCI 过度依赖检测硬塞进机器人场景（如"机器人遥操作中的过度依赖"）会导致 idea 完整性丧失且缺乏真实研究基础，不可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6cbf972-be38-46f3-93b5-4e989ead0960",
  "isSidechain": false,
  "requestId": "req_011CbD63sRHrsyesgC4L4BKC",
  "type": "assistant",
  "uuid": "7c4e65aa-9179-44e5-b6fd-1d17ded945c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wxGEA2NxbsoroHosG6TX5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14283,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3926,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14283
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to provide a comprehensive a…",
  "leafUuid": "7c4e65aa-9179-44e5-b6fd-1d17ded945c3",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate OverrelianceGuard proposal for CoRL 2026",
  "sessionId": "6c461b59-1705-47dc-8872-8c5338ac0aa1"
}
```

---
