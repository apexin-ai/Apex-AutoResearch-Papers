# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/5e323eb2-fbca-4698-8ef4-dbe6db083e75.jsonl`
- **Structured JSON:** [`000634230921cc5983d5.json`](../../sessions/00/000634230921cc5983d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:45:57.086Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:45:57.086Z",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：会议投稿方向完全不匹配】\n\n本 proposal 的目标投稿会议是 CoRL 2026（Conference on Robot Learning），但 proposal 内容是一项纯 HCI/行为科学人因实验——关于人类在 AI 辅助信息评估中的认知退化、脚手架式摩擦干预和信任校准。这与 CoRL 的 scope 完全不相关。\n\nCoRL 2026 明确的征稿范围包括：robot perception and control、robot foundation models、imitation learning、reinforcement learning for physical robots、robot manipulation/navigation/locomotion/driving/flight、robot systems and hardware、theoretical foundations of robot learning。投稿须\"focus on a core robotics problem and demonstrate relevance to robotics\"。\n\n本 proposal 没有任何机器人学习成分——没有机器人、没有感知/控制、没有强化学习、没有 sim-to-real。这是一项在 Prolific 平台上的 N≈480 人因被试实验，研究人类认知技能退化。合理的目标会议应为 CHI 2027、CSCW 2027、FAccT 2027 或 AAAI HCOMP。\n\n如果坚持投 CoRL，接受概率为 0%——不是 idea 质量问题，而是会在 desk review 阶段被直接拒绝（out of scope）。\n\n以下评估假设 proposal 投向合理的 HCI 会议（如 CHI 2027），仅评 idea 内核质量。\n\n---\n\n【领域调研】:\n\n- [Rani et al., arXiv 2510.01537] (CHI 2026): 最直接前序工作。N=67，within-subjects，GPT-4o 辅助错误信息检测，4 周后准确率下降 15.3%。无干预、无对照组、36% 流失率。明确呼吁后续做 scaffolding 干预研究。论文真实存在，已正式发表于 CHI '26（ACM DL 可查）。Proposal 描述准确。\n\n- [Althea, arXiv 2602.11161] (2026, N=963): 最接近的 scaffolding 对比工作。比较三种交互模式对 fact-checking 的影响，自主搜索模式在 10 天随访中表现最持久。但无 AI 撤除设计、无 unrestricted-AI 条件、作者自认测量的是\"short-term retention\"。论文真实存在，描述准确。\n\n- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026, N=1222): 大规模 RCT，仅 10 分钟 AI 使用即导致数学和阅读理解的独立表现下降。因果证据强。无干预测试。论文真实存在，描述准确。\n\n- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, MIT, 2026): 纯理论动态模型，证明理性 AI 采用可导致稳态技能损失。识别 training rate (κ) 和 workflow design (β) 作为缓解杠杆。无实证验证。论文真实存在，描述准确。\n\n- [Adjust for Trust, arXiv 2502.13321] (IUI 2026): 信任自适应干预，含 10 秒强制暂停，最高降低 38% 不当依赖。仅 within-session 测量。论文真实存在，描述准确。\n\n- [Farach et al., arXiv 2604.08678] (2026, N=388): Fortune 500 公司现场实验，行为脚手架反而降低质量，认知脚手架仅对顶尖表现者有效。单次会话测量。论文真实存在。\n\n- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程领域 AI 导致 17% 技能下降。无干预。论文真实存在。\n\n- [Metacognitive scripts, arXiv 2602.20206] (2026): 编程领域的 scaffolded friction + AI-blackout 测试。77% vs 39% 任务失败率。无纵向随访。论文真实存在。\n\n- [Budzyń et al.] (Lancet Gastroenterol Hepatol 2025): 临床领域，AI 撤除后腺瘤检出率下降 6 个百分点。真实存在。\n\n- 调研总结: AI 导致的认知退化（deskilling）在 2025-2026 年已成为 HCI/AI 领域的热点话题，跨医疗、教育、编程多个领域均有实证。但\"如何通过 scaffolded friction 预防 AI 撤除后的纵向技能退化\"这一具体问题确实尚无直接回答。Proposal 定位于 Rani et al. 明确呼吁的 follow-up 研究，属于\"well-motivated incremental next step\"而非\"paradigm-shifting insight\"。\n\n---\n\n【Trivial Alternative 检验】:\n\n存在多个更简单的替代方案威胁：\n\n1. **最简单的 trivial baseline——\"先独立思考再看 AI\"**：这本质上就是 proposal 的 scaffolded friction 条件的核心操作（mandatory independent attempt）。Berger et al. (2603.29866) 已经在 10 个数据集上证明\"先独立判断再看 AI 建议\"能提高准确率。CFF 文献（Buçinca et al. 2021）也证明了类似的 within-session 效果。Proposal 的增量价值在于：将这个已知有效的 within-session 策略延伸到 cross-session longitudinal skill retention 测量。这是一个真实的增量，但核心干预本身并不新——新的是测量维度。\n\n2. **\"少用 AI\"**：如果限制 AI 使用时间或频率，是否也能减缓退化？Proposal 没有包含这个条件。这不是致命缺陷，但审稿人可能会追问。\n\n**增量价值判断**：增量确实存在（longitudinal AI-withdrawal + scaffolding 的组合是新的），但主要是方法论/实验设计层面的新颖性，而非概念层面的新颖性。核心 insight——\"让人在用 AI 时保持认知参与可以减少退化\"——是直觉上显而易见的。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **关键假设：within-session cognitive engagement → cross-session skill retention**。CFF/scaffolding 被证明能减少 within-session 过度依赖，但\"减少依赖\"≠\"保留技能\"。完全有可能：scaffolding 在使用时降低了依赖率，但撤除 AI 后技能仍然退化（因为参与者虽然在 session 内被迫思考，但没有真正内化推理策略）。这个跳跃是 proposal 最大的假设风险。\n\n2. **Rani et al. 效应的可复现性**：N=67, 36% attrition, within-subjects, no control group。15.3% 的效应量可能不稳健。如果这个前提不成立（即 unrestricted-AI 条件未能复现显著退化），整个实验的核心对比将失去意义。\n\n3. **30 分钟 treatment 足以产生可测量的退化**：Rani et al. 用了 4 周纵向设计，而大型 RCT (2604.04721) 仅用 10 分钟就产生了效果。但信息评估任务的难度和认知深度可能不同，30 分钟的 treatment 是否足够是经验性假设。\n\n4. **Trust 作为 deskilling 调节变量的假设**：Adjust for Trust 证明 trust 预测 within-session reliance，但\"trust → reliance\"和\"trust → cross-session skill decay rate\"是不同的因果路径。后者缺乏理论或实证支撑。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是将已有技术（CFF/scaffolding）应用到一个新的测量范式（AI-withdrawal + longitudinal skill decay curve）。各个组件都已存在：CFF 干预（Buçinca et al. 2021）、AI 撤除导致退化（Rani et al. CHI 2026; 2604.04721）、scaffolding 模式对比（Althea 2602.11161）、trust 预测 reliance（Adjust for Trust 2502.13321）。Proposal 的新颖性在于将这些组件组合为一个统一实验——\"first controlled test of scaffolded friction + AI-withdrawal + longitudinal decay curve\"。这是一种实验设计层面的新颖性（\"no one has combined A+B+C+D in one study\"），而非概念层面的新颖性（\"here is a new insight about how X works\"）。审稿人可能会说：\"The experimental design is well-motivated, but the core hypothesis—that scaffolding preserves skills—is not surprising.\" 给弱-中是因为组合确实产生了新的科学问题（longitudinal decay prevention），但该问题的答案在 positive 情况下不具有 surprise value。\n\n2. **Significance: 中** — \n   研究问题本身——\"如何防止 AI 撤除后的认知退化\"——是重要且及时的。AI deskilling 已成为 2025-2026 的热门话题（CACM 社论、Lancet 临床证据、多篇 arXiv 高引论文）。但 proposal 的贡献形态是\"intervention study in a specific domain (information evaluation)\"，其可推广性有限：(a) 任务域是信息评估/错误信息检测，这是一个相对小众的应用场景；(b) 30 分钟 treatment + Prolific 被试的生态效度有限；(c) 即使结果 positive（scaffolding 有效），对领域的 insight 推进不大——\"保持认知参与有助于技能保留\"接近 common sense。如果结果 negative（scaffolding 也无法阻止退化），反而更有 significance。Trust moderation 维度是一个不错的补充，但本身不够构成独立贡献。\n\n3. **Related Work: 强** — \n   Proposal 的 related work 覆盖极为全面——Rani et al., Althea, CFF 文献, Augmentation Trap, Adjust for Trust, 大型 RCT, 临床证据, metacognitive scripts, Farach et al. 全部涵盖。引文描述经核实均准确。差异化定位清晰明确：逐一与每篇关键工作做 key distinction 对比。这是 proposal 最强的维度。唯一轻微不足是缺少对\"AI-free periods\"实践（如新加坡医疗系统已在做的）的引用，但不影响整体质量。\n\n---\n\n【概率估计】: [25% - 35%] 中位 30%\n（注：此概率假设投向 CHI 2027 等合理 HCI 会议。如投 CoRL 2026，概率为 0%。）\n\n【估计理由】: \nIdea 属于\"well-motivated incremental follow-up\"类型——直接回应 Rani et al. (CHI 2026) 明确呼吁的 future work，实验设计扎实、related work 覆盖优秀、差异化定位清晰。但核心 novelty 限制了上限：（1）各组件均非原创，novelty 来自组合而非 insight；（2）core hypothesis positive 时不具 surprise value（审稿人大概率说\"I would have guessed that scaffolding helps\"）；（3）概念增量主要在测量维度（longitudinal → cross-session）而非方法或理论。Related Work 的强势和实验设计的规范性（N≈480, pre-registered, between-subjects, multi-timepoint）确保了下限（不会因设计缺陷被拒），但 Novelty 的弱-中限制了上限（很难让审稿人 excited）。\n\n如果 Novelty 更强（比如发现了反直觉的 deskilling 机制，而不仅是测试已有干预），中位概率可以到 40%+。\n\n【主要风险】:\n1. **\"Predictable outcome\" 质疑**：如果 scaffolding 有效，审稿人会认为这是 expected；如果无效，可能认为是 treatment 不够强。无论哪个方向，insight 增量都有限。这是最可能导致被拒的 idea 层面风险。\n2. **\"Combination ≠ Contribution\" 质疑**：审稿人可能认为将已有组件（CFF + AI-withdrawal + longitudinal + trust moderation）拼在一起做一个大实验，虽然 well-executed，但缺乏 conceptual novelty——\"a well-designed study is not the same as a novel contribution\"。\n```\n\n---\n\n**补充说明（投稿方向）**：这是一篇做得很扎实的 HCI 行为科学 proposal，但 **绝对不应投 CoRL 2026**。CoRL 是机器人学习会议，本 proposal 不含任何机器人学习内容，会被 desk reject。建议改投：\n- **CHI 2027**（最匹配，Rani et al. 原文也在 CHI 发表）\n- **CSCW 2027**（CFF 文献的主要发表地）\n- **FAccT 2027**（AI 公平性/社会影响）\n- **AAAI HCOMP 2026**（人-AI 协作）\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Rani et al. - Dialogues with AI (CHI 2026)](https://arxiv.org/abs/2510.01537)\n- [Althea (arXiv 2602.11161)](https://arxiv.org/abs/2602.11161)\n- [AI Assistance Reduces Persistence (arXiv 2604.04721)](https://arxiv.org/abs/2604.04721)\n- [The Augmentation Trap (arXiv 2604.03501)](https://arxiv.org/abs/2604.03501)\n- [Adjust for Trust (arXiv 2502.13321)](https://arxiv.org/abs/2502.13321)\n- [AI deskilling is a structural problem (AI & Society 2025)](https://link.springer.com/article/10.1007/s00146-025-02686-z)\n- [The AI Deskilling Paradox (CACM)](https://cacm.acm.org/news/the-ai-deskilling-paradox/)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：会议投稿匹配度】\n\n本 proposal 拟投 CoRL 2026（Conference on Robot Learning），但 CoRL 的 Call for Papers 明确要求：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\"\n\"Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 的内容是：AI 辅助信息评估中的认知去技能化（deskilling）、scaffold 摩擦干预、信任校准——这是一个纯粹的 HCI/认知科学/人因学研究，涉及在线 Prolific 实验、误信息检测任务、信任量表等。与机器人学（manipulation, locomotion, sim-to-real, robot learning）完全无交集。\n\n**结论：此 proposal 在 CoRL 将被 desk reject，无需进入审稿流程。** 合适的投稿会议应为 CHI、CSCW、FAccT、AAAI HCOMP 等 HCI/human-AI interaction 会议。\n\n以下评估将同时给出：(a) CoRL 投稿的实际概率，(b) 假设投到合适 HCI 会议（如 CHI/CSCW）时的 idea 质量评估，供后续决策参考。\n\n---\n\n【领域调研】:\n\n- [Rani et al., arXiv 2510.01537] (CHI 2026): 最直接的前序工作。N=67 的 within-subjects 研究，发现 AI 辅助误信息检测在 4 周后导致 15.3% 准确率下降。无干预、无对照组、样本小。本 proposal 正是对其 future work call 的直接回应。论文真实存在，描述准确。\n\n- [arXiv 2604.04721, Liu et al.] (under review, 2026): 1,222 人 RCT，证明仅 10 分钟 AI 使用即可降低算术和阅读理解的独立表现。提供了因果证据但未测试干预。论文真实存在，描述准确。\n\n- [Althea, arXiv 2602.11161, Churina et al.] (2026, N=963): 比较三种 scaffolding 模式在 fact-checking 中的效果，发现自主搜索模式产生最持久的改善。但无 AI-withdrawal 设计、无 unrestricted AI 对照组。论文真实存在，描述准确。\n\n- [Augmentation Trap, arXiv 2604.03501, Caosun & Aral] (2026): MIT Sloan 的理论模型，证明理性 AI 采纳也可能导致稳态技能损失。提出 training rate (κ) 和 workflow design (β) 两个缓解杠杆，但纯理论、无实证。论文真实存在，描述准确。\n\n- [Adjust for Trust, arXiv 2502.13321, Srinivasan & Thomason] (IUI 2026): 测试信任自适应干预（解释、强制暂停），达到 38% 不当依赖减少。仅限 within-session，未测量跨会话技能保持。论文真实存在，描述准确。\n\n- [Metacognitive Scripts, arXiv 2602.20206] (2026, N=78): 在编程领域测试 scaffold 摩擦（Explanation Gate），unrestricted AI 用户 77% 在 AI-blackout 任务中失败 vs. scaffolded 组 39%。不同领域，无纵向随访。论文真实存在，描述准确。\n\n- [Farach et al., arXiv 2604.08678] (2026, N=388): 行为 vs. 认知 scaffold 的 Fortune 500 现场实验。行为 scaffold 反而降低质量，认知 scaffold 仅对顶尖表现者有效。单次会话测量。论文真实存在。\n\n- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 提出通过 multi-agent 认知强制函数实施 scaffold 摩擦的理论框架，零实证。\n\n- **调研总结**: AI 去技能化（deskilling after AI withdrawal）是 2025-2026 年的热门议题，已有多个方向的因果证据（Rani et al., 1222人RCT, 编程领域 Shen & Tamkin）。Scaffolding/friction 干预在 within-session overreliance 上已被广泛研究（CFF, Adjust for Trust），但\"scaffold 能否预防 AI 撤回后的纵向技能退化\"确实是一个尚未被填补的空白。本 proposal 精准定位在这个空白上，属于\"自然下一步\"而非\"意外发现\"。\n\n---\n\n【Trivial Alternative 检验】:\n\n**存在 trivial alternative 威胁，但有部分增量价值。**\n\n最简单的替代方案是：在 AI 辅助期间，简单地要求用户\"先自己做一遍再看 AI 答案\"（即 mandatory independent attempt alone）。这不需要复杂的 incremental hints 系统或 self-explanation gates，但可能就已经能预防大部分 deskilling。Berger et al. (2603.29866) 已经证明\"独立判断优先\"能在 10 个数据集上提升人-AI 准确率。\n\n增量价值在于：\n1. 本研究不仅测试\"是否有效\"，还比较了两种不同 scaffold 哲学（friction vs. agency-preserving exploration）\n2. Trust 作为 moderator 的维度是额外贡献\n3. 纵向 decay curve（即时/1周/4周）提供了过程信息\n\n但核心干预手段（\"先自己试，再看提示\"）并不新颖。如果结果显示简单的 mandatory independent attempt 就足够了，那 incremental hints + self-explanation gates 的额外工程就是过度设计。\n\n---\n\n【前提假设检验】:\n\n核心 claim 的逻辑链条中有以下未经验证的假设：\n\n1. **30 分钟 AI 治疗足以诱发可测量的 deskilling**：1222人 RCT 用 10 分钟诱发了 deskilling，但那是在算术/阅读理解（低复杂度任务）中。信息评估（claim verification, multi-source synthesis）是否在 30 分钟内产生足够的认知依赖以导致可测量退化，这是假设，不是事实。Rani et al. 的 deskilling 是在 4 周多次 AI 交互后才出现的。\n\n2. **Prolific 在线实验者的行为可推广到真实场景**：proposal 将 Prolific 上的 30 分钟任务产生的 deskilling 类比于现实中长期 AI 使用者的技能退化——生态效度存疑。\n\n3. **Qwen 3.5 27B 能提供与 GPT-4o 可比的\"逼真\" AI 辅助**：Rani et al. 使用 GPT-4o + Google Search。Qwen 3.5 27B（较弱模型）是否能诱发相同程度的信任和认知卸载，直接影响实验效果。\n\n4. **Trust 作为 deskilling speed 的 moderator**：这是一个合理但未经验证的假设。Adjust for Trust 证明 trust 预测 within-session reliance，但 within-session reliance → cross-session deskilling 的映射不是必然成立的。\n\n---\n\n【3 维度打分】:\n\n1. **Novelty: 中** — 本 proposal 的核心贡献是将已有组件（scaffolded friction + AI withdrawal design + longitudinal decay curve + trust moderation）组合应用于信息评估领域。每个组件单独来看都不新颖：scaffolded friction 在 CFF 文献和 2602.20206 中已有测试；AI withdrawal 设计在 2604.04721 和 Rani et al. 中已有使用；trust 作为 reliance moderator 在 Adjust for Trust (2502.13321) 中已有验证。真正的 novelty 是组合——\"scaffold + withdrawal + longitudinal + trust moderation\" 在信息评估中的首次完整测试。这是 solid incremental contribution，但审稿人很可能会说\"这是 Rani et al. future work 的直接执行，是一个很好的 follow-up study，但 conceptual novelty 有限\"。核心发现如果是 positive（scaffold 确实减缓 deskilling），多数审稿人会说\"I would have guessed this\"。\n\n2. **Significance: 中** — 研究问题本身重要：AI deskilling 是 2025-2026 年的热点问题，有明确的政策和教育含义。但本 proposal 的实际 impact 受限于：(a) 30 分钟 online 实验的生态效度——真实世界的 deskilling 发生在长期、高频使用场景中；(b) 信息评估任务的可推广性——claim verification 不等于真实的新闻消费或日常决策；(c) 如果 scaffold 确实有效（高先验概率），finding 的信息量不高；如果无效，那更有意思但也更难发表。对领域的推动主要在于提供\"是否有效\"的量化证据，而非概念性突破。\n\n3. **Related Work: 强** — 这是本 proposal 的最大亮点。文献覆盖极其全面：从 Rani et al. 到 Althea，从 Augmentation Trap 到 Adjust for Trust，从 CFF 到 metacognitive scripts，几乎涵盖了所有 2025-2026 年的相关工作。每篇论文的描述都经我调研验证准确。差异化定位也非常清晰——每个\"Key distinction\"段落都精确指出了与前序工作的差异（within-session vs. cross-session, improvement persistence vs. deskilling prevention, etc.）。\n\n---\n\n【概率估计】:\n\n- **CoRL 2026**: 0-2%，中位 1%（desk reject，完全的会议-主题不匹配）\n- **如果投到合适的 HCI 会议（CHI/CSCW）**: 25-35%，中位 28%\n\n【估计理由】:\n\n**CoRL**: Proposal 是纯 HCI/认知科学研究，涉及在线人类实验、误信息检测、trust 量表。CoRL 要求\"core robotics problem\"，无机器人内容将被直接退回。这不是 idea 质量问题，而是根本性的会议匹配错误。\n\n**合适 HCI 会议 (28%)**: \n- Related Work 维度强，说明作者对领域有深入理解，positioning 清晰。\n- 但 Novelty 为\"中\"限制了上界——核心 claim 方向可预测（scaffold 应该能减缓 deskilling），组合式贡献（combinatorial contribution）在顶会中通常被视为 incremental。\n- Significance 为\"中\"进一步限制——30 分钟 Prolific 实验的生态效度可能招致审稿人质疑实际影响力。\n- 如果实验执行出色且结果有 nuance（比如 scaffold 在某些维度有效但在另一些维度无效，或 trust moderation 效应出人意料），概率可上升到 35%。\n- 如果结果全面 positive 且符合预期，审稿人可能认为 contribution 不够 surprising，概率下探至 22-25%。\n\n【主要风险】:\n\n1. **\"Natural next step\" 陷阱**：本 proposal 本质是 Rani et al. (CHI 2026) 明确呼吁的 future work 的直接执行。审稿人可能认为这是一个 well-executed follow-up study，但缺乏独立的 conceptual contribution。如果核心发现是 positive（scaffold 减缓 deskilling），方向完全可预测，surprise value 低。\n\n2. **致命的会议选择错误**：投 CoRL = 确定性 desk reject。这是可以立刻纠正但必须纠正的问题。\n```\n\n---\n\n**总结**：这个 proposal 的 idea 质量是 **中等偏上**——文献把握扎实、gap 定位精准、设计逻辑自洽，是一个典型的 \"well-motivated incremental contribution\"。但有两个关键问题：\n\n1. **（致命）会议选择完全错误。** CoRL 是 Conference on Robot Learning，本 proposal 无任何机器人内容，将被 desk reject（0-2%）。应改投 CHI、CSCW、FAccT 等 HCI 会议。\n\n2. **（idea 层面）核心发现方向可预测。** 即使投到正确会议，\"scaffolded friction 能减缓 AI 撤回后的 deskilling\"这一预期结果对多数审稿人来说并不 surprising，Novelty 上限受限于组合式贡献的本质。\n\n建议：如果确认是 CoRL，应立即止损；如果投稿目标可以调整为 CHI/CSCW，该 idea 值得进入后续完善流程。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)\n- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)\n- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)\n- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)\n- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance](https://arxiv.org/abs/2502.13321)\n- [Metacognitive Scripts for Novice Programming](https://arxiv.org/abs/2602.20206)\n- [Cognitive Agency Surrender](https://arxiv.org/pdf/2603.21735)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have enough information to provide a thorough assessment. Let me compile my evaluation.\n\n---\n\n```\n【阶段】: Triage\n```\n\n## ⚠️ 致命前置问题：投稿目标会议严重不匹配\n\n**CoRL (Conference on Robot Learning) 2026 的主题范围是机器人学习**——包括 robot perception, manipulation, navigation, locomotion, reinforcement learning for physical robots, robot foundation models 等。其 Call for Papers 明确指出 **\"submissions without a robotics focus will be returned without review\"**。\n\n本 proposal 是一个纯 HCI/认知科学研究：在线被试实验、scaffolded friction、cognitive deskilling prevention、trust calibration——**与机器人学习没有任何关联**。提交至 CoRL 将被 desk reject，不会进入审稿流程。\n\n**合适的目标会议**：CHI 2027、CSCW 2026/2027、FAccT 2027、IUI 2027、或 AAAI/IJCAI 的 Human-AI Interaction track。\n\n> 以下评估基于 idea 本身的质量（假设投到合适的 HCI 会议），但概率估计会将 CoRL 的 venue mismatch 作为致命因素纳入。\n\n---\n\n```\n【领域调研】:\n```\n\n- **[Rani et al., arXiv 2510.01537] (CHI 2026)**: 本 proposal 最核心的先驱工作。N=67 within-subjects 设计，发现 AI 辅助 misinformation detection 后 4 周 unassisted accuracy 下降 15.3%。无干预、无对照组。该论文 future work 明确呼吁 scaffolding interventions。Proposal 直接回应此呼吁——定位准确。\n\n- **[arXiv 2604.04721, Liu et al.] (under review 2026)**: 1,222 人 RCT，因果证据表明仅 10 分钟 AI 使用即可降低 arithmetic/reading comprehension 独立表现。提供了 deskilling 的大规模因果证据，但未测试任何干预。Proposal 准确引用。\n\n- **[Althea, arXiv 2602.11161, Churina et al.] (2026)**: N=963，比较三种 scaffolding 模式对 fact-checking 的改善持久性。Self-directed search 产生最持久的改进。但无 AI-withdrawal 设计，无 unrestricted-AI 条件，作者承认仅测量\"short-term retention\"。Proposal 引用准确，定位差异化清晰。\n\n- **[The Augmentation Trap, arXiv 2604.03501, Caosun & Aral] (2026)**: MIT Sloan 的形式化动态模型，证明理性 AI 采用仍可导致 steady-state skill loss。纯理论，无实证。Proposal 声称 operationalize 其 mitigation levers (training rate κ, workflow design β)——这一连接是合理的但需验证。\n\n- **[Adjust for Trust, arXiv 2502.13321, Srinivasan & Thomason] (IUI 2026)**: Trust-adaptive interventions 减少 38% inappropriate reliance，但仅测量 within-session reliance decisions，非 cross-session skill retention。Proposal 引用准确。\n\n- **[arXiv 2602.20206] Metacognitive Scripts in Programming (2026)**: Scaffolded friction 在编程领域，AI-blackout test 中 77% vs 39% failure，但无纵向 follow-up，不同领域。\n\n- **[Farach et al., arXiv 2604.08678] (2026)**: 388 人 field experiment，behavioral vs. cognitive scaffolding；single-session measurement，无纵向跟踪。\n\n- **调研总结**: AI-induced deskilling 在 2025-2026 已成为一个活跃且有实证支撑的研究领域，跨多个 domain（医学、编程、信息评估、算术）。**核心空白确实存在**：目前没有研究同时具备 (a) scaffolding 干预 + (b) AI-withdrawal longitudinal design + (c) information evaluation domain。但该空白的性质更接近\"experimental design gap\"（实验设计层的空缺），而非\"conceptual gap\"（概念层的突破）。\n\n---\n\n```\n【Trivial Alternative 检验】:\n```\n\n**存在明显的 trivial alternative 威胁。**\n\n1. **Mandatory independent attempt alone**: Proposal 的 scaffolded friction 条件包含三个组件（mandatory independent attempt, incremental hints, self-explanation gates）。但 Berger et al. (arXiv 2603.29866) 已证明仅\"independent judgment first\"就能跨 10 个数据集提升 accuracy。**最简单的 baseline——仅强制独立尝试（无 hints、无 self-explanation）——可能已经捕获了大部分 deskilling prevention 效果。** 如果 scaffolded friction 的效果主要来自 mandatory independent attempt 这一组件，那么 incremental hints 和 self-explanation gates 的增量价值就很有限。\n\n2. **Reduced AI quality**: 直接降低 AI 输出的完整度/质量（如只给 partial hints 而非完整答案）是否就足以防止 deskilling？这不需要复杂的 scaffolding 机制。\n\n3. **Proposal 的增量价值**: Proposal 的真正增量在于 *longitudinal AI-withdrawal design* + *多条件对比的 skill decay curve*。但这更多是实验设计的贡献，而非方法论或理论创新。\n\n---\n\n```\n【前提假设检验】:\n```\n\n**核心 claim 的逻辑链条中有两个关键的未验证假设：**\n\n1. **\"30 分钟 AI 辅助足以产生可测量的 deskilling\"**: 这是整个实验的基础假设。Rani et al. 用了 4 周 weekly sessions，deskilling RCT 用了 10 分钟但在算术/阅读理解（远比 information evaluation 更练习敏感的简单任务）。本 proposal 仅用 30 分钟单次 session 在 information evaluation 这一复杂认知任务上，能否诱导出足够大的 deskilling 效应以被检测到？**这一假设缺乏直接支撑。** 如果 unrestricted-AI 条件在 30 分钟后未产生显著 deskilling，整个研究的 scaffolding 对比就失去了意义。\n\n2. **\"Trust calibration 是 deskilling severity 的有意义 moderator\"**: Adjust for Trust 证明了 trust predicts within-session reliance behavior，但 trust → cross-session skill decay 的跳跃是一个额外的、未经验证的推断。Between-subjects 设计中 N≈120/condition 对 trust × condition × time 三重交互的统计功效可能不足。\n\n3. **\"Scaffolded friction 的效果可以跨 4 周保持\"**: 即使 scaffolding 在 immediate post-test 有效，1-week 和 4-week follow-up 时 scaffolding 条件是否仍优于 unrestricted-AI 条件是未知的。人类遗忘曲线可能抹平初始差异。\n\n---\n\n```\n【3 维度打分】:\n```\n\n### 1. Novelty: **中** (偏弱)\n\n**理由**: Proposal 正确识别了一个 empirical gap——没有研究同时结合 scaffolding intervention + AI-withdrawal longitudinal design + information evaluation。但这个 gap 的性质是 **experimental design gap**，而非 **conceptual novelty**。核心假设\"强制认知参与可以防止认知退化\"本质上是教育心理学中 desirable difficulties (Bjork, 1994) 和 generation effect 的直接应用——这并不新颖。\n\n- Rani et al. (CHI 2026) 已建立 deskilling 存在；\n- Althea (2602.11161) 已证明 scaffolding 的 improvement persistence；\n- Berger et al. (2603.29866) 已证明 independent judgment first 的有效性；\n- Metacognitive scripts (2602.20206) 已在编程中测试 scaffolded friction with AI-blackout。\n\n本 proposal 做的是把这些已有元素**组合到一个更完整的实验设计中**——这是 execution novelty，不是 idea novelty。如果核心结果是 positive（scaffolding reduces deskilling），大多数审稿人会说 **\"I would have guessed this\"**。\n\n### 2. Significance: **中**\n\n**理由**: AI deskilling 确实是 2025-2026 的热门问题，有广泛的社会关切（Frontiers 2026 framework, FAccT 2026, Lancet 2025 clinical evidence）。如果结果为 positive，提供的是 **实践指导**（\"设计 AI 工具时加入 scaffolded friction\"），这有价值但不令人意外。如果结果为 negative（scaffolding 不能防止 deskilling），这反而更有 significance，因为它挑战了领域的乐观假设。\n\n但 significance 受限于：\n- 任务域较窄（online information evaluation with Prolific workers）\n- 30 分钟单次 session 的生态效度有限\n- 发现难以推广到高风险专业领域（医学、法律）\n\n### 3. Related Work: **强**\n\n**理由**: 这是 proposal 最突出的优势。文献覆盖极其全面——Rani et al., Althea, deskilling RCT, Augmentation Trap, Adjust for Trust, CFF literature, Cognitive Agency Surrender, Farach et al., metacognitive scripts, Critical Inker, Berger et al.——关键论文均已核实为真实存在且描述准确。每篇的差异化定位（\"Key distinction from X\"）清晰且合理。唯一的小问题是 proposal 过度强调\"no study combines (a)+(b)+(c)+(d)+(e)\"——这种组合式 novelty claiming 容易被审稿人视为 gap-filling exercise。\n\n---\n\n```\n【概率估计】: 0% — 3%（中位 ~1%）[投稿 CoRL 2026]\n```\n\n```\n【概率估计（如投稿 CHI/CSCW 等合适 HCI 会议）】: 25% — 35%（中位 ~30%）\n```\n\n```\n【估计理由】:\n```\n\n**CoRL 概率（~1%）**: 本 proposal 与 CoRL 的主题范围（robot learning）完全不匹配。CoRL 明确声明 \"submissions without a robotics focus will be returned without review\"。这是一个纯 HCI/认知科学的在线用户实验，不涉及任何机器人、物理系统或 embodied learning。**Desk reject 是几乎确定的结果。**\n\n**HCI 会议概率（~30%）**: 如果投到 CHI/CSCW 等合适会议，idea 质量处于 25-35% 区间：\n- **方向正确**：deskilling prevention 是 timely 且重要的问题\n- **真实的 empirical gap**：longitudinal scaffolding + AI-withdrawal 设计确实无先例\n- **Related work 极为扎实**\n- **但 idea 内核是\"组合式 gap-filling\"**：将已有的 scaffolding 方法（CFF + Althea-style）放入一个更完整的实验框架，核心发现若 positive 不具备 surprising 性\n- **Trivial alternative 威胁**限制了上界：mandatory independent attempt alone 可能解释大部分效果\n- **30 分钟 treatment 能否诱导可测量 deskilling** 是一个基础性风险\n\n```\n【主要风险】:\n```\n\n1. **Venue mismatch（致命）**: 投 CoRL = desk reject。这是最直接、最不可补救的风险。\n2. **\"I would have guessed this\" 问题**: 核心发现（scaffolded friction reduces deskilling）高度符合直觉，缺乏 surprising element。审稿人可能认为这是 confirmatory study，novelty delta 不足以支撑 top-venue acceptance。\n\n---\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)\n- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)\n- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)\n- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)\n- [Adjust for Trust](https://arxiv.org/abs/2502.13321)\n- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)\n- [Farach et al. - Scaffolding Human-AI Collaboration Field Experiment](https://arxiv.org/abs/2604.08678)\n- [Metacognitive Scripts for Programming](https://arxiv.org/abs/2602.20206)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# When the AI Goes Away: Scaffolded Friction, Trust Calibration, and the Skill Decay Curve After AI-Assisted Information Evaluation\n\n## Description\nRani et al. (CHI 2026) demonstrate that AI-assisted misinformation detection leads to 15.3% skill degradation over 4 weeks after AI withdrawal—but their study tested no interventions, included no control group, and had only N=67. We provide the first controlled test of whether scaffolded cognitive friction can prevent this degradation—and whether trust calibration moderates deskilling severity. While the deskilling problem in information evaluation is now empirically established (Rani et al.), the scaffolding literature (Althea, CFF studies, Adjust for Trust) measures only within-session or short-term improvements, not whether interventions protect independent capability after AI is permanently removed. We address this gap with a pre-registered, between-subjects experiment (N≈480) comparing four conditions: no-AI control, unrestricted LLM access (Qwen 3.5 27B), scaffolded friction (mandatory independent attempt, incremental hints, self-explanation gates—operationalizing the Augmentation Trap's theoretical mitigation levers), and exploratory scaffolding (Althea-style modular evidence exploration). Participants complete information evaluation tasks—claim verification, multi-source synthesis, argument quality evaluation—across three phases: baseline assessment, AI-assisted treatment, and post-AI independent assessment at three timepoints (immediate, 1-week, 4-week), yielding per-condition skill decay curves. This design directly answers Rani et al.'s call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains,' extends Althea beyond their acknowledged limitation of measuring only 'short-term retention of reasoning patterns,' and operationalizes the Frontiers framework's distinction between overreliance-as-behavior (measured by CFF studies) and deskilling-as-outcome (measured by our cross-session capability decline). A trust calibration dimension—building on Adjust for Trust's finding that trust predicts within-session reliance—tests whether users who develop higher AI trust during treatment deskill faster after AI removal. The study provides the first empirical test of scaffolded friction interventions combined with an AI-withdrawal design, multi-timepoint decay curve, and trust moderation for deskilling prevention in information evaluation.\n\n## Core Problem\nCan scaffolded cognitive friction interventions prevent the rapid skill degradation that emerges after AI assistance is removed from information evaluation tasks—and does the speed of deskilling depend on how much users trusted the AI? Rani et al. (CHI 2026, N=67) have now demonstrated that AI-assisted misinformation detection leads to a 15.3% accuracy decline after 4 weeks of AI withdrawal, but their study tested no interventions, included no control group, and explicitly calls for scaffolding-based solutions. The CFF and scaffolding literatures (Buçinca et al., Althea, Adjust for Trust) test friction and trust-adaptive interventions to reduce within-session overreliance, but no study has tested whether such interventions protect independent capability after AI access is permanently revoked—nor whether trust calibration moderates the severity of post-withdrawal skill decay.\n\n## Opportunity\nA convergence of causal, clinical, and now longitudinal evidence creates a precisely bounded gap. Rani et al. (arXiv 2510.01537, CHI 2026) provide the first longitudinal evidence that AI-assisted information evaluation causes deskilling after AI removal: 15.3% accuracy decline over 4 weeks in misinformation detection (N=67, within-subjects, no control group, no interventions). Their authors explicitly call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains' as future work—this is exactly the study we propose. The landmark 1,222-participant RCT (arXiv 2604.04721) provides causal evidence that just 10 minutes of AI use degrades independent performance in arithmetic and reading comprehension. The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) formalizes this as a dynamic model where rational AI adoption can still leave workers worse off, identifying training rate (κ) and workflow design (β) as mitigation levers—but provides no empirical test. Clinical data shows 6-point adenoma detection drops after AI removal (Budzyń et al., Lancet Gastroenterol Hepatol 2025). The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction as a countermeasure but tests nothing empirically. Althea (arXiv 2602.11161, N=963) demonstrates that self-directed scaffolding produces more persistent fact-checking improvements at 10-day follow-up—but has no AI-withdrawal test, no unrestricted-AI condition, no pre-AI baseline, and its authors explicitly acknowledge measuring 'short-term retention of reasoning patterns, not durable skill acquisition.' The metacognitive scripts study (arXiv 2602.20206) tests scaffolded friction in programming (77% vs. 39% failure on AI-blackout tasks) but not information evaluation and lacks longitudinal follow-up. Shen & Tamkin (arXiv 2601.20245) provide RCT evidence of 17% deskilling in programming skill formation with AI but test no interventions and measure only within-session outcomes. Adjust for Trust (arXiv 2502.13321, IUI 2026) tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance—but measures only within-session reliance decisions, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment but measure single-session document quality, not longitudinal skill retention. No study combines: (a) scaffolded friction interventions, (b) an AI-withdrawal design with pre/during/post phases, (c) information evaluation tasks, (d) a multi-timepoint skill decay curve, and (e) trust calibration as a moderator of deskilling severity. The gap is not 'does deskilling occur after AI withdrawal in information evaluation?'—Rani et al. have answered yes. The gap is 'can scaffolded friction prevent it, and does trust predict who deskills fastest?'\n\n## Related Work / Landscape\nEvidence of AI-induced deskilling is now robust, cross-domain, and—critically—extends to information evaluation with longitudinal AI-withdrawal data.\n\n**Deskilling evidence:** Rani et al. (arXiv 2510.01537, CHI 2026) provide the most directly relevant finding: in a month-long within-subjects study (N=67), AI dialogues about misinformation produced +21% accuracy gains during assisted sessions but −15.3% unassisted accuracy at Week 4 vs. Week 0 (β=−0.077, p<.001), with decline driven entirely by fake item detection. Their study used GPT-4o with Google Search but tested no scaffolding interventions, included no independent control group, and had 36% attrition (105→67). The 1,222-participant RCT (arXiv 2604.04721) shows immediate performance degradation after AI exposure in arithmetic and reading comprehension. Shen & Tamkin (arXiv 2601.20245) demonstrate 17% lower quiz scores in AI-assisted programming learners (N=52, d=0.738) and identify six interaction patterns—three cognitively engaged patterns that preserve learning, suggesting that engagement-preserving interventions could work. Clinical trials show 6-point adenoma detection drops after AI removal (Budzyń et al., 2025). Neuroimaging reveals lower brain activation in AI-assisted learners (Kosmyna et al., 2025).\n\n**Theoretical frameworks:** The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) provides a formal dynamic model decomposing AI productivity into skill-independent (α) and skill-complementary (β) channels, proving that rational adoption can produce steady-state loss and identifying five deployment regimes—but offers no empirical validation and notes that 'draft-then-revise' workflows (analogous to our mandatory independent attempt) should preserve the skill-complementary channel. The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction via multi-agent cognitive forcing functions but provides zero empirical validation. The Frontiers 'Deskilling dilemma' framework (2026) distinguishes cognitive, diagnostic, and moral deskilling as an outcome from overreliance as a behavior—a distinction no intervention study has operationalized.\n\n**Scaffolding and friction interventions:** Althea (arXiv 2602.11161, N=963) compares three scaffolding modes for fact-checking across immediate and 10-day follow-up, finding self-directed search yields strongest persistence—but measures improvement durability during/after scaffolded interaction, not deskilling prevention after AI removal, has no unrestricted-AI condition, and explicitly calls for longer-term studies. Adjust for Trust (arXiv 2502.13321, IUI 2026, Srinivasan & Thomason) tests trust-adaptive interventions—supporting explanations at low trust, counter-explanations at high trust, and 10-second forced pauses at high trust—achieving up to 38% reduction in inappropriate reliance across science questions (N=30/condition) and medical diagnosis (N=20/condition), but measures only within-session reliance decisions across a 30-problem sequence, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment at a Fortune 500 company, finding behavioral scaffolding actually reduced quality while cognitive scaffolding helped only top performers—but measure single-session document quality with no longitudinal follow-up. Critical Inker (arXiv 2604.07167) scaffolds critical thinking in AI-assisted writing through Socratic questioning but reports only a small-scale pilot. The CFF literature (Buçinca et al., CSCW 2021; Ghosh et al., 2026) measures immediate reliance decisions, not longitudinal skill retention. Berger et al. (arXiv 2603.29866) show that eliciting independent judgment before AI input boosts accuracy across 10 datasets but do not measure whether this protects skills over time. The overreliance measurement paper (arXiv 2509.08010) identifies three gaps in current overreliance measurement, arguing that LLMs' conversational style creates unique trust dynamics.\n\n**The precise gap:** Rani et al. establish that AI-assisted information evaluation causes deskilling after AI withdrawal. Our study tests whether scaffolded friction can prevent it. This is the direct next step their paper calls for.\n\n## Approach\nWe conduct a pre-registered, between-subjects online experiment (N≈480, recruited via Prolific) with four conditions across three phases, using an AI-withdrawal design that directly tests whether scaffolded friction prevents the deskilling that Rani et al. (CHI 2026) documented in information evaluation.\n\n**Conditions (4):** (1) No-AI control (participants complete all tasks independently—addressing Rani et al.'s lack of a control group), (2) Unrestricted LLM access (standard chatbot interaction using Qwen 3.5 27B via API for open-source reproducibility—replicating the deskilling-inducing condition), (3) Scaffolded friction (mandatory independent attempt with confidence rating before AI output, incremental hint system, self-explanation gates—operationalizing the untested Cognitive Agency Surrender framework and the Augmentation Trap's 'draft-then-revise' workflow design lever), (4) Althea-style exploratory scaffolding (modular evidence exploration without verdict delivery—to directly compare friction-based deskilling prevention against the epistemic-agency scaffolding strategy that Althea found most persistent for improvement). This fourth condition enables a head-to-head comparison of two scaffolding philosophies: friction-as-deskilling-prevention vs. agency-preserving-exploration.\n\n**Phases (3):** Phase 1—Baseline skills assessment: all participants complete information evaluation tasks independently (claim verification adapted from AVeriTeC/FEVER, multi-source synthesis, argument quality evaluation) plus trust disposition measures (Jian et al. trust scale adapted for AI). Phase 2—AI-assisted treatment (30 min): participants work on parallel-form tasks with their assigned AI condition; trust in AI is measured again post-treatment. Phase 3—Post-AI independent assessment: participants complete held-out test items WITHOUT any AI access at three timepoints: immediate (same session), 1-week delayed, and 4-week delayed.\n\n**Primary outcome:** Skill retention, operationalized as the pre-to-post accuracy delta on held-out test items completed independently after AI removal. The three post-withdrawal timepoints (immediate, 1-week, 4-week) yield a skill decay curve per condition. This directly extends Rani et al.'s observation of 15.3% decline (no interventions, N=67, within-subjects) to an interventional, between-subjects design at 7× sample size with a control group.\n\n**Secondary outcomes:** (a) Persistence: time-on-task before abandonment at each post-test; (b) Trust calibration: confidence-accuracy alignment and trust scale changes; (c) Trust-as-moderator: whether pre-treatment trust disposition and within-treatment trust change predict steeper deskilling in the unrestricted-AI condition—extending Adjust for Trust's finding that trust predicts within-session reliance to test whether it also predicts cross-session skill decay; (d) Cognitive engagement: Cognitive Reflection Test and NASA-TLX; (e) Strategy transfer: verification strategy diversity at each timepoint.\n\n**Key distinction from Rani et al. (CHI 2026):** Rani et al. demonstrate that deskilling occurs in information evaluation after AI withdrawal (15.3% decline, N=67, no interventions, no control group, within-subjects). We test whether scaffolded friction can prevent this degradation (N≈480, 4 conditions including no-AI control, between-subjects, with scaffolding interventions). Their study answers 'does AI cause deskilling in information evaluation?' Our study answers 'can we prevent it?' Their limitations—no interventions, no control group, small sample, within-subjects confounds—are precisely what our design addresses.\n\n**Key distinction from Althea:** Althea compares scaffolding modes along an epistemic agency spectrum and measures improvement persistence (post-task → 10-day follow-up). We compare scaffolding modes along a friction spectrum against an unrestricted-AI deskilling baseline and measure skill degradation after AI withdrawal (pre-AI baseline → post-AI independent performance) across a 4-week decay curve. Althea asks 'which scaffolding mode best improves reasoning?' We ask 'which scaffolding mode best prevents the reasoning degradation that unrestricted AI induces?'\n\n**Key distinction from Adjust for Trust (IUI 2026):** Srinivasan & Thomason test trust-adaptive interventions (explanations, forced pauses) to reduce inappropriate reliance during a 30-problem within-session sequence. We measure whether friction during AI-assisted work protects independent capability after AI is permanently removed. They optimize within-session reliance decisions; we optimize cross-session skill retention. We also adopt their insight that trust level predicts reliance behavior—but test whether it similarly predicts the severity of post-withdrawal skill decay.\n\n**Key distinction from CFF literature:** CFF studies measure within-session reliance behavior (agreement rate with AI suggestions). We measure cross-session capability change (can you still do this independently after AI is gone?). This operationalizes the Frontiers framework's distinction between overreliance-as-behavior and deskilling-as-outcome.\n\n**Key distinction from the deskilling RCT (2604.04721):** They demonstrate the problem (AI use degrades independent performance in arithmetic/reading). We test a solution (scaffolded friction prevents that degradation) in information evaluation and add a trust moderation dimension.\n\n**Key distinction from the Augmentation Trap (2604.03501):** Caosun & Aral provide a formal model predicting that training rate and workflow design can mitigate AI-induced skill decay but offer no empirical validation. Our scaffolded friction conditions operationalize their theoretical mitigation levers—mandatory independent attempts preserve the skill-complementary (β) channel, and self-explanation gates increase the effective learning rate (κ)—providing the first empirical test of interventions aligned with their formal framework.\n\n**Model choice:** Qwen 3.5 27B, the largest dense model in the Qwen 3.5 series, served via API (OpenRouter: ~$0.14/M input, $1/M output tokens) or self-hosted on a single H100 via vLLM for consistency. This model is selected for: open-source reproducibility, sufficient capability for realistic AI assistance in information evaluation, and cost efficiency.\n\n## Inspiration\nField guide gap: cognitive deskilling identified as key risk (P3, P13, P14) but measurement and intervention are absent from NLP/HCI research. Critical catalyst: Rani et al. (CHI 2026) demonstrate the problem—15.3% skill degradation after AI withdrawal in misinformation detection—and their future work section explicitly calls for scaffolding-based solutions, which is exactly what we propose. Pattern transfer: the pre/during/post withdrawal design from the deskilling RCT (2604.04721) + the scaffolding mode comparison logic from Althea + the CFF intervention toolkit (P15-P17) reframed for longitudinal skill retention + the independent-judgment-first approach from Berger et al. (2603.29866) + the trust-adaptive intervention logic from Adjust for Trust (2502.13321) reframed for cross-session skill protection + the formal skill-decay dynamics from the Augmentation Trap (2604.03501) operationalized empirically. Novel angle: trust as a moderator of deskilling speed, connecting the deskilling prevention contribution to the trust calibration literature—building on Adjust for Trust's finding that trust level predicts reliance behavior to ask whether it also predicts skill decay severity.\n\n## Key References\n- Dialogues with AI Reduce Beliefs in Misinformation but Build No Lasting Discernment Skills (arXiv 2510.01537, Rani et al., CHI 2026, N=67) — most directly relevant concurrent work: demonstrates 15.3% accuracy decline after 4-week AI withdrawal in misinformation detection using within-subjects design with GPT-4o dialogues; tested no interventions, no control group; their future work explicitly calls for scaffolding-based solutions, which is exactly what we propose\n- Althea: Scaffolding Epistemic Agency for Durable Fact-Checking (arXiv 2602.11161, Churina et al., 2026, N=963) — closest scaffolding concurrent work; compares scaffolding modes for fact-checking improvement persistence but uses no AI-withdrawal design, no unrestricted-AI condition, and authors acknowledge design measures 'short-term retention of reasoning patterns, not durable skill acquisition'\n- AI Assistance Reduces Persistence and Hurts Independent Performance (arXiv 2604.04721, under review 2026) — establishes the deskilling problem with causal evidence from a 1,222-participant RCT\n- The Augmentation Trap: AI Productivity and the Cost of Cognitive Offloading (arXiv 2604.03501, Caosun & Aral, 2026) — formal dynamic model proving rational AI adoption can produce steady-state skill loss; identifies training rate (κ) and workflow design (β) as mitigation levers our interventions operationalize; purely theoretical, no empirical validation\n- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (arXiv 2502.13321, Srinivasan & Thomason, IUI 2026) — tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance; measures within-session reliance only, not cross-session skill retention; supports trust-as-moderator dimension\n- Cognitive Agency Surrender: Defending Epistemic Sovereignty via Scaffolded AI Friction (arXiv 2603.21735, 2026) — theoretical framework we operationalize empirically\n- Beyond AI advice—independent aggregation boosts human–AI accuracy (arXiv 2603.29866, Berger et al., 2026) — demonstrates independent-judgment-first approach boosts accuracy across 10 datasets; conceptually parallel to our mandatory independent attempt, but measures immediate accuracy not skill retention\n- Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing (arXiv 2604.08678, Farach et al., 2026, N=388) — field experiment comparing behavioral vs. cognitive scaffolding; found behavioral scaffolding reduced quality while cognitive scaffolding helped only top performers; single-session measurement, no longitudinal follow-up\n- How AI Impacts Skill Formation (arXiv 2601.20245, Shen & Tamkin, 2026, N=52) — RCT evidence of 17% deskilling in programming with AI (d=0.738); identifies cognitively-engaged interaction patterns that preserve learning; programming domain only, single-session, no interventions tested\n- Critical Inker: Scaffolding Critical Thinking in AI-Assisted Writing Through Socratic Questioning (arXiv 2604.07167, Hugenroth et al., 2026) — Socratic scaffolding for writing; small pilot, different domain\n- Brainrot: Deskilling and Addiction are Overlooked AI Risks (FAccT 2026, Chalkidis & Søgaard)\n- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making (CSCW 2021, Buçinca et al.)\n- Endoscopist deskilling risk after exposure to AI in colonoscopy (Budzyń et al., Lancet Gastroenterol Hepatol 2025)\n- Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant (Kosmyna et al., 2025)\n- Mitigating Epistemic Debt in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts (arXiv 2602.20206, 2026) — scaffolded friction in programming with AI-blackout test; different domain, no longitudinal follow-up\n- Deskilling dilemma: brain over automation (Frontiers in Medicine, 2026) — provides cognitive/diagnostic/moral deskilling typology and distinguishes deskilling-as-outcome from overreliance-as-behavior\n- Measuring and mitigating overreliance is necessary for building human-compatible AI (arXiv 2509.08010) — identifies gaps in overreliance measurement and LLM-specific trust dynamics\n- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, Ghosh et al., 2026)\n- From Algorithm Aversion to AI Dependence: Deskilling, Upskilling, and Emerging Addictions in the GenAI Age (Kim, Consumer Psychology Review 2026)\n- Generative AI Reliance and Executive Function Attenuation (Baldeo, Technology Mind & Behavior 2026)\n- Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '40–60 (self-hosting Qwen 3.5 27B on H100 for real-time experiment serving; or ~$50–80 via API with no self-hosting needed)', 'timeline': '5 months (1 mo platform design + task creation, 3–4 weeks IRB approval, 2 weeks pilot N=80, 6 weeks main data collection in overlapping waves to accommodate 4-week follow-ups, 5 weeks analysis + writing)', 'estimated_gpu_cost': '$80–120 (H100 at ~$2/hr) or $50–80 via OpenRouter API'}\n- **human_in_loop**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4.5 months (Claude accelerates platform dev, task item generation via IRT-calibrated stimulus pools, statistical analysis scripting, and manuscript drafting)', 'claude_api_cost': '$350 (platform scaffolding, stimulus generation, R/Python analysis pipelines, growth-curve modeling code, manuscript drafting)', 'estimated_gpu_cost': '$80–120 or $50–80 via API'}\n- **auto_research**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4 months (automated pilot analysis, adaptive task calibration, parallel manuscript drafting)', 'claude_api_cost': '$900 (end-to-end experimental platform generation, automated IRT-based item analysis, growth-curve model specification, full statistical report generation, iterative manuscript revision)', 'estimated_gpu_cost': '$80–120 or $50–80 via API', 'speed_bottleneck': 'IRB approval (3–6 weeks, irreducible) and the 4-week delayed follow-up window; participant compensation dominates total cost: N=480 initial session (40 min at $12/hr = $3,840) + 33.3% Prolific academic fee ($1,279) + 1-week follow-up (~385 retained, 20 min, $1,540 + $513 fee) + 4-week follow-up (~310 retained, 20 min, $1,240 + $413 fee) + completion bonuses (~$700 + $233 fee) = ~$9,760 total participant costs'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T18:45:57.089Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:45:57.089Z",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T18:45:57.103Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：会议投稿方向完全不匹配】

本 proposal 的目标投稿会议是 CoRL 2026（Conference on Robot Learning），但 proposal 内容是一项纯 HCI/行为科学人因实验——关于人类在 AI 辅助信息评估中的认知退化、脚手架式摩擦干预和信任校准。这与 CoRL 的 scope 完全不相关。

CoRL 2026 明确的征稿范围包括：robot perception and control、robot foundation models、imitation learning、reinforcement learning for physical robots、robot manipulation/navigation/locomotion/driving/flight、robot systems and hardware、theoretical foundations of robot learning。投稿须"focus on a core robotics problem and demonstrate relevance to robotics"。

本 proposal 没有任何机器人学习成分——没有机器人、没有感知/控制、没有强化学习、没有 sim-to-real。这是一项在 Prolific 平台上的 N≈480 人因被试实验，研究人类认知技能退化。合理的目标会议应为 CHI 2027、CSCW 2027、FAccT 2027 或 AAAI HCOMP。

如果坚持投 CoRL，接受概率为 0%——不是 idea 质量问题，而是会在 desk review 阶段被直接拒绝（out of scope）。

以下评估假设 proposal 投向合理的 HCI 会议（如 CHI 2027），仅评 idea 内核质量。

---

【领域调研】:

- [Rani et al., arXiv 2510.01537] (CHI 2026): 最直接前序工作。N=67，within-subjects，GPT-4o 辅助错误信息检测，4 周后准确率下降 15.3%。无干预、无对照组、36% 流失率。明确呼吁后续做 scaffolding 干预研究。论文真实存在，已正式发表于 CHI '26（ACM DL 可查）。Proposal 描述准确。

- [Althea, arXiv 2602.11161] (2026, N=963): 最接近的 scaffolding 对比工作。比较三种交互模式对 fact-checking 的影响，自主搜索模式在 10 天随访中表现最持久。但无 AI 撤除设计、无 unrestricted-AI 条件、作者自认测量的是"short-term retention"。论文真实存在，描述准确。

- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026, N=1222): 大规模 RCT，仅 10 分钟 AI 使用即导致数学和阅读理解的独立表现下降。因果证据强。无干预测试。论文真实存在，描述准确。

- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, MIT, 2026): 纯理论动态模型，证明理性 AI 采用可导致稳态技能损失。识别 training rate (κ) 和 workflow design (β) 作为缓解杠杆。无实证验证。论文真实存在，描述准确。

- [Adjust for Trust, arXiv 2502.13321] (IUI 2026): 信任自适应干预，含 10 秒强制暂停，最高降低 38% 不当依赖。仅 within-session 测量。论文真实存在，描述准确。

- [Farach et al., arXiv 2604.08678] (2026, N=388): Fortune 500 公司现场实验，行为脚手架反而降低质量，认知脚手架仅对顶尖表现者有效。单次会话测量。论文真实存在。

- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程领域 AI 导致 17% 技能下降。无干预。论文真实存在。

- [Metacognitive scripts, arXiv 2602.20206] (2026): 编程领域的 scaffolded friction + AI-blackout 测试。77% vs 39% 任务失败率。无纵向随访。论文真实存在。

- [Budzyń et al.] (Lancet Gastroenterol Hepatol 2025): 临床领域，AI 撤除后腺瘤检出率下降 6 个百分点。真实存在。

- 调研总结: AI 导致的认知退化（deskilling）在 2025-2026 年已成为 HCI/AI 领域的热点话题，跨医疗、教育、编程多个领域均有实证。但"如何通过 scaffolded friction 预防 AI 撤除后的纵向技能退化"这一具体问题确实尚无直接回答。Proposal 定位于 Rani et al. 明确呼吁的 follow-up 研究，属于"well-motivated incremental next step"而非"paradigm-shifting insight"。

