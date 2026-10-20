# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/bf23ecc5-764f-4ec9-88b0-f175a21f334c.jsonl`
- **Structured JSON:** [`b6fa9938c45655855591.json`](../../sessions/b6/b6fa9938c45655855591.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T20:52:44.861Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T20:52:44.861Z",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前提问题 — 会场匹配】:\n在进入 idea 质量评估之前，必须首先指出一个致命的会场匹配问题：\n\nCoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：\n• \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n• \"Submissions without a robotics focus will be returned without review.\"\n• \"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\"\n\n本 proposal 的内容是 LLM 多轮对话安全、注意力机制、越狱防御——**完全没有任何机器人学内容**。使用的 benchmark (MT-AgentRisk, OpenAgentSafety) 是 LLM tool-use 安全评估，不涉及机器人感知、控制、操作或导航。这篇论文投稿 CoRL 2026 会被 **desk reject（不送审直接退稿）**。\n\n合适的目标会场应为：NeurIPS 2026, ICLR 2027, ACL 2026/2027, EMNLP 2026, USENIX Security 2026, 或 CCS 2026 等 NLP/AI Safety 会议。\n\n**以下 idea 质量评估假设投稿到一个匹配的 NLP/AI Safety 会场（如 ICLR 2027，proposal 自身也提到 \"comfortable for ICLR 2027\"），但最终概率估计会同时给出 CoRL 和匹配会场两个数字。**\n\n---\n\n【领域调研】:\n- [DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)](https://arxiv.org/abs/2504.13562): 确认存在，内容与 proposal 描述一致。通过推理时修改注意力掩码实现注意力重分配，在 LLaMA-2 上 ASR 从 46% 降至 1.2%。确为单轮设定。\n- [ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)](https://arxiv.org/abs/2509.25843): 确认存在，已发表于 ICLR 2026。使用 EAP-IG 识别因果链路上的注意力头，训练通道级缩放向量。确认针对特定可定位漏洞（时态越狱）。Proposal 描述准确。\n- [Wan et al. (arXiv:2602.03664)](https://arxiv.org/abs/2602.03664): \"Mitigating Conversational Inertia in Multi-Turn Agents\"，确认存在。识别对角注意力（conversational inertia），提出 CPL。确认注意力分析仅在聚合层面（所有头平均），proposal 的\"首次逐头分解\"claim 可能成立。但该论文是关于 agentic 任务表现，非安全。\n- [Deng et al. (arXiv:2603.08234)](https://arxiv.org/abs/2603.08234): \"The Struggle Between Continuation and Refusal\"，确认存在。确认了 continuation heads 和 safety heads 之间的竞争机制。Proposal 描述准确。\n- [Johnson & Huo (arXiv:2602.14370)](https://arxiv.org/abs/2602.14370): \"Competition for attention predicts good-to-bad tipping in AI\"，确认存在。提出基于点积竞争的数学化 tipping point 公式。Proposal 描述准确。\n- [Zhou et al. (ICLR 2025, arXiv:2410.13708)](https://arxiv.org/abs/2410.13708): 确认存在，关于注意力头在 LLM 安全中的角色，发现少数关键安全头。\n- [Attention-Aware GNN-based Input Defense (arXiv:2507.07146)](https://arxiv.org/abs/2507.07146): 本调研中新发现的竞争工作——用 GNN 构建多轮查询实体图来检测多轮越狱。与本 proposal 采用完全不同的路线，但同样针对多轮越狱防御中的注意力机制。\n- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697)](https://arxiv.org/abs/2508.19697): 提出分布式安全头训练策略 (AHD)，与本 proposal 的\"注意力竞争\"视角互补但路线不同。\n\n**调研总结**: 多轮 LLM 安全是一个活跃且拥挤的研究领域。2025-2026 年间，攻击侧、防御侧、机制解释侧都有大量工作。该 proposal 试图在\"注意力竞争\"这一机制解释框架下连接\"对话惯性\"(Wan et al.)与\"安全退化\"——这个连接点确实是新的，但核心方法（将 CPL 从任务性能迁移到安全场景）本质上是一个\"方法迁移+机制验证\"研究，而非提出新方法或新理论。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。**\n\n1. **直接在多轮安全数据上 SFT/DPO** — XGuard-Train SFT 已经实现 48.3% 的漏洞减少，MTSA 的 RL 方法将 ASR 从 74.5% 降至 23.5%，X-Boundary 将 ASR 降至 16-25%。这些方法直接优化安全目标，成本与 CPL 相当甚至更低。Proposal 将 XGuard-Train 作为 control，但核心问题是：**如果 CPL（不直接优化安全目标）不能超越直接安全训练，这个 idea 的价值在哪？** Proposal 的回答是\"CPL 解决根因而非症状\"——但这恰恰是未经验证的假设。\n\n2. **简单的上下文管理** — 截断/压缩历史对话、限制上下文窗口长度，是减少\"对话惯性\"的最直观方法。Wan et al. 自己也在推理时提供了 context management strategies。这些零训练成本的方法可能已经能部分缓解惯性导致的安全退化。\n\n3. **推理时注意力干预** — DETAM 在单轮已证明 97%+ ASR 减少。Proposal 论证 DETAM 在多轮中因\"意图分布\"而失效，但这个论证本身是推测性的——没有实证表明 DETAM 在多轮中确实失效。一个简单的 trivial baseline 是：直接在多轮设定中测试 DETAM（将每轮视为独立单轮处理），看它是否真的失效。\n\n**增量价值**: 如果（且仅如果）实验证明 CPL 通过隐式注意力重分配在多轮安全上超越直接安全训练，且这种效果确实由注意力竞争机制介导，那么 proposal 的增量价值在于提供了一种新的\"间接安全防御\"范式。但这是 dual-conditional 的——两个条件都需满足，概率较低。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有 **三个关键未验证假设**：\n\n1. **\"对角注意力（对话惯性）与安全注意力存在竞争关系\"** — 这是整个 hypothesis 的核心前提。虽然 softmax 的零和性质在数学上成立，但\"对角注意力增加 → 安全注意力减少 → 安全退化\"的因果链需要实证。对角注意力可能主要竞争的是非安全相关的其他注意力模式（如语法、语义关联），而非安全关键词注意力。**这是最大的逻辑风险。**\n\n2. **\"CPL 减少对角注意力 → 安全注意力回升\"** — 即使假设 1 成立，CPL 释放的注意力容量不一定流向安全相关 token。注意力重分配的去向是不可控的——被释放的 capacity 可能流向任何其他 pattern。只有在 Level 1（同头竞争）且安全注意力是该头的\"默认状态\"时，减少惯性注意力才会自然回流到安全注意力。\n\n3. **\"多轮安全退化的主要驱动力是注意力惯性\"** — 多轮安全退化可能有多种成因：目标漂移、上下文污染、表征空间偏移（X-Boundary 的视角）、累积 sycophancy 等。Proposal 聚焦于注意力惯性这一个因素，但没有证据表明它是主要或充分的成因。STAR (arXiv:2603.15684) 显示的是从 refusal representation 的单调漂移，这与注意力惯性可能相关也可能独立。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \"将 CPL 从 agentic 任务迁移到安全场景\"是一个有意义的新连接，但本质上是\"方法迁移 + 假设验证\"研究，而非新方法/新理论。Per-head diagonal attention decomposition（Phase 0.5）是一个真实的增量贡献，但属于 engineering/measurement novelty 而非 conceptual novelty。三级注意力竞争假设是一个有组织性的框架，但 softmax 零和性本身是 trivial observation，框架的价值取决于实验能否区分三个 level——这已经是实验设计层面而非 idea 层面。与最近工作的区分：DETAM/ASGuard 做推理时/训练时的 targeted 注意力干预，本 proposal 做训练时 untargeted 干预——这个差异点是真实的，但\"untargeted 训练间接影响安全\"这个 claim 如果 positive，审稿人可能说 \"interesting but I would have guessed that any representation-improving training helps safety\"。\n\n2. **Significance: 中** — 多轮安全确实是重要问题。但 proposal 的贡献取决于 dual-conditional 结果：(a) CPL 需要真的有安全效果，(b) 效果需要通过注意力竞争机制介导。如果 (a) 不成立，贡献缩小为 Phase 0.5 的头分析（中等贡献）。如果 (a) 成立但 (b) 不成立（即 CPL 通过其他机制改善安全，如一般性的表征改善），核心 hypothesis 被证伪，论文叙事需要大幅重构。**最乐观情况下（两个条件都满足），这是一个有影响力的发现；但这个情况的先验概率不高。** 另外，即使所有假设都验证，practical impact 有限——CPL 的安全改善不太可能超越直接安全训练方法。\n\n3. **Related Work: 强** — 这是 proposal 最强的维度。对 DETAM、ASGuard、AISA、Deng et al.、Johnson & Huo、Zhou et al.、X-Boundary、XGuard-Train、MUSE-D、MTSA 等工作的覆盖非常全面且细致。差异化定位清晰（单轮 vs 多轮、推理时 vs 训练时、targeted vs untargeted、circuit-specific vs discourse-level）。引用的论文经调研确认均真实存在，描述准确。唯一缺失的是注意力感知 GNN 防御 (arXiv:2507.07146) 等最新工作，但不影响整体判断。\n\n---\n\n【概率估计】:\n\n**对 CoRL 2026**: 0-2%（致命会场不匹配，会被 desk reject）\n\n**对匹配会场 (ICLR 2027 / NeurIPS 2026)**: [18% - 28%] 中位 22%\n\n【估计理由】:\n\nIdea 本身方向站得住脚（多轮安全 + 注意力机制解释），有真实的 novelty delta（CPL→安全的迁移、per-head 分解），related work 覆盖优秀。但 idea 内核受限于以下因素：\n- **Novelty 上界受限**：核心是\"方法迁移+假设验证\"而非\"新方法/新理论\"，即使结果 positive，审稿人的反应更可能是 \"useful empirical study\" 而非 \"surprising finding\"。\n- **Trivial alternative 威胁真实**：直接安全训练已有 48.3% 漏洞减少（XGuard-Train），CPL 作为 untargeted 方法难以在效果上超越 targeted 方法，那么其价值退化为\"机制理解\"——这压低了 significance。\n- **前提假设链条长且 conditional**：三个关键假设需同时成立，任一断裂都会 undermine 核心叙事。\n- **形式完善度极高但掩盖了内核的 thinness**：proposal 的 5-phase 设计、triple triangulation、dual-outcome framing 等展示了极强的实验设计功底，但剥离这些形式后，核心问题是 \"CPL 能改善多轮安全吗？\" + \"是因为注意力竞争吗？\"——这两个问题虽有价值，但 novelty 天花板有限。\n\nRelated Work 的强度提供了下限保障（审稿人不会说 \"missed critical work\"），但 Novelty 和 Significance 的中等评级限制了上界。\n\n【主要风险】:\n1. **\"为什么不直接做安全训练？\"** — 审稿人极可能质疑：既然 XGuard-Train SFT 已经很有效，为什么要绕道通过 discourse 训练间接改善安全？如果 CPL 不能超越直接安全训练，整个 motivation 会被质疑为 \"a solution in search of a problem\"。\n2. **核心假设的可证伪性风险** — 如果 Phase 0.5 发现对角注意力头与安全头重叠极低（Level 3），整个\"注意力竞争\"叙事退化为\"表征级别的间接效应\"，这与 X-Boundary 等已有工作的视角重叠，novelty 进一步缩减。Proposal 虽设计了 null-result framing，但\"standalone contributions\"（per-head 分解、三方法比较）作为独立贡献体量不足以支撑一篇顶会论文。\n```\n\n---\n\nSources:\n- [DETAM - ACL Anthology](https://aclanthology.org/2025.findings-acl.613/)\n- [DETAM - arXiv](https://arxiv.org/abs/2504.13562)\n- [ASGuard - arXiv](https://arxiv.org/abs/2509.25843)\n- [ASGuard - OpenReview (ICLR 2026)](https://openreview.net/forum?id=wmiEXNEXPs)\n- [Wan et al. Conversational Inertia - arXiv](https://arxiv.org/abs/2602.03664)\n- [Deng et al. Continuation vs Refusal - arXiv](https://arxiv.org/abs/2603.08234)\n- [Johnson & Huo Attention Tipping - arXiv](https://arxiv.org/abs/2602.14370)\n- [Zhou et al. Attention Heads in Safety - arXiv](https://arxiv.org/abs/2410.13708)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Attention-Aware GNN Defense - arXiv](https://arxiv.org/abs/2507.07146)\n- [Safety Alignment More Than Few Heads - arXiv](https://arxiv.org/abs/2508.19697)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have enough field context. Let me compile my comprehensive evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)**: 推理时注意力重分配防御——在 LLaMA-2 上 ASR 从 46% 降至 1.2%，无需权重修改。仅限单轮，需运行时识别 intent tokens。Proposal 对该工作的描述准确。\n\n2. **ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)**: 训练时电路级注意力头修改——通过 EAP-IG 识别因果头、channel-wise scaling 向量 + preventative fine-tuning。在 tense jailbreaking 上 ASR 42%→8%。确认发表于 ICLR 2026，proposal 描述准确，包括 Layer 13 的 4 个 vulnerable heads。\n\n3. **Wan et al. (ICML 2026, arXiv:2602.03664)**: 识别 conversational inertia（对角注意力）并提出 CPL。确认该工作 focus 是 agent 性能而非安全，且注意力分析为 aggregate（所有 head 取平均）。CPL 从未被评估过安全性。Proposal 对此描述准确。\n\n4. **Multi-turn safety defenses (2025-2026)**:\n   - XGuard-Train (COLM 2025, arXiv:2504.13203): SFT 在 30K 多轮安全数据上，48.3% vulnerability reduction\n   - MUSE-D (EMNLP 2025, arXiv:2509.14651): turn-level DPO，24% ASR reduction\n   - X-Boundary (EMNLP 2025, arXiv:2502.09990): 表征层边界，ASR 58.5%→16%\n   - MTSA (ACL 2025, arXiv:2505.17147): 多轮 RL，ASR 74.5%→23.5%\n   所有这些方法直接使用安全标签数据训练。\n\n5. **Attention-safety 机制研究**:\n   - Johnson & Huo (arXiv:2602.14370): 注意力竞争数学建模——存在，但该论文聚焦于 edge AI 中的 good-to-bad tipping，并非直接针对 LLM 多轮安全\n   - Deng et al. (arXiv:2603.08234): continuation vs. refusal heads 竞争——确认存在\n   - Zhou et al. (ICLR 2025, arXiv:2410.13708): Ships 评分，安全头识别\n   - AISA (arXiv:2602.13547): 时空分析定位安全头——确认存在，K=16 heads 达 0.92 检测精度\n\n6. **CoRL 2026 scope**: Conference on Robot Learning，明确要求 \"Submissions should focus on a core robotics problem\"，\"Submissions without a robotics focus will be returned without review\"。主题涵盖 robot learning, manipulation, locomotion, perception for robots 等。\n\n- **调研总结**: 该领域（多轮 LLM 安全 + 注意力机制分析）在 2025-2026 非常活跃，已有大量直接安全训练方法和注意力机制分析工作。Proposal 提出的\"discourse 训练间接改善安全\"的连接是新颖的，但该研究完全属于 NLP/AI Safety 范畴，与 CoRL 的 robotics 主题毫无关联。\n\n---\n\n【⚠️ 致命性前置问题：会议选择】\n\n在进入 idea 质量评估之前，必须首先指出一个致命性问题：\n\n**本 proposal 与 CoRL 2026 的 scope 完全不匹配。** CoRL 是 Conference on Robot Learning，明确要求论文聚焦于 robotics 核心问题。该 proposal 的全部内容——多轮 LLM 安全对齐、jailbreak 防御、注意力头分析、DPO 训练——属于 NLP / AI Safety / ML Interpretability 领域，与机器人学无任何交叉。Proposal 使用的 benchmark（MT-AgentRisk, OpenAgentSafety）均为文本 tool-use agent benchmark，非机器人任务。CoRL 的 Call for Papers 明确声明 \"Submissions without a robotics focus will be returned without review\"。**该论文会被 desk reject，无需进入实质审稿。**\n\n适合的投稿目标应为：NeurIPS 2026、ICLR 2027、ACL 2026/2027、EMNLP 2026 等。\n\n以下 idea 质量评估假设投稿到一个合适的 venue（如 ICLR 2027，proposal 本身也提到 timeline \"comfortable for ICLR 2027\"），以便后续流程有参考价值。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在明显的 trivial alternative 威胁。** 核心问题是：既然我们已经有直接的安全训练方法（XGuard-Train SFT 达 48.3% 改善，X-Boundary 将 ASR 降至 16-25%，MTSA 将 ASR 降至 23.5%），为什么要走\"discourse 训练→间接改善安全\"的迂回路线？\n\n具体而言：\n- **更简单的 baseline**: 直接在安全标注数据上做 DPO/SFT（如 MUSE-D、XGuard-Train）已经有效。如果 CPL 也\"恰好\"改善了安全，这可能仅仅说明任何改变注意力分布的训练都会产生一些安全 side effect，而非证明了一个有深度的机制。\n- **增量价值的真实性**：Proposal 的核心 pitch 是\"间接 discourse 训练能达到直接安全训练的效果\"——但即使成立，这在实践中为何更优？如果你有安全标注数据（benchmark 本身就需要），直接训练不是更高效？Proposal 的回答是\"CPL 不需要安全标签\"，但 CPL 需要 preference pair 构造（dual-rollout），成本并不低。\n- **response length confound**: Proposal 承认了 DPO 的 length bias 问题并设计了控制。但如果 CPL 的安全改善大部分可以被 response length 缩短解释，剩余的 novelty 就很薄了。\n\n**增量价值最有说服力的论点**: CPL 是 untargeted discourse 训练——如果它确实改善了安全，意味着 discourse dynamics 和 safety 之间存在此前未知的因果连接，这在 mechanistic understanding 上有价值。但这更像是一个\"如果 positive 就有趣\"的 bet，而非一个强有力的 a priori argument。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条为：\n1. 对角注意力（inertia）存在 ✅（Wan et al. 已验证）\n2. 安全性依赖特定注意力头 ✅（Zhou et al., AISA, Depth Charge 等多方验证）\n3. **对角注意力和安全注意力在 softmax 层面竞争（zero-sum）** ⚠️ **这是核心假设，完全未经验证**\n4. 因此减少 inertia 可以释放安全注意力 → 完全依赖 #3\n5. CPL 减少 inertia ✅（Wan et al. 已验证）\n6. 因此 CPL 改善安全 → 依赖全链\n\n**关键薄弱环节：**\n\n- **假设 #3 是整个项目的支柱，但 zero-sum competition 并非必然。** Softmax 确实是归一化的，但这不意味着减少一种 attention pattern 必然增加另一种。注意力是高维空间中的操作——减少对角位置的注意力可能分散到任意位置，不一定流向安全关键 token。Proposal 试图用 Phase 0.5 来验证这一假设，但承认如果 overlap < 10%（Level 3），就需要回退到更弱的\"表征漂移\"假设——而 Level 3 的因果论证力度显著下降。\n\n- **Johnson & Huo 的 tipping point 理论的适用性**：该论文关注 \"edge AI\" 中的 competition for attention，其数学框架是否直接适用于 transformer attention heads 的 softmax competition 是一个未验证的类比。Proposal 将其作为理论支柱，但实际上是在做隐喻性引用。\n\n- **\"CPL 实现 implicit DETAM\" 的假设跳跃很大**：DETAM 是精确地在特定 token 位置增强注意力，CPL 是通过 preference learning 间接改变全局注意力分布。两者的机制非常不同，声称 CPL 能达到\"implicit DETAM\"效果需要远比目前更强的论证。\n\n- **多轮 crescendo attack 中 intent 不可定位的论点**：这是 proposal 论证 DETAM 不适用于多轮的关键论点。虽然有道理，但这不等于证明\"discourse 训练是唯一/最佳替代方案\"——其他多轮防御（MTSA 的 RL with future rewards, X-Boundary 的表征边界）已经在不需要 intent localization 的前提下取得了不错效果。\n\n---\n\n【3 维度打分】:\n\n**1. Novelty: 中** \n- \"discourse 训练间接改善安全\"的 **连接** 确实是新颖的——调研中没有找到任何直接测试 CPL→safety 的工作。\n- per-head diagonal attention decomposition 是对 Wan et al. 的 incremental extension（他们 average all heads，proposal 做 per-head），novelty 有但不高。\n- triple-triangulation 方法整合 Ships + DETAM sensitivity + AISA 是方法论贡献，但属于\"组合已有方法\"而非\"提出新方法\"。\n- 核心 novelty 在于\"连接两个已知现象\"——这类 novelty 的天花板受限于结果是否 surprising。如果 positive（CPL 帮助安全），多数审稿人可能会说 \"makes sense, attention is zero-sum, so reducing inertia should help safety somewhat\"——**not surprising**。如果 negative，\"different heads serve different functions\" 也不 surprising。\n- 与 ASGuard (ICLR 2026) 对比：ASGuard 在 **targeted** circuit intervention 上做得更深入且机制更清晰；本 proposal 的 \"untargeted discourse → safety\" 路线在机制理解上更模糊。\n\n**2. Significance: 弱-中**\n- **对于合适 venue（如 ICLR）**: 多轮安全确实是重要问题（16% ASR 增加）。但该 proposal 的研究问题更偏\"机制理解\"而非\"防御效果\"——如果 CPL 的安全改善不如直接安全训练方法，实际影响有限。\n- **如果对 CoRL**: 完全无关（致命）。\n- 该研究的核心问题可以被概括为\"discourse dynamics 是否因果地影响安全？\"——这对理解 LLM 内部机制有价值，但 practical impact 受限于 CPL 是否真的比直接安全训练更优。如果答案是\"CPL 有一些帮助但不如直接方法\"，论文价值主要在 mechanistic insight 层面，影响力中等。\n- null-result framing 设计得很周全（per-head decomposition, triple-method comparison 等作为 standalone contribution），但这些单独贡献的 significance 偏低——每个都是对已有工作的扩展而非突破。\n\n**3. Related Work: 强**\n- 这是 proposal 最突出的优势。对已有工作的覆盖极为全面——DETAM、ASGuard、AISA、XGuard-Train、MUSE-D、X-Boundary、MTSA、Zhou et al.、Deng et al.、Johnson & Huo 等均有准确描述，差异化定位清晰。\n- 调研验证了 proposal 引用的关键论文均真实存在、venue 和内容描述准确（DETAM → ACL 2025 Findings ✅，ASGuard → ICLR 2026 ✅，Wan et al. → ICML 2026 ✅）。\n- Gap statement 逻辑清晰：(a) 无人测试 discourse 训练对安全的因果效果；(b) 无 per-head diagonal attention 分解；(c) 无 discourse-targeted vs. safety-targeted 的 matched 比较；(d) 无 DPO length confound 控制。\n- 唯一隐忧：某些论文的 venue 标注为 \"arXiv 2026\" 没有确认 venue（如 Deng et al., Johnson & Huo），但这在 proposal 阶段可以接受。\n\n---\n\n【概率估计】: \n- **对 CoRL 2026**: 0-2%，中位 1%（desk reject 概率极高，会议 scope 完全不匹配）\n- **对合适 venue（如 ICLR 2027）**: 20-30%，中位 24%\n\n【估计理由】: \n**对 CoRL 2026**：该论文属于 NLP/AI Safety，完全不涉及 robotics——CoRL 明确声明 \"Submissions without a robotics focus will be returned without review\"。即使 idea 本身有质量，venue 不匹配意味着不会进入实质审稿。概率几乎为零。\n\n**对合适 venue（如 ICLR 2027）**：\n- Novelty（中）是主要限制因素——核心贡献是\"连接两个已知现象\"，结果无论正负都不太 surprising，审稿人大概率会说 \"I would have guessed this\"。\n- Trivial alternative 威胁真实——\"直接安全训练\" 是更简单的替代方案，proposal 需要强有力地论证为何间接路线的机制发现有独立价值。\n- 前提假设（注意力竞争）未经验证，且 Phase 0.5 可能给出 Level 3（弱竞争）结果，大幅削弱论文叙事。\n- 正面因素：Related work 极为扎实，实验设计严谨（多 confound control），null-result design 提供下限保护——这些提升了执行层面的下限，但不改变 idea 的上限。\n- 该领域已有密集 benchmark 论文（MT-AgentRisk, OpenAgentSafety, MultiBreak），机制分析论文（DETAM, ASGuard, Deng et al.）和防御论文（XGuard, MUSE-D, MTSA）——审稿人可能认为在已经拥挤的领域中的增量贡献不足。\n\n【主要风险】: \n1. **\"So what?\" 风险**: 即使实验完美执行、CPL 确实改善安全，审稿人可能认为这仅证明\"任何改变注意力的训练都有安全副效用\"，缺乏深刻的机制洞察——核心发现的 surprise 值不足以支撑 top venue 接收。\n2. **前提假设坍塌风险**: 如果 Phase 0.5 发现 diagonal attention heads 与 safety heads 几乎无 overlap（Level 3），整个 \"attention competition\" narrative 将严重弱化，论文需退回到更弱的\"表征漂移\"解释，而这个解释已有 X-Boundary (EMNLP 2025) 覆盖。\n```\n\n---\n\n**补充说明**：该 proposal 在**形式完善度**上极高——五阶段实验设计、go/no-go checkpoint、dual-outcome framing、triple-method triangulation、五个 confound control、多个 fallback plan。这说明作者对研究方法论掌握熟练。但正如 rubric 所要求的，形式完善度 ≠ idea 好——透过形式看本质，核心 insight（\"减少 inertia → 改善安全\"）的 novelty delta 和 surprise value 中等偏弱，且存在 trivial alternative 威胁。\n\n**最关键的建议**：该 proposal **绝对不应投稿 CoRL 2026**，会被 desk reject。如果目标是 ICLR 2027，需要显著强化\"为什么 mechanistic insight（discourse→safety 因果连接）比直接安全训练的实际效果更重要\"这个论点。\n\nSources:\n- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification](https://arxiv.org/abs/2504.13562)\n- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack](https://arxiv.org/abs/2509.25843)\n- [Mitigating Conversational Inertia in Multi-Turn Agents](https://arxiv.org/abs/2602.03664)\n- [AISA: Awakening Intrinsic Safety Awareness in Large Language Models](https://arxiv.org/abs/2602.13547)\n- [MTSA: Multi-turn Safety Alignment for LLMs](https://arxiv.org/abs/2505.17147)\n- [X-Boundary: Establishing Exact Safety Boundary](https://arxiv.org/pdf/2502.09990)\n- [Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/pdf/2602.14370)\n- [The Struggle Between Continuation and Refusal](https://arxiv.org/pdf/2603.08234)\n- [On the Role of Attention Heads in LLM Safety](https://arxiv.org/abs/2410.13708)\n- [Safety Alignment Should Be Made More Than Just A Few Attention Heads](https://arxiv.org/pdf/2508.19697)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information to conduct a thorough, evidence-based evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n\n1. **DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)**: 真实存在，已发表。通过修改因果遮罩矩阵实现推理时注意力重分配，LLaMA-2 上 ASR 46%→1.2%。Proposal 对其描述准确。但 DETAM 是单轮方法。\n\n2. **ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)**: 真实存在，已发表于 ICLR 2026。通过电路分析定位 tense jailbreaking 的脆弱注意力头，训练 channel-wise scaling vector。Proposal 对其描述准确（针对可定位电路，单轮）。\n\n3. **Wan et al. (arXiv:2602.03664)**: 真实存在。提出 conversational inertia 概念和 CPL (Context Preference Learning)。在 8 个 agentic 环境验证了减少对角注意力可提升 agent 表现。Proposal 准确指出其只在聚合层面刻画对角注意力，未做 per-head 分解。OpenReview 记录存在（UubLs3lUfk）。**但注意**：该论文的 ICML 2026 发表状态需确认（会议 7 月 6-11 日在首尔），arXiv 版本为 2 月提交。\n\n4. **Johnson & Huo (arXiv:2602.14370)**: 真实存在。用物理/数学框架建模 dot-product 注意力竞争的 tipping point。但这是一篇偏理论/物理视角的论文，在 ML 社区的影响力有限。\n\n5. **Deng et al. (arXiv:2603.08234, Mar 2026)**: 真实存在。对 continuation-triggered jailbreak 做机制分析，发现 continuation heads 与 safety heads 的竞争关系。\n\n6. **AISA (Song et al., arXiv:2602.13547)**: 真实存在。通过时空分析定位 safety-critical 注意力头，用 K=16 头达到 0.92 检测精度。\n\n7. **Zhou et al. (ICLR 2025, arXiv:2410.13708)**: 真实存在，ICLR 2025 Oral。提出 Ships score，发现单个 safety head 消融可使有害查询响应增加 16×。\n\n8. **多轮安全防御 baselines**: XGuard-Train (COLM 2025), MUSE-D (EMNLP 2025), X-Boundary (EMNLP 2025), MTSA (ACL 2025) 均为真实且已发表的工作。\n\n9. **CoRL 2026 Call for Papers**: 明确要求 \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\" 涵盖的主题包括机器人感知、控制、基础模型、模仿学习、强化学习控制物理机器人、机器人安全与对齐等。\n\n- **调研总结**: 多轮 LLM 安全领域在 2025-2026 年进展迅速，攻击机制（注意力竞争、continuation vs. refusal）和防御方法（推理时注意力修改、训练时电路干预、多轮安全训练）都有大量工作。该 proposal 试图在 conversational inertia（discourse 层面）和 safety（安全层面）之间建立因果桥梁，这个连接本身是新的。**但 CoRL 是机器人学习会议，该 proposal 完全没有涉及任何机器人问题。**\n\n---\n\n【⚠️ 致命问题：严重的 venue mismatch】\n\n**这个 proposal 投稿 CoRL 2026 存在根本性的 venue mismatch，这是一个独立于 idea 质量的致命问题。**\n\nCoRL 2026 的 Call for Papers 明确要求：\n> \"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\"\n\n该 proposal 的全部内容：\n- 核心问题：LLM 多轮对话安全 / jailbreak 防御\n- 方法：注意力机制分析 + DPO 训练\n- 评估基准：MT-AgentRisk（文本工具调用 agent）、OpenAgentSafety（文本多轮任务）\n- 模型：Qwen3-8B、Llama 3.1-8B-Instruct（纯语言模型）\n- **零机器人相关内容**：无物理机器人、无 sim-to-real、无操纵/导航/运动、无具身智能\n\n即使 CoRL 包含 \"learning approaches to robot safety and alignment\" 话题，那也是指**机器人**的安全与对齐，不是 LLM chatbot 的 jailbreak 防御。\n\n**这个 proposal 属于 NeurIPS / ICML / ICLR / ACL / EMNLP 的审稿范畴，投 CoRL 将几乎确定被 desk reject。**\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在强 trivial alternative 威胁。** \n\n核心问题：如果目标是提升多轮安全性，最直接的方法是**在安全数据上直接训练**——XGuard-Train SFT 已实现高达 48.3% 的脆弱性减少，MTSA 的 RL 方法将 ASR 从 74.5% 降至 23.5%，X-Boundary 在表示层面将 ASR 降至 16-25%。这些方法都是直接针对安全问题训练的。\n\n该 proposal 的增量价值声称是：CPL 通过减少\"根因\"（注意力惯性）来间接改善安全，而非直接治\"症状\"。但这个\"根因\"论断本身是**未经验证的假设**——我们并不知道对角注意力惯性是否真的是多轮安全退化的主要驱动因素。可能的替代解释包括：累积上下文效应、表示漂移（STAR 已提供证据）、或简单的 context window 内安全信号稀释。\n\n如果最终 CPL 确实改善了安全，审稿人的第一个问题必然是：\"和直接在安全数据上训练相比，CPL 的优势在哪？\" Proposal 包含了 XGuard-Train 作为对照，但如果 XGuard-Train 效果更好或相当，CPL 的 narrative 就很难站住脚。\n\n**增量价值判断**：真正的增量在于**机制理解**（per-head 分解、overlap 分析），而非 CPL 本身作为防御方法的实用性。但机制理解类贡献的 impact 天花板较低。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链存在**多个未经验证的环节**：\n\n1. **\"对角注意力与安全注意力在同一头/层竞争\"** — 这是整个 hypothesis 的支柱，但完全是推测。Phase 0.5 的设计正是为了验证这一点，这意味着 proposal 自己也承认这是未知的。如果 Phase 0.5 结果显示 overlap < 10%（Level 3），整个 \"attention capacity competition\" 故事的说服力会大幅下降。\n\n2. **\"CPL 的注意力重分配会具体惠及 safety-relevant tokens\"** — CPL 是为了减少 conversational inertia（提升 agent 性能）而设计的通用 discourse 干预，没有任何机制保证它重新分配的注意力会流向安全关键 token 而非其他任务相关 token。\n\n3. **\"注意力惯性是多轮安全退化的主要/重要驱动因素\"** — 多轮安全退化的机制可能是多方面的：representation drift (STAR)、context dilution、safety instruction forgetting 等。对角注意力惯性可能只是众多因素之一，甚至可能是伴随现象而非因果因素。\n\n4. **\"Johnson & Huo 的 tipping point 理论适用于多轮 agent 场景\"** — 该理论基于 dot-product 竞争的数学建模，在 edge AI 小模型上验证，其在 8B 参数生产级模型 + 多轮 agent 设置中的适用性并未被验证。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — \n   - **新颖的部分**：将 conversational inertia (Wan et al.) 与 safety 连接起来是一个新的 research question；per-head 对角注意力分解确实是 Wan et al. 的空白（他们明确只做了 aggregate 分析）；triple-method head identification 的 cross-validation 设计有方法论贡献。\n   - **限制 novelty 的因素**：核心干预方法（CPL）完全借用自 Wan et al.，不是本文提出的新方法；将现有方法应用于新场景（\"CPL → safety\"）本质上是一个 application/empirical study；Phase 0.5 的 per-head 分解虽然新，但技术上是 straightforward 的分析（对每个头分别计算 Wan et al. 的 metric，不需要新的分析框架）；注意力头 overlap 分析的思路在 Zhou et al. (ICLR 2025) 和 Deng et al. 之后并不令人意外。\n   - **与现有工作的差异**：相对于 DETAM（推理时 + 单轮）、ASGuard（训练时 + 电路靶向 + 单轮）、XGuard-Train/MUSE-D/MTSA（训练时 + 直接安全数据），proposal 的定位是\"训练时 + discourse 干预 + 多轮\"——这个组合确实是新的，但\"新组合\"和\"新洞见\"是两回事。\n\n2. **Significance: 中偏弱** — \n   - 多轮安全问题本身很重要，但该 proposal 的核心贡献更偏向**机制验证/理解**（\"inertia 和 safety 是否竞争？\"）而非**方法创新**（CPL 是借用的）。\n   - 如果结果为 positive（CPL 改善安全），审稿人可能的反应是 \"interesting connection, but not surprising — if inertia competes with safety attention, reducing inertia should help\"。这不满足 \"surprising, not what I expected\" 的标准。\n   - 如果结果为 negative（CPL 不改善安全），null-result 贡献（per-head 分解、overlap 分析）是有价值的但 incremental——它们不会改变领域的研究方向。\n   - **对 CoRL 的 significance 为零**——这与机器人学习完全无关。即使对 NLP/AI safety 社区，significance 也受限于核心发现的可预测性。\n\n3. **Related Work: 强** — \n   - 这是 proposal 最突出的部分。Related work 覆盖极为全面，涵盖了注意力重分配防御（DETAM）、训练时头干预（ASGuard）、安全头定位（Zhou et al., AISA, Depth Charge）、注意力竞争理论（Johnson & Huo, Deng et al.）、多轮安全基准和防御（MT-AgentRisk, XGuard-Train, MUSE-D, X-Boundary, MTSA, OpenAgentSafety）以及 discourse dynamics (Wan et al.)。\n   - 差异化定位清晰：明确标注了每个相关工作的局限（DETAM: 单轮 + 需要 intent 定位；ASGuard: 电路靶向 + 单轮；直接安全训练：不测试 discourse 机制的因果性）。\n   - 引用的论文经核实均真实存在，描述准确。\n   - **唯一弱点**：虽然 coverage 全面，但\"全面的 related work\" 可能部分源于 proposal 将大量不同线索松散连接（6 条独立线索），而非深入聚焦于一个紧密的研究空间。\n\n---\n\n【概率估计】: 0% - 5%，中位 2%\n\n【估计理由】: \n\n**存在两个独立的限制因素，任何一个都足以致命：**\n\n**（A）Venue Mismatch — 致命（将概率压至 ~0-5%）：** CoRL 2026 明确要求 \"focus on a core robotics problem\"。该 proposal 是纯 LLM 安全研究，零机器人相关内容，极大概率在 desk review 阶段被拒。这一因素独立于 idea 质量，是投稿策略层面的致命错误。\n\n**（B）即使忽略 venue mismatch，idea 本身的质量对顶会（NeurIPS/ICML/ICLR/ACL）估计约 20-30%：**\n- Novelty 中等：核心干预借用自 Wan et al.，本文的新颖性在于\"连接\"而非\"方法\"\n- 存在 trivial alternative 威胁：直接安全训练可能效果更好\n- 核心假设（inertia-safety 竞争）未经验证，是整篇论文的赌注\n- 正向结果的 surprise factor 有限\n\n将 (A) 和 (B) 综合：投稿 CoRL 2026 的中稿概率为 0-5%。\n\n【主要风险】: \n1. **致命 venue mismatch**: 该 proposal 是 LLM 多轮安全研究，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。投稿 CoRL 将几乎确定被 desk reject，无论 idea 质量如何。这是最核心的风险。\n2. **核心假设未验证 + trivial alternative**: 如果对角注意力惯性与 safety heads 的 overlap 很低（Phase 0.5 Level 3 结果），整个 competition hypothesis 的说服力大打折扣。同时，直接在安全数据上训练（XGuard-Train 48.3% 脆弱性减少）可能以更低成本达到类似或更好效果，使 CPL 的间接路径显得缺乏动机。\n```\n\n---\n\n**补充建议**：如果作者希望推进这个 research，应该：\n1. **立即更换目标 venue** — 考虑 NeurIPS 2026、ICLR 2027、ACL 2026/2027、EMNLP 2026 等 NLP/ML 安全相关会议\n2. 在适合的 venue 下，idea 有一定潜力（约 20-30%），但需要加强核心假设的前期验证（Phase 0.5 结果应尽早获得以 de-risk），并清晰回应 \"为什么不直接在安全数据上训练\" 的 trivial alternative 挑战\n\nSources:\n- [DeTAM: ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.613/)\n- [DeTAM arXiv](https://arxiv.org/abs/2504.13562)\n- [ASGuard: ICLR 2026](https://openreview.net/forum?id=wmiEXNEXPs)\n- [ASGuard arXiv](https://arxiv.org/abs/2509.25843)\n- [Wan et al. Conversational Inertia arXiv](https://arxiv.org/abs/2602.03664)\n- [Johnson & Huo tipping point](https://arxiv.org/abs/2602.14370)\n- [Deng et al. Continuation vs Refusal](https://arxiv.org/abs/2603.08234)\n- [AISA arXiv](https://arxiv.org/abs/2602.13547)\n- [Zhou et al. ICLR 2025 Safety Heads](https://arxiv.org/abs/2410.13708)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis\n\n## Description\nThis project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.\n\n## Core Problem\nMulti-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.\n\n## Opportunity\nSix independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.\n\n## Related Work / Landscape\n**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.\n\n## Approach\nWe run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.\n\n**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.\n\n**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.\n\n**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.\n\n**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).\n\n**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).\n\n**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.\n\n**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.\n\n**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.\n\n**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.\n\n**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.\n\n**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.\n\n**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.\n\nAll primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).\n\n## Inspiration\nField guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.\n\n## Key References\n- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)\n- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)\n- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)\n- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)\n- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)\n- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)\n- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)\n- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)\n- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)\n- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)\n- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)\n- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)\n- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)\n- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)\n- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)\n- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)\n- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)\n- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)\n- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)\n- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)\n- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)\n- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)\n- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)\n- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)\n- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)\n- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)\n- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)\n- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)\n- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)\n- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)\n- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)\n- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)\n- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)\n- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)\n- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)\n- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)\n- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)\n- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}\n- **human_in_loop**: {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}\n- **auto_research**: {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T20:52:44.864Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T20:52:44.864Z",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T20:52:44.878Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile my evaluation.

---

```
【阶段】: Triage

【致命前提问题 — 会场匹配】:
在进入 idea 质量评估之前，必须首先指出一个致命的会场匹配问题：

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确声明：
• "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
• "Submissions without a robotics focus will be returned without review."
• "Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

本 proposal 的内容是 LLM 多轮对话安全、注意力机制、越狱防御——**完全没有任何机器人学内容**。使用的 benchmark (MT-AgentRisk, OpenAgentSafety) 是 LLM tool-use 安全评估，不涉及机器人感知、控制、操作或导航。这篇论文投稿 CoRL 2026 会被 **desk reject（不送审直接退稿）**。

合适的目标会场应为：NeurIPS 2026, ICLR 2027, ACL 2026/2027, EMNLP 2026, USENIX Security 2026, 或 CCS 2026 等 NLP/AI Safety 会议。

**以下 idea 质量评估假设投稿到一个匹配的 NLP/AI Safety 会场（如 ICLR 2027，proposal 自身也提到 "comfortable for ICLR 2027"），但最终概率估计会同时给出 CoRL 和匹配会场两个数字。**

---

【领域调研】:
- [DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)](https://arxiv.org/abs/2504.13562): 确认存在，内容与 proposal 描述一致。通过推理时修改注意力掩码实现注意力重分配，在 LLaMA-2 上 ASR 从 46% 降至 1.2%。确为单轮设定。
- [ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)](https://arxiv.org/abs/2509.25843): 确认存在，已发表于 ICLR 2026。使用 EAP-IG 识别因果链路上的注意力头，训练通道级缩放向量。确认针对特定可定位漏洞（时态越狱）。Proposal 描述准确。
- [Wan et al. (arXiv:2602.03664)](https://arxiv.org/abs/2602.03664): "Mitigating Conversational Inertia in Multi-Turn Agents"，确认存在。识别对角注意力（conversational inertia），提出 CPL。确认注意力分析仅在聚合层面（所有头平均），proposal 的"首次逐头分解"claim 可能成立。但该论文是关于 agentic 任务表现，非安全。
- [Deng et al. (arXiv:2603.08234)](https://arxiv.org/abs/2603.08234): "The Struggle Between Continuation and Refusal"，确认存在。确认了 continuation heads 和 safety heads 之间的竞争机制。Proposal 描述准确。
- [Johnson & Huo (arXiv:2602.14370)](https://arxiv.org/abs/2602.14370): "Competition for attention predicts good-to-bad tipping in AI"，确认存在。提出基于点积竞争的数学化 tipping point 公式。Proposal 描述准确。
- [Zhou et al. (ICLR 2025, arXiv:2410.13708)](https://arxiv.org/abs/2410.13708): 确认存在，关于注意力头在 LLM 安全中的角色，发现少数关键安全头。
- [Attention-Aware GNN-based Input Defense (arXiv:2507.07146)](https://arxiv.org/abs/2507.07146): 本调研中新发现的竞争工作——用 GNN 构建多轮查询实体图来检测多轮越狱。与本 proposal 采用完全不同的路线，但同样针对多轮越狱防御中的注意力机制。
- [Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697)](https://arxiv.org/abs/2508.19697): 提出分布式安全头训练策略 (AHD)，与本 proposal 的"注意力竞争"视角互补但路线不同。

**调研总结**: 多轮 LLM 安全是一个活跃且拥挤的研究领域。2025-2026 年间，攻击侧、防御侧、机制解释侧都有大量工作。该 proposal 试图在"注意力竞争"这一机制解释框架下连接"对话惯性"(Wan et al.)与"安全退化"——这个连接点确实是新的，但核心方法（将 CPL 从任务性能迁移到安全场景）本质上是一个"方法迁移+机制验证"研究，而非提出新方法或新理论。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。**

1. **直接在多轮安全数据上 SFT/DPO** — XGuard-Train SFT 已经实现 48.3% 的漏洞减少，MTSA 的 RL 方法将 ASR 从 74.5% 降至 23.5%，X-Boundary 将 ASR 降至 16-25%。这些方法直接优化安全目标，成本与 CPL 相当甚至更低。Proposal 将 XGuard-Train 作为 control，但核心问题是：**如果 CPL（不直接优化安全目标）不能超越直接安全训练，这个 idea 的价值在哪？** Proposal 的回答是"CPL 解决根因而非症状"——但这恰恰是未经验证的假设。

2. **简单的上下文管理** — 截断/压缩历史对话、限制上下文窗口长度，是减少"对话惯性"的最直观方法。Wan et al. 自己也在推理时提供了 context management strategies。这些零训练成本的方法可能已经能部分缓解惯性导致的安全退化。

3. **推理时注意力干预** — DETAM 在单轮已证明 97%+ ASR 减少。Proposal 论证 DETAM 在多轮中因"意图分布"而失效，但这个论证本身是推测性的——没有实证表明 DETAM 在多轮中确实失效。一个简单的 trivial baseline 是：直接在多轮设定中测试 DETAM（将每轮视为独立单轮处理），看它是否真的失效。

**增量价值**: 如果（且仅如果）实验证明 CPL 通过隐式注意力重分配在多轮安全上超越直接安全训练，且这种效果确实由注意力竞争机制介导，那么 proposal 的增量价值在于提供了一种新的"间接安全防御"范式。但这是 dual-conditional 的——两个条件都需满足，概率较低。

---

【前提假设检验】:

核心 claim 的逻辑链条中有 **三个关键未验证假设**：

1. **"对角注意力（对话惯性）与安全注意力存在竞争关系"** — 这是整个 hypothesis 的核心前提。虽然 softmax 的零和性质在数学上成立，但"对角注意力增加 → 安全注意力减少 → 安全退化"的因果链需要实证。对角注意力可能主要竞争的是非安全相关的其他注意力模式（如语法、语义关联），而非安全关键词注意力。**这是最大的逻辑风险。**

2. **"CPL 减少对角注意力 → 安全注意力回升"** — 即使假设 1 成立，CPL 释放的注意力容量不一定流向安全相关 token。注意力重分配的去向是不可控的——被释放的 capacity 可能流向任何其他 pattern。只有在 Level 1（同头竞争）且安全注意力是该头的"默认状态"时，减少惯性注意力才会自然回流到安全注意力。

3. **"多轮安全退化的主要驱动力是注意力惯性"** — 多轮安全退化可能有多种成因：目标漂移、上下文污染、表征空间偏移（X-Boundary 的视角）、累积 sycophancy 等。Proposal 聚焦于注意力惯性这一个因素，但没有证据表明它是主要或充分的成因。STAR (arXiv:2603.15684) 显示的是从 refusal representation 的单调漂移，这与注意力惯性可能相关也可能独立。

---

【3 维度打分】:

1. **Novelty: 中** — "将 CPL 从 agentic 任务迁移到安全场景"是一个有意义的新连接，但本质上是"方法迁移 + 假设验证"研究，而非新方法/新理论。Per-head diagonal attention decomposition（Phase 0.5）是一个真实的增量贡献，但属于 engineering/measurement novelty 而非 conceptual novelty。三级注意力竞争假设是一个有组织性的框架，但 softmax 零和性本身是 trivial observation，框架的价值取决于实验能否区分三个 level——这已经是实验设计层面而非 idea 层面。与最近工作的区分：DETAM/ASGuard 做推理时/训练时的 targeted 注意力干预，本 proposal 做训练时 untargeted 干预——这个差异点是真实的，但"untargeted 训练间接影响安全"这个 claim 如果 positive，审稿人可能说 "interesting but I would have guessed that any representation-improving training helps safety"。

2. **Significance: 中** — 多轮安全确实是重要问题。但 proposal 的贡献取决于 dual-conditional 结果：(a) CPL 需要真的有安全效果，(b) 效果需要通过注意力竞争机制介导。如果 (a) 不成立，贡献缩小为 Phase 0.5 的头分析（中等贡献）。如果 (a) 成立但 (b) 不成立（即 CPL 通过其他机制改善安全，如一般性的表征改善），核心 hypothesis 被证伪，论文叙事需要大幅重构。**最乐观情况下（两个条件都满足），这是一个有影响力的发现；但这个情况的先验概率不高。** 另外，即使所有假设都验证，practical impact 有限——CPL 的安全改善不太可能超越直接安全训练方法。

3. **Related Work: 强** — 这是 proposal 最强的维度。对 DETAM、ASGuard、AISA、Deng et al.、Johnson & Huo、Zhou et al.、X-Boundary、XGuard-Train、MUSE-D、MTSA 等工作的覆盖非常全面且细致。差异化定位清晰（单轮 vs 多轮、推理时 vs 训练时、targeted vs untargeted、circuit-specific vs discourse-level）。引用的论文经调研确认均真实存在，描述准确。唯一缺失的是注意力感知 GNN 防御 (arXiv:2507.07146) 等最新工作，但不影响整体判断。

---

【概率估计】:

**对 CoRL 2026**: 0-2%（致命会场不匹配，会被 desk reject）

**对匹配会场 (ICLR 2027 / NeurIPS 2026)**: [18% - 28%] 中位 22%

【估计理由】:

Idea 本身方向站得住脚（多轮安全 + 注意力机制解释），有真实的 novelty delta（CPL→安全的迁移、per-head 分解），related work 覆盖优秀。但 idea 内核受限于以下因素：
- **Novelty 上界受限**：核心是"方法迁移+假设验证"而非"新方法/新理论"，即使结果 positive，审稿人的反应更可能是 "useful empirical study" 而非 "surprising finding"。
- **Trivial alternative 威胁真实**：直接安全训练已有 48.3% 漏洞减少（XGuard-Train），CPL 作为 untargeted 方法难以在效果上超越 targeted 方法，那么其价值退化为"机制理解"——这压低了 significance。
- **前提假设链条长且 conditional**：三个关键假设需同时成立，任一断裂都会 undermine 核心叙事。
- **形式完善度极高但掩盖了内核的 thinness**：proposal 的 5-phase 设计、triple triangulation、dual-outcome framing 等展示了极强的实验设计功底，但剥离这些形式后，核心问题是 "CPL 能改善多轮安全吗？" + "是因为注意力竞争吗？"——这两个问题虽有价值，但 novelty 天花板有限。

Related Work 的强度提供了下限保障（审稿人不会说 "missed critical work"），但 Novelty 和 Significance 的中等评级限制了上界。

【主要风险】:
1. **"为什么不直接做安全训练？"** — 审稿人极可能质疑：既然 XGuard-Train SFT 已经很有效，为什么要绕道通过 discourse 训练间接改善安全？如果 CPL 不能超越直接安全训练，整个 motivation 会被质疑为 "a solution in search of a problem"。
2. **核心假设的可证伪性风险** — 如果 Phase 0.5 发现对角注意力头与安全头重叠极低（Level 3），整个"注意力竞争"叙事退化为"表征级别的间接效应"，这与 X-Boundary 等已有工作的视角重叠，novelty 进一步缩减。Proposal 虽设计了 null-result framing，但"standalone contributions"（per-head 分解、三方法比较）作为独立贡献体量不足以支撑一篇顶会论文。
```

---

Sources:
- [DETAM - ACL Anthology](https://aclanthology.org/2025.findings-acl.613/)
- [DETAM - arXiv](https://arxiv.org/abs/2504.13562)
- [ASGuard - arXiv](https://arxiv.org/abs/2509.25843)
- [ASGuard - OpenReview (ICLR 2026)](https://openreview.net/forum?id=wmiEXNEXPs)
- [Wan et al. Conversational Inertia - arXiv](https://arxiv.org/abs/2602.03664)
- [Deng et al. Continuation vs Refusal - arXiv](https://arxiv.org/abs/2603.08234)
- [Johnson & Huo Attention Tipping - arXiv](https://arxiv.org/abs/2602.14370)
- [Zhou et al. Attention Heads in Safety - arXiv](https://arxiv.org/abs/2410.13708)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Attention-Aware GNN Defense - arXiv](https://arxiv.org/abs/2507.07146)
- [Safety Alignment More Than Few Heads - arXiv](https://arxiv.org/abs/2508.19697)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have enough field context. Let me compile my comprehensive evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)**: 推理时注意力重分配防御——在 LLaMA-2 上 ASR 从 46% 降至 1.2%，无需权重修改。仅限单轮，需运行时识别 intent tokens。Proposal 对该工作的描述准确。

2. **ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)**: 训练时电路级注意力头修改——通过 EAP-IG 识别因果头、channel-wise scaling 向量 + preventative fine-tuning。在 tense jailbreaking 上 ASR 42%→8%。确认发表于 ICLR 2026，proposal 描述准确，包括 Layer 13 的 4 个 vulnerable heads。

3. **Wan et al. (ICML 2026, arXiv:2602.03664)**: 识别 conversational inertia（对角注意力）并提出 CPL。确认该工作 focus 是 agent 性能而非安全，且注意力分析为 aggregate（所有 head 取平均）。CPL 从未被评估过安全性。Proposal 对此描述准确。

4. **Multi-turn safety defenses (2025-2026)**:
   - XGuard-Train (COLM 2025, arXiv:2504.13203): SFT 在 30K 多轮安全数据上，48.3% vulnerability reduction
   - MUSE-D (EMNLP 2025, arXiv:2509.14651): turn-level DPO，24% ASR reduction
   - X-Boundary (EMNLP 2025, arXiv:2502.09990): 表征层边界，ASR 58.5%→16%
   - MTSA (ACL 2025, arXiv:2505.17147): 多轮 RL，ASR 74.5%→23.5%
   所有这些方法直接使用安全标签数据训练。

5. **Attention-safety 机制研究**:
   - Johnson & Huo (arXiv:2602.14370): 注意力竞争数学建模——存在，但该论文聚焦于 edge AI 中的 good-to-bad tipping，并非直接针对 LLM 多轮安全
   - Deng et al. (arXiv:2603.08234): continuation vs. refusal heads 竞争——确认存在
   - Zhou et al. (ICLR 2025, arXiv:2410.13708): Ships 评分，安全头识别
   - AISA (arXiv:2602.13547): 时空分析定位安全头——确认存在，K=16 heads 达 0.92 检测精度

6. **CoRL 2026 scope**: Conference on Robot Learning，明确要求 "Submissions should focus on a core robotics problem"，"Submissions without a robotics focus will be returned without review"。主题涵盖 robot learning, manipulation, locomotion, perception for robots 等。

- **调研总结**: 该领域（多轮 LLM 安全 + 注意力机制分析）在 2025-2026 非常活跃，已有大量直接安全训练方法和注意力机制分析工作。Proposal 提出的"discourse 训练间接改善安全"的连接是新颖的，但该研究完全属于 NLP/AI Safety 范畴，与 CoRL 的 robotics 主题毫无关联。

---

【⚠️ 致命性前置问题：会议选择】

在进入 idea 质量评估之前，必须首先指出一个致命性问题：

**本 proposal 与 CoRL 2026 的 scope 完全不匹配。** CoRL 是 Conference on Robot Learning，明确要求论文聚焦于 robotics 核心问题。该 proposal 的全部内容——多轮 LLM 安全对齐、jailbreak 防御、注意力头分析、DPO 训练——属于 NLP / AI Safety / ML Interpretability 领域，与机器人学无任何交叉。Proposal 使用的 benchmark（MT-AgentRisk, OpenAgentSafety）均为文本 tool-use agent benchmark，非机器人任务。CoRL 的 Call for Papers 明确声明 "Submissions without a robotics focus will be returned without review"。**该论文会被 desk reject，无需进入实质审稿。**

适合的投稿目标应为：NeurIPS 2026、ICLR 2027、ACL 2026/2027、EMNLP 2026 等。

以下 idea 质量评估假设投稿到一个合适的 venue（如 ICLR 2027，proposal 本身也提到 timeline "comfortable for ICLR 2027"），以便后续流程有参考价值。

---

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。** 核心问题是：既然我们已经有直接的安全训练方法（XGuard-Train SFT 达 48.3% 改善，X-Boundary 将 ASR 降至 16-25%，MTSA 将 ASR 降至 23.5%），为什么要走"discourse 训练→间接改善安全"的迂回路线？

具体而言：
- **更简单的 baseline**: 直接在安全标注数据上做 DPO/SFT（如 MUSE-D、XGuard-Train）已经有效。如果 CPL 也"恰好"改善了安全，这可能仅仅说明任何改变注意力分布的训练都会产生一些安全 side effect，而非证明了一个有深度的机制。
- **增量价值的真实性**：Proposal 的核心 pitch 是"间接 discourse 训练能达到直接安全训练的效果"——但即使成立，这在实践中为何更优？如果你有安全标注数据（benchmark 本身就需要），直接训练不是更高效？Proposal 的回答是"CPL 不需要安全标签"，但 CPL 需要 preference pair 构造（dual-rollout），成本并不低。
- **response length confound**: Proposal 承认了 DPO 的 length bias 问题并设计了控制。但如果 CPL 的安全改善大部分可以被 response length 缩短解释，剩余的 novelty 就很薄了。

**增量价值最有说服力的论点**: CPL 是 untargeted discourse 训练——如果它确实改善了安全，意味着 discourse dynamics 和 safety 之间存在此前未知的因果连接，这在 mechanistic understanding 上有价值。但这更像是一个"如果 positive 就有趣"的 bet，而非一个强有力的 a priori argument。

---

【前提假设检验】:

核心 claim 的逻辑链条为：
1. 对角注意力（inertia）存在 ✅（Wan et al. 已验证）
2. 安全性依赖特定注意力头 ✅（Zhou et al., AISA, Depth Charge 等多方验证）
3. **对角注意力和安全注意力在 softmax 层面竞争（zero-sum）** ⚠️ **这是核心假设，完全未经验证**
4. 因此减少 inertia 可以释放安全注意力 → 完全依赖 #3
5. CPL 减少 inertia ✅（Wan et al. 已验证）
6. 因此 CPL 改善安全 → 依赖全链

**关键薄弱环节：**

- **假设 #3 是整个项目的支柱，但 zero-sum competition 并非必然。** Softmax 确实是归一化的，但这不意味着减少一种 attention pattern 必然增加另一种。注意力是高维空间中的操作——减少对角位置的注意力可能分散到任意位置，不一定流向安全关键 token。Proposal 试图用 Phase 0.5 来验证这一假设，但承认如果 overlap < 10%（Level 3），就需要回退到更弱的"表征漂移"假设——而 Level 3 的因果论证力度显著下降。

- **Johnson & Huo 的 tipping point 理论的适用性**：该论文关注 "edge AI" 中的 competition for attention，其数学框架是否直接适用于 transformer attention heads 的 softmax competition 是一个未验证的类比。Proposal 将其作为理论支柱，但实际上是在做隐喻性引用。

- **"CPL 实现 implicit DETAM" 的假设跳跃很大**：DETAM 是精确地在特定 token 位置增强注意力，CPL 是通过 preference learning 间接改变全局注意力分布。两者的机制非常不同，声称 CPL 能达到"implicit DETAM"效果需要远比目前更强的论证。

- **多轮 crescendo attack 中 intent 不可定位的论点**：这是 proposal 论证 DETAM 不适用于多轮的关键论点。虽然有道理，但这不等于证明"discourse 训练是唯一/最佳替代方案"——其他多轮防御（MTSA 的 RL with future rewards, X-Boundary 的表征边界）已经在不需要 intent localization 的前提下取得了不错效果。

---

【3 维度打分】:

**1. Novelty: 中** 
- "discourse 训练间接改善安全"的 **连接** 确实是新颖的——调研中没有找到任何直接测试 CPL→safety 的工作。
- per-head diagonal attention decomposition 是对 Wan et al. 的 incremental extension（他们 average all heads，proposal 做 per-head），novelty 有但不高。
- triple-triangulation 方法整合 Ships + DETAM sensitivity + AISA 是方法论贡献，但属于"组合已有方法"而非"提出新方法"。
- 核心 novelty 在于"连接两个已知现象"——这类 novelty 的天花板受限于结果是否 surprising。如果 positive（CPL 帮助安全），多数审稿人可能会说 "makes sense, attention is zero-sum, so reducing inertia should help safety somewhat"——**not surprising**。如果 negative，"different heads serve different functions" 也不 surprising。
- 与 ASGuard (ICLR 2026) 对比：ASGuard 在 **targeted** circuit intervention 上做得更深入且机制更清晰；本 proposal 的 "untargeted discourse → safety" 路线在机制理解上更模糊。

**2. Significance: 弱-中**
- **对于合适 venue（如 ICLR）**: 多轮安全确实是重要问题（16% ASR 增加）。但该 proposal 的研究问题更偏"机制理解"而非"防御效果"——如果 CPL 的安全改善不如直接安全训练方法，实际影响有限。
- **如果对 CoRL**: 完全无关（致命）。
- 该研究的核心问题可以被概括为"discourse dynamics 是否因果地影响安全？"——这对理解 LLM 内部机制有价值，但 practical impact 受限于 CPL 是否真的比直接安全训练更优。如果答案是"CPL 有一些帮助但不如直接方法"，论文价值主要在 mechanistic insight 层面，影响力中等。
- null-result framing 设计得很周全（per-head decomposition, triple-method comparison 等作为 standalone contribution），但这些单独贡献的 significance 偏低——每个都是对已有工作的扩展而非突破。

**3. Related Work: 强**
- 这是 proposal 最突出的优势。对已有工作的覆盖极为全面——DETAM、ASGuard、AISA、XGuard-Train、MUSE-D、X-Boundary、MTSA、Zhou et al.、Deng et al.、Johnson & Huo 等均有准确描述，差异化定位清晰。
- 调研验证了 proposal 引用的关键论文均真实存在、venue 和内容描述准确（DETAM → ACL 2025 Findings ✅，ASGuard → ICLR 2026 ✅，Wan et al. → ICML 2026 ✅）。
- Gap statement 逻辑清晰：(a) 无人测试 discourse 训练对安全的因果效果；(b) 无 per-head diagonal attention 分解；(c) 无 discourse-targeted vs. safety-targeted 的 matched 比较；(d) 无 DPO length confound 控制。
- 唯一隐忧：某些论文的 venue 标注为 "arXiv 2026" 没有确认 venue（如 Deng et al., Johnson & Huo），但这在 proposal 阶段可以接受。

---

【概率估计】: 
- **对 CoRL 2026**: 0-2%，中位 1%（desk reject 概率极高，会议 scope 完全不匹配）
- **对合适 venue（如 ICLR 2027）**: 20-30%，中位 24%

【估计理由】: 
**对 CoRL 2026**：该论文属于 NLP/AI Safety，完全不涉及 robotics——CoRL 明确声明 "Submissions without a robotics focus will be returned without review"。即使 idea 本身有质量，venue 不匹配意味着不会进入实质审稿。概率几乎为零。

**对合适 venue（如 ICLR 2027）**：
- Novelty（中）是主要限制因素——核心贡献是"连接两个已知现象"，结果无论正负都不太 surprising，审稿人大概率会说 "I would have guessed this"。
- Trivial alternative 威胁真实——"直接安全训练" 是更简单的替代方案，proposal 需要强有力地论证为何间接路线的机制发现有独立价值。
- 前提假设（注意力竞争）未经验证，且 Phase 0.5 可能给出 Level 3（弱竞争）结果，大幅削弱论文叙事。
- 正面因素：Related work 极为扎实，实验设计严谨（多 confound control），null-result design 提供下限保护——这些提升了执行层面的下限，但不改变 idea 的上限。
- 该领域已有密集 benchmark 论文（MT-AgentRisk, OpenAgentSafety, MultiBreak），机制分析论文（DETAM, ASGuard, Deng et al.）和防御论文（XGuard, MUSE-D, MTSA）——审稿人可能认为在已经拥挤的领域中的增量贡献不足。

【主要风险】: 
1. **"So what?" 风险**: 即使实验完美执行、CPL 确实改善安全，审稿人可能认为这仅证明"任何改变注意力的训练都有安全副效用"，缺乏深刻的机制洞察——核心发现的 surprise 值不足以支撑 top venue 接收。
2. **前提假设坍塌风险**: 如果 Phase 0.5 发现 diagonal attention heads 与 safety heads 几乎无 overlap（Level 3），整个 "attention competition" narrative 将严重弱化，论文需退回到更弱的"表征漂移"解释，而这个解释已有 X-Boundary (EMNLP 2025) 覆盖。
```

---

**补充说明**：该 proposal 在**形式完善度**上极高——五阶段实验设计、go/no-go checkpoint、dual-outcome framing、triple-method triangulation、五个 confound control、多个 fallback plan。这说明作者对研究方法论掌握熟练。但正如 rubric 所要求的，形式完善度 ≠ idea 好——透过形式看本质，核心 insight（"减少 inertia → 改善安全"）的 novelty delta 和 surprise value 中等偏弱，且存在 trivial alternative 威胁。

**最关键的建议**：该 proposal **绝对不应投稿 CoRL 2026**，会被 desk reject。如果目标是 ICLR 2027，需要显著强化"为什么 mechanistic insight（discourse→safety 因果连接）比直接安全训练的实际效果更重要"这个论点。

Sources:
- [DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification](https://arxiv.org/abs/2504.13562)
- [ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack](https://arxiv.org/abs/2509.25843)
- [Mitigating Conversational Inertia in Multi-Turn Agents](https://arxiv.org/abs/2602.03664)
- [AISA: Awakening Intrinsic Safety Awareness in Large Language Models](https://arxiv.org/abs/2602.13547)
- [MTSA: Multi-turn Safety Alignment for LLMs](https://arxiv.org/abs/2505.17147)
- [X-Boundary: Establishing Exact Safety Boundary](https://arxiv.org/pdf/2502.09990)
- [Competition for attention predicts good-to-bad tipping in AI](https://arxiv.org/pdf/2602.14370)
- [The Struggle Between Continuation and Refusal](https://arxiv.org/pdf/2603.08234)
- [On the Role of Attention Heads in LLM Safety](https://arxiv.org/abs/2410.13708)
- [Safety Alignment Should Be Made More Than Just A Few Attention Heads](https://arxiv.org/pdf/2508.19697)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information to conduct a thorough, evidence-based evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562)**: 真实存在，已发表。通过修改因果遮罩矩阵实现推理时注意力重分配，LLaMA-2 上 ASR 46%→1.2%。Proposal 对其描述准确。但 DETAM 是单轮方法。

2. **ASGuard (Park et al., ICLR 2026, arXiv:2509.25843)**: 真实存在，已发表于 ICLR 2026。通过电路分析定位 tense jailbreaking 的脆弱注意力头，训练 channel-wise scaling vector。Proposal 对其描述准确（针对可定位电路，单轮）。

3. **Wan et al. (arXiv:2602.03664)**: 真实存在。提出 conversational inertia 概念和 CPL (Context Preference Learning)。在 8 个 agentic 环境验证了减少对角注意力可提升 agent 表现。Proposal 准确指出其只在聚合层面刻画对角注意力，未做 per-head 分解。OpenReview 记录存在（UubLs3lUfk）。**但注意**：该论文的 ICML 2026 发表状态需确认（会议 7 月 6-11 日在首尔），arXiv 版本为 2 月提交。

4. **Johnson & Huo (arXiv:2602.14370)**: 真实存在。用物理/数学框架建模 dot-product 注意力竞争的 tipping point。但这是一篇偏理论/物理视角的论文，在 ML 社区的影响力有限。

5. **Deng et al. (arXiv:2603.08234, Mar 2026)**: 真实存在。对 continuation-triggered jailbreak 做机制分析，发现 continuation heads 与 safety heads 的竞争关系。

6. **AISA (Song et al., arXiv:2602.13547)**: 真实存在。通过时空分析定位 safety-critical 注意力头，用 K=16 头达到 0.92 检测精度。

7. **Zhou et al. (ICLR 2025, arXiv:2410.13708)**: 真实存在，ICLR 2025 Oral。提出 Ships score，发现单个 safety head 消融可使有害查询响应增加 16×。

8. **多轮安全防御 baselines**: XGuard-Train (COLM 2025), MUSE-D (EMNLP 2025), X-Boundary (EMNLP 2025), MTSA (ACL 2025) 均为真实且已发表的工作。

9. **CoRL 2026 Call for Papers**: 明确要求 "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." 涵盖的主题包括机器人感知、控制、基础模型、模仿学习、强化学习控制物理机器人、机器人安全与对齐等。

- **调研总结**: 多轮 LLM 安全领域在 2025-2026 年进展迅速，攻击机制（注意力竞争、continuation vs. refusal）和防御方法（推理时注意力修改、训练时电路干预、多轮安全训练）都有大量工作。该 proposal 试图在 conversational inertia（discourse 层面）和 safety（安全层面）之间建立因果桥梁，这个连接本身是新的。**但 CoRL 是机器人学习会议，该 proposal 完全没有涉及任何机器人问题。**

---

【⚠️ 致命问题：严重的 venue mismatch】

**这个 proposal 投稿 CoRL 2026 存在根本性的 venue mismatch，这是一个独立于 idea 质量的致命问题。**

CoRL 2026 的 Call for Papers 明确要求：
> "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

该 proposal 的全部内容：
- 核心问题：LLM 多轮对话安全 / jailbreak 防御
- 方法：注意力机制分析 + DPO 训练
- 评估基准：MT-AgentRisk（文本工具调用 agent）、OpenAgentSafety（文本多轮任务）
- 模型：Qwen3-8B、Llama 3.1-8B-Instruct（纯语言模型）
- **零机器人相关内容**：无物理机器人、无 sim-to-real、无操纵/导航/运动、无具身智能

即使 CoRL 包含 "learning approaches to robot safety and alignment" 话题，那也是指**机器人**的安全与对齐，不是 LLM chatbot 的 jailbreak 防御。

**这个 proposal 属于 NeurIPS / ICML / ICLR / ACL / EMNLP 的审稿范畴，投 CoRL 将几乎确定被 desk reject。**

---

【Trivial Alternative 检验】:

**存在强 trivial alternative 威胁。** 

核心问题：如果目标是提升多轮安全性，最直接的方法是**在安全数据上直接训练**——XGuard-Train SFT 已实现高达 48.3% 的脆弱性减少，MTSA 的 RL 方法将 ASR 从 74.5% 降至 23.5%，X-Boundary 在表示层面将 ASR 降至 16-25%。这些方法都是直接针对安全问题训练的。

该 proposal 的增量价值声称是：CPL 通过减少"根因"（注意力惯性）来间接改善安全，而非直接治"症状"。但这个"根因"论断本身是**未经验证的假设**——我们并不知道对角注意力惯性是否真的是多轮安全退化的主要驱动因素。可能的替代解释包括：累积上下文效应、表示漂移（STAR 已提供证据）、或简单的 context window 内安全信号稀释。

如果最终 CPL 确实改善了安全，审稿人的第一个问题必然是："和直接在安全数据上训练相比，CPL 的优势在哪？" Proposal 包含了 XGuard-Train 作为对照，但如果 XGuard-Train 效果更好或相当，CPL 的 narrative 就很难站住脚。

**增量价值判断**：真正的增量在于**机制理解**（per-head 分解、overlap 分析），而非 CPL 本身作为防御方法的实用性。但机制理解类贡献的 impact 天花板较低。

---

【前提假设检验】:

核心 claim 的逻辑链存在**多个未经验证的环节**：

1. **"对角注意力与安全注意力在同一头/层竞争"** — 这是整个 hypothesis 的支柱，但完全是推测。Phase 0.5 的设计正是为了验证这一点，这意味着 proposal 自己也承认这是未知的。如果 Phase 0.5 结果显示 overlap < 10%（Level 3），整个 "attention capacity competition" 故事的说服力会大幅下降。

2. **"CPL 的注意力重分配会具体惠及 safety-relevant tokens"** — CPL 是为了减少 conversational inertia（提升 agent 性能）而设计的通用 discourse 干预，没有任何机制保证它重新分配的注意力会流向安全关键 token 而非其他任务相关 token。

3. **"注意力惯性是多轮安全退化的主要/重要驱动因素"** — 多轮安全退化的机制可能是多方面的：representation drift (STAR)、context dilution、safety instruction forgetting 等。对角注意力惯性可能只是众多因素之一，甚至可能是伴随现象而非因果因素。

4. **"Johnson & Huo 的 tipping point 理论适用于多轮 agent 场景"** — 该理论基于 dot-product 竞争的数学建模，在 edge AI 小模型上验证，其在 8B 参数生产级模型 + 多轮 agent 设置中的适用性并未被验证。

---

【3 维度打分】:

1. **Novelty: 中** — 
   - **新颖的部分**：将 conversational inertia (Wan et al.) 与 safety 连接起来是一个新的 research question；per-head 对角注意力分解确实是 Wan et al. 的空白（他们明确只做了 aggregate 分析）；triple-method head identification 的 cross-validation 设计有方法论贡献。
   - **限制 novelty 的因素**：核心干预方法（CPL）完全借用自 Wan et al.，不是本文提出的新方法；将现有方法应用于新场景（"CPL → safety"）本质上是一个 application/empirical study；Phase 0.5 的 per-head 分解虽然新，但技术上是 straightforward 的分析（对每个头分别计算 Wan et al. 的 metric，不需要新的分析框架）；注意力头 overlap 分析的思路在 Zhou et al. (ICLR 2025) 和 Deng et al. 之后并不令人意外。
   - **与现有工作的差异**：相对于 DETAM（推理时 + 单轮）、ASGuard（训练时 + 电路靶向 + 单轮）、XGuard-Train/MUSE-D/MTSA（训练时 + 直接安全数据），proposal 的定位是"训练时 + discourse 干预 + 多轮"——这个组合确实是新的，但"新组合"和"新洞见"是两回事。

2. **Significance: 中偏弱** — 
   - 多轮安全问题本身很重要，但该 proposal 的核心贡献更偏向**机制验证/理解**（"inertia 和 safety 是否竞争？"）而非**方法创新**（CPL 是借用的）。
   - 如果结果为 positive（CPL 改善安全），审稿人可能的反应是 "interesting connection, but not surprising — if inertia competes with safety attention, reducing inertia should help"。这不满足 "surprising, not what I expected" 的标准。
   - 如果结果为 negative（CPL 不改善安全），null-result 贡献（per-head 分解、overlap 分析）是有价值的但 incremental——它们不会改变领域的研究方向。
   - **对 CoRL 的 significance 为零**——这与机器人学习完全无关。即使对 NLP/AI safety 社区，significance 也受限于核心发现的可预测性。

3. **Related Work: 强** — 
   - 这是 proposal 最突出的部分。Related work 覆盖极为全面，涵盖了注意力重分配防御（DETAM）、训练时头干预（ASGuard）、安全头定位（Zhou et al., AISA, Depth Charge）、注意力竞争理论（Johnson & Huo, Deng et al.）、多轮安全基准和防御（MT-AgentRisk, XGuard-Train, MUSE-D, X-Boundary, MTSA, OpenAgentSafety）以及 discourse dynamics (Wan et al.)。
   - 差异化定位清晰：明确标注了每个相关工作的局限（DETAM: 单轮 + 需要 intent 定位；ASGuard: 电路靶向 + 单轮；直接安全训练：不测试 discourse 机制的因果性）。
   - 引用的论文经核实均真实存在，描述准确。
   - **唯一弱点**：虽然 coverage 全面，但"全面的 related work" 可能部分源于 proposal 将大量不同线索松散连接（6 条独立线索），而非深入聚焦于一个紧密的研究空间。

---

【概率估计】: 0% - 5%，中位 2%

【估计理由】: 

**存在两个独立的限制因素，任何一个都足以致命：**

**（A）Venue Mismatch — 致命（将概率压至 ~0-5%）：** CoRL 2026 明确要求 "focus on a core robotics problem"。该 proposal 是纯 LLM 安全研究，零机器人相关内容，极大概率在 desk review 阶段被拒。这一因素独立于 idea 质量，是投稿策略层面的致命错误。

**（B）即使忽略 venue mismatch，idea 本身的质量对顶会（NeurIPS/ICML/ICLR/ACL）估计约 20-30%：**
- Novelty 中等：核心干预借用自 Wan et al.，本文的新颖性在于"连接"而非"方法"
- 存在 trivial alternative 威胁：直接安全训练可能效果更好
- 核心假设（inertia-safety 竞争）未经验证，是整篇论文的赌注
- 正向结果的 surprise factor 有限

将 (A) 和 (B) 综合：投稿 CoRL 2026 的中稿概率为 0-5%。

【主要风险】: 
1. **致命 venue mismatch**: 该 proposal 是 LLM 多轮安全研究，与 CoRL（Conference on Robot Learning）的 scope 完全不匹配。投稿 CoRL 将几乎确定被 desk reject，无论 idea 质量如何。这是最核心的风险。
2. **核心假设未验证 + trivial alternative**: 如果对角注意力惯性与 safety heads 的 overlap 很低（Phase 0.5 Level 3 结果），整个 competition hypothesis 的说服力大打折扣。同时，直接在安全数据上训练（XGuard-Train 48.3% 脆弱性减少）可能以更低成本达到类似或更好效果，使 CPL 的间接路径显得缺乏动机。
```

---

**补充建议**：如果作者希望推进这个 research，应该：
1. **立即更换目标 venue** — 考虑 NeurIPS 2026、ICLR 2027、ACL 2026/2027、EMNLP 2026 等 NLP/ML 安全相关会议
2. 在适合的 venue 下，idea 有一定潜力（约 20-30%），但需要加强核心假设的前期验证（Phase 0.5 结果应尽早获得以 de-risk），并清晰回应 "为什么不直接在安全数据上训练" 的 trivial alternative 挑战

Sources:
- [DeTAM: ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.613/)
- [DeTAM arXiv](https://arxiv.org/abs/2504.13562)
- [ASGuard: ICLR 2026](https://openreview.net/forum?id=wmiEXNEXPs)
- [ASGuard arXiv](https://arxiv.org/abs/2509.25843)
- [Wan et al. Conversational Inertia arXiv](https://arxiv.org/abs/2602.03664)
- [Johnson & Huo tipping point](https://arxiv.org/abs/2602.14370)
- [Deng et al. Continuation vs Refusal](https://arxiv.org/abs/2603.08234)
- [AISA arXiv](https://arxiv.org/abs/2602.13547)
- [Zhou et al. ICLR 2025 Safety Heads](https://arxiv.org/abs/2410.13708)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Does Reducing Conversational Inertia Improve Multi-Turn Safety? Testing the Attention Capacity Competition Hypothesis

## Description
This project conducts the first controlled interventional study testing whether mitigating conversational inertia — diagonal attention to previous outputs (Wan et al., ICML 2026) — causally reduces multi-turn safety erosion, organized around a refined three-level 'attention capacity competition hypothesis.' We build on DETAM's proof that inference-time attention reallocation improves safety (ASR 46%→1.2%) and ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities, testing whether CPL achieves broad attention reallocation through untargeted discourse training — addressing the progressive multi-turn erosion that DETAM (single-turn, requires runtime intent localization) and ASGuard (targets specific localizable circuits) structurally cannot. In multi-turn crescendo attacks, malicious intent is distributed across turns, making DETAM's intent-token identification ill-defined; CPL instead reduces the cumulative inertia that pushes systems past Johnson & Huo's tipping point. A novel Phase 0.5 provides the first per-head decomposition of diagonal attention (Wan et al. explicitly averages all heads) and measures overlap with safety-critical heads using triple triangulation (Ships score, DETAM sensitivity, AISA spatiotemporal analysis), cross-validated against published head sets (Zhou et al., Depth Charge, ASGuard — whose 4 Layer-13 vulnerable heads independently corroborate the continuation-safety nexus). Our five-phase causal design tests CPL against five confound controls including XGuard-Train SFT at both published and CPL-matched ranks. Mechanistic verification tests whether CPL achieves 'implicit DETAM' (same heads, same direction) and 'implicit circuit modification' (affecting ASGuard's identified vulnerable heads without targeting them). The study is designed for informative outcomes at all three competition levels, with the per-head diagonal attention decomposition, triple-method head identification comparison, and DETAM/ASGuard mechanistic comparison constituting standalone contributions.

## Core Problem
Multi-turn agent interactions exhibit systematic safety degradation (16% higher attack success rates), and while recent work has identified attention-level mechanisms — attention dispersion on safety keywords (ASJA, AAAI 2025), competition between safety and continuation heads (Deng et al., 2026), and attention reallocation as a defense (DETAM, ACL 2025 Findings) — and developed multi-turn safety defenses (MUSE-D turn-level DPO, EMNLP 2025; XGuard-Train SFT, COLM 2025; X-Boundary representation boundaries, EMNLP 2025; MTSA RL-based alignment, ACL 2025), and even training-time attention head interventions for specific vulnerability types (ASGuard circuit-targeted scaling, ICLR 2026), these studies are either attack-oriented, single-turn, operate at inference time, target specific localizable vulnerabilities, or train directly on safety-labeled data without testing whether discourse-level mechanisms causally drive safety erosion. Critically, DETAM (Li et al., ACL 2025 Findings) demonstrates that simply reallocating attention from attack tokens toward safety-relevant tokens at inference time — without any weight changes — reduces ASR from 46% to 1.2% on LLaMA-2, providing the strongest existing evidence that attention redistribution causally improves safety. Yet DETAM requires explicit identification of 'intent tokens' at runtime and operates only in single-turn settings — in multi-turn crescendo attacks where malicious intent is progressively distributed across turns, the notion of localizable 'intent tokens' breaks down fundamentally. ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant heads is feasible via circuit-targeted scaling vectors, but its efficacy 'hinges on localizable causal circuits' for specific attack types (tense jailbreaking) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits. No work has tested whether a training-time discourse intervention (reducing conversational inertia) achieves broad attention reallocation indirectly, nor whether the specific attention heads carrying diagonal inertia patterns overlap with safety-critical heads — a prerequisite for the softmax zero-sum competition mechanism to operate at the head level. Notably, the only characterization of diagonal attention (Wan et al., ICML 2026) reports aggregate-level patterns averaged across all heads; no per-head decomposition exists, leaving the head-level competition question empirically open. Additionally, the response-length confound in DPO-based interventions has never been explicitly controlled for in safety evaluations of discourse-level interventions.

## Opportunity
Six independent research threads have converged to make a controlled causal study newly feasible: (1) Conversational Inertia (Wan et al., ICML 2026) identifies diagonal attention where the i-th token attends to the i-th previous output position and provides Context Preference Learning (CPL) as a parameter-efficient intervention (0.4% params, LoRA rank-16 DPO with beta=0.01), validated on Qwen3-8B and Llama 3.1-8B-Instruct across eight agentic environments but never evaluated for safety — crucially, the diagonal attention pattern is characterized only at the aggregate level (averaged across all heads), so the per-head distribution remains unknown; (2) DETAM (Li et al., ACL 2025 Findings) provides direct causal evidence that attention reallocation toward safety-relevant tokens improves safety — reducing ASR by 97%+ without weight modification — but requires runtime intent token identification and is single-turn only, creating a fundamental limitation for multi-turn settings where intent is distributed across turns; (3) ASGuard (Park et al., ICLR 2026) demonstrates that training-time modification of safety-relevant attention heads is feasible via circuit-targeted channel-wise scaling vectors and preventative fine-tuning — crucially, ASGuard identifies 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30), exactly where Deng et al. find continuation heads, providing independent corroboration that Layer 13 is a nexus of safety-relevant competition — but ASGuard targets specific localizable vulnerability circuits (tense jailbreaking) rather than discourse-level dynamics; (4) Multi-turn safety erosion is now well-benchmarked via MT-AgentRisk (365 tasks, 5 tools, avg 3.19 turns) with ToolShield as a defense baseline, and supplemented by OpenAgentSafety (ICLR 2026, 356 real-tool tasks with multi-turn multi-user dynamics); (5) Multi-turn safety training has mature baselines spanning multiple paradigms: XGuard-Train SFT (COLM 2025, up to 48.3% vulnerability reduction), MUSE-D turn-level DPO (EMNLP 2025, 24% ASR reduction), X-Boundary representation-level boundaries (EMNLP 2025, ASR reduction to 16-25%), and MTSA RL with future rewards (ACL 2025, ASR 74.5% to 23.5%) — but all train directly on safety-labeled data; (6) AISA (Song et al., arXiv:2602.13547) provides a third complementary method for localizing safety-critical attention heads via spatiotemporal analysis — identifying that safety-discriminative signals concentrate in middle-layer head outputs with K=16 heads achieving 0.92 detection accuracy — enabling methodological triangulation in our head overlap analysis. This six-thread convergence, combined with Johnson & Huo's (2026) formalization of attention competition tipping points and the layered distribution of safety mechanisms across layers 2-27, motivates a three-level attention capacity competition hypothesis testable through a novel Phase 0.5 head overlap analysis.

## Related Work / Landscape
**Attention reallocation defenses:** DETAM (Li et al., ACL 2025 Findings, arXiv:2504.13562) is the most directly relevant inference-time prior work. It identifies attention heads sensitive to jailbreaks by computing attention score differences between successful and unsuccessful defenses (threshold alpha: 0.1 for LLaMA-2, 0.03 for Vicuna). During inference, it modifies the causal mask matrix by multiplying mask values at intent token positions by beta=5.0, amplifying attention to the user's core intention. DETAM reduces average ASR from 46.0% to 1.2% on LLaMA-2-7b-chat and from 81.8% to 4.0% on Vicuna-13b-v1.5. Cross-model transferability: sensitive heads from LLaMA-2 transferred to Meta-LLaMA-3 achieve 4% ASR vs. 96% vanilla. However, DETAM has three fundamental limitations for multi-turn agent settings: (a) it requires runtime identification of 'intent tokens' — in multi-turn crescendo attacks (Russinovich et al., USENIX Security 2025) where harmful intent is progressively distributed across turns, no single set of tokens constitutes 'the intent,' making DETAM's token-level localization fundamentally ill-defined; (b) it is tested only in single-turn settings and cannot address the cumulative attention shift across turns that Johnson & Huo's tipping point theory predicts; (c) it imposes per-turn computational overhead for mask modification in each forward pass across all turns of agent interaction. Our study tests whether CPL achieves DETAM-like attention redistribution persistently through training, addressing a failure mode DETAM structurally cannot: the gradual accumulation of continuation pressure across turns that progressively dilutes safety attention below the tipping point. **Training-time attention head intervention:** ASGuard (Park et al., ICLR 2026, arXiv:2509.25843) is the closest existing work to training-time attention head modification for safety. It uses Edge Attribution Patching with Integrated Gradients (EAP-IG) to identify attention heads causally linked to specific jailbreaking vulnerabilities, trains channel-wise activation scaling vectors (s_j ∈ R^{d_head}, applied via Hadamard product H'_{l,j} = H_{l,j} ⊙ s_j) on identified heads, and applies preventative fine-tuning with scaling vectors frozen. On tense jailbreaking, ASGuard reduces ASR from 42% to 8% on Llama-3.1-8B and 51% to 8% on Qwen2.5-7B, achieving Pareto-optimal safety-utility balance. Critically, ASGuard identifies 11 vulnerable heads in Llama-3.1-8B, of which 4 are at Layer 13 (L13H8, L13H18, L13H25, L13H30) — exactly where Deng et al. find continuation heads — providing independent corroboration that Layer 13 is a nexus of safety-relevant attention competition. However, ASGuard differs from our approach in three key ways: (a) it targets specific, localizable vulnerability circuits ('efficacy hinges on localizable causal circuits' — their Limitations, Section 7) — multi-turn safety erosion through cumulative discourse dynamics may not produce such localizable circuits, as the failure is progressive rather than circuit-specific; (b) it surgically fixes known attack types (tense jailbreaking, GCG, LogiBreak) one at a time, whereas CPL is an untargeted discourse intervention testing whether reducing general inertia achieves broad safety benefits; (c) it is single-turn only. ASGuard's success actually supports a key premise of our hypothesis: training-time modification of attention heads CAN improve safety. Our study tests whether indirect, untargeted discourse training achieves what targeted head intervention achieves — and whether it generalizes to the multi-turn progressive erosion that targeted approaches cannot address. **Safety head localization methods:** AISA (Song et al., arXiv:2602.13547) provides a third complementary approach to localizing safety-critical heads via spatiotemporal analysis — large-scale linear probing across 15 positions per layer identifies that attention head outputs demonstrate superior safety separability, with top-K=16 heads (concentrated in middle layers) achieving 0.92 detection accuracy and O(1) runtime overhead. AISA's finding that safety heads cluster in middle layers in standard models but shift toward higher layers in strongly safety-aligned models adds nuance to the competition hypothesis — the relevant layers may differ by alignment strength. **Attack-side mechanisms:** Du et al. (ASJA, AAAI 2025) show that successful multi-turn jailbreaks correlate with attention dispersion away from safety keywords (p=4.38e-07), achieving 44.9% higher ASR. Deng et al. (arXiv:2603.08234) identify competing safety and continuation attention heads — safety heads concentrated in layers 25-27, continuation heads in middle layers (~Layer 13) — whose antagonistic interaction determines jailbreak success. Notably, continuation heads at Layer 13 occupy the same layer range as both induction/copying mechanisms AND ASGuard's identified vulnerable heads, suggesting this layer is a critical nexus where diagonal attention patterns, continuation signals, and safety vulnerability converge. Depth Charge (Wu et al., arXiv:2603.05772, March 2026) introduces SAHA using Ablation-Impact Ranking and Layer-Wise Perturbation, achieving 82-91% ASR, revealing layer-specific safety head concentrations (layer 7 for Llama 3.1-8B, layer 5 for Qwen 1.5-7B, head 31 universally important) and sharp threshold behavior. Attention Eclipse (Zaree et al., arXiv:2502.15334) achieves 91.2% ASR by manipulating attention to strengthen harmful content focus and weaken safety focus. **Attention competition theory:** Johnson & Huo (arXiv:2602.14370, Feb 2026) formalize the competition-for-attention mechanism mathematically, showing that dot-product competition creates dynamical tipping points (n*) where behavior transitions from safe to unsafe — providing the theoretical framework for why cumulative inertia across turns can push the system past a tipping point that single-turn defenses like DETAM cannot prevent. **Multi-turn safety benchmarking:** Yang et al. (arXiv 2026) document 16% average ASR increase on MT-AgentRisk and propose ToolShield (~30% ASR reduction). OpenAgentSafety (ICLR 2026) provides 356 multi-turn, multi-user tasks with real tools. Li et al. (STAR, arXiv:2603.15684) show monotonic drift from refusal representations. MultiBreak (arXiv:2605.01687) provides 10,389 multi-turn adversarial prompts. **Multi-turn safety defenses:** X-Teaming (COLM 2025, arXiv:2504.13203) introduces XGuard-Train, a 30K multi-turn safety training dataset. Models SFT-trained on a 14K subset with LoRA rank-8, lr=1e-4, 3 epochs achieve up to 48.3% vulnerability reduction on Llama-3.1-8B and Qwen-2.5-7B. MUSE-D (EMNLP 2025, arXiv:2509.14651) applies turn-level DPO achieving 24% ASR reduction. X-Boundary (Lu et al., EMNLP 2025, arXiv:2502.09990) operates at the representation level, reducing multi-turn ASR from 58.5-76.0% to 16.0-25.0% while reducing over-refusal by ~20%. MTSA (Guo et al., ACL 2025, arXiv:2505.17147) performs RL with future rewards, reducing ASR from 74.5% to 23.5%, with the finding that maximum attack effectiveness peaks at round 5 — confirming multi-turn pressure accumulates through discourse dynamics. Agent Safety Alignment (Sha et al., arXiv:2507.08270) proposes unified sandboxed RL with benign/malicious/sensitive taxonomy. STREAM (arXiv:2506.00668) proposes safety reasoning moderator reducing ASR by 51.2%. TurnGate (arXiv:2605.05630) introduces turn-level harm detection. **Discourse dynamics:** Wan et al. (ICML 2026, arXiv:2602.03664; note: also submitted to ICLR 2026 as OpenReview #UubLs3lUfk, subsequently published in PMLR 306 at ICML 2026, Seoul, July 6-11) identify conversational inertia and propose CPL. The paper characterizes diagonal attention only at the aggregate level — explicitly stating 'All attention heads are averaged to create a unified attention matrix' and 'the trend of diagonal attention in the final layer is similar to other layers' — with no per-head decomposition. Code not released. **Safety attention head mechanisms:** Zhou et al. (ICLR 2025, arXiv:2410.13708) show the single most critical head in Llama-2-7B-Chat is Head (2, 26) at Layer 2. Wei et al. identify safety layers at layers 9-14. The refusal direction (Arditi et al.) is strongest around layer 15. Safety Alignment Should Be Made More Than Just A Few Attention Heads (arXiv:2508.19697) proposes distributed safety head training. **Safety persistence:** Plaut (arXiv:2603.02229) shows LoRA safety DPO persists with 90-94% retention, Pareto frontier R-squared=0.77, slope=-0.83. **DPO length bias:** Park et al. (2024) and Meng et al. (2024) document hidden length dependence. **Gap:** Despite convergent progress on inference-time attention reallocation (DETAM), training-time targeted head intervention (ASGuard), training-time safety defenses (XGuard-Train, MUSE-D, X-Boundary, MTSA), safety head localization (Zhou et al., AISA, Depth Charge), attention competition theory (Johnson & Huo), and discourse dynamics (conversational inertia), no work has: (a) tested whether a training-time discourse intervention achieves broad DETAM-like attention reallocation and causally reduces safety erosion in multi-turn settings — addressing the progressive accumulation that both DETAM (single-turn only) and ASGuard (circuit-specific only) cannot; (b) provided a per-head decomposition of diagonal attention to determine whether inertia heads overlap with safety heads; (c) compared discourse-targeted vs. safety-targeted training under matched parameter budgets; or (d) controlled for DPO response-length confounds in discourse-safety evaluations.

## Approach
We run a five-phase causal study on MT-AgentRisk (primary) and OpenAgentSafety (secondary) benchmarks using Qwen3-8B and Llama 3.1-8B-Instruct, organized around the 'attention capacity competition hypothesis' and motivated by a specific gap that neither DETAM nor ASGuard can address: progressive multi-turn safety erosion through cumulative discourse dynamics.

**Why Training-Time Discourse Intervention? The Multi-Turn Intent Distribution Problem.** DETAM achieves 97%+ ASR reduction in single-turn settings at zero training cost — but it requires identifying 'intent tokens' at runtime. In multi-turn crescendo attacks where harmful intent is progressively distributed across 3-10 turns (MTSA finds peak attack at round 5), no single set of tokens constitutes 'the intent.' The malicious instruction at turn 7 is only harmful in the context of the innocuous-seeming turns 1-6 that established the frame. DETAM cannot solve this because its mechanism — amplifying attention to intent tokens in sensitive heads — presupposes that intent is localizable within a single turn. ASGuard demonstrates training-time head modification is feasible but targets specific localizable circuits (tense jailbreaking), and its own Limitations section notes 'efficacy hinges on localizable causal circuits.' Multi-turn safety erosion through cumulative inertia is NOT a localizable circuit — it's a progressive process where each turn incrementally shifts the attention distribution. CPL's advantage is that it operates at the discourse dynamics level: reducing the cumulative inertia that progressively dilutes safety attention across turns, without needing to identify which tokens are 'intent' tokens or which circuits carry a specific vulnerability. It addresses the ROOT CAUSE (attention inertia accumulation across turns) rather than the SYMPTOM (misallocated attention at any single turn). This is the failure mode that Johnson & Huo's tipping point theory predicts: gradual accumulation of continuation pressure pushes the system past n* — and the only way to prevent reaching the tipping point is to reduce the per-turn accumulation rate, which is exactly what CPL does.

**The Attention Capacity Competition Hypothesis (Three-Level Framework):** We theorize that diagonal attention (the inertia mechanism) competes with safety-keyword attention at three distinct levels: **Level 1 (Head-level, strong form):** If diagonal attention and safety attention share the same heads, softmax's zero-sum constraint directly displaces safety-keyword attention. Given that safety heads span layers 2-27 and induction/copying mechanisms typically concentrate in middle layers, partial overlap is plausible. **Level 2 (Layer-level, medium form):** If diagonal and safety attention occupy different heads within the same or adjacent layers, competition occurs through the residual stream. This is supported by Deng et al.'s finding that continuation heads (Layer 13) antagonize safety heads (Layers 25-27), and strikingly corroborated by ASGuard's identification of 4 vulnerable heads at Layer 13 in Llama-3.1-8B (L13H8, L13H18, L13H25, L13H30) — the same layer where continuation heads reside, independently confirming Layer 13 as a nexus of safety-relevant competition. **Level 3 (Representation-level, weak form):** Competition mediated through accumulated representation drift, validated by X-Boundary's success (ASR 58.5% to 16.5%). Phase 0.5 empirically determines which level(s) apply.

**Phase 0 — CPL Acquisition/Reproduction + Baseline Preparation (weeks 1-3):** Contact Wan et al. for CPL checkpoints (ICML 2026 July 6-11). Simultaneously reproduce CPL using TRL DPOTrainer + PEFT: LoRA rank-16, alpha-16, 0.4% params, DPO with beta=0.01, sigmoid loss, 2 epochs, lr=5e-7, AdamW, 1000 preference pairs per environment. The training recipe maps directly to TRL v1.0+ (sigmoid loss is the default DPOConfig, all hyperparameters natively supported); the main reproduction risk is the preference pair construction pipeline (dual-rollout with long-context vs. short-context on AgentGym environments) rather than the training loop itself. Estimated: ~40 A100-hours per model. In parallel, prepare XGuard-Train SFT baselines: (a) LoRA rank-8 with lr=1e-4, 3 epochs (matching published configuration from X-Teaming, validated on Llama-3.1-8B and Qwen-2.5-7B); (b) LoRA rank-16 with CPL-matched hyperparameters for parameter-matched comparison. Construct extended-turn variants: prepend 4-6 benign tool-use turns to 50 representative MT-AgentRisk tasks.

**Hard Go/No-Go Checkpoint at Week 3:** The project proceeds to Phase 0.5 only if ALL criteria are met: (1) AgentGym environment setup working for >=3 of 8 environments (prioritizing ALFWorld, WebShop, HotpotQA); (2) dual-rollout preference pair generation produces pairs where long-context trajectories show measurably higher diagonal attention scores than short-context trajectories (statistically significant at p<0.05 on at least 2 environments); (3) DPO training pipeline converges (decreasing loss, increasing reward margins over 2 epochs); (4) base model evaluation on >=2 environments matches Wan et al.'s published baselines within 1 SEM. **Fallback paths:** (a) environment failure: proceed with 2-3 most reliable environments; (b) inertia differential failure: pivot to correlational-only study (Phases 1 and 4 only); (c) training failure: debug 1 additional week — if still failing by week 4, pivot to 'DETAM in multi-turn settings' (extending DETAM's mechanism to MT-AgentRisk, testing whether Focus Loss intensifies across turns).

**Phase 0.5 — Head Overlap Test and Per-Head Diagonal Attention Decomposition (weeks 3-4, ~20 A100-hours):** This phase provides the first per-head decomposition of diagonal attention patterns and tests the prerequisite assumption of the competition hypothesis. Using both base models on 50 MT-AgentRisk tasks: (a) **Novel per-head diagonal attention decomposition:** Compute diagonal attention scores per head (not just aggregate) using Wan et al.'s metric (attention between current output position i and previous assistant output position i +/- 5 tokens) — this is the first such decomposition, given that Wan et al. explicitly average all heads ('All attention heads are averaged to create a unified attention matrix'). Identify which heads carry the strongest diagonal patterns and their layer distribution. (b) **Safety head identification via triple triangulation:** Apply three complementary methods: (i) Ships score (Zhou et al., ICLR 2025) via KL divergence after head ablation; (ii) DETAM's sensitivity metric (attention score differences between successful/unsuccessful safety responses); (iii) AISA's spatiotemporal analysis — linear probing on head outputs at final structural tokens to identify safety-discriminative heads (K=16). Cross-validate against published localizations: Zhou et al.'s Head (2,26) for Llama-2-family; Depth Charge's layer-specific data (layer 7 for Llama 3.1-8B); ASGuard's EAP-IG identified heads (11 heads for Llama-3.1-8B including 4 at Layer 13). Using three independent methods plus cross-validation against three published head sets provides robust head identification. (c) **Overlap analysis:** Compute Jaccard index between top-k diagonal attention heads and top-k safety heads (k = 5, 10, 20, 50) with permutation tests. Also measure layer-level co-occurrence (same layer, different heads). Cross-reference against ASGuard's Layer 13 vulnerable heads — if diagonal attention heads concentrate at Layer 13, this would connect conversational inertia to the continuation-safety competition nexus identified by both Deng et al. and ASGuard independently. (d) **Level determination:** Level 1 (>30% head overlap) — proceed with strong per-head softmax hypothesis; Level 2 (same layers, <30% head overlap) — reformulate around residual stream competition, particularly the Layer 13 continuation-inertia-safety nexus; Level 3 (<10% overlap in both heads and layers) — reformulate around representation-level competition. Each determination shapes subsequent analysis. This phase costs ~20 A100-hours but de-risks the project and provides standalone novel contributions (first per-head diagonal attention map; first triple-method safety head identification comparison).

**Phase 1 — Correlational with Attention Capacity Analysis (weeks 4-7):** Measure diagonal attention (per-head, informed by Phase 0.5) AND safety-keyword attention concentration at each turn on 365 MT-AgentRisk tasks and 50 extended-turn variants. Calibrate analysis to competition level from Phase 0.5. Fit mixed-effects regressions testing P1 (diagonal attention negatively correlates with safety attention at the operative level), controlling for turn position, task category, model, and response token count. Test Granger causality for temporal dynamics.

**Phase 2 — Interventional with Confound Controls (weeks 7-11):** Apply CPL and re-evaluate on MT-AgentRisk. Five control conditions: (a) **Random-Preference LoRA** — shuffled preference labels, same architecture; (b) **Reversed-CPL** — prefer long-context over short-context; (c) **XGuard-Train SFT (rank-8)** — published configuration for validation against published results; (d) **XGuard-Train SFT (rank-16)** — CPL-matched parameters for direct paradigm comparison (discourse-targeted vs. safety-targeted training); (e) **Response-Length Analysis** — ASR stratified by length quartiles, per-100-token normalization, regression with length covariate (testing P3: CPL's safety effect, if any, is not explained by response-length changes). Frame CPL's effect relative to both DETAM and ASGuard: test whether CPL affects the same heads DETAM identifies as sensitive and shifts attention in the same direction (implicit DETAM test), and whether it affects ASGuard's identified vulnerable heads at Layer 13 (implicit untargeted circuit modification test). Compare against ToolShield baseline and MUSE-D's published results.

**Phase 3 — Autonomy Tax Audit (weeks 9-11, parallel):** Step-1 completion rate, cascade failure rate, end-to-end success, over-refusal. Report safety-competence Pareto frontier extending Plaut's analysis. Compare CPL's frontier position with X-Boundary's ~20% over-refusal reduction, ASGuard's Pareto-optimal balance, and XGuard-SFT's published results.

**Phase 4 — Mechanistic Verification (weeks 10-14):** (a) SRI signal framework for step-wise refusal dynamics; (b) Head-level analysis extending Deng et al.'s safety-continuation head identification to multi-turn, calibrated by Phase 0.5 overlap findings — test whether CPL modulates the Layer 13 continuation vs. Layer 25-27 safety head balance across conversation turns; (c) **DETAM-informed analysis:** Apply DETAM's sensitivity metric to CPL-treated models — does CPL training shift attention in the same heads and direction that DETAM targets at inference time? If so, CPL achieves 'implicit DETAM' through discourse training, but persistently and without runtime intent localization; (d) **ASGuard-informed analysis:** Test whether CPL affects ASGuard's identified vulnerable heads (particularly the 4 at Layer 13) despite not targeting them — this would demonstrate that untargeted discourse training can modify the same heads that targeted circuit analysis identifies, but as a side effect of reducing general inertia rather than through explicit circuit surgery; (e) Level-appropriate analysis: Level 2 — residual stream composition analysis at shared layers; Level 3 — representation trajectory analysis following X-Boundary's framework.

**Secondary Evaluation — OpenAgentSafety (weeks 12-14):** Best-performing config and XGuard-SFT on a subset for ecological validity.

**Null-Result Framing Strategy:** (1) First per-head decomposition of diagonal attention patterns and their overlap (or non-overlap) with safety heads — novel regardless of CPL results; (2) First triple-method safety head identification comparison (Ships + DETAM sensitivity + AISA spatiotemporal), cross-validated against three published head sets (Zhou et al., Depth Charge, ASGuard); (3) Empirical evidence for or against the three-level competition hierarchy; (4) First confound-controlled causal framework for discourse-safety evaluation; (5) First discourse-targeted vs. safety-targeted training comparison under matched parameters; (6) First multi-turn extension of DETAM's Focus Loss analysis; (7) Empirical test of whether CPL-like untargeted training affects the same heads as ASGuard's targeted circuit intervention.

**Extended-Turn Variant Validity (Limitation):** Acknowledged with mitigations: OpenAgentSafety for ecological validity, attention pattern validation, conservative amplification framing.

All primary experiments use MT-AgentRisk (365 tasks), ToolShield codebase (GitHub: CHATS-lab/ToolShield), XGuard-Train (HuggingFace: marslabucla/XGuard-Train), and the CPL training recipe from Wan et al. (ICML 2026).

## Inspiration
Field guide Section 4 (cascading failures, production gap) + Section 5.2 (error propagation as primary bottleneck). Key insight: DETAM's demonstration that inference-time attention reallocation dramatically improves safety (ASR 46% to 1.2%) establishes the empirical foundation for our hypothesis — if explicitly redirecting attention works, does implicit redirection via discourse training also work? ASGuard's demonstration that training-time head modification is feasible for specific vulnerabilities raises the natural question: can untargeted discourse training achieve what targeted circuit intervention achieves, but for the progressive multi-turn erosion that circuit-based approaches cannot address? The three-level competition hierarchy was motivated by the finding that Wan et al. only characterizes diagonal attention at the aggregate level (explicitly averaging all heads into a unified matrix) and that safety heads span multiple layer ranges (L2, L9-14, L25-27), while continuation heads at Layer 13 overlap with both induction/copying head territory and ASGuard's identified vulnerable heads (4 of 11 Llama-3.1-8B vulnerable heads are at L13). Johnson & Huo's (2026) formalization of attention competition tipping points provides the theoretical framework for why cumulative discourse inertia can push multi-turn interactions past a safety threshold that per-turn defenses cannot prevent. The reviewer's observation about per-head specificity led to Phase 0.5, which provides the first per-head decomposition of diagonal attention — a novel contribution regardless of results. AISA's spatiotemporal analysis provides methodological triangulation for safety head identification, strengthening Phase 0.5's robustness.

## Key References
- DETAM: Defending LLMs Against Jailbreak Attacks via Targeted Attention Modification (Li et al., ACL 2025 Findings, arXiv:2504.13562)
- ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack (Park et al., ICLR 2026, arXiv:2509.25843)
- AISA: Awakening Intrinsic Safety Awareness in Large Language Models against Jailbreak Attacks (Song et al., arXiv:2602.13547, Feb 2026)
- Multi-Turn Jailbreaking Large Language Models via Attention Shifting (ASJA, AAAI 2025)
- Mitigating Conversational Inertia in Multi-Turn Agents (Wan et al., ICML 2026, arXiv:2602.03664)
- Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents (Yang et al., arXiv 2026)
- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents (COLM 2025, arXiv:2504.13203)
- MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety (EMNLP 2025, arXiv:2509.14651)
- X-Boundary: Establishing Exact Safety Boundary to Shield LLMs from Multi-Turn Jailbreaks without Compromising Usability (Lu et al., EMNLP 2025, arXiv:2502.09990)
- MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming (Guo et al., ACL 2025, arXiv:2505.17147)
- Agent Safety Alignment via Reinforcement Learning (Sha et al., arXiv:2507.08270)
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (Plaut, arXiv:2603.02229, March 2026)
- The Struggle Between Continuation and Refusal (Deng et al., arXiv:2603.08234, Mar 2026)
- The Autonomy Tax: Defense Training Breaks LLM Agents (Li & Zhao, arXiv:2603.19423, Mar 2026)
- On the Role of Attention Heads in Large Language Model Safety (Zhou et al., ICLR 2025, arXiv:2410.13708)
- Depth Charge: Jailbreak Large Language Models from Deep Safety Attention Heads (Wu et al., arXiv:2603.05772, Mar 2026)
- Safety Alignment Should Be Made More Than Just A Few Attention Heads (Huang et al., arXiv:2508.19697, 2025)
- Competition for attention predicts good-to-bad tipping in AI (Johnson & Huo, arXiv:2602.14370, Feb 2026)
- Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment (Zaree et al., arXiv:2502.15334, Feb 2025)
- Safety Layers in Aligned Large Language Models (Wei et al., arXiv:2408.17003, 2024)
- Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., arXiv:2406.11717, 2024)
- State-Dependent Safety Failures in Multi-Turn Language Model Interaction (STAR, arXiv:2603.15684, Mar 2026)
- OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety (ICLR 2026, arXiv:2507.06134)
- One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue (TurnGate, arXiv:2605.05630, May 2026)
- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv:2605.01687, May 2026)
- STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (arXiv:2506.00668, May 2025)
- Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions (arXiv 2026)
- Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2026)
- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv 2025)
- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction (arXiv 2026)
- SafetyDrift: Predicting When AI Agents Cross the Line Before They Actually Do (arXiv 2026)
- Token Statistics Reveal Conversational Drift in Multi-turn LLM Interaction (arXiv 2026)
- Asking Forever: Universal Activations Behind Turn Amplification (arXiv:2602.17778, Feb 2026)
- Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models (arXiv:2602.02600, Feb 2026)
- Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection (arXiv:2604.28129, Apr 2026)
- Many-Turn Jailbreaking (arXiv:2508.06755, Aug 2025)
- Disentangling Length from Quality in Direct Preference Optimization (Park et al., arXiv:2403.19159, 2024)
- Length Desensitization in Direct Preference Optimization (Meng et al., arXiv:2409.06411, 2024)
- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., USENIX Security 2025, arXiv:2404.01833)

## Resource Estimate
- **manual**: {'gpu_hours': '720-900 A100-hours (CPL reproduction 2 models ~80h, XGuard-SFT rank-8 + rank-16 training 2 models ~60h, 2 control LoRAs for 2 models ~80h, Phase 0.5 head overlap test with AISA probing ~25h, MT-AgentRisk evaluation across 6 conditions x 2 models ~240h, extended-turn evaluation ~40h, OpenAgentSafety subset ~60h, SRI signal analysis ~30h, attention analysis including per-head diagonal decomposition + DETAM-informed + ASGuard-informed metrics ~85h, head-level safety-continuation analysis ~40h, response-length analysis ~10h)', 'timeline': '15-17 weeks (3 weeks Phase 0 + go/no-go, 1 week Phase 0.5, 3 weeks Phase 1, 4 weeks Phase 2 + Phase 3 parallel, 4 weeks Phase 4 + OpenAgentSafety, 3 weeks writing; comfortable for ICLR 2027)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}
- **human_in_loop**: {'gpu_hours': '720-900 A100-hours', 'timeline': '13-15 weeks (Claude accelerates CPL reproduction, Phase 0.5 triple-method pipeline, DETAM/ASGuard comparison metrics, statistical analysis)', 'claude_api_cost': '$300-450 (CPL reproduction, per-head diagonal decomposition, triple-method head overlap analysis, DETAM/ASGuard-informed metrics, experiment orchestration, statistical modeling)', 'estimated_gpu_cost': '$1080-1350 at $1.50/A100-hr spot pricing'}
- **auto_research**: {'gpu_hours': '920-1140 A100-hours (additional automated sweeps, full OpenAgentSafety evaluation, extended ablation across competition levels, comprehensive per-head analysis with triple methods)', 'timeline': '9-11 weeks (parallelized execution, automated Phase 0.5 -> Phase 1 pipeline)', 'claude_api_cost': '$600-850 (end-to-end orchestration including CPL reproduction, triple-method head analysis, DETAM/ASGuard comparison, control sweeps, result interpretation, draft generation)', 'estimated_gpu_cost': '$1380-1710 at $1.50/A100-hr spot pricing', 'speed_bottleneck': 'Sequential multi-turn interaction generation; 12 model configurations (2 models x 6 conditions); Phase 0.5 is a serial dependency before Phase 1; triple-method safety head analysis computationally intensive'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f993c679-4d0e-4ec4-834b-a96d32ce2ef9",
  "type": "user",
  "uuid": "c43e5a5b-ca98-45fa-96f7-5df2e85bc672",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T20:52:44.876Z_

```json
{
  "parentUuid": "c43e5a5b-ca98-45fa-96f7-5df2e85bc672",
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
  "uuid": "a455c9fe-9c4f-4621-8309-07571ca4b01b",
  "timestamp": "2026-05-19T20:52:44.876Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T20:52:44.876Z_

```json
{
  "parentUuid": "a455c9fe-9c4f-4621-8309-07571ca4b01b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "536c0f8c-81ec-4619-b45f-4beacddd183e",
  "timestamp": "2026-05-19T20:52:44.876Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information. Let me compile my evaluatio…",
  "leafUuid": "536c0f8c-81ec-4619-b45f-4beacddd183e",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Multi-turn LLM safety and attention competition hypothesis",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c"
}
```

---

### Assistant

_source line 8 · 2026-05-19T20:53:30.312Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to my Meta Judge role.

Let me extract the key data points:

**Reviewer 1:**
- CoRL 2026: 0-2%
- Matching venue (ICLR 2027): [18% - 28%] 中位 22%
- Novelty: 中
- Significance: 中
- Related Work: 强
- Key concerns: Trivial alternative (direct safety training), 3 unverified assumptions, "method transfer + hypothesis verification" not new method/theory, dual-conditional results
  
**Reviewer 2:**
- CoRL 2026: 0-2%, 中位 1%
- Matching venue (ICLR 2027): [20% - 30%] 中位 24%
- Novelty: 中
- Significance: 弱-中
- Related Work: 强
- Key concerns: "So what?" risk, trivial alternative, core assumption collapse risk, surprise value limited

**Reviewer 3:**
- CoRL 2026: [0% - 5%] 中位 2%
- Matching venue: ~20-30%
- Novelty: 中
- Significance: 中偏弱
- Related Work: 强
- Key concerns: Venue mismatch (fatal flaw), limited novelty, weak significance

Now I'm aggregating the acceptance probabilities. For CoRL 2026, the three reviewers converge tightly around 1-2%, with a median of 1%. For a better-matched venue like ICLR 2027, the estimates cluster around 22-25%, suggesting the paper's core ideas have more potential in the right context. all three reviewers agree on the fatal venue mismatch with CoRL, and they're also aligned on several other critical issues: medium novelty, strong related work coverage, medium-to-weak significance, the threat of direct safety training as a simpler alternative, the unverified attention competition hypothesis, risks from the dual-conditional structure and long assumption chains, CPL being a borrowed rather than novel method, limited surprise value, and Phase 0.5 Level 3 risks undermining the narrative. Only one reviewer flagged concerns about Johnson & Huo theory applicability.

Now I'm looking at the venue probability estimates—R1 at 22%, R2 at 24%, R3 around 25%—with very tight consistency around 1.5% standard deviation. All three converge on the 20-28% range, so I should anchor to the median area given this agreement. But I need to be careful here since the proposal explicitly targets CoRL 2026, and the reviewers have independently flagged this as a fundamental mismatch.

For CoRL specifically, this is essentially a rejection—R1 gives ~1%, R2 gives 1%, R3 gives 2%, with standard deviation around 0.6%. The consistency is high, so the median sits right around 1%. I should present both the CoRL assessment and the conditional matching venue estimates since all three reviewers provided those alternative probabilities. 最终概率: [0% - 3%] 中位 1%

**Matching venue (ICLR 2027):**
三次中位: [22%, 24%, 25%], std ≈ 1.5% → High consistency
最终概率: [18% - 28%] 中位 23%

Recommendation: For CoRL → KILL (venue mismatch). For matching venue → 不推荐 (below 36% threshold, but not unsalvageable with work).

Since the formal output format requires a single set of numbers and CoRL 2026 is the stated target, I'll make that the primary recommendation of KILL due to guaranteed desk rejection from venue mismatch, while noting that the paper could potentially reach ~23% acceptance probability at a better-matched venue with further refinement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "536c0f8c-81ec-4619-b45f-4beacddd183e",
  "isSidechain": false,
  "requestId": "req_011CbCbDFLXwFuvQhsgLPhax",
  "type": "assistant",
  "uuid": "e09af151-9217-4a5e-b42e-3eb9b9742887",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cYxDW6oRFqZBb2n9ZnahZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31770,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4485,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 31770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31770
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

_source line 9 · 2026-05-19T20:54:37.308Z_

【阶段】: Meta Judge

【三次中位（CoRL 2026）】: [1%, 1%, 2%]  std=0.6%
【三次中位（匹配会场 ICLR 2027）】: [22%, 24%, 25%]  std=1.5%

【共识维度】:
1. **Venue Mismatch — 致命**（3/3 一致）：CoRL 2026 明确要求 "focus on a core robotics problem"，本 proposal 是纯 LLM 多轮安全研究，零机器人内容，将被 desk reject。三位审稿人均独立发现并以"致命"级别标注。信号极强。
2. **Novelty — 中**（3/3 一致）：核心干预（CPL）借用自 Wan et al.，本文贡献本质是"方法迁移 + 假设验证"，非新方法/新理论。Per-head 分解是增量 engineering novelty。三位审稿人措辞高度一致（"连接两个已知现象"、"新组合 ≠ 新洞见"、"application/empirical study"）。
3. **Related Work — 强**（3/3 一致）：覆盖全面、引用真实、差异化定位清晰。这是 proposal 的最强维度，三位无异议。
4. **Significance — 中偏弱**（3/3 一致，R1 给"中"，R2 给"弱-中"，R3 给"中偏弱"）：贡献偏向机制理解而非方法创新，positive 结果的 surprise value 有限（"interesting but not surprising"），practical impact 受限。
5. **Trivial Alternative 威胁 — 真实**（3/3 一致）：直接安全训练（XGuard-Train 48.3%、MTSA ASR→23.5%、X-Boundary ASR→16-25%）已高效有效，CPL 作为 untargeted discourse 干预难以在效果上超越 targeted 安全训练，动机被质疑为 "a solution in search of a problem"。
6. **核心假设链条长且未验证**（3/3 一致）：对角注意力与安全注意力竞争的因果链需三个假设同时成立（竞争存在 → CPL 释放流向安全 → 惯性是退化主因），任一断裂则核心叙事崩塌。Phase 0.5 Level 3 风险被三位同时标注。
7. **Dual-conditional 结果风险**（3/3 一致）：CPL 需既有安全效果，又需通过注意力竞争机制介导——两个条件的联合先验概率较低。
8. **形式完善度高但 idea 内核单薄**（2/3 明确，R1 + R2 直接点出）：五阶段设计、triple triangulation 等展示实验设计功底，但剥离形式后核心问题是两个相对直接的验证性问题。

【异常维度】:
1. **Attention-Aware GNN 防御（arXiv:2507.07146）作为遗漏竞争工作**：仅 R1 提及，R2/R3 未标注。路线完全不同（GNN 构建实体图 vs. 注意力竞争），不构成对 Related Work 评分的实质影响。→ 降权处理，不影响最终判断。
2. **Johnson & Huo 理论适用性质疑**：R2 和 R3 提出该理论在 8B 参数多轮场景的适用性未验证（R2 称"隐喻性引用"），R1 未单独标注。→ 2/3 提及，属共识边缘，纳入风险考量但不作独立扣分项。

【最终概率（CoRL 2026）】: [0% - 3%] 中位 1%

【最终概率（匹配会场 ICLR 2027）】: [18% - 27%] 中位 23%

【一致性】: 高（CoRL std=0.6%；匹配会场 std=1.5%；rubric 维度判决几乎完全收敛）

【综合理由】:

**关于 CoRL 2026**：三位审稿人独立、一致地将 venue mismatch 标注为致命缺陷，且均引用了 CoRL CFP 的原文（"Submissions without a robotics focus will be returned without review"）。该 proposal 涉及零机器人内容（无物理机器人、无 sim-to-real、无具身智能）。这是一个独立于 idea 质量的投稿策略层面的致命错误。取三位中位 1%，区间收窄至 [0%-3%]。

**关于匹配会场（ICLR 2027 等）**：三位在 rubric 三维度的判决高度一致——Novelty 中、Significance 中偏弱、Related Work 强。核心限制因素是 idea 天花板：(1) CPL 是借用方法而非新方法，novelty 在"连接"而非"创造"；(2) positive 结果的 surprise value 有限（softmax 零和 → 减少惯性应有一些安全效果，这并不令人意外）；(3) trivial alternative（直接安全训练）威胁真实且三位均标注。Related Work 的强度提供了下限保护（~18%），但 Novelty 和 Significance 的中等评级封死了上限（~27%）。取中位 23%，偏向 R1 的更严格估计（22%），因分歧时宁缺毋滥原则。

**分歧处理**：Significance 维度 R1 给"中"而 R2 给"弱-中"，存在微弱分歧。按偏严原则，采纳 R2 的"弱-中"判断，这支持将上界从 R2 的 30% 压缩至 27%。

【建议】: KILL（对 CoRL 2026）/ 不推荐但可抢救（对匹配会场，需强化 idea 内核）

【实施评估】:
- **计算资源**: 720-900 A100-hours（约 $1080-1350 spot pricing），涵盖 CPL 复现（~80h）、XGuard-SFT 训练（~60h）、控制实验（~80h）、Phase 0.5 头分析（~25h）、MT-AgentRisk 全条件评估（~240h）、注意力分析（~85h）等。需稳定多卡 A100 集群访问。资源需求在学术研究范围内合理。
- **数据需求**: MT-AgentRisk（365 tasks，公开）、OpenAgentSafety（356 tasks，ICLR 2026 公开）、XGuard-Train（HuggingFace 公开）、AgentGym 环境（CPL preference pair 构造所需）。数据均公开可得，无标注瓶颈。
- **人工介入**: 低。主要人工节点为 Phase 0 的 go/no-go 判断、Phase 0.5 的 level determination 解读、以及 null-result 情况下的叙事重构。无需人工标注。
- **训练需求**: 需训练 CPL（LoRA rank-16 DPO，每模型 ~40 A100-hours）、XGuard-SFT（两个 rank 配置）、两个控制 LoRA。均为 8B 参数模型的 LoRA 微调，规模可控。主要风险在 CPL 复现（代码未公开，需依赖论文描述的 dual-rollout pipeline）。
- **新 Benchmark**: 不需要构建新 benchmark。使用已有公开 benchmark（MT-AgentRisk、OpenAgentSafety）。Extended-turn variants（50 tasks prepend 4-6 benign turns）为小规模扩展，非新 benchmark。
- **预估周期**: 15-17 周（手动），9-11 周（自动化流水线）。对 ICLR 2027（预计 2026 年 9-10 月截稿）时间线充裕。关键路径为 Phase 0 go/no-go（第 3 周）和 Phase 0.5 level determination（第 4 周），这两个串行依赖决定后续所有阶段的方向。

---

**致终审决策**：

鉴于 CoRL 2026 投稿为 KILL 级别判定（venue 致命不匹配，三位审稿人一致），建议流程的后续行动取决于用户是否愿意将目标会场切换至 NLP/AI Safety 类会议（ICLR 2027 / NeurIPS 2026 / ACL 2027 / EMNLP 2026）。

若切换会场，当前 proposal 在匹配会场的中位概率为 23%（低于 36% 通过线），仍需进入迭代优化。核心优化方向应聚焦于：
1. **强化 idea 内核的不可替代性**：回应"为什么不直接做安全训练"的 trivial alternative 挑战——需论证 mechanistic insight 的独立价值超越纯效果比较
2. **降低假设链条风险**：Phase 0.5 应尽早执行以 de-risk；如果 Level 3，需提前准备 pivot narrative
3. **提升 surprise value**：当前"减少惯性 → 改善安全"的因果方向过于可预测，需要找到一个"反直觉"或"非显然"的角度

若坚持 CoRL 2026，建议止损——无论如何优化 idea 本身，venue mismatch 都无法克服。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09af151-9217-4a5e-b42e-3eb9b9742887",
  "isSidechain": false,
  "requestId": "req_011CbCbDFLXwFuvQhsgLPhax",
  "type": "assistant",
  "uuid": "6f3bd8e8-8c0e-407e-ac02-eb842a7462f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cYxDW6oRFqZBb2n9ZnahZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 31770,
      "cache_read_input_tokens": 11374,
      "output_tokens": 4485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4485,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 31770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31770
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information. Let me compile my evaluatio…",
  "leafUuid": "6f3bd8e8-8c0e-407e-ac02-eb842a7462f4",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge: Multi-turn LLM safety and attention competition hypothesis",
  "sessionId": "bf23ecc5-764f-4ec9-88b0-f175a21f334c"
}
```

---
