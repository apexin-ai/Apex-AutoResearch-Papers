# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/d4e28f65-4760-47a6-b10d-e8880e3c757c.jsonl`
- **Structured JSON:** [`3c10d4170795c34c7b53.json`](../../sessions/3c/3c10d4170795c34c7b53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:47:39.694Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:47:39.694Z",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient evidence to produce my evaluation. Let me compile the analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. The Verifier Tax (arXiv 2603.19328, Mar 2026):\n   - 核心发现：即使 guardrail 能拦截高达 94% 的不安全操作，Safe Success Rate (SSR) 在大多数设置下仍低于 5%。Recovery rate 在简单 Airline 任务中为 ~21%，在复杂 Retail 任务中趋近 0%（GPT-OSS-20B, GLM-4-9B）。\n   - 与本 proposal 的关系：直接提供了核心 motivating evidence。Proposal 对其数据的引用经核实准确。但 Verifier Tax 本身的贡献是诊断问题（Safety-Capability Gap + Integrity Leaks），而非解决 recovery 问题。\n\n2. Symbolic Guardrails (arXiv 2604.15579, Apr 2026):\n   - 核心发现：对 80 个 agent safety benchmark 的系统综述；symbolic guardrails 在提供 informative error messages 时，GPT-4o pass rate 从 0.36 提升至 0.48（+33% relative），GPT-5 从 0.68 到 0.70。\n   - 与本 proposal 的关系：提供 model-dependent recovery gap 的证据。Proposal 正确指出该论文将 recovery 作为 pass rate 的副产品度量而非 first-class target。但注意：Symbolic Guardrails 的核心贡献是 symbolic guardrail 设计而非 recovery 研究，所以\"没有研究 recovery\"并非一个 gap——而是该论文本来就不做这件事。\n\n3. Fission-GRPO (arXiv 2601.15625, Jan 2026):\n   - 核心发现：通过 on-policy error augmentation + Error Simulator 反馈，Qwen3-8B 在 BFCL v4 Multi-Turn 上 error recovery rate 提升 5.7%（42.75%→46.75%）。\n   - 与本 proposal 的关系：RA-FGRPO 直接改编自 Fission-GRPO，将 operational error recovery 替换为 safety-specific post-blocking recovery。技术改造幅度有限——核心 mechanism（fission + diagnostic context + resampling）不变，只是 Error Simulator → Safety Recovery Simulator。\n\n4. BackBench (arXiv 2604.18847, Apr 2026):\n   - 核心发现：50 个 computer-use 场景的 post-harm recovery benchmark，使用 1,150 pairwise human preference judgments 训练 reward model，+120 Elo。\n   - 与本 proposal 的关系：Post-harm ≠ post-blocking，domain（GUI/OS vs tool-use API）不同。Proposal 对二者的区分是清晰且准确的。\n\n5. ToolMisuseBench (arXiv 2604.01508, Apr 2026):\n   - 核心发现：6,800 tasks，deterministic fault injection，replayable evaluation。\n   - 与本 proposal 的关系：Operational faults（schema drift, rate limits）vs safety-policy violations。Proposal 承认其 methodological adjacency 且提及 inspiration，定位合理。\n\n6. SafeAgent (arXiv 2604.17562, Apr 2026):\n   - 核心发现：Runtime protection architecture，包含 constrained replanning 机制——当 agent 动作偏离目标或风险升高时触发 replanning。\n   - 与本 proposal 的关系：SafeAgent 已经实现了 constrained replanning 作为 recovery mechanism，虽然未提供 disaggregated recovery metrics。这是 proposal 需要更严肃对待的竞争者——其 replanning 机制在精神上与本 proposal 的 agent-side replanning 目标高度一致，尽管 SafeAgent 是 runtime architecture 而非 dedicated benchmark + training。\n\n7. GTPO (arXiv 2511.14846, Nov 2025, revised Apr 2026):\n   - 核心发现：Turn-level reward assignment，+3.0% over GRPO on multi-turn tool-integrated reasoning。\n   - 与本 proposal 的关系：作为 RA-FGRPO 的 primary credit assignment 方法被直接采用。Proposal 描述准确。\n\n8. ReGuard (arXiv 2510.13727, Oct 2025):\n   - 核心发现：Control-theoretic guardrail，学习 safety value function V(z) 和 fallback policy π_safe，在 simulated driving 和 simple e-commerce 上评估。\n   - 与本 proposal 的关系：Guardrail-side correction vs agent-side replanning，定位互补。Proposal 的处理合理。\n\n- 调研总结：Post-blocking task recovery 作为一个 distinct failure mode 确实没有被现有工作作为 first-class research target isolate 出来。但这个 gap 的价值需要审慎评估：(a) Verifier Tax 和 Symbolic Guardrails 提供了清晰的 motivating evidence，(b) 现有 recovery 工作（Fission-GRPO, BackBench, ToolMisuseBench, SafeAgent）各自处理不同类型的 recovery 但均未直接 address post-blocking recovery，(c) 技术方案层面，核心训练方法（RA-FGRPO）是 Fission-GRPO 在 safety domain 的直接迁移，创新幅度有限。\n\n【Trivial Alternative 检验】:\n\n存在显著的 trivial alternative 威胁：\n\n1. **Better prompting/context baseline**: Symbolic Guardrails 已经证明，仅仅提供 informative blocking feedback（解释哪条 policy 被违反），GPT-4o pass rate 就能从 0.36 提升到 0.48（+33% relative improvement）。对于 open-source models，一个自然的 trivial baseline 是：在 blocking 时提供结构化的 diagnostic context（与 proposal 的 SRS diagnostic feedback 类似）+ few-shot recovery examples，不做 RL 训练。如果这个 prompting baseline 已经能显著提升 recovery，那 RA-FGRPO 的增量价值就很有限。\n\n2. **Supervised fine-tuning on recovery trajectories**: 相比 RA-FGRPO 的 on-policy RL + tiered credit assignment 的复杂方案，用 oracle safe trajectories（proposal 中已经需要计算）做简单的 SFT，可能是成本更低且效果接近的替代方案。Proposal 只对比了 offline DPO，未提及 SFT baseline。\n\n3. **Informative error message design**: 如果 recovery gap 的核心瓶颈是\"model 不理解 blocking feedback\"（Symbolic Guardrails 的发现暗示这一点），那么工程上优化 blocking message 格式可能比 RL 训练更 practical。\n\nProposal 的增量价值主要在于：(a) 系统化的 benchmark 和 metrics 框架，(b) 对 unrecoverable scenario recognition 的评估维度。但训练方法的增量价值存疑。\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **\"Post-blocking recovery 是一个独立的、需要专门训练的能力\"（核心假设）**: 这个假设是 proposal 的根基，但可能不成立。Recovery 本质上是 replanning——这是一个通用的 agent 能力，不一定需要 safety-specific 训练。Fission-GRPO 训练的 general error recovery 能力可能已经足以 transfer 到 post-blocking settings。如果 Fission-GRPO 本身就能提升 post-blocking recovery（因为 replanning 能力是通用的），那么 safety-specific RA-FGRPO 的价值就大打折扣。\n\n2. **\"Open-source models 的 recovery gap 主要源于缺乏 recovery-specific training\"**: Verifier Tax 的数据也可能被解释为：小模型的 recovery 差是因为它们的通用推理/规划能力本身就弱，而非缺乏 safety-specific recovery 训练。如果是前者，那么通用能力提升（scale up, better pretraining）比 specialized recovery training 更有效。\n\n3. **\"tau-bench 上的 recovery 训练能泛化到其他 tool-use domains\"**: 整个 benchmark 和训练都基于 tau-bench 的 Airline/Retail 两个 domain。这些 domain 的 policy rules 相对结构化和有限，recovery 也相应地 constrained。泛化到 policy rules 更模糊的 real-world settings（如医疗、法律）未经验证。\n\n4. **\"SRS 的 safe alternative enumeration 可以覆盖足够多的 recovery paths\"**: Proposal 声称通过 exhaustive search over constraint-satisfying action space 来 verify recoverable/unrecoverable 分类，但 tau-bench 的 action space 是否真的可以被穷举？如果 action space 很大或有 combinatorial 的 multi-step dependencies，exhaustive search 可能不 feasible，导致 recoverable/unrecoverable 标注不准确。\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   \n   **正面**: 将 post-blocking task recovery 作为一个 distinct failure mode 从 post-harm (BackBench)、post-incident (AIR)、post-error (Fission-GRPO/ToolMisuseBench)、guardrail-side correction (ReGuard/AGENT-C) 中独立出来，这个 conceptual framing 是新的，且经调研确认没有现有工作将其作为 first-class benchmark target。The dual-challenge formulation (recover when possible + recognize impossibility) 增加了评估深度。Feedback informativeness 作为 experimental condition 的系统变化直接扩展了 Symbolic Guardrails 的隐含发现。\n\n   **负面**: 技术层面的 novelty 有限。RA-FGRPO 本质上是 Fission-GRPO (arXiv 2601.15625) 的 Error Simulator → Safety Recovery Simulator 的替换 + GTPO (arXiv 2511.14846) credit assignment 的嫁接。Benchmark 设计是在 tau-bench (ICLR 2025) 上 instrument guardrail injection + 定义 5 个新 metrics。这些是 well-motivated 的 engineering 组合，但剥去 surface differences 后，核心技术 contribution 是\"把已有方法适配到一个新 setting\"。SafeAgent (arXiv 2604.17562) 已经实现了 constrained replanning（虽然缺 disaggregated metrics），进一步压缩了 novelty space。\n\n2. Significance: 【中】\n\n   **正面**: 问题本身具有实际重要性——Verifier Tax 和 Symbolic Guardrails 提供了具体量化证据表明 blocking ≠ task completion。随着 agent 在生产环境中的部署增加，safety-capability gap 是一个需要被解决的 real problem。Dual-challenge formulation 对推动该领域的评估标准有建设性作用。\n\n   **负面**: 实际影响力受限于 (a) 仅基于 tau-bench 两个 domain（Airline + Retail），场景覆盖窄，(b) 目标模型是 3B-35B MoE open-source models，虽然有实际意义但 scope 有限，(c) 如果核心发现是 \"RL training improves recovery for small models\"，这是一个 \"I would have guessed this\" 级别的发现——方向是可预测的，问题在于幅度和 transfer。审稿人不太可能写 \"surprising\"。更具意义的 surprising findings 需要来自负面或反直觉方向（如\"recovery training 在复杂 Retail 场景反而降低 recovery\"），但 proposal 未能将 surprising insights 作为核心贡献来设计。\n\n3. Related Work: 【强】\n\n   经调研验证，proposal 的 related work 覆盖异常全面且准确：\n   - 五类 recovery paradigm 的 taxonomy（post-blocking / post-harm / post-incident / post-error / guardrail-side correction）清晰且有证据支撑\n   - 与每个最直接竞争者（BackBench, AIR, Fission-GRPO, ToolMisuseBench, ReGuard, AGENT-C, SafeAgent）的差异化定位均有具体、准确的 dimension 区分\n   - 所有关键引用论文均经 WebSearch 验证存在且描述准确\n   - 覆盖了非常新的工作（GAGPO May 2026, SafeAgent Apr 2026, TraceSafe Apr 2026）\n   - 唯一可改善之处：SafeAgent 的 constrained replanning 机制可以被更深入地讨论作为最接近的 agent-side recovery 工作\n\n【概率估计】: [22% - 32%] 中位 27%\n\n【估计理由】:\n- Related Work 维度（强）为 proposal 提供了扎实的定位基础，但这是\"最低限度\"而非\"加分项\"——好的 related work 覆盖是必要条件而非充分条件。\n- Significance（中）支撑了问题的合理性但未到 compelling 级别。问题真实存在、有数据支撑，但 scope 较窄（两个 tau-bench domain）且预期发现方向可预测。\n- Novelty（中）是限制上界的关键因素。Conceptual framing 是新的（五类 taxonomy + dual-challenge），但技术 contribution 是现有方法的 domain adaptation（Fission-GRPO → RA-FGRPO），审稿人可能认为\"applying existing RL methods to a new setting\"不足以支撑 top-venue 录用。\n- Trivial alternative 威胁（better prompting + informative feedback，如 Symbolic Guardrails 已证明有效的方向）可能被审稿人直接提出，如果 prompting baseline 已经能获得 substantial recovery improvement，训练方法的增量价值会被质疑。\n- 概率下界 22% 反映了\"framing novelty 有价值 + benchmark 设计 reasonable + 问题有实际意义\"的基本面；上界 32% 反映了\"如果实验结果中出现 surprising insights（如 feedback informativeness 的 interaction effects、unrecoverable recognition 的 novel failure patterns），可能 push 过线\"的可能性。但基于 idea 本身的质量评估，中位 27% 是合理的。\n\n【主要风险】:\n1. **Novelty 被判 insufficient**: 审稿人可能认为核心技术贡献（RA-FGRPO = Fission-GRPO 在 safety setting 的直接迁移；RecoverBench = tau-bench + guardrail injection + 新 metrics）是 \"straightforward application/adaptation\"，不够支撑 top-venue 级别的 novelty 要求。\n2. **Trivial baseline 威胁**: 审稿人可能要求证明 RA-FGRPO 相比 \"informative blocking feedback + few-shot recovery prompting\"（不做 RL 训练）有显著增量。如果 prompting baseline 已经能关闭大部分 recovery gap，整个 training 方法的 motivation 就被削弱。\n```\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct the evaluation. Let me synthesize my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [The Verifier Tax] (arXiv 2603.19328, Mar 2026): 直接动机来源。在 tau-bench 上用 GPT-OSS-20B 和 GLM-4-9B 测量，guardrail 可拦截高达 94% 不安全动作，但 SSR 在大多数设置下低于 5%，recovery rate 从简单 Airline 任务的 21% 到复杂 Retail 场景的近 0%。论文确实存在，描述准确。\n- [Symbolic Guardrails] (arXiv 2604.15579, Apr 2026): 直接动机来源。在 tau²-bench 上测试 symbolic guardrails 对 pass rate 的影响。GPT-4o 从 0.36→0.48（+33% relative），GPT-5 从 0.68→0.70。论文确实存在，但 proposal 对其\"recovery\"的描述有微妙的外推——原文核心贡献是 symbolic guardrail 设计，recovery 只是 pass rate 副产品，proposal 对此有正确承认。\n- [Fission-GRPO] (arXiv 2601.15625, Jan 2026): 训练方法的直接基础。在 BFCL v4 Multi-Turn 上，Qwen3-8B recovery rate 提升 5.7%，overall accuracy +4%。论文确实存在，描述准确。核心区别：Fission-GRPO 处理的是一般工具执行错误，而非 safety policy violation。\n- [ToolMisuseBench] (arXiv 2604.01508, Apr 2026): 最接近的 benchmark 竞争者。6800 tasks，deterministic fault injection，测量 recovery quality 和 budgeted efficiency。论文确实存在。关键区别：ToolMisuseBench 的 faults 是 operational（schema drift, rate limits），不是 safety policy violations。\n- [BackBench] (arXiv 2604.18847, Apr 2026): Post-harm recovery benchmark。50 tasks in OSWorld，reward model trained on 1,150 pairwise judgments。确实存在，描述准确。关键区别：BackBench 假设 harm 已发生需补救，本 proposal 假设 harm 被阻止需替代路径。\n- [GTPO] (arXiv 2511.14846, Nov 2025): Turn-level reward assignment，+3.0% over GRPO。论文确实存在，描述准确。\n- [AGENT-C] (arXiv 2512.23738, Dec 2025): Constrained decoding for temporal safety，100% safety conformance，utility 提升。论文确实存在。这是最强的\"guardrail-side correction\"竞争者。\n- [Canonical Path Deviation] (arXiv 2602.19008, Feb 2026): Off-canonical actions compound subsequent deviation by 22.7 pp。论文确实存在，描述准确。\n- 调研总结: Agent safety 领域在 2025-2026 年经历了快速成熟期，guardrail blocking 能力已基本解决（blocking rate 高达 94-100%），但 blocking 之后的 agent 行为（recovery/replanning）是一个确实存在的 gap。现有 benchmark 分别覆盖了 post-harm (BackBench)、post-error (ToolMisuseBench/Fission-GRPO)、post-incident (AIR)、guardrail-side correction (AGENT-C/ReGuard)，但确实没有专门的 post-blocking recovery benchmark。Proposal 准确定位了这个空白，但空白的\"宽度\"需要审视——post-blocking recovery 与 post-error recovery 的技术距离可能比 proposal 声称的要近。\n\n【Trivial Alternative 检验】:\n存在两个显著的 trivial alternative 威胁：\n\n(1) **Informative feedback + in-context prompting**: Symbolic Guardrails 已经表明，仅仅给 agent 提供信息量更大的 blocking feedback（解释哪条 policy 被违反、为什么），GPT-4o pass rate 就能从 0.36 提升到 0.48（+33%）。一个自然的 trivial baseline 是：给 open-source 模型同样的 informative feedback + few-shot recovery examples。Proposal 没有直接回答\"为什么这不够\"——The Verifier Tax 的实验并未使用 informative feedback，所以我们实际上不知道 informative feedback 对小模型的效果如何。这是增量价值最需要论证的地方。\n\n(2) **直接用 AGENT-C/ReGuard 的 guardrail-side correction**: AGENT-C 已经实现 100% safety conformance 且提升了 utility。如果 guardrail 端可以直接生成合规替代动作，为什么还需要训练 agent-side replanning？Proposal 声称二者互补，但没有论证在哪些场景下 AGENT-C 不足以解决问题。\n\n**增量价值判断**: Proposal 的真实增量价值取决于两个实证问题的答案：(a) informative feedback 对小模型的效果是否显著低于对 frontier 模型的效果？(b) 是否存在 guardrail-side correction 无法覆盖的复杂多步 recovery 场景？如果两个答案都是\"是\"，增量价值成立。但目前这两个问题都是 assumption，不是 evidence。\n\n【前提假设检验】:\n核心逻辑链有三个关键的未验证假设：\n\n(1) **\"Post-blocking recovery 与 post-error recovery 有本质区别\"**: 这是整个 taxonomy 和 benchmark 存在理由的基石。Proposal 的论证是：safety constraint 消除了整类解决方案，而 operational error 只是暂时性失败。但从 agent 的决策角度看，两者都是\"当前路径不通，需要找替代路径\"。reviewer 可以合理质疑：为什么不能在 ToolMisuseBench 上加一个 safety-fault 类别，而非需要一个全新 benchmark？\n\n(2) **\"Open-source 模型的 recovery 差距可以通过 RL 训练来弥合\"**: The Verifier Tax 显示小模型 recovery 近乎为零，但这可能是小模型整体 capability 不足的表现，而非缺乏专门 recovery 训练的结果。如果模型的基础推理能力不够，专门的 recovery 训练可能只会在 distribution 内有效（tau-bench 的 2 个 domain），而无法泛化。\n\n(3) **\"Correctly Unrecoverable 识别是一个独特的 challenge\"**: 这是 benchmark 的 dual-challenge 设计核心，但目前没有任何实证表明现有模型在这方面存在系统性问题。可能当前模型已经能较好地识别不可恢复场景（通过 common sense），而这个维度不增加多少评估价值。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   Proposal 准确识别了一个确实没有被现有工作专门覆盖的 gap：post-blocking recovery 作为 first-class benchmark target。五类 recovery 的 taxonomy（post-blocking / post-harm / post-incident / post-error / guardrail-side correction）是清晰且有贡献的概念框架。Dual-challenge 设计（recover when possible, recognize impossibility when not）是一个有价值的设计元素。\n   \n   然而，novelty 存在\"距离问题\"：与 ToolMisuseBench（post-error recovery, Apr 2026）和 Fission-GRPO（error recovery training, Jan 2026）的技术距离较近。核心差异是\"error type\"（safety violation vs. operational error），而非\"recovery mechanism\"——agent 仍然在做同一件事：replanning。这使得 novelty 更像是\"已有 paradigm 的 domain specialization\"而非\"fundamentally new problem\"。RA-FGRPO 本身是 Fission-GRPO + SRS + GTPO 的组合，每个组件都来自已有工作，组合层面的创新是增量的。\n   \n   与最相关的 5-10 篇工作相比，剔除 surface differences 后，剩余的核心 novelty delta 是：(a) safety-specific recovery 的 benchmark 设计（含 CU 类别和 FRR 指标），(b) feedback informativeness 作为系统化实验变量。这是 solid 但非 breakthrough 级别的贡献。\n\n2. **Significance: 中** — \n   问题本身确实重要且有实际影响力。The Verifier Tax 量化的 safety-capability gap（SSR < 5%）是 striking 的数字，说明 guardrail blocking ≠ safe task completion 是一个真实且 under-addressed 的问题。如果解决了，对 open-source model 的安全部署有直接价值。\n   \n   但 significance 存在上界限制：(a) benchmark 仅构建在 tau-bench 2 个 domain 上（Airline, Retail），generalizability 受限；(b) 如果核心发现是 \"dedicated recovery training improves recovery rates for small models\"，审稿人的反应更可能是 \"makes sense, I would have guessed this\" 而非 \"surprising\"；(c) 与 AGENT-C（100% safety, utility 提升）相比，agent-side recovery training 的实际部署 value proposition 不明确——如果 guardrail-side correction 已经够用，agent-side training 的 marginal value 就比较有限。\n\n3. **Related Work: 强** — \n   Related work 的覆盖极为全面和准确。五类 recovery 的 taxonomy 差异化定位清晰。所有主要引用的论文（The Verifier Tax, Symbolic Guardrails, Fission-GRPO, ToolMisuseBench, BackBench, AGENT-C, ReGuard, GTPO, Canonical Path Deviation）均经验证存在且描述基本准确。对 AGENT-C 和 ReGuard 作为 guardrail-side correction 的定位和互补性论述到位。对 SafeAgent 的 \"constrained replanning\" 的引用也准确——SafeAgent 确实提到 replanning 但未提供 disaggregated metrics。对于一个 proposal 阶段的文档，这一水准的 related work 分析是优秀的。\n   \n   唯一的小瑕疵：部分论文非常新（GAGPO, May 2026），其方法尚未被独立验证，proposal 对此有正确声明。\n\n【概率估计】: [22% - 33%] 中位 27%\n\n【估计理由】: \n三个维度综合来看——Related Work 是强项（覆盖面和差异化定位优秀），但这主要决定下限而非上限。Novelty 是中等水平：gap 确实存在但较窄，核心技术贡献（RA-FGRPO）是增量式组合创新。Significance 同样中等：问题重要但预期发现的\"surprise factor\"偏低——如果 positive result 是 \"recovery training helps small models recover better\"，这更接近 confirmatory 而非 surprising。\n\n**限制上界的关键因素**是 Novelty 和 Significance 的交叉：\n- Novelty 维度：与 ToolMisuseBench 和 Fission-GRPO 的技术距离过近，核心差异（safety-specific vs. operational error）可能被审稿人视为 domain adaptation 而非 fundamental contribution\n- Significance 维度：核心发现的预期\"surprise\"偏低，且 AGENT-C 的存在削弱了 agent-side recovery training 的 value proposition\n- 两个 trivial alternative（informative feedback + ICL；AGENT-C guardrail-side correction）都需要在 paper 中被有力地 empirically refuted，否则会严重威胁 acceptance\n\n概率未低于 22% 的原因：问题定位准确、gap 确实存在、benchmark 设计（dual-challenge + feedback informativeness + FRR）有真实贡献、related work 质量高。\n\n【主要风险】:\n1. **Novelty 距离风险**: Reviewer 可能判定 post-blocking recovery 只是 ToolMisuseBench/Fission-GRPO 在 safety domain 的简单特化（\"Why not just add safety-fault injection to ToolMisuseBench?\"），从而将整个 benchmark 的 novelty 判为 incremental。这是最可能的 rejection 理由。\n2. **Trivial alternative 风险**: 如果 informative blocking feedback + few-shot prompting 就能让小模型达到接近 RA-FGRPO 训练后的 recovery 效果，整个训练方法的 contribution 就被 undermine。Symbolic Guardrails 已经证明 informative feedback 对 frontier 模型非常有效（+33%），但对小模型的效果是 unknown——如果实验发现 informative feedback 本身就足够，paper 的训练贡献就变成了 null result。\n```\n\nSources:\n- [The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents](https://arxiv.org/abs/2603.19328)\n- [Symbolic Guardrails for Domain-Specific Agents](https://arxiv.org/abs/2604.15579)\n- [Fission-GRPO: Learning to Recover from Execution Errors](https://arxiv.org/abs/2601.15625)\n- [ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery](https://arxiv.org/pdf/2604.01508)\n- [BackBench: Human-Guided Harm Recovery for Computer Use Agents](https://arxiv.org/html/2604.18847v1)\n- [GTPO: Group Turn Policy Optimization](https://arxiv.org/abs/2511.14846)\n- [AGENT-C: Enforcing Temporal Constraints for LLM Agents](https://arxiv.org/abs/2512.23738)\n- [Canonical Path Deviation as a Causal Mechanism of Agent Failure](https://arxiv.org/abs/2602.19008)\n- [SafeAgent: A Runtime Protection Architecture for Agentic Systems](https://arxiv.org/abs/2604.17562)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [The Verifier Tax] (arXiv 2603.19328, Mar 2026): 直接动机论文。在 tau-bench 上用 GPT-OSS-20B 和 GLM-4-9B 测试，发现安全中介可拦截高达 94% 不合规动作，但 SSR 在大多数设置下低于 5%，recovery rate 从 Airline 的 21% 到 Retail 的近 0%。Proposal 对该论文的引用和数据描述准确。\n- [Symbolic Guardrails for Domain-Specific Agents] (arXiv 2604.15579, Apr 2026): 在 τ²-Bench/CAR-bench/MedAgentBench 上评估 symbolic guardrails 对安全性和 agent 成功率的影响。Proposal 引用其 GPT-4o pass rate 从 0.36→0.48 的改善。该论文确实存在且关注 guardrail 如何影响 agent 表现，但其核心贡献是 guardrail 设计而非 recovery 评估——proposal 准确地指出 recovery 在该论文中只是\"side effect\"而非一等公民。\n- [Fission-GRPO] (arXiv 2601.15625, Jan 2026): 在 BFCL v4 Multi-Turn 上通过 on-policy error augmentation 提升 Qwen3-8B 的 error recovery rate +5.7%。解决的是**操作性错误**（tool-calling errors），不是 safety policy violations。Proposal 的 RA-FGRPO 直接建立在此方法之上。\n- [BackBench] (arXiv 2604.18847, Apr 2026): 50 个 OSWorld 场景，测试 computer-use agent 的 post-harm recovery，用 1,150 个 human preference judgments 训练 reward model。与 proposal 的区分清晰：BackBench 假设 harm 已发生需修复，proposal 假设 harm 被阻止后需恢复任务。\n- [ToolMisuseBench] (arXiv 2604.01508, Apr 2026): 6,800 个任务，覆盖 CRUD/retrieval/file/scheduling 环境，有确定性 fault injection。解决的是操作性错误（schema drift, rate limits, authorization failures），不是 safety policy violations。与 proposal 的区分点明确。\n- [GTPO] (arXiv 2511.14846, Nov 2025, revised Apr 2026): Turn-level reward assignment，在 math reasoning 上比 GRPO +3.0%。Proposal 选其作为主要 credit assignment 方法，理由合理（最成熟、overhead 小）。\n- [ReGuard] (arXiv 2510.13727, Oct 2025): Control-theoretic guardrail-side correction，guardrail 自身注入修正动作而非 agent 重新规划。在 simulated driving 和简单 e-commerce 上评估。Proposal 正确区分这是 guardrail-side vs agent-side 的差异。\n- [AGENT-C] (arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop): Constrained decoding 方法，通过 SMT solving 检测非合规 tool calls 并在 token 生成层面纠正。同样是 guardrail-side correction。\n- [SafeAgent] (arXiv 2604.17562, Apr 2026): 运行时保护架构，提到 constrained replanning 作为 recovery 机制，但没有对 replanning 成功率的独立评估。Proposal 正确指出其缺乏 disaggregated metrics。\n- [CostBench] (arXiv 2511.02734): 引入动态 blocking events 要求 agent 重新规划，但关注 cost-optimality 而非 safety recovery。方法论上有一定相关性。\n\n- 调研总结: Agent safety 领域在 2025-2026 年出现了大量 benchmark 和方法（guardrail 设计、安全评估、错误恢复），但**post-blocking task recovery**（guardrail 正确阻止不安全动作后，agent 如何恢复完成任务）确实是一个已被记录（Verifier Tax, Symbolic Guardrails）但未被专门 benchmark 化和训练的 gap。最接近的工作是 Fission-GRPO（操作性错误恢复）和 ToolMisuseBench（操作性错误 benchmark），但两者都不涉及 safety policy violations 后的恢复。这个 gap 是真实的。\n\n【Trivial Alternative 检验】:\n存在两个潜在的 trivial alternatives:\n\n1. **\"更好的 error message + 更大的模型\"作为 baseline**: Symbolic Guardrails 已经显示，仅通过提供 informative blocking feedback，GPT-4o 就能获得 33% 的相对改善（0.36→0.48）。一个 trivial baseline 是：对任何开源模型，简单地在 guardrail blocking 时提供更丰富的错误信息（policy citation + available actions），不做任何专门训练，看 recovery 能改善多少。Proposal 的 feedback informativeness 实验确实设计了这个对照（minimal vs policy-cited vs diagnostic），但关键问题是：**如果 diagnostic feedback 本身就能大幅提升 recovery，RA-FGRPO 的增量价值有多大？** 这是一个需要实验回答的问题，但也是 idea 层面的潜在 trivial alternative 威胁。\n\n2. **\"直接用 Fission-GRPO + safety-specific 数据\"**: RA-FGRPO 的核心相对于 Fission-GRPO 的差异在于：(a) Safety Recovery Simulator 提供 diagnostic context 而非 Error Simulator 的一般错误反馈，(b) 安全相关的 constraint compliance verification。但这是否足以构成一个独立的方法贡献？还是仅仅是 Fission-GRPO 在新 domain 上的 straightforward application？\n\n增量价值主要在于：(1) benchmark 本身（gap 真实存在）；(2) dual-challenge formulation（recoverable + unrecoverable 的区分）；(3) False Recovery Rate 指标（检测 agent 是否通过另一条不安全路径绕过限制）。这些是 benchmark 设计层面的 genuine contributions，但训练方法的增量价值较弱。\n\n【前提假设检验】:\n核心 claim 的逻辑链条中，以下环节是未经验证的假设：\n\n1. **\"Post-blocking recovery 是一个可独立训练的能力\"**: Proposal 假设 recovery 可以通过专门训练来改善（特别是对小模型），但有一种可能性是：recovery 能力本质上是通用推理能力的体现，不可能通过 narrow task-specific training 来有效提升（尤其是在 tau-bench 之外的场景中的 generalization）。这个假设的验证依赖于实验结果。\n\n2. **\"Safety-specific error augmentation 比 general error augmentation 效果更好\"**: RA-FGRPO 与 Fission-GRPO 的关键区别在于 safety-specific context。但如果 recovery 本质上是一个通用的 replanning 问题（无论错误原因是 safety violation 还是 rate limit），那么 safety-specific 训练可能不会比 general error recovery 训练有显著优势。\n\n3. **\"Oracle exhaustive search 可以可靠地验证 recoverable/unrecoverable 分类\"**: Proposal 依赖 oracle exhaustive search 来确认哪些场景 genuinely unrecoverable。在 tau-bench 的 API action space 上这可能可行，但这个假设的成立范围有限——如果 action space 更复杂，exhaustive search 可能不可行。\n\n4. **\"Canonical Path Deviation 解释了 recovery 难度\"**: Proposal 引用 CPD 论文（off-canonical actions compound deviation by 22.7 pp），但这个发现是否适用于 guardrail-blocked 场景（而非 agent 自发偏离）是一个未验证的类比推理。\n\n【3 维度打分】:\n  1. Novelty: 中 — \n     **Benchmark 贡献有真实 novelty**: 调研确认目前没有专门 benchmark 测量 post-blocking task recovery。Verifier Tax 和 Symbolic Guardrails 记录了这个问题但没有提出 benchmark。ToolMisuseBench 覆盖操作性错误而非 safety violations。BackBench 覆盖 post-harm 而非 post-blocking。这个 gap 是真实的，RecoverBench 填补了它。\n     **Dual-challenge formulation 有一定 novelty**: 同时要求 agent recover when possible + recognize impossibility when not，这在 safety recovery 领域未被专门提出（SafeAgentBench 的 5-10% rejection rates 暗示这是一个真实挑战）。\n     **False Recovery Rate 指标有 novelty**: 检测 agent 是否通过替代不安全路径绕过 guardrail，这是一个审稿人可能会认为 insightful 的指标设计。\n     **但训练方法 novelty 有限**: RA-FGRPO 本质上是 Fission-GRPO + GTPO credit assignment，应用于 safety recovery 场景。Safety Recovery Simulator 相对于 Fission-GRPO 的 Error Simulator 的区别主要在于 domain-specific context formatting，不是方法论创新。三种 credit assignment 的\"tiered\"策略看起来更像 hedging 而非贡献。\n     **总体**: 核心 novelty 在 benchmark 设计和 problem formulation，而非方法论。这是可以的（benchmark paper + method），但审稿人可能会觉得 method 部分是\"applying existing RL methods to new domain\"。\n\n  2. Significance: 中 — \n     **问题的实际重要性**：随着 guardrail 在生产环境中的广泛部署，\"block but fail to complete task\"确实是一个日益重要的实际问题。Verifier Tax 的数据让这个问题变得具体可度量。\n     **对 NLP/CL 领域的影响**：这个贡献主要服务于 agent safety 这一子领域。Benchmark 和 training method 的范围限于 tau-bench（Airline + Retail），generalizability 到其他 domains 不确定。\n     **核心发现的\"surprise factor\"偏低**：如果实验 positive（RA-FGRPO 提升了小模型的 recovery），审稿人更可能说\"I would have guessed that dedicated training helps\"而不是\"surprising\"。如果 negative，则变成一个 benchmark-only paper，意义进一步降低。\n     **但 dual-challenge 维度提升了 significance**：如果实验发现 agent 在 unrecoverable scenario recognition 上表现极差（类似 SafeAgentBench 的 5-10%），这本身就是一个有价值的 finding。\n\n  3. Related Work: 强 — \n     **覆盖极为充分**：Proposal 展示了对领域的深入理解，引用了所有主要的近期工作（Verifier Tax, Symbolic Guardrails, Fission-GRPO, BackBench, ToolMisuseBench, GTPO, AT²PO, ReGuard, AGENT-C, SafeAgent, AgentSpec 等），且引用描述基本准确（经调研验证）。\n     **五种 recovery paradigm 的 taxonomy 是真正的贡献**: post-blocking vs post-harm vs post-incident vs post-error vs guardrail-side correction 的分类清晰、有意义，每个类别都有具体论文支撑。这种 taxonomy 本身就能帮助领域组织思路。\n     **差异化定位清晰**：与每个最相关工作的区别都有明确阐述（BackBench: post-harm vs post-blocking; ToolMisuseBench: operational vs safety; ReGuard: guardrail-side vs agent-side; Fission-GRPO: general errors vs safety blocks）。\n     **唯一小瑕疵**：Symbolic Guardrails 的具体数据（GPT-4o: 0.36→0.48）我未能在搜索中直接验证到 exact numbers，但论文确实存在且主题一致。\n\n【概率估计】: [25% - 35%] 中位 28%\n\n【估计理由】: \nNovelty 中等（benchmark 填补真实 gap，但 training method 是已有方法的 domain adaptation），Significance 中等（问题真实重要但范围窄、核心发现 surprise factor 低），Related Work 强（taxonomy 和覆盖都是一流水平）。\n\n概率上界被两个因素限制：\n(1) **Training method novelty 不足**——RA-FGRPO 相对于 Fission-GRPO 的增量 delta 主要是 domain adaptation 而非方法论创新，三种 credit assignment 的 tiered 设计看起来像 hedging 而非贡献，审稿人可能会认为 \"applying Fission-GRPO to safety recovery\" 不构成独立方法贡献。\n(2) **核心发现的可预测性**——\"专门训练可以改善小模型的 post-blocking recovery\" 是一个审稿人会说 \"I would have guessed this\" 的结论。如果这篇论文的 main finding 是 \"we trained and it worked\"，novelty 评价会偏低。\n\n概率下界由问题的真实性和 benchmark 设计的严谨性支撑：这个 gap 确实存在、确实没人做过、benchmark 设计有 thoughtful 的维度（dual-challenge, FRR 指标, feedback informativeness variation），即使 training method 部分被认为 incremental，benchmark 贡献本身也有价值。\n\n【主要风险】: \n1. **Method vs Benchmark 张力**：Proposal 同时想做 benchmark paper 和 training method paper，但 training method 的 novelty 不足以支撑方法贡献，可能导致审稿人觉得\"benchmark 有价值但 method 部分 incremental\"——这是 EMNLP 常见的被 Borderline 的模式。\n2. **Trivial alternative 威胁**：如果 diagnostic feedback 本身（不做训练）就能大幅改善 recovery，RA-FGRPO 的增量价值会被大幅削弱。Symbolic Guardrails 已经展示了 informative feedback 的效果，如果 RecoverBench 的实验发现 feedback level 是主要 driver 而非 training method，核心 story 会 collapse。\n```\n\nSources:\n- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)\n- [Symbolic Guardrails for Domain-Specific Agents (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)\n- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)\n- [BackBench: Human-Guided Harm Recovery (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)\n- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/abs/2604.01508)\n- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)\n- [ReGuard (arXiv 2510.13727)](https://arxiv.org/abs/2510.13727)\n- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)\n- [SafeAgent (arXiv 2604.17562)](https://arxiv.org/abs/2604.17562)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Beyond Blocking: Benchmarking and Training Agent Task Recovery After Guardrail Interventions in Multi-Step Tool Use\n\n## Description\nCurrent agent safety guardrails achieve high blocking rates (up to 94%) for unsafe actions, yet post-blocking recovery is inconsistent and model-dependent: open-source models (GPT-OSS-20B, GLM-4-9B) achieve safe success rates below 5% with recovery rates from 21% to near 0% (The Verifier Tax, 2026), while frontier models with informative blocking feedback show partial recovery (GPT-4o: 0.36→0.48 pass rate per Symbolic Guardrails, 2026) but still fail 52% of tasks. We identify post-blocking task recovery as a distinct failure mode — categorically different from post-harm recovery (BackBench), post-incident response (AIR), post-error recovery (RAC/Fission-GRPO/ToolMisuseBench), and guardrail-side correction (ReGuard, AGENT-C). We propose RecoverBench, a benchmark measuring agent task recovery after guardrail interventions in multi-step tool-use settings, featuring a dual challenge: agents must recover when safe alternatives exist AND recognize when recovery is impossible. Built atop tau-bench (Airline/Retail), RecoverBench injects guardrail blocks at critical trajectory points with systematically varied feedback informativeness (minimal, policy-cited, diagnostic) and introduces three task categories (recoverable, correctly unrecoverable, partially recoverable) evaluated by five metrics: Safe Recovery Rate, False Recovery Rate (detecting constraint gaming via alternative unsafe pathways), Unrecoverable Recognition Rate, Recovery Latency, and Alternative Path Quality. We detail a three-module Safety Recovery Simulator (constraint extraction, safe alternative enumeration via API specification parsing, diagnostic context formatting) that generates training signal without revealing oracle solutions. For training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO) with a tiered credit assignment strategy: GTPO-based turn-level rewards as primary (most established, +3.0% over GRPO), AT²PO-based tree credit as validated fallback, and GAGPO-style grouped credit as future extension pending independent validation. RA-FGRPO adapts Fission-GRPO's on-policy error augmentation for safety-specific recovery, generating G'=4 parallel recovery attempts per blocked trajectory. We evaluate on Qwen3.6-35B-A3B and Qwen3-4B across complexity bins, targeting the model-dependent recovery gap: approaching frontier-model recovery levels for open-source models. Ablations compare against vanilla GRPO, offline DPO, ToolSafe pre-execution feedback, ReGuard-style guardrail-side correction, and frontier model baselines with informative blocking.\n\n## Core Problem\nCurrent guardrails achieve high unsafe-action blocking rates (up to 94%), but post-blocking task recovery is inconsistent, model-dependent, and unmeasured as a first-class capability. For smaller open-source models (GPT-OSS-20B, GLM-4-9B), recovery rates range from 21% on simpler procedural tasks to near 0% on complex Retail scenarios, with safe success rates below 5% in most settings (The Verifier Tax, 2026). Frontier models with informative blocking feedback fare substantially better — Symbolic Guardrails (2026) shows GPT-4o pass rates improving from 0.36 to 0.48 on tau²-bench when guardrails provide policy-violation explanations, and GPT-5 from 0.68 to 0.70 — but even GPT-4o still fails 52% of tasks after blocking. Critically, no existing work isolates post-blocking recovery as a dedicated benchmark target: Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation, not recovery quality, and provides no recoverable/unrecoverable task classification, no false recovery rate measurement, and no recovery-specific training method. This represents a distinct and underexplored failure mode: post-blocking task recovery. Unlike post-harm recovery (BackBench) where harm has occurred and must be remediated, post-incident response (AIR) where the system detects and contains safety breaches, post-error recovery (RAC/Fission-GRPO) where operational errors must be corrected, or guardrail-side correction (ReGuard, AGENT-C) where the guardrail itself generates corrective actions, post-blocking recovery requires the AGENT to find an alternative safe path to complete the user's legitimate task after being correctly prevented from taking an unsafe action. Critically, some blocked scenarios may genuinely have no safe alternative path — the agent must also learn to recognize when recovery is impossible and gracefully inform the user. No existing benchmark isolates this specific failure mode with its dual challenge (recover when possible, recognize impossibility when not), and no training method specifically targets the agent's adaptive replanning ability after correct guardrail intervention.\n\n## Opportunity\nThe Verifier Tax (Mar 2026) quantifies a devastating Safety-Capability Gap for open-source models: with GPT-OSS-20B and GLM-4-9B on tau-bench, even with 94% unsafe action blocking, safe success rates remain below 5% in most settings, and recovery rates following blocked actions range from 21% in simpler procedural Airline tasks to near 0% in complex Retail scenarios. Symbolic Guardrails (Apr 2026) reveals the model-dependency dimension: when guardrails provide informative blocking feedback (explaining which policy was violated and why), GPT-4o achieves a 33% relative improvement in pass rate (0.36→0.48) on tau²-bench Airline, and GPT-5 a modest 3% improvement (0.68→0.70) — demonstrating that (a) recovery IS possible when the agent receives informative feedback, (b) even frontier models still fail 52% of tasks (GPT-4o) despite recovery attempts, and (c) recovery quality is never measured as a first-class metric. This model-dependent recovery gap creates a clear motivation: if frontier models can partially recover with informative feedback but smaller models cannot, then dedicated recovery training can close this gap for open-source models. The gap is distinct from what AIR (>90% remediation success in post-incident response), BackBench (50 post-harm recovery scenarios in OSWorld), and ReGuard (control-theoretic guardrail correction in driving/e-commerce) address. In post-blocking recovery, the guardrail works as intended — harm is prevented — but the agent fails at adaptive replanning. Canonical Path Deviation (Feb 2026) explains the structural difficulty: off-canonical actions compound subsequent deviation by 22.7 percentage points, meaning that once an agent is pushed off its solution path by a blocked action, the probability of finding an alternative path drops sharply. Meanwhile, ToolSafe (Jan 2026) shows that safety-feedback-driven reasoning can improve benign task completion by ~10% and reduce harmful tool invocations by 65%, but this represents pre-execution guidance, not post-blocking recovery training. TraceSafe (Apr 2026) demonstrates that guardrail efficacy in multi-step settings depends more on structural data competence than semantic safety alignment, suggesting the recovery problem requires structured training beyond alignment alone. The maturation of turn-level RL methods for multi-step agents — GTPO (Nov 2025, turn-level reward assignment with +3.0% over GRPO), AT²PO (Jan 2026, tree-based turn-wise credit), Fission-GRPO (Jan 2026, on-policy error augmentation), GAGPO (May 2026, critic-free grouped temporal credit) — provides robust methodological foundations for training recovery behavior, with multiple established fallback options for credit assignment.\n\n## Landscape\nWe identify four distinct recovery paradigms in current agent safety research, plus a complementary guardrail-side correction approach, each requiring different metrics, training approaches, and benchmarks:\n\n(1) POST-BLOCKING TASK RECOVERY (ours): After a guardrail correctly blocks an unsafe action, the agent must find an alternative safe path to complete the original task — or recognize when no safe path exists. The Verifier Tax (Mar 2026) documents recovery rates from 21% (simpler Airline tasks) to near 0% (complex Retail scenarios) for GPT-OSS-20B and GLM-4-9B with TRIAD-SAFETY on tau-bench, with SSR below 5% in most settings. Symbolic Guardrails (Apr 2026) shows that recovery is model-dependent and feedback-dependent: on tau²-bench Airline (50 tasks), GPT-4o pass rates improve from 0.36 to 0.48 (+33% relative) and GPT-5 from 0.68 to 0.70 (+3% relative) when symbolic guardrails block unsafe actions and provide informative error messages explaining which policy was violated. The paper explicitly states agents 'use this feedback to adjust its subsequent actions, retry with a safer alternative, and often complete the task successfully.' However, Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation — recovery is neither a first-class metric nor a dedicated research target. It provides no recovery-specific benchmark, no recoverable/unrecoverable task classification, no false recovery rate measurement, no recovery latency analysis, no path quality assessment, and no recovery-specific training method. Its finding that even GPT-4o still fails 52% of tasks after blocking, combined with the near-zero recovery of smaller models documented by The Verifier Tax, directly MOTIVATES our work: recovery happens partially and uncontrollably for frontier models, but remains an unsolved problem for smaller open-source models that need dedicated training.\n\n(2) POST-HARM RECOVERY: After harm has occurred, the agent must remediate it. BackBench (arXiv 2604.18847, Apr 2026) provides 50 backtracking scenarios in OSWorld for computer-use agents, with a reward model trained on 1,150 pairwise human preference judgments, achieving +120 Elo improvement. Key differences from ours: (a) BackBench presupposes harm has occurred and must be undone; we presuppose harm was prevented; (b) BackBench operates in GUI/OS environments; we operate in tool-use API settings; (c) BackBench optimizes recovery quality via human preferences; we measure task completion, latency, path quality, AND recognition of unrecoverable scenarios.\n\n(3) POST-INCIDENT RESPONSE: AIR (arXiv 2602.11749, Feb 2026) provides a DSL-based incident response framework achieving >90% detection, remediation, and eradication rates. Critically, AIR terminates the task after remediation — it does not attempt to resume and complete the original task via an alternative safe path.\n\n(4) POST-ERROR RECOVERY: RAC (ACM CAIS 2026) provides log-based rollback for general execution errors on tau-bench/REALM-Bench. Fission-GRPO (Jan 2026) trains recovery from tool-calling errors via on-policy error augmentation (+5.7% recovery rate on BFCL v4). ToolMisuseBench (arXiv 2604.01508, Apr 2026) provides 6,800 tasks across CRUD/retrieval/file/scheduling environments with deterministic fault injection, measuring recovery quality and budgeted efficiency under explicit step/call/retry budgets — the operational-error counterpart to our safety-specific recovery benchmark. Its replayable fault injection methodology and budgeted efficiency metric S(k) are methodologically adjacent to our approach, but its faults are operational (schema drift, rate limits, authorization failures) rather than safety-policy violations. Hell or High Water (COLM 2025) evaluates recovery from environmental failures.\n\n(5) GUARDRAIL-SIDE CORRECTION: Three distinct technical approaches exist for correcting unsafe actions at the guardrail level rather than training agent-side replanning:\n\n(5a) ReGuard ('From Refusal to Recovery', arXiv 2510.13727, Oct 2025) learns a control-theoretic safety value function V(z) and fallback policy π_safe that INJECTS corrective actions when Q(z,a) ≤ 0 — the agent never replans, the guardrail replaces its unsafe action with a safe one. Evaluated on simulated driving (obstacle avoidance) and simple e-commerce (shopping cart budget constraints), not multi-step tool-use API settings with complex policy rules. Requires simulator access during guardrail training. Achieves 77.3% success vs 44.4% for myopic refusal, but proposes no recovery-specific benchmark.\n\n(5b) AGENT-C ('Enforcing Temporal Constraints for LLM Agents', arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2) provides guardrail-side correction via constrained decoding: it translates temporal safety specifications into first-order logic and uses SMT solving to detect non-compliant tool calls during token generation, then leverages constrained generation to produce compliant alternatives. AGENT-C achieves 100% safety conformance while improving utility (Claude Sonnet 4.5: 71.8%→75.2%; GPT-5: 66.1%→70.6%). Unlike ReGuard's control-theoretic approach, AGENT-C operates at the token generation level via formal verification, but shares the same fundamental characteristic: the GUARDRAIL corrects the action rather than the AGENT learning to replan. For open-weight models it can enforce at fine-grained token level; for closed-source models at coarser call-level resampling.\n\n(5c) Symbolic Guardrails' informative blocking feedback can be viewed as a lightweight guardrail-side intervention — by explaining policy violations, the guardrail provides implicit guidance toward safe alternatives, though without generating the corrective action itself.\n\nOur work is complementary to all category (5) approaches: they improve guardrail correction capability; we improve agent replanning capability. The optimal deployment may combine both — a smarter guardrail (ReGuard/AGENT-C/Symbolic) paired with an agent trained to replan when guardrail-side corrections are insufficient or unavailable. Our ReGuard ablation directly tests this complementarity.\n\nAdditional relevant concurrent work: SafePred (Feb 2026) achieves 97.6% safety via predictive prevention with world models — prevents unsafe actions but does not address recovery. MOSAIC (Mar 2026) introduces Plan-Check-Act/Refuse with up to 50% harmful behavior reduction — evaluates refusal quality, not post-refusal replanning. SafeAgent (Apr 2026) mentions constrained replanning as a recovery mechanism but provides no disaggregated metrics for replanning success rate, recovery rate, or path quality — overall evaluation uses ASR and NRP without isolating replanning contribution. Mind the GAP (Feb 2026) demonstrates text safety does not transfer to tool-call safety, motivating tool-level guardrails. OpenAgentSafety (ICLR 2026) provides a comprehensive 350+ task evaluation framework for agent safety with real tools but focuses on risk evaluation, not recovery. ATBench (Apr 2026) benchmarks trajectory-level safety with 1,000 trajectories across 2,084 tools but evaluates safety detection, not recovery. ToolSafe (Jan 2026) guides agents toward safety-aware reasoning via pre-execution feedback (TS-Flow), reducing harmful tool invocations by 65% — closest to our setting in spirit, but operates as a guardrail providing preventive guidance rather than training recovery. TraceSafe (Apr 2026) reveals guardrail efficacy depends more on structural JSON parsing than semantic alignment. AgentSpec (ICSE 2026) provides a DSL-based runtime enforcement framework with >90% unsafe execution prevention — its constraint specification approach directly informs our Safety Recovery Simulator's alternative action enumeration. SafeAgentBench (Dec 2024) includes hazardous tasks with only 5-10% rejection rates, demonstrating that recognizing unrecoverable scenarios is itself a challenge.\n\n## Approach\nWe construct RecoverBench by instrumenting tau-bench (Airline + Retail) with a guardrail intervention simulator that injects safety blocks at systematically varied trajectory points. The benchmark explicitly includes three task categories: (a) RECOVERABLE tasks where at least one safe alternative path exists (verified by oracle exhaustive search over constraint-satisfying action space), (b) CORRECTLY UNRECOVERABLE (CU) tasks where the user's request inherently requires a policy-violating action with no safe alternative (e.g., full refund on non-refundable ticket past cancellation window), and (c) PARTIALLY RECOVERABLE tasks where a degraded but safe version of the task can be completed (e.g., store credit instead of cash refund). We measure five metrics: Safe Recovery Rate (SRR: percentage of recoverable episodes where the agent finds an alternative safe path), False Recovery Rate (FRR: percentage of all episodes where the agent claims task completion but actually violates safety constraints via a DIFFERENT pathway than the blocked one — measuring constraint gaming/safety circumvention), Unrecoverable Recognition Rate (URR: percentage of CU episodes where the agent correctly identifies no safe path exists and gracefully informs the user), Recovery Latency (additional turns required after blocking for successful recoveries), and Alternative Path Quality (semantic similarity to optimal safe trajectories plus task reward preservation). The benchmark is explicitly designed to complement BackBench (post-harm, GUI/OS), AIR (post-incident, multi-domain), ToolMisuseBench (post-error, operational faults with deterministic replay), and RAC (post-error, general).\n\nBLOCKING FEEDBACK DESIGN: Motivated by Symbolic Guardrails' finding that informative error messages (explaining which policy was violated and why) enable partial recovery in frontier models, RecoverBench systematically varies blocking feedback informativeness as an experimental condition: (i) MINIMAL feedback (action blocked, no explanation), (ii) POLICY-CITED feedback (action blocked + specific policy rule citation, matching Symbolic Guardrails' approach), and (iii) DIAGNOSTIC feedback (action blocked + policy citation + available alternative actions, matching our SRS training context). This enables measuring how feedback informativeness affects recovery across model capability levels, directly extending Symbolic Guardrails' implicit finding that informative feedback helps.\n\nSAFETY RECOVERY SIMULATOR (SRS) SPECIFICATION: The SRS — the component that generates diagnostic context for RA-FGRPO training — operates through three modules: (1) CONSTRAINT EXTRACTION MODULE: Parses tau-bench's domain policy files (airline rebooking rules, retail return policies) to extract formal constraints as predicate functions, following AgentSpec's (ICSE 2026) trigger→predicate→enforcement pattern. Each constraint maps an action type to its validity conditions in the current environment state. (2) SAFE ALTERNATIVE ENUMERATOR: Given a blocked action and current state, queries the tau-bench API specification for all valid actions in the current state, filters out actions violating the triggered constraint or related constraints, and ranks remaining actions by semantic relevance to the original task intent (using embedding similarity between the blocked action's inferred goal and candidate action descriptions). For CU scenarios, returns an empty set. For partially recoverable scenarios, returns degraded alternatives with explicit quality annotations. (3) DIAGNOSTIC CONTEXT FORMATTER: Constructs augmented context as [trajectory_prefix; BLOCKED: action_name(args) → REASON: policy_rule_citation; AVAILABLE_ACTIONS: [ranked_action_list]; TASK_GOAL: original_user_request]. Critically, we provide WHICH actions are available but NOT which specific sequence solves the task — the agent must learn replanning, not memorize recovery templates. SRS validity is verified against oracle safe trajectories (computed offline via exhaustive search) to ensure enumeration completeness.\n\nFor training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO), adapting Fission-GRPO's on-policy error recovery augmentation for safety-specific guardrail interventions, with a tiered credit assignment strategy to mitigate dependency on any single unvalidated method. RA-FGRPO works as follows: (1) Standard GRPO exploration generates rollouts through guardrail-blocked scenarios on tau-bench; (2) The Safety Recovery Simulator intercepts blocked trajectories and augments them with diagnostic context from the three modules above; (3) Fission-based resampling generates G'=4 parallel recovery attempts from augmented contexts, creating dense on-policy training signal specifically for post-blocking adaptation; (4) PRIMARY CREDIT ASSIGNMENT: GTPO-based turn-level reward assignment (arXiv 2511.14846, Nov 2025, revised Apr 2026) provides fine-grained per-turn feedback with return-based advantage estimation and self-supervised reward shaping — adapted so the self-supervision signal comes from constraint compliance verification at each turn rather than code execution signals. GTPO is chosen as primary because: (a) it is the most established turn-level method (6+ months, revised), (b) it outperforms GRPO by 3.0% on multi-turn tool-integrated reasoning with negligible overhead, (c) its self-supervised reward shaping naturally adapts to safety constraint signals. FALLBACK CREDIT ASSIGNMENT: AT²PO-based tree-wise credit (arXiv 2601.04767, Jan 2026) serves as the validated fallback, using entropy-guided tree expansion for diverse recovery path exploration and recursive turn-wise value propagation — particularly suited when recovery requires exploring multiple branching alternatives. FUTURE EXTENSION: GAGPO's (arXiv 2605.13217, May 2026) critic-free grouped value proxy could further improve credit assignment if independently validated, but its requirement for exact textual state matching across rollouts needs adaptation for tool-use states (serialized API state + conversation history). We explicitly ablate all three credit assignment strategies.\n\nWe train open-source models (Qwen3.6-35B-A3B with 3B active parameters, Qwen3-4B) and evaluate across task complexity bins aligned with the Verifier Tax's horizon-dependent analysis. This model selection is directly motivated by the model-dependent recovery gap: Symbolic Guardrails shows frontier models (GPT-4o, GPT-5) partially recover with informative feedback, while The Verifier Tax shows open-source models (GPT-OSS-20B, GLM-4-9B) achieve near-zero recovery in complex scenarios — our training targets exactly this capability gap in open-source models. We additionally analyze how Canonical Path Deviation severity modulates recovery difficulty and whether RA-FGRPO helps agents re-anchor to canonical solution paths after guardrail intervention. A key ablation compares RA-FGRPO (with GTPO credit) against: vanilla GRPO, RA-FGRPO with AT²PO credit, RA-FGRPO with GAGPO credit (if feasible), offline DPO (DiaTool-DPO-style trajectory pairs), ToolSafe-style pre-execution safety feedback, and ReGuard-style guardrail-side correction (control-theoretic fallback policy). The ReGuard ablation is particularly important: it directly compares our agent-side replanning approach against guardrail-side action injection, testing whether the two are complementary. We also compare against frontier model baselines (GPT-4o, GPT-5) with Symbolic Guardrails-style informative blocking to establish the recovery ceiling that our training aims to approach for open-source models.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1,100 H100 hours (benchmark construction with oracle trajectory computation: 250h, RA-FGRPO training with GTPO credit + online rollouts on 3B-35B MoE models: 450h, evaluation sweeps across complexity bins and feedback conditions: 200h, ablations including AT²PO/GAGPO credit + ReGuard comparison: 200h)', 'timeline': '14-16 weeks', 'estimated_gpu_cost': '$2,200 (H100 spot at ~$2/hr)'}, 'human_in_loop': {'gpu_hours': '~1,100 H100 hours (same compute, faster iteration on SRS design and CU scenario curation)', 'timeline': '10-12 weeks', 'claude_api_cost': '$300-500 (code generation for SRS modules, constraint extraction, trajectory analysis, paper drafting)', 'estimated_gpu_cost': '$2,200'}, 'auto_research': {'gpu_hours': '~1,500 H100 hours (additional hyperparameter exploration, Fission resampling sweeps, three-way credit assignment ablations, ReGuard comparison, oracle trajectory exhaustive search for CU validation, feedback informativeness sweeps)', 'timeline': '6-8 weeks', 'claude_api_cost': '$800-1,200 (end-to-end pipeline orchestration, automated ablation design, constraint extraction from tau-bench policies, SRS validation)', 'estimated_gpu_cost': '$3,000', 'speed_bottleneck': \"GPU availability for concurrent RA-FGRPO online rollouts across model sizes; oracle safe trajectory computation for CU scenario validation; Fission resampling throughput (G'=4 parallel recovery attempts per blocked trajectory)\"}}\n\n## Inspired By\nField guide Section 7 (Defenses: guardrails, verification, monitoring) combined with Section 4.1 (pass@1 vs. production reliability gap). The Verifier Tax's quantitative evidence makes the gap between blocking success and task recovery concrete and measurable for open-source models, while Symbolic Guardrails reveals that recovery is model-dependent — frontier models partially recover with informative feedback, but smaller models cannot. This model-dependency motivates dedicated recovery training as the intervention point. The four-way taxonomy of recovery types (plus guardrail-side correction as a complementary paradigm) emerged from successive rounds of critical feedback, with the 'From Refusal to Recovery' and AGENT-C differentiation revealing that recovery requires distinguishing WHERE the intervention happens (guardrail vs. agent) and WHAT the intervention does (inject/constrain corrected action vs. replan). ToolMisuseBench's deterministic fault injection and budgeted efficiency metric inspired our benchmark design for replayability and efficiency measurement. The reviewer's 'correctly unrecoverable' insight led to the dual-challenge formulation (recover when possible, recognize impossibility when not), strengthening the benchmark's evaluative power. Fission-GRPO's on-policy error augmentation directly inspires our training approach; GTPO's turn-level reward assignment provides the primary credit mechanism; AT²PO's tree-based credit provides the validated fallback. Pattern: 'complementary gap-filling' with 'dual-challenge evaluation.'\n\n## Target Venues\n- EACL 2027 via ARR Aug 3, 2026 (commitment Oct 11, 2026 — primary target, 11 weeks for full RecoverBench + RA-FGRPO paper)\n- AAAI 2027 (abstract Jul 21 / paper Jul 28, 2026 — parallel stretch goal, scoped to RecoverBench benchmark paper only, deferring RA-FGRPO training results to extended version)\n- NAACL 2027 via ARR Oct-Nov 2026 (extended version with cross-benchmark comparison against BackBench/AIR/ToolMisuseBench and ReGuard complementarity analysis)\n\n## Key References\n- The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents (arXiv 2603.19328, Mar 2026)\n- Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility (arXiv 2604.15579, Apr 2026)\n- Enforcing Temporal Constraints for LLM Agents [AGENT-C] (arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2)\n- From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails [ReGuard] (arXiv 2510.13727, Oct 2025)\n- AIR: Improving Agent Safety through Incident Response (arXiv 2602.11749, Feb 2026)\n- Human-Guided Harm Recovery for Computer Use Agents [BackBench] (arXiv 2604.18847, Apr 2026)\n- Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors (arXiv 2601.15625, Jan 2026)\n- ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery in Agentic Systems (arXiv 2604.01508, Apr 2026)\n- Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization [GTPO] (arXiv 2511.14846, Nov 2025, revised Apr 2026)\n- AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv 2601.04767, Jan 2026)\n- GAGPO: Generalized Advantage Grouped Policy Optimization (arXiv 2605.13217, May 2026)\n- SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (arXiv, Feb 2026)\n- Learning When to Act or Refuse [MOSAIC] (arXiv, Mar 2026)\n- SafeAgent: A Runtime Protection Architecture for Agentic Systems (arXiv 2604.17562, Apr 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure (arXiv, Feb 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents (arXiv 2602.16943, Feb 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026)\n- ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis (arXiv 2604.02022, Apr 2026)\n- ToolSafe: Enhancing Tool Invocation Safety via Proactive Step-level Guardrail and Feedback (arXiv 2601.10156, Jan 2026)\n- TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories (arXiv 2604.07223, Apr 2026)\n- tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (ICLR 2025)\n- AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents (ICSE 2026)\n- Robust Agent Compensation (RAC) (ACM CAIS 2026)\n- Hell or High Water: Evaluating Agentic Recovery from External Failures (COLM 2025)\n- EmbodiedGovBench: Governance, Recovery, and Upgrade Safety in Embodied Agent Systems (arXiv, Apr 2026)\n- DiaTool-DPO: Multi-Turn DPO for Tool-Augmented LLMs (SIGDIAL 2025, arXiv 2504.02882, Apr 2025)\n- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv 2602.03025, Feb 2026)\n- T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL (ICML 2026 Spotlight)\n- SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents (arXiv 2412.13178, Dec 2024)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:47:39.698Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:47:39.698Z",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:47:39.712Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient evidence to produce my evaluation. Let me compile the analysis.

---

```
【阶段】: Triage

【领域调研】:

1. The Verifier Tax (arXiv 2603.19328, Mar 2026):
   - 核心发现：即使 guardrail 能拦截高达 94% 的不安全操作，Safe Success Rate (SSR) 在大多数设置下仍低于 5%。Recovery rate 在简单 Airline 任务中为 ~21%，在复杂 Retail 任务中趋近 0%（GPT-OSS-20B, GLM-4-9B）。
   - 与本 proposal 的关系：直接提供了核心 motivating evidence。Proposal 对其数据的引用经核实准确。但 Verifier Tax 本身的贡献是诊断问题（Safety-Capability Gap + Integrity Leaks），而非解决 recovery 问题。

2. Symbolic Guardrails (arXiv 2604.15579, Apr 2026):
   - 核心发现：对 80 个 agent safety benchmark 的系统综述；symbolic guardrails 在提供 informative error messages 时，GPT-4o pass rate 从 0.36 提升至 0.48（+33% relative），GPT-5 从 0.68 到 0.70。
   - 与本 proposal 的关系：提供 model-dependent recovery gap 的证据。Proposal 正确指出该论文将 recovery 作为 pass rate 的副产品度量而非 first-class target。但注意：Symbolic Guardrails 的核心贡献是 symbolic guardrail 设计而非 recovery 研究，所以"没有研究 recovery"并非一个 gap——而是该论文本来就不做这件事。

3. Fission-GRPO (arXiv 2601.15625, Jan 2026):
   - 核心发现：通过 on-policy error augmentation + Error Simulator 反馈，Qwen3-8B 在 BFCL v4 Multi-Turn 上 error recovery rate 提升 5.7%（42.75%→46.75%）。
   - 与本 proposal 的关系：RA-FGRPO 直接改编自 Fission-GRPO，将 operational error recovery 替换为 safety-specific post-blocking recovery。技术改造幅度有限——核心 mechanism（fission + diagnostic context + resampling）不变，只是 Error Simulator → Safety Recovery Simulator。

4. BackBench (arXiv 2604.18847, Apr 2026):
   - 核心发现：50 个 computer-use 场景的 post-harm recovery benchmark，使用 1,150 pairwise human preference judgments 训练 reward model，+120 Elo。
   - 与本 proposal 的关系：Post-harm ≠ post-blocking，domain（GUI/OS vs tool-use API）不同。Proposal 对二者的区分是清晰且准确的。

5. ToolMisuseBench (arXiv 2604.01508, Apr 2026):
   - 核心发现：6,800 tasks，deterministic fault injection，replayable evaluation。
   - 与本 proposal 的关系：Operational faults（schema drift, rate limits）vs safety-policy violations。Proposal 承认其 methodological adjacency 且提及 inspiration，定位合理。

6. SafeAgent (arXiv 2604.17562, Apr 2026):
   - 核心发现：Runtime protection architecture，包含 constrained replanning 机制——当 agent 动作偏离目标或风险升高时触发 replanning。
   - 与本 proposal 的关系：SafeAgent 已经实现了 constrained replanning 作为 recovery mechanism，虽然未提供 disaggregated recovery metrics。这是 proposal 需要更严肃对待的竞争者——其 replanning 机制在精神上与本 proposal 的 agent-side replanning 目标高度一致，尽管 SafeAgent 是 runtime architecture 而非 dedicated benchmark + training。

7. GTPO (arXiv 2511.14846, Nov 2025, revised Apr 2026):
   - 核心发现：Turn-level reward assignment，+3.0% over GRPO on multi-turn tool-integrated reasoning。
   - 与本 proposal 的关系：作为 RA-FGRPO 的 primary credit assignment 方法被直接采用。Proposal 描述准确。

8. ReGuard (arXiv 2510.13727, Oct 2025):
   - 核心发现：Control-theoretic guardrail，学习 safety value function V(z) 和 fallback policy π_safe，在 simulated driving 和 simple e-commerce 上评估。
   - 与本 proposal 的关系：Guardrail-side correction vs agent-side replanning，定位互补。Proposal 的处理合理。

- 调研总结：Post-blocking task recovery 作为一个 distinct failure mode 确实没有被现有工作作为 first-class research target isolate 出来。但这个 gap 的价值需要审慎评估：(a) Verifier Tax 和 Symbolic Guardrails 提供了清晰的 motivating evidence，(b) 现有 recovery 工作（Fission-GRPO, BackBench, ToolMisuseBench, SafeAgent）各自处理不同类型的 recovery 但均未直接 address post-blocking recovery，(c) 技术方案层面，核心训练方法（RA-FGRPO）是 Fission-GRPO 在 safety domain 的直接迁移，创新幅度有限。

【Trivial Alternative 检验】:

存在显著的 trivial alternative 威胁：

1. **Better prompting/context baseline**: Symbolic Guardrails 已经证明，仅仅提供 informative blocking feedback（解释哪条 policy 被违反），GPT-4o pass rate 就能从 0.36 提升到 0.48（+33% relative improvement）。对于 open-source models，一个自然的 trivial baseline 是：在 blocking 时提供结构化的 diagnostic context（与 proposal 的 SRS diagnostic feedback 类似）+ few-shot recovery examples，不做 RL 训练。如果这个 prompting baseline 已经能显著提升 recovery，那 RA-FGRPO 的增量价值就很有限。

2. **Supervised fine-tuning on recovery trajectories**: 相比 RA-FGRPO 的 on-policy RL + tiered credit assignment 的复杂方案，用 oracle safe trajectories（proposal 中已经需要计算）做简单的 SFT，可能是成本更低且效果接近的替代方案。Proposal 只对比了 offline DPO，未提及 SFT baseline。

3. **Informative error message design**: 如果 recovery gap 的核心瓶颈是"model 不理解 blocking feedback"（Symbolic Guardrails 的发现暗示这一点），那么工程上优化 blocking message 格式可能比 RL 训练更 practical。

Proposal 的增量价值主要在于：(a) 系统化的 benchmark 和 metrics 框架，(b) 对 unrecoverable scenario recognition 的评估维度。但训练方法的增量价值存疑。

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"Post-blocking recovery 是一个独立的、需要专门训练的能力"（核心假设）**: 这个假设是 proposal 的根基，但可能不成立。Recovery 本质上是 replanning——这是一个通用的 agent 能力，不一定需要 safety-specific 训练。Fission-GRPO 训练的 general error recovery 能力可能已经足以 transfer 到 post-blocking settings。如果 Fission-GRPO 本身就能提升 post-blocking recovery（因为 replanning 能力是通用的），那么 safety-specific RA-FGRPO 的价值就大打折扣。

2. **"Open-source models 的 recovery gap 主要源于缺乏 recovery-specific training"**: Verifier Tax 的数据也可能被解释为：小模型的 recovery 差是因为它们的通用推理/规划能力本身就弱，而非缺乏 safety-specific recovery 训练。如果是前者，那么通用能力提升（scale up, better pretraining）比 specialized recovery training 更有效。

3. **"tau-bench 上的 recovery 训练能泛化到其他 tool-use domains"**: 整个 benchmark 和训练都基于 tau-bench 的 Airline/Retail 两个 domain。这些 domain 的 policy rules 相对结构化和有限，recovery 也相应地 constrained。泛化到 policy rules 更模糊的 real-world settings（如医疗、法律）未经验证。

4. **"SRS 的 safe alternative enumeration 可以覆盖足够多的 recovery paths"**: Proposal 声称通过 exhaustive search over constraint-satisfying action space 来 verify recoverable/unrecoverable 分类，但 tau-bench 的 action space 是否真的可以被穷举？如果 action space 很大或有 combinatorial 的 multi-step dependencies，exhaustive search 可能不 feasible，导致 recoverable/unrecoverable 标注不准确。

【3 维度打分】:

1. Novelty: 【中】
   
   **正面**: 将 post-blocking task recovery 作为一个 distinct failure mode 从 post-harm (BackBench)、post-incident (AIR)、post-error (Fission-GRPO/ToolMisuseBench)、guardrail-side correction (ReGuard/AGENT-C) 中独立出来，这个 conceptual framing 是新的，且经调研确认没有现有工作将其作为 first-class benchmark target。The dual-challenge formulation (recover when possible + recognize impossibility) 增加了评估深度。Feedback informativeness 作为 experimental condition 的系统变化直接扩展了 Symbolic Guardrails 的隐含发现。

   **负面**: 技术层面的 novelty 有限。RA-FGRPO 本质上是 Fission-GRPO (arXiv 2601.15625) 的 Error Simulator → Safety Recovery Simulator 的替换 + GTPO (arXiv 2511.14846) credit assignment 的嫁接。Benchmark 设计是在 tau-bench (ICLR 2025) 上 instrument guardrail injection + 定义 5 个新 metrics。这些是 well-motivated 的 engineering 组合，但剥去 surface differences 后，核心技术 contribution 是"把已有方法适配到一个新 setting"。SafeAgent (arXiv 2604.17562) 已经实现了 constrained replanning（虽然缺 disaggregated metrics），进一步压缩了 novelty space。

2. Significance: 【中】

   **正面**: 问题本身具有实际重要性——Verifier Tax 和 Symbolic Guardrails 提供了具体量化证据表明 blocking ≠ task completion。随着 agent 在生产环境中的部署增加，safety-capability gap 是一个需要被解决的 real problem。Dual-challenge formulation 对推动该领域的评估标准有建设性作用。

   **负面**: 实际影响力受限于 (a) 仅基于 tau-bench 两个 domain（Airline + Retail），场景覆盖窄，(b) 目标模型是 3B-35B MoE open-source models，虽然有实际意义但 scope 有限，(c) 如果核心发现是 "RL training improves recovery for small models"，这是一个 "I would have guessed this" 级别的发现——方向是可预测的，问题在于幅度和 transfer。审稿人不太可能写 "surprising"。更具意义的 surprising findings 需要来自负面或反直觉方向（如"recovery training 在复杂 Retail 场景反而降低 recovery"），但 proposal 未能将 surprising insights 作为核心贡献来设计。

3. Related Work: 【强】

   经调研验证，proposal 的 related work 覆盖异常全面且准确：
   - 五类 recovery paradigm 的 taxonomy（post-blocking / post-harm / post-incident / post-error / guardrail-side correction）清晰且有证据支撑
   - 与每个最直接竞争者（BackBench, AIR, Fission-GRPO, ToolMisuseBench, ReGuard, AGENT-C, SafeAgent）的差异化定位均有具体、准确的 dimension 区分
   - 所有关键引用论文均经 WebSearch 验证存在且描述准确
   - 覆盖了非常新的工作（GAGPO May 2026, SafeAgent Apr 2026, TraceSafe Apr 2026）
   - 唯一可改善之处：SafeAgent 的 constrained replanning 机制可以被更深入地讨论作为最接近的 agent-side recovery 工作

【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
- Related Work 维度（强）为 proposal 提供了扎实的定位基础，但这是"最低限度"而非"加分项"——好的 related work 覆盖是必要条件而非充分条件。
- Significance（中）支撑了问题的合理性但未到 compelling 级别。问题真实存在、有数据支撑，但 scope 较窄（两个 tau-bench domain）且预期发现方向可预测。
- Novelty（中）是限制上界的关键因素。Conceptual framing 是新的（五类 taxonomy + dual-challenge），但技术 contribution 是现有方法的 domain adaptation（Fission-GRPO → RA-FGRPO），审稿人可能认为"applying existing RL methods to a new setting"不足以支撑 top-venue 录用。
- Trivial alternative 威胁（better prompting + informative feedback，如 Symbolic Guardrails 已证明有效的方向）可能被审稿人直接提出，如果 prompting baseline 已经能获得 substantial recovery improvement，训练方法的增量价值会被质疑。
- 概率下界 22% 反映了"framing novelty 有价值 + benchmark 设计 reasonable + 问题有实际意义"的基本面；上界 32% 反映了"如果实验结果中出现 surprising insights（如 feedback informativeness 的 interaction effects、unrecoverable recognition 的 novel failure patterns），可能 push 过线"的可能性。但基于 idea 本身的质量评估，中位 27% 是合理的。

【主要风险】:
1. **Novelty 被判 insufficient**: 审稿人可能认为核心技术贡献（RA-FGRPO = Fission-GRPO 在 safety setting 的直接迁移；RecoverBench = tau-bench + guardrail injection + 新 metrics）是 "straightforward application/adaptation"，不够支撑 top-venue 级别的 novelty 要求。
2. **Trivial baseline 威胁**: 审稿人可能要求证明 RA-FGRPO 相比 "informative blocking feedback + few-shot recovery prompting"（不做 RL 训练）有显著增量。如果 prompting baseline 已经能关闭大部分 recovery gap，整个 training 方法的 motivation 就被削弱。
```

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct the evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

【领域调研】:
- [The Verifier Tax] (arXiv 2603.19328, Mar 2026): 直接动机来源。在 tau-bench 上用 GPT-OSS-20B 和 GLM-4-9B 测量，guardrail 可拦截高达 94% 不安全动作，但 SSR 在大多数设置下低于 5%，recovery rate 从简单 Airline 任务的 21% 到复杂 Retail 场景的近 0%。论文确实存在，描述准确。
- [Symbolic Guardrails] (arXiv 2604.15579, Apr 2026): 直接动机来源。在 tau²-bench 上测试 symbolic guardrails 对 pass rate 的影响。GPT-4o 从 0.36→0.48（+33% relative），GPT-5 从 0.68→0.70。论文确实存在，但 proposal 对其"recovery"的描述有微妙的外推——原文核心贡献是 symbolic guardrail 设计，recovery 只是 pass rate 副产品，proposal 对此有正确承认。
- [Fission-GRPO] (arXiv 2601.15625, Jan 2026): 训练方法的直接基础。在 BFCL v4 Multi-Turn 上，Qwen3-8B recovery rate 提升 5.7%，overall accuracy +4%。论文确实存在，描述准确。核心区别：Fission-GRPO 处理的是一般工具执行错误，而非 safety policy violation。
- [ToolMisuseBench] (arXiv 2604.01508, Apr 2026): 最接近的 benchmark 竞争者。6800 tasks，deterministic fault injection，测量 recovery quality 和 budgeted efficiency。论文确实存在。关键区别：ToolMisuseBench 的 faults 是 operational（schema drift, rate limits），不是 safety policy violations。
- [BackBench] (arXiv 2604.18847, Apr 2026): Post-harm recovery benchmark。50 tasks in OSWorld，reward model trained on 1,150 pairwise judgments。确实存在，描述准确。关键区别：BackBench 假设 harm 已发生需补救，本 proposal 假设 harm 被阻止需替代路径。
- [GTPO] (arXiv 2511.14846, Nov 2025): Turn-level reward assignment，+3.0% over GRPO。论文确实存在，描述准确。
- [AGENT-C] (arXiv 2512.23738, Dec 2025): Constrained decoding for temporal safety，100% safety conformance，utility 提升。论文确实存在。这是最强的"guardrail-side correction"竞争者。
- [Canonical Path Deviation] (arXiv 2602.19008, Feb 2026): Off-canonical actions compound subsequent deviation by 22.7 pp。论文确实存在，描述准确。
- 调研总结: Agent safety 领域在 2025-2026 年经历了快速成熟期，guardrail blocking 能力已基本解决（blocking rate 高达 94-100%），但 blocking 之后的 agent 行为（recovery/replanning）是一个确实存在的 gap。现有 benchmark 分别覆盖了 post-harm (BackBench)、post-error (ToolMisuseBench/Fission-GRPO)、post-incident (AIR)、guardrail-side correction (AGENT-C/ReGuard)，但确实没有专门的 post-blocking recovery benchmark。Proposal 准确定位了这个空白，但空白的"宽度"需要审视——post-blocking recovery 与 post-error recovery 的技术距离可能比 proposal 声称的要近。

【Trivial Alternative 检验】:
存在两个显著的 trivial alternative 威胁：

(1) **Informative feedback + in-context prompting**: Symbolic Guardrails 已经表明，仅仅给 agent 提供信息量更大的 blocking feedback（解释哪条 policy 被违反、为什么），GPT-4o pass rate 就能从 0.36 提升到 0.48（+33%）。一个自然的 trivial baseline 是：给 open-source 模型同样的 informative feedback + few-shot recovery examples。Proposal 没有直接回答"为什么这不够"——The Verifier Tax 的实验并未使用 informative feedback，所以我们实际上不知道 informative feedback 对小模型的效果如何。这是增量价值最需要论证的地方。

(2) **直接用 AGENT-C/ReGuard 的 guardrail-side correction**: AGENT-C 已经实现 100% safety conformance 且提升了 utility。如果 guardrail 端可以直接生成合规替代动作，为什么还需要训练 agent-side replanning？Proposal 声称二者互补，但没有论证在哪些场景下 AGENT-C 不足以解决问题。

**增量价值判断**: Proposal 的真实增量价值取决于两个实证问题的答案：(a) informative feedback 对小模型的效果是否显著低于对 frontier 模型的效果？(b) 是否存在 guardrail-side correction 无法覆盖的复杂多步 recovery 场景？如果两个答案都是"是"，增量价值成立。但目前这两个问题都是 assumption，不是 evidence。

【前提假设检验】:
核心逻辑链有三个关键的未验证假设：

(1) **"Post-blocking recovery 与 post-error recovery 有本质区别"**: 这是整个 taxonomy 和 benchmark 存在理由的基石。Proposal 的论证是：safety constraint 消除了整类解决方案，而 operational error 只是暂时性失败。但从 agent 的决策角度看，两者都是"当前路径不通，需要找替代路径"。reviewer 可以合理质疑：为什么不能在 ToolMisuseBench 上加一个 safety-fault 类别，而非需要一个全新 benchmark？

(2) **"Open-source 模型的 recovery 差距可以通过 RL 训练来弥合"**: The Verifier Tax 显示小模型 recovery 近乎为零，但这可能是小模型整体 capability 不足的表现，而非缺乏专门 recovery 训练的结果。如果模型的基础推理能力不够，专门的 recovery 训练可能只会在 distribution 内有效（tau-bench 的 2 个 domain），而无法泛化。

(3) **"Correctly Unrecoverable 识别是一个独特的 challenge"**: 这是 benchmark 的 dual-challenge 设计核心，但目前没有任何实证表明现有模型在这方面存在系统性问题。可能当前模型已经能较好地识别不可恢复场景（通过 common sense），而这个维度不增加多少评估价值。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 准确识别了一个确实没有被现有工作专门覆盖的 gap：post-blocking recovery 作为 first-class benchmark target。五类 recovery 的 taxonomy（post-blocking / post-harm / post-incident / post-error / guardrail-side correction）是清晰且有贡献的概念框架。Dual-challenge 设计（recover when possible, recognize impossibility when not）是一个有价值的设计元素。
   
   然而，novelty 存在"距离问题"：与 ToolMisuseBench（post-error recovery, Apr 2026）和 Fission-GRPO（error recovery training, Jan 2026）的技术距离较近。核心差异是"error type"（safety violation vs. operational error），而非"recovery mechanism"——agent 仍然在做同一件事：replanning。这使得 novelty 更像是"已有 paradigm 的 domain specialization"而非"fundamentally new problem"。RA-FGRPO 本身是 Fission-GRPO + SRS + GTPO 的组合，每个组件都来自已有工作，组合层面的创新是增量的。
   
   与最相关的 5-10 篇工作相比，剔除 surface differences 后，剩余的核心 novelty delta 是：(a) safety-specific recovery 的 benchmark 设计（含 CU 类别和 FRR 指标），(b) feedback informativeness 作为系统化实验变量。这是 solid 但非 breakthrough 级别的贡献。

2. **Significance: 中** — 
   问题本身确实重要且有实际影响力。The Verifier Tax 量化的 safety-capability gap（SSR < 5%）是 striking 的数字，说明 guardrail blocking ≠ safe task completion 是一个真实且 under-addressed 的问题。如果解决了，对 open-source model 的安全部署有直接价值。
   
   但 significance 存在上界限制：(a) benchmark 仅构建在 tau-bench 2 个 domain 上（Airline, Retail），generalizability 受限；(b) 如果核心发现是 "dedicated recovery training improves recovery rates for small models"，审稿人的反应更可能是 "makes sense, I would have guessed this" 而非 "surprising"；(c) 与 AGENT-C（100% safety, utility 提升）相比，agent-side recovery training 的实际部署 value proposition 不明确——如果 guardrail-side correction 已经够用，agent-side training 的 marginal value 就比较有限。

3. **Related Work: 强** — 
   Related work 的覆盖极为全面和准确。五类 recovery 的 taxonomy 差异化定位清晰。所有主要引用的论文（The Verifier Tax, Symbolic Guardrails, Fission-GRPO, ToolMisuseBench, BackBench, AGENT-C, ReGuard, GTPO, Canonical Path Deviation）均经验证存在且描述基本准确。对 AGENT-C 和 ReGuard 作为 guardrail-side correction 的定位和互补性论述到位。对 SafeAgent 的 "constrained replanning" 的引用也准确——SafeAgent 确实提到 replanning 但未提供 disaggregated metrics。对于一个 proposal 阶段的文档，这一水准的 related work 分析是优秀的。
   
   唯一的小瑕疵：部分论文非常新（GAGPO, May 2026），其方法尚未被独立验证，proposal 对此有正确声明。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
三个维度综合来看——Related Work 是强项（覆盖面和差异化定位优秀），但这主要决定下限而非上限。Novelty 是中等水平：gap 确实存在但较窄，核心技术贡献（RA-FGRPO）是增量式组合创新。Significance 同样中等：问题重要但预期发现的"surprise factor"偏低——如果 positive result 是 "recovery training helps small models recover better"，这更接近 confirmatory 而非 surprising。

**限制上界的关键因素**是 Novelty 和 Significance 的交叉：
- Novelty 维度：与 ToolMisuseBench 和 Fission-GRPO 的技术距离过近，核心差异（safety-specific vs. operational error）可能被审稿人视为 domain adaptation 而非 fundamental contribution
- Significance 维度：核心发现的预期"surprise"偏低，且 AGENT-C 的存在削弱了 agent-side recovery training 的 value proposition
- 两个 trivial alternative（informative feedback + ICL；AGENT-C guardrail-side correction）都需要在 paper 中被有力地 empirically refuted，否则会严重威胁 acceptance

概率未低于 22% 的原因：问题定位准确、gap 确实存在、benchmark 设计（dual-challenge + feedback informativeness + FRR）有真实贡献、related work 质量高。

【主要风险】:
1. **Novelty 距离风险**: Reviewer 可能判定 post-blocking recovery 只是 ToolMisuseBench/Fission-GRPO 在 safety domain 的简单特化（"Why not just add safety-fault injection to ToolMisuseBench?"），从而将整个 benchmark 的 novelty 判为 incremental。这是最可能的 rejection 理由。
2. **Trivial alternative 风险**: 如果 informative blocking feedback + few-shot prompting 就能让小模型达到接近 RA-FGRPO 训练后的 recovery 效果，整个训练方法的 contribution 就被 undermine。Symbolic Guardrails 已经证明 informative feedback 对 frontier 模型非常有效（+33%），但对小模型的效果是 unknown——如果实验发现 informative feedback 本身就足够，paper 的训练贡献就变成了 null result。
```

Sources:
- [The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents](https://arxiv.org/abs/2603.19328)
- [Symbolic Guardrails for Domain-Specific Agents](https://arxiv.org/abs/2604.15579)
- [Fission-GRPO: Learning to Recover from Execution Errors](https://arxiv.org/abs/2601.15625)
- [ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery](https://arxiv.org/pdf/2604.01508)
- [BackBench: Human-Guided Harm Recovery for Computer Use Agents](https://arxiv.org/html/2604.18847v1)
- [GTPO: Group Turn Policy Optimization](https://arxiv.org/abs/2511.14846)
- [AGENT-C: Enforcing Temporal Constraints for LLM Agents](https://arxiv.org/abs/2512.23738)
- [Canonical Path Deviation as a Causal Mechanism of Agent Failure](https://arxiv.org/abs/2602.19008)
- [SafeAgent: A Runtime Protection Architecture for Agentic Systems](https://arxiv.org/abs/2604.17562)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [The Verifier Tax] (arXiv 2603.19328, Mar 2026): 直接动机论文。在 tau-bench 上用 GPT-OSS-20B 和 GLM-4-9B 测试，发现安全中介可拦截高达 94% 不合规动作，但 SSR 在大多数设置下低于 5%，recovery rate 从 Airline 的 21% 到 Retail 的近 0%。Proposal 对该论文的引用和数据描述准确。
- [Symbolic Guardrails for Domain-Specific Agents] (arXiv 2604.15579, Apr 2026): 在 τ²-Bench/CAR-bench/MedAgentBench 上评估 symbolic guardrails 对安全性和 agent 成功率的影响。Proposal 引用其 GPT-4o pass rate 从 0.36→0.48 的改善。该论文确实存在且关注 guardrail 如何影响 agent 表现，但其核心贡献是 guardrail 设计而非 recovery 评估——proposal 准确地指出 recovery 在该论文中只是"side effect"而非一等公民。
- [Fission-GRPO] (arXiv 2601.15625, Jan 2026): 在 BFCL v4 Multi-Turn 上通过 on-policy error augmentation 提升 Qwen3-8B 的 error recovery rate +5.7%。解决的是**操作性错误**（tool-calling errors），不是 safety policy violations。Proposal 的 RA-FGRPO 直接建立在此方法之上。
- [BackBench] (arXiv 2604.18847, Apr 2026): 50 个 OSWorld 场景，测试 computer-use agent 的 post-harm recovery，用 1,150 个 human preference judgments 训练 reward model。与 proposal 的区分清晰：BackBench 假设 harm 已发生需修复，proposal 假设 harm 被阻止后需恢复任务。
- [ToolMisuseBench] (arXiv 2604.01508, Apr 2026): 6,800 个任务，覆盖 CRUD/retrieval/file/scheduling 环境，有确定性 fault injection。解决的是操作性错误（schema drift, rate limits, authorization failures），不是 safety policy violations。与 proposal 的区分点明确。
- [GTPO] (arXiv 2511.14846, Nov 2025, revised Apr 2026): Turn-level reward assignment，在 math reasoning 上比 GRPO +3.0%。Proposal 选其作为主要 credit assignment 方法，理由合理（最成熟、overhead 小）。
- [ReGuard] (arXiv 2510.13727, Oct 2025): Control-theoretic guardrail-side correction，guardrail 自身注入修正动作而非 agent 重新规划。在 simulated driving 和简单 e-commerce 上评估。Proposal 正确区分这是 guardrail-side vs agent-side 的差异。
- [AGENT-C] (arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop): Constrained decoding 方法，通过 SMT solving 检测非合规 tool calls 并在 token 生成层面纠正。同样是 guardrail-side correction。
- [SafeAgent] (arXiv 2604.17562, Apr 2026): 运行时保护架构，提到 constrained replanning 作为 recovery 机制，但没有对 replanning 成功率的独立评估。Proposal 正确指出其缺乏 disaggregated metrics。
- [CostBench] (arXiv 2511.02734): 引入动态 blocking events 要求 agent 重新规划，但关注 cost-optimality 而非 safety recovery。方法论上有一定相关性。

- 调研总结: Agent safety 领域在 2025-2026 年出现了大量 benchmark 和方法（guardrail 设计、安全评估、错误恢复），但**post-blocking task recovery**（guardrail 正确阻止不安全动作后，agent 如何恢复完成任务）确实是一个已被记录（Verifier Tax, Symbolic Guardrails）但未被专门 benchmark 化和训练的 gap。最接近的工作是 Fission-GRPO（操作性错误恢复）和 ToolMisuseBench（操作性错误 benchmark），但两者都不涉及 safety policy violations 后的恢复。这个 gap 是真实的。

【Trivial Alternative 检验】:
存在两个潜在的 trivial alternatives:

1. **"更好的 error message + 更大的模型"作为 baseline**: Symbolic Guardrails 已经显示，仅通过提供 informative blocking feedback，GPT-4o 就能获得 33% 的相对改善（0.36→0.48）。一个 trivial baseline 是：对任何开源模型，简单地在 guardrail blocking 时提供更丰富的错误信息（policy citation + available actions），不做任何专门训练，看 recovery 能改善多少。Proposal 的 feedback informativeness 实验确实设计了这个对照（minimal vs policy-cited vs diagnostic），但关键问题是：**如果 diagnostic feedback 本身就能大幅提升 recovery，RA-FGRPO 的增量价值有多大？** 这是一个需要实验回答的问题，但也是 idea 层面的潜在 trivial alternative 威胁。

2. **"直接用 Fission-GRPO + safety-specific 数据"**: RA-FGRPO 的核心相对于 Fission-GRPO 的差异在于：(a) Safety Recovery Simulator 提供 diagnostic context 而非 Error Simulator 的一般错误反馈，(b) 安全相关的 constraint compliance verification。但这是否足以构成一个独立的方法贡献？还是仅仅是 Fission-GRPO 在新 domain 上的 straightforward application？

增量价值主要在于：(1) benchmark 本身（gap 真实存在）；(2) dual-challenge formulation（recoverable + unrecoverable 的区分）；(3) False Recovery Rate 指标（检测 agent 是否通过另一条不安全路径绕过限制）。这些是 benchmark 设计层面的 genuine contributions，但训练方法的增量价值较弱。

【前提假设检验】:
核心 claim 的逻辑链条中，以下环节是未经验证的假设：

1. **"Post-blocking recovery 是一个可独立训练的能力"**: Proposal 假设 recovery 可以通过专门训练来改善（特别是对小模型），但有一种可能性是：recovery 能力本质上是通用推理能力的体现，不可能通过 narrow task-specific training 来有效提升（尤其是在 tau-bench 之外的场景中的 generalization）。这个假设的验证依赖于实验结果。

2. **"Safety-specific error augmentation 比 general error augmentation 效果更好"**: RA-FGRPO 与 Fission-GRPO 的关键区别在于 safety-specific context。但如果 recovery 本质上是一个通用的 replanning 问题（无论错误原因是 safety violation 还是 rate limit），那么 safety-specific 训练可能不会比 general error recovery 训练有显著优势。

3. **"Oracle exhaustive search 可以可靠地验证 recoverable/unrecoverable 分类"**: Proposal 依赖 oracle exhaustive search 来确认哪些场景 genuinely unrecoverable。在 tau-bench 的 API action space 上这可能可行，但这个假设的成立范围有限——如果 action space 更复杂，exhaustive search 可能不可行。

4. **"Canonical Path Deviation 解释了 recovery 难度"**: Proposal 引用 CPD 论文（off-canonical actions compound deviation by 22.7 pp），但这个发现是否适用于 guardrail-blocked 场景（而非 agent 自发偏离）是一个未验证的类比推理。

【3 维度打分】:
  1. Novelty: 中 — 
     **Benchmark 贡献有真实 novelty**: 调研确认目前没有专门 benchmark 测量 post-blocking task recovery。Verifier Tax 和 Symbolic Guardrails 记录了这个问题但没有提出 benchmark。ToolMisuseBench 覆盖操作性错误而非 safety violations。BackBench 覆盖 post-harm 而非 post-blocking。这个 gap 是真实的，RecoverBench 填补了它。
     **Dual-challenge formulation 有一定 novelty**: 同时要求 agent recover when possible + recognize impossibility when not，这在 safety recovery 领域未被专门提出（SafeAgentBench 的 5-10% rejection rates 暗示这是一个真实挑战）。
     **False Recovery Rate 指标有 novelty**: 检测 agent 是否通过替代不安全路径绕过 guardrail，这是一个审稿人可能会认为 insightful 的指标设计。
     **但训练方法 novelty 有限**: RA-FGRPO 本质上是 Fission-GRPO + GTPO credit assignment，应用于 safety recovery 场景。Safety Recovery Simulator 相对于 Fission-GRPO 的 Error Simulator 的区别主要在于 domain-specific context formatting，不是方法论创新。三种 credit assignment 的"tiered"策略看起来更像 hedging 而非贡献。
     **总体**: 核心 novelty 在 benchmark 设计和 problem formulation，而非方法论。这是可以的（benchmark paper + method），但审稿人可能会觉得 method 部分是"applying existing RL methods to new domain"。

  2. Significance: 中 — 
     **问题的实际重要性**：随着 guardrail 在生产环境中的广泛部署，"block but fail to complete task"确实是一个日益重要的实际问题。Verifier Tax 的数据让这个问题变得具体可度量。
     **对 NLP/CL 领域的影响**：这个贡献主要服务于 agent safety 这一子领域。Benchmark 和 training method 的范围限于 tau-bench（Airline + Retail），generalizability 到其他 domains 不确定。
     **核心发现的"surprise factor"偏低**：如果实验 positive（RA-FGRPO 提升了小模型的 recovery），审稿人更可能说"I would have guessed that dedicated training helps"而不是"surprising"。如果 negative，则变成一个 benchmark-only paper，意义进一步降低。
     **但 dual-challenge 维度提升了 significance**：如果实验发现 agent 在 unrecoverable scenario recognition 上表现极差（类似 SafeAgentBench 的 5-10%），这本身就是一个有价值的 finding。

  3. Related Work: 强 — 
     **覆盖极为充分**：Proposal 展示了对领域的深入理解，引用了所有主要的近期工作（Verifier Tax, Symbolic Guardrails, Fission-GRPO, BackBench, ToolMisuseBench, GTPO, AT²PO, ReGuard, AGENT-C, SafeAgent, AgentSpec 等），且引用描述基本准确（经调研验证）。
     **五种 recovery paradigm 的 taxonomy 是真正的贡献**: post-blocking vs post-harm vs post-incident vs post-error vs guardrail-side correction 的分类清晰、有意义，每个类别都有具体论文支撑。这种 taxonomy 本身就能帮助领域组织思路。
     **差异化定位清晰**：与每个最相关工作的区别都有明确阐述（BackBench: post-harm vs post-blocking; ToolMisuseBench: operational vs safety; ReGuard: guardrail-side vs agent-side; Fission-GRPO: general errors vs safety blocks）。
     **唯一小瑕疵**：Symbolic Guardrails 的具体数据（GPT-4o: 0.36→0.48）我未能在搜索中直接验证到 exact numbers，但论文确实存在且主题一致。

【概率估计】: [25% - 35%] 中位 28%

【估计理由】: 
Novelty 中等（benchmark 填补真实 gap，但 training method 是已有方法的 domain adaptation），Significance 中等（问题真实重要但范围窄、核心发现 surprise factor 低），Related Work 强（taxonomy 和覆盖都是一流水平）。

概率上界被两个因素限制：
(1) **Training method novelty 不足**——RA-FGRPO 相对于 Fission-GRPO 的增量 delta 主要是 domain adaptation 而非方法论创新，三种 credit assignment 的 tiered 设计看起来像 hedging 而非贡献，审稿人可能会认为 "applying Fission-GRPO to safety recovery" 不构成独立方法贡献。
(2) **核心发现的可预测性**——"专门训练可以改善小模型的 post-blocking recovery" 是一个审稿人会说 "I would have guessed this" 的结论。如果这篇论文的 main finding 是 "we trained and it worked"，novelty 评价会偏低。

概率下界由问题的真实性和 benchmark 设计的严谨性支撑：这个 gap 确实存在、确实没人做过、benchmark 设计有 thoughtful 的维度（dual-challenge, FRR 指标, feedback informativeness variation），即使 training method 部分被认为 incremental，benchmark 贡献本身也有价值。

【主要风险】: 
1. **Method vs Benchmark 张力**：Proposal 同时想做 benchmark paper 和 training method paper，但 training method 的 novelty 不足以支撑方法贡献，可能导致审稿人觉得"benchmark 有价值但 method 部分 incremental"——这是 EMNLP 常见的被 Borderline 的模式。
2. **Trivial alternative 威胁**：如果 diagnostic feedback 本身（不做训练）就能大幅改善 recovery，RA-FGRPO 的增量价值会被大幅削弱。Symbolic Guardrails 已经展示了 informative feedback 的效果，如果 RecoverBench 的实验发现 feedback level 是主要 driver 而非 training method，核心 story 会 collapse。
```

Sources:
- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)
- [Symbolic Guardrails for Domain-Specific Agents (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)
- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)
- [BackBench: Human-Guided Harm Recovery (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)
- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/abs/2604.01508)
- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)
- [ReGuard (arXiv 2510.13727)](https://arxiv.org/abs/2510.13727)
- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)
- [SafeAgent (arXiv 2604.17562)](https://arxiv.org/abs/2604.17562)


【原始 proposal（允许参考但不是主要依据）】:
# Beyond Blocking: Benchmarking and Training Agent Task Recovery After Guardrail Interventions in Multi-Step Tool Use

## Description
Current agent safety guardrails achieve high blocking rates (up to 94%) for unsafe actions, yet post-blocking recovery is inconsistent and model-dependent: open-source models (GPT-OSS-20B, GLM-4-9B) achieve safe success rates below 5% with recovery rates from 21% to near 0% (The Verifier Tax, 2026), while frontier models with informative blocking feedback show partial recovery (GPT-4o: 0.36→0.48 pass rate per Symbolic Guardrails, 2026) but still fail 52% of tasks. We identify post-blocking task recovery as a distinct failure mode — categorically different from post-harm recovery (BackBench), post-incident response (AIR), post-error recovery (RAC/Fission-GRPO/ToolMisuseBench), and guardrail-side correction (ReGuard, AGENT-C). We propose RecoverBench, a benchmark measuring agent task recovery after guardrail interventions in multi-step tool-use settings, featuring a dual challenge: agents must recover when safe alternatives exist AND recognize when recovery is impossible. Built atop tau-bench (Airline/Retail), RecoverBench injects guardrail blocks at critical trajectory points with systematically varied feedback informativeness (minimal, policy-cited, diagnostic) and introduces three task categories (recoverable, correctly unrecoverable, partially recoverable) evaluated by five metrics: Safe Recovery Rate, False Recovery Rate (detecting constraint gaming via alternative unsafe pathways), Unrecoverable Recognition Rate, Recovery Latency, and Alternative Path Quality. We detail a three-module Safety Recovery Simulator (constraint extraction, safe alternative enumeration via API specification parsing, diagnostic context formatting) that generates training signal without revealing oracle solutions. For training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO) with a tiered credit assignment strategy: GTPO-based turn-level rewards as primary (most established, +3.0% over GRPO), AT²PO-based tree credit as validated fallback, and GAGPO-style grouped credit as future extension pending independent validation. RA-FGRPO adapts Fission-GRPO's on-policy error augmentation for safety-specific recovery, generating G'=4 parallel recovery attempts per blocked trajectory. We evaluate on Qwen3.6-35B-A3B and Qwen3-4B across complexity bins, targeting the model-dependent recovery gap: approaching frontier-model recovery levels for open-source models. Ablations compare against vanilla GRPO, offline DPO, ToolSafe pre-execution feedback, ReGuard-style guardrail-side correction, and frontier model baselines with informative blocking.