---

【Trivial Alternative 检验】:

存在多个更简单的替代方案威胁：

1. **最简单的 trivial baseline——"先独立思考再看 AI"**：这本质上就是 proposal 的 scaffolded friction 条件的核心操作（mandatory independent attempt）。Berger et al. (2603.29866) 已经在 10 个数据集上证明"先独立判断再看 AI 建议"能提高准确率。CFF 文献（Buçinca et al. 2021）也证明了类似的 within-session 效果。Proposal 的增量价值在于：将这个已知有效的 within-session 策略延伸到 cross-session longitudinal skill retention 测量。这是一个真实的增量，但核心干预本身并不新——新的是测量维度。

2. **"少用 AI"**：如果限制 AI 使用时间或频率，是否也能减缓退化？Proposal 没有包含这个条件。这不是致命缺陷，但审稿人可能会追问。

**增量价值判断**：增量确实存在（longitudinal AI-withdrawal + scaffolding 的组合是新的），但主要是方法论/实验设计层面的新颖性，而非概念层面的新颖性。核心 insight——"让人在用 AI 时保持认知参与可以减少退化"——是直觉上显而易见的。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **关键假设：within-session cognitive engagement → cross-session skill retention**。CFF/scaffolding 被证明能减少 within-session 过度依赖，但"减少依赖"≠"保留技能"。完全有可能：scaffolding 在使用时降低了依赖率，但撤除 AI 后技能仍然退化（因为参与者虽然在 session 内被迫思考，但没有真正内化推理策略）。这个跳跃是 proposal 最大的假设风险。

