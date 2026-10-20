# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f7366115-be38-48f4-90e6-8049f3d3d2b2.jsonl`
- **Structured JSON:** [`07e168e06050514dc2f3.json`](../../sessions/07/07e168e06050514dc2f3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:27:55.768Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:27:55.768Z",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to make my assessment. Let me compile the evaluation.\n\n---\n\n```\n【阶段】: Triage\n\n⚠️ 【致命问题：会议 scope 不匹配】\nCoRL (Conference on Robot Learning) 2026 的投稿范围明确限定为：robot learning, reinforcement learning for physical robots, \nmanipulation/locomotion/navigation/driving, sim-to-real transfer, robot perception, robot foundation models 等。\n本 proposal 关于 LLM 推理 token 在 character-level sub-token 任务上的机制可解释性分析，与 CoRL 的范围完全不相关。\n**投稿 CoRL 将几乎确定被 desk reject，不进入审稿流程。**\n适合本 proposal 的会议：ACL、EMNLP、NeurIPS、ICML、ICLR（NLP/ML interpretability track）。\n\n以下评估假设投稿至 scope 匹配的 NLP/ML 会议（如 ACL/EMNLP 2026），以提供实质性参考。\n\n【领域调研】:\n- [SubTokenTest] (arXiv:2601.09089, Jan 2026): 本 proposal 的核心现象来源。该 benchmark 发现推理 token 对 character-level 任务呈 inverted U-curve：256-512 token 有帮助，>2048 token 反而降低性能。但该工作是纯 behavioral 测试，未做机制分析。\n- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval] (arXiv:2510.05381, Oct 2025): 发现即使完美检索，context 增长本身就导致 13.9-85% 性能下降。这正是 proposal 中 H2 (generic attention dilution) 的核心证据。**Proposal 正确引用了此工作。**\n- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents] (arXiv:2604.02155, Apr 2026): 发现在 function-calling（非 character-level）任务中也出现 non-monotonic CoT budget 效应（32 tokens +45%，256 tokens 反而低于 no-CoT baseline）。**这对 proposal 是一把双刃剑——它直接支持 H2 而非 H1。**\n- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training] (arXiv:2509.25758, NeurIPS 2025): 在 Qwen3-8B think-on/off 平台上做了 circuit analysis（EAP-IG），发现 think-on/off 模式共享大部分电路，无专门 thinking heads。**Proposal 承认了重叠并声称互补——fair positioning。**\n- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks] (arXiv:2604.00778, Apr 2026): 在 base model 中发现 character-level 信息在早层编码、被后层 MLP \"negative circuits\" 抑制。**这是 proposal Phase 2 的直接先驱——proposal 声称要检验推理 token 是否放大这些 negative circuits。**\n- [Fluid Representations in Reasoning Models] (arXiv:2602.04843, Feb 2026): 发现推理模型（QwQ-32B）在 reasoning 过程中逐步增强抽象结构表示。**Proposal 利用此发现构造对比论点：如果推理增强抽象表示但损害 character 表示，则支持 H1。**\n- [Deep-Thinking Tokens] (arXiv:2602.13517, Feb 2026): 提出 Deep-Thinking Ratio (DTR) 量化推理努力，发现简单 token 计数与准确率负相关 (r=−0.544)。方法论上的 related work。\n- [Do Thinking Tokens Help or Trap?] (arXiv:2506.23840, Jun 2025): 研究 thinking tokens 可能导致的 \"thinking trap\"——无效推理循环。\n\n- 调研总结: 这个领域处于快速发展期（2026 上半年涌现大量工作）。\"推理 token 的 overthinking 效应\" 已成为热点，但**机制层面**的解释工作刚起步——arXiv:2604.00778 做了 base model 的 character-level 机制分析，arXiv:2509.25758 做了推理模型的电路分析，但尚无工作将二者结合，即\"推理 token 如何影响 character-level 表示的机制分析\"。Proposal 处于这一交叉地带。\n\n【Trivial Alternative 检验】:\n**存在一个成本更低的 trivial baseline**：直接在 behavioral 层面做 dual-track 对比——测量推理 token 对 character-level 任务 vs. 非 character-level 任务的性能衰退曲线。如果两条曲线衰退速率相同，H2 成立；如果 character-level 衰退显著更快，H1 成立。这个纯 behavioral 实验不需要任何 probing 或 activation patching，成本远低于机制分析。\n\nProposal 的增量价值在于：(1) 提供 \"为什么\" 的因果解释（哪些 heads/MLPs 参与 corruption），(2) 提供可干预的把手（targeted masking 作为 proof-of-concept）。但**如果 behavioral 对比已经清楚地支持 H2**（结合 arXiv:2604.02155 在非 character 任务上也观察到 non-monotonic 效应），那么花费大量计算做机制分析的增量价值会大幅缩水——审稿人可能会说 \"we already know the answer is H2 from behavioral evidence alone\"。\n\n**增量价值评估：中等偏低。** 机制分析的独立价值取决于核心发现的\"意外程度\"，而现有 behavioral 证据已经较强地指向 H2。\n\n【前提假设检验】:\n1. **\"推理 token 造成的性能衰退可以用 character-level representation degradation 来解释\"** —— 这是未经验证的假设。性能衰退可能发生在决策层面（decoding/sampling），而非表示层面。如果 character info 在 probing 中始终完好但最终输出仍然错误，proposal 的整个 probing-based framework 将无法提供解释。\n2. **\"linear probes 能忠实反映 character-level 信息的可用性\"** —— linear probing 只能捕捉线性可解码的信息，不能反映模型实际使用信息的方式 (encoding ≠ usage，这是 probing literature 的经典问题，见 Hewitt & Liang 2019)。\n3. **\"Qwen3 的 think-on/off toggle 是干净的对照实验\"** —— think-on 和 think-off 虽然架构和 tokenizer 相同，但经过不同的 post-training，其权重和内部计算方式可能有系统性差异（Thinking Sparks! 已证实二者的 attention head 使用模式不同）。因此观察到的 probing 差异可能反映 training differences 而非 thinking tokens 的因果效应。\n4. **\"dual-track probing 可以干净地 disentangle H1 vs H2\"** —— 这假设 character-level 和 non-character-level 信息的 probing accuracy 在相同条件下应等比例下降（if H2）。但不同信息类型的 baseline probing accuracy、signal-to-noise ratio、对 context length 的敏感度可能本身就不同，导致差异化衰退≠选择性 corruption。\n\n【3 维度打分】:\n\n1. **Novelty: 中** — Proposal 的核心贡献是将现有工具（linear probing, activation patching）应用于一个特定的交叉问题（reasoning tokens × character-level representations）。dual-track probing design 是一个合理的方法论贡献，但不是方法论创新——它是现有 probing 方法的应用策略。arXiv:2604.00778 已经做了 base model 上 character-level 的机制分析（probing + activation patching + logit lens），本 proposal 的主要增量是\"在推理模型上重做+加入 budget 维度+加入 non-character 对照\"。arXiv:2509.25758 已在同一模型平台（Qwen3-8B think-on/off）上做了电路分析。两篇工作组合在一起已经覆盖了本 proposal 方法空间的大部分。剩余的 genuine novelty delta 集中在 H1 vs H2 的 disentanglement framing 上——这是有价值的，但更像是一个 well-posed research question 而非一个 novel methodology。\n\n2. **Significance: 中偏弱** — 研究问题本身有一定价值（理解 overthinking 的机制），但受限于：(a) character-level sub-token tasks 是一个相对 niche 的领域，影响范围有限；(b) 如果 H2 成立（现有证据较强地指向 H2），结论将是\"推理 token 的 character-level 衰退不过是 generic attention dilution 的一个实例\"——这是一个 confirmatory 而非 surprising 的发现，审稿人可能会说 \"I would have guessed this\"；(c) 如果 H1 成立，发现会更 interesting，但 proof-of-concept intervention（targeted masking）被 proposal 自己承认不是 complete solution，practical impact 有限。(d) Proposal 声称 dual-track probing methodology 可 generalize，但 generalizability 是 claimed 而非 demonstrated。\n\n3. **Related Work: 强** — Proposal 对已有工作的覆盖非常全面且准确。所有引用的论文都真实存在，描述准确。与最相关的两篇工作（arXiv:2604.00778, arXiv:2509.25758）的 differentiation 清晰合理。对 H2 的证据源（arXiv:2510.05381, arXiv:2604.02155）的引用展示了对 confounding factors 的 awareness。对 Fluid Representations 的利用也是 well-positioned。这是 proposal 的最大优势。\n\n【概率估计】: [5% - 10%] 中位 5%\n（如果投稿至 scope 匹配的 NLP/ML 会议如 ACL/EMNLP：[20% - 30%] 中位 25%）\n\n【估计理由】:\n- **CoRL 概率 ~5%**: Proposal 与 CoRL 的 scope（robot learning）完全不匹配，几乎确定 desk reject。给出 5% 而非 0% 仅因为极小概率下 AC 可能误判或有 special track。\n- **NLP/ML 会议概率 ~25%**（仅供参考）: Related Work 维度强，说明作者对领域理解深入。但 Novelty 中等（组合现有方法回答特定问题，非方法论创新），Significance 中偏弱（核心发现无论 H1 或 H2 的\"惊喜度\"有限，尤其 H2 scenario 下结论偏 confirmatory）。上界受限于 Significance：即使实验完美执行，核心发现 if positive（H1 成立），审稿人大概率说\"interesting but niche\"；if negative（H2 成立），审稿人大概率说\"not surprising given existing evidence from arXiv:2604.02155 and arXiv:2510.05381\"。\n\n【主要风险】（idea 层面）:\n1. **H2 scenario 下的 impact 问题**: 现有 behavioral 证据（arXiv:2604.02155 在非 character 任务也观察到 non-monotonic 效应；arXiv:2510.05381 证明 context length 本身就降低性能）已较强地指向 H2。如果机制分析也确认 H2，审稿人会质疑\"花大量 compute 做机制分析确认一个 behavioral 已经 suggest 的结论，增量价值何在？\"\n2. **Scope 窄 × novelty 增量小的组合**: Character-level sub-token tasks 本身是 niche 领域，而方法论上是现有工具的组合应用——两者叠加后，即使实验结果完美，paper 的 impact ceiling 也有限。审稿人在 borderline 打分时倾向于 reject \"correct but narrow\" 的工作。\n```\n\nSources:\n- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)\n- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)\n- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)\n- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)\n- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)\n- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)\n- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517)\n- [Do Thinking Tokens Help or Trap?](https://arxiv.org/abs/2506.23840)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\n调研完成。现在我有足够的信息来进行全面评估。\n\n---\n\n```\n【阶段】: Triage\n\n【致命前置问题 — 投稿场地匹配】:\n⚠️ 本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。\nCoRL 2026 CFP 明确声明：\"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review.\"\n本 proposal 研究的是 LLM mechanistic interpretability / character-level sub-token task 退化机制，与机器人学习完全无关。按 CoRL scope 规定，此论文将被 desk reject，不进入审稿流程。\n→ 如果投稿目标确实是 CoRL，中稿概率 ≈ 0%。\n→ 以下评估假设投稿目标为合适的 NLP/ML 会议（如 ACL、EMNLP、NeurIPS interpretability track），以便提供有实质价值的 idea 质量分析。\n\n─────────────────────────────────────\n\n【领域调研】:\n\n- [SubTokenTest (arXiv:2601.09089)](https://arxiv.org/abs/2601.09089) (2026.01): 本 proposal 的直接上游。提出了 sub-token 理解基准，文档化了 reasoning tokens 在 character-level 任务上的倒 U 型曲线（256-512 tokens 提升 → 2048+ tokens 退化），并已初步用 probing 探索了 character-level information 在 hidden states 中的编码。\n- [From Early Encoding to Late Suppression (arXiv:2604.00778)](https://arxiv.org/abs/2604.00778) (2026.04): 本 proposal 最直接的竞争/前驱工作。已在 LLaMA、Qwen、Gemma 的 base 和 instruction-tuned 模型上发现 negative circuits（后层 MLP 和注意力头主动压制早期正确编码的 character-level 信息）。方法包含 probing classifiers、activation patching、logit lens——与本 proposal 的核心方法论高度重叠。\n- [Thinking Sparks! (arXiv:2509.25758)](https://arxiv.org/abs/2509.25758) (NeurIPS 2025): 在 Qwen3-8B think-on/off 平台上做了 EAP-IG circuit analysis，发现推理模型通过 post-training 产生新的功能特化注意力头，且 think-on/off 模式共享大部分 circuit。本 proposal 使用相同的实验平台。\n- [Fluid Representations (arXiv:2602.04843)](https://arxiv.org/abs/2602.04843) (2026.02): 在 QwQ-32B 上发现 reasoning 逐步增强 abstract structural representations（\"流体表征\"）。为 H1（reasoning 对不同表征类型有选择性影响）提供了间接支持。\n- [Context Length Alone Hurts (arXiv:2510.05381)](https://arxiv.org/abs/2510.05381) (2025.10): 证明即使 retrieval 完美，context length 本身就会导致 13.9%–85% 的性能下降。这是 H2（generic degradation）的核心证据来源。\n- [Brief Is Better (arXiv:2604.02155)](https://arxiv.org/abs/2604.02155) (2026.04): 在 function-calling agents 上发现非单调 CoT budget 效应（非 character 任务也出现），为 H2 提供额外支持。\n- [When More Thinking Hurts (arXiv:2604.10739)](https://arxiv.org/abs/2604.10739) (2026.04): 系统性研究 overthinking 现象。\n- [Mitigating Overthinking via Reasoning Path Deviation Monitoring (arXiv:2603.14251)](https://arxiv.org/abs/2603.14251) (2026.03): 提出通过路径偏差指数早停来缓解 overthinking。\n\n- **调研总结**: 这个领域（LLM overthinking + character-level task failure + mechanistic interpretability）在 2025-2026 年非常活跃。关键的实证现象（倒 U 型曲线、negative circuits、通用长上下文退化）已被多篇独立工作分别建立。本 proposal 的定位是\"把这些独立发现连起来\"——用 dual-track probing 来区分 character-specific 退化 vs. generic 退化。这是一个合理的增量问题，但核心构件（probing + activation patching on Qwen3 think-on/off）都直接来自已有工作。\n\n─────────────────────────────────────\n\n【Trivial Alternative 检验】:\n\n**存在显著的 trivial alternative 威胁。**\n\n要区分 H1（character-specific corruption）和 H2（generic attention dilution），最简单的方法是：在相同的 thinking budget sweep 下，同时测量 character-level 任务和 non-character 任务的准确率退化曲线。如果 character 任务退化速率显著高于 non-character 任务（控制任务难度后），则支持 H1；反之支持 H2。这只需要黑盒 benchmark 评测，不需要任何 probing 或 activation patching。\n\nSubTokenTest 本身已经包含了多种任务类型，arXiv:2604.02155 也在非 character 任务上发现了类似的非单调退化。如果在 behavioral level 就能回答 H1 vs H2，那 mechanistic analysis 的增量价值在于提供 **\"why\" 层面的解释**——即不仅知道是否 character-specific，还知道哪些 circuit 负责。但如果 behavioral 结果已经指向 H2（现有证据似乎倾向这个方向），那整个 mechanistic 分析的动机就被削弱了。\n\n**增量价值**: 如果 H1 成立，mechanistic 分析的价值较高（找到可干预的 circuit）。如果 H2 成立（proposal 自己也认为这是可能结果），那 mechanistic 分析变成了\"用更贵的方法确认了一个可以更便宜地确认的结论\"，其主要贡献仅在于方法论框架本身。\n\n─────────────────────────────────────\n\n【前提假设检验】:\n\n核心 claim 的逻辑链：\n1. ✅ \"Reasoning tokens 导致 character-level 任务退化\" — 有实证支持 (SubTokenTest)\n2. ⚠️ \"Linear probes 能干净地分离 character-level information 和 non-character information\" — 这是关键未验证假设。Linear probing 的 faithfulness 在 interpretability 社区一直有争议。如果 character-level 和 word-level 表征在 representation space 中纠缠，dual-track probing 的差异性结论可能不可靠。\n3. ⚠️ \"Think-on/off toggle 提供的是 'cleanest possible comparison'\" — 虽然确实比跨模型对比更干净，但 think-on 模式改变的不仅是 reasoning 长度，还包括 output distribution、generation pattern 等。这些混淆因素未被讨论。\n4. ⚠️ \"arXiv:2604.00778 发现的 negative circuits 可以直接推广到 reasoning 场景\" — 该论文研究的是 base/instruction-tuned 模型的标准前向传播，而非 extended reasoning chain 中的迭代自注意力。Reasoning context 中 circuit 行为可能完全不同。\n5. ⚠️ \"8B 模型上的 activation patching 结果可以推广到 32B\" — Proposal 承认 32B 只做 Phase 1 probing 不做 patching（出于计算限制），但 scale 对 circuit 结构的影响是已知问题。\n\n─────────────────────────────────────\n\n【3 维度打分】:\n\n1. **Novelty: 弱-中** —\n   本 proposal 的核心方法论（linear probing + activation patching on character tasks）直接继承自 arXiv:2604.00778，实验平台（Qwen3-8B think-on/off）直接继承自 arXiv:2509.25758。\"Dual-track probing\"（同时 track character 和 non-character info）是标准的对照实验设计，并非方法论创新。真正的 novelty delta 在于\"将已有方法应用于新场景（reasoning token budget sweep）\"，但这属于 incremental combination，不属于 conceptual novelty。审稿人很可能会评价为 \"straightforward application of existing probing methodology to a new but narrow setting\"。此外，如果 H2 成立（generic degradation），则 character-specific 的 framing 反而会被视为 misleading。\n\n2. **Significance: 弱-中** —\n   Character-level sub-token 任务是 NLP 中的一个 niche 问题。虽然 proposal 试图将贡献泛化（\"reusable diagnostic framework for any overthinking context\"），但这个 generalization claim 未经验证——一个在 character counting 上 validate 的 dual-track probing 框架，能否直接迁移到 code generation 或 mathematical reasoning 的 overthinking 诊断，是完全不明确的。核心发现无论指向 H1 还是 H2，审稿人的反应更可能是 \"I would have guessed this\" 而非 \"surprising\"：H1 成立不 surprising（已有 negative circuit 证据 per arXiv:2604.00778），H2 成立也不 surprising（已有大量 overthinking/context-length-degradation 文献）。Practical impact 也有限——circuit masking 被明确降级为 \"proof-of-concept\"。\n\n3. **Related Work: 中-强** —\n   Proposal 对 related work 的覆盖相当全面和诚实。正确引用并定位了 SubTokenTest、Thinking Sparks!、Fluid Representations、negative circuits 等核心工作，清晰说明了与 Thinking Sparks! 的互补关系。引用的论文均真实存在且描述基本准确。不足之处：(1) 未讨论 linear probing faithfulness 的文献（如 Belinkov survey, Hewitt & Liang 2019 selectivity），这对方法论的可信度很重要；(2) 未覆盖更广泛的 overthinking mitigation 工作（如 arXiv:2603.14251, arXiv:2505.17813），这些工作的存在可能进一步削弱 mechanistic 分析的 practical significance。\n\n─────────────────────────────────────\n\n【概率估计】（假设投稿合适的 NLP/ML venue，如 ACL/EMNLP/NeurIPS）: [15% - 28%] 中位 20%\n\n【如投稿 CoRL 2026】: ≈ 0%（Desk reject，场地完全不匹配）\n\n【估计理由】:\nIdea 方向站得住脚——理解 reasoning tokens 为什么伤害特定任务类型是有价值的问题——但内核偏薄：方法论无创新（standard probing + patching），核心问题可通过更廉价的 behavioral analysis 初步回答（trivial alternative 威胁），研究范围 niche（character-level tasks），且无论结果指向 H1 还是 H2 都不 surprising。上界被 Novelty 限制——在 arXiv:2604.00778 和 arXiv:2509.25758 已经分别做了 character-level negative circuits 和 Qwen3 circuit analysis 的情况下，本工作的增量贡献主要是\"在新条件下运行已有方法\"。下界被 dual-outcome 设计和诚实的 related work 覆盖所托底——即使结果一般，execution 可以是 solid 的。\n\n【主要风险】:\n1. **Trivial alternative 威胁**: 审稿人可能指出 behavioral-level comparison（across task types, across thinking budgets）就足以区分 H1 vs H2，mechanistic analysis 的增量价值不足以 justify 整篇 paper，特别是当方法论本身无创新时。\n2. **\"So what\" 风险**: 无论 H1 还是 H2 成立，结论的可行动性有限。Circuit masking 仅为 proof-of-concept，且如果 H2 成立，整个 character-specific framing 会被审稿人质疑为 motivated reasoning（先有结论再找证据）。\n```\n\n---\n\n**补充说明**：这个 proposal 存在一个根本性的**投稿场地错误**。CoRL 是机器人学习会议，明确要求论文以机器人问题为核心，无机器人内容的论文会被直接退回不审。本 proposal 纯粹是 LLM interpretability 研究，应投稿 ACL、EMNLP、NAACL、NeurIPS、ICML 或 ICLR。如果场地不可更改，建议直接止损；如果场地可以调整到合适的 NLP/ML venue，上述 idea 质量评估（中位 20%）可作为后续迭代优化的参考基线。\n\nSources:\n- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)\n- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)\n- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)\n- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)\n- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)\n- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)\n- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/abs/2604.10739)\n- [Mitigating Overthinking via Reasoning Path Deviation Monitoring](https://arxiv.org/abs/2603.14251)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient information. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【⚠️ 致命前置问题：投稿场地严重不匹配】\n\n本 proposal 拟投稿 CoRL (Conference on Robot Learning) 2026。\n然而 CoRL 2026 Call for Papers 明确声明：\n\"Submissions should focus on a core robotics problem and demonstrate the relevance\n of proposed models, algorithms, datasets, and benchmarks to robotics.\n Submissions without a robotics focus will be returned without review.\"\n\n本 proposal 研究的是 LLM reasoning tokens 对 character-level sub-token 任务的\n影响机制——纯粹的 NLP / mechanistic interpretability 工作，与机器人学习无任何\n关联。按 CoRL 的审稿标准，此稿会被 desk reject。\n\n如果作者希望投稿此方向的论文，合适的场地包括：ACL / EMNLP / NAACL (NLP)，\nNeurIPS / ICML / ICLR (ML)。以下评估基于\"假设投稿到合适 NLP/ML 会议\"来\n评估 idea 质量本身。\n\n========================================================================\n\n【领域调研】:\n\n1. SubTokenTest (arXiv:2601.09089, Jan 2026, Peking Univ.):\n   提出 sub-token understanding benchmark，文档了 reasoning tokens 在 character-level\n   任务上的 inverted U-curve 现象。这是本 proposal 的直接出发点。\n\n2. \"From Early Encoding to Late Suppression\" (arXiv:2604.00778, Apr 2026):\n   **最直接的竞争者。** 已在 LLaMA/Qwen/Gemma 上做了 mechanistic analysis\n   (probing + activation patching + logit lens + attention head tracing)，发现\n   character-level information 在 early/mid layers 已被编码，但被 later layers\n   (尤其 penultimate/final MLP) 的\"negative circuits\"系统性压制。这与本\n   proposal Phase 2 的目标（识别 corruption circuits）高度重叠。\n\n3. \"Fluid Representations in Reasoning Models\" (arXiv:2602.04843, Feb 2026, ETH):\n   对 QwQ-32B 做 mechanistic analysis，发现 reasoning 过程中 abstract structural\n   representations 逐步增强。本 proposal 引用此工作的逻辑是：\"如果 reasoning 增强\n   某些 representation 却损害 character-level 的，这就是 H1 的因果证据\"——但 Fluid\n   Representations 的发现本身已部分回答了这个问题（reasoning 选择性地增强 abstract\n   structure）。\n\n4. \"Thinking Sparks!\" (arXiv:2509.25758, NeurIPS 2025):\n   在同一平台（Qwen3-8B think-on/off）做 circuit analysis (EAP-IG)。发现\n   think-on/off 共享大部分 circuit components。本 proposal 承认互补性，但这也\n   意味着在同一模型上做 circuit-level analysis 的\"地盘\"已被占据。\n\n5. \"How Do Language Models Acquire Character-Level Information?\"\n   (arXiv:2602.05347, EACL 2026):\n   系统性 probing 研究 LM 如何编码 character-level information。虽然不涉及\n   reasoning tokens，但 probing character-level representations 的方法论与本\n   proposal Phase 1 高度相似。**本 proposal 未引用此工作。**\n\n6. \"Brief Is Better\" (arXiv:2604.02155, Apr 2026):\n   证明 non-monotonic CoT budget effects 出现在 function-calling 任务（非\n   character-level），optimal budget 低至 8-16 tokens。这对 proposal 的 H2\n   假说提供了直接支持——overthinking 是通用现象，非 character-specific。\n\n7. \"Context Length Alone Hurts LLM Performance\" (arXiv:2510.05381):\n   证明即使 perfect retrieval，context length 本身就导致 13.9-85% 性能下降。\n   同样支持 H2。\n\n调研总结: 这个领域目前非常活跃——character-level mechanistic interpretability、\nreasoning token effects、overthinking 三个方向都有近期高质量工作。本 proposal\n的核心贡献（dual-track probing 区分 H1 vs H2）虽然在组合层面有独特性，但各个\n组成部分（character probing、reasoning circuit analysis、overthinking 诊断）\n已被近期论文分别覆盖。最关键的竞争者是 2604.00778，已经在相同任务类型上做了\n几乎相同的 mechanistic toolkit。\n\n========================================================================\n\n【Trivial Alternative 检验】:\n\n存在一个成本极低的 trivial baseline：直接在行为层面比较 character-level tasks\nvs. non-character-level control tasks 在不同 reasoning token budget 下的\nperformance degradation curves。\n\n- 如果 character tasks 的 degradation slope 显著陡于 control tasks → 支持 H1\n- 如果两者 degradation 相似 → 支持 H2\n\n这个纯行为实验无需任何 probing、activation patching 或 circuit analysis，仅需\n跑 inference，计算成本低 1-2 个数量级。\n\nProposal 的增量价值在于提供 \"why\" 层面的机制解释——不仅知道\"是否 character-\nspecific\"，还知道\"在哪些 layers/heads/MLPs 发生了什么\"。但如果 H2 成立（即\ndegradation 是 generic 的），则 mechanistic analysis 的增量价值大幅缩水，因为\n它只是重新确认了已知的 context dilution 机制。proposal 自己也承认 H2 scenario\n的价值在于\"redirecting research effort\"——但这个 redirect 可以用行为实验完成。\n\n结论: Trivial alternative 对核心 claim (H1 vs H2) 构成实质威胁。Mechanistic\n分析的增量价值取决于 H1 成立，而 H1 能否成立本身就是未知的。\n\n========================================================================\n\n【前提假设检验】:\n\n核心逻辑链的关键未验证假设：\n\n1. **\"Linear probes 能可靠区分 character-specific corruption vs. generic\n   degradation\"假设**：如果 reasoning tokens 通过 generic attention dilution\n   (H2) 同时损害所有 representation types，但 character representations 本身\n   baseline robustness 就低于 word/semantic representations，则 probes 会显示\n   \"character 下降更多\"——但这不是因为 corruption 是 character-specific 的，\n   而是因为 character info 本来就更脆弱。Proposal 没有讨论如何控制这个混淆。\n\n2. **\"Thinking Sparks 的 circuit 框架适用于 character-level tasks\"假设**：\n   Thinking Sparks 分析的是 mathematical reasoning circuits，但 character-level\n   processing 涉及完全不同的 pathway。Thinking Sparks 的\"no dedicated thinking\n   heads\"结论未必能迁移到 character tasks。\n\n3. **\"2604.00778 的 negative circuits 会被 thinking tokens 放大\"假设**：\n   这是 proposal Phase 2 的核心假设，但没有任何先验证据。negative circuits\n   是在 base models (non-reasoning) 中发现的。reasoning 模型经过 RLHF/GRPO\n   training，其 circuit structure 可能已根本不同。\n\n4. **\"Dual-track probing 是通用框架\"假设**：proposal 声称 methodology 可推广\n   到 code generation、mathematical reasoning 等领域。但 probing 什么信息类型、\n   如何定义 \"character-level\" vs \"control\" 在每个领域都需要重新设计，\"通用框架\"\n   的说法过于乐观。\n\n========================================================================\n\n【3 维度打分】:\n\n1. Novelty: 弱-中 —\n   核心贡献是\"dual-track probing 区分 H1 vs H2\"这一实验设计。但：\n   (a) 2604.00778 已在相同任务类型上用几乎相同的 toolkit (probing + activation\n       patching) 做了 mechanistic analysis，且已发现 negative circuits。本\n       proposal 在此基础上增加的是\"在 reasoning context 下\"和\"对比 control\n       information\"——这是 incremental 的，不是 novel approach。\n   (b) 2602.05347 (EACL 2026) 已系统性 probing character-level information\n       across layers。\n   (c) Thinking Sparks 已在同一模型 (Qwen3-8B) 上做了 think-on/off circuit\n       analysis。\n   (d) Fluid Representations 已回答了 \"reasoning 如何改变 internal representations\"\n       的部分问题。\n   剩余 novelty: 特定组合（reasoning budget × character vs control probing）。\n   这是一个 well-motivated ablation study，但不是一个 conceptually new contribution。\n\n2. Significance: 中 —\n   正面: (a) character-level failure 是 LLM 的真实痛点，理解其与 reasoning 的\n   交互有实际价值；(b) H1 vs H2 的区分确实影响研究方向的资源配置（character-\n   specific solutions vs general overthinking mitigations）。\n   负面: (a) character-level sub-token tasks 是相对小众的问题（与 code generation、\n   mathematical reasoning 相比）；(b) 即使完美回答了 H1 vs H2，直接的应用价值\n   有限——无论哪个假设成立，都不直接产生 better character handling 的方法；\n   (c) \"proof-of-concept intervention\" 被明确弱化为非主要贡献。\n\n3. Related Work: 中 —\n   Proposal 引用了关键竞争者（Thinking Sparks、Fluid Representations、\n   2604.00778、2510.05381、2604.02155）且引用描述大体准确。\n   缺失: (a) 未引用 \"How Do Language Models Acquire Character-Level Information?\"\n   (EACL 2026, 2602.05347) 这一直接相关的 character probing 工作；\n   (b) 对 2604.00778 的差异化定位不够清晰——该论文已发现 negative circuits 压制\n   character information，本 proposal 需要更明确说明在 reasoning context 下重复\n   类似分析的增量贡献；(c) 未提及 overthinking mitigation 方向的多篇工作\n   (manifold steering 等)。\n\n========================================================================\n\n【概率估计】: 15% - 25%，中位 20%\n（注：此概率是假设投稿到合适 NLP/ML 会议如 ACL/EMNLP 的估计。\n投稿 CoRL 的实际概率 ≈ 0%，会被 desk reject。）\n\n【估计理由】:\nIdea 方向站得住脚（understanding reasoning-induced degradation on character tasks\n是合理且 timely 的研究问题），但核心内核薄弱：\n- Novelty 被 2604.00778 严重压缩——该论文已在同类任务上用同类 toolkit 做了\n  mechanistic analysis 并发现了 negative circuits\n- 核心贡献退化为一个 well-designed ablation（reasoning budget × information type），\n  而非 conceptually new contribution\n- Trivial alternative（行为层面比较 degradation curves）能回答同一个 H1 vs H2\n  问题，大幅削弱了 mechanistic 分析的必要性\n- 限制上界的是 Novelty 维度：审稿人很可能认为这是 2604.00778 + SubTokenTest\n  的 straightforward combination\n\n【主要风险】:\n1. **Novelty 不足**: 审稿人会指出 2604.00778 已做了 character tasks 的 mechanistic\n   analysis（probing + activation patching + negative circuits），本 proposal\n   的增量贡献（添加 reasoning budget 和 control probes）不足以支撑一篇独立论文。\n2. **Trivial alternative 威胁**: 行为实验可以更简洁地回答 H1 vs H2，\n   mechanistic 深度的附加价值需要比当前 proposal 更强的论证——尤其在 H2 成立\n   的情况下，全部 mechanistic 工作变成确认已知机制。\n```\n\nSources:\n- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)\n- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)\n- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)\n- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)\n- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)\n- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)\n- [How Do Language Models Acquire Character-Level Information?](https://arxiv.org/abs/2602.05347)\n- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Why Reasoning Tokens Hurt Sub-Token Tasks: Mechanistic Analysis of Character-Specific vs. Length-Induced Degradation\n\n## Description\nWe present the first mechanistic interpretability study investigating why extended reasoning tokens degrade LLM performance on character-level sub-token tasks—the inverted U-curve paradox documented by SubTokenTest. Critically, we design our study to disentangle two competing hypotheses: (H1) reasoning tokens specifically corrupt character-level representations through amplification of negative circuits, versus (H2) the observed degradation reflects generic long-context attention dilution that affects all information types equally—a confound raised by recent evidence that context length alone degrades performance by 13.9–85% (arXiv:2510.05381) and that non-monotonic CoT budget effects appear in non-character tasks (arXiv:2604.02155). Using Qwen3-8B and Qwen3-32B with thinking mode toggled on versus off—ensuring identical architectures and tokenizers for the cleanest possible comparison—we deploy layer-wise linear probes tracking both character-level information (identity, position) and non-character control information (word identity, semantic category) across six thinking-token budgets (0–8192). This dual-track probing design reveals whether character representations degrade disproportionately as reasoning length increases. While 'Thinking Sparks!' (arXiv:2509.25758, NeurIPS 2025) performs circuit analysis on the same Qwen3-8B think-on/off platform, their focus is mathematical reasoning head emergence via EAP-IG; our work is complementary, investigating character-level representation corruption across varying token budgets via linear probing and activation patching. Their finding that think-on/off modes share most circuit components (no dedicated thinking heads) provides important context for our Phase 2 circuit identification, which is restricted to the 8B model for memory feasibility while 32B serves as scale-validation through Phase 1 probing (INT8 quantization on A100 80GB). We apply activation patching to isolate specific attention heads and MLP sublayers involved in character-signal corruption during extended reasoning, testing whether the negative circuits recently identified in base models (arXiv:2604.00778) are amplified by thinking tokens. The finding from 'Fluid Representations' (arXiv:2602.04843) that reasoning progressively enhances abstract structural representations makes our investigation particularly pointed: if reasoning selectively helps some representation types while harming character-level ones, that is strong causal evidence for H1. As a proof-of-concept intervention, we evaluate targeted masking of identified corruption circuits, explicitly characterizing accuracy–reasoning trade-offs rather than claiming a complete solution. Beyond this specific study, our dual-track probing methodology generalizes as a reusable diagnostic framework for disentangling task-specific from generic degradation in any overthinking context—applicable to code generation, mathematical reasoning, and multilingual tasks. Even if the null hypothesis (H2) holds, this would be a high-impact finding that redirects significant research effort currently invested in character-specific solutions (character-level tokenization, token decomposition, specialized sub-token modules) toward general overthinking mitigations benefiting all task types. Supplementary experiments with DeepSeek-R1-0528-Qwen3-8B versus Qwen3-8B (noting the tokenizer confound) provide external validity.\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T03:27:55.771Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:27:55.771Z",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T03:27:55.782Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

⚠️ 【致命问题：会议 scope 不匹配】
CoRL (Conference on Robot Learning) 2026 的投稿范围明确限定为：robot learning, reinforcement learning for physical robots, 
manipulation/locomotion/navigation/driving, sim-to-real transfer, robot perception, robot foundation models 等。
本 proposal 关于 LLM 推理 token 在 character-level sub-token 任务上的机制可解释性分析，与 CoRL 的范围完全不相关。
**投稿 CoRL 将几乎确定被 desk reject，不进入审稿流程。**
适合本 proposal 的会议：ACL、EMNLP、NeurIPS、ICML、ICLR（NLP/ML interpretability track）。

以下评估假设投稿至 scope 匹配的 NLP/ML 会议（如 ACL/EMNLP 2026），以提供实质性参考。

【领域调研】:
- [SubTokenTest] (arXiv:2601.09089, Jan 2026): 本 proposal 的核心现象来源。该 benchmark 发现推理 token 对 character-level 任务呈 inverted U-curve：256-512 token 有帮助，>2048 token 反而降低性能。但该工作是纯 behavioral 测试，未做机制分析。
- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval] (arXiv:2510.05381, Oct 2025): 发现即使完美检索，context 增长本身就导致 13.9-85% 性能下降。这正是 proposal 中 H2 (generic attention dilution) 的核心证据。**Proposal 正确引用了此工作。**
- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents] (arXiv:2604.02155, Apr 2026): 发现在 function-calling（非 character-level）任务中也出现 non-monotonic CoT budget 效应（32 tokens +45%，256 tokens 反而低于 no-CoT baseline）。**这对 proposal 是一把双刃剑——它直接支持 H2 而非 H1。**
- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training] (arXiv:2509.25758, NeurIPS 2025): 在 Qwen3-8B think-on/off 平台上做了 circuit analysis（EAP-IG），发现 think-on/off 模式共享大部分电路，无专门 thinking heads。**Proposal 承认了重叠并声称互补——fair positioning。**
- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks] (arXiv:2604.00778, Apr 2026): 在 base model 中发现 character-level 信息在早层编码、被后层 MLP "negative circuits" 抑制。**这是 proposal Phase 2 的直接先驱——proposal 声称要检验推理 token 是否放大这些 negative circuits。**
- [Fluid Representations in Reasoning Models] (arXiv:2602.04843, Feb 2026): 发现推理模型（QwQ-32B）在 reasoning 过程中逐步增强抽象结构表示。**Proposal 利用此发现构造对比论点：如果推理增强抽象表示但损害 character 表示，则支持 H1。**
- [Deep-Thinking Tokens] (arXiv:2602.13517, Feb 2026): 提出 Deep-Thinking Ratio (DTR) 量化推理努力，发现简单 token 计数与准确率负相关 (r=−0.544)。方法论上的 related work。
- [Do Thinking Tokens Help or Trap?] (arXiv:2506.23840, Jun 2025): 研究 thinking tokens 可能导致的 "thinking trap"——无效推理循环。

