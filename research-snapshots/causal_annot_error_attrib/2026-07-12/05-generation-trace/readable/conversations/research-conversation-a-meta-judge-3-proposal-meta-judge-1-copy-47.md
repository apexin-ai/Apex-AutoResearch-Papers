# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/917b0c4a-fc44-4277-9e81-b3341d570fb4.jsonl`
- **Structured JSON:** [`dff411321d00b1f3536a.json`](../../sessions/df/dff411321d00b1f3536a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:01:17.377Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:01:17.377Z",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\n调研完成。我现在可以给出完整的入口评审。这里有一个 **极其关键的前置问题** 需要首先指出。\n\n---\n\n```\n【阶段】: Triage\n\n==========================================================================\n⚠️ 致命问题：投稿目标 CoRL 2026 与 proposal 内容完全不匹配\n==========================================================================\n\nCoRL (Conference on Robot Learning) 的核心议题包括：\n- 模仿学习、强化学习（用于机器人控制）\n- Sim-to-real transfer\n- 机器人感知、操控、移动\n- 机器人基础模型\n- 机器人硬件与系统\n- 会议明确鼓励\"real-robot experiments\"\n\n本 proposal 的内容是：\n- AI 辅助信息评估中的认知去技能化（misinformation detection）\n- 基于 Prolific 的人类被试实验（N≈480）\n- 脚手架式认知摩擦干预\n- 信任校准与技能衰退曲线\n- 纯 HCI / 认知心理学方法论，无任何机器人相关成分\n\n这是一个 100% 的 venue mismatch。该论文在 CoRL 会被 desk-reject，\n不会进入审稿流程。\n\n正确的投稿目标应为：CHI、CSCW、FAccT、AAAI HCOMP、或 IUI。\n==========================================================================\n\n以下评估基于 idea 本身的学术质量（假设投稿到正确的 HCI 会议），\n以便为后续流程提供参考。但 CoRL 中稿概率为 ~0%。\n\n==========================================================================\n\n【领域调研】:\n\n- [Rani et al., \"Dialogues with AI Reduce Beliefs in Misinformation \n  but Build No Lasting Discernment Skills\"](https://arxiv.org/abs/2510.01537) \n  (CHI 2026): 最直接的前序工作。N=67 被试在 AI 辅助后 4 周出现 15.3% \n  准确率下降。无干预、无对照组、within-subjects 设计。明确呼吁未来做\n  scaffolding 干预研究。本 proposal 是对该呼吁的直接回应。✅ 论文真实存在，\n  描述准确。\n\n- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161) \n  (2026, N=963): 比较三种脚手架模式（Exploratory/Summary/Self-search）的\n  fact-checking 效果，发现 self-directed search 的改善最持久（10 天随访）。\n  但无 AI-withdrawal 设计、无 unrestricted-AI 条件、无 pre-AI baseline。\n  作者承认仅测量\"short-term retention\"。✅ 论文真实，描述准确。\n\n- [\"AI Assistance Reduces Persistence and Hurts Independent Performance\"](https://arxiv.org/abs/2604.04721) \n  (2026, N=1222 RCT): 因果证据表明 AI 使用降低独立表现（arithmetic, \n  reading comprehension）。仅测 within-session，无干预测试。✅ 真实存在。\n\n- [The Augmentation Trap](https://arxiv.org/abs/2604.03501) \n  (Caosun & Aral, 2026): 形式化动态模型，证明理性 AI 采用仍可导致\n  稳态技能损失。纯理论，无实证验证。✅ 真实，描述准确。\n\n- [Adjust for Trust](https://arxiv.org/abs/2502.13321) \n  (Srinivasan & Thomason, IUI 2026): 信任自适应干预减少不当依赖达 38%。\n  仅测 within-session reliance，非 cross-session skill retention。\n  ✅ 真实，描述准确。\n\n- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735) \n  (2026): 提出 scaffolded AI friction 的理论框架但无实证验证。✅ 真实。\n\n- [Farach et al.](https://arxiv.org/abs/2604.08678) \n  (2026, N=388): behavioral vs cognitive scaffolding 的 field experiment。\n  单次测量，无纵向随访。✅ 真实。\n\n- [Metacognitive Scripts for Programming](https://arxiv.org/abs/2602.20206) \n  (2026): 编程领域的脚手架摩擦 + AI blackout test（77% vs 39% 失败率）。\n  不同领域，无纵向随访。✅ 真实。\n\n- Budzyń et al. (Lancet Gastroenterol Hepatol 2025): 临床领域 AI 撤除后\n  腺瘤检出率下降 6 个百分点。✅ 真实。\n\n- 调研总结: AI 辅助导致认知去技能化在 2025-2026 年已成为 cross-domain 的\n  确认事实（信息评估、编程、数学、临床医学）。现有干预研究（CFF、Althea、\n  Adjust for Trust）均仅测量 within-session 或 short-term 效果，\n  尚无研究测试干预能否在 AI 永久撤除后保护独立能力。\n  本 proposal 精准定位于这一空缺。\n\n\n【Trivial Alternative 检验】:\n\n存在一个显著的 trivial alternative 威胁：\n\"mandatory independent attempt first\"（强制先独立尝试）本身就可能\n是防止去技能化的充分条件。Berger et al. (2603.29866) 已证明 independent \njudgment first 在 10 个数据集上提升准确率。如果仅\"先独立做一遍\"就足以\n阻止大部分去技能化，那么 proposal 中精心设计的 incremental hints、\nself-explanation gates 等复杂脚手架的增量价值可能很小。\n\nProposal 的 4 条件设计部分缓解了这一问题（因为可以通过对比 Condition 3 \nvs 更简单的变体来分离贡献），但核心风险是：最终发现 scaffolded friction \n≈ \"just try it yourself first\"，这会使 contribution 大打折扣。\n\n增量价值的关键在于：(a) scaffolded friction 是否比 mere independent \nattempt 在 4-week 衰退曲线上有显著额外保护效果，(b) trust moderation \n维度是否提供有意义的 mechanistic insight。如果两者都不成立，本研究退化\n为\"控制实验验证了一个符合直觉的结论\"。\n\n\n【前提假设检验】:\n\n核心逻辑链中有两个关键未验证假设：\n\n1. **30 分钟 AI 辅助治疗足以在 unrestricted 条件下诱导可测量的去技能化。**\n   Rani et al. 使用了 1 个月的纵向交互，1222-RCT 使用了 10 分钟但在\n   arithmetic/reading（更简单的认知任务）。信息评估任务（claim verification、\n   multi-source synthesis）的认知复杂度更高，30 分钟的单次暴露是否足以\n   产生效果是完全未知的。如果 unrestricted 条件未能产生显著去技能化，\n   整个实验的 contrast 失效——scaffolding 无从\"prevent\"一个未发生的现象。\n\n2. **Between-subjects 设计下，baseline 个体差异的噪声是否会掩盖\n   condition 间的差异。** Rani et al. 使用 within-subjects 设计\n   （自身对照）才检测到 15.3% 的效果。Between-subjects 设计在 N≈120/条件\n   下检测类似大小的效应需要较大 power——如果实际效应比 Rani 的小\n   （因为暴露时间短得多），可能出现 underpowered 的问题。\n\n\n【3 维度打分】:\n\n1. Novelty: 【中】\n   — 核心贡献是一个实验设计层面的\"first combination\"：将已有的脚手架\n     干预工具（CFF, Buçinca et al. 2021; Althea 2026）应用到一个新验证\n     的问题（AI 撤除后去技能化, Rani et al. 2026）上，加入纵向随访\n     和信任调节维度。每个组件（scaffolded friction、AI-withdrawal design、\n     trust-as-moderator）在之前的工作中都已出现，novelty 来自组合。\n   — 组合式 novelty 在 HCI 中是可接受的，但不构成强 novelty。\n     审稿人可能会评价为\"well-motivated follow-up study\"而非\n     \"conceptual advance\"。\n   — Adjust for Trust (IUI 2026) 已经测试了 trust-adaptive 干预；\n     Althea (2026) 已经测试了多种脚手架模式的持久性；\n     Berger et al. (2026) 已经测试了 independent-judgment-first。\n     本 proposal 的核心 delta 是\"把这些放到 AI-withdrawal + \n     longitudinal 框架里测\"，这是重要的实证推进，但概念层面的 novelty \n     有限。\n\n2. Significance: 【强】\n   — 研究问题的重要性和时效性极高。AI 去技能化是 2025-2026 年跨学科\n     的核心关切，且从问题识别到干预验证是自然的、急需的研究进展方向。\n   — Rani et al. 的 explicit call for exactly this study 表明该领域\n     认可这一空缺。\n   — 如果 scaffolded friction 确实能防止去技能化，这一发现对 AI 系统\n     设计（educational AI、AI assistants、clinical AI）有广泛的实践\n     指导价值。\n   — 但如前所述，positive result（\"scaffolding helps\"）并不 surprising。\n     审稿人不太可能说\"I would not have guessed this\"。Negative result\n     （\"scaffolding doesn't help\"）反而更有学术冲击力。\n\n3. Related Work: 【强】\n   — Related work 的覆盖异常全面。所有关键论文均真实存在，描述准确，\n     gap 分析精确。每篇论文的局限性（Rani: 无干预/无对照/小样本；\n     Althea: 无 AI-withdrawal；Adjust for Trust: 仅 within-session；\n     CFF: 仅 reliance behavior）都被正确识别并用于论证 gap。\n   — 差异化定位清晰：对每个关键竞争工作（Rani, Althea, Adjust for Trust, \n     CFF, Augmentation Trap, 1222-RCT）都有专门的\"Key distinction\"段落。\n   — 在 HCI 审稿标准下，这一水平的 related work 分析属于优秀。\n\n\n【概率估计】（假设投稿到正确 venue，如 CHI 2027）: \n[25% - 38%] 中位 30%\n\n【概率估计】（投稿 CoRL 2026）: \n~0%（desk reject，venue 完全不匹配）\n\n【估计理由】:\n假设正确 venue (CHI/CSCW)：\nSignificance 维度强（研究问题重要且 timely），Related Work 强（覆盖\n全面、定位清晰），但 Novelty 处于中位——核心贡献是\"组合式 first \nempirical test\"，每个组件都已在先前工作中出现。这在 CHI 中可以接受\n但不突出。关键限制上界的是两个因素：(a) Trivial alternative 威胁——\n\"independent attempt first\"可能已足够，复杂脚手架的增量价值存疑；\n(b) positive result 不 surprising——审稿人会觉得\"scaffolding prevents \ndeskilling\"符合直觉，降低了论文的 intellectual excitement。\n这是一个 well-executed follow-up study 的 profile，不是一个 \nparadigm-shifting contribution 的 profile。\n\n对于 CoRL：本 proposal 与 Conference on Robot Learning 的 scope \n完全不相交。信息评估、misinformation detection、Prolific 人类被试实验\n均不在 CoRL 的审稿范围内。无论 idea 质量如何，CoRL 中稿概率为零。\n\n【主要风险】:\n1. **致命 venue mismatch**: CoRL 是 Conference on Robot Learning，\n   本 proposal 是纯 HCI/cognitive psychology 研究，无任何机器人相关内容。\n   这不是\"borderline\"——是完全不相关的领域。\n\n2. **Trivial alternative 威胁（idea 层面）**: 如果\"强制先独立尝试\"就\n   足以防止大部分去技能化，elaborate scaffolding 的增量贡献可能微不足道，\n   核心 claim 退化为显而易见的结论。\n\n3. **剂量-效应风险（idea 层面）**: 30 分钟的 AI 暴露是否足以在信息评估\n   任务上诱导可测量的去技能化完全未知，如果 unrestricted 条件不能产生\n   基准效应，整个实验设计的 contrast 基础不存在。\n```\n\n---\n\n**总结**: 这个 proposal 在 idea 层面是一个 solid 但非 outstanding 的 HCI 研究——研究问题重要、文献分析到位、gap 真实存在，但 novelty 偏组合式、positive result 不够 surprising。然而，**投稿 CoRL 2026 是一个根本性的方向错误**——CoRL 是机器人学习会议，这篇论文与其 scope 完全不相交，中稿概率本质上为零。建议重新考虑投稿目标（CHI 2027、CSCW 2027、FAccT 2027 等 HCI 会议）。\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n- [Rani et al., CHI 2026](https://arxiv.org/abs/2510.01537)\n- [Althea, 2026](https://arxiv.org/abs/2602.11161)\n- [AI Assistance Reduces Persistence, 2026](https://arxiv.org/abs/2604.04721)\n- [The Augmentation Trap, 2026](https://arxiv.org/abs/2604.03501)\n- [Adjust for Trust, IUI 2026](https://arxiv.org/abs/2502.13321)\n- [Cognitive Agency Surrender, 2026](https://arxiv.org/abs/2603.21735)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\n调研完成。现在我有足够的信息来做客观评估。\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：会议领域匹配】:\n本 proposal 研究的是 AI 辅助信息评估中的认知去技能化（cognitive deskilling）、支架式认知摩擦（scaffolded friction）和信任校准（trust calibration），属于 HCI/认知科学 领域。\nCoRL（Conference on Robot Learning）的核心 scope 是：imitation learning、reinforcement learning for robots、sim-to-real transfer、robot perception、learned manipulation/locomotion、robot foundation models 等。\n本 proposal 与 CoRL 的学科范畴零重叠，投稿 CoRL 大概率会被 desk reject。\n合适的投稿目标应为 CHI、CSCW、FAccT、IUI 等 HCI 会议。\n\n以下评估基于 idea 本身的学术质量（假设投稿至合适的 HCI 会议），但最终概率估计必须反映 CoRL 这个目标会议。\n\n\n【领域调研】:\n- [Rani et al., arXiv 2510.01537] (CHI 2026): 确认真实存在。N=67，within-subjects，AI 辅助误信息检测导致 4 周后 15.3% 准确率下降。无干预、无对照组。Proposal 的描述准确。\n- [Althea, arXiv 2602.11161] (2026, N=963): 确认真实存在。比较三种 scaffolding 模式的 fact-checking 效果，self-directed search 产生最持久改善。无 AI-withdrawal 设计、无 unrestricted-AI 条件。Proposal 描述准确。\n- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026, under review, N=1222): 确认真实存在。RCT 证据表明 AI 辅助降低独立表现和坚持度。在算术和阅读理解任务中，仅 10 分钟 AI 使用即导致退化。\n- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, 2026): 确认真实存在。纯理论形式化模型，无实证验证。Proposal 描述准确。\n- [Adjust for Trust, arXiv 2502.13321] (IUI 2026): 确认真实存在。测试信任自适应干预（forced pauses 等），降低 38% 不当依赖，但仅测量 within-session 依赖决策。\n- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 确认真实存在。理论框架，提出 scaffolded AI friction 概念，但零实证验证。\n- [Farach et al., arXiv 2604.08678] (2026, N=388): 行为 vs. 认知 scaffolding 的 field experiment，但仅 single-session 测量。\n- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程技能形成中 17% deskilling，单次 session，无干预。\n- [Metacognitive scripts, arXiv 2602.20206] (2026): 编程领域的 scaffolded friction + AI-blackout 测试（77% vs 39% failure），但无纵向跟踪。\n- 调研总结: AI deskilling 在 2025-2026 成为爆发性热点，多篇高影响力论文从不同角度（因果证据、形式模型、神经影像、临床数据）确认了问题的存在。但\"scaffolded friction 能否预防 AI withdrawal 后的 deskilling\"这一具体问题确实尚无直接实证回答。然而，该领域属于 HCI/认知科学，与 CoRL 的机器人学习 scope 完全不相关。\n\n\n【Trivial Alternative 检验】:\n存在 trivial alternative 威胁。核心干预\"mandatory independent attempt before AI output\"（先独立判断再看 AI 结果）本质上就是 Berger et al. (2603.29866) 的 \"independent judgment first\" 策略。Berger et al. 已在 10 个数据集上展示了该策略对即时准确率的提升效果。Proposal 的完整 scaffolding 机制（incremental hints、self-explanation gates）相对于一个简单的\"先自己想，再看 AI\"指令的增量价值不明确。\n\n关键缺陷：4 个实验条件中缺少一个\"minimal friction\"条件（仅要求先独立判断，无 hints/gates），导致无法区分核心效果来自\"要求独立思考\"这个简单操作，还是来自精心设计的 scaffolding 机制。如果仅\"先想后看\"就能防止 deskilling，那 proposal 的 scaffolding 设计就不是 necessary 的。\n\n增量价值的可能辩护：Proposal 可以主张 scaffolding 的各组件（hints、self-explanation gates）会比简单的 \"think first\" 产生更强的防护效果——但这需要实验验证，且当前条件设计无法直接回答这个问题。\n\n\n【前提假设检验】:\n核心 claim 的逻辑链：(1) AI 辅助导致 deskilling [已有实证] → (2) Within-session overreliance 是 deskilling 的机制 [合理但非唯一机制] → (3) 减少 within-session overreliance 的干预（scaffolded friction）能防止 cross-session deskilling [关键跳跃，未经验证] → (4) Trust 调节 deskilling 速度 [探索性假设]\n\n关键未验证环节：\n1. **从 within-session 到 cross-session 的跳跃**：CFF 文献证明 friction 减少 within-session 依赖行为，但\"减少依赖行为\"≠\"保护独立技能\"。可能存在其他机制（如 cognitive offloading 的神经适应、动机变化）使得即使 session 内表现更独立，removal 后仍然 deskill。\n2. **30 分钟处理期的充分性**：Rani et al. 的 deskilling 来自 4 周 AI 交互。2604.04721 的 10 分钟效应来自简单任务（算术、阅读理解）。在信息评估这类复杂任务中，30 分钟是否足以产生可测量的 deskilling 效应？如果 deskilling 效应在 unrestricted-AI 条件中不显著，整个实验就没有待保护的效应。\n3. **Between-subjects 设计下个体差异的噪声**：Rani et al. 的 within-subjects 设计控制了个体差异，但也引入了 order effects。Proposal 用 between-subjects 设计消除了 order effects 但引入了大量个体差异噪声。N≈120/condition 是否足够检测 deskilling 差异？\n\n\n【3 维度打分】:\n  1. Novelty: 弱-中 — Proposal 正确识别了一个 gap（scaffolded friction + AI-withdrawal + longitudinal + trust moderation 的组合），但这本质上是一个\"组合填空\"式贡献。每个组件（deskilling 证据、scaffolding 干预、信任测量、纵向设计）都已在近期文献中存在。核心假设方向（\"让人在用 AI 时多思考，移除 AI 后技能保留更好\"）直觉上显然成立——如果结果是 positive 的，审稿人大概率会说 \"I would have guessed this\"，而非 \"surprising\"。Metacognitive scripts 研究 (2602.20206) 已经在编程领域用 scaffolded friction + AI-blackout 展示了类似逻辑（77% vs 39% failure），本 proposal 相当于将其扩展到信息评估领域并增加纵向跟踪——这是 incremental extension，非概念突破。\n  \n  2. Significance: 中 — AI deskilling 无疑是一个重要且 timely 的研究问题，2025-2026 多篇高影响力论文（Rani et al., The Augmentation Trap, 2604.04721）共同推动了该领域。但本 proposal 的贡献主要在于提供\"scaffolding 有效\"的实证确认（而非提出新概念或新范式）。如果 positive result 出现，它验证了已有理论预测（Cognitive Agency Surrender 框架、Augmentation Trap 的 κ 和 β 杠杆）。对领域的影响是\"确认性的\"而非\"开创性的\"。Trust-as-moderator 维度是一个有趣的 secondary contribution，但作为探索性分析，其分量有限。\n  \n  3. Related Work: 强 — 这是 Proposal 最突出的优点。文献覆盖极其全面（17+ 篇核心引用），每篇论文的描述经核实均准确。与每项先行工作的差异化定位通过 6 个 \"Key distinction from X\" 段落清晰阐述。Gap 的界定精确且有防御力。几乎可以作为 deskilling+scaffolding 文献的 mini survey。\n\n\n【概率估计】: 0-2%（CoRL 2026），25-35% 中位 30%（如投稿 CHI/CSCW 等合适会议）\n\n【估计理由】: \nCoRL 维度：本 proposal 研究的是 HCI/认知科学问题（AI 辅助信息评估中的 cognitive deskilling prevention），与 CoRL（Conference on Robot Learning）的所有 topic areas（robot manipulation, locomotion, sim-to-real, RL for robots, robot perception 等）零交集。投稿 CoRL 几乎必然被 desk reject。\n\n如投稿合适会议的 idea 质量评估：Related Work 覆盖强，gap 定位精确，实验设计有章法（这些是形式优点）。但 idea 内核是 incremental gap-filling：核心假设方向可预测（\"friction helps retention\"），存在 trivial alternative 威胁（简单的 \"think first\" 可能就够了），30 分钟处理期的充分性是未验证假设。Novelty 弱-中 限制了上限，使其难以突破 35%。\n\n【主要风险】: \n1. **致命的会议-领域不匹配**：CoRL 是机器人学习会议，本 proposal 是纯 HCI/认知科学研究。投稿 CoRL = desk reject。\n2. **Idea 层面：可预测的结果方向 + trivial alternative 威胁**：\"scaffolded friction 帮助保留技能\"在概念层面近乎不言自明，且缺少\"minimal friction\"控制条件来区分精心设计的 scaffolding 与简单的\"先想后看\"指令之间的增量价值。审稿人可能会认为这是一个 \"the answer is in the question\" 类型的研究。\n```\n\n---\n\n**关键建议**：\n\n1. **最紧迫**：请确认目标会议。如果确实是 CoRL 2026，这个 proposal 需要根本性的方向调整（比如将 deskilling/scaffolding 问题重新框架到机器人遥操作、robot learning from human feedback 等 CoRL scope 内的场景）。如果是笔误，合适的目标会议包括 CHI 2027、CSCW 2027、IUI 2027、FAccT 2027 等。\n\n2. **如投合适会议**：建议增加一个 \"minimal friction\" 条件（仅 \"think first, then see AI\"，无 hints/gates），以回答 trivial alternative 质疑——这会显著提升 novelty 和 contribution 的说服力。\n\nSources:\n- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)\n- [Althea - Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)\n- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)\n- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)\n- [Adjust for Trust](https://arxiv.org/pdf/2502.13321)\n- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 About](https://www.corl.org/about-corl)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a thorough, evidence-based assessment. Let me compile my findings.\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题：投稿目标与 proposal 方向完全不匹配】\n\nCoRL (Conference on Robot Learning) 2026 的 call for papers 明确限定主题为：\nrobot manipulation, navigation, locomotion, driving, flight; learning representations for robotic perception and control; imitation learning; reinforcement learning for physical robots; robot foundation models; robot safety and alignment; robot systems/hardware/sensors。投稿要求 \"Submissions should focus on a core robotics problem and demonstrate the relevance… to robotics.\"\n\n本 proposal 是一项纯粹的 HCI/认知科学人因实验研究——测试 scaffolded cognitive friction 是否能防止 AI 辅助信息评估任务中的人类技能退化。它不涉及任何机器人系统、机器人感知/控制、模仿学习、强化学习、也不涉及任何物理机器人实验。与 CoRL 的学术范围零交集。\n\n这意味着无论 idea 本身质量如何，投稿 CoRL 几乎必然在 desk rejection 阶段即被拒。合适的目标会议应为 CHI、CSCW、FAccT、IUI 或 AAAI/NeurIPS 的 Human-AI Interaction workshop。\n\n以下评估将同时提供：(A) 对 CoRL 的实际中稿概率，以及 (B) 假设投至合适 HCI 会议（如 CHI 2027）时的 idea 质量评估，供参考。\n\n===========================================\n\n【领域调研】:\n\n- [Rani et al., arXiv 2510.01537] (CHI 2026): 本 proposal 的核心前置工作。N=67，within-subjects，GPT-4o 辅助假新闻检测，4 周后无 AI 辅助准确率下降 15.3%。无干预、无控制组。论文明确 call for \"scaffolding interventions designed to reduce dependency while maintaining immediate gains\"。已验证存在且描述准确。\n\n- [Althea, arXiv 2602.11161] (Churina et al., 2026): N=963，比较三种 scaffolding 模式（exploratory/summary/self-search）对 fact-checking 的影响。Self-directed search 在 10 天 follow-up 后改善最持久。但无 AI-withdrawal 设计、无 unrestricted-AI 对照、作者承认仅测量 \"short-term retention of reasoning patterns\"。已验证存在且描述准确。\n\n- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, MIT Sloan, 2026): 形式化动态模型，证明理性 AI 采纳仍可导致稳态技能损失。识别 training rate (κ) 和 workflow design (β) 为缓解杠杆。纯理论，无实证验证。已验证存在。\n\n- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026): 1222 人 RCT，10 分钟 AI 使用即导致算术和阅读理解独立表现退化。验证了因果性但不涉及信息评估领域，也不测试干预。\n\n- [Adjust for Trust, arXiv 2502.13321] (Srinivasan & Thomason, IUI 2026): 信任自适应干预（解释、强制暂停），单 session 内减少 38% 不当依赖。仅测 within-session，不测跨 session 技能保留。\n\n- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 提出 scaffolded cognitive friction 理论框架，使用 multi-agent cognitive forcing functions。纯理论，零实证验证。\n\n- [Farach et al., arXiv 2604.08678] (2026, N=388): Fortune 500 公司现场实验，比较 behavioral vs. cognitive scaffolding。单次 session，无纵向 follow-up。\n\n- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程领域 AI 辅助导致 17% 测验分数下降。单 session，无干预。\n\n- [Metacognitive Scripts, arXiv 2602.20206] (2026): 编程领域 scaffolded friction，AI-blackout 测试 77% vs 39% 失败率。不同领域，无纵向 follow-up。\n\n- 调研总结: AI-induced deskilling 在 2025-2026 年已成为 HCI/认知科学的热点问题，多项研究从不同角度确认了问题的存在性（Rani et al. 在信息评估领域，RCT 在算术/阅读领域，Shen & Tamkin 在编程领域）。理论框架（Augmentation Trap, Cognitive Agency Surrender）已经提出但均缺乏实证。Scaffolding 干预（Althea, CFF, Adjust for Trust）已在 within-session 场景中展示效果，但尚无研究将 scaffolded friction 与 AI-withdrawal longitudinal design 结合来测试技能退化的预防。该 proposal 处于这一确定性领域图景中\"最显而易见的下一步\"位置。\n\n===========================================\n\n【Trivial Alternative 检验】:\n\n存在 trivial alternative 威胁，但 proposal 部分地址了它：\n\n1. **\"不给 AI 就没有 deskilling\"**：proposal 的 no-AI control 条件本身就是这个 baseline。问题在于 \"能否在保留 AI 辅助的即时收益的同时避免技能退化\"，这不是 trivial 的。\n\n2. **\"让用户先独立尝试再看 AI 输出\"（independent-judgment-first）**：Berger et al. (2603.29866) 已在 10 个数据集上证明这能提升即时准确率。Proposal 的 scaffolded friction 条件核心就是这个机制加上 self-explanation gates 和 incremental hints。增量价值在于：(a) 测试这是否能保护纵向技能而非仅仅即时准确率；(b) 与 Althea-style exploratory scaffolding 的 head-to-head 比较。这个增量是真实的但不大——核心干预本身并非新发明，只是在新时间维度上的验证。\n\n3. **简单的 \"forced delay / forced pause\"**：Adjust for Trust 已证明 10 秒强制暂停能减少 38% 不当依赖。是否这种最简单的 friction 就足以防止 deskilling？Proposal 没有包含一个 minimal friction（仅强制暂停）条件来排除这一可能，削弱了因果推断。\n\n**结论：增量价值存在但中等偏窄——核心贡献是\"已知干预手段在新时间维度上的验证\"，而非全新的干预方法或反直觉的发现。**\n\n===========================================\n\n【前提假设检验】:\n\n核心 claim 的逻辑链中有以下未经验证的环节：\n\n1. **\"30 分钟 AI 辅助足以产生可测量的 deskilling\"**：Rani et al. 使用了 4 周纵向 AI 辅助，1222 人 RCT 使用了 10 分钟但测的是算术/阅读。本 proposal 仅 30 分钟 AI 辅助处理信息评估任务——这足以在 between-subjects 设计中产生足够大的效应量吗？如果 unrestricted-AI 条件不能复现 deskilling，整个研究的核心比较就失效了。这是最大的设计风险。\n\n2. **\"Rani et al. 的 15.3% deskilling 效应是稳健的\"**：该结果来自 N=67、within-subjects、无控制组、36% 流失率的研究。效应可能部分或全部由 regression to the mean、practice effects、或参与者疲劳解释。Proposal 将一个尚未被独立复现的效应当作已建立的事实来设计后续研究，存在根基不稳的风险。\n\n3. **\"Trust calibration 是 deskilling 速度的有意义 moderator\"**：Adjust for Trust 证明信任预测 within-session 依赖行为，但\"信任→依赖\"和\"信任→跨 session 技能退化速度\"是不同的因果路径。后者需要信任通过认知参与度的中介机制来影响长期技能编码，这一路径是理论推测而非已证实的。\n\n4. **\"Between-subjects 设计能检测到足够小的效应\"**：N≈120/条件的 between-subjects 设计，检测 medium effect (d=0.5) 的 power 约 80%。但如果 scaffolding 的保护效应较小（d=0.3），这个 N 不够。\n\n===========================================\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** — \n   核心贡献是\"将已有 CFF/scaffolding 干预应用于已识别的 deskilling 问题的纵向验证\"。干预手段本身（mandatory independent attempt, self-explanation gates, incremental hints）完全来自 Buçinca et al. (CSCW 2021) 和 CFF 文献。研究设计（pre/during/post withdrawal）来自 deskilling RCT (2604.04721)。Scaffold 条件设计来自 Althea (2602.11161)。Trust moderation 来自 Adjust for Trust (2502.13321)。Proposal 的真正 novelty 是这些已有元素在 \"信息评估 × 纵向 AI-withdrawal × scaffolding 干预\" 这一特定交叉点的首次组合——这是一种 \"组合 novelty\" 而非概念性创新。Rani et al. 论文本身就明确 call for 了这项研究，意味着这是 field 中最显而易见的下一步，审稿人更可能说 \"this is competent follow-up work\" 而非 \"this is surprising\"。\n\n2. **Significance: 中** — \n   研究问题本身（\"能否防止 AI 导致的技能退化？\"）是当前 HCI/认知科学领域的核心关切，有真实的应用意义（教育、医疗、信息素养）。如果 positive result（scaffolding 确实防止 deskilling），对实践有指导价值。但显著性受限于：(a) 发现的可预测性——\"scaffolding 帮助保留技能\"基本是 desirable difficulties 文献的直接推论，审稿人会说 \"I would have guessed this\"；(b) 如果 negative result（scaffolding 不能防止 deskilling），反而更有意义更 surprising，但 proposal 未充分讨论这一可能性的理论含义。此外，对 NLP/CL 社区的意义有限——这本质上是人因实验，不贡献新的 NLP 方法、模型或 benchmark。\n\n3. **Related Work: 强** — \n   Proposal 对相关工作的覆盖极为详尽（15+ 篇核心引用），差异化定位清晰且准确。每篇关键工作都有精确的 \"Key distinction from X\" 段落。经调研验证，引用的论文均真实存在，描述准确。与 Rani et al.、Althea、Adjust for Trust、CFF 文献、Augmentation Trap 的差异化定位均合理。唯一的小问题是：exhaustive differentiation 本身暗示 novelty delta 较窄——当你需要写 7 个 \"Key distinction\" 段落来论证你和已有工作不同时，实际差异可能主要在于实验设计的排列组合而非概念性突破。\n\n===========================================\n\n【概率估计 — CoRL 2026】: 0% - 2%，中位 ~1%\n\n【CoRL 估计理由】: Proposal 与 CoRL 的学术范围（robot learning、robot perception/control、robot manipulation 等）完全不相关。这是一项关于人类认知技能退化的 HCI 实验研究，不涉及任何机器人系统。即使 idea 本身出色，也会在 scope check 阶段被 desk reject。\n\n---\n\n【参考概率估计 — 假设投至合适 HCI 会议（如 CHI 2027）】: 25% - 38%，中位 ~30%\n\n【参考估计理由】: \n- Related Work 维度是强项（覆盖详尽、定位准确），为 proposal 提供了良好的底线。\n- Significance 中等——问题重要但发现的可预测性限制了 impact。\n- Novelty 是限制上界的关键维度：核心贡献是\"已有方法在新交叉点的首次验证\"，属于 competent follow-up 而非 conceptual breakthrough。如果 positive result，审稿人大概率会说 \"this confirms what we would have expected from the desirable difficulties literature\"，这对顶会来说 novelty 不足以进入 top tier。\n- 概率落在 25-35% 区间的上半部分（~30%）：idea 方向正确、gap 真实、设计严谨，但核心发现的 surprise value 不高。如果 negative result（scaffolding 意外无效）反而更有价值。\n\n【主要风险】: \n1. **Novelty 不足 / \"obvious next step\" 风险**: Rani et al. 明确 call for 了这项研究，CFF 文献已提供了所有干预手段——审稿人可能认为这是 \"executing on someone else's future work section\" 而非独立的创新贡献。核心发现如果 positive，predictability 过高。\n2. **效应复现风险**: 整个研究的根基建立在 Rani et al. N=67 无控制组的单一研究之上。如果 30 分钟 AI 辅助在 between-subjects 设计中不能产生可测量的 deskilling，核心比较就失效了。这不是 idea 层面的问题，而是 idea 的前提假设脆弱性。\n```\n\n---\n\n**总结性说明**：这是一份在 HCI 框架下方法论上非常扎实、文献覆盖极其详尽的 proposal。其核心弱点不在执行层面（实验设计、统计 power 等都考虑周到），而在于 idea 内核——它是一个\"显而易见的下一步\"研究，组合了多个已有工作的元素但缺乏概念性突破。**但最致命的问题是投稿目标：CoRL 是 Conference on Robot Learning，与本 proposal 零交集，建议转投 CHI / CSCW / FAccT。**\n\nSources:\n- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)\n- [Althea - Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)\n- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)\n- [AI Assistance Reduces Persistence](https://arxiv.org/pdf/2604.04721)\n- [Adjust for Trust](https://arxiv.org/abs/2502.13321)\n- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Overview](https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# When the AI Goes Away: Scaffolded Friction, Trust Calibration, and the Skill Decay Curve After AI-Assisted Information Evaluation\n\n## Description\nRani et al. (CHI 2026) demonstrate that AI-assisted misinformation detection leads to 15.3% skill degradation over 4 weeks after AI withdrawal—but their study tested no interventions, included no control group, and had only N=67. We provide the first controlled test of whether scaffolded cognitive friction can prevent this degradation—and whether trust calibration moderates deskilling severity. While the deskilling problem in information evaluation is now empirically established (Rani et al.), the scaffolding literature (Althea, CFF studies, Adjust for Trust) measures only within-session or short-term improvements, not whether interventions protect independent capability after AI is permanently removed. We address this gap with a pre-registered, between-subjects experiment (N≈480) comparing four conditions: no-AI control, unrestricted LLM access (Qwen 3.5 27B), scaffolded friction (mandatory independent attempt, incremental hints, self-explanation gates—operationalizing the Augmentation Trap's theoretical mitigation levers), and exploratory scaffolding (Althea-style modular evidence exploration). Participants complete information evaluation tasks—claim verification, multi-source synthesis, argument quality evaluation—across three phases: baseline assessment, AI-assisted treatment, and post-AI independent assessment at three timepoints (immediate, 1-week, 4-week), yielding per-condition skill decay curves. This design directly answers Rani et al.'s call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains,' extends Althea beyond their acknowledged limitation of measuring only 'short-term retention of reasoning patterns,' and operationalizes the Frontiers framework's distinction between overreliance-as-behavior (measured by CFF studies) and deskilling-as-outcome (measured by our cross-session capability decline). A trust calibration dimension—building on Adjust for Trust's finding that trust predicts within-session reliance—tests whether users who develop higher AI trust during treatment deskill faster after AI removal. The study provides the first empirical test of scaffolded friction interventions combined with an AI-withdrawal design, multi-timepoint decay curve, and trust moderation for deskilling prevention in information evaluation.\n\n## Core Problem\nCan scaffolded cognitive friction interventions prevent the rapid skill degradation that emerges after AI assistance is removed from information evaluation tasks—and does the speed of deskilling depend on how much users trusted the AI? Rani et al. (CHI 2026, N=67) have now demonstrated that AI-assisted misinformation detection leads to a 15.3% accuracy decline after 4 weeks of AI withdrawal, but their study tested no interventions, included no control group, and explicitly calls for scaffolding-based solutions. The CFF and scaffolding literatures (Buçinca et al., Althea, Adjust for Trust) test friction and trust-adaptive interventions to reduce within-session overreliance, but no study has tested whether such interventions protect independent capability after AI access is permanently revoked—nor whether trust calibration moderates the severity of post-withdrawal skill decay.\n\n## Opportunity\nA convergence of causal, clinical, and now longitudinal evidence creates a precisely bounded gap. Rani et al. (arXiv 2510.01537, CHI 2026) provide the first longitudinal evidence that AI-assisted information evaluation causes deskilling after AI removal: 15.3% accuracy decline over 4 weeks in misinformation detection (N=67, within-subjects, no control group, no interventions). Their authors explicitly call for 'scaffolding interventions designed to reduce dependency while maintaining immediate gains' as future work—this is exactly the study we propose. The landmark 1,222-participant RCT (arXiv 2604.04721) provides causal evidence that just 10 minutes of AI use degrades independent performance in arithmetic and reading comprehension. The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) formalizes this as a dynamic model where rational AI adoption can still leave workers worse off, identifying training rate (κ) and workflow design (β) as mitigation levers—but provides no empirical test. Clinical data shows 6-point adenoma detection drops after AI removal (Budzyń et al., Lancet Gastroenterol Hepatol 2025). The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction as a countermeasure but tests nothing empirically. Althea (arXiv 2602.11161, N=963) demonstrates that self-directed scaffolding produces more persistent fact-checking improvements at 10-day follow-up—but has no AI-withdrawal test, no unrestricted-AI condition, no pre-AI baseline, and its authors explicitly acknowledge measuring 'short-term retention of reasoning patterns, not durable skill acquisition.' The metacognitive scripts study (arXiv 2602.20206) tests scaffolded friction in programming (77% vs. 39% failure on AI-blackout tasks) but not information evaluation and lacks longitudinal follow-up. Shen & Tamkin (arXiv 2601.20245) provide RCT evidence of 17% deskilling in programming skill formation with AI but test no interventions and measure only within-session outcomes. Adjust for Trust (arXiv 2502.13321, IUI 2026) tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance—but measures only within-session reliance decisions, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment but measure single-session document quality, not longitudinal skill retention. No study combines: (a) scaffolded friction interventions, (b) an AI-withdrawal design with pre/during/post phases, (c) information evaluation tasks, (d) a multi-timepoint skill decay curve, and (e) trust calibration as a moderator of deskilling severity. The gap is not 'does deskilling occur after AI withdrawal in information evaluation?'—Rani et al. have answered yes. The gap is 'can scaffolded friction prevent it, and does trust predict who deskills fastest?'\n\n## Related Work / Landscape\nEvidence of AI-induced deskilling is now robust, cross-domain, and—critically—extends to information evaluation with longitudinal AI-withdrawal data.\n\n**Deskilling evidence:** Rani et al. (arXiv 2510.01537, CHI 2026) provide the most directly relevant finding: in a month-long within-subjects study (N=67), AI dialogues about misinformation produced +21% accuracy gains during assisted sessions but −15.3% unassisted accuracy at Week 4 vs. Week 0 (β=−0.077, p<.001), with decline driven entirely by fake item detection. Their study used GPT-4o with Google Search but tested no scaffolding interventions, included no independent control group, and had 36% attrition (105→67). The 1,222-participant RCT (arXiv 2604.04721) shows immediate performance degradation after AI exposure in arithmetic and reading comprehension. Shen & Tamkin (arXiv 2601.20245) demonstrate 17% lower quiz scores in AI-assisted programming learners (N=52, d=0.738) and identify six interaction patterns—three cognitively engaged patterns that preserve learning, suggesting that engagement-preserving interventions could work. Clinical trials show 6-point adenoma detection drops after AI removal (Budzyń et al., 2025). Neuroimaging reveals lower brain activation in AI-assisted learners (Kosmyna et al., 2025).\n\n**Theoretical frameworks:** The Augmentation Trap (arXiv 2604.03501, Caosun & Aral) provides a formal dynamic model decomposing AI productivity into skill-independent (α) and skill-complementary (β) channels, proving that rational adoption can produce steady-state loss and identifying five deployment regimes—but offers no empirical validation and notes that 'draft-then-revise' workflows (analogous to our mandatory independent attempt) should preserve the skill-complementary channel. The Cognitive Agency Surrender framework (arXiv 2603.21735) proposes scaffolded friction via multi-agent cognitive forcing functions but provides zero empirical validation. The Frontiers 'Deskilling dilemma' framework (2026) distinguishes cognitive, diagnostic, and moral deskilling as an outcome from overreliance as a behavior—a distinction no intervention study has operationalized.\n\n**Scaffolding and friction interventions:** Althea (arXiv 2602.11161, N=963) compares three scaffolding modes for fact-checking across immediate and 10-day follow-up, finding self-directed search yields strongest persistence—but measures improvement durability during/after scaffolded interaction, not deskilling prevention after AI removal, has no unrestricted-AI condition, and explicitly calls for longer-term studies. Adjust for Trust (arXiv 2502.13321, IUI 2026, Srinivasan & Thomason) tests trust-adaptive interventions—supporting explanations at low trust, counter-explanations at high trust, and 10-second forced pauses at high trust—achieving up to 38% reduction in inappropriate reliance across science questions (N=30/condition) and medical diagnosis (N=20/condition), but measures only within-session reliance decisions across a 30-problem sequence, not cross-session skill retention. Farach et al. (arXiv 2604.08678) test behavioral vs. cognitive scaffolding in a 388-person field experiment at a Fortune 500 company, finding behavioral scaffolding actually reduced quality while cognitive scaffolding helped only top performers—but measure single-session document quality with no longitudinal follow-up. Critical Inker (arXiv 2604.07167) scaffolds critical thinking in AI-assisted writing through Socratic questioning but reports only a small-scale pilot. The CFF literature (Buçinca et al., CSCW 2021; Ghosh et al., 2026) measures immediate reliance decisions, not longitudinal skill retention. Berger et al. (arXiv 2603.29866) show that eliciting independent judgment before AI input boosts accuracy across 10 datasets but do not measure whether this protects skills over time. The overreliance measurement paper (arXiv 2509.08010) identifies three gaps in current overreliance measurement, arguing that LLMs' conversational style creates unique trust dynamics.\n\n**The precise gap:** Rani et al. establish that AI-assisted information evaluation causes deskilling after AI withdrawal. Our study tests whether scaffolded friction can prevent it. This is the direct next step their paper calls for.\n\n## Approach\nWe conduct a pre-registered, between-subjects online experiment (N≈480, recruited via Prolific) with four conditions across three phases, using an AI-withdrawal design that directly tests whether scaffolded friction prevents the deskilling that Rani et al. (CHI 2026) documented in information evaluation.\n\n**Conditions (4):** (1) No-AI control (participants complete all tasks independently—addressing Rani et al.'s lack of a control group), (2) Unrestricted LLM access (standard chatbot interaction using Qwen 3.5 27B via API for open-source reproducibility—replicating the deskilling-inducing condition), (3) Scaffolded friction (mandatory independent attempt with confidence rating before AI output, incremental hint system, self-explanation gates—operationalizing the untested Cognitive Agency Surrender framework and the Augmentation Trap's 'draft-then-revise' workflow design lever), (4) Althea-style exploratory scaffolding (modular evidence exploration without verdict delivery—to directly compare friction-based deskilling prevention against the epistemic-agency scaffolding strategy that Althea found most persistent for improvement). This fourth condition enables a head-to-head comparison of two scaffolding philosophies: friction-as-deskilling-prevention vs. agency-preserving-exploration.\n\n**Phases (3):** Phase 1—Baseline skills assessment: all participants complete information evaluation tasks independently (claim verification adapted from AVeriTeC/FEVER, multi-source synthesis, argument quality evaluation) plus trust disposition measures (Jian et al. trust scale adapted for AI). Phase 2—AI-assisted treatment (30 min): participants work on parallel-form tasks with their assigned AI condition; trust in AI is measured again post-treatment. Phase 3—Post-AI independent assessment: participants complete held-out test items WITHOUT any AI access at three timepoints: immediate (same session), 1-week delayed, and 4-week delayed.\n\n**Primary outcome:** Skill retention, operationalized as the pre-to-post accuracy delta on held-out test items completed independently after AI removal. The three post-withdrawal timepoints (immediate, 1-week, 4-week) yield a skill decay curve per condition. This directly extends Rani et al.'s observation of 15.3% decline (no interventions, N=67, within-subjects) to an interventional, between-subjects design at 7× sample size with a control group.\n\n**Secondary outcomes:** (a) Persistence: time-on-task before abandonment at each post-test; (b) Trust calibration: confidence-accuracy alignment and trust scale changes; (c) Trust-as-moderator: whether pre-treatment trust disposition and within-treatment trust change predict steeper deskilling in the unrestricted-AI condition—extending Adjust for Trust's finding that trust predicts within-session reliance to test whether it also predicts cross-session skill decay; (d) Cognitive engagement: Cognitive Reflection Test and NASA-TLX; (e) Strategy transfer: verification strategy diversity at each timepoint.\n\n**Key distinction from Rani et al. (CHI 2026):** Rani et al. demonstrate that deskilling occurs in information evaluation after AI withdrawal (15.3% decline, N=67, no interventions, no control group, within-subjects). We test whether scaffolded friction can prevent this degradation (N≈480, 4 conditions including no-AI control, between-subjects, with scaffolding interventions). Their study answers 'does AI cause deskilling in information evaluation?' Our study answers 'can we prevent it?' Their limitations—no interventions, no control group, small sample, within-subjects confounds—are precisely what our design addresses.\n\n**Key distinction from Althea:** Althea compares scaffolding modes along an epistemic agency spectrum and measures improvement persistence (post-task → 10-day follow-up). We compare scaffolding modes along a friction spectrum against an unrestricted-AI deskilling baseline and measure skill degradation after AI withdrawal (pre-AI baseline → post-AI independent performance) across a 4-week decay curve. Althea asks 'which scaffolding mode best improves reasoning?' We ask 'which scaffolding mode best prevents the reasoning degradation that unrestricted AI induces?'\n\n**Key distinction from Adjust for Trust (IUI 2026):** Srinivasan & Thomason test trust-adaptive interventions (explanations, forced pauses) to reduce inappropriate reliance during a 30-problem within-session sequence. We measure whether friction during AI-assisted work protects independent capability after AI is permanently removed. They optimize within-session reliance decisions; we optimize cross-session skill retention. We also adopt their insight that trust level predicts reliance behavior—but test whether it similarly predicts the severity of post-withdrawal skill decay.\n\n**Key distinction from CFF literature:** CFF studies measure within-session reliance behavior (agreement rate with AI suggestions). We measure cross-session capability change (can you still do this independently after AI is gone?). This operationalizes the Frontiers framework's distinction between overreliance-as-behavior and deskilling-as-outcome.\n\n**Key distinction from the deskilling RCT (2604.04721):** They demonstrate the problem (AI use degrades independent performance in arithmetic/reading). We test a solution (scaffolded friction prevents that degradation) in information evaluation and add a trust moderation dimension.\n\n**Key distinction from the Augmentation Trap (2604.03501):** Caosun & Aral provide a formal model predicting that training rate and workflow design can mitigate AI-induced skill decay but offer no empirical validation. Our scaffolded friction conditions operationalize their theoretical mitigation levers—mandatory independent attempts preserve the skill-complementary (β) channel, and self-explanation gates increase the effective learning rate (κ)—providing the first empirical test of interventions aligned with their formal framework.\n\n**Model choice:** Qwen 3.5 27B, the largest dense model in the Qwen 3.5 series, served via API (OpenRouter: ~$0.14/M input, $1/M output tokens) or self-hosted on a single H100 via vLLM for consistency. This model is selected for: open-source reproducibility, sufficient capability for realistic AI assistance in information evaluation, and cost efficiency.\n\n## Inspiration\nField guide gap: cognitive deskilling identified as key risk (P3, P13, P14) but measurement and intervention are absent from NLP/HCI research. Critical catalyst: Rani et al. (CHI 2026) demonstrate the problem—15.3% skill degradation after AI withdrawal in misinformation detection—and their future work section explicitly calls for scaffolding-based solutions, which is exactly what we propose. Pattern transfer: the pre/during/post withdrawal design from the deskilling RCT (2604.04721) + the scaffolding mode comparison logic from Althea + the CFF intervention toolkit (P15-P17) reframed for longitudinal skill retention + the independent-judgment-first approach from Berger et al. (2603.29866) + the trust-adaptive intervention logic from Adjust for Trust (2502.13321) reframed for cross-session skill protection + the formal skill-decay dynamics from the Augmentation Trap (2604.03501) operationalized empirically. Novel angle: trust as a moderator of deskilling speed, connecting the deskilling prevention contribution to the trust calibration literature—building on Adjust for Trust's finding that trust level predicts reliance behavior to ask whether it also predicts skill decay severity.\n\n## Key References\n- Dialogues with AI Reduce Beliefs in Misinformation but Build No Lasting Discernment Skills (arXiv 2510.01537, Rani et al., CHI 2026, N=67) — most directly relevant concurrent work: demonstrates 15.3% accuracy decline after 4-week AI withdrawal in misinformation detection using within-subjects design with GPT-4o dialogues; tested no interventions, no control group; their future work explicitly calls for scaffolding-based solutions, which is exactly what we propose\n- Althea: Scaffolding Epistemic Agency for Durable Fact-Checking (arXiv 2602.11161, Churina et al., 2026, N=963) — closest scaffolding concurrent work; compares scaffolding modes for fact-checking improvement persistence but uses no AI-withdrawal design, no unrestricted-AI condition, and authors acknowledge design measures 'short-term retention of reasoning patterns, not durable skill acquisition'\n- AI Assistance Reduces Persistence and Hurts Independent Performance (arXiv 2604.04721, under review 2026) — establishes the deskilling problem with causal evidence from a 1,222-participant RCT\n- The Augmentation Trap: AI Productivity and the Cost of Cognitive Offloading (arXiv 2604.03501, Caosun & Aral, 2026) — formal dynamic model proving rational AI adoption can produce steady-state skill loss; identifies training rate (κ) and workflow design (β) as mitigation levers our interventions operationalize; purely theoretical, no empirical validation\n- Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance (arXiv 2502.13321, Srinivasan & Thomason, IUI 2026) — tests trust-adaptive interventions including 10-second forced pauses, achieving up to 38% reduction in inappropriate reliance; measures within-session reliance only, not cross-session skill retention; supports trust-as-moderator dimension\n- Cognitive Agency Surrender: Defending Epistemic Sovereignty via Scaffolded AI Friction (arXiv 2603.21735, 2026) — theoretical framework we operationalize empirically\n- Beyond AI advice—independent aggregation boosts human–AI accuracy (arXiv 2603.29866, Berger et al., 2026) — demonstrates independent-judgment-first approach boosts accuracy across 10 datasets; conceptually parallel to our mandatory independent attempt, but measures immediate accuracy not skill retention\n- Scaffolding Human-AI Collaboration: A Field Experiment on Behavioral Protocols and Cognitive Reframing (arXiv 2604.08678, Farach et al., 2026, N=388) — field experiment comparing behavioral vs. cognitive scaffolding; found behavioral scaffolding reduced quality while cognitive scaffolding helped only top performers; single-session measurement, no longitudinal follow-up\n- How AI Impacts Skill Formation (arXiv 2601.20245, Shen & Tamkin, 2026, N=52) — RCT evidence of 17% deskilling in programming with AI (d=0.738); identifies cognitively-engaged interaction patterns that preserve learning; programming domain only, single-session, no interventions tested\n- Critical Inker: Scaffolding Critical Thinking in AI-Assisted Writing Through Socratic Questioning (arXiv 2604.07167, Hugenroth et al., 2026) — Socratic scaffolding for writing; small pilot, different domain\n- Brainrot: Deskilling and Addiction are Overlooked AI Risks (FAccT 2026, Chalkidis & Søgaard)\n- To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making (CSCW 2021, Buçinca et al.)\n- Endoscopist deskilling risk after exposure to AI in colonoscopy (Budzyń et al., Lancet Gastroenterol Hepatol 2025)\n- Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant (Kosmyna et al., 2025)\n- Mitigating Epistemic Debt in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts (arXiv 2602.20206, 2026) — scaffolded friction in programming with AI-blackout test; different domain, no longitudinal follow-up\n- Deskilling dilemma: brain over automation (Frontiers in Medicine, 2026) — provides cognitive/diagnostic/moral deskilling typology and distinguishes deskilling-as-outcome from overreliance-as-behavior\n- Measuring and mitigating overreliance is necessary for building human-compatible AI (arXiv 2509.08010) — identifies gaps in overreliance measurement and LLM-specific trust dynamics\n- An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing (arXiv 2601.18033, Ghosh et al., 2026)\n- From Algorithm Aversion to AI Dependence: Deskilling, Upskilling, and Emerging Addictions in the GenAI Age (Kim, Consumer Psychology Review 2026)\n- Generative AI Reliance and Executive Function Attenuation (Baldeo, Technology Mind & Behavior 2026)\n- Cognitive Forcing for Better Decision-Making: Reducing Overreliance on AI Systems Through Partial Explanations (CSCW 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '40–60 (self-hosting Qwen 3.5 27B on H100 for real-time experiment serving; or ~$50–80 via API with no self-hosting needed)', 'timeline': '5 months (1 mo platform design + task creation, 3–4 weeks IRB approval, 2 weeks pilot N=80, 6 weeks main data collection in overlapping waves to accommodate 4-week follow-ups, 5 weeks analysis + writing)', 'estimated_gpu_cost': '$80–120 (H100 at ~$2/hr) or $50–80 via OpenRouter API'}\n- **human_in_loop**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4.5 months (Claude accelerates platform dev, task item generation via IRT-calibrated stimulus pools, statistical analysis scripting, and manuscript drafting)', 'claude_api_cost': '$350 (platform scaffolding, stimulus generation, R/Python analysis pipelines, growth-curve modeling code, manuscript drafting)', 'estimated_gpu_cost': '$80–120 or $50–80 via API'}\n- **auto_research**: {'gpu_hours': '40–60 (or API equivalent)', 'timeline': '4 months (automated pilot analysis, adaptive task calibration, parallel manuscript drafting)', 'claude_api_cost': '$900 (end-to-end experimental platform generation, automated IRT-based item analysis, growth-curve model specification, full statistical report generation, iterative manuscript revision)', 'estimated_gpu_cost': '$80–120 or $50–80 via API', 'speed_bottleneck': 'IRB approval (3–6 weeks, irreducible) and the 4-week delayed follow-up window; participant compensation dominates total cost: N=480 initial session (40 min at $12/hr = $3,840) + 33.3% Prolific academic fee ($1,279) + 1-week follow-up (~385 retained, 20 min, $1,540 + $513 fee) + 4-week follow-up (~310 retained, 20 min, $1,240 + $413 fee) + completion bonuses (~$700 + $233 fee) = ~$9,760 total participant costs'}\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T21:01:17.381Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:01:17.381Z",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T21:01:17.395Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
调研完成。我现在可以给出完整的入口评审。这里有一个 **极其关键的前置问题** 需要首先指出。

---

```
【阶段】: Triage

==========================================================================
⚠️ 致命问题：投稿目标 CoRL 2026 与 proposal 内容完全不匹配
==========================================================================

CoRL (Conference on Robot Learning) 的核心议题包括：
- 模仿学习、强化学习（用于机器人控制）
- Sim-to-real transfer
- 机器人感知、操控、移动
- 机器人基础模型
- 机器人硬件与系统
- 会议明确鼓励"real-robot experiments"

本 proposal 的内容是：
- AI 辅助信息评估中的认知去技能化（misinformation detection）
- 基于 Prolific 的人类被试实验（N≈480）
- 脚手架式认知摩擦干预
- 信任校准与技能衰退曲线
- 纯 HCI / 认知心理学方法论，无任何机器人相关成分

这是一个 100% 的 venue mismatch。该论文在 CoRL 会被 desk-reject，
不会进入审稿流程。

正确的投稿目标应为：CHI、CSCW、FAccT、AAAI HCOMP、或 IUI。
==========================================================================

以下评估基于 idea 本身的学术质量（假设投稿到正确的 HCI 会议），
以便为后续流程提供参考。但 CoRL 中稿概率为 ~0%。

==========================================================================

【领域调研】:

- [Rani et al., "Dialogues with AI Reduce Beliefs in Misinformation 
  but Build No Lasting Discernment Skills"](https://arxiv.org/abs/2510.01537) 
  (CHI 2026): 最直接的前序工作。N=67 被试在 AI 辅助后 4 周出现 15.3% 
  准确率下降。无干预、无对照组、within-subjects 设计。明确呼吁未来做
  scaffolding 干预研究。本 proposal 是对该呼吁的直接回应。✅ 论文真实存在，
  描述准确。

- [Althea: Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161) 
  (2026, N=963): 比较三种脚手架模式（Exploratory/Summary/Self-search）的
  fact-checking 效果，发现 self-directed search 的改善最持久（10 天随访）。
  但无 AI-withdrawal 设计、无 unrestricted-AI 条件、无 pre-AI baseline。
  作者承认仅测量"short-term retention"。✅ 论文真实，描述准确。

- ["AI Assistance Reduces Persistence and Hurts Independent Performance"](https://arxiv.org/abs/2604.04721) 
  (2026, N=1222 RCT): 因果证据表明 AI 使用降低独立表现（arithmetic, 
  reading comprehension）。仅测 within-session，无干预测试。✅ 真实存在。

- [The Augmentation Trap](https://arxiv.org/abs/2604.03501) 
  (Caosun & Aral, 2026): 形式化动态模型，证明理性 AI 采用仍可导致
  稳态技能损失。纯理论，无实证验证。✅ 真实，描述准确。

- [Adjust for Trust](https://arxiv.org/abs/2502.13321) 
  (Srinivasan & Thomason, IUI 2026): 信任自适应干预减少不当依赖达 38%。
  仅测 within-session reliance，非 cross-session skill retention。
  ✅ 真实，描述准确。

- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735) 
  (2026): 提出 scaffolded AI friction 的理论框架但无实证验证。✅ 真实。

- [Farach et al.](https://arxiv.org/abs/2604.08678) 
  (2026, N=388): behavioral vs cognitive scaffolding 的 field experiment。
  单次测量，无纵向随访。✅ 真实。

- [Metacognitive Scripts for Programming](https://arxiv.org/abs/2602.20206) 
  (2026): 编程领域的脚手架摩擦 + AI blackout test（77% vs 39% 失败率）。
  不同领域，无纵向随访。✅ 真实。

- Budzyń et al. (Lancet Gastroenterol Hepatol 2025): 临床领域 AI 撤除后
  腺瘤检出率下降 6 个百分点。✅ 真实。

- 调研总结: AI 辅助导致认知去技能化在 2025-2026 年已成为 cross-domain 的
  确认事实（信息评估、编程、数学、临床医学）。现有干预研究（CFF、Althea、
  Adjust for Trust）均仅测量 within-session 或 short-term 效果，
  尚无研究测试干预能否在 AI 永久撤除后保护独立能力。
  本 proposal 精准定位于这一空缺。


【Trivial Alternative 检验】:

存在一个显著的 trivial alternative 威胁：
"mandatory independent attempt first"（强制先独立尝试）本身就可能
是防止去技能化的充分条件。Berger et al. (2603.29866) 已证明 independent 
judgment first 在 10 个数据集上提升准确率。如果仅"先独立做一遍"就足以
阻止大部分去技能化，那么 proposal 中精心设计的 incremental hints、
self-explanation gates 等复杂脚手架的增量价值可能很小。

Proposal 的 4 条件设计部分缓解了这一问题（因为可以通过对比 Condition 3 
vs 更简单的变体来分离贡献），但核心风险是：最终发现 scaffolded friction 
≈ "just try it yourself first"，这会使 contribution 大打折扣。

增量价值的关键在于：(a) scaffolded friction 是否比 mere independent 
attempt 在 4-week 衰退曲线上有显著额外保护效果，(b) trust moderation 
维度是否提供有意义的 mechanistic insight。如果两者都不成立，本研究退化
为"控制实验验证了一个符合直觉的结论"。


【前提假设检验】:

核心逻辑链中有两个关键未验证假设：

1. **30 分钟 AI 辅助治疗足以在 unrestricted 条件下诱导可测量的去技能化。**
   Rani et al. 使用了 1 个月的纵向交互，1222-RCT 使用了 10 分钟但在
   arithmetic/reading（更简单的认知任务）。信息评估任务（claim verification、
   multi-source synthesis）的认知复杂度更高，30 分钟的单次暴露是否足以
   产生效果是完全未知的。如果 unrestricted 条件未能产生显著去技能化，
   整个实验的 contrast 失效——scaffolding 无从"prevent"一个未发生的现象。

2. **Between-subjects 设计下，baseline 个体差异的噪声是否会掩盖
   condition 间的差异。** Rani et al. 使用 within-subjects 设计
   （自身对照）才检测到 15.3% 的效果。Between-subjects 设计在 N≈120/条件
   下检测类似大小的效应需要较大 power——如果实际效应比 Rani 的小
   （因为暴露时间短得多），可能出现 underpowered 的问题。


【3 维度打分】:

1. Novelty: 【中】
   — 核心贡献是一个实验设计层面的"first combination"：将已有的脚手架
     干预工具（CFF, Buçinca et al. 2021; Althea 2026）应用到一个新验证
     的问题（AI 撤除后去技能化, Rani et al. 2026）上，加入纵向随访
     和信任调节维度。每个组件（scaffolded friction、AI-withdrawal design、
     trust-as-moderator）在之前的工作中都已出现，novelty 来自组合。
   — 组合式 novelty 在 HCI 中是可接受的，但不构成强 novelty。
     审稿人可能会评价为"well-motivated follow-up study"而非
     "conceptual advance"。
   — Adjust for Trust (IUI 2026) 已经测试了 trust-adaptive 干预；
     Althea (2026) 已经测试了多种脚手架模式的持久性；
     Berger et al. (2026) 已经测试了 independent-judgment-first。
     本 proposal 的核心 delta 是"把这些放到 AI-withdrawal + 
     longitudinal 框架里测"，这是重要的实证推进，但概念层面的 novelty 
     有限。

2. Significance: 【强】
   — 研究问题的重要性和时效性极高。AI 去技能化是 2025-2026 年跨学科
     的核心关切，且从问题识别到干预验证是自然的、急需的研究进展方向。
   — Rani et al. 的 explicit call for exactly this study 表明该领域
     认可这一空缺。
   — 如果 scaffolded friction 确实能防止去技能化，这一发现对 AI 系统
     设计（educational AI、AI assistants、clinical AI）有广泛的实践
     指导价值。
   — 但如前所述，positive result（"scaffolding helps"）并不 surprising。
     审稿人不太可能说"I would not have guessed this"。Negative result
     （"scaffolding doesn't help"）反而更有学术冲击力。

3. Related Work: 【强】
   — Related work 的覆盖异常全面。所有关键论文均真实存在，描述准确，
     gap 分析精确。每篇论文的局限性（Rani: 无干预/无对照/小样本；
     Althea: 无 AI-withdrawal；Adjust for Trust: 仅 within-session；
     CFF: 仅 reliance behavior）都被正确识别并用于论证 gap。
   — 差异化定位清晰：对每个关键竞争工作（Rani, Althea, Adjust for Trust, 
     CFF, Augmentation Trap, 1222-RCT）都有专门的"Key distinction"段落。
   — 在 HCI 审稿标准下，这一水平的 related work 分析属于优秀。


【概率估计】（假设投稿到正确 venue，如 CHI 2027）: 
[25% - 38%] 中位 30%

【概率估计】（投稿 CoRL 2026）: 
~0%（desk reject，venue 完全不匹配）

【估计理由】:
假设正确 venue (CHI/CSCW)：
Significance 维度强（研究问题重要且 timely），Related Work 强（覆盖
全面、定位清晰），但 Novelty 处于中位——核心贡献是"组合式 first 
empirical test"，每个组件都已在先前工作中出现。这在 CHI 中可以接受
但不突出。关键限制上界的是两个因素：(a) Trivial alternative 威胁——
"independent attempt first"可能已足够，复杂脚手架的增量价值存疑；
(b) positive result 不 surprising——审稿人会觉得"scaffolding prevents 
deskilling"符合直觉，降低了论文的 intellectual excitement。
这是一个 well-executed follow-up study 的 profile，不是一个 
paradigm-shifting contribution 的 profile。

对于 CoRL：本 proposal 与 Conference on Robot Learning 的 scope 
完全不相交。信息评估、misinformation detection、Prolific 人类被试实验
均不在 CoRL 的审稿范围内。无论 idea 质量如何，CoRL 中稿概率为零。

【主要风险】:
1. **致命 venue mismatch**: CoRL 是 Conference on Robot Learning，
   本 proposal 是纯 HCI/cognitive psychology 研究，无任何机器人相关内容。
   这不是"borderline"——是完全不相关的领域。

2. **Trivial alternative 威胁（idea 层面）**: 如果"强制先独立尝试"就
   足以防止大部分去技能化，elaborate scaffolding 的增量贡献可能微不足道，
   核心 claim 退化为显而易见的结论。

3. **剂量-效应风险（idea 层面）**: 30 分钟的 AI 暴露是否足以在信息评估
   任务上诱导可测量的去技能化完全未知，如果 unrestricted 条件不能产生
   基准效应，整个实验设计的 contrast 基础不存在。
```

---

**总结**: 这个 proposal 在 idea 层面是一个 solid 但非 outstanding 的 HCI 研究——研究问题重要、文献分析到位、gap 真实存在，但 novelty 偏组合式、positive result 不够 surprising。然而，**投稿 CoRL 2026 是一个根本性的方向错误**——CoRL 是机器人学习会议，这篇论文与其 scope 完全不相交，中稿概率本质上为零。建议重新考虑投稿目标（CHI 2027、CSCW 2027、FAccT 2027 等 HCI 会议）。

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Rani et al., CHI 2026](https://arxiv.org/abs/2510.01537)
- [Althea, 2026](https://arxiv.org/abs/2602.11161)
- [AI Assistance Reduces Persistence, 2026](https://arxiv.org/abs/2604.04721)
- [The Augmentation Trap, 2026](https://arxiv.org/abs/2604.03501)
- [Adjust for Trust, IUI 2026](https://arxiv.org/abs/2502.13321)
- [Cognitive Agency Surrender, 2026](https://arxiv.org/abs/2603.21735)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
调研完成。现在我有足够的信息来做客观评估。

---

```
【阶段】: Triage

【⚠️ 致命前置问题：会议领域匹配】:
本 proposal 研究的是 AI 辅助信息评估中的认知去技能化（cognitive deskilling）、支架式认知摩擦（scaffolded friction）和信任校准（trust calibration），属于 HCI/认知科学 领域。
CoRL（Conference on Robot Learning）的核心 scope 是：imitation learning、reinforcement learning for robots、sim-to-real transfer、robot perception、learned manipulation/locomotion、robot foundation models 等。
本 proposal 与 CoRL 的学科范畴零重叠，投稿 CoRL 大概率会被 desk reject。
合适的投稿目标应为 CHI、CSCW、FAccT、IUI 等 HCI 会议。

以下评估基于 idea 本身的学术质量（假设投稿至合适的 HCI 会议），但最终概率估计必须反映 CoRL 这个目标会议。


【领域调研】:
- [Rani et al., arXiv 2510.01537] (CHI 2026): 确认真实存在。N=67，within-subjects，AI 辅助误信息检测导致 4 周后 15.3% 准确率下降。无干预、无对照组。Proposal 的描述准确。
- [Althea, arXiv 2602.11161] (2026, N=963): 确认真实存在。比较三种 scaffolding 模式的 fact-checking 效果，self-directed search 产生最持久改善。无 AI-withdrawal 设计、无 unrestricted-AI 条件。Proposal 描述准确。
- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026, under review, N=1222): 确认真实存在。RCT 证据表明 AI 辅助降低独立表现和坚持度。在算术和阅读理解任务中，仅 10 分钟 AI 使用即导致退化。
- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, 2026): 确认真实存在。纯理论形式化模型，无实证验证。Proposal 描述准确。
- [Adjust for Trust, arXiv 2502.13321] (IUI 2026): 确认真实存在。测试信任自适应干预（forced pauses 等），降低 38% 不当依赖，但仅测量 within-session 依赖决策。
- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 确认真实存在。理论框架，提出 scaffolded AI friction 概念，但零实证验证。
- [Farach et al., arXiv 2604.08678] (2026, N=388): 行为 vs. 认知 scaffolding 的 field experiment，但仅 single-session 测量。
- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程技能形成中 17% deskilling，单次 session，无干预。
- [Metacognitive scripts, arXiv 2602.20206] (2026): 编程领域的 scaffolded friction + AI-blackout 测试（77% vs 39% failure），但无纵向跟踪。
- 调研总结: AI deskilling 在 2025-2026 成为爆发性热点，多篇高影响力论文从不同角度（因果证据、形式模型、神经影像、临床数据）确认了问题的存在。但"scaffolded friction 能否预防 AI withdrawal 后的 deskilling"这一具体问题确实尚无直接实证回答。然而，该领域属于 HCI/认知科学，与 CoRL 的机器人学习 scope 完全不相关。


【Trivial Alternative 检验】:
存在 trivial alternative 威胁。核心干预"mandatory independent attempt before AI output"（先独立判断再看 AI 结果）本质上就是 Berger et al. (2603.29866) 的 "independent judgment first" 策略。Berger et al. 已在 10 个数据集上展示了该策略对即时准确率的提升效果。Proposal 的完整 scaffolding 机制（incremental hints、self-explanation gates）相对于一个简单的"先自己想，再看 AI"指令的增量价值不明确。

关键缺陷：4 个实验条件中缺少一个"minimal friction"条件（仅要求先独立判断，无 hints/gates），导致无法区分核心效果来自"要求独立思考"这个简单操作，还是来自精心设计的 scaffolding 机制。如果仅"先想后看"就能防止 deskilling，那 proposal 的 scaffolding 设计就不是 necessary 的。

增量价值的可能辩护：Proposal 可以主张 scaffolding 的各组件（hints、self-explanation gates）会比简单的 "think first" 产生更强的防护效果——但这需要实验验证，且当前条件设计无法直接回答这个问题。


【前提假设检验】:
核心 claim 的逻辑链：(1) AI 辅助导致 deskilling [已有实证] → (2) Within-session overreliance 是 deskilling 的机制 [合理但非唯一机制] → (3) 减少 within-session overreliance 的干预（scaffolded friction）能防止 cross-session deskilling [关键跳跃，未经验证] → (4) Trust 调节 deskilling 速度 [探索性假设]

关键未验证环节：
1. **从 within-session 到 cross-session 的跳跃**：CFF 文献证明 friction 减少 within-session 依赖行为，但"减少依赖行为"≠"保护独立技能"。可能存在其他机制（如 cognitive offloading 的神经适应、动机变化）使得即使 session 内表现更独立，removal 后仍然 deskill。
2. **30 分钟处理期的充分性**：Rani et al. 的 deskilling 来自 4 周 AI 交互。2604.04721 的 10 分钟效应来自简单任务（算术、阅读理解）。在信息评估这类复杂任务中，30 分钟是否足以产生可测量的 deskilling 效应？如果 deskilling 效应在 unrestricted-AI 条件中不显著，整个实验就没有待保护的效应。
3. **Between-subjects 设计下个体差异的噪声**：Rani et al. 的 within-subjects 设计控制了个体差异，但也引入了 order effects。Proposal 用 between-subjects 设计消除了 order effects 但引入了大量个体差异噪声。N≈120/condition 是否足够检测 deskilling 差异？


【3 维度打分】:
  1. Novelty: 弱-中 — Proposal 正确识别了一个 gap（scaffolded friction + AI-withdrawal + longitudinal + trust moderation 的组合），但这本质上是一个"组合填空"式贡献。每个组件（deskilling 证据、scaffolding 干预、信任测量、纵向设计）都已在近期文献中存在。核心假设方向（"让人在用 AI 时多思考，移除 AI 后技能保留更好"）直觉上显然成立——如果结果是 positive 的，审稿人大概率会说 "I would have guessed this"，而非 "surprising"。Metacognitive scripts 研究 (2602.20206) 已经在编程领域用 scaffolded friction + AI-blackout 展示了类似逻辑（77% vs 39% failure），本 proposal 相当于将其扩展到信息评估领域并增加纵向跟踪——这是 incremental extension，非概念突破。
  
  2. Significance: 中 — AI deskilling 无疑是一个重要且 timely 的研究问题，2025-2026 多篇高影响力论文（Rani et al., The Augmentation Trap, 2604.04721）共同推动了该领域。但本 proposal 的贡献主要在于提供"scaffolding 有效"的实证确认（而非提出新概念或新范式）。如果 positive result 出现，它验证了已有理论预测（Cognitive Agency Surrender 框架、Augmentation Trap 的 κ 和 β 杠杆）。对领域的影响是"确认性的"而非"开创性的"。Trust-as-moderator 维度是一个有趣的 secondary contribution，但作为探索性分析，其分量有限。
  
  3. Related Work: 强 — 这是 Proposal 最突出的优点。文献覆盖极其全面（17+ 篇核心引用），每篇论文的描述经核实均准确。与每项先行工作的差异化定位通过 6 个 "Key distinction from X" 段落清晰阐述。Gap 的界定精确且有防御力。几乎可以作为 deskilling+scaffolding 文献的 mini survey。


【概率估计】: 0-2%（CoRL 2026），25-35% 中位 30%（如投稿 CHI/CSCW 等合适会议）

【估计理由】: 
CoRL 维度：本 proposal 研究的是 HCI/认知科学问题（AI 辅助信息评估中的 cognitive deskilling prevention），与 CoRL（Conference on Robot Learning）的所有 topic areas（robot manipulation, locomotion, sim-to-real, RL for robots, robot perception 等）零交集。投稿 CoRL 几乎必然被 desk reject。

如投稿合适会议的 idea 质量评估：Related Work 覆盖强，gap 定位精确，实验设计有章法（这些是形式优点）。但 idea 内核是 incremental gap-filling：核心假设方向可预测（"friction helps retention"），存在 trivial alternative 威胁（简单的 "think first" 可能就够了），30 分钟处理期的充分性是未验证假设。Novelty 弱-中 限制了上限，使其难以突破 35%。

【主要风险】: 
1. **致命的会议-领域不匹配**：CoRL 是机器人学习会议，本 proposal 是纯 HCI/认知科学研究。投稿 CoRL = desk reject。
2. **Idea 层面：可预测的结果方向 + trivial alternative 威胁**："scaffolded friction 帮助保留技能"在概念层面近乎不言自明，且缺少"minimal friction"控制条件来区分精心设计的 scaffolding 与简单的"先想后看"指令之间的增量价值。审稿人可能会认为这是一个 "the answer is in the question" 类型的研究。
```

---

**关键建议**：

1. **最紧迫**：请确认目标会议。如果确实是 CoRL 2026，这个 proposal 需要根本性的方向调整（比如将 deskilling/scaffolding 问题重新框架到机器人遥操作、robot learning from human feedback 等 CoRL scope 内的场景）。如果是笔误，合适的目标会议包括 CHI 2027、CSCW 2027、IUI 2027、FAccT 2027 等。

2. **如投合适会议**：建议增加一个 "minimal friction" 条件（仅 "think first, then see AI"，无 hints/gates），以回答 trivial alternative 质疑——这会显著提升 novelty 和 contribution 的说服力。

Sources:
- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)
- [Althea - Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)
- [AI Assistance Reduces Persistence and Hurts Independent Performance](https://arxiv.org/abs/2604.04721)
- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)
- [Adjust for Trust](https://arxiv.org/pdf/2502.13321)
- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a thorough, evidence-based assessment. Let me compile my findings.

---

```
【阶段】: Triage

【致命前置问题：投稿目标与 proposal 方向完全不匹配】

CoRL (Conference on Robot Learning) 2026 的 call for papers 明确限定主题为：
robot manipulation, navigation, locomotion, driving, flight; learning representations for robotic perception and control; imitation learning; reinforcement learning for physical robots; robot foundation models; robot safety and alignment; robot systems/hardware/sensors。投稿要求 "Submissions should focus on a core robotics problem and demonstrate the relevance… to robotics."

本 proposal 是一项纯粹的 HCI/认知科学人因实验研究——测试 scaffolded cognitive friction 是否能防止 AI 辅助信息评估任务中的人类技能退化。它不涉及任何机器人系统、机器人感知/控制、模仿学习、强化学习、也不涉及任何物理机器人实验。与 CoRL 的学术范围零交集。

这意味着无论 idea 本身质量如何，投稿 CoRL 几乎必然在 desk rejection 阶段即被拒。合适的目标会议应为 CHI、CSCW、FAccT、IUI 或 AAAI/NeurIPS 的 Human-AI Interaction workshop。

以下评估将同时提供：(A) 对 CoRL 的实际中稿概率，以及 (B) 假设投至合适 HCI 会议（如 CHI 2027）时的 idea 质量评估，供参考。

===========================================

【领域调研】:

- [Rani et al., arXiv 2510.01537] (CHI 2026): 本 proposal 的核心前置工作。N=67，within-subjects，GPT-4o 辅助假新闻检测，4 周后无 AI 辅助准确率下降 15.3%。无干预、无控制组。论文明确 call for "scaffolding interventions designed to reduce dependency while maintaining immediate gains"。已验证存在且描述准确。

- [Althea, arXiv 2602.11161] (Churina et al., 2026): N=963，比较三种 scaffolding 模式（exploratory/summary/self-search）对 fact-checking 的影响。Self-directed search 在 10 天 follow-up 后改善最持久。但无 AI-withdrawal 设计、无 unrestricted-AI 对照、作者承认仅测量 "short-term retention of reasoning patterns"。已验证存在且描述准确。

- [The Augmentation Trap, arXiv 2604.03501] (Caosun & Aral, MIT Sloan, 2026): 形式化动态模型，证明理性 AI 采纳仍可导致稳态技能损失。识别 training rate (κ) 和 workflow design (β) 为缓解杠杆。纯理论，无实证验证。已验证存在。

- [AI Assistance Reduces Persistence, arXiv 2604.04721] (2026): 1222 人 RCT，10 分钟 AI 使用即导致算术和阅读理解独立表现退化。验证了因果性但不涉及信息评估领域，也不测试干预。

- [Adjust for Trust, arXiv 2502.13321] (Srinivasan & Thomason, IUI 2026): 信任自适应干预（解释、强制暂停），单 session 内减少 38% 不当依赖。仅测 within-session，不测跨 session 技能保留。

- [Cognitive Agency Surrender, arXiv 2603.21735] (2026): 提出 scaffolded cognitive friction 理论框架，使用 multi-agent cognitive forcing functions。纯理论，零实证验证。

- [Farach et al., arXiv 2604.08678] (2026, N=388): Fortune 500 公司现场实验，比较 behavioral vs. cognitive scaffolding。单次 session，无纵向 follow-up。

- [Shen & Tamkin, arXiv 2601.20245] (2026, N=52): 编程领域 AI 辅助导致 17% 测验分数下降。单 session，无干预。

- [Metacognitive Scripts, arXiv 2602.20206] (2026): 编程领域 scaffolded friction，AI-blackout 测试 77% vs 39% 失败率。不同领域，无纵向 follow-up。

- 调研总结: AI-induced deskilling 在 2025-2026 年已成为 HCI/认知科学的热点问题，多项研究从不同角度确认了问题的存在性（Rani et al. 在信息评估领域，RCT 在算术/阅读领域，Shen & Tamkin 在编程领域）。理论框架（Augmentation Trap, Cognitive Agency Surrender）已经提出但均缺乏实证。Scaffolding 干预（Althea, CFF, Adjust for Trust）已在 within-session 场景中展示效果，但尚无研究将 scaffolded friction 与 AI-withdrawal longitudinal design 结合来测试技能退化的预防。该 proposal 处于这一确定性领域图景中"最显而易见的下一步"位置。

===========================================

【Trivial Alternative 检验】:

存在 trivial alternative 威胁，但 proposal 部分地址了它：

1. **"不给 AI 就没有 deskilling"**：proposal 的 no-AI control 条件本身就是这个 baseline。问题在于 "能否在保留 AI 辅助的即时收益的同时避免技能退化"，这不是 trivial 的。

2. **"让用户先独立尝试再看 AI 输出"（independent-judgment-first）**：Berger et al. (2603.29866) 已在 10 个数据集上证明这能提升即时准确率。Proposal 的 scaffolded friction 条件核心就是这个机制加上 self-explanation gates 和 incremental hints。增量价值在于：(a) 测试这是否能保护纵向技能而非仅仅即时准确率；(b) 与 Althea-style exploratory scaffolding 的 head-to-head 比较。这个增量是真实的但不大——核心干预本身并非新发明，只是在新时间维度上的验证。

3. **简单的 "forced delay / forced pause"**：Adjust for Trust 已证明 10 秒强制暂停能减少 38% 不当依赖。是否这种最简单的 friction 就足以防止 deskilling？Proposal 没有包含一个 minimal friction（仅强制暂停）条件来排除这一可能，削弱了因果推断。

**结论：增量价值存在但中等偏窄——核心贡献是"已知干预手段在新时间维度上的验证"，而非全新的干预方法或反直觉的发现。**

===========================================

【前提假设检验】:

核心 claim 的逻辑链中有以下未经验证的环节：

1. **"30 分钟 AI 辅助足以产生可测量的 deskilling"**：Rani et al. 使用了 4 周纵向 AI 辅助，1222 人 RCT 使用了 10 分钟但测的是算术/阅读。本 proposal 仅 30 分钟 AI 辅助处理信息评估任务——这足以在 between-subjects 设计中产生足够大的效应量吗？如果 unrestricted-AI 条件不能复现 deskilling，整个研究的核心比较就失效了。这是最大的设计风险。

2. **"Rani et al. 的 15.3% deskilling 效应是稳健的"**：该结果来自 N=67、within-subjects、无控制组、36% 流失率的研究。效应可能部分或全部由 regression to the mean、practice effects、或参与者疲劳解释。Proposal 将一个尚未被独立复现的效应当作已建立的事实来设计后续研究，存在根基不稳的风险。

3. **"Trust calibration 是 deskilling 速度的有意义 moderator"**：Adjust for Trust 证明信任预测 within-session 依赖行为，但"信任→依赖"和"信任→跨 session 技能退化速度"是不同的因果路径。后者需要信任通过认知参与度的中介机制来影响长期技能编码，这一路径是理论推测而非已证实的。

4. **"Between-subjects 设计能检测到足够小的效应"**：N≈120/条件的 between-subjects 设计，检测 medium effect (d=0.5) 的 power 约 80%。但如果 scaffolding 的保护效应较小（d=0.3），这个 N 不够。

===========================================

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是"将已有 CFF/scaffolding 干预应用于已识别的 deskilling 问题的纵向验证"。干预手段本身（mandatory independent attempt, self-explanation gates, incremental hints）完全来自 Buçinca et al. (CSCW 2021) 和 CFF 文献。研究设计（pre/during/post withdrawal）来自 deskilling RCT (2604.04721)。Scaffold 条件设计来自 Althea (2602.11161)。Trust moderation 来自 Adjust for Trust (2502.13321)。Proposal 的真正 novelty 是这些已有元素在 "信息评估 × 纵向 AI-withdrawal × scaffolding 干预" 这一特定交叉点的首次组合——这是一种 "组合 novelty" 而非概念性创新。Rani et al. 论文本身就明确 call for 了这项研究，意味着这是 field 中最显而易见的下一步，审稿人更可能说 "this is competent follow-up work" 而非 "this is surprising"。

2. **Significance: 中** — 
   研究问题本身（"能否防止 AI 导致的技能退化？"）是当前 HCI/认知科学领域的核心关切，有真实的应用意义（教育、医疗、信息素养）。如果 positive result（scaffolding 确实防止 deskilling），对实践有指导价值。但显著性受限于：(a) 发现的可预测性——"scaffolding 帮助保留技能"基本是 desirable difficulties 文献的直接推论，审稿人会说 "I would have guessed this"；(b) 如果 negative result（scaffolding 不能防止 deskilling），反而更有意义更 surprising，但 proposal 未充分讨论这一可能性的理论含义。此外，对 NLP/CL 社区的意义有限——这本质上是人因实验，不贡献新的 NLP 方法、模型或 benchmark。

3. **Related Work: 强** — 
   Proposal 对相关工作的覆盖极为详尽（15+ 篇核心引用），差异化定位清晰且准确。每篇关键工作都有精确的 "Key distinction from X" 段落。经调研验证，引用的论文均真实存在，描述准确。与 Rani et al.、Althea、Adjust for Trust、CFF 文献、Augmentation Trap 的差异化定位均合理。唯一的小问题是：exhaustive differentiation 本身暗示 novelty delta 较窄——当你需要写 7 个 "Key distinction" 段落来论证你和已有工作不同时，实际差异可能主要在于实验设计的排列组合而非概念性突破。

===========================================

【概率估计 — CoRL 2026】: 0% - 2%，中位 ~1%

【CoRL 估计理由】: Proposal 与 CoRL 的学术范围（robot learning、robot perception/control、robot manipulation 等）完全不相关。这是一项关于人类认知技能退化的 HCI 实验研究，不涉及任何机器人系统。即使 idea 本身出色，也会在 scope check 阶段被 desk reject。

---

【参考概率估计 — 假设投至合适 HCI 会议（如 CHI 2027）】: 25% - 38%，中位 ~30%

【参考估计理由】: 
- Related Work 维度是强项（覆盖详尽、定位准确），为 proposal 提供了良好的底线。
- Significance 中等——问题重要但发现的可预测性限制了 impact。
- Novelty 是限制上界的关键维度：核心贡献是"已有方法在新交叉点的首次验证"，属于 competent follow-up 而非 conceptual breakthrough。如果 positive result，审稿人大概率会说 "this confirms what we would have expected from the desirable difficulties literature"，这对顶会来说 novelty 不足以进入 top tier。
- 概率落在 25-35% 区间的上半部分（~30%）：idea 方向正确、gap 真实、设计严谨，但核心发现的 surprise value 不高。如果 negative result（scaffolding 意外无效）反而更有价值。

【主要风险】: 
1. **Novelty 不足 / "obvious next step" 风险**: Rani et al. 明确 call for 了这项研究，CFF 文献已提供了所有干预手段——审稿人可能认为这是 "executing on someone else's future work section" 而非独立的创新贡献。核心发现如果 positive，predictability 过高。
2. **效应复现风险**: 整个研究的根基建立在 Rani et al. N=67 无控制组的单一研究之上。如果 30 分钟 AI 辅助在 between-subjects 设计中不能产生可测量的 deskilling，核心比较就失效了。这不是 idea 层面的问题，而是 idea 的前提假设脆弱性。
```

---

**总结性说明**：这是一份在 HCI 框架下方法论上非常扎实、文献覆盖极其详尽的 proposal。其核心弱点不在执行层面（实验设计、统计 power 等都考虑周到），而在于 idea 内核——它是一个"显而易见的下一步"研究，组合了多个已有工作的元素但缺乏概念性突破。**但最致命的问题是投稿目标：CoRL 是 Conference on Robot Learning，与本 proposal 零交集，建议转投 CHI / CSCW / FAccT。**

Sources:
- [Rani et al. - Dialogues with AI Reduce Beliefs in Misinformation](https://arxiv.org/abs/2510.01537)
- [Althea - Human-AI Collaboration for Fact-Checking](https://arxiv.org/abs/2602.11161)
- [The Augmentation Trap](https://arxiv.org/abs/2604.03501)
- [AI Assistance Reduces Persistence](https://arxiv.org/pdf/2604.04721)
- [Adjust for Trust](https://arxiv.org/abs/2502.13321)
- [Cognitive Agency Surrender](https://arxiv.org/abs/2603.21735)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Overview](https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/)


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
  "promptId": "2447dbe5-067e-45f9-9f0a-33029aa5913d",
  "type": "user",
  "uuid": "38b3eade-57d4-4eaa-9dfe-80353cacd4c9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:01:17.393Z_

```json
{
  "parentUuid": "38b3eade-57d4-4eaa-9dfe-80353cacd4c9",
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
  "uuid": "7e5623c0-3e24-42ac-b550-51352232e69c",
  "timestamp": "2026-05-19T21:01:17.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:01:17.393Z_

```json
{
  "parentUuid": "7e5623c0-3e24-42ac-b550-51352232e69c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "97539991-d5b0-42b4-812d-22e17ac0d8ff",
  "timestamp": "2026-05-19T21:01:17.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 调研完成。我现在可以给出完整的入口评审。这里有一个 **极其关键的前置问题** 需要首先指出。  ---  ``` 【阶段】…",
  "leafUuid": "97539991-d5b0-42b4-812d-22e17ac0d8ff",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4"
}
````

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis of three peer reviews on deskilling prevention proposal",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:01:45.549Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews of this proposal and synthesize them as the Meta Judge.

First, let me extract the key data points:

**Reviewer 1:**
- Novelty: 中 (Medium)
- Significance: 强 (Strong)
- Related Work: 强 (Strong)
- CoRL probability: ~0%
- CHI probability: [25% - 38%] 中位 30%
- Key concerns: venue mismatch (fatal), trivial alternative threat, dose-effect risk (30 min exposure), positive result not surprising
  
Now looking at Reviewers 2 and 3, they're both converging on similar assessments: weak-to-medium novelty with medium significance and strong related work coverage. Both rate CoRL acceptance as essentially zero (1% median), while CHI sits around 30%. The consistent fatal flaw across all three is the venue mismatch, and there's a shared concern about the results being predictable given the trivial alternative condition and potential replication issues. around 30%, with virtually no variance across reviewers—all three independently converged on the same range of 25-38%. The key divergence emerges in how they rate Significance and Novelty, where Reviewer 1 sees stronger contributions than Reviewers 2 and 3, though this doesn't shift their collective verdict on venue appropriateness or core feasibility concerns.

Now I'm assessing the implementation requirements for this human subjects study—it's not computationally intensive but rather logistically demanding, with participant recruitment costs dominating the budget, minimal GPU needs for serving the language model, and a substantial timeline constraint from IRB review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97539991-d5b0-42b4-812d-22e17ac0d8ff",
  "isSidechain": false,
  "requestId": "req_011CbCbs2RTZqQi4HNtBfV9g",
  "type": "assistant",
  "uuid": "a45bd365-bfbe-4e97-b001-ba3cf042e613",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018w6ycUzEkRpt4cLvxbtLV3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20220,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3564,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3564,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20220
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

_source line 9 · 2026-05-19T21:02:43.363Z_

【阶段】: Meta Judge
【三次中位】: [30%, 30%, 30%]  std=0%
【共识维度】:
- **Venue Mismatch: 致命**（3/3 独立识别）— CoRL 是 Conference on Robot Learning，本 proposal 是纯 HCI/认知科学研究，零交集，必然 desk reject
- **Related Work: 强**（3/3 一致）— 文献覆盖详尽（15+ 篇核心引用），所有论文经验证真实存在且描述准确，差异化定位清晰
- **Trivial Alternative 威胁: 中等风险**（3/3 独立提出）— "independent judgment first"（Berger et al. 2603.29866）可能已足够防止大部分去技能化，缺少 minimal friction 对照条件无法排除此威胁
- **30 分钟暴露充分性: 中等风险**（3/3 独立提出）— Rani et al. 用 4 周纵向交互产生 15.3% 退化，1222-RCT 的 10 分钟效应来自简单认知任务（算术/阅读），30 分钟在信息评估这种复杂任务上能否产生可测量的 deskilling 完全未知
- **Positive Result 可预测性: 中等风险**（3/3 独立提出）— "scaffolding helps retention" 是 desirable difficulties 文献的直接推论，审稿人大概率认为 "I would have guessed this"
- **Novelty: 弱-中**（2/3 判弱-中，1/3 判中）— 核心贡献是已有元素（CFF 干预 + AI-withdrawal 设计 + 纵向随访 + 信任调节）的首次组合，属 "competent follow-up" 而非概念性突破
- **Significance: 中**（2/3 判中，1/3 判强）— 研究问题 timely 且重要，但发现的可预测性限制了 impact

【异常维度】:
- Reviewer 1 对 Significance 判"强"（其余两位判"中"）— Reviewer 1 更强调研究问题的时效性和 Rani et al. 的 explicit call，但 Reviewers 2&3 认为"确认性贡献"的 significance 应降档。2/3 共识为"中"，Reviewer 1 的"强"判定为 outlier，降权处理。
- Reviewer 1 对 Novelty 判"中"（其余两位判"弱-中"）— 同样为 outlier。Reviewer 1 在措辞中也承认"组合式 novelty 在 HCI 中可接受但不突出"，实质判断与"弱-中"差距不大。

【最终概率】: [0% - 2%] 中位 0%（CoRL 2026）；[24% - 35%] 中位 29%（假设投至 CHI/CSCW 等合适 HCI 会议）
【一致性】: 高（CoRL 概率和 HCI 概率均高度收敛，std≈0%）
【综合理由】:

**CoRL 维度**：三位审稿人独立且一致地识别出致命的 venue mismatch。CoRL 2026 的 scope 严格限定在 robot learning（manipulation, locomotion, sim-to-real, RL for robots 等），而本 proposal 是纯粹的 HCI/认知科学人因实验（Prolific 在线被试、信息评估任务、scaffolded friction 干预），与 CoRL 的所有 topic areas 零交集。这不是 borderline case——是完全不相关的学科。投稿 CoRL 会在 desk review 阶段被直接拒绝。三份评审对此判断完全一致，无需进一步讨论。

**假设正确 venue (CHI/CSCW) 的 idea 质量评估**：

三位审稿人在 CHI 概率上极度收敛（均给出中位 30%），这为最终估计提供了高置信度。综合 rubric 判决：

- **Related Work（强，3/3 共识）**：这是 proposal 最突出的优势，文献覆盖近乎 exhaustive，差异化定位清晰有力。但正如 Reviewer 3 精辟指出："当你需要写 7 个 Key distinction 段落来论证差异时，实际差异可能主要在于实验设计的排列组合"——Related Work 的强势反而暴露了 Novelty 的窄。

- **Novelty（弱-中，2/3 共识）**：核心贡献是"将 CFF/scaffolding 干预 + AI-withdrawal 设计 + 纵向随访 + 信任调节"首次组合在信息评估领域。每个组件都已有先例（CFF → Buçinca 2021; AI-withdrawal → 2604.04721; 纵向 scaffolding → Althea; trust-as-moderator → Adjust for Trust）。Rani et al. 论文本身就明确 call for 了这项研究，使其成为 "field 中最显而易见的下一步"。Metacognitive scripts 研究 (2602.20206) 已在编程领域展示了几乎相同的逻辑（scaffolded friction + AI-blackout）。这限制了概率上限至约 35%。

- **Significance（中，2/3 共识）**：AI deskilling 无疑是 timely 且重要的问题，但本 proposal 的贡献属于"确认性的"（验证已有理论预测）而非"开创性的"。Positive result 可预测性高，negative result 反而更有学术冲击力——但 proposal 未充分讨论 negative result 的理论含义。

- **关键风险的交叉验证**：trivial alternative 威胁和 30 分钟暴露充分性这两个风险被全部三位审稿人独立识别，属于高置信度信号。特别是 trivial alternative——如果 "independent judgment first" 这个简单操作就足以防止大部分 deskilling，那精心设计的 scaffolding 机制的增量价值可能微不足道，核心 contribution 将大打折扣。

最终中位从 30% 微调至 29%：三份评审均收敛于 30%，但按照"分歧时偏严"原则，Significance 维度 Reviewer 1 的"强"判定被降权后，整体画面略偏向更严格的评估。区间上界从 38%（Reviewer 1&3 的上界）收窄至 35%，因为 Novelty 弱-中 构成硬性天花板。

【建议】: 不推荐（投 CoRL 2026）；边缘（若转投 CHI/CSCW 2027 并按建议优化）

【实施评估】:
- **计算资源**: 极低。Qwen 3.5 27B 实验服务需 40-60 H100 GPU 小时（~$80-120 自托管）或 $50-80 通过 OpenRouter API。无需大规模计算集群。
- **数据需求**: 无需构建新数据集。信息评估任务改编自公开数据集（AVeriTeC/FEVER）。需设计 IRT 校准的平行题组（parallel forms），这是标准心理测量流程。
- **人工介入**: 高。需要 Prolific 平台招募 N≈480 被试，含 3 个时间点的纵向随访（即时、1 周、4 周）。预计被试补偿总成本 ~$9,760（含 Prolific 平台费和流失补偿）。需 IRB 审批（3-6 周不可压缩）。被试流失管理是关键风险（Rani et al. 流失率 36%）。
- **训练需求**: 无模型训练。使用现成的 Qwen 3.5 27B 做推理服务即可。
- **新 Benchmark**: 不需要。但需要设计和 IRT 校准信息评估任务的题目池，这本身需要一定的心理测量专业能力。
- **预估周期**: 4-5 个月（1 个月平台开发 + 任务设计 → 3-4 周 IRB 审批 → 2 周 pilot N=80 → 6 周主实验数据收集含 4 周随访 → 5 周分析写作）。**不可压缩瓶颈**：IRB 审批（3-6 周）和 4 周延迟随访窗口。总项目成本（不含人力）约 $10,000-11,000，以被试补偿为绝对主体。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a45bd365-bfbe-4e97-b001-ba3cf042e613",
  "isSidechain": false,
  "requestId": "req_011CbCbs2RTZqQi4HNtBfV9g",
  "type": "assistant",
  "uuid": "625dfd87-0264-4e16-baff-402906a4e499",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018w6ycUzEkRpt4cLvxbtLV3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20220,
      "cache_read_input_tokens": 16560,
      "output_tokens": 3564,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3564,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 20220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20220
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

````json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ 调研完成。我现在可以给出完整的入口评审。这里有一个 **极其关键的前置问题** 需要首先指出。  ---  ``` 【阶段】…",
  "leafUuid": "625dfd87-0264-4e16-baff-402906a4e499",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4"
}
````

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Meta Judge synthesis of three peer reviews on deskilling prevention proposal",
  "sessionId": "917b0c4a-fc44-4277-9e81-b3341d570fb4"
}
```

---
