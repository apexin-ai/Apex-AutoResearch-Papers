# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/49e3a0f1-663e-4536-9d5a-8f53396ad32b.jsonl`
- **Structured JSON:** [`3bbd3f246c89ff3bd298.json`](../../sessions/3b/3bbd3f246c89ff3bd298.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:38:56.105Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:38:56.105Z",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to write a thorough evaluation. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【重要前置说明 — 致命级别的投稿方向不匹配】\n\n本 proposal 的研究内容是 \"LLM 辅助决策中的自适应双重解释呈现\"，属于 HCI / Human-AI Decision Making 领域。\n然而用户要求评估的目标会议是 **CoRL 2026（Conference on Robot Learning）**。\n\nCoRL 2026 的 Call for Papers 明确要求：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\" 涵盖的主题包括：imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception, manipulation, locomotion, robot foundation models 等。\n\n**本 proposal 与 CoRL 的 scope 完全不相关**——没有机器人、没有物理控制、没有 embodied learning。proposal 自身列出的目标会议是 CHI 2027 / CSCW 2027 / FAccT 2027，这些才是合理的投稿方向。投稿 CoRL 几乎必然被 desk reject。\n\n以下评估将从两个层面展开：\n(A) 针对 CoRL 2026 的中稿概率（scope mismatch 是压倒性因素）\n(B) 针对 proposal 自身 idea 质量的客观评价（假设投稿合适的 HCI venue）\n\n---\n\n【领域调研】:\n\n- **[arXiv 2605.10930] \"Evaluating the False Trust engendered by LLM Explanations\" (May 2026)**：\n  建立了 dual explanations（pro + contra）是唯一真正能提高用户区分 LLM 正确/错误输出能力的解释类型，其他解释类型（reasoning traces, post-hoc explanations）仅增加接受率。论文确认存在，描述准确。这是本 proposal 的核心前提之一。\n\n- **[arXiv 2502.13321] \"Adjust for Trust\" (IUI 2026)**：\n  trust-gated counter-explanations 减少 inappropriate reliance 38%，trust ≥ 8 阈值。需要每次决策后的 trust 自报告和准确性反馈。论文确认存在，描述准确。这是本 proposal 的主要对比基线（Condition 3）。\n\n- **[arXiv 2412.15584] \"To Rely or Not to Rely?\" (Bo et al., CHI 2025)**：\n  在 N=400 上测试 3 种 reliance interventions。Uncertainty Highlighting 反效果（增加 algorithm aversion）。论文确认存在，描述准确。本 proposal 用此论证 \"向用户展示不确定性有害，但作为后端信号可行\"。\n\n- **[arXiv 2502.11919] \"From Text to Trust\" (Li et al., CHI 2025)**：\n  动态规划框架 + 学习行为模型来选择性呈现 LLM 分析。需要先验交互数据，存在 cold-start 问题。论文确认存在，描述准确。本 proposal 的方法不需要用户历史数据，这是一个差异点。\n\n- **[arXiv 2603.21172] \"Entropy Alone is Insufficient\" (2026)**：\n  展示 semantic entropy 存在 \"confidently wrong\" regime，将其与 Probability of Correctness probe 结合可提高可靠性。论文确认存在，描述准确。本 proposal 的 Phase 1 技术方案直接来源于此。\n\n- **[arXiv 2508.07872] \"Unequal Uncertainty\" (2025)**：\n  首个关于 uncertainty-gated interventions 公平性风险的社会技术+法律分析。论文确认存在，描述准确。本 proposal 的 RQ3（fairness analysis）受此启发。\n\n- **[arXiv 2603.29915] \"Uncertainty Gating for Cost-Aware XAI\" (2026)**：\n  用 epistemic uncertainty 对 ML 分类器 gate 解释方法。应用场景不同（ML classifiers vs. human overreliance），但机制类似——用 uncertainty 选择是否/哪种解释方法。这是技术层面最接近的工作之一。\n\n- **调研总结**：该领域近期呈现三线汇聚态势：(1) dual/contrastive explanations 被验证有效；(2) adaptive/selective 解释呈现优于 always-on；(3) uncertainty 作为 gating signal 在 XAI 中已有应用但未用于 human overreliance。本 proposal 定位在 (1)+(2)+(3) 的交汇点，但本质上是将已有组件的组合验证——技术组件（SE+PC probe）和解释类型（dual）均来自先前工作，核心贡献在于实验比较。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在两个 trivial alternative 威胁：**\n\n1. **Always-on dual explanation**：如果 dual explanation 是唯一有效的类型（2605.10930 的结论），为什么不默认总是展示 dual？这是 Condition 2。如果 always-on 和 gated 的效果差异不显著，那么 gating 机制的增量价值为零——甚至 worse（增加了系统复杂度但没有收益）。proposal 把 always-on 作为对照，但没有强论证为什么 always-on 会明显劣于 gated。认知负荷的差异可能存在但难以达到实质性差别。\n\n2. **随机 gating**：一个 50/50 随机决定是否展示 dual explanation 的 baseline，成本为零且无任何用户/模型依赖。如果随机 gating 的效果接近 uncertainty gating，说明\"何时展示\"其实不重要，重要的只是\"有时展示\"。proposal 未包含此对照。\n\n**增量价值论证**：proposal 的增量价值主要是 practical（无需用户调查，首次交互即可用），而非 intellectual。如果核心发现是 \"uncertainty-gating non-inferior to trust-gating\"，审稿人很可能反应是 \"I would have guessed this\"——因为 uncertainty 与 model correctness 的相关性是已知的（AUROC ≥ 0.75 是 Phase 1 的准入门槛），所以 uncertainty-gating 能工作并不令人惊讶。\n\n---\n\n【前提假设检验】:\n\n1. **\"Gating 比 always-on 更好\" 假设未充分论证**：proposal 的核心前提是选择性呈现 dual explanation 优于总是呈现。但 2605.10930 发现 dual explanations 整体有效，没有报告 \"dual 在 model 正确时有害\" 的证据。如果 dual 在 model 正确时无害（只是冗余），那么 gating 的价值缩减为仅 cognitive load 减少——这是一个较弱的卖点。\n\n2. **\"Trust-gating 的 38% reduction 可迁移到知识 QA 任务\" 假设**：Adjust for Trust 使用 science QA 和 medical diagnosis（30 trials），但 proposal 使用 general-knowledge questions。任务类型差异可能导致 trust-gating 效果不同。proposal 假设效果可比，但未提供论证。\n\n3. **\"Uncertainty threshold 对所有问题类型均稳定\" 假设**：Youden's J optimal cutpoint 是在 200 个问题的验证集上优化的。不同领域/难度的问题可能需要不同阈值。proposal 假设单一阈值足够。\n\n4. **\"非劣效性 margin d=0.35 足以说服审稿人\" 假设**：Cohen's d = 0.35 对应 ~7 pp 的 overreliance rate 差异。在一个 baseline overreliance rate 可能为 30-50% 的场景下，7pp 的差异可能是实质性的。审稿人可能质疑这个 margin 过于宽松。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是 \"用 model uncertainty 替代 user trust 作为 gating signal\"。这个替代思路本身较直观——一旦知道 (a) dual explanations 有效 和 (b) uncertainty estimation 可行，用 uncertainty 来 gate 就是一个自然的工程组合。Uncertainty Gating for Cost-Aware XAI (2603.29915) 已经在 ML 分类器层面用 uncertainty gate 解释方法选择，机制高度类似。\"From Text to Trust\" (Li et al., CHI 2025) 已经展示了 adaptive explanation selection 的有效性。本 proposal 的差异化在于 (1) 用 uncertainty 而非 learned user model，(2) 非劣效性比较框架，(3) fairness 分析。其中 (1) 是技术上最自然的替代方案，(2) 和 (3) 是方法论贡献但非 conceptual novelty。总体上，这是一个 \"well-motivated incremental combination\" 而非 \"conceptually new idea\"。\n\n2. **Significance: 中** — \n   研究问题本身是重要的：如何 scalably 部署 adaptive explanation 是 LLM-assisted decision-making 的实际瓶颈。如果 uncertainty-gating 确实 non-inferior，这对实际部署有价值。但 significance 受限于：(a) 结果预期性高——如果 uncertainty 和 correctness 相关，gating 会工作，这不 surprising；(b) 仅适用于 knowledge QA（Persuasion Paradox 的 task-dependence 发现表明可推广性有限）；(c) 非劣效性结论的实践影响依赖于 margin 选择，不同 margin 得出不同结论。fairness analysis (RQ3) 是有价值的但作为 secondary 分析，影响力有限。\n\n3. **Related Work: 强** — \n   Related work 覆盖极为全面。核心对比工作（Adjust for Trust, false trust, Bo et al., Li et al.）均有准确引用和详细差异化分析。方法论基础（GLMM, TOST, Westfall et al.）也有扎实引用。甚至包括了 fairness（Unequal Uncertainty）、uncertainty estimation（Entropy Alone is Insufficient, SE Probes）、task-dependence（Persuasion Paradox）等边缘但相关的工作。论文引用均经验证真实。唯一微小遗漏：可以更深入讨论 \"Why Not Both?\"（Frontiers 2025）中 uncertainty 和 explanation 互补关系的具体发现。\n\n---\n\n【概率估计 — CoRL 2026】: 0% - 3% 中位 1%\n\n【估计理由 — CoRL 2026】: \n这是一个完全的 scope mismatch。CoRL 要求 \"focus on a core robotics problem\"，本 proposal 关于 LLM 文本解释的 human-AI decision-making，没有任何机器人、物理控制、embodied learning 成分。会被 desk reject。\n\n---\n\n【概率估计 — 假设投稿合适 venue (CHI/CSCW)】: 20% - 33% 中位 25%\n\n【估计理由 — 假设合适 venue】: \nRelated Work 维度强，methodological rigor 很高（preregistered, TOST, GLMMs, fairness），这些都会帮助通过审查。但 **idea 的 novelty 上限限制了总概率**：核心贡献是组件重组（现有 uncertainty method + 现有 dual explanation + 比较研究），审稿人大概率反应为 \"I would have guessed this works\"。非劣效性框架虽然在 HCI 中较少见（这是加分项），但不足以弥补 conceptual novelty 的不足。always-on dual 作为 trivial alternative 的威胁也会被审稿人注意到。对于 CHI 而言可能落在 borderline 区域；对 CSCW 稍好（fairness 角度 + 实践部署论证更被重视）。\n\n【主要风险】: \n1. **\"Why not always-on?\" 威胁**：如果 always-on dual（Condition 2）效果与 gated conditions 相当，审稿人会质疑整个 gating 框架的价值——\"the complexity of uncertainty estimation adds nothing over simply always showing dual explanations.\" 这是最可能的致命质疑。\n2. **Novelty 不足被挑战**：核心思路（用 uncertainty gate 解释类型）过于自然/直觉，审稿人可能评价为 \"competent execution of an obvious idea\"，在 competitive venue 中 novelty bar 不够。\n```\n\n**补充说明**：\n\n本 proposal 的 **形式完善度极高**——preregistered design, TOST equivalence testing, GLMM with crossed random effects, fairness analysis, ecological validity discussion 等，在方法论层面几乎无可挑剔。但正如评估原则所强调的，形式完善度 ≠ idea 好。透过形式看本质，核心问 \"用 model uncertainty 替代 trust 做 gating\" 是一个工程层面自然且可预测的替代方案，而非 conceptual breakthrough。\n\n如果目标确实是 CoRL，建议 **不要投稿此 proposal**，这是完全错误的 venue。如果目标是 CHI/CSCW，建议在迭代中重点解决 \"为什么 gating 比 always-on 更好\" 的论证，以及增加 conceptual novelty（例如发现 uncertainty-gating 在某些条件下 *优于* trust-gating 的机制性解释，而非仅做非劣效性验证）。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Adjust for Trust (arXiv 2502.13321)](https://arxiv.org/abs/2502.13321)\n- [Evaluating the False Trust (arXiv 2605.10930)](https://arxiv.org/abs/2605.10930)\n- [To Rely or Not to Rely (arXiv 2412.15584)](https://arxiv.org/abs/2412.15584)\n- [From Text to Trust (arXiv 2502.11919)](https://arxiv.org/abs/2502.11919)\n- [Entropy Alone is Insufficient (arXiv 2603.21172)](https://arxiv.org/abs/2603.21172)\n- [Unequal Uncertainty (arXiv 2508.07872)](https://arxiv.org/abs/2508.07872)\n- [Uncertainty Gating for Cost-Aware XAI (arXiv 2603.29915)](https://arxiv.org/html/2603.29915v1)\n- [Semantic Entropy Probes (arXiv 2406.15927)](https://arxiv.org/abs/2406.15927)\n- [LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306)](https://arxiv.org/html/2604.05306)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. \"Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance\" (IUI 2026, arXiv 2502.13321): \n   最直接的先行工作。提出基于用户自报信任度的自适应反向解释策略，在科学问答和医学诊断任务中将不当依赖降低38%。但需要每次决策后用户填写信任量表+准确性反馈，部署成本高。该 proposal 的 Condition 3 直接复现此机制。论文确实存在且描述准确。\n\n2. \"Evaluating the False Trust engendered by LLM Explanations\" (arXiv 2605.10930, May 2026): \n   确认双重解释（pro + contra）是唯一真正提高用户区分正确/错误 LLM 输出能力的解释类型，其他类型仅增加接受率。论文存在，描述准确，是 proposal 的关键动机之一。\n\n3. \"To Rely or Not to Rely?\" (Bo et al., CHI 2025, arXiv 2412.15584): \n   测试三种干预措施，发现 Uncertainty Highlighting 直接向用户展示不确定性反而加剧算法厌恶。论文存在且描述准确。Proposal 利用此发现论证\"后端使用不确定性而非前端展示\"的设计合理性。\n\n4. \"From Text to Trust\" (Li et al., CHI 2025, arXiv 2502.11919): \n   使用动态规划框架+学习的人类行为模型来选择性展示 LLM 生成的特征分析。需要先前交互数据（冷启动问题），操作对象为表格数据特征分析而非自然语言双重解释。论文存在，描述准确。\n\n5. \"Uncertainty Gating for Cost-Aware Explainable AI\" (arXiv 2603.29915): \n   使用认知不确定性来门控解释方法（选择不同的 XAI 方法），但针对传统 ML 分类器而非 LLM 辅助决策中的人类过度依赖。机制类似但应用域不同。\n\n6. \"Unequal Uncertainty\" (arXiv 2508.07872): \n   首次对基于不确定性的算法干预进行社会技术+法律分析，指出不确定性阈值可能对代表性不足的群体产生不成比例的影响。论文存在，proposal 的公平性分析 (RQ3) 直接受此启发。\n\n7. \"Entropy Alone is Insufficient for Safe Selective Prediction in LLMs\" (arXiv 2603.21172): \n   证明语义熵存在\"自信但错误\"区域，结合 Probability of Correctness probe 显著提高可靠性。Proposal 的混合不确定性估计器直接来源于此。\n\n8. \"Semantic Entropy Probes\" (Kossen et al., arXiv 2406.15927): \n   从单次生成的隐藏状态近似语义熵，大幅降低计算成本。Proposal 将其作为 Phase 1 的备选方案。\n\n- 调研总结: 这个领域（LLM 辅助决策中的自适应解释/干预）在 2024-2026 年非常活跃，\"什么时候该给什么样的解释\"是一个被广泛关注的问题。核心先行工作——信任门控 (IUI 2026) 和双重解释有效性 (2605.10930)——都是 2026 年的最新成果，proposal 的定位是对这些工作的自然组合与实用性改进。但\"用模型不确定性替代用户信任度作为门控信号\"这个想法本身是一个相当直觉化的工程替代，而非概念层面的突破。\n\n\n【Trivial Alternative 检验】:\n\n**存在严重的 trivial alternative 威胁：Always-On Dual Explanation (Condition 2)。**\n\n如果 2605.10930 已经证明双重解释是唯一真正有效的解释类型，那么最简单的策略就是**始终展示双重解释**——不需要任何门控信号、不需要不确定性估计、不需要信任量表、零额外部署成本。Proposal 确实包含了这个条件作为 baseline (Condition 2)，但这恰恰暴露了核心逻辑的薄弱：\n\n- 如果 always-on ≈ uncertainty-gated，那门控的价值存疑（唯一可能的 argument 是降低认知负荷，但这需要 H3 positive 来支撑，而这本身是一个较弱的预期效应）\n- 如果 always-on > uncertainty-gated，那 uncertainty-gating 就输给了 trivial baseline\n- 只有 uncertainty-gated > always-on（选择性触发比始终触发更好）才能充分证明门控的价值，但 proposal 并没有将此设为核心假设\n\n增量价值主要落在**实用性层面**（不需要用户问卷、首次交互即可用）相对于 trust-gating 的优势，以及**认知负荷**层面相对于 always-on 的优势。这些是工程/部署论证，不是科学洞见。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未经验证的关键假设：\n\n1. **\"模型不确定性高 ≈ 用户最需要双重解释的时刻\"**——这是整个 idea 的核心假设，但没有理论或实证支撑。模型不确定性高意味着模型可能出错，但用户过度依赖的原因是多方面的（过度信任、认知懒惰、锚定效应等），不确定性高的题目不一定是用户最容易过度依赖的题目。信任门控至少直接测量了用户状态，而不确定性门控假设模型状态可以替代用户状态——这个替代性本身就是需要被验证的。\n\n2. **非劣效性框架的预设立场**——H2 使用 TOST 检验\"不确定性门控不劣于信任门控\"（Cohen's d = 0.35 等价边界），这意味着 proposal 的\"最佳结果\"仅仅是\"大致一样有效\"。如果一个研究的天花板就是\"我的新方法和旧方法差不多\"，其学术贡献主要在实用性而非科学发现。\n\n3. **假设 Qwen3-30B-A3B 的混合不确定性估计器能在通用知识问答上达到 AUROC ≥ 0.75**——虽然 proposal 设置了 fallback 方案，但如果这个阈值达不到，整个研究的基础就不存在。2505.23854 已经指出 LLM 在知识密集型任务上的校准比推理任务差。\n\n4. **假设\"准确性反馈\"这个实验条件的引入不会严重扭曲生态效度**——proposal 自己承认准确性反馈在部署中罕见，但所有条件都提供了反馈。这意味着 uncertainty-gating 在实验中的相对优势可能被低估（如 proposal 所述），但也可能意味着实验结果对真实部署场景的外推存在系统性偏差。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — 核心贡献是\"用模型不确定性替代用户信任度作为双重解释的门控信号\"。这是一个自然、直觉化的工程替代，而非概念突破。\n   - \"Adjust for Trust\" (IUI 2026) 已建立自适应门控框架\n   - \"Uncertainty Gating for Cost-Aware XAI\" (2603.29915) 已在 ML 分类器上使用不确定性做解释门控\n   - Li et al. (CHI 2025) 已建立自适应解释选择框架\n   - 本 proposal 的增量是将\"不确定性作为后端门控\"应用到\"双重解释\"场景——组合性贡献而非原创性贡献\n   - \"后端使用 vs 前端展示\"不确定性的区分有一定见解，但更像是工程设计选择而非理论洞见（Bo et al. 的发现已经隐含了这个方向）\n   - 如果核心发现是 positive（不确定性门控 ≈ 信任门控），审稿人很可能说 \"I would have guessed this\"——用模型内部信号替代人工问卷直觉上是合理的\n\n2. **Significance: 中** — 研究问题在 HCI/AI-assisted decision making 领域有实际价值：部署中如何无侵入地实现自适应解释是一个真实痛点。\n   - 但对领域的推动是渐进式的：主要贡献是实用性改进（去掉问卷）而非新的理解或理论\n   - 公平性分析 (RQ3) 是有意义的补充，但作为二级贡献，不足以独立支撑论文\n   - 非劣效性框架限制了学术影响力的上限——即使所有假设成立，结论也只是\"可以用不确定性替代信任度，效果差不多\"\n   - 对 NLP/CL 领域的贡献有限，更多是 HCI 贡献\n   - **关键问题：这是一篇 CHI/CSCW 论文，不是 CoRL 论文**（见下文）\n\n3. **Related Work: 强** — 对已有工作的覆盖非常充分且准确。\n   - 所有核心引用（2605.10930, 2502.13321, 2412.15584, 2502.11919, 2603.21172, 2508.07872）均经验证存在且描述准确\n   - 差异化定位清晰：明确区分了与 \"Adjust for Trust\"（门控信号不同）、Li et al.（任务域和方法不同）、Bo et al.（前端展示 vs 后端门控）的差异\n   - 对 uncertainty quantification 文献的覆盖也足够（semantic entropy, PC probes, calibration）\n   - 对最新 2025-2026 工作的跟踪及时\n\n\n【概率估计】: [0% - 3%] 中位 1%\n\n【估计理由】: \n**概率估计受到致命的 venue mismatch 约束。** CoRL (Conference on Robot Learning) 是一个聚焦机器人学习的单轨会议，核心话题包括：机器人感知与控制的学习表征、模仿学习、强化学习、sim-to-real、机器人操作等。本 proposal 是一项纯 HCI 用户研究，涉及 LLM 辅助知识问答中的解释设计和人类过度依赖——**与机器人学习没有任何交集**。没有物理机器人、没有控制策略、没有感知系统、没有仿真环境。即使 idea 本身在 HCI 领域有一定价值，投稿 CoRL 也几乎必然被 desk rejection。\n\n如果抛开 venue mismatch 纯评 idea 质量（假设投稿 CHI/CSCW），概率估计约为 **[20% - 35%] 中位 27%**：idea 方向正确且有实际需求，但核心贡献是组合性/工程性的而非原创性的，非劣效性框架限制了学术影响力上限，且面临 always-on dual explanation 这一 trivial alternative 的严重威胁。Novelty 维度是主要限制因素。\n\n【主要风险】:\n1. **致命的 venue 不匹配**：CoRL 是机器人学习会议，本 proposal 是 HCI 用户研究，与 CoRL 的 scope 完全不重叠，几乎确定被 desk reject。\n2. **Trivial alternative 威胁**（idea 层面）：Always-on dual explanation 是一个零成本的替代方案，如果其效果接近或优于 uncertainty-gating，则门控机制的增量价值难以成立。核心创新沦为\"差不多一样好但更方便\"的实用性论证，这对顶会 novelty 要求而言不够。\n```\n\n**补充说明：**\n\n该 proposal 自身列出的目标 venue 是 CHI 2027、CSCW 2027、FAccT 2027——这些都是合理的 venue 选择。但用户询问的是 **CoRL 2026** 的中稿潜力，这存在根本性的 scope 不匹配。建议将投稿目标调整回 proposal 原始规划的 HCI 会议。\n\n即使在 CHI/CSCW 的语境下，idea 的核心瓶颈仍然是 **novelty 不够强**：核心贡献是一个直觉化的工程替代（用不确定性替代信任问卷），非劣效性框架进一步削弱了学术影响力上限。要提升中稿概率，需要在 idea 层面找到超越 \"practical alternative\" 的 deeper insight——例如，不确定性门控和信任门控在何种条件下会 diverge（不仅仅是\"差不多\"），或者为什么模型不确定性能捕捉到用户信任度捕捉不到的过度依赖模式。\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make an informed assessment. Let me write up the triage evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 严重前置问题：投稿目标与 proposal 内容的根本性错配】\n\n本 proposal 的内容是 HCI 领域的 human-AI decision-making 用户研究（自适应解释呈现策略比较），\nproposal 自身列出的目标会议为 CHI 2027、CSCW 2027、FAccT 2027。\n然而系统指定的评估目标是 **CoRL 2026（Conference on Robot Learning）**——\nCoRL 的核心 scope 是机器人学习（manipulation, locomotion, planning, sim-to-real, RL for robotics 等），\n与本 proposal 的研究主题（LLM 解释呈现策略的用户研究）**完全不相关**。\n\n如果强行投稿 CoRL 2026，预计会在 desk review 阶段被拒（scope mismatch），\n中稿概率接近 0%，与 idea 质量无关。\n\n以下评估将 **独立于 venue fit** 客观评价 idea 本身的质量，概率估计同时给出\nCoRL 场景和 proposal 自身目标 venue（CHI/CSCW）场景的估计。\n\n\n【领域调研】:\n\n- [2605.10930] \"Evaluating the False Trust engendered by LLM Explanations\" (arXiv, May 2026):\n  确认存在。发现 dual explanations（pro + contra）是唯一真正改善用户辨别 LLM 正确/错误\n  能力的解释类型；其他解释类型仅增加接受率。本 proposal 的核心前提之一。\n\n- [2502.13321] \"Adjust for Trust\" (IUI 2026):\n  确认存在。基于自报告 trust 自适应触发 counter-explanation，减少 38% 不当依赖。\n  关键局限：需要每次决策后的 trust 自报告 + 准确度反馈。本 proposal 的主要对比对象。\n\n- [2412.15584] Bo et al., \"To Rely or Not to Rely?\" (CHI 2025):\n  确认存在。发现 uncertainty highlighting 直接展示给用户会适得其反（增加 algorithm aversion）。\n  本 proposal 用此证据支持\"后端 gating\"设计（不向用户展示 uncertainty），论证链成立。\n\n- [2502.11919] Li et al., \"From Text to Trust\" (CHI 2025):\n  确认存在。动态规划框架 + learned user model 自适应选择 LLM feature analyses，\n  需要先验交互数据（cold-start 问题）。与本 proposal 的 gating 信号不同。\n\n- [2508.07872] \"Unequal Uncertainty\" (arXiv):\n  确认存在。首个对 uncertainty-gated interventions 的社会技术 + 法律分析，\n  证明 uncertainty 阈值可能对 underrepresented groups 产生不成比例的影响。\n\n- [2603.21172] \"Entropy Alone is Insufficient\" (arXiv 2026):\n  确认存在。指出 semantic entropy 的\"confidently wrong\"问题，\n  提出结合 Probability of Correctness probe 的混合方法。\n\n- [2603.29915] \"Uncertainty Gating for Cost-Aware XAI\" (arXiv 2026):\n  确认存在。用 epistemic uncertainty 门控 ML classifier 的解释方法选择，\n  但应用场景是 ML 模型解释成本优化，不涉及人类过度依赖问题。\n\n- Semantic Entropy Probes (Kossen et al., 2406.15927):\n  确认存在。从单次生成的 hidden states 近似 semantic entropy，大幅降低计算开销。\n\n- 调研总结：自适应解释呈现（adaptive explanation presentation）是 2025-2026 HCI 领域\n  的活跃方向。\"trust-gated\"和\"uncertainty-based\"分别已有独立工作，但 **head-to-head\n  comparison 确实尚未出现**。核心 gap 是真实的，但 gap 的性质是\"两个已知方法的\n  系统性比较\"，而非\"提出新方法\"。\n\n\n【Trivial Alternative 检验】:\n\n存在明显的 trivial alternative 威胁：\n\n1. **Always-on dual explanation（Condition 2）**：如果 dual explanation 是唯一有效的\n   解释类型（2605.10930），最简单的策略就是\"总是提供 dual explanation\"。selective gating\n   的价值取决于 always-on 是否有显著的副作用（认知负荷增加、满意度下降），但 proposal\n   自己承认这只是 H3（Condition 4 vs. Condition 2 的认知负荷比较），且 effect size\n   未必大。如果 always-on 的代价很小，整个 gating 框架的必要性就被削弱了。\n\n2. **Random gating baseline 缺失**：如果比较的是\"uncertainty gating vs. trust gating\"，\n   一个关键问题是：是否**任何 selective gating**（甚至随机触发）都已经足够好？\n   缺少随机触发 baseline 无法排除这一可能性。\n\n增量价值的论证依赖于：(a) always-on 有显著认知负荷代价，且 (b) uncertainty gating\n的选择性（而非随机性）对效果有贡献。这两个前提都未被预先验证。\n\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的假设：\n\n1. **\"Uncertainty 信号在 general-knowledge QA 任务上能达到 AUROC ≥ 0.75\"**——\n   proposal 自己引用 2505.23854 指出 LLM 在 knowledge-heavy 任务上的 calibration\n   比 reasoning 任务更差。虽然 proposal 设了 0.75 阈值和 fallback 方案，但如果\n   Phase 1 失败，整个研究的核心比较就无法进行。这是一个 **前提性假设**。\n\n2. **\"Non-inferiority = practical superiority\" 的论证跳跃**——H2 测试的是 uncertainty-gating\n   不劣于 trust-gating（d ≤ 0.35）。但\"不劣于 + 无需用户调查\"→ \"实践中更优\" 的\n   推理需要假设部署场景中确实不存在 trust 信号的替代获取方式（如 behavioral indicators、\n   implicit feedback 等）。虽然 proposal 引用了 F1 ≤ 0.5 的被动 trust 检测结果，\n   但这来自单一研究，且 NLP 领域的 behavioral modeling 进展很快。\n\n3. **\"Accuracy feedback 不影响 uncertainty-gating 但严重影响 trust-gating\"**——\n   proposal 的生态效度论证假设在无反馈场景下 uncertainty-gating 的相对优势会\"更大\"。\n   但反馈的缺失也可能改变用户与系统的整体交互模式（如降低 engagement），这种\n   交互效应并未被建模。\n\n4. **跨任务可迁移性假设**——整个研究在 general-knowledge QA 上进行，但 claim\n   推广到了\"LLM-assisted decision-making\" 这一更大范畴。2604.03237 的发现恰恰\n   表明解释效果高度依赖任务类型，这限制了结论的推广性。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是**两个已知方法的系统性比较**（trust-gating vs. uncertainty-gating），\n   而非提出新方法或新理论。\"head-to-head comparison 尚未出现\"是真实的 gap，\n   但这种 gap 的性质是 empirical comparison，novelty 来自 \"做比较\" 本身。\n   调研确认 [2502.13321] 提出 trust-gating，[2603.21172] 和 [2406.15927] 提供\n   uncertainty estimation 工具，[2603.29915] 已将 uncertainty 用于 gating 解释方法。\n   本 proposal 的独特组合（uncertainty gating + dual explanation + user study）\n   确有增量新意，但核心 insight（\"uncertainty 可以替代 trust 作为 gating signal\"）\n   在概念层面并不 surprising。如果结果是 positive（uncertainty-gating non-inferior），\n   多数审稿人的反应可能是 **\"makes sense, I would have guessed this\"** 而非 \"surprising\"。\n   \n   非劣效性（non-inferiority）的实验设计进一步限制了 novelty 上限：最佳结果是\n   \"和已有方法一样好但更方便\"——这是工程/实践贡献而非科学发现。\n\n2. **Significance: 中** — \n   研究问题有实际意义：如何在不需要用户自报告的情况下实现自适应解释呈现。\n   这对 LLM 部署场景有直接价值。但影响范围受到多重限制：\n   (a) 仅在 general-knowledge QA 一个任务类型上验证，[2604.03237] 已证明\n   跨任务迁移性差；\n   (b) 核心发现的 surprise factor 低——如果 uncertainty-gating 确实 non-inferior，\n   审稿人可能觉得这是预期之内的；\n   (c) 如果 uncertainty-gating 实际上 inferior，那结论变成\"trust-gating 更好但\n   不实用\"，这也不是特别有影响力的发现。\n   公平性分析（RQ3）增加了一些 significance 但感觉是附加的而非核心。\n\n3. **Related Work: 强** — \n   这是本 proposal 最突出的优点。Related work 覆盖非常全面、准确：\n   - 核心对比论文 [2502.13321]、[2605.10930]、[2412.15584] 均经调研确认真实存在\n     且描述准确\n   - 差异化定位清晰（vs. Li et al. [2502.11919] 的 learned user model，\n     vs. Bo et al. 的 user-facing uncertainty display，vs. [2603.29915] 的 ML classifier\n     成本优化）\n   - 对 counter-evidence 的处理诚实（如 Bo et al. 的 uncertainty highlighting 反效果）\n   - 方法论参考文献（Lakens 2017, Westfall et al. 2014, Baayen et al. 2008）\n     均为领域标准\n   - 唯一缺失：缺少对 2025-2026 年 CHI/CSCW 领域更广泛的 adaptive AI interaction\n     工作的覆盖（如 Human-AI Deliberation 等新方向）\n\n\n【概率估计】:\n\n→ **CoRL 2026**: 0-2%（中位 1%）\n   理由：完全的 scope mismatch，会在 desk review 被拒，与 idea 质量无关。\n\n→ **CHI 2027 / CSCW 2027（proposal 实际目标 venue）**: 20-32%（中位 25%）\n   基于 idea 质量的估计，不含执行层面因素。\n\n【估计理由】:\n\n以 CHI/CSCW 为参考（因为 CoRL 是纯 scope 问题）：\n\nIdea 处于 rubric 的 25-35% 区间——方向正确、gap 真实、related work 强，但\n核心 novelty 是 \"两个已知方法的系统比较\"，最佳结果（non-inferiority）的 surprise \nfactor 低。审稿人大概率的反应是 \"well-executed comparison study, but limited \nnovelty / I would have guessed this result\"。\n\n上界受限的主要因素是 **Novelty**：这是一个 empirical comparison 而非 method/theory \n贡献，且非劣效性设计意味着正面结果本身 = \"和已有方法一样好\"。如果投 CSCW（更看重\nempirical HCI contribution），概率可能接近上界；如果投 CHI（更看重 novelty），\n可能在下界附近。\n\n下界被 Related Work 的强度和实验设计的严谨性（TOST, GLMM, preregistration）\n支撑——这降低了被拒的概率下限。\n\n【主要风险】:\n\n1. **\"Comparison study, limited novelty\" 拒稿理由**：审稿人可能认为这是一个\n   工程性比较（比较两个现成方法在用户研究中的表现），缺乏深层的科学洞见或\n   方法创新。Non-inferiority design 使得最佳结果是 \"一样好但更方便\"，\n   这不够 surprising。\n\n2. **Trivial alternative 威胁（always-on dual explanation）**：如果 always-on \n   dual explanation 的认知负荷代价不大，审稿人会质疑整个 selective gating 框架\n   的必要性——\"为什么不直接总是给 dual explanation？\"\n```\n\n---\n\n**补充说明**：\n\n关于 CoRL 2026 的 scope 问题，这是一个**致命性的 venue mismatch**。CoRL 关注的是机器人学习（robot manipulation, locomotion, navigation, sim-to-real, RL for robotics），而本 proposal 是一个纯 HCI 用户研究，研究 LLM 解释呈现策略。即使 idea 本身是 ACM CHI best paper 水平，投 CoRL 也会被直接 desk reject。\n\n如果评估目标确实是 CoRL，建议直接放弃此方向；如果实际目标是 CHI/CSCW（如 proposal 自身所列），则 idea 质量处于\"可以做但 novelty 受限\"的区间，核心风险在于 comparison study 的 novelty ceiling 较低。\n\nSources:\n- [Evaluating the False Trust engendered by LLM Explanations](https://arxiv.org/abs/2605.10930)\n- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance](https://arxiv.org/abs/2502.13321)\n- [To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on LLMs](https://arxiv.org/abs/2412.15584)\n- [From Text to Trust: Empowering AI-assisted Decision Making](https://arxiv.org/abs/2502.11919)\n- [Unequal Uncertainty: Rethinking Algorithmic Interventions](https://arxiv.org/abs/2508.07872)\n- [Uncertainty Gating for Cost-Aware Explainable AI](https://arxiv.org/html/2603.29915v1)\n- [Semantic Entropy Probes](https://arxiv.org/abs/2406.15927)\n- [Entropy Alone is Insufficient for Safe Selective Prediction](https://arxiv.org/abs/2603.21172)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Making\n\n## Description\nWe propose the first head-to-head comparison of model uncertainty and user trust as gating signals for adaptive dual explanation presentation in LLM-assisted decision-making. Building on three convergent findings—that dual explanations are the only explanation type genuinely reducing overreliance (2605.10930), that trust-gated counter-explanations cut inappropriate reliance by 38% but require obtrusive self-reports and accuracy feedback (Adjust for Trust, IUI 2026), and that displaying uncertainty directly to users backfires by increasing algorithm aversion (Bo et al., CHI 2025)—we test whether automatic model uncertainty can serve as a practical, first-interaction-ready *backend* gating signal that selects explanation type without burdening users. The system uses a validated hybrid uncertainty estimator (semantic entropy + Probability of Correctness probe over Qwen3-30B-A3B's shared residual stream representations, addressing both the 'confidently wrong' regime identified by 2603.21172 and MoE-specific probing considerations) to selectively trigger dual explanations when model error is likely. The uncertainty threshold is set via Youden's J-optimal cutpoint with cross-validated calibration, and triggering rates are verified against the trust-gated condition in a pilot study. A preregistered between-subjects study (N≈560, Prolific) compares four conditions across 30 general-knowledge questions: no explanation, always-on dual explanation, trust-gated dual explanation (replicating the Adjust for Trust mechanism with trust ≥ 8 threshold), and uncertainty-gated dual explanation. We measure overreliance reduction, discrimination accuracy, appropriate reliance ratio, cognitive load, and satisfaction. The central hypothesis (H2) tests non-inferiority of uncertainty-gating via TOST with a pre-registered equivalence margin of Cohen's d = 0.35 (≈7 percentage points on overreliance rate), justified by cost-benefit SESOI reasoning: below this threshold, uncertainty-gating's deployment advantages (no surveys, no feedback dependency, first-interaction readiness) outweigh any effectiveness loss. Power analysis confirms N=140/group provides 80% power for TOST at d = 0.35 (Lakens, 2017). Analysis uses GLMMs with crossed random effects for participants and items (Baayen et al., 2008; Westfall et al., 2014) to account for question-specific variance. Unlike prior adaptive approaches that require learned user models from prior interactions (Li et al., CHI 2025), our uncertainty-gated condition requires no user state measurement and works from the first interaction. Uniquely, we include a fairness analysis—motivated by 'Unequal Uncertainty' (2508.07872)—examining whether uncertainty-gated interventions trigger disproportionately across demographic groups. We explicitly acknowledge the ecological validity limitation that accuracy feedback (provided for comparability) is rarely available in deployment, and argue—supported by Okamura & Yamada (CHI 2024)—that uncertainty-gating's relative advantage is likely *larger* in practice because trust calibration degrades without feedback while uncertainty-gating is feedback-independent. This work bridges uncertainty quantification in NLP with adaptive explanation design in HCI, offering both a principled comparison of gating strategies and a deployable framework that requires no user state measurement.\n\n## Core Problem\nWhich gating signal—model uncertainty (automatic, available from first interaction) or user trust (self-reported, requiring repeated measurement)—better governs when to present dual explanations for reducing LLM overreliance, and does uncertainty-based gating introduce demographic fairness risks through differential triggering?\n\n## Opportunity\nTwo recent lines of work create a convergent opportunity. First, the 'false trust' study (2605.10930, May 2026) establishes that dual explanations (pro + contra arguments) are the *only* explanation type that genuinely improves users' ability to distinguish correct from incorrect LLM outputs—all other types merely increase acceptance. Second, 'Adjust for Trust' (2502.13321, IUI 2026) demonstrates that adaptively triggering counter-explanations based on user trust reduces inappropriate reliance by up to 38%. However, their approach requires obtrusive trust self-reports after every decision and real-time accuracy feedback—conditions rarely met in deployment. Their own analysis reveals that predicting trust from behavioral signals alone achieves F1 ≤ 0.5, making passive trust detection impractical, and they explicitly acknowledge that 'a key assumption of our setup does not hold in most real-world settings: that both parties have access to real-time feedback about decision accuracy.' Model uncertainty offers a complementary gating signal: it is computed automatically, requires no user input, works from the first interaction, and—critically—does not depend on accuracy feedback for calibration. Yet no work has empirically compared these two gating strategies. Meanwhile, 'The Persuasion Paradox' (2604.03237) shows that explanation effectiveness is strongly task-dependent—explanations help for language-based reasoning (72.5% accuracy vs. 48.5% baseline on LSAT) but hurt for visual reasoning—suggesting that uncertainty-gated explanation switching is most valuable precisely for the knowledge QA domain where explanations are effective. Critically, 'To Rely or Not to Rely?' (2412.15584, CHI 2025) finds that *displaying* uncertainty to users (via token-level probability highlighting) actually backfires—increasing algorithm aversion without improving appropriate reliance. This counter-evidence is important because it shows that uncertainty information is counterproductive when presented directly to users, but it does not indict using uncertainty as a *backend gating signal* to select which explanation type to present. Indeed, it strengthens the case for our approach: rather than burdening users with uncertainty visualization, we use uncertainty behind the scenes to select the more effective dual explanation format when model error is likely. The missing piece remains a head-to-head comparison that determines when model uncertainty outperforms, matches, or falls short of trust-based gating, while also measuring the fairness implications that 'Unequal Uncertainty' (2508.07872) warns about.\n\n## Landscape\nThe false trust paper (2605.10930, May 2026) establishes dual explanations as uniquely effective but tested them uniformly. 'Adjust for Trust' (2502.13321, IUI 2026) is the closest prior work on gating strategy: it gates between supporting and counter-explanations based on self-reported user trust (11-point scale, 0-10), achieving 38% reduction in inappropriate reliance and 20% accuracy improvement across science QA and medical diagnosis with 30 trials per participant. Critically, their trust measurement requires accuracy feedback after each trial and explicit trust surveys—conditions that limit deployment scalability. Their trust threshold (≥8 on 0-10 scale for counter-explanations) was set by visual inspection of reliance curves, not formal optimization. Their attempt to predict trust from interaction features yielded F1 ≤ 0.5. 'From Text to Trust' (Li et al., 2502.11919, CHI 2025) is the closest prior work on adaptive explanation selection: they use a dynamic programming framework with a learned human behavior model to selectively decide which LLM-generated feature analyses to present for tabular AI predictions (income, recidivism; N=447 and N=397, 15 trials per participant), significantly improving appropriate reliance versus always-on and control conditions. However, their approach differs from ours in three key respects: (1) it requires prior interaction data to train the behavior model (cold-start problem), (2) it operates on tabular feature-level analyses rather than natural-language dual explanations, and (3) their gating is based on predicted utility of each analysis rather than on model uncertainty or user trust as explicit signals. Our work complements theirs by comparing two deployment-practical gating signals (model uncertainty and self-reported trust) for a different intervention type (dual pro/contra explanations) in knowledge QA. 'To Rely or Not to Rely?' (Bo et al., 2412.15584, CHI 2025) benchmarks three reliance interventions on N=400 participants across LSAT and image estimation (only 4 trials per participant): Reliance Disclaimer (static warning text), Uncertainty Highlighting (red/pink token-level probability visualization), and Implicit Answer (removing explicit answer statements). Their central finding is sobering: while interventions reduce over-reliance, they generally fail to improve *appropriate* reliance—only Reliance Disclaimer improves the Appropriate Reliance Ratio, and only on LSAT (ARR=1.62 vs. 1.17 control, p=.04). Uncertainty Highlighting specifically backfired, significantly reducing perceived accuracy and helpfulness and increasing algorithm aversion rather than calibrating reliance. This is critical counter-evidence that our approach must address. The key distinction is mechanistic: Bo et al.'s Uncertainty Highlighting *displays* uncertainty information to users, imposing cognitive burden and triggering aversion. Our uncertainty-gated approach uses uncertainty as a *backend signal* to select explanation type—users never see uncertainty scores; they see adaptively selected explanation content. Furthermore, their interventions (disclaimer, highlighting, implicit answer) are simpler cognitive forcing mechanisms, whereas our dual explanation (pro + contra arguments) is the only format shown to genuinely improve discrimination ability (2605.10930). 'Selectively Providing Reliance Calibration Cues' (2302.09995) predicts human reliance behavior to selectively present calibration cues, but uses a learned user model rather than model uncertainty and does not switch explanation types. 'The Persuasion Paradox' (2604.03237) finds that uncertainty-based selective automation outperforms explanations for visual reasoning, but their own results show LLM explanations dramatically improve performance on language-based tasks (LSAT: 72.5% vs. 48.5%), supporting explanation-type switching for knowledge QA. 'Contrastive Explanations That Anticipate Misconceptions' (2410.04253, CHI 2025) generates explanations addressing the gap between AI and user reasoning (N=628, improves decision skills), but applies them uniformly without selective gating. 'Don't Just Translate, Agitate' (2504.12424) proposes LLMs as devil's advocates for XAI but is a position paper without empirical evaluation. 'Why Not Both?' (Frontiers 2025) shows explanations and uncertainty estimates serve complementary roles—uncertainty improves accuracy while explanations improve understanding—supporting the value of combining both signals. 'Unequal Uncertainty' (2508.07872) provides the first socio-technical and legal analysis of uncertainty-gated interventions, showing they can disproportionately affect underrepresented groups through differential triggering rates, creating fairness and legal risks under UK Equality Act 2010. 'Entropy Alone is Insufficient' (2603.21172) demonstrates that semantic entropy has a 'confidently wrong regime' and combining it with a Probability of Correctness probe substantially improves reliability. 'Revisiting Uncertainty Estimation' (2505.23854) shows LLMs have better calibration on reasoning tasks than knowledge-heavy ones across 80 models, and that good calibration does not guarantee effective error ranking—necessitating explicit validation for our QA domain. 'LLMs Should Express Uncertainty Explicitly' (2604.05306) proposes verbalized confidence and reasoning-time uncertainty markers, achieving improved calibration. 'Dissenting Explanations' (AAAI 2024) leverages model multiplicity for disagreeing explanations but applies them uniformly. Partial explanations (de Jong et al., PACM HCI 2025) reduce overreliance through cognitive forcing but do not modulate explanation type. 'Framework for Machine Evaluation of Reasoning Completeness' (Patil, 2510.21884) introduces the RACE framework evaluating alignment between LLM explanations and interpretable feature importance, finding a 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues—relevant context for understanding how explanation quality may covary with model correctness. Multi-AI panel work (2603.22152) finds single dissent reduces conformity while broad disagreement confuses. Uncertainty Gating for Cost-Aware XAI (2603.29915) uses epistemic uncertainty to gate explanation methods for ML classifiers, not human overreliance; notably, they use percentile-based thresholds calibrated per dataset across ν ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. No existing work directly compares model uncertainty and user trust as competing gating signals for adaptive explanation presentation in LLM-assisted decision-making.\n\n## Approach\nThe study proceeds in two phases. **Phase 1: Uncertainty Signal Validation.** Before any human-subjects work, we validate the gating signal on our specific task. Using Qwen3-30B-A3B—a Mixture-of-Experts model with 30.5B total parameters but only 3.3B activated per token (128 experts/layer, 8 selected per token)—we generate answers to 200 candidate general-knowledge questions and compute semantic entropy over 10 sampled completions per question. Semantic entropy operates on output-level semantics (clustering sampled completions by meaning), so it is unaffected by MoE routing variability. Following 'Entropy Alone is Insufficient' (2603.21172), we also train a lightweight Probability of Correctness (PC) probe on Qwen3-30B-A3B's hidden-state activations using a held-out set. For the PC probe specifically, we address MoE-specific considerations: we probe the shared residual stream representations (post-attention, pre-MoE routing) rather than post-expert states, avoiding the routing variability where different tokens activate different expert subsets. We validate probe stability by measuring variance across multiple forward passes on identical inputs, since MoE routing is deterministic for greedy decoding but may vary under sampling. Alternatively, we can adopt the Semantic Entropy Probes approach (Kossen et al., 2024), which approximates semantic entropy from single-generation hidden states, eliminating the need for multiple samples entirely. We combine semantic entropy and PC probe scores via logistic regression to produce a hybrid uncertainty signal. We require AUROC ≥ 0.75 for distinguishing correct from incorrect answers before proceeding; if this threshold is not met, we evaluate alternative models (Llama-4-Scout-17B, Mixtral-8x22B) or uncertainty methods (semantic energy, verbalized confidence per 2604.05306). **Threshold calibration:** The uncertainty gating threshold is set at the Youden's J optimal cutpoint (maximizing sensitivity + specificity − 1) on Phase 1 validation data, with bootstrap 95% CI for the cutpoint to quantify threshold uncertainty. Cross-validation (leave-20%-out) prevents overfitting on the 200-question set. From validated questions, we select 30 for the main study (15 where the model is correct, 15 where it is incorrect, balanced across uncertainty levels and topic domains). The increase from 20 to 30 items matches the 'Adjust for Trust' protocol (30 trials per participant) and provides sufficient levels for stable item-level random effects estimation in the GLMM analysis (Westfall, Kenny, & Judd, 2014, show that with ≤8 items, maximal attainable power is <0.5 regardless of participant N; 30 items is well above this threshold and above the ≥5-level minimum recommended by Gelman & Hill, 2006). **Phase 2: Comparative User Study.** A preregistered between-subjects study (N≈560, 140 per condition) on Prolific with four conditions: (1) **No explanation**—LLM answer only; (2) **Always-on dual explanation**—every answer includes structured pro and contra arguments (replicating the effective condition from 2605.10930); (3) **Trust-gated dual explanation**—participants report trust on an 11-point scale (0-10) after each of the 30 trials; when trust exceeds 8 (adopting the 'Adjust for Trust' threshold, which was empirically calibrated against reliance behavior), the next trial presents dual explanation, otherwise single explanation; (4) **Uncertainty-gated dual explanation**—when the hybrid uncertainty signal exceeds the Youden's J-optimal threshold from Phase 1, dual explanation is presented; otherwise single explanation. **Triggering rate calibration:** In the pilot study (N=60, 15 per condition), we compare empirical triggering rates between Conditions 3 and 4. If rates differ by >15 percentage points, we adjust the uncertainty threshold to the percentile that approximately matches the trust-gated triggering rate, reporting both Youden-optimal and rate-matched thresholds as sensitivity analyses. This ensures condition comparability while preserving transparency about any threshold adjustment. Crucially, unlike the Uncertainty Highlighting intervention in Bo et al. (2412.15584) which *displays* token-level probability information to users (and backfired by increasing algorithm aversion), our uncertainty-gated condition uses uncertainty purely as a backend signal—participants see only the selected explanation format, never the uncertainty estimate itself. This design choice is directly informed by Bo et al.'s finding that user-facing uncertainty visualization is counterproductive. All conditions receive accuracy feedback after each trial (following 'Adjust for Trust' protocol, ensuring comparability). Dual explanations are generated via Claude API with structured prompting (pro: 3-4 sentences supporting the answer; contra: 2-3 sentences presenting the strongest counter-argument and alternative answer), with human review for quality. **Measures**: Primary—overreliance rate (accepting incorrect AI answers), discrimination accuracy (AUROC of accept/reject decisions vs. correctness), appropriate reliance (composite of over- and under-reliance, following the Appropriate Reliance Ratio from Bo et al., 2412.15584). Secondary—cognitive load (NASA-TLX), task completion time, subjective satisfaction (7-point Likert), perceived AI competence. **Analysis plan**: Generalized linear mixed model (GLMM) with a logit link for trial-level accept/reject decisions, including crossed random intercepts for participants and items (questions), and random slopes for condition by item to capture differential treatment effects across questions (following Baayen, Davidson, & Bates, 2008; Westfall, Kenny, & Judd, 2014). Fixed effects: condition (4 levels), item correctness (correct/incorrect), and their interaction. Participant-level covariates: age, education, domain knowledge (pre-test). This approach accounts for item-level variance (question difficulty, topic familiarity) that would otherwise inflate Type I error if items were treated as fixed (Judd, Westfall, & Kenny, 2012). **Equivalence testing specification (H2)**: We use Two One-Sided Tests (TOST; Lakens, 2017) with a pre-registered equivalence margin of Cohen's d = 0.35, justified by cost-benefit SESOI reasoning (Lakens, Scheel, & Isager, 2018): this represents the maximum effectiveness difference at which uncertainty-gating's deployment advantages—no user surveys, no accuracy feedback dependency, first-interaction readiness—still outweigh the performance loss versus trust-gating. In raw terms, d = 0.35 corresponds to approximately 7 percentage points on overreliance rate (assuming participant-level SD ≈ 0.20), meaning we accept non-inferiority if uncertainty-gating's overreliance rate is no more than 7pp higher than trust-gating's. As sensitivity analyses, we also report equivalence tests at d = 0.25 (stricter) and d = 0.50 (more lenient) to demonstrate robustness to margin specification. **Power analysis**: For H2 (TOST non-inferiority, d = 0.35 bounds, α = 0.05): N = 140 per group provides ~80% power (computed via TOSTER::power_t_TOST; consistent with Lakens, 2017, Table 1: d = 0.30 requires N = 191/group, d = 0.40 requires N = 108/group, interpolating to ~140 for d = 0.35). For H1 and H3 (superiority tests, expected d ≈ 0.50 based on 'Adjust for Trust' effect sizes): N = 140 per group provides >95% power. Total sample: N = 560 (140 per condition). **Fairness analysis** (RQ3, addressing 'Unequal Uncertainty'): We collect demographic data (gender, race/ethnicity, education, English proficiency) and analyze whether uncertainty-gated dual explanations trigger at different rates for questions where demographic knowledge gaps exist, whether differential triggering correlates with demographics, and whether any differential triggering translates to differential overreliance reduction. **Key hypotheses**: H1—Conditions 3 and 4 both reduce overreliance compared to Condition 1; H2—Condition 4 (uncertainty-gated) achieves non-inferior overreliance reduction compared to Condition 3 (trust-gated), tested via TOST with equivalence margin d = 0.35; H3—Condition 4 produces lower cognitive load and higher satisfaction than Condition 2 (always-on dual); H4—Condition 4 incurs no measurement burden (no trust surveys), making it more practical; H5—Uncertainty-gated triggering rates do not differ significantly across demographic groups (fairness hypothesis, tested as a secondary analysis with appropriate corrections for multiple comparisons). **Ecological validity limitation**: Accuracy feedback after every trial, while necessary for the trust-gated condition (Condition 3) and provided to all conditions for comparability, is rarely available in real-world deployment. The 'Adjust for Trust' authors explicitly acknowledge this limitation. Okamura and Yamada (CHI 2024, arXiv 2111.08222) demonstrate that outcome feedback substantially improves trust calibration, while interpretability alone does not—implying that trust-gating's effectiveness degrades in feedback-free settings. Critically, uncertainty-gating is feedback-independent: the model computes uncertainty from its own outputs regardless of whether users receive outcome information. This means our study likely *underestimates* uncertainty-gating's relative advantage over trust-gating in deployment, because the experimental feedback supports trust calibration that would be absent in practice. We discuss this asymmetry as a key deployment implication: in feedback-scarce environments (the norm for most LLM-assisted decisions), uncertainty-gating may be the *only* viable adaptive strategy, as trust-gating without feedback relies on potentially miscalibrated self-reports that the 'Adjust for Trust' authors themselves note may reflect 'potentially incorrect perceptions of expertise.' A follow-up study varying feedback availability (present vs. absent) across both gating conditions would directly quantify this interaction and is identified as priority future work.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '300-400 (Qwen3-30B-A3B hosting for Phase 1 validation: ~2K questions × 10 samples + PC probe training on shared residual stream representations; Phase 2: ~10K inference calls × 10 samples for pilot + main study on A100-80GB; note Qwen3-30B-A3B activates only 3.3B parameters per token, reducing per-inference cost vs. dense 30B models)', 'timeline': '5-7 months (Month 1: system build + Phase 1 uncertainty validation + threshold calibration; Month 2: IRB submission + pilot design; Month 3: IRB approval + pilot N=60 + triggering rate calibration; Month 4: pilot analysis + main study refinement; Month 5: main study N≈560; Month 6-7: analysis + writing; aggressive 4.5-month variant possible if IRB uses expedited review for minimal-risk online study)', 'estimated_gpu_cost': '$700-1000 (A100 at ~$3/hr; MoE efficiency reduces per-inference cost)'}, 'human_in_loop': {'gpu_hours': '200-300 (Claude API generates candidate explanations and counter-arguments; GPU only for Qwen3-30B-A3B uncertainty estimation and PC probe training)', 'timeline': '4.5-6 months (Claude accelerates explanation generation, stimulus quality control, statistical modeling, and fairness analysis code)', 'claude_api_cost': '$600-900 (explanation generation for 200 candidate + 30 final questions × 4 conditions × multiple pilot rounds, plus analysis assistance)', 'estimated_gpu_cost': '$500-750'}, 'auto_research': {'gpu_hours': '200-300', 'timeline': '4.5-6 months minimum', 'claude_api_cost': '$900-1400 (automated stimulus optimization, power analysis simulation, equivalence testing code, fairness analysis, draft writing)', 'estimated_gpu_cost': '$500-750', 'speed_bottleneck': 'IRB approval (4-8 weeks, expedited review possible for minimal-risk online survey) and Prolific data collection (~2-3 weeks for N=560) are non-automatable; participant compensation ~$6,200-7,000 (560 participants × ~40 min average session × $12/hr Prolific recommended minimum + 33.3% Prolific academic service fee + ~10% buffer for rejections/replacements; Condition 3 sessions may extend to ~45 min due to trust surveys after each of 30 trials); trust measurement in Condition 3 requires interactive protocol that may extend session duration'}}\n\n## Inspired By\nThe 'Adjust for Trust' finding that trust-gated counter-explanations reduce overreliance by 38%—combined with their own limitation that trust cannot be reliably predicted from behavior (F1 ≤ 0.5) and their acknowledgment that accuracy feedback is unavailable in most deployment settings—directly motivates testing model uncertainty as a practical alternative gating signal. The convergence of (1) dual explanations as uniquely effective (2605.10930), (2) adaptive gating as effective but trust-measurement-limited (2502.13321), (3) adaptive explanation selection as effective but requiring learned user models (2502.11919), (4) 'Entropy Alone is Insufficient' showing hybrid uncertainty signals improve reliability (2603.21172), (5) uncertainty *display* backfiring while the underlying signal remains informative (2412.15584), and (6) 'Unequal Uncertainty' raising fairness concerns about uncertainty-gated interventions (2508.07872) creates a well-motivated research question that no single prior paper addresses.\n\n## Target Venues\n- CHI 2027 (paper deadline Sep 10, 2026 — aggressive but achievable with 4.5-month timeline if Phase 1 validates quickly and IRB uses expedited review; flagship HCI venue, strong fit for adaptive AI-assisted decision-making comparison study; revise-and-resubmit process available)\n- CSCW 2027 (rolling submission from Jan 2027 — comfortable primary target if CHI 2027 timeline proves too tight; strongest fit for adaptive AI-assisted decision-making with fairness analysis; 3-4 month review cycle)\n- FAccT 2027 (estimated deadline ~Jan 2027 — fairness analysis of uncertainty-gated interventions is strong fit; equity framing as secondary contribution)\n- CHI 2028 (paper deadline ~Sep 2027 — safe fallback if earlier venues require major revision)\n\n## Key References\n- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321) — *primary point of differentiation*: trust-gated adaptive counter-explanations, 38% reduction in inappropriate reliance, 30 trials/participant, trust ≥ 8 threshold; our Condition 3 replicates their mechanism\n- Evaluating the False Trust engendered by LLM Explanations (arXiv 2605.10930, May 2026) — establishes dual explanations as uniquely effective; motivates explanation type selection\n- From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (Li et al., CHI 2025, arXiv 2502.11919) — dynamic programming framework with learned human behavior model for selectively presenting LLM-generated feature analyses (N=447, N=397, 15 trials/participant); improves appropriate reliance on tabular AI tasks; differs from our work in requiring prior interaction data, operating on feature-level analyses rather than dual explanations, and using predicted utility rather than model uncertainty or trust as gating signal\n- To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models (Bo et al., CHI 2025, arXiv 2412.15584) — benchmarks three reliance interventions (Reliance Disclaimer, Uncertainty Highlighting, Implicit Answer) on N=400 (only 4 trials/participant); finds interventions generally fail to improve appropriate reliance; Uncertainty Highlighting specifically backfires by increasing algorithm aversion; *critical counter-evidence* that motivates our backend-gating design: we use uncertainty to select explanation type, never displaying it to users; Appropriate Reliance Ratio adopted as primary metric\n- The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance (arXiv 2604.03237) — shows explanation effectiveness is task-dependent; supports explanation switching for language-based QA while selective automation is better for visual tasks\n- Selectively Providing Reliance Calibration Cues With Reliance Prediction (arXiv 2302.09995) — selective intervention via predicted reliance behavior; differs in gating signal (user model vs. model uncertainty) and intervention type (calibration cues vs. explanation switching)\n- Contrastive Explanations That Anticipate Human Misconceptions (CHI 2025, arXiv 2410.04253) — human-centered contrastive explanations improve decision skills (N=628); applied uniformly, not selectively gated\n- Don't Just Translate, Agitate: Using LLMs as Devil's Advocates for AI Explanations (arXiv 2504.12424) — position paper proposing LLMs as constructive agitators; no empirical evaluation\n- Why Not Both? Complementing Explanations with Uncertainty (Frontiers in Computer Science 2025) — shows explanations and uncertainty serve complementary roles; supports combining both signals\n- Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI (arXiv 2508.07872) — fairness risks of uncertainty-gated interventions; directly motivates our RQ3 fairness analysis\n- Entropy Alone is Insufficient for Safe Selective Prediction in LLMs (arXiv 2603.21172) — demonstrates 'confidently wrong' regime of semantic entropy; motivates our hybrid SE + PC probe approach\n- Revisiting Uncertainty Estimation and Calibration of Large Language Models (arXiv 2505.23854) — shows calibration varies across 80 models, worse on knowledge vs. reasoning tasks; motivates Phase 1 validation\n- LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306) — verbalized confidence and reasoning-time uncertainty markers improve calibration; alternative uncertainty elicitation if SE fails validation\n- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance (CSCW 2021) — establishes effectiveness-usability tradeoff in CFF interventions\n- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, January 2026) — Assumption CFF reduces overreliance but decreases satisfaction\n- Cognitive Forcing for Better Decision-Making: Reducing Overreliance Through Partial Explanations (PACM HCI 2025) — partial explanations as cognitive forcing; no uncertainty-based modulation\n- Dissenting Explanations: Leveraging Disagreement to Reduce Model Overreliance (AAAI 2024) — model multiplicity for disagreeing explanations; applied uniformly without selective gating\n- More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice (arXiv 2603.22152) — single dissent reduces conformity; supports targeted rather than blanket counter-argumentation\n- Uncertainty Gating for Cost-Aware Explainable AI (arXiv 2603.29915) — uses epistemic uncertainty to gate explanation methods for ML classifiers with percentile-based thresholds; analogous mechanism but entirely different application domain\n- Framework for Machine Evaluation of Reasoning Completeness in Large Language Models for Classification Tasks (Patil, arXiv 2510.21884) — RACE framework evaluating explanation-feature alignment; finds 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues; relevant context for understanding explanation quality covariation with model correctness\n- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (Kossen et al., arXiv 2406.15927) — approximates semantic entropy from single-generation hidden states, reducing computational overhead to near zero; potential efficiency improvement for Phase 1 uncertainty estimation\n- Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (Lakens, 2017, Social Psychological and Personality Science) — TOST procedure and power analysis tables; our equivalence margin and power calculations follow this framework\n- Equivalence Testing for Psychological Research: A Tutorial (Lakens, Scheel, & Isager, 2018, AMPPS) — SESOI justification approaches including cost-benefit analysis; grounds our d = 0.35 margin choice\n- Statistical Power and Optimal Design in Experiments in Which Samples of Participants Respond to Samples of Stimuli (Westfall, Kenny, & Judd, 2014, JEP:General) — power analysis for crossed random effects designs; shows ≤8 items cap maximal power at <0.5; motivates our 30-item stimulus set\n- Mixed-Effects Modeling with Crossed Random Effects for Subjects and Items (Baayen, Davidson, & Bates, 2008, J Memory & Language) — methodological foundation for our GLMM analysis plan with crossed random effects for participants and items\n- Adaptive Trust Calibration for Human-AI Collaboration (Okamura & Yamada, CHI 2024, arXiv 2111.08222) — directly compares feedback vs. no-feedback conditions; shows outcome feedback substantially improves trust calibration while interpretability alone does not; grounds our ecological validity discussion\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:38:56.109Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:38:56.109Z",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:38:56.123Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to write a thorough evaluation. Let me compile the analysis.

---

```
【阶段】: Triage

【重要前置说明 — 致命级别的投稿方向不匹配】

本 proposal 的研究内容是 "LLM 辅助决策中的自适应双重解释呈现"，属于 HCI / Human-AI Decision Making 领域。
然而用户要求评估的目标会议是 **CoRL 2026（Conference on Robot Learning）**。

CoRL 2026 的 Call for Papers 明确要求："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." 涵盖的主题包括：imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception, manipulation, locomotion, robot foundation models 等。

**本 proposal 与 CoRL 的 scope 完全不相关**——没有机器人、没有物理控制、没有 embodied learning。proposal 自身列出的目标会议是 CHI 2027 / CSCW 2027 / FAccT 2027，这些才是合理的投稿方向。投稿 CoRL 几乎必然被 desk reject。

以下评估将从两个层面展开：
(A) 针对 CoRL 2026 的中稿概率（scope mismatch 是压倒性因素）
(B) 针对 proposal 自身 idea 质量的客观评价（假设投稿合适的 HCI venue）

---

【领域调研】:

- **[arXiv 2605.10930] "Evaluating the False Trust engendered by LLM Explanations" (May 2026)**：
  建立了 dual explanations（pro + contra）是唯一真正能提高用户区分 LLM 正确/错误输出能力的解释类型，其他解释类型（reasoning traces, post-hoc explanations）仅增加接受率。论文确认存在，描述准确。这是本 proposal 的核心前提之一。

- **[arXiv 2502.13321] "Adjust for Trust" (IUI 2026)**：
  trust-gated counter-explanations 减少 inappropriate reliance 38%，trust ≥ 8 阈值。需要每次决策后的 trust 自报告和准确性反馈。论文确认存在，描述准确。这是本 proposal 的主要对比基线（Condition 3）。

- **[arXiv 2412.15584] "To Rely or Not to Rely?" (Bo et al., CHI 2025)**：
  在 N=400 上测试 3 种 reliance interventions。Uncertainty Highlighting 反效果（增加 algorithm aversion）。论文确认存在，描述准确。本 proposal 用此论证 "向用户展示不确定性有害，但作为后端信号可行"。

- **[arXiv 2502.11919] "From Text to Trust" (Li et al., CHI 2025)**：
  动态规划框架 + 学习行为模型来选择性呈现 LLM 分析。需要先验交互数据，存在 cold-start 问题。论文确认存在，描述准确。本 proposal 的方法不需要用户历史数据，这是一个差异点。

- **[arXiv 2603.21172] "Entropy Alone is Insufficient" (2026)**：
  展示 semantic entropy 存在 "confidently wrong" regime，将其与 Probability of Correctness probe 结合可提高可靠性。论文确认存在，描述准确。本 proposal 的 Phase 1 技术方案直接来源于此。

- **[arXiv 2508.07872] "Unequal Uncertainty" (2025)**：
  首个关于 uncertainty-gated interventions 公平性风险的社会技术+法律分析。论文确认存在，描述准确。本 proposal 的 RQ3（fairness analysis）受此启发。

- **[arXiv 2603.29915] "Uncertainty Gating for Cost-Aware XAI" (2026)**：
  用 epistemic uncertainty 对 ML 分类器 gate 解释方法。应用场景不同（ML classifiers vs. human overreliance），但机制类似——用 uncertainty 选择是否/哪种解释方法。这是技术层面最接近的工作之一。

- **调研总结**：该领域近期呈现三线汇聚态势：(1) dual/contrastive explanations 被验证有效；(2) adaptive/selective 解释呈现优于 always-on；(3) uncertainty 作为 gating signal 在 XAI 中已有应用但未用于 human overreliance。本 proposal 定位在 (1)+(2)+(3) 的交汇点，但本质上是将已有组件的组合验证——技术组件（SE+PC probe）和解释类型（dual）均来自先前工作，核心贡献在于实验比较。

---

【Trivial Alternative 检验】:

**存在两个 trivial alternative 威胁：**

1. **Always-on dual explanation**：如果 dual explanation 是唯一有效的类型（2605.10930 的结论），为什么不默认总是展示 dual？这是 Condition 2。如果 always-on 和 gated 的效果差异不显著，那么 gating 机制的增量价值为零——甚至 worse（增加了系统复杂度但没有收益）。proposal 把 always-on 作为对照，但没有强论证为什么 always-on 会明显劣于 gated。认知负荷的差异可能存在但难以达到实质性差别。

2. **随机 gating**：一个 50/50 随机决定是否展示 dual explanation 的 baseline，成本为零且无任何用户/模型依赖。如果随机 gating 的效果接近 uncertainty gating，说明"何时展示"其实不重要，重要的只是"有时展示"。proposal 未包含此对照。

**增量价值论证**：proposal 的增量价值主要是 practical（无需用户调查，首次交互即可用），而非 intellectual。如果核心发现是 "uncertainty-gating non-inferior to trust-gating"，审稿人很可能反应是 "I would have guessed this"——因为 uncertainty 与 model correctness 的相关性是已知的（AUROC ≥ 0.75 是 Phase 1 的准入门槛），所以 uncertainty-gating 能工作并不令人惊讶。

---

【前提假设检验】:

1. **"Gating 比 always-on 更好" 假设未充分论证**：proposal 的核心前提是选择性呈现 dual explanation 优于总是呈现。但 2605.10930 发现 dual explanations 整体有效，没有报告 "dual 在 model 正确时有害" 的证据。如果 dual 在 model 正确时无害（只是冗余），那么 gating 的价值缩减为仅 cognitive load 减少——这是一个较弱的卖点。

2. **"Trust-gating 的 38% reduction 可迁移到知识 QA 任务" 假设**：Adjust for Trust 使用 science QA 和 medical diagnosis（30 trials），但 proposal 使用 general-knowledge questions。任务类型差异可能导致 trust-gating 效果不同。proposal 假设效果可比，但未提供论证。

3. **"Uncertainty threshold 对所有问题类型均稳定" 假设**：Youden's J optimal cutpoint 是在 200 个问题的验证集上优化的。不同领域/难度的问题可能需要不同阈值。proposal 假设单一阈值足够。

4. **"非劣效性 margin d=0.35 足以说服审稿人" 假设**：Cohen's d = 0.35 对应 ~7 pp 的 overreliance rate 差异。在一个 baseline overreliance rate 可能为 30-50% 的场景下，7pp 的差异可能是实质性的。审稿人可能质疑这个 margin 过于宽松。

---

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是 "用 model uncertainty 替代 user trust 作为 gating signal"。这个替代思路本身较直观——一旦知道 (a) dual explanations 有效 和 (b) uncertainty estimation 可行，用 uncertainty 来 gate 就是一个自然的工程组合。Uncertainty Gating for Cost-Aware XAI (2603.29915) 已经在 ML 分类器层面用 uncertainty gate 解释方法选择，机制高度类似。"From Text to Trust" (Li et al., CHI 2025) 已经展示了 adaptive explanation selection 的有效性。本 proposal 的差异化在于 (1) 用 uncertainty 而非 learned user model，(2) 非劣效性比较框架，(3) fairness 分析。其中 (1) 是技术上最自然的替代方案，(2) 和 (3) 是方法论贡献但非 conceptual novelty。总体上，这是一个 "well-motivated incremental combination" 而非 "conceptually new idea"。

2. **Significance: 中** — 
   研究问题本身是重要的：如何 scalably 部署 adaptive explanation 是 LLM-assisted decision-making 的实际瓶颈。如果 uncertainty-gating 确实 non-inferior，这对实际部署有价值。但 significance 受限于：(a) 结果预期性高——如果 uncertainty 和 correctness 相关，gating 会工作，这不 surprising；(b) 仅适用于 knowledge QA（Persuasion Paradox 的 task-dependence 发现表明可推广性有限）；(c) 非劣效性结论的实践影响依赖于 margin 选择，不同 margin 得出不同结论。fairness analysis (RQ3) 是有价值的但作为 secondary 分析，影响力有限。

3. **Related Work: 强** — 
   Related work 覆盖极为全面。核心对比工作（Adjust for Trust, false trust, Bo et al., Li et al.）均有准确引用和详细差异化分析。方法论基础（GLMM, TOST, Westfall et al.）也有扎实引用。甚至包括了 fairness（Unequal Uncertainty）、uncertainty estimation（Entropy Alone is Insufficient, SE Probes）、task-dependence（Persuasion Paradox）等边缘但相关的工作。论文引用均经验证真实。唯一微小遗漏：可以更深入讨论 "Why Not Both?"（Frontiers 2025）中 uncertainty 和 explanation 互补关系的具体发现。

---

【概率估计 — CoRL 2026】: 0% - 3% 中位 1%

【估计理由 — CoRL 2026】: 
这是一个完全的 scope mismatch。CoRL 要求 "focus on a core robotics problem"，本 proposal 关于 LLM 文本解释的 human-AI decision-making，没有任何机器人、物理控制、embodied learning 成分。会被 desk reject。

---

【概率估计 — 假设投稿合适 venue (CHI/CSCW)】: 20% - 33% 中位 25%

【估计理由 — 假设合适 venue】: 
Related Work 维度强，methodological rigor 很高（preregistered, TOST, GLMMs, fairness），这些都会帮助通过审查。但 **idea 的 novelty 上限限制了总概率**：核心贡献是组件重组（现有 uncertainty method + 现有 dual explanation + 比较研究），审稿人大概率反应为 "I would have guessed this works"。非劣效性框架虽然在 HCI 中较少见（这是加分项），但不足以弥补 conceptual novelty 的不足。always-on dual 作为 trivial alternative 的威胁也会被审稿人注意到。对于 CHI 而言可能落在 borderline 区域；对 CSCW 稍好（fairness 角度 + 实践部署论证更被重视）。

【主要风险】: 
1. **"Why not always-on?" 威胁**：如果 always-on dual（Condition 2）效果与 gated conditions 相当，审稿人会质疑整个 gating 框架的价值——"the complexity of uncertainty estimation adds nothing over simply always showing dual explanations." 这是最可能的致命质疑。
2. **Novelty 不足被挑战**：核心思路（用 uncertainty gate 解释类型）过于自然/直觉，审稿人可能评价为 "competent execution of an obvious idea"，在 competitive venue 中 novelty bar 不够。
```

**补充说明**：

本 proposal 的 **形式完善度极高**——preregistered design, TOST equivalence testing, GLMM with crossed random effects, fairness analysis, ecological validity discussion 等，在方法论层面几乎无可挑剔。但正如评估原则所强调的，形式完善度 ≠ idea 好。透过形式看本质，核心问 "用 model uncertainty 替代 trust 做 gating" 是一个工程层面自然且可预测的替代方案，而非 conceptual breakthrough。

如果目标确实是 CoRL，建议 **不要投稿此 proposal**，这是完全错误的 venue。如果目标是 CHI/CSCW，建议在迭代中重点解决 "为什么 gating 比 always-on 更好" 的论证，以及增加 conceptual novelty（例如发现 uncertainty-gating 在某些条件下 *优于* trust-gating 的机制性解释，而非仅做非劣效性验证）。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Adjust for Trust (arXiv 2502.13321)](https://arxiv.org/abs/2502.13321)
- [Evaluating the False Trust (arXiv 2605.10930)](https://arxiv.org/abs/2605.10930)
- [To Rely or Not to Rely (arXiv 2412.15584)](https://arxiv.org/abs/2412.15584)
- [From Text to Trust (arXiv 2502.11919)](https://arxiv.org/abs/2502.11919)
- [Entropy Alone is Insufficient (arXiv 2603.21172)](https://arxiv.org/abs/2603.21172)
- [Unequal Uncertainty (arXiv 2508.07872)](https://arxiv.org/abs/2508.07872)
- [Uncertainty Gating for Cost-Aware XAI (arXiv 2603.29915)](https://arxiv.org/html/2603.29915v1)
- [Semantic Entropy Probes (arXiv 2406.15927)](https://arxiv.org/abs/2406.15927)
- [LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306)](https://arxiv.org/html/2604.05306)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance" (IUI 2026, arXiv 2502.13321): 
   最直接的先行工作。提出基于用户自报信任度的自适应反向解释策略，在科学问答和医学诊断任务中将不当依赖降低38%。但需要每次决策后用户填写信任量表+准确性反馈，部署成本高。该 proposal 的 Condition 3 直接复现此机制。论文确实存在且描述准确。

2. "Evaluating the False Trust engendered by LLM Explanations" (arXiv 2605.10930, May 2026): 
   确认双重解释（pro + contra）是唯一真正提高用户区分正确/错误 LLM 输出能力的解释类型，其他类型仅增加接受率。论文存在，描述准确，是 proposal 的关键动机之一。

3. "To Rely or Not to Rely?" (Bo et al., CHI 2025, arXiv 2412.15584): 
   测试三种干预措施，发现 Uncertainty Highlighting 直接向用户展示不确定性反而加剧算法厌恶。论文存在且描述准确。Proposal 利用此发现论证"后端使用不确定性而非前端展示"的设计合理性。

4. "From Text to Trust" (Li et al., CHI 2025, arXiv 2502.11919): 
   使用动态规划框架+学习的人类行为模型来选择性展示 LLM 生成的特征分析。需要先前交互数据（冷启动问题），操作对象为表格数据特征分析而非自然语言双重解释。论文存在，描述准确。

5. "Uncertainty Gating for Cost-Aware Explainable AI" (arXiv 2603.29915): 
   使用认知不确定性来门控解释方法（选择不同的 XAI 方法），但针对传统 ML 分类器而非 LLM 辅助决策中的人类过度依赖。机制类似但应用域不同。

6. "Unequal Uncertainty" (arXiv 2508.07872): 
   首次对基于不确定性的算法干预进行社会技术+法律分析，指出不确定性阈值可能对代表性不足的群体产生不成比例的影响。论文存在，proposal 的公平性分析 (RQ3) 直接受此启发。

7. "Entropy Alone is Insufficient for Safe Selective Prediction in LLMs" (arXiv 2603.21172): 
   证明语义熵存在"自信但错误"区域，结合 Probability of Correctness probe 显著提高可靠性。Proposal 的混合不确定性估计器直接来源于此。

8. "Semantic Entropy Probes" (Kossen et al., arXiv 2406.15927): 
   从单次生成的隐藏状态近似语义熵，大幅降低计算成本。Proposal 将其作为 Phase 1 的备选方案。

- 调研总结: 这个领域（LLM 辅助决策中的自适应解释/干预）在 2024-2026 年非常活跃，"什么时候该给什么样的解释"是一个被广泛关注的问题。核心先行工作——信任门控 (IUI 2026) 和双重解释有效性 (2605.10930)——都是 2026 年的最新成果，proposal 的定位是对这些工作的自然组合与实用性改进。但"用模型不确定性替代用户信任度作为门控信号"这个想法本身是一个相当直觉化的工程替代，而非概念层面的突破。


【Trivial Alternative 检验】:

**存在严重的 trivial alternative 威胁：Always-On Dual Explanation (Condition 2)。**

如果 2605.10930 已经证明双重解释是唯一真正有效的解释类型，那么最简单的策略就是**始终展示双重解释**——不需要任何门控信号、不需要不确定性估计、不需要信任量表、零额外部署成本。Proposal 确实包含了这个条件作为 baseline (Condition 2)，但这恰恰暴露了核心逻辑的薄弱：

- 如果 always-on ≈ uncertainty-gated，那门控的价值存疑（唯一可能的 argument 是降低认知负荷，但这需要 H3 positive 来支撑，而这本身是一个较弱的预期效应）
- 如果 always-on > uncertainty-gated，那 uncertainty-gating 就输给了 trivial baseline
- 只有 uncertainty-gated > always-on（选择性触发比始终触发更好）才能充分证明门控的价值，但 proposal 并没有将此设为核心假设

增量价值主要落在**实用性层面**（不需要用户问卷、首次交互即可用）相对于 trust-gating 的优势，以及**认知负荷**层面相对于 always-on 的优势。这些是工程/部署论证，不是科学洞见。


【前提假设检验】:

核心逻辑链中有以下未经验证的关键假设：

1. **"模型不确定性高 ≈ 用户最需要双重解释的时刻"**——这是整个 idea 的核心假设，但没有理论或实证支撑。模型不确定性高意味着模型可能出错，但用户过度依赖的原因是多方面的（过度信任、认知懒惰、锚定效应等），不确定性高的题目不一定是用户最容易过度依赖的题目。信任门控至少直接测量了用户状态，而不确定性门控假设模型状态可以替代用户状态——这个替代性本身就是需要被验证的。

2. **非劣效性框架的预设立场**——H2 使用 TOST 检验"不确定性门控不劣于信任门控"（Cohen's d = 0.35 等价边界），这意味着 proposal 的"最佳结果"仅仅是"大致一样有效"。如果一个研究的天花板就是"我的新方法和旧方法差不多"，其学术贡献主要在实用性而非科学发现。

3. **假设 Qwen3-30B-A3B 的混合不确定性估计器能在通用知识问答上达到 AUROC ≥ 0.75**——虽然 proposal 设置了 fallback 方案，但如果这个阈值达不到，整个研究的基础就不存在。2505.23854 已经指出 LLM 在知识密集型任务上的校准比推理任务差。

4. **假设"准确性反馈"这个实验条件的引入不会严重扭曲生态效度**——proposal 自己承认准确性反馈在部署中罕见，但所有条件都提供了反馈。这意味着 uncertainty-gating 在实验中的相对优势可能被低估（如 proposal 所述），但也可能意味着实验结果对真实部署场景的外推存在系统性偏差。


【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是"用模型不确定性替代用户信任度作为双重解释的门控信号"。这是一个自然、直觉化的工程替代，而非概念突破。
   - "Adjust for Trust" (IUI 2026) 已建立自适应门控框架
   - "Uncertainty Gating for Cost-Aware XAI" (2603.29915) 已在 ML 分类器上使用不确定性做解释门控
   - Li et al. (CHI 2025) 已建立自适应解释选择框架
   - 本 proposal 的增量是将"不确定性作为后端门控"应用到"双重解释"场景——组合性贡献而非原创性贡献
   - "后端使用 vs 前端展示"不确定性的区分有一定见解，但更像是工程设计选择而非理论洞见（Bo et al. 的发现已经隐含了这个方向）
   - 如果核心发现是 positive（不确定性门控 ≈ 信任门控），审稿人很可能说 "I would have guessed this"——用模型内部信号替代人工问卷直觉上是合理的

2. **Significance: 中** — 研究问题在 HCI/AI-assisted decision making 领域有实际价值：部署中如何无侵入地实现自适应解释是一个真实痛点。
   - 但对领域的推动是渐进式的：主要贡献是实用性改进（去掉问卷）而非新的理解或理论
   - 公平性分析 (RQ3) 是有意义的补充，但作为二级贡献，不足以独立支撑论文
   - 非劣效性框架限制了学术影响力的上限——即使所有假设成立，结论也只是"可以用不确定性替代信任度，效果差不多"
   - 对 NLP/CL 领域的贡献有限，更多是 HCI 贡献
   - **关键问题：这是一篇 CHI/CSCW 论文，不是 CoRL 论文**（见下文）

3. **Related Work: 强** — 对已有工作的覆盖非常充分且准确。
   - 所有核心引用（2605.10930, 2502.13321, 2412.15584, 2502.11919, 2603.21172, 2508.07872）均经验证存在且描述准确
   - 差异化定位清晰：明确区分了与 "Adjust for Trust"（门控信号不同）、Li et al.（任务域和方法不同）、Bo et al.（前端展示 vs 后端门控）的差异
   - 对 uncertainty quantification 文献的覆盖也足够（semantic entropy, PC probes, calibration）
   - 对最新 2025-2026 工作的跟踪及时


【概率估计】: [0% - 3%] 中位 1%

【估计理由】: 
**概率估计受到致命的 venue mismatch 约束。** CoRL (Conference on Robot Learning) 是一个聚焦机器人学习的单轨会议，核心话题包括：机器人感知与控制的学习表征、模仿学习、强化学习、sim-to-real、机器人操作等。本 proposal 是一项纯 HCI 用户研究，涉及 LLM 辅助知识问答中的解释设计和人类过度依赖——**与机器人学习没有任何交集**。没有物理机器人、没有控制策略、没有感知系统、没有仿真环境。即使 idea 本身在 HCI 领域有一定价值，投稿 CoRL 也几乎必然被 desk rejection。

如果抛开 venue mismatch 纯评 idea 质量（假设投稿 CHI/CSCW），概率估计约为 **[20% - 35%] 中位 27%**：idea 方向正确且有实际需求，但核心贡献是组合性/工程性的而非原创性的，非劣效性框架限制了学术影响力上限，且面临 always-on dual explanation 这一 trivial alternative 的严重威胁。Novelty 维度是主要限制因素。

【主要风险】:
1. **致命的 venue 不匹配**：CoRL 是机器人学习会议，本 proposal 是 HCI 用户研究，与 CoRL 的 scope 完全不重叠，几乎确定被 desk reject。
2. **Trivial alternative 威胁**（idea 层面）：Always-on dual explanation 是一个零成本的替代方案，如果其效果接近或优于 uncertainty-gating，则门控机制的增量价值难以成立。核心创新沦为"差不多一样好但更方便"的实用性论证，这对顶会 novelty 要求而言不够。
```

**补充说明：**

该 proposal 自身列出的目标 venue 是 CHI 2027、CSCW 2027、FAccT 2027——这些都是合理的 venue 选择。但用户询问的是 **CoRL 2026** 的中稿潜力，这存在根本性的 scope 不匹配。建议将投稿目标调整回 proposal 原始规划的 HCI 会议。

即使在 CHI/CSCW 的语境下，idea 的核心瓶颈仍然是 **novelty 不够强**：核心贡献是一个直觉化的工程替代（用不确定性替代信任问卷），非劣效性框架进一步削弱了学术影响力上限。要提升中稿概率，需要在 idea 层面找到超越 "practical alternative" 的 deeper insight——例如，不确定性门控和信任门控在何种条件下会 diverge（不仅仅是"差不多"），或者为什么模型不确定性能捕捉到用户信任度捕捉不到的过度依赖模式。

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make an informed assessment. Let me write up the triage evaluation.

---

```
【阶段】: Triage

【⚠️ 严重前置问题：投稿目标与 proposal 内容的根本性错配】

本 proposal 的内容是 HCI 领域的 human-AI decision-making 用户研究（自适应解释呈现策略比较），
proposal 自身列出的目标会议为 CHI 2027、CSCW 2027、FAccT 2027。
然而系统指定的评估目标是 **CoRL 2026（Conference on Robot Learning）**——
CoRL 的核心 scope 是机器人学习（manipulation, locomotion, planning, sim-to-real, RL for robotics 等），
与本 proposal 的研究主题（LLM 解释呈现策略的用户研究）**完全不相关**。

如果强行投稿 CoRL 2026，预计会在 desk review 阶段被拒（scope mismatch），
中稿概率接近 0%，与 idea 质量无关。

以下评估将 **独立于 venue fit** 客观评价 idea 本身的质量，概率估计同时给出
CoRL 场景和 proposal 自身目标 venue（CHI/CSCW）场景的估计。


【领域调研】:

- [2605.10930] "Evaluating the False Trust engendered by LLM Explanations" (arXiv, May 2026):
  确认存在。发现 dual explanations（pro + contra）是唯一真正改善用户辨别 LLM 正确/错误
  能力的解释类型；其他解释类型仅增加接受率。本 proposal 的核心前提之一。

- [2502.13321] "Adjust for Trust" (IUI 2026):
  确认存在。基于自报告 trust 自适应触发 counter-explanation，减少 38% 不当依赖。
  关键局限：需要每次决策后的 trust 自报告 + 准确度反馈。本 proposal 的主要对比对象。

- [2412.15584] Bo et al., "To Rely or Not to Rely?" (CHI 2025):
  确认存在。发现 uncertainty highlighting 直接展示给用户会适得其反（增加 algorithm aversion）。
  本 proposal 用此证据支持"后端 gating"设计（不向用户展示 uncertainty），论证链成立。

- [2502.11919] Li et al., "From Text to Trust" (CHI 2025):
  确认存在。动态规划框架 + learned user model 自适应选择 LLM feature analyses，
  需要先验交互数据（cold-start 问题）。与本 proposal 的 gating 信号不同。

- [2508.07872] "Unequal Uncertainty" (arXiv):
  确认存在。首个对 uncertainty-gated interventions 的社会技术 + 法律分析，
  证明 uncertainty 阈值可能对 underrepresented groups 产生不成比例的影响。

- [2603.21172] "Entropy Alone is Insufficient" (arXiv 2026):
  确认存在。指出 semantic entropy 的"confidently wrong"问题，
  提出结合 Probability of Correctness probe 的混合方法。

- [2603.29915] "Uncertainty Gating for Cost-Aware XAI" (arXiv 2026):
  确认存在。用 epistemic uncertainty 门控 ML classifier 的解释方法选择，
  但应用场景是 ML 模型解释成本优化，不涉及人类过度依赖问题。

- Semantic Entropy Probes (Kossen et al., 2406.15927):
  确认存在。从单次生成的 hidden states 近似 semantic entropy，大幅降低计算开销。

- 调研总结：自适应解释呈现（adaptive explanation presentation）是 2025-2026 HCI 领域
  的活跃方向。"trust-gated"和"uncertainty-based"分别已有独立工作，但 **head-to-head
  comparison 确实尚未出现**。核心 gap 是真实的，但 gap 的性质是"两个已知方法的
  系统性比较"，而非"提出新方法"。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **Always-on dual explanation（Condition 2）**：如果 dual explanation 是唯一有效的
   解释类型（2605.10930），最简单的策略就是"总是提供 dual explanation"。selective gating
   的价值取决于 always-on 是否有显著的副作用（认知负荷增加、满意度下降），但 proposal
   自己承认这只是 H3（Condition 4 vs. Condition 2 的认知负荷比较），且 effect size
   未必大。如果 always-on 的代价很小，整个 gating 框架的必要性就被削弱了。

2. **Random gating baseline 缺失**：如果比较的是"uncertainty gating vs. trust gating"，
   一个关键问题是：是否**任何 selective gating**（甚至随机触发）都已经足够好？
   缺少随机触发 baseline 无法排除这一可能性。

增量价值的论证依赖于：(a) always-on 有显著认知负荷代价，且 (b) uncertainty gating
的选择性（而非随机性）对效果有贡献。这两个前提都未被预先验证。


【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的假设：

1. **"Uncertainty 信号在 general-knowledge QA 任务上能达到 AUROC ≥ 0.75"**——
   proposal 自己引用 2505.23854 指出 LLM 在 knowledge-heavy 任务上的 calibration
   比 reasoning 任务更差。虽然 proposal 设了 0.75 阈值和 fallback 方案，但如果
   Phase 1 失败，整个研究的核心比较就无法进行。这是一个 **前提性假设**。

2. **"Non-inferiority = practical superiority" 的论证跳跃**——H2 测试的是 uncertainty-gating
   不劣于 trust-gating（d ≤ 0.35）。但"不劣于 + 无需用户调查"→ "实践中更优" 的
   推理需要假设部署场景中确实不存在 trust 信号的替代获取方式（如 behavioral indicators、
   implicit feedback 等）。虽然 proposal 引用了 F1 ≤ 0.5 的被动 trust 检测结果，
   但这来自单一研究，且 NLP 领域的 behavioral modeling 进展很快。

3. **"Accuracy feedback 不影响 uncertainty-gating 但严重影响 trust-gating"**——
   proposal 的生态效度论证假设在无反馈场景下 uncertainty-gating 的相对优势会"更大"。
   但反馈的缺失也可能改变用户与系统的整体交互模式（如降低 engagement），这种
   交互效应并未被建模。

4. **跨任务可迁移性假设**——整个研究在 general-knowledge QA 上进行，但 claim
   推广到了"LLM-assisted decision-making" 这一更大范畴。2604.03237 的发现恰恰
   表明解释效果高度依赖任务类型，这限制了结论的推广性。


【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是**两个已知方法的系统性比较**（trust-gating vs. uncertainty-gating），
   而非提出新方法或新理论。"head-to-head comparison 尚未出现"是真实的 gap，
   但这种 gap 的性质是 empirical comparison，novelty 来自 "做比较" 本身。
   调研确认 [2502.13321] 提出 trust-gating，[2603.21172] 和 [2406.15927] 提供
   uncertainty estimation 工具，[2603.29915] 已将 uncertainty 用于 gating 解释方法。
   本 proposal 的独特组合（uncertainty gating + dual explanation + user study）
   确有增量新意，但核心 insight（"uncertainty 可以替代 trust 作为 gating signal"）
   在概念层面并不 surprising。如果结果是 positive（uncertainty-gating non-inferior），
   多数审稿人的反应可能是 **"makes sense, I would have guessed this"** 而非 "surprising"。
   
   非劣效性（non-inferiority）的实验设计进一步限制了 novelty 上限：最佳结果是
   "和已有方法一样好但更方便"——这是工程/实践贡献而非科学发现。

2. **Significance: 中** — 
   研究问题有实际意义：如何在不需要用户自报告的情况下实现自适应解释呈现。
   这对 LLM 部署场景有直接价值。但影响范围受到多重限制：
   (a) 仅在 general-knowledge QA 一个任务类型上验证，[2604.03237] 已证明
   跨任务迁移性差；
   (b) 核心发现的 surprise factor 低——如果 uncertainty-gating 确实 non-inferior，
   审稿人可能觉得这是预期之内的；
   (c) 如果 uncertainty-gating 实际上 inferior，那结论变成"trust-gating 更好但
   不实用"，这也不是特别有影响力的发现。
   公平性分析（RQ3）增加了一些 significance 但感觉是附加的而非核心。

3. **Related Work: 强** — 
   这是本 proposal 最突出的优点。Related work 覆盖非常全面、准确：
   - 核心对比论文 [2502.13321]、[2605.10930]、[2412.15584] 均经调研确认真实存在
     且描述准确
   - 差异化定位清晰（vs. Li et al. [2502.11919] 的 learned user model，
     vs. Bo et al. 的 user-facing uncertainty display，vs. [2603.29915] 的 ML classifier
     成本优化）
   - 对 counter-evidence 的处理诚实（如 Bo et al. 的 uncertainty highlighting 反效果）
   - 方法论参考文献（Lakens 2017, Westfall et al. 2014, Baayen et al. 2008）
     均为领域标准
   - 唯一缺失：缺少对 2025-2026 年 CHI/CSCW 领域更广泛的 adaptive AI interaction
     工作的覆盖（如 Human-AI Deliberation 等新方向）


【概率估计】:

→ **CoRL 2026**: 0-2%（中位 1%）
   理由：完全的 scope mismatch，会在 desk review 被拒，与 idea 质量无关。

→ **CHI 2027 / CSCW 2027（proposal 实际目标 venue）**: 20-32%（中位 25%）
   基于 idea 质量的估计，不含执行层面因素。

【估计理由】:

以 CHI/CSCW 为参考（因为 CoRL 是纯 scope 问题）：

Idea 处于 rubric 的 25-35% 区间——方向正确、gap 真实、related work 强，但
核心 novelty 是 "两个已知方法的系统比较"，最佳结果（non-inferiority）的 surprise 
factor 低。审稿人大概率的反应是 "well-executed comparison study, but limited 
novelty / I would have guessed this result"。

上界受限的主要因素是 **Novelty**：这是一个 empirical comparison 而非 method/theory 
贡献，且非劣效性设计意味着正面结果本身 = "和已有方法一样好"。如果投 CSCW（更看重
empirical HCI contribution），概率可能接近上界；如果投 CHI（更看重 novelty），
可能在下界附近。

下界被 Related Work 的强度和实验设计的严谨性（TOST, GLMM, preregistration）
支撑——这降低了被拒的概率下限。

【主要风险】:

1. **"Comparison study, limited novelty" 拒稿理由**：审稿人可能认为这是一个
   工程性比较（比较两个现成方法在用户研究中的表现），缺乏深层的科学洞见或
   方法创新。Non-inferiority design 使得最佳结果是 "一样好但更方便"，
   这不够 surprising。

2. **Trivial alternative 威胁（always-on dual explanation）**：如果 always-on 
   dual explanation 的认知负荷代价不大，审稿人会质疑整个 selective gating 框架
   的必要性——"为什么不直接总是给 dual explanation？"
```

---

**补充说明**：

关于 CoRL 2026 的 scope 问题，这是一个**致命性的 venue mismatch**。CoRL 关注的是机器人学习（robot manipulation, locomotion, navigation, sim-to-real, RL for robotics），而本 proposal 是一个纯 HCI 用户研究，研究 LLM 解释呈现策略。即使 idea 本身是 ACM CHI best paper 水平，投 CoRL 也会被直接 desk reject。

如果评估目标确实是 CoRL，建议直接放弃此方向；如果实际目标是 CHI/CSCW（如 proposal 自身所列），则 idea 质量处于"可以做但 novelty 受限"的区间，核心风险在于 comparison study 的 novelty ceiling 较低。

Sources:
- [Evaluating the False Trust engendered by LLM Explanations](https://arxiv.org/abs/2605.10930)
- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance](https://arxiv.org/abs/2502.13321)
- [To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on LLMs](https://arxiv.org/abs/2412.15584)
- [From Text to Trust: Empowering AI-assisted Decision Making](https://arxiv.org/abs/2502.11919)
- [Unequal Uncertainty: Rethinking Algorithmic Interventions](https://arxiv.org/abs/2508.07872)
- [Uncertainty Gating for Cost-Aware Explainable AI](https://arxiv.org/html/2603.29915v1)
- [Semantic Entropy Probes](https://arxiv.org/abs/2406.15927)
- [Entropy Alone is Insufficient for Safe Selective Prediction](https://arxiv.org/abs/2603.21172)


【原始 proposal（允许参考但不是主要依据）】:
# Model Uncertainty vs. User Trust as Gating Signals for Adaptive Dual Explanations in LLM-Assisted Decision-Making

## Description
We propose the first head-to-head comparison of model uncertainty and user trust as gating signals for adaptive dual explanation presentation in LLM-assisted decision-making. Building on three convergent findings—that dual explanations are the only explanation type genuinely reducing overreliance (2605.10930), that trust-gated counter-explanations cut inappropriate reliance by 38% but require obtrusive self-reports and accuracy feedback (Adjust for Trust, IUI 2026), and that displaying uncertainty directly to users backfires by increasing algorithm aversion (Bo et al., CHI 2025)—we test whether automatic model uncertainty can serve as a practical, first-interaction-ready *backend* gating signal that selects explanation type without burdening users. The system uses a validated hybrid uncertainty estimator (semantic entropy + Probability of Correctness probe over Qwen3-30B-A3B's shared residual stream representations, addressing both the 'confidently wrong' regime identified by 2603.21172 and MoE-specific probing considerations) to selectively trigger dual explanations when model error is likely. The uncertainty threshold is set via Youden's J-optimal cutpoint with cross-validated calibration, and triggering rates are verified against the trust-gated condition in a pilot study. A preregistered between-subjects study (N≈560, Prolific) compares four conditions across 30 general-knowledge questions: no explanation, always-on dual explanation, trust-gated dual explanation (replicating the Adjust for Trust mechanism with trust ≥ 8 threshold), and uncertainty-gated dual explanation. We measure overreliance reduction, discrimination accuracy, appropriate reliance ratio, cognitive load, and satisfaction. The central hypothesis (H2) tests non-inferiority of uncertainty-gating via TOST with a pre-registered equivalence margin of Cohen's d = 0.35 (≈7 percentage points on overreliance rate), justified by cost-benefit SESOI reasoning: below this threshold, uncertainty-gating's deployment advantages (no surveys, no feedback dependency, first-interaction readiness) outweigh any effectiveness loss. Power analysis confirms N=140/group provides 80% power for TOST at d = 0.35 (Lakens, 2017). Analysis uses GLMMs with crossed random effects for participants and items (Baayen et al., 2008; Westfall et al., 2014) to account for question-specific variance. Unlike prior adaptive approaches that require learned user models from prior interactions (Li et al., CHI 2025), our uncertainty-gated condition requires no user state measurement and works from the first interaction. Uniquely, we include a fairness analysis—motivated by 'Unequal Uncertainty' (2508.07872)—examining whether uncertainty-gated interventions trigger disproportionately across demographic groups. We explicitly acknowledge the ecological validity limitation that accuracy feedback (provided for comparability) is rarely available in deployment, and argue—supported by Okamura & Yamada (CHI 2024)—that uncertainty-gating's relative advantage is likely *larger* in practice because trust calibration degrades without feedback while uncertainty-gating is feedback-independent. This work bridges uncertainty quantification in NLP with adaptive explanation design in HCI, offering both a principled comparison of gating strategies and a deployable framework that requires no user state measurement.

## Core Problem
Which gating signal—model uncertainty (automatic, available from first interaction) or user trust (self-reported, requiring repeated measurement)—better governs when to present dual explanations for reducing LLM overreliance, and does uncertainty-based gating introduce demographic fairness risks through differential triggering?

## Opportunity
Two recent lines of work create a convergent opportunity. First, the 'false trust' study (2605.10930, May 2026) establishes that dual explanations (pro + contra arguments) are the *only* explanation type that genuinely improves users' ability to distinguish correct from incorrect LLM outputs—all other types merely increase acceptance. Second, 'Adjust for Trust' (2502.13321, IUI 2026) demonstrates that adaptively triggering counter-explanations based on user trust reduces inappropriate reliance by up to 38%. However, their approach requires obtrusive trust self-reports after every decision and real-time accuracy feedback—conditions rarely met in deployment. Their own analysis reveals that predicting trust from behavioral signals alone achieves F1 ≤ 0.5, making passive trust detection impractical, and they explicitly acknowledge that 'a key assumption of our setup does not hold in most real-world settings: that both parties have access to real-time feedback about decision accuracy.' Model uncertainty offers a complementary gating signal: it is computed automatically, requires no user input, works from the first interaction, and—critically—does not depend on accuracy feedback for calibration. Yet no work has empirically compared these two gating strategies. Meanwhile, 'The Persuasion Paradox' (2604.03237) shows that explanation effectiveness is strongly task-dependent—explanations help for language-based reasoning (72.5% accuracy vs. 48.5% baseline on LSAT) but hurt for visual reasoning—suggesting that uncertainty-gated explanation switching is most valuable precisely for the knowledge QA domain where explanations are effective. Critically, 'To Rely or Not to Rely?' (2412.15584, CHI 2025) finds that *displaying* uncertainty to users (via token-level probability highlighting) actually backfires—increasing algorithm aversion without improving appropriate reliance. This counter-evidence is important because it shows that uncertainty information is counterproductive when presented directly to users, but it does not indict using uncertainty as a *backend gating signal* to select which explanation type to present. Indeed, it strengthens the case for our approach: rather than burdening users with uncertainty visualization, we use uncertainty behind the scenes to select the more effective dual explanation format when model error is likely. The missing piece remains a head-to-head comparison that determines when model uncertainty outperforms, matches, or falls short of trust-based gating, while also measuring the fairness implications that 'Unequal Uncertainty' (2508.07872) warns about.

## Landscape
The false trust paper (2605.10930, May 2026) establishes dual explanations as uniquely effective but tested them uniformly. 'Adjust for Trust' (2502.13321, IUI 2026) is the closest prior work on gating strategy: it gates between supporting and counter-explanations based on self-reported user trust (11-point scale, 0-10), achieving 38% reduction in inappropriate reliance and 20% accuracy improvement across science QA and medical diagnosis with 30 trials per participant. Critically, their trust measurement requires accuracy feedback after each trial and explicit trust surveys—conditions that limit deployment scalability. Their trust threshold (≥8 on 0-10 scale for counter-explanations) was set by visual inspection of reliance curves, not formal optimization. Their attempt to predict trust from interaction features yielded F1 ≤ 0.5. 'From Text to Trust' (Li et al., 2502.11919, CHI 2025) is the closest prior work on adaptive explanation selection: they use a dynamic programming framework with a learned human behavior model to selectively decide which LLM-generated feature analyses to present for tabular AI predictions (income, recidivism; N=447 and N=397, 15 trials per participant), significantly improving appropriate reliance versus always-on and control conditions. However, their approach differs from ours in three key respects: (1) it requires prior interaction data to train the behavior model (cold-start problem), (2) it operates on tabular feature-level analyses rather than natural-language dual explanations, and (3) their gating is based on predicted utility of each analysis rather than on model uncertainty or user trust as explicit signals. Our work complements theirs by comparing two deployment-practical gating signals (model uncertainty and self-reported trust) for a different intervention type (dual pro/contra explanations) in knowledge QA. 'To Rely or Not to Rely?' (Bo et al., 2412.15584, CHI 2025) benchmarks three reliance interventions on N=400 participants across LSAT and image estimation (only 4 trials per participant): Reliance Disclaimer (static warning text), Uncertainty Highlighting (red/pink token-level probability visualization), and Implicit Answer (removing explicit answer statements). Their central finding is sobering: while interventions reduce over-reliance, they generally fail to improve *appropriate* reliance—only Reliance Disclaimer improves the Appropriate Reliance Ratio, and only on LSAT (ARR=1.62 vs. 1.17 control, p=.04). Uncertainty Highlighting specifically backfired, significantly reducing perceived accuracy and helpfulness and increasing algorithm aversion rather than calibrating reliance. This is critical counter-evidence that our approach must address. The key distinction is mechanistic: Bo et al.'s Uncertainty Highlighting *displays* uncertainty information to users, imposing cognitive burden and triggering aversion. Our uncertainty-gated approach uses uncertainty as a *backend signal* to select explanation type—users never see uncertainty scores; they see adaptively selected explanation content. Furthermore, their interventions (disclaimer, highlighting, implicit answer) are simpler cognitive forcing mechanisms, whereas our dual explanation (pro + contra arguments) is the only format shown to genuinely improve discrimination ability (2605.10930). 'Selectively Providing Reliance Calibration Cues' (2302.09995) predicts human reliance behavior to selectively present calibration cues, but uses a learned user model rather than model uncertainty and does not switch explanation types. 'The Persuasion Paradox' (2604.03237) finds that uncertainty-based selective automation outperforms explanations for visual reasoning, but their own results show LLM explanations dramatically improve performance on language-based tasks (LSAT: 72.5% vs. 48.5%), supporting explanation-type switching for knowledge QA. 'Contrastive Explanations That Anticipate Misconceptions' (2410.04253, CHI 2025) generates explanations addressing the gap between AI and user reasoning (N=628, improves decision skills), but applies them uniformly without selective gating. 'Don't Just Translate, Agitate' (2504.12424) proposes LLMs as devil's advocates for XAI but is a position paper without empirical evaluation. 'Why Not Both?' (Frontiers 2025) shows explanations and uncertainty estimates serve complementary roles—uncertainty improves accuracy while explanations improve understanding—supporting the value of combining both signals. 'Unequal Uncertainty' (2508.07872) provides the first socio-technical and legal analysis of uncertainty-gated interventions, showing they can disproportionately affect underrepresented groups through differential triggering rates, creating fairness and legal risks under UK Equality Act 2010. 'Entropy Alone is Insufficient' (2603.21172) demonstrates that semantic entropy has a 'confidently wrong regime' and combining it with a Probability of Correctness probe substantially improves reliability. 'Revisiting Uncertainty Estimation' (2505.23854) shows LLMs have better calibration on reasoning tasks than knowledge-heavy ones across 80 models, and that good calibration does not guarantee effective error ranking—necessitating explicit validation for our QA domain. 'LLMs Should Express Uncertainty Explicitly' (2604.05306) proposes verbalized confidence and reasoning-time uncertainty markers, achieving improved calibration. 'Dissenting Explanations' (AAAI 2024) leverages model multiplicity for disagreeing explanations but applies them uniformly. Partial explanations (de Jong et al., PACM HCI 2025) reduce overreliance through cognitive forcing but do not modulate explanation type. 'Framework for Machine Evaluation of Reasoning Completeness' (Patil, 2510.21884) introduces the RACE framework evaluating alignment between LLM explanations and interpretable feature importance, finding a 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues—relevant context for understanding how explanation quality may covary with model correctness. Multi-AI panel work (2603.22152) finds single dissent reduces conformity while broad disagreement confuses. Uncertainty Gating for Cost-Aware XAI (2603.29915) uses epistemic uncertainty to gate explanation methods for ML classifiers, not human overreliance; notably, they use percentile-based thresholds calibrated per dataset across ν ∈ {0.1, 0.3, 0.5, 0.7, 0.9}. No existing work directly compares model uncertainty and user trust as competing gating signals for adaptive explanation presentation in LLM-assisted decision-making.

## Approach
The study proceeds in two phases. **Phase 1: Uncertainty Signal Validation.** Before any human-subjects work, we validate the gating signal on our specific task. Using Qwen3-30B-A3B—a Mixture-of-Experts model with 30.5B total parameters but only 3.3B activated per token (128 experts/layer, 8 selected per token)—we generate answers to 200 candidate general-knowledge questions and compute semantic entropy over 10 sampled completions per question. Semantic entropy operates on output-level semantics (clustering sampled completions by meaning), so it is unaffected by MoE routing variability. Following 'Entropy Alone is Insufficient' (2603.21172), we also train a lightweight Probability of Correctness (PC) probe on Qwen3-30B-A3B's hidden-state activations using a held-out set. For the PC probe specifically, we address MoE-specific considerations: we probe the shared residual stream representations (post-attention, pre-MoE routing) rather than post-expert states, avoiding the routing variability where different tokens activate different expert subsets. We validate probe stability by measuring variance across multiple forward passes on identical inputs, since MoE routing is deterministic for greedy decoding but may vary under sampling. Alternatively, we can adopt the Semantic Entropy Probes approach (Kossen et al., 2024), which approximates semantic entropy from single-generation hidden states, eliminating the need for multiple samples entirely. We combine semantic entropy and PC probe scores via logistic regression to produce a hybrid uncertainty signal. We require AUROC ≥ 0.75 for distinguishing correct from incorrect answers before proceeding; if this threshold is not met, we evaluate alternative models (Llama-4-Scout-17B, Mixtral-8x22B) or uncertainty methods (semantic energy, verbalized confidence per 2604.05306). **Threshold calibration:** The uncertainty gating threshold is set at the Youden's J optimal cutpoint (maximizing sensitivity + specificity − 1) on Phase 1 validation data, with bootstrap 95% CI for the cutpoint to quantify threshold uncertainty. Cross-validation (leave-20%-out) prevents overfitting on the 200-question set. From validated questions, we select 30 for the main study (15 where the model is correct, 15 where it is incorrect, balanced across uncertainty levels and topic domains). The increase from 20 to 30 items matches the 'Adjust for Trust' protocol (30 trials per participant) and provides sufficient levels for stable item-level random effects estimation in the GLMM analysis (Westfall, Kenny, & Judd, 2014, show that with ≤8 items, maximal attainable power is <0.5 regardless of participant N; 30 items is well above this threshold and above the ≥5-level minimum recommended by Gelman & Hill, 2006). **Phase 2: Comparative User Study.** A preregistered between-subjects study (N≈560, 140 per condition) on Prolific with four conditions: (1) **No explanation**—LLM answer only; (2) **Always-on dual explanation**—every answer includes structured pro and contra arguments (replicating the effective condition from 2605.10930); (3) **Trust-gated dual explanation**—participants report trust on an 11-point scale (0-10) after each of the 30 trials; when trust exceeds 8 (adopting the 'Adjust for Trust' threshold, which was empirically calibrated against reliance behavior), the next trial presents dual explanation, otherwise single explanation; (4) **Uncertainty-gated dual explanation**—when the hybrid uncertainty signal exceeds the Youden's J-optimal threshold from Phase 1, dual explanation is presented; otherwise single explanation. **Triggering rate calibration:** In the pilot study (N=60, 15 per condition), we compare empirical triggering rates between Conditions 3 and 4. If rates differ by >15 percentage points, we adjust the uncertainty threshold to the percentile that approximately matches the trust-gated triggering rate, reporting both Youden-optimal and rate-matched thresholds as sensitivity analyses. This ensures condition comparability while preserving transparency about any threshold adjustment. Crucially, unlike the Uncertainty Highlighting intervention in Bo et al. (2412.15584) which *displays* token-level probability information to users (and backfired by increasing algorithm aversion), our uncertainty-gated condition uses uncertainty purely as a backend signal—participants see only the selected explanation format, never the uncertainty estimate itself. This design choice is directly informed by Bo et al.'s finding that user-facing uncertainty visualization is counterproductive. All conditions receive accuracy feedback after each trial (following 'Adjust for Trust' protocol, ensuring comparability). Dual explanations are generated via Claude API with structured prompting (pro: 3-4 sentences supporting the answer; contra: 2-3 sentences presenting the strongest counter-argument and alternative answer), with human review for quality. **Measures**: Primary—overreliance rate (accepting incorrect AI answers), discrimination accuracy (AUROC of accept/reject decisions vs. correctness), appropriate reliance (composite of over- and under-reliance, following the Appropriate Reliance Ratio from Bo et al., 2412.15584). Secondary—cognitive load (NASA-TLX), task completion time, subjective satisfaction (7-point Likert), perceived AI competence. **Analysis plan**: Generalized linear mixed model (GLMM) with a logit link for trial-level accept/reject decisions, including crossed random intercepts for participants and items (questions), and random slopes for condition by item to capture differential treatment effects across questions (following Baayen, Davidson, & Bates, 2008; Westfall, Kenny, & Judd, 2014). Fixed effects: condition (4 levels), item correctness (correct/incorrect), and their interaction. Participant-level covariates: age, education, domain knowledge (pre-test). This approach accounts for item-level variance (question difficulty, topic familiarity) that would otherwise inflate Type I error if items were treated as fixed (Judd, Westfall, & Kenny, 2012). **Equivalence testing specification (H2)**: We use Two One-Sided Tests (TOST; Lakens, 2017) with a pre-registered equivalence margin of Cohen's d = 0.35, justified by cost-benefit SESOI reasoning (Lakens, Scheel, & Isager, 2018): this represents the maximum effectiveness difference at which uncertainty-gating's deployment advantages—no user surveys, no accuracy feedback dependency, first-interaction readiness—still outweigh the performance loss versus trust-gating. In raw terms, d = 0.35 corresponds to approximately 7 percentage points on overreliance rate (assuming participant-level SD ≈ 0.20), meaning we accept non-inferiority if uncertainty-gating's overreliance rate is no more than 7pp higher than trust-gating's. As sensitivity analyses, we also report equivalence tests at d = 0.25 (stricter) and d = 0.50 (more lenient) to demonstrate robustness to margin specification. **Power analysis**: For H2 (TOST non-inferiority, d = 0.35 bounds, α = 0.05): N = 140 per group provides ~80% power (computed via TOSTER::power_t_TOST; consistent with Lakens, 2017, Table 1: d = 0.30 requires N = 191/group, d = 0.40 requires N = 108/group, interpolating to ~140 for d = 0.35). For H1 and H3 (superiority tests, expected d ≈ 0.50 based on 'Adjust for Trust' effect sizes): N = 140 per group provides >95% power. Total sample: N = 560 (140 per condition). **Fairness analysis** (RQ3, addressing 'Unequal Uncertainty'): We collect demographic data (gender, race/ethnicity, education, English proficiency) and analyze whether uncertainty-gated dual explanations trigger at different rates for questions where demographic knowledge gaps exist, whether differential triggering correlates with demographics, and whether any differential triggering translates to differential overreliance reduction. **Key hypotheses**: H1—Conditions 3 and 4 both reduce overreliance compared to Condition 1; H2—Condition 4 (uncertainty-gated) achieves non-inferior overreliance reduction compared to Condition 3 (trust-gated), tested via TOST with equivalence margin d = 0.35; H3—Condition 4 produces lower cognitive load and higher satisfaction than Condition 2 (always-on dual); H4—Condition 4 incurs no measurement burden (no trust surveys), making it more practical; H5—Uncertainty-gated triggering rates do not differ significantly across demographic groups (fairness hypothesis, tested as a secondary analysis with appropriate corrections for multiple comparisons). **Ecological validity limitation**: Accuracy feedback after every trial, while necessary for the trust-gated condition (Condition 3) and provided to all conditions for comparability, is rarely available in real-world deployment. The 'Adjust for Trust' authors explicitly acknowledge this limitation. Okamura and Yamada (CHI 2024, arXiv 2111.08222) demonstrate that outcome feedback substantially improves trust calibration, while interpretability alone does not—implying that trust-gating's effectiveness degrades in feedback-free settings. Critically, uncertainty-gating is feedback-independent: the model computes uncertainty from its own outputs regardless of whether users receive outcome information. This means our study likely *underestimates* uncertainty-gating's relative advantage over trust-gating in deployment, because the experimental feedback supports trust calibration that would be absent in practice. We discuss this asymmetry as a key deployment implication: in feedback-scarce environments (the norm for most LLM-assisted decisions), uncertainty-gating may be the *only* viable adaptive strategy, as trust-gating without feedback relies on potentially miscalibrated self-reports that the 'Adjust for Trust' authors themselves note may reflect 'potentially incorrect perceptions of expertise.' A follow-up study varying feedback availability (present vs. absent) across both gating conditions would directly quantify this interaction and is identified as priority future work.

## Resource Estimate
{'manual': {'gpu_hours': '300-400 (Qwen3-30B-A3B hosting for Phase 1 validation: ~2K questions × 10 samples + PC probe training on shared residual stream representations; Phase 2: ~10K inference calls × 10 samples for pilot + main study on A100-80GB; note Qwen3-30B-A3B activates only 3.3B parameters per token, reducing per-inference cost vs. dense 30B models)', 'timeline': '5-7 months (Month 1: system build + Phase 1 uncertainty validation + threshold calibration; Month 2: IRB submission + pilot design; Month 3: IRB approval + pilot N=60 + triggering rate calibration; Month 4: pilot analysis + main study refinement; Month 5: main study N≈560; Month 6-7: analysis + writing; aggressive 4.5-month variant possible if IRB uses expedited review for minimal-risk online study)', 'estimated_gpu_cost': '$700-1000 (A100 at ~$3/hr; MoE efficiency reduces per-inference cost)'}, 'human_in_loop': {'gpu_hours': '200-300 (Claude API generates candidate explanations and counter-arguments; GPU only for Qwen3-30B-A3B uncertainty estimation and PC probe training)', 'timeline': '4.5-6 months (Claude accelerates explanation generation, stimulus quality control, statistical modeling, and fairness analysis code)', 'claude_api_cost': '$600-900 (explanation generation for 200 candidate + 30 final questions × 4 conditions × multiple pilot rounds, plus analysis assistance)', 'estimated_gpu_cost': '$500-750'}, 'auto_research': {'gpu_hours': '200-300', 'timeline': '4.5-6 months minimum', 'claude_api_cost': '$900-1400 (automated stimulus optimization, power analysis simulation, equivalence testing code, fairness analysis, draft writing)', 'estimated_gpu_cost': '$500-750', 'speed_bottleneck': 'IRB approval (4-8 weeks, expedited review possible for minimal-risk online survey) and Prolific data collection (~2-3 weeks for N=560) are non-automatable; participant compensation ~$6,200-7,000 (560 participants × ~40 min average session × $12/hr Prolific recommended minimum + 33.3% Prolific academic service fee + ~10% buffer for rejections/replacements; Condition 3 sessions may extend to ~45 min due to trust surveys after each of 30 trials); trust measurement in Condition 3 requires interactive protocol that may extend session duration'}}

## Inspired By
The 'Adjust for Trust' finding that trust-gated counter-explanations reduce overreliance by 38%—combined with their own limitation that trust cannot be reliably predicted from behavior (F1 ≤ 0.5) and their acknowledgment that accuracy feedback is unavailable in most deployment settings—directly motivates testing model uncertainty as a practical alternative gating signal. The convergence of (1) dual explanations as uniquely effective (2605.10930), (2) adaptive gating as effective but trust-measurement-limited (2502.13321), (3) adaptive explanation selection as effective but requiring learned user models (2502.11919), (4) 'Entropy Alone is Insufficient' showing hybrid uncertainty signals improve reliability (2603.21172), (5) uncertainty *display* backfiring while the underlying signal remains informative (2412.15584), and (6) 'Unequal Uncertainty' raising fairness concerns about uncertainty-gated interventions (2508.07872) creates a well-motivated research question that no single prior paper addresses.

## Target Venues
- CHI 2027 (paper deadline Sep 10, 2026 — aggressive but achievable with 4.5-month timeline if Phase 1 validates quickly and IRB uses expedited review; flagship HCI venue, strong fit for adaptive AI-assisted decision-making comparison study; revise-and-resubmit process available)
- CSCW 2027 (rolling submission from Jan 2027 — comfortable primary target if CHI 2027 timeline proves too tight; strongest fit for adaptive AI-assisted decision-making with fairness analysis; 3-4 month review cycle)
- FAccT 2027 (estimated deadline ~Jan 2027 — fairness analysis of uncertainty-gated interventions is strong fit; equity framing as secondary contribution)
- CHI 2028 (paper deadline ~Sep 2027 — safe fallback if earlier venues require major revision)

## Key References
- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (IUI 2026, arXiv 2502.13321) — *primary point of differentiation*: trust-gated adaptive counter-explanations, 38% reduction in inappropriate reliance, 30 trials/participant, trust ≥ 8 threshold; our Condition 3 replicates their mechanism
- Evaluating the False Trust engendered by LLM Explanations (arXiv 2605.10930, May 2026) — establishes dual explanations as uniquely effective; motivates explanation type selection
- From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis (Li et al., CHI 2025, arXiv 2502.11919) — dynamic programming framework with learned human behavior model for selectively presenting LLM-generated feature analyses (N=447, N=397, 15 trials/participant); improves appropriate reliance on tabular AI tasks; differs from our work in requiring prior interaction data, operating on feature-level analyses rather than dual explanations, and using predicted utility rather than model uncertainty or trust as gating signal
- To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models (Bo et al., CHI 2025, arXiv 2412.15584) — benchmarks three reliance interventions (Reliance Disclaimer, Uncertainty Highlighting, Implicit Answer) on N=400 (only 4 trials/participant); finds interventions generally fail to improve appropriate reliance; Uncertainty Highlighting specifically backfires by increasing algorithm aversion; *critical counter-evidence* that motivates our backend-gating design: we use uncertainty to select explanation type, never displaying it to users; Appropriate Reliance Ratio adopted as primary metric
- The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance (arXiv 2604.03237) — shows explanation effectiveness is task-dependent; supports explanation switching for language-based QA while selective automation is better for visual tasks
- Selectively Providing Reliance Calibration Cues With Reliance Prediction (arXiv 2302.09995) — selective intervention via predicted reliance behavior; differs in gating signal (user model vs. model uncertainty) and intervention type (calibration cues vs. explanation switching)
- Contrastive Explanations That Anticipate Human Misconceptions (CHI 2025, arXiv 2410.04253) — human-centered contrastive explanations improve decision skills (N=628); applied uniformly, not selectively gated
- Don't Just Translate, Agitate: Using LLMs as Devil's Advocates for AI Explanations (arXiv 2504.12424) — position paper proposing LLMs as constructive agitators; no empirical evaluation
- Why Not Both? Complementing Explanations with Uncertainty (Frontiers in Computer Science 2025) — shows explanations and uncertainty serve complementary roles; supports combining both signals
- Unequal Uncertainty: Rethinking Algorithmic Interventions for Mitigating Discrimination from AI (arXiv 2508.07872) — fairness risks of uncertainty-gated interventions; directly motivates our RQ3 fairness analysis
- Entropy Alone is Insufficient for Safe Selective Prediction in LLMs (arXiv 2603.21172) — demonstrates 'confidently wrong' regime of semantic entropy; motivates our hybrid SE + PC probe approach
- Revisiting Uncertainty Estimation and Calibration of Large Language Models (arXiv 2505.23854) — shows calibration varies across 80 models, worse on knowledge vs. reasoning tasks; motivates Phase 1 validation
- LLMs Should Express Uncertainty Explicitly (arXiv 2604.05306) — verbalized confidence and reasoning-time uncertainty markers improve calibration; alternative uncertainty elicitation if SE fails validation
- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance (CSCW 2021) — establishes effectiveness-usability tradeoff in CFF interventions
- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, January 2026) — Assumption CFF reduces overreliance but decreases satisfaction
- Cognitive Forcing for Better Decision-Making: Reducing Overreliance Through Partial Explanations (PACM HCI 2025) — partial explanations as cognitive forcing; no uncertainty-based modulation
- Dissenting Explanations: Leveraging Disagreement to Reduce Model Overreliance (AAAI 2024) — model multiplicity for disagreeing explanations; applied uniformly without selective gating
- More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice (arXiv 2603.22152) — single dissent reduces conformity; supports targeted rather than blanket counter-argumentation
- Uncertainty Gating for Cost-Aware Explainable AI (arXiv 2603.29915) — uses epistemic uncertainty to gate explanation methods for ML classifiers with percentile-based thresholds; analogous mechanism but entirely different application domain
- Framework for Machine Evaluation of Reasoning Completeness in Large Language Models for Classification Tasks (Patil, arXiv 2510.21884) — RACE framework evaluating explanation-feature alignment; finds 'support-contra asymmetry' where correct predictions reference more supporting lexical cues while incorrect predictions reference more contradicting cues; relevant context for understanding explanation quality covariation with model correctness
- Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs (Kossen et al., arXiv 2406.15927) — approximates semantic entropy from single-generation hidden states, reducing computational overhead to near zero; potential efficiency improvement for Phase 1 uncertainty estimation
- Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (Lakens, 2017, Social Psychological and Personality Science) — TOST procedure and power analysis tables; our equivalence margin and power calculations follow this framework
- Equivalence Testing for Psychological Research: A Tutorial (Lakens, Scheel, & Isager, 2018, AMPPS) — SESOI justification approaches including cost-benefit analysis; grounds our d = 0.35 margin choice
- Statistical Power and Optimal Design in Experiments in Which Samples of Participants Respond to Samples of Stimuli (Westfall, Kenny, & Judd, 2014, JEP:General) — power analysis for crossed random effects designs; shows ≤8 items cap maximal power at <0.5; motivates our 30-item stimulus set
- Mixed-Effects Modeling with Crossed Random Effects for Subjects and Items (Baayen, Davidson, & Bates, 2008, J Memory & Language) — methodological foundation for our GLMM analysis plan with crossed random effects for participants and items
- Adaptive Trust Calibration for Human-AI Collaboration (Okamura & Yamada, CHI 2024, arXiv 2111.08222) — directly compares feedback vs. no-feedback conditions; shows outcome feedback substantially improves trust calibration while interpretability alone does not; grounds our ecological validity discussion


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5ed16400-6c57-4e06-8617-3a11802eb67c",
  "type": "user",
  "uuid": "98e67d14-542d-4b7e-bb01-53e846b8e8ff",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:38:56.121Z_

```json
{
  "parentUuid": "98e67d14-542d-4b7e-bb01-53e846b8e8ff",
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
  "uuid": "35f5d7f8-3807-499a-a62b-64dacafd068d",
  "timestamp": "2026-05-20T03:38:56.121Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:38:56.121Z_

```json
{
  "parentUuid": "35f5d7f8-3807-499a-a62b-64dacafd068d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cad9fce5-6e11-4c1b-b970-cede781904ac",
  "timestamp": "2026-05-20T03:38:56.121Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to write a thorough evaluati…",
  "leafUuid": "cad9fce5-6e11-4c1b-b970-cede781904ac",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare model uncertainty vs user trust for adaptive LLM explanations",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:39:30.694Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

Let me first extract the key data points:

**Reviewer 1:**
- CoRL 2026: 0%-3%, median 1%
- CHI/CSCW (hypothetical): 20%-33%, median 25%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Key risks: "Why not always-on?" threat, novelty insufficient


- Venue mismatch: fatal

**Reviewer 2:**
- CoRL 2026: 0%-3%, median 1%
- CHI/CSCW (hypothetical): 20%-35%, median 27%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Key risks: venue mismatch (fatal), trivial alternative threat

**Reviewer 3:**
- CoRL 2026: 0%-2%, median 1%
- CHI/CSCW (hypothetical): 20%-32%, median 25%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Key risks: comparison study limited novelty, trivial alternative

Now I'm aggregating the reviewer assessments. For CoRL 2026, all three reviewers converge on a 1% median acceptance rate with essentially zero variance—this is a clear desk reject due to scope mismatch. But for CHI/CSCW, the medians cluster tightly around 25-27% with minimal standard deviation, showing strong consensus that the idea has moderate potential in the right venue. Across all reviewers, there's complete agreement on novelty being weak-to-moderate, significance being medium, and related work coverage being strong, with the core risks being limited novelty from the comparison study and the trivial alternative threat. Reviewer 1 also flags "Why Not Both?" from Frontiers 2025 as a minor gap, though that's an isolated concern. Now I need to synthesize the Meta Judge assessment—the venue mismatch is fatal across all reviewers, making CoRL essentially a 0% probability, but the idea itself lands around 25-27% for a more appropriate venue like CHI or CSCW where the HCI framing would be relevant. I should structure the final output to reflect CoRL's unsuitability while providing the conditional assessment for the paper's actual domain. The implementation is quite feasible—they're looking at modest compute requirements, a manageable dataset of 200 questions with around 560 participants recruited through Prolific, and straightforward human evaluation costs around $6-7K for IRB approval and compensation. The training phase is lightweight since they're just probing existing models rather than doing large-scale retraining, and they've estimated a realistic 4.5 to 7 month timeline without needing to develop new benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad9fce5-6e11-4c1b-b970-cede781904ac",
  "isSidechain": false,
  "requestId": "req_011CbD8BkjfRPUsJpqrsXLVs",
  "type": "assistant",
  "uuid": "4132bc26-cd67-4fb1-aecb-561bd4b1a823",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137VZcr5bHRwxQkeexMcoEN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22484,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22484
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

_source line 9 · 2026-05-20T03:40:29.379Z_

【阶段】: Meta Judge
【三次中位】: [1%, 1%, 1%] (CoRL 2026)　/　[25%, 27%, 25%] (CHI/CSCW 假设) std=0% (CoRL) / std≈1.15% (CHI/CSCW)
【共识维度】:
- **Venue Mismatch: 致命**（3/3）— CoRL 是机器人学习会议，本 proposal 是纯 HCI 用户研究，零交集，必然 desk reject
- **Novelty: 弱-中**（3/3）— 核心贡献是"用 model uncertainty 替代 user trust 作为 gating signal"，是已有组件的直觉化工程组合（trust-gating 已有 [2502.13321]，uncertainty gating XAI 已有 [2603.29915]，dual explanation 已验证 [2605.10930]），非 conceptual breakthrough；non-inferiority 框架进一步压低 novelty 天花板（最佳结果 = "和已有方法差不多"）
- **Significance: 中**（3/3）— 研究问题有实际部署价值（去掉 trust 问卷），但贡献是 practical/incremental 而非 scientific insight；结果预期性高（"I would have guessed this"）
- **Related Work: 强**（3/3）— 覆盖全面、引用准确、差异化清晰，所有核心文献经验证真实；方法论引用（Lakens, Westfall, Baayen）均为领域标准
- **Trivial Alternative 威胁: 严重**（3/3）— Always-on dual explanation（Condition 2）是零成本替代方案，如果 always-on 与 gated 效果相当则 gating 增量价值归零
- **Random Gating Baseline 缺失**（2/3，R1+R3）— 无法排除"任意 selective gating 已足够"的可能性
- **Non-inferiority 限制学术影响力上限**（3/3）— 最佳结论仅为"可替代、更方便"，是工程/部署论证而非科学发现
【异常维度】:
- R1 单独提到 "d=0.35 margin 可能过宽" 的审稿质疑风险 — 合理但非共识关切，降权
- R3 单独提到缺少 "Human-AI Deliberation" 等更广 adaptive AI interaction 文献覆盖 — 边缘遗漏，降权
- R1 单独提到 "Why Not Both?" (Frontiers 2025) 覆盖不足 — 微小遗漏，降权
【最终概率】: [0% - 2%] 中位 1% (CoRL 2026)　｜　[20% - 30%] 中位 25% (CHI/CSCW 假设)
【一致性】: 高（三份评审在 CoRL 判定上完全一致；在 idea 质量评估上 std≈1.15%，远低于 3% 阈值；rubric 三维度判定完全相同）
【综合理由】:

**CoRL 概率（主评估目标）：** 三位审稿人对 venue mismatch 的判定完全一致且理由充分——CoRL 的 scope 明确要求 "focus on a core robotics problem"，本 proposal 是纯 HCI 用户研究（LLM 解释呈现策略比较），无机器人、无物理控制、无 embodied learning 成分。这不是 idea 质量问题，是根本性的投稿方向错误。概率取三人共识的 1%。

**CHI/CSCW 概率（假设正确 venue）：** 三位审稿人独立得出几乎相同的 rubric 判定（Novelty 弱-中 / Significance 中 / Related Work 强）和概率区间（中位 25-27%）。高一致性下取中位附近值。

概率上限受 Novelty 硬约束：核心贡献是组件重组（现有 uncertainty method + 现有 dual explanation + 比较研究），审稿人预期反应为 "well-executed comparison, limited novelty"。Non-inferiority 框架进一步封顶——最佳结果仅证明"可替代"而非"更好"。Trivial alternative（always-on dual）威胁是审稿人最可能的致命质疑点。这些因素将 idea 天花板压在 ~30%。

概率下限由 Related Work 强度和方法论严谨性（preregistered, TOST, GLMM, fairness analysis）支撑——这些不会让论文"好"到被接收，但会防止被"碾压式"拒稿，保住 ~20% 地板。

综合判定：中位 25%，偏向三份中更严格的两份（R1 和 R3 的 25%）而非较宽松的 R2（27%）。

【建议】: **KILL**（针对 CoRL 2026）/ **边缘偏不推荐**（针对 CHI/CSCW，需重大 idea 层面强化）

具体建议：
1. **立即放弃 CoRL 2026 投稿**。这是 100% 确定的 scope mismatch。
2. **如转投 CHI/CSCW**，当前 idea 处于 borderline-reject 区间（25%），核心瓶颈是 Novelty。要提升到 competitive 区间（≥36%），需要在 idea 层面实现突破——不是"比较两个已有方法"，而是发现 uncertainty-gating 和 trust-gating 在何种条件下 diverge 的机制性洞见，或者证明 uncertainty-gating 在特定场景下 strictly superior（而非仅 non-inferior）。
3. **三位审稿人共同指出的最大威胁**——"Why not always-on dual?"——必须在 idea framing 层面得到根本性回应，否则任何实验层面的完善都无法弥补。

【实施评估】:
- **计算资源**: 200-400 GPU hours（A100-80GB），主要用于 Qwen3-30B-A3B 推理（MoE 架构，仅激活 3.3B 参数/token，单卡可推理）+ PC probe 训练；Claude API $600-1400 用于解释生成。总 GPU 成本约 $500-1000。资源门槛低。
- **数据需求**: 200 道候选通用知识问题（自建）+ Prolific 平台招募 N≈560 被试。问题集需自行构建和验证，Prolific 数据公开可获取。无需外部非公开数据集。
- **人工介入**: IRB 审批（4-8 周，最低风险在线调查可走快速通道）；被试补偿约 $6,200-7,000；生成的 dual explanation 需人工质量审核；实验设计和 pilot 分析需研究者参与。人工介入量中等。
- **训练需求**: 仅需训练轻量 PC probe（logistic regression / 小型 MLP on hidden states），无大规模模型训练。训练成本可忽略。
- **新 Benchmark**: 不需要。使用现有评测范式（overreliance rate, discrimination accuracy, ARR）和标准量表（NASA-TLX）。需自建 30 道 general-knowledge QA 题目集，但这是 stimulus set 而非 benchmark。
- **预估周期**: 4.5-7 个月（Phase 1 不确定性验证 1 个月 → IRB + pilot 2 个月 → 主实验 1 个月 → 分析写作 1.5-2 个月）。关键瓶颈是 IRB 审批和 Prolific 数据收集，不可自动化。如目标 CHI 2027（DDL 2026.09.10），时间极紧但理论可行。CSCW 2027（2027.01 rolling）更安全。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4132bc26-cd67-4fb1-aecb-561bd4b1a823",
  "isSidechain": false,
  "requestId": "req_011CbD8BkjfRPUsJpqrsXLVs",
  "type": "assistant",
  "uuid": "88401410-bef7-456b-b8e8-2ee5bc0d736d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137VZcr5bHRwxQkeexMcoEN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22484,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3538,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22484
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to write a thorough evaluati…",
  "leafUuid": "88401410-bef7-456b-b8e8-2ee5bc0d736d",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare model uncertainty vs user trust for adaptive LLM explanations",
  "sessionId": "49e3a0f1-663e-4536-9d5a-8f53396ad32b"
}
```

---