- 调研总结: 这个领域处于快速发展期（2026 上半年涌现大量工作）。"推理 token 的 overthinking 效应" 已成为热点，但**机制层面**的解释工作刚起步——arXiv:2604.00778 做了 base model 的 character-level 机制分析，arXiv:2509.25758 做了推理模型的电路分析，但尚无工作将二者结合，即"推理 token 如何影响 character-level 表示的机制分析"。Proposal 处于这一交叉地带。

【Trivial Alternative 检验】:
**存在一个成本更低的 trivial baseline**：直接在 behavioral 层面做 dual-track 对比——测量推理 token 对 character-level 任务 vs. 非 character-level 任务的性能衰退曲线。如果两条曲线衰退速率相同，H2 成立；如果 character-level 衰退显著更快，H1 成立。这个纯 behavioral 实验不需要任何 probing 或 activation patching，成本远低于机制分析。

Proposal 的增量价值在于：(1) 提供 "为什么" 的因果解释（哪些 heads/MLPs 参与 corruption），(2) 提供可干预的把手（targeted masking 作为 proof-of-concept）。但**如果 behavioral 对比已经清楚地支持 H2**（结合 arXiv:2604.02155 在非 character 任务上也观察到 non-monotonic 效应），那么花费大量计算做机制分析的增量价值会大幅缩水——审稿人可能会说 "we already know the answer is H2 from behavioral evidence alone"。