2. **Rani et al. 效应的可复现性**：N=67, 36% attrition, within-subjects, no control group。15.3% 的效应量可能不稳健。如果这个前提不成立（即 unrestricted-AI 条件未能复现显著退化），整个实验的核心对比将失去意义。

3. **30 分钟 treatment 足以产生可测量的退化**：Rani et al. 用了 4 周纵向设计，而大型 RCT (2604.04721) 仅用 10 分钟就产生了效果。但信息评估任务的难度和认知深度可能不同，30 分钟的 treatment 是否足够是经验性假设。

4. **Trust 作为 deskilling 调节变量的假设**：Adjust for Trust 证明 trust 预测 within-session reliance，但"trust → reliance"和"trust → cross-session skill decay rate"是不同的因果路径。后者缺乏理论或实证支撑。

---

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将已有技术（CFF/scaffolding）应用到一个新的测量范式（AI-withdrawal + longitudinal skill decay curve）。各个组件都已存在：CFF 干预（Buçinca et al. 2021）、AI 撤除导致退化（Rani et al. CHI 2026; 2604.04721）、scaffolding 模式对比（Althea 2602.11161）、trust 预测 reliance（Adjust for Trust 2502.13321）。Proposal 的新颖性在于将这些组件组合为一个统一实验——"first controlled test of scaffolded friction + AI-withdrawal + longitudinal decay curve"。这是一种实验设计层面的新颖性（"no one has combined A+B+C+D in one study"），而非概念层面的新颖性（"here is a new insight about how X works"）。审稿人可能会说："The experimental design is well-motivated, but the core hypothesis—that scaffolding preserves skills—is not surprising." 给弱-中是因为组合确实产生了新的科学问题（longitudinal decay prevention），但该问题的答案在 positive 情况下不具有 surprise value。