## Core Problem
Current guardrails achieve high unsafe-action blocking rates (up to 94%), but post-blocking task recovery is inconsistent, model-dependent, and unmeasured as a first-class capability. For smaller open-source models (GPT-OSS-20B, GLM-4-9B), recovery rates range from 21% on simpler procedural tasks to near 0% on complex Retail scenarios, with safe success rates below 5% in most settings (The Verifier Tax, 2026). Frontier models with informative blocking feedback fare substantially better — Symbolic Guardrails (2026) shows GPT-4o pass rates improving from 0.36 to 0.48 on tau²-bench when guardrails provide policy-violation explanations, and GPT-5 from 0.68 to 0.70 — but even GPT-4o still fails 52% of tasks after blocking. Critically, no existing work isolates post-blocking recovery as a dedicated benchmark target: Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation, not recovery quality, and provides no recoverable/unrecoverable task classification, no false recovery rate measurement, and no recovery-specific training method. This represents a distinct and underexplored failure mode: post-blocking task recovery. Unlike post-harm recovery (BackBench) where harm has occurred and must be remediated, post-incident response (AIR) where the system detects and contains safety breaches, post-error recovery (RAC/Fission-GRPO) where operational errors must be corrected, or guardrail-side correction (ReGuard, AGENT-C) where the guardrail itself generates corrective actions, post-blocking recovery requires the AGENT to find an alternative safe path to complete the user's legitimate task after being correctly prevented from taking an unsafe action. Critically, some blocked scenarios may genuinely have no safe alternative path — the agent must also learn to recognize when recovery is impossible and gracefully inform the user. No existing benchmark isolates this specific failure mode with its dual challenge (recover when possible, recognize impossibility when not), and no training method specifically targets the agent's adaptive replanning ability after correct guardrail intervention.