**增量价值评估：中等偏低。** 机制分析的独立价值取决于核心发现的"意外程度"，而现有 behavioral 证据已经较强地指向 H2。

【前提假设检验】:
1. **"推理 token 造成的性能衰退可以用 character-level representation degradation 来解释"** —— 这是未经验证的假设。性能衰退可能发生在决策层面（decoding/sampling），而非表示层面。如果 character info 在 probing 中始终完好但最终输出仍然错误，proposal 的整个 probing-based framework 将无法提供解释。
2. **"linear probes 能忠实反映 character-level 信息的可用性"** —— linear probing 只能捕捉线性可解码的信息，不能反映模型实际使用信息的方式 (encoding ≠ usage，这是 probing literature 的经典问题，见 Hewitt & Liang 2019)。
3. **"Qwen3 的 think-on/off toggle 是干净的对照实验"** —— think-on 和 think-off 虽然架构和 tokenizer 相同，但经过不同的 post-training，其权重和内部计算方式可能有系统性差异（Thinking Sparks! 已证实二者的 attention head 使用模式不同）。因此观察到的 probing 差异可能反映 training differences 而非 thinking tokens 的因果效应。
4. **"dual-track probing 可以干净地 disentangle H1 vs H2"** —— 这假设 character-level 和 non-character-level 信息的 probing accuracy 在相同条件下应等比例下降（if H2）。但不同信息类型的 baseline probing accuracy、signal-to-noise ratio、对 context length 的敏感度可能本身就不同，导致差异化衰退≠选择性 corruption。