2. **Significance: 中** — 
   研究问题本身——"如何防止 AI 撤除后的认知退化"——是重要且及时的。AI deskilling 已成为 2025-2026 的热门话题（CACM 社论、Lancet 临床证据、多篇 arXiv 高引论文）。但 proposal 的贡献形态是"intervention study in a specific domain (information evaluation)"，其可推广性有限：(a) 任务域是信息评估/错误信息检测，这是一个相对小众的应用场景；(b) 30 分钟 treatment + Prolific 被试的生态效度有限；(c) 即使结果 positive（scaffolding 有效），对领域的 insight 推进不大——"保持认知参与有助于技能保留"接近 common sense。如果结果 negative（scaffolding 也无法阻止退化），反而更有 significance。Trust moderation 维度是一个不错的补充，但本身不够构成独立贡献。

3. **Related Work: 强** — 
   Proposal 的 related work 覆盖极为全面——Rani et al., Althea, CFF 文献, Augmentation Trap, Adjust for Trust, 大型 RCT, 临床证据, metacognitive scripts, Farach et al. 全部涵盖。引文描述经核实均准确。差异化定位清晰明确：逐一与每篇关键工作做 key distinction 对比。这是 proposal 最强的维度。唯一轻微不足是缺少对"AI-free periods"实践（如新加坡医疗系统已在做的）的引用，但不影响整体质量。

---

【概率估计】: [25% - 35%] 中位 30%
（注：此概率假设投向 CHI 2027 等合理 HCI 会议。如投 CoRL 2026，概率为 0%。）

【估计理由】: 
Idea 属于"well-motivated incremental follow-up"类型——直接回应 Rani et al. (CHI 2026) 明确呼吁的 future work，实验设计扎实、related work 覆盖优秀、差异化定位清晰。但核心 novelty 限制了上限：（1）各组件均非原创，novelty 来自组合而非 insight；（2）core hypothesis positive 时不具 surprise value（审稿人大概率说"I would have guessed that scaffolding helps"）；（3）概念增量主要在测量维度（longitudinal → cross-session）而非方法或理论。Related Work 的强势和实验设计的规范性（N≈480, pre-registered, between-subjects, multi-timepoint）确保了下限（不会因设计缺陷被拒），但 Novelty 的弱-中限制了上限（很难让审稿人 excited）。

如果 Novelty 更强（比如发现了反直觉的 deskilling 机制，而不仅是测试已有干预），中位概率可以到 40%+。

【主要风险】:
1. **"Predictable outcome" 质疑**：如果 scaffolding 有效，审稿人会认为这是 expected；如果无效，可能认为是 treatment 不够强。无论哪个方向，insight 增量都有限。这是最可能导致被拒的 idea 层面风险。
2. **"Combination ≠ Contribution" 质疑**：审稿人可能认为将已有组件（CFF + AI-withdrawal + longitudinal + trust moderation）拼在一起做一个大实验，虽然 well-executed，但缺乏 conceptual novelty——"a well-designed study is not the same as a novel contribution"。
```

---

**补充说明（投稿方向）**：这是一篇做得很扎实的 HCI 行为科学 proposal，但 **绝对不应投 CoRL 2026**。CoRL 是机器人学习会议，本 proposal 不含任何机器人学习内容，会被 desk reject。建议改投：
- **CHI 2027**（最匹配，Rani et al. 原文也在 CHI 发表）
- **CSCW 2027**（CFF 文献的主要发表地）
- **FAccT 2027**（AI 公平性/社会影响）
- **AAAI HCOMP 2026**（人-AI 协作）

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Rani et al. - Dialogues with AI (CHI 2026)](https://arxiv.org/abs/2510.01537)
- [Althea (arXiv 2602.11161)](https://arxiv.org/abs/2602.11161)
- [AI Assistance Reduces Persistence (arXiv 2604.04721)](https://arxiv.org/abs/2604.04721)
- [The Augmentation Trap (arXiv 2604.03501)](https://arxiv.org/abs/2604.03501)
- [Adjust for Trust (arXiv 2502.13321)](https://arxiv.org/abs/2502.13321)
- [AI deskilling is a structural problem (AI & Society 2025)](https://link.springer.com/article/10.1007/s00146-025-02686-z)
- [The AI Deskilling Paradox (CACM)](https://cacm.acm.org/news/the-ai-deskilling-paradox/)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：会议投稿匹配度】

本 proposal 拟投 CoRL 2026（Conference on Robot Learning），但 CoRL 的 Call for Papers 明确要求：
"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics."
"Submissions without a robotics focus will be returned without review."

本 proposal 的内容是：AI 辅助信息评估中的认知去技能化（deskilling）、scaffold 摩擦干预、信任校准——这是一个纯粹的 HCI/认知科学/人因学研究，涉及在线 Prolific 实验、误信息检测任务、信任量表等。与机器人学（manipulation, locomotion, sim-to-real, robot learning）完全无交集。

**结论：此 proposal 在 CoRL 将被 desk reject，无需进入审稿流程。** 合适的投稿会议应为 CHI、CSCW、FAccT、AAAI HCOMP 等 HCI/human-AI interaction 会议。

以下评估将同时给出：(a) CoRL 投稿的实际概率，(b) 假设投到合适 HCI 会议（如 CHI/CSCW）时的 idea 质量评估，供后续决策参考。

---

【领域调研】:

- [Rani et al., arXiv 2510.01537] (CHI 2026): 最直接的前序工作。N=67 的 within-subjects 研究，发现 AI 辅助误信息检测在 4 周后导致 15.3% 准确率下降。无干预、无对照组、样本小。本 proposal 正是对其 future work call 的直接回应。论文真实存在，描述准确。

- [arXiv 2604.04721, Liu et al.] (under review, 2026): 1,222 人 RCT，证明仅 10 分钟 AI 使用即可降低算术和阅读理解的独立表现。提供了因果证据但未测试干预。论文真实存在，描述准确。

- [Althea, arXiv 2602.11161, Churina et al.] (2026, N=963): 比较三种 scaffolding 模式在 fact-checking 中的效果，发现自主搜索模式产生最持久的改善。但无 AI-withdrawal 设计、无 unrestricted AI 对照组。论文真实存在，描述准确。

- [Augmentation Trap, arXiv 2604.03501, Caosun & Aral] (2026): MIT Sloan 的理论模型，证明理性 AI 采纳也可能导致稳态技能损失。提出 training rate (κ) 和 workflow design (β) 两个缓解杠杆，但纯理论、无实证。论文真实存在，描述准确。

- [Adjust for Trust, arXiv 2502.13321, Srinivasan & Thomason] (IUI 2026): 测试信任自适应干预（解释、强制暂停），达到 38% 不当依赖减少。仅限 within-session，未测量跨会话技能保持。论文真实存在，描述准确。

- [Metacognitive Scripts, arXiv 2602.20206] (2026, N=78): 在编程领域测试 scaffold 摩擦（Explanation Gate），unrestricted AI 用户 77% 在 AI-blackout 任务中失败 vs. scaffolded 组 39%。不同领域，无纵向随访。论文真实存在，描述准确。

- [Farach et al., arXiv 2604.08678] (2026, N=388): 行为 vs. 认知 scaffold 的 Fortune 500 现场实验。行为 scaffold 反而降低质量，认知 scaffold 仅对顶尖表现者有效。单次会话测量。论文真实存在。

- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 提出通过 multi-agent 认知强制函数实施 scaffold 摩擦的理论框架，零实证。

- **调研总结**: AI 去技能化（deskilling after AI withdrawal）是 2025-2026 年的热门议题，已有多个方向的因果证据（Rani et al., 1222人RCT, 编程领域 Shen & Tamkin）。Scaffolding/friction 干预在 within-session overreliance 上已被广泛研究（CFF, Adjust for Trust），但"scaffold 能否预防 AI 撤回后的纵向技能退化"确实是一个尚未被填补的空白。本 proposal 精准定位在这个空白上，属于"自然下一步"而非"意外发现"。

---

【Trivial Alternative 检验】:

**存在 trivial alternative 威胁，但有部分增量价值。**

最简单的替代方案是：在 AI 辅助期间，简单地要求用户"先自己做一遍再看 AI 答案"（即 mandatory independent attempt alone）。这不需要复杂的 incremental hints 系统或 self-explanation gates，但可能就已经能预防大部分 deskilling。Berger et al. (2603.29866) 已经证明"独立判断优先"能在 10 个数据集上提升人-AI 准确率。

增量价值在于：
1. 本研究不仅测试"是否有效"，还比较了两种不同 scaffold 哲学（friction vs. agency-preserving exploration）
2. Trust 作为 moderator 的维度是额外贡献
3. 纵向 decay curve（即时/1周/4周）提供了过程信息

但核心干预手段（"先自己试，再看提示"）并不新颖。如果结果显示简单的 mandatory independent attempt 就足够了，那 incremental hints + self-explanation gates 的额外工程就是过度设计。

---

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **30 分钟 AI 治疗足以诱发可测量的 deskilling**：1222人 RCT 用 10 分钟诱发了 deskilling，但那是在算术/阅读理解（低复杂度任务）中。信息评估（claim verification, multi-source synthesis）是否在 30 分钟内产生足够的认知依赖以导致可测量退化，这是假设，不是事实。Rani et al. 的 deskilling 是在 4 周多次 AI 交互后才出现的。

2. **Prolific 在线实验者的行为可推广到真实场景**：proposal 将 Prolific 上的 30 分钟任务产生的 deskilling 类比于现实中长期 AI 使用者的技能退化——生态效度存疑。

3. **Qwen 3.5 27B 能提供与 GPT-4o 可比的"逼真" AI 辅助**：Rani et al. 使用 GPT-4o + Google Search。Qwen 3.5 27B（较弱模型）是否能诱发相同程度的信任和认知卸载，直接影响实验效果。

4. **Trust 作为 deskilling speed 的 moderator**：这是一个合理但未经验证的假设。Adjust for Trust 证明 trust 预测 within-session reliance，但 within-session reliance → cross-session deskilling 的映射不是必然成立的。

---

【3 维度打分】:

1. **Novelty: 中** — 本 proposal 的核心贡献是将已有组件（scaffolded friction + AI withdrawal design + longitudinal decay curve + trust moderation）组合应用于信息评估领域。每个组件单独来看都不新颖：scaffolded friction 在 CFF 文献和 2602.20206 中已有测试；AI withdrawal 设计在 2604.04721 和 Rani et al. 中已有使用；trust 作为 reliance moderator 在 Adjust for Trust (2502.13321) 中已有验证。真正的 novelty 是组合——"scaffold + withdrawal + longitudinal + trust moderation" 在信息评估中的首次完整测试。这是 solid incremental contribution，但审稿人很可能会说"这是 Rani et al. future work 的直接执行，是一个很好的 follow-up study，但 conceptual novelty 有限"。核心发现如果是 positive（scaffold 确实减缓 deskilling），多数审稿人会说"I would have guessed this"。

2. **Significance: 中** — 研究问题本身重要：AI deskilling 是 2025-2026 年的热点问题，有明确的政策和教育含义。但本 proposal 的实际 impact 受限于：(a) 30 分钟 online 实验的生态效度——真实世界的 deskilling 发生在长期、高频使用场景中；(b) 信息评估任务的可推广性——claim verification 不等于真实的新闻消费或日常决策；(c) 如果 scaffold 确实有效（高先验概率），finding 的信息量不高；如果无效，那更有意思但也更难发表。对领域的推动主要在于提供"是否有效"的量化证据，而非概念性突破。

3. **Related Work: 强** — 这是本 proposal 的最大亮点。文献覆盖极其全面：从 Rani et al. 到 Althea，从 Augmentation Trap 到 Adjust for Trust，从 CFF 到 metacognitive scripts，几乎涵盖了所有 2025-2026 年的相关工作。每篇论文的描述都经我调研验证准确。差异化定位也非常清晰——每个"Key distinction"段落都精确指出了与前序工作的差异（within-session vs. cross-session, improvement persistence vs. deskilling prevention, etc.）。

---

【概率估计】:

- **CoRL 2026**: 0-2%，中位 1%（desk reject，完全的会议-主题不匹配）
- **如果投到合适的 HCI 会议（CHI/CSCW）**: 25-35%，中位 28%

【估计理由】:

**CoRL**: Proposal 是纯 HCI/认知科学研究，涉及在线人类实验、误信息检测、trust 量表。CoRL 要求"core robotics problem"，无机器人内容将被直接退回。这不是 idea 质量问题，而是根本性的会议匹配错误。

**合适 HCI 会议 (28%)**: 
- Related Work 维度强，说明作者对领域有深入理解，positioning 清晰。
- 但 Novelty 为"中"限制了上界——核心 claim 方向可预测（scaffold 应该能减缓 deskilling），组合式贡献（combinatorial contribution）在顶会中通常被视为 incremental。
- Significance 为"中"进一步限制——30 分钟 Prolific 实验的生态效度可能招致审稿人质疑实际影响力。
- 如果实验执行出色且结果有 nuance（比如 scaffold 在某些维度有效但在另一些维度无效，或 trust moderation 效应出人意料），概率可上升到 35%。
- 如果结果全面 positive 且符合预期，审稿人可能认为 contribution 不够 surprising，概率下探至 22-25%。

【主要风险】:

1. **"Natural next step" 陷阱**：本 proposal 本质是 Rani et al. (CHI 2026) 明确呼吁的 future work 的直接执行。审稿人可能认为这是一个 well-executed follow-up study，但缺乏独立的 conceptual contribution。如果核心发现是 positive（scaffold 减缓 deskilling），方向完全可预测，surprise value 低。

2. **致命的会议选择错误**：投 CoRL = 确定性 desk reject。这是可以立刻纠正但必须纠正的问题。
```