## Opportunity
The Verifier Tax (Mar 2026) quantifies a devastating Safety-Capability Gap for open-source models: with GPT-OSS-20B and GLM-4-9B on tau-bench, even with 94% unsafe action blocking, safe success rates remain below 5% in most settings, and recovery rates following blocked actions range from 21% in simpler procedural Airline tasks to near 0% in complex Retail scenarios. Symbolic Guardrails (Apr 2026) reveals the model-dependency dimension: when guardrails provide informative blocking feedback (explaining which policy was violated and why), GPT-4o achieves a 33% relative improvement in pass rate (0.36→0.48) on tau²-bench Airline, and GPT-5 a modest 3% improvement (0.68→0.70) — demonstrating that (a) recovery IS possible when the agent receives informative feedback, (b) even frontier models still fail 52% of tasks (GPT-4o) despite recovery attempts, and (c) recovery quality is never measured as a first-class metric. This model-dependent recovery gap creates a clear motivation: if frontier models can partially recover with informative feedback but smaller models cannot, then dedicated recovery training can close this gap for open-source models. The gap is distinct from what AIR (>90% remediation success in post-incident response), BackBench (50 post-harm recovery scenarios in OSWorld), and ReGuard (control-theoretic guardrail correction in driving/e-commerce) address. In post-blocking recovery, the guardrail works as intended — harm is prevented — but the agent fails at adaptive replanning. Canonical Path Deviation (Feb 2026) explains the structural difficulty: off-canonical actions compound subsequent deviation by 22.7 percentage points, meaning that once an agent is pushed off its solution path by a blocked action, the probability of finding an alternative path drops sharply. Meanwhile, ToolSafe (Jan 2026) shows that safety-feedback-driven reasoning can improve benign task completion by ~10% and reduce harmful tool invocations by 65%, but this represents pre-execution guidance, not post-blocking recovery training. TraceSafe (Apr 2026) demonstrates that guardrail efficacy in multi-step settings depends more on structural data competence than semantic safety alignment, suggesting the recovery problem requires structured training beyond alignment alone. The maturation of turn-level RL methods for multi-step agents — GTPO (Nov 2025, turn-level reward assignment with +3.0% over GRPO), AT²PO (Jan 2026, tree-based turn-wise credit), Fission-GRPO (Jan 2026, on-policy error augmentation), GAGPO (May 2026, critic-free grouped temporal credit) — provides robust methodological foundations for training recovery behavior, with multiple established fallback options for credit assignment.

