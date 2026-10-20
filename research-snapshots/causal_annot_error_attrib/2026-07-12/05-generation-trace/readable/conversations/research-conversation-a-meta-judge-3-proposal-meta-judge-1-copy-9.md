# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/ec86b9d5-60f3-40aa-8a7e-07272460d8cf.jsonl`
- **Structured JSON:** [`1230c7d9a6d46b7e8069.json`](../../sessions/12/1230c7d9a6d46b7e8069.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:32:00.901Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:32:00.901Z",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have enough research to produce a thorough, evidence-based assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【致命前置问题：投稿目标与 Proposal 内容严重不匹配】\n\n本 Proposal 的投稿目标被指定为 **CoRL 2026**（Conference on Robot Learning），但 Proposal 内容与 CoRL 的 scope 完全不匹配：\n\n- **CoRL 明确要求**：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics\" 以及 \"Submissions without a robotics focus will be returned without review\"（来源：CoRL 2026 Call for Papers, corl.org）\n- **本 Proposal 的实际内容**：text-based LLM agent safety，基于 tau-bench（Airline/Retail 客服场景），评估 agent 在 guardrail 阻断后的 tool-use replanning 能力\n- **Proposal 自身列出的 target venues**：EACL 2027, AAAI 2027, NAACL 2027 — 全部是 NLP/AI 会议，无一提及 CoRL\n- **Proposal 无任何 robotics 内容**：没有 real-robot 实验、没有 sim-to-real、没有 embodied agent、没有物理世界交互\n\n**结论：提交至 CoRL 2026 几乎必然 desk rejection（未进审稿即退回）。** 中稿概率约为 0-2%，与 idea 质量无关，纯粹是 scope mismatch。\n\n以下评估将忽略 venue mismatch，聚焦于 idea 本身的质量，以便判断其在 **适配 venue**（如 EACL/AAAI/NAACL/EMNLP/ACL）的潜力。\n\n---\n\n【领域调研】:\n\n- **[The Verifier Tax](https://arxiv.org/abs/2603.19328)** (arXiv, Mar 2026): 本 proposal 的核心动机论文。量化了 runtime safety enforcement 对 task completion 的影响：94% 阻断率但 SSR < 5%，recovery rate 从 21%（Airline）到 ~0%（Retail）。论文本身并未将 recovery 作为研究目标，而是作为 verifier tax 的一个副产品记录。**与 proposal 的关系：提供了 motivating evidence，但未提供 recovery 的 benchmark 或训练方法。**\n\n- **[Symbolic Guardrails](https://arxiv.org/abs/2604.15579)** (arXiv, Apr 2026, CMU): 在 tau²-bench 上评估 symbolic guardrails，发现 informative error messages 使 GPT-4o pass rate 从 0.36 提升到 0.48。**关键发现：recovery 是 model-dependent，frontier models 能部分 recover，smaller models 不能。但 recovery 不是该论文的研究目标，只是 side observation。**\n\n- **[Fission-GRPO](https://arxiv.org/abs/2601.15625)** (arXiv, Jan 2026): 针对 tool-calling error recovery 的 RL 训练方法，通过 on-policy error augmentation + diagnostic feedback 提升 Qwen3-8B 的 error recovery rate +5.7%。**与 proposal 的关系：RA-FGRPO 直接基于此方法，从 \"operational error recovery\" 适配到 \"safety-specific recovery\"——这是一个相对 incremental 的适配。**\n\n- **[BackBench](https://arxiv.org/abs/2604.18847)** (arXiv, Apr 2026): 50 个 post-harm recovery scenarios in OSWorld。**与 proposal 的关系：proposal 正确区分了 post-harm recovery (BackBench) 与 post-blocking recovery (theirs)，但这也暴露了 post-blocking 是一个更窄的 sub-problem。**\n\n- **[GTPO](https://arxiv.org/abs/2511.14846)** (arXiv, Nov 2025): Turn-level reward assignment for multi-turn tool-integrated reasoning，+3.0% over GRPO。**与 proposal 的关系：被选为 RA-FGRPO 的 primary credit assignment 方法。**\n\n- **[ToolMisuseBench](https://arxiv.org/abs/2604.01508)** (arXiv, Apr 2026): 6,800 tasks with deterministic fault injection for tool misuse and recovery。**与 proposal 的关系：operational-error counterpart。ToolMisuseBench 已经覆盖了 \"recovery after tool failure\" 的 benchmark 维度；proposal 的增量是 \"safety policy violation\" 而非 \"operational failure\" 作为 trigger。**\n\n- **[Canonical Path Deviation](https://arxiv.org/abs/2602.19008)** (arXiv, Feb 2026): Off-canonical actions compound subsequent deviation by 22.7pp。**与 proposal 的关系：为 recovery difficulty 提供了理论解释——被 block 后偏离 canonical path，后续 recovery 概率急剧下降。**\n\n- **[AIR](https://arxiv.org/abs/2602.11749)** (arXiv, Feb 2026): Post-incident response framework, >90% remediation success. **与 proposal 的关系：不同 recovery 范式，AIR 终止任务而非 resume。**\n\n- **调研总结**：Agent safety 的 benchmark 和 guardrail 研究在 2025-2026 年爆发式增长，但 **post-blocking recovery（guardrail 成功阻断后 agent 的 replanning 能力）确实是一个尚无专门 benchmark 和训练方法的 gap**。最接近的工作是 Fission-GRPO（operational error recovery）和 Symbolic Guardrails（观测到 recovery 但未专门研究）。该 gap 的真实存在性是可信的。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在 trivial alternative 威胁，但 proposal 有部分回应。**\n\n最显然的 trivial baseline：**给 smaller model 提供 informative error messages + few-shot recovery demonstrations（in-context learning）**。Symbolic Guardrails 已经表明 informative feedback 能使 GPT-4o 从 0.36→0.48（+33% relative）。如果对 smaller models 也 simply 提供 rich error context + 几个 recovery 示例，是否就能 close 大部分 gap？\n\nProposal 的隐含回应是：(a) smaller models（GPT-OSS-20B, GLM-4-9B）即使有 blocking 也 near-zero recovery，说明 informative feedback alone 不够；(b) 需要专门的 RL 训练。但这个论证有漏洞——**The Verifier Tax 测试的 smaller models 是否收到了 informative feedback？如果没有，那 \"informative feedback + ICL for smaller models\" 这个 baseline 就尚未被排除。** 如果这个 trivial baseline 就能 close 大部分 gap，则 RA-FGRPO 的增量价值大打折扣。\n\n**增量价值的核心在于**：(1) RecoverBench 作为专门 benchmark 的系统化评测（包括 CU 识别），(2) RA-FGRPO 相对于 informative-feedback-only 的训练增益。如果后者的增益不显著，论文会变成一个 benchmark-only paper。\n\n---\n\n【前提假设检验】:\n\n核心逻辑链中有以下未验证假设：\n\n1. **\"Recovery failure 主要是 safety-specific 的，而非 general capability 不足\"**：这是最关键的假设。Smaller models 的 near-zero recovery 可能不是因为缺乏 safety-specific recovery training，而是因为这些模型在 multi-step planning 上本身就弱。如果是后者，safety-specific 训练（RA-FGRPO）可能不比 general capability 提升更有效。Proposal 没有提供区分这两个原因的证据。\n\n2. **\"Fission-GRPO 从 operational errors 到 safety policy violations 的迁移是 straightforward 的\"**：Proposal 将 Fission-GRPO 的 error augmentation 框架直接搬到 safety context，但 safety violations 与 operational errors 有本质区别——safety violations 涉及 policy interpretation、constraint satisfaction、multi-hop reasoning about what IS and ISN'T allowed，比 \"API returned error code\" 复杂得多。这个迁移的有效性是假设的。\n\n3. **\"Oracle exhaustive search 在 tau-bench 上可行\"**：CU/partially-recoverable 分类依赖于 \"oracle exhaustive search over constraint-satisfying action space\"，但 tau-bench 的 action space 是否小到可以穷举？如果不可以，benchmark 的 ground truth 就不可靠。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   核心 novelty 在于识别并形式化 \"post-blocking recovery\" 作为一个 distinct failure mode，与 post-harm (BackBench)、post-error (Fission-GRPO/ToolMisuseBench)、post-incident (AIR)、guardrail-side correction (ReGuard/AGENT-C) 进行系统化区分。这个 taxonomy 和 gap identification 是有价值的。RecoverBench 的 dual challenge（recover + recognize unrecoverability）增加了评估深度。\n\n   **但 novelty 受限于两点**：(a) 训练方法 RA-FGRPO 是 Fission-GRPO 的直接适配，核心创新（on-policy error augmentation + diagnostic feedback）来自 Fission-GRPO，credit assignment 来自 GTPO/AT²PO——proposal 的方法贡献更多是 **组合** 而非 **创造**；(b) benchmark 构建方法（在 tau-bench 上注入 blocks + 分类 recoverable/unrecoverable）是 relatively mechanical 的——ToolMisuseBench 在 operational domain 已经展示了类似的 deterministic fault injection methodology。\n\n   如果核心发现是 positive（RA-FGRPO 提升 recovery），审稿人的反应更可能是 \"makes sense, I would have guessed that safety-specific training helps\" 而非 \"surprising\"。\n\n2. **Significance: 中** — \n   Agent safety 是一个重要且时效性强的方向。Post-blocking recovery 确实是一个 practical problem：如果 guardrails 阻断 unsafe actions 但 agent 无法完成 legitimate tasks，guardrails 的 deployment value 就会受到质疑（The Verifier Tax 的核心论点）。\n\n   **但 significance 受限于**：(a) 问题的范围较窄——只关注 tau-bench（Airline/Retail），generalizability 到其他 domain 未知；(b) 对 NLP/agent 社区的影响取决于 \"recovery 是否真的需要 safety-specific 训练\"——如果答案是 \"general capability 提升就够了\"，则 significance 大打折扣；(c) 实际影响路径不完全清晰——production 系统中 guardrail + agent 的 co-design 是一个工程问题，academic benchmark 能多大程度指导实践存疑。\n\n3. **Related Work: 强** — \n   这是 proposal 最出色的维度。Proposal 对相关工作的覆盖非常系统化和全面：五类 recovery paradigm 的分类清晰且有依据，每篇论文的定位和差异化描述准确（经我调研验证，引用的关键论文均真实存在且描述基本准确）。Canonical Path Deviation、TraceSafe、ToolSafe 等论文的引用体现了对领域的深度理解。与 ToolMisuseBench 的 \"operational vs safety\" 区分、与 ReGuard/AGENT-C 的 \"guardrail-side vs agent-side\" 区分、与 BackBench 的 \"post-harm vs post-blocking\" 区分都是准确且有说服力的。\n\n---\n\n【概率估计】（针对适配 venue 如 EACL/AAAI/NAACL/ACL）: [22% - 32%] 中位 27%\n\n【概率估计】（针对用户指定的 CoRL 2026）: [0% - 3%] 中位 1%\n   — CoRL 明确要求 robotics focus，本 proposal 零 robotics 内容，几乎必然 desk rejection。\n\n【估计理由】:\n\n针对适配 NLP/AI venue 的估计（27%）：\n- Related Work 是强项，表明作者对领域有深刻理解，这在审稿中会加分\n- Gap identification 是真实的——post-blocking recovery 确实没有专门的 benchmark 和训练方法\n- **Novelty（中）是上界限制因素**：核心方法贡献是组合式的（Fission-GRPO + GTPO + tau-bench + safety context），审稿人可能认为 methodological novelty 不足。如果 RA-FGRPO 的实验结果只是 modest improvement（类似 Fission-GRPO 的 +5.7%），paper 的 impact 会进一步受限\n- **Trivial alternative 威胁真实存在**：如果 \"informative feedback + ICL\" 就能 close 大部分 gap for smaller models，RA-FGRPO 的必要性会被质疑。这需要在实验中明确排除\n- 概率落在 25-35% 区间（\"有实质内核，但核心发现 if positive 审稿人会说 'I would have guessed this'\"）的下半段\n\n针对 CoRL 的估计（1%）：纯 venue mismatch，与 idea 质量无关。\n\n【主要风险】:\n\n1. **\"是 safety-specific 问题还是 general capability 问题？\"** — 如果审稿人认为 smaller models 的 recovery failure 本质上是 multi-step planning 能力不足（而非缺乏 safety-specific recovery training），则整个 training contribution 的立论基础会被动摇。这是最致命的 idea-level 风险。\n\n2. **方法 novelty 不足** — RA-FGRPO = Fission-GRPO（已发表）+ GTPO credit（已发表）+ safety context（domain adaptation）。审稿人可能判定这是 \"engineering contribution\"（将现有方法 apply 到新 domain）而非 \"methodological contribution\"。如果是 benchmark-only paper（RecoverBench），则 benchmark 的规模（仅 tau-bench 的 Airline + Retail 两个 domain）和 task diversity 可能被认为不足。\n```\n\nSources:\n- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)\n- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)\n- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)\n- [BackBench (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)\n- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)\n- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/abs/2604.01508)\n- [Canonical Path Deviation (arXiv 2602.19008)](https://arxiv.org/abs/2602.19008)\n- [AIR (arXiv 2602.11749)](https://arxiv.org/abs/2602.11749)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328) (Mar 2026): \n   验证了 runtime safety enforcement 对 task completion 的代价。GPT-OSS-20B/GLM-4-9B 在 tau-bench 上 SSR<5%，recovery rates 21%→~0%。论文存在且核心数据与 proposal 描述一致。这是 proposal 的主要 motivation source。\n\n2. [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579) (Apr 2026): \n   对 80 个 agent safety benchmark 做 systematic review，评估 symbolic guardrails 对 safety/utility 的影响。GPT-4o 在 informative blocking feedback 下 pass rate 0.36→0.48。关键点：该论文**已经隐式测量了 recovery**（pass rate improvement IS recovery），只是未将其作为 first-class metric。Proposal 的核心 novelty claim（\"no existing work isolates post-blocking recovery\"）需要相对于这篇论文 justify 增量。\n\n3. [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625) (Jan 2026): \n   on-policy error augmentation 训练 tool-calling error recovery，Qwen3-8B recovery rate +5.7%。proposal 的 RA-FGRPO 本质上是 Fission-GRPO 在 safety domain 的 adaptation + GTPO credit assignment。方法论上的增量有限。\n\n4. [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/pdf/2604.01508) (Apr 2026): \n   6800 tasks，deterministic fault injection，budgeted efficiency metric。Proposal 承认与其 \"methodologically adjacent\"，区别仅在 fault 类型（operational vs. safety-policy）。这意味着 proposal 的 benchmark design 在结构上与 ToolMisuseBench 高度重叠，区别仅在于 inject 的是 safety block 而非 operational error。\n\n5. [Recovery-Bench (Letta, OpenReview)](https://openreview.net/forum?id=8FZRnDgDxq) (2026): \n   **Proposal 完全未引用的直接竞争工作。** Recovery-Bench 测量 agent 从 mistakes 和 corrupted context 中的恢复能力。虽然不聚焦 safety，但在 \"agent recovery benchmark\" 这个 niche 上直接竞争。GPT-5 在 recovery 场景表现显著不同于 clean 场景。\n\n6. [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738) (Dec 2025, ICLR 2026 Workshop): \n   guardrail-side correction via constrained decoding，100% safety conformance + utility improvement。Proposal 将其归为 \"complementary\"，但审稿人可能会问：如果 guardrail 能直接生成 compliant alternative（AGENT-C 的做法），为什么还需要训练 agent 做 recovery？\n\n7. [BackBench (arXiv 2604.18847)](https://arxiv.org/html/2604.18847v1) (Apr 2026): \n   50 post-harm recovery scenarios in OSWorld。Proposal 对其定位清晰（post-harm vs. post-blocking），差异化成立。\n\n8. [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846) (Nov 2025, revised Apr 2026): \n   turn-level reward assignment，+3.0% over GRPO。Proposal 将其用作 primary credit assignment，但 GTPO 本身并非 safety-aware，adaptation 的技术贡献不明确。\n\n9. [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): \n   **CoRL 2026 明确要求 \"focus on a core robotics problem\" 和 \"real-robot experiments or convincing evidence that simulation experiments are transferable to real robots\"。** Topics 包括 robot manipulation, navigation, locomotion, driving, flight — 全部是物理机器人学习。\n\n- **调研总结**: Agent safety recovery 是 2026 上半年的活跃研究方向，已有多个 benchmark（ToolMisuseBench、Recovery-Bench、BackBench）和训练方法（Fission-GRPO、GTPO）覆盖了不同方面。Proposal 的定位是在 \"post-blocking\" 这个细分 niche 填补空白，但该 niche 与 \"post-error recovery\" 的边界较模糊。**最关键的问题是：这是一个 NLP/agent safety proposal，与 CoRL（机器人学习会议）的 scope 完全不匹配。**\n\n\n【⚠️ 致命问题：venue mismatch】\n\n在进入 3 维度评估之前，必须指出一个**与 idea 质量无关但对中稿概率有决定性影响的事实**：\n\n**这个 proposal 与 CoRL 2026 的 scope 完全不匹配。**\n\n- CoRL 要求 \"submissions should focus on a core robotics problem\"\n- CoRL 要求 \"real-robot experiments or convincing evidence of sim-to-real transfer\"\n- CoRL 的 topics 包括 manipulation, navigation, locomotion, driving, flight — 全部是物理机器人\n- 本 proposal 是关于 text-based customer service agent（tau-bench Airline/Retail）的 tool-use safety recovery，无任何物理机器人组件\n- Proposal 自身列出的 target venues 也是 EACL/AAAI/NAACL（NLP venues），进一步证实 scope 不匹配\n\n**这不是 idea 质量问题，是 scope 问题。** CoRL 的 area chair 极大概率会在 desk review 阶段直接拒稿，甚至不进入 peer review。\n\n以下 3 维度评估基于 idea 本身的学术质量（而非 venue fit），但概率估计会反映 CoRL 的 scope 要求。\n\n\n【Trivial Alternative 检验】:\n\n存在多个成本更低的替代方案：\n\n1. **Prompt engineering / few-shot recovery demos**: 在 blocking message 中附上 few-shot 示例，教 agent 如何 replan。不需要任何训练。Symbolic Guardrails 已经证明 informative feedback 能将 GPT-4o pass rate 提升 33%，说明很大一部分 recovery 问题可以通过更好的 feedback 信息解决，而不需要 dedicated training。\n\n2. **Guardrail-side correction（AGENT-C）**: 直接在 guardrail 层面生成 compliant alternative，agent 完全不需要 replan。AGENT-C 已经实现 100% safety + utility improvement。如果 guardrail 能直接修正 action，为什么要训练 agent 自己做 recovery？Proposal 称 \"complementary\"，但缺乏证据说明在什么场景下 guardrail-side correction 不够用。\n\n3. **直接在 Fission-GRPO 训练中 inject safety blocks**: 把 safety blocks 作为 error 的一个子类型，直接复用 Fission-GRPO 的 pipeline。不需要设计新的 RA-FGRPO。\n\n增量价值主要在于：(a) \"correctly unrecoverable\" 场景的识别，(b) False Recovery Rate 指标（检测 constraint gaming）。这两点确实是 trivial alternatives 无法覆盖的，是 proposal 的真正 delta。但这个 delta 是否足以支撑一整篇论文，值得商榷。\n\n\n【前提假设检验】:\n\n核心逻辑链中有以下未验证假设：\n\n1. **\"Post-blocking recovery 是 agent 缺乏的一种 distinct skill，需要 dedicated training\"**: 这是最核心的假设。替代假设是 recovery 能力随 general reasoning 能力自然提升（GPT-5 的 recovery 比 GPT-4o 好就暗示了这一点），不需要 dedicated training。Proposal 没有排除这个替代假设。\n\n2. **\"Open-source models 的 recovery gap 主要源于缺乏 safety-specific recovery training signal\"**: 替代解释是 open-source models 的 general instruction following 和 reasoning 能力不足（The Verifier Tax 提到 SSR<5% 本身可能反映 general capability gap）。如果根本原因是 general capability，safety-specific training 不会有效。\n\n3. **\"在 tau-bench Airline/Retail 上的 recovery improvement 可以 generalize 到其他 domains\"**: Proposal 只在两个 customer service domain 上构建 benchmark 和训练。Recovery 在这些特定 domain 的 improvement 可能高度 domain-specific（利用特定 airline/retail policy 结构），不一定 generalize。\n\n4. **\"SRS 的 safe alternative enumeration 不会 leak oracle information\"**: Proposal 声称 \"we provide WHICH actions are available but NOT which specific sequence solves the task\"，但在 tau-bench 这种 constrained environment 中，available actions list 本身可能就高度 informative（等价于严重 hint），使得训出来的 recovery 能力是 benchmark-specific 的，而非 generalizable 的。\n\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n\n   核心 insight（\"agent 需要在 guardrail block 后 recover\"）虽然在 framing 上是新的，但本质上与 post-error recovery（Fission-GRPO, ToolMisuseBench）高度类似。剔除 surface differences 后，novelty delta 主要集中在两点：(a) \"correctly unrecoverable\" 分类和 URR 指标，(b) False Recovery Rate 检测 constraint gaming。这两点有真实价值，但不足以支撑 \"strong novelty\" 的 claim。\n\n   具体对比：\n   - vs. Fission-GRPO：RA-FGRPO ≈ Fission-GRPO + GTPO credit + safety-specific blocks。方法论增量有限。\n   - vs. ToolMisuseBench：RecoverBench ≈ ToolMisuseBench 的 benchmark design paradigm + safety blocks instead of operational faults。\n   - vs. Symbolic Guardrails：Recovery measurement ≈ Symbolic Guardrails 的 pass rate delta 的更细粒度版本。\n   - vs. Recovery-Bench (Letta)：在 \"agent recovery benchmark\" 这个 niche 上直接竞争，且 proposal 未引用。\n   \n   Proposal 的 taxonomy（5 种 recovery 类型）是有组织价值的，但 taxonomy 本身不算 technical novelty。\n\n2. **Significance: 弱-中** — \n\n   对 NLP/agent safety 社区：问题是真实的（agents 确实在 block 后 recovery 困难），但研究的 scope 非常窄（只在 tau-bench 两个 domain，只针对 open-source models），实际影响力有限。更重要的是：如果 base model capability 是 recovery 的主要瓶颈（GPT-5 > GPT-4o > open-source 的梯度暗示了这一点），那么 dedicated recovery training 可能很快被更强的 base models 淘汰。\n   \n   对 CoRL/robotics 社区：**零相关性**。Proposal 不涉及任何物理机器人、embodied agent、sim-to-real transfer、manipulation/navigation/locomotion。tau-bench 的 Airline/Retail domain 是纯文本客服场景。\n\n3. **Related Work: 强（对 NLP venues）/ 致命（对 CoRL）** — \n\n   Proposal 对 NLP agent safety 领域的 related work 覆盖极其充分（30+ 引用），taxonomy 清晰，差异化定位 well-articulated。唯一的显著遗漏是 Letta 的 Recovery-Bench。\n   \n   但对 CoRL 而言，related work 完全没有涉及 robotics recovery literature（如 robot error recovery, manipulation failure recovery, safe RL for robotics），这进一步暴露了 venue mismatch。\n\n\n【概率估计】: [1% - 5%] 中位 2%\n\n【估计理由】: \n\n**概率极低的决定性因素不是 idea 质量，而是 venue scope mismatch。** \n\nCoRL 2026 明确要求 \"focus on a core robotics problem\" 和 real-robot experiments。本 proposal 是一个纯 NLP/agent safety 工作（text-based customer service tool-use），与机器人学习完全无关。极大概率在 desk review 阶段被拒，甚至不进入 peer review。\n\n如果假设投稿到 proposal 自身列出的 NLP venues（EACL/AAAI/NAACL via ARR），idea 质量的概率估计会在 **[18% - 30%] 中位 22%** 的范围——idea 方向站得住脚但内核偏薄：novelty delta 有限（safety-specific recovery vs. general error recovery 的边界模糊），存在 trivial alternative 威胁（guardrail-side correction, better prompting），核心前提假设（recovery 需要 dedicated training 而非 general capability improvement）未经验证。即便在 NLP venues，审稿人看到 positive results 可能会说 \"makes sense, I would have guessed that training on recovery would help recovery\"，而不是 \"surprising\"。\n\n【主要风险】:\n\n1. **CoRL 投稿：Desk reject due to scope mismatch（致命风险）** — 这是一个纯文本 tool-use agent safety 的工作，CoRL 不接收此类论文。Proposal 自身的 target venues 也没有列 CoRL，列的是 EACL/AAAI/NAACL。建议投稿到 NLP 或 AI safety venues。\n\n2. **即便换到 NLP venues：Core novelty 被 challenge** — 审稿人很可能提出 \"post-blocking recovery 与 post-error recovery 有什么本质区别？为什么不直接扩展 Fission-GRPO / ToolMisuseBench？\" 以及 \"AGENT-C 这样的 guardrail-side correction 能否直接解决你的问题，不需要 agent-side training？\" 这两个问题 proposal 目前的回答不够有力。\n```\n\n---\n\n**补充说明**：\n\n本 proposal 的形式完善度极高——30+ 引用、5 种 recovery 类型 taxonomy、5 个评估指标、tiered credit assignment、详细 ablation plan。但形式完善度不等于 idea 质量。透过形式看：核心发现如果是 positive（\"safety-specific recovery training 提升了 open-source models 的 recovery rate\"），审稿人的反应更可能是 \"I would have guessed this\" 而非 \"surprising\"。\n\n**对后续流程的建议**：如果要继续审，应首先确认 venue 选择——投 CoRL 几乎可以确定被拒。如果改投 NLP venues，idea 有一定潜力但需要发掘 agent 帮助强化 core novelty delta（特别是 \"correctly unrecoverable\" recognition 和 False Recovery Rate 这两个真正有新意的点），同时补救 agent 需要解决 trivial alternative 威胁和核心前提假设问题。\n\nSources:\n- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)\n- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)\n- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)\n- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/pdf/2604.01508)\n- [Recovery-Bench (OpenReview)](https://openreview.net/forum?id=8FZRnDgDxq)\n- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)\n- [BackBench (arXiv 2604.18847)](https://arxiv.org/html/2604.18847v1)\n- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [tau-bench (arXiv 2406.12045)](https://arxiv.org/abs/2406.12045)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题：venue 匹配性】\n\n本 proposal 投稿目标是 CoRL 2026（Conference on Robot Learning）。然而：\n\n1. CoRL 2026 CFP 明确声明：\"submissions without a robotics focus will be returned without review\"。\n2. 本 proposal 的全部内容是 LLM agent 在 airline/retail 客服场景中的 tool-use 安全恢复——没有任何机器人操控、导航、感知、仿真迁移、物理交互等 robotics 内容。\n3. Proposal 自身列出的 Target Venues 是 EACL 2027、AAAI 2027、NAACL 2027——全部是 NLP/AI 会议，完全没有提到 CoRL。\n4. CoRL 2025 的 accepted papers 几乎全部涉及物理机器人学习（manipulation、locomotion、sim-to-real），不存在纯 NLP agent tool-use safety 论文被接收的先例。\n\n**结论：这是一个 scope 层面的致命不匹配。即使 idea 本身质量优秀，在 CoRL 主会也几乎必然被 desk reject。** 以下评估仍会对 idea 本身的质量进行客观打分，但概率估计必须反映 venue 不匹配这一事实。\n\n---\n\n【领域调研】:\n\n- [The Verifier Tax (arXiv 2603.19328, Mar 2026)](https://arxiv.org/abs/2603.19328): 本 proposal 的核心动机论文。在 tau-bench 上量化了 safety mediation 的代价：即使阻断率达 94%，SSR（严格安全成功率）仍低于 5%，recovery rate 从 21%（简单 Airline 任务）降至近 0%（复杂 Retail 场景）。Proposal 对该论文的引用和描述准确。\n  \n- [Symbolic Guardrails (arXiv 2604.15579, Apr 2026)](https://arxiv.org/abs/2604.15579): Proposal 的第二核心动机论文。在 τ²-bench 上展示了 symbolic guardrails 提供 informative blocking feedback 后，GPT-4o pass rate 从 0.36 提升到 0.48。但该论文的主要贡献是 guardrail 设计而非 recovery 研究，recovery 只是被观察到的 side effect。Proposal 的描述基本准确。\n\n- [BackBench (arXiv 2604.18847, Apr 2026)](https://arxiv.org/abs/2604.18847): 50 个 post-harm recovery 场景（OSWorld/GUI），与本 proposal 的 post-blocking recovery 确实属于不同范畴。Proposal 的区分合理。\n\n- [Fission-GRPO (arXiv 2601.15625, Jan 2026)](https://arxiv.org/abs/2601.15625): 训练 tool-calling error recovery 的 RL 方法，在 BFCL v4 上提升 5.7% recovery rate。这是本 proposal 训练方法 RA-FGRPO 的直接基础——RA-FGRPO 本质是 Fission-GRPO 在 safety block 场景的领域适配。\n\n- [GTPO (arXiv 2511.14846, Nov 2025)](https://arxiv.org/abs/2511.14846): Turn-level credit assignment 方法，比 GRPO +3.0%。作为 RA-FGRPO 的 credit assignment 组件被引用，描述准确。\n\n- [ReGuard (arXiv 2510.13727, Oct 2025)](https://arxiv.org/abs/2510.13727): Guardrail-side 控制理论方法，在 driving/e-commerce 场景注入纠正动作。Proposal 正确区分了 agent-side replanning vs. guardrail-side correction。\n\n- [AGENT-C (arXiv 2512.23738, Dec 2025)](https://arxiv.org/abs/2512.23738): Token-level constrained decoding 实现 100% safety conformance + utility 提升（Claude Sonnet 4.5: 71.8%→75.2%）。这是 proposal 最强的 trivial alternative 竞争者。\n\n- [ToolMisuseBench (arXiv 2604.01508, Apr 2026)](https://huggingface.co/datasets/sigdelakshey/ToolMisuseBench): 6800 task 的 operational error recovery benchmark。与本 proposal 的区别在于 fault 类型（operational vs. safety policy），但方法论高度相似。\n\n- 调研总结: Agent safety 领域在 2025-2026 年爆发式增长，围绕 guardrail 的工作已形成完整生态：blocking（TraceSafe, ATBench）、guardrail-side correction（AGENT-C, ReGuard）、post-error recovery（Fission-GRPO, ToolMisuseBench）、post-harm recovery（BackBench）。本 proposal 定位在 \"post-blocking agent-side recovery\" 这一具体 niche，确实是一个尚未被独立 benchmark 覆盖的子问题，但其独立存在的价值取决于 agent-side recovery 相比 guardrail-side correction 的增量贡献是否充分。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在两个显著的 trivial alternative 威胁：\n\n1. **AGENT-C 已经\"解决\"了这个问题的大部分**：AGENT-C 通过 constrained decoding 在 guardrail 端实现 100% safety conformance + utility 提升。如果 guardrail 本身就能纠正不安全动作并保持 utility，为什么还需要训练 agent 学会 replanning？Proposal 承认两者 complementary，但没有论证在 AGENT-C 已部署的情况下，agent-side recovery 的剩余价值有多大。\n\n2. **Simply providing better error messages（Symbolic Guardrails 已有的发现）**：Symbolic Guardrails 已经展示了 informative blocking feedback 让 GPT-4o 从 0.36 提升到 0.48——不需要任何新 benchmark 或 training method。本 proposal 的 RecoverBench 在 diagnostic feedback 条件下测试的效果，可能大部分归因于 feedback quality 而非 agent 训练。\n\n3. **Fission-GRPO 直接应用**：Fission-GRPO 已经训练 error recovery。将 safety block 当作一种特殊的 execution error，直接用 Fission-GRPO 训练（不需要 RA-FGRPO 这个\"安全特化\"版本），可能效果差距不大。\n\n增量价值的论点：Proposal 的真正增量在于 (a) dual-challenge 设计（recoverable + unrecoverable 分类）和 (b) 系统化测量 recovery 质量的 5 个 metrics。但这更多是 benchmark engineering 的贡献，而非概念突破。\n\n---\n\n【前提假设检验】:\n\n核心 claim 逻辑链中有几个未经验证的假设：\n\n1. **\"Post-blocking recovery 是一个独立的、值得单独建 benchmark 的 failure mode\"** — 这是本 proposal 最核心的前提假设。但 Symbolic Guardrails 已经在 guardrail evaluation 的框架下 incidentally 测量了 recovery（pass rate 变化），且 AGENT-C 通过 guardrail-side correction 可能使 agent-side recovery 变得不那么重要。这个 failure mode 是否\"独立\"到值得专门研究，取决于 guardrail-side correction 是否已经足够好——如果 AGENT-C 类方法部署后 recovery 问题大幅缓解，这个 benchmark 的长期价值会打折。\n\n2. **\"Open-source model 的 recovery gap 可以通过 RA-FGRPO 训练来弥合\"** — 这建立在假设 recovery 是一个可以通过 RL fine-tuning 显著提升的 capability 之上。但 The Verifier Tax 显示 open-source model 的 SSR < 5%，recovery near 0%——这可能不是 \"缺少 recovery 训练\" 的问题，而是这些模型（GPT-OSS-20B, GLM-4-9B）的基础能力（planning, reasoning）不足以支撑 multi-step replanning。如果基础能力是瓶颈，单独训练 recovery 可能收效甚微。\n\n3. **\"Unrecoverable recognition（URR）是 agent 可以学会的\"** — 判断一个任务在 policy constraints 下是否无解，本质上是一个 constraint satisfaction 推理问题。小模型（3B-4B active parameters）是否有足够的推理能力学会这一点是存疑的。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — Proposal 的核心 novelty 在于提出 \"post-blocking recovery\" 作为独立 failure mode 并构建专门 benchmark。但：\n   - 对 recovery 的观测已在 Symbolic Guardrails 和 The Verifier Tax 中存在，只是没有被显式命名为独立 benchmark target\n   - RecoverBench 的构建方法（在 tau-bench 上注入 guardrail blocks）是直接的工程工作，不涉及新方法论\n   - RA-FGRPO = Fission-GRPO + GTPO credit + safety block 场景适配，是现有方法的直接组合\n   - 真正的 novelty delta：(a) dual-challenge 设计（recover + recognize unrecoverable）有一定价值，(b) 5 个 metrics 的系统化设计（尤其 FRR 测量 constraint gaming）有实用意义，(c) feedback informativeness 作为实验维度有 analytical value。但这些更接近 benchmark engineering 贡献而非 conceptual breakthrough。\n\n2. **Significance: 中** — 问题本身确实重要——agent safety 是热门方向，recovery gap 是真实存在的问题（有 The Verifier Tax 的实证支持）。但 significance 受限于：\n   - AGENT-C 类 guardrail-side correction 可能使 agent-side recovery 训练的实际部署需求降低\n   - 结果如果 positive（RA-FGRPO 提升了 open-source model 的 recovery），审稿人更可能说 \"I would have guessed that RL training helps\" 而非 \"surprising\"\n   - Benchmark 局限于 tau-bench（Airline + Retail 两个领域），generalizability 有限\n   - 对 NLP/AI 领域有中等影响力；对 robotics 领域几乎无影响力\n\n3. **Related Work: 强** — 这是 proposal 最突出的优点。Related work 覆盖极其全面，taxonomy 清晰（5 类 recovery paradigm + guardrail-side correction），对每篇工作的区分精确。Post-blocking recovery vs. post-harm recovery vs. post-error recovery vs. post-incident response vs. guardrail-side correction 的分类有独立价值。对 Symbolic Guardrails、The Verifier Tax、BackBench、Fission-GRPO、ReGuard、AGENT-C 的定位都准确且有实质性区分。\n\n---\n\n【概率估计】: [0% - 3%] 中位 1%\n\n【估计理由】:\n\n**这个概率估计几乎完全由 venue 不匹配决定。**\n\nCoRL 是 Conference on Robot Learning，其 CFP 明确要求 robotics focus，且声明 \"submissions without a robotics focus will be returned without review\"。本 proposal 是一个纯 NLP/AI agent tool-use safety 工作，在 airline/retail 客服 API 场景中运行，不涉及任何机器人学习内容——没有物理交互、没有感知、没有 manipulation、没有 sim-to-real、没有 embodied agent。这是一个近乎确定的 desk reject。\n\n**如果改投 proposal 自身列出的 target venues（EACL/AAAI/NAACL），idea 本身的质量估计大致在 20-30% 范围**：\n- Novelty 弱-中（组合性贡献，benchmark engineering 为主）限制了上界\n- Significance 中（问题重要但 trivial alternative 威胁显著）\n- Related Work 强（对下限有支撑）\n- 核心风险在于 AGENT-C 和 Symbolic Guardrails informative feedback 作为 trivial alternative 会被审稿人质疑\n\n但对于 CoRL 2026 主会，概率实质为 0-3%。\n\n【主要风险】:\n1. **致命 venue 不匹配**：CoRL 要求 robotics focus，本 proposal 没有任何 robotics 内容，几乎必然 desk reject\n2. **Trivial alternative 威胁**（假设投向 NLP venue）：AGENT-C 的 guardrail-side correction 已实现 100% safety + utility 提升，reviewer 会质疑 agent-side recovery training 的增量价值；Symbolic Guardrails 的 informative feedback 已展示 partial recovery，reviewer 会问 \"为什么不直接改善 feedback 质量\"\n```\n\n---\n\n**补充建议**：如果作者认为这个 idea 有价值，应该投向自身已列出的 NLP/AI venues（EACL 2027 via ARR、AAAI 2027、NAACL 2027），而非 CoRL。如果一定要投 CoRL，需要彻底重构 proposal：将 recovery 问题迁移到 robotics 场景（如 embodied agent 在物理环境中被 safety guardrail 阻断后的 replanning），使用机器人仿真环境而非 tau-bench API 场景。但这本质上是一个完全不同的 paper。\n\nSources:\n- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)\n- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)\n- [BackBench (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)\n- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)\n- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)\n- [ReGuard (arXiv 2510.13727)](https://arxiv.org/abs/2510.13727)\n- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)\n- [ToolMisuseBench](https://huggingface.co/datasets/sigdelakshey/ToolMisuseBench)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Homepage](https://www.corl.org/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Beyond Blocking: Benchmarking and Training Agent Task Recovery After Guardrail Interventions in Multi-Step Tool Use\n\n## Description\nCurrent agent safety guardrails achieve high blocking rates (up to 94%) for unsafe actions, yet post-blocking recovery is inconsistent and model-dependent: open-source models (GPT-OSS-20B, GLM-4-9B) achieve safe success rates below 5% with recovery rates from 21% to near 0% (The Verifier Tax, 2026), while frontier models with informative blocking feedback show partial recovery (GPT-4o: 0.36→0.48 pass rate per Symbolic Guardrails, 2026) but still fail 52% of tasks. We identify post-blocking task recovery as a distinct failure mode — categorically different from post-harm recovery (BackBench), post-incident response (AIR), post-error recovery (RAC/Fission-GRPO/ToolMisuseBench), and guardrail-side correction (ReGuard, AGENT-C). We propose RecoverBench, a benchmark measuring agent task recovery after guardrail interventions in multi-step tool-use settings, featuring a dual challenge: agents must recover when safe alternatives exist AND recognize when recovery is impossible. Built atop tau-bench (Airline/Retail), RecoverBench injects guardrail blocks at critical trajectory points with systematically varied feedback informativeness (minimal, policy-cited, diagnostic) and introduces three task categories (recoverable, correctly unrecoverable, partially recoverable) evaluated by five metrics: Safe Recovery Rate, False Recovery Rate (detecting constraint gaming via alternative unsafe pathways), Unrecoverable Recognition Rate, Recovery Latency, and Alternative Path Quality. We detail a three-module Safety Recovery Simulator (constraint extraction, safe alternative enumeration via API specification parsing, diagnostic context formatting) that generates training signal without revealing oracle solutions. For training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO) with a tiered credit assignment strategy: GTPO-based turn-level rewards as primary (most established, +3.0% over GRPO), AT²PO-based tree credit as validated fallback, and GAGPO-style grouped credit as future extension pending independent validation. RA-FGRPO adapts Fission-GRPO's on-policy error augmentation for safety-specific recovery, generating G'=4 parallel recovery attempts per blocked trajectory. We evaluate on Qwen3.6-35B-A3B and Qwen3-4B across complexity bins, targeting the model-dependent recovery gap: approaching frontier-model recovery levels for open-source models. Ablations compare against vanilla GRPO, offline DPO, ToolSafe pre-execution feedback, ReGuard-style guardrail-side correction, and frontier model baselines with informative blocking.\n\n## Core Problem\nCurrent guardrails achieve high unsafe-action blocking rates (up to 94%), but post-blocking task recovery is inconsistent, model-dependent, and unmeasured as a first-class capability. For smaller open-source models (GPT-OSS-20B, GLM-4-9B), recovery rates range from 21% on simpler procedural tasks to near 0% on complex Retail scenarios, with safe success rates below 5% in most settings (The Verifier Tax, 2026). Frontier models with informative blocking feedback fare substantially better — Symbolic Guardrails (2026) shows GPT-4o pass rates improving from 0.36 to 0.48 on tau²-bench when guardrails provide policy-violation explanations, and GPT-5 from 0.68 to 0.70 — but even GPT-4o still fails 52% of tasks after blocking. Critically, no existing work isolates post-blocking recovery as a dedicated benchmark target: Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation, not recovery quality, and provides no recoverable/unrecoverable task classification, no false recovery rate measurement, and no recovery-specific training method. This represents a distinct and underexplored failure mode: post-blocking task recovery. Unlike post-harm recovery (BackBench) where harm has occurred and must be remediated, post-incident response (AIR) where the system detects and contains safety breaches, post-error recovery (RAC/Fission-GRPO) where operational errors must be corrected, or guardrail-side correction (ReGuard, AGENT-C) where the guardrail itself generates corrective actions, post-blocking recovery requires the AGENT to find an alternative safe path to complete the user's legitimate task after being correctly prevented from taking an unsafe action. Critically, some blocked scenarios may genuinely have no safe alternative path — the agent must also learn to recognize when recovery is impossible and gracefully inform the user. No existing benchmark isolates this specific failure mode with its dual challenge (recover when possible, recognize impossibility when not), and no training method specifically targets the agent's adaptive replanning ability after correct guardrail intervention.\n\n## Opportunity\nThe Verifier Tax (Mar 2026) quantifies a devastating Safety-Capability Gap for open-source models: with GPT-OSS-20B and GLM-4-9B on tau-bench, even with 94% unsafe action blocking, safe success rates remain below 5% in most settings, and recovery rates following blocked actions range from 21% in simpler procedural Airline tasks to near 0% in complex Retail scenarios. Symbolic Guardrails (Apr 2026) reveals the model-dependency dimension: when guardrails provide informative blocking feedback (explaining which policy was violated and why), GPT-4o achieves a 33% relative improvement in pass rate (0.36→0.48) on tau²-bench Airline, and GPT-5 a modest 3% improvement (0.68→0.70) — demonstrating that (a) recovery IS possible when the agent receives informative feedback, (b) even frontier models still fail 52% of tasks (GPT-4o) despite recovery attempts, and (c) recovery quality is never measured as a first-class metric. This model-dependent recovery gap creates a clear motivation: if frontier models can partially recover with informative feedback but smaller models cannot, then dedicated recovery training can close this gap for open-source models. The gap is distinct from what AIR (>90% remediation success in post-incident response), BackBench (50 post-harm recovery scenarios in OSWorld), and ReGuard (control-theoretic guardrail correction in driving/e-commerce) address. In post-blocking recovery, the guardrail works as intended — harm is prevented — but the agent fails at adaptive replanning. Canonical Path Deviation (Feb 2026) explains the structural difficulty: off-canonical actions compound subsequent deviation by 22.7 percentage points, meaning that once an agent is pushed off its solution path by a blocked action, the probability of finding an alternative path drops sharply. Meanwhile, ToolSafe (Jan 2026) shows that safety-feedback-driven reasoning can improve benign task completion by ~10% and reduce harmful tool invocations by 65%, but this represents pre-execution guidance, not post-blocking recovery training. TraceSafe (Apr 2026) demonstrates that guardrail efficacy in multi-step settings depends more on structural data competence than semantic safety alignment, suggesting the recovery problem requires structured training beyond alignment alone. The maturation of turn-level RL methods for multi-step agents — GTPO (Nov 2025, turn-level reward assignment with +3.0% over GRPO), AT²PO (Jan 2026, tree-based turn-wise credit), Fission-GRPO (Jan 2026, on-policy error augmentation), GAGPO (May 2026, critic-free grouped temporal credit) — provides robust methodological foundations for training recovery behavior, with multiple established fallback options for credit assignment.\n\n## Landscape\nWe identify four distinct recovery paradigms in current agent safety research, plus a complementary guardrail-side correction approach, each requiring different metrics, training approaches, and benchmarks:\n\n(1) POST-BLOCKING TASK RECOVERY (ours): After a guardrail correctly blocks an unsafe action, the agent must find an alternative safe path to complete the original task — or recognize when no safe path exists. The Verifier Tax (Mar 2026) documents recovery rates from 21% (simpler Airline tasks) to near 0% (complex Retail scenarios) for GPT-OSS-20B and GLM-4-9B with TRIAD-SAFETY on tau-bench, with SSR below 5% in most settings. Symbolic Guardrails (Apr 2026) shows that recovery is model-dependent and feedback-dependent: on tau²-bench Airline (50 tasks), GPT-4o pass rates improve from 0.36 to 0.48 (+33% relative) and GPT-5 from 0.68 to 0.70 (+3% relative) when symbolic guardrails block unsafe actions and provide informative error messages explaining which policy was violated. The paper explicitly states agents 'use this feedback to adjust its subsequent actions, retry with a safer alternative, and often complete the task successfully.' However, Symbolic Guardrails measures pass rate as a side effect of guardrail evaluation — recovery is neither a first-class metric nor a dedicated research target. It provides no recovery-specific benchmark, no recoverable/unrecoverable task classification, no false recovery rate measurement, no recovery latency analysis, no path quality assessment, and no recovery-specific training method. Its finding that even GPT-4o still fails 52% of tasks after blocking, combined with the near-zero recovery of smaller models documented by The Verifier Tax, directly MOTIVATES our work: recovery happens partially and uncontrollably for frontier models, but remains an unsolved problem for smaller open-source models that need dedicated training.\n\n(2) POST-HARM RECOVERY: After harm has occurred, the agent must remediate it. BackBench (arXiv 2604.18847, Apr 2026) provides 50 backtracking scenarios in OSWorld for computer-use agents, with a reward model trained on 1,150 pairwise human preference judgments, achieving +120 Elo improvement. Key differences from ours: (a) BackBench presupposes harm has occurred and must be undone; we presuppose harm was prevented; (b) BackBench operates in GUI/OS environments; we operate in tool-use API settings; (c) BackBench optimizes recovery quality via human preferences; we measure task completion, latency, path quality, AND recognition of unrecoverable scenarios.\n\n(3) POST-INCIDENT RESPONSE: AIR (arXiv 2602.11749, Feb 2026) provides a DSL-based incident response framework achieving >90% detection, remediation, and eradication rates. Critically, AIR terminates the task after remediation — it does not attempt to resume and complete the original task via an alternative safe path.\n\n(4) POST-ERROR RECOVERY: RAC (ACM CAIS 2026) provides log-based rollback for general execution errors on tau-bench/REALM-Bench. Fission-GRPO (Jan 2026) trains recovery from tool-calling errors via on-policy error augmentation (+5.7% recovery rate on BFCL v4). ToolMisuseBench (arXiv 2604.01508, Apr 2026) provides 6,800 tasks across CRUD/retrieval/file/scheduling environments with deterministic fault injection, measuring recovery quality and budgeted efficiency under explicit step/call/retry budgets — the operational-error counterpart to our safety-specific recovery benchmark. Its replayable fault injection methodology and budgeted efficiency metric S(k) are methodologically adjacent to our approach, but its faults are operational (schema drift, rate limits, authorization failures) rather than safety-policy violations. Hell or High Water (COLM 2025) evaluates recovery from environmental failures.\n\n(5) GUARDRAIL-SIDE CORRECTION: Three distinct technical approaches exist for correcting unsafe actions at the guardrail level rather than training agent-side replanning:\n\n(5a) ReGuard ('From Refusal to Recovery', arXiv 2510.13727, Oct 2025) learns a control-theoretic safety value function V(z) and fallback policy π_safe that INJECTS corrective actions when Q(z,a) ≤ 0 — the agent never replans, the guardrail replaces its unsafe action with a safe one. Evaluated on simulated driving (obstacle avoidance) and simple e-commerce (shopping cart budget constraints), not multi-step tool-use API settings with complex policy rules. Requires simulator access during guardrail training. Achieves 77.3% success vs 44.4% for myopic refusal, but proposes no recovery-specific benchmark.\n\n(5b) AGENT-C ('Enforcing Temporal Constraints for LLM Agents', arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2) provides guardrail-side correction via constrained decoding: it translates temporal safety specifications into first-order logic and uses SMT solving to detect non-compliant tool calls during token generation, then leverages constrained generation to produce compliant alternatives. AGENT-C achieves 100% safety conformance while improving utility (Claude Sonnet 4.5: 71.8%→75.2%; GPT-5: 66.1%→70.6%). Unlike ReGuard's control-theoretic approach, AGENT-C operates at the token generation level via formal verification, but shares the same fundamental characteristic: the GUARDRAIL corrects the action rather than the AGENT learning to replan. For open-weight models it can enforce at fine-grained token level; for closed-source models at coarser call-level resampling.\n\n(5c) Symbolic Guardrails' informative blocking feedback can be viewed as a lightweight guardrail-side intervention — by explaining policy violations, the guardrail provides implicit guidance toward safe alternatives, though without generating the corrective action itself.\n\nOur work is complementary to all category (5) approaches: they improve guardrail correction capability; we improve agent replanning capability. The optimal deployment may combine both — a smarter guardrail (ReGuard/AGENT-C/Symbolic) paired with an agent trained to replan when guardrail-side corrections are insufficient or unavailable. Our ReGuard ablation directly tests this complementarity.\n\nAdditional relevant concurrent work: SafePred (Feb 2026) achieves 97.6% safety via predictive prevention with world models — prevents unsafe actions but does not address recovery. MOSAIC (Mar 2026) introduces Plan-Check-Act/Refuse with up to 50% harmful behavior reduction — evaluates refusal quality, not post-refusal replanning. SafeAgent (Apr 2026) mentions constrained replanning as a recovery mechanism but provides no disaggregated metrics for replanning success rate, recovery rate, or path quality — overall evaluation uses ASR and NRP without isolating replanning contribution. Mind the GAP (Feb 2026) demonstrates text safety does not transfer to tool-call safety, motivating tool-level guardrails. OpenAgentSafety (ICLR 2026) provides a comprehensive 350+ task evaluation framework for agent safety with real tools but focuses on risk evaluation, not recovery. ATBench (Apr 2026) benchmarks trajectory-level safety with 1,000 trajectories across 2,084 tools but evaluates safety detection, not recovery. ToolSafe (Jan 2026) guides agents toward safety-aware reasoning via pre-execution feedback (TS-Flow), reducing harmful tool invocations by 65% — closest to our setting in spirit, but operates as a guardrail providing preventive guidance rather than training recovery. TraceSafe (Apr 2026) reveals guardrail efficacy depends more on structural JSON parsing than semantic alignment. AgentSpec (ICSE 2026) provides a DSL-based runtime enforcement framework with >90% unsafe execution prevention — its constraint specification approach directly informs our Safety Recovery Simulator's alternative action enumeration. SafeAgentBench (Dec 2024) includes hazardous tasks with only 5-10% rejection rates, demonstrating that recognizing unrecoverable scenarios is itself a challenge.\n\n## Approach\nWe construct RecoverBench by instrumenting tau-bench (Airline + Retail) with a guardrail intervention simulator that injects safety blocks at systematically varied trajectory points. The benchmark explicitly includes three task categories: (a) RECOVERABLE tasks where at least one safe alternative path exists (verified by oracle exhaustive search over constraint-satisfying action space), (b) CORRECTLY UNRECOVERABLE (CU) tasks where the user's request inherently requires a policy-violating action with no safe alternative (e.g., full refund on non-refundable ticket past cancellation window), and (c) PARTIALLY RECOVERABLE tasks where a degraded but safe version of the task can be completed (e.g., store credit instead of cash refund). We measure five metrics: Safe Recovery Rate (SRR: percentage of recoverable episodes where the agent finds an alternative safe path), False Recovery Rate (FRR: percentage of all episodes where the agent claims task completion but actually violates safety constraints via a DIFFERENT pathway than the blocked one — measuring constraint gaming/safety circumvention), Unrecoverable Recognition Rate (URR: percentage of CU episodes where the agent correctly identifies no safe path exists and gracefully informs the user), Recovery Latency (additional turns required after blocking for successful recoveries), and Alternative Path Quality (semantic similarity to optimal safe trajectories plus task reward preservation). The benchmark is explicitly designed to complement BackBench (post-harm, GUI/OS), AIR (post-incident, multi-domain), ToolMisuseBench (post-error, operational faults with deterministic replay), and RAC (post-error, general).\n\nBLOCKING FEEDBACK DESIGN: Motivated by Symbolic Guardrails' finding that informative error messages (explaining which policy was violated and why) enable partial recovery in frontier models, RecoverBench systematically varies blocking feedback informativeness as an experimental condition: (i) MINIMAL feedback (action blocked, no explanation), (ii) POLICY-CITED feedback (action blocked + specific policy rule citation, matching Symbolic Guardrails' approach), and (iii) DIAGNOSTIC feedback (action blocked + policy citation + available alternative actions, matching our SRS training context). This enables measuring how feedback informativeness affects recovery across model capability levels, directly extending Symbolic Guardrails' implicit finding that informative feedback helps.\n\nSAFETY RECOVERY SIMULATOR (SRS) SPECIFICATION: The SRS — the component that generates diagnostic context for RA-FGRPO training — operates through three modules: (1) CONSTRAINT EXTRACTION MODULE: Parses tau-bench's domain policy files (airline rebooking rules, retail return policies) to extract formal constraints as predicate functions, following AgentSpec's (ICSE 2026) trigger→predicate→enforcement pattern. Each constraint maps an action type to its validity conditions in the current environment state. (2) SAFE ALTERNATIVE ENUMERATOR: Given a blocked action and current state, queries the tau-bench API specification for all valid actions in the current state, filters out actions violating the triggered constraint or related constraints, and ranks remaining actions by semantic relevance to the original task intent (using embedding similarity between the blocked action's inferred goal and candidate action descriptions). For CU scenarios, returns an empty set. For partially recoverable scenarios, returns degraded alternatives with explicit quality annotations. (3) DIAGNOSTIC CONTEXT FORMATTER: Constructs augmented context as [trajectory_prefix; BLOCKED: action_name(args) → REASON: policy_rule_citation; AVAILABLE_ACTIONS: [ranked_action_list]; TASK_GOAL: original_user_request]. Critically, we provide WHICH actions are available but NOT which specific sequence solves the task — the agent must learn replanning, not memorize recovery templates. SRS validity is verified against oracle safe trajectories (computed offline via exhaustive search) to ensure enumeration completeness.\n\nFor training, we propose Recovery-Aware Fission-GRPO (RA-FGRPO), adapting Fission-GRPO's on-policy error recovery augmentation for safety-specific guardrail interventions, with a tiered credit assignment strategy to mitigate dependency on any single unvalidated method. RA-FGRPO works as follows: (1) Standard GRPO exploration generates rollouts through guardrail-blocked scenarios on tau-bench; (2) The Safety Recovery Simulator intercepts blocked trajectories and augments them with diagnostic context from the three modules above; (3) Fission-based resampling generates G'=4 parallel recovery attempts from augmented contexts, creating dense on-policy training signal specifically for post-blocking adaptation; (4) PRIMARY CREDIT ASSIGNMENT: GTPO-based turn-level reward assignment (arXiv 2511.14846, Nov 2025, revised Apr 2026) provides fine-grained per-turn feedback with return-based advantage estimation and self-supervised reward shaping — adapted so the self-supervision signal comes from constraint compliance verification at each turn rather than code execution signals. GTPO is chosen as primary because: (a) it is the most established turn-level method (6+ months, revised), (b) it outperforms GRPO by 3.0% on multi-turn tool-integrated reasoning with negligible overhead, (c) its self-supervised reward shaping naturally adapts to safety constraint signals. FALLBACK CREDIT ASSIGNMENT: AT²PO-based tree-wise credit (arXiv 2601.04767, Jan 2026) serves as the validated fallback, using entropy-guided tree expansion for diverse recovery path exploration and recursive turn-wise value propagation — particularly suited when recovery requires exploring multiple branching alternatives. FUTURE EXTENSION: GAGPO's (arXiv 2605.13217, May 2026) critic-free grouped value proxy could further improve credit assignment if independently validated, but its requirement for exact textual state matching across rollouts needs adaptation for tool-use states (serialized API state + conversation history). We explicitly ablate all three credit assignment strategies.\n\nWe train open-source models (Qwen3.6-35B-A3B with 3B active parameters, Qwen3-4B) and evaluate across task complexity bins aligned with the Verifier Tax's horizon-dependent analysis. This model selection is directly motivated by the model-dependent recovery gap: Symbolic Guardrails shows frontier models (GPT-4o, GPT-5) partially recover with informative feedback, while The Verifier Tax shows open-source models (GPT-OSS-20B, GLM-4-9B) achieve near-zero recovery in complex scenarios — our training targets exactly this capability gap in open-source models. We additionally analyze how Canonical Path Deviation severity modulates recovery difficulty and whether RA-FGRPO helps agents re-anchor to canonical solution paths after guardrail intervention. A key ablation compares RA-FGRPO (with GTPO credit) against: vanilla GRPO, RA-FGRPO with AT²PO credit, RA-FGRPO with GAGPO credit (if feasible), offline DPO (DiaTool-DPO-style trajectory pairs), ToolSafe-style pre-execution safety feedback, and ReGuard-style guardrail-side correction (control-theoretic fallback policy). The ReGuard ablation is particularly important: it directly compares our agent-side replanning approach against guardrail-side action injection, testing whether the two are complementary. We also compare against frontier model baselines (GPT-4o, GPT-5) with Symbolic Guardrails-style informative blocking to establish the recovery ceiling that our training aims to approach for open-source models.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1,100 H100 hours (benchmark construction with oracle trajectory computation: 250h, RA-FGRPO training with GTPO credit + online rollouts on 3B-35B MoE models: 450h, evaluation sweeps across complexity bins and feedback conditions: 200h, ablations including AT²PO/GAGPO credit + ReGuard comparison: 200h)', 'timeline': '14-16 weeks', 'estimated_gpu_cost': '$2,200 (H100 spot at ~$2/hr)'}, 'human_in_loop': {'gpu_hours': '~1,100 H100 hours (same compute, faster iteration on SRS design and CU scenario curation)', 'timeline': '10-12 weeks', 'claude_api_cost': '$300-500 (code generation for SRS modules, constraint extraction, trajectory analysis, paper drafting)', 'estimated_gpu_cost': '$2,200'}, 'auto_research': {'gpu_hours': '~1,500 H100 hours (additional hyperparameter exploration, Fission resampling sweeps, three-way credit assignment ablations, ReGuard comparison, oracle trajectory exhaustive search for CU validation, feedback informativeness sweeps)', 'timeline': '6-8 weeks', 'claude_api_cost': '$800-1,200 (end-to-end pipeline orchestration, automated ablation design, constraint extraction from tau-bench policies, SRS validation)', 'estimated_gpu_cost': '$3,000', 'speed_bottleneck': \"GPU availability for concurrent RA-FGRPO online rollouts across model sizes; oracle safe trajectory computation for CU scenario validation; Fission resampling throughput (G'=4 parallel recovery attempts per blocked trajectory)\"}}\n\n## Inspired By\nField guide Section 7 (Defenses: guardrails, verification, monitoring) combined with Section 4.1 (pass@1 vs. production reliability gap). The Verifier Tax's quantitative evidence makes the gap between blocking success and task recovery concrete and measurable for open-source models, while Symbolic Guardrails reveals that recovery is model-dependent — frontier models partially recover with informative feedback, but smaller models cannot. This model-dependency motivates dedicated recovery training as the intervention point. The four-way taxonomy of recovery types (plus guardrail-side correction as a complementary paradigm) emerged from successive rounds of critical feedback, with the 'From Refusal to Recovery' and AGENT-C differentiation revealing that recovery requires distinguishing WHERE the intervention happens (guardrail vs. agent) and WHAT the intervention does (inject/constrain corrected action vs. replan). ToolMisuseBench's deterministic fault injection and budgeted efficiency metric inspired our benchmark design for replayability and efficiency measurement. The reviewer's 'correctly unrecoverable' insight led to the dual-challenge formulation (recover when possible, recognize impossibility when not), strengthening the benchmark's evaluative power. Fission-GRPO's on-policy error augmentation directly inspires our training approach; GTPO's turn-level reward assignment provides the primary credit mechanism; AT²PO's tree-based credit provides the validated fallback. Pattern: 'complementary gap-filling' with 'dual-challenge evaluation.'\n\n## Target Venues\n- EACL 2027 via ARR Aug 3, 2026 (commitment Oct 11, 2026 — primary target, 11 weeks for full RecoverBench + RA-FGRPO paper)\n- AAAI 2027 (abstract Jul 21 / paper Jul 28, 2026 — parallel stretch goal, scoped to RecoverBench benchmark paper only, deferring RA-FGRPO training results to extended version)\n- NAACL 2027 via ARR Oct-Nov 2026 (extended version with cross-benchmark comparison against BackBench/AIR/ToolMisuseBench and ReGuard complementarity analysis)\n\n## Key References\n- The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents (arXiv 2603.19328, Mar 2026)\n- Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility (arXiv 2604.15579, Apr 2026)\n- Enforcing Temporal Constraints for LLM Agents [AGENT-C] (arXiv 2512.23738, Dec 2025, ICLR 2026 Workshop VerifAI-2)\n- From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails [ReGuard] (arXiv 2510.13727, Oct 2025)\n- AIR: Improving Agent Safety through Incident Response (arXiv 2602.11749, Feb 2026)\n- Human-Guided Harm Recovery for Computer Use Agents [BackBench] (arXiv 2604.18847, Apr 2026)\n- Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors (arXiv 2601.15625, Jan 2026)\n- ToolMisuseBench: An Offline Deterministic Benchmark for Tool Misuse and Recovery in Agentic Systems (arXiv 2604.01508, Apr 2026)\n- Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization [GTPO] (arXiv 2511.14846, Nov 2025, revised Apr 2026)\n- AT²PO: Agentic Turn-based Policy Optimization via Tree Search (arXiv 2601.04767, Jan 2026)\n- GAGPO: Generalized Advantage Grouped Policy Optimization (arXiv 2605.13217, May 2026)\n- SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (arXiv, Feb 2026)\n- Learning When to Act or Refuse [MOSAIC] (arXiv, Mar 2026)\n- SafeAgent: A Runtime Protection Architecture for Agentic Systems (arXiv 2604.17562, Apr 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure (arXiv, Feb 2026)\n- Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents (arXiv 2602.16943, Feb 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026)\n- ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis (arXiv 2604.02022, Apr 2026)\n- ToolSafe: Enhancing Tool Invocation Safety via Proactive Step-level Guardrail and Feedback (arXiv 2601.10156, Jan 2026)\n- TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories (arXiv 2604.07223, Apr 2026)\n- tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains (ICLR 2025)\n- AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents (ICSE 2026)\n- Robust Agent Compensation (RAC) (ACM CAIS 2026)\n- Hell or High Water: Evaluating Agentic Recovery from External Failures (COLM 2025)\n- EmbodiedGovBench: Governance, Recovery, and Upgrade Safety in Embodied Agent Systems (arXiv, Apr 2026)\n- DiaTool-DPO: Multi-Turn DPO for Tool-Augmented LLMs (SIGDIAL 2025, arXiv 2504.02882, Apr 2025)\n- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv 2602.03025, Feb 2026)\n- T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL (ICML 2026 Spotlight)\n- SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents (arXiv 2412.13178, Dec 2024)\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:32:00.905Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:32:00.905Z",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:32:00.920Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have enough research to produce a thorough, evidence-based assessment. Let me compile my findings.

---

```
【阶段】: Triage

⚠️ 【致命前置问题：投稿目标与 Proposal 内容严重不匹配】

本 Proposal 的投稿目标被指定为 **CoRL 2026**（Conference on Robot Learning），但 Proposal 内容与 CoRL 的 scope 完全不匹配：

- **CoRL 明确要求**："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics" 以及 "Submissions without a robotics focus will be returned without review"（来源：CoRL 2026 Call for Papers, corl.org）
- **本 Proposal 的实际内容**：text-based LLM agent safety，基于 tau-bench（Airline/Retail 客服场景），评估 agent 在 guardrail 阻断后的 tool-use replanning 能力
- **Proposal 自身列出的 target venues**：EACL 2027, AAAI 2027, NAACL 2027 — 全部是 NLP/AI 会议，无一提及 CoRL
- **Proposal 无任何 robotics 内容**：没有 real-robot 实验、没有 sim-to-real、没有 embodied agent、没有物理世界交互

**结论：提交至 CoRL 2026 几乎必然 desk rejection（未进审稿即退回）。** 中稿概率约为 0-2%，与 idea 质量无关，纯粹是 scope mismatch。

以下评估将忽略 venue mismatch，聚焦于 idea 本身的质量，以便判断其在 **适配 venue**（如 EACL/AAAI/NAACL/EMNLP/ACL）的潜力。

---

【领域调研】:

- **[The Verifier Tax](https://arxiv.org/abs/2603.19328)** (arXiv, Mar 2026): 本 proposal 的核心动机论文。量化了 runtime safety enforcement 对 task completion 的影响：94% 阻断率但 SSR < 5%，recovery rate 从 21%（Airline）到 ~0%（Retail）。论文本身并未将 recovery 作为研究目标，而是作为 verifier tax 的一个副产品记录。**与 proposal 的关系：提供了 motivating evidence，但未提供 recovery 的 benchmark 或训练方法。**

- **[Symbolic Guardrails](https://arxiv.org/abs/2604.15579)** (arXiv, Apr 2026, CMU): 在 tau²-bench 上评估 symbolic guardrails，发现 informative error messages 使 GPT-4o pass rate 从 0.36 提升到 0.48。**关键发现：recovery 是 model-dependent，frontier models 能部分 recover，smaller models 不能。但 recovery 不是该论文的研究目标，只是 side observation。**

- **[Fission-GRPO](https://arxiv.org/abs/2601.15625)** (arXiv, Jan 2026): 针对 tool-calling error recovery 的 RL 训练方法，通过 on-policy error augmentation + diagnostic feedback 提升 Qwen3-8B 的 error recovery rate +5.7%。**与 proposal 的关系：RA-FGRPO 直接基于此方法，从 "operational error recovery" 适配到 "safety-specific recovery"——这是一个相对 incremental 的适配。**

- **[BackBench](https://arxiv.org/abs/2604.18847)** (arXiv, Apr 2026): 50 个 post-harm recovery scenarios in OSWorld。**与 proposal 的关系：proposal 正确区分了 post-harm recovery (BackBench) 与 post-blocking recovery (theirs)，但这也暴露了 post-blocking 是一个更窄的 sub-problem。**

- **[GTPO](https://arxiv.org/abs/2511.14846)** (arXiv, Nov 2025): Turn-level reward assignment for multi-turn tool-integrated reasoning，+3.0% over GRPO。**与 proposal 的关系：被选为 RA-FGRPO 的 primary credit assignment 方法。**

- **[ToolMisuseBench](https://arxiv.org/abs/2604.01508)** (arXiv, Apr 2026): 6,800 tasks with deterministic fault injection for tool misuse and recovery。**与 proposal 的关系：operational-error counterpart。ToolMisuseBench 已经覆盖了 "recovery after tool failure" 的 benchmark 维度；proposal 的增量是 "safety policy violation" 而非 "operational failure" 作为 trigger。**

- **[Canonical Path Deviation](https://arxiv.org/abs/2602.19008)** (arXiv, Feb 2026): Off-canonical actions compound subsequent deviation by 22.7pp。**与 proposal 的关系：为 recovery difficulty 提供了理论解释——被 block 后偏离 canonical path，后续 recovery 概率急剧下降。**

- **[AIR](https://arxiv.org/abs/2602.11749)** (arXiv, Feb 2026): Post-incident response framework, >90% remediation success. **与 proposal 的关系：不同 recovery 范式，AIR 终止任务而非 resume。**

- **调研总结**：Agent safety 的 benchmark 和 guardrail 研究在 2025-2026 年爆发式增长，但 **post-blocking recovery（guardrail 成功阻断后 agent 的 replanning 能力）确实是一个尚无专门 benchmark 和训练方法的 gap**。最接近的工作是 Fission-GRPO（operational error recovery）和 Symbolic Guardrails（观测到 recovery 但未专门研究）。该 gap 的真实存在性是可信的。

---

【Trivial Alternative 检验】:

**存在 trivial alternative 威胁，但 proposal 有部分回应。**

最显然的 trivial baseline：**给 smaller model 提供 informative error messages + few-shot recovery demonstrations（in-context learning）**。Symbolic Guardrails 已经表明 informative feedback 能使 GPT-4o 从 0.36→0.48（+33% relative）。如果对 smaller models 也 simply 提供 rich error context + 几个 recovery 示例，是否就能 close 大部分 gap？

Proposal 的隐含回应是：(a) smaller models（GPT-OSS-20B, GLM-4-9B）即使有 blocking 也 near-zero recovery，说明 informative feedback alone 不够；(b) 需要专门的 RL 训练。但这个论证有漏洞——**The Verifier Tax 测试的 smaller models 是否收到了 informative feedback？如果没有，那 "informative feedback + ICL for smaller models" 这个 baseline 就尚未被排除。** 如果这个 trivial baseline 就能 close 大部分 gap，则 RA-FGRPO 的增量价值大打折扣。

**增量价值的核心在于**：(1) RecoverBench 作为专门 benchmark 的系统化评测（包括 CU 识别），(2) RA-FGRPO 相对于 informative-feedback-only 的训练增益。如果后者的增益不显著，论文会变成一个 benchmark-only paper。

---

【前提假设检验】:

核心逻辑链中有以下未验证假设：

1. **"Recovery failure 主要是 safety-specific 的，而非 general capability 不足"**：这是最关键的假设。Smaller models 的 near-zero recovery 可能不是因为缺乏 safety-specific recovery training，而是因为这些模型在 multi-step planning 上本身就弱。如果是后者，safety-specific 训练（RA-FGRPO）可能不比 general capability 提升更有效。Proposal 没有提供区分这两个原因的证据。

2. **"Fission-GRPO 从 operational errors 到 safety policy violations 的迁移是 straightforward 的"**：Proposal 将 Fission-GRPO 的 error augmentation 框架直接搬到 safety context，但 safety violations 与 operational errors 有本质区别——safety violations 涉及 policy interpretation、constraint satisfaction、multi-hop reasoning about what IS and ISN'T allowed，比 "API returned error code" 复杂得多。这个迁移的有效性是假设的。

3. **"Oracle exhaustive search 在 tau-bench 上可行"**：CU/partially-recoverable 分类依赖于 "oracle exhaustive search over constraint-satisfying action space"，但 tau-bench 的 action space 是否小到可以穷举？如果不可以，benchmark 的 ground truth 就不可靠。

---

【3 维度打分】:

1. **Novelty: 中** — 
   核心 novelty 在于识别并形式化 "post-blocking recovery" 作为一个 distinct failure mode，与 post-harm (BackBench)、post-error (Fission-GRPO/ToolMisuseBench)、post-incident (AIR)、guardrail-side correction (ReGuard/AGENT-C) 进行系统化区分。这个 taxonomy 和 gap identification 是有价值的。RecoverBench 的 dual challenge（recover + recognize unrecoverability）增加了评估深度。

   **但 novelty 受限于两点**：(a) 训练方法 RA-FGRPO 是 Fission-GRPO 的直接适配，核心创新（on-policy error augmentation + diagnostic feedback）来自 Fission-GRPO，credit assignment 来自 GTPO/AT²PO——proposal 的方法贡献更多是 **组合** 而非 **创造**；(b) benchmark 构建方法（在 tau-bench 上注入 blocks + 分类 recoverable/unrecoverable）是 relatively mechanical 的——ToolMisuseBench 在 operational domain 已经展示了类似的 deterministic fault injection methodology。

   如果核心发现是 positive（RA-FGRPO 提升 recovery），审稿人的反应更可能是 "makes sense, I would have guessed that safety-specific training helps" 而非 "surprising"。

2. **Significance: 中** — 
   Agent safety 是一个重要且时效性强的方向。Post-blocking recovery 确实是一个 practical problem：如果 guardrails 阻断 unsafe actions 但 agent 无法完成 legitimate tasks，guardrails 的 deployment value 就会受到质疑（The Verifier Tax 的核心论点）。

   **但 significance 受限于**：(a) 问题的范围较窄——只关注 tau-bench（Airline/Retail），generalizability 到其他 domain 未知；(b) 对 NLP/agent 社区的影响取决于 "recovery 是否真的需要 safety-specific 训练"——如果答案是 "general capability 提升就够了"，则 significance 大打折扣；(c) 实际影响路径不完全清晰——production 系统中 guardrail + agent 的 co-design 是一个工程问题，academic benchmark 能多大程度指导实践存疑。

3. **Related Work: 强** — 
   这是 proposal 最出色的维度。Proposal 对相关工作的覆盖非常系统化和全面：五类 recovery paradigm 的分类清晰且有依据，每篇论文的定位和差异化描述准确（经我调研验证，引用的关键论文均真实存在且描述基本准确）。Canonical Path Deviation、TraceSafe、ToolSafe 等论文的引用体现了对领域的深度理解。与 ToolMisuseBench 的 "operational vs safety" 区分、与 ReGuard/AGENT-C 的 "guardrail-side vs agent-side" 区分、与 BackBench 的 "post-harm vs post-blocking" 区分都是准确且有说服力的。

---

【概率估计】（针对适配 venue 如 EACL/AAAI/NAACL/ACL）: [22% - 32%] 中位 27%

【概率估计】（针对用户指定的 CoRL 2026）: [0% - 3%] 中位 1%
   — CoRL 明确要求 robotics focus，本 proposal 零 robotics 内容，几乎必然 desk rejection。

【估计理由】:

针对适配 NLP/AI venue 的估计（27%）：
- Related Work 是强项，表明作者对领域有深刻理解，这在审稿中会加分
- Gap identification 是真实的——post-blocking recovery 确实没有专门的 benchmark 和训练方法
- **Novelty（中）是上界限制因素**：核心方法贡献是组合式的（Fission-GRPO + GTPO + tau-bench + safety context），审稿人可能认为 methodological novelty 不足。如果 RA-FGRPO 的实验结果只是 modest improvement（类似 Fission-GRPO 的 +5.7%），paper 的 impact 会进一步受限
- **Trivial alternative 威胁真实存在**：如果 "informative feedback + ICL" 就能 close 大部分 gap for smaller models，RA-FGRPO 的必要性会被质疑。这需要在实验中明确排除
- 概率落在 25-35% 区间（"有实质内核，但核心发现 if positive 审稿人会说 'I would have guessed this'"）的下半段

针对 CoRL 的估计（1%）：纯 venue mismatch，与 idea 质量无关。

【主要风险】:

1. **"是 safety-specific 问题还是 general capability 问题？"** — 如果审稿人认为 smaller models 的 recovery failure 本质上是 multi-step planning 能力不足（而非缺乏 safety-specific recovery training），则整个 training contribution 的立论基础会被动摇。这是最致命的 idea-level 风险。

2. **方法 novelty 不足** — RA-FGRPO = Fission-GRPO（已发表）+ GTPO credit（已发表）+ safety context（domain adaptation）。审稿人可能判定这是 "engineering contribution"（将现有方法 apply 到新 domain）而非 "methodological contribution"。如果是 benchmark-only paper（RecoverBench），则 benchmark 的规模（仅 tau-bench 的 Airline + Retail 两个 domain）和 task diversity 可能被认为不足。
```

Sources:
- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)
- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)
- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)
- [BackBench (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)
- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)
- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/abs/2604.01508)
- [Canonical Path Deviation (arXiv 2602.19008)](https://arxiv.org/abs/2602.19008)
- [AIR (arXiv 2602.11749)](https://arxiv.org/abs/2602.11749)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328) (Mar 2026): 
   验证了 runtime safety enforcement 对 task completion 的代价。GPT-OSS-20B/GLM-4-9B 在 tau-bench 上 SSR<5%，recovery rates 21%→~0%。论文存在且核心数据与 proposal 描述一致。这是 proposal 的主要 motivation source。

2. [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579) (Apr 2026): 
   对 80 个 agent safety benchmark 做 systematic review，评估 symbolic guardrails 对 safety/utility 的影响。GPT-4o 在 informative blocking feedback 下 pass rate 0.36→0.48。关键点：该论文**已经隐式测量了 recovery**（pass rate improvement IS recovery），只是未将其作为 first-class metric。Proposal 的核心 novelty claim（"no existing work isolates post-blocking recovery"）需要相对于这篇论文 justify 增量。

3. [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625) (Jan 2026): 
   on-policy error augmentation 训练 tool-calling error recovery，Qwen3-8B recovery rate +5.7%。proposal 的 RA-FGRPO 本质上是 Fission-GRPO 在 safety domain 的 adaptation + GTPO credit assignment。方法论上的增量有限。

4. [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/pdf/2604.01508) (Apr 2026): 
   6800 tasks，deterministic fault injection，budgeted efficiency metric。Proposal 承认与其 "methodologically adjacent"，区别仅在 fault 类型（operational vs. safety-policy）。这意味着 proposal 的 benchmark design 在结构上与 ToolMisuseBench 高度重叠，区别仅在于 inject 的是 safety block 而非 operational error。

5. [Recovery-Bench (Letta, OpenReview)](https://openreview.net/forum?id=8FZRnDgDxq) (2026): 
   **Proposal 完全未引用的直接竞争工作。** Recovery-Bench 测量 agent 从 mistakes 和 corrupted context 中的恢复能力。虽然不聚焦 safety，但在 "agent recovery benchmark" 这个 niche 上直接竞争。GPT-5 在 recovery 场景表现显著不同于 clean 场景。

6. [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738) (Dec 2025, ICLR 2026 Workshop): 
   guardrail-side correction via constrained decoding，100% safety conformance + utility improvement。Proposal 将其归为 "complementary"，但审稿人可能会问：如果 guardrail 能直接生成 compliant alternative（AGENT-C 的做法），为什么还需要训练 agent 做 recovery？

7. [BackBench (arXiv 2604.18847)](https://arxiv.org/html/2604.18847v1) (Apr 2026): 
   50 post-harm recovery scenarios in OSWorld。Proposal 对其定位清晰（post-harm vs. post-blocking），差异化成立。

8. [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846) (Nov 2025, revised Apr 2026): 
   turn-level reward assignment，+3.0% over GRPO。Proposal 将其用作 primary credit assignment，但 GTPO 本身并非 safety-aware，adaptation 的技术贡献不明确。

9. [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers): 
   **CoRL 2026 明确要求 "focus on a core robotics problem" 和 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。** Topics 包括 robot manipulation, navigation, locomotion, driving, flight — 全部是物理机器人学习。

- **调研总结**: Agent safety recovery 是 2026 上半年的活跃研究方向，已有多个 benchmark（ToolMisuseBench、Recovery-Bench、BackBench）和训练方法（Fission-GRPO、GTPO）覆盖了不同方面。Proposal 的定位是在 "post-blocking" 这个细分 niche 填补空白，但该 niche 与 "post-error recovery" 的边界较模糊。**最关键的问题是：这是一个 NLP/agent safety proposal，与 CoRL（机器人学习会议）的 scope 完全不匹配。**


【⚠️ 致命问题：venue mismatch】

在进入 3 维度评估之前，必须指出一个**与 idea 质量无关但对中稿概率有决定性影响的事实**：

**这个 proposal 与 CoRL 2026 的 scope 完全不匹配。**

- CoRL 要求 "submissions should focus on a core robotics problem"
- CoRL 要求 "real-robot experiments or convincing evidence of sim-to-real transfer"
- CoRL 的 topics 包括 manipulation, navigation, locomotion, driving, flight — 全部是物理机器人
- 本 proposal 是关于 text-based customer service agent（tau-bench Airline/Retail）的 tool-use safety recovery，无任何物理机器人组件
- Proposal 自身列出的 target venues 也是 EACL/AAAI/NAACL（NLP venues），进一步证实 scope 不匹配

**这不是 idea 质量问题，是 scope 问题。** CoRL 的 area chair 极大概率会在 desk review 阶段直接拒稿，甚至不进入 peer review。

以下 3 维度评估基于 idea 本身的学术质量（而非 venue fit），但概率估计会反映 CoRL 的 scope 要求。


【Trivial Alternative 检验】:

存在多个成本更低的替代方案：

1. **Prompt engineering / few-shot recovery demos**: 在 blocking message 中附上 few-shot 示例，教 agent 如何 replan。不需要任何训练。Symbolic Guardrails 已经证明 informative feedback 能将 GPT-4o pass rate 提升 33%，说明很大一部分 recovery 问题可以通过更好的 feedback 信息解决，而不需要 dedicated training。

2. **Guardrail-side correction（AGENT-C）**: 直接在 guardrail 层面生成 compliant alternative，agent 完全不需要 replan。AGENT-C 已经实现 100% safety + utility improvement。如果 guardrail 能直接修正 action，为什么要训练 agent 自己做 recovery？Proposal 称 "complementary"，但缺乏证据说明在什么场景下 guardrail-side correction 不够用。

3. **直接在 Fission-GRPO 训练中 inject safety blocks**: 把 safety blocks 作为 error 的一个子类型，直接复用 Fission-GRPO 的 pipeline。不需要设计新的 RA-FGRPO。

增量价值主要在于：(a) "correctly unrecoverable" 场景的识别，(b) False Recovery Rate 指标（检测 constraint gaming）。这两点确实是 trivial alternatives 无法覆盖的，是 proposal 的真正 delta。但这个 delta 是否足以支撑一整篇论文，值得商榷。


【前提假设检验】:

核心逻辑链中有以下未验证假设：

1. **"Post-blocking recovery 是 agent 缺乏的一种 distinct skill，需要 dedicated training"**: 这是最核心的假设。替代假设是 recovery 能力随 general reasoning 能力自然提升（GPT-5 的 recovery 比 GPT-4o 好就暗示了这一点），不需要 dedicated training。Proposal 没有排除这个替代假设。

2. **"Open-source models 的 recovery gap 主要源于缺乏 safety-specific recovery training signal"**: 替代解释是 open-source models 的 general instruction following 和 reasoning 能力不足（The Verifier Tax 提到 SSR<5% 本身可能反映 general capability gap）。如果根本原因是 general capability，safety-specific training 不会有效。

3. **"在 tau-bench Airline/Retail 上的 recovery improvement 可以 generalize 到其他 domains"**: Proposal 只在两个 customer service domain 上构建 benchmark 和训练。Recovery 在这些特定 domain 的 improvement 可能高度 domain-specific（利用特定 airline/retail policy 结构），不一定 generalize。

4. **"SRS 的 safe alternative enumeration 不会 leak oracle information"**: Proposal 声称 "we provide WHICH actions are available but NOT which specific sequence solves the task"，但在 tau-bench 这种 constrained environment 中，available actions list 本身可能就高度 informative（等价于严重 hint），使得训出来的 recovery 能力是 benchmark-specific 的，而非 generalizable 的。


【3 维度打分】:

1. **Novelty: 弱-中** — 

   核心 insight（"agent 需要在 guardrail block 后 recover"）虽然在 framing 上是新的，但本质上与 post-error recovery（Fission-GRPO, ToolMisuseBench）高度类似。剔除 surface differences 后，novelty delta 主要集中在两点：(a) "correctly unrecoverable" 分类和 URR 指标，(b) False Recovery Rate 检测 constraint gaming。这两点有真实价值，但不足以支撑 "strong novelty" 的 claim。

   具体对比：
   - vs. Fission-GRPO：RA-FGRPO ≈ Fission-GRPO + GTPO credit + safety-specific blocks。方法论增量有限。
   - vs. ToolMisuseBench：RecoverBench ≈ ToolMisuseBench 的 benchmark design paradigm + safety blocks instead of operational faults。
   - vs. Symbolic Guardrails：Recovery measurement ≈ Symbolic Guardrails 的 pass rate delta 的更细粒度版本。
   - vs. Recovery-Bench (Letta)：在 "agent recovery benchmark" 这个 niche 上直接竞争，且 proposal 未引用。
   
   Proposal 的 taxonomy（5 种 recovery 类型）是有组织价值的，但 taxonomy 本身不算 technical novelty。

2. **Significance: 弱-中** — 

   对 NLP/agent safety 社区：问题是真实的（agents 确实在 block 后 recovery 困难），但研究的 scope 非常窄（只在 tau-bench 两个 domain，只针对 open-source models），实际影响力有限。更重要的是：如果 base model capability 是 recovery 的主要瓶颈（GPT-5 > GPT-4o > open-source 的梯度暗示了这一点），那么 dedicated recovery training 可能很快被更强的 base models 淘汰。
   
   对 CoRL/robotics 社区：**零相关性**。Proposal 不涉及任何物理机器人、embodied agent、sim-to-real transfer、manipulation/navigation/locomotion。tau-bench 的 Airline/Retail domain 是纯文本客服场景。

3. **Related Work: 强（对 NLP venues）/ 致命（对 CoRL）** — 

   Proposal 对 NLP agent safety 领域的 related work 覆盖极其充分（30+ 引用），taxonomy 清晰，差异化定位 well-articulated。唯一的显著遗漏是 Letta 的 Recovery-Bench。
   
   但对 CoRL 而言，related work 完全没有涉及 robotics recovery literature（如 robot error recovery, manipulation failure recovery, safe RL for robotics），这进一步暴露了 venue mismatch。


【概率估计】: [1% - 5%] 中位 2%

【估计理由】: 

**概率极低的决定性因素不是 idea 质量，而是 venue scope mismatch。** 

CoRL 2026 明确要求 "focus on a core robotics problem" 和 real-robot experiments。本 proposal 是一个纯 NLP/agent safety 工作（text-based customer service tool-use），与机器人学习完全无关。极大概率在 desk review 阶段被拒，甚至不进入 peer review。

如果假设投稿到 proposal 自身列出的 NLP venues（EACL/AAAI/NAACL via ARR），idea 质量的概率估计会在 **[18% - 30%] 中位 22%** 的范围——idea 方向站得住脚但内核偏薄：novelty delta 有限（safety-specific recovery vs. general error recovery 的边界模糊），存在 trivial alternative 威胁（guardrail-side correction, better prompting），核心前提假设（recovery 需要 dedicated training 而非 general capability improvement）未经验证。即便在 NLP venues，审稿人看到 positive results 可能会说 "makes sense, I would have guessed that training on recovery would help recovery"，而不是 "surprising"。

【主要风险】:

1. **CoRL 投稿：Desk reject due to scope mismatch（致命风险）** — 这是一个纯文本 tool-use agent safety 的工作，CoRL 不接收此类论文。Proposal 自身的 target venues 也没有列 CoRL，列的是 EACL/AAAI/NAACL。建议投稿到 NLP 或 AI safety venues。

2. **即便换到 NLP venues：Core novelty 被 challenge** — 审稿人很可能提出 "post-blocking recovery 与 post-error recovery 有什么本质区别？为什么不直接扩展 Fission-GRPO / ToolMisuseBench？" 以及 "AGENT-C 这样的 guardrail-side correction 能否直接解决你的问题，不需要 agent-side training？" 这两个问题 proposal 目前的回答不够有力。
```

---

**补充说明**：

本 proposal 的形式完善度极高——30+ 引用、5 种 recovery 类型 taxonomy、5 个评估指标、tiered credit assignment、详细 ablation plan。但形式完善度不等于 idea 质量。透过形式看：核心发现如果是 positive（"safety-specific recovery training 提升了 open-source models 的 recovery rate"），审稿人的反应更可能是 "I would have guessed this" 而非 "surprising"。

**对后续流程的建议**：如果要继续审，应首先确认 venue 选择——投 CoRL 几乎可以确定被拒。如果改投 NLP venues，idea 有一定潜力但需要发掘 agent 帮助强化 core novelty delta（特别是 "correctly unrecoverable" recognition 和 False Recovery Rate 这两个真正有新意的点），同时补救 agent 需要解决 trivial alternative 威胁和核心前提假设问题。

Sources:
- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)
- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)
- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)
- [ToolMisuseBench (arXiv 2604.01508)](https://arxiv.org/pdf/2604.01508)
- [Recovery-Bench (OpenReview)](https://openreview.net/forum?id=8FZRnDgDxq)
- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)
- [BackBench (arXiv 2604.18847)](https://arxiv.org/html/2604.18847v1)
- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [tau-bench (arXiv 2406.12045)](https://arxiv.org/abs/2406.12045)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【致命前置问题：venue 匹配性】

本 proposal 投稿目标是 CoRL 2026（Conference on Robot Learning）。然而：

1. CoRL 2026 CFP 明确声明："submissions without a robotics focus will be returned without review"。
2. 本 proposal 的全部内容是 LLM agent 在 airline/retail 客服场景中的 tool-use 安全恢复——没有任何机器人操控、导航、感知、仿真迁移、物理交互等 robotics 内容。
3. Proposal 自身列出的 Target Venues 是 EACL 2027、AAAI 2027、NAACL 2027——全部是 NLP/AI 会议，完全没有提到 CoRL。
4. CoRL 2025 的 accepted papers 几乎全部涉及物理机器人学习（manipulation、locomotion、sim-to-real），不存在纯 NLP agent tool-use safety 论文被接收的先例。

**结论：这是一个 scope 层面的致命不匹配。即使 idea 本身质量优秀，在 CoRL 主会也几乎必然被 desk reject。** 以下评估仍会对 idea 本身的质量进行客观打分，但概率估计必须反映 venue 不匹配这一事实。

---

【领域调研】:

- [The Verifier Tax (arXiv 2603.19328, Mar 2026)](https://arxiv.org/abs/2603.19328): 本 proposal 的核心动机论文。在 tau-bench 上量化了 safety mediation 的代价：即使阻断率达 94%，SSR（严格安全成功率）仍低于 5%，recovery rate 从 21%（简单 Airline 任务）降至近 0%（复杂 Retail 场景）。Proposal 对该论文的引用和描述准确。
  
- [Symbolic Guardrails (arXiv 2604.15579, Apr 2026)](https://arxiv.org/abs/2604.15579): Proposal 的第二核心动机论文。在 τ²-bench 上展示了 symbolic guardrails 提供 informative blocking feedback 后，GPT-4o pass rate 从 0.36 提升到 0.48。但该论文的主要贡献是 guardrail 设计而非 recovery 研究，recovery 只是被观察到的 side effect。Proposal 的描述基本准确。

- [BackBench (arXiv 2604.18847, Apr 2026)](https://arxiv.org/abs/2604.18847): 50 个 post-harm recovery 场景（OSWorld/GUI），与本 proposal 的 post-blocking recovery 确实属于不同范畴。Proposal 的区分合理。

- [Fission-GRPO (arXiv 2601.15625, Jan 2026)](https://arxiv.org/abs/2601.15625): 训练 tool-calling error recovery 的 RL 方法，在 BFCL v4 上提升 5.7% recovery rate。这是本 proposal 训练方法 RA-FGRPO 的直接基础——RA-FGRPO 本质是 Fission-GRPO 在 safety block 场景的领域适配。

- [GTPO (arXiv 2511.14846, Nov 2025)](https://arxiv.org/abs/2511.14846): Turn-level credit assignment 方法，比 GRPO +3.0%。作为 RA-FGRPO 的 credit assignment 组件被引用，描述准确。

- [ReGuard (arXiv 2510.13727, Oct 2025)](https://arxiv.org/abs/2510.13727): Guardrail-side 控制理论方法，在 driving/e-commerce 场景注入纠正动作。Proposal 正确区分了 agent-side replanning vs. guardrail-side correction。

- [AGENT-C (arXiv 2512.23738, Dec 2025)](https://arxiv.org/abs/2512.23738): Token-level constrained decoding 实现 100% safety conformance + utility 提升（Claude Sonnet 4.5: 71.8%→75.2%）。这是 proposal 最强的 trivial alternative 竞争者。

- [ToolMisuseBench (arXiv 2604.01508, Apr 2026)](https://huggingface.co/datasets/sigdelakshey/ToolMisuseBench): 6800 task 的 operational error recovery benchmark。与本 proposal 的区别在于 fault 类型（operational vs. safety policy），但方法论高度相似。

- 调研总结: Agent safety 领域在 2025-2026 年爆发式增长，围绕 guardrail 的工作已形成完整生态：blocking（TraceSafe, ATBench）、guardrail-side correction（AGENT-C, ReGuard）、post-error recovery（Fission-GRPO, ToolMisuseBench）、post-harm recovery（BackBench）。本 proposal 定位在 "post-blocking agent-side recovery" 这一具体 niche，确实是一个尚未被独立 benchmark 覆盖的子问题，但其独立存在的价值取决于 agent-side recovery 相比 guardrail-side correction 的增量贡献是否充分。

---

【Trivial Alternative 检验】:

存在两个显著的 trivial alternative 威胁：

1. **AGENT-C 已经"解决"了这个问题的大部分**：AGENT-C 通过 constrained decoding 在 guardrail 端实现 100% safety conformance + utility 提升。如果 guardrail 本身就能纠正不安全动作并保持 utility，为什么还需要训练 agent 学会 replanning？Proposal 承认两者 complementary，但没有论证在 AGENT-C 已部署的情况下，agent-side recovery 的剩余价值有多大。

2. **Simply providing better error messages（Symbolic Guardrails 已有的发现）**：Symbolic Guardrails 已经展示了 informative blocking feedback 让 GPT-4o 从 0.36 提升到 0.48——不需要任何新 benchmark 或 training method。本 proposal 的 RecoverBench 在 diagnostic feedback 条件下测试的效果，可能大部分归因于 feedback quality 而非 agent 训练。

3. **Fission-GRPO 直接应用**：Fission-GRPO 已经训练 error recovery。将 safety block 当作一种特殊的 execution error，直接用 Fission-GRPO 训练（不需要 RA-FGRPO 这个"安全特化"版本），可能效果差距不大。

增量价值的论点：Proposal 的真正增量在于 (a) dual-challenge 设计（recoverable + unrecoverable 分类）和 (b) 系统化测量 recovery 质量的 5 个 metrics。但这更多是 benchmark engineering 的贡献，而非概念突破。

---

【前提假设检验】:

核心 claim 逻辑链中有几个未经验证的假设：

1. **"Post-blocking recovery 是一个独立的、值得单独建 benchmark 的 failure mode"** — 这是本 proposal 最核心的前提假设。但 Symbolic Guardrails 已经在 guardrail evaluation 的框架下 incidentally 测量了 recovery（pass rate 变化），且 AGENT-C 通过 guardrail-side correction 可能使 agent-side recovery 变得不那么重要。这个 failure mode 是否"独立"到值得专门研究，取决于 guardrail-side correction 是否已经足够好——如果 AGENT-C 类方法部署后 recovery 问题大幅缓解，这个 benchmark 的长期价值会打折。

2. **"Open-source model 的 recovery gap 可以通过 RA-FGRPO 训练来弥合"** — 这建立在假设 recovery 是一个可以通过 RL fine-tuning 显著提升的 capability 之上。但 The Verifier Tax 显示 open-source model 的 SSR < 5%，recovery near 0%——这可能不是 "缺少 recovery 训练" 的问题，而是这些模型（GPT-OSS-20B, GLM-4-9B）的基础能力（planning, reasoning）不足以支撑 multi-step replanning。如果基础能力是瓶颈，单独训练 recovery 可能收效甚微。

3. **"Unrecoverable recognition（URR）是 agent 可以学会的"** — 判断一个任务在 policy constraints 下是否无解，本质上是一个 constraint satisfaction 推理问题。小模型（3B-4B active parameters）是否有足够的推理能力学会这一点是存疑的。

---

【3 维度打分】:

1. **Novelty: 弱-中** — Proposal 的核心 novelty 在于提出 "post-blocking recovery" 作为独立 failure mode 并构建专门 benchmark。但：
   - 对 recovery 的观测已在 Symbolic Guardrails 和 The Verifier Tax 中存在，只是没有被显式命名为独立 benchmark target
   - RecoverBench 的构建方法（在 tau-bench 上注入 guardrail blocks）是直接的工程工作，不涉及新方法论
   - RA-FGRPO = Fission-GRPO + GTPO credit + safety block 场景适配，是现有方法的直接组合
   - 真正的 novelty delta：(a) dual-challenge 设计（recover + recognize unrecoverable）有一定价值，(b) 5 个 metrics 的系统化设计（尤其 FRR 测量 constraint gaming）有实用意义，(c) feedback informativeness 作为实验维度有 analytical value。但这些更接近 benchmark engineering 贡献而非 conceptual breakthrough。

2. **Significance: 中** — 问题本身确实重要——agent safety 是热门方向，recovery gap 是真实存在的问题（有 The Verifier Tax 的实证支持）。但 significance 受限于：
   - AGENT-C 类 guardrail-side correction 可能使 agent-side recovery 训练的实际部署需求降低
   - 结果如果 positive（RA-FGRPO 提升了 open-source model 的 recovery），审稿人更可能说 "I would have guessed that RL training helps" 而非 "surprising"
   - Benchmark 局限于 tau-bench（Airline + Retail 两个领域），generalizability 有限
   - 对 NLP/AI 领域有中等影响力；对 robotics 领域几乎无影响力

3. **Related Work: 强** — 这是 proposal 最突出的优点。Related work 覆盖极其全面，taxonomy 清晰（5 类 recovery paradigm + guardrail-side correction），对每篇工作的区分精确。Post-blocking recovery vs. post-harm recovery vs. post-error recovery vs. post-incident response vs. guardrail-side correction 的分类有独立价值。对 Symbolic Guardrails、The Verifier Tax、BackBench、Fission-GRPO、ReGuard、AGENT-C 的定位都准确且有实质性区分。

---

【概率估计】: [0% - 3%] 中位 1%

【估计理由】:

**这个概率估计几乎完全由 venue 不匹配决定。**

CoRL 是 Conference on Robot Learning，其 CFP 明确要求 robotics focus，且声明 "submissions without a robotics focus will be returned without review"。本 proposal 是一个纯 NLP/AI agent tool-use safety 工作，在 airline/retail 客服 API 场景中运行，不涉及任何机器人学习内容——没有物理交互、没有感知、没有 manipulation、没有 sim-to-real、没有 embodied agent。这是一个近乎确定的 desk reject。

**如果改投 proposal 自身列出的 target venues（EACL/AAAI/NAACL），idea 本身的质量估计大致在 20-30% 范围**：
- Novelty 弱-中（组合性贡献，benchmark engineering 为主）限制了上界
- Significance 中（问题重要但 trivial alternative 威胁显著）
- Related Work 强（对下限有支撑）
- 核心风险在于 AGENT-C 和 Symbolic Guardrails informative feedback 作为 trivial alternative 会被审稿人质疑

但对于 CoRL 2026 主会，概率实质为 0-3%。

【主要风险】:
1. **致命 venue 不匹配**：CoRL 要求 robotics focus，本 proposal 没有任何 robotics 内容，几乎必然 desk reject
2. **Trivial alternative 威胁**（假设投向 NLP venue）：AGENT-C 的 guardrail-side correction 已实现 100% safety + utility 提升，reviewer 会质疑 agent-side recovery training 的增量价值；Symbolic Guardrails 的 informative feedback 已展示 partial recovery，reviewer 会问 "为什么不直接改善 feedback 质量"
```

---

**补充建议**：如果作者认为这个 idea 有价值，应该投向自身已列出的 NLP/AI venues（EACL 2027 via ARR、AAAI 2027、NAACL 2027），而非 CoRL。如果一定要投 CoRL，需要彻底重构 proposal：将 recovery 问题迁移到 robotics 场景（如 embodied agent 在物理环境中被 safety guardrail 阻断后的 replanning），使用机器人仿真环境而非 tau-bench API 场景。但这本质上是一个完全不同的 paper。

Sources:
- [The Verifier Tax (arXiv 2603.19328)](https://arxiv.org/abs/2603.19328)
- [Symbolic Guardrails (arXiv 2604.15579)](https://arxiv.org/abs/2604.15579)
- [BackBench (arXiv 2604.18847)](https://arxiv.org/abs/2604.18847)
- [Fission-GRPO (arXiv 2601.15625)](https://arxiv.org/abs/2601.15625)
- [GTPO (arXiv 2511.14846)](https://arxiv.org/abs/2511.14846)
- [ReGuard (arXiv 2510.13727)](https://arxiv.org/abs/2510.13727)
- [AGENT-C (arXiv 2512.23738)](https://arxiv.org/abs/2512.23738)
- [ToolMisuseBench](https://huggingface.co/datasets/sigdelakshey/ToolMisuseBench)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Homepage](https://www.corl.org/)


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
  "promptId": "e1c670b7-94e6-4cf0-88fb-730734bf428d",
  "type": "user",
  "uuid": "c8598713-b6db-4d9a-a2aa-49b6bc53335c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:32:00.918Z_

```json
{
  "parentUuid": "c8598713-b6db-4d9a-a2aa-49b6bc53335c",
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
  "uuid": "962978ed-aba2-4220-83a9-2b4fb785f499",
  "timestamp": "2026-05-20T03:32:00.918Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:32:00.918Z_

```json
{
  "parentUuid": "962978ed-aba2-4220-83a9-2b4fb785f499",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "def80eff-d602-4df2-b67d-f2603fd37ba8",
  "timestamp": "2026-05-20T03:32:00.918Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough research to produce a thorough, evidence-bas…",
  "leafUuid": "def80eff-d602-4df2-b67d-f2603fd37ba8",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Assess agent recovery benchmark and training method proposal",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:32:37.678Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewers' assessments systematically to produce the Meta Judge output.

## Extracting Key Data

### Reviewer 1:
- Novelty: 中
- Significance: 中
- Related Work: 强
- CoRL probability: [0% - 3%] 中位 1%
- NLP venue probability: [22% - 32%] 中位 27%
- Key risks: safety-specific vs general capability question; method novelty insufficient (combinatorial)
- Noted venue mismatch as fatal

### Reviewer 2:
- Novelty: 弱-中


- Significance: 弱-中
- Related Work: 强 (for NLP) / 致命 (for CoRL)
- CoRL probability: [1% - 5%] 中位 2%
- NLP venue probability: [18% - 30%] 中位 22%
- Key risks: venue mismatch (fatal); trivial alternatives (AGENT-C, informative feedback); Recovery-Bench (Letta) not cited
- Noted venue mismatch as fatal

### Reviewer 3:
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- CoRL probability: [0% - 2%] 中位 1%
- NLP venue probability: [25% - 35%] 中位 30%
- Key risks: limited scope; lacks depth in analysis; missing comparisons with related work
- Noted venue mismatch as fatal

Now I'm aggregating the venue probabilities across reviewers. The CoRL assessments are consistently low at 1-2%, while NLP venues show stronger potential around 22-30%. For NLP specifically, the reviewers estimate roughly 20-30% acceptance likelihood, with R3 suggesting the upper end of that range. The fatal venue mismatch concern appears across multiple reviews, which is a critical issue to address.

Looking at the rubric dimensions for NLP venues, there's general agreement that novelty falls in the weak-to-medium range, with two reviewers leaning toward weak-to-medium and one toward medium. On significance, the consensus tilts slightly higher—two reviewers rate it as medium while one says weak-to-medium, so medium seems like the stronger assessment.

All three reviewers unanimously praise the related work section as strong. Across the board, there are five major shared concerns: the fundamental venue mismatch that's fatal for CoRL, the observation that RA-FGRPO is essentially a combination of existing methods (Fission-GRPO, GTPO, and safety context), and three trivial alternatives that all reviewers identified—informative feedback through prompting, AGENT-C's guardrail-side correction approach, and the underlying question of whether the method addresses safety-specific challenges or just general capability improvements.

Additionally, all three note that the positive results feel unsurprising given prior work, the evaluation is narrowly scoped to just tau-bench's airline and retail domains, and there's uncertainty about whether recovery failures are truly safety-specific phenomena.

A few points stand out as raised by only one reviewer: the missing citation of Recovery-Bench from Letta work, a concern about whether the SRS safe alternative enumeration could leak oracle information, and R1's emphasis on canonical path deviation as supporting evidence—though the others don't highlight this as strongly.

The consensus for CoRL is decisive and negative.

For NLP venues where this work actually belongs, the three reviewers converge around 22-27% acceptance probability with minimal disagreement, suggesting this is where the paper's real assessment lies rather than at a robotics venue. Both show strong reviewer agreement. Now I need to pull together the implementation details from the proposal's resource section and what the reviewers noted, then compile everything into the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "def80eff-d602-4df2-b67d-f2603fd37ba8",
  "isSidechain": false,
  "requestId": "req_011CbD7f9aj8kbevcj8ed7fk",
  "type": "assistant",
  "uuid": "1d59655c-dd72-4ec4-8ae3-c0cf839ab1fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcMD6gFyWC1yxPJKVHpWqk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22565,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4275,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22565
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

_source line 9 · 2026-05-20T03:33:35.636Z_

【阶段】: Meta Judge

【三次中位（CoRL 2026）】: [1%, 2%, 1%] std≈0.5%
【三次中位（NLP适配venue，参考值）】: [27%, 22%, 25%] std≈2.1%

【共识维度】:
- **Venue Mismatch = 致命**（3/3）：CoRL 要求 robotics focus，proposal 零 robotics 内容，几乎确定 desk reject。Proposal 自身列出的 target venues 也全是 NLP 会议（EACL/AAAI/NAACL），进一步佐证。这是所有审稿人最强共识，与 idea 质量无关。
- **Related Work = 强**（3/3）：30+ 引用，5 类 recovery paradigm taxonomy 清晰准确，差异化定位 well-articulated。三位审稿人一致认为这是 proposal 最突出的优点。
- **Method Novelty 受限 = 弱-中至中**（3/3）：RA-FGRPO = Fission-GRPO（已发表）+ GTPO credit（已发表）+ safety context（domain adaptation），是组合式贡献而非方法论创新。三位审稿人均指出这一点。
- **Trivial Alternative 威胁显著**（3/3）：(a) AGENT-C guardrail-side correction 已实现 100% safety + utility 提升；(b) Symbolic Guardrails 的 informative feedback 已展示 partial recovery（+33% relative for GPT-4o）；(c) Fission-GRPO 直接应用（safety block 作为 error 子类型）。三位审稿人均认为增量价值论证不充分。
- **核心前提假设未验证**（3/3）：recovery failure 是 safety-specific 的还是 general capability 不足？GPT-5 > GPT-4o > open-source 的梯度暗示可能是后者。若是 general capability 问题，dedicated safety-specific training 的立论基础被动摇。
- **结果可预测性 = "I would have guessed this"**（3/3）：如果 RA-FGRPO positive，审稿人反应更可能是 "makes sense" 而非 "surprising"。
- **Scope 窄**（3/3）：仅 tau-bench Airline + Retail 两个 domain，generalizability 未知。
- **Significance = 弱-中至中**（3/3）：问题真实但 trivial alternative 威胁和 scope 限制压低了影响力（R1: 中, R2: 弱-中, R3: 中）。

【异常维度】:
- **Recovery-Bench (Letta, OpenReview) 未引用**（仅 R2 提及）：R2 指出 Recovery-Bench 在 "agent recovery benchmark" niche 上直接竞争，proposal 完全未引用。若属实，这是 Related Work 的显著遗漏，但不改变总体"强"评价，降级为"强-"。
- **SRS alternative enumeration 可能 leak oracle info**（仅 R2 提及）：tau-bench 受限环境中 available actions list 可能高度 informative，使 recovery 能力变为 benchmark-specific。这是一个有效但不致命的技术质疑。
- **Oracle exhaustive search 可行性**（仅 R1 提及）：CU/partially-recoverable 分类依赖 oracle exhaustive search，但 action space 是否可穷举存疑。

【最终概率】: [0% - 3%] 中位 1%

【一致性】: 高（CoRL 概率 std≈0.5%，三方对 venue mismatch 判定完全一致）

【综合理由】:

**CoRL 2026 概率（1%）的推导逻辑：**

三位审稿人在 venue mismatch 问题上达成了最高等级的共识——std 仅 0.5%，判决完全一致。CoRL 2026 CFP 明确声明 "submissions without a robotics focus will be returned without review"，而本 proposal 是纯文本 tool-use agent safety 工作（tau-bench Airline/Retail 客服场景），零 robotics 内容——没有物理交互、没有感知、没有 embodied agent、没有 sim-to-real、没有 manipulation/navigation/locomotion。Proposal 自身列出的 target venues 也全是 NLP 会议。这是一个 scope 层面的致命不匹配，几乎必然 desk reject。

因此，中位取 1%（保留极小概率应对 "area chair 误读分配" 等极端情况），上界不超过 3%。**此概率与 idea 质量无关。**

**NLP 适配 venue 概率（参考值）：**

若改投 EACL/AAAI/NAACL，三位审稿人的估计为 27%/22%/25%，std≈2.1%，属高一致。取中位附近略偏保守：**[20% - 28%] 中位 24%**。理由：
- idea 天花板由 Novelty（弱-中至中）和 Significance（弱-中至中）决定，上界约 30%
- Related Work 强为下限提供支撑，但无法弥补方法论 novelty 不足
- Trivial alternative 威胁和核心前提假设问题是审稿人最可能的 reject reason
- 偏向更严格的 R2（22%），因为 R2 发现了 Recovery-Bench 未引用这一具体遗漏，调研更细致

【建议】: KILL（针对 CoRL 2026）；边缘（针对 NLP venues，需显著强化 novelty delta 和 trivial alternative 回应）

【实施评估】:
- 计算资源: ~1,100-1,500 H100 GPU hours（benchmark 构建含 oracle 轨迹计算 ~250h，RA-FGRPO 训练含 online rollouts ~450h，评估 sweeps ~200h，ablations ~200h），预估 GPU 成本 $2,200-$3,000（H100 spot pricing）。规模适中，非计算受限项目。
- 数据需求: 基于 tau-bench（ICLR 2025，公开可得）的 Airline + Retail 两个 domain。需要从 tau-bench domain policy files 提取约束并构建 oracle safe trajectories。不需额外私有数据。
- 人工介入: CU（correctly unrecoverable）场景分类需要人工或半自动验证；SRS 的 constraint extraction 模块可能需要领域专家审核。Proposal 声称 oracle exhaustive search 可自动完成，但可行性存疑（R1 异常维度）。估算 ~2-4 人周人工标注/验证。
- 训练需求: 需要训练 Qwen3.6-35B-A3B（3B active params）和 Qwen3-4B 两个模型。RA-FGRPO 含 online rollouts + Fission resampling（G'=4），训练复杂度中等。需要 ablation 对比 vanilla GRPO、offline DPO、AT²PO credit、GAGPO credit 等 ~6 个变体。
- 新 Benchmark: 需要构建 RecoverBench（核心贡献之一）。基于 tau-bench 注入 guardrail blocks + 三级 feedback + 三类任务分类。benchmark 构建本身是主要工程工作量。
- 预估周期: 10-16 周（取决于自动化程度）。Proposal 自身估计 human-in-loop 10-12 周，auto-research 6-8 周。ARR Aug 3 deadline 给出约 11 周窗口，时间紧但可行（仅限 benchmark + 训练的核心实验，cross-benchmark 比较推迟至 NAACL 版本）。

---

**对后续流程的明确建议：**

1. **CoRL 2026 投稿应直接放弃**，这不是 idea 质量问题，是 scope 致命不匹配。三位审稿人一致确认。
2. **若改投 NLP venues（EACL/AAAI/NAACL）**，当前中位约 24%，属于"边缘"区间。进入迭代优化有意义，但需要重点强化：(a) Novelty delta——特别是 dual-challenge（recover + recognize unrecoverable）和 FRR（constraint gaming 检测）这两个真正有差异化的点；(b) 系统性回应 trivial alternative 威胁——需要在实验设计中明确排除 informative feedback alone、AGENT-C style correction、vanilla Fission-GRPO 等 baseline 能 close 大部分 gap 的可能性；(c) 回应核心前提假设——设计实验区分 "safety-specific skill deficit" vs "general capability deficit"。
3. **若要进入迭代**，建议系统将 venue 从 CoRL 2026 调整为 proposal 自身列出的 NLP venues，否则任何 idea 层面的优化都无法改变 desk reject 的结局。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d59655c-dd72-4ec4-8ae3-c0cf839ab1fe",
  "isSidechain": false,
  "requestId": "req_011CbD7f9aj8kbevcj8ed7fk",
  "type": "assistant",
  "uuid": "d44f0676-202c-4c99-89cb-3b456d2876cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcMD6gFyWC1yxPJKVHpWqk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22565,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4275,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 22565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22565
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have enough research to produce a thorough, evidence-bas…",
  "leafUuid": "d44f0676-202c-4c99-89cb-3b456d2876cd",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Assess agent recovery benchmark and training method proposal",
  "sessionId": "ec86b9d5-60f3-40aa-8a7e-07272460d8cf"
}
```

---