---

**总结**：这个 proposal 的 idea 质量是 **中等偏上**——文献把握扎实、gap 定位精准、设计逻辑自洽，是一个典型的 "well-motivated incremental contribution"。但有两个关键问题：

1. **（致命）会议选择完全错误。** CoRL 是 Conference on Robot Learning，本 proposal 无任何机器人内容，将被 desk reject（0-2%）。应改投 CHI、CSCW、FAccT 等 HCI 会议。

2. **（idea 层面）核心发现方向可预测。** 即使投到正确会议，"scaffolded friction 能减缓 AI 撤回后的 deskilling"这一预期结果对多数审稿人来说并不 surprising，Novelty 上限受限于组合式贡献的本质。

建议：如果确认是 CoRL，应立即止损；如果投稿目标可以调整为 CHI/CSCW，该 idea 值得进入后续完善流程。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)
- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)
- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)
- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)
- [Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance](https://arxiv.org/abs/2502.13321)
- [Metacognitive Scripts for Novice Programming](https://arxiv.org/abs/2602.20206)
- [Cognitive Agency Surrender](https://arxiv.org/pdf/2603.21735)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have enough information to provide a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage
```

## ⚠️ 致命前置问题：投稿目标会议严重不匹配

**CoRL (Conference on Robot Learning) 2026 的主题范围是机器人学习**——包括 robot perception, manipulation, navigation, locomotion, reinforcement learning for physical robots, robot foundation models 等。其 Call for Papers 明确指出 **"submissions without a robotics focus will be returned without review"**。

本 proposal 是一个纯 HCI/认知科学研究：在线被试实验、scaffolded friction、cognitive deskilling prevention、trust calibration——**与机器人学习没有任何关联**。提交至 CoRL 将被 desk reject，不会进入审稿流程。

**合适的目标会议**：CHI 2027、CSCW 2026/2027、FAccT 2027、IUI 2027、或 AAAI/IJCAI 的 Human-AI Interaction track。

> 以下评估基于 idea 本身的质量（假设投到合适的 HCI 会议），但概率估计会将 CoRL 的 venue mismatch 作为致命因素纳入。

---

```
【领域调研】:
```

- **[Rani et al., arXiv 2510.01537] (CHI 2026)**: 本 proposal 最核心的先驱工作。N=67 within-subjects 设计，发现 AI 辅助 misinformation detection 后 4 周 unassisted accuracy 下降 15.3%。无干预、无对照组。该论文 future work 明确呼吁 scaffolding interventions。Proposal 直接回应此呼吁——定位准确。

- **[arXiv 2604.04721, Liu et al.] (under review 2026)**: 1,222 人 RCT，因果证据表明仅 10 分钟 AI 使用即可降低 arithmetic/reading comprehension 独立表现。提供了 deskilling 的大规模因果证据，但未测试任何干预。Proposal 准确引用。

- **[Althea, arXiv 2602.11161, Churina et al.] (2026)**: N=963，比较三种 scaffolding 模式对 fact-checking 的改善持久性。Self-directed search 产生最持久的改进。但无 AI-withdrawal 设计，无 unrestricted-AI 条件，作者承认仅测量"short-term retention"。Proposal 引用准确，定位差异化清晰。

- **[The Augmentation Trap, arXiv 2604.03501, Caosun & Aral] (2026)**: MIT Sloan 的形式化动态模型，证明理性 AI 采用仍可导致 steady-state skill loss。纯理论，无实证。Proposal 声称 operationalize 其 mitigation levers (training rate κ, workflow design β)——这一连接是合理的但需验证。

- **[Adjust for Trust, arXiv 2502.13321, Srinivasan & Thomason] (IUI 2026)**: Trust-adaptive interventions 减少 38% inappropriate reliance，但仅测量 within-session reliance decisions，非 cross-session skill retention。Proposal 引用准确。

- **[arXiv 2602.20206] Metacognitive Scripts in Programming (2026)**: Scaffolded friction 在编程领域，AI-blackout test 中 77% vs 39% failure，但无纵向 follow-up，不同领域。

- **[Farach et al., arXiv 2604.08678] (2026)**: 388 人 field experiment，behavioral vs. cognitive scaffolding；single-session measurement，无纵向跟踪。

- **调研总结**: AI-induced deskilling 在 2025-2026 已成为一个活跃且有实证支撑的研究领域，跨多个 domain（医学、编程、信息评估、算术）。**核心空白确实存在**：目前没有研究同时具备 (a) scaffolding 干预 + (b) AI-withdrawal longitudinal design + (c) information evaluation domain。但该空白的性质更接近"experimental design gap"（实验设计层的空缺），而非"conceptual gap"（概念层的突破）。

---

```
【Trivial Alternative 检验】:
```

**存在明显的 trivial alternative 威胁。**

1. **Mandatory independent attempt alone**: Proposal 的 scaffolded friction 条件包含三个组件（mandatory independent attempt, incremental hints, self-explanation gates）。但 Berger et al. (arXiv 2603.29866) 已证明仅"independent judgment first"就能跨 10 个数据集提升 accuracy。**最简单的 baseline——仅强制独立尝试（无 hints、无 self-explanation）——可能已经捕获了大部分 deskilling prevention 效果。** 如果 scaffolded friction 的效果主要来自 mandatory independent attempt 这一组件，那么 incremental hints 和 self-explanation gates 的增量价值就很有限。

2. **Reduced AI quality**: 直接降低 AI 输出的完整度/质量（如只给 partial hints 而非完整答案）是否就足以防止 deskilling？这不需要复杂的 scaffolding 机制。

3. **Proposal 的增量价值**: Proposal 的真正增量在于 *longitudinal AI-withdrawal design* + *多条件对比的 skill decay curve*。但这更多是实验设计的贡献，而非方法论或理论创新。

---

```
【前提假设检验】:
```

**核心 claim 的逻辑链条中有两个关键的未验证假设：**

1. **"30 分钟 AI 辅助足以产生可测量的 deskilling"**: 这是整个实验的基础假设。Rani et al. 用了 4 周 weekly sessions，deskilling RCT 用了 10 分钟但在算术/阅读理解（远比 information evaluation 更练习敏感的简单任务）。本 proposal 仅用 30 分钟单次 session 在 information evaluation 这一复杂认知任务上，能否诱导出足够大的 deskilling 效应以被检测到？**这一假设缺乏直接支撑。** 如果 unrestricted-AI 条件在 30 分钟后未产生显著 deskilling，整个研究的 scaffolding 对比就失去了意义。

2. **"Trust calibration 是 deskilling severity 的有意义 moderator"**: Adjust for Trust 证明了 trust predicts within-session reliance behavior，但 trust → cross-session skill decay 的跳跃是一个额外的、未经验证的推断。Between-subjects 设计中 N≈120/condition 对 trust × condition × time 三重交互的统计功效可能不足。

3. **"Scaffolded friction 的效果可以跨 4 周保持"**: 即使 scaffolding 在 immediate post-test 有效，1-week 和 4-week follow-up 时 scaffolding 条件是否仍优于 unrestricted-AI 条件是未知的。人类遗忘曲线可能抹平初始差异。

---

```
【3 维度打分】:
```

### 1. Novelty: **中** (偏弱)

**理由**: Proposal 正确识别了一个 empirical gap——没有研究同时结合 scaffolding intervention + AI-withdrawal longitudinal design + information evaluation。但这个 gap 的性质是 **experimental design gap**，而非 **conceptual novelty**。核心假设"强制认知参与可以防止认知退化"本质上是教育心理学中 desirable difficulties (Bjork, 1994) 和 generation effect 的直接应用——这并不新颖。

- Rani et al. (CHI 2026) 已建立 deskilling 存在；
- Althea (2602.11161) 已证明 scaffolding 的 improvement persistence；
- Berger et al. (2603.29866) 已证明 independent judgment first 的有效性；
- Metacognitive scripts (2602.20206) 已在编程中测试 scaffolded friction with AI-blackout。

本 proposal 做的是把这些已有元素**组合到一个更完整的实验设计中**——这是 execution novelty，不是 idea novelty。如果核心结果是 positive（scaffolding reduces deskilling），大多数审稿人会说 **"I would have guessed this"**。

### 2. Significance: **中**

**理由**: AI deskilling 确实是 2025-2026 的热门问题，有广泛的社会关切（Frontiers 2026 framework, FAccT 2026, Lancet 2025 clinical evidence）。如果结果为 positive，提供的是 **实践指导**（"设计 AI 工具时加入 scaffolded friction"），这有价值但不令人意外。如果结果为 negative（scaffolding 不能防止 deskilling），这反而更有 significance，因为它挑战了领域的乐观假设。

但 significance 受限于：
- 任务域较窄（online information evaluation with Prolific workers）
- 30 分钟单次 session 的生态效度有限
- 发现难以推广到高风险专业领域（医学、法律）

### 3. Related Work: **强**

**理由**: 这是 proposal 最突出的优势。文献覆盖极其全面——Rani et al., Althea, deskilling RCT, Augmentation Trap, Adjust for Trust, CFF literature, Cognitive Agency Surrender, Farach et al., metacognitive scripts, Critical Inker, Berger et al.——关键论文均已核实为真实存在且描述准确。每篇的差异化定位（"Key distinction from X"）清晰且合理。唯一的小问题是 proposal 过度强调"no study combines (a)+(b)+(c)+(d)+(e)"——这种组合式 novelty claiming 容易被审稿人视为 gap-filling exercise。

---

```
【概率估计】: 0% — 3%（中位 ~1%）[投稿 CoRL 2026]
```

```
【概率估计（如投稿 CHI/CSCW 等合适 HCI 会议）】: 25% — 35%（中位 ~30%）
```

```
【估计理由】:
```

**CoRL 概率（~1%）**: 本 proposal 与 CoRL 的主题范围（robot learning）完全不匹配。CoRL 明确声明 "submissions without a robotics focus will be returned without review"。这是一个纯 HCI/认知科学的在线用户实验，不涉及任何机器人、物理系统或 embodied learning。**Desk reject 是几乎确定的结果。**

**HCI 会议概率（~30%）**: 如果投到 CHI/CSCW 等合适会议，idea 质量处于 25-35% 区间：
- **方向正确**：deskilling prevention 是 timely 且重要的问题
- **真实的 empirical gap**：longitudinal scaffolding + AI-withdrawal 设计确实无先例
- **Related work 极为扎实**
- **但 idea 内核是"组合式 gap-filling"**：将已有的 scaffolding 方法（CFF + Althea-style）放入一个更完整的实验框架，核心发现若 positive 不具备 surprising 性
- **Trivial alternative 威胁**限制了上界：mandatory independent attempt alone 可能解释大部分效果
- **30 分钟 treatment 能否诱导可测量 deskilling** 是一个基础性风险

```
【主要风险】:
```

1. **Venue mismatch（致命）**: 投 CoRL = desk reject。这是最直接、最不可补救的风险。
2. **"I would have guessed this" 问题**: 核心发现（scaffolded friction reduces deskilling）高度符合直觉，缺乏 surprising element。审稿人可能认为这是 confirmatory study，novelty delta 不足以支撑 top-venue acceptance。

---

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)
- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)
- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)
- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)
- [Adjust for Trust](https://arxiv.org/abs/2502.13321)
- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)
- [Farach et al. - Scaffolding Human-AI Collaboration Field Experiment](https://arxiv.org/abs/2604.08678)
- [Metacognitive Scripts for Programming](https://arxiv.org/abs/2602.20206)


【原始 proposal（允许参考但不是主要依据）】:
# When the AI Goes Away: Scaffolded Friction, Trust Calibration, and the Skill Decay Curve After AI-Assisted Information Evaluation

## Description
Rani et al. (CHI 2026) demonstrate that AI-assisted misinformation detection leads to 15.3% skill degradation over 4 weeks after AI withdrawal—but their study tested no interventions, included no control group, and had only N=67. We provide the first controlled test of whether scaffolded cognitive friction can prevent this degradation—and whether trust calibration moderates deskilling severity. While the deskilling problem in information evaluation is now empirically established (Rani et al.), the scaffolding literature (Althea, CFF studies, Adjust for Trust) measures only within-session or short-term improvements, not whether interventions protect independent capability after AI is permanently removed. We address this gap with a pre-registered, between-subjects experiment (N≈480) comparing four conditions: no-AI control, unrestricted LLM access (Qwen 3.5 27B), scaffolded friction (mandatory independent attempt, incremental hints, self-explanation gates—operationalizing the Augmentation Trap's theoretical mitigation levers), and exploratory scaffolding (Althea-style modular evidence exploration). Participants complete information evaluation tasks—claim verification, multi-source synthesis, argument quality evaluation—across three phases: baseline assessment, AI-assisted treatment, and post-AI independent assessment at three timepoints (immediate, 1-week, 4-week), yielding per-condition skill decay curves. This design directly answers Rani et al.'s call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains,' extends Althea beyond their acknowledged limitation of measuring only 'short-term retention of reasoning patterns,' and operationalizes the Frontiers framework's distinction between overreliance-as-behavior (measured by CFF studies) and deskilling-as-outcome (measured by our cross-session capability decline). A trust calibration dimension—building on Adjust for Trust's finding that trust predicts within-session reliance—tests whether users who develop higher AI trust during treatment deskill faster after AI removal. The study provides the first empirical test of scaffolded friction interventions combined with an AI-withdrawal design, multi-timepoint decay curve, and trust moderation for deskilling prevention in information evaluation.

## Core Problem
Can scaffolded cognitive friction interventions prevent the rapid skill degradation that emerges after AI assistance is removed from information evaluation tasks—and does the speed of deskilling depend on how much users trusted the AI? Rani et al. (CHI 2026, N=67) have now demonstrated that AI-assisted misinformation detection leads to a 15.3% accuracy decline after 4 weeks of AI withdrawal, but their study tested no interventions, included no control group, and explicitly calls for scaffolding-based solutions. The CFF and scaffolding literatures (Buçinca et al., Althea, Adjust for Trust) test friction and trust-adaptive interventions to reduce within-session overreliance, but no study has tested whether such interventions protect independent capability after AI access is permanently revoked—nor whether trust calibration moderates the severity of post-withdrawal skill decay.

## Opportunity
A convergence of causal, clinical, and now longitudinal evidence creates a precisely bounded gap. Rani et al. (arXiv 2510.01537, CHI 2026) provide the first longitudinal evidence that AI-assisted information evaluation causes deskilling after AI removal: 15.3% accuracy decline over 4 weeks in misinformation detection (N=67, within-subjects, no control group, no interventions). Their authors explicitly call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains' as future work—this is exactly the study we propose. The landmark 1,222-participant RCT (arXiv 2604.04721) provides causal evidence that just 10 minutes of AI use degrades independent performance in arithmetic and reading comprehension. The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) formalizes this as a dynamic model where rational AI adoption can still leave workers worse off, identifying training rate (κ) and workflow design (β) as mitigation levers—but provides no empirical test. Clinical data shows 6-point adenoma detection drops after AI removal (Budzyń et al., Lancet Gastroenterol Hepatol 2025). The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction as a countermeasure but tests nothing empirically. Althea (arXiv 2602.11161, N=963) demonstrates that self-directed scaffolding produces more persistent fact-checking improvements at 10-day follow-up—but has no AI-withdrawal test, no unrestricted-AI condition, no pre-AI baseline, and its authors explicitly acknowledge measuring 'short-term retention of reasoning patterns, not durable skill acquisition.' The metacognitive scripts study (arXiv 2602.20206) tests scaffolded friction in programming (77% vs. 39% failure on AI-blackout tasks) but not information evaluation and lacks longitudinal follow-up. Shen & Tamkin (arXiv 2601.20245) provide RCT evidence of 17% deskilling in programming skill formation with AI but test no interventions and measure only within-session outcomes. Adjust for Trust (arXiv 2502.13321, IUI 2026) tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance—but measures only within-session reliance decisions, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment but measure single-session document quality, not longitudinal skill retention. No study combines: (a) scaffolded friction interventions, (b) an AI-withdrawal design with pre/during/post phases, (c) information evaluation tasks, (d) a multi-timepoint skill decay curve, and (e) trust calibration as a moderator of deskilling severity. The gap is not 'does deskilling occur after AI withdrawal in information evaluation?'—Rani et al. have answered yes. The gap is 'can scaffolded friction prevent it, and does trust predict who deskills fastest?'

## Related Work / Landscape
Evidence of AI-induced deskilling is now robust, cross-domain, and—critically—extends to information evaluation with longitudinal AI-withdrawal data.

**Deskilling evidence:** Rani et al. (arXiv 2510.01537, CHI 2026) provide the most directly relevant finding: in a month-long within-subjects study (N=67), AI dialogues about misinformation produced +21% accuracy gains during assisted sessions but −15.3% unassisted accuracy at Week 4 vs. Week 0 (β=−0.077, p<.001), with decline driven entirely by fake item detection. Their study used GPT-4o with Google Search but tested no scaffolding interventions, included no independent control group, and had 36% attrition (105→67). The 1,222-participant RCT (arXiv 2604.04721) shows immediate performance degradation after AI exposure in arithmetic and reading comprehension. Shen & Tamkin (arXiv 2601.20245) demonstrate 17% lower quiz scores in AI-assisted programming learners (N=52, d=0.738) and identify six interaction patterns—three cognitively engaged patterns that preserve learning, suggesting that engagement-preserving interventions could work. Clinical trials show 6-point adenoma detection drops after AI removal (Budzyń et al., 2025). Neuroimaging reveals lower brain activation in AI-assisted learners (Kosmyna et al., 2025).

**Theoretical frameworks:** The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) provides a formal dynamic model decomposing AI productivity into skill-independent (α) and skill-complementary (β) channels, proving that rational adoption can produce steady-state loss and identifying five deployment regimes—but offers no empirical validation and notes that 'draft-then-revise' workflows (analogous to our mandatory independent attempt) should preserve the skill-complementary channel. The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction via multi-agent cognitive forcing functions but provides zero empirical validation. The Frontiers 'Deskilling dilemma' framework (2026) distinguishes cognitive, diagnostic, and moral deskilling as an outcome from overreliance as a behavior—a distinction no intervention study has operationalized.

**Scaffolding and friction interventions:** Althea (arXiv 2602.11161, N=963) compares three scaffolding modes for fact-checking across immediate and 10-day follow-up, finding self-directed search yields strongest persistence—but measures improvement durability during/after scaffolded interaction, not deskilling prevention after AI removal, has no unrestricted-AI condition, and explicitly calls for longer-term studies. Adjust for Trust (arXiv 2502.13321, IUI 2026, Srinivasan & Thomason) tests trust-adaptive interventions—supporting explanations at low trust, counter-explanations at high trust, and 10-second forced pauses at high trust—achieving up to 38% reduction in inappropriate reliance across science questions (N=30/condition) and medical diagnosis (N=20/condition), but measures only within-session reliance decisions across a 30-problem sequence, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment at a Fortune 500 company, finding behavioral scaffolding actually reduced quality while cognitive scaffolding helped only top performers—but measure single-session document quality with no longitudinal follow-up. Critical Inker (arXiv 2604.07167) scaffolds critical thinking in AI-assisted writing through Socratic questioning but reports only a small-scale pilot. The CFF literature (Buçinca et al., CSCW 2021; Ghosh et al., 2026) measures immediate reliance decisions, not longitudinal skill retention. Berger et al. (arXiv 2603.29866) show that eliciting independent judgment before AI input boosts accuracy across 10 datasets but do not measure whether this protects skills over time. The overreliance measurement paper (arXiv 2509.08010) identifies three gaps in current overreliance measurement, arguing that LLMs' conversational style creates unique trust dynamics.

**The precise gap:** Rani et al. establish that AI-assisted information evaluation causes deskilling after AI withdrawal. Our study tests whether scaffolded friction can prevent it. This is the direct next step their paper calls for.

## Approach
We conduct a pre-registered, between-subjects online experiment (N≈480, recruited via Prolific) with four conditions across three phases, using an AI-withdrawal design that directly tests whether scaffolded friction prevents the deskilling that Rani et al. (CHI 2026) documented in information evaluation.

**Conditions (4):** (1) No-AI control (participants complete all tasks independently—addressing Rani et al.'s lack of a control group), (2) Unrestricted LLM access (standard chatbot interaction using Qwen 3.5 27B via API for open-source reproducibility—replicating the deskilling-inducing condition), (3) Scaffolded friction (mandatory independent attempt with confidence rating before AI output, incremental hint system, self-explanation gates—operationalizing the untested Cognitive Agency Surrender framework and the Augmentation Trap's 'draft-then-revise' workflow design lever), (4) Althea-style exploratory scaffolding (modular evidence exploration without verdict delivery—to directly compare friction-based deskilling prevention against the epistemic-agency scaffolding strategy that Althea found most persistent for improvement). This fourth condition enables a head-to-head comparison of two scaffolding philosophies: friction-as-deskilling-prevention vs. agency-preserving-exploration.

**Phases (3):** Phase 1—Baseline skills assessment: all participants complete information evaluation tasks independently (claim verification adapted from AVeriTeC/FEVER, multi-source synthesis, argument quality evaluation) plus trust disposition measures (Jian et al. trust scale adapted for AI). Phase 2—AI-assisted treatment (30 min): participants work on parallel-form tasks with their assigned AI condition; trust in AI is measured again post-treatment. Phase 3—Post-AI independent assessment: participants complete held-out test items WITHOUT any AI access at three timepoints: immediate (same session), 1-week delayed, and 4-week delayed.

**Primary outcome:** Skill retention, operationalized as the pre-to-post accuracy delta on held-out test items completed independently after AI removal. The three post-withdrawal timepoints (immediate, 1-week, 4-week) yield a skill decay curve per condition. This directly extends Rani et al.'s observation of 15.3% decline (no interventions, N=67, within-subjects) to an interventional, between-subjects design at 7× sample size with a control group.

**Secondary outcomes:** (a) Persistence: time-on-task before abandonment at each post-test; (b) Trust calibration: confidence-accuracy alignment and trust scale changes; (c) Trust-as-moderator: whether pre-treatment trust disposition and within-treatment trust change predict steeper deskilling in the unrestricted-AI condition—extending Adjust for Trust's finding that trust predicts within-session reliance to test whether it also predicts cross-session skill decay; (d) Cognitive engagement: Cognitive Reflection Test and NASA-TLX; (e) Strategy transfer: verification strategy diversity at each timepoint.

**Key distinction from Rani et al. (CHI 2026):** Rani et al. demonstrate that deskilling occurs in information evaluation after AI withdrawal (15.3% decline, N=67, no interventions, no control group, within-subjects). We test whether scaffolded friction can prevent this degradation (N≈480, 4 conditions including no-AI control, between-subjects, with scaffolding interventions). Their study answers 'does AI cause deskilling in information evaluation?' Our study answers 'can we prevent it?' Their limitations—no interventions, no control group, small sample, within-subjects confounds—are precisely what our design addresses.

**Key distinction from Althea:** Althea compares scaffolding modes along an epistemic agency spectrum and measures improvement persistence (post-task → 10-day follow-up). We compare scaffolding modes along a friction spectrum against an unrestricted-AI deskilling baseline and measure skill degradation after AI withdrawal (pre-AI baseline → post-AI independent performance) across a 4-week decay curve. Althea asks 'which scaffolding mode best improves reasoning?' We ask 'which scaffolding mode best prevents the reasoning degradation that unrestricted AI induces?'

**Key distinction from Adjust for Trust (IUI 2026):** Srinivasan & Thomason test trust-adaptive interventions (explanations, forced pauses) to reduce inappropriate reliance during a 30-problem within-session sequence. We measure whether friction during AI-assisted work protects independent capability after AI is permanently removed. They optimize within-session reliance decisions; we optimize cross-session skill retention. We also adopt their insight that trust level predicts reliance behavior—but test whether it similarly predicts the severity of post-withdrawal skill decay.

**Key distinction from CFF literature:** CFF studies measure within-session reliance behavior (agreement rate with AI suggestions). We measure cross-session capability change (can you still do this independently after AI is gone?). This operationalizes the Frontiers framework's distinction between overreliance-as-behavior and deskilling-as-outcome.

**Key distinction from the deskilling RCT (2604.04721):** They demonstrate the problem (AI use degrades independent performance in arithmetic/reading). We test a solution (scaffolded friction prevents that degradation) in information evaluation and add a trust moderation dimension.

**Key distinction from the Augmentation Trap (2604.03501):** Caosun & Aral provide a formal model predicting that training rate and workflow design can mitigate AI-induced skill decay but offer no empirical validation. Our scaffolded friction conditions operationalize their theoretical mitigation levers—mandatory independent attempts preserve the skill-complementary (β) channel, and self-explanation gates increase the effective learning rate (κ)—providing the first empirical test of interventions aligned with their formal framework.

**Model choice:** Qwen 3.5 27B, the largest dense model in the Qwen 3.5 series, served via API (OpenRouter: ~$0.14/M input, $1/M output tokens) or self-hosted on a single H100 via vLLM for consistency. This model is selected for: open-source reproducibility, sufficient capability for realistic AI assistance in information evaluation, and cost efficiency.

## Inspiration
Field guide gap: cognitive deskilling identified as key risk (P3, P13, P14) but measurement and intervention are absent from NLP/HCI research. Critical catalyst: Rani et al. (CHI 2026) demonstrate the problem—15.3% skill degradation after AI withdrawal in misinformation detection—and their future work section explicitly calls for scaffolding-based solutions, which is exactly what we propose. Pattern transfer: the pre/during/post withdrawal design from the deskilling RCT (2604.04721) + the scaffolding mode comparison logic from Althea + the CFF intervention toolkit (P15-P17) reframed for longitudinal skill retention + the independent-judgment-first approach from Berger et al. (2603.29866) + the trust-adaptive intervention logic from Adjust for Trust (2502.13321) reframed for cross-session skill protection + the formal skill-decay dynamics from the Augmentation Trap (2604.03501) operationalized empirically. Novel angle: trust as a moderator of deskilling speed, connecting the deskilling prevention contribution to the trust calibration literature—building on Adjust for Trust's finding that trust level predicts reliance behavior to ask whether it also predicts skill decay severity.

## Key References
- Dialogues with AI Reduce Beliefs in Misinformation but Build No Lasting Discernment Skills (arXiv 2510.01537, Rani et al., CHI 2026, N=67) — most directly relevant concurrent work: demonstrates 15.3% accuracy decline after 4-week AI withdrawal in misinformation detection using within-subjects design with GPT-4o dialogues; tested no interventions, no control group; their future work explicitly calls for scaffolding-based solutions, which is exactly what we propose
- Althea: Scaffolding Epistemic Agency for Durable Fact-Checking (arXiv 2602.11161, Churina et al., 2026, N=963) — closest scaffolding concurrent work; compares scaffolding modes for fact-checking improvement persistence but uses no AI-withdrawal design, no unrestricted-AI condition, and authors acknowledge design measures 'short-term retention of reasoning patterns, not durable skill acquisition'
- AI Assistance Reduces Persistence and Hurts Independent Performance (arXiv 2604.04721, under review 2026) — establishes the deskilling problem with causal evidence from a 1,222-participant RCT
- The Augmentation Trap: AI Productivity and the Cost of Cognitive Offloading (arXiv 2604.03501, Caosun & Aral, 2026) — formal dynamic model proving rational AI adoption can produce steady-state skill loss; identifies training rate (κ) and workflow design (β) as mitigation levers our interventions operationalize; purely theoretical, no empirical validation
- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (arXiv 2502.13321, Srinivasan & Thomason, IUI 2026) — tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance; measures within-session reliance only, not cross-session skill retention; supports trust-as-moderator dimension
- Cognitive Agency Surrender: Defending Epistemic Sovereignty via Scaffolded AI Friction (arXiv 2603.21735, 2026) — theoretical framework we operationalize empirically
- Beyond AI advice—independent aggregation boosts human–AI accuracy (arXiv 2603.29866, Berger et al., 2026) — demonstrates independent-judgment-first approach boosts accuracy across 10 datasets; conceptually parallel to our mandatory independent attempt, but measures immediate accuracy not skill retention
- Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing (arXiv 2604.08678, Farach et al., 2026, N=388) — field experiment comparing behavioral vs. cognitive scaffolding; found behavioral scaffolding reduced quality while cognitive scaffolding helped only top performers; single-session measurement, no longitudinal follow-up
- How AI Impacts Skill Formation (arXiv 2601.20245, Shen & Tamkin, 2026, N=52) — RCT evidence of 17% deskilling in programming with AI (d=0.738); identifies cognitively-engaged interaction patterns that preserve learning; programming domain only, single-session, no interventions tested
- Critical Inker: Scaffolding Critical Thinking in AI-Assisted Writing Through Socratic Questioning (arXiv 2604.07167, Hugenroth et al., 2026) — Socratic scaffolding for writing; small pilot, different domain
- Brainrot: Deskilling and Addiction are Overlooked AI Risks (FAccT 2026, Chalkidis & Søgaard)
- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making (CSCW 2021, Buçinca et al.)
- Endoscopist deskilling risk after exposure to AI in colonoscopy (Budzyń et al., Lancet Gastroenterol Hepatol 2025)
- Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant (Kosmyna et al., 2025)
- Mitigating Epistemic Debt in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts (arXiv 2602.20206, 2026) — scaffolded friction in programming with AI-blackout test; different domain, no longitudinal follow-up
- Deskilling dilemma: brain over automation (Frontiers in Medicine, 2026) — provides cognitive/diagnostic/moral deskilling typology and distinguishes deskilling-as-outcome from overreliance-as-behavior
- Measuring and mitigating overreliance is necessary for building human-compatible AI (arXiv 2509.08010) — identifies gaps in overreliance measurement and LLM-specific trust dynamics
- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, Ghosh et al., 2026)
- From Algorithm Aversion to AI Dependence: Deskilling, Upskilling, and Emerging Addictions in the GenAI Age (Kim, Consumer Psychology Review 2026)
- Generative AI Reliance and Executive Function Attenuation (Baldeo, Technology Mind & Behavior 2026)
- Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)

## Resource Estimate
- **manual**: {'gpu_hours': '40–60 (self-hosting Qwen 3.5 27B on H100 for real-time experiment serving; or ~$50–80 via API with no self-hosting needed)', 'timeline': '5 months (1 mo platform design + task creation, 3–4 weeks IRB approval, 2 weeks pilot N=80, 6 weeks main data collection in overlapping waves to accommodate 4-week follow-ups, 5 weeks analysis + writing)', 'estimated_gpu_cost': '$80–120 (H100 at ~$2/hr) or $50–80 via OpenRouter API'}
- **human_in_loop**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4.5 months (Claude accelerates platform dev, task item generation via IRT-calibrated stimulus pools, statistical analysis scripting, and manuscript drafting)', 'claude_api_cost': '$350 (platform scaffolding, stimulus generation, R/Python analysis pipelines, growth-curve modeling code, manuscript drafting)', 'estimated_gpu_cost': '$80–120 or $50–80 via API'}
- **auto_research**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4 months (automated pilot analysis, adaptive task calibration, parallel manuscript drafting)', 'claude_api_cost': '$900 (end-to-end experimental platform generation, automated IRT-based item analysis, growth-curve model specification, full statistical report generation, iterative manuscript revision)', 'estimated_gpu_cost': '$80–120 or $50–80 via API', 'speed_bottleneck': 'IRB approval (3–6 weeks, irreducible) and the 4-week delayed follow-up window; participant compensation dominates total cost: N=480 initial session (40 min at $12/hr = $3,840) + 33.3% Prolific academic fee ($1,279) + 1-week follow-up (~385 retained, 20 min, $1,540 + $513 fee) + 4-week follow-up (~310 retained, 20 min, $1,240 + $413 fee) + completion bonuses (~$700 + $233 fee) = ~$9,760 total participant costs'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a35ae121-7b8c-49fd-913d-bd7d578f0163",
  "type": "user",
  "uuid": "1d0d33a0-c6bc-4c45-a5ff-ff962801c0e9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:45:57.101Z_

```json
{
  "parentUuid": "1d0d33a0-c6bc-4c45-a5ff-ff962801c0e9",
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
  "uuid": "68a1fe15-3c3f-43c7-ac6d-faa368ee14ae",
  "timestamp": "2026-05-19T18:45:57.101Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:45:57.101Z_

```json
{
  "parentUuid": "68a1fe15-3c3f-43c7-ac6d-faa368ee14ae",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ba4a9e5-faf1-4390-bb56-428b393518f3",
  "timestamp": "2026-05-19T18:45:57.101Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "5ba4a9e5-faf1-4390-bb56-428b393518f3",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Prevent AI-induced skill decay through scaffolded friction",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:46:24.373Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three reviewer assessments and synthesize them as the Meta Judge.

Let me identify the key patterns:

**Reviewer 1**: 
- CoRL mismatch: fatal (0% for CoRL)
- If CHI: [25%-35%] median 30%
- Novelty: 弱-中
- Significance: 中
- Related Work: 强
- Main risks: "Predictable outcome", "Combination ≠ Contribution"


- Reviewers 2 and 3 largely align with this assessment, both seeing fatal CoRL mismatches (1-3% range) and similar CHI/CSCW acceptance probabilities around 28-30%. All three identify medium novelty and significance with strong related work coverage. The consistent concern across reviewers is that this reads as a natural extension rather than a substantive contribution, with the venue mismatch being the primary barrier to acceptance. The key insight is that reviewers are remarkably aligned on the core issues: the venue mismatch is fatal, the experimental design feels predictable rather than novel, and several methodological concerns recur across all three evaluations—the treatment duration might be insufficient, the trust mechanism lacks validation, and the alternative explanation (forgetting curve) isn't adequately ruled out. The minor divergences are just individual observations that don't shift the overall assessment. Looking at the implementation feasibility, all three reference the proposal's cost breakdown, which shows the experiment is technically doable within the stated timeline and budget, though the participant costs are the main driver.

For the final probability, the three reviewers converge on essentially the same conclusion for CoRL 2026—this is a desk reject with near-unanimous confidence. The median sits around 1% with minimal variance, reflecting how decisively the venue mismatch and conceptual concerns eliminate this paper from consideration at a robotics conference. If this were reframed for a human-computer interaction venue like CHI or CSCW, the outlook would shift dramatically to around 28%, but that's not the task at hand.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba4a9e5-faf1-4390-bb56-428b393518f3",
  "isSidechain": false,
  "requestId": "req_011CbCRYSjFmwHG7aVVgDeoS",
  "type": "assistant",
  "uuid": "e33de8b1-5d74-42fa-a26b-29d9fb7e0e73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBPAYJrcuSZYyUGPuuiB4K",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19929,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3720,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 19929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19929
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

_source line 9 · 2026-05-19T18:47:23.531Z_

【阶段】: Meta Judge
【三次中位】: [30%, 28%, 30%]（假设合适 HCI 会议）  std≈1.2%；CoRL 投稿中位 [1%, 1%, 1%] std≈0.5%

【共识维度】（3/3 审稿人一致）:
- **会议匹配：致命** — 三位审稿人均独立判定 proposal 与 CoRL 2026 完全不匹配（纯 HCI/认知科学 vs. 机器人学习），将被 desk reject。CoRL CFP 原文 "submissions without a robotics focus will be returned without review" 被三人同时引用。
- **Novelty：弱-中** — 三人一致认为核心贡献是"已有组件的实验设计组合"（CFF + AI-withdrawal + longitudinal + trust moderation），非概念层面创新。R1 明确给弱-中，R2 给中，R3 给中偏弱。共识是：experimental design novelty ≠ conceptual novelty。
- **Significance：中** — 三人一致认为研究问题重要（deskilling 是 2025-2026 热点），但贡献形态受限于 30 分钟 Prolific 实验的生态效度和任务域可推广性。
- **Related Work：强** — 三人一致认为这是 proposal 最突出的优势。文献覆盖全面、引用准确、差异化定位清晰。
- **"Predictable outcome" 风险** — 三人均指出：若 scaffolding 有效→"I would have guessed this"；若无效→treatment 不够强或难发表。无论哪个方向，insight 增量有限。
- **Trivial alternative 威胁** — 三人均指出 mandatory independent attempt alone（Berger et al. 2603.29866 已验证）可能捕获大部分效果，削弱 incremental hints / self-explanation gates 的增量价值。
- **30 分钟 treatment 诱导 deskilling 的假设风险** — 三人均质疑：Rani et al. 用 4 周多次 session，10 分钟 RCT 是算术/阅读理解（低复杂度），30 分钟单次 session 在信息评估这一复杂认知任务上能否产生可检测的退化。
- **Trust 跨 session moderator 假设未验证** — 三人均指出 Adjust for Trust 仅验证了 trust → within-session reliance，trust → cross-session skill decay rate 是未经支撑的推断跳跃。

【异常维度】（仅 1 人提及，降权处理）:
- R1：缺少"AI-free periods"实践引用（新加坡医疗系统）——轻微遗漏，不影响整体
- R2：Qwen 3.5 27B 与 GPT-4o 能力差异可能影响认知卸载程度——合理关切，但非致命
- R3：人类遗忘曲线可能在 4 周内抹平初始差异——有道理但属于实验结果的经验性不确定性

【最终概率】: [0% - 2%] 中位 1%（投稿 CoRL 2026）；[24% - 33%] 中位 28%（若改投 CHI/CSCW 等合适 HCI 会议）

【一致性】: 高（三份评审在所有核心维度上高度收敛，CoRL 概率 std≈0.5%，HCI 概率 std≈1.2%）

【综合理由】:

**CoRL 概率（中位 1%）**：三位审稿人独立、一致地判定这是投稿方向的致命错误。Proposal 是纯 HCI/认知科学人因实验（Prolific 在线被试、误信息检测、scaffolded friction、trust 量表），与 CoRL 的征稿范围（robot perception, manipulation, locomotion, RL for physical robots, robot foundation models）零交集。这不是 idea 质量问题——是 desk review 阶段会被直接退回的硬性不匹配。三人均引用了 CoRL CFP 的原文作为依据。此判断无分歧，无需降权或加宽区间。

**HCI 会议概率（中位 28%）**：三份评审的 HCI 概率估计极度收敛（30%, 28%, 30%），反映出对 idea 质量的一致认知。综合逻辑如下：

1. **Related Work 的强势确保了下限**（≥24%）。三人一致认为文献覆盖是 proposal 最大优势——覆盖全面、描述准确、差异化清晰。这保证了 proposal 不会因"忽略关键前序工作"或"定位不清"被拒，为概率提供了坚实的底部。

2. **Novelty 的弱-中限制了上限**（≤33%）。三人一致认为核心贡献是"已有组件的实验设计组合"——CFF（Buçinca et al. 2021）、AI withdrawal（Rani et al.）、longitudinal（已有多项 4 周研究）、trust moderation（Adjust for Trust）——每个组件单独不新，组合产生的是 execution novelty 而非 conceptual novelty。核心假设"强制认知参与可防止退化"是 desirable difficulties 文献的直接推论，positive 结果不具 surprise value。这个上限即使实验设计再完美也无法突破。

3. **取中位偏严**。R2 的 28% 是三人中最低的，其理由（"Rani et al. future work 的直接执行"、"confirmatory study"）是三人共识的核心化表达。鉴于高一致性 + 宁缺毋滥原则，最终中位取 28% 而非 30%。

4. **异常维度处理**。R2 提出的 Qwen 3.5 27B 与 GPT-4o 能力差异是一个合理但非致命的操作性关切——如果 Qwen 产生的 AI 辅助不够"逼真"，可能削弱 deskilling 效应的诱导强度，这会加剧"30 分钟 treatment 是否足够"的基础性风险。此点与三人共识的 treatment duration 风险方向一致，已被隐含纳入区间的宽度中。R3 提出的遗忘曲线抹平效应属于实验结果的自然不确定性，不额外调整概率。

【建议】: KILL（投 CoRL 2026）/ 边缘（若改投 CHI 2027 或 CSCW 2027）

具体建议：
- **如果必须投 CoRL 2026**：立即止损，不进入迭代。0% 的 venue match 无法通过任何 idea 优化补救。
- **如果可以改投 CHI/CSCW**：idea 质量处于边缘区间（28%），值得进入迭代优化流程。主要优化方向应集中在提升 Novelty（从弱-中到中或中+），因为 Related Work 已经很强，实验设计已经规范，瓶颈在 idea 的概念新颖性和 surprise potential。

【实施评估】:
- **计算资源**: 极低。Qwen 3.5 27B 自托管需 1 张 H100（40-60 GPU-hours，约 $80-120）；或通过 OpenRouter API 调用约 $50-80。无大规模训练需求。
- **数据需求**: 无需预先存在的大规模数据集。实验刺激材料（claim verification items）可基于 AVeriTeC/FEVER 适配构建。Prolific 在线招募 N≈480 被试。
- **人工介入**: 较高。需要 IRB 审批（3-6 周，不可压缩）；需设计并校准任务刺激（IRT 校准）；需 pilot study（N≈80）；需管理 4 周纵向随访的被试留存（预期 ~35% 流失）。
- **训练需求**: 无模型训练。使用现成的 Qwen 3.5 27B，仅做推理 serving。
- **新 Benchmark**: 无需构建新 benchmark。实验刺激可基于已有 fact-checking 数据集适配。
- **预估周期**: 4-5 个月（1 个月平台搭建 + 任务设计 → 3-4 周 IRB → 2 周 pilot → 6 周主实验含 4 周随访 → 5 周分析写作）。主要成本瓶颈是被试补偿（约 $9,760）和 4 周纵向随访的不可压缩等待时间。
- **总预算估计**: ~$10,000-11,000（被试补偿 ~$9,760 + 计算 ~$80-120 + 杂项），如果用 Claude API 辅助开发/分析额外 $350-900。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e33de8b1-5d74-42fa-a26b-29d9fb7e0e73",
  "isSidechain": false,
  "requestId": "req_011CbCRYSjFmwHG7aVVgDeoS",
  "type": "assistant",
  "uuid": "7ef64436-2e35-4c78-b578-e57ccce96c55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBPAYJrcuSZYyUGPuuiB4K",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19929,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3720,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 19929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19929
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research to provide a thorough evaluatio…",
  "leafUuid": "7ef64436-2e35-4c78-b578-e57ccce96c55",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Prevent AI-induced skill decay through scaffolded friction",
  "sessionId": "5e323eb2-fbca-4698-8ef4-dbe6db083e75"
}
```

---