## Landscape
We identify four distinct recovery paradigms in current agent safety research, plus a complementary guardrail-side correction approach, each requiring different metrics, training approaches, and benchmarks:

(1) POST-BLOCKING TASK RECOVERY (ours): After a guardrail correctly blocks an unsafe action, the agent must find an alternative safe path to complete the original task — or recognize when no safe path exists. The Verifier Tax (Mar 2026) documents recovery rates from 21% (simpler Airline tasks) to near 0% (complex Retail scenarios) for GPT-OSS-20B and GLM-4-9B with TRIAD-SAFETY on tau-bench, with SSR below 5% in most settings. Symbolic Guardrails (Apr 2026) shows that recovery is model-dependent and feedback-dependent: on tau²-bench Airline (50 tasks), GPT-4o pass rates improve from 0.36 to 0.48 (+33% relative) and GPT-5 from 0.68 to 0.70 (+3% relative) when symbolic guardrails block unsafe actions and provide informative error messages explaining which policy was violated. The paper explicitly states agents 'use this feedback to adjust its subsequent actions, retry with a safer alternative, and often complete the task successfully.' However, Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation — recovery is neither a first-class metric nor a dedicated research target. It provides no recovery-specific benchmark, no recoverable/unrecoverable task classification, no false recovery rate measurement, no recovery latency analysis, no path quality assessment, and no recovery-specific training method. Its finding that even GPT-4o still fails 52% of tasks after blocking, combined with the near-zero recovery of smaller models documented by The Verifier Tax, directly MOTIVATES our work: recovery happens partially and uncontrollably for frontier models, but remains an unsolved problem for smaller open-source models that need dedicated training.