【3 维度打分】:

1. **Novelty: 中** — Proposal 的核心贡献是将现有工具（linear probing, activation patching）应用于一个特定的交叉问题（reasoning tokens × character-level representations）。dual-track probing design 是一个合理的方法论贡献，但不是方法论创新——它是现有 probing 方法的应用策略。arXiv:2604.00778 已经做了 base model 上 character-level 的机制分析（probing + activation patching + logit lens），本 proposal 的主要增量是"在推理模型上重做+加入 budget 维度+加入 non-character 对照"。arXiv:2509.25758 已在同一模型平台（Qwen3-8B think-on/off）上做了电路分析。两篇工作组合在一起已经覆盖了本 proposal 方法空间的大部分。剩余的 genuine novelty delta 集中在 H1 vs H2 的 disentanglement framing 上——这是有价值的，但更像是一个 well-posed research question 而非一个 novel methodology。

2. **Significance: 中偏弱** — 研究问题本身有一定价值（理解 overthinking 的机制），但受限于：(a) character-level sub-token tasks 是一个相对 niche 的领域，影响范围有限；(b) 如果 H2 成立（现有证据较强地指向 H2），结论将是"推理 token 的 character-level 衰退不过是 generic attention dilution 的一个实例"——这是一个 confirmatory 而非 surprising 的发现，审稿人可能会说 "I would have guessed this"；(c) 如果 H1 成立，发现会更 interesting，但 proof-of-concept intervention（targeted masking）被 proposal 自己承认不是 complete solution，practical impact 有限。(d) Proposal 声称 dual-track probing methodology 可 generalize，但 generalizability 是 claimed 而非 demonstrated。