(2) POST-HARM RECOVERY: After harm has occurred, the agent must remediate it. BackBench (arXiv 2604.18847, Apr 2026) provides 50 backtracking scenarios in OSWorld for computer-use agents, with a reward model trained on 1,150 pairwise human preference judgments, achieving +120 Elo improvement. Key differences from ours: (a) BackBench presupposes harm has occurred and must be undone; we presuppose harm was prevented; (b) BackBench operates in GUI/OS environments; we operate in tool-use API settings; (c) BackBench optimizes recovery quality via human preferences; we measure task completion, latency, path quality, AND recognition of unrecoverable scenarios.

(3) POST-INCIDENT RESPONSE: AIR (arXiv 2602.11749, Feb 2026) provides a DSL-based incident response framework achieving >90% detection, remediation, and eradication rates. Critically, AIR terminates the task after remediation — it does not attempt to resume and complete the original task via an alternative safe path.

(4) POST-ERROR RECOVERY: RAC (ACM CAIS 2026) provides log-based rollback for general execution errors on tau-bench/REALM-Bench. Fission-GRPO (Jan 2026) trains recovery from tool-calling errors via on-policy error augmentation (+5.7% recovery rate on BFCL v4). ToolMisuseBench (arXiv 2604.01508, Apr 2026) provides 6,800 tasks across CRUD/retrieval/file/scheduling environments with deterministic fault injection, measuring recovery quality and budgeted efficiency under explicit step/call/retry budgets — the operational-error counterpart to our safety-specific recovery benchmark. Its replayable fault injection methodology and budgeted efficiency metric S(k) are methodologically adjacent to our approach, but its faults are operational (schema drift, rate limits, authorization failures) rather than safety-policy violations. Hell or High Water (COLM 2025) evaluates recovery from environmental failures.

(5) GUARDRAIL-SIDE CORRECTION: Three distinct technical approaches exist for correcting unsafe actions at the guardrail level rather than training agent-side replanning:

(5a) ReGuard ('From Refusal to Recovery', arXiv 2510.13727, Oct 2025) learns a control-theoretic safety value function V(z) and fallback policy π_safe that INJECTS corrective actions when Q(z,a) ≤ 0 — the agent never replans, the guardrail replaces its unsafe action with a safe one. Evaluated on simulated driving (obstacle avoidance) and simple e-commerce (shopping cart budget constraints), not multi-step tool-use API settings with complex policy rules. Requires simulator access during guardrail training. Achieves 77.3% success vs 44.4% for myopic refusal, but proposes no recovery-specific benchmark.

(5b) AGENT-C ('Enforcing Temporal Constraints for LLM Agents', arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2) provides guardrail-side correction via constrained decoding: it translates temporal safety specifications into first-order logic and uses SMT solving to detect non-compliant tool calls during token generation, then leverages constrained generation to produce compliant alternatives. AGENT-C achieves 100% safety conformance while improving utility (Claude Sonnet 4.5: 71.8%→75.2%; GPT-5: 66.1%→70.6%). Unlike ReGuard's control-theoretic approach, AGENT-C operates at the token generation level via formal verification, but shares the same fundamental characteristic: the GUARDRAIL corrects the action rather than the AGENT learning to replan. For open-weight models it can enforce at fine-grained token level; for closed-source models at coarser call-level resampling.