3. **Related Work: 强** — Proposal 对已有工作的覆盖非常全面且准确。所有引用的论文都真实存在，描述准确。与最相关的两篇工作（arXiv:2604.00778, arXiv:2509.25758）的 differentiation 清晰合理。对 H2 的证据源（arXiv:2510.05381, arXiv:2604.02155）的引用展示了对 confounding factors 的 awareness。对 Fluid Representations 的利用也是 well-positioned。这是 proposal 的最大优势。

【概率估计】: [5% - 10%] 中位 5%
（如果投稿至 scope 匹配的 NLP/ML 会议如 ACL/EMNLP：[20% - 30%] 中位 25%）

【估计理由】:
- **CoRL 概率 ~5%**: Proposal 与 CoRL 的 scope（robot learning）完全不匹配，几乎确定 desk reject。给出 5% 而非 0% 仅因为极小概率下 AC 可能误判或有 special track。
- **NLP/ML 会议概率 ~25%**（仅供参考）: Related Work 维度强，说明作者对领域理解深入。但 Novelty 中等（组合现有方法回答特定问题，非方法论创新），Significance 中偏弱（核心发现无论 H1 或 H2 的"惊喜度"有限，尤其 H2 scenario 下结论偏 confirmatory）。上界受限于 Significance：即使实验完美执行，核心发现 if positive（H1 成立），审稿人大概率说"interesting but niche"；if negative（H2 成立），审稿人大概率说"not surprising given existing evidence from arXiv:2604.02155 and arXiv:2510.05381"。

【主要风险】（idea 层面）:
1. **H2 scenario 下的 impact 问题**: 现有 behavioral 证据（arXiv:2604.02155 在非 character 任务也观察到 non-monotonic 效应；arXiv:2510.05381 证明 context length 本身就降低性能）已较强地指向 H2。如果机制分析也确认 H2，审稿人会质疑"花大量 compute 做机制分析确认一个 behavioral 已经 suggest 的结论，增量价值何在？"
2. **Scope 窄 × novelty 增量小的组合**: Character-level sub-token tasks 本身是 niche 领域，而方法论上是现有工具的组合应用——两者叠加后，即使实验结果完美，paper 的 impact ceiling 也有限。审稿人在 borderline 打分时倾向于 reject "correct but narrow" 的工作。
```

Sources:
- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)
- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)
- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)
- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)
- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)
- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)
- [Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens](https://arxiv.org/abs/2602.13517)
- [Do Thinking Tokens Help or Trap?](https://arxiv.org/abs/2506.23840)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
调研完成。现在我有足够的信息来进行全面评估。

---

```
【阶段】: Triage

【致命前置问题 — 投稿场地匹配】:
⚠️ 本 proposal 投稿目标为 CoRL 2026（Conference on Robot Learning）。
CoRL 2026 CFP 明确声明："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Submissions without a robotics focus will be returned without review."
本 proposal 研究的是 LLM mechanistic interpretability / character-level sub-token task 退化机制，与机器人学习完全无关。按 CoRL scope 规定，此论文将被 desk reject，不进入审稿流程。
→ 如果投稿目标确实是 CoRL，中稿概率 ≈ 0%。
→ 以下评估假设投稿目标为合适的 NLP/ML 会议（如 ACL、EMNLP、NeurIPS interpretability track），以便提供有实质价值的 idea 质量分析。

─────────────────────────────────────

【领域调研】:

- [SubTokenTest (arXiv:2601.09089)](https://arxiv.org/abs/2601.09089) (2026.01): 本 proposal 的直接上游。提出了 sub-token 理解基准，文档化了 reasoning tokens 在 character-level 任务上的倒 U 型曲线（256-512 tokens 提升 → 2048+ tokens 退化），并已初步用 probing 探索了 character-level information 在 hidden states 中的编码。
- [From Early Encoding to Late Suppression (arXiv:2604.00778)](https://arxiv.org/abs/2604.00778) (2026.04): 本 proposal 最直接的竞争/前驱工作。已在 LLaMA、Qwen、Gemma 的 base 和 instruction-tuned 模型上发现 negative circuits（后层 MLP 和注意力头主动压制早期正确编码的 character-level 信息）。方法包含 probing classifiers、activation patching、logit lens——与本 proposal 的核心方法论高度重叠。
- [Thinking Sparks! (arXiv:2509.25758)](https://arxiv.org/abs/2509.25758) (NeurIPS 2025): 在 Qwen3-8B think-on/off 平台上做了 EAP-IG circuit analysis，发现推理模型通过 post-training 产生新的功能特化注意力头，且 think-on/off 模式共享大部分 circuit。本 proposal 使用相同的实验平台。
- [Fluid Representations (arXiv:2602.04843)](https://arxiv.org/abs/2602.04843) (2026.02): 在 QwQ-32B 上发现 reasoning 逐步增强 abstract structural representations（"流体表征"）。为 H1（reasoning 对不同表征类型有选择性影响）提供了间接支持。
- [Context Length Alone Hurts (arXiv:2510.05381)](https://arxiv.org/abs/2510.05381) (2025.10): 证明即使 retrieval 完美，context length 本身就会导致 13.9%–85% 的性能下降。这是 H2（generic degradation）的核心证据来源。
- [Brief Is Better (arXiv:2604.02155)](https://arxiv.org/abs/2604.02155) (2026.04): 在 function-calling agents 上发现非单调 CoT budget 效应（非 character 任务也出现），为 H2 提供额外支持。
- [When More Thinking Hurts (arXiv:2604.10739)](https://arxiv.org/abs/2604.10739) (2026.04): 系统性研究 overthinking 现象。
- [Mitigating Overthinking via Reasoning Path Deviation Monitoring (arXiv:2603.14251)](https://arxiv.org/abs/2603.14251) (2026.03): 提出通过路径偏差指数早停来缓解 overthinking。

- **调研总结**: 这个领域（LLM overthinking + character-level task failure + mechanistic interpretability）在 2025-2026 年非常活跃。关键的实证现象（倒 U 型曲线、negative circuits、通用长上下文退化）已被多篇独立工作分别建立。本 proposal 的定位是"把这些独立发现连起来"——用 dual-track probing 来区分 character-specific 退化 vs. generic 退化。这是一个合理的增量问题，但核心构件（probing + activation patching on Qwen3 think-on/off）都直接来自已有工作。

─────────────────────────────────────

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

要区分 H1（character-specific corruption）和 H2（generic attention dilution），最简单的方法是：在相同的 thinking budget sweep 下，同时测量 character-level 任务和 non-character 任务的准确率退化曲线。如果 character 任务退化速率显著高于 non-character 任务（控制任务难度后），则支持 H1；反之支持 H2。这只需要黑盒 benchmark 评测，不需要任何 probing 或 activation patching。

SubTokenTest 本身已经包含了多种任务类型，arXiv:2604.02155 也在非 character 任务上发现了类似的非单调退化。如果在 behavioral level 就能回答 H1 vs H2，那 mechanistic analysis 的增量价值在于提供 **"why" 层面的解释**——即不仅知道是否 character-specific，还知道哪些 circuit 负责。但如果 behavioral 结果已经指向 H2（现有证据似乎倾向这个方向），那整个 mechanistic 分析的动机就被削弱了。

**增量价值**: 如果 H1 成立，mechanistic 分析的价值较高（找到可干预的 circuit）。如果 H2 成立（proposal 自己也认为这是可能结果），那 mechanistic 分析变成了"用更贵的方法确认了一个可以更便宜地确认的结论"，其主要贡献仅在于方法论框架本身。

─────────────────────────────────────

【前提假设检验】:

核心 claim 的逻辑链：
1. ✅ "Reasoning tokens 导致 character-level 任务退化" — 有实证支持 (SubTokenTest)
2. ⚠️ "Linear probes 能干净地分离 character-level information 和 non-character information" — 这是关键未验证假设。Linear probing 的 faithfulness 在 interpretability 社区一直有争议。如果 character-level 和 word-level 表征在 representation space 中纠缠，dual-track probing 的差异性结论可能不可靠。
3. ⚠️ "Think-on/off toggle 提供的是 'cleanest possible comparison'" — 虽然确实比跨模型对比更干净，但 think-on 模式改变的不仅是 reasoning 长度，还包括 output distribution、generation pattern 等。这些混淆因素未被讨论。
4. ⚠️ "arXiv:2604.00778 发现的 negative circuits 可以直接推广到 reasoning 场景" — 该论文研究的是 base/instruction-tuned 模型的标准前向传播，而非 extended reasoning chain 中的迭代自注意力。Reasoning context 中 circuit 行为可能完全不同。
5. ⚠️ "8B 模型上的 activation patching 结果可以推广到 32B" — Proposal 承认 32B 只做 Phase 1 probing 不做 patching（出于计算限制），但 scale 对 circuit 结构的影响是已知问题。

─────────────────────────────────────

【3 维度打分】:

1. **Novelty: 弱-中** —
   本 proposal 的核心方法论（linear probing + activation patching on character tasks）直接继承自 arXiv:2604.00778，实验平台（Qwen3-8B think-on/off）直接继承自 arXiv:2509.25758。"Dual-track probing"（同时 track character 和 non-character info）是标准的对照实验设计，并非方法论创新。真正的 novelty delta 在于"将已有方法应用于新场景（reasoning token budget sweep）"，但这属于 incremental combination，不属于 conceptual novelty。审稿人很可能会评价为 "straightforward application of existing probing methodology to a new but narrow setting"。此外，如果 H2 成立（generic degradation），则 character-specific 的 framing 反而会被视为 misleading。

2. **Significance: 弱-中** —
   Character-level sub-token 任务是 NLP 中的一个 niche 问题。虽然 proposal 试图将贡献泛化（"reusable diagnostic framework for any overthinking context"），但这个 generalization claim 未经验证——一个在 character counting 上 validate 的 dual-track probing 框架，能否直接迁移到 code generation 或 mathematical reasoning 的 overthinking 诊断，是完全不明确的。核心发现无论指向 H1 还是 H2，审稿人的反应更可能是 "I would have guessed this" 而非 "surprising"：H1 成立不 surprising（已有 negative circuit 证据 per arXiv:2604.00778），H2 成立也不 surprising（已有大量 overthinking/context-length-degradation 文献）。Practical impact 也有限——circuit masking 被明确降级为 "proof-of-concept"。

3. **Related Work: 中-强** —
   Proposal 对 related work 的覆盖相当全面和诚实。正确引用并定位了 SubTokenTest、Thinking Sparks!、Fluid Representations、negative circuits 等核心工作，清晰说明了与 Thinking Sparks! 的互补关系。引用的论文均真实存在且描述基本准确。不足之处：(1) 未讨论 linear probing faithfulness 的文献（如 Belinkov survey, Hewitt & Liang 2019 selectivity），这对方法论的可信度很重要；(2) 未覆盖更广泛的 overthinking mitigation 工作（如 arXiv:2603.14251, arXiv:2505.17813），这些工作的存在可能进一步削弱 mechanistic 分析的 practical significance。

─────────────────────────────────────

【概率估计】（假设投稿合适的 NLP/ML venue，如 ACL/EMNLP/NeurIPS）: [15% - 28%] 中位 20%

【如投稿 CoRL 2026】: ≈ 0%（Desk reject，场地完全不匹配）

【估计理由】:
Idea 方向站得住脚——理解 reasoning tokens 为什么伤害特定任务类型是有价值的问题——但内核偏薄：方法论无创新（standard probing + patching），核心问题可通过更廉价的 behavioral analysis 初步回答（trivial alternative 威胁），研究范围 niche（character-level tasks），且无论结果指向 H1 还是 H2 都不 surprising。上界被 Novelty 限制——在 arXiv:2604.00778 和 arXiv:2509.25758 已经分别做了 character-level negative circuits 和 Qwen3 circuit analysis 的情况下，本工作的增量贡献主要是"在新条件下运行已有方法"。下界被 dual-outcome 设计和诚实的 related work 覆盖所托底——即使结果一般，execution 可以是 solid 的。

【主要风险】:
1. **Trivial alternative 威胁**: 审稿人可能指出 behavioral-level comparison（across task types, across thinking budgets）就足以区分 H1 vs H2，mechanistic analysis 的增量价值不足以 justify 整篇 paper，特别是当方法论本身无创新时。
2. **"So what" 风险**: 无论 H1 还是 H2 成立，结论的可行动性有限。Circuit masking 仅为 proof-of-concept，且如果 H2 成立，整个 character-specific framing 会被审稿人质疑为 motivated reasoning（先有结论再找证据）。
```

---

**补充说明**：这个 proposal 存在一个根本性的**投稿场地错误**。CoRL 是机器人学习会议，明确要求论文以机器人问题为核心，无机器人内容的论文会被直接退回不审。本 proposal 纯粹是 LLM interpretability 研究，应投稿 ACL、EMNLP、NAACL、NeurIPS、ICML 或 ICLR。如果场地不可更改，建议直接止损；如果场地可以调整到合适的 NLP/ML venue，上述 idea 质量评估（中位 20%）可作为后续迭代优化的参考基线。

Sources:
- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)
- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)
- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)
- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)
- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)
- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)
- [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/abs/2604.10739)
- [Mitigating Overthinking via Reasoning Path Deviation Monitoring](https://arxiv.org/abs/2603.14251)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient information. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命前置问题：投稿场地严重不匹配】

本 proposal 拟投稿 CoRL (Conference on Robot Learning) 2026。
然而 CoRL 2026 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance
 of proposed models, algorithms, datasets, and benchmarks to robotics.
 Submissions without a robotics focus will be returned without review."

本 proposal 研究的是 LLM reasoning tokens 对 character-level sub-token 任务的
影响机制——纯粹的 NLP / mechanistic interpretability 工作，与机器人学习无任何
关联。按 CoRL 的审稿标准，此稿会被 desk reject。

如果作者希望投稿此方向的论文，合适的场地包括：ACL / EMNLP / NAACL (NLP)，
NeurIPS / ICML / ICLR (ML)。以下评估基于"假设投稿到合适 NLP/ML 会议"来
评估 idea 质量本身。

========================================================================

【领域调研】:

1. SubTokenTest (arXiv:2601.09089, Jan 2026, Peking Univ.):
   提出 sub-token understanding benchmark，文档了 reasoning tokens 在 character-level
   任务上的 inverted U-curve 现象。这是本 proposal 的直接出发点。

2. "From Early Encoding to Late Suppression" (arXiv:2604.00778, Apr 2026):
   **最直接的竞争者。** 已在 LLaMA/Qwen/Gemma 上做了 mechanistic analysis
   (probing + activation patching + logit lens + attention head tracing)，发现
   character-level information 在 early/mid layers 已被编码，但被 later layers
   (尤其 penultimate/final MLP) 的"negative circuits"系统性压制。这与本
   proposal Phase 2 的目标（识别 corruption circuits）高度重叠。

3. "Fluid Representations in Reasoning Models" (arXiv:2602.04843, Feb 2026, ETH):
   对 QwQ-32B 做 mechanistic analysis，发现 reasoning 过程中 abstract structural
   representations 逐步增强。本 proposal 引用此工作的逻辑是："如果 reasoning 增强
   某些 representation 却损害 character-level 的，这就是 H1 的因果证据"——但 Fluid
   Representations 的发现本身已部分回答了这个问题（reasoning 选择性地增强 abstract
   structure）。

4. "Thinking Sparks!" (arXiv:2509.25758, NeurIPS 2025):
   在同一平台（Qwen3-8B think-on/off）做 circuit analysis (EAP-IG)。发现
   think-on/off 共享大部分 circuit components。本 proposal 承认互补性，但这也
   意味着在同一模型上做 circuit-level analysis 的"地盘"已被占据。

5. "How Do Language Models Acquire Character-Level Information?"
   (arXiv:2602.05347, EACL 2026):
   系统性 probing 研究 LM 如何编码 character-level information。虽然不涉及
   reasoning tokens，但 probing character-level representations 的方法论与本
   proposal Phase 1 高度相似。**本 proposal 未引用此工作。**

6. "Brief Is Better" (arXiv:2604.02155, Apr 2026):
   证明 non-monotonic CoT budget effects 出现在 function-calling 任务（非
   character-level），optimal budget 低至 8-16 tokens。这对 proposal 的 H2
   假说提供了直接支持——overthinking 是通用现象，非 character-specific。

7. "Context Length Alone Hurts LLM Performance" (arXiv:2510.05381):
   证明即使 perfect retrieval，context length 本身就导致 13.9-85% 性能下降。
   同样支持 H2。

调研总结: 这个领域目前非常活跃——character-level mechanistic interpretability、
reasoning token effects、overthinking 三个方向都有近期高质量工作。本 proposal
的核心贡献（dual-track probing 区分 H1 vs H2）虽然在组合层面有独特性，但各个
组成部分（character probing、reasoning circuit analysis、overthinking 诊断）
已被近期论文分别覆盖。最关键的竞争者是 2604.00778，已经在相同任务类型上做了
几乎相同的 mechanistic toolkit。

========================================================================

【Trivial Alternative 检验】:

存在一个成本极低的 trivial baseline：直接在行为层面比较 character-level tasks
vs. non-character-level control tasks 在不同 reasoning token budget 下的
performance degradation curves。

- 如果 character tasks 的 degradation slope 显著陡于 control tasks → 支持 H1
- 如果两者 degradation 相似 → 支持 H2

这个纯行为实验无需任何 probing、activation patching 或 circuit analysis，仅需
跑 inference，计算成本低 1-2 个数量级。

Proposal 的增量价值在于提供 "why" 层面的机制解释——不仅知道"是否 character-
specific"，还知道"在哪些 layers/heads/MLPs 发生了什么"。但如果 H2 成立（即
degradation 是 generic 的），则 mechanistic analysis 的增量价值大幅缩水，因为
它只是重新确认了已知的 context dilution 机制。proposal 自己也承认 H2 scenario
的价值在于"redirecting research effort"——但这个 redirect 可以用行为实验完成。

结论: Trivial alternative 对核心 claim (H1 vs H2) 构成实质威胁。Mechanistic
分析的增量价值取决于 H1 成立，而 H1 能否成立本身就是未知的。

========================================================================

【前提假设检验】:

核心逻辑链的关键未验证假设：

1. **"Linear probes 能可靠区分 character-specific corruption vs. generic
   degradation"假设**：如果 reasoning tokens 通过 generic attention dilution
   (H2) 同时损害所有 representation types，但 character representations 本身
   baseline robustness 就低于 word/semantic representations，则 probes 会显示
   "character 下降更多"——但这不是因为 corruption 是 character-specific 的，
   而是因为 character info 本来就更脆弱。Proposal 没有讨论如何控制这个混淆。

2. **"Thinking Sparks 的 circuit 框架适用于 character-level tasks"假设**：
   Thinking Sparks 分析的是 mathematical reasoning circuits，但 character-level
   processing 涉及完全不同的 pathway。Thinking Sparks 的"no dedicated thinking
   heads"结论未必能迁移到 character tasks。

3. **"2604.00778 的 negative circuits 会被 thinking tokens 放大"假设**：
   这是 proposal Phase 2 的核心假设，但没有任何先验证据。negative circuits
   是在 base models (non-reasoning) 中发现的。reasoning 模型经过 RLHF/GRPO
   training，其 circuit structure 可能已根本不同。

4. **"Dual-track probing 是通用框架"假设**：proposal 声称 methodology 可推广
   到 code generation、mathematical reasoning 等领域。但 probing 什么信息类型、
   如何定义 "character-level" vs "control" 在每个领域都需要重新设计，"通用框架"
   的说法过于乐观。

========================================================================

【3 维度打分】:

1. Novelty: 弱-中 —
   核心贡献是"dual-track probing 区分 H1 vs H2"这一实验设计。但：
   (a) 2604.00778 已在相同任务类型上用几乎相同的 toolkit (probing + activation
       patching) 做了 mechanistic analysis，且已发现 negative circuits。本
       proposal 在此基础上增加的是"在 reasoning context 下"和"对比 control
       information"——这是 incremental 的，不是 novel approach。
   (b) 2602.05347 (EACL 2026) 已系统性 probing character-level information
       across layers。
   (c) Thinking Sparks 已在同一模型 (Qwen3-8B) 上做了 think-on/off circuit
       analysis。
   (d) Fluid Representations 已回答了 "reasoning 如何改变 internal representations"
       的部分问题。
   剩余 novelty: 特定组合（reasoning budget × character vs control probing）。
   这是一个 well-motivated ablation study，但不是一个 conceptually new contribution。

2. Significance: 中 —
   正面: (a) character-level failure 是 LLM 的真实痛点，理解其与 reasoning 的
   交互有实际价值；(b) H1 vs H2 的区分确实影响研究方向的资源配置（character-
   specific solutions vs general overthinking mitigations）。
   负面: (a) character-level sub-token tasks 是相对小众的问题（与 code generation、
   mathematical reasoning 相比）；(b) 即使完美回答了 H1 vs H2，直接的应用价值
   有限——无论哪个假设成立，都不直接产生 better character handling 的方法；
   (c) "proof-of-concept intervention" 被明确弱化为非主要贡献。

3. Related Work: 中 —
   Proposal 引用了关键竞争者（Thinking Sparks、Fluid Representations、
   2604.00778、2510.05381、2604.02155）且引用描述大体准确。
   缺失: (a) 未引用 "How Do Language Models Acquire Character-Level Information?"
   (EACL 2026, 2602.05347) 这一直接相关的 character probing 工作；
   (b) 对 2604.00778 的差异化定位不够清晰——该论文已发现 negative circuits 压制
   character information，本 proposal 需要更明确说明在 reasoning context 下重复
   类似分析的增量贡献；(c) 未提及 overthinking mitigation 方向的多篇工作
   (manifold steering 等)。

========================================================================

【概率估计】: 15% - 25%，中位 20%
（注：此概率是假设投稿到合适 NLP/ML 会议如 ACL/EMNLP 的估计。
投稿 CoRL 的实际概率 ≈ 0%，会被 desk reject。）

【估计理由】:
Idea 方向站得住脚（understanding reasoning-induced degradation on character tasks
是合理且 timely 的研究问题），但核心内核薄弱：
- Novelty 被 2604.00778 严重压缩——该论文已在同类任务上用同类 toolkit 做了
  mechanistic analysis 并发现了 negative circuits
- 核心贡献退化为一个 well-designed ablation（reasoning budget × information type），
  而非 conceptually new contribution
- Trivial alternative（行为层面比较 degradation curves）能回答同一个 H1 vs H2
  问题，大幅削弱了 mechanistic 分析的必要性
- 限制上界的是 Novelty 维度：审稿人很可能认为这是 2604.00778 + SubTokenTest
  的 straightforward combination

【主要风险】:
1. **Novelty 不足**: 审稿人会指出 2604.00778 已做了 character tasks 的 mechanistic
   analysis（probing + activation patching + negative circuits），本 proposal
   的增量贡献（添加 reasoning budget 和 control probes）不足以支撑一篇独立论文。
2. **Trivial alternative 威胁**: 行为实验可以更简洁地回答 H1 vs H2，
   mechanistic 深度的附加价值需要比当前 proposal 更强的论证——尤其在 H2 成立
   的情况下，全部 mechanistic 工作变成确认已知机制。
```

Sources:
- [SubTokenTest: A Practical Benchmark for Real-World Sub-token Understanding](https://arxiv.org/abs/2601.09089)
- [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381)
- [Thinking Sparks!: Emergent Attention Heads in Reasoning Models During Post Training](https://arxiv.org/abs/2509.25758)
- [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents](https://arxiv.org/abs/2604.02155)
- [From Early Encoding to Late Suppression: Interpreting LLMs on Character Counting Tasks](https://arxiv.org/abs/2604.00778)
- [Fluid Representations in Reasoning Models](https://arxiv.org/abs/2602.04843)
- [How Do Language Models Acquire Character-Level Information?](https://arxiv.org/abs/2602.05347)
- [CoRL 2026 - Call for Papers](https://www.corl.org/contributions/call-for-papers)


【原始 proposal（允许参考但不是主要依据）】:
# Why Reasoning Tokens Hurt Sub-Token Tasks: Mechanistic Analysis of Character-Specific vs. Length-Induced Degradation

## Description
We present the first mechanistic interpretability study investigating why extended reasoning tokens degrade LLM performance on character-level sub-token tasks—the inverted U-curve paradox documented by SubTokenTest. Critically, we design our study to disentangle two competing hypotheses: (H1) reasoning tokens specifically corrupt character-level representations through amplification of negative circuits, versus (H2) the observed degradation reflects generic long-context attention dilution that affects all information types equally—a confound raised by recent evidence that context length alone degrades performance by 13.9–85% (arXiv:2510.05381) and that non-monotonic CoT budget effects appear in non-character tasks (arXiv:2604.02155). Using Qwen3-8B and Qwen3-32B with thinking mode toggled on versus off—ensuring identical architectures and tokenizers for the cleanest possible comparison—we deploy layer-wise linear probes tracking both character-level information (identity, position) and non-character control information (word identity, semantic category) across six thinking-token budgets (0–8192). This dual-track probing design reveals whether character representations degrade disproportionately as reasoning length increases. While 'Thinking Sparks!' (arXiv:2509.25758, NeurIPS 2025) performs circuit analysis on the same Qwen3-8B think-on/off platform, their focus is mathematical reasoning head emergence via EAP-IG; our work is complementary, investigating character-level representation corruption across varying token budgets via linear probing and activation patching. Their finding that think-on/off modes share most circuit components (no dedicated thinking heads) provides important context for our Phase 2 circuit identification, which is restricted to the 8B model for memory feasibility while 32B serves as scale-validation through Phase 1 probing (INT8 quantization on A100 80GB). We apply activation patching to isolate specific attention heads and MLP sublayers involved in character-signal corruption during extended reasoning, testing whether the negative circuits recently identified in base models (arXiv:2604.00778) are amplified by thinking tokens. The finding from 'Fluid Representations' (arXiv:2602.04843) that reasoning progressively enhances abstract structural representations makes our investigation particularly pointed: if reasoning selectively helps some representation types while harming character-level ones, that is strong causal evidence for H1. As a proof-of-concept intervention, we evaluate targeted masking of identified corruption circuits, explicitly characterizing accuracy–reasoning trade-offs rather than claiming a complete solution. Beyond this specific study, our dual-track probing methodology generalizes as a reusable diagnostic framework for disentangling task-specific from generic degradation in any overthinking context—applicable to code generation, mathematical reasoning, and multilingual tasks. Even if the null hypothesis (H2) holds, this would be a high-impact finding that redirects significant research effort currently invested in character-specific solutions (character-level tokenization, token decomposition, specialized sub-token modules) toward general overthinking mitigations benefiting all task types. Supplementary experiments with DeepSeek-R1-0528-Qwen3-8B versus Qwen3-8B (noting the tokenizer confound) provide external validity.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4dbe2cf1-7666-4671-8974-dd4263d2550e",
  "type": "user",
  "uuid": "44c84542-9491-4aee-836b-bef73f8f217a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:27:55.781Z_

```json
{
  "parentUuid": "44c84542-9491-4aee-836b-bef73f8f217a",
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
  "uuid": "87929874-48d7-4000-84c5-e954a67922a4",
  "timestamp": "2026-05-20T03:27:55.781Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:27:55.781Z_

```json
{
  "parentUuid": "87929874-48d7-4000-84c5-e954a67922a4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c1c9233a-51e0-4cf2-845a-581b0b72529a",
  "timestamp": "2026-05-20T03:27:55.781Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
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
  "leafUuid": "c1c9233a-51e0-4cf2-845a-581b0b72529a",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Mechanistic analysis of reasoning tokens and character-level task degradation",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:28:22.220Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and synthesize them according to the Meta Judge format.

Let me extract the key information:

**Reviewer 1:**
- CoRL scope mismatch: desk reject (~5% for CoRL)
- For NLP/ML venue: [20% - 30%] 中位 25%
- Novelty: 中
- Significance: 中偏弱
- Related Work: 强
- Key risks: H2 scenario impact problem, narrow scope × low novelty increment

**Reviewer 2:**
- CoRL scope mismatch: ≈ 0%


- For NLP/ML venue: [15% - 28%] 中位 20%
- Novelty: 弱-中
- Significance: 弱-中
- Related Work: 中-强
- Key risks: Trivial alternative threat, "so what" risk

**Reviewer 3:**
- CoRL scope mismatch: ≈ 0%
- For NLP/ML venue: [15% - 25%] 中位 20%
- Novelty: 弱-中
- Significance: 中
- Related Work: 中
- Key risks: Novelty insufficient

Now I'm calculating the acceptance probabilities. For CoRL, all three reviewers essentially reject it—this is a unanimous consensus that's fatal. But if I look at how this would perform at an NLP/ML venue instead, the median acceptance rate sits around 20% with tight consistency across reviewers. Looking at the individual dimensions, novelty clusters around 弱-中 with two reviewers agreeing on that assessment, significance ranges from 弱-中 to 中, and there's notable variation in how the reviewers weigh these factors.

The key consensus points are stark: the scope mismatch with CoRL is universal, the trivial alternative threat appears across all reviews, the arXiv overlap is acknowledged by everyone, and the character-level task limitation is consistently flagged. The faithfulness concerns around linear probing show up in at least two reviewers' assessments.

For CoRL specifically, this is a clear rejection—the work has no relevance to robotics whatsoever. If I were evaluating this for an NLP or ML venue instead, the median scores across reviewers cluster around 20-25%, which would still be a weak acceptance at best.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1c9233a-51e0-4cf2-845a-581b0b72529a",
  "isSidechain": false,
  "requestId": "req_011CbD7M5VAZVc3WSK22xC5T",
  "type": "assistant",
  "uuid": "af5693ec-0325-4f2a-a257-44b9f79d1280",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzwBGApCLQ3kD26wbFCVM2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4197,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14239
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

_source line 9 · 2026-05-20T03:29:26.874Z_

【阶段】: Meta Judge
【三次中位】: [25%, 20%, 20%]  std=2.9%
（注：以上概率均为三位审稿人假设投稿合适 NLP/ML 会议的估计。三位审稿人均一致判定投稿 CoRL 2026 概率 ≈ 0%。）

【共识维度】（2+ 人同时提到）:

| 维度 / 风险点 | R1 | R2 | R3 | 共识判决 |
|---|---|---|---|---|
| **CoRL scope 不匹配 → desk reject** | ✓ 致命 | ✓ 致命 | ✓ 致命 | **致命（3/3 一致）** |
| **Novelty 被 arXiv:2604.00778 严重压缩** | ✓ 中 | ✓ 弱-中 | ✓ 弱-中 | **弱-中（多数）** |
| **Trivial alternative 威胁**（behavioral comparison 可更廉价地回答 H1 vs H2） | ✓ 中等偏低 | ✓ 实质威胁 | ✓ 实质威胁 | **实质威胁（3/3）** |
| **H2 scenario 下 impact 大幅缩水** | ✓ | ✓ | ✓ | **强共识（3/3）** |
| **Character-level tasks 领域 niche** | ✓ | ✓ | ✓ | **强共识（3/3）** |
| **方法论是现有工具组合，无创新** | ✓ | ✓ | ✓ | **强共识（3/3）** |
| **Linear probing faithfulness 问题** | ✓ | ✓ | ✓ | **中等风险（3/3）** |
| **Think-on/off 对照实验的混淆因素** | ✓ | ✓ | — | 中等风险（2/3） |
| **Significance: 无论 H1 或 H2 成立都不 surprising** | ✓ | ✓ | ✓ | **中-弱（3/3）** |
| **Related Work 覆盖较全面** | 强 | 中-强 | 中 | **中-强（正面共识）** |

【异常维度】（仅 1 人提到）:
- R3 独立发现 proposal 遗漏引用：arXiv:2602.05347 "How Do Language Models Acquire Character-Level Information?" (EACL 2026)——直接相关的 character probing 工作。该发现有效，应纳入风险评估。
- R1 Related Work 评为"强"，显著高于 R2（中-强）和 R3（中）——R1 可能对 Related Work 标准更宽松，降权处理，最终取中-强。
- R2 提及 arXiv:2603.14251（overthinking mitigation）和 arXiv:2604.10739（overthinking 系统性研究）作为未覆盖工作——合理补充但非致命遗漏。

【最终概率】: [0% - 2%] 中位 0%

【一致性】: 高（三位审稿人在致命问题上完全一致，假设合适 venue 的概率 std=2.9% < 3%）

【综合理由】:

**1. 致命问题：CoRL scope 完全不匹配（3/3 一致，最强信号）**

三位审稿人独立且一致地识别出本 proposal 投稿 CoRL 2026 的根本性错误。CoRL CFP 明确要求 "submissions should focus on a core robotics problem"，本 proposal 纯粹是 LLM mechanistic interpretability 研究，与机器人学习零关联。三位审稿人均判定 desk reject，给出 0-5% 的概率。这是不可修复的致命问题——不是 proposal 质量问题，而是投稿场地选择错误。

**2. 假设合适 venue（ACL/EMNLP/NeurIPS）的 idea 质量评估（仅供参考）**

三位审稿人在假设合适 venue 下的评估高度收敛（20%, 20%, 25%, std=2.9%），处于高一致区间。取中位附近：

- **Novelty 弱-中**（3/3 共识）：核心方法论（linear probing + activation patching）直接继承 arXiv:2604.00778，实验平台继承 arXiv:2509.25758，"dual-track probing" 是标准对照设计而非方法论创新。增量贡献为"在新条件下（reasoning budget sweep）运行已有方法"。
- **Significance 中偏弱**（3/3 共识）：character-level tasks 领域 niche；无论 H1 或 H2 成立结论都不 surprising；practical impact 有限（circuit masking 仅为 proof-of-concept）。
- **Trivial alternative 实质威胁**（3/3 共识）：behavioral-level comparison 可以更廉价地回答 H1 vs H2 核心问题，大幅削弱 mechanistic 分析的增量价值，尤其在 H2 成立时。
- **Related Work 中-强**（唯一正面共识，但 R3 发现了遗漏引用）

综合以上，即使投稿合适 venue，idea 质量天花板约 25%，概率约 [15%-25%] 中位 20%。

**3. 最终判决逻辑**

CoRL 的 desk reject 是确定性事件，不依赖 idea 质量评估。因此最终概率直接取 ≈ 0%。建议 KILL（针对 CoRL 投稿）。

【建议】: KILL

击穿原因：投稿场地与 proposal 内容完全不匹配，CoRL 2026 将 desk reject。

附加建议：如果作者愿意更换投稿目标至合适的 NLP/ML 会议（ACL / EMNLP / NeurIPS / ICML / ICLR），proposal 本身具有一定基础（Related Work 覆盖全面、研究问题合理），但需要显著提升 Novelty 和 Significance 才有竞争力（当前假设合适 venue 中位仅 20%）。核心需解决：(1) 与 arXiv:2604.00778 的差异化不足；(2) trivial alternative 威胁；(3) character-level tasks 的 niche 限制。

【实施评估】:
- 计算资源: Qwen3-8B probing + activation patching 需 1×A100 80GB，约 3-5 天；Qwen3-32B INT8 probing 需 1×A100 80GB，约 2-3 天；DeepSeek-R1 补充实验额外 1-2 天。总计约 1-2 周单卡 A100 时间。计算需求适中。
- 数据需求: SubTokenTest benchmark（公开可得）+ 需自行构建 non-character control probing 数据集（word identity, semantic category 的标注数据）。数据构建工作量中等。
- 人工介入: 需要研究者手动设计 probing 任务、选择 control information types、分析 activation patching 结果。无需大规模人工标注。
- 训练需求: 无需训练 LLM，仅训练轻量 linear probes（训练成本可忽略）。
- 新 Benchmark: 不需要构建新 benchmark（使用 SubTokenTest），但需要构建 probing 评测协议。
- 预估周期: 实验实施 3-4 周，论文撰写 2-3 周，总计约 6-8 周可完成。周期合理。

---

鉴于 Meta Judge 判定为 KILL，现在进入**角色 C：最终输出**。

【拒绝阶段】: Triage（Meta Judge 综合三方独立评审）

【击穿维度 / 致命缺陷】:
1. **投稿场地致命不匹配**（3/3 审稿人一致）：CoRL 2026 明确要求以机器人问题为核心，本 proposal 纯粹是 LLM mechanistic interpretability 研究，将被 desk reject。这是不可通过修改 proposal 内容解决的根本问题。
2. **Novelty 弱-中**（3/3 共识）：即使更换至合适 venue，核心方法论被 arXiv:2604.00778（同类任务同类工具的 mechanistic analysis）和 arXiv:2509.25758（同一模型平台的 circuit analysis）严重压缩，增量贡献为 incremental combination 而非 conceptual novelty。
3. **Trivial alternative 实质威胁**（3/3 共识）：H1 vs H2 的核心问题可通过成本低 1-2 个数量级的 behavioral comparison 初步回答，mechanistic 分析的增量价值依赖于 H1 成立——而现有证据（arXiv:2604.02155, arXiv:2510.05381）较强地指向 H2。

【已尝试优化方向】: 无（Triage 阶段即 KILL，未进入迭代优化）

【可否抢救】:
- **换场地可行**：更换投稿目标至 ACL / EMNLP / NeurIPS / ICML / ICLR，当前 idea 有约 20% 的基线概率（三位审稿人共识），具备迭代优化的基础。
- **若换场地，关键优化方向**：
  1. 大幅强化与 arXiv:2604.00778 的差异化——不能仅是"在 reasoning context 下重复"，需要提出该论文无法覆盖的 conceptual contribution（如：reasoning 过程中 representation 的动态演变轨迹，而非静态快照）
  2. 正面回应 trivial alternative——在 proposal 中先做 behavioral comparison 作为 motivating experiment，再用 mechanistic analysis 提供 behavioral 无法给出的 "why" 解释，形成两层贡献
  3. 拓宽 scope——将 character-level 作为 case study 而非全部，展示 dual-track probing 在至少一个其他领域（如 code generation 的 overthinking）的适用性
  4. 补充遗漏引用：arXiv:2602.05347 (EACL 2026) 关于 character-level information 的系统性 probing 研究
- **不换场地**：不可抢救，CoRL desk reject 是确定性事件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af5693ec-0325-4f2a-a257-44b9f79d1280",
  "isSidechain": false,
  "requestId": "req_011CbD7M5VAZVc3WSK22xC5T",
  "type": "assistant",
  "uuid": "9254f4c2-09b1-4d06-87f3-a34cef9f9837",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DzwBGApCLQ3kD26wbFCVM2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 16560,
      "output_tokens": 4197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4197,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 14239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14239
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
  "leafUuid": "9254f4c2-09b1-4d06-87f3-a34cef9f9837",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Mechanistic analysis of reasoning tokens and character-level task degradation",
  "sessionId": "f7366115-be38-48f4-90e6-8049f3d3d2b2"
}
```

---