(5c) Symbolic Guardrails' informative blocking feedback can be viewed as a lightweight guardrail-side intervention — by explaining policy violations, the guardrail provides implicit guidance toward safe alternatives, though without generating the corrective action itself.

Our work is complementary to all category (5) approaches: they improve guardrail correction capability; we improve agent replanning capability. The optimal deployment may combine both — a smarter guardrail (ReGuard/AGENT-C/Symbolic) paired with an agent trained to replan when guardrail-side corrections are insufficient or unavailable. Our ReGuard ablation directly tests this complementarity.

Additional relevant concurrent work: SafePred (Feb 2026) achieves 97.6% safety via predictive prevention with world models — prevents unsafe actions but does not address recovery. MOSAIC (Mar 2026) introduces Plan-Check-Act/Refuse with up to 50% harmful behavior reduction — evaluates refusal quality, not post-refusal replanning. SafeAgent (Apr 2026) mentions constrained replanning as a recovery mechanism but provides no disaggregated metrics for replanning success rate, recovery rate, or path quality — overall evaluation uses ASR and NRP without isolating replanning contribution. Mind the GAP (Feb 2026) demonstrates text safety does not transfer to tool-call safety, motivating tool-level guardrails. OpenAgentSafety (ICLR 2026) provides a comprehensive 350+ task evaluation framework for agent safety with real tools but focuses on risk evaluation, not recovery. ATBench (Apr 2026) benchmarks trajectory-level safety with 1,000 trajectories across 2,084 tools but evaluates safety detection, not recovery. ToolSafe (Jan 2026) guides agents toward safety-aware reasoning via pre-execution feedback (TS-Flow), reducing harmful tool invocations by 65% — closest to our setting in spirit, but operates as a guardrail providing preventive guidance rather than training recovery. TraceSafe (Apr 2026) reveals guardrail efficacy depends more on structural JSON parsing than semantic alignment. AgentSpec (ICSE 2026) provides a DSL-based runtime enforcement framework with >90% unsafe execution prevention — its constraint specification approach directly informs our Safety Recovery Simulator's alternative action enumeration. SafeAgentBench (Dec 2024) includes hazardous tasks with only 5-10% rejection rates, demonstrating that recognizing unrecoverable scenarios is itself a challenge.

## Approach
We construct RecoverBench by instrumenting tau-bench (Airline + Retail) with a guardrail intervention simulator that injects safety blocks at systematically varied trajectory points. The benchmark explicitly includes three task categories: (a) RECOVERABLE tasks where at least one safe alternative path exists (verified by oracle exhaustive search over constraint-satisfying action space), (b) CORRECTLY UNRECOVERABLE (CU) tasks where the user's request inherently requires a policy-violating action with no safe alternative (e.g., full refund on non-refundable ticket past cancellation window), and (c) PARTIALLY RECOVERABLE tasks where a degraded but safe version of the task can be completed (e.g., store credit instead of cash refund). We measure five metrics: Safe Recovery Rate (SRR: percentage of recoverable episodes where the agent finds an alternative safe path), False Recovery Rate (FRR: percentage of all episodes where the agent claims task completion but actually violates safety constraints via a DIFFERENT pathway than the blocked one — measuring constraint gaming/safety circumvention), Unrecoverable Recognition Rate (URR: percentage of CU episodes where the agent correctly identifies no safe path exists and gracefully informs the user), Recovery Latency (additional turns required after blocking for successful recoveries), and Alternative Path Quality (semantic similarity to optimal safe trajectories plus task reward preservation). The benchmark is explicitly designed to complement BackBench (post-harm, GUI/OS), AIR (post-incident, multi-domain), ToolMisuseBench (post-error, operational faults with deterministic replay), and RAC (post-error, general).

BLOCKING FEEDBACK DESIGN: Motivated by Symbolic Guardrails' finding that informative error messages (explaining which policy was violated and why) enable partial recovery in frontier models, RecoverBench systematically varies blocking feedback informativeness as an experimental condition: (i) MINIMAL feedback (action blocked, no explanation), (ii) POLICY-CITED feedback (action blocked + specific policy rule citation, matching Symbolic Guardrails' approach), and (iii) DIAGNOSTIC feedback (action blocked + policy citation + available alternative actions, matching our SRS training context). This enables measuring how feedback informativeness affects recovery across model capability levels, directly extending Symbolic Guardrails' implicit finding that informative feedback helps.

SAFETY RECOVERY SIMULATOR (SRS) SPECIFICATION: The SRS — the component that generates diagnostic context for RA-FGRPO training — operates through three modules: (1) CONSTRAINT EXTRACTION MODULE: Parses tau-bench's domain policy files (airline rebooking rules, retail return policies) to extract formal constraints as predicate functions, following AgentSpec's (ICSE 2026) trigger→predicate→enforcement pattern. Each constraint maps an action type to its validity conditions in the current environment state. (2) SAFE ALTERNATIVE ENUMERATOR: Given a blocked action and current state, queries the tau-bench API specification for all valid actions in the current state, filters out actions violating the triggered constraint or related constraints, and ranks remaining actions by semantic relevance to the original task intent (using embedding similarity between the blocked action's inferred goal and candidate action descriptions). For CU scenarios, returns an empty set. For partially recoverable scenarios, returns degraded alternatives with explicit quality annotations. (3) DIAGNOSTIC CONTEXT FORMATTER: Constructs augmented context as [trajectory_prefix; BLOCKED: action_name(args) → REASON: policy_rule_citation; AVAILABLE_ACTIONS: [ranked_action_list]; TASK_GOAL: original_user_request]. Critically, we provide WHICH actions are available but NOT which specific sequence solves the task — the agent must learn replanning, not memorize recovery templates. SRS validity is verified against oracle safe trajectories (computed offline via exhaustive search) to ensure enumeration completeness.

For training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO), adapting Fission-GRPO's on-policy error recovery augmentation for safety-specific guardrail interventions, with a tiered credit assignment strategy to mitigate dependency on any single unvalidated method. RA-FGRPO works as follows: (1) Standard GRPO exploration generates rollouts through guardrail-blocked scenarios on tau-bench; (2) The Safety Recovery Simulator intercepts blocked trajectories and augments them with diagnostic context from the three modules above; (3) Fission-based resampling generates G'=4 parallel recovery attempts from augmented contexts, creating dense on-policy training signal specifically for post-blocking adaptation; (4) PRIMARY CREDIT ASSIGNMENT: GTPO-based turn-level reward assignment (arXiv 2511.14846, Nov 2025, revised Apr 2026) provides fine-grained per-turn feedback with return-based advantage estimation and self-supervised reward shaping — adapted so the self-supervision signal comes from constraint compliance verification at each turn rather than code execution signals. GTPO is chosen as primary because: (a) it is the most established turn-level method (6+ months, revised), (b) it outperforms GRPO by 3.0% on multi-turn tool-integrated reasoning with negligible overhead, (c) its self-supervised reward shaping naturally adapts to safety constraint signals. FALLBACK CREDIT ASSIGNMENT: AT²PO-based tree-wise credit (arXiv 2601.04767, Jan 2026) serves as the validated fallback, using entropy-guided tree expansion for diverse recovery path exploration and recursive turn-wise value propagation — particularly suited when recovery requires exploring multiple branching alternatives. FUTURE EXTENSION: GAGPO's (arXiv 2605.13217, May 2026) critic-free grouped value proxy could further improve credit assignment if independently validated, but its requirement for exact textual state matching across rollouts needs adaptation for tool-use states (serialized API state + conversation history). We explicitly ablate all three credit assignment strategies.

We train open-source models (Qwen3.6-35B-A3B with 3B active parameters, Qwen3-4B) and evaluate across task complexity bins aligned with the Verifier Tax's horizon-dependent analysis. This model selection is directly motivated by the model-dependent recovery gap: Symbolic Guardrails shows frontier models (GPT-4o, GPT-5) partially recover with informative feedback, while The Verifier Tax shows open-source models (GPT-OSS-20B, GLM-4-9B) achieve near-zero recovery in complex scenarios — our training targets exactly this capability gap in open-source models. We additionally analyze how Canonical Path Deviation severity modulates recovery difficulty and whether RA-FGRPO helps agents re-anchor to canonical solution paths after guardrail intervention. A key ablation compares RA-FGRPO (with GTPO credit) against: vanilla GRPO, RA-FGRPO with AT²PO credit, RA-FGRPO with GAGPO credit (if feasible), offline DPO (DiaTool-DPO-style trajectory pairs), ToolSafe-style pre-execution safety feedback, and ReGuard-style guardrail-side correction (control-theoretic fallback policy). The ReGuard ablation is particularly important: it directly compares our agent-side replanning approach against guardrail-side action injection, testing whether the two are complementary. We also compare against frontier model baselines (GPT-4o, GPT-5) with Symbolic Guardrails-style informative blocking to establish the recovery ceiling that our training aims to approach for open-source models.

## Resource Estimate
{'manual': {'gpu_hours': '~1,100 H100 hours (benchmark construction with oracle trajectory computation: 250h, RA-FGRPO training with GTPO credit + online rollouts on 3B-35B MoE models: 450h, evaluation sweeps across complexity bins and feedback conditions: 200h, ablations including AT²PO/GAGPO credit + ReGuard comparison: 200h)', 'timeline': '14-16 weeks', 'estimated_gpu_cost': '$2,200 (H100 spot at ~$2/hr)'}, 'human_in_loop': {'gpu_hours': '~1,100 H100 hours (same compute, faster iteration on SRS design and CU scenario curation)', 'timeline': '10-12 weeks', 'claude_api_cost': '$300-500 (code generation for SRS modules, constraint extraction, trajectory analysis, paper drafting)', 'estimated_gpu_cost': '$2,200'}, 'auto_research': {'gpu_hours': '~1,500 H100 hours (additional hyperparameter exploration, Fission resampling sweeps, three-way credit assignment ablations, ReGuard comparison, oracle trajectory exhaustive search for CU validation, feedback informativeness sweeps)', 'timeline': '6-8 weeks', 'claude_api_cost': '$800-1,200 (end-to-end pipeline orchestration, automated ablation design, constraint extraction from tau-bench policies, SRS validation)', 'estimated_gpu_cost': '$3,000', 'speed_bottleneck': "GPU availability for concurrent RA-FGRPO online rollouts across model sizes; oracle safe trajectory computation for CU scenario validation; Fission resampling throughput (G'=4 parallel recovery attempts per blocked trajectory)"}}

## Inspired By
Field guide Section 7 (Defenses: guardrails, verification, monitoring) combined with Section 4.1 (pass@1 vs. production reliability gap). The Verifier Tax's quantitative evidence makes the gap between blocking success and task recovery concrete and measurable for open-source models, while Symbolic Guardrails reveals that recovery is model-dependent — frontier models partially recover with informative feedback, but smaller models cannot. This model-dependency motivates dedicated recovery training as the intervention point. The four-way taxonomy of recovery types (plus guardrail-side correction as a complementary paradigm) emerged from successive rounds of critical feedback, with the 'From Refusal to Recovery' and AGENT-C differentiation revealing that recovery requires distinguishing WHERE the intervention happens (guardrail vs. agent) and WHAT the intervention does (inject/constrain corrected action vs. replan). ToolMisuseBench's deterministic fault injection and budgeted efficiency metric inspired our benchmark design for replayability and efficiency measurement. The reviewer's 'correctly unrecoverable' insight led to the dual-challenge formulation (recover when possible, recognize impossibility when not), strengthening the benchmark's evaluative power. Fission-GRPO's on-policy error augmentation directly inspires our training approach; GTPO's turn-level reward assignment provides the primary credit mechanism; AT²PO's tree-based credit provides the validated fallback. Pattern: 'complementary gap-filling' with 'dual-challenge evaluation.'

## Target Venues
- EACL 2027 via ARR Aug 3, 2026 (commitment Oct 11, 2026 — primary target, 11 weeks for full RecoverBench + RA-FGRPO paper)
- AAAI 2027 (abstract Jul 21 / paper Jul 28, 2026 — parallel stretch goal, scoped to RecoverBench benchmark paper only, deferring RA-FGRPO training results to extended version)
- NAACL 2027 via ARR Oct-Nov 2026 (extended version with cross-benchmark comparison against BackBench/AIR/ToolMisuseBench and ReGuard complementarity analysis)

## Key References
- The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents (arXiv 2603.19328, Mar 2026)
- Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility (arXiv 2604.15579, Apr 2026)
- Enforcing Temporal Constraints for LLM Agents [AGENT-C] (arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2)
- From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails [ReGuard] (arXiv 2510.13727, Oct 2025)
- AIR: Improving Agent Safety through Incident Response (arXiv 2602.11749, Feb 2026)
- Human-Guided Harm Recovery for Computer Use Agents [BackBench] (arXiv 2604.18847, Apr 2026)
- Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors (arXiv 2601.15625, Jan 2026)
- ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery in Agentic Systems (arXiv 2604.01508, Apr 2026)
- Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization [GTPO] (arXiv 2511.14846, Nov 2025, revised Apr 2026)
- AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv 2601.04767, Jan 2026)
- GAGPO: Generalized Advantage Grouped Policy Optimization (arXiv 2605.13217, May 2026)
- SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (arXiv, Feb 2026)
- Learning When to Act or Refuse [MOSAIC] (arXiv, Mar 2026)
- SafeAgent: A Runtime Protection Architecture for Agentic Systems (arXiv 2604.17562, Apr 2026)
- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure (arXiv, Feb 2026)
- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents (arXiv 2602.16943, Feb 2026)
- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026)
- ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis (arXiv 2604.02022, Apr 2026)
- ToolSafe: Enhancing Tool Invocation Safety via Proactive Step-level Guardrail and Feedback (arXiv 2601.10156, Jan 2026)
- TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories (arXiv 2604.07223, Apr 2026)
- tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (ICLR 2025)
- AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents (ICSE 2026)
- Robust Agent Compensation (RAC) (ACM CAIS 2026)
- Hell or High Water: Evaluating Agentic Recovery from External Failures (COLM 2025)
- EmbodiedGovBench: Governance, Recovery, and Upgrade Safety in Embodied Agent Systems (arXiv, Apr 2026)
- DiaTool-DPO: Multi-Turn DPO for Tool-Augmented LLMs (SIGDIAL 2025, arXiv 2504.02882, Apr 2025)
- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv 2602.03025, Feb 2026)
- T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL (ICML 2026 Spotlight)
- SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents (arXiv 2412.13178, Dec 2024)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d1d477c8-b21a-41e7-8ec6-a0ea5cea2801",
  "type": "user",
  "uuid": "e1568f85-5639-4547-89c1-86cd84f248a8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:47:39.710Z_

```json
{
  "parentUuid": "e1568f85-5639-4547-89c1-86cd84f248a8",
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
  "uuid": "0c57b17f-f242-4c6d-8e43-cf480bdcc198",
  "timestamp": "2026-05-20T03:47:39.710Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:47:39.710Z_

```json
{
  "parentUuid": "0c57b17f-f242-4c6d-8e43-cf480bdcc198",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f00a7e80-d07f-423a-8b0f-51d7408d81f7",
  "timestamp": "2026-05-20T03:47:39.710Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient evidence to produce my evaluation. Let m…",
  "leafUuid": "f00a7e80-d07f-423a-8b0f-51d7408d81f7",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize post-blocking recovery benchmark reviews",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:48:07.815Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' evaluations carefully and produce a Meta Judge synthesis.

Let me extract the key information:

**Reviewer 1:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 32%] 中位 27%
- Key risks: Novelty insufficient (RA-FGRPO = Fission-GRPO domain adaptation), Trivial baseline threat (informative feedback + few-shot)


**Reviewer 2:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [22% - 33%] 中位 27%
- Key risks: Novelty distance problem (close to ToolMisuseBench/Fission-GRPO), Trivial alternative (informative feedback + ICL; AGENT-C)
**Reviewer 3:**
- Novelty: 中
- Significance: 中
- Related Work: 强
- Probability: [25% - 35%] 中位 28%
- Key risks: Method vs Benchmark distinction

, Trivial alternative (diagnostic feedback alone)

The three median probabilities cluster tightly around 27-28% with minimal variance, showing strong agreement across reviewers. Looking at the consensus, all three reviewers converge on medium novelty and significance ratings. They acknowledge the benchmark addresses a genuine gap, but note that the core technical contribution—adapting Fission-GRPO to this domain—is incremental. The conceptual framing through taxonomy and dual-challenge structure adds some value, though the technical novelty remains limited. On significance, reviewers agree the problem matters but the scope is narrow, confined to just two domains in tau-bench, and the main finding lacks surprising insights.

The related work section stands out as a genuine strength with comprehensive coverage and an authentic five-category taxonomy. However, all three reviewers flag a critical vulnerability: a simpler baseline of informative feedback plus prompting without RL training could potentially achieve similar results, especially given that Symbolic Guardrails already demonstrated a 33% improvement for GPT-4o using just informative feedback. The RA-FGRPO mechanism itself is largely unchanged from Fission-GRPO—only the domain-specific context formatting differs. Most tellingly, reviewers 2 and 3 explicitly note the core finding feels predictable, with reviewer 1 implying the same concern.

The three reviewers show remarkable alignment across all dimensions, with a standard deviation around 0.58%—essentially the strongest convergence possible. Their probability estimates cluster tightly around 27-28%, with ranges of [22-32], [22-33], and [25-35] respectively. Given this consistency, I should narrow toward the median with a final estimate that respects the most lenient reviewer's upper bound of 35%.

I'm settling on [23% - 32%] with a median of 27%, then moving on to compile the implementation assessment from the resource estimates and reviewer feedback.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f00a7e80-d07f-423a-8b0f-51d7408d81f7",
  "isSidechain": false,
  "requestId": "req_011CbD8rMQJMLNBqKfKZ8gHy",
  "type": "assistant",
  "uuid": "d881bc48-3579-41bd-be75-1280be3d157a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGxxvoUHTcbCJFypzct8Ly",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27582,
      "cache_read_input_tokens": 11374,
      "output_tokens": 2949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2949,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 27582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27582
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

_source line 9 · 2026-05-20T03:48:49.087Z_

【阶段】: Meta Judge
【三次中位】: [27%, 27%, 28%]  std=0.6%
【共识维度】: 
- **Novelty = 中**（3/3 一致）：benchmark 填补了 post-blocking recovery 这一真实 gap，five-category taxonomy 和 dual-challenge formulation 有概念贡献；但 RA-FGRPO 是 Fission-GRPO 的 domain adaptation，技术方法论 novelty 有限
- **Significance = 中**（3/3 一致）：问题真实重要（Verifier Tax 数据有说服力），但 scope 窄（tau-bench 2 domains）、核心发现的 surprise factor 低（"training helps small models recover" 是可预测结论）
- **Related Work = 强**（3/3 一致）：覆盖面、准确性、差异化定位均为一流水平，five-category taxonomy 本身是贡献
- **Trivial alternative 威胁**（3/3 一致）：informative blocking feedback + prompting（不做 RL 训练）可能已经大幅提升 recovery，Symbolic Guardrails 已证明 +33% relative improvement for GPT-4o，若 prompting baseline 已够用则 RA-FGRPO 增量价值被严重削弱
- **RA-FGRPO 增量有限**（3/3 一致）：核心机制（fission + diagnostic context + resampling）不变，Safety Recovery Simulator 相对 Error Simulator 主要是 domain-specific context formatting，不是方法论创新
- **"I would have guessed this" 风险**（2/3 明确提及，第 3 位隐含）：positive result 是 confirmatory 而非 surprising

【异常维度】: 
- R1 特别强调 SafeAgent constrained replanning 作为最接近竞争者 → 合理补充但不改变整体判断
- R2 特别强调 AGENT-C 作为 trivial alternative（guardrail-side correction 使 agent-side training 不必要）→ 被 R1/R3 的 trivial alternative 讨论部分涵盖，属于同一类威胁的不同实例
- R3 单独提出 "Method vs Benchmark 张力" 作为常见 borderline rejection pattern → 是对 Novelty 中判断的具体化阐释，非独立维度

【最终概率】: [23% - 32%] 中位 27%
【一致性】: 高（std=0.6%，三份评审在所有 rubric 维度判决完全一致）
【综合理由】: 
三份评审呈现罕见的高度一致：rubric 三维度判决完全相同（中/中/强），概率估计几乎重合（27%/27%/28%），核心风险识别高度重叠。这种一致性赋予结论很高的置信度。

**概率锚定在 27% 的核心逻辑：**
1. **Novelty 和 Significance 双中等构成天花板**：三位审稿人均认为 benchmark 贡献真实但 training method 是 incremental adaptation，核心发现方向可预测。Novelty+Significance 双中在 EMNLP 通常对应 borderline-reject 区间（25-35%），无 surprising insight 设计则偏下半区。
2. **Related Work 强不能弥补 Novelty 中**：Related Work 是必要条件非充分条件，三位审稿人均持此判断。优秀的 related work 保障了下限（不会低于 22-23%），但不能推高上限。
3. **Trivial alternative 是最大系统性风险**：三位审稿人不约而同指出同一威胁——informative feedback + prompting 作为零训练 baseline 可能已足够好。这不是实验能否做好的问题，而是 idea 立意层面的风险：如果实验发现 feedback level 是主要 driver 而非 training method，paper 的核心 story 会 collapse。
4. **上界 32% 而非更高**：R3 给出 35% 上界但 R1/R2 为 32-33%，高一致性下取偏保守端，且三位均未识别出任何可能推高到 35%+ 的 upside scenario。
5. **下界 23%**：benchmark 填补真实 gap + dual-challenge 设计 + FRR 指标的原创性保障了一个 solid 的下限，即使 method 部分完全被视为 incremental。

【建议】: 不推荐（中位 27% < 36% 阈值，且三审高度一致无上调空间，但 idea 立意方向合理、不构成 KILL，可通过迭代优化尝试提升）

【实施评估】:
- **计算资源**: ~1,100-1,500 H100 GPU hours（含 benchmark oracle trajectory computation 250h、RA-FGRPO 训练 450h、评估和消融 200-400h），约 $2,200-3,000 spot pricing。属于中等规模，对有 GPU 资源的实验室可行。
- **数据需求**: 基于 tau-bench（ICLR 2025，公开可得）的 Airline + Retail 两个 domain。需要自行构建 guardrail injection 和 oracle safe trajectory，但底层数据公开。不需要私有数据。
- **人工介入**: SRS 模块中的 constraint extraction 需要对 tau-bench policy rules 进行人工解析和形式化；CU（correctly unrecoverable）场景的 curation 需要人工验证。估计 2-4 人周的专家标注/验证工作。
- **训练需求**: 需要对 Qwen3.6-35B-A3B（3B active）和 Qwen3-4B 进行 RL 训练（RA-FGRPO）。训练规模可控（3-4B active params），但 on-policy rollout + fission resampling（G'=4）的吞吐量是瓶颈。
- **新 Benchmark**: 是，RecoverBench 是核心贡献之一。需要在 tau-bench 上构建 guardrail injection layer + 三类场景分类 + 五个评估指标。构建周期约 4-6 周。
- **预估周期**: 10-16 周（取决于自动化程度），目标投稿 ARR Aug 2026 或 AAAI 2027。时间线紧但技术上可行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d881bc48-3579-41bd-be75-1280be3d157a",
  "isSidechain": false,
  "requestId": "req_011CbD8rMQJMLNBqKfKZ8gHy",
  "type": "assistant",
  "uuid": "50e83da5-277e-4d21-a4bf-13c232e3b34f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGxxvoUHTcbCJFypzct8Ly",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 27582,
      "cache_read_input_tokens": 11374,
      "output_tokens": 2949,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2949,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 27582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27582
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient evidence to produce my evaluation. Let m…",
  "leafUuid": "50e83da5-277e-4d21-a4bf-13c232e3b34f",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize post-blocking recovery benchmark reviews",
  "sessionId": "d4e28f65-4760-47a6-b10d-e8880e3c757c"
}
```

---
